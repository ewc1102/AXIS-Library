# The AXIS Commons

AXIS-Library is a commons of verified code.

Contributors put work into the commons because shared verified components make
everyone's work easier — agents stop regenerating common functions, humans stop
auditing the same code repeatedly, downstream projects compose trusted pieces
instead of rebuilding them.

## How the commons works

- **Contributions are gifts, not transactions.** You add a function because
  others will benefit. You retain no special rights over it after publication.
- **Anyone can use, anyone can fork, anyone can build on it.** Apache-2.0
  guarantees that. The license also protects the commons from patent claims —
  including claims by past contributors.
- **Identity is the hash, not the author.** Once a function passes verification
  and is published under `fn:<hash>`, that exact byte sequence belongs to the
  commons forever. Authors aren't tracked as owners; they're tracked as
  contributors for credit and accountability, not control.
- **Quality is non-negotiable.** Verification is what makes the commons
  valuable. A library full of unverified code is just another package manager.
  Every entry passes the full AXIS pipeline (typecheck, effect check,
  contracts, property tests) before it's accepted.

## What contributors gain

- Credit in the registry record (you wrote `fn:<hash>`).
- Recognition as a trusted publisher if you submit consistent quality over
  time.
- A permanent, immutable record that your contribution exists and works.
- The same benefit every consumer gets: reuse of verified components instead
  of regenerating them.

## What contributors give up

- Control over downstream use. Once published, you can't restrict who uses it
  or how.
- The right to retroactively assert ownership claims. Apache-2.0 is one-way.
- Silent edits. Bugs are fixed by publishing a new entry under a new hash
  and revoking the old one via signed revocation feed — not by mutating
  existing entries.

## What consumers gain

- Frictionless use. No agreement to sign, no account to create, no API key.
  Just clone or import.
- Cryptographic verification. Every entry's hash recomputes, every trusted
  publisher's signature verifies, every revocation feed is checked.
- Composability. Verified components compose into verified programs.

## What this commons is not

- Not a marketplace. Nothing is sold. No transactions.
- Not a popularity contest. Hash-based discovery, not stars or downloads.
- Not a gatekeeping system. The verification bar is high, but the door is
  open to anyone who can meet it.
- Not a place for proprietary or restricted code. If you can't publish under
  Apache-2.0, this isn't the venue.

## The expected outcome

A commons that compounds. Every verified function added is a permanent
reduction in future work across the entire ecosystem of AXIS users —
human, agent, and otherwise. The library starts empty, fills slowly, and
eventually carries enough verified weight that building on top of it is
faster and safer than building from scratch.
