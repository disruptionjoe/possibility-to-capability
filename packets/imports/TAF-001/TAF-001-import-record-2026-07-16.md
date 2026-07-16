---
artifact_type: import_record
packet_id: TAF-001
status: imported
created: 2026-07-16
constitutional: false
---

# TAF-001 import record (receiver-owned; accompanies, never edits, the frozen packet)

Per the Frozen-Packet Rule, everything in this file is a receiver-side annotation.
The packet bytes in this directory are immutable; time-as-finality owns their content.

## Identity and pins

| field | value |
|---|---|
| source repository | time-as-finality |
| source-issued packet id | TAF-001 (Frozen-Packet Contract v0.2, `packet_status: SOURCE_FROZEN`) |
| content-freeze commit (`source.revision`) | `e0414d6497e8344df811ce594648649ee1480ba4` |
| issuance commit (adds `packet.json` + `ISSUANCE.md`) | `ae37ec196f253de4ea9a70e03ff775094158b4f4` |
| source claim status | exploration (unchanged by import) |
| source evidence grade | formal only (finite executable toy model) (unchanged) |
| mailbox delivery | `system/mailboxes/possibility-to-capability/`, message dated 2026-07-16 (archived with processing receipt) |

## Byte-identical copy declaration

Every file in this directory except this record is an exact byte copy of the git
blob at the issuance commit (`git show ae37ec19:exports/packets/TAF-001-paired-record-intervention-v0.1/<file>`),
including the bundle's own `.gitattributes` (`* -text`), which pins the copies
against eol normalization.

Receiver-verified integrity (re-executed 2026-07-16 against the actual source tree
and again against this imported directory):

- 5/5 manifest blobs re-hashed byte-exact (`byte_length` + `content_sha256` all match).
- Digests recomputed under `ptc-frozen-bundle-v1` via
  `tests/validate_frozen_packet_v0_2_contract.py::expected_digests`:
  `manifest_digest b9a06ac273acd4fe3294267572a480eab45c8b096b7dac2da108f07b751e9d1f`,
  `packet_digest baf974fc92875774511428935327beec3ea8b4288d594a1f2e75c290a5562f9a`,
  `bundle_digest`/`digest` `0b0085419670a619c9574cd2accf1c4347e68ab6f249762372d8626bd8256a94`
  — all match packet fields and the mailbox-claimed values.
- `validate_packet` with this directory as `bundle_root`: 0 errors (run twice:
  against the source tree, and post-write against this imported copy).
- Imported `packet.json` sha256 `0f99b5783c2c26ff5a5d4a332364e3cda1c6d9d10c90da72b774fd96c85739f4`
  = the issuance-commit blob; `ISSUANCE.md` sha256
  `5031d625ced9633180b759514ed1df6309b41b41395368597693a7d62740bfb8`.
- Git provenance in the source repo (read-only): `source.revision` exists, is a
  strict ancestor of the issuance commit; issuance commit is an ancestor of the
  source HEAD; all 5 manifest blobs byte-identical at the pinned
  `source.revision`; two-commit freeze confirmed (`packet.json` absent at the
  content-freeze commit, added at issuance).
- Re-execution: `blobs/taf001_paired_intervention.py` copied to scratchpad and
  run (Python 3): exit 0; stdout identical to `blobs/taf001_output.txt` after
  CRLF/LF normalization (Windows text-mode stdout emits CRLF; the frozen blob
  is CRLF, 2038 bytes raw / 2006 bytes LF-normalized). Logged as an eol
  observation, not a defect: the hashed blob bytes are authoritative and match.

## Gate-run summary (acceptance gates; import tier, not the founding-case Deliverable 1C)

| # | gate | verdict | one-line reasoning |
|---|---|---|---|
| 1 | provenance | PASS | source-issued two-commit freeze; 5/5 blobs + 3 digests + contract validator pass at the pin and post-import; issuer independently re-ran the computation at issuance |
| 2 | read-only / sovereignty | PASS | `authority_transfer: false`; `source_status_unchanged: true`; no TaF claim moves; no source file edited by this run |
| 3 | construction | PASS | three construction forks explicit (task semantics, threshold k, witness family) with transfer status; TaF-native task semantics declared as premise A5, receiver mapping named as receiver work |
| 4 | formation | PASS | one coherent evidence object (baseline W0 + two single-factor interventions + achievability vectors) forms without changing source meanings; the intervention descriptions are mechanical statements of which TaF object was edited |
| 5 | completion/null | PASS | residuals R-1..R-5 honestly scope the nulls (one-directional simulability, clause sensitivity unswept, costs unexercised, composite world uncomputed); fact 3's universal leg is an exhaustive finite sweep (16 access subsets), its simulability leg a single witness |
| 6 | no-artificial-success | PASS | `raw_method_count_is_independence_count: false`; M1/M2 declared one implementation, one run, shared premises A1-A5; packet asserts no independence result and no joint pass |
| 7 | neutrality | PASS | TaF assigns no diagnostic label to ALPHA or BETA under any receiver taxonomy (nonclaims); classification is receiver-owned; issuance was blind to receiver diagnostic labels (the receiver's Rank-2 expectations were frozen in a P2C-side prereg the source never read) |

**Disposition: ACCEPTED (imported, exploration tier).** Import confers no
promotion; grades carry through unweakened and unstrengthened.

## Receiver annotations (readings, not edits)

- **Annotation A — sealed-intent-label posture.** The packet declares targeted
  factors mechanically (ALPHA: access-structure change, record inventory and
  graph fixed; BETA: record-formation change, observer access set fixed) and
  explicitly refuses any receiver-taxonomy diagnostic label. How that
  declaration practice interacts with the receiver's frozen RANK2-PR-001 check
  vocabulary is adjudicated in the Rank-2 run record, not here.
- **Annotation B — D6 quarantine advisory honored.** Per the issuance note's
  referee advisory D6, the receiver's classification run computes from the
  frozen computation blobs (`taf001_paired_intervention.py`, `taf001_output.txt`)
  with the framing prose quarantined from classification decisions.
- **Annotation C — corrected fact 3 received at source strength.** The
  non-interchangeability of ALPHA/BETA deltas is one-directional only (a
  formation-only edit reproduces ALPHA's delta; no access edit reproduces
  BETA's); the invariance assert in the computation is by-construction and
  carries no evidential weight (source's applied referee corrections D1/D2).
- **Annotation D — no physics.** Designed finite witnesses; nothing here bears
  on real systems, GU-001, bar(b), H59, Krein positivity, or physical issuance.
