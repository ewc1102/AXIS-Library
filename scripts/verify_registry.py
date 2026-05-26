"""Verify the AXIS-Library repository structure and registry contents."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys


REQUIRED_DIRS = [
    "registry",
    "registry/objects/fn",
    "registry/objects/gfn",
    "registry/objects/mod",
    "trust",
    "trust/publishers",
    "revocations",
    "governance",
    "submissions/pending",
]


def run(cmd, cwd):
    result = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)
    return result.stdout


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON: {path}: {exc}") from exc


def find_axis_dir(library_root, explicit):
    candidates = []
    if explicit:
        candidates.append(Path(explicit))
    candidates.extend([library_root.parent / "axis", library_root / "axis"])
    for candidate in candidates:
        if (candidate / "axis_registry.py").exists() and (candidate / "axis.py").exists():
            return candidate.resolve()
    raise SystemExit("Could not find AXIS checkout. Pass --axis or set AXIS_TOOL_DIR.")


def verify_required_dirs(library_root):
    missing = [path for path in REQUIRED_DIRS if not (library_root / path).is_dir()]
    if missing:
        raise SystemExit(f"Missing required directories: {', '.join(missing)}")


def verify_json_files(library_root):
    for path in library_root.rglob("*.json"):
        if ".git" not in path.parts:
            load_json(path)


def verify_registry(library_root, axis_dir, trust_policy):
    registry_py = axis_dir / "axis_registry.py"
    registry_root = library_root / "registry"
    status_raw = run(
        [sys.executable, str(registry_py), "--registry", str(registry_root), "status"],
        cwd=axis_dir,
    )
    status = json.loads(status_raw)
    if not status.get("ok"):
        raise SystemExit(f"Registry status failed: {json.dumps(status, sort_keys=True)}")

    run([sys.executable, str(registry_py), "--registry", str(registry_root), "verify-log"], cwd=axis_dir)

    manifest = load_json(registry_root / "registry.json")
    for entry in manifest.get("entries", []):
        cmd = [sys.executable, str(registry_py), "--registry", str(registry_root), "verify", entry["id"]]
        if trust_policy.exists():
            cmd.extend(["--trust-policy", str(trust_policy)])
        raw = run(cmd, cwd=axis_dir)
        result = json.loads(raw)
        if not result.get("ok"):
            raise SystemExit(f"Entry verification failed for {entry['id']}: {raw}")


def verify_pending_submissions(library_root, axis_dir):
    axis_py = axis_dir / "axis.py"
    for module_path in sorted((library_root / "submissions" / "pending").rglob("*.ax")):
        run([sys.executable, str(axis_py), "validate", str(module_path)], cwd=axis_dir)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Verify AXIS-Library")
    parser.add_argument("--library", default=".")
    parser.add_argument("--axis", default=None)
    parser.add_argument("--trust-policy", default="trust/trust.json")
    args = parser.parse_args(argv)

    library_root = Path(args.library).resolve()
    axis_dir = find_axis_dir(library_root, args.axis)
    trust_policy = library_root / args.trust_policy

    verify_required_dirs(library_root)
    verify_json_files(library_root)
    verify_registry(library_root, axis_dir, trust_policy)
    verify_pending_submissions(library_root, axis_dir)
    print("AXIS-Library verification passed")


if __name__ == "__main__":
    main()
