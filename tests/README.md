# Tests

This directory is reserved for deterministic checks and adversarial fixtures
owned by this repository. Source-repo test suites remain in their source repos.

## Frozen-packet contract

- `validate_frozen_packet_contract.py` protects the unchanged v0.1 contract.
- `validate_frozen_packet_v0_2_contract.py` verifies v0.1 coexistence, the v0.2
  positive bundle and receiving assessment, and adversarial cases covering
  path normalization, raw-byte integrity, all digest layers, artifact coverage,
  premise-map symmetry, shared premises, dependency edges, false unanimity,
  method-count inflation, source-wording drift, status upgrades, and unknown or
  contested receiving classifications.
- `fixtures/bundle-v0.2/` contains controlled raw bytes. `.gitattributes`
  disables text conversion for those files so the fixture digest is portable.

Run both contracts from the repository root:

```text
python tests/validate_frozen_packet_contract.py
python tests/validate_frozen_packet_v0_2_contract.py
```
