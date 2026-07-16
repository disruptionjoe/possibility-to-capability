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
