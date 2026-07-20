> Part of the 2026-07-16 P2C big swing (four adversarially-verified lanes). Exploration tier; no claim promotion; the attached referee report GOVERNS the grades — read it before citing the lane report.

# P2C Deliverable 1B: Founding Packet #1 — Importability Determination

## VERDICT: IMPORTABLE

GU has already frozen a source-issued packet for GU-001 (commit `dde3792`, 2026-07-15 14:29 -0500): `packets/GU-001-grading-sign-barb-v0.2.json` (authoritative) + `packets/GU-001-grading-sign-barb.md` (companion), Frozen-Packet Contract v0.2, `packet_status: SOURCE_FROZEN`. Every leg of the charter's Deliverable-1B checklist is traceable to a completed source artifact with its own grade and provenance, and the packet content is consistent with the 2026-07-15 adapter-2 correction (verified below). No `NOT_YET_IMPORTABLE` gap exists.

## Pinned revisions

| object | revision |
|---|---|
| GU repo HEAD now (recommended p2c import pin) | `77879e544cb3856db4201c917383b456949b812f` |
| Packet-internal evidence pin (`source.revision` in the JSON) | `d62a82f3a74731b322a5d65b5ee15a2b861e2855` (2026-07-15 14:14 -0500; ancestor of HEAD) |
| Packet issuance commit | `dde3792d6226fcd6cf67c3451bb63dab48e13b38` |
| Adapter-2 correction commit | `159ca768ae81489645fb87a224ac9b35fb48cfc3` (2026-07-15 23:47 -0500) |

Verified: all 16 hash-scoped evidence artifacts are **byte-identical** between `d62a82f3` and HEAD `77879e5` (`git diff --stat` empty on those paths; only the packet JSON itself was added after the pin). So importing at HEAD gives a single pin containing both the frozen packet and the correction, with the packet's internal `content_sha256` manifest still valid. Spot-check: 4 of 16 manifest hashes recomputed from `git show d62a82f3:<path>` — all match (W202 note `1e6fd2…`, W206 note `ce58de…`, W211 note `0e1c21…`, W211 test `e533d9…`).

## Correction-compatibility audit (the governing constraint)

The pin `d62a82f3` **predates** correction commit `159ca76` by ~9.5 hours, so the question was whether the frozen packet asserts anything the correction withdrew. It does not:

- The withdrawn claim was `bar(b) = finality-axis polarity` (the adapter-2 branch-preserving functor). The packet never asserts it. Its `nonclaims[1]`: "This does NOT assert any TI/TaF or cross-repository identity; the boundary fields are typed-interface requests only." Its `interfaces[1]` marks the TaF datum "gated and no cross-repo identity is asserted."
- `bar(b)` and `H59` are carried as OPEN throughout (`residuals[0]`, companion §"bar (b) status"), matching the correction's end state.
- The correction's own receipt says no current canon/operational surface asserted the ratified identity.
- What the packet DOES claim (five-method located-not-forced; monotone-but-external Z/2; "compute harder inside GU" ruled out) is untouched by the correction — the correction withdrew only the *identification* of that external bit with TaF finality-axis polarity, not its externality.

**Two wording cautions p2c must carry as receiver-side annotations (not packet edits, per the Frozen-Packet Rule):**

1. `evidence_structure.premise_ledger[P-EXTERNAL-C-OPERATOR].exact_statement` contains the chain "the interacting C-operator = the unbuilt C2-closing Y14 connection-curvature spectral section (W173) = the TaF-owned finality activation = the finality-reservoir metric signature." Post-correction, the last two "=" links are OPEN conjectural bridges (a Z/2 fiber over a common finality profile, per the correction), not established identities. The packet's own `nonclaims` discipline this reading, but the receiver must record that the correction (`explorations/time-as-finality-crosswalk/adapter2-correction-polarity-fiber-not-axis-2026-07-15.md`, absent at the packet pin, present at HEAD) governs.
2. The correction's stale-wording sweep column lists `RESEARCH-STATUS.md`, `CANON.md`, `DERIVATION-PROGRESS.md`, `NEXT-STEPS.md`, `canon/`, `papers/`, `explorations/`, `lab/`, `tests/` — `packets/` was not in the searched set. The audit above closes that gap for GU-001.

## Packet manifest draft — 17 charter fields (Frozen-Packet Schema v0.1) with file-level provenance

All paths relative to `../gu-formalization/` at pin `77879e5` (evidence bytes identical at `d62a82f3`).

| # | Charter v0.1 field | Status | Source (exact file / JSON field) |
|---|---|---|---|
| 1 | Source repository + immutable revision | SATISFIED | `packets/GU-001-grading-sign-barb-v0.2.json` `source.repository` = `gu-formalization`, `source.revision` = `d62a82f3…` |
| 2 | Source-issued packet identifier | SATISFIED | `packet_id` = `GU-001` (source-issued at commit `dde3792`) |
| 3 | Exact question decided | SATISFIED | `question.exact_question` (is the C-operator grading sign / bar(b) forced or a residual Z/2), `decision_type` = `not_forced` |
| 4 | Definitions and notation | SATISFIED | Inline in `question`/`claim`/`premise_ledger` exact statements + the 8 frozen exploration notes in `source.artifact_paths` (W202, W203, W206–W211), each hash-pinned in `integrity.manifest` |
| 5 | Construction choice + retained forks | SATISFIED | `construction_forks` (2 forks: program-native-vs-standard-field, `transfers`; derived-in-form-vs-posited-in-sign, `does_not_transfer`) |
| 6 | Assumptions and quantifiers | SATISFIED | `assumptions` (5 items incl. Cl(9,5)=M(64,H) caveat, no-Lean-build) + `quantifiers` (5 exact universally-quantified statements) |
| 7 | Method-by-method result ledger | SATISFIED | `method_ledger` (5 entries W206–W210, each: label, `artifact_path`, `artifact_revision`, result `RESIDUAL-BIT-STANDS`, verbatim grade, verification script, `premise_ids`) |
| 8 | Proof/computation/argument/exploration grades | SATISFIED | Per-method `grade` fields (EXACT / STRONG / STRUCTURAL / ARGUED distinctions verbatim) + `source.evidence_grade` |
| 9 | Verification and replication status | SATISFIED | `verification.artifacts` (6 test scripts, all exit 0) + `replication_status` (internal-tier only; no external replication; no Lean/Lake build — stated honestly) |
| 10 | Claim status in source repository | SATISFIED | `source.claim_status` = `exploration`; `claim.source_status_unchanged` = `true`; RESEARCH-STATUS.md line 124 (W211 row: exploration-tier, verdict-stable, bar(b)/H59 OPEN) |
| 11 | Scope of independence/impossibility result | SATISFIED | `claim.independence_scope` + `independence_type` = `proof_theoretic_independence` (Godel-independence of the RESULT), with `raw_method_count_is_independence_count` = `false` — convergence explicitly typed as shared-premise, not evidential independence |
| 12 | Admissible alternatives or countermodels | SATISFIED | `alternatives` (external TI/TaF supply; Krein-positivity axiom; compute-harder ruled out) + W208's two-fixed-point countermodel (C_good vs C_path) in `method_ledger[2]` |
| 13 | Named residuals + known failure conditions | SATISFIED | `residuals` (6 items: bar(b)/H59 OPEN, unbuilt interacting C-operator + K_S proxy, kappa/Z_U, STRUCTURAL-lift limits, rep-canonicity, W154 assumption) |
| 14 | Statements explicitly not established | SATISFIED | `nonclaims` (6 items, incl. no cross-repo identity, no sign selection, not-an-independence-count) |
| 15 | Source-repository ownership | SATISFIED | `ownership` (`source_owner` = gu-formalization, `receiving_owner` = possibility-to-capability, `authority_transfer` = false) |
| 16 | Requested boundary interfaces | SATISFIED | `interfaces` (p2c: receiving-independence assessment, may weaken never strengthen; time-as-finality: the external Z/2 as typed interface, `joint_seam`, gated) |
| 17 | Content hash / freezing mechanism | SATISFIED | `integrity`: sha256, `ptc-frozen-bundle-v1`, 16-file manifest with per-file `byte_length` + `content_sha256` (4/16 independently reverified against git blobs, all match), `manifest_digest` `964f39…`, `packet_digest` `a3f7fc…`, `bundle_digest` `ab64db…`, `frozen: true` |

**Missing fields: none.** 17/17 satisfiable from existing committed GU artifacts.

## Receiver-side import record (p2c-owned; to accompany, never edit, the packet)

- **Import pin:** `77879e544cb3856db4201c917383b456949b812f` (contains packet + correction; evidence bytes identical to packet-internal pin `d62a82f3`).
- **Annotation A (correction supremacy):** the "=" chain in `P-EXTERNAL-C-OPERATOR` and the phrase "the finality-reservoir metric signature … supplies the one bit" in `alternatives[0]` are read as typed-interface descriptions per the packet's own `nonclaims`; the adapter-2 correction (`adapter2-correction-polarity-fiber-not-axis-2026-07-15.md`, `adapter2_repair_audit.py`) establishes the GU-sign-to-TaF-polarity identification is OPEN (untransported Z/2 fiber, forgetful functor, two flipped anchors, six-condition reopen burden). Located-Is-Not-Forced applies at the seam too: W211 locates the datum at the boundary; nothing yet identifies it with any specific TaF object.
- **Annotation B (independence typing accepted at source type or weaker):** p2c receives `proof_theoretic_independence` for the result; the five methods are one dependence-driven convergence unit (all five share all five load-bearing premises), never counted as five evidential units.
- **Annotation C:** source claim tier is exploration; import confers no promotion. All grades (EXACT/STRONG/STRUCTURAL/ARGUED, internal-tier verification only) carry through unweakened and unstrengthened.
- **Note for Gate 1 (Provenance):** RESEARCH-STATUS.md line 124 says "FIVE independent methods" — the packet's typing (`raw_method_count_is_independence_count = false`) is the stricter and governing wording; flag as a source-surface wording variance, not a provenance failure.

Key files: `../gu-formalization/packets/GU-001-grading-sign-barb-v0.2.json`, `.../packets/GU-001-grading-sign-barb.md`, `.../RESEARCH-STATUS.md` (line 124), `.../explorations/time-as-finality-crosswalk/adapter2-correction-polarity-fiber-not-axis-2026-07-15.md`.

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs grades)

# Referee Report: LANE A-packet-provenance (P2C Deliverable 1B)

## 1. VERDICT: SOUND-WITH-CORRECTIONS

The core determination (IMPORTABLE) survives adversarial re-derivation. I independently re-executed every executable claim and extended the report's own verification beyond what it performed:

| Check | Report's evidence | Referee re-derivation | Result |
|---|---|---|---|
| Pinned revisions/timestamps (dde3792 14:29, 159ca76 23:47, d62a82f3 14:14, ancestor-of-HEAD) | asserted | `git log`, `git merge-base --is-ancestor` | all confirmed |
| Manifest hashes at pin | 4/16 spot-checked | all 16/16 recomputed from `git show d62a82f3:<path>` | all match (incl. the 4 quoted prefixes 1e6fd2/ce58de/0e1c21/e533d9) |
| Evidence byte-identity pin→HEAD | `git diff --stat` empty | reproduced | empty on all 16 paths |
| Digest chain | quoted, not recomputed | recomputed `manifest_digest`/`packet_digest`/`bundle_digest` via p2c's own `ptc-frozen-bundle-v1` canonicalization (`tests/validate_frozen_packet_v0_2_contract.py` functions) | 964f39…/a3f7fc…/ab64db… all match |
| Contract v0.2 conformance | asserted, no receipt | validated GU-001 JSON against `packets/schema/frozen-packet-v0.2.schema.json` (jsonschema Draft 2020-12) | 0 errors |
| "all exit 0" | asserted | re-ran W206, W208, W211 tests + `adapter2_repair_audit.py` | all exit 0 |
| Packet-field quotes (nonclaims, interfaces, residuals[0], premise chain, counts 2/5/5/5/3/6/6, `raw_method_count_is_independence_count=false`, `source_status_unchanged=true`) | quoted | read from JSON | all accurate |
| Correction-doc quotes (sweep column omits `packets/`, receipt text, fiber-not-axis picture, six-condition reopen burden) | quoted | read correction file | accurate (one paraphrase issue, defect 2) |

No cannot-fail test, no mislabeled control, no ADAPTER2-01 contradiction, no source-sovereignty violation (annotations-not-edits is the charter-correct mechanism), and the charter's own `NOT_YET_IMPORTABLE` trigger ("GU has not frozen all five method results into an importable source packet") is demonstrably not met. The defects below are wording/coverage errors, not verdict-changing.

## 2. Defects found

**D1 — MODERATE (claim graded above its shown evidence).** The verdict line asserts "Frozen-Packet Contract v0.2" conformance, but the report never ran p2c's v0.2 schema or recomputed the three digests; its integrity evidence was a 4/16 hash spot-check. The assertion happens to be true (I verified: schema 0 errors, digests match), but as written it was an unreceipted grade. In a program burned by exactly this class of error, conformance claims need the receipt attached.

**D2 — MODERATE (overbroad paraphrase of the correction receipt).** "The correction's own receipt says no current canon/operational surface asserted the ratified identity." The receipt actually says no **canon file, paper, CANON.md, DERIVATION-PROGRESS.md, or current NEXT-STEPS.md block** asserted it. Exploration-layer surfaces DID assert it — the RATIFIED doc, adapter contract, gate-pipeline conclusion, and hardening script were all rewritten in commit 159ca76 itself (11 files, 625 deletions). The paraphrase understates how much of the repo carried the withdrawn claim.

**D3 — MINOR (incomplete correction-sensitivity sweep of the packet).** Annotation A covers `premise_ledger[P-EXTERNAL-C-OPERATOR]` and `alternatives[0]` but misses that `claim.statement` itself carries the same TaF-identifying apposition: "…must be supplied by the external unbuilt interacting C-operator (the C2-closing Y14-curvature spectral section / **TaF-owned finality activation**)." The load-bearing claim field needs the same receiver annotation as the premise ledger. (Also note the RESEARCH-STATUS W211 row, cited for field 10, says "The one datum is EXTERNAL (the TI/TaF finality-reservoir signature)" — same flavor, source-side, survived GU's own sweep; worth one line in the Gate-1 note.)

**D4 — MINOR (false parenthetical).** "only the packet JSON itself was added after the pin" is wrong. Between d62a82f3 and HEAD: commit 924adfd added the W244 re-verification note and tests; dde3792 added the packet JSON **and** the .md companion; then five more commits added the adapter-2 arc, its ratification, its correction, and the recovery gate. True only when restricted to the 16 manifest paths.

**D5 — MINOR (missed provenance nit).** The packet's `source.issued_at` is `2026-07-15T12:00:00-05:00`, which **predates** its own evidence pin's commit time (d62a82f3, 14:14:51) and its issuance commit (14:29). A packet claiming noon issuance pinned to a 14:14 commit is internally anachronistic. Harmless (git commit times govern), but the receiver record should log it; the report's provenance audit should have caught it.

**D6 — MINOR (checklist conflation).** The verdict says "Every leg of the charter's Deliverable-**1B** checklist is traceable," but the 17-field table audits Deliverable-**1A**'s schema list. 1B has its own nine "separately preserves" items. I verified all nine do map (W203 coefficients and W202 decoupling in `claim.statement`/`nonclaims[5]`; binary datum; per-leg method ledger with grade+revision; independence meaning in `independence_scope`/`evidence_structure`; locate-vs-select in `nonclaims[4]`; bar(b) unchanged in `residuals[0]`/`nonclaims[2]`; TI/TaF boundary deps in `interfaces`; caveats/forks/grades in `assumptions`/`construction_forks`/method grades) — so substance holds, but the report proves 1A and labels it 1B.

## 3. Corrected wording

- **D1 (verdict paragraph):** "…Frozen-Packet Contract v0.2, `packet_status: SOURCE_FROZEN`" → "…Frozen-Packet Contract v0.2 (**validated against p2c's `frozen-packet-v0.2.schema.json`, 0 errors; manifest, packet, and bundle digests recomputed under `ptc-frozen-bundle-v1` and matching**), `packet_status: SOURCE_FROZEN`."
- **D2:** → "The correction's receipt states that no canon file, paper, CANON.md, DERIVATION-PROGRESS.md, or current NEXT-STEPS.md block asserted the ratified identity; the exploration-layer adapter documents that did assert it were rewritten in the correction commit itself."
- **D4:** → "the 16 manifest paths are byte-identical between the pin and HEAD; the commits after the pin (W244 re-verification, the GU-001 packet pair, the adapter-2 arc and its correction, the recovery gate) touch none of them."
- **D3 (Annotation A, add):** "…the same annotation governs the parenthetical '/ TaF-owned finality activation' inside `claim.statement`."
- **D6:** retitle the table "17 Deliverable-1A schema fields" and add a nine-row 1B preservation map (all nine SATISFIED).

## 4. Grade the main result actually earns

**IMPORTABLE — stands, now at receiver-verified grade** (full 16/16 manifest verification, digest recomputation under p2c's own canonicalization, p2c v0.2 schema validation 0 errors, test re-execution), with the corrections above applied and receiver annotations extended to `claim.statement` plus a logged `issued_at` anachronism. Import confers no promotion: the underlying GU result remains **exploration-tier, located-not-forced, one external Z/2 posit, five-method convergence explicitly typed as one dependence-driven unit** — and the GU-sign-to-TaF-polarity identification remains **OPEN** per ADAPTER2-01, exactly as the report's annotations state.

Key files verified: `../gu-formalization/packets/GU-001-grading-sign-barb-v0.2.json`, `../gu-formalization/explorations/time-as-finality-crosswalk/adapter2-correction-polarity-fiber-not-axis-2026-07-15.md`, `./governance/CHARTER.md`, `./packets/schema/frozen-packet-v0.2.schema.json`, `./tests/validate_frozen_packet_v0_2_contract.py`.