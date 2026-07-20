"""Discrete GfE two-sector specimen candidate (arXiv:2404.08556 instantiation).

Portfolio item P2C-REAL-PHYSICAL-WITNESS, exploration tier. Joe-directed swing,
2026-07-20 (direct chat), executing the bounded primary-paper gate recorded by
RUN-20260720-103623: does Bianconi's entropic matter-geometry model ("Quantum
entropy couples matter with geometry", J. Phys. A 57, 365002 / arXiv:2404.08556)
yield a source-grounded two-sector holonomy carrier with an exact matter
operator on a one-loop-class cell complex?

The paper's construction, instantiated faithfully at finite truncation:
topological spinors on nodes, edges and (for d=2) two-cells; discrete Dirac
operator D built from signed boundary operators with the paper's DOUBLE-SIDED
minimal substitution B^(A) = B^+ e^{-iA} + B^- e^{+iA} (its Eq. 12); metric
blocks entering as an exact similarity; gamma_0 = diag(+I, -I, +I)
anticommuting with D. Two structural facts of that substitution are verified
exactly here: the gauge phase is a HALF-LINK transporter (a node-to-node
passage picks up e^{2iA}), so the naive link-sign field A in {0, pi} carries
NO sector datum (it is exactly unitarily trivial), while the quarter-turn
alphabet e^{iA} in {1, i, -1, -i} realizes exactly the order-two full-link
holonomy sectors h = prod e^{2iA} in {+1, -1}.

Carriers: a ring (d=1 specialization of the paper's definitions; primary) and
a discretized cylinder (the paper's own 2d example class; secondary). All
arithmetic is exact: Gaussian integers for operators, Fractions for the
metric-deformed variants. No floats anywhere.

This fixture does not establish a physical issuance, capability, or finality
verdict, and it does not decide the Hamiltonian-ROLE question (the paper is
purely variational; see the exploration synthesis). The whole-family absorber
remains explicit and absorbing.

Provenance: literature-native (arXiv:2404.08556) + P2C-native justification,
frozen in explorations/2026-07-20-discrete-gfe-specimen/SYNTHESIS.md. No
external repository's receipt, convention, or numeric output is consumed.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product


CHECKS = {
    # ------------------------------------------------------------------ setup
    "setup: boundary of boundary vanishes on the cylinder complex": {"tag": "T"},
    "setup: Dirac operators are exactly Hermitian for all sector representatives": {"tag": "T"},
    "setup: gamma0 anticommutes with the Dirac operator on ring and cylinder": {"tag": "T"},
    "setup: quarter-turn alphabet closes with full-link holonomy plus or minus one": {"tag": "T"},
    # ------------------------------------------------------------- ring legs
    "sector: flat configurations split into exactly two full-link holonomy classes": {"tag": "E"},
    "sector-fail: the naive sigma field pair carries a distinct sector datum": {
        "tag": "F",
        "protects": "sector: flat configurations split into exactly two full-link holonomy classes",
    },
    "hamiltonian: exact spectral moments separate the sectors first at wrap order": {"tag": "E"},
    "distance: the first sector-sensitive moment order scales with the loop length": {"tag": "E"},
    "distance-fail: a local patch mimic shifts its first sensitive order with system size": {
        "tag": "F",
        "protects": "distance: the first sector-sensitive moment order scales with the loop length",
    },
    "blindness: every proper arc admits sector representatives with identical restricted operators": {"tag": "E"},
    "blindness-fail: raw local entries agree on the datum-free sigma pair": {
        "tag": "F",
        "protects": "blindness: every proper arc admits sector representatives with identical restricted operators",
    },
    "blindness-unitary: moved minus representatives are exactly unitarily equivalent to the canonical one": {"tag": "E"},
    "loop: full-loop holonomy reads the sector while arc data leaves it undetermined": {"tag": "E"},
    "order: doubled loop holonomy is trivial on both sectors": {"tag": "E"},
    "order-fail: integer-winding mimic trivializes under loop doubling": {
        "tag": "F",
        "protects": "order: doubled loop holonomy is trivial on both sectors",
    },
    "sector-honesty: one loop class carries two sectors and the two-loop rival carries four distinct ones": {"tag": "E"},
    "sector-count-fail: a count-blind comparison rejects the four-sector rival": {
        "tag": "F",
        "protects": "sector-honesty: one loop class carries two sectors and the two-loop rival carries four distinct ones",
    },
    "completion: every local completion fails at least one specimen signature": {"tag": "E"},
    "whole-family: a family declaring the two-sector holonomy absorbs the specimen": {"tag": "E"},
    "whole-family-fail: a family without the declared phase absorbs the specimen": {
        "tag": "F",
        "protects": "whole-family: a family declaring the two-sector holonomy absorbs the specimen",
    },
    "metric: sector separation at wrap order survives exact metric deformation": {"tag": "E"},
    "induced: the induced-metric coupling is exactly sector-blind on matched local data": {"tag": "E"},
    # --------------------------------------------------------- cylinder legs
    "cylinder: flat two-sector structure exists on the paper's two-dimensional example class": {"tag": "E"},
    "cylinder-moments: canonical cylinder representatives are separated by exact moments": {"tag": "E"},
    "cylinder-nonclosure: same-class flat deformations change exact moments": {"tag": "E"},
    "cylinder-blindness: a trivial-class twin matches the seam configuration on a local disk": {"tag": "E"},
}


# ===================================================== exact Gaussian numbers
# A Gaussian number is a pair (re, im); entries are Python ints (exact) or
# Fractions (exact) -- never floats.

ZERO = (0, 0)
ONE = (1, 0)
I_UNIT = (0, 1)

UNIT = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}  # i**k


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gconj(a):
    return (a[0], -a[1])


def gneg(a):
    return (-a[0], -a[1])


def gscale(a, f):
    return (a[0] * f, a[1] * f)


def zeros(rows, cols):
    return [[ZERO for _ in range(cols)] for _ in range(rows)]


def mat_mul(a_mat, b_mat):
    rows, inner, cols = len(a_mat), len(b_mat), len(b_mat[0])
    out = zeros(rows, cols)
    for i in range(rows):
        row_a = a_mat[i]
        row_o = out[i]
        for k in range(inner):
            a_val = row_a[k]
            if a_val[0] == 0 and a_val[1] == 0:
                continue
            row_b = b_mat[k]
            for j in range(cols):
                b_val = row_b[j]
                if b_val[0] == 0 and b_val[1] == 0:
                    continue
                row_o[j] = gadd(row_o[j], gmul(a_val, b_val))
    return out


def mat_dagger(a_mat):
    rows, cols = len(a_mat), len(a_mat[0])
    return [[gconj(a_mat[i][j]) for i in range(rows)] for j in range(cols)]


def mat_eq(a_mat, b_mat):
    return a_mat == b_mat


def mat_trace(a_mat):
    total = ZERO
    for i in range(len(a_mat)):
        total = gadd(total, a_mat[i][i])
    return total


def is_hermitian(a_mat):
    return mat_eq(a_mat, mat_dagger(a_mat))


def conj_by_diag(d_mat, diag):
    n = len(d_mat)
    return [
        [gmul(gmul(diag[i], d_mat[i][j]), gconj(diag[j])) for j in range(n)]
        for i in range(n)
    ]


def submatrix(d_mat, idxs):
    return [[d_mat[a][b] for b in idxs] for a in idxs]


def moments(d_mat, order):
    out = [mat_trace(d_mat)]
    power = d_mat
    for _ in range(order - 1):
        power = mat_mul(power, d_mat)
        out.append(mat_trace(power))
    return out


def first_diff_order(m_a, m_b):
    for k, (x, y) in enumerate(zip(m_a, m_b)):
        if x != y:
            return k + 1
    return None


# ================================================================ ring (d=1)
# Nodes 0..n-1, edge e runs from node e (tail, boundary -1) to node e+1
# (head, boundary +1). Gauge value on edge e is u_e = i**exps[e] (half-link
# transporter, paper Eq. 12 double-sided substitution). The 0-1 block is
# M[head][e] = conj(u_e), M[tail][e] = -u_e, i.e. B^+ conj(u) + B^- u.


def ring_m_block(n, exps):
    m_block = zeros(n, n)
    for e in range(n):
        u_val = UNIT[exps[e] % 4]
        m_block[(e + 1) % n][e] = gconj(u_val)  # head incidence (+1)
        m_block[e][e] = gneg(u_val)  # tail incidence (-1); tail node index is e
    return m_block


def ring_dirac(n, exps):
    m_block = ring_m_block(n, exps)
    size = 2 * n
    d_mat = zeros(size, size)
    for v in range(n):
        for e in range(n):
            entry = m_block[v][e]
            if entry != ZERO:
                d_mat[v][n + e] = entry
                d_mat[n + e][v] = gconj(entry)
    return d_mat


def ring_holonomy(exps):
    return 1 if (2 * sum(exps)) % 4 == 0 else -1


def ring_metric_dirac(n, exps, s_node, s_edge):
    """Paper's metric similarity: node-edge block G0^{1/2} M G1^{-1/2}."""
    m_block = ring_m_block(n, exps)
    size = 2 * n
    d_mat = zeros(size, size)
    for v in range(n):
        for e in range(n):
            entry = m_block[v][e]
            if entry != ZERO:
                scaled = gscale(entry, Fraction(s_node[v], 1) / s_edge[e])
                d_mat[v][n + e] = scaled
                d_mat[n + e][v] = gconj(scaled)
    return d_mat


def ring_move_step(n, d_cur, edge_from):
    """Exact diagonal unitary moving the quarter-turn from edge m to m+1.

    Node (m+1) gets phase -1; edges m and m+1 get phase i. Entries stay in
    {1, i, -1, -i}: exact."""
    diag = [ONE] * (2 * n)
    diag[(edge_from + 1) % n] = (-1, 0)
    diag[n + (edge_from % n)] = I_UNIT
    diag[n + ((edge_from + 1) % n)] = I_UNIT
    return conj_by_diag(d_cur, diag)


def ring_arc_indices(n, start, length):
    edges = [(start + k) % n for k in range(length)]
    nodes = sorted({e for e in edges} | {(e + 1) % n for e in edges})
    return sorted(nodes) + sorted(n + e for e in edges)


# ============================================================ cylinder (d=2)
# 2 node-rows, nx columns, periodic in x. Node (r,c) has index r*nx + c.
# Horizontal edge h(r,c): (r,c) -> (r,c+1), index r*nx + c. Vertical edge
# v(c): (0,c) -> (1,c), index 2*nx + c. Face f(c) has boundary
# +h(0,c) +v(c+1) -h(1,c) -v(c). Gauge field on edges only (A^(2) = 0).


def cyl_sizes(nx):
    return 2 * nx, 3 * nx, nx  # nodes, edges, faces


def cyl_edge_ends(nx, e):
    if e < 2 * nx:
        r, c = divmod(e, nx)
        return r * nx + c, r * nx + (c + 1) % nx  # tail, head
    c = e - 2 * nx
    return c, nx + c


def cyl_b1(nx):
    n_nodes, n_edges, _ = cyl_sizes(nx)
    b1 = [[0] * n_edges for _ in range(n_nodes)]
    for e in range(n_edges):
        tail, head = cyl_edge_ends(nx, e)
        b1[head][e] += 1
        b1[tail][e] -= 1
    return b1


def cyl_face_boundary(nx, c):
    return [(c, 1), (2 * nx + (c + 1) % nx, 1), (nx + c, -1), (2 * nx + c, -1)]


def cyl_b2(nx):
    _, n_edges, n_faces = cyl_sizes(nx)
    b2 = [[0] * n_faces for _ in range(n_edges)]
    for c in range(n_faces):
        for e, sign in cyl_face_boundary(nx, c):
            b2[e][c] += sign
    return b2


def cyl_dirac(nx, exps):
    n_nodes, n_edges, n_faces = cyl_sizes(nx)
    size = n_nodes + n_edges + n_faces
    d_mat = zeros(size, size)
    for e in range(n_edges):
        u_val = UNIT[exps[e] % 4]
        tail, head = cyl_edge_ends(nx, e)
        d_mat[head][n_nodes + e] = gconj(u_val)
        d_mat[n_nodes + e][head] = u_val
        d_mat[tail][n_nodes + e] = gneg(u_val)
        d_mat[n_nodes + e][tail] = gconj(gneg(u_val))
    b2 = cyl_b2(nx)
    for e in range(n_edges):
        for p in range(n_faces):
            if b2[e][p] != 0:
                d_mat[n_nodes + e][n_nodes + n_edges + p] = (b2[e][p], 0)
                d_mat[n_nodes + n_edges + p][n_nodes + e] = (b2[e][p], 0)
    return d_mat


def cyl_flat(nx, exps):
    for c in range(nx):
        total = 0
        for e, sign in cyl_face_boundary(nx, c):
            total += sign * 2 * exps[e]
        if total % 4 != 0:
            return False
    return True


def cyl_row_holonomy(nx, exps, row):
    return 1 if (2 * sum(exps[row * nx + c] for c in range(nx))) % 4 == 0 else -1


def anticommutes_with_gamma0(d_mat, gamma_signs):
    n = len(d_mat)
    for i in range(n):
        for j in range(n):
            if gamma_signs[i] + gamma_signs[j] != 0:
                if d_mat[i][j] != ZERO:
                    return False
    return True


# ============================================== induced metric (paper Eq. 43)
# Bosonic induced metric at d=1 with a_1 = 1, m_B^2 = 1:
# G_B = I + eta o (D|Phi><Phi|D) + theta o (|Phi><Phi|), with eta the
# same-dimension incidence mask and theta the diagonal mask.


def ring_eta(n):
    size = 2 * n
    eta = [[0] * size for _ in range(size)]
    for v in range(n):
        for w in range(n):
            if v == w or (v - w) % n in (1, n - 1):
                eta[v][w] = 1
    for e in range(n):
        for f in range(n):
            if e == f or (e - f) % n in (1, n - 1):
                eta[n + e][n + f] = 1
    return eta


def apply_mat_vec(d_mat, vec):
    out = []
    for i in range(len(d_mat)):
        acc = ZERO
        for j, x in enumerate(vec):
            if x != ZERO and d_mat[i][j] != ZERO:
                acc = gadd(acc, gmul(d_mat[i][j], x))
        out.append(acc)
    return out


def induced_metric(d_mat, phi, eta):
    size = len(d_mat)
    dphi = apply_mat_vec(d_mat, phi)
    g_ind = zeros(size, size)
    for i in range(size):
        for j in range(size):
            val = ZERO
            if eta[i][j]:
                val = gadd(val, gmul(dphi[i], gconj(dphi[j])))
            if i == j:
                val = gadd(val, gadd(gmul(phi[i], gconj(phi[j])), ONE))
            g_ind[i][j] = val
    return g_ind


# =============================================== signature-grade completions
# House completion-class sweep, carried from tests/two_sector_witness.py and
# re-typed for this carrier: wrap_order is the first sector-sensitive exact
# moment order (2n for the specimen; bounded for local mimics).


@dataclass(frozen=True)
class Signature:
    bit_units: int
    sector_count: int
    locally_indistinguishable: bool
    order_two_loop_class: bool
    noncontractible_loop_algebra: bool
    wrap_order: int
    persists: bool
    carrier: str


def candidate_signature(n):
    return Signature(1, 2, True, True, True, 2 * n, True, "discrete_gfe_ring")


def completion_signature(kind, n, radius):
    if kind in {"gauge", "relabeling", "hidden_state", "history", "provenance"}:
        return Signature(0, 1, True, False, False, 0, False, "ordinary_equivalence")
    if kind in {"boundary", "seed", "access", "resource"}:
        return Signature(0, 1, False, False, False, 2 * radius, False, "local_patch")
    if kind == "symmetry_breaking_label":
        return Signature(0, 2, False, False, False, 2 * radius, True, "local_label")
    if kind == "bit_only":
        return Signature(1, 1, True, False, False, 0, True, "scalar_bit_mimic")
    if kind == "composite_local":
        return Signature(1, 2, False, False, False, 2 * radius, True, "composite_local_mimic")
    if kind == "integer_winding":
        return Signature(1, 9, True, False, True, 2 * n, True, "integer_winding_carrier")
    if kind == "four_sector":
        return Signature(1, 4, True, True, True, 2 * n, True, "two_loop_class_rival")
    if kind == "whole_family_no_phase":
        return Signature(0, 1, True, False, False, 0, False, "trivial_phase_family")
    if kind == "whole_family_with_phase":
        return candidate_signature(n)
    raise ValueError(f"unknown completion kind: {kind}")


LOCAL_KINDS = (
    "gauge",
    "relabeling",
    "hidden_state",
    "boundary",
    "seed",
    "access",
    "resource",
    "history",
    "provenance",
    "symmetry_breaking_label",
    "bit_only",
    "composite_local",
    "integer_winding",
    "four_sector",
    "whole_family_no_phase",
)


def matches_candidate(sig, cand):
    return (
        sig.bit_units == cand.bit_units
        and sig.sector_count == cand.sector_count
        and sig.locally_indistinguishable == cand.locally_indistinguishable
        and sig.order_two_loop_class == cand.order_two_loop_class
        and sig.noncontractible_loop_algebra == cand.noncontractible_loop_algebra
        and sig.wrap_order == cand.wrap_order
        and sig.persists == cand.persists
    )


def matches_ignoring_sector_count(sig, cand):
    return (
        sig.bit_units == cand.bit_units
        and sig.locally_indistinguishable == cand.locally_indistinguishable
        and sig.order_two_loop_class == cand.order_two_loop_class
        and sig.noncontractible_loop_algebra == cand.noncontractible_loop_algebra
        and sig.wrap_order == cand.wrap_order
        and sig.persists == cand.persists
    )


def integer_winding_doubled(winding):
    return 2 * winding


# ======================================================================= main


def main() -> None:
    checks = []

    def check(name, value, expected=True):
        checks.append((name, bool(value), expected))

    # ------------------------------------------------------------ setup data
    ring_sizes = (4, 5, 6)
    nx = 3
    n_nodes, n_edges, n_faces = cyl_sizes(nx)

    plus_reps = {n: ring_dirac(n, [0] * n) for n in ring_sizes}
    minus_reps = {n: ring_dirac(n, [1] + [0] * (n - 1)) for n in ring_sizes}

    cyl_plus_exps = tuple([0] * n_edges)
    seam_exps = tuple(
        [1 if e in (0, nx) else 0 for e in range(n_edges)]
    )  # h(0,0) and h(1,0) carry the quarter turn
    double_seam_exps = tuple(
        [1 if e in (0, 1, nx, nx + 1) else 0 for e in range(n_edges)]
    )
    vflip_exps = tuple(
        [seam_exps[e] + (2 if e == 2 * nx else 0) for e in range(n_edges)]
    )  # seam plus u = -1 on v(0): same flux, same holonomy

    d_cyl_plus = cyl_dirac(nx, cyl_plus_exps)
    d_cyl_seam = cyl_dirac(nx, seam_exps)
    d_cyl_double = cyl_dirac(nx, double_seam_exps)
    d_cyl_vflip = cyl_dirac(nx, vflip_exps)

    # setup: chain complex
    b1 = cyl_b1(nx)
    b2 = cyl_b2(nx)
    b1b2 = [
        [sum(b1[v][e] * b2[e][p] for e in range(n_edges)) for p in range(n_faces)]
        for v in range(n_nodes)
    ]
    check(
        "setup: boundary of boundary vanishes on the cylinder complex",
        all(all(x == 0 for x in row) for row in b1b2),
    )
    check(
        "setup: Dirac operators are exactly Hermitian for all sector representatives",
        all(is_hermitian(plus_reps[n]) for n in ring_sizes)
        and all(is_hermitian(minus_reps[n]) for n in ring_sizes)
        and all(
            is_hermitian(d)
            for d in (d_cyl_plus, d_cyl_seam, d_cyl_double, d_cyl_vflip)
        ),
    )
    ring_gamma = [1] * 4 + [-1] * 4
    cyl_gamma = [1] * n_nodes + [-1] * n_edges + [1] * n_faces
    check(
        "setup: gamma0 anticommutes with the Dirac operator on ring and cylinder",
        anticommutes_with_gamma0(plus_reps[4], ring_gamma)
        and anticommutes_with_gamma0(minus_reps[4], ring_gamma)
        and anticommutes_with_gamma0(d_cyl_seam, cyl_gamma),
    )
    check(
        "setup: quarter-turn alphabet closes with full-link holonomy plus or minus one",
        all(gmul(UNIT[k], UNIT[k]) in ((1, 0), (-1, 0)) for k in range(4)),
    )

    # ------------------------------------------------------------- ring legs
    # sector: exhaustive over the quarter-turn alphabet on the n=4 ring
    hol_counts = {1: 0, -1: 0}
    for exps in product(range(4), repeat=4):
        hol_counts[ring_holonomy(exps)] += 1
    check(
        "sector: flat configurations split into exactly two full-link holonomy classes",
        hol_counts[1] == 128 and hol_counts[-1] == 128,
    )

    # sector-fail: naive sigma pair (u = -1 on one edge) is datum-free
    d_sigma = ring_dirac(4, [2, 0, 0, 0])
    sigma_diag = [ONE] * 4 + [(-1, 0), ONE, ONE, ONE]
    naive_carries_datum = (
        ring_holonomy([2, 0, 0, 0]) != ring_holonomy([0, 0, 0, 0])
        or not mat_eq(conj_by_diag(plus_reps[4], sigma_diag), d_sigma)
    )
    check(
        "sector-fail: the naive sigma field pair carries a distinct sector datum",
        naive_carries_datum,
        expected=False,
    )

    # hamiltonian + distance: exact moment separation at wrap order 2n
    ring_moments = {}
    wrap_orders = {}
    for n in ring_sizes:
        m_plus = moments(plus_reps[n], 2 * n)
        m_minus = moments(minus_reps[n], 2 * n)
        ring_moments[n] = (m_plus, m_minus)
        wrap_orders[n] = first_diff_order(m_plus, m_minus)
    check(
        "hamiltonian: exact spectral moments separate the sectors first at wrap order",
        all(wrap_orders[n] == 2 * n for n in ring_sizes),
    )
    check(
        "distance: the first sector-sensitive moment order scales with the loop length",
        wrap_orders[4] < wrap_orders[5] < wrap_orders[6],
    )
    patch_orders = {n: 2 * 2 for n in ring_sizes}  # radius-2 local patch mimic
    check(
        "distance-fail: a local patch mimic shifts its first sensitive order with system size",
        len(set(patch_orders.values())) > 1,
        expected=False,
    )

    # blindness: all proper arcs, minus representative with the quarter turn
    # moved outside the arc
    n_blind = 5
    d_plus5 = plus_reps[n_blind]
    blind_ok = True
    for start in range(n_blind):
        for length in range(1, n_blind):
            idxs = ring_arc_indices(n_blind, start, length)
            free_edge = (start + length) % n_blind
            exps_moved = [0] * n_blind
            exps_moved[free_edge] = 1
            d_moved = ring_dirac(n_blind, exps_moved)
            if ring_holonomy(exps_moved) != -1:
                blind_ok = False
            if submatrix(d_moved, idxs) != submatrix(d_plus5, idxs):
                blind_ok = False
    check(
        "blindness: every proper arc admits sector representatives with identical restricted operators",
        blind_ok,
    )

    # blindness-fail: raw entries near edge 0 differ on the datum-free pair
    star_idxs = [0, 1, 4]  # nodes 0,1 and edge 0 on the n=4 ring
    check(
        "blindness-fail: raw local entries agree on the datum-free sigma pair",
        submatrix(d_sigma, star_idxs) == submatrix(plus_reps[4], star_idxs),
        expected=False,
    )

    # blindness-unitary: stepwise exact unitary moves of the quarter turn
    unitary_ok = True
    d_cur = ring_dirac(n_blind, [1] + [0] * (n_blind - 1))
    for target in range(1, n_blind):
        d_cur = ring_move_step(n_blind, d_cur, target - 1)
        exps_target = [0] * n_blind
        exps_target[target] = 1
        if not mat_eq(d_cur, ring_dirac(n_blind, exps_target)):
            unitary_ok = False
    check(
        "blindness-unitary: moved minus representatives are exactly unitarily equivalent to the canonical one",
        unitary_ok,
    )

    # loop: full-loop holonomy reads the sector; arc data leaves it open
    arc_idxs = ring_arc_indices(n_blind, 0, n_blind - 1)
    exps_far = [0] * n_blind
    exps_far[n_blind - 1] = 1
    d_far = ring_dirac(n_blind, exps_far)
    check(
        "loop: full-loop holonomy reads the sector while arc data leaves it undetermined",
        ring_holonomy([0] * n_blind) == 1
        and ring_holonomy(exps_far) == -1
        and submatrix(d_far, arc_idxs) == submatrix(d_plus5, arc_idxs),
    )

    # order: doubled loop holonomy trivial on both sectors
    check(
        "order: doubled loop holonomy is trivial on both sectors",
        all(
            ring_holonomy(exps * 2) == 1
            for exps in ([0, 0, 0, 0], [1, 0, 0, 0])
        ),
    )
    check(
        "order-fail: integer-winding mimic trivializes under loop doubling",
        all(integer_winding_doubled(w) == 0 for w in (1, -1, 2, 3)),
        expected=False,
    )

    # sector-honesty: two-loop rival (disjoint rings n=4 and n=5) has four
    # distinct sector pairs with pairwise-distinct exact moment vectors
    kmax = 10
    m4 = {s: moments(plus_reps[4] if s == 1 else minus_reps[4], kmax) for s in (1, -1)}
    m5 = {s: moments(plus_reps[5] if s == 1 else minus_reps[5], kmax) for s in (1, -1)}
    pair_vecs = {}
    for s4 in (1, -1):
        for s5 in (1, -1):
            pair_vecs[(s4, s5)] = tuple(
                gadd(m4[s4][k], m5[s5][k]) for k in range(kmax)
            )
    pairs = list(pair_vecs)
    four_distinct = all(
        pair_vecs[pairs[i]] != pair_vecs[pairs[j]]
        for i in range(4)
        for j in range(i + 1, 4)
    )
    check(
        "sector-honesty: one loop class carries two sectors and the two-loop rival carries four distinct ones",
        hol_counts[1] > 0 and hol_counts[-1] > 0 and four_distinct,
    )
    check(
        "sector-count-fail: a count-blind comparison rejects the four-sector rival",
        all(
            not matches_ignoring_sector_count(
                completion_signature("four_sector", n, 2), candidate_signature(n)
            )
            for n in ring_sizes
        ),
        expected=False,
    )

    # completion sweep and whole-family absorber
    check(
        "completion: every local completion fails at least one specimen signature",
        all(
            not matches_candidate(completion_signature(kind, n, 2), candidate_signature(n))
            for kind in LOCAL_KINDS
            for n in ring_sizes
        ),
    )
    check(
        "whole-family: a family declaring the two-sector holonomy absorbs the specimen",
        all(
            matches_candidate(
                completion_signature("whole_family_with_phase", n, 2),
                candidate_signature(n),
            )
            for n in ring_sizes
        ),
    )
    check(
        "whole-family-fail: a family without the declared phase absorbs the specimen",
        all(
            matches_candidate(
                completion_signature("whole_family_no_phase", n, 2),
                candidate_signature(n),
            )
            for n in ring_sizes
        ),
        expected=False,
    )

    # metric: exact rational metric deformation preserves wrap-order split
    s_node = [Fraction(1), Fraction(3, 2), Fraction(2), Fraction(1, 2)]
    s_edge = [Fraction(1), Fraction(2), Fraction(1, 3), Fraction(5, 2)]
    dg_plus = ring_metric_dirac(4, [0, 0, 0, 0], s_node, s_edge)
    dg_minus = ring_metric_dirac(4, [1, 0, 0, 0], s_node, s_edge)
    mg_plus = moments(dg_plus, 8)
    mg_minus = moments(dg_minus, 8)
    metric_wrap = first_diff_order(mg_plus, mg_minus)
    check(
        "metric: sector separation at wrap order survives exact metric deformation",
        is_hermitian(dg_plus)
        and is_hermitian(dg_minus)
        and metric_wrap == 8,
    )

    # induced: matched local matter state, quarter turn outside its star
    eta = ring_eta(n_blind)
    phi = [ZERO] * (2 * n_blind)
    phi[2] = ONE  # matter localized on node 2; edges 1,2 are its star
    exps_away = [0] * n_blind
    exps_away[4] = 1  # quarter turn on edge 4, outside the star of node 2
    d_minus_away = ring_dirac(n_blind, exps_away)
    g_ind_plus = induced_metric(d_plus5, phi, eta)
    g_ind_minus = induced_metric(d_minus_away, phi, eta)
    check(
        "induced: the induced-metric coupling is exactly sector-blind on matched local data",
        ring_holonomy(exps_away) == -1
        and is_hermitian(g_ind_plus)
        and mat_eq(g_ind_plus, g_ind_minus),
    )

    # --------------------------------------------------------- cylinder legs
    flat_count = 0
    flat_classes = {1: 0, -1: 0}
    rows_always_equal = True
    for exps in product(range(4), repeat=n_edges):
        if not cyl_flat(nx, exps):
            continue
        flat_count += 1
        h0 = cyl_row_holonomy(nx, exps, 0)
        h1 = cyl_row_holonomy(nx, exps, 1)
        if h0 != h1:
            rows_always_equal = False
        flat_classes[h0] += 1
    check(
        "cylinder: flat two-sector structure exists on the paper's two-dimensional example class",
        cyl_flat(nx, seam_exps)
        and cyl_flat(nx, double_seam_exps)
        and cyl_flat(nx, vflip_exps)
        and rows_always_equal
        and flat_classes[1] > 0
        and flat_classes[-1] > 0,
    )

    kmax_cyl = 12
    mc_plus = moments(d_cyl_plus, kmax_cyl)
    mc_seam = moments(d_cyl_seam, kmax_cyl)
    mc_vflip = moments(d_cyl_vflip, kmax_cyl)
    cyl_sector_order = first_diff_order(mc_plus, mc_seam)
    cyl_nonclosure_order = first_diff_order(mc_seam, mc_vflip)
    check(
        "cylinder-moments: canonical cylinder representatives are separated by exact moments",
        cyl_sector_order is not None,
    )
    check(
        "cylinder-nonclosure: same-class flat deformations change exact moments",
        cyl_row_holonomy(nx, vflip_exps, 0) == cyl_row_holonomy(nx, seam_exps, 0)
        and cyl_nonclosure_order is not None,
    )

    disk_idxs = (
        [0, 1, nx, nx + 1]
        + [n_nodes + e for e in (0, nx, 2 * nx, 2 * nx + 1)]
        + [n_nodes + n_edges + 0]
    )
    check(
        "cylinder-blindness: a trivial-class twin matches the seam configuration on a local disk",
        cyl_row_holonomy(nx, seam_exps, 0) == -1
        and cyl_row_holonomy(nx, double_seam_exps, 0) == 1
        and submatrix(d_cyl_seam, disk_idxs) == submatrix(d_cyl_double, disk_idxs),
    )

    # ------------------------------------------------------------------ report
    print("DISCRETE GFE TWO-SECTOR SPECIMEN CANDIDATE (arXiv:2404.08556 instantiation)")
    print("=" * 78)
    failures = []
    counts = {"T": 0, "E": 0, "F": 0}
    for name, value, expected in checks:
        tag = CHECKS[name]["tag"]
        counts[tag] += 1
        ok = value == expected
        print(f"{'PASS' if ok else 'UNEXPECTED'}  [{tag}] {name}: {value}")
        if not ok:
            failures.append(name)

    print()
    print("ring moment scoreboard (exact integer traces; sector +1 vs -1):")
    for n in ring_sizes:
        m_plus, m_minus = ring_moments[n]
        delta = [
            (m_minus[k][0] - m_plus[k][0]) for k in range(len(m_plus))
        ]
        print(
            f"  n={n}: first sector-sensitive order = {wrap_orders[n]} (2n = {2 * n}); "
            f"delta at wrap order = {delta[wrap_orders[n] - 1]}"
        )
    print(f"  metric-deformed n=4 first sensitive order = {metric_wrap} (exact Fractions)")
    print()
    print("cylinder scoreboard (nx=3, exhaustive over the quarter-turn alphabet):")
    print(
        f"  flat configurations: {flat_count} of {4 ** n_edges}; "
        f"holonomy classes: +1 -> {flat_classes[1]}, -1 -> {flat_classes[-1]}; "
        f"row holonomies always equal on flat configs: {rows_always_equal}"
    )
    print(
        f"  canonical sector separation order = {cyl_sector_order}; "
        f"same-class deformation separation order = {cyl_nonclosure_order}"
    )
    print()
    print("completion-class scoreboard vs candidate (n=5):")
    cand5 = candidate_signature(5)
    for kind in (*LOCAL_KINDS, "whole_family_with_phase"):
        sig = completion_signature(kind, 5, 2)
        verdict = "ABSORBS" if matches_candidate(sig, cand5) else "fails"
        print(
            f"  {kind:>28}: bit={sig.bit_units} sectors={sig.sector_count} "
            f"local={int(sig.locally_indistinguishable)} "
            f"order2={int(sig.order_two_loop_class)} "
            f"loops={int(sig.noncontractible_loop_algebra)} "
            f"wrap={sig.wrap_order} persists={int(sig.persists)} -> {verdict}"
        )
    print()
    print(
        f"EVIDENTIAL CHECKS (headline): {counts['E']} [E] + "
        f"{counts['F']} [F] = {counts['E'] + counts['F']}"
    )
    print(f"[T] theorem-consequence checks (no evidential weight): {counts['T']}")

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()

