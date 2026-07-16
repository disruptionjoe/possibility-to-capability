---
artifact_type: import_record
packet_id: GU-001
status: imported
created: 2026-07-16
constitutional: false
---

# GU-001 import record (receiver-owned; accompanies, never edits, the frozen packet)

Per the Frozen-Packet Rule, everything in this file is a receiver-side annotation.
The packet bytes in this directory are immutable; the source repository owns their content.

## Identity and pins

| field | value |
|---|---|
| source repository | gu-formalization |
| source-issued packet id | GU-001 (Frozen-Packet Contract v0.2, `packet_status: SOURCE_FROZEN`) |
| import pin (p2c-selected) | `77879e544cb3856db4201c917383b456949b812f` (contains the frozen packet AND the ADAPTER2-01 correction) |
| packet-internal evidence pin (`source.revision`) | `d62a82f3a74731b322a5d65b5ee15a2b861e2855` (ancestor of the import pin; all 16 hash-scoped artifacts byte-identical between the two) |
| packet issuance commit | `dde3792d6226fcd6cf67c3451bb63dab48e13b38` |
| adapter-2 correction commit | `159ca768ae81489645fb87a224ac9b35fb48cfc3` |
| source claim status | exploration (unchanged by import) |

## Byte-identical copy declaration

The two files in this directory are exact byte copies of the git blobs at the import pin
(`git show 77879e5:packets/<file>`), NOT of the Windows working tree, whose checkout renders
the JSON with CRLF (sha256 `385f97b137b46d39d3d6263f1ce5c184d24b498d4970512f3c0833faf28c4bc0`
— a live demonstration that the byte check has a real failing direction). `.gitattributes`
(`* -text`) pins the copies against eol normalization.

| file | sha256 (frozen blob bytes) |
|---|---|
| `GU-001-grading-sign-barb-v0.2.json` | `0f9720163b44685a1fc7b11fd22da312883debc9b346189710929204ff36db7a` |
| `GU-001-grading-sign-barb.md` | `b2695247307fe30dc9b88bf53d6e07ef17fe63ecc4dbfbf97120d6be6405a541` |

Receiver-verified integrity (re-executed 2026-07-16, receipts in the gate run):
16/16 manifest blobs re-extracted at the pin and re-hashed (all match `byte_length` +
`content_sha256`); `manifest_digest` `964f398f…`, `packet_digest` `a3f7fc5d…`,
`bundle_digest`/`digest` `ab64dbea…` recomputed under `ptc-frozen-bundle-v1` via
`tests/validate_frozen_packet_v0_2_contract.py` (match); `validate_packet` 0 errors with
blob-level bundle check; `frozen-packet-v0.2.schema.json` (jsonschema) 0 errors.
Post-write receipt: `python tests/evaluate_gate_run.py` re-run against the written repo paths
in this directory — valid:true, computed_aggregate PASS, exit 0 (see commit introducing this
directory).

## Receiver annotations (readings, not edits)

- **Annotation A — correction supremacy.** The "=" chain in
  `evidence_structure.premise_ledger[P-EXTERNAL-C-OPERATOR]` ("… = the TaF-owned finality
  activation = the finality-reservoir metric signature"), the phrase in `alternatives[0]`
  ("the finality-reservoir metric signature … supplies the one bit"), AND the apposition
  inside `claim.statement` itself ("… / TaF-owned finality activation") are read as
  typed-interface descriptions per the packet's own `nonclaims[1]` and `interfaces[1]`.
  The governing document is the adapter-2 correction
  (`explorations/time-as-finality-crosswalk/adapter2-correction-polarity-fiber-not-axis-2026-07-15.md`,
  absent at the evidence pin, present at the import pin): the GU-sign-to-TaF-finality-axis-polarity
  identification is OPEN — an untransported Z/2 fiber over a common finality profile, a forgetful
  functor, two globally flipped anchors, and a six-condition reopen burden. Located-Is-Not-Forced
  applies at the seam too: W211 locates the datum at the boundary; nothing identifies it with any
  specific TaF object.
- **Annotation B — independence typing.** Received at exactly source strength
  (`proof_theoretic_independence` of the RESULT). The five methods (W206-W210) are ONE
  dependence-driven convergence unit — all five share all five load-bearing premises and reduce
  to the single external Z/2 posit — never five evidential units
  (`raw_method_count_is_independence_count = false`). Formalized in `GU-001-IA-001` (this
  directory), which passes p2c's receiving-independence contract (0 errors) and neither
  strengthens nor weakens the source typing.
- **Annotation C — no promotion.** Source claim tier is exploration; import confers no promotion.
  All grades (EXACT / STRONG / STRUCTURAL / ARGUED; internal-tier verification only; no Lean/Lake
  build; no external replication) carry through unweakened and unstrengthened.
- **Annotation D — issued_at anachronism (logged, not amended).** `source.issued_at` is
  `2026-07-15T12:00:00-05:00`, which predates both the evidence pin's commit time
  (`d62a82f3`, 14:14:51 -0500) and the issuance commit (`dde3792`, 14:29 -0500). Internally
  anachronistic; harmless; git commit times govern. The field stands as issued.
- **Annotation E — bundle is byte-frozen, not runtime-closed (found by receiver re-execution).**
  `tests/W210_decisive_bit_helmholtz.py` imports `tests/generation-sector/gen_sector_bridge.py`,
  which is OUTSIDE the 16-file `hash_scope` (verified byte-identical at pin and HEAD,
  sha256 `dc9b8297f392d49147944edfbf9636cda86b2ede7c9f2bf5283bc9396e0a4ec7`). The extracted
  bundle alone cannot re-execute W210; its exit-0 receipt comes from the pinned repo tree.
  W206/W207/W209 re-run exit 0 from the pinned tree; W208 and W211 re-run exit 0 from the
  extracted bundle alone. Logged as a first-class bounding note (Failure-Preservation Rule),
  not a packet defect.
- **RESEARCH-STATUS wording variance (logged).** `RESEARCH-STATUS.md` line 124 (W211 row) says
  "FIVE independent methods" and "The one datum is EXTERNAL (the TI/TaF finality-reservoir
  signature)". For this import the receiver reads both phrasings under Annotation B and
  Annotation A respectively; the source-surface wording is GU-owned and stands as written.
  Source-surface wording variance, not a provenance failure; the correction's stale-wording
  sweep did not include `packets/`; the receiver has audited GU-001's packet and companion
  against the correction (swing lane A + this record). Source-side closure of the sweep gap
  belongs to gu-formalization.

## Companion receiver artifacts

| artifact | id | hash |
|---|---|---|
| receiving-independence assessment | GU-001-IA-001 | canonical-JSON sha256 `77646c7d381f391a4f882848ca6689987fb68a13636f8a935843dc006dbafe02`; file sha256 `5f7fc7cd09eb08e1cf6be769ca9d5a86d3a60f8069a0247efe08180ba6234120` |
| neutral gate run (Deliverable 1C) | GU-001-GR-001 | aggregate PASS (8/8), `evaluate_gate_run.py` valid, exit 0; file sha256 `f79bdc9c68fb164c941e1861ca978d31a32fd0842afaa642d07f00010641f9e7` |

## Gate-run summary (details and receipts in GU-001-GR-001)

| # | gate | verdict | one-line reasoning |
|---|---|---|---|
| 1 | provenance | PASS | 16/16 blobs + 3 digests + 2 contract validators pass at the pin; issued_at anachronism, RESEARCH-STATUS wording, and W210 runtime-closure gap logged as variances, not failures |
| 2 | construction | PASS | both forks explicit with transfer status; rep-canonicity caveat carried; both sign branches remain live |
| 3 | formation | PASS | one joint object (good-stable + one external Z/2 at a typed boundary) forms under Annotation A without altering source meanings |
| 4 | completion-null | PASS | residual survives all DECLARED completions ("compute harder" ruled out 5 ways; refinement enlarges dim 2->4); failing direction real (full so(9,5) absorbs the ungraded metric); unbuilt completions explicitly untested |
| 5 | capability | PASS | branches differ by a basis-invariant (definite vs indefinite physical inner product on the record sector), not a relabeling; failing direction demonstrated ((14,0) control: fork vanishes); physical cash-out (bar(b)) stays OPEN |
| 6 | finality | PASS | externality = Godel independence at source grade; owner identified at typed-boundary grade per interfaces[1] — a disclosed definitional construal of the charter's "owner is identified"; object-level identification remains OPEN per ADAPTER2-01 — without asserting the withdrawn TaF identification |
| 7 | no-artificial-success | PASS | one argument (W211 @ d62a82f3, annotations A/B/C), one branch, one chain across all substantive gates; enforced mechanically |
| 8 | neutrality | PASS | exact branch-label swap leaves verdict NO_BRANCH_SELECTED; the gate criterion has a demonstrated failing direction elsewhere in this repo (the aliveness-anchor rule fails it — different rule, different artifact); within this run the label swap is a recorded metamorphic argument resting on machine-checked sign-symmetric lemmas (W210 HELM2b, W208 fixed-point count 2, W206 PC_FULL), not an executed re-run under swapped labels |

**Overall disposition: PASS (structural, exploration tier)** — with two disclosed grade qualifiers:
the neutrality pass is at recorded-metamorphic / argued-from-machine-checked-lemmas grade, and the
finality pass is definition-relative (owner = typed joint seam). The founding specimen is a coherent
joint-seam object that survives the charter's full gate sequence. This establishes no physics,
selects no branch, clears no debit, and reopens nothing; reopening conditions are listed in the
gate-run file.
