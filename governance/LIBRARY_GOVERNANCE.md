# AXIS-Library Governance

AXIS-Library is the public commons of verified AXIS code (see `COMMONS.md`).
Submissions are reviewed before merge, but the trust model is cryptographic
and content-addressed — review is about quality, not about gatekeeping who
gets to contribute.

## Publisher Admission

- Every publisher has a stable ID and an RSA public key in `trust/trust.json`.
- Development HMAC signatures are not accepted for public entries.
- Publishers must provide a contact channel and agree to revocation handling.
- Publishers must accept `PUBLISHER_AGREEMENT.md` before their signatures are
  trusted by the public library.
- New publishers start at `static_checked` until reviewed. This is a quality
  signal for consumers, not a permission gate — `static_checked` entries are
  fully usable and content-addressed; higher quality tiers (`property_tested`,
  `reviewed`, `audited`) require evidence per the entry review checklist.

## Entry Requirements

- Every accepted entry must be content-addressed and pass `verify`.
- Public entries should include `intent`, parameter types, return type, and
  effect declarations.
- `property_tested`, `reviewed`, and `audited` quality labels require evidence.
- Generated concrete generic instantiations may inherit trust only through a
  signed `gfn:` template and a trusted monomorphizer version.

## Review Flow

1. Publisher opens a PR with submission material under `submissions/pending/`.
2. CI verifies registry structure, submissions, trust policy, and revocations.
3. CI verifies every commit has a DCO sign-off.
4. Reviewer checks intent, effects, contracts, and evidence.
5. Maintainer indexes accepted entries into `registry/`.
6. Merge publishes the updated read-only library state.

## Revocation

- Revocations are signed feeds, not silent deletes.
- Reasons should be one of: `incorrect`, `insecure`, `superseded`,
  `publisher_compromised`, or `policy_violation`.
- Public registries must publish the latest revocation feed alongside trust
  policy updates.
- Consumers should fail closed when a required revocation feed cannot be
  verified.
