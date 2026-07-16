"""Condition 2' NO-GO fixture (P2C swing-2 follow-up, adversarial-twin lane,
impossibility direction).

CLAIM UNDER TEST (toy grade): no finality/issuance-native structure can derive
a sector-ASYMMETRIC spectral condition with an ORIENTATION (i.e. name which
Krein sector carries the bounded-below spectrum), because every functional
definable from a flip-equivariant vocabulary is flip-equivariant, and the
sector swap has no fixed point on {K+, K-}.

THE HYPOTHESIS CLASS H (total precision; see deliverable Section 2):
A signature Sigma = (sorts, constants, primitives) with a finite Sigma-structure
M is *finality/issuance-native* iff the global flip g -- defined per sort below
-- (i) maps each domain bijectively to itself, (ii) fixes every constant, and
(iii) commutes with every primitive:  f(g a_1, ..., g a_k) = g(f(a_1, ..., a_k))
for ALL argument tuples.  Equivalently: g is a Sigma-automorphism of M;
equivalently: graph(g) is a subalgebra of M x M.  Membership in H is
MECHANICALLY DECIDABLE for finite M: run the exhaustive primitive battery in
this file (function `battery`).  That battery IS the induction step of the
no-go theorem, so any claimed escape from the no-go must present a primitive
(or constant) that FAILS the battery -- and that failure is the posit.

THE FLIP g, per sort (the unique nontrivial simultaneous action; g o g = id):
  Prop         : identity
  Lit          : (p, e) -> (p, -e)                    [sign flip]
  State        : elementwise Lit flip
  Obs          : script flipped elementwise, stop time unchanged
  Pop          : elementwise Obs flip
  Gen          : A -> S A S   (S = e1<->e3, e2<->e4; the swing-2 lane-3
                 recoordinatized global flip: form -> -form, J -> -J,
                 labels swapped, all folded into S-conjugation)
  Vec          : v -> S v
  Sector       : K+ <-> K-, NONE fixed                [the swap: NO fixed
                                                       point on {K+, K-}]
  SectorPair   : identity (the pair {K+, K-} is UNORDERED -- flip-fixed)
  Bool/Nat/Real: identity

THEOREM T1 (equivariance; symbolic, structural induction -- proof in the
deliverable): if M is in H then every Sigma-term t(x_1..x_n) satisfies
t(g a_1, ..., g a_n) = g(t(a_1, ..., a_n)).  Base: variables (trivial) and
constants (clause ii).  Step: clause iii.  Nothing else is a term.  QED.
The proof does not use finiteness of M.

COROLLARIES (machine-checked below):
  C1  every CLOSED Sector-term denotes a g-fixed point, i.e. NONE: the
      vocabulary cannot canonize a sector without parameters.
  C2  orbit-indistinguishability COMPLETENESS: no Bool-valued Sigma-term
      separates a generator A from flip(A) (upgrades swing-2 lane 3's
      instance-battery orbit lemma to all definable functionals over Sigma --
      the referee's L6 gap, closed at toy grade).
  C3  the UNORIENTED sector-asymmetric spectral condition ("exactly one
      sector has positive restricted spectrum") IS Sigma-definable and
      flip-invariant; only its ORIENTATION is underivable.  The fork is
      expressible; the selection is not.

CHECK LABELS (house style, swing-2 discipline):
  [T] theorem-consequence: outcome fixed by construction/AFTER T1+E1; carries
      NO evidential weight for the headline; listed separately.
  [E] genuine check: exhaustive verification whose failure was possible at
      formalization time (an implementation or proof error would be caught;
      the [F] controls demonstrate the same code path catching planted
      failures).  E2-E6 are entailed by T1 GIVEN E1; they are [E] with
      respect to implementation/proof error only -- disclosed here, not
      hidden.
  [F] failing-direction control exercising the SAME checker code path.

Exit 0 iff every check matches its pre-declared expected value.
numpy used only to PRECOMPUTE the finite Krein-side tables at load time; the
term machinery is pure Python over finite hashable domains.
"""

from __future__ import annotations

import itertools

import numpy as np

# =====================================================================
# Krein toy (conventions of tests/krein_norm_link_probe.py, commit 96b96bc)
# =====================================================================

ETA4 = np.diag([1.0, 1.0, -1.0, -1.0])
S4 = np.eye(4)[[2, 3, 0, 1]]


def expm(m: np.ndarray) -> np.ndarray:
    m = np.asarray(m, dtype=complex)
    s = int(max(0, np.ceil(np.log2(max(1.0, np.linalg.norm(m, 2))))) + 4)
    a = m / (2.0 ** s)
    out = np.eye(m.shape[0], dtype=complex)
    term = np.eye(m.shape[0], dtype=complex)
    for k in range(1, 24):
        term = term @ a / k
        out = out + term
    for _ in range(s):
        out = out @ out
    return out


A_C = np.zeros((4, 4))
A_C[:2, :2] = [[-1.0, 0.5], [0.0, -2.0]]      # spectrum {-1, -2}
A_C[2:, 2:] = [[0.7, -0.4], [0.2, 1.3]]       # spectrum {0.9, 1.1}
H_SPEC = np.diag([1.0, 2.0, -3.0, -4.0])
A_BSYM = -np.eye(4) + 0.3 * (np.outer(np.eye(4)[0], np.eye(4)[2])
                             - np.outer(np.eye(4)[2], np.eye(4)[0]))
A_A = np.diag([-1.0, -2.0, 1.0, 0.5])

# Gen sort: named orbit-CLOSED set (both orbit members present; NO generator
# is a constant of the signature -- naming one would fail clause (ii)).
GEN_MATS = {
    "A_c": A_C, "A_c~": S4 @ A_C @ S4,
    "H_spec": H_SPEC, "H_spec~": S4 @ H_SPEC @ S4,
    "A_bsym": A_BSYM, "A_bsym~": S4 @ A_BSYM @ S4,
    "A_a": A_A, "A_a~": S4 @ A_A @ S4,
}
GEN_FLIP = {"A_c": "A_c~", "A_c~": "A_c", "H_spec": "H_spec~",
            "H_spec~": "H_spec", "A_bsym": "A_bsym~", "A_bsym~": "A_bsym",
            "A_a": "A_a~", "A_a~": "A_a"}

SECTOR_IDX = {"KP": [0, 1], "KM": [2, 3]}


def _sector_bounded(mat: np.ndarray, sec: str) -> bool:
    """Orbit-boundedness of the issuance semigroup started in the sector
    (t-grid sup, threshold 1e3; every instance used is >= e^15 from the
    threshold -- same disclosed numeric failure mode as the twin fixture)."""
    if sec == "NONE":
        return False
    sup = 0.0
    for t in np.linspace(0.0, 30.0, 61):
        e = expm(t * mat)
        for i in SECTOR_IDX[sec]:
            sup = max(sup, float(np.linalg.norm(e[:, i])))
    return sup < 1e3


def _restr_spec_pos(mat: np.ndarray, sec: str) -> bool:
    if sec == "NONE":
        return False
    idx = SECTOR_IDX[sec]
    return bool(np.all(np.linalg.eigvals(mat[np.ix_(idx, idx)]).real > 0))


# Precompute all Krein-side primitive tables (finite; primitives below are
# pure dict lookups, so the term machinery is deterministic and fast).
PRE_BOUND = {(gname, sec): _sector_bounded(m, sec)
             for gname, m in GEN_MATS.items() for sec in ("KP", "KM", "NONE")}
PRE_RSP = {(gname, sec): _restr_spec_pos(m, sec)
           for gname, m in GEN_MATS.items() for sec in ("KP", "KM", "NONE")}


def _c_from(table, gname: str) -> str:
    bp, bm = table[(gname, "KP")], table[(gname, "KM")]
    if bp == bm:
        return "NONE"
    return "KP" if bp else "KM"


PRE_CSTAB = {g: _c_from(PRE_BOUND, g) for g in GEN_MATS}
PRE_CENERGY = {g: _c_from(PRE_RSP, g) for g in GEN_MATS}
PRE_TRACE = {g: round(float(np.trace(m)), 6) for g, m in GEN_MATS.items()}
PRE_SPECABS = {g: round(float(np.max(np.linalg.eigvals(m).real)), 6)
               for g, m in GEN_MATS.items()}

# Oriented-eta functional -- deliberately NOT in Sigma (it is the sign posit
# restated, swing-2 T-a'); used only by the [F2] control.
def _eta_contractive(mat: np.ndarray) -> bool:
    m = ETA4 @ mat + mat.T @ ETA4
    return float(np.max(np.linalg.eigvalsh((m + m.T) / 2))) <= 1e-10


PRE_ETACON = {g: _eta_contractive(m) for g, m in GEN_MATS.items()}

# =====================================================================
# Record / issuance side (TI-native toy, lane-D conventions)
# =====================================================================

PROPS = ("p", "q")
LITS = tuple((p, e) for p in PROPS for e in (1, -1))


def consistent(s: frozenset) -> bool:
    vals: dict[str, int] = {}
    for prop, sign in s:
        if prop in vals and vals[prop] != sign:
            return False
        vals[prop] = sign
    return True


STATES = tuple(sorted((frozenset(c) for r in range(len(LITS) + 1)
                       for c in itertools.combinations(LITS, r)
                       if consistent(frozenset(c))),
                      key=lambda s: (len(s), sorted(s))))
assert len(STATES) == 9

# Observers: name -> (script, stop).  Population is orbit-closed as a DOMAIN;
# no observer is a constant (a signed script is not g-fixed).
OBS_DATA = {
    "alice":  ((("p", 1), ("q", 1)), 3),
    "alice~": ((("p", -1), ("q", -1)), 3),
    "bob":    ((("p", -1),), 1),
    "bob~":   ((("p", 1),), 1),
    "carol":  ((("q", -1), ("p", 1)), 2),
    "carol~": ((("q", 1), ("p", -1)), 2),
}
OBS_FLIP = {"alice": "alice~", "alice~": "alice", "bob": "bob~",
            "bob~": "bob", "carol": "carol~", "carol~": "carol"}
NATS = (0, 1, 2)
HMAX = 2

# Populations: a curated g-closed set of observer subsets (asymmetric
# populations EXIST in the domain -- as parameters; none is a constant).
POPS = tuple(sorted({
    frozenset(), frozenset({"alice"}), frozenset({"alice~"}),
    frozenset({"bob"}), frozenset({"bob~"}),
    frozenset({"alice", "bob"}), frozenset({"alice~", "bob~"}),
    frozenset({"alice", "alice~"}), frozenset(OBS_DATA),
}, key=lambda s: (len(s), sorted(s))))

VECS = tuple(sorted({(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
                     (1, 0, 1, 0), (1, 0, -1, 0), (-1, 0, 1, 0)}))

# =====================================================================
# The flip g, per sort (dicts: element -> element)
# =====================================================================


def flip_lit(l):
    return (l[0], -l[1])


def flip_state(s):
    return frozenset(flip_lit(l) for l in s)


GMAPS = {
    "Bool": {b: b for b in (True, False)},
    "Nat": {n: n for n in NATS},
    "Lit": {l: flip_lit(l) for l in LITS},
    "State": {s: flip_state(s) for s in STATES},
    "Obs": dict(OBS_FLIP),
    "Pop": {P: frozenset(OBS_FLIP[o] for o in P) for P in POPS},
    "Gen": dict(GEN_FLIP),
    "Vec": {v: (v[2], v[3], v[0], v[1]) for v in VECS},
    "Sector": {"KP": "KM", "KM": "KP", "NONE": "NONE"},
    "Pair": {"PAIR": "PAIR"},
}
DOMAINS = {
    "Bool": (True, False), "Nat": NATS, "Lit": LITS, "State": STATES,
    "Obs": tuple(sorted(OBS_DATA)), "Pop": POPS, "Gen": tuple(sorted(GEN_MATS)),
    "Vec": VECS, "Sector": ("KP", "KM", "NONE"), "Pair": ("PAIR",),
}

# =====================================================================
# The signature Sigma: constants (0-ary) and primitives
# Each entry: (name, argsorts, ressort, fn)
# =====================================================================


def history(o, t):
    script, stop = OBS_DATA[o]
    return frozenset(script[:min(t, stop)])


def issued_after(o, t):
    script, stop = OBS_DATA[o]
    return frozenset(script[t:stop])


def live(o, t):
    script, stop = OBS_DATA[o]
    return stop > t and len(script) > t


def add_lit(s, l):
    u = s | {l}
    return u if consistent(u) else s


def live_slice(P, t):
    u = frozenset(l for o in P if live(o, t) for l in issued_after(o, t))
    return u if consistent(u) else frozenset()


def some_live_extender(s, P, t):
    return any(live(o, t) and s <= history(o, HMAX) for o in P)


SIGMA = [
    # --- constants (all g-fixed; clause ii)
    ("empty", (), "State", lambda: frozenset()),
    ("none", (), "Sector", lambda: "NONE"),
    ("the_pair", (), "Pair", lambda: "PAIR"),
    ("n0", (), "Nat", lambda: 0),
    ("n1", (), "Nat", lambda: 1),
    ("n2", (), "Nat", lambda: 2),
    # --- extension order / record structure
    ("extends", ("State", "State"), "Bool", lambda a, b: a <= b),
    ("card", ("State",), "Nat", len),
    ("contains", ("State", "Lit"), "Bool", lambda s, l: l in s),
    ("add_lit", ("State", "Lit"), "State", add_lit),
    ("consistent_union", ("State", "State"), "Bool",
     lambda a, b: consistent(a | b)),
    # --- observers / aliveness / issuance
    ("history", ("Obs", "Nat"), "State", history),
    ("issued_after", ("Obs", "Nat"), "State", issued_after),
    ("live", ("Obs", "Nat"), "Bool", live),
    ("assigned_gen", ("Obs",), "Gen",
     {"alice": "A_c", "alice~": "A_c~", "bob": "H_spec", "bob~": "H_spec~",
      "carol": "A_bsym", "carol~": "A_bsym~"}.__getitem__),
    # --- populations / fork realization (lane-D aliveness rule, in-Sigma)
    ("live_slice", ("Pop", "Nat"), "State", live_slice),
    ("some_live_extender", ("State", "Pop", "Nat"), "Bool",
     some_live_extender),
    # --- Krein side: unordered pair, sectors, spectra, realizability
    ("memb", ("Sector", "Pair"), "Bool", lambda s, P: s in ("KP", "KM")),
    ("other", ("Sector",), "Sector",
     {"KP": "KM", "KM": "KP", "NONE": "NONE"}.__getitem__),
    ("eq_sector", ("Sector", "Sector"), "Bool", lambda a, b: a == b),
    ("sector_bounded", ("Gen", "Sector"), "Bool",
     lambda g, s: PRE_BOUND[(g, s)]),
    ("restr_spec_pos", ("Gen", "Sector"), "Bool",
     lambda g, s: PRE_RSP[(g, s)]),
    ("c_stab", ("Gen",), "Sector", PRE_CSTAB.__getitem__),
    ("c_energy", ("Gen",), "Sector", PRE_CENERGY.__getitem__),
    ("trace", ("Gen",), "Real", PRE_TRACE.__getitem__),
    ("specabs", ("Gen",), "Real", PRE_SPECABS.__getitem__),
    ("eq_gen", ("Gen", "Gen"), "Bool", lambda a, b: a == b),
    # --- eta, via its flip-equivariant derivatives (form up to overall sign)
    ("sector_of", ("Vec",), "Sector",
     lambda v: "KP" if v[2] == v[3] == 0 else
               ("KM" if v[0] == v[1] == 0 else "NONE")),
    ("q_neutral", ("Vec",), "Bool",
     lambda v: v[0] ** 2 + v[1] ** 2 - v[2] ** 2 - v[3] ** 2 == 0),
    ("q_abs", ("Vec",), "Real",
     lambda v: abs(v[0] ** 2 + v[1] ** 2 - v[2] ** 2 - v[3] ** 2)),
    # --- logic / arithmetic glue
    ("not_", ("Bool",), "Bool", lambda b: not b),
    ("and_", ("Bool", "Bool"), "Bool", lambda a, b: a and b),
    ("leq_nat", ("Nat", "Nat"), "Bool", lambda a, b: a <= b),
    ("succ", ("Nat",), "Nat", lambda n: min(n + 1, HMAX)),
    ("rleq", ("Real", "Real"), "Bool", lambda a, b: a <= b),
    ("ite_sector", ("Bool", "Sector", "Sector"), "Sector",
     lambda b, x, y: x if b else y),
]

# Real domain: exactly the reachable outputs of the numeric primitives.
DOMAINS["Real"] = tuple(sorted(set(PRE_TRACE.values())
                               | set(PRE_SPECABS.values())
                               | {abs(v[0]**2 + v[1]**2 - v[2]**2 - v[3]**2)
                                  for v in VECS}))
GMAPS["Real"] = {r: r for r in DOMAINS["Real"]}

# [F]-control primitives (NOT in Sigma; each must be caught by the battery):
PRIM_KPLUS = ("kplus", (), "Sector", lambda: "KP")            # sector constant
PRIM_ETACON = ("eta_contractive", ("Gen",), "Bool",           # oriented eta
               PRE_ETACON.__getitem__)

# =====================================================================
# Checker machinery (ONE comparator, injected everywhere -- the [F] controls
# sabotage exactly this comparator / the g-map, on the same code paths)
# =====================================================================


def good_compare(got, want):
    return got == want


def battery(prims, gmaps, compare):
    """Exhaustive: for every primitive and EVERY argument tuple, check
    f(g a_1,...,g a_k) == g(f(a_1,...,a_k)).  Returns (violations, n_tuples).
    This is the mechanical membership test for class H and the induction
    step of T1 (graph(g) is a subalgebra of M x M  <=>  battery passes)."""
    violations = []
    n = 0
    for name, argsorts, ressort, fn in prims:
        for args in itertools.product(*(DOMAINS[s] for s in argsorts)):
            n += 1
            got = fn(*(gmaps[s][a] for s, a in zip(argsorts, args)))
            want = gmaps[ressort][fn(*args)]
            if not compare(got, want):
                violations.append((name, args, got, want))
    return violations, n


def enumerate_and_verify(varspec, depth, prims, gmaps, compare):
    """Enumerate ALL Sigma-terms over the variable context `varspec` up to
    `depth`, with semantic deduplication (two terms with the same value on
    every assignment have the same equivariance status, so verifying each
    distinct semantic vector verifies every term in the fragment).  Verify
    equivariance pointwise:  t(g(v)) == g(t(v))  for every assignment v.
    Returns (per-sort distinct counts, n_candidates, violations)."""
    rows = list(itertools.product(*(DOMAINS[s] for _, s in varspec)))
    rowindex = {r: i for i, r in enumerate(rows)}
    gperm = [rowindex[tuple(gmaps[s][val] for val, (_, s) in zip(r, varspec))]
             for r in rows]

    # kept[sort] : semantic-vector -> (depth, syntax)
    kept: dict[str, dict[tuple, tuple[int, str]]] = {}
    n_candidates = 0

    def put(sort, vec, d, syn):
        tbl = kept.setdefault(sort, {})
        if vec not in tbl:
            tbl[vec] = (d, syn)
            return True
        return False

    # depth 1: variables and constants
    for j, (vn, s) in enumerate(varspec):
        put(s, tuple(r[j] for r in rows), 1, vn)
    for name, argsorts, ressort, fn in prims:
        if not argsorts:
            n_candidates += 1
            put(ressort, tuple(fn() for _ in rows), 1, f"{name}()")

    for d in range(2, depth + 1):
        new = []
        for name, argsorts, ressort, fn in prims:
            if not argsorts:
                continue
            pools = [[(vec, dep, syn) for vec, (dep, syn) in
                      kept.get(s, {}).items() if dep <= d - 1]
                     for s in argsorts]
            for combo in itertools.product(*pools):
                if max(c[1] for c in combo) != d - 1:
                    continue
                n_candidates += 1
                vec = tuple(fn(*(c[0][i] for c in combo))
                            for i in range(len(rows)))
                syn = f"{name}({', '.join(c[2] for c in combo)})"
                new.append((ressort, vec, d, syn))
        for ressort, vec, dd, syn in new:
            put(ressort, vec, dd, syn)

    violations = []
    counts = {}
    for sort, tbl in kept.items():
        counts[sort] = len(tbl)
        gm = gmaps[sort]
        for vec, (dd, syn) in tbl.items():
            for i in range(len(rows)):
                if not compare(vec[gperm[i]], gm[vec[i]]):
                    violations.append((sort, syn, rows[i]))
                    break
    return counts, n_candidates, violations


def closed_term_closure(prims, gmaps):
    """All parameter-free definable elements: close the constants under all
    primitives to fixpoint.  Returns (reachable, non_g_fixed)."""
    reach: dict[str, set] = {s: set() for s in DOMAINS}
    for name, argsorts, ressort, fn in prims:
        if not argsorts:
            reach[ressort].add(fn())
    changed = True
    while changed:
        changed = False
        for name, argsorts, ressort, fn in prims:
            if not argsorts:
                continue
            for args in itertools.product(*(sorted(reach[s], key=repr)
                                            for s in argsorts)):
                v = fn(*args)
                if v not in reach[ressort]:
                    reach[ressort].add(v)
                    changed = True
    non_fixed = [(s, v) for s, vs in reach.items() for v in vs
                 if gmaps[s][v] != v]
    return reach, non_fixed


# =====================================================================
# Main: checks with pre-declared expectations
# =====================================================================


def main() -> None:
    checks: list[tuple[str, bool, bool]] = []

    def check(name, value, expected=True):
        checks.append((name, bool(value), expected))

    # ---------------- [T] setup / definitional
    check("[T] t1: g is an involution on every sort (g o g = id)",
          all(GMAPS[s][GMAPS[s][a]] == a for s in DOMAINS for a in DOMAINS[s]))
    check("[T] t2: every domain is g-closed (g is a bijection of each domain "
          "onto itself)",
          all(len({GMAPS[s][a] for a in DOMAINS[s]}) == len(DOMAINS[s])
              and {GMAPS[s][a] for a in DOMAINS[s]} == set(DOMAINS[s])
              for s in DOMAINS))
    check("[T] t3: S is an orthogonal involution with S eta S = -eta",
          np.allclose(S4 @ S4, np.eye(4)) and np.allclose(S4, S4.T)
          and np.allclose(S4 @ ETA4 @ S4, -ETA4))
    check("[T] t4: the sector swap has NO fixed point on {K+, K-}",
          GMAPS["Sector"]["KP"] != "KP" and GMAPS["Sector"]["KM"] != "KM")
    check("[T] t5: all states consistent; all observer scripts admissible "
          "monotone issuance chains",
          all(consistent(s) for s in STATES)
          and all(consistent(history(o, t)) and history(o, t) <=
                  history(o, t + 1) for o in OBS_DATA for t in range(HMAX)))

    # ---------------- [E1] the battery = induction step of T1, exhaustively
    viol, n_tuples = battery(SIGMA, GMAPS, good_compare)
    check(f"[E] e1: primitive-equivariance battery -- ALL {len(SIGMA)} "
          f"symbols x ALL argument tuples ({n_tuples} tuples), 0 violations "
          "(graph(g) is a subalgebra of MxM; membership test for class H)",
          len(viol) == 0)

    # ---------------- [E2] CTX-A {x:Gen} depth 6: orbit indistinguishability
    counts_a, cand_a, viol_a = enumerate_and_verify(
        [("x", "Gen")], 6, SIGMA, GMAPS, good_compare)
    check(f"[E] e2: CTX-A {{x:Gen}} depth<=6 -- {sum(counts_a.values())} "
          f"distinct definable functionals ({cand_a} candidate applications), "
          "EVERY one flip-equivariant => no Sigma-term of any sort separates "
          "A from flip(A) with flipped context (orbit lemma, completeness "
          "form over the fragment)", len(viol_a) == 0)
    # explicit corollary scan (C2): Bool functionals of x are literally
    # constant on flip-orbits.  Re-enumerate CTX-A keeping the vectors.
    def scan_enum():
        varspec = [("x", "Gen")]
        rws = [(g,) for g in DOMAINS["Gen"]]
        ridx = {r: i for i, r in enumerate(rws)}
        gp = [ridx[(GMAPS["Gen"][r[0]],)] for r in rws]
        kept: dict[str, dict[tuple, tuple[int, str]]] = {}

        def put(sort, vec, d, syn):
            tbl = kept.setdefault(sort, {})
            if vec not in tbl:
                tbl[vec] = (d, syn)

        put("Gen", tuple(r[0] for r in rws), 1, "x")
        for name, argsorts, ressort, fn in SIGMA:
            if not argsorts:
                put(ressort, tuple(fn() for _ in rws), 1, f"{name}()")
        for d in range(2, 7):
            new = []
            for name, argsorts, ressort, fn in SIGMA:
                if not argsorts:
                    continue
                pools = [[(v, dep, sy) for v, (dep, sy) in
                          kept.get(s, {}).items() if dep <= d - 1]
                         for s in argsorts]
                for combo in itertools.product(*pools):
                    if max(c[1] for c in combo) != d - 1:
                        continue
                    vec = tuple(fn(*(c[0][i] for c in combo))
                                for i in range(len(rws)))
                    new.append((ressort, vec, d,
                                f"{name}({', '.join(c[2] for c in combo)})"))
            for rs, vec, dd, sy in new:
                put(rs, vec, dd, sy)
        return kept, rws, gp

    kept_scan, rws_scan, gp_scan = scan_enum()
    orbit_pairs = [(i, gp_scan[i]) for i in range(len(rws_scan))]
    scan_ok = all(vec[i] == vec[j]
                  for vec in kept_scan.get("Bool", {})
                  for (i, j) in orbit_pairs)
    check("[T] t6: corollary C2 exhibited -- every enumerated Bool functional "
          "phi satisfies phi(A) == phi(flip A) for every generator "
          "(entailed by T1+e1; direct scan)", scan_ok)

    # ---------------- [E3] CTX-B {x:Gen, o:Obs, t:Nat} depth 4 (coupling)
    counts_b, cand_b, viol_b = enumerate_and_verify(
        [("x", "Gen"), ("o", "Obs"), ("t", "Nat")], 4, SIGMA, GMAPS,
        good_compare)
    check(f"[E] e3: CTX-B {{x:Gen, o:Obs, t:Nat}} depth<=4 -- "
          f"{sum(counts_b.values())} distinct functionals ({cand_b} "
          "candidates), EVERY one flip-equivariant (issuance-to-spectrum "
          "coupling fragment)", len(viol_b) == 0)

    # ---------------- [E4] CTX-C {s:State, l:Lit, P:Pop, t:Nat} depth 4
    counts_c, cand_c, viol_c = enumerate_and_verify(
        [("s", "State"), ("l", "Lit"), ("P", "Pop"), ("t", "Nat")], 4,
        SIGMA, GMAPS, good_compare)
    check(f"[E] e4: CTX-C {{s:State, l:Lit, P:Pop, t:Nat}} depth<=4 -- "
          f"{sum(counts_c.values())} distinct functionals ({cand_c} "
          "candidates), EVERY one flip-equivariant (record/fork/aliveness "
          "fragment)", len(viol_c) == 0)

    # ---------------- [E5] CTX-D {v:Vec, x:Gen} depth 4 (eta fragment)
    counts_d, cand_d, viol_d = enumerate_and_verify(
        [("v", "Vec"), ("x", "Gen")], 4, SIGMA, GMAPS, good_compare)
    check(f"[E] e5: CTX-D {{v:Vec, x:Gen}} depth<=4 -- "
          f"{sum(counts_d.values())} distinct functionals ({cand_d} "
          "candidates), EVERY one flip-equivariant (eta-derivative fragment)",
          len(viol_d) == 0)

    # ---------------- [E6] closed terms: parameter-free definables
    reach, non_fixed = closed_term_closure(SIGMA, GMAPS)
    check("[E] e6: closed-term closure (corollary C1) -- every parameter-free "
          "definable element is g-fixed; Sector-definables = {NONE} exactly",
          len(non_fixed) == 0 and reach["Sector"] == {"NONE"})

    # ---------------- [T] C3: the UNORIENTED asymmetry is definable...
    asym = {g: PRE_CENERGY[g] != "NONE" for g in DOMAINS["Gen"]}
    check("[T] t7: corollary C3(i) -- 'exactly one sector spectrally "
          "positive' is Sigma-definable (not_(eq_sector(c_energy(x), "
          "none()))) and flip-INVARIANT; TRUE on the H_spec orbit",
          asym["H_spec"] and asym["H_spec~"]
          and all(asym[g] == asym[GEN_FLIP[g]] for g in asym))
    check("[T] t8: corollary C3(ii) -- ...but its ORIENTATION is equivariant, "
          "not invariant: c_energy(H_spec) and c_energy(flip H_spec) are the "
          "two DIFFERENT pair members (the selection flips with the orbit "
          "representative)",
          PRE_CENERGY["H_spec"] == "KP" and PRE_CENERGY["H_spec~"] == "KM")

    # ---------------- [T] twin-direction terms exhibited (inside class H)
    # A1 irreversibility-as-spectrum: coupled term using order + spectra.
    # A2 growth functional: record-count monotone.
    # A3 fork-realization: realized branch above s at literal l.
    def verify_term(varspec, fn, ressort):
        rws = list(itertools.product(*(DOMAINS[s] for _, s in varspec)))
        ridx = {r: i for i, r in enumerate(rws)}
        gp = [ridx[tuple(GMAPS[s][val] for val, (_, s) in zip(r, varspec))]
              for r in rws]
        vec = [fn(*r) for r in rws]
        return all(good_compare(vec[gp[i]], GMAPS[ressort][vec[i]])
                   for i in range(len(rws)))

    a1 = verify_term(
        [("o", "Obs"), ("t", "Nat")],
        lambda o, t: (PRE_CSTAB[{"alice": "A_c", "alice~": "A_c~",
                                 "bob": "H_spec", "bob~": "H_spec~",
                                 "carol": "A_bsym", "carol~": "A_bsym~"}[o]]
                      if live(o, t) else "NONE"),
        "Sector")
    check("[T] t9: twin A1 (irreversibility-as-spectrum) as a Sigma-term "
          "ite_sector(live(o,t), c_stab(assigned_gen(o)), none()) -- inside "
          "class H, flip-equivariant (selects only relative to the orbit "
          "representative)", a1)
    a2 = verify_term(
        [("o", "Obs"), ("t", "Nat")],
        lambda o, t: len(issued_after(o, t)),
        "Nat")
    check("[T] t10: twin A2 (growth functional) as a Sigma-term "
          "card(issued_after(o,t)) -- inside class H, flip-invariant "
          "(growth counts cannot see the sign)", a2)
    a3 = verify_term(
        [("s", "State"), ("l", "Lit"), ("P", "Pop"), ("t", "Nat")],
        lambda s, l, P, t: some_live_extender(add_lit(s, l), P, t),
        "Bool")
    check("[T] t11: twin A3 (fork-realization) as a Sigma-term "
          "some_live_extender(add_lit(s,l), P, t) -- inside class H, "
          "flip-equivariant (realization tracks the flipped branch)", a3)
    laneD = verify_term(
        [("l", "Lit"), ("P", "Pop"), ("t", "Nat")],
        lambda l, P, t: l in live_slice(P, t),
        "Bool")
    check("[T] t12: lane D's aliveness selection rule as a Sigma-term "
          "contains(live_slice(P,t), l) -- inside class H, flip-equivariant "
          "(reproduces lane D's framework theorem inside Sigma)", laneD)

    # ---------------- [F] controls (same code paths)
    # F1: sector-naming constant -- battery must catch it.
    viol_f1, _ = battery(SIGMA + [PRIM_KPLUS], GMAPS, good_compare)
    check("[F] f1: vocabulary + sector constant kplus() -- the SAME battery "
          "catches it (violations = exactly the kplus tuples)",
          len(viol_f1) > 0 and all(v[0] == "kplus" for v in viol_f1))
    # F1b: term-level -- the SAME enumeration/verification finds
    # non-equivariant TERMS (kplus() and its compounds).
    _, _, viol_f1t = enumerate_and_verify(
        [("x", "Gen")], 3, SIGMA + [PRIM_KPLUS], GMAPS, good_compare)
    f1_syntaxes = {v[1] for v in viol_f1t}
    check(f"[F] f1b: term enumeration over the kplus vocabulary finds "
          f"{len(viol_f1t)} non-equivariant terms incl. the depth-1 witness "
          "kplus() (same enumeration+verifier code path)",
          len(viol_f1t) > 0 and "kplus()" in f1_syntaxes)
    # F2: oriented-eta primitive (the sign posit restated, T-a') -- caught.
    viol_f2, _ = battery(SIGMA + [PRIM_ETACON], GMAPS, good_compare)
    f2_witnesses = {v[1][0] for v in viol_f2}
    check("[F] f2: vocabulary + eta_contractive (oriented-eta / T-a' "
          "label-reader) -- battery catches it; witnesses include the A_a "
          "and A_c orbits",
          len(viol_f2) > 0 and all(v[0] == "eta_contractive" for v in viol_f2)
          and "A_a" in f2_witnesses and "A_c" in f2_witnesses)
    # F3: sabotaged comparator (never flags) on the SAME battery + SAME
    # planted defect -- must MISS it (proves the pass in e1/f1 is the
    # comparison actually running, not plumbing).
    broken_compare = lambda got, want: True  # noqa: E731
    viol_f3, _ = battery(SIGMA + [PRIM_KPLUS], GMAPS, broken_compare)
    check("[F] f3: deliberately broken comparator on the same battery + same "
          "planted kplus defect reports 0 violations -- checker without "
          "teeth demonstrably fails", len(viol_f3) == 0)
    _, _, viol_f3t = enumerate_and_verify(
        [("x", "Gen")], 3, SIGMA + [PRIM_KPLUS], GMAPS, broken_compare)
    check("[F] f3b: broken comparator on the same term enumeration misses "
          "all term-level violations too", len(viol_f3t) == 0)
    # F4: sabotaged flip (forgets to swap sectors) -- kplus now passes AND
    # genuine equivariant primitives get falsely flagged: catching depends
    # on the correct g.
    gmaps_bad = dict(GMAPS)
    gmaps_bad["Sector"] = {s: s for s in DOMAINS["Sector"]}
    viol_f4, _ = battery(SIGMA + [PRIM_KPLUS], gmaps_bad, good_compare)
    f4_names = {v[0] for v in viol_f4}
    check("[F] f4: sabotaged flip (identity on Sector) -- the planted kplus "
          "is now MISSED while genuine mixed-sort primitives "
          "(c_stab/c_energy/sector_of) are falsely flagged: both verdict "
          "directions depend on the correct flip action (pure-Sector symbols "
          "like other/eq_sector commute with the identity trivially and are "
          "correctly not flagged)",
          "kplus" not in f4_names and "c_stab" in f4_names
          and "c_energy" in f4_names and "sector_of" in f4_names
          and "other" not in f4_names)

    # ---------------- report
    print("CONDITION 2' NO-GO FIXTURE: flip-equivariance completeness over a")
    print("finality/issuance-native signature (class H)")
    print("=" * 74)
    print(f"Signature Sigma: {len(SIGMA)} symbols "
          f"({sum(1 for p in SIGMA if not p[1])} constants, "
          f"{sum(1 for p in SIGMA if p[1])} primitives) over "
          f"{len(DOMAINS)} sorts")
    print(f"CTX-A counts by sort: { {k: v for k, v in sorted(counts_a.items())} }")
    print(f"CTX-B counts by sort: { {k: v for k, v in sorted(counts_b.items())} }")
    print(f"CTX-C counts by sort: { {k: v for k, v in sorted(counts_c.items())} }")
    print(f"CTX-D counts by sort: { {k: v for k, v in sorted(counts_d.items())} }")
    total_distinct = (sum(counts_a.values()) + sum(counts_b.values())
                      + sum(counts_c.values()) + sum(counts_d.values()))
    total_cand = cand_a + cand_b + cand_c + cand_d
    print(f"TOTAL: {total_distinct} distinct definable functionals verified "
          f"({total_cand} candidate term applications examined), "
          f"{n_tuples} battery tuples")
    print("-" * 74)
    failures = []
    for name, value, expected in checks:
        ok = value == expected
        print(f"{'PASS' if ok else 'UNEXPECTED'}  {name}: {value}")
        if not ok:
            failures.append(name)
    print()
    if failures:
        print("UNEXPECTED RESULTS:", failures)
        raise SystemExit(1)
    print("All checks match pre-declared expectations. Exit 0.")


if __name__ == "__main__":
    main()
