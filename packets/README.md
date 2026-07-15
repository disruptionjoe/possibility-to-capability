# Frozen Packets

This directory is reserved for immutable packet manifests, provenance receipts,
and locally owned analyses of frozen imports.

A packet must name its source repository, exact source references or commit,
construction used, evidence grade, open fields, and source-repo verdict. Import
never transfers ownership and never authorizes edits to the source repository.

## First deliverable after activation

1. Co-develop Frozen-Packet Schema v0.1 against the founding GU case.
2. Receive GU Packet #1 as a source-issued frozen packet covering the
   C-operator grading-sign result and all five completed method legs.
3. Run it through the repository's provenance, construction, formation,
   completion/null, capability, finality, no-artificial-success, and neutrality
   gates.

If the source packet does not yet trace all five completed legs with their
grades and immutable provenance, record `NOT_YET_IMPORTABLE`. Do not construct a
synthetic unanimous result from partial source artifacts.

## Current state

- Schema: `packets/schema/frozen-packet-v0.1.schema.json`
- Contract checks: `tests/validate_frozen_packet_contract.py`
- Founding-case readiness: `packets/intake/GU-001-readiness-2026-07-14.md`
- GU-001: `NOT_YET_IMPORTABLE` pending a source-issued manifest and bundle hash.
