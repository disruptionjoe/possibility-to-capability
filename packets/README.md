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

- Schemas: v0.1 remains supported; v0.2 adds reproducible bundle integrity,
  method-dependency structure, and a separate non-upgrading receiving
  independence assessment.
- Normative v0.2 contract: `packets/schema/frozen-packet-v0.2.md`
- Contract checks: v0.1 and v0.2 deterministic/adversarial validators under
  `tests/`.
- Founding-case readiness: `packets/intake/GU-001-readiness-2026-07-14.md`
- Founding-case blocked preflight:
  `packets/intake/GU-001-blocked-preflight-v0.1-2026-07-14.json`
- GU-001: IMPORTED 2026-07-16 at pin `77879e5`; see `packets/imports/GU-001/`.
- TAF-001: IMPORTED 2026-07-16 (source-issued by time-as-finality, issuance
  commit `ae37ec19`); see `packets/imports/TAF-001/`.
- TI-PIT-002: IMPORTED 2026-07-16 (source-issued by temporal-issuance, issuance
  commit `8fa01a6f`); see `packets/imports/TI-PIT-002/`, including the standing
  authorship-quarantine restriction recorded in its import record.

Schema hardening does not change packet readiness. A source must issue a packet
against an explicit version; the receiver never migrates or completes it on the
source's behalf.

The blocked preflight is a receiver-owned stop record, not an imported packet.
It keeps every downstream gate `BLOCKED`/`NOT_RUN` until source issuance makes
provenance admissible.
