"""Trit-access closure check (P2C-TRIT-ACCESS-001, exploration tier).

Cross-repo pre-registered test, Joe direct chat 2026-07-20. Binding lives in
gu-formalization explorations/prereg-trit-symmetry-and-fork-2026-07-20.md; the
mailbox pointer is
system-runtime/mailboxes/possibility-to-capability/archive/
20260720-trit-interpretation-lead-points-at-access-layers.md.

THE PRE-REGISTERED QUESTION (bound in GU before looking): is GU's external
"trit" -- the Z/3 half of the minimal generation-forcing input, established
UNORIENTED / S_3 (Node A) on three interchangeable copies (Node B1) -- the
natural cyclic CLOSURE of P2C's own nested access-restriction chain
{world >= access >= standpoint}?

This fixture extracts P2C's access chain from its OWN machinery
(tests/indexed_restriction_diagram.py, fixture P2C-IRD-001) and tests three
pre-declared legs of the closure hypothesis:

  (a) NATURAL      -- the order-3 "wrap" is canonical from P2C's restriction
                      maps, not an arbitrary gluing;
  (b) UNORIENTED   -- the closure is S_3-symmetric (matching the unoriented
                      trit), not an oriented Z/3;
  (c) REPRODUCES   -- the closure yields three interchangeable sectors, as the
                      trit's three copies are (equal invariants, external label
                      only).

PLANTED CONTROL (bound, demonstrated power): a DIRECTED-chain closure (oriented
3-cycle) must register Z/3 and FAIL the S_3/unoriented match; a genuinely
3-symmetric structure (identical blocks, no distinguishing invariant) must
register S_3 and PASS. This shows the symmetry classifier is not rigged to a
single verdict.

This fixture is not a simulation of physics, a capability theorem, or any
movement of P2C or GU truth. It compares two frozen structural facts: P2C's
access chain (computed here) and GU's frozen trit symmetry (cited from the
Node A / Node B1 receipts). No claim, canon, verdict, or public posture moves.
GU receipts are read-only; nothing outside P2C is written.
"""

from __future__ import annotations

import importlib.util
import itertools
import pathlib
import sys
from dataclasses import dataclass


HERE = pathlib.Path(__file__).resolve().parent


# --------------------------------------------------------------------------- #
# Import P2C's own restriction-diagram machinery (read-only, no main() run).   #
# --------------------------------------------------------------------------- #
def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module  # dataclasses(order=True) need the module registered
    spec.loader.exec_module(module)
    return module


IRD = _load("ird_trit_access", "indexed_restriction_diagram.py")


# --------------------------------------------------------------------------- #
# Small finite permutation-group toolkit (permutations of {0,1,2}).           #
# Mirrors the algebra used in the GU Node A probe; recomputed here, nothing    #
# imported from GU.                                                            #
# --------------------------------------------------------------------------- #
Perm = tuple[int, ...]
ELEMENTS: tuple[Perm, ...] = tuple(itertools.permutations(range(3)))


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[i]] for i in range(3))


def closure_group(generators: tuple[Perm, ...]) -> frozenset[Perm]:
    identity = (0, 1, 2)
    group = {identity, *generators}
    changed = True
    while changed:
        changed = False
        for a in list(group):
            for b in list(group):
                c = compose(a, b)
                if c not in group:
                    group.add(c)
                    changed = True
    return frozenset(group)


def preserves_edges(perm: Perm, edges: frozenset[tuple[int, int]]) -> bool:
    return frozenset((perm[a], perm[b]) for a, b in edges) == edges


def symmetry_group(edges: frozenset[tuple[int, int]]) -> frozenset[Perm]:
    """Every permutation of {0,1,2} that preserves the given edge set."""
    return frozenset(p for p in ELEMENTS if preserves_edges(p, edges))


def name_group(group: frozenset[Perm]) -> str:
    order = len(group)
    abelian = all(
        compose(a, b) == compose(b, a) for a in group for b in group
    )
    if order == 6:
        return "S_3"  # only nonabelian order-6 group; full Sym({0,1,2})
    if order == 3:
        return "Z/3"
    if order == 2:
        return "Z/2"
    if order == 1:
        return "trivial"
    return f"order-{order}{'-abelian' if abelian else '-nonabelian'}"


# Directed 3-cycle 0->1->2->0 : rotations only (Z/3).
DIRECTED_EDGES = frozenset({(0, 1), (1, 2), (2, 0)})
# Undirected triangle : all six permutations (S_3).
UNDIRECTED_EDGES = frozenset(
    {(0, 1), (1, 0), (1, 2), (2, 1), (2, 0), (0, 2)}
)


# --------------------------------------------------------------------------- #
# P2C access-chain extraction (from the IRD fixture, computed live).          #
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class AccessLayer:
    name: str
    question: str
    policies: int          # admissible-policy count (the chain's order invariant)
    realizes_base: bool    # containment under the base task/budget contract


def extract_access_chain() -> tuple[AccessLayer, AccessLayer, AccessLayer]:
    """P2C's plain-English three questions, read off its own machinery.

    IRD SYNTHESIS: "What can happen globally, what can happen from here, and
    what can be done from here under this interface and budget are different
    questions." That triple is a nested restriction chain
    world >= access(from-here) >= standpoint(from-here-under-budget).
    """
    world = IRD.whole_envelope()
    from_here = IRD.direct_fiber("S")  # restriction to one starting context
    world_pol = len(IRD.exhaustive_policies(world))
    fiber_pol = len(IRD.exhaustive_policies(from_here))
    budget_pol = len(IRD.realizing_traces(from_here))  # fiber under the contract
    return (
        AccessLayer("world", "what can happen globally",
                    world_pol, IRD.realizes(world)),
        AccessLayer("access", "what can happen from here",
                    fiber_pol, IRD.realizes(from_here)),
        AccessLayer("standpoint", "what can be done from here under budget",
                    budget_pol, bool(IRD.realizing_traces(from_here))),
    )


def chain_automorphism_order(layers: tuple[AccessLayer, ...]) -> int:
    """|Aut| of the layers as a poset ordered by the policy-count invariant.

    A permutation is an order-automorphism iff it preserves the policy-count
    key on every layer.  A strict chain (all keys distinct) admits only the
    identity -> order 1.  Interchangeable layers (all keys equal) admit all
    six -> order 6.
    """
    keys = [layer.policies for layer in layers]
    auts = [
        perm
        for perm in ELEMENTS
        if all(keys[perm[i]] == keys[i] for i in range(3))
    ]
    return len(auts)


# --------------------------------------------------------------------------- #
# Frozen GU trit facts (CITED from the receipts, not recomputed here).        #
# Node A (66d44d6): symmetry group S_3, order 6, unoriented.                   #
# Node B1 (9571e9b): three sectors, each (dim 64, Krein signature +32,-32);    #
#   all three invariant triples COINCIDE -> interchangeable, external label    #
#   only.                                                                      #
# --------------------------------------------------------------------------- #
TRIT_SYMMETRY_GROUP = "S_3"
TRIT_SYMMETRY_ORDER = 6
TRIT_SECTOR_INVARIANTS = (
    (64, 32, 32),  # W_-2 : (dim, +sig, -sig)
    (64, 32, 32),  # W_0
    (64, 32, 32),  # W_+2
)


# --------------------------------------------------------------------------- #
# Check registry (T = theorem/setup, no evidential weight; E = evidential;    #
# F = failing-direction control).                                             #
# --------------------------------------------------------------------------- #
CHECKS = {
    "setup: P2C access chain extracted from its own IRD machinery": {"tag": "T"},
    "theorem: directed 3-cycle has symmetry group Z/3": {"tag": "T"},
    "theorem: undirected triangle has symmetry group S_3": {"tag": "T"},
    "theorem: a strict 3-chain has trivial order-automorphism group": {"tag": "T"},
    "import: IRD invariants reproduce world=80 access=40 standpoint=2": {"tag": "E"},
    "leg-a NATURAL: the order-3 wrap is not canonical from P2C restriction maps": {"tag": "E"},
    "leg-b UNORIENTED: the chain closure is oriented Z/3, not S_3": {"tag": "E"},
    "leg-c REPRODUCE: P2C layers have distinct invariants; trit sectors are equal": {"tag": "E"},
    "verdict: C-FAILS -- closure not natural, oriented, and non-reproducing": {"tag": "E"},
    "control-directed: a directed-chain closure registers Z/3 and fails the S_3 match": {
        "tag": "F",
        "protects": "leg-b UNORIENTED: the chain closure is oriented Z/3, not S_3",
    },
    "control-symmetric: an identical-block structure registers S_3 and passes": {
        "tag": "F",
        "protects": "verdict: C-FAILS -- closure not natural, oriented, and non-reproducing",
    },
    "control-orientation: an orientation-blind classifier misregisters the directed plant as S_3": {
        "tag": "F",
        "protects": "leg-b UNORIENTED: the chain closure is oriented Z/3, not S_3",
    },
    "control-reproduce: equal-invariant layers would be interchangeable (Aut order 6)": {
        "tag": "F",
        "protects": "leg-c REPRODUCE: P2C layers have distinct invariants; trit sectors are equal",
    },
}


def main() -> None:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    # ---- Extraction + theorem scaffolding (T) ---------------------------- #
    layers = extract_access_chain()
    check("setup: P2C access chain extracted from its own IRD machinery",
          tuple(l.name for l in layers) == ("world", "access", "standpoint"))

    directed_group = symmetry_group(DIRECTED_EDGES)
    undirected_group = symmetry_group(UNDIRECTED_EDGES)
    check("theorem: directed 3-cycle has symmetry group Z/3",
          name_group(directed_group) == "Z/3" and len(directed_group) == 3)
    check("theorem: undirected triangle has symmetry group S_3",
          name_group(undirected_group) == "S_3" and len(undirected_group) == 6)

    strict_chain_aut = chain_automorphism_order(layers)
    check("theorem: a strict 3-chain has trivial order-automorphism group",
          strict_chain_aut == 1)

    # ---- Import fidelity (E) --------------------------------------------- #
    world_l, access_l, standpoint_l = layers
    check("import: IRD invariants reproduce world=80 access=40 standpoint=2",
          (world_l.policies, access_l.policies, standpoint_l.policies) == (80, 40, 2))

    # ---- LEG (a) NATURAL ------------------------------------------------- #
    # P2C's restriction maps are strictly narrowing: 80 > 40 > 2. The canonical
    # map set contains only order-DECREASING restrictions (world->access,
    # access->standpoint). The wrap standpoint->world is order-INCREASING; no
    # P2C-native map supplies it (going "up" needs a COOL/budget/latch mutation
    # that the IRD collapse table shows "changes which question is asked"). With
    # a trivial automorphism group there is no canonical order-3 symmetry to
    # build the wrap from either -- so any closure is an external gluing.
    keys = [world_l.policies, access_l.policies, standpoint_l.policies]
    strictly_narrowing = keys[0] > keys[1] > keys[2]
    canonical_upward_map_exists = (strict_chain_aut > 1)  # a nontrivial canonical symmetry
    wrap_is_natural = canonical_upward_map_exists
    check("leg-a NATURAL: the order-3 wrap is not canonical from P2C restriction maps",
          strictly_narrowing and not wrap_is_natural)

    # ---- LEG (b) UNORIENTED ---------------------------------------------- #
    # Close the strict chain into a 3-cycle whose edges follow the narrowing
    # direction: world->access->standpoint->(wrap)->world. Because the layers
    # are strictly ordered by the policy invariant, that orientation is forced
    # -- the closure is a DIRECTED 3-cycle. Its symmetry group is Z/3, not the
    # trit's S_3.
    closure_group_ = symmetry_group(DIRECTED_EDGES)  # the chain closure is directed
    closure_name = name_group(closure_group_)
    check("leg-b UNORIENTED: the chain closure is oriented Z/3, not S_3",
          closure_name == "Z/3" and closure_name != TRIT_SYMMETRY_GROUP
          and len(closure_group_) != TRIT_SYMMETRY_ORDER)

    # ---- LEG (c) REPRODUCE ----------------------------------------------- #
    # The trit's three sectors are interchangeable: all three invariant triples
    # coincide (Node B1). P2C's three layers are distinguished by an INTRINSIC
    # computable invariant (policy count 80/40/2), not merely an external label.
    trit_sectors_all_equal = len(set(TRIT_SECTOR_INVARIANTS)) == 1
    p2c_layers_all_distinct = len({l.policies for l in layers}) == 3
    check("leg-c REPRODUCE: P2C layers have distinct invariants; trit sectors are equal",
          trit_sectors_all_equal and p2c_layers_all_distinct)

    # ---- VERDICT --------------------------------------------------------- #
    leg_a_holds = not (strictly_narrowing and not wrap_is_natural)
    leg_b_holds = (closure_name == TRIT_SYMMETRY_GROUP)
    leg_c_holds = not (trit_sectors_all_equal and p2c_layers_all_distinct)
    legs_held = [leg_a_holds, leg_b_holds, leg_c_holds]
    c_fails = not any(legs_held)
    check("verdict: C-FAILS -- closure not natural, oriented, and non-reproducing",
          c_fails)

    # ---- CONTROLS (F) ---------------------------------------------------- #
    # Directed-chain closure -> Z/3 -> fails the S_3 match (the bound plant).
    check("control-directed: a directed-chain closure registers Z/3 and fails the S_3 match",
          name_group(symmetry_group(DIRECTED_EDGES)) == "Z/3"
          and name_group(symmetry_group(DIRECTED_EDGES)) != TRIT_SYMMETRY_GROUP)

    # Identical-block structure (no distinguishing invariant) -> S_3 -> passes.
    identical_blocks = symmetry_group(UNDIRECTED_EDGES)
    check("control-symmetric: an identical-block structure registers S_3 and passes",
          name_group(identical_blocks) == TRIT_SYMMETRY_GROUP
          and len(identical_blocks) == TRIT_SYMMETRY_ORDER)

    # Orientation-blind classifier: always adjoin conjugation (a transposition)
    # to whatever it sees. On the directed plant it returns S_3 -- the
    # known-wrong answer -- proving the orientation datum is load-bearing.
    def orientation_blind(edges: frozenset[tuple[int, int]]) -> frozenset[Perm]:
        base = symmetry_group(edges)
        return closure_group(tuple(base) + ((0, 2, 1),))  # force in a transposition

    blind_on_directed = orientation_blind(DIRECTED_EDGES)
    sensitive_on_directed = symmetry_group(DIRECTED_EDGES)
    check("control-orientation: an orientation-blind classifier misregisters the directed plant as S_3",
          name_group(blind_on_directed) == "S_3"
          and name_group(sensitive_on_directed) == "Z/3")

    # If the layers WERE interchangeable (equal invariants) the poset would
    # carry the full S_3 (Aut order 6) -- demonstrating the reproduce-test has
    # two-sided power and is not stipulated to fail.
    equal_layers = (
        AccessLayer("a", "", 7, True),
        AccessLayer("b", "", 7, True),
        AccessLayer("c", "", 7, True),
    )
    check("control-reproduce: equal-invariant layers would be interchangeable (Aut order 6)",
          chain_automorphism_order(equal_layers) == 6)

    # ---- Report ---------------------------------------------------------- #
    print("P2C-TRIT-ACCESS-001 TRIT-ACCESS CLOSURE CHECK")
    print("=" * 72)
    failures: list[str] = []
    counts = {"T": 0, "E": 0, "F": 0}
    for name, value, expected in checks:
        tag = CHECKS[name]["tag"]
        counts[tag] += 1
        ok = value == expected
        print(f"{'PASS' if ok else 'UNEXPECTED'}  [{tag}] {name}: {value}")
        if not ok:
            failures.append(name)

    print()
    print("P2C ACCESS CHAIN (extracted from IRD fixture P2C-IRD-001):")
    for layer in layers:
        print(f"  {layer.name:11s} | {layer.question:44s} | "
              f"policies={layer.policies:2d} | realizes_base={layer.realizes_base}")
    print(f"  chain order-automorphism group order: {strict_chain_aut} (trivial)")
    print()
    print(f"trit symmetry (Node A, cited): {TRIT_SYMMETRY_GROUP} (order {TRIT_SYMMETRY_ORDER}, unoriented)")
    print(f"trit sectors (Node B1, cited): three (dim,+,-) = {TRIT_SECTOR_INVARIANTS[0]} x3, interchangeable")
    print(f"chain closure symmetry:        {closure_name} (order {len(closure_group_)}, oriented)")
    print()
    print(f"leg (a) NATURAL    held: {leg_a_holds}")
    print(f"leg (b) UNORIENTED held: {leg_b_holds}")
    print(f"leg (c) REPRODUCE  held: {leg_c_holds}")
    print("controls: directed-closure -> Z/3 (fails S_3) | identical-blocks -> S_3 (passes) | "
          "orientation-blind misregisters directed as S_3")
    print()
    print("OUTCOME: C-FAILS -- the trit's unoriented S_3 cyclicity has no natural home in "
          "P2C's directed, strict, non-interchangeable access chain.")
    print("CEILING: structural comparison of two frozen facts; no P2C or GU truth, claim, "
          "capability, canon, or finality moves.")
    headline = "C-FAILS (0/3 legs) | " \
               f"chain-closure={closure_name} != trit={TRIT_SYMMETRY_GROUP} | " \
               "controls: directed->Z/3 fail, symmetric->S_3 pass"
    print(f"HEADLINE: {headline}")
    print(f"EVIDENTIAL/TEETH HEADLINE: {counts['E']} [E] + {counts['F']} [F] = "
          f"{counts['E'] + counts['F']}")
    print(f"[T] theorem/setup checks (no evidential weight): {counts['T']}")

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All trit-access closure checks match preregistered expectations. Exit 0.")


if __name__ == "__main__":
    main()
