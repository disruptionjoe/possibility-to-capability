# Frozen-Packet Schemas

This directory owns the receiving repository's machine-readable contract for a
source-issued frozen packet. It does not authorize this repository to construct
a source packet on another repository's behalf.

## Versions and files

- `frozen-packet-v0.1.schema.json` - original interoperable contract; preserved
  unchanged for existing v0.1 packets.
- `frozen-packet-v0.2.schema.json` - source-issued packet contract with a
  reproducible manifest and explicit method-premise dependency structure.
- `receiving-independence-assessment-v0.2.schema.json` - separate receiver-owned
  classification that cannot strengthen or rewrite the source statement.
- `frozen-packet-v0.2.md` - normative v0.2 canonicalization, compatibility,
  migration, nonclaim, and falsifier specification.
- `../../tests/fixtures/` - synthetic positive bundle and assessment fixtures.
- `../../tests/validate_frozen_packet_contract.py` - v0.1 checks.
- `../../tests/validate_frozen_packet_v0_2_contract.py` - v0.2 semantic,
  integrity, compatibility, and adversarial checks.

## Acceptance boundary

An accepted packet must be source-issued, revision-pinned, hash-bearing,
explicit about construction forks and nonclaims, and frozen. Import does not
transfer authority or upgrade source claim status.

Receiver-owned annotations live beside an imported packet. They never modify
the source-issued object. In v0.2, typed independence assessment may preserve
the source type or weaken it to `unknown_or_contested`; it cannot choose a
different or stronger type.

`NOT_YET_IMPORTABLE` is an intake receipt, not a degraded packet. It belongs
under `packets/intake/` and must state which source-owned fields are missing.

## Validation

From the repository root:

```text
python tests/validate_frozen_packet_contract.py
python tests/validate_frozen_packet_v0_2_contract.py
```
