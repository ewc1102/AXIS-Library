# Contributing To AXIS-Library

AXIS-Library accepts contributions through GitHub pull requests. Contributions
include AXIS modules, registry objects, trust policy changes, revocation feeds,
governance changes, CI changes, and documentation.

## License

AXIS-Library is licensed under Apache-2.0. By contributing, you agree that your
contribution is licensed under the same license as the repository unless a file
explicitly says otherwise.

## Who Can Agree

AI agents cannot accept legal terms on their own. The human or organization
operating the agent is responsible for the contribution, the license grant, and
the review of any generated code.

If you do not agree to these contribution terms, do not submit a pull request
and do not ask an agent to submit one for you. Public read-only consumption of
this repository is governed by `LICENSE`.

## Developer Certificate Of Origin

Every commit must include a DCO sign-off:

```text
Signed-off-by: Name <email@example.com>
```

Use:

```sh
git commit -s
```

The sign-off certifies:

```text
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.

Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

## AI-Generated Contributions

AI-generated contributions are allowed only when the human/operator submitting
the PR reviews them and takes responsibility for them.

Pull requests must disclose AI assistance when material code, registry entries,
or governance text was generated or transformed by an AI system.

The submitter certifies that:

- they had the right to provide all prompts, context, and source material used;
- no private, proprietary, or license-incompatible code was intentionally copied;
- generated code was reviewed before submission;
- the contribution can be distributed under Apache-2.0.

## Trusted Publisher Contributions

Being a normal contributor is not the same as being a trusted publisher.

Trusted publishers must complete `governance/PUBLISHER_AGREEMENT.md` and be
added to `trust/trust.json` by maintainers. Trusted entries must be signed with
the accepted publisher key and remain subject to revocation.

## Pull Request Requirements

- Run `python scripts/verify_registry.py --axis ../axis` locally when possible.
- Keep pending submissions under `submissions/pending/<publisher>/`.
- Use `governance/ENTRY_REVIEW_CHECKLIST.md` for entry review evidence.
- Use `governance/REVOCATION_RUNBOOK.md` for revocation feeds.
- Do not commit private keys, bearer tokens, prompts containing secrets, or
  proprietary source material.
