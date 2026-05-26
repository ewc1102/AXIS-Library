#!/usr/bin/env python3
"""Reject destructive edits to published AXIS-Library state."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


IMMUTABLE_PREFIXES = (
    "registry/objects/",
    "governance/accepted/",
    "trust/publishers/",
    "revocations/",
)

QUALITY_ORDER = {
    "static_checked": 0,
    "property_tested": 1,
    "reviewed": 2,
    "audited": 3,
}


def run_git(args: list[str], *, text: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=text,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout


def normalize_path(path: str) -> str:
    return path.replace("\\", "/")


def is_immutable_path(path: str) -> bool:
    clean = normalize_path(path)
    return any(clean.startswith(prefix) for prefix in IMMUTABLE_PREFIXES)


def file_at_ref(ref: str, path: str) -> dict[str, Any] | None:
    result = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode != 0:
        return None
    return json.loads(result.stdout)


def diff_name_status(base_ref: str, head_ref: str) -> list[tuple[str, list[str]]]:
    raw = run_git(["diff", "--name-status", "--find-renames", f"{base_ref}...{head_ref}"])
    rows: list[tuple[str, list[str]]] = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        rows.append((parts[0], parts[1:]))
    return rows


def check_immutable_paths(base_ref: str, head_ref: str) -> list[str]:
    errors: list[str] = []
    for status, paths in diff_name_status(base_ref, head_ref):
        touched = [path for path in paths if is_immutable_path(path)]
        if not touched:
            continue

        if status == "A":
            continue

        joined = ", ".join(touched)
        errors.append(
            f"{status} is not allowed for immutable published path(s): {joined}. "
            "Publish replacements as new content-addressed objects and use revocation feeds."
        )
    return errors


def entries_by_id(registry: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    if not registry:
        return {}
    entries = registry.get("entries", [])
    if not isinstance(entries, list):
        return {}
    return {
        entry["id"]: entry
        for entry in entries
        if isinstance(entry, dict) and isinstance(entry.get("id"), str)
    }


def check_registry_json(base_ref: str, head_ref: str) -> list[str]:
    base = file_at_ref(base_ref, "registry/registry.json")
    head = file_at_ref(head_ref, "registry/registry.json")
    if base is None or head is None:
        return []

    errors: list[str] = []
    base_entries = entries_by_id(base)
    head_entries = entries_by_id(head)

    for entry_id, base_entry in sorted(base_entries.items()):
        head_entry = head_entries.get(entry_id)
        if head_entry is None:
            errors.append(f"registry/registry.json removed published entry {entry_id}.")
        elif head_entry != base_entry:
            errors.append(f"registry/registry.json modified published entry {entry_id}.")

    return errors


def check_trust_policy(base_ref: str, head_ref: str) -> list[str]:
    base = file_at_ref(base_ref, "trust/trust.json")
    head = file_at_ref(head_ref, "trust/trust.json")
    if base is None or head is None:
        return []

    errors: list[str] = []
    if base.get("require_signature") is True and head.get("require_signature") is not True:
        errors.append("trust/trust.json cannot disable require_signature.")

    base_min = base.get("min_quality")
    head_min = head.get("min_quality")
    if (
        isinstance(base_min, str)
        and isinstance(head_min, str)
        and QUALITY_ORDER.get(head_min, -1) < QUALITY_ORDER.get(base_min, -1)
    ):
        errors.append(
            f"trust/trust.json cannot lower min_quality from {base_min} to {head_min}."
        )

    base_publishers = base.get("trusted_publishers", {})
    head_publishers = head.get("trusted_publishers", {})
    if isinstance(base_publishers, dict) and isinstance(head_publishers, dict):
        for publisher, base_record in sorted(base_publishers.items()):
            head_record = head_publishers.get(publisher)
            if head_record is None:
                errors.append(f"trust/trust.json removed trusted publisher {publisher}.")
            elif head_record != base_record:
                errors.append(f"trust/trust.json modified trusted publisher {publisher}.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check append-only invariants for published AXIS-Library state."
    )
    parser.add_argument("--base-ref", required=True)
    parser.add_argument("--head-ref", default="HEAD")
    args = parser.parse_args()

    repo_root = Path(run_git(["rev-parse", "--show-toplevel"]).strip())
    if Path.cwd() != repo_root:
        # Keep git path handling predictable for local and CI use.
        import os

        os.chdir(repo_root)

    errors = []
    errors.extend(check_immutable_paths(args.base_ref, args.head_ref))
    errors.extend(check_registry_json(args.base_ref, args.head_ref))
    errors.extend(check_trust_policy(args.base_ref, args.head_ref))

    if errors:
        print("AXIS-Library append-only check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("AXIS-Library append-only check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
