"""P2C ENRICHED-TOY (closer-to-native) Gate #1 fixture: non-thin Ext_S -> multi-observer D1Field.

Exploration tier. Pure Python, no dependencies. No claim promotion.
Addresses the lane-B referee defects D2, D5, D7, D8 at a closer-to-native tier.

SOURCE (non-thin, per RUN-0025's warning that Ext_S must not be replaced by its
thin reflection <=_S):
  objects   = consistent literal-states S (finite sets of (proposition, +/-1))
  morphisms = admissible-extension WITNESSES, not inclusions:
                (S, S', seq, d)
              where seq is an ISSUANCE ORDER (a permutation of S'\\S: the order
              in which the new literals are issued, echoing RUN-0081's
              Iss_n/e_n/w_n shape) and d in {0,1} is an AUDIT DEPTH (a second
              witness datum; composition saturates: min(d1+d2,1)).
              Distinct morphisms between the same objects exist whenever
              |S'\\S| >= 2 (order) or always (depth), so the category is
              genuinely non-thin; its thin reflection is exactly the old
              inclusion preorder.

TARGET (multi-observer D1Field per TaF T24/T26, D1RestrictionSystem-shaped):
  a fixed OBSERVER POPULATION (sites are observers, not proposition names),
  per-observer bounded holder access (FORMALISM.md observer contract),
  per-(site,prop) local D1 profiles (A,R,B,C) computed from a causal record
  graph with SHARED HOLDERS (so R < A somewhere) and CORROBORATION records
  (so profiles STRICTLY INCREASE along some morphisms),
  per-site proposition readouts under per-observer polarity frames eps_o
  (declared, value-blind model data -- a switching frame, not a state datum),
  trusted transport edges over observers (connected in M1, PARTITIONED in M2),
  gluing constraints = per-edge per-prop relative signs (readout products),
  and the T26 global-section predicate over the patch layer.

ADJUDICATED QUESTIONS
 (1) Does the branch-preserving D1Field functor survive the non-thin source
     (functor laws on witness composition, which is order-sensitive)?
 (2) Do morphism-level invariants exist that the thin shadow cannot see
     (RUN-0025's fact, reproduced executably), and is any of them
     sign-selecting?
 (3) Does the multi-observer transport/gluing (patch) layer carry
     sign-selecting data, or is the global flip still an automorphism with the
     fiber undetermined?  Measured concretely: the set of global sections of
     the patch system, its flip-orbit structure, and its size 2^(#components).

CONTROLS: every substantive check has a demonstrated failing direction
(a deliberately broken variant run through the SAME code path and shown to
fail).  See the TEETH_ section.

BUG-REGRESSION GUARD (ADAPTER2-01): source facts and target facts are computed
by disjoint code paths and labeled SOURCE_/TARGET_; no branch-preservation
verdict cites the source no-common-successor fact.

Exit 0 means every check matched its pre-declared expectation.
"""

from __future__ import annotations

from dataclasses import dataclass, replace, field
from itertools import combinations, permutations, product


# ---------------------------------------------------------------------------
# Source objects (shared with toy tier): consistent literal-states
# ---------------------------------------------------------------------------

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


def sigma(state: frozenset) -> frozenset:
    """Global polarity flip on objects."""
    return frozenset((p, -v) for p, v in state)


def strip(state: frozenset) -> frozenset:
    return frozenset(p for p, _ in state)


# ---------------------------------------------------------------------------
# NON-THIN source category: issuance-order + audit-depth witnesses
# ---------------------------------------------------------------------------
# morphism = (dom, cod, seq, d):
#   seq = tuple of literals of cod\dom in issuance order
#   d   = audit depth in {0,1}; identity has d=0; composition saturates.

def source_morphisms(states: tuple) -> tuple:
    mors = []
    for a in states:
        for b in states:
            if a <= b:
                for perm in permutations(sorted(b - a)):
                    for d in (0, 1):
                        mors.append((a, b, tuple(perm), d))
    return tuple(mors)


def id_src(s: frozenset):
    return (s, s, (), 0)


def compose_src(m1, m2):
    """m2 after m1 (diagrammatic: first m1, then m2)."""
    a, b, s1, d1 = m1
    b2, c, s2, d2 = m2
    assert b == b2, "non-composable"
    return (a, c, s1 + s2, min(d1 + d2, 1))


def sigma_mor(m):
    a, b, seq, d = m
    return (sigma(a), sigma(b), tuple((p, -v) for p, v in seq), d)


# broken variants (failing directions for the source-category checks)

def compose_src_uncapped(m1, m2):
    a, b, s1, d1 = m1
    _, c, s2, d2 = m2
    return (a, c, s1 + s2, d1 + d2)          # d=2 leaves the morphism set


def compose_src_nand_depth(m1, m2):
    a, b, s1, d1 = m1
    _, c, s2, d2 = m2
    return (a, c, s1 + s2, 1 - min(d1, d2))  # non-associative depth rule


def sigma_mor_object_only(m):
    a, b, seq, d = m
    return (sigma(a), sigma(b), seq, d)      # forgets to flip the witness


# morphism-level invariants (the RUN-0025 axis)

def inv_first_prop(m):
    """Value-blind: name of the first-issued proposition (None on identities)."""
    _, _, seq, _ = m
    return seq[0][0] if seq else None


def inv_first_sign(m):
    """Label-reading: sign of the first-issued literal."""
    _, _, seq, _ = m
    return seq[0][1] if seq else 0


def inv_audit_depth(m):
    return m[3]


# ---------------------------------------------------------------------------
# TaF realization: causal record graph, shared holders, corroboration
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Record:
    rid: str
    prop: str
    value: int
    event: str
    holder: str


@dataclass(frozen=True)
class Model:
    name: str
    props: tuple
    base_mult: tuple          # ((prop, multiplicity), ...)
    style: str                # 'antichain' | 'chain' base-event geometry
    tau: int
    observers: tuple
    access: tuple             # ((observer, frozenset of holder FAMILIES), ...)
    eps: tuple                # ((observer, +/-1), ...) polarity frames
    tedges: tuple             # trusted transport edges over observers
    corrob: bool = True       # corroboration records (strict growth source)
    unique_holders: bool = False
    interference: bool = False  # BROKEN: presence of others destroys a record

    def mult(self, p):
        return dict(self.base_mult)[p]

    def acc(self, o):
        return dict(self.access)[o]

    def frame(self, o):
        return dict(self.eps)[o]


def holder_family(holder: str) -> str:
    return "h_pool" if holder.startswith("h_pool") else "_".join(
        holder.split("_")[:2])


def realize(state: frozenset, m: Model):
    """Record structure (events, holders, causal edges, multiplicities)
    depends only on strip(state) -- a value-symmetric realization, disclosed
    as a modeling choice (referee D3 caveat carries over). Values ride in the
    record tokens."""
    records, edges = [], set()
    vals = {p: v for p, v in state}
    present = sorted(vals)
    hit = m.interference and len(present) > 1
    base_evs = {}
    for p in present:
        n = m.mult(p) - (1 if hit else 0)
        evs = [f"e_{p}_{i}" for i in range(n)]
        base_evs[p] = evs
        for i, ev in enumerate(evs):
            holder = f"h_{p}_{i}" if m.unique_holders else f"h_{p}"
            records.append(Record(f"r_{p}_{i}", p, vals[p], ev, holder))
        if m.style == "chain":
            edges.update((evs[i], evs[i + 1]) for i in range(n - 1))
    if m.corrob:
        for p in present:
            for q in present:
                if q == p:
                    continue
                ev = f"e_c_{p}_{q}"
                holder = (f"h_pool_{p}_{q}" if m.unique_holders else "h_pool")
                records.append(Record(f"r_c_{p}_{q}", p, vals[p], ev, holder))
                for e2 in base_evs[p] + base_evs[q]:
                    edges.add((e2, ev))
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


def site_profile(x, records, leq, m: Model, o: str) -> tuple:
    """Per-OBSERVER local D1 profile F_O,e(x) = (A,R,B,C): bounded holder
    access per FORMALISM.md; R counts distinct holder tokens, A counts
    records, so shared holders give R < A."""
    p, v = x
    acc = m.acc(o)
    supp = [r for r in records
            if r.prop == p and r.value == v and holder_family(r.holder) in acc]
    A = len(supp)
    R = len({r.holder for r in supp})
    B = antichain_width({r.event for r in supp}, leq)
    C = max(0, A - m.tau + 1)
    return (A, R, B, C)


# ---------------------------------------------------------------------------
# Multi-observer D1Field target objects and morphisms
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class FieldObj:
    sites: tuple       # OBSERVERS (a population), not proposition names
    profiles: tuple    # ((site, prop, (A,R,B,C)), ...) for all present props
    values: tuple      # (((site, prop), readout), ...) only where A >= 1
    edges: tuple       # trusted transport edges among observers
    agreements: tuple  # ((edge, prop, relative sign), ...) gluing constraints


def compute_agreements(values: dict, tedges, props):
    out = []
    for (s, t) in tedges:
        for p in props:
            if (s, p) in values and (t, p) in values:
                out.append(((s, t), p, values[(s, p)] * values[(t, p)]))
    return tuple(sorted(out))


def make_field(state: frozenset, m: Model, corrupt: bool = False) -> FieldObj:
    records, eedges = realize(state, m)
    leq = leq_fn(eedges)
    vals = {p: v for p, v in state}
    present = sorted(vals)
    profiles, values = [], {}
    for o in m.observers:
        for p in present:
            prof = site_profile((p, vals[p]), records, leq, m, o)
            profiles.append((o, p, prof))
            if prof[0] >= 1:
                values[(o, p)] = m.frame(o) * vals[p]
    agreements = list(compute_agreements(values, m.tedges, present))
    if corrupt and agreements:
        e, p, g = agreements[0]
        agreements[0] = (e, p, -g)   # simulated corrupted transport edge
    return FieldObj(tuple(m.observers), tuple(sorted(profiles)),
                    tuple(sorted(values.items())), tuple(m.tedges),
                    tuple(sorted(agreements)))


def sigma_T(X: FieldObj) -> FieldObj:
    """Global target flip: negate every per-site readout. Agreements are
    relative signs (degree-2 products), hence carried unchanged."""
    return replace(X, values=tuple(sorted((k, -v) for k, v in X.values)))


def sigma_T_single_site(X: FieldObj, site: str) -> FieldObj:
    """BROKEN flip: negates readouts at one site only."""
    return replace(X, values=tuple(sorted(
        (k, -v if k[0] == site else v) for k, v in X.values)))


def forget_values(X: FieldObj) -> FieldObj:
    """CONTROL: keep sites, profiles, edges AND the whole gluing layer;
    forget only absolute readouts."""
    return replace(X, values=())


def odd_degree_gluing(X: FieldObj):
    """BROKEN transport datum: stores an ABSOLUTE endpoint readout per edge
    (odd degree in readouts) instead of the relative sign."""
    vals = dict(X.values)
    return tuple(sorted(((s, t), p, vals[(s, p)])
                        for (s, t), p, _ in X.agreements))


def cheat_named_slot_readout(X: FieldObj):
    """Label-reading pseudo-invariant: the absolute readout at a NAMED site
    for a NAMED proposition. Breaks the flip on the fork and is exactly a
    relabel-test failure. (A subtler candidate, 'count of +1 readouts', is
    NOT even guaranteed to break the flip: under mixed observer frames the
    fork's +/- counts can balance -- measured and reported as a finding.)"""
    return dict(X.values).get(("o1", "p"))


def plus_count(X: FieldObj) -> int:
    return sum(1 for _, v in X.values if v == 1)


# target morphisms: fixed observer population, order-carrying prop schedule

def F_mor(m_src, model: Model, fields: dict):
    a, b, seq, _d = m_src              # audit depth d is FORGOTTEN (disclosed)
    return (fields[a], fields[b], tuple(p for p, _v in seq))


def id_tmor(X: FieldObj):
    return (X, X, ())


def compose_tmor(t1, t2):
    assert t1[1] == t2[0], "non-composable"
    return (t1[0], t2[1], t1[2] + t2[2])


def compose_tmor_reversed(t1, t2):
    return (t1[0], t2[1], t2[2] + t1[2])     # BROKEN: reverses issuance order


def F_mor_audit(m_src, model: Model, fields: dict):
    """BROKEN functor: tries to carry the audit depth as extra schedule
    marks; saturating source depth vs concatenating schedule cannot agree."""
    a, b, seq, d = m_src
    return (fields[a], fields[b], tuple(p for p, _v in seq) + ("audit",) * d)


def F_mor_sentinel(m_src, model: Model, fields: dict):
    """BROKEN functor: appends a sentinel to every schedule (identities
    included) -- fails the identity law."""
    a, b, seq, _d = m_src
    return (fields[a], fields[b], tuple(p for p, _v in seq) + ("sentinel",))


def valid_field_mor(t) -> bool:
    X, Y, sched = t
    if X.sites != Y.sites:
        return False
    px = {(o, p): pr for o, p, pr in X.profiles}
    py = {(o, p): pr for o, p, pr in Y.profiles}
    props_x = {p for _o, p, _pr in X.profiles}
    props_y = {p for _o, p, _pr in Y.profiles}
    if len(set(sched)) != len(sched) or (set(sched) & props_x):
        return False
    if props_x | set(sched) != props_y:
        return False
    for key, pr in px.items():
        if key not in py:
            return False
        if not all(c1 <= c2 for c1, c2 in zip(pr, py[key])):
            return False                     # local D1 must not decrease
    vy = dict(Y.values)
    for k, v in dict(X.values).items():
        if vy.get(k) != v:
            return False                     # readouts transported, not altered
    ay = {(e, p): g for e, p, g in Y.agreements}
    for e, p, g in X.agreements:
        if ay.get((e, p)) != g:
            return False                     # gluing constraints preserved
    return True


# ---------------------------------------------------------------------------
# Patch layer: T26-style global sections over the gluing constraints
# ---------------------------------------------------------------------------

def global_sections(X: FieldObj) -> tuple:
    slots = tuple(sorted(k for k, _ in X.values))
    out = []
    for assign in product((-1, 1), repeat=len(slots)):
        x = dict(zip(slots, assign))
        if all(x[(s, p)] * x[(t, p)] == g for (s, t), p, g in X.agreements):
            out.append(tuple(sorted(x.items())))
    return tuple(out)


def flip_section(sec):
    return tuple(sorted((k, -v) for k, v in sec))


def component_count(X: FieldObj) -> int:
    """Number of (proposition, transport-component) blocks over DEFINED
    slots; balanced patch systems have exactly 2^count global sections."""
    slots = [k for k, _ in X.values]
    props = sorted({p for _s, p in slots})
    total = 0
    for p in props:
        sites = [s for s, pp in slots if pp == p]
        parent = {s: s for s in sites}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for (s, t), pp, _g in X.agreements:
            if pp == p:
                parent[find(s)] = find(t)
        total += len({find(s) for s in sites})
    return total


def section_selector(X: FieldObj):
    """A definable selector (lexicographically least section). Exhibited to
    show that ANY such selector fails the relabel test."""
    secs = global_sections(X)
    return min(secs) if secs else None


# ---------------------------------------------------------------------------
# Audit driver
# ---------------------------------------------------------------------------

def out_map(mors):
    om: dict = {}
    for m in mors:
        om.setdefault(m[0], []).append(m)
    return om


def audit_model(model: Model):
    checks: dict = {}
    meta: dict = {}
    states = all_states(model.props)
    mors = source_morphisms(states)
    mor_set = set(mors)
    om = out_map(mors)
    comp_pairs = [(m1, m2) for m1 in mors for m2 in om.get(m1[1], ())]
    meta["n_states"], meta["n_morphisms"] = len(states), len(mors)
    meta["n_composable_pairs"] = len(comp_pairs)

    # ---------------- SOURCE: non-thin category facts ----------------
    checks["src_composition_closed"] = all(
        compose_src(m1, m2) in mor_set for m1, m2 in comp_pairs)
    checks["src_identity_neutral"] = all(
        compose_src(id_src(m[0]), m) == m and compose_src(m, id_src(m[1])) == m
        for m in mors)
    n_triples = 0
    assoc = True
    for m1, m2 in comp_pairs:
        for m3 in om.get(m2[1], ()):
            n_triples += 1
            assoc &= (compose_src(compose_src(m1, m2), m3)
                      == compose_src(m1, compose_src(m2, m3)))
    checks["src_associativity_exhaustive"] = assoc
    meta["n_composable_triples"] = n_triples

    checks["sigma_src_object_bijection"] = (
        {sigma(s) for s in states} == set(states))
    checks["sigma_src_morphism_bijection"] = (
        {sigma_mor(m) for m in mors} == mor_set)
    checks["sigma_src_preserves_identity_and_composition"] = all(
        sigma_mor(id_src(s)) == id_src(sigma(s)) for s in states) and all(
        sigma_mor(compose_src(m1, m2))
        == compose_src(sigma_mor(m1), sigma_mor(m2))
        for m1, m2 in comp_pairs)
    checks["sigma_src_involution"] = all(
        sigma_mor(sigma_mor(m)) == m for m in mors)

    s_plus = frozenset({("p", 1)})
    s_minus = frozenset({("p", -1)})
    empty = frozenset()
    checks["fork_objects_single_sigma_orbit"] = (
        sigma(s_plus) == s_minus and sigma(s_minus) == s_plus)
    plus_issuers = {m for m in mors if m[0] == empty and m[1] == s_plus}
    minus_issuers = {m for m in mors if m[0] == empty and m[1] == s_minus}
    checks["fork_issuing_morphisms_swapped_by_sigma"] = (
        {sigma_mor(m) for m in plus_issuers} == minus_issuers)

    # SOURCE fact -- disjoint code path from every target fact (ADAPTER2-01):
    checks["SOURCE_fact_fork_no_common_successor"] = not any(
        s_plus <= t and s_minus <= t for t in states)

    # RUN-0025's fact, executable: parallel distinct morphisms exist, and a
    # morphism-level invariant does not factor through the thin shadow.
    parallel = {}
    for m in mors:
        parallel.setdefault((m[0], m[1]), []).append(m)
    par_multi = {k: v for k, v in parallel.items() if len(v) > 1}
    checks["nonthin_parallel_distinct_morphisms_exist"] = len(par_multi) > 0
    meta["n_parallel_classes_with_multiplicity"] = len(par_multi)
    checks["nonthin_first_prop_invariant_not_thin_definable"] = any(
        len({inv_first_prop(m) for m in v}) > 1 for v in par_multi.values())
    checks["nonthin_first_prop_invariant_is_flip_invariant"] = all(
        inv_first_prop(sigma_mor(m)) == inv_first_prop(m) for m in mors)
    checks["nonthin_audit_depth_distinguishes_parallel_morphisms"] = any(
        len({inv_audit_depth(m) for m in v}) > 1 for v in par_multi.values())
    # the label-reading morphism invariant: separates the fork issuers but
    # fails the relabel test (its sigma-conjugate is distinct and equally
    # admissible: a nontrivial orbit, no canonical choice).
    checks["MOR_INV_first_sign_separates_fork_issuers"] = (
        {inv_first_sign(m) for m in plus_issuers}
        != {inv_first_sign(m) for m in minus_issuers})
    checks["MOR_INV_first_sign_fails_relabel_test"] = any(
        inv_first_sign(sigma_mor(m)) != inv_first_sign(m) for m in mors)

    # ---------------- TARGET: realization non-degeneracy ----------------
    fields = {s: make_field(s, model) for s in states}
    thin_pairs = sorted({(m[0], m[1]) for m in mors},
                        key=lambda ab: (sorted(ab[0]), sorted(ab[1])))

    strict = {0: 0, 1: 0, 2: 0, 3: 0}     # per-coordinate strict increases
    strict_b_nonzero_base = 0             # B growth not explained by 0 -> k
    for a, b in thin_pairs:
        pa = {(o, p): pr for o, p, pr in fields[a].profiles}
        pb = {(o, p): pr for o, p, pr in fields[b].profiles}
        for key, pr in pa.items():
            for i in range(4):
                if pb[key][i] > pr[i]:
                    strict[i] += 1
            if pb[key][2] > pr[2] >= 1:
                strict_b_nonzero_base += 1
    for i, cname in enumerate("ARBC"):
        checks[f"realization_strict_growth_{cname}_present"] = strict[i] > 0
    meta["strict_growth_instances_ARBC"] = tuple(strict[i] for i in range(4))
    meta["strict_B_growth_from_nonzero_base"] = strict_b_nonzero_base

    rlta = sum(1 for X in fields.values()
               for _o, _p, (A, R, _B, _C) in X.profiles if 0 < R < A)
    checks["redundancy_strictly_below_support_somewhere"] = rlta > 0
    meta["R_lt_A_instances"] = rlta

    hetero = 0
    for X in fields.values():
        by_prop: dict = {}
        for o, p, pr in X.profiles:
            by_prop.setdefault(p, set()).add(pr)
        hetero += sum(1 for v in by_prop.values() if len(v) > 1)
    checks["site_profiles_heterogeneous_somewhere"] = hetero > 0
    meta["heterogeneous_site_profile_instances"] = hetero

    mixed = sum(1 for X in fields.values()
                for _e, _p, g in X.agreements if g == -1)
    checks["mixed_sign_agreements_present"] = mixed > 0
    meta["negative_agreement_instances"] = mixed

    checks["agreements_match_readout_products"] = all(
        X.agreements == compute_agreements(
            dict(X.values), X.edges, sorted({p for _o, p, _pr in X.profiles}))
        for X in fields.values())

    # ---------------- FUNCTOR on the non-thin category ----------------
    Fm = {m: F_mor(m, model, fields) for m in mors}
    checks["F_all_image_morphisms_valid"] = all(
        valid_field_mor(t) for t in Fm.values())
    checks["F_identity_law"] = all(
        Fm[id_src(s)] == id_tmor(fields[s]) for s in states)
    checks["F_composition_law_all_pairs"] = all(
        compose_tmor(Fm[m1], Fm[m2]) == Fm[compose_src(m1, m2)]
        for m1, m2 in comp_pairs)
    checks["F_not_faithful_audit_depth_forgotten"] = any(
        len(v) > 1 and len({Fm[m] for m in v}) < len(v)
        for v in par_multi.values())

    # TARGET facts (disjoint code path from the SOURCE fact):
    Xp, Xm = fields[s_plus], fields[s_minus]
    checks["TARGET_fact_field_fork_images_distinct"] = Xp != Xm
    checks["fork_images_differ_only_in_values_slot"] = (
        Xp.sites == Xm.sites and Xp.profiles == Xm.profiles
        and Xp.edges == Xm.edges and Xp.agreements == Xm.agreements
        and Xp.values != Xm.values)

    # ---------------- FLIP: automorphism + equivariance ----------------
    checks["sigmaT_involution"] = all(
        sigma_T(sigma_T(X)) == X for X in fields.values())
    checks["equivariance_on_objects"] = all(
        sigma_T(fields[s]) == fields[sigma(s)] for s in states)
    checks["equivariance_on_morphisms"] = all(
        (sigma_T(t[0]), sigma_T(t[1]), t[2]) == Fm[sigma_mor(m)]
        for m, t in Fm.items())
    checks["sigmaT_automorphism_of_image"] = all(
        valid_field_mor((sigma_T(t[0]), sigma_T(t[1]), t[2]))
        for t in Fm.values())
    checks["gluing_products_flip_invariant_recomputed"] = all(
        compute_agreements(
            {k: -v for k, v in dict(X.values).items()}, X.edges,
            sorted({p for _o, p, _pr in X.profiles})) == X.agreements
        for X in fields.values())
    checks["CONTROL_gluing_kept_values_forgotten_collapses_fork"] = (
        forget_values(Xp) == forget_values(Xm))
    checks["cheat_named_slot_readout_breaks_flip_and_fails_relabel"] = (
        cheat_named_slot_readout(Xp) != cheat_named_slot_readout(sigma_T(Xp))
        ) and any(
        cheat_named_slot_readout(sigma_T(X)) != cheat_named_slot_readout(X)
        for X in fields.values() if dict(X.values).get(("o1", "p")))
    # measured finding, not a control: does the naive '+1 count' break the
    # flip at the fork? Under mixed eps frames it can balance out.
    meta["plus_count_breaks_flip_at_fork"] = (
        plus_count(Xp) != plus_count(sigma_T(Xp)))

    # ---------------- PATCH LAYER: global sections and the fiber ----------
    secs = {s: global_sections(fields[s]) for s in states}
    checks["readout_is_a_global_section"] = all(
        tuple(sorted(dict(fields[s].values).items())) in secs[s]
        for s in states)
    checks["section_set_flip_closed"] = all(
        {flip_section(sec) for sec in secs[s]} == set(secs[s])
        for s in states)
    slotted = [s for s in states if fields[s].values]
    checks["no_flip_fixed_section"] = all(
        flip_section(sec) != sec for s in slotted for sec in secs[s])
    checks["section_count_equals_2_pow_components"] = all(
        len(secs[s]) == 2 ** component_count(fields[s]) for s in states)
    checks["fork_section_count_is_two"] = (
        len(secs[s_plus]) == 2 and len(secs[s_minus]) == 2)
    full = max(states, key=lambda s: (len(s), sorted(s)))
    meta["fork_sections"] = len(secs[s_plus])
    meta["largest_state"] = tuple(sorted(full))
    meta["largest_state_components"] = component_count(fields[full])
    meta["largest_state_sections"] = len(secs[full])
    # any definable selector fails the relabel test: conjugating the
    # lexicographic selector by the flip picks the OTHER section.
    checks["FIBER_section_selector_fails_relabel"] = all(
        flip_section(section_selector(sigma_T(fields[s])))
        != section_selector(fields[s]) for s in slotted)

    return checks, meta


# ---------------------------------------------------------------------------
# TEETH: demonstrated failing directions for every substantive check
# ---------------------------------------------------------------------------

def audit_teeth(model: Model):
    """Each entry is True iff the deliberately broken variant FAILS the same
    predicate the honest run passes (same code paths)."""
    t: dict = {}
    states = all_states(model.props)
    mors = source_morphisms(states)
    mor_set = set(mors)
    om = out_map(mors)
    comp_pairs = [(m1, m2) for m1 in mors for m2 in om.get(m1[1], ())]
    fields = {s: make_field(s, model) for s in states}
    Fm = {m: F_mor(m, model, fields) for m in mors}

    # source-category checks have failing directions
    t["TEETH_uncapped_depth_breaks_closure"] = any(
        compose_src_uncapped(m1, m2) not in mor_set for m1, m2 in comp_pairs)
    assoc_broken = False
    for m1, m2 in comp_pairs:
        for m3 in om.get(m2[1], ()):
            if (compose_src_nand_depth(compose_src_nand_depth(m1, m2), m3)
                    != compose_src_nand_depth(
                        m1, compose_src_nand_depth(m2, m3))):
                assoc_broken = True
                break
        if assoc_broken:
            break
    t["TEETH_nand_depth_breaks_associativity"] = assoc_broken
    t["TEETH_object_only_sigma_leaves_category"] = any(
        sigma_mor_object_only(m) not in mor_set for m in mors)

    # realization checks have failing directions
    m_no_corrob = replace(model, corrob=False, name=model.name + "/no-corrob")
    f_nc = {s: make_field(s, m_no_corrob) for s in states}
    strict_any = False
    for m in mors:
        pa = {(o, p): pr for o, p, pr in f_nc[m[0]].profiles}
        pb = {(o, p): pr for o, p, pr in f_nc[m[1]].profiles}
        strict_any |= any(any(pb[k][i] > pr[i] for i in range(4))
                          for k, pr in pa.items())
    t["TEETH_corroboration_off_kills_strict_growth"] = not strict_any

    m_intf = replace(model, interference=True, name=model.name + "/interf")
    f_it = {s: make_field(s, m_intf) for s in states}
    t["TEETH_interference_breaks_monotonicity"] = any(
        not valid_field_mor(F_mor(m, m_intf, f_it)) for m in mors)

    m_uh = replace(model, unique_holders=True, name=model.name + "/uniqueH")
    f_uh = {s: make_field(s, m_uh) for s in states}
    t["TEETH_unique_holders_kill_R_lt_A"] = not any(
        0 < R < A for X in f_uh.values() for _o, _p, (A, R, _B, _C)
        in X.profiles)

    all_fams = frozenset(
        {f"h_{p}" for p in model.props} | {"h_pool"})
    m_ua = replace(model,
                   access=tuple((o, all_fams) for o in model.observers),
                   name=model.name + "/uniform-access")
    f_ua = {s: make_field(s, m_ua) for s in states}
    het = False
    for X in f_ua.values():
        by_prop: dict = {}
        for o, p, pr in X.profiles:
            by_prop.setdefault(p, set()).add(pr)
        het |= any(len(v) > 1 for v in by_prop.values())
    t["TEETH_uniform_access_kills_site_heterogeneity"] = not het

    m_ue = replace(model, eps=tuple((o, 1) for o in model.observers),
                   name=model.name + "/uniform-eps")
    f_ue = {s: make_field(s, m_ue) for s in states}
    t["TEETH_uniform_eps_kills_mixed_agreements"] = not any(
        g == -1 for X in f_ue.values() for _e, _p, g in X.agreements)

    # functor checks have failing directions
    t["TEETH_reversed_schedule_breaks_composition_law"] = any(
        compose_tmor_reversed(Fm[m1], Fm[m2]) != Fm[compose_src(m1, m2)]
        for m1, m2 in comp_pairs)
    Fa = {m: F_mor_audit(m, model, fields) for m in mors}
    t["TEETH_audit_carrying_functor_breaks_composition_law"] = any(
        compose_tmor(Fa[m1], Fa[m2]) != Fa[compose_src(m1, m2)]
        for m1, m2 in comp_pairs)
    t["TEETH_sentinel_functor_breaks_identity_law"] = any(
        F_mor_sentinel(id_src(s), model, fields) != id_tmor(fields[s])
        for s in states)

    # morphism-validity legs have failing directions
    two = next(s for s in states if len(s) == 2)
    sub = next(s for s in states if len(s) == 1 and s <= two)
    sched = tuple(sorted(strip(two) - strip(sub)))
    t["TEETH_corrupt_agreement_detected_invalid"] = not valid_field_mor(
        (fields[two], make_field(two, model, corrupt=True), ()))
    t["TEETH_flipped_target_values_detected_invalid"] = not valid_field_mor(
        (fields[sub], sigma_T(fields[two]), sched))

    # flip checks have failing directions
    site0 = model.observers[0]
    t["TEETH_single_site_flip_breaks_equivariance"] = any(
        sigma_T_single_site(fields[s], site0) != fields[sigma(s)]
        for s in states)
    t["TEETH_single_site_flip_breaks_gluing_consistency"] = any(
        compute_agreements(
            dict(sigma_T_single_site(X, site0).values), X.edges,
            sorted({p for _o, p, _pr in X.profiles})) != X.agreements
        for X in fields.values() if X.values)
    t["TEETH_odd_degree_gluing_datum_breaks_flip_invariance"] = any(
        odd_degree_gluing(sigma_T(X)) != odd_degree_gluing(X)
        for X in fields.values() if X.agreements)

    # patch-layer checks have failing directions
    Xc = make_field(two, model, corrupt=True)
    t["TEETH_corrupt_agreement_creates_gluing_obstruction"] = (
        len(global_sections(Xc)) == 0
        and len(global_sections(fields[two])) > 0)
    t["TEETH_corrupt_breaks_product_consistency"] = (
        Xc.agreements != compute_agreements(
            dict(Xc.values), Xc.edges,
            sorted({p for _o, p, _pr in Xc.profiles})))
    return t


# ---------------------------------------------------------------------------
# Expectations (the adjudication contract) and driver
# ---------------------------------------------------------------------------

MAIN_EXPECTED_TRUE = [
    "src_composition_closed", "src_identity_neutral",
    "src_associativity_exhaustive",
    "sigma_src_object_bijection", "sigma_src_morphism_bijection",
    "sigma_src_preserves_identity_and_composition", "sigma_src_involution",
    "fork_objects_single_sigma_orbit",
    "fork_issuing_morphisms_swapped_by_sigma",
    "SOURCE_fact_fork_no_common_successor",
    "nonthin_parallel_distinct_morphisms_exist",
    "nonthin_first_prop_invariant_not_thin_definable",
    "nonthin_first_prop_invariant_is_flip_invariant",
    "nonthin_audit_depth_distinguishes_parallel_morphisms",
    "MOR_INV_first_sign_separates_fork_issuers",
    "MOR_INV_first_sign_fails_relabel_test",
    "realization_strict_growth_A_present",
    "realization_strict_growth_R_present",
    "realization_strict_growth_B_present",
    "realization_strict_growth_C_present",
    "redundancy_strictly_below_support_somewhere",
    "site_profiles_heterogeneous_somewhere",
    "mixed_sign_agreements_present",
    "agreements_match_readout_products",
    "F_all_image_morphisms_valid", "F_identity_law",
    "F_composition_law_all_pairs",
    "F_not_faithful_audit_depth_forgotten",
    "TARGET_fact_field_fork_images_distinct",
    "fork_images_differ_only_in_values_slot",
    "sigmaT_involution", "equivariance_on_objects",
    "equivariance_on_morphisms", "sigmaT_automorphism_of_image",
    "gluing_products_flip_invariant_recomputed",
    "CONTROL_gluing_kept_values_forgotten_collapses_fork",
    "cheat_named_slot_readout_breaks_flip_and_fails_relabel",
    "readout_is_a_global_section", "section_set_flip_closed",
    "no_flip_fixed_section", "section_count_equals_2_pow_components",
    "fork_section_count_is_two",
    "FIBER_section_selector_fails_relabel",
]

# No model-specific overrides: every listed check is expected True on both
# models. (A first-draft override predicting no strict B-growth in M2 was
# wrong -- B grows 0 -> 1 when a pool-only observer gains its first
# accessible formation event; the run corrected the prediction and the
# nonzero-base B-growth count is reported separately as a measurement.)
OVERRIDES: dict = {}


def build_models():
    m1 = Model(
        name="M1",
        props=("p", "q", "r"),
        base_mult=(("p", 2), ("q", 2), ("r", 3)),
        style="antichain",
        tau=2,
        observers=("o1", "o2", "o3"),
        access=(("o1", frozenset({"h_p", "h_q", "h_r", "h_pool"})),
                ("o2", frozenset({"h_p", "h_q", "h_r"})),
                ("o3", frozenset({"h_pool"}))),
        eps=(("o1", 1), ("o2", 1), ("o3", -1)),
        tedges=(("o1", "o2"), ("o2", "o3"), ("o1", "o3")),
    )
    m2 = Model(
        name="M2",
        props=("p", "q"),
        base_mult=(("p", 2), ("q", 1)),
        style="chain",
        tau=1,
        observers=("o1", "o2", "o3"),
        access=(("o1", frozenset({"h_p", "h_q", "h_pool"})),
                ("o2", frozenset({"h_p", "h_q"})),
                ("o3", frozenset({"h_pool"}))),
        eps=(("o1", 1), ("o2", -1), ("o3", 1)),
        tedges=(("o1", "o2"),),   # PARTITIONED transport: o3 isolated
    )
    return [m1, m2]


def main() -> None:
    print("P2C ENRICHED-TOY (closer-to-native) GATE #1: NON-THIN Ext_S -> MULTI-OBSERVER D1FIELD")
    print("=" * 76)
    models = build_models()
    failures = []

    for model in models:
        checks, meta = audit_model(model)
        print(f"\nMODEL {model.name}: props={model.props} "
              f"base_mult={dict(model.base_mult)} style={model.style} "
              f"tau={model.tau}")
        print(f"  observers={model.observers} transport={model.tedges}")
        print(f"  eps frames={dict(model.eps)}")
        print(f"  objects={meta['n_states']}  "
              f"nonthin_morphisms={meta['n_morphisms']}  "
              f"composable_pairs={meta['n_composable_pairs']}  "
              f"composable_triples={meta['n_composable_triples']}  "
              "(exhaustive, no sampling)")
        for k in MAIN_EXPECTED_TRUE:
            expected = OVERRIDES.get((model.name, k), True)
            ok = checks[k] == expected
            tag = "PASS " if ok else "FAIL "
            note = "" if expected else "  [expected ABSENT here, declared]"
            print(f"  {tag} {k}: {checks[k]}{note}")
            if not ok:
                failures.append((model.name, k, checks[k], expected))
        print(f"  [info] strict-growth instances (A,R,B,C): "
              f"{meta['strict_growth_instances_ARBC']}  "
              f"(B-growth from nonzero base: "
              f"{meta['strict_B_growth_from_nonzero_base']})")
        print(f"  [info] naive '+1 count' breaks flip at fork: "
              f"{meta['plus_count_breaks_flip_at_fork']} "
              "(frame-dependent; not a reliable label-reader)")
        print(f"  [info] R<A instances: {meta['R_lt_A_instances']}   "
              f"heterogeneous-site instances: "
              f"{meta['heterogeneous_site_profile_instances']}   "
              f"negative agreements: {meta['negative_agreement_instances']}")
        print(f"  [info] parallel morphism classes with multiplicity: "
              f"{meta['n_parallel_classes_with_multiplicity']}")
        print(f"  [info] fork sections: {meta['fork_sections']}   "
              f"largest state {meta['largest_state']}: "
              f"components={meta['largest_state_components']}, "
              f"sections={meta['largest_state_sections']} "
              f"(= 2^components)")

    print("\nTEETH SUITE (failing directions; broken variants through the "
          "SAME code paths, on M1)")
    teeth = audit_teeth(models[0])
    for k, v in teeth.items():
        ok = v is True
        print(f"  {'PASS ' if ok else 'FAIL '} {k}: {v}")
        if not ok:
            failures.append(("M1-teeth", k, v, True))

    print("\nBUG-REGRESSION GUARD (ADAPTER2-01)")
    print("  The SOURCE fact (fork has no common successor) and the TARGET")
    print("  facts (field fork images distinct; profiles/agreements equal)")
    print("  are computed by disjoint code paths and labeled SOURCE_/TARGET_.")
    print("  No branch-preservation verdict cites the SOURCE fact.")

    print("\nVERDICT (exploration tier; exhaustive-finite on these models)")
    print("  1. The branch-preserving D1Field functor SURVIVES the non-thin")
    print("     source: functor laws hold on order-sensitive witness")
    print("     composition; the audit-depth witness is forgotten (F is not")
    print("     faithful) -- disclosed, not hidden.")
    print("  2. Morphism-level invariants beyond the thin shadow EXIST")
    print("     (issuance order, audit depth) -- RUN-0025's warning is")
    print("     reproduced executably -- and every value-blind one is")
    print("     flip-invariant; the only fork-separating morphism invariant")
    print("     found reads the +/- label and fails the relabel test.")
    print("  3. At multi-observer tier the flip is STILL an automorphism and")
    print("     F is equivariant. The patch layer pins exactly the relative")
    print("     polarities: the T26 global-section set has size")
    print("     2^(#(prop,transport-component)) and is a free Z/2-torsor per")
    print("     block; the global flip is the diagonal. No transport/gluing")
    print("     datum selects a section: even-degree (relative) data are")
    print("     flip-invariant, and odd-degree (absolute) data fail the")
    print("     relabel test. Partitioned transport (M2) makes the")
    print("     undetermined fiber STRICTLY LARGER than one global sign.")
    print("  bar(b), H59, Krein positivity, physical issuance: remain OPEN.")

    if failures:
        print(f"\nMISMATCHES: {failures}")
        raise SystemExit(1)
    print("\nAll checks matched pre-declared expectations. Exit 0.")


if __name__ == "__main__":
    main()
