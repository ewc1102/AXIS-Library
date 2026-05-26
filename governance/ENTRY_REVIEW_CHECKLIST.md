# Entry Review Checklist

## Entry

- Entry ID:
- Kind: function / generic_function / module
- Publisher:
- Claimed quality:
- Source registry:

## Mechanical Verification

- [ ] `axis_registry.py verify <id> --trust-policy trust/trust.json` accepts.
- [ ] Content hash recomputes locally.
- [ ] Signature verifies against trusted publisher key.
- [ ] Revocation feeds verify and do not include the entry ID.
- [ ] Transparency log verifies.

## Semantic Review

- [ ] Intent is clear and specific.
- [ ] Parameter and return types match intent.
- [ ] Effects are minimal and declared.
- [ ] Preconditions/postconditions cover obvious failure modes.
- [ ] Property-test evidence is present when claiming `property_tested`.
- [ ] Human review evidence is present when claiming `reviewed`.
- [ ] Audit evidence is present when claiming `audited`.

## Decision

- Status: accept / reject / needs changes
- Reviewer:
- Date:
- Notes:
