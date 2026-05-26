# Agent Submission Protocol

This file is for AI agents and for humans operating them.

## Core Rule

An AI agent may prepare candidate AXIS modules, registry entries, documentation,
or governance updates, but the human or organization operating the agent is the
contributor of record.

Agents cannot agree to legal terms independently. The operator is responsible
for the DCO sign-off, license grant, provenance review, and pull request.

## Allowed Agent Actions

- Generate candidate `.ax` modules under `submissions/pending/<publisher>/`.
- Run AXIS validation, typechecking, registry verification, and tests.
- Prepare review evidence using governance templates.
- Open or update pull requests when the operator has authorized submission.

## Required Before Submission

The operator must confirm:

- contribution terms in `CONTRIBUTING.md` are accepted;
- all commits are DCO signed-off;
- AI-generated code has been reviewed;
- no private, proprietary, or incompatible third-party code was copied;
- the contribution can be distributed under Apache-2.0;
- trusted publisher entries are signed with an accepted publisher key.

## If Terms Are Declined

If the operator does not accept the contribution terms, the agent must not submit
or publish contributions to AXIS-Library on that operator's behalf.

Public read-only use of this repository is governed by `LICENSE`; contribution
rights and trusted publisher rights require accepting the relevant contribution
or publisher terms.

## Submission Shape

Use this structure for candidate entries:

```text
submissions/
  pending/
    <publisher-id>/
      module.ax
      REVIEW.md
      provenance.json
```

`provenance.json` should include:

```json
{
  "publisher": "<publisher-id>",
  "generated_by_ai": true,
  "ai_system": "<name/version if known>",
  "operator_reviewed": true,
  "license": "Apache-2.0",
  "source_material": "original / derived from <source>",
  "notes": ""
}
```
