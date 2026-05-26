# Repository Protection

AXIS-Library is intended to be append-mostly. The files in this repository
provide CI-level guardrails, but GitHub branch protection must also be enabled
on `main` so nobody can bypass those guardrails with a direct destructive push.

## Required GitHub Settings

Enable a branch protection rule or ruleset for `main` with:

- Require a pull request before merging.
- Require approvals.
- Require review from Code Owners.
- Dismiss stale approvals when new commits are pushed.
- Require status checks to pass before merging:
  - `Verify AXIS-Library / verify`
  - `DCO`
- Require branches to be up to date before merging.
- Block force pushes.
- Block branch deletion.
- Restrict who can push to `main`; ideally only maintainers.
- Do not allow bypassing the rule except for emergency recovery by the owner.

## Append-Only Policy

The CI check `scripts/check_append_only.py` rejects pull requests that:

- modify or delete published files under `registry/objects/`;
- modify or delete accepted governance records under `governance/accepted/`;
- modify or delete publisher records under `trust/publishers/`;
- modify or delete revocation feeds under `revocations/`;
- remove or edit existing entries in `registry/registry.json`;
- disable required signatures, lower `min_quality`, or remove/modify existing
  trusted publishers in `trust/trust.json`.

Legitimate corrections are published as new records. Unsafe or superseded code
is handled through signed revocation feeds rather than history deletion.
