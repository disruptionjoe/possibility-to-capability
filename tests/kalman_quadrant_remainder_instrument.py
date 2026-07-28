"""P2C calibration fixture: the Kalman-quadrant remainder instrument.

Exploration tier. Pure Python stdlib, deterministic, no dependencies, no
randomness. No claim promotion; no source claim status moves.

FRAMING GUARD (load-bearing, read first)
  This fixture claims ZERO novel typing. P2C's own methodology novelty scan
  (explorations/2026-07-22-methodology-novelty-genre-scan/SYNTHESIS.md)
  recorded the access/capability distinction as SUBSUMED by control theory's
  reachability/observability duality and the Kalman decomposition ("Not
  novel"), and the same folder's TRANSFER-BREAKER-PREREG-SKELETON.md row 2
  forecasts "TRANSFER FAILS -- Kalman decomposition already types this" for
  the computation/systems domain. This fixture BUILDS ON that verdict rather
  than contesting it: it makes the known mathematics executable as a
  calibration instrument -- a fully specified toy world with exact ground
  truth, where the reconstruction remainder is COMPUTED against the answer
  key instead of argued about. Instrument, not ontology.

THE WORLD (finite directed influence graph; everything declared below)
  Cells carry a static ground-truth parameter (what reconstruction is about)
  and a dynamic excitation state (packets). Node AGT emits agent actions;
  node REC collects the agent's verified interaction records. The agent is
  a process emitting actions and accumulating ONLY those records. Sectors:
    collision   wall, hinge, latch   agent actions reach them AND they feed
                                     the record channel (reachable, observable)
    render mesh mesh_a, mesh_b      agent actions reach them (probing
                                     excites them); NOTHING from them ever
                                     feeds records (reachable, not observable)
    sealed room room_a, room_b, vent agent actions can NEVER reach them; if
                                     the world's initial excitation differs
                                     there, later records differ -- they feed
                                     records only through free response via
                                     the vent (not reachable, observable)
    inert       rock, slab           neither (not reachable, not observable)

DEFINITIONS -- what the words mean HERE (graph closures; stated to block the
equivocation failure mode: these are this fixture's meanings, nothing else's)
  capability edge  a directed influence edge of the world graph, including
                   action edges AGT->c and record edges c->REC. An edge is an
                   arc. The six-arm-swing correction's line "a capability
                   edge is a cycle, not an arc" names the conjunctive reading
                   the teeth below vindicate: recoverability needs the round
                   trip (reached AND feeding records), not any single arc.
  reachable(c)     c is in the forward closure of AGT along edges.
  observable(c)    c is in the backward closure of REC along edges.
  record stream    the per-step sequence of sets of packets delivered to
                   REC. A packet accumulates a stamp (cell, value) for every
                   cell it is created at or moves onto.
  recoverable(c,T) over the declared world class, every class member whose
                   stream prefix of length T equals the true world's agrees
                   with the true world on param[c] (the posterior at the
                   truth collapses to a singleton). One definition, used
                   everywhere in this file.
  remainder R(T)   cells not recoverable at horizon T, computed DIRECTLY by
                   enumeration + simulation + stream matching. The FORMULA
                   path computes ~(reachable & observable) by graph closure
                   only. The two computations share only the world
                   declaration; neither consults the other's result.

KNOWN-INITIAL-STATE CAVEAT (load-bearing; both regimes executed)
  KNOWN-INIT   initial excitation declared known (= rest everywhere).
               Expected: direct remainder at the plateau EQUALS the formula
               ~(reachable & observable), exactly.
  UNKNOWN-INIT the unreachable sector's initial excitation is undeclared
               (the agent can never re-prepare that sector; the reachable
               sector relaxes to rest by itself in this pulse world, so its
               preparation is not in question). Expected: the not-reachable-
               but-observable cells become PARTLY recoverable through free
               response, so the direct remainder falls STRICTLY BELOW the
               formula floor. That divergence is the demonstrated caveat --
               the reason the known-initial-state declaration is load-
               bearing in the capability-formalism record -- not an
               instrument failure.

TEETH-CONTROLS (deliberately wrong hypotheses; each must FAIL, and the
fixture asserts the failure -- a passing tooth aborts the run)
  T1 edge-free hypothesis: remainder = cells carrying no capability edges.
     Must fail on the sealed room: room_a carries a dispositional out-edge
     (room_a->vent) and still sits in the known-init remainder.
  T2 ORIGINAL disjunctive downstream-only conjecture (the mailbox-spec
     form): remainder = exactly the causally-downstream-only structure
     (here: reachable and not observable). Must fail: the sealed room is
     not downstream-only yet is in the remainder. This executes, as a
     machine witness inside P2C, the counterexample shape recorded in the
     2026-07-27 six-arm-swing correction (H3 refuted; only the conjunctive
     Kalman reading survives). The correction is source-owned unratified
     thinking; this fixture's computation stands on its own either way.
  T3 render-mesh-observable control: asserts mesh_a is observable (graph
     leg) and that some record stream varies with mesh parameters (stream
     leg). Both legs must fail.
  POSITIVE reading that must PASS: known-init plateau remainder
     == ~(reachable & observable)  -- the conjunctive/Kalman reading.

ASSUMPTIONS (the instrument's class; outside it, no claim is made)
  A1 finite, deterministic, known dynamics; no noise; fixed probing policy
     that exercises every action edge (declared below). Recoverability is
     policy-relative below the floor; the symbolic discharge shows the
     floor itself is policy-independent.
  A2 records are maximally informative interaction outcomes: a delivered
     packet carries a faithful stamp (cell, param) for every cell on its
     path, EXCEPT the declared lossy sealed-room emission (room_b stamps
     param mod 2). Faithful stamps on the reachable-and-observable sector
     are required for the exact coincidence; a lossy collision channel
     would strand a reachable-and-observable cell in the direct remainder
     and break exactness. That is a declared falsifier surface, not a
     hidden case.
  A3 the reconstruction target is ground-truth parameters; dynamics and
     wiring are declared known (system identification of the rules is a
     different experiment, out of scope here).
  A4 "best case for reconstruction" reading: because records are maximally
     informative (A2), the remainder computed here is a STRUCTURAL floor --
     it comes from reach/influence topology, not from record poverty.

TEF REGISTRY: [T] setup/theorem-consequence (no evidential weight),
[E] genuine experiment, [F] failing-direction control (must fail; declares
what it protects). The headline counts [E] and [F] only.

Exit 0 iff every check matches its expectation. Expectations are declared
in this same file before execution; no external preregistration receipt
exists for this fixture.
"""

from __future__ import annotations

from itertools import product

AGT, REC = "AGT", "REC"

CELLS = ("wall", "hinge", "latch", "mesh_a", "mesh_b",
         "room_a", "room_b", "vent", "rock", "slab")

SECTOR = {
    "wall": "collision", "hinge": "collision", "latch": "collision",
    "mesh_a": "render_mesh", "mesh_b": "render_mesh",
    "room_a": "sealed_room", "room_b": "sealed_room", "vent": "sealed_room",
    "rock": "inert", "slab": "inert",
}

# Declared world-spec typing per sector as (reachable, observable). The [T]
# setup check verifies the graph closures reproduce this exactly.
SECTOR_QUADRANT = {
    "collision": (True, True),
    "render_mesh": (True, False),
    "sealed_room": (False, True),
    "inert": (False, False),
}

EDGES = (
    (AGT, "wall"), (AGT, "hinge"), (AGT, "mesh_a"),   # action edges
    ("hinge", "latch"), ("mesh_a", "mesh_b"),          # internal influence
    ("room_a", "vent"), ("room_b", "vent"),            # dispositional (room)
    ("wall", REC), ("latch", REC), ("vent", REC),      # record edges
)

PARAM_DOMAIN = {c: (0, 1) for c in CELLS}
PARAM_DOMAIN["room_b"] = (0, 1, 2)   # lossy emission needs a >2-value domain

TRUE_PARAMS = {"wall": 1, "hinge": 0, "latch": 1, "mesh_a": 1, "mesh_b": 0,
               "room_a": 1, "room_b": 0, "vent": 1, "rock": 0, "slab": 1}

LOSSY_STAMP_CELLS = ("room_b",)  # declared lossy sealed-room emission channel

# Probing policy: exercises every action edge, then idles so deep
# propagation and the free response can land. T_MAX bounds every horizon.
POLICY = (("probe", "wall"), ("probe", "hinge"), ("probe", "mesh_a"))
T_MAX = 8

# UNKNOWN-INIT regime: excitation varies on the sector the agent can never
# re-prepare. Declared literally here (sealed room + inert); the [T] setup
# check pins that this equals the unreachable sector, so the direct code
# path never consults the closure computation.
INIT_VARIABLE_CELLS = ("room_a", "room_b", "vent", "rock", "slab")
TRUE_INIT_UNKNOWN = frozenset({"room_a", "room_b"})


# ---------------------------------------------------------------------------
# FORMULA code path: graph closures only. No simulation, no enumeration.
# ---------------------------------------------------------------------------

def forward_closure(start: str) -> frozenset:
    out: dict = {}
    for a, b in EDGES:
        out.setdefault(a, set()).add(b)
    seen, stack = set(), [start]
    while stack:
        node = stack.pop()
        for nxt in sorted(out.get(node, ())):
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return frozenset(seen & set(CELLS))


def backward_closure(end: str) -> frozenset:
    inc: dict = {}
    for a, b in EDGES:
        inc.setdefault(b, set()).add(a)
    seen, stack = set(), [end]
    while stack:
        node = stack.pop()
        for prv in sorted(inc.get(node, ())):
            if prv not in seen:
                seen.add(prv)
                stack.append(prv)
    return frozenset(seen & set(CELLS))


def formula_remainder(reach: frozenset, obs: frozenset) -> frozenset:
    """~(reachable & observable), by closures alone."""
    return frozenset(c for c in CELLS if not (c in reach and c in obs))


# ---------------------------------------------------------------------------
# DIRECT code path: enumeration + simulation + stream matching.
# ---------------------------------------------------------------------------

def stamp(cell: str, params: dict) -> tuple:
    v = params[cell]
    if cell in LOSSY_STAMP_CELLS:
        return (cell, v % 2)
    return (cell, v)


def simulate(params: dict, excited: frozenset, T: int):
    """Deterministic pulse propagation. Returns (stream, touched).

    stream  tuple over steps of frozensets of delivered packets; a packet is
            a frozenset of stamps.
    touched cells that ever held a packet (used by the render-mesh check).
    """
    out: dict = {}
    for a, b in EDGES:
        out.setdefault(a, set()).add(b)
    state = {c: set() for c in CELLS}
    for c in excited:
        state[c].add(frozenset({stamp(c, params)}))
    touched = set(excited)
    stream = []
    for t in range(T):
        action = POLICY[t] if t < len(POLICY) else ("idle", None)
        if action[0] == "probe":
            state[action[1]].add(frozenset({stamp(action[1], params)}))
            touched.add(action[1])
        new_state = {c: set() for c in CELLS}
        delivered = set()
        for c in CELLS:
            for pkt in state[c]:
                for dst in out.get(c, ()):
                    if dst == REC:
                        delivered.add(pkt)
                    elif dst in new_state:
                        new_state[dst].add(pkt | {stamp(dst, params)})
                        touched.add(dst)
        state = new_state
        stream.append(frozenset(delivered))
    return tuple(stream), frozenset(touched)


def init_subsets() -> tuple:
    cells = INIT_VARIABLE_CELLS
    subs = []
    for mask in range(2 ** len(cells)):
        subs.append(frozenset(c for i, c in enumerate(cells) if mask >> i & 1))
    return tuple(subs)


def build_members(regime: str) -> list:
    """Every (params, init, stream-at-T_MAX) in the regime's world class."""
    inits = (frozenset(),) if regime == "known" else init_subsets()
    members = []
    for values in product(*(PARAM_DOMAIN[c] for c in CELLS)):
        params = dict(zip(CELLS, values))
        for init in inits:
            stream, _ = simulate(params, init, T_MAX)
            members.append((params, init, stream))
    return members


def posterior_at_truth(members: list, true_stream: tuple, T: int) -> dict:
    prefix = true_stream[:T]
    post = {c: set() for c in CELLS}
    for params, _init, stream in members:
        if stream[:T] == prefix:
            for c in CELLS:
                post[c].add(params[c])
    return post


def direct_remainder(post: dict) -> frozenset:
    return frozenset(c for c in CELLS if len(post[c]) > 1)


# ---------------------------------------------------------------------------
# Teeth hypothesis sets (the deliberately wrong readings)
# ---------------------------------------------------------------------------

def edge_free_cells() -> frozenset:
    """T1's prediction: cells incident to no capability edge at all."""
    touched = set()
    for a, b in EDGES:
        touched.add(a)
        touched.add(b)
    return frozenset(c for c in CELLS if c not in touched)


def downstream_only_cells(reach: frozenset, obs: frozenset) -> frozenset:
    """T2's prediction: reachable-from-agent cells feeding no records."""
    return frozenset(c for c in reach if c not in obs)


# ---------------------------------------------------------------------------
# TEF check registry
# ---------------------------------------------------------------------------

CHECKS = {
    "setup: graph closures reproduce the declared sector typing and the"
    " unknown-init sector equals the unreachable sector": {"tag": "T"},
    "setup: the declared policy exercises every action edge": {"tag": "T"},
    "rcurve: R(T+1) subset-of R(T) in both regimes (prefix-nesting"
    " consequence; no evidential weight)": {"tag": "T"},
    "kalman: known-init direct remainder at horizon T_MAX equals"
    " ~(reachable & observable) computed by closures": {"tag": "E"},
    "rcurve: the structural floor is reached at finite T and no further"
    " records help through T_MAX": {"tag": "E"},
    "sealed room: under known-init the stream carries zero information"
    " about the room (full posteriors) despite the dispositional edge":
        {"tag": "E"},
    "caveat: dropping the known-init declaration strictly shrinks the"
    " remainder through free response (room_a and vent recovered)":
        {"tag": "E"},
    "caveat: the lossy free response only partly constrains room_b"
    " (posterior shrinks to a doubleton, room_b stays in the remainder)":
        {"tag": "E"},
    "render mesh: agent actions excite it, yet no delivered packet in"
    " either regime carries a mesh stamp": {"tag": "E"},
    "t1-fail: edge-free hypothesis (remainder = cells with no capability"
    " edges) is rejected; witness: sealed room's dispositional edge": {
        "tag": "F",
        "protects": "kalman: known-init direct remainder at horizon T_MAX"
        " equals ~(reachable & observable) computed by closures",
    },
    "t2-fail: ORIGINAL disjunctive downstream-only conjecture (remainder ="
    " exactly the downstream-only structure) is rejected; witness: sealed"
    " room in remainder, not downstream-only": {
        "tag": "F",
        "protects": "kalman: known-init direct remainder at horizon T_MAX"
        " equals ~(reachable & observable) computed by closures",
    },
    "t3-fail: render-mesh-observable control is rejected on both the graph"
    " leg and the stream leg": {
        "tag": "F",
        "protects": "render mesh: agent actions excite it, yet no delivered"
        " packet in either regime carries a mesh stamp",
    },
}


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def fmt(cells) -> str:
    return "{" + ", ".join(sorted(cells)) + "}" if cells else "{}"


def main() -> int:
    print("P2C CALIBRATION FIXTURE: KALMAN-QUADRANT REMAINDER INSTRUMENT")
    print("=" * 76)
    print("FRAMING GUARD: zero novel typing is claimed. The Kalman")
    print("decomposition already types this (P2C novelty scan: SUBSUMED;")
    print("transfer-breaker row 2: TRANSFER FAILS). This is a calibration")
    print("instrument that makes the known mathematics executable.")

    # ---- formula code path ----
    reach = forward_closure(AGT)
    obs = backward_closure(REC)
    remainder_formula = formula_remainder(reach, obs)

    quadrant = {c: (c in reach, c in obs) for c in CELLS}
    q_ro = frozenset(c for c in CELLS if quadrant[c] == (True, True))
    q_rx = frozenset(c for c in CELLS if quadrant[c] == (True, False))
    q_xo = frozenset(c for c in CELLS if quadrant[c] == (False, True))
    q_xx = frozenset(c for c in CELLS if quadrant[c] == (False, False))

    print("\nWORLD (10 cells; edges as declared in EDGES)")
    print(f"  {'cell':8} {'sector':12} {'reach':6} {'obs':5} "
          f"{'domain':9} true")
    for c in CELLS:
        print(f"  {c:8} {SECTOR[c]:12} {str(c in reach):6} "
              f"{str(c in obs):5} {str(PARAM_DOMAIN[c]):9} {TRUE_PARAMS[c]}")

    print("\nKALMAN QUADRANTS (computed by graph closures)")
    print(f"   reachable &  observable : {fmt(q_ro)}")
    print(f"   reachable & ~observable : {fmt(q_rx)}   (downstream-only)")
    print(f"  ~reachable &  observable : {fmt(q_xo)}   (sealed room)")
    print(f"  ~reachable & ~observable : {fmt(q_xx)}   (inert)")

    # ---- direct code path, both regimes ----
    members_known = build_members("known")
    members_unknown = build_members("unknown")
    true_stream_known, touched_known = simulate(
        TRUE_PARAMS, frozenset(), T_MAX)
    true_stream_unknown, _ = simulate(TRUE_PARAMS, TRUE_INIT_UNKNOWN, T_MAX)

    curve_known, curve_unknown = [], []
    for T in range(T_MAX + 1):
        curve_known.append(direct_remainder(
            posterior_at_truth(members_known, true_stream_known, T)))
        curve_unknown.append(direct_remainder(
            posterior_at_truth(members_unknown, true_stream_unknown, T)))
    post_known = posterior_at_truth(members_known, true_stream_known, T_MAX)
    post_unknown = posterior_at_truth(
        members_unknown, true_stream_unknown, T_MAX)
    r_known = curve_known[T_MAX]
    r_unknown = curve_unknown[T_MAX]

    print(f"\nREMAINDER, TWO WAYS (horizon T={T_MAX})")
    print(f"  formula ~(reachable & observable)          : "
          f"{fmt(remainder_formula)} ({len(remainder_formula)})")
    print(f"  direct, KNOWN-INIT   ({len(members_known):>6} worlds)       : "
          f"{fmt(r_known)} ({len(r_known)})")
    print(f"  direct, UNKNOWN-INIT ({len(members_unknown):>6} worlds)       : "
          f"{fmt(r_unknown)} ({len(r_unknown)})")
    print("  KNOWN-INIT coincides with the formula; UNKNOWN-INIT falls")
    print(f"  strictly below it: {fmt(remainder_formula - r_unknown)} "
          "recovered through free response,")
    print(f"  room_b posterior {sorted(post_unknown['room_b'])} (partial, "
          "not pinned). THIS IS THE")
    print("  KNOWN-INITIAL-STATE CAVEAT, demonstrated in both regimes.")

    print("\nR-CURVE (remainder size vs record length)")
    print(f"  {'T':>2} {'R_known':>8} {'newly recovered':24} "
          f"{'R_unknown':>10} newly recovered")
    for T in range(T_MAX + 1):
        nk = fmt(curve_known[T - 1] - curve_known[T]) if T else "-"
        nu = fmt(curve_unknown[T - 1] - curve_unknown[T]) if T else "-"
        print(f"  {T:>2} {len(curve_known[T]):>8} {nk:24} "
              f"{len(curve_unknown[T]):>10} {nu}")
    floor_hits = [T for T in range(T_MAX + 1)
                  if curve_known[T] == remainder_formula]
    t_floor = floor_hits[0] if floor_hits else None
    print(f"  known-init floor {len(remainder_formula)} reached at T={t_floor}"
          f"; stable through T={T_MAX} (no further records help).")

    # ---- teeth hypothesis sets ----
    h_edge_free = edge_free_cells()
    h_downstream = downstream_only_cells(reach, obs)
    room_a_out_edges = [e for e in EDGES if e[0] == "room_a"]

    mesh_variant_streams_equal = True
    for cell in ("mesh_a", "mesh_b"):
        for v in PARAM_DOMAIN[cell]:
            if v == TRUE_PARAMS[cell]:
                continue
            alt = dict(TRUE_PARAMS)
            alt[cell] = v
            s_k, _ = simulate(alt, frozenset(), T_MAX)
            s_u, _ = simulate(alt, TRUE_INIT_UNKNOWN, T_MAX)
            if s_k != true_stream_known or s_u != true_stream_unknown:
                mesh_variant_streams_equal = False
    mesh_stamp_delivered = any(
        s[0] in ("mesh_a", "mesh_b")
        for stream in (true_stream_known, true_stream_unknown)
        for rec_set in stream for pkt in rec_set for s in pkt)

    print("\nTEETH (each deliberately wrong reading must FAIL)")
    print(f"  T1 edge-free      predicts {fmt(h_edge_free)}; actual "
          f"{fmt(r_known)}.")
    print(f"     Witness: room_a is in the remainder yet carries the"
          f" dispositional edge {room_a_out_edges[0]}.")
    print(f"  T2 downstream-only predicts {fmt(h_downstream)}; actual "
          f"{fmt(r_known)}.")
    print("     Witness: room_a is in the remainder and is NOT downstream-"
          "only (it feeds records,")
    print("     is not reachable). Machine witness for the six-arm-swing H3"
          " refutation: the")
    print("     disjunctive reading is false; the conjunctive/Kalman reading"
          " is the survivor.")
    print(f"  T3 mesh-observable graph leg: mesh_a in OBS = "
          f"{'mesh_a' in obs}; stream leg: some stream")
    print(f"     varies with mesh params = {not mesh_variant_streams_equal}."
          " Both legs false.")

    print("\nSYMBOLIC DISCHARGE (any policy, any horizon; known-init)")
    print("  A stamp of cell c enters a packet only when a packet is created")
    print("  at c (a probe: only action-edge targets, all reachable) or")
    print("  moves onto c (only along in-edges from an already-stamped")
    print("  packet, so only within the forward closure of AGT). A packet is")
    print("  delivered only along an edge into REC, so only from the")
    print("  backward closure of REC. Hence under known-init every delivered")
    print("  stamp names a cell in REACH & OBS, for EVERY policy and horizon:")
    print("  the floor ~(reachable & observable) is structural, not a policy")
    print("  artifact. (Under unknown-init, packet creation also happens at")
    print("  initially excited cells -- exactly the free-response door.)")

    # ---- checks ----
    results = []

    def check(name: str, value: bool) -> None:
        results.append((name, bool(value)))

    typing_ok = all(
        quadrant[c] == SECTOR_QUADRANT[SECTOR[c]] for c in CELLS
    ) and set(INIT_VARIABLE_CELLS) == set(CELLS) - set(reach)
    check(
        "setup: graph closures reproduce the declared sector typing and the"
        " unknown-init sector equals the unreachable sector",
        typing_ok,
    )
    check(
        "setup: the declared policy exercises every action edge",
        {b for a, b in EDGES if a == AGT}
        == {c for kind, c in POLICY if kind == "probe"},
    )
    check(
        "rcurve: R(T+1) subset-of R(T) in both regimes (prefix-nesting"
        " consequence; no evidential weight)",
        all(curve_known[T + 1] <= curve_known[T] for T in range(T_MAX))
        and all(curve_unknown[T + 1] <= curve_unknown[T]
                for T in range(T_MAX)),
    )
    check(
        "kalman: known-init direct remainder at horizon T_MAX equals"
        " ~(reachable & observable) computed by closures",
        r_known == remainder_formula,
    )
    check(
        "rcurve: the structural floor is reached at finite T and no further"
        " records help through T_MAX",
        t_floor is not None and t_floor < T_MAX
        and all(curve_known[T] == remainder_formula
                for T in range(t_floor, T_MAX + 1)),
    )
    check(
        "sealed room: under known-init the stream carries zero information"
        " about the room (full posteriors) despite the dispositional edge",
        all(post_known[c] == set(PARAM_DOMAIN[c])
            for c in ("room_a", "room_b", "vent")),
    )
    check(
        "caveat: dropping the known-init declaration strictly shrinks the"
        " remainder through free response (room_a and vent recovered)",
        r_unknown < r_known
        and "room_a" not in r_unknown and "vent" not in r_unknown,
    )
    check(
        "caveat: the lossy free response only partly constrains room_b"
        " (posterior shrinks to a doubleton, room_b stays in the remainder)",
        post_unknown["room_b"] == {0, 2} and "room_b" in r_unknown,
    )
    check(
        "render mesh: agent actions excite it, yet no delivered packet in"
        " either regime carries a mesh stamp",
        "mesh_a" in touched_known and "mesh_b" in touched_known
        and not mesh_stamp_delivered,
    )
    check(
        "t1-fail: edge-free hypothesis (remainder = cells with no capability"
        " edges) is rejected; witness: sealed room's dispositional edge",
        h_edge_free != r_known
        and "room_a" in r_known - h_edge_free
        and len(room_a_out_edges) > 0,
    )
    check(
        "t2-fail: ORIGINAL disjunctive downstream-only conjecture (remainder"
        " = exactly the downstream-only structure) is rejected; witness:"
        " sealed room in remainder, not downstream-only",
        h_downstream != r_known
        and "room_a" in r_known and "room_a" not in h_downstream,
    )
    check(
        "t3-fail: render-mesh-observable control is rejected on both the"
        " graph leg and the stream leg",
        "mesh_a" not in obs and mesh_variant_streams_equal,
    )

    n_e = sum(1 for n, _ in results if CHECKS[n]["tag"] == "E")
    n_f = sum(1 for n, _ in results if CHECKS[n]["tag"] == "F")
    n_t = sum(1 for n, _ in results if CHECKS[n]["tag"] == "T")
    print(f"\nCHECKS ({n_e} [E] + {n_f} [F] = {n_e + n_f} evidential; "
          f"{n_t} [T] setup, excluded from the headline)")
    failed = []
    for name, value in results:
        tag = CHECKS[name]["tag"]
        status = "PASS" if value else "FAIL"
        if not value:
            failed.append(name)
        print(f"  {status} [{tag}] {name}")

    print("\nVERDICT")
    if failed:
        print("  FIXTURE INVALID -- the following checks missed their")
        print("  declared expectations (teeth that passed or positives that")
        print("  failed are reported, not smoothed):")
        for name in failed:
            print(f"    {name}")
        return 1
    print("  The conjunctive/Kalman reading PASSES: known-init remainder =")
    print("  ~(reachable & observable), computed two independent ways.")
    print("  The edge-free and disjunctive downstream-only readings FAIL on")
    print("  the sealed room, as required. The known-initial-state caveat is")
    print("  demonstrated: free response partly recovers the unreachable-")
    print("  but-observable sector. Zero novel typing claimed; the SUBSUMED")
    print("  verdict stands. Calibration instrument only.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
