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
