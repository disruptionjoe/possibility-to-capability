> Part of the 2026-07-16 P2C swing 2 (four adversarially-refereed lanes). Exploration tier; no claim promotion; the attached referee report GOVERNS the grades — read it before citing the lane report.

Exit 0, all checks matched pre-declared expectations. The deliverable follows.

---

# NATIVE-TIER Gate #1: non-thin Ext_S → multi-observer D1Field — executable adjudication

Exploration tier. No claim promotion. Nothing here reopens the withdrawn ADAPTER2-01 identity or moves any source-repo claim. `bar(b)`, H59, Krein positivity, physical issuance remain OPEN. This lifts the 2026-07-16 lane-B toy result along the referee's own defect list (D2, D5, D7, D8), which was treated as the spec.

Fixture: `<local-scratchpad>/gate1_native_nonthin_multiobserver.py` (pure Python, no deps, exit 0, runtime <1s). Recommend persisting to `possibility-to-capability/tests/gate1_native_nonthin_multiobserver.py` alongside the toy fixture (referee D9: scratchpad evidence evaporates); persistence left to the orchestrator.

## 1. What was built (and how it differs from the toy)

**Source — non-thin Ext_S** (addresses D5 / RUN-0025's "thin shadow" caveat directly). Objects: consistent literal-states. Morphisms are extension *witnesses*, not inclusions: `(S, S', seq, d)` where `seq` is an issuance order (a permutation of `S'\S`, echoing RUN-0081's `Iss_n/e_n/w_n` shape) and `d ∈ {0,1}` is an audit depth with saturating composition `min(d1+d2,1)`. Distinct parallel morphisms between the same objects exist (125 parallel classes with multiplicity in M1, 25 in M2); the thin reflection is exactly the old inclusion preorder. Category axioms (closure, identity, associativity) verified exhaustively: M1 = 27 objects / 402 morphisms / 2,172 composable pairs / 8,808 composable triples; M2 = 9 / 58 / 228 / 744. No sampling.

**Target — multi-observer D1Field** (addresses D7, D8, D2). Sites are *observers* (a population of 3), not proposition names. Per-observer bounded holder access (FORMALISM.md observer contract); records with **shared holders** so R < A (132 instances in M1, 12 in M2); **corroboration records** on a communal pool holder so profiles **strictly increase** along morphisms — all four coordinates A, R, B, C have strict-growth instances in both models (M1: 192/96/96/168; M2: 16/16/8/16; B-growth from a nonzero base: 48 in M1, 0 in M2 — reported as a measurement). Per-site readouts under per-observer polarity frames `eps_o` (declared value-blind switching data), giving genuinely mixed-sign gluing constraints (96 / 12 negative agreements). Transport is connected (M1, triangle) and **partitioned** (M2, one edge; one observer isolated). The T26 global-section predicate runs over the patch layer.

Honest disclosure carried over from the toy referee (D3): the realization is value-symmetric (record structure depends only on `strip(state)`); "value-blind" results are relative to that modeling choice and to the σ-invariance/Neutrality criterion.

## 2. Precise results and grades

**N1 — The branch-preserving functor survives the non-thin source.** F: E^w → D1Field (objects → multi-observer field objects; witnesses → order-carrying prop schedules over a fixed observer population) satisfies identity and composition laws under *order-sensitive* witness composition, with every image morphism valid (profiles non-decreasing including strictly-increasing cases, readouts transported, gluing preserved), and is branch-preserving: the fork images are distinct and differ **only** in the values slot. F is **not faithful**: the audit-depth witness is forgotten (exhibited, disclosed — parallel morphisms with equal image). *Grade: exhaustive-finite on both models.* The composition-law check has a failing direction that exists *only because the source is non-thin* (reversed-schedule composition fails; an audit-depth-carrying schedule also fails — saturating source composition cannot ride in a concatenating slot).

**N2 — Morphism-level invariants beyond the thin shadow exist; none is sign-selecting.** RUN-0025's warning is reproduced executably: the value-blind invariant "first-issued proposition" takes different values on distinct parallel morphisms, hence does not factor through the thin reflection. But: σ extends to an involutive automorphism of the *non-thin* category (object and morphism bijections, preserves identity and composition — exhaustive), the fork objects *and their issuing morphism sets* form single σ-orbits, every value-blind morphism invariant tested is flip-invariant, and the one fork-separating morphism invariant found ("sign of first-issued literal") reads the ± label and fails the relabel test (its σ-conjugate is distinct and equally admissible). *Grade: exhaustive-finite for the automorphism and orbit facts; definitional for "any σ-invariant morphism invariant agrees on σ-orbits" given the verified automorphism; the collapse-or-smuggle dichotomy remains definition-relative (Neutrality criterion), per the lane-B referee's corrected wording.*

**N3 — At multi-observer tier the flip is still an automorphism; the patch layer carries no sign-selecting data.** σ_T (negate all per-site readouts) is an involution, an automorphism of the image, and F is equivariant **on objects and on morphisms** (exhaustive). Gluing constraints are relative signs (degree-2 readout products): recomputing them from flipped readouts returns them unchanged (exhaustive; near-definitional given the product form — disclosed). The decisive control: **keeping the entire gluing/transport layer and forgetting only absolute readouts collapses the fork** — so at this tier the fiber lives entirely in the absolute-readout slot, not in transport or gluing. A sign-selecting transport datum would have to be odd-degree in readouts (an absolute readout); the exhibited one breaks flip-invariance and thereby fails the relabel test. *Grade: exhaustive-finite; the "no structural invariant breaks the flip" generalization is definitional given the automorphism, as the toy referee required it to be stated.*

**N4 — New native-tier structure: the undetermined fiber is generically LARGER than one global sign.** The T26 global-section set of the patch system was computed exhaustively for every state: the actual readout is a section; the section set is flip-closed with no flip-fixed point; any definable selector fails the relabel test; and the count is exactly `2^(#(proposition, transport-component) blocks)` (a Harary/switching consistency fact verified exhaustively, consistent with lane C's "known mathematics" verdict — organizational, not novel). Concretely: fork states have exactly 2 sections (the toy's single Z/2), but the 3-prop state in connected M1 has 8, and the 2-prop state under **partitioned transport** (M2) has 16. So gluing pins *all and only* the intra-component relative polarities; the free data is `(Z/2)^Σ`, and the global flip is merely its diagonal. Consequence for the program: a single `bar(b)`-like binary datum is well-posed at this tier only relative to declared cross-proposition and cross-component identifications (connected trusted transport plus a naming convention) — any future external anchor must select coherently per block, not just break one global Z/2. *Grade: exhaustive-finite on these models; the shape statement is argued. This is a bounding result (Failure-Preservation first-class); it raises, not lowers, the anchor burden, and is consistent with the correction's fiber picture.*

**N5 — Measured side-finding.** The naive label-reader "count of +1 readouts" is *not* even a reliable flip-breaker: under mixed observer frames it balances at the M2 fork (True at M1's fork, False at M2's). A reliable flip-breaker must name a site *and* a label (the exhibited `readout at (o1,p)`), and then fails the relabel test. Under Neutrality this sharpens what "importing the label" means at multi-observer tier: it requires naming an observer frame, not just a global sign.

**Prediction correction (honesty receipt).** A first-draft expectation predicted no strict B-growth in M2; the run falsified it (B grows 0→1 when a pool-only observer gains its first accessible formation event). The override was removed and nonzero-base B-growth is reported as a separate measurement. One control was redesigned after the first run falsified it (plus-count → named-slot readout), with the falsified behavior kept and reported as finding N5 rather than discarded.

## 3. Controls — every check has a demonstrated failing direction

18 TEETH entries, each running a deliberately broken variant through the *same* code path and shown failing (all fired): uncapped depth breaks closure; NAND-depth breaks associativity; object-only σ leaves the category; corroboration-off kills strict growth (this is exactly the old toy realization — D2's vacuity reproduced as the failing direction); interference realization breaks monotonicity; unique holders kill R<A; uniform access kills site heterogeneity; uniform eps kills mixed agreements; reversed-schedule and audit-carrying functors break the composition law; sentinel functor breaks the identity law; corrupt agreements are detected as invalid morphisms and create a genuine T26 gluing obstruction (0 sections); flipped-target values are detected; single-site flip breaks equivariance and gluing consistency; odd-degree gluing data break flip-invariance. No hardcoded literals are presented as controls; the two near-definitional main checks (`gluing_products_flip_invariant_recomputed`, given the product form; the definitional battery replacement) are labeled as such above rather than counted as evidence.

## 4. Honest disposition — native-tier obligations after this work

- **Reopen obligations (1)–(2)** (native categories; non-constant branch-preserving functor on their actual morphisms): **still OPEN at fully-native grade, but materially advanced.** The referee's named defects are now each discharged by an executable model: the source is genuinely non-thin with order- and depth-carrying witnesses (D5), the target has real observer sites over a population (D7), R is exercised as a distinct axis via shared holders (D8), and monotone legs have strictly-increasing cases with a demonstrated failing direction (D2). What remains is the *actual-native* gap, now precisely named rather than a defect list: TI's `Ext_n` with real admissibility-proof witnesses `w_n : Adm_n(e_n)` (Lean-tier objects, not a two-point depth), and TaF's full `D1RestrictionSystem` with overlap tests, patch constraints beyond pairwise relative signs, restriction morphisms *between* systems, and `TypedTransportNetwork` layers with site maps that merge/split observers.
- **Obligation (3)-shaped evidence** (target polarity not an imported label): extended one tier — equivariance now holds on a non-thin source and on morphisms of a multi-observer target, and the "fiber undetermined" statement is sharpened to "gluing determines exactly the relative polarities; the free data is one Z/2 per (proposition, transport-component)." Still definition-relative (Neutrality criterion), not a theorem about TaF's native object.
- **Obligations (4)–(5)** (physical finality direction; non-circular map to the GU positive-norm branch): untouched, OPEN. Nothing here supplies an anchor; N4 shows the anchor burden is *heavier* than one bit under partitioned transport.
- **Verdict in one sentence:** the toy result survives the non-thin and multi-observer lift in strengthened form — the flip remains an automorphism, the fiber remains equivariantly transported and undetermined, and the patch layer provably (exhaustive-finite) carries only relative-polarity data — while native tier is still not exhausted, and the newly located per-block structure of the fiber is a first-class bounding result.

## 5. Full fixture source

```python
"""P2C NATIVE-TIER Gate #1 fixture: non-thin Ext_S -> multi-observer D1Field.

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
    print("P2C NATIVE-TIER GATE #1: NON-THIN Ext_S -> MULTI-OBSERVER D1FIELD")
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
```

## 6. Full fixture output (exit code 0, runtime 0.7s)

```
P2C NATIVE-TIER GATE #1: NON-THIN Ext_S -> MULTI-OBSERVER D1FIELD
============================================================================

MODEL M1: props=('p', 'q', 'r') base_mult={'p': 2, 'q': 2, 'r': 3} style=antichain tau=2
  observers=('o1', 'o2', 'o3') transport=(('o1', 'o2'), ('o2', 'o3'), ('o1', 'o3'))
  eps frames={'o1': 1, 'o2': 1, 'o3': -1}
  objects=27  nonthin_morphisms=402  composable_pairs=2172  composable_triples=8808  (exhaustive, no sampling)
  PASS  src_composition_closed: True
  PASS  src_identity_neutral: True
  PASS  src_associativity_exhaustive: True
  PASS  sigma_src_object_bijection: True
  PASS  sigma_src_morphism_bijection: True
  PASS  sigma_src_preserves_identity_and_composition: True
  PASS  sigma_src_involution: True
  PASS  fork_objects_single_sigma_orbit: True
  PASS  fork_issuing_morphisms_swapped_by_sigma: True
  PASS  SOURCE_fact_fork_no_common_successor: True
  PASS  nonthin_parallel_distinct_morphisms_exist: True
  PASS  nonthin_first_prop_invariant_not_thin_definable: True
  PASS  nonthin_first_prop_invariant_is_flip_invariant: True
  PASS  nonthin_audit_depth_distinguishes_parallel_morphisms: True
  PASS  MOR_INV_first_sign_separates_fork_issuers: True
  PASS  MOR_INV_first_sign_fails_relabel_test: True
  PASS  realization_strict_growth_A_present: True
  PASS  realization_strict_growth_R_present: True
  PASS  realization_strict_growth_B_present: True
  PASS  realization_strict_growth_C_present: True
  PASS  redundancy_strictly_below_support_somewhere: True
  PASS  site_profiles_heterogeneous_somewhere: True
  PASS  mixed_sign_agreements_present: True
  PASS  agreements_match_readout_products: True
  PASS  F_all_image_morphisms_valid: True
  PASS  F_identity_law: True
  PASS  F_composition_law_all_pairs: True
  PASS  F_not_faithful_audit_depth_forgotten: True
  PASS  TARGET_fact_field_fork_images_distinct: True
  PASS  fork_images_differ_only_in_values_slot: True
  PASS  sigmaT_involution: True
  PASS  equivariance_on_objects: True
  PASS  equivariance_on_morphisms: True
  PASS  sigmaT_automorphism_of_image: True
  PASS  gluing_products_flip_invariant_recomputed: True
  PASS  CONTROL_gluing_kept_values_forgotten_collapses_fork: True
  PASS  cheat_named_slot_readout_breaks_flip_and_fails_relabel: True
  PASS  readout_is_a_global_section: True
  PASS  section_set_flip_closed: True
  PASS  no_flip_fixed_section: True
  PASS  section_count_equals_2_pow_components: True
  PASS  fork_section_count_is_two: True
  PASS  FIBER_section_selector_fails_relabel: True
  [info] strict-growth instances (A,R,B,C): (192, 96, 96, 168)  (B-growth from nonzero base: 48)
  [info] naive '+1 count' breaks flip at fork: True (frame-dependent; not a reliable label-reader)
  [info] R<A instances: 132   heterogeneous-site instances: 54   negative agreements: 96
  [info] parallel morphism classes with multiplicity: 125
  [info] fork sections: 2   largest state (('p', 1), ('q', 1), ('r', 1)): components=3, sections=8 (= 2^components)

MODEL M2: props=('p', 'q') base_mult={'p': 2, 'q': 1} style=chain tau=1
  observers=('o1', 'o2', 'o3') transport=(('o1', 'o2'),)
  eps frames={'o1': 1, 'o2': -1, 'o3': 1}
  objects=9  nonthin_morphisms=58  composable_pairs=228  composable_triples=744  (exhaustive, no sampling)
  PASS  src_composition_closed: True
  PASS  src_identity_neutral: True
  PASS  src_associativity_exhaustive: True
  PASS  sigma_src_object_bijection: True
  PASS  sigma_src_morphism_bijection: True
  PASS  sigma_src_preserves_identity_and_composition: True
  PASS  sigma_src_involution: True
  PASS  fork_objects_single_sigma_orbit: True
  PASS  fork_issuing_morphisms_swapped_by_sigma: True
  PASS  SOURCE_fact_fork_no_common_successor: True
  PASS  nonthin_parallel_distinct_morphisms_exist: True
  PASS  nonthin_first_prop_invariant_not_thin_definable: True
  PASS  nonthin_first_prop_invariant_is_flip_invariant: True
  PASS  nonthin_audit_depth_distinguishes_parallel_morphisms: True
  PASS  MOR_INV_first_sign_separates_fork_issuers: True
  PASS  MOR_INV_first_sign_fails_relabel_test: True
  PASS  realization_strict_growth_A_present: True
  PASS  realization_strict_growth_R_present: True
  PASS  realization_strict_growth_B_present: True
  PASS  realization_strict_growth_C_present: True
  PASS  redundancy_strictly_below_support_somewhere: True
  PASS  site_profiles_heterogeneous_somewhere: True
  PASS  mixed_sign_agreements_present: True
  PASS  agreements_match_readout_products: True
  PASS  F_all_image_morphisms_valid: True
  PASS  F_identity_law: True
  PASS  F_composition_law_all_pairs: True
  PASS  F_not_faithful_audit_depth_forgotten: True
  PASS  TARGET_fact_field_fork_images_distinct: True
  PASS  fork_images_differ_only_in_values_slot: True
  PASS  sigmaT_involution: True
  PASS  equivariance_on_objects: True
  PASS  equivariance_on_morphisms: True
  PASS  sigmaT_automorphism_of_image: True
  PASS  gluing_products_flip_invariant_recomputed: True
  PASS  CONTROL_gluing_kept_values_forgotten_collapses_fork: True
  PASS  cheat_named_slot_readout_breaks_flip_and_fails_relabel: True
  PASS  readout_is_a_global_section: True
  PASS  section_set_flip_closed: True
  PASS  no_flip_fixed_section: True
  PASS  section_count_equals_2_pow_components: True
  PASS  fork_section_count_is_two: True
  PASS  FIBER_section_selector_fails_relabel: True
  [info] strict-growth instances (A,R,B,C): (16, 16, 8, 16)  (B-growth from nonzero base: 0)
  [info] naive '+1 count' breaks flip at fork: False (frame-dependent; not a reliable label-reader)
  [info] R<A instances: 12   heterogeneous-site instances: 12   negative agreements: 12
  [info] parallel morphism classes with multiplicity: 25
  [info] fork sections: 2   largest state (('p', 1), ('q', 1)): components=4, sections=16 (= 2^components)

TEETH SUITE (failing directions; broken variants through the SAME code paths, on M1)
  PASS  TEETH_uncapped_depth_breaks_closure: True
  PASS  TEETH_nand_depth_breaks_associativity: True
  PASS  TEETH_object_only_sigma_leaves_category: True
  PASS  TEETH_corroboration_off_kills_strict_growth: True
  PASS  TEETH_interference_breaks_monotonicity: True
  PASS  TEETH_unique_holders_kill_R_lt_A: True
  PASS  TEETH_uniform_access_kills_site_heterogeneity: True
  PASS  TEETH_uniform_eps_kills_mixed_agreements: True
  PASS  TEETH_reversed_schedule_breaks_composition_law: True
  PASS  TEETH_audit_carrying_functor_breaks_composition_law: True
  PASS  TEETH_sentinel_functor_breaks_identity_law: True
  PASS  TEETH_corrupt_agreement_detected_invalid: True
  PASS  TEETH_flipped_target_values_detected_invalid: True
  PASS  TEETH_single_site_flip_breaks_equivariance: True
  PASS  TEETH_single_site_flip_breaks_gluing_consistency: True
  PASS  TEETH_odd_degree_gluing_datum_breaks_flip_invariance: True
  PASS  TEETH_corrupt_agreement_creates_gluing_obstruction: True
  PASS  TEETH_corrupt_breaks_product_consistency: True

BUG-REGRESSION GUARD (ADAPTER2-01)
  The SOURCE fact (fork has no common successor) and the TARGET
  facts (field fork images distinct; profiles/agreements equal)
  are computed by disjoint code paths and labeled SOURCE_/TARGET_.
  No branch-preservation verdict cites the SOURCE fact.

VERDICT (exploration tier; exhaustive-finite on these models)
  1. The branch-preserving D1Field functor SURVIVES the non-thin
     source: functor laws hold on order-sensitive witness
     composition; the audit-depth witness is forgotten (F is not
     faithful) -- disclosed, not hidden.
  2. Morphism-level invariants beyond the thin shadow EXIST
     (issuance order, audit depth) -- RUN-0025's warning is
     reproduced executably -- and every value-blind one is
     flip-invariant; the only fork-separating morphism invariant
     found reads the +/- label and fails the relabel test.
  3. At multi-observer tier the flip is STILL an automorphism and
     F is equivariant. The patch layer pins exactly the relative
     polarities: the T26 global-section set has size
     2^(#(prop,transport-component)) and is a free Z/2-torsor per
     block; the global flip is the diagonal. No transport/gluing
     datum selects a section: even-degree (relative) data are
     flip-invariant, and odd-degree (absolute) data fail the
     relabel test. Partitioned transport (M2) makes the
     undetermined fiber STRICTLY LARGER than one global sign.
  bar(b), H59, Krein positivity, physical issuance: remain OPEN.

All checks matched pre-declared expectations. Exit 0.
```

## 7. Honest bounds and what remains genuinely open

- **Exploration tier throughout.** All positive statements are exhaustive-finite on M1/M2 as specified above, definitional where flagged, argued for the general shape. Nothing is claimed about TaF's or TI's full native objects.
- **What "native" still means beyond this fixture:** (i) TI's actual `Ext_n` morphisms carry admissibility *proofs* (`w_n : Adm_n(e_n)`, Lean-hardened per RUN-0123), not a two-point audit depth — richer witness algebra could in principle carry structure this enrichment cannot; (ii) TaF's `D1RestrictionSystem` includes overlap tests, patch constraints beyond pairwise relative signs, restriction morphisms *between* systems, and `TypedTransportNetwork` layers with genuine site maps (merging/splitting observers), none of which are modeled; (iii) the realization is value-symmetric by construction (D3 carries over: "value-blind" is criterion-relative).
- **Per Located-Is-Not-Forced:** the fiber is now located more precisely (per-(proposition, transport-component) switching freedom with the global flip as diagonal); nothing forces a branch. Per Failure-Preservation, N4 is a first-class bounding result: any future anchor must break one Z/2 per block coherently, and a single global `bar(b)`-like sign is only well-posed given connected trusted transport plus declared cross-block identifications.
- **The truthful verdict:** the toy result survives the lift to non-thin source and multi-observer target in strengthened, sharpened form; native tier is still not exhausted; no sign-selecting structure appeared at this tier, and the one place it could have hidden (the transport/gluing patch layer) was tested directly and provably-on-these-models carries only relative-polarity data.

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs grades)

# Referee report: LANE 2-native-tier-gate1

**Independently verified before writing this:** re-ran the fixture from disk (`...scratchpad\gate1_native_nonthin_multiobserver.py`, exit 0, 0.22s); every reported number reproduces exactly (27/402/2172/8808; 9/58/228/744; strict-growth 192/96/96/168 and 16/16/8/16; B-from-nonzero-base 48/0; R<A 132/12; negative agreements 96/12; parallel classes 125/25; sections 2/8/16 = 2^blocks; all 43 main checks and 18 TEETH pass). Citations re-fetched: RUN-0025's thin-shadow warning is real and quoted accurately (temporal-issuance/agent-runs/RUN-0025, lines 56-57); `Iss_n/e_n/w_n` and `w_n : Adm_n(e_n)` exist in TI `FORMAL-OBJECT.md`; RUN-0123 "Lean-hardened" confirmed; TaF `FORMALISM.md` confirms the bounded-holder observer contract, T24 field-valued D1, T26 `D1RestrictionSystem`, `TypedTransportNetwork`. No contradiction of ADAPTER2-01 found: bar(b)/H59/Krein stay OPEN, N4 extends (does not reopen) the fiber picture and explicitly raises the anchor burden. No source-sovereignty violation; the toy fixture the report proposes to sit alongside already exists at `possibility-to-capability/tests/gate1_branch_preserving_functor.py`. The lane-B referee defects D2/D5/D7/D8 are genuinely discharged as executable-model defects (strict growth with corrob-off failing direction; genuinely non-thin source; observer sites; R<A exercised).

## (1) VERDICT: SOUND-WITH-CORRECTIONS

The computational content is real, reproducible, and correctly bounded in §4/§7. The defects are concentrated in the §3 controls framing (a softer recurrence of the exact burned error class), one battery-of-one phrased as a battery, and encoding-level facts wearing formalism-level names.

## (2) Defects

**F1 (MEDIUM) — §3's heading "every check has a demonstrated failing direction" is false, and one "control" cannot fail.** 43 main checks, 18 TEETH; I verified computationally that several main checks have no failing direction and cannot fail:
- `CONTROL_gluing_kept_values_forgotten_collapses_fork` — billed in §2/N3 as "the decisive control" — is *logically implied* by the co-listed `fork_images_differ_only_in_values_slot` (verified: given equal profiles/edges/agreements, forgetting values forces equality). A control that cannot fail given another passing check is exactly the class the lane-B referee burned (its D1).
- `FIBER_section_selector_fails_relabel` reduces to `no_flip_fixed_section`: I verified `global_sections(sigma_T(X)) == global_sections(X)` for every state in both models, so the selector is identical on both sides and the check is a conditional tautology.
- `section_set_flip_closed` and `no_flip_fixed_section` are algebra-forced for ±1 assignments under product constraints (a nonempty ±1 vector never equals its negation); `readout_is_a_global_section` is same-code-path (agreements are computed *from* the readout); `cheat_named_slot_readout_breaks_flip...` and `MOR_INV_first_sign_fails_relabel_test` are definitional. The report labels only **two** near-definitional checks; at least five more are in the same class and are counted in the PASS wall.
Mitigation: the corrupt-agreement TEETH entries do give the section machinery a real failing direction, `section_count_equals_2_pow_components` and `fork_section_count_is_two` are genuine cross-checks, and the TEETH suite itself is real (all 18 rerun and fire). The defect is the *heading* and the "decisive control" billing, not the suite.

**F2 (MEDIUM) — "every value-blind morphism invariant tested is flip-invariant" is a battery of one.** Exactly one value-blind morphism invariant is flip-invariance-tested (`inv_first_prop`); audit depth's flip-invariance is never checked (it holds by construction of `sigma_mor` — same-code-path). This repeats the lane-B D4 pattern (battery generalization presented as accumulated evidence) in miniature, though the report does flag the generalization itself as definitional.

**F3 (MEDIUM) — Encoding-level facts stated as formalism-level facts.**
- "The T26 global-section predicate runs over the patch layer": the fixture runs a T26-*style* predicate over its own encoding (per-(site,prop) slots, pairwise product constraints). T26's actual `D1RestrictionSystem` (FORMALISM.md lines 368-376) carries **one proposition value per site** plus **optional overlap tests and finite patch constraints** — none modeled. Disclosed in §4(ii), but the §1/§2 naming claims the formalism object.
- Verdict sentence: "the patch layer provably (exhaustive-finite) carries only relative-polarity data" — true of a gluing layer *constructed* as degree-2 readout products; flip-invariance is then near-definitional (the report concedes this for the recompute check but drops the qualifier in the verdict). The place a sign could still hide — TaF's optional non-pairwise patch constraints — is precisely what is unmodeled.
- "A sign-selecting transport datum would have to be odd-degree in readouts": arbitrary data are not degree-graded; this is a parity metaphor from one exhibit stated as a classification fact. The provable statement is the definitional dichotomy (flip-invariant ⇒ agrees on the fork; non-flip-invariant ⇒ fails the relabel test by the Neutrality criterion).
- The lane title "NATIVE-TIER" overstates what §4 itself concedes is still an "actual-native gap" (two-point depth vs Lean witnesses; fixed population, no site maps that merge/split; no restriction morphisms between systems; T24's time/scale labels also absent and not in the disclosed gap list). "Enriched-toy / closer-to-native" is what was built.

**F4 (LOW/MEDIUM) — "all checks matched pre-declared expectations" (lane header and exit-0 line) overstates a second-draft expectation set.** The report's own honesty receipt says one expectation (M2 B-growth override) was deleted after the first run falsified it and one control was redesigned after falsification. So the shipped `OVERRIDES = {}` is post-hoc for at least one entry, and there is no pre-registration receipt (lane-B D9 class). The disclosure is commendable; the headline contradicts it.

**F5 (LOW) — TEETH run on M1 only.** Disclosed in the output banner but §3's prose ("every check…") doesn't say the failing directions were demonstrated on one model. M2's partitioned transport is never exercised by any broken variant.

**F6 (LOW) — Non-thinness is partly trivial.** All 125/25 hom-sets have multiplicity because the depth bit doubles *every* hom-set (including endomorphism sets `(a,a,(),1)`). The order-witness multiplicity (the part RUN-0025 actually warns about) exists only where |S′\S| ≥ 2. Genuine non-thinness, but "125 parallel classes" flatters the enrichment.

**Not defects (checked and cleared):** ADAPTER2-01 consistency (SOURCE_/TARGET_ separation is real in code; no verdict cites the source fact; N4's (Z/2)^Σ refinement is consistent with the correction's fiber picture and heavier-anchor direction); all citations (RUN-0025/0081/0123, E-shape, T24/T26, observer contract); all numeric claims; source sovereignty; the D2/D5/D7/D8 discharge claims; the prediction-correction receipt itself.

## (3) Corrected wordings

- §3 heading "Controls — every check has a demonstrated failing direction" → **"Controls — 18 broken-variant TEETH entries (run on M1) cover the load-bearing category, realization, functor, flip, and patch-machinery checks; the remaining patch-layer positives (section-set flip closure, no flip-fixed section, readout-is-a-section, values-forgotten collapse, selector relabel failure) are definitional or implied by co-listed checks and carry no independent evidential weight."**
- "The decisive control: keeping the entire gluing/transport layer and forgetting only absolute readouts collapses the fork" → **"Corollary of `fork_images_differ_only_in_values_slot`: since the fork images agree outside the values slot, forgetting readouts collapses them; this restates where the fiber lives, it is not an independent control."**
- "every value-blind morphism invariant tested is flip-invariant" → **"the one value-blind morphism invariant tested (first-issued proposition) is flip-invariant; audit depth is flip-invariant by construction of σ; no broader invariant battery was run."**
- "Exit 0, all checks matched pre-declared expectations" → **"Exit 0 against the final expectation set; one expectation and one control were revised after a first run falsified them (disclosed); no pre-registration receipt exists."**
- "The T26 global-section predicate runs over the patch layer" → **"A T26-style global-section predicate runs over this fixture's patch encoding (per-(site,prop) slots, pairwise relative-sign constraints); T26's `D1RestrictionSystem` — one proposition value per site, optional overlap tests, patch constraints beyond pairwise — is not modeled."**
- "the patch layer provably (exhaustive-finite) carries only relative-polarity data" → **"the patch layer as encoded here (degree-2 readout products) carries only relative-polarity data — near-definitional given the product form; TaF's optional overlap/patch constraints remain the untested hiding place."**
- "A sign-selecting transport datum would have to be odd-degree in readouts" → **"by the Neutrality criterion, any flip-invariant transport datum agrees on the fork; the exhibited absolute-readout datum breaks flip-invariance and fails the relabel test; no general degree classification was proved."**
- Title "NATIVE-TIER Gate #1" → **"Gate #1 enriched-toy lift (closer-to-native): non-thin witnesses + multi-observer target."**

## (4) Grade the main result actually earns

**Exploration-tier, exhaustive-finite on two enriched finite toy models** (minimal two-datum witness enrichment of the thin source; fixed three-observer population; value-symmetric realization; pairwise-product gluing encoding). By component: **N1 earns its stated grade** (exhaustive-finite functor-law survival on a genuinely non-thin source, with a non-thin-only failing direction — the strongest and cleanest result in the lane). **N2/N3 earn "exhaustive-finite for the automorphism/equivariance/orbit facts + definition-relative (Neutrality-criterion) for every no-sign-selection claim,"** with the morphism-invariant leg an exhibit, not a battery. **N4 earns "exhaustive-finite on these models" for the 2^blocks section structure and the strictly-larger fiber under partitioned transport** — this is the lane's genuinely new bounding content — with the program consequence (per-block anchor burden) argued and encoding-relative. Net: **a real one-tier lift of the lane-B toy result that discharges the lane-B referee's named defects (D2, D5, D7, D8) at enriched-toy tier, sharpens the ADAPTER2-01 fiber picture to per-block structure, and settles no reopen obligation** — which §4 itself states correctly. The report's own §4/§7 self-assessment survives; the §3 controls framing and the formalism-level naming do not.

## (5) GO / NO-GO on file writes

Not applicable — this is lane 2; no file writes were proposed for referee gating (persistence of the fixture to `possibility-to-capability/tests/` was explicitly left to the orchestrator). If the orchestrator persists it, no objection, on two conditions: the accompanying lane document carries the corrected wordings above (especially the §3 controls heading and the "pre-declared" headline), and the file drops "NATIVE-TIER" from its self-description in favor of "enriched-toy / closer-to-native."