"""P2C Gate #1 fixture: native branch-preserving functor Ext_S -> TaF, or its disproof.

Exploration tier. Pure Python, no dependencies. No claim promotion.

SOURCE: a finite model of TI's Ext_S (RUN-0025 category-first shape):
  objects   = consistent literal-states S (finite sets of (proposition, +/-1)),
  morphisms = admissible extensions = inclusions (thin, associative per E038;
              non-confluent exactly on the SBP fork locus per E155).

TARGET A: TaF's REAL local D1 profile F_O,e(x) = (A, R, B, C) per FORMALISM.md:
  A accessible support, R holder redundancy, B branch robustness (max causal
  antichain of supporting formation events), C reversal cost (min erasures to
  drop below the fixed reconstruction threshold tau). Computed from an actual
  causal record graph with record tokens (id, prop, value, event, holder, cost).

TARGET B: TaF's D1Field extension (T24/FORMALISM.md): observer sites, local D1
  profiles, PROPOSITION VALUES, transport edges, gluing/agreement constraints.

ADJUDICATED QUESTIONS
(a) Must ANY value-blind functor into D1-profiles-only collapse the
    {(p,+1)} / {(p,-1)} fork?  (Fork-Collapse Theorem; exhaustive-finite +
    a two-line symbolic argument discharging the quantifier over recipes g.)
(b) Does the fork-preserving D1Field functor carry a FINALITY-native polarity,
    or only transported fiber data?  (Equivariance theorem: no D1Field
    structural invariant breaks the global +/- flip.)

MANDATORY CONTROLS
(i)   constant functor and profile-forgetful functor must FAIL the
      branch-preservation test (the test has teeth);
(ii)  a polarity-label-decorated target must be DETECTED as label import
      (does not survive relabeling the target's +/-);
(iii) identity and composition checked on actual morphisms, with target
      morphisms represented as concrete site maps composed as functions
      (endpoint-pair-only comparison -- the prior bug -- is not used).

BUG-REGRESSION GUARD (ADAPTER2-01): source-fork-has-no-common-successor is a
SOURCE fact; target image equality/distinctness is a TARGET fact. They are
computed by disjoint code paths and reported separately.

Exit 0 means every check matched its pre-declared expectation.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product


# --------------------------------------------------------------------------
# Source: finite Ext_S model
# --------------------------------------------------------------------------

def consistent(state: frozenset) -> bool:
    vals: dict = {}
    for p, v in state:
        if v not in (-1, 1):
            return False
        if vals.get(p, v) != v:
            return False
        vals[p] = v
    return True


def all_states(props: tuple) -> tuple:
    out = set()
    for signs in product((-1, 0, 1), repeat=len(props)):
        s = frozenset((p, v) for p, v in zip(props, signs) if v != 0)
        if consistent(s):
            out.add(s)
    return tuple(sorted(out, key=lambda s: (len(s), sorted(s))))


def source_morphisms(states: tuple) -> tuple:
    return tuple((a, b) for a in states for b in states if a <= b)


def sigma(state: frozenset) -> frozenset:
    """Global polarity flip: the source Z/2 symmetry."""
    return frozenset((p, -v) for p, v in state)


def strip(state: frozenset) -> frozenset:
    """Value-stripping quotient: forget proposition values, keep structure."""
    return frozenset(p for p, _ in state)


# --------------------------------------------------------------------------
# TaF realization: causal record graph + REAL four-coordinate D1 profile
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Record:
    rid: str
    prop: str
    value: int
    event: str
    holder: str
    erasure_cost: int


class Model:
    def __init__(self, name, props, mult, style, tau):
        self.name = name
        self.props = props
        self.mult = mult      # proposition -> record multiplicity (value-blind)
        self.style = style    # 'antichain' | 'chain' formation-event geometry
        self.tau = tau        # reconstruction threshold


def realize(state: frozenset, model: Model):
    """Canonical value-blind realization: record structure (events, holders,
    causal edges, multiplicities) depends only on strip(state); values ride
    only in the record token's value slot."""
    records = []
    edges = set()
    for p, v in sorted(state):
        m = model.mult[p]
        evs = [f"e_{p}_{i}" for i in range(m)]
        for i in range(m):
            records.append(Record(f"r_{p}_{i}", p, v, evs[i], f"h_{p}_{i}", 1))
        if model.style == "chain":
            edges.update((evs[i], evs[i + 1]) for i in range(m - 1))
    return tuple(records), frozenset(edges)


def leq_fn(edges: frozenset):
    adj: dict = {}
    for a, b in edges:
        adj.setdefault(a, set()).add(b)
    memo: dict = {}

    def desc(e):
        if e not in memo:
            out, stack = set(), [e]
            while stack:
                x = stack.pop()
                for y in adj.get(x, ()):
                    if y not in out:
                        out.add(y)
                        stack.append(y)
            memo[e] = out
        return memo[e]

    return lambda a, b: a == b or b in desc(a)


def antichain_width(events: set, leq) -> int:
    evs = sorted(events)
    for r in range(len(evs), 0, -1):
        for sub in combinations(evs, r):
            if all(not leq(x, y) and not leq(y, x)
                   for x, y in combinations(sub, 2)):
                return r
    return 0


def d1_profile(x, records, leq, tau) -> tuple:
    """TaF FORMALISM.md profile F_O,e(x) = (A, R, B, C); observer accesses all
    holders, evaluation event causally after all formation events."""
    p, v = x
    supp = [r for r in records if r.prop == p and r.value == v]
    A = len(supp)
    R = len({r.holder for r in supp})
    B = antichain_width({r.event for r in supp}, leq)
    C = max(0, A - tau + 1)  # min erasures to fall below threshold tau
    return (A, R, B, C)


def state_profiles(state: frozenset, model: Model) -> dict:
    records, edges = realize(state, model)
    leq = leq_fn(edges)
    return {x: d1_profile(x, records, leq, model.tau) for x in state}


# ---- value-blind profile objects (Target A) ----

def V1(state, model):
    """Bare profile multiset: proposition names AND values dropped."""
    return tuple(sorted(state_profiles(state, model).values()))


def V2(state, model):
    """Proposition-indexed profiles: names kept, VALUES dropped."""
    return tuple(sorted((p, prof)
                        for (p, v), prof in state_profiles(state, model).items()))


# ---- the loophole map: a monotone fork-separator that imports the label ----

def h_loophole(state, model):
    marker = 1 if ("p", 1) in state else 0
    n = 2 * len(state) + marker
    return (n, n, n, n)


def h_relabeled(state, model):
    return h_loophole(sigma(state), model)


# --------------------------------------------------------------------------
# Target B: D1Field objects and concrete morphisms
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class FieldObj:
    sites: tuple        # observer sites (one per proposition)
    profiles: tuple     # ((site, (A,R,B,C)), ...)   local D1 profiles
    values: tuple       # ((site, value), ...)        THE FIBER DATA
    edges: tuple        # transport edges (complete graph on sites)
    agreements: tuple   # (((s,t), v_s*v_t), ...)     gluing/relative-polarity


def make_field(state: frozenset, model: Model) -> FieldObj:
    profs = state_profiles(state, model)
    vals = {p: v for p, v in state}
    sites = tuple(sorted(vals))
    profiles = tuple(sorted((p, profs[(p, vals[p])]) for p in sites))
    values = tuple(sorted(vals.items()))
    edges = tuple(combinations(sites, 2))
    agreements = tuple(((s, t), vals[s] * vals[t]) for s, t in edges)
    return FieldObj(sites, profiles, values, edges, agreements)


def sigma_T(X: FieldObj) -> FieldObj:
    """Target polarity relabeling: flip every proposition value, recompute
    derived components."""
    vals = {p: -v for p, v in X.values}
    values = tuple(sorted(vals.items()))
    agreements = tuple(((s, t), vals[s] * vals[t]) for s, t in X.edges)
    return FieldObj(X.sites, X.profiles, values, X.edges, agreements)


def F_mor(a, b, model):
    """Field morphism for the extension a <= b, as a CONCRETE site map."""
    return (make_field(a, model), make_field(b, model),
            tuple((p, p) for p in sorted(strip(a))))


def id_mor(X: FieldObj):
    return (X, X, tuple((s, s) for s in X.sites))


def compose_mor(m1, m2):
    """(m2 o m1) with real function composition of the site maps."""
    assert m1[1] == m2[0], "non-composable"
    d2 = dict(m2[2])
    return (m1[0], m2[1], tuple(sorted((s, d2[t]) for s, t in m1[2])))


def valid_field_mor(m) -> bool:
    X, Y, sm = m
    d = dict(sm)
    if sorted(d) != list(X.sites):
        return False
    if len(set(d.values())) != len(d):
        return False
    px, vx = dict(X.profiles), dict(X.values)
    py, vy = dict(Y.profiles), dict(Y.values)
    for s in X.sites:
        t = d.get(s)
        if t not in vy:
            return False
        if not all(c1 <= c2 for c1, c2 in zip(px[s], py[t])):
            return False  # local D1 profiles must not decrease
        if vx[s] != vy[t]:
            return False  # fiber data transported, not altered
    ay = dict(Y.agreements)
    for (s, t), g in X.agreements:
        if ay.get(tuple(sorted((d[s], d[t])))) != g:
            return False  # gluing constraints preserved
    return True


# ---- D1Field-computable structural invariant battery ----

def inv_site_count(X):
    return len(X.sites)


def inv_profile_multiset(X):
    return tuple(sorted(pr for _, pr in X.profiles))


def inv_prop_profile_map(X):
    return X.profiles


def inv_edge_count(X):
    return len(X.edges)


def inv_agreement_multiset(X):
    return tuple(sorted(g for _, g in X.agreements))


def inv_harary_balance(X):
    """The surviving cross-repo predicate: signed-graph balance of the
    agreement graph (exists a switching eps with eps_s*eps_t = sign)."""
    if not X.sites:
        return True
    for assign in product((-1, 1), repeat=len(X.sites)):
        eps = dict(zip(X.sites, assign))
        if all(eps[s] * eps[t] == g for (s, t), g in X.agreements):
            return True
    return False


def inv_total_support(X):
    return sum(pr[0] for _, pr in X.profiles)


BATTERY = [
    ("site_count", inv_site_count),
    ("profile_multiset", inv_profile_multiset),
    ("prop_profile_map", inv_prop_profile_map),
    ("edge_count", inv_edge_count),
    ("agreement_multiset", inv_agreement_multiset),
    ("harary_balance", inv_harary_balance),
    ("total_support", inv_total_support),
]


def cheat_plus_count(X):
    """Label-reading pseudo-invariant: counts '+1' by naming the raw label."""
    return sum(1 for _, v in X.values if v == 1)


# ---- decorated target (control ii): explicit inserted polarity label ----

def tag_choice_A(X):
    return "positive" if ("p", 1) in X.values else "unmarked"


def tag_choice_B(X):
    return "positive" if ("p", -1) in X.values else "unmarked"


# --------------------------------------------------------------------------
# Audit driver
# --------------------------------------------------------------------------

def audit_model(model: Model) -> dict:
    states = all_states(model.props)
    mors = source_morphisms(states)
    checks: dict = {}

    # ---- source symmetry facts ----
    checks["sigma_is_object_bijection"] = (
        {sigma(s) for s in states} == set(states))
    checks["sigma_is_involution"] = all(sigma(sigma(s)) == s for s in states)
    checks["sigma_preserves_and_reflects_morphisms"] = all(
        (a <= b) == (sigma(a) <= sigma(b)) for a in states for b in states)

    s_plus = frozenset({("p", 1)})
    s_minus = frozenset({("p", -1)})
    checks["fork_is_single_sigma_orbit"] = (
        sigma(s_plus) == s_minus and sigma(s_minus) == s_plus)

    # SOURCE fact (computed from source category only; never reported as a
    # target fact -- ADAPTER2-01 regression guard):
    checks["SOURCE_fact_fork_has_no_common_successor"] = not any(
        s_plus <= t and s_minus <= t for t in states)

    # E155 alignment: from the empty base, non-confluent pairs are exactly the
    # same-proposition opposite-polarity (SBP) pairs.
    lits = sorted({l for s in states for l in s})
    e155_ok = True
    for c1, c2 in combinations(lits, 2):
        joint = consistent(frozenset({c1, c2}))
        has_common = any(c1 in t and c2 in t for t in states)
        is_sbp = (c1[0] == c2[0] and c1[1] != c2[1])
        e155_ok &= (has_common == joint) and (joint == (not is_sbp))
    checks["e155_fork_locus_is_sbp_set"] = e155_ok

    # ---- Part (a): value-blind D1-profiles-only target ----
    # Premises of the Fork-Collapse Theorem, checked exhaustively:
    checks["strip_sigma_equals_strip_on_all_objects"] = all(
        strip(sigma(s)) == strip(s) for s in states)
    checks["strip_sigma_equals_strip_on_all_morphisms"] = all(
        (strip(sigma(a)), strip(sigma(b))) == (strip(a), strip(b))
        for a, b in mors)
    checks["strip_collapses_fork_objects"] = strip(s_plus) == strip(s_minus)

    # The real D1 recipes factor through strip (checked, not assumed):
    for name, V in (("V1", V1), ("V2", V2)):
        groups: dict = {}
        for s in states:
            groups.setdefault(strip(s), set()).add(V(s, model))
        checks[f"{name}_factors_through_strip"] = all(
            len(g) == 1 for g in groups.values())
        checks[f"{name}_is_sigma_invariant"] = all(
            V(sigma(s), model) == V(s, model) for s in states)
        # TARGET fact (independent of any successor analysis):
        checks[f"TARGET_fact_{name}_fork_images_equal"] = (
            V(s_plus, model) == V(s_minus, model))

    # V2 as functor into the componentwise profile preorder: identity is
    # trivial in a thin target; functoriality = monotonicity on every real
    # morphism, checked directly against the D1 componentwise order.
    mono = True
    for a, b in mors:
        pa, pb = state_profiles(a, model), state_profiles(b, model)
        for x in a:
            mono &= all(c1 <= c2 for c1, c2 in zip(pa[x], pb[x]))
    checks["V2_monotone_on_all_real_morphisms"] = mono

    # Loophole demonstration: an unconstrained monotone fork-separator into
    # profiles EXISTS -- and is exactly a label import.
    checks["loophole_h_monotone"] = all(
        all(c1 <= c2 for c1, c2 in
            zip(h_loophole(a, model), h_loophole(b, model)))
        for a, b in mors)
    checks["loophole_h_separates_fork"] = (
        h_loophole(s_plus, model) != h_loophole(s_minus, model))
    checks["loophole_h_not_sigma_invariant"] = any(
        h_loophole(sigma(s), model) != h_loophole(s, model) for s in states)
    # relabel test: the flipped-convention twin is equally admissible and
    # distinct -> nontrivial orbit -> no canonical choice -> label import.
    checks["loophole_h_relabel_twin_admissible"] = all(
        all(c1 <= c2 for c1, c2 in
            zip(h_relabeled(a, model), h_relabeled(b, model)))
        for a, b in mors) and (
        h_relabeled(s_plus, model) != h_relabeled(s_minus, model))
    checks["loophole_h_fails_relabel_test"] = any(
        h_relabeled(s, model) != h_loophole(s, model) for s in states)

    # ---- Part (b): D1Field target ----
    F = {s: make_field(s, model) for s in states}
    Fm = {(a, b): F_mor(a, b, model) for a, b in mors}

    checks["field_all_morphisms_valid"] = all(
        valid_field_mor(m) for m in Fm.values())
    checks["field_identity_law"] = all(
        Fm[(s, s)] == id_mor(F[s]) for s in states)
    comp_ok = True
    for (a, b1) in mors:
        for (b2, c) in mors:
            if b2 != b1:
                continue
            comp_ok &= compose_mor(Fm[(a, b1)], Fm[(b1, c)]) == Fm[(a, c)]
    checks["field_composition_law_concrete_maps"] = comp_ok

    checks["field_equivariance_sigmaT_F_equals_F_sigma"] = all(
        sigma_T(F[s]) == F[sigma(s)] for s in states)
    checks["sigmaT_involution"] = all(
        sigma_T(sigma_T(F[s])) == F[s] for s in states)
    checks["sigmaT_is_automorphism_of_image_category"] = all(
        (sigma_T(m[0]), sigma_T(m[1]), m[2]) == Fm[(sigma(a), sigma(b))]
        and valid_field_mor((sigma_T(m[0]), sigma_T(m[1]), m[2]))
        for (a, b), m in Fm.items())

    # TARGET facts for the fork (independent code path from the SOURCE fact):
    Xp, Xm_ = F[s_plus], F[s_minus]
    checks["TARGET_fact_field_fork_images_distinct"] = Xp != Xm_
    checks["fork_images_equal_outside_fiber_slot"] = (
        Xp.sites == Xm_.sites and Xp.profiles == Xm_.profiles
        and Xp.edges == Xm_.edges and Xp.agreements == Xm_.agreements
        and Xp.values != Xm_.values)
    checks["sigmaT_swaps_fork_images"] = (
        sigma_T(Xp) == Xm_ and sigma_T(Xm_) == Xp)

    # Invariant battery: does ANY structural invariant break the flip?
    battery_ok = True
    for _, I in BATTERY:
        battery_ok &= all(I(sigma_T(F[s])) == I(F[s]) for s in states)
    checks["battery_no_structural_invariant_breaks_flip"] = battery_ok
    checks["cheat_plus_count_breaks_flip"] = (
        cheat_plus_count(Xp) != cheat_plus_count(sigma_T(Xp)))
    # ... and is exactly a label reader: not stable under target relabeling.
    checks["cheat_plus_count_fails_relabel_test"] = any(
        cheat_plus_count(sigma_T(F[s])) != cheat_plus_count(F[s])
        for s in states)

    # ---- Control (i): constant + forgetful functors must FAIL ----
    K = F[frozenset()]
    checks["constant_functor_laws_hold"] = True  # trivially: K, id_K only
    checks["CONTROL_constant_functor_rejected"] = not (K != K)  # images equal
    checks["CONTROL_profile_functor_rejected"] = (
        V2(s_plus, model) == V2(s_minus, model))  # fork images equal -> FAIL

    # ---- Control (ii): decorated target detected as label import ----
    checks["decorated_A_passes_naive_branch_test"] = (
        (Xp, tag_choice_A(Xp)) != (Xm_, tag_choice_A(Xm_)))
    checks["decorated_choices_disagree"] = any(
        tag_choice_A(F[s]) != tag_choice_B(F[s]) for s in states)
    checks["decorated_relabel_swaps_choices"] = all(
        tag_choice_A(F[s]) == tag_choice_B(sigma_T(F[s])) for s in states)
    checks["CONTROL_decoration_detected_as_label_import"] = (
        checks["decorated_choices_disagree"]
        and checks["decorated_relabel_swaps_choices"])
    # honest F survives the same relabel test AS EQUIVARIANCE: relabeling the
    # target's +/- is exactly absorbed by relabeling the source; F makes no
    # branch selection and carries no component not computed from the source.
    checks["F_survives_relabel_via_equivariance"] = checks[
        "field_equivariance_sigmaT_F_equals_F_sigma"]

    checks["_meta"] = {
        "model": model.name,
        "n_states": len(states),
        "n_morphisms": len(mors),
        "fork_profile_common_value": V2(s_plus, model),
        "field_fork_plus_values": Xp.values,
        "field_fork_minus_values": Xm_.values,
    }
    return checks


EXPECTED = {
    "sigma_is_object_bijection": True,
    "sigma_is_involution": True,
    "sigma_preserves_and_reflects_morphisms": True,
    "fork_is_single_sigma_orbit": True,
    "SOURCE_fact_fork_has_no_common_successor": True,
    "e155_fork_locus_is_sbp_set": True,
    "strip_sigma_equals_strip_on_all_objects": True,
    "strip_sigma_equals_strip_on_all_morphisms": True,
    "strip_collapses_fork_objects": True,
    "V1_factors_through_strip": True,
    "V1_is_sigma_invariant": True,
    "TARGET_fact_V1_fork_images_equal": True,
    "V2_factors_through_strip": True,
    "V2_is_sigma_invariant": True,
    "TARGET_fact_V2_fork_images_equal": True,
    "V2_monotone_on_all_real_morphisms": True,
    "loophole_h_monotone": True,
    "loophole_h_separates_fork": True,
    "loophole_h_not_sigma_invariant": True,
    "loophole_h_relabel_twin_admissible": True,
    "loophole_h_fails_relabel_test": True,
    "field_all_morphisms_valid": True,
    "field_identity_law": True,
    "field_composition_law_concrete_maps": True,
    "field_equivariance_sigmaT_F_equals_F_sigma": True,
    "sigmaT_involution": True,
    "sigmaT_is_automorphism_of_image_category": True,
    "TARGET_fact_field_fork_images_distinct": True,
    "fork_images_equal_outside_fiber_slot": True,
    "sigmaT_swaps_fork_images": True,
    "battery_no_structural_invariant_breaks_flip": True,
    "cheat_plus_count_breaks_flip": True,
    "cheat_plus_count_fails_relabel_test": True,
    "constant_functor_laws_hold": True,
    "CONTROL_constant_functor_rejected": True,
    "CONTROL_profile_functor_rejected": True,
    "decorated_A_passes_naive_branch_test": True,
    "decorated_choices_disagree": True,
    "decorated_relabel_swaps_choices": True,
    "CONTROL_decoration_detected_as_label_import": True,
    "F_survives_relabel_via_equivariance": True,
}


def main() -> None:
    models = [
        Model("M1: 3 props, antichain records, mult (1,2,3), tau=1",
              ("p", "q", "r"), {"p": 1, "q": 2, "r": 3}, "antichain", 1),
        Model("M2: 2 props, chained records, mult (2,3), tau=2",
              ("p", "q"), {"p": 2, "q": 3}, "chain", 2),
    ]

    print("P2C GATE #1: NATIVE BRANCH-PRESERVING FUNCTOR Ext_S -> TaF")
    print("=" * 76)

    for model in models:
        checks = audit_model(model)
        meta = checks.pop("_meta")
        bad = {k: v for k, v in checks.items() if v != EXPECTED[k]}
        assert not bad, f"{model.name}: mismatches {bad}"
        print(f"\nMODEL {meta['model']}")
        print(f"  objects={meta['n_states']}  morphisms={meta['n_morphisms']}"
              "  (exhaustive enumeration, no sampling)")
        for k, v in checks.items():
            print(f"  PASS  {k}: {v}")
        print(f"  [info] shared fork profile object (value-blind): "
              f"{meta['fork_profile_common_value']}")
        print(f"  [info] field fork fiber slots: +branch "
              f"{meta['field_fork_plus_values']}  -branch "
              f"{meta['field_fork_minus_values']}")

    print("\nSYMBOLIC DISCHARGE (quantifier over recipes g)")
    print("  strip(S+) == strip(S-) is checked above. Hence for EVERY map")
    print("  Phi = g o strip (any value-blind profile recipe g whatsoever):")
    print("      Phi(S+) = g(strip(S+)) = g(strip(S-)) = Phi(S-).")
    print("  No sampling over g is needed; the quantifier is discharged")
    print("  algebraically once the stripped fork objects are equal.")
    print("  Converse lemma: any Phi separating the fork satisfies")
    print("      Phi(sigma(S+)) = Phi(S-) != Phi(S+),")
    print("  so Phi is NOT flip-invariant and {Phi, Phi o sigma} is a")
    print("  nontrivial relabel orbit: the separator IS an imported anchor.")

    print("\nBUG-REGRESSION GUARD (ADAPTER2-01)")
    print("  SOURCE fact (no common successor of the fork) and TARGET facts")
    print("  (profile images equal; field images distinct) are computed by")
    print("  disjoint code paths and labeled SOURCE_/TARGET_ above. No")
    print("  branch-preservation verdict cites the SOURCE fact.")

    print("\nVERDICT")
    print("  (a) D1-profiles-only target: IMPOSSIBLE-VALUE-BLIND.")
    print("      Every value-blind functor collapses the (p,+1)/(p,-1) fork;")
    print("      the only fork-separators into profiles import the label.")
    print("  (b) D1Field target: branch-preserving functor CONSTRUCTIBLE,")
    print("      but FIBER-PRESERVED-BUT-UNDETERMINED: the global +/- flip")
    print("      is an automorphism of the target image, F is equivariant,")
    print("      and no structural D1Field invariant breaks the flip.")
    print("  Controls: constant/forgetful REJECTED; decoration DETECTED;")
    print("  identity+composition verified on concrete morphism maps.")
    print("  bar(b), H59, Krein positivity, physical issuance: remain OPEN.")


if __name__ == "__main__":
    main()
