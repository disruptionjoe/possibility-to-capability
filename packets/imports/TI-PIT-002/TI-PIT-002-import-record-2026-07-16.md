---
artifact_type: import_record
packet_id: TI-PIT-002
status: imported
created: 2026-07-16
constitutional: false
---

# TI-PIT-002 import record (receiver-owned; accompanies, never edits, the frozen packet)

Per the Frozen-Packet Rule, everything in this file is a receiver-side annotation.
The packet bytes in this directory are immutable; temporal-issuance owns their content.

## Identity and pins

| field | value |
|---|---|
| source repository | temporal-issuance |
| source-issued packet id | TI-PIT-002 (Frozen-Packet Contract v0.2, `packet_status: SOURCE_FROZEN`) |
| content-freeze commit (`source.revision`) | `61fc4e6f8530d8620c0a3b66446c2e28e4fda164` |
| issuance commit (adds `packet.json` + `ISSUANCE.md`) | `8fa01a6f0126e49433d7f856450ea0c9c03c5ad4` |
| source claim status | exploration (unchanged by import) |
| source evidence grade | formal only (finite executable toy fixture; absorbed under RUN-0081 gate clause 4) (unchanged) |
| draft lineage | receiver-side draft v0.2 (P2C commit `9652474f`) sovereignly verified and adopted by TI (RUN-0166); counts as evidence only in the exact form TI issued |
| mailbox delivery | `system/mailboxes/possibility-to-capability/`, message dated 2026-07-16 (archived with processing receipt) |

## Byte-identical copy declaration

Every file in this directory except this record is an exact byte copy of the git
blob at the issuance commit (`git show 8fa01a6f:exports/packets/TI-PIT-002-proj-vs-adm-paired-intervention-v0.2/<file>`),
including the bundle's own `.gitattributes` (`* -text`).

Receiver-verified integrity (re-executed 2026-07-16 against the actual source tree
and again against this imported directory):

- 4/4 manifest blobs re-hashed byte-exact (`byte_length` + `content_sha256` all match).
- Digests recomputed under `ptc-frozen-bundle-v1`:
  `manifest_digest f96c8443dbf0baf8d8d4692b254d4fe158634600b512b532378bc4ce567919af`,
  `packet_digest cbf8dceda29c14364398da2ce2c14b93385953d4592aa3c0c23d703e29b44d19`,
  `bundle_digest`/`digest` `9c8e4ec77ca57a2f349057f89613d4e0cb45e50979af01385353d66c19589c39`
  — all match packet fields and the mailbox-claimed values.
- `validate_packet` with this directory as `bundle_root`: 0 errors (source tree
  and post-write imported copy).
- Imported `packet.json` sha256 `663ab3e81f89cbc8d781170d347c725354cab832fcff4eeab89a25bdf1e3f143`
  = the issuance-commit blob; `ISSUANCE.md` sha256
  `4b821f87b611e9d74e2235d8e65f4914fe25e2a74504ea555099cd2ddc6c84bf`.
- Git provenance in the source repo (read-only): `source.revision` exists, is a
  strict ancestor of the issuance commit; issuance commit is an ancestor of the
  source HEAD; all 4 manifest blobs byte-identical at the pinned
  `source.revision`; two-commit freeze confirmed.
- Re-execution: `blobs/ti_pit_02_fixture.py` copied to scratchpad and run
  (Python 3): exit 0; stdout byte-identical (raw, 4999 bytes) to
  `blobs/ti_pit_02_output.txt`; exit 0 requires all six [F] failing-direction
  probes to fail, and they did.

## Gate-run summary (acceptance gates; import tier)

| # | gate | verdict | one-line reasoning |
|---|---|---|---|
| 1 | provenance | PASS | source-issued two-commit freeze; 4/4 blobs + 3 digests + contract validator pass at the pin and post-import; TI re-ran the fixture from the frozen blob at issuance |
| 2 | read-only / sovereignty | PASS | `authority_transfer: false`; `source_status_unchanged: true`; TI-C019/TI-C020 and `Issue[S]^physical: false` untouched; no source file edited by this run |
| 3 | construction | PASS | four construction forks explicit (Ext_n trivialized-not-dropped, hypothesis class H, Glue_n present-not-exercised, witness family) with transfer status; the native seven-component RUN-0081 signature is quoted exactly with an honest instantiation map |
| 4 | formation | PASS | one coherent evidence object (baseline + ALPHA/BETA/BETA-prime single-factor interventions + issuance/decidability consequences) forms without changing source meanings |
| 5 | completion/null | PASS | residuals R-1..R-4 honestly scope the nulls (Glue_n unexercised, H-relativity unswept, globally-patchable-by-construction family, composite uncomputed); quantifiers flag BETA invisibility as an L=2 parameter fact, not structural necessity |
| 6 | no-artificial-success | PASS | `raw_method_count_is_independence_count: false`; M1/M2/M3 declared one implementation, one run, shared premises A1-A5; the [T]-tagged ALPHA issuance identity is excluded from the evidential headline |
| 7 | neutrality | PASS | TI assigns no diagnostic label to ALPHA/BETA/BETA-prime under any receiver taxonomy; classification is receiver-owned; the packet cites, scores, and advocates no frame |

**Disposition: ACCEPTED (imported, exploration tier)** — with one standing
restriction the receiver must honor, below.

## Standing restriction (carried in the packet's nonclaims; binding on receiver use)

**Authorship quarantine.** "This packet and any frame authored by its
originating P2C lane may not be used together as a frame-discriminating pair in
any receiver adjudication; the receiver's independent-reviewer and blind-issuer
roles must be satisfied by other parties." Additionally, Frame R v0.2's own
freeze provenance (`experiments/rival-frames/FRAME-R-access-constitutive-v0.2.md`,
sections R.-1 and P4) records that Frame R's v0.1 advocate (lane C) co-authored
this case's draft lineage and that the v0.2 re-freezing advocate incidentally
sighted the draft text pre-freeze; Frame R earns zero predictive credit from
any advocate-authored case, and the receiver's frozen stop condition S5
(RANK2-PR-001) is stricter still (authored, co-authored, OR read). How this
restricts the Rank-2 run is adjudicated and recorded in the Rank-2 run record,
not here. Acceptance of the packet itself is unaffected.

## Receiver annotations (readings, not edits)

- **Annotation A — sealed-intent-label posture.** Targeted factors are declared
  mechanically (ALPHA: projection-only; BETA: admissibility-only; BETA-prime:
  same admissibility change under fixed wider projection); TI refuses any
  receiver-taxonomy diagnostic label. Interaction with the receiver's frozen
  Rank-2 check vocabulary is adjudicated in the Rank-2 run record.
- **Annotation B — no physical significance.** Absorbed under RUN-0081 gate
  clause 4; must not be cited as evidence for `Issue[S]` of any type; nothing
  here bears on GU-001, bar(b), H59, Krein positivity, or physical issuance.
- **Annotation C — globally patchable by construction.** Residual R-3: the
  family is deterministic and single-observer; per Frame R v0.2's own scope
  discipline (P3), such families neither support nor cheaply fire the
  contextuality prediction either way.
