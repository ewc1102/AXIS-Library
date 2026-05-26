# AXIS-Library Submission Protocol

This protocol explains how candidate code moves from an agent or human into the
public library.

## Roles

- **Consumer:** reads or imports public registry content under `LICENSE`.
- **Contributor:** submits pull requests under `CONTRIBUTING.md` and DCO.
- **Trusted publisher:** signs entries accepted by `trust/trust.json`.
- **Maintainer:** reviews submissions, trust changes, and revocations.
- **Agent:** assists a human/operator but is not the legal contributor.

## Consumer Access

AXIS-Library is public and Apache-2.0 licensed. Consumers may read, clone, fork,
and import public registry content under `LICENSE`.

Declining contribution terms prevents contribution or trusted publishing; it
does not revoke the public Apache-2.0 license for read-only consumption.

## Contribution Path

1. Contributor creates a branch.
2. Candidate `.ax` modules go under `submissions/pending/<publisher>/`.
3. Contributor includes provenance and review evidence.
4. Contributor signs off every commit with DCO.
5. CI runs registry verification and DCO checks.
6. Maintainer reviews and either requests changes or accepts.

## Trusted Entry Publication Path

1. Publisher agreement is accepted.
2. Publisher key is added to `trust/trust.json`.
3. Candidate module is indexed with AXIS registry tooling.
4. Entry is signed by the publisher key.
5. Revocation feeds and transparency log verify.
6. Entry is merged into `registry/`.

## Rejection

Maintainers may reject submissions for unclear rights, missing sign-off,
license incompatibility, missing provenance, failed verification, weak evidence,
security concerns, or marketplace policy concerns.
