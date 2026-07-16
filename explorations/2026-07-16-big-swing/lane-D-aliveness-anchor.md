> Part of the 2026-07-16 P2C big swing (four adversarially-verified lanes). Exploration tier; no claim promotion; the attached referee report GOVERNS the grades — read it before citing the lane report.

All checks pass. Assembling the deliverable.

---

# P2C ranked item 4 — Observer-aliveness anchor hypothesis: formalization + neutrality gate

Tier: exploration. Grade: executable toy model + structural argument. No claim promotion; GU/TI/TaF remain sovereign; nothing here changes `bar(b)`, H59, Krein positivity, or physical-issuance status (all OPEN). Governed by ADAPTER2-01 (the sign is a Z/2 fiber over the finality profile, not the finality-axis direction); nothing below contradicts it.

## 1. Formal statement (steelman)

**Setting.** Let `(R, ≤)` be the record poset (states = consistent finite literal sets over propositions `P`, ordered by extension, as in TI's surviving `SourceRealization = (C, ≤_S, Ext_S)` and the ADAPTER2-01 finite model). The sign datum is a point of the two-element torsor `T ≅ Z/2` sitting as a fiber over each proposition's slot in the profile: the global flip `g : (p, ε) ↦ (p, −ε)` acts on everything and exchanges the two admissible anchors.

**Observers and aliveness.** An observer `o` is a chain `c_o : t ↦ S_t` in `(R, ≤)` (its issued-record history), monotone under inclusion. At reference time `t₀`:

- `Live(o, t₀)` iff `o`'s chain strictly extends after `t₀` (it keeps issuing records: `S_{t} ⊊ S_{t'}` for some `t' > t ≥ t₀`);
- `Dead(o, t₀)` iff its chain is frozen from some `t ≤ t₀` on (its slice has gone dark).

**Selection rule A (the hypothesis, strongest form).** Let `L_live(t₀) = ⋃ { literals issued after t₀ by observers live at t₀ }`. If `L_live(t₀)` is Harary-balanced (the live slice is mutually consistent — the surviving hard-core predicate), define

```
A(M, t₀) : p ↦ the sign ε with (p, ε) ∈ L_live(t₀),
```

and declare the physical (positive-norm) anchor of `T` to be the one aligned with `A`: **the positive-norm branch is the branch whose records are still being extended by live observers; the opposite-polarity branch's observer slices are terminal.** In fork terms: given `{(p,+1)}` vs `{(p,−1)}`, select the branch above which the issuance dynamics is still realizing extensions.

This is the strongest honest version: it is stated on the source-side extension order (not on readout profiles), it uses only the surviving balance predicate as its well-definedness condition, and it invokes a genuinely dynamical distinction (still-extending vs frozen) rather than a static label.

## 2. Neutrality gate (charter gate 8) — executable test

Model: scripted observers (issuance chains with stop times) over propositions `{p, q, r}`; three model families (the hypothesis's own intended scenario — live carrier of `+`, dead carrier of `−`; a multi-live-observer variant; a variant with live observers on the `−` labels); global flip `g`; plus two controls (order-reversal, and a rigged sign-referencing law).

Script: `C:\Users\joe\AppData\Local\Temp\claude\C--Users-joe-JB\38a54106-9cc3-428a-92e4-2bb753410f40\scratchpad\aliveness_neutrality_test.py` (scratchpad is ephemeral; full source below for reproducibility).

```python
"""P2C ranked item 4: neutrality test for the observer-aliveness anchor hypothesis.

Formalized selection rule A: given a record poset with issuance dynamics and an
aliveness predicate, A returns the torsor point (sign assignment) carried by the
literals that live observers are still issuing.

Charter gate 8 (Neutrality): globally relabel + <-> - everywhere; if the rule's
output simply flips with the labels (equivariance), it relabels rather than
selects, and fails neutrality.

Pure Python. Exit 0 means every check matches its expected value.
"""

from __future__ import annotations
from dataclasses import dataclass

Literal = tuple[str, int]
State = frozenset


def consistent(state: State) -> bool:
    values: dict[str, int] = {}
    for prop, sign in state:
        if sign not in (-1, 1):
            return False
        if prop in values and values[prop] != sign:
            return False
        values[prop] = sign
    return True


def flip_literal(lit: Literal) -> Literal:
    prop, sign = lit
    return (prop, -sign)


@dataclass(frozen=True)
class Observer:
    """script: literals issued in order; stop: step after which it goes dark."""
    name: str
    script: tuple[Literal, ...]
    stop: int

    def history(self, t: int) -> State:
        return frozenset(self.script[: min(t, self.stop)])

    def live(self, t: int) -> bool:
        return self.stop > t and len(self.script) > t

    def issued_after(self, t: int) -> frozenset:
        return frozenset(self.script[t : self.stop])


@dataclass(frozen=True)
class Model:
    observers: tuple[Observer, ...]
    horizon: int


def flip_model(m: Model) -> Model:
    return Model(
        tuple(Observer(o.name, tuple(flip_literal(l) for l in o.script), o.stop)
              for o in m.observers),
        m.horizon,
    )


def aliveness_rule(m: Model, t0: int):
    """Sign assignment aligned with continued participation, or None if the
    live slice is unbalanced (rule undefined)."""
    live_literals: set[Literal] = set()
    for o in m.observers:
        if o.live(t0):
            live_literals |= o.issued_after(t0)
    if not consistent(frozenset(live_literals)):
        return None
    return {prop: sign for prop, sign in live_literals}


def flip_selection(sel):
    if sel is None:
        return None
    return {prop: -sign for prop, sign in sel.items()}


def structural_fingerprint(m: Model, t0: int):
    """Everything label-free: aliveness statuses, chain lengths, pairwise
    conflict pattern, live-slice balance."""
    alive = tuple(o.live(t0) for o in m.observers)
    lengths = tuple(len(o.history(m.horizon)) for o in m.observers)
    conflicts = tuple(
        not consistent(a.history(m.horizon) | b.history(m.horizon))
        for i, a in enumerate(m.observers) for b in m.observers[i + 1 :]
    )
    balanced_live = aliveness_rule(m, t0) is not None
    return (alive, lengths, conflicts, balanced_live)


def is_admissible_issuance(chain: tuple[State, ...]) -> bool:
    """Issuance dynamics: records only accumulate (past-fixed, future-open)."""
    return all(a.issubset(b) and consistent(b) for a, b in zip(chain, chain[1:])) \
        and all(consistent(s) for s in chain)


def observer_chain(o: Observer, horizon: int) -> tuple[State, ...]:
    return tuple(o.history(t) for t in range(horizon + 1))


def build_models():
    models = []
    # M1: the hypothesis's own intended scenario.
    models.append(("M1_intended_scenario", Model((
        Observer("alice_live", (("p", 1), ("q", 1), ("r", 1)), stop=99),
        Observer("bob_dead", (("p", -1),), stop=1)), 3), 1))
    # M2: two live agreeing observers, one dead dissenter.
    models.append(("M2_multi_live", Model((
        Observer("a", (("p", 1), ("q", -1), ("r", 1)), stop=99),
        Observer("b", (("q", -1), ("r", 1)), stop=99),
        Observer("c_dead", (("p", -1), ("q", 1)), stop=1)), 3), 1))
    # M3: live observers carry the '-' labels.
    models.append(("M3_live_on_minus", Model((
        Observer("a", (("p", -1), ("q", -1), ("r", -1)), stop=99),
        Observer("b_dead", (("p", 1),), stop=1)), 3), 1))
    return models


def main() -> None:
    models = build_models()
    checks: dict[str, bool] = {}

    # 1. Global flip is an automorphism: same physics, relabeled.
    checks["flip_is_model_automorphism"] = all(
        structural_fingerprint(m, t0) == structural_fingerprint(flip_model(m), t0)
        for _, m, t0 in models)

    # 2. Neutrality gate: A(flip(M)) == flip(A(M)) means the output co-varies
    #    with the labels — the rule reads the label off the live branch.
    checks["rule_is_flip_equivariant"] = all(
        aliveness_rule(flip_model(m), t0) == flip_selection(aliveness_rule(m, t0))
        for _, m, t0 in models)

    # A rule that PASSES would need a flip-INVARIANT defined output somewhere.
    checks["invariant_selection_exists"] = any(
        aliveness_rule(m, t0) is not None
        and aliveness_rule(flip_model(m), t0) == aliveness_rule(m, t0)
        and flip_model(m) != m
        for _, m, t0 in models)

    # 3. Flip-invariant residue: the balance predicate only.
    checks["live_slice_balance_is_flip_invariant"] = all(
        (aliveness_rule(m, t0) is None) == (aliveness_rule(flip_model(m), t0) is None)
        for _, m, t0 in models)

    # 4. Escape hatch: aliveness names a REAL label-independent asymmetry,
    #    but of the ORDER direction, not the sign fiber. Sign flip commutes
    #    with issuance; time reversal breaks it.
    checks["issuance_direction_is_flip_invariant"] = (
        all(is_admissible_issuance(observer_chain(o, m.horizon))
            for _, m, _ in models for o in m.observers)
        and all(is_admissible_issuance(observer_chain(o, m.horizon))
                for _, m, _ in models for o in flip_model(m).observers))
    checks["issuance_direction_breaks_time_reversal"] = all(
        not is_admissible_issuance(tuple(reversed(observer_chain(o, m.horizon))))
        for _, m, _ in models for o in m.observers
        if len(o.history(m.horizon)) >= 1)

    # 5. Circularity control: a law "only sign-s carriers survive" makes the
    #    rule pick s, but the flipped model is the mirror law picking -s:
    #    equivariant across the class; the asymmetry was inserted, not derived.
    def rigged(sign: int) -> Model:
        return Model((Observer("s", (("p", sign), ("q", sign)), stop=99),
                      Observer("d", (("p", -sign),), stop=1)), 3)

    rig_plus, rig_minus = rigged(1), rigged(-1)
    checks["rigged_law_still_equivariant_across_class"] = (
        aliveness_rule(rig_plus, 1) == {"q": 1}
        and aliveness_rule(rig_minus, 1) == {"q": -1}
        and flip_model(rig_plus).observers == rig_minus.observers)

    expected = {
        "flip_is_model_automorphism": True,
        "rule_is_flip_equivariant": True,
        "invariant_selection_exists": False,
        "live_slice_balance_is_flip_invariant": True,
        "issuance_direction_is_flip_invariant": True,
        "issuance_direction_breaks_time_reversal": True,
        "rigged_law_still_equivariant_across_class": True,
    }
    assert checks == expected, (checks, expected)

    print("ALIVENESS-ANCHOR NEUTRALITY TEST (charter gate 8)")
    print("=" * 72)
    for name, value in checks.items():
        print(f"PASS  {name}: {value}")
    print()
    print("PER-MODEL SELECTIONS (rule output under both labelings)")
    for name, m, t0 in models:
        a = aliveness_rule(m, t0)
        b = aliveness_rule(flip_model(m), t0)
        print(f"  {name}: A(M)={a}  A(flip M)={b}  equivariant={b == flip_selection(a)}")


if __name__ == "__main__":
    main()
```

**Output (verbatim, exit 0):**

```
ALIVENESS-ANCHOR NEUTRALITY TEST (charter gate 8)
========================================================================
PASS  flip_is_model_automorphism: True
PASS  rule_is_flip_equivariant: True
PASS  invariant_selection_exists: False
PASS  live_slice_balance_is_flip_invariant: True
PASS  issuance_direction_is_flip_invariant: True
PASS  issuance_direction_breaks_time_reversal: True
PASS  rigged_law_still_equivariant_across_class: True

PER-MODEL SELECTIONS (rule output under both labelings)
  M1_intended_scenario: A(M)={'r': 1, 'q': 1}  A(flip M)={'q': -1, 'r': -1}  equivariant=True
  M2_multi_live: A(M)={'r': 1, 'q': -1}  A(flip M)={'r': -1, 'q': 1}  equivariant=True
  M3_live_on_minus: A(M)={'q': -1, 'r': -1}  A(flip M)={'r': 1, 'q': 1}  equivariant=True
```

**Reading.** The global flip is an automorphism of the model (identical aliveness statuses, chain lengths, conflict patterns, balance — check 1), so both labelings are the same physics. On that same physics the rule's output flips with the labels in every model, including the hypothesis's own intended scenario M1 (check 2), and no flip-invariant defined selection exists anywhere in the class (check 3). The rule reads the sign off whatever the live branch happens to carry; it does not select a branch for a label-independent reason. The rigged control (check 5) closes the obvious repair: postulating a law "only `+` carriers stay alive" makes the rule output `+`, but that law's global flip is the mirror law, equally admissible, and the class-level selection is still equivariant — the asymmetry was inserted as a posit, which is exactly the external datum (`bar(b)`-grade) the rule was supposed to derive.

## 3. Verdict

**PARTIAL** — decomposed precisely:

- **The selection rule as stated FAILS-relabels.** As a selector of a point of the sign torsor, aliveness is flip-equivariant: it relabels, it does not select. In M1, "the live observer's sign" is `+` under one labeling and `−` under the other, for the identical physical situation. This is the same failure shape ADAPTER2-01 already carved out ("two globally flipped anchors; selecting one requires extra symmetry-breaking data"): aliveness, as formalized, supplies no such data.
- **But aliveness names a real, label-independent asymmetry** (checks 4): the extension direction. "New records still appear here" breaks time-reversal — a frozen/dead slice and a still-extending slice are structurally distinguishable without any sign label, and this survives the flip. That asymmetry is genuine and is not nothing.
- **The asymmetry lives on the base, not the fiber.** It is an asymmetry of the finality/extension order (future-open vs past-fixed), i.e. of the *base* of ADAPTER2-01's corrected picture (polarity fiber Z/2 over finality profile). Both fork branches `{(p,+1)}` and `{(p,−1)}` sit over the same profile and both admit continued extension; liveness does not differentiate the fiber points. Converting a base asymmetry into a fiber selection requires a transport/connection datum, and that is precisely what is missing. **The norm-link is OPEN.**

## 4. Steelman for the escape hatch (the strongest non-circular norm-link argument)

*Argument sketch (grade: informal, unproved):* In the Krein-space setting, probabilities are Born-rule frequencies. Frequencies exist only over outcomes that are actually being generated — i.e., over records still being issued. A negative-norm sector cannot support a frequency interpretation: its "probabilities" are negative or non-normalizable, so no ensemble of issued records can instantiate them. Therefore the sector on which issuance dynamics can continue indefinitely (live observers, stable record generation) is forced to be the positive-norm sector — not by labeling, but by a stability/interpretability condition: the issuance semigroup is realizable (contractive / probability-conserving) only on one sector of the Krein space. On this argument, aliveness is not reading a label; it is a *witness* of which sector supports realizable issuance, and "positive norm" is characterized operationally (frequencies of ongoing records exist) rather than conventionally.

The strongest version makes this a checkable mathematical condition: exhibit an issuance generator whose restriction to one Krein sector is dissipative/probability-conserving and to the other is not, with "the live sector" defined by that dynamical property alone.

*Weakest link:* the argument's load-bearing premise — "continued issuance requires positive norm" — is currently either (a) definitional, since standard quantum probability *defines* the physical sector as the positive one, in which case the argument is circular ("the physical branch is physical"); or (b) an unproved dynamical claim, since flipping the fundamental symmetry `J` exchanges which sector is "positive," and any sector-asymmetric property of the issuance semigroup must then be anchored to something else (energy positivity, spectral boundedness, an arrow already chosen) — pushing the selection to yet another external datum rather than deriving it from aliveness. TaF cannot currently supply that anchor: its T18 direction is graded conditional-constructor only, with T57 leaving arrow-direction circularity open (per ADAPTER2-01). Until someone exhibits a `J`-flip-robust, non-definitional characterization of "issuance-supporting sector," the norm-link is a posit wearing a dynamical costume.

## 5. Check against TI's own results (E160 / RUN-0019)

- **RUN-0019 (issuance-to-finality bridge):** TI demoted `kappa_i` (observer cadence), `G_ij`, and `Omega_ij` to **readout-side**; the source-side survivor is `SourceRealization = (C, ≤_S, Ext_S)`. "An observer that is still alive keeps issuing records" is a cadence/participation property of observers — it is `kappa_i`-shaped. On TI's own ledger, aliveness as stated is **observer-readout, not source-side**: different cadences changed apparent finality without changing source realization. To become source-side it would have to be recast as a property of `Ext_S` itself (e.g., "the extension set above this state is nonempty and realized") — but that property is polarity-symmetric in the fork (both branches extend), which reproduces the neutrality failure above.
- **E160 (holonomy transport-functor fixture):** TI's positive shape for nontrivial Z/2 transport requires an admissibility rule that is (i) **source-side** and (ii) carries a **composition-compatible parity label** on morphisms; a supplied transport table is extra data, not a derivation. Aliveness fails both prongs: it is readout-side per RUN-0019, and it is a unary predicate on observers with no edge labeling and no composition law at all. It is not even the right *type* of object to induce the needed transport. (This is the P2C-side reflection of open-belt obligations (2), (3), and (5).)

## 6. What would change the verdict

The hypothesis reopens as a live anchor candidate only if a construction supplies, jointly (aligned with the open belt, obligations 4–5, and E160's positive shape):

1. a source-side (not cadence/readout) formulation of "participation in finality" carrying a composition-compatible Z/2 label on extension morphisms;
2. a proof that the issuance dynamics is realizable (stable/probability-conserving) on exactly one Krein sector, characterized without reference to the sign convention or to `J` (i.e., robust under the global flip *including* the flip of `J`); and
3. a demonstration that this characterization is not a restatement of "physical = positive-norm" (the definitional circle).

Absent all three, the honest state is: **aliveness contributes to the base (a real future-open/past-fixed asymmetry of extension dynamics, already implicit in TaF's finality order) and contributes nothing to the fiber (the sign remains an unselected Z/2 posit).**

## 7. Honest bounds

Negative-leaning result, first-class under the Failure-Preservation Rule. Toy-model grade only: the executable test establishes flip-equivariance in a finite scripted-observer model, not a theorem about all possible aliveness formalizations; the steelman norm-link (Section 4, condition 2 of Section 6) is stated but untested and is the identified open door. No GU/TI/TaF claim moves. `bar(b)`, H59, Krein positivity, physical issuance: all remain OPEN at source grades. Located-Is-Not-Forced applies: this note locates *why* aliveness fails to force the sign (base/fiber mismatch + readout-side typing), which is itself the reusable content.

Sources consulted: `possibility-to-capability/governance/CHARTER.md`; `possibility-to-capability/explorations/2026-07-16-research-program-state-and-gate-1-milestone.md`; `gu-formalization/explorations/time-as-finality-crosswalk/adapter2-correction-polarity-fiber-not-axis-2026-07-15.md` + `adapter2_repair_audit.py`; `temporal-issuance/explorations/E160-holonomy-transport-functor-derivation-fixture-2026-07-10.md`; `temporal-issuance/FORMAL-DEFINITION-REPAIR.md` (RUN-0019 bridge verdict); `temporal-issuance/FORMAL-OBJECT.md`. Test script (rerunnable, exit 0): `C:\Users\joe\AppData\Local\Temp\claude\C--Users-joe-JB\38a54106-9cc3-428a-92e4-2bb753410f40\scratchpad\aliveness_neutrality_test.py` (full source embedded above; scratchpad is ephemeral, so the embedded copy is canonical).

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs grades)

# Referee report — LANE D-aliveness-anchor

## 1. VERDICT: SOUND-WITH-CORRECTIONS

The core negative result is correct and correctly not promoted: the aliveness selection rule, as formalized, is flip-equivariant (it relabels, it does not select), the asymmetry it names lives on the finality/extension base and not on the Z/2 fiber, and the norm-link stays OPEN. I re-ran the script (exit 0, output reproduced), re-derived the rigged control by hand (correct), and verified every source characterization against the actual files: RUN-0019's `kappa_i` → readout-side demotion and the `SourceRealization` survivor (`temporal-issuance/FORMAL-DEFINITION-REPAIR.md` lines 115, 123), E160's source-side + composition-compatible parity + "supplied transport table is extra data" requirements, the ranked-item-4 assignment, and full consistency with ADAPTER2-01's base/fiber picture and its T18/T57 caveats. No source-sovereignty violation; no claim moved. The defects below are grading and presentation errors, one of which is exactly the class that burned the program yesterday, but here it inflates the *rhetoric* of a negative result rather than manufacturing a positive one, so the conclusion survives.

## 2. Defects

**D1 — Tests that cannot fail, presented as model-sampled evidence. Severity: MODERATE (the burned class).**
Checks 1, 2, and 4 (`flip_is_model_automorphism`, `rule_is_flip_equivariant`, `issuance_direction_is_flip_invariant`) are theorems of the framework, not experiments. The rule and fingerprint are built exclusively from sign-symmetric primitives (`consistent`, cardinalities, liveness, set union), so equivariance holds identically for *every* model expressible in the framework. I confirmed this adversarially: **0 violations across 20,000 random models** (probe script: `C:\Users\joe\AppData\Local\Temp\claude\C--Users-joe-JB\38a54106-9cc3-428a-92e4-2bb753410f40\scratchpad\referee_probe.py`). The three "model families" contribute zero discriminating power to these checks; the outcome was fixed at formalization time, because the model contains no sign-referencing structure (no Krein norm, no `J`) that any rule *could* use to break the symmetry. The Section 2 "Reading" sells this as if M1/M2/M3 were informative samples ("in every model, including the hypothesis's own intended scenario M1"). The honest statement is stronger and cheaper: it is a two-line proof, and the script is its consistency certificate. The real untested content is Section 4's Krein-dynamical door — which the report does acknowledge as the open door, saving the verdict.

**D2 — Overclaimed quantifier on the invariant-selection check. Severity: MODERATE.**
"no flip-invariant defined selection exists anywhere in the class (check 3)" is false as implemented. The check quantifies over 3 hand-picked models, and the code's own criterion is satisfiable: an all-dead model yields `A(M) = {}`, which is not-None, flip-invariant, with `flip_model(M) != M` — probe 2 confirms it returns True. The check's False is an artifact of model choice plus a criterion that fails to require a nonempty selection. (The substantive point survives: an empty selection selects nothing, and nonempty flip-invariant output is impossible by the equivariance theorem — but that is not what the code tests.)

**D3 — The "intended scenario" never selects the fork proposition. Severity: MODERATE.**
In M1, `A(M) = {q:+1, r:+1}`; the fork proposition `p` is excluded because alice issued it before `t0` (probe 3 confirms). So the flagship demo of the hypothesis — "given `{(p,+1)}` vs `{(p,−1)}`, select the branch..." — never actually assigns a torsor point over the fork. Section 3's sentence "In M1, 'the live observer's sign' is `+` under one labeling and `−` under the other" is true of `q` and `r` only. The conclusion is unaffected (a full-history variant is equally equivariant), but the "strongest honest version" claim is dented: the executable demo does not exercise fork-branch selection.

**D4 — Torsor type mismatch vs ADAPTER2-01. Severity: MINOR.**
Section 1 declares a single two-element torsor `T ≅ Z/2` (matching ADAPTER2-01's one fiber over one common profile, and GU's single bit `bar(b)`), but the rule outputs a *per-proposition* sign map — a point of `(Z/2)^P`. M2's mixed output `{r:+1, q:−1}` is aligned with no single anchor of `T`, so "declare the physical anchor of `T` to be the one aligned with `A`" is undefined in exactly the multi-observer case the report introduces. Equivariance is unaffected; the formal statement doesn't type-check as written.

**D5 — Base asymmetry graded slightly above its evidence. Severity: MINOR.**
"aliveness names a real, label-independent asymmetry ... That asymmetry is genuine" — in the toy, monotone accumulation is posited by construction (`history` is monotone by fiat), not discovered; and physically, ADAPTER2-01 explicitly holds that TaF cannot currently supply a physical arrow (T18 conditional-constructor, T57 circularity open). The report cites those caveats in Section 4 but Section 3 states the base asymmetry unconditionally.

**D6 — "PARTIAL" headline verdict is generous. Severity: MINOR.**
The assigned question (milestone doc, gate 8 framing) is binary: "does aliveness genuinely break the +/− relabeling symmetry ... If it only relabels, it fails neutrality." At this grade the answer is: it only relabels — FAIL. The "partial" credit is (i) built into the model by assumption and (ii) already TaF/TI-owned content, as the report itself concedes ("already implicit in TaF's finality order"). PARTIAL is defensible only because the decomposition immediately follows; as a headline it grades above the evidence.

**D7 — Cosmetic. Severity: TRIVIAL.**
(a) "Output (verbatim, exit 0)": the on-disk script prints an extra VERDICT block absent from the embedded "canonical" copy, and per-model dict key order is nondeterministic across runs — "verbatim" is not strictly earned. (b) Opening line "All checks pass" is skimmable as "hypothesis passed" when passing means the hypothesis fails. (c) The Reading paragraph's "check 3" does not match the code comments' numbering.

## 3. Corrected wording

- **For D1** (replace "On that same physics the rule's output flips with the labels in every model, including the hypothesis's own intended scenario M1 (check 2), and no flip-invariant defined selection exists anywhere in the class (check 3)"):
  "Flip-equivariance of the rule is a theorem of the framework, not a sampled finding: the rule is defined solely from sign-symmetric primitives, so `A(flip M) = flip(A(M))` holds for every expressible model; the script verifies this identity on three representative models including the hypothesis's intended scenario. Consequently no rule definable from this model's data can produce a nonempty flip-invariant selection — breaking the symmetry would require sign-referencing structure (a norm, a `J`, an external posit) the model deliberately does not contain."
- **For D2**: "in none of the three test models does the rule produce a nonempty flip-invariant selection (and by the equivariance theorem, no nonempty one is possible; the empty-selection degenerate case is excluded as selecting nothing)."
- **For D5**: "aliveness names a label-independent asymmetry *of the model's posited extension order* (monotone issuance breaks time reversal); physically, that direction currently inherits TaF's conditional grade (T18 conditional-constructor, T57 circularity open, per ADAPTER2-01) and is assumed here, not derived."
- **For D6** (verdict line): "**FAILS-NEUTRALITY (at this formalization grade)** — the rule relabels rather than selects; the reusable content is the located diagnosis (base/fiber mismatch + readout-side typing per RUN-0019/E160); the Krein-dynamical norm-link (Section 4) is the one untested door and remains OPEN."

## 4. Grade the main result actually earns

**Toy-grade no-go with a located diagnosis, exploration tier, negative result, no promotion** — specifically: "the aliveness selection rule, formalized on TI's surviving source-side vocabulary with no sign-referencing structure, is provably flip-equivariant; the asymmetry aliveness names lives on the finality base, not the Z/2 fiber; converting it to a fiber selection requires transport data of the E160 shape, which aliveness (a unary, readout-side, cadence-typed predicate) cannot supply; the Krein-dynamical escape hatch is stated but untested." That is essentially the report's own Section 3/7 content, restated with the equivariance upgraded from "sampled in three models" to "framework theorem" (a stronger and more honest claim) and the headline downgraded from PARTIAL to FAILS-NEUTRALITY-with-located-diagnosis. It does *not* earn: a verdict on all aliveness formalizations, any claim about the physical arrow, or any movement on `bar(b)`, H59, Krein positivity, or physical issuance — and the report, to its credit, claims none of those.