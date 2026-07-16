---
artifact_type: import_record
packet_id: TAF-002
status: imported
created: 2026-07-16
constitutional: false
---

# TAF-002 import record (receiver-owned; accompanies, never edits, the frozen packet)

Per the Frozen-Packet Rule, everything in this file is a receiver-side annotation.
The packet bytes in this directory are immutable; time-as-finality owns their content.

## Identity and pins

| field | value |
|---|---|
| source repository | time-as-finality |
| source-issued packet id | TAF-002 (Frozen-Packet Contract v0.2, `packet_status: SOURCE_FROZEN`) |
| content-freeze commit (`source.revision`) | `0749ce51c2eb542defe4010341787f1974a56a7d` |
| issuance commit (adds `packet.json` + `ISSUANCE.md`) | `e0b5773d7ede2e72cc1afb1e367ee581418fed75` |
| source claim status | exploration (unchanged by import) |
| source evidence grade | formal only (finite executable designed witness over literature-grade stipulated physics) (unchanged) |
| adjudicated input | P2C-W1 witness bundle, UNCHANGED, freeze commit `4c9c28bb`, all four blob sha256 pinned in `blobs/taf002_semantics.md` section 1 (receiver re-confirmed identity against `exports/witness/P2C-W1-superconducting-ring-v0.1/witness.json`) |
| mailbox delivery | `system/mailboxes/possibility-to-capability/20260716-taf002-p2cw1-capability-adjudication-frozen-return.md` (archived with processing receipt) |

## Byte-identical copy declaration

Every file in this directory except this record is an exact byte copy of the git
blob at the issuance commit
(`git show e0b5773d:exports/packets/TAF-002-p2cw1-capability-adjudication-v0.1/<file>`),
including the bundle's own `.gitattributes` (`* -text`), which pins the copies
against eol normalization.

Receiver-verified integrity (re-executed 2026-07-16 against the actual source tree
and again against this imported directory; harness and full log in
`explorations/2026-07-16-cross-repo-adjudication/`):

- 6/6 manifest blobs re-hashed byte-exact (`byte_length` + `content_sha256` all match),
  in the source tree, at the pinned `source.revision` (git-show blob re-hash), and
  post-write in this imported copy.
- Digests recomputed under `ptc-frozen-bundle-v1` via
  `tests/validate_frozen_packet_v0_2_contract.py::expected_digests`:
  `manifest_digest 6826fc19dfbddaaab6b2226620a41b70b0a9d936efe509ebe908142ec0255487`,
  `packet_digest 4bf8c8efe8ad6f9bbeb9a7b7b920bd613e2bcb4439b1c040a374992c54159c72`,
  `bundle_digest`/`digest` `0237f93b6e075968600b065b08dbd2ee334290dd428b3821eb4c57502e17ed79`
  — all match packet fields and the mailbox-claimed values.
- `validate_packet` with this directory as `bundle_root`: 0 errors (run twice:
  against the source tree, and post-write against this imported copy).
- Imported `packet.json` sha256 `f1fb13e6cfefd1122f75b61b382cb0d4e225d995a3fcf2a56a68dca714b0c831`
  = the issuance-commit blob; `ISSUANCE.md` sha256
  `92a1d1fa36ba63c1c2741436ed922985c800653a6b1481fd84270961f1652344`.
- Git provenance in the source repo (read-only): `source.revision` exists, is a
  strict ancestor of the issuance commit; issuance commit is an ancestor of the
  source HEAD; all 6 manifest blobs byte-identical at the pinned
  `source.revision`; two-commit freeze confirmed (`packet.json` absent at the
  content-freeze commit, added at issuance).
- Re-execution: `blobs/taf002_p2cw1_adjudication.py` run (Python 3): exit 0;
  stdout identical to `blobs/taf002_output.txt` after CRLF/LF normalization
  (Windows text-mode stdout; the hashed blob bytes are authoritative and match).
  Headline confirmed: 10 [E] + 3 [F] evidential checks, 1 [T].
- Same-frozen-witness rule: the packet's pinned P2C-W1 manifest (all four blob
  sha256s and the freeze commit) matches `witness.json` exactly; the receiver
  additionally re-verified its own witness bundle (blob re-hash + discriminator
  re-run byte-identical, exit 0) before treating the returns as combinable.

## Gate-run summary (acceptance gates; import tier, not the founding-case Deliverable 1C)

| # | gate | verdict | one-line reasoning |
|---|---|---|---|
| 1 | provenance | PASS | source-issued two-commit freeze; 6/6 blobs + 3 digests + contract validator pass at the pin and post-import; issuer re-ran the computation at issuance and this run re-ran it again |
| 2 | read-only / sovereignty | PASS | `authority_transfer: false`; `source_status_unchanged: true`; no TaF claim moves; TaF asserted nothing inside P2C's hierarchy (nonclaims); no source file edited by this run |
| 3 | construction | PASS | three construction forks explicit (task semantics, context individuation of the pair, branch physics) with transfer status; the load-bearing fork — two-context vs one-context individuation — is declared as `source_only`/unadjudicated, exactly the F1 boundary |
| 4 | formation | PASS | one coherent evidence object (two region-indexed T583 contexts modeling the witness's declared R-D1 frame + controls c1-c12) forms without changing source meanings; the witness physics is consumed as quarantined literature-grade stipulation (A4) |
| 5 | completion/null | PASS | residuals R-1..R-5 honestly scope the nulls (one designed frame, tau_P capped at the metastability horizon, physics-as-stipulation, no Clause-2-to-Clause-3 bridge, D1 at k=1 single-holder); the fail-closed controls (access, resource x10^6, hidden state) are exercised executably |
| 6 | no-artificial-success | PASS | `raw_method_count_is_independence_count: false`; one method, one implementation, shared premises A1-A6; the packet asserts no independence result; the witness's own discriminator re-run is explicitly excluded from evidential weight |
| 7 | neutrality | PASS | branch-label-swap neutrality exercised in the fixture (c7) with a demonstrated failing direction (c8); the SPLIT verdict endorses neither context individuation; no desired verdict was honored (the proposal contained none) |

**Disposition: ACCEPTED (imported, exploration tier).** Import confers no
promotion; grades carry through unweakened and unstrengthened.

## Receiver annotations (readings, not edits)

- **Annotation A — verdict is frame-indexed and vocabulary-quarantined.** Clause 1
  affirms a capability change only inside the declared budget-matched
  counterfactual pair, in TaF's native task semantics (reconstructibility). The
  packet explicitly refuses P2C's "enlargement vs disclosure" vocabulary; any
  mapping onto P2C hierarchy grades is receiver work and is performed (with its
  own grade) only in the combining-adjudication record, not here.
- **Annotation B — Clause 3 is a first-class non-answer.** TaF rules the
  fixed-family absorber not adjudicable by its frame-taking contract and leaves
  P2C falsifier F1 untouched in both directions. This import does not convert
  that boundary statement into evidence for either direction.
- **Annotation C — tau_P rider is binding on receiver use.** Persistence is
  affirmed only up to the literature metastability cap; the carriers surviving at
  every horizon and budget are tau_Q and tau_I. Any receiver conclusion citing
  persistence must carry this cap.
- **Annotation D — task-semantics fork is untested transfer.** TaF's
  "achievability = reconstructibility" is declared as premise A2 with
  `transfer_status: untested` to any other task semantics, including P2C's
  Capability type; the combining adjudication must carry this as a named
  conditionality, not silently identify the two.
