# Revocation Feeds

Signed revocation feeds live here.

Revocation is how AXIS handles bad immutable content-addressed IDs. Existing
objects are not rewritten in place; instead, affected IDs are listed in a signed
feed and replacement code is published under new IDs.

Use `governance/REVOCATION_RUNBOOK.md` for the operating process.
