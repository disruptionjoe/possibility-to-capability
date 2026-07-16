---
artifact_type: exploration
status: frozen_record
created: 2026-07-16
constitutional: false
work_item: P2C-CROSS-REPO-ADJUDICATION
tier: provisional_synthesis
governing_referee_report: REFEREE-REPORT.md (in this directory; GOVERNS — read before citing)
---

# Combining adjudication: what witness P2C-W1 establishes given the TAF-002 and TI-WFA-001 sovereign returns

**This is a provisional synthesis at exploration tier. Nothing here is canon;
nothing is `proved` or `resolved`; source claim status moves nowhere. The
referee report in this directory governs.**

## 0. Activation and inputs (all frozen, all verified)

The gated portfolio item `P2C-CROSS-REPO-ADJUDICATION` activated: two sovereign
frozen returns now exist for the SAME frozen witness.

| object | owner | pin | receiver verification |
|---|---|---|---|
| Witness `P2C-W1` (superconducting ring) | possibility-to-capability | freeze commit `4c9c28bb`, 4-blob sha256 manifest in `witness.json` | blobs re-hashed; discriminator re-run exit 0, stdout matches frozen output |
| `TAF-002` capability adjudication | time-as-finality | `source.revision 0749ce51`, issuance `e0b5773d`, bundle digest `0237f93b...` | full gate run PASS; imported at `packets/imports/TAF-002/` (P2C commit 6ff1faa) |
| `TI-WFA-001` whole-family legitimacy adjudication | temporal-issuance | `source.revision a336132d`, issuance `7db52289`, TI manifest digest `2190631f...` | full gate run PASS with one named schema deviation adjudicated in the import record; imported at `packets/imports/TI-WFA-001/` (P2C commit 6ff1faa) |

Same-frozen-witness rule (portfolio `handoffs.return_activation`): both returns
pin the identical P2C-W1 manifest, byte for byte. Verified executably
(`gate_verify.py` in this directory, all required checks PASS). The returns are
therefore combinable in principle; whether they combine in substance is the
question of this record.

## 1. Construction identity: do the two returns compose or diverge?

They adjudicate the same witness under two different, explicitly declared
scopes. The determination is that the scopes **compose at a typed seam**, and
the seam is verified rather than assumed:

- **TaF is frame-taking.** TAF-002 models the witness's declared R-D1 frame
  (budget-matched counterfactual pair) as two region-indexed T583 contexts and
  adjudicates capability INSIDE that frame. Its Clause 3 declares the
  one-context whole-family reading not adjudicable by TaF's standards and names
  it as an open fork (`construction_forks[1]`, "context individuation of the
  pair", `transfer_status: source_only`).
- **TI is conclusion-class-scoped.** TI-WFA-001 adjudicates exactly that open
  fork's completion move — admitting the target phase into the fixed family —
  under CompletionClass v1, and returns its legitimacy and its earned
  conclusion class.
- **The seam is the same object in all three fixtures.** The witness's `k2` /
  `k2-fail` (absorption caused specifically by admitting the target phase),
  TaF's `c9`/`c10` (one-context declaration absorbs; same move without the
  target phase absorbs nothing), and TI's `e1`/`e2`/`e2-fail` (whole_family
  with the S phase reproduces the (Q,I,P) signature; cap load-bearing) are
  mirrored implementations of one move. TaF stops exactly where TI starts.
- **The operational claim is indexed to the same frame in both returns.**
  TaF Clause 1 affirms the achievability delta in the declared pair; TI's F-3
  states the untouched residue as "realize the task from the N frame at matched
  budget" — the same declared pair, mirroring the witness's `k1`.

No divergence was found: neither return contradicts, reinterprets, or reframes
the other's scope, and each explicitly disclaims the other's question (TAF-002
nonclaims; TI-WFA-001 nonclaims). **Construction identity holds at the seam;
the returns compose.**

## 2. The one-chain joint argument

Per the No-Artificial-Success Rule, a joint conclusion exists only if ONE
explicit argument satisfies the whole gate chain. Here is that argument; every
leg is a frozen executable or frozen sovereign verdict on the same witness,
and the receiver's own moves are named as conditions C1-C4 (section 4).

Let **A** be the witness's capability claim: *in the declared budget-matched
counterfactual pair (frame R-D1), the task tau — hold a quantized, locally
invariant, zero-maintenance persistent memory — is realizable in the S branch
and not realizable in the N branch at any budget.* A is an operational/
context-class claim, frame-indexed per Hierarchy v0.2 section 2.5.

1. **Formation.** The joint object is {P2C-W1, TAF-002, TI-WFA-001} pinned to
   one manifest. Both sovereigns verified and adjudicated the unchanged bundle.
   Source meanings are preserved: TaF's statements are consumed in TaF
   vocabulary, TI's in CompletionClass v1 vocabulary; the receiver adds exactly
   two typed moves (the C1 task-semantics mapping and the C2 consumption of
   v1 as the routed legitimacy standard), both named, neither silent.
   **Formation gate: PASS.**
2. **Completion — local legs (P2C-owned).** Nine local completion classes
   (resource, seed/boundary, access, history, hidden-state, provenance,
   relabeling, gauge, whole-family-without-target-phase) each fail at least one
   of the (Q,I,P) signatures (`k1`, [E]; D-Q/D-I backed by literature-grade real
   experiments). The unique surviving absorber is whole-family WITH the target
   phase (`k2`, with `k2-fail` showing the absorption is caused specifically by
   the admission).
3. **Capability leg (TaF-owned, frame-indexed).** TAF-002 Clause 1: the
   achievability delta (1,1,1) vs (0,0,0) over (tau_Q, tau_I, tau_P) survives
   TaF's admissible reformulations (T584 representation/gauge/coarse-graining)
   and its fail-closed controls: access enlargement (`c1`), resource
   enlargement x10^6 (`c2`), hidden state (`c3`). Clause 2: the carrier is
   record-formation/erasure structure, and that factoring is non-deflationary
   in TaF semantics. Under the C1 mapping this instantiates the hierarchy's
   Capability type: a change in what is realizable, not in representation,
   access, or description.
4. **Completion — the surviving absorber (TI-owned, class-capped).** TI-WFA-001:
   admitting the S phase is a LEGITIMATE whole_family completion earning
   `GLOBAL_ONTOLOGICAL_ABSORPTION` only. The conclusion-class firewall is
   load-bearing (removing it operationally absorbs even the null phase,
   emptying the operational positive class — `e2-fail`), is closed under v1's
   declared compositions, and no operational or physical witness reproduces tau
   from the N frame at matched budget (`e3`, TI's mirror of `k1`).
5. **The join.** Combining 2-4: **each declared completion class, taken
   singly, either fails on measurable signatures (step 2, P2C-owned grade) or,
   in its sole surviving form, earns a conclusion class disjoint from A's
   class (step 4, TI-owned, v1-relative).** Therefore A survives every
   declared completion class singly plus the capped whole-family absorber at
   operational strength, while the witness is simultaneously and legitimately
   absorbed at global/ontological strength (no absolute semantic/metaphysical
   novelty claim survives — superconductivity is a broken-symmetry phase of a
   known Hamiltonian). Referee correction D2: **compositions of local
   completion classes were never tested** (`k1` scores classes singly; TI's
   closure statement covers only the cap); a composite local absorber remains
   an untested escape route. The two verdicts do not contradict: they are
   class-indexed, and the class split is itself frozen sovereign contract (TI)
   plus frozen sovereign boundary (TaF Clause 3), not receiver convenience.
   **Completion/null gate: PASS, scoped and conditional (C2, C4, D2 gap).**
6. **Capability gate: PASS**, frame-indexed (step 3, condition C1), with the
   tau_P metastability rider carried (C3): persistence is affirmed only up to
   the literature cap; the carriers surviving at every horizon and budget are
   tau_Q and tau_I.
7. **Finality gate: NOT REACHED.** No finality-level claim is made by the
   witness or either return. TAF-002's strict-finalization observation is
   intra-context and expressly consequence-free. The joint conclusion asserts
   nothing at the hierarchy's finality level. (Under "finality-if-reached"
   this leg is vacuously satisfied; it is recorded as NOT_REACHED, not PASS.)
8. **Neutrality gate: PASS.** Branch-label invariance is exercised with
   demonstrated failing directions in the witness (`n1`/`n1-fail`) and TAF-002
   (`c7`/`c8`); TI's verdict is structurally both-and (legitimacy affirmed AND
   restriction affirmed), favoring neither the witness surviving nor the
   absorber winning. The joint conclusion cuts against the hierarchy's
   "hoped-for" reading in two places: the ontological-absorption leg is
   AFFIRMED against the witness, and no enlargement-simpliciter verdict is
   issued. Descriptive note (referee correction D3): neither sovereign was
   sent a desired verdict and neither saw the other's return, and both
   returned "your dichotomy is false" shapes — but the two shapes are
   correlated through the shared witness bundle (including its framing prose)
   and are NOT counted as independent convergence evidence.
9. **No-Artificial-Success.** One chain, steps 1-8, one witness, one frame.
   The operational survival borrows no strength from the ontological
   absorption or vice versa; the split is preserved as first-class. Method
   counts are not independence counts: TI's `e3` mirrors the witness's `k1`
   (shared structure, not an independent method), and all fixtures are
   formal-only. **PASS.**

## 3. The combined verdict (exact scope and grade)

**SCOPED SURVIVOR, CLASS-SPLIT** — at exploration tier, provisional synthesis,
formal-only fixtures over literature-grade stipulated physics, conditions
C1-C4 binding:

> In the declared budget-matched counterfactual-pair construction, the frozen
> witness P2C-W1 establishes at the hierarchy's Capability level a
> **frame-indexed capability change** that survives every declared completion
> class taken singly — including the previously undischarged fixed-family
> absorber, whose legitimate strength is capped at global/ontological, a
> conclusion class disjoint from the operational claim — while the SAME witness
> is simultaneously and **legitimately absorbed at global/ontological
> strength** (no absolute-novelty claim survives). Compositions of local
> completion classes remain untested (referee D2).

Receiver disposition update for the witness (P2C-owned bookkeeping, no source
status moved):

- from `SURVIVES_LOCAL_COMPLETIONS / UNDISCHARGED_VS_WHOLE_FAMILY`
- to `SURVIVES_DECLARED_COMPLETION_FAMILY_AT_OPERATIONAL_CLASS /
  ABSORBED_AT_GLOBAL_ONTOLOGICAL_CLASS` (frame-indexed; conditional C1-C4).

What this does for the hard core (stated carefully): this is the first real
physical case on which the hierarchy's disclosure-vs-capability-change
discrimination was pressed to its pre-declared kill vector and **did not
collapse** — it resolved into two non-contradictory, class-indexed verdicts
issued by two sovereigns who were asked no leading question. That is evidence
the discrimination is *diagnosable* on real cases, at exploration tier. It is
not proof of the hierarchy, not a canon claim, and not an
enlargement-simpliciter verdict. The most informative single sentence: **the
fixed-family absorber is universally available but nowhere free** — invoking
it either changes the frame (an unmatched comparison, TaF Clause 3 / T583) or
caps the conclusion below the capability class (TI's firewall).

## 4. Conditions and what remains OPEN (binding on any citation)

- **C1 — task-semantics mapping (untested transfer).** TaF affirms capability
  change in its native semantics (achievability = reconstructibility). The
  identification with P2C's Capability type follows the witness's own section-1
  mapping, at definitional-draft grade. A different task semantics could
  decouple the legs. OPEN: test the mapping (a Track-2 candidate).
- **C2 — legitimacy-standard relativity.** The conclusion-class cap is
  CompletionClass v1's frozen contract. P2C routed the legitimacy question to
  TI, so consuming v1 is per the witness's own interface — but P2C has NOT yet
  built or adopted its own legitimate completion class. A rival standard
  without a class firewall could reopen the absorption. This is now the
  sharpest live content of F1 and the direct target of
  `P2C-NULL-COMPLETION-CLOSURE`.
- **C3 — tau_P metastability rider.** Persistence is "effectively infinite
  (literature)", never "provably infinite"; the history leg is capped, not
  killed. Carriers at every horizon and budget: tau_Q, tau_I.
- **C4 — construction-fork discipline (Located-Is-Not-Forced).** The
  two-context individuation is DECLARED, not forced. The one-context
  whole-family individuation remains materially admissible; under it there is
  no pair and no frame-indexed claim to attack (TaF endorses neither
  individuation; TI's cap governs the completion move, not the choice of
  individuation). The combined verdict is relative to the declared
  counterfactual-pair construction. Per-construction transfer is UNTESTED
  (BCS-native, topological, one-context, and alternate-task-semantics
  reformulations; also Alternate C replication in an independent domain).
- **Scope of the completion tournament.** TI scored only the `whole_family`
  primitive — the unique survivor of the witness's local sweep — not a full
  eleven-primitive tournament with nonfactorization certificates. Composition
  closure is asserted by TI for the cap; a full tournament remains open.
- **D2 composition gap (referee, binding).** Compositions of LOCAL completion
  classes (e.g., seed + hidden-state + history) were never tested against
  (Q,I,P); `k1` scores classes singly. A composite local absorber is the
  strongest untested attack on the operational-survival leg.
- **Receipt-strength asymmetry (referee D5).** TI's native packet format lacks
  the v0.2 evidence-structure fields, so its premise/method dependency honesty
  is asserted in prose, not machine-checked; acceptable at exploration tier,
  recorded as a receipt-strength difference between the two imported legs.
- **Formal-only evidence.** All three fixtures are finite designed
  computations; the physics is stipulated at literature grade, not re-measured.
  D-Q/D-I correspond to real 1961 experiments; no new physical measurement
  backs this record.

## 5. F1 status (recorded exactly; falsifier bookkeeping is receiver-owned)

F1 (Hierarchy v0.2, section 5): *"the admissible class can always be
re-presented as a fixed completed family with changing access (the fixed-family
absorber wins everywhere): possibility collapses into access."*

**Status: LIVE, NARROWED — one branch conditionally discharged.**

- **Discharged branch (conditional on C2):** the fiat-trivialization reading —
  "admitting any realized phase empties the capability level by fiat" — is
  dissolved relative to CompletionClass v1: the fiat-absorber only ever earns
  the weakest, non-causal conclusion class, so the operational positive class
  is not emptied (TI-WFA-001 F-2, `e2`/`e2-fail`, load-bearing). TI itself
  marks the discharge as its contract's work, not a new add-on.
- **Live remainder:** (a) whether a P2C-owned legitimate completion class must
  and can carry an equivalent conclusion-class restriction non-circularly —
  if the restriction were ad hoc, F1 returns; (b) whether the absorber "wins
  everywhere" under legitimacy standards other than v1 and on other real
  witnesses; (c) the individuation fork (C4) — the re-presentation F1 names is
  universally AVAILABLE; what this record shows is that under the two frozen
  sovereign standards it is nowhere FREE. (d) General family-exhaustiveness
  remains an open v1 proof obligation (TI R-2).
- **TAF-002 contributed nothing to F1 in either direction** (its Clause 3,
  honored as a first-class non-answer).

**F5 watch note (referee D6, binding).** The combined verdict is permanently
frame-indexed (C4). That is consistent with Hierarchy v0.2's frame-as-parameter
design (section 2.5), but it is also the pattern falsifier F5 names: if
equally admissible frames keep yielding divergent diagnoses with no invariant
quotient across real cases, F5 fires and the Capability level is
construction-dependent. This case neither fires nor retires F5; it feeds the
watch. A cross-frame invariant quotient (or its provable absence) is the
discriminating target.

No edit is made to the frozen Hierarchy v0.2 draft; this record and the
portfolio carry the falsifier state.

## 6. Portfolio consequences (recorded in steward/research-portfolio.json)

1. `P2C-CROSS-REPO-ADJUDICATION`: success condition ("one unchanged witness
   survives the neutral formation, completion, capability, finality, and
   neutrality gates") is **MET at exploration tier in the scoped, class-split
   form**, with the finality gate NOT_REACHED (vacuous) and conditions C1-C4
   attached. Kill condition (pass assembled from different constructions/
   assumptions/partial results) checked by the governing referee pass and not
   triggered: one witness, one frame, one chain, splits preserved. Item →
   `RESOLVED_SCOPED_SURVIVOR`; re-arm condition: a new frozen witness with
   sovereign returns (e.g., Alternate C BEC replication) or a P2C-owned
   completion class ready for a second-standard re-adjudication.
2. `P2C-NULL-COMPLETION-CLOSURE` (rank 1) is now the F1 carrier and the next
   swing: build P2C's own legitimate completion class and adjudicate whether an
   equivalent conclusion-class firewall is derivable/necessary rather than
   stipulated — or produce the counterexample that reopens absorption.
3. `P2C-REAL-PHYSICAL-WITNESS`: disposition upgraded as in section 3;
   escalation paths (Alternate B gamma = log D; Alternate C BEC) unchanged and
   now better motivated as per-construction transfer tests (C4).

## 7. Files and receipts

- `gate_verify.py` + `gate_verify_output.txt` (this directory): Phase-1
  receiver verification harness and frozen log (all required checks PASS).
- `packets/imports/TAF-002/`, `packets/imports/TI-WFA-001/`: immutable imports
  with receiver import records (gate tables) beside content.
- `REFEREE-REPORT.md` (this directory): adversarial pass; GOVERNS this record.
- Mailbox messages archived with processing receipts in
  `CapacityOS/system/mailboxes/possibility-to-capability/archive/`.
