# Accepted Seed Entries: 2026-05-26

Initial signed entries published by trusted publisher `ewc1102`.

## Entries

| Entry ID | Kind | Name | Quality |
|---|---|---|---|
| `mod:5eeeedea7123c1c02cfed9650856e635` | module | factorial module | `property_tested` |
| `fn:9492475d580480addc55905a6d974645` | function | factorial | `property_tested` |
| `mod:9f0b1e6bccfda851aaeb41bc88daeb4e` | module | gcd module | `property_tested` |
| `fn:f3f21e55f891b36768e0622e28be1d57` | function | gcd | `property_tested` |

## Source

- `../axis/examples/factorial.ax`
- `../axis/examples/gcd.ax`

## Commands

```powershell
python ..\axis\axis_registry.py --registry registry index ..\axis\examples\factorial.ax --proptest 25
python ..\axis\axis_registry.py --registry registry index ..\axis\examples\gcd.ax --proptest 25

python ..\axis\axis_registry.py --registry registry sign-rsa mod:5eeeedea7123c1c02cfed9650856e635 --publisher ewc1102 --private-key <private-key-outside-repo>
python ..\axis\axis_registry.py --registry registry sign-rsa fn:9492475d580480addc55905a6d974645 --publisher ewc1102 --private-key <private-key-outside-repo>
python ..\axis\axis_registry.py --registry registry sign-rsa mod:9f0b1e6bccfda851aaeb41bc88daeb4e --publisher ewc1102 --private-key <private-key-outside-repo>
python ..\axis\axis_registry.py --registry registry sign-rsa fn:f3f21e55f891b36768e0622e28be1d57 --publisher ewc1102 --private-key <private-key-outside-repo>
```

## Verification

```powershell
python scripts\verify_registry.py --axis ..\axis
python ..\axis\axis_registry.py --registry registry status
```

Status after publication:

- entries: 4
- functions: 2
- modules: 2
- quality: all `property_tested`
- transparency log events: 8

Each entry verifies with `trust/trust.json` and has an RSA-SHA256 signature from
trusted publisher `ewc1102`.
