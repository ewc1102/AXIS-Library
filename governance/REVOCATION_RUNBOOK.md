# Revocation Runbook

## Trigger

- Affected entry IDs:
- Reporter:
- Reason: incorrect / insecure / superseded / publisher_compromised / policy_violation
- Severity:

## Steps

1. Verify the affected object IDs and reproduce the issue when possible.
2. Create a signed revocation feed:

   ```sh
   python axis_registry.py --registry registry revoke feed-YYYY-MM-DD revocations/feed-YYYY-MM-DD.json <id> --publisher <publisher> --private-key publisher-private.json
   ```

3. Publish the revocation feed beside the trust policy.
4. Update consumers to require the new feed.
5. If publisher key compromise is suspected, remove or rotate the publisher key.
6. Publish replacement entries under new content IDs when available.

## Closure

- Feed path:
- Signature verified by:
- Trust policy updated by:
- Replacement IDs:
- Closure date:
