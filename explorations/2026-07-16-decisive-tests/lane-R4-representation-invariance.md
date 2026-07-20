> Part of the 2026-07-16 decisive-tests swing (north-star lane; ranked program v0.1, ranks 1-4). Exploration tier; receiver updates only; the attached referee report GOVERNS — its corrected receiver update supersedes the lane headline.

# RANK 4 — Representation and Construction-Fork Invariance Challenge: Deliverable

**Grade: PROVISIONAL / PREPARATION** (Rank 4 prerequisites incomplete — see §3). Exploration tier throughout. No source-repo claim moves; bar(b), H59, Krein positivity, physical issuance remain OPEN; ADAPTER2-01 governs.

---

## 1. Classification of available evidence against Rank 4's outcome menu

### (a) Three-representation agreement (XOR-SAT / signed-graph 2-colouring / Z/2-cocycle, 720/720, `adapter_three_object.py`) — **SUPPORTS invariance, BOUNDED not VOIDED; preparation-grade only**

The load-bearing caveat ("agreement partly by construction of the shared encoding") **bounds** the representation-invariance reading rather than voiding it. What is genuinely evidential: three algorithmically distinct decision procedures (Gaussian elimination over GF(2), BFS 2-colouring, cocycle exactness) agree on one input — real algorithm-level invariance of the balance predicate, [E]-grade. What is by-construction and therefore NOT evidence for Rank 4's decisive question: the equivalence of the three **native source objects** (GU Gate-2a, TaF T39, TI encoding) was manufactured by the receiver's shared encoding, which is exactly the move the program forbids treating as source equivalence ("No receiver may declare two source constructions equivalent merely because that makes the diagnoses agree"). Verdict-class: contributes to "equivalent representations preserve diagnosis" **at encoding tier only**; cannot discharge the rank, because the equivalence tested was receiver-stipulated, not source-certified (Rank 4 prerequisite 3 unmet for this item).

### (b) GU-001 construction forks — **RETAINED CONSTRUCTION FORKS, correctly never averaged; one branch untested (open, not a disagreement)**

Verified against GR-001 and the import record: the receiver's construction gate (gate 2, PASS) retained both forks explicitly with transfer status — fork 1 (program-native vs standard-field; selected program-native; **transfers**) and fork 2 (derived-in-form vs posited-in-sign; selected posited-in-sign, RESIDUAL-BIT-STANDS; **does_not_transfer**) — and the one-chain control rode a **single** branch (`program-native`) through all 8 gates, with the no-artificial-success gate mechanically enforcing singleton branch identity. So: branches retained separately, never merged into the pass — the Construction-Fork Rule was honored. What Rank 4 still lacks from this item: no gate run exists **on the standard-field branch**, so cross-branch diagnosis agreement/disagreement is untested. Fork 2's `does_not_transfer` marks precisely where a cross-branch run would be expected to diverge — that would be a **principled** `CONSTRUCTION_FORK` retention, not a failure, but it is currently a prediction, not a result. Classification: retained fork, cross-branch comparison OPEN.

### (c) Binary-alphabet caveat on the T26 classification lemma (link 6) — **was a genuinely open representation-dependence RISK; now PARTIALLY BOUNDED by the new fixture (§2)**

Pre-fixture status: fixture-imposed representation choice on TaF's unconstrained string field — exactly a Rank 4 risk, with door 1 predicting the lemma's biconditional fails for |V| ≥ 3. Post-fixture (below): the risk **splits**. The lemma's biconditional is confirmed representation-dependent (it breaks at |V| = 3), but the diagnosis it carried survives the re-encoding. Residual openness: physically motivated alphabets, Z/3 (3-cycle) actions — which change the datum's group and are therefore a *different* frozen content, not an equivalent representation — and native-tier vocabularies.

### (d) No-go vocabulary-relativity (link 8, class stipulated) — **GENUINELY OPEN representation-dependence risk; the sharpest one; untouched by this rank's work**

The 36-symbol vocabulary class is a stipulated formalization of "finality/issuance-native"; the diagnosis under a materially different vocabulary is precisely Rank 4's question and no fixture here tests it (door 2 / 2a: finite-presentation gap). Classify as an open risk AND as a meta-level construction fork (vocabulary choice is a noncanonical construction choice) — retained, never averaged into the no-go's standing. Any future natural primitive failing the flip-automorphism battery is *characterized* (as carrying one Z/2 bit), not refuted; whether that is legitimate physics or the posit renamed is nature's question (Located-Is-Not-Forced).

---

## 2. New fixture: ternary-alphabet representation probe (door 1 × Rank 4)

**File:** `./tests/rank4_ternary_alphabet_representation_probe.py` (commit `5a21f3b`, pushed to main). Pure Python stdlib. Lints clean under `tef_check_tag_linter.py --strict` (registry mode, 0 violations, 0 advisories).

**Re-encoding tested:** same frozen fork content (one Z/2 fork between sign-labelled branches) re-encoded over V = {-1, 0, +1} with the flip embedded as the **transposition** (-1 ↔ +1), fixing 0. The three transpositions of V are conjugate under relabelling, so this is representative. A 3-cycle embedding is a declared nonclaim: not an involution, so it changes the datum's group Z/2 → Z/3 — different physical content, not an equivalent representation (the cyclic-orientation door stays a door).

**Diagnosis tested for stability:** "no label-free patch predicate can select the sign; sign selection requires a label-naming ingredient."

**Check discipline:** 15 checks — 3 [T] (listed separately, no evidential weight), 9 [E], 3 [F] (each firing through the same code path as the checker it protects: broken involution → `is_flip_even`; broken pattern extractor → `is_label_free`; non-selector control → `selects_sign`). Expectations pre-declared in `EXPECT`; algebra-forced [E]s disclosed inline as machine-verification.

**Output (run 2026-07-16, exit 0):**

```
RANK-4 TERNARY-ALPHABET REPRESENTATION PROBE
PASS  [T] setup_tau_is_involutive_bijection_of_V3 · setup_labelfree_implies_flipeven_k1
PASS  [T] setup_binary_sublemma_reproduced_k2  (binary: fe=4, lf=4, odd&free=0, even&naming=0)
PASS  [E] e1_k1_no_flipodd_labelfree_predicate            (8 predicates, odd&free=0)
PASS  [E] e2_k1_flipeven_but_labelnaming_predicates_exist (even&naming=2, e.g. "x0==0")
PASS  [E] e2b_k1_exemplar_x0_eq_zero_flipeven_and_labelnaming
PASS  [E] e3_k2_no_flipodd_labelfree_predicate            (512 predicates, odd&free=0)
PASS  [E] e3b_k2_labelfree_strictly_inside_flipeven       (lf=4 < fe=32; even&naming=28)
PASS  [E] e4_k2_patternclass_family_equals_bruteforce_labelfree
PASS  [E] e4b_k3_all_32_labelfree_predicates_are_flipeven (5 pattern classes, 2^5 exhaustive)
PASS  [E] e5_sign_selectors_are_flipodd_and_labelnaming   (all_plus, x0_plus, majority_sign)
PASS  [E] e6_pattern_class_splits_into_multiple_flip_orbits ({(-1,-1),(1,1)} vs {(0,0)})
PASS  [F] f1_broken_flip_misclassifies (fires) · f2_broken_pattern (fires) · f3_nonselector (fires)
EVIDENTIAL: 9 [E] + 3 [F] = 12; [T] excluded: 3. Exit 0.
```

**Finding (two-part, both first-class):**
1. **The LEMMA is representation-dependent — confirmed.** The binary biconditional {label-free} = {flip-even} **breaks** at |V| = 3: 2 of 4 flip-even k=1 predicates (28 of 32 at k=2) are label-naming (e.g. "x0 == 0" — invariant under the sign flip yet names the inert label). Mechanism exhibited: a single equality-pattern class splits into ≥ 2 flip orbits, which cannot happen over a binary alphabet. This confirms door 1's premise rather than the synthesis being wrong: link 6 already carried the caveat; the fixture converts the caveat from prose to a machine receipt.
2. **The DIAGNOSIS survives the re-encoding.** No flip-odd label-free predicate exists at k = 1, 2 (exhaustive over all 8 and 512 predicates) or among all 32 label-free predicates at k = 3 (exhaustive via pattern classes, cross-validated against brute force at k = 2); every exhibited sign selector is flip-odd AND label-naming. So "sign selection requires label-naming" is **stable** under this representation change — a genuine [E] outcome, since a diagnosis change would have been reported as a first-class REVISE_HIERARCHY signal (the fixture prints exactly that on any unexpected result; it did not fire).

Honest deflation, disclosed in the fixture: the surviving direction (label-free ⇒ flip-even) is algebra-forced once "label-free" means invariance under every uniform bijection of V (the flip is one such bijection). The evidential content is (i) the biconditional's confirmed break with its mechanism, and (ii) that the house definitions, code paths, and controls behave as predicted on the enlarged alphabet. Door 1 is **narrowed** (transposition-embedded flips over one enlarged alphabet), not closed: physically motivated alphabets and native-tier reruns remain its price.

---

## 3. Rank 4 receiver update

**Update: `REMAINS_UNDERDETERMINED` at rank level, issued PROVISIONALLY as preparation, with one bounded positive sub-finding and forks retained.** Not averaged into any pass.

**Why provisional (prerequisites audit against the program):**
- Prereq 1 (accepted real packet with two admissible constructions): **met** — GU-001, forks explicit in the frozen packet.
- Prereq 2 (frozen transformation maps, retained branch identifiers, predicted invariant/variant fields): **partially met** — branch identifiers retained (GR-001); the transformation maps exercised here (shared signed-graph encoding; ternary re-encoding) are receiver-constructed, not source-issued frozen maps.
- Prereq 3 (independent review that the transformation preserves the physical content relevant to the diagnosis): **not met** — no source owner has certified or contested physical equivalence of any representation pair; the receiver may not settle source equivalence by fiat.
- Serialization: Rank 2 and Rank 3 receiver verdicts have not been issued; per the sequence rule this output is graded **PREPARATION**, stated conditionally, and cannot satisfy the rank.

**Conditional content of the update:**
- *If* the transposition-embedded ternary re-encoding is accepted (by a source owner / independent reviewer) as an equivalent representation of the fork content, then the sub-finding is **"equivalent representation preserves diagnosis"** at toy/exhaustive-finite grade — favoring the candidate's representation-respecting ambition on this one transformation — while simultaneously registering a bounded, characterized representation dependence of the supporting *lemma* (biconditional binary-only). This is a lemma-scope correction, not a diagnosis change, so it does **not** trigger `REVISE_HIERARCHY`; the trigger condition (diagnosis change under an equivalent representation) was tested and did not fire.
- The three-representation 720/720 agreement contributes only encoding-tier support; its by-construction caveat is load-bearing and prevents promotion to rank-satisfying evidence (equivalence itself is receiver-stipulated → that leg is `REMAINS_UNDERDETERMINED` per the "equivalence is contested/unsettled" outcome).
- The no-go's vocabulary relativity (item d) is the dominant open Rank 4 risk and is untouched.

**Construction forks retained explicitly and separately (never averaged):**
1. **GU-001 fork 1** — program-native vs standard-field machinery; gate run executed on program-native only; standard-field branch diagnosis untested (transfers per packet, unexecuted by receiver).
2. **GU-001 fork 2** — derived-in-form vs posited-in-sign; `does_not_transfer`; RESIDUAL-BIT-STANDS; both sign branches live per the Construction-Fork Rule and GR-001's neutrality control (NO_BRANCH_SELECTED, label-invariant).
3. **Vocabulary-class fork (receiver-side, meta)** — the stipulated 36-symbol finality/issuance-native class vs unenumerated richer/native vocabularies (doors 2, 2a, 3).
4. **Alphabet fork (receiver-side, new, from this fixture)** — binary vs ternary-with-transposition representations now both machine-receipted with the same diagnosis; ternary-with-3-cycle explicitly excluded as different content (Z/3 ≠ Z/2), held as a separate door, not silently folded in.

**What would complete the rank:** (i) source-certified equivalence (or contest) of at least one representation pair with frozen transformation maps and predicted invariant/variant fields; (ii) a receiver gate run on the standard-field branch of GU-001 with cross-branch diagnosis comparison; (iii) a battery rerun over a second, independently defended vocabulary (door 2). Stop condition honored: no branch was dropped and both the favorable and the dependence-exposing findings are published together.

**Artifacts:** fixture `tests/rank4_ternary_alphabet_representation_probe.py` @ commit `5a21f3b` (exit 0; TEF-lint strict clean); evidence read from `packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json`, `GU-001-import-record-2026-07-16.md`, `synthesis/2026-07-16-bounded-fiber-theorem-v1.0.md`, `experiments/2026-07-14-ranked-decisive-test-program-v0.1.md`, `governance/CHARTER.md`.

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs; corrected receiver update supersedes)

# Referee Report — Lane R4-representation-invariance

## Re-execution record (all claims checked against artifacts)

- `tests/rank4_ternary_alphabet_representation_probe.py` re-run: **exit 0**, all 15 checks PASS. Every census number in the lane's output block verified against the live run (k=1: 8 preds, odd&free=0, even&naming=2; k=2: 512 preds, lf=4 < fe=32, ean=28; k=3: 5 classes, 32 label-free, all flip-even; binary anchor fe=lf=4; selectors and orbit-split as reported).
- `tef_check_tag_linter.py --strict`: registry mode, 15 checks, 0 violations, 0 advisories — as claimed.
- Commit `5a21f3b` exists, contains the fixture, is on `origin/main` — as claimed.
- `adapter_three_object.py` (gu-formalization) re-run: **exit 0**, 720/720 agreement, and it self-discloses "full native-object isomorphism is not tested" — the lane's item (a) framing matches the artifact.
- `GU-001-GR-001-gate-run-v0.1.json` verified: fork 1 (program-native, transfers) and fork 2 (posited-in-sign, does_not_transfer, RESIDUAL-BIT-STANDS) explicit; singleton branch identity mechanically enforced by `evaluate_gate_run.py`; NO_BRANCH_SELECTED before/after — item (b) claims match.
- No source-claim movement found; ADAPTER2-01 respected everywhere; forks never averaged; favorable and unfavorable findings published together.

## (1) VERDICT: **SOUND-WITH-CORRECTIONS**

The artifact layer survives full adversarial re-execution. The defects are in the classification/update layer: one banked sub-finding is vacuous by construction, and the rank-level vocabulary item is the wrong one.

## (2) Defects

**D1 — MAJOR (vacuous discrimination banked as conditional support).** The conditional sub-finding "equivalent representation preserves diagnosis... favoring the candidate's representation-respecting ambition" has **no live failure direction**. "Label-free" is defined as invariance under *every* uniform bijection of V; τ is such a bijection; therefore label-free ⇒ flip-even ⇒ no label-free sign selector is forced for **any** alphabet enlargement with the flip embedded as a bijection. The diagnosis could not have changed; the REVISE_HIERARCHY trigger "was tested and did not fire" is misleading — it could not fire absent a code bug. The lane's own "honest deflation" paragraph admits the forcing, then §3 banks the sub-finding anyway. A test that cannot produce the disconfirming menu outcome earns no menu-outcome-1 weight, conditional or not. *Corrected wording:* "The re-encoding demonstrates that bijection-embedded-flip transformations are definitionally non-discriminating for Rank 4 under the house label-free definition; a future Rank 4 test requires transformations under which the diagnosis is not invariant by construction. No conditional FAVORS-side weight is earned."

**D2 — MAJOR/MEDIUM (wrong vocabulary item).** The lane routes through "equivalence itself is contested → REMAINS_UNDERDETERMINED." Nothing is contested: prereq 3 (independent equivalence review) is simply **absent**, and prereq 2 is partial (receiver-constructed maps, not frozen source-issued ones). The program's vocabulary for an absent prerequisite is **BLOCKED** ("a prerequisite is absent; downstream judgments are not run"). Mitigation: the lane grades everything PROVISIONAL/PREPARATION and states it cannot satisfy the rank. *Corrected wording:* replace "REMAINS_UNDERDETERMINED at rank level, issued PROVISIONALLY" with "BLOCKED at rank level; preparation receipts logged below."

**D3 — MEDIUM ([T]-content inside the [E] headline).** e1, e3, e4b, and the load-bearing conjuncts of e5 (selector ⇒ flip-odd is definitional; flip-odd ⇒ label-naming follows from the forced direction) are theorem-consequences given the declared definitions — the same class as the fixture's own [T]s. Only e2/e2b/e3b/e4/e6 carry contingent content (the break, its counts, the shortcut cross-validation, the orbit-split mechanism). The headline "9 [E] + 3 [F] = 12" and the phrase "a genuine [E] outcome" for diagnosis-survival overstate; the fixture discloses forcing only at e1. *Corrected wording:* "5 contingent [E] + 4 machine-verification [E] (algebra-forced, disclosed) + 3 [F]; the diagnosis-survival direction is machine-verification of a definitional consequence, not discovery."

**D4 — MEDIUM (preregistration not artifact-backed).** "Expectations pre-declared in EXPECT" — EXPECT is same-file, same-commit, and derivable from the tags (`tag != "F"`); no two-phase commit exists. The program requires preregistration before outcomes are inspected, and the repo's own synthesis §4 concedes such process claims "are assertions, not mechanized receipts." *Corrected wording:* "Expectations are declared in-file at the fixture's single commit; no two-phase preregistration artifact exists (synthesis §4 caveat applies)."

**D5 — MINOR (non-verbatim transcript).** The "Output (run 2026-07-16, exit 0)" block is an edited condensation (merged lines, inline annotations, reworded summary line), not the program's output. Every number in it verified faithful on re-run, so this is presentation, not fabrication. *Correction:* label it "condensed; verbatim receipt reproducible via exit-0 re-run."

**D6 — MINOR (synthetic-to-real framing creep).** "Same frozen fork content... re-encoded" — the fixture re-encodes a toy surrogate (one abstract Z/2 fork over sign labels), not GU-001's native Krein objects. The §3 hedge ("if accepted by a source owner") partially covers this; the §2 framing should say "toy surrogate of the fork content."

**D7 — MINOR ("narrowed" overstates door 1 payment).** Door 1's stated price is "exhibit the alphabet's **physical meaning** and rerun the classification." The ternary alphabet is receiver-chosen with no physical meaning; the classification was rerun but the price is unpaid. *Corrected wording:* "receipted at one unphysical instance," not "narrowed."

**D8 — MINOR (serialization audit incomplete).** The lane states Ranks 2-3 verdicts are unissued but is silent on Rank 1's verdict status: GR-001 exists (8/8 PASS), yet Rank 1's prereq 5 (preregistration before gate-outcome inspection) is admitted absent per synthesis §4, so even "Prereq 1: met" should carry a condition.

**D9 — MINOR (grade qualifier dropped).** "GR-001's neutrality control (NO_BRANCH_SELECTED, label-invariant)" is cited without gate 8's own qualifier: recorded-metamorphic argument on sign-symmetric lemmas, **not** an executed label-swap re-run.

**D10 — MINOR (rival reading unassessed).** Rank 4's menu includes "one deeper constraint object collapses all forks → favors the constraint-first rival." The Harary-balance predicate underlying the 720/720 agreement is precisely a candidate deeper constraint object; the lane never runs this reading, even as an open note.

## (3) The receiver update the evidence ACTUALLY earns

**`BLOCKED` at Rank 4** (prereq 3 absent, prereq 2 partial, Ranks 2-3 receiver verdicts unissued per the serialization rule; Rank 1's own verdict status conditional on its missing preregistration artifact). Logged beneath the block, at preparation/exploration tier, unconditionally ownable by the receiver:

1. **Lemma-scope representation dependence machine-receipted:** the binary biconditional {label-free} = {flip-even} breaks at |V| = 3 (mechanism: pattern classes split into multiple flip orbits) — converts door 1's already-asserted strictness from prose to receipt. Lemma-tier characterization; no hierarchy-tier REVISE_HIERARCHY.
2. **A negative methodological result:** bijection-embedded-flip re-encodings are definitionally non-discriminating for Rank 4's decisive question under the house definitions; this transformation family must be excluded from (or redesigned for) any future Rank 4 test.
3. **Fork inventory** (items b, c, d and the four retained forks): correct and useful as preparation; the vocabulary-relativity risk (item d) correctly identified as dominant and untouched.

No FAVORS_CANDIDATE weight, conditional or otherwise. No REMAINS_UNDERDETERMINED issued, because the failure is prerequisite absence, not tested non-discrimination.

## (4) Stop conditions

**Respected.** Both the favorable (diagnosis-stable) and unfavorable (lemma-breaks) findings were published together; no branch was dropped or averaged; the 3-cycle/Z-3 case was excluded openly as a nonclaim rather than folded in; no source-receiver evidence blending; ADAPTER2-01 uncontradicted. The one stop-adjacent weakness is D4: the program's "before outcomes are inspected" preregistration discipline is asserted, not mechanized — a program-wide gap the repo has already self-reported, not a lane-specific concealment.