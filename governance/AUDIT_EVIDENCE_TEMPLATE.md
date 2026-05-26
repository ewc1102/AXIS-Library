# Audit Evidence Template

## Scope

- Registry root:
- Trust policy:
- Revocation feeds:
- Time window:
- Auditor:

## Commands

```sh
python axis_registry.py --registry registry status
python axis_registry.py --registry registry verify-log
python axis_registry.py --registry registry export-bundle audit-bundle.json
```

For sampled entries:

```sh
python axis_registry.py --registry registry verify <entry-id> --trust-policy trust/trust.json
python axis_registry.py --registry registry materialize <entry-id> audit/<entry-id>.ax
```

## Evidence

- Status output:
- Transparency log output:
- Bundle hash:
- Sampled entry IDs:
- Signature verification results:
- Revocation verification results:
- Backup restore drill result:

## Findings

- Critical:
- High:
- Medium:
- Low:

## Sign-Off

- Auditor:
- Date:
- Notes:
