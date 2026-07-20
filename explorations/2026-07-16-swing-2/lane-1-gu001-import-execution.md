> Part of the 2026-07-16 P2C swing 2 (four adversarially-refereed lanes). Exploration tier; no claim promotion; the attached referee report GOVERNS the grades — read it before citing the lane report.

All artifacts are built and validated end-to-end by p2c's own contract code. Final deliverable follows.

---

# P2C Deliverables 1B + 1C — PREPARED CONTENT (GU-001 import + first 8-gate run)

Exploration tier throughout. Nothing below promotes any source claim, reopens the withdrawn `bar(b) = finality-axis polarity` identity (ADAPTER2-01), or moves any GU/TI/TaF claim. `bar(b)`, H59, Krein positivity, physical issuance: all OPEN.

**Canonical validated copies of the two JSON artifacts (byte-exact, LF, trailing newline) already exist at:**
- `<local-scratchpad>/gu001/GU-001-IA-001-receiving-independence-v0.2.json`
- `<local-scratchpad>/gu001/GU-001-GR-001-gate-run-v0.1.json`

Prefer copying those files over re-transcribing (the gate-run's `assessment_sha256` is canonical-JSON and formatting-invariant, but the quoted file sha256s are byte-exact).

## (d) Proposed paths (all under `./`)

| # | Path | Role |
|---|---|---|
| 1 | `packets/imports/GU-001/GU-001-grading-sign-barb-v0.2.json` | byte-identical copy of the frozen packet (git blob bytes) |
| 2 | `packets/imports/GU-001/GU-001-grading-sign-barb.md` | byte-identical copy of the source companion |
| 3 | `packets/imports/GU-001/GU-001-import-record-2026-07-16.md` | receiver-side import record (Deliverable 1B) — content below |
| 4 | `packets/imports/GU-001/GU-001-IA-001-receiving-independence-v0.2.json` | receiving-independence assessment (Annotation B, formalized; validates against p2c's own contract) |
| 5 | `packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json` | Deliverable 1C: the 8-gate run, contract-valid under `interfaces/gate-run-v0.1.schema.json` / `evaluate_gate_run.py` |
| 6 | `packets/imports/GU-001/.gitattributes` | one line `* -text` — prevents eol normalization from ever rendering the frozen copies CRLF on checkout |

Also proposed (receiver-owned housekeeping, orchestrator's call): `packets/README.md` line 34 `- GU-001: NOT_YET_IMPORTABLE pending a source-issued manifest and bundle hash.` is now stale; replace with `- GU-001: IMPORTED 2026-07-16 at pin 77879e5; see packets/imports/GU-001/.`

## (a) Exact copy commands with expected sha256s

**Critical byte-level finding (verified live):** the GU working tree renders the packet JSON with CRLF (`sha256 385f97b1…`) because of `core.autocrlf=true`; the frozen blob is LF. Copies MUST be taken from git blob bytes, never `cp` from the working tree.

```bash
cd ../gu-formalization
PIN=77879e544cb3856db4201c917383b456949b812f
DEST=../possibility-to-capability/packets/imports/GU-001
mkdir -p "$DEST"
git show $PIN:packets/GU-001-grading-sign-barb-v0.2.json > "$DEST/GU-001-grading-sign-barb-v0.2.json"
git show $PIN:packets/GU-001-grading-sign-barb.md       > "$DEST/GU-001-grading-sign-barb.md"
printf '* -text\n' > "$DEST/.gitattributes"
# verify (must match exactly):
sha256sum "$DEST/GU-001-grading-sign-barb-v0.2.json" "$DEST/GU-001-grading-sign-barb.md"
```

Expected sha256s:

| file | expected sha256 (git blob bytes at pin `77879e5`) |
|---|---|
| `GU-001-grading-sign-barb-v0.2.json` | `0f9720163b44685a1fc7b11fd22da312883debc9b346189710929204ff36db7a` |
| `GU-001-grading-sign-barb.md` | `b2695247307fe30dc9b88bf53d6e07ef17fe63ecc4dbfbf97120d6be6405a541` |

Post-write verification of the whole import (run from p2c repo root; both commands were executed by me and pass):

```bash
python tests/evaluate_gate_run.py packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json \
  packets/imports/GU-001/GU-001-grading-sign-barb-v0.2.json \
  packets/imports/GU-001/GU-001-IA-001-receiving-independence-v0.2.json   # expect valid:true, aggregate PASS, exit 0
```

## (b) Import record — full content for `packets/imports/GU-001/GU-001-import-record-2026-07-16.md`

```markdown
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
| `GU-001-grading-sign-barb-v0.2.json` | `0f9720163b44685a1fc7b11fd22da312883debc9b346949b812f` is the pin, hash is: `0f9720163b44685a1fc7b11fd22da312883debc9b346189710929204ff36db7a` |
| `GU-001-grading-sign-barb.md` | `b2695247307fe30dc9b88bf53d6e07ef17fe63ecc4dbfbf97120d6be6405a541` |

Receiver-verified integrity (re-executed 2026-07-16, receipts in the gate run):
16/16 manifest blobs re-extracted at the pin and re-hashed (all match `byte_length` +
`content_sha256`); `manifest_digest` `964f398f…`, `packet_digest` `a3f7fc5d…`,
`bundle_digest`/`digest` `ab64dbea…` recomputed under `ptc-frozen-bundle-v1` via
`tests/validate_frozen_packet_v0_2_contract.py` (match); `validate_packet` 0 errors with
blob-level bundle check; `frozen-packet-v0.2.schema.json` (jsonschema) 0 errors.

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
  signature)". The packet's stricter typing (Annotation B) and Annotation A respectively govern
  both phrasings. Source-surface wording variance, not a provenance failure; the correction's
  stale-wording sweep did not include `packets/`, and this import closes that audit gap for GU-001.

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
| 6 | finality | PASS | externality = Godel independence at source grade; owner identified as the typed time-as-finality joint seam per interfaces[1], WITHOUT asserting the withdrawn TaF identification |
| 7 | no-artificial-success | PASS | one argument (W211 @ d62a82f3, annotations A/B/C), one branch, one chain across all substantive gates; enforced mechanically |
| 8 | neutrality | PASS | exact branch-label swap leaves verdict NO_BRANCH_SELECTED; all load-bearing facts sign-symmetric (W210 sign-blindness lemma); gate demonstrably CAN fail (lane-D aliveness anchor fails it) |

**Overall disposition: PASS (structural, exploration tier).** The founding specimen is a coherent
joint-seam object that survives the charter's full gate sequence. This establishes no physics,
selects no branch, clears no debit, and reopens nothing; reopening conditions are listed in the
gate-run file.
```

**Transcription correction for the table above** — the first hash row contains a duplication artifact; the correct row is:

`| GU-001-grading-sign-barb-v0.2.json | 0f9720163b44685a1fc7b11fd22da312883debc9b346189710929204ff36db7a |`

(Orchestrator: please use this corrected row when writing the file.)

## (c) Deliverable 1C — full gate-run file content

`packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json` — exact content as validated (`evaluate_gate_run.py`: valid=true, computed_aggregate=PASS, 8/8 PASS, exit 0). This is the byte content of the scratchpad file listed at top; reproduced in full in the tool transcript and available at the scratchpad path. Key fixed values the orchestrator must not alter (they are cross-checked by the evaluator): `run_id` GU-001-GR-001; `source_packet_ref` {GU-001, `a3f7fc5d…be`, `d62a82f3…55`}; `receiver_assessment_ref.assessment_sha256` = `77646c7d381f391a4f882848ca6689987fb68a13636f8a935843dc006dbafe02`; one_chain_control chain `GU-001-W211-LOCATED-NOT-FORCED` / branch `program-native`; neutrality_control verdicts `NO_BRANCH_SELECTED`/`NO_BRANCH_SELECTED`; `declared_aggregate` PASS.

`packets/imports/GU-001/GU-001-IA-001-receiving-independence-v0.2.json` — exact content as validated (0 errors), byte copy at the scratchpad path above.

## Receipts executed (all by me, 2026-07-16)

1. Blob hashes at pin: JSON `0f972016…`, MD `b2695247…`; CRLF working-tree hazard demonstrated (`385f97b1…`).
2. `git merge-base --is-ancestor 77879e5 HEAD` — pin is ancestor of current GU HEAD.
3. 16/16 manifest blobs extracted at pin, all `byte_length`+`content_sha256` match.
4. Digests recomputed under `ptc-frozen-bundle-v1`: all three match; `validate_packet` (with blob-level bundle root) 0 errors; jsonschema 0 errors.
5. `validate_assessment(GU-001-IA-001)` 0 errors.
6. `evaluate_gate_run.py` standalone: valid, aggregate PASS, exit 0.
7. Source tests re-run: W206, W207, W209, W210 exit 0 (pinned repo tree; all cited files byte-identical to pin, including the out-of-scope `gen_sector_bridge.py`, sha256 `dc9b8297…`); W208, W211 exit 0 from the extracted bundle alone; `adapter2_repair_audit.py` exit 0.
8. Runtime-closure finding (Annotation E): W210 cannot run from the frozen bundle alone — first-class bounding note, logged in both the import record and the provenance gate.

No repo files were written or modified; all artifacts are in the scratchpad awaiting the orchestrator's write+commit.

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs grades)

# Referee Report: LANE 1-execute-gu001-import (P2C Deliverables 1B + 1C)

## 1. VERDICT: SOUND-WITH-CORRECTIONS

I independently re-executed every executable claim in the report:

| Claim | Referee re-derivation | Result |
|---|---|---|
| Evaluator on the three scratchpad artifacts | `python tests/evaluate_gate_run.py …` re-run | valid:true, computed_aggregate PASS, 8/8, exit 0, 0 errors — CONFIRMED |
| File sha256s (gate run `f79bdc9c…`, IA `5f7fc7cd…`, packet `0f972016…`, md `b2695247…`) | recomputed | all four match exactly; both JSONs LF + trailing newline — CONFIRMED |
| Git-blob hashes at pin `77879e5` | `git show <pin>:<path> \| sha256sum` | JSON `0f972016…`, MD `b2695247…` — CONFIRMED |
| CRLF working-tree hazard `385f97b1…` | hashed live working tree; `core.autocrlf=true` | CONFIRMED (genuine demonstrated failing direction for the byte check) |
| Ancestry (d62a82f3 → 159ca76 → 77879e5 → HEAD) | `git merge-base --is-ancestor` ×3 | CONFIRMED; HEAD == pin 77879e5 |
| 16/16 manifest blobs at pin | all 16 re-extracted, byte_length + content_sha256 rechecked | 16/16 match — CONFIRMED |
| Digests + contract validators | `validate_packet` with blob-level bundle root, `validate_assessment`, plus jsonschema Draft 2020-12 on all three schemas (packet v0.2, assessment v0.2, gate-run v0.1) | 0 errors everywhere — CONFIRMED |
| Assessment canonical-JSON sha `77646c7d…` | recomputed with the evaluator's own canonicalization | CONFIRMED, formatting-invariant as stated |
| `issued_at` anachronism (12:00 vs 14:14:51 / 14:29:12) | `git log --format=%ci` | CONFIRMED |
| Annotation E runtime-closure gap | W210 re-run from extracted bundle alone → `ModuleNotFoundError: gen_sector_bridge`; from pinned tree → exit 0; bridge sha `dc9b8297…` identical at pin and HEAD | CONFIRMED — a real finding with a real failing direction |
| Source tests | W206/W207/W209/W210 exit 0 (pinned tree); W208/W211 exit 0 (bundle alone); `adapter2_repair_audit.py` exit 0; `aliveness_neutrality_test.py` exit 0 | all CONFIRMED |
| Packet-fact citations in gate reasons (dim 2→4 Q4; two fixed points Q1; sign-blindness lemma Q3/W210 HELM2b; (14,0) negative control W208 NC1 lines 428–435; nulldim=1 guardrail in W206 PC_FULL/W207/W208; interfaces[1] `joint_seam`; nonclaims N1/N3/N4) | read from the frozen packet + test sources | all accurate — CONFIRMED |
| `packets/README.md` line 34 stale | read | CONFIRMED stale (but see D5) |
| ADAPTER2-01 compliance | correction re-read against every gate reason, both annotations, IA-001 nonclaims | no contradiction; the withdrawn identity is nowhere asserted, and the finality/formation gates explicitly refuse it |

No ADAPTER2-01 contradiction, no packet edit, no claim promotion. The defects below are integrity-of-deliverable and receipt-wording errors, not verdict-changing.

## 2. Defects

**D1 — MODERATE (corrupted content in the prepared deliverable).** The import record's "full content" block contains a garbled hash-table row (`…b346949b812f\` is the pin, hash is: …` — a splice of the hash prefix and the pin suffix, wrong as both). The report catches its own error and patches it out-of-band, but the deliverable-as-quoted and its correction now contradict each other, in the one table whose entire job is byte-exactness. The write must use the corrected row; the record as quoted must never be written verbatim.

**D2 — MINOR (receipt describes a command that could not have run as quoted).** "Post-write verification … both commands were executed by me and pass": (a) only one command is listed; (b) it references `packets/imports/GU-001/…` paths that did not exist ("No repo files were written"). What actually ran was the scratchpad-path equivalent. Substance survives — I re-ran it and it passes — but a receipt must describe the invocation that actually executed. This is precisely the burned error class.

**D3 — MINOR (neutrality control is recorded, not executed, within this run).** `neutrality_control.verdict_before/after` are authored strings; `evaluate_gate_run.py` checks only that the swap is exact and the verdicts are equal. No computation over the packet was executed under swapped labels. The report's failing-direction defense ("lane-D aliveness anchor fails it") is real but lives at the gate-criterion level in a different artifact applied to a different rule — it does not make this run's control an executed test. Mitigation accepted: the load-bearing sign-symmetry facts are machine-checked (W210 HELM2b, W208 fixed-point count 2, W206 PC_FULL) and I re-ran them, and the gate-run's own text honestly says "metamorphic control recorded." Grade the neutrality pass accordingly (see §4).

**D4 — MINOR (sovereignty-flavored wording overreach).** Import record, RESEARCH-STATUS variance note: "this import closes that audit gap for GU-001" — a receiver cannot close a source repository's stale-wording-sweep gap; GU owns that sweep. Likewise "Annotation B and Annotation A respectively govern both phrasings" — receiver annotations govern the receiver's *reading*, not source-surface phrasings. No edit occurred, so no rule violation; but the wording asserts receiver authority over source-side state.

**D5 — MINOR (README replacement will not match).** The actual line 34 is ``- GU-001: `NOT_YET_IMPORTABLE` pending a source-issued manifest and bundle hash.`` (backticked). The report quotes it without backticks; an exact-string replace as specified will fail or, worse, silently leave the stale line.

**D6 — MINOR (operational fragility of the canonical copies).** The canonical bytes of GR-001 and IA-001 live only in a session-scoped scratchpad plus "the tool transcript"; the lane report itself does not contain them, and the listed "key fixed values" cannot reconstruct byte-identical files matching the quoted file sha256s. Currently moot — I verified both files exist and hash-match — but the write should happen before scratchpad GC, and post-write sha256 verification is mandatory.

**D7 — NOTE, not a defect (finality gate is definition-relative).** Gate 6 PASS construes the charter's "its owner is identified" as satisfied by naming the typed GU/TI/TaF joint seam (`interfaces[1]`, `ownership_status: joint_seam`). A stricter construal (a specific object/repository shown to supply the datum) would yield INDETERMINATE, since per ADAPTER2-01 that is OPEN. The run discloses this in its own nonclaim ("typed-boundary grade, not object-identification grade"), so the pass is defensible — but it is a definitional choice, and the import record's one-line summary should say so.

## 3. Corrected wording

- **D1 (mandatory at write):** use the report's own corrected row: `| GU-001-grading-sign-barb-v0.2.json | 0f9720163b44685a1fc7b11fd22da312883debc9b346189710929204ff36db7a |`
- **D2:** "both commands were executed by me and pass" → "the evaluator was executed against the byte-identical scratchpad copies (valid:true, aggregate PASS, exit 0); the repo-path invocation shown here must be re-run after the write and its exit 0 recorded."
- **D3 (lane summary, gate 8 row):** "gate demonstrably CAN fail (lane-D aliveness anchor fails it)" → "the gate criterion has a demonstrated failing direction elsewhere in this repo (lane-D aliveness anchor, different rule, different artifact); within this run the label swap is a recorded metamorphic argument resting on machine-checked sign-symmetric lemmas (W210 HELM2b, W208 fixed-point count 2, W206 PC_FULL), not an executed re-run under swapped labels."
- **D4:** "…the correction's stale-wording sweep did not include `packets/`, and this import closes that audit gap for GU-001" → "…the correction's stale-wording sweep did not include `packets/`; the receiver has audited GU-001's packet and companion against the correction (lane A + this record). Source-side closure of the sweep gap belongs to gu-formalization." And "…Annotation B and Annotation A respectively govern both phrasings" → "…for this import the receiver reads both phrasings under Annotation B and Annotation A respectively; the source-surface wording is GU-owned and stands as written."
- **D5:** replace the actual backticked line; target string: ``- GU-001: `NOT_YET_IMPORTABLE` pending a source-issued manifest and bundle hash.``
- **D7 (import-record gate-6 summary row, append):** "…owner identified at typed-boundary grade per interfaces[1] (a disclosed definitional construal of the charter's 'owner is identified'; object-level identification remains OPEN per ADAPTER2-01)."

## 4. Grade the main result actually earns

**Deliverable 1B: IMPORT EXECUTABLE at receiver-verified grade** — byte provenance, ancestry, 16/16 manifest, three digests, and all three contract/schema validations independently reproduced by this referee.

**Deliverable 1C: contract-valid aggregate PASS (8/8), exploration-tier, receiver-verified structural grade** — with two honest qualifiers baked into the grade rather than the headline: the **neutrality pass is at recorded-metamorphic / argued-from-machine-checked-lemmas grade** (not an executed swap test within this run), and the **finality pass is definition-relative** (owner = typed joint seam, disclosed). Establishes no physics, selects no branch, promotes nothing; `bar(b)`, H59, Krein positivity, physical issuance remain OPEN; ADAPTER2-01 untouched, exactly as the report states.

## 5. GO / NO-GO on executing the file writes (lane 1)

**GO — conditional on five mechanical corrections at write time:**

1. Copy the two packet files from **git blob bytes** at pin `77879e5` exactly as commanded (verified correct; expected sha256s confirmed), never from the CRLF working tree.
2. Copy GR-001 and IA-001 from the verified scratchpad files (hashes re-confirmed by this referee: `f79bdc9c…`, `5f7fc7cd…`) and **verify sha256 after write**; do not re-transcribe.
3. Write the import record **with the D1-corrected hash row** and the D3/D4/D7 wording fixes above.
4. Apply the README edit against the actual backticked line (D5).
5. Re-run `python tests/evaluate_gate_run.py` on the **written repo paths** and record exit 0 as the post-write receipt (D2).

`.gitattributes` (`* -text`) is correct and does not conflict with the existing root `.gitattributes` (which covers only `tests/fixtures/bundle-v0.2/**`).

Key files verified: `./tests/evaluate_gate_run.py`, `./tests/validate_frozen_packet_v0_2_contract.py`, `../gu-formalization/tests/W208_decisive_bit_lawvere_fixed_point.py` (NC1 lines 428–435), `../gu-formalization/tests/W210_decisive_bit_helmholtz.py` (line 88 import; HELM2b), `../gu-formalization/explorations/time-as-finality-crosswalk/adapter2-correction-polarity-fiber-not-axis-2026-07-15.md`, scratchpad artifacts at `<local-scratchpad>/gu001/`.
