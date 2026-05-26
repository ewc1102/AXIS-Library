## Summary

- What is being added or changed?
- Publisher ID:
- Entry IDs affected:

## Submission Type

- [ ] New publisher application
- [ ] New registry entry
- [ ] Registry entry update
- [ ] Revocation feed
- [ ] Governance/documentation change

## Verification

- [ ] `python scripts/verify_registry.py --axis ../axis` passes locally.
- [ ] Every commit has a DCO `Signed-off-by:` line.
- [ ] I have the right to contribute this code/content.
- [ ] I am contributing this to the commons under Apache-2.0.
- [ ] I disclosed material AI assistance, if any.
- [ ] I reviewed any AI-generated code before submission.
- [ ] No private, proprietary, trade-secret, or incompatible third-party code is included.
- [ ] For new `.ax` entries: `python ../axis/axis.py validate <file>` passes (schema + typecheck + effects).
- [ ] For new `.ax` entries: declared preconditions, postconditions, and effects accurately reflect the function's behavior.
- [ ] For new `.ax` entries: `python ../axis/axis.py test <file> <fn>` passes (property tests, when applicable).
- [ ] New entries are content-addressed.
- [ ] New entries are signed by a trusted publisher or are explicitly pending.
- [ ] Revocation feeds are signed and referenced by trust policy.
- [ ] Review evidence is attached for claimed quality level.

## Notes
