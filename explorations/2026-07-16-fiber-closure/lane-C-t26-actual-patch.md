> Part of the 2026-07-16 fiber-closure swing (2-prime adversarial twins + T26 + tooling). Exploration tier; no claim promotion; the attached referee report GOVERNS the grades — read it before citing the lane report.

Exit 0, all checks matched pre-declared expectations on the first run. The deliverable follows.

---

# CLOSING THE LAST HIDING PLACE: TaF's actual T26 `D1RestrictionSystem` patch/overlap machinery vs the global flip

> Exploration tier. No claim promotion. Nothing here reopens the withdrawn ADAPTER2-01 identity or moves any source-repo claim. `bar(b)`, H59, Krein positivity, physical issuance: **ALL REMAIN OPEN.** This executes ranked item 1 of the swing-2 SYNTHESIS (lane-2 referee defect F3: "T26's actual `D1RestrictionSystem` — one proposition value per site, optional overlap tests, finite patch constraints beyond pairwise — none modeled... the place a sign could still hide").

**Fixture:** `possibility-to-capability/tests/gate1_t26_actual_patch_machinery.py` — committed and pushed at `6ed76a5` on `main`. Pure Python, no dependencies beyond TaF's own repo, runtime ~3s, exit 0. Full source and output embedded below (§8, §9).

**Method upgrade over every prior lane:** instead of building a "faithful model" of T26, the fixture **imports and drives TaF's actual shipped code unmodified** (`time-as-finality/models/d1_restriction_system.py` — read in full before writing; every behavioral prediction below was made from the source reading and the run is the receipt). "Faithful to T26" is therefore not a modeling claim; it is T26.

**Pre-registration receipt (honesty):** the `EXPECT_TRUE` list, all Part-A counts, and all Part-B behavioral predictions were written into the fixture **before its first execution**. The first run passed 47/47 with zero mismatches. **No expectation was revised at any point.** (This is the receipt swing-2's F4 said was missing.)

---

## 1. What "label-free" means here — the definition that carries the result

For a k-site patch predicate `f` over the binary value alphabet `V = {-1,+1}` (V carries **no order and no distinguished element**):

- **Label-free:** `f(x)` depends only on the **equality pattern** of `x` — the partition of the k sites induced by `x_i == x_j`. Equivalently: `f` is invariant under **every** bijection of V applied uniformly to all sites. Anything else is **label-naming**: its definition consumes extra structure on V — a distinguished constant ("the value +1"), an order ("left ≤ right"), or any other device not invariant under relabeling.
- **Flip-even:** `f(-x) = f(x)` for all `x`; otherwise **flip-odd**.

This definition is deliberately *not* "flip-invariant" (which would make the dichotomy a tautology over a binary alphabet); it is the equality-pattern/relabeling definition, under which the coincidence with flip-evenness is a **theorem to be proved and machine-checked**, not a definition.

## 2. The Patch-Collapse Classification Theorem (the heart, answering "does any flip-odd label-free constraint exist?")

**Theorem.** Over the binary alphabet, at **every** arity k: {label-free constraints} = {flip-even constraints}, **exactly**. Hence flip-odd ⟺ label-naming. **No flip-odd, label-free patch constraint exists at any arity** — not for triples, not for parity-over-a-patch, not for anything.

**Proof.** (⊆) `pattern(x) = pattern(-x)` because `x_i = x_j ⟺ -x_i = -x_j`; so any pattern-definable `f` has `f(-x) = f(x)`. (⊇) Over a binary alphabet, an equality pattern with site-blocks `B₁, B₂` has exactly two realizations, `x` and `-x` (fix the value on one site; the pattern forces all others). So pattern classes **are** flip orbits, and any flip-even `f` (constant on flip orbits) factors through the pattern. ∎

**Machine verification [E, algebra-forced — disclosed]:** the fixture enumerates **all** predicates at k = 1, 2, 3, 4 (4 + 16 + 256 + 65,536 = 65,812 predicates) with independent `is_flip_even` / `is_label_free` checkers and finds the two classes **identical** at every arity, with counts matching the orbit formula `2^(2^(k-1))` — (2, 4, 16, 256) — and **zero** flip-odd label-free constraints. Grade: because the one-paragraph proof exists, this enumeration is a *machine verification of the proof*, not an independent discovery; it is tagged [E] only in the sense that a wrong proof would have been falsified by it. It is not counted as standalone evidence beyond that.

**Named exemplars, all classified as predicted [E]:** pairwise same/different → even+free; **triple parity `x₀x₁x₂ = +1` → odd+naming** (which parity? naming +1); **quad parity → even+free** (blocks of an even-size pattern have equal size-parity — the pattern determines it); not-all-equal-3 → even+free; majority-is-+1 → odd+naming; named-slot `x₀ = +1` → odd+naming; all-three-equal → even+free.

**Scope condition (disclosed):** the exactness is **binary-alphabet-specific** (for |V| ≥ 3 there is no canonical flip and label-free is strictly stronger than invariance under any one involution). Binary is the native case: TaF's own T39 establishes that the `D1RestrictionSystem` patch language *is* a binary {-1,1} CSP.

## 3. TaF's actual patch layer: the hiding place is not merely empty — it is **disconnected from the values**

Findings on the shipped code, each with an executable receipt:

**3.1 [E] `global_section` never dereferences proposition values.** T26's `RestrictionPatch` constrains **abstract patch variables**; `global_section` enumerates ±1 assignments to those variables and never touches `local_values`. Receipt: for a 3-site system with a two-patch constraint set, the full `GlobalSectionResult` is **identical across all 8 proposition-value assignments** (not merely flip-pairs — all of them). Predicted from source; confirmed exhaustively (`B1_E_*`). So in shipped T26, patch constraints *cannot* break the flip for the strongest possible reason: they are not wired to the fiber at all.

**3.2 [T] Corollary — the shipped patch language can only express flip-even constraints even under the charitable semantics.** T26's constraint atoms are exactly `PatchConstraint(left, right, "same"|"different")` — pairwise equality atoms. "Finite patch constraints beyond pairwise" **do not exist at atom level in shipped T26** (only conjunctions of pairwise atoms within a patch). Under the charitable/intended reading (patch variables = site polarities), every conjunction of equality atoms is equality-pattern-definable, hence label-free, hence flip-even by the theorem. Notably, **triple parity is not expressible** in the shipped language — consistent: it is flip-odd, and the language can only say label-free things. Part A covers every extension of the language to arbitrary arity anyway.

**3.3 [E] The actual `global_section` reproduces the (Z/2)^blocks structure.** Encoding per-site polarity variables with same-constraints along the constraint graph: connected chain → **2** global witnesses; partitioned → **4**; fully isolated → **8** — exactly `2^blocks`, on TaF's own code (`B2_E`), reproducing swing-2's N4 at actual-code grade. TaF's own `contextual_gluing_scenario` reproduces its obstruction (local witnesses = all patches, global witnesses = 0). **[F]** Same code path, deliberately broken: an odd `different`-cycle split across three individually-satisfiable patches → 3 local witnesses, 0 global, `obstruction_detected` — the section machinery has teeth (`B2_F`).

## 4. The overlap-test language: the ONLY flip-breaking primitives in all of T26, and they read the label

**4.1 [E] Exhaustive sweep of the entire shipped overlap language.** All 24 primitives — dimensions {`proposition_value`, `profile`, 4 D1 dims} × relations {`same`, `different`, `left_leq_right`, `left_geq_right`} — over **all** two-site value assignments, verdicts via the public `analyze_compatibility` path, heterogeneous profiles so profile tests are non-degenerate. Result (`B3_E`): the flip-sensitive set is **exactly** `{(proposition_value, left_leq_right), (proposition_value, left_geq_right)}`. Equality relations on values: flip-even (label-free — theorem instance). All profile-dimension tests: value-independent (profiles don't flip; T24 site labels — population/scale/time_step/trust_domain, all distinct in the fixture — don't flip either).

**4.2 The flip-odd primitives are label-naming, and not metaphorically.** In the shipped implementation, `left_leq_right` on `proposition_value` compares the **label strings themselves under Python string order** (`_overlap_test_passes`, d1_restriction_system.py lines 997–1000: `left_value <= right_value` on `str`). "The order smuggles the label" is literally the implementation: the test reads the label's spelling. Under §1's definition it is label-naming (an order on V is non-relabeling-invariant structure). **[T]** The flip conjugates `leq ↔ geq` (any total order on a 2-element set is reversed by swapping the elements) — verified but algebra-forced, no evidential weight. **[E]** `leq` and `geq` are **distinct, equally admissible** tests in the declared language (`B3_E_leq_and_geq_are_distinct_tests`): fixing either one is a labeling choice whose flip-conjugate is different and equally legal — the relabel-test failure, exhibited in TaF's own vocabulary. **[F]** The same sweep harness run with a broken single-site flip registers the equality relations as sensitive too (`B3_F`) — the sweep detects sensitivity when it exists; the null result for `same`/`different` under the true flip is earned, not harness blindness.

So the collapse-or-smuggle dichotomy holds **inside TaF's shipped code**: every value-touching primitive is either an equality atom (label-free, flip-even, fork-collapsing) or an order atom (flip-odd, label-reading, relabel-failing). There is no third kind.

## 5. Restriction morphisms — merges, splits, composites, and the holonomy worry

**5.1 [E] The shipped morphism analyzer is value-blind by omission.** `analyze_morphism` checks site-map totality, profile-dimension equality, trust-path preservation, and obstruction-status agreement — and **never reads `proposition_value`**. Receipts, exhaustive: all 16 identity-map (source-values × target-values) combos are `reached`, including `X → flip(X)` (`B4_E`); all 8 genuine merges (both source sites → one target site) are `reached` **including sources whose two sites carry opposite values** (the merge silently swallows a value conflict); all 8 splits and all 16 merge-then-split composites are `reached` regardless of values (`B5_E`). **Adjacent non-vacuity controls [E]:** the analyzer is not vacuously positive — a profile-mismatched merge fails (`local_profile_mismatch`), TaF's own `failed_transport_morphism` fails, TaF's own `positive_relabel_morphism` passes.

**5.2 The holonomy worry is closed by a dichotomy, not just by omission.** Can site maps that merge/split create sign-selecting structure absent in both endpoints? In shipped T26: **no, vacuously** — the morphism layer cannot see the fiber, so it cannot select in it (and `reached` is trivially flip-invariant over the whole mixed battery of 32 configs, 24 passing + 8 failing: `B6_E`, with the source-only-flip invariance explicitly labeled **VACUOUS** in the check name — it is a bounding fact about T26, not a symmetry theorem). But the fixture also answers the *upgraded* question: any value-sensitive extension of the morphism layer faces the Part-A dichotomy, demonstrated live on the actual objects:

- A **strict-transport analyzer** (actual analyzer + the equality atom "mapped value equals source value") is value-sensitive — it passes `X→X` and fails `X→flip(X)` — yet **remains full-flip invariant** over the whole battery (`B6_E_value_strict_analyzer_STILL_full_flip_invariant`): equality-atom transport is label-free, hence flip-even. A theorem instance running on shipped dataclasses.
- **[F5a]** The same invariance harness with the strict analyzer under **source-only** flip detects the break — the B6 invariance checks have teeth; the actual analyzer's invariance is a property of TaF's code, not harness blindness.
- **[F5b]** A **label-naming analyzer** ("reached only if every target value is `+1`") breaks even full-flip invariance through the same harness — the only exhibited way to make the morphism layer sign-selecting is to name a label.

**5.3 First-class bounding finding (Failure-Preservation).** T26 restriction morphisms perform **no value-transport check at all**: a merge of two sites carrying opposite proposition values into one site carrying either value is a fully `reached` morphism. The flip-neutrality of the morphism layer is real but *unearned* — it comes from not looking. Constructive corollary (mailbox-grade observation for TaF, no source edit made or proposed here): adding an equality-atom value-transport check would close the silent merge-conflict gap **and provably preserve flip-neutrality** (it is label-free, hence flip-even — demonstrated in 5.2). TaF can have value integrity without buying a sign.

## 6. Check ledger and controls

47 checks, all matching pre-declared expectations. By tag: **[T] 1** (`B3_T_flip_conjugates_leq_to_geq` — listed, labeled, zero evidential weight, not load-bearing anywhere). **[F] 7**, each exercising the *same code path* it protects, each fired: broken involution through `is_flip_even` (misclassifies a known flip-even constraint); broken pattern extractor through `is_label_free` (misclassifies a known label-free constraint); odd-cycle patches through the actual `global_section` (obstruction created); broken single-site flip through the same overlap sweep (equality relations register sensitive); strict analyzer under source-only flip through the same invariance harness (break detected); label-naming analyzer under full flip through the same harness (break detected); plus `B6_E_strict_analyzer_passes_XtoX_fails_XtoFlipX` establishing the harness sees value-sensitivity when an analyzer has it. **[E] 39**, of which the 12 Part-A enumeration checks and 8 exemplar checks are disclosed as algebra-forced given the §2 proof (graded as machine verification), and the Part-B checks are genuine experiments on an external artifact (TaF's shipped code), each predicted from a source reading with the run as receipt. Headline claims rest only on the theorem-plus-verification and the Part-B [E]s — never on the [T].

## 7. Honest bounds, named gaps, and verdict

**What this does NOT cover (named gaps):**
1. **T37 `TypedTransportNetwork`** was audited by source reading only (its fixture sets every `proposition_value` to `"true"` uniformly; path-dependent admissibility is driven by `forgotten_structure` declarations, which are value-independent) — but it was **not driven executably** here. It was also not part of F3's named hiding place (F3 named T26's machinery). Flagged as the adjacent next surface, expected-null by the same audit logic.
2. **Non-binary value alphabets:** the classification exactness is binary-specific (disclosed §2). T39 fixes binary as the native patch language; a future TaF move to richer alphabets would reopen the classification question in a changed form.
3. **All-systems generalization grade:** the Part-B exhaustive batteries cover 2–3-site systems, the full 24-primitive overlap language, and a 32-config morphism battery. The generalization to *all* systems ("`global_section` and `analyze_morphism` never read values") is **source-audit grade** — structural facts of the shipped code, exhibited executably on the batteries, not enumerated over all systems.
4. **The morphism layer's flip-invariance is vacuous** (by omission) — kept first-class as a bounding result, not spent as evidence of symmetry. The non-vacuous morphism-level content is the dichotomy demonstration (5.2), which has teeth on both arms.

**Charter compliance:** Located-Is-Not-Forced — the fiber is now located *through* TaF's entire T26 surface and nothing forces a branch; no anchor produced or implied. No-Artificial-Success — the strongest results here are negative/structural (value-decoupling; vacuous invariance; label-naming order relations), reported as such. Failure-Preservation — 3.1, 5.1/5.3, and the binary-scope condition are first-class. Neutrality — every "no sign-selection" claim is stated relative to §1's declared label-free criterion, which is the definition that carries the result.

**Consistency with the fiber picture:** everything extends, nothing reopens. The (Z/2)^blocks structure reproduces on TaF's own `global_section` (3.3); the collapse-or-smuggle dichotomy that lane-B/lane-2 found at toy and enriched-toy tier is now a **theorem** at the patch level (all arities, binary alphabet) and an **exhaustive inventory fact** at shipped-code level; lane 3's "every separator consumes the external bit" and lane D's base-vs-fiber diagnosis are untouched and corroborated in shape. `bar(b)`, H59, Krein positivity, physical issuance: all open; the anchor burden is unchanged (and per N4 still per-block).

### VERDICT: **HIDING-PLACE-CLOSED** (at the following stated grades)

1. **All-arity theorem grade (binary alphabet)** for patch constraints: under the declared equality-pattern definition of label-free, **flip-odd ⟺ label-naming, exactly** — proved (§2) and machine-verified exhaustively for every constraint on ≤4 sites (65,812 predicates, zero exceptions). No flip-odd label-free patch object exists to be discovered; the "discovery" branch of the tasking is closed by classification, not by failure to search.
2. **Shipped-code grade** for TaF's actual T26: patch constraints are value-decoupled (cannot touch the fiber); the shipped patch language can express only flip-even constraints even under charitable semantics; the **only** flip-breaking primitives in the entire object are the two order relations on `proposition_value`, which read the label string order and fail the relabel test as a leq/geq conjugate pair; restriction morphisms — including genuine merges, splits, and composites — are value-blind, and any value-sensitive upgrade is subject to the same dichotomy (label-free ⇒ flip-even, live-demonstrated; label-naming ⇒ flip-breaking, live-demonstrated).
3. **The flip is still an automorphism of everything T26 can say, and the fiber is still undetermined** — now with the strongest available reason at each layer: the patch layer by disconnection, the overlap layer by exhaustive inventory (equality atoms even; order atoms label-naming), the morphism layer by omission (bounding) plus dichotomy (non-vacuous).

Residual surfaces are the named gaps above (T37 executably, non-binary alphabets) — neither is part of the hiding place F3 named. The last hiding place inside T26 is closed.

## 8. Full fixture source

`possibility-to-capability/tests/gate1_t26_actual_patch_machinery.py` @ `6ed76a5`:

```python
"""P2C swing-3 fixture: TaF's ACTUAL T26 D1RestrictionSystem patch/overlap
machinery vs the global polarity flip — closing the last hiding place named by
the swing-2 lane-2 referee (defect F3).

Exploration tier. No claim promotion. Nothing here reopens the withdrawn
ADAPTER2-01 identity or moves any source-repo claim. bar(b), H59, Krein
positivity, physical issuance: ALL OPEN.

TWO PARTS:

PART A (self-contained): exhaustive classification of ALL finite patch
constraints over the binary +/-1 value alphabet at arities k = 1..4
(4 + 16 + 256 + 65536 predicates), under the declared definition:

  LABEL-FREE (the definition that carries the result): a k-site patch
  predicate f over the value alphabet V = {-1,+1} is label-free iff f(x)
  depends only on the EQUALITY PATTERN of x — the partition of sites induced
  by x_i == x_j — equivalently, iff f is invariant under every bijection of V
  applied uniformly to all sites. Anything else is LABEL-NAMING: its
  definition consumes extra structure on V (a distinguished constant, an
  order, or any other non-relabeling-invariant device).

  FLIP-EVEN: f(-x) == f(x) for all x. FLIP-ODD: not flip-even.

  PATCH-COLLAPSE CLASSIFICATION THEOREM (proved in prose in the lane report;
  machine-verified exhaustively here): over the binary alphabet, at every
  arity, {label-free} = {flip-even} EXACTLY. Hence flip-odd <=> label-naming:
  no flip-odd label-free patch constraint exists at ANY arity. Proof sketch:
  pattern(x) = pattern(-x) gives label-free => flip-even; over a binary
  alphabet an equality pattern has exactly two realizations {x, -x}, so
  pattern classes ARE flip orbits, giving flip-even => label-free.

PART B (drives TaF's actual shipped code): imports
time-as-finality/models/d1_restriction_system.py UNMODIFIED and adjudicates,
on the real objects (ObserverSite with T24 population/scale/time_step/
trust_domain labels; one proposition value per site; RestrictionPatch;
OverlapTest; D1RestrictionMorphism with site maps incl. merges/splits;
global_section / analyze_compatibility / analyze_morphism):

  B1  whether global_section is value-decoupled (patches constrain abstract
      variables, never dereferencing local proposition values),
  B2  whether the actual global_section reproduces the (Z/2)^blocks section
      structure under connected / partitioned / isolated patch constraint
      graphs, plus TaF's own contextual gluing obstruction,
  B3  an exhaustive sweep of the ENTIRE shipped overlap-test language
      (6 dimensions x 4 relations x all two-site value assignments):
      which (dimension, relation) pairs are flip-sensitive,
  B4  whether analyze_morphism is value-blind (exhaustive over identity
      site maps and all value combinations),
  B5  merges (2->1 site maps), splits (1->2), and merge-then-split
      composites: can any create sign-selecting structure? plus the
      adjacent controls showing the analyzer is NOT vacuously positive
      (profile mismatch fails; TaF's own failed transport morphism fails),
  B6  flip-invariance of the whole morphism layer over a mixed config
      battery (passing AND failing configs), under full flip and under
      source-only flip, for the actual analyzer, a value-strict analyzer,
      and a label-naming analyzer.

CHECK DISCIPLINE (house style, swing 2): every check is tagged
  [T] theorem-consequence — outcome fixed by construction/algebra; listed
      separately; carries NO evidential weight; never counted in a headline.
  [E] genuine experiment — outcome not fixed at formalization time by THIS
      fixture's construction. Part-B [E] checks are experiments on an
      EXTERNAL artifact (TaF's shipped code): each is predicted from a
      source-code reading, and the run is the receipt; where a Part-A [E]
      is algebra-forced by the accompanying hand proof, that is disclosed
      inline and the check is graded as machine-verification of the proof,
      not as an independent discovery.
  [F] failing-direction control — a deliberately broken variant run through
      the SAME code path as the check it protects, shown to FAIL.

Expectations are pre-declared in EXPECT below; any post-run revision must be
disclosed in the lane report. Exit 0 iff every check matches its declared
expectation and every [F] fires.
"""

from __future__ import annotations

import sys
from dataclasses import replace
from itertools import combinations, product

TAF_ROOT = r"C:/Users/joe/JB/CapacityOS/repos/public/time-as-finality"
sys.path.insert(0, TAF_ROOT)

import models.d1_restriction_system as t26  # noqa: E402  (TaF actual code)

CHECKS: dict = {}
META: dict = {}


# ===========================================================================
# PART A — exhaustive classification of binary patch constraints, k = 1..4
# ===========================================================================

def neg(x: tuple) -> tuple:
    return tuple(-v for v in x)


def pattern(x: tuple) -> tuple:
    """Equality pattern: which site pairs carry equal values."""
    return tuple(x[i] == x[j] for i, j in combinations(range(len(x)), 2))


def pattern_dropping_first_pair(x: tuple) -> tuple:
    """BROKEN pattern extractor: forgets the (0,1) equality bit."""
    return pattern(x)[1:]


def broken_flip(x: tuple) -> tuple:
    """BROKEN involution: negates only coordinate 0."""
    return (-x[0],) + tuple(x[1:])


def is_flip_even(fset: frozenset, inputs: tuple, flip=neg) -> bool:
    return all((x in fset) == (flip(x) in fset) for x in inputs)


def is_label_free(fset: frozenset, inputs: tuple, pat=pattern) -> bool:
    by_pat: dict = {}
    for x in inputs:
        by_pat.setdefault(pat(x), set()).add(x in fset)
    return all(len(v) == 1 for v in by_pat.values())


def classify_arity(k: int, flip=neg, pat=pattern):
    inputs = tuple(product((-1, 1), repeat=k))
    n_funcs = 2 ** len(inputs)
    flip_even = label_free = odd_and_free = 0
    for mask in range(n_funcs):
        fset = frozenset(x for i, x in enumerate(inputs) if (mask >> i) & 1)
        fe = is_flip_even(fset, inputs, flip)
        lf = is_label_free(fset, inputs, pat)
        flip_even += fe
        label_free += lf
        if (not fe) and lf:
            odd_and_free += 1
        if fe != lf:
            # exact-coincidence witness bookkeeping (any mismatch recorded)
            META.setdefault(f"A_k{k}_mismatch_examples", []).append(mask)
    return n_funcs, flip_even, label_free, odd_and_free


def named_constraint(k: int, fn) -> frozenset:
    inputs = tuple(product((-1, 1), repeat=k))
    return frozenset(x for x in inputs if fn(x))


def run_part_a() -> None:
    # exhaustive classification, k = 1..4
    expected_counts = {1: (4, 2, 2), 2: (16, 4, 4),
                       3: (256, 16, 16), 4: (65536, 256, 256)}
    for k in (1, 2, 3, 4):
        n, fe, lf, oaf = classify_arity(k)
        META[f"A_k{k}_counts_total_flipeven_labelfree"] = (n, fe, lf)
        CHECKS[f"A_E_k{k}_counts_match_orbit_formula"] = (
            (n, fe, lf) == expected_counts[k])
        CHECKS[f"A_E_k{k}_no_flip_odd_label_free_constraint"] = (oaf == 0)
        CHECKS[f"A_E_k{k}_label_free_EQUALS_flip_even_exactly"] = (
            f"A_k{k}_mismatch_examples" not in META)

    # named exemplars (k as noted): (name, k, predicate, expected (fe, lf))
    exemplars = [
        ("pairwise_same", 2, lambda x: x[0] == x[1], (True, True)),
        ("pairwise_different", 2, lambda x: x[0] != x[1], (True, True)),
        ("triple_parity_product_plus", 3,
         lambda x: x[0] * x[1] * x[2] == 1, (False, False)),
        ("quad_parity_product_plus", 4,
         lambda x: x[0] * x[1] * x[2] * x[3] == 1, (True, True)),
        ("not_all_equal_3", 3,
         lambda x: len(set(x)) > 1, (True, True)),
        ("majority_is_plus_3", 3,
         lambda x: sum(1 for v in x if v == 1) >= 2, (False, False)),
        ("named_slot_x0_is_plus", 3, lambda x: x[0] == 1, (False, False)),
        ("all_three_equal", 3, lambda x: len(set(x)) == 1, (True, True)),
    ]
    for name, k, fn, (exp_fe, exp_lf) in exemplars:
        inputs = tuple(product((-1, 1), repeat=k))
        fset = named_constraint(k, fn)
        fe = is_flip_even(fset, inputs)
        lf = is_label_free(fset, inputs)
        CHECKS[f"A_E_exemplar_{name}_classified_as_predicted"] = (
            (fe, lf) == (exp_fe, exp_lf))
        META[f"A_exemplar_{name}"] = {"flip_even": fe, "label_free": lf}

    # [F1] broken involution through the SAME is_flip_even path: the truly
    # flip-even, label-free constraint [x0 == x1] must be MISclassified
    # (classified flip-odd) under the broken flip — proving the flip-parity
    # checker actually depends on the involution being the real flip.
    inputs2 = tuple(product((-1, 1), repeat=2))
    f_eq01 = named_constraint(2, lambda x: x[0] == x[1])
    CHECKS["A_F_broken_involution_misclassifies_pairwise_same"] = (
        is_flip_even(f_eq01, inputs2, flip=neg)
        and not is_flip_even(f_eq01, inputs2, flip=broken_flip))

    # [F2] broken pattern extractor through the SAME is_label_free path:
    # the truly label-free [x0 == x1] must be MISclassified label-naming.
    CHECKS["A_F_broken_pattern_extractor_misclassifies_pairwise_same"] = (
        is_label_free(f_eq01, inputs2, pat=pattern)
        and not is_label_free(f_eq01, inputs2,
                              pat=pattern_dropping_first_pair))


# ===========================================================================
# PART B — TaF's actual T26 code
# ===========================================================================

FLIP_VALUE = {"+1": "-1", "-1": "+1"}
P_LOW = t26.D1Profile(2, 1, 1, 1)
P_HIGH = t26.D1Profile(3, 2, 1, 2)
SCALES = ("person", "lab", "institution")


def mk_system(name, values, edges, patches=(), overlap_tests=(),
              profiles=None, source=None, target=None):
    """Build an actual t26.D1RestrictionSystem. `values` is an ordered dict
    site_id -> "+1"/"-1". Sites carry DISTINCT T24 labels (population/scale/
    time_step/trust_domain)."""
    site_ids = list(values)
    profiles = profiles or {s: P_LOW for s in site_ids}
    local_values = tuple(
        t26.LocalD1Value(
            site=t26.ObserverSite(sid, f"pop_{i}", SCALES[i % 3], i,
                                  "trusted"),
            proposition_value=values[sid],
            profile=profiles[sid],
        )
        for i, sid in enumerate(site_ids)
    )
    return t26.D1RestrictionSystem(
        name=name,
        proposition="record_R",
        local_values=local_values,
        transport_edges=tuple(
            t26.TransportEdge(a, b, "trusted_report") for a, b in edges),
        source_site=source or site_ids[0],
        target_site=target or site_ids[-1],
        patches=tuple(patches),
        overlap_tests=tuple(overlap_tests),
    )


def flip_sys(system):
    """The global polarity flip on an actual system: negate every site's
    proposition value; touch nothing else (profiles, edges, patches,
    overlap tests, T24 labels all fixed)."""
    return replace(system, local_values=tuple(
        replace(v, proposition_value=FLIP_VALUE[v.proposition_value])
        for v in system.local_values))


def flip_one_site(system, site_id):
    """BROKEN flip: negates the value at one named site only."""
    return replace(system, local_values=tuple(
        replace(v, proposition_value=FLIP_VALUE[v.proposition_value])
        if v.site.observer_id == site_id else v
        for v in system.local_values))


def patch(pid, sites, variables, constraints):
    return t26.RestrictionPatch(
        patch_id=pid, site_ids=tuple(sites), variables=tuple(variables),
        constraints=tuple(t26.PatchConstraint(l, r, rel)
                          for l, r, rel in constraints))


ALL_V3 = tuple(product(("+1", "-1"), repeat=3))
ALL_V2 = tuple(product(("+1", "-1"), repeat=2))


def run_part_b1() -> None:
    """B1 [E]: is the actual global_section value-decoupled?  Predicted from
    source reading (global_section dereferences only patches, never
    local_values); the run is the receipt."""
    patches = (
        patch("pa", ("a", "b"), ("va", "vb"), [("va", "vb", "same")]),
        patch("pb", ("a", "b", "c"), ("va", "vb", "vc"),
              [("vb", "vc", "different")]),
    )
    results = []
    flip_pairs_equal = []
    for vals in ALL_V3:
        vmap = dict(zip(("a", "b", "c"), vals))
        X = mk_system("b1", vmap, [("a", "b"), ("b", "c")], patches=patches)
        gs = t26.global_section(X)
        results.append(gs)
        flip_pairs_equal.append(gs == t26.global_section(flip_sys(X)))
    CHECKS["B1_E_global_section_flip_invariant_all_8_assignments"] = all(
        flip_pairs_equal)
    CHECKS["B1_E_global_section_identical_across_ALL_value_assignments"] = (
        len(set(results)) == 1)
    META["B1_witnesses"] = (results[0].local_witness_count,
                            results[0].global_witness_count)
    # validation sanity on the actual axioms (patch closure, site refs, ...)
    CHECKS["B1_E_actual_validate_system_passes"] = t26.validate_system(
        mk_system("b1v", dict(zip(("a", "b", "c"), ALL_V3[0])),
                  [("a", "b"), ("b", "c")], patches=patches)).valid


def run_part_b2() -> None:
    """B2 [E]: (Z/2)^blocks in the ACTUAL global_section, and TaF's own
    contextual gluing obstruction."""
    vmap = {"a": "+1", "b": "+1", "c": "+1"}
    edges = [("a", "b"), ("b", "c")]
    connected = mk_system("chain", vmap, edges, patches=(
        patch("p1", ("a", "b", "c"), ("va", "vb", "vc"),
              [("va", "vb", "same"), ("vb", "vc", "same")]),))
    partitioned = mk_system("part", vmap, edges, patches=(
        patch("p1", ("a", "b", "c"), ("va", "vb", "vc"),
              [("va", "vb", "same")]),))
    isolated = mk_system("isol", vmap, edges, patches=(
        patch("p1", ("a", "b", "c"), ("va", "vb", "vc"), []),))
    counts = tuple(t26.global_section(s).global_witness_count
                   for s in (connected, partitioned, isolated))
    META["B2_section_counts_connected_partitioned_isolated"] = counts
    CHECKS["B2_E_actual_section_counts_are_2_4_8_equals_2_pow_blocks"] = (
        counts == (2, 4, 8))

    # TaF's own contextual gluing obstruction, via TaF's own scenario:
    contextual = t26.system_from_scenario(t26.contextual_gluing_scenario())
    gs = t26.global_section(contextual)
    CHECKS["B2_E_taf_own_contextual_obstruction_reproduces"] = (
        gs.obstruction_detected and gs.global_witness_count == 0
        and gs.local_patches_satisfiable)

    # [F3] same global_section code path, deliberately broken patch set:
    # an odd 'different'-cycle split across three individually satisfiable
    # patches must yield local witnesses AND zero global witnesses.
    odd = mk_system("odd", vmap, edges, patches=(
        patch("q1", ("a", "b"), ("va", "vb"), [("va", "vb", "same")]),
        patch("q2", ("b", "c"), ("vb", "vc"), [("vb", "vc", "same")]),
        patch("q3", ("a", "c"), ("va", "vc"), [("va", "vc", "different")]),
    ))
    gso = t26.global_section(odd)
    CHECKS["B2_F_odd_cycle_creates_obstruction_same_code_path"] = (
        gso.local_witness_count == 3 and gso.global_witness_count == 0
        and gso.obstruction_detected)


DIMENSIONS = ("proposition_value", "profile", "accessible_support",
              "holder_redundancy", "branch_support", "reversal_cost")
RELATIONS = ("same", "different", "left_leq_right", "left_geq_right")


def overlap_verdict(vals, dim, rel):
    """Compatibility verdict of a 2-site system carrying ONE overlap test,
    through the actual public analyze_compatibility path. Heterogeneous
    profiles so profile-dimension tests are non-degenerate."""
    vmap = dict(zip(("a", "b"), vals))
    X = mk_system("ov", vmap, [("a", "b")],
                  overlap_tests=(t26.OverlapTest("a", "b", dim, rel),),
                  profiles={"a": P_LOW, "b": P_HIGH})
    return t26.analyze_compatibility(X).overlap_tests_pass


def sensitivity_sweep(flip_fn):
    """For each (dimension, relation) in the FULL shipped overlap language:
    is the verdict changed by flip_fn on any value assignment?"""
    sensitive = set()
    for dim in DIMENSIONS:
        for rel in RELATIONS:
            for vals in ALL_V2:
                flipped = tuple(flip_fn(vals))
                if (overlap_verdict(vals, dim, rel)
                        != overlap_verdict(flipped, dim, rel)):
                    sensitive.add((dim, rel))
                    break
    return sensitive


def run_part_b3() -> None:
    """B3 [E]: exhaustive flip-sensitivity sweep of the entire shipped
    overlap-test language."""
    true_flip = lambda vals: tuple(FLIP_VALUE[v] for v in vals)  # noqa: E731
    sensitive = sensitivity_sweep(true_flip)
    META["B3_flip_sensitive_overlap_primitives"] = sorted(sensitive)
    CHECKS["B3_E_only_order_relations_on_proposition_value_break_flip"] = (
        sensitive == {("proposition_value", "left_leq_right"),
                      ("proposition_value", "left_geq_right")})

    # [T] conjugation identity: passes(x, leq) == passes(flip x, geq) for all
    # x — algebra-forced (the flip swaps the two labels, reversing any total
    # order on a two-element set). Listed separately; no evidential weight.
    CHECKS["B3_T_flip_conjugates_leq_to_geq"] = all(
        overlap_verdict(vals, "proposition_value", "left_leq_right")
        == overlap_verdict(true_flip(vals), "proposition_value",
                           "left_geq_right")
        for vals in ALL_V2)

    # [E] the conjugate is a DISTINCT, equally admissible test (so fixing
    # either one is a labeling choice that fails the relabel test):
    CHECKS["B3_E_leq_and_geq_are_distinct_tests"] = any(
        overlap_verdict(vals, "proposition_value", "left_leq_right")
        != overlap_verdict(vals, "proposition_value", "left_geq_right")
        for vals in ALL_V2)

    # [F4] broken single-site flip through the SAME sweep harness: equality
    # relations must now register as sensitive — proving the sweep detects
    # sensitivity when it exists.
    broken = lambda vals: (FLIP_VALUE[vals[0]], vals[1])  # noqa: E731
    broken_sensitive = sensitivity_sweep(broken)
    CHECKS["B3_F_single_site_flip_detected_by_same_sweep"] = (
        ("proposition_value", "same") in broken_sensitive
        and ("proposition_value", "different") in broken_sensitive
        and broken_sensitive != sensitive)


def analyze_reached(source, target, site_map):
    return t26.analyze_morphism(t26.D1RestrictionMorphism(
        name="probe", source=source, target=target,
        site_map=tuple(t26.SiteMap(s, t) for s, t in site_map))).reached


def two_site(name, vals, profiles=None):
    return mk_system(name, dict(zip(("a", "b"), vals)), [("a", "b")],
                     profiles=profiles)


def run_part_b45() -> None:
    """B4/B5 [E]: value-blindness of the actual morphism analyzer; merges,
    splits, composites; adjacent non-vacuity controls."""
    ident = (("a", "a"), ("b", "b"))

    # B4: identity site maps, ALL 16 (source values x target values) combos.
    outcomes = [analyze_reached(two_site("s", sv), two_site("t", tv), ident)
                for sv in ALL_V2 for tv in ALL_V2]
    CHECKS["B4_E_identity_morphism_reached_for_all_16_value_combos"] = all(
        outcomes)
    META["B4_reached_count"] = f"{sum(outcomes)}/16"
    # includes X -> flip(X) in particular:
    X = two_site("x", ("+1", "-1"))
    CHECKS["B4_E_X_to_flipX_is_a_reached_morphism"] = analyze_reached(
        X, flip_sys(X), ident)

    # B5 merges: both source sites -> one target site; 4 x 2 value combos,
    # INCLUDING sources whose two sites carry OPPOSITE values.
    def one_site(name, val, profile=P_LOW):
        return mk_system(name, {"t": val}, [], profiles={"t": profile})

    merge_map = (("a", "t"), ("b", "t"))
    merge_outcomes = [
        analyze_reached(two_site("s", sv), one_site("t", tv), merge_map)
        for sv in ALL_V2 for tv in ("+1", "-1")]
    CHECKS["B5_E_all_8_merges_reached_incl_conflicting_source_values"] = all(
        merge_outcomes)

    # B5 splits: one source site mapped into a two-site target; 2 x 4 combos.
    split_outcomes = [
        analyze_reached(one_site("s", sv), two_site("t2", tv),
                        (("t", "a"),))
        for sv in ("+1", "-1") for tv in ALL_V2]
    CHECKS["B5_E_all_8_splits_reached_regardless_of_values"] = all(
        split_outcomes)

    # B5 merge-then-split composite (a,b -> t -> u1): composite site map
    # sends both source sites to one target site of a two-site system.
    comp_outcomes = [
        analyze_reached(two_site("s", sv), two_site("u", tv),
                        (("a", "a"), ("b", "a")))
        for sv in ALL_V2 for tv in ALL_V2]
    CHECKS["B5_E_all_16_merge_split_composites_reached"] = all(comp_outcomes)

    # Adjacent controls: the analyzer is NOT vacuously positive.
    CHECKS["B5_E_profile_mismatch_merge_fails"] = not analyze_reached(
        two_site("s", ("+1", "+1")),
        one_site("t", "+1", profile=P_HIGH), merge_map)
    CHECKS["B5_E_taf_own_failed_transport_morphism_fails"] = (
        not t26.analyze_morphism(t26.failed_transport_morphism()).reached)
    CHECKS["B5_E_taf_own_positive_relabel_morphism_reached"] = (
        t26.analyze_morphism(t26.positive_relabel_morphism()).reached)


def morphism_configs():
    """Mixed battery: passing AND failing configs (so invariance checks are
    non-vacuous over both outcomes)."""
    ident = (("a", "a"), ("b", "b"))
    merge_map = (("a", "t"), ("b", "t"))
    cfgs = []
    for sv in ALL_V2:
        for tv in ALL_V2:
            cfgs.append((two_site("s", sv), two_site("t", tv), ident))
    for sv in ALL_V2:
        for tv in ("+1", "-1"):
            cfgs.append((two_site("s", sv),
                         mk_system("t1", {"t": tv}, []), merge_map))
            # failing variant: profile mismatch at the merged site
            cfgs.append((two_site("s", sv),
                         mk_system("t1h", {"t": tv}, [],
                                   profiles={"t": P_HIGH}), merge_map))
    return cfgs


def reached_with(analyzer, cfg):
    return analyzer(*cfg)


def strict_transport_analyzer(source, target, site_map):
    """Actual analyzer PLUS a label-free value-transport check: the merged/
    mapped value must EQUAL the source value (an equality atom — label-free
    by the Part-A definition)."""
    base = analyze_reached(source, target, site_map)
    sv = {v.site.observer_id: v.proposition_value
          for v in source.local_values}
    tv = {v.site.observer_id: v.proposition_value
          for v in target.local_values}
    return base and all(sv[s] == tv[t] for s, t in site_map)


def label_naming_analyzer(source, target, site_map):
    """Deliberately label-naming analyzer: additionally requires every
    target value to BE the named label '+1'."""
    base = analyze_reached(source, target, site_map)
    return base and all(v.proposition_value == "+1"
                        for v in target.local_values)


def invariant_under(analyzer, transform, cfgs):
    return all(
        reached_with(analyzer, cfg)
        == reached_with(analyzer, transform(cfg))
        for cfg in cfgs)


def run_part_b6() -> None:
    cfgs = morphism_configs()
    outcomes = [analyze_reached(*c) for c in cfgs]
    META["B6_config_battery"] = (
        f"{len(cfgs)} configs, {sum(outcomes)} reached, "
        f"{len(outcomes) - sum(outcomes)} failing")
    CHECKS["B6_E_battery_contains_both_outcomes"] = (
        0 < sum(outcomes) < len(outcomes))

    flip_both = lambda c: (flip_sys(c[0]), flip_sys(c[1]), c[2])  # noqa: E731
    flip_src = lambda c: (flip_sys(c[0]), c[1], c[2])             # noqa: E731

    # actual analyzer: full-flip invariant AND source-only-flip invariant.
    # The latter is invariance BY OMISSION (values unread) — disclosed as
    # vacuous in the lane report, not counted as a symmetry theorem.
    CHECKS["B6_E_actual_analyzer_full_flip_invariant"] = invariant_under(
        analyze_reached, flip_both, cfgs)
    CHECKS["B6_E_actual_analyzer_source_only_flip_invariant_VACUOUS"] = (
        invariant_under(analyze_reached, flip_src, cfgs))

    # value-strict analyzer: STILL full-flip invariant (an equality-atom
    # transport check is label-free, hence flip-even — a live instance of
    # the Part-A classification theorem on the actual objects)...
    CHECKS["B6_E_value_strict_analyzer_STILL_full_flip_invariant"] = (
        invariant_under(strict_transport_analyzer, flip_both, cfgs))
    # ...[F5a] but NOT source-only-flip invariant: the same invariance
    # harness detects the break, proving the B6 invariance checks have teeth
    # (the actual analyzer's invariance is a property of TaF's code, not a
    # blindness of this harness).
    CHECKS["B6_F_value_strict_analyzer_breaks_source_only_flip"] = (
        not invariant_under(strict_transport_analyzer, flip_src, cfgs))

    # [F5b] label-naming analyzer breaks even FULL-flip invariance through
    # the same harness — the collapse-or-smuggle dichotomy at morphism level:
    # the only exhibited way to make the morphism layer sign-selecting is to
    # name a value label.
    CHECKS["B6_F_label_naming_analyzer_breaks_full_flip"] = (
        not invariant_under(label_naming_analyzer, flip_both, cfgs))

    # [E] and the strict analyzer distinguishes X->X from X->flip(X)
    # (value-sensitivity exists in the harness when the analyzer has it):
    X = two_site("x", ("+1", "-1"))
    ident = (("a", "a"), ("b", "b"))
    CHECKS["B6_E_strict_analyzer_passes_XtoX_fails_XtoFlipX"] = (
        strict_transport_analyzer(X, X, ident)
        and not strict_transport_analyzer(X, flip_sys(X), ident))


# ===========================================================================
# Expectations (pre-declared) and driver
# ===========================================================================

EXPECT_TRUE = [
    # PART A
    "A_E_k1_counts_match_orbit_formula",
    "A_E_k1_no_flip_odd_label_free_constraint",
    "A_E_k1_label_free_EQUALS_flip_even_exactly",
    "A_E_k2_counts_match_orbit_formula",
    "A_E_k2_no_flip_odd_label_free_constraint",
    "A_E_k2_label_free_EQUALS_flip_even_exactly",
    "A_E_k3_counts_match_orbit_formula",
    "A_E_k3_no_flip_odd_label_free_constraint",
    "A_E_k3_label_free_EQUALS_flip_even_exactly",
    "A_E_k4_counts_match_orbit_formula",
    "A_E_k4_no_flip_odd_label_free_constraint",
    "A_E_k4_label_free_EQUALS_flip_even_exactly",
    "A_E_exemplar_pairwise_same_classified_as_predicted",
    "A_E_exemplar_pairwise_different_classified_as_predicted",
    "A_E_exemplar_triple_parity_product_plus_classified_as_predicted",
    "A_E_exemplar_quad_parity_product_plus_classified_as_predicted",
    "A_E_exemplar_not_all_equal_3_classified_as_predicted",
    "A_E_exemplar_majority_is_plus_3_classified_as_predicted",
    "A_E_exemplar_named_slot_x0_is_plus_classified_as_predicted",
    "A_E_exemplar_all_three_equal_classified_as_predicted",
    "A_F_broken_involution_misclassifies_pairwise_same",
    "A_F_broken_pattern_extractor_misclassifies_pairwise_same",
    # PART B
    "B1_E_global_section_flip_invariant_all_8_assignments",
    "B1_E_global_section_identical_across_ALL_value_assignments",
    "B1_E_actual_validate_system_passes",
    "B2_E_actual_section_counts_are_2_4_8_equals_2_pow_blocks",
    "B2_E_taf_own_contextual_obstruction_reproduces",
    "B2_F_odd_cycle_creates_obstruction_same_code_path",
    "B3_E_only_order_relations_on_proposition_value_break_flip",
    "B3_T_flip_conjugates_leq_to_geq",
    "B3_E_leq_and_geq_are_distinct_tests",
    "B3_F_single_site_flip_detected_by_same_sweep",
    "B4_E_identity_morphism_reached_for_all_16_value_combos",
    "B4_E_X_to_flipX_is_a_reached_morphism",
    "B5_E_all_8_merges_reached_incl_conflicting_source_values",
    "B5_E_all_8_splits_reached_regardless_of_values",
    "B5_E_all_16_merge_split_composites_reached",
    "B5_E_profile_mismatch_merge_fails",
    "B5_E_taf_own_failed_transport_morphism_fails",
    "B5_E_taf_own_positive_relabel_morphism_reached",
    "B6_E_battery_contains_both_outcomes",
    "B6_E_actual_analyzer_full_flip_invariant",
    "B6_E_actual_analyzer_source_only_flip_invariant_VACUOUS",
    "B6_E_value_strict_analyzer_STILL_full_flip_invariant",
    "B6_F_value_strict_analyzer_breaks_source_only_flip",
    "B6_F_label_naming_analyzer_breaks_full_flip",
    "B6_E_strict_analyzer_passes_XtoX_fails_XtoFlipX",
]


def main() -> None:
    print("P2C: TaF ACTUAL T26 PATCH/OVERLAP MACHINERY vs THE GLOBAL FLIP")
    print("=" * 74)
    print(f"driving TaF code at: {TAF_ROOT}/models/d1_restriction_system.py")

    run_part_a()
    run_part_b1()
    run_part_b2()
    run_part_b3()
    run_part_b45()
    run_part_b6()

    failures = []
    print("\nCHECKS ([T] no evidential weight; [E] experiments; "
          "[F] failing-direction controls)")
    for name in EXPECT_TRUE:
        val = CHECKS.get(name, "MISSING")
        ok = val is True
        print(f"  {'PASS ' if ok else 'FAIL '}{name}: {val}")
        if not ok:
            failures.append((name, val))
    extra = set(CHECKS) - set(EXPECT_TRUE)
    if extra:
        failures.append(("undeclared_checks_present", sorted(extra)))

    print("\nMEASUREMENTS")
    for k, v in sorted(META.items()):
        print(f"  {k}: {v}")

    print("\nVERDICT (exploration tier)")
    print("  PART A: over the binary alphabet, at every arity k<=4")
    print("  (exhaustive; all-arity by the accompanying proof), label-free")
    print("  = flip-even EXACTLY; every flip-odd patch constraint is")
    print("  label-naming. No flip-odd label-free constraint exists.")
    print("  PART B: in TaF's actual shipped T26, (i) patch constraints")
    print("  never dereference proposition values (global_section is")
    print("  value-decoupled and reproduces (Z/2)^blocks); (ii) the ONLY")
    print("  flip-breaking primitives in the whole overlap language are the")
    print("  order relations on proposition_value, which read the label")
    print("  string order and fail the relabel test (leq/geq conjugate);")
    print("  (iii) restriction morphisms (incl. merges and splits) are")
    print("  value-blind by omission - their flip-invariance is vacuous,")
    print("  and a label-free strict-transport upgrade would stay")
    print("  flip-even (theorem instance) while a label-naming one breaks")
    print("  the flip. The flip remains an automorphism; the fiber remains")
    print("  undetermined. bar(b), H59, Krein positivity, physical")
    print("  issuance: ALL REMAIN OPEN.")

    if failures:
        print(f"\nMISMATCHES: {failures}")
        raise SystemExit(1)
    print("\nAll checks matched the declared expectations. Exit 0.")


if __name__ == "__main__":
    main()
```

## 9. Full fixture output (exit code 0, runtime ~3s)

```
P2C: TaF ACTUAL T26 PATCH/OVERLAP MACHINERY vs THE GLOBAL FLIP
==========================================================================
driving TaF code at: C:/Users/joe/JB/CapacityOS/repos/public/time-as-finality/models/d1_restriction_system.py

CHECKS ([T] no evidential weight; [E] experiments; [F] failing-direction controls)
  PASS A_E_k1_counts_match_orbit_formula: True
  PASS A_E_k1_no_flip_odd_label_free_constraint: True
  PASS A_E_k1_label_free_EQUALS_flip_even_exactly: True
  PASS A_E_k2_counts_match_orbit_formula: True
  PASS A_E_k2_no_flip_odd_label_free_constraint: True
  PASS A_E_k2_label_free_EQUALS_flip_even_exactly: True
  PASS A_E_k3_counts_match_orbit_formula: True
  PASS A_E_k3_no_flip_odd_label_free_constraint: True
  PASS A_E_k3_label_free_EQUALS_flip_even_exactly: True
  PASS A_E_k4_counts_match_orbit_formula: True
  PASS A_E_k4_no_flip_odd_label_free_constraint: True
  PASS A_E_k4_label_free_EQUALS_flip_even_exactly: True
  PASS A_E_exemplar_pairwise_same_classified_as_predicted: True
  PASS A_E_exemplar_pairwise_different_classified_as_predicted: True
  PASS A_E_exemplar_triple_parity_product_plus_classified_as_predicted: True
  PASS A_E_exemplar_quad_parity_product_plus_classified_as_predicted: True
  PASS A_E_exemplar_not_all_equal_3_classified_as_predicted: True
  PASS A_E_exemplar_majority_is_plus_3_classified_as_predicted: True
  PASS A_E_exemplar_named_slot_x0_is_plus_classified_as_predicted: True
  PASS A_E_exemplar_all_three_equal_classified_as_predicted: True
  PASS A_F_broken_involution_misclassifies_pairwise_same: True
  PASS A_F_broken_pattern_extractor_misclassifies_pairwise_same: True
  PASS B1_E_global_section_flip_invariant_all_8_assignments: True
  PASS B1_E_global_section_identical_across_ALL_value_assignments: True
  PASS B1_E_actual_validate_system_passes: True
  PASS B2_E_actual_section_counts_are_2_4_8_equals_2_pow_blocks: True
  PASS B2_E_taf_own_contextual_obstruction_reproduces: True
  PASS B2_F_odd_cycle_creates_obstruction_same_code_path: True
  PASS B3_E_only_order_relations_on_proposition_value_break_flip: True
  PASS B3_T_flip_conjugates_leq_to_geq: True
  PASS B3_E_leq_and_geq_are_distinct_tests: True
  PASS B3_F_single_site_flip_detected_by_same_sweep: True
  PASS B4_E_identity_morphism_reached_for_all_16_value_combos: True
  PASS B4_E_X_to_flipX_is_a_reached_morphism: True
  PASS B5_E_all_8_merges_reached_incl_conflicting_source_values: True
  PASS B5_E_all_8_splits_reached_regardless_of_values: True
  PASS B5_E_all_16_merge_split_composites_reached: True
  PASS B5_E_profile_mismatch_merge_fails: True
  PASS B5_E_taf_own_failed_transport_morphism_fails: True
  PASS B5_E_taf_own_positive_relabel_morphism_reached: True
  PASS B6_E_battery_contains_both_outcomes: True
  PASS B6_E_actual_analyzer_full_flip_invariant: True
  PASS B6_E_actual_analyzer_source_only_flip_invariant_VACUOUS: True
  PASS B6_E_value_strict_analyzer_STILL_full_flip_invariant: True
  PASS B6_F_value_strict_analyzer_breaks_source_only_flip: True
  PASS B6_F_label_naming_analyzer_breaks_full_flip: True
  PASS B6_E_strict_analyzer_passes_XtoX_fails_XtoFlipX: True

MEASUREMENTS
  A_exemplar_all_three_equal: {'flip_even': True, 'label_free': True}
  A_exemplar_majority_is_plus_3: {'flip_even': False, 'label_free': False}
  A_exemplar_named_slot_x0_is_plus: {'flip_even': False, 'label_free': False}
  A_exemplar_not_all_equal_3: {'flip_even': True, 'label_free': True}
  A_exemplar_pairwise_different: {'flip_even': True, 'label_free': True}
  A_exemplar_pairwise_same: {'flip_even': True, 'label_free': True}
  A_exemplar_quad_parity_product_plus: {'flip_even': True, 'label_free': True}
  A_exemplar_triple_parity_product_plus: {'flip_even': False, 'label_free': False}
  A_k1_counts_total_flipeven_labelfree: (4, 2, 2)
  A_k2_counts_total_flipeven_labelfree: (16, 4, 4)
  A_k3_counts_total_flipeven_labelfree: (256, 16, 16)
  A_k4_counts_total_flipeven_labelfree: (65536, 256, 256)
  B1_witnesses: (2, 2)
  B2_section_counts_connected_partitioned_isolated: (2, 4, 8)
  B3_flip_sensitive_overlap_primitives: [('proposition_value', 'left_geq_right'), ('proposition_value', 'left_leq_right')]
  B4_reached_count: 16/16
  B6_config_battery: 32 configs, 24 reached, 8 failing

VERDICT (exploration tier)
  PART A: over the binary alphabet, at every arity k<=4
  (exhaustive; all-arity by the accompanying proof), label-free
  = flip-even EXACTLY; every flip-odd patch constraint is
  label-naming. No flip-odd label-free constraint exists.
  PART B: in TaF's actual shipped T26, (i) patch constraints
  never dereference proposition values (global_section is
  value-decoupled and reproduces (Z/2)^blocks); (ii) the ONLY
  flip-breaking primitives in the whole overlap language are the
  order relations on proposition_value, which read the label
  string order and fail the relabel test (leq/geq conjugate);
  (iii) restriction morphisms (incl. merges and splits) are
  value-blind by omission - their flip-invariance is vacuous,
  and a label-free strict-transport upgrade would stay
  flip-even (theorem instance) while a label-naming one breaks
  the flip. The flip remains an automorphism; the fiber remains
  undetermined. bar(b), H59, Krein positivity, physical
  issuance: ALL REMAIN OPEN.

All checks matched the declared expectations. Exit 0.
```

---

**Sources consulted:** `possibility-to-capability/governance/CHARTER.md`; swing-2 `SYNTHESIS.md`, `lane-2-gate1-enriched-toy-lift.md` (incl. referee report — F3 is the spec for this lane), `lane-3-krein-normlink-probe.md`; big-swing `lane-D-aliveness-anchor.md`; `gu-formalization/.../adapter2-correction-polarity-fiber-not-axis-2026-07-15.md` (via governing summaries); `time-as-finality/FORMALISM.md` (T24, T25, T26, T29/T31, T37, T39 sections); `time-as-finality/tests/T26-d1-restriction-system.md`; **`time-as-finality/models/d1_restriction_system.py` (read in full — the adjudicated artifact)**; `time-as-finality/models/multiscale_observer_field.py` (dataclass layer); `time-as-finality/models/transport_network.py` (T37, read-only audit for the named gap). Existing fixtures `tests/gate1_branch_preserving_functor.py` and `tests/gate1_enriched_toy_nonthin_multiobserver.py` reviewed for house style continuity. Fixture persisted and pushed: `possibility-to-capability/tests/gate1_t26_actual_patch_machinery.py` @ `6ed76a5` (main).

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs grades)

# Referee Report — Lane C-t26-native-patch

## (1) VERDICT: **SOUND-WITH-CORRECTIONS**

Independent re-execution: `tests/gate1_t26_actual_patch_machinery.py` re-run from disk — exit 0, all 47 checks PASS, every MEASUREMENTS line byte-identical to the report's embedded output (counts 4/16/256/65536 → flip-even = label-free = 2/4/16/256; B2 = (2,4,8); B3 sensitive set = the two order relations; B4 16/16; B6 32/24/8). Commit `6ed76a5` exists, is on `main`, is pushed to `origin/main`, and adds only this 684-line fixture (no TaF writes — source sovereignty clean). The line-number claim checks out: `_overlap_test_passes` compares `left_value <= right_value` on the raw value at `d1_restriction_system.py:997–1000`, and for `proposition_value` that value is the `str` itself. I independently confirmed via grep that `proposition_value` is dereferenced in exactly **one** function in the entire TaF module (`_overlap_test_passes`; `_observer_profile` at line 1029 is dead code) — the value-decoupling findings are real. The Part-A proof is correct (flip is fixed-point-free on ±1 tuples → 2^(k−1) orbits → 2^(2^(k−1)) flip-even predicates; pattern classes = flip orbits over a binary alphabet). No contradiction of ADAPTER2-01 (identity stays OPEN; this lane only extends the automorphism/undetermined-fiber picture). Process claims F3/F4/ranked-item-1 verified against swing-2's lane-2 referee report and SYNTHESIS — accurate. The lane survives refutation on its core content; it does not survive on scoping, tagging, and one process claim.

## (2) Defects

**D1 (MEDIUM) — Encoding-level fact presented with formalism-level wording: the binary value alphabet and "the global flip" are fixture impositions, not T26 objects.** Shipped T26's `proposition_value` is an unconstrained `str`; `validate_system` imposes no alphabet; FORMALISM.md's T26 says only "one proposition value per site"; TaF's own T24/T26 scenarios set every `proposition_value` to `"true"` (verified: `multiscale_observer_field.py:163,187–190`), where no flip partner even exists in-repo. TaF defines no flip anywhere. The report's §2 warrant — "T39 establishes that the `D1RestrictionSystem` patch language *is* a binary {-1,1} CSP" — is accurately quoted (FORMALISM.md CSP-reframing update) but is about **patch variables** (natively `product((-1,1))` in code), and is silently extended to license binary as "the native case" for the site **value** fiber in Part B. Sentences like "the flip remains an automorphism of everything T26 can say" state a fixture-defined operation on a fixture-chosen two-string sub-alphabet as if it were a T26-native symmetry. Mitigation (why not UNSOUND): the substance generalizes — B1 actually proves the stronger fact (invariance under *all* 8 assignments, i.e., under any relabeling), equality semantics are injective-relabeling-invariant on any alphabet, and order-sensitivity holds for any two distinct strings. Wording fix required, not retraction.

**D2 (MEDIUM) — "The fiber is now located *through TaF's entire T26 surface*" overclaims coverage against FORMALISM's own field list.** FORMALISM's T26 tuple includes "scalar and vector projection maps" and compatibility/transport predicates as first-class components. `scalar_projection`, `vector_projection`, `compare_systems`, `analyze_transport`, and `relabeled_transport_system` were neither driven executably nor listed in §7's named gaps. They are in fact value-blind (my grep, above), so the claim is *true* — but at source-audit grade, undisclosed, in a report that elsewhere carefully grades exactly this distinction (§7 gap 3). The lane also missed the strongest honest statement available: *the whole module reads `proposition_value` in exactly one function*. Field-by-field verdict on the orchestrator's specific question: the lane drives actual code (so no model-mismatch is possible for what it drives — sites/values/profiles ✓, edges ✓, patches ✓, overlap tests ✓, morphisms ✓, global section ✓, compatibility ✓), but two FORMALISM-declared T26 fields (scalar/vector projections) are absent from both the batteries and the gaps list.

**D3 (MEDIUM) — "Pre-registration receipt" is an assertion, not a receipt (unverifiable process claim).** Delivery is a single commit (`6ed76a5`) containing the finished fixture with `EXPECT_TRUE` already populated. Nothing mechanically separates expectation-writing from first execution — no prior expectations commit, no hash, no two-phase artifact. Swing-2's F4 flagged the *absence of a pre-registration receipt*; this lane answers with a stronger *claim* ("written before its first execution... No expectation was revised") but the same absence of mechanism. The exit-0-iff-declared-match + undeclared-checks guard design bounds post-hoc drift but cannot verify temporal ordering.

**D4 (LOW/MEDIUM) — §6 check ledger contradicts the fixture's own tags.** The committed fixture's names count **[E] 40, [F] 6, [T] 1** (verified by script). §6 reports "[F] 7, [E] 39," conscripting `B6_E_strict_analyzer_passes_XtoX_fails_XtoFlipX` into the [F] column while its name and in-code comment tag it [E]. Additionally, by the fixture's own [E] definition ("outcome not fixed at formalization time by THIS fixture's construction"), `B6_E_value_strict_analyzer_STILL_full_flip_invariant` is algebra-forced on a *fixture-defined* analyzer (equality atoms are invariant under any bijection applied to both sides — the report itself calls it "a theorem instance"); it carries [T]-grade weight, tagged [E]. Not load-bearing for the headline (which rests on B1–B3/B5 and the Part-A theorem), hence not MEDIUM+.

**D5 (LOW) — [E]-count inflation.** B1/B4/B5's ~10 [E] checks all instantiate one structural source fact (values never read by section/morphism paths), counted separately. Disclosed as source-predicted, but "39 [E]" overstates independent experimental content in any downstream tally.

**D6 (LOW) — Untallied prose [T].** §3.2 carries a [T]-labeled corollary that is not a ledger check while §6 asserts "[T] 1"; harmless (ledger counts checks) but invites miscounting downstream.

**D7 (LOW) — Grandiosity in naming.** The "Patch-Collapse Classification Theorem" is an elementary two-step combinatorial lemma (relabeling-invariance = flip-invariance over a two-letter alphabet). Correct, honestly proved, and properly used to demote the enumeration to machine-verification — but syntheses should not weight "theorem grade at every arity" as deep mathematical content.

**Controls audit (passed):** all 6 fixture [F]s exercise the same code path they protect (`is_flip_even`, `is_label_free`, actual `global_section` via odd different-cycle — a genuine T39 negative cycle, the same `sensitivity_sweep`, the same `invariant_under` harness twice) and each fires. B3_T is correctly tagged (order reversal under label swap is forced for any total order on 2 elements) and is not counted as evidence anywhere. No [T] found masquerading as headline evidence.

## (3) Corrected wording

- "The flip is still an automorphism of everything T26 can say" → **"Under the fixture's two-string value encoding, every injective relabeling of proposition values — the flip in particular — leaves every value-touching primitive of shipped T26 invariant except the two string-order overlap relations. Shipped T26 itself imposes no value alphabet and defines no flip; the flip is the fixture's restriction of the GU-side fiber question onto T26's opaque string field."**
- "the fiber is now located *through* TaF's entire T26 surface" → **"located through every value-reading path in shipped T26 — `proposition_value` is dereferenced in exactly one function (`_overlap_test_passes`); the remaining T26 surface (including the scalar/vector projections and `compare_systems`, not driven here) is value-blind at source-audit grade."**
- "Binary is the native case: TaF's own T39 establishes that the `D1RestrictionSystem` patch language *is* a binary {-1,1} CSP" → **append:** "…for patch variables. For site proposition values, binary is a fixture-imposed encoding; shipped T26 leaves the value alphabet unconstrained (TaF's own fixtures use the single value `'true'`)."
- "Pre-registration receipt (honesty): … written into the fixture before its first execution" → **"Pre-registration assertion (not mechanically verifiable from the single-commit delivery): … The fixture's exit-0-iff-declared-match design plus the undeclared-checks guard bounds, but cannot prove absence of, post-hoc revision. A verifiable receipt requires committing the expectation set before the first run."**
- "**[F] 7** … **[E] 39**" → **"[F]-named 6, [E]-named 40, [T]-named 1; `B6_E_strict_analyzer_passes_XtoX_fails_XtoFlipX` functions as a harness-sensitivity control, and the two strict-analyzer B6 [E]s are theorem instances on fixture-defined analyzers carrying [T]-grade weight."**
- "Exhaustive sweep … over **all** two-site value assignments" → **"over all two-site assignments from the fixture's two-string alphabet (the flip's domain of definition); on the unbounded shipped `str` domain, equality-relation invariance holds for any injective relabeling and order-relation sensitivity for any two distinct strings."**

## (4) Grade the main result actually earns

**Shipped-code-grade null result for exactly the surface swing-2's F3 named** (patch constraints, overlap tests, morphisms incl. merges/splits of TaF's actual `D1RestrictionSystem`), plus **an elementary but correct binary-alphabet classification lemma** (label-free = flip-even, all arities) that closes the discovery branch by classification. "HIDING-PLACE-CLOSED" is earned **for F3's named surface**, with three riders: (i) the flip and binary value fiber are fixture-imposed encodings on T26's unconstrained string field (D1); (ii) two FORMALISM-declared T26 components were covered only implicitly at source-audit grade (D2); (iii) the first-run/pre-registration claim is unverifiable (D3). The verdict's own three-part grading (§ verdict items 1–3) is otherwise accurate, and its bounding findings (value-decoupling; vacuous morphism invariance; label-reading order atoms) are genuine, correctly signed, Failure-Preservation-compliant results. Nothing here moves bar(b), H59, Krein, or ADAPTER2-01 — correctly stated.

## (5) Implication for the 2-prime twin lanes

This lane's Part-A lemma is the **adjudication key for the 2′ pair**, and it is asymmetric:

- **Constructive 2′ twin (`condition2prime_constructive_probe`): predicted to FAIL or smuggle.** Any candidate Condition-2′ discriminator that is (a) a finite-arity predicate over binary data and (b) label-free under the mechanically decidable equality-pattern criterion **is flip-even, hence cannot select the sign** — at any arity, exactly. Every apparent success must, on inspection, consume non-relabeling-invariant structure (a distinguished value, an order, an external anchor) and should be reclassified label-naming. The already-committed probe result ("three derivation attempts, all characterized — equivariance wall," commit `a193a3b`) is exactly the configuration this lane predicts.
- **No-go 2′ twin (`no_go_2prime_flip_equivariance`): predicted to SUCCEED**, and its flip-equivariance obstruction should be derivable as a corollary of (indeed is weaker than) this lane's classification: equivariance rules out one discriminator at a time; the classification rules out the whole label-free class.
- **Adjudication rule for the orchestrator:** the pair is mutually consistent **only** as (constructive = wall, no-go = holds). If the constructive twin claims a label-free flip-odd discriminator, one lane has a class-boundary error — check first that both twins use the *same mechanically decidable boundary* (equality-pattern invariance, as implemented here in `is_label_free`), the same binary alphabet, and no imported external structure; divergence there reconciles the conflict by reclassification, not by falsification. If the no-go twin *fails* on a genuinely binary, genuinely label-free counterexample, that falsifies this lane's Part A and this report's verdict must be reopened. **Scope limit:** the pre-emption does not cover non-binary alphabets (|V| ≥ 3, where label-free is strictly stronger than any single-involution evenness) or discriminators consuming declared external anchors — a constructive success in either regime would be outside this lane's theorem, not in conflict with it.