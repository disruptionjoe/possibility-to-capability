# Frozen-Packet Schema v0.1

This directory owns the receiving repository's machine-readable contract for a
source-issued frozen packet. It does not authorize this repository to construct
a source packet on another repository's behalf.

## Files

- `frozen-packet-v0.1.schema.json` - interoperable JSON Schema contract.
- `../../tests/fixtures/frozen-packet-valid.json` - synthetic positive fixture.
- `../../tests/validate_frozen_packet_contract.py` - dependency-light semantic
  validator and adversarial controls.

## Acceptance boundary

An accepted packet must be source-issued, revision-pinned, hash-bearing,
explicit about construction forks and nonclaims, and frozen. Import does not
transfer authority or upgrade source claim status.

`NOT_YET_IMPORTABLE` is an intake receipt, not a degraded packet. It belongs
under `packets/intake/` and must state which source-owned fields are missing.

## Validation

From the repository root:

```text
python tests/validate_frozen_packet_contract.py
```
