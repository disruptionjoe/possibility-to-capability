"""Raw-transition restriction-diagram fixture P2C-IRD-001.

The fixture exhausts a four-state deterministic resource-labelled model.  It
tests direct-fiber/pullback equality, faithful bisimulation preservation, and
the exact construction changes that collapse the scoped separation.  It is not
a simulation of superconducting physics or a universal capability theorem.
"""

from __future__ import annotations

import itertools
import json
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Callable, Iterable


CHECKS = {
    "setup: IRD expectations were frozen before implementation": {"tag": "T"},
    "import: prior indexed-fork and finite descent results are unchanged": {"tag": "E"},
    "pullback: N and S restrictions preserve states actions transitions costs and observations": {"tag": "E"},
    "profile: exhaustive policies give N hold minimum one and S hold minimum zero": {"tag": "E"},
    "containment: W contains the task while the N evaluation fiber does not at base budget": {"tag": "E"},
    "theorem-a: direct fiber profile equals W-restricted profile": {"tag": "T"},
    "theorem-b: faithful relabel bisimulation preserves the bounded task profile": {"tag": "T"},
    "theorem-c: unequal profiles exclude a faithful N-S bisimulation": {"tag": "T"},
    "neutrality: carrier relabel preserves policies costs and verifier output": {"tag": "T"},
    "outcome: raw restriction diagram yields scoped profile separation": {"tag": "E"},
    "collapse taxonomy: preparation resource and interface mutants are typed separately": {"tag": "E"},
    "horizon: shortening the task horizon removes both profiles without favoring a fiber": {"tag": "E"},
    "cost-fail: altered pullback cost still commutes": {
        "tag": "F",
        "protects": "pullback: N and S restrictions preserve states actions transitions costs and observations",
    },
    "closure-fail: omitted reachable policy still equals exhaustive closure": {
        "tag": "F",
        "protects": "profile: exhaustive policies give N hold minimum one and S hold minimum zero",
    },
    "cool-fail: admitting COOL as evaluation leaves N unable at the same vector budget": {
        "tag": "F",
        "protects": "collapse taxonomy: preparation resource and interface mutants are typed separately",
    },
    "budget-fail: raising hold budget leaves N unable": {
        "tag": "F",
        "protects": "collapse taxonomy: preparation resource and interface mutants are typed separately",
    },
    "latch-fail: adding a zero-hold N interface action leaves N unable": {
        "tag": "F",
        "protects": "collapse taxonomy: preparation resource and interface mutants are typed separately",
    },
    "coarse-fail: state-count quotient certifies faithful N-S bisimulation": {
        "tag": "F",
        "protects": "theorem-c: unequal profiles exclude a faithful N-S bisimulation",
    },
    "verifier-fail: fiber-name verifier survives certified relabel": {
        "tag": "F",
        "protects": "neutrality: carrier relabel preserves policies costs and verifier output",
    },
    "family-fail: whole envelope and N fiber have one well-defined task profile": {
        "tag": "F",
        "protects": "containment: W contains the task while the N evaluation fiber does not at base budget",
    },
    "smuggling-fail: desired-verdict field is accepted into model specification": {
        "tag": "F",
        "protects": "outcome: raw restriction diagram yields scoped profile separation",
    },
}


@dataclass(frozen=True, order=True)
class Cost:
    prep: int = 0
    write: int = 0
    hold: int = 0

    def __add__(self, other: "Cost") -> "Cost":
        return Cost(
            self.prep + other.prep,
            self.write + other.write,
            self.hold + other.hold,
        )

    def within(self, limit: "Cost") -> bool:
        return (
            self.prep <= limit.prep
            and self.write <= limit.write
            and self.hold <= limit.hold
        )


@dataclass(frozen=True)
class Transition:
    source: str
    action: str
    target: str
    cost: Cost
    stage: str


@dataclass(frozen=True)
class Model:
    model_id: str
    states: tuple[str, ...]
    starts: tuple[str, ...]
    evaluation_actions: tuple[str, ...]
    transitions: tuple[Transition, ...]
    verifier_id: str = "carrier_neutral_digit_v1"


@dataclass(frozen=True)
class Trace:
    start: str
    actions: tuple[str, ...]
    states: tuple[str, ...]
    cost: Cost

    @property
    def final_state(self) -> str:
        return self.states[-1]


@dataclass(frozen=True)
class TaskContract:
    task_id: str
    limit: Cost
    max_length: int
    hold_actions: tuple[str, ...]
    error_tolerance: int
    verifier_semantics: str


BASE_LIMIT = Cost(prep=5, write=1, hold=0)
MAX_LENGTH = 3
BASE_HOLD_ACTIONS = ("IDLE", "DRIVE")
BASE_TASK = TaskContract(
    task_id="set_then_hold_digit_one",
    limit=BASE_LIMIT,
    max_length=MAX_LENGTH,
    hold_actions=BASE_HOLD_ACTIONS,
    error_tolerance=0,
    verifier_semantics="last_two_actions_SET_then_declared_hold_and_final_digit_exactly_one",
)
ALLOWED_SPEC_FIELDS = {
    "states",
    "starts",
    "evaluation_actions",
    "transitions",
    "verifier_id",
}
FORBIDDEN_SPEC_FIELDS = {
    "desired_verdict",
    "capability_label",
    "frame_winner",
    "finality_label",
}


def root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(*parts: str) -> dict:
    return json.loads(root().joinpath(*parts).read_text(encoding="utf-8"))


def digit(state: str) -> int:
    if not state or state[-1] not in "01":
        raise ValueError(f"state lacks carrier-neutral digit observation: {state}")
    return int(state[-1])


def transition_rows(prefix: str) -> tuple[Transition, ...]:
    zero, one = f"{prefix}0", f"{prefix}1"
    return (
        Transition(zero, "SET", one, Cost(write=1), "evaluation"),
        Transition(one, "SET", one, Cost(write=1), "evaluation"),
        Transition(zero, "IDLE", zero, Cost(), "evaluation"),
        Transition(
            one,
            "IDLE",
            zero if prefix == "N" else one,
            Cost(),
            "evaluation",
        ),
        Transition(zero, "DRIVE", zero, Cost(hold=1), "evaluation"),
        Transition(one, "DRIVE", one, Cost(hold=1), "evaluation"),
    )


def whole_envelope() -> Model:
    rows = [*transition_rows("N"), *transition_rows("S")]
    rows.extend(
        (
            Transition("N0", "COOL", "S0", Cost(prep=5), "preparation"),
            Transition("N1", "COOL", "S1", Cost(prep=5), "preparation"),
            Transition("S0", "COOL", "S0", Cost(), "preparation"),
            Transition("S1", "COOL", "S1", Cost(), "preparation"),
        )
    )
    return Model(
        model_id="W",
        states=("N0", "N1", "S0", "S1"),
        starts=("N0", "S0"),
        evaluation_actions=("SET", "IDLE", "DRIVE"),
        transitions=tuple(rows),
    )


def direct_fiber(prefix: str) -> Model:
    return Model(
        model_id=f"F_{prefix}",
        states=(f"{prefix}0", f"{prefix}1"),
        starts=(f"{prefix}0",),
        evaluation_actions=("SET", "IDLE", "DRIVE"),
        transitions=transition_rows(prefix),
    )


def restrict_evaluation(
    model: Model,
    states: tuple[str, ...],
    start: str,
    restriction_id: str,
) -> Model:
    state_set = set(states)
    rows = tuple(
        transition
        for transition in model.transitions
        if transition.stage == "evaluation"
        and transition.source in state_set
        and transition.target in state_set
        and transition.action in model.evaluation_actions
    )
    return Model(
        model_id=f"Res_{restriction_id}({model.model_id})",
        states=states,
        starts=(start,),
        evaluation_actions=model.evaluation_actions,
        transitions=rows,
        verifier_id=model.verifier_id,
    )


def transition_map(model: Model) -> dict[tuple[str, str], Transition]:
    result: dict[tuple[str, str], Transition] = {}
    for transition in model.transitions:
        key = (transition.source, transition.action)
        if key in result:
            raise ValueError(f"nondeterministic duplicate transition: {key}")
        result[key] = transition
    return result


def is_evaluation_closed(model: Model) -> bool:
    states = set(model.states)
    table = transition_map(model)
    return all(
        (state, action) in table
        and table[(state, action)].target in states
        and table[(state, action)].stage == "evaluation"
        for state in model.states
        for action in model.evaluation_actions
    )


def model_signature(model: Model) -> tuple:
    return (
        tuple(model.states),
        tuple(model.starts),
        tuple(model.evaluation_actions),
        tuple(
            sorted(
                (
                    row.source,
                    row.action,
                    row.target,
                    row.cost,
                    row.stage,
                    digit(row.source),
                    digit(row.target),
                )
                for row in model.transitions
            )
        ),
        model.verifier_id,
    )


def run_policy(model: Model, start: str, actions: tuple[str, ...]) -> Trace | None:
    if start not in model.starts:
        return None
    table = transition_map(model)
    state = start
    states = [state]
    cost = Cost()
    for action in actions:
        row = table.get((state, action))
        if row is None or action not in model.evaluation_actions:
            return None
        state = row.target
        states.append(state)
        cost = cost + row.cost
    return Trace(start, actions, tuple(states), cost)


def exhaustive_policies(
    model: Model, contract: TaskContract = BASE_TASK
) -> tuple[Trace, ...]:
    traces = []
    for start in model.starts:
        for length in range(contract.max_length + 1):
            for actions in itertools.product(model.evaluation_actions, repeat=length):
                trace = run_policy(model, start, actions)
                if trace is not None:
                    traces.append(trace)
    return tuple(traces)


def task_success(
    trace: Trace,
    contract: TaskContract = BASE_TASK,
    verifier: Callable[[Trace], bool] | None = None,
) -> bool:
    structural = (
        len(trace.actions) >= 2
        and trace.actions[-2] == "SET"
        and trace.actions[-1] in contract.hold_actions
        and digit(trace.final_state) == 1
        and trace.cost.within(contract.limit)
        and contract.error_tolerance == 0
    )
    return structural and (verifier(trace) if verifier else True)


def realizing_traces(
    model: Model,
    contract: TaskContract = BASE_TASK,
    verifier: Callable[[Trace], bool] | None = None,
) -> tuple[Trace, ...]:
    return tuple(
        trace
        for trace in exhaustive_policies(model, contract)
        if task_success(trace, contract, verifier)
    )


def realizes(
    model: Model,
    contract: TaskContract = BASE_TASK,
    verifier: Callable[[Trace], bool] | None = None,
) -> bool:
    return bool(realizing_traces(model, contract, verifier))


def minimum_hold_cost(model: Model) -> int | None:
    broad = replace(BASE_TASK, limit=Cost(prep=5, write=1, hold=9))
    successes = realizing_traces(model, broad)
    return min((trace.cost.hold for trace in successes), default=None)


def relabel_model(model: Model, old: str, new: str) -> Model:
    def rename(state: str) -> str:
        return new + state[1:] if state.startswith(old) else state

    return Model(
        model_id=f"relabel({model.model_id})",
        states=tuple(rename(state) for state in model.states),
        starts=tuple(rename(state) for state in model.starts),
        evaluation_actions=model.evaluation_actions,
        transitions=tuple(
            Transition(
                rename(row.source),
                row.action,
                rename(row.target),
                row.cost,
                row.stage,
            )
            for row in model.transitions
        ),
        verifier_id=model.verifier_id,
    )


def faithful_functional_bisimulation(
    left: Model,
    right: Model,
    mapping: dict[str, str],
    left_task: TaskContract = BASE_TASK,
    right_task: TaskContract = BASE_TASK,
) -> bool:
    if set(mapping) != set(left.states) or set(mapping.values()) != set(right.states):
        return False
    if tuple(mapping[start] for start in left.starts) != right.starts:
        return False
    if left.evaluation_actions != right.evaluation_actions:
        return False
    if left.verifier_id != right.verifier_id:
        return False
    if left_task != right_task:
        return False
    lt, rt = transition_map(left), transition_map(right)
    for state in left.states:
        if digit(state) != digit(mapping[state]):
            return False
        for action in left.evaluation_actions:
            lrow = lt.get((state, action))
            rrow = rt.get((mapping[state], action))
            if lrow is None or rrow is None:
                return False
            if mapping[lrow.target] != rrow.target or lrow.cost != rrow.cost:
                return False
            if lrow.stage != rrow.stage or digit(lrow.target) != digit(rrow.target):
                return False
    return True


def add_cool_to_evaluation(envelope: Model) -> Model:
    return Model(
        model_id="N_with_eval_COOL",
        states=envelope.states,
        starts=("N0",),
        evaluation_actions=("COOL", "SET", "IDLE", "DRIVE"),
        transitions=tuple(
            replace(row, stage="evaluation") if row.action == "COOL" else row
            for row in envelope.transitions
        ),
        verifier_id=envelope.verifier_id,
    )


def add_n_latch(model: Model) -> Model:
    rows = [*model.transitions]
    rows.extend(
        (
            Transition("N0", "LATCH_HOLD", "N0", Cost(), "evaluation"),
            Transition("N1", "LATCH_HOLD", "N1", Cost(), "evaluation"),
        )
    )
    return Model(
        model_id="N_with_interface_latch",
        states=model.states,
        starts=model.starts,
        evaluation_actions=(*model.evaluation_actions, "LATCH_HOLD"),
        transitions=tuple(rows),
        verifier_id="carrier_neutral_digit_with_latch_v1",
    )


def validate_model_spec(spec: dict) -> None:
    unknown = set(spec) - ALLOWED_SPEC_FIELDS
    if unknown:
        raise ValueError(f"forbidden or unknown model fields: {sorted(unknown)}")
    if FORBIDDEN_SPEC_FIELDS.intersection(spec):
        raise ValueError("verdict-carrying model specification")


def coarse_union_quotient(model: Model) -> tuple[
    dict[str, str], set[tuple[str, str, str, Cost]]
]:
    """The explicit N/S-forgetting quotient attacked by the preregistration."""
    quotient = {"N0": "q0", "S0": "q0", "N1": "q1", "S1": "q1"}
    transitions = {
        (quotient[row.source], row.action, quotient[row.target], row.cost)
        for row in model.transitions
        if row.stage == "evaluation"
    }
    return quotient, transitions


def quotient_is_deterministic(
    transitions: set[tuple[str, str, str, Cost]]
) -> bool:
    targets: dict[tuple[str, str], set[tuple[str, Cost]]] = {}
    for source, action, target, cost in transitions:
        targets.setdefault((source, action), set()).add((target, cost))
    return all(len(values) == 1 for values in targets.values())


def main() -> None:
    prereg = root().joinpath(
        "explorations", "2026-07-19-indexed-restriction-diagram", "PREREGISTRATION.md"
    ).read_text(encoding="utf-8")
    xframe_result = load_json(
        "explorations",
        "2026-07-19-cross-frame-descent-or-fork",
        "P2C-XFRAME-001.results.json",
    )
    descent_result = load_json(
        "explorations",
        "2026-07-19-profile-descent-theorem",
        "P2C-DESCENT-001.results.json",
    )

    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    check(
        "setup: IRD expectations were frozen before implementation",
        "status: expectations_frozen_before_execution" in prereg
        and "experiment_id: P2C-IRD-001" in prereg
        and "RESTRICTION_PROFILE_SEPARATION_SCOPED" in prereg,
    )
    check(
        "import: prior indexed-fork and finite descent results are unchanged",
        xframe_result["outcome"] == "INDEXED_CONSTRUCTION_FORK"
        and descent_result["result"]
        == "PROFILE_DESCENT_AND_FAITHFUL_TOP_LABEL_NON_DESCENT",
    )

    envelope = whole_envelope()
    direct_n, direct_s = direct_fiber("N"), direct_fiber("S")
    pull_n = restrict_evaluation(envelope, ("N0", "N1"), "N0", "N")
    pull_s = restrict_evaluation(envelope, ("S0", "S1"), "S0", "S")
    pullbacks_preserve = (
        is_evaluation_closed(pull_n)
        and is_evaluation_closed(pull_s)
        and model_signature(direct_n) == model_signature(replace(pull_n, model_id=direct_n.model_id))
        and model_signature(direct_s) == model_signature(replace(pull_s, model_id=direct_s.model_id))
    )
    check(
        "pullback: N and S restrictions preserve states actions transitions costs and observations",
        pullbacks_preserve,
    )

    n_min, s_min = minimum_hold_cost(direct_n), minimum_hold_cost(direct_s)
    n_policies, s_policies = exhaustive_policies(direct_n), exhaustive_policies(direct_s)
    check(
        "profile: exhaustive policies give N hold minimum one and S hold minimum zero",
        len(n_policies) == 40
        and len(s_policies) == 40
        and n_min == 1
        and s_min == 0,
    )
    w_contains = realizes(envelope)
    check(
        "containment: W contains the task while the N evaluation fiber does not at base budget",
        w_contains and not realizes(direct_n) and realizes(direct_s),
    )
    check(
        "theorem-a: direct fiber profile equals W-restricted profile",
        (minimum_hold_cost(direct_n), realizes(direct_n))
        == (minimum_hold_cost(pull_n), realizes(pull_n))
        and (minimum_hold_cost(direct_s), realizes(direct_s))
        == (minimum_hold_cost(pull_s), realizes(pull_s)),
    )

    relabeled_s = relabel_model(direct_s, "S", "T")
    s_to_t = {"S0": "T0", "S1": "T1"}
    relabel_is_faithful = faithful_functional_bisimulation(
        direct_s, relabeled_s, s_to_t
    )
    check(
        "theorem-b: faithful relabel bisimulation preserves the bounded task profile",
        relabel_is_faithful
        and minimum_hold_cost(direct_s) == minimum_hold_cost(relabeled_s)
        and realizes(direct_s) == realizes(relabeled_s),
    )
    n_to_s = {"N0": "S0", "N1": "S1"}
    check(
        "theorem-c: unequal profiles exclude a faithful N-S bisimulation",
        (minimum_hold_cost(direct_n), realizes(direct_n))
        != (minimum_hold_cost(direct_s), realizes(direct_s))
        and not faithful_functional_bisimulation(direct_n, direct_s, n_to_s),
    )
    check(
        "neutrality: carrier relabel preserves policies costs and verifier output",
        relabel_is_faithful
        and tuple((trace.actions, trace.cost, digit(trace.final_state)) for trace in s_policies)
        == tuple(
            (trace.actions, trace.cost, digit(trace.final_state))
            for trace in exhaustive_policies(relabeled_s)
        ),
    )

    outcome = (
        "RESTRICTION_PROFILE_SEPARATION_SCOPED"
        if pullbacks_preserve
        and w_contains
        and not realizes(direct_n)
        and realizes(direct_s)
        and not faithful_functional_bisimulation(direct_n, direct_s, n_to_s)
        else "BLOCKED_NONFAITHFUL_RESTRICTION"
    )
    check(
        "outcome: raw restriction diagram yields scoped profile separation",
        outcome == "RESTRICTION_PROFILE_SEPARATION_SCOPED",
    )

    cool_model = add_cool_to_evaluation(envelope)
    cool_collapse = realizes(cool_model, BASE_TASK)
    budget_collapse = realizes(
        direct_n, replace(BASE_TASK, limit=Cost(prep=5, write=1, hold=1))
    )
    latch_model = add_n_latch(direct_n)
    latch_collapse = realizes(
        latch_model,
        replace(
            BASE_TASK,
            hold_actions=(*BASE_HOLD_ACTIONS, "LATCH_HOLD"),
            verifier_semantics=(
                "last_two_actions_SET_then_declared_hold_including_interface_latch_"
                "and_final_digit_exactly_one"
            ),
        ),
    )
    collapse_outcomes = {
        "cool": "COLLAPSE_AFTER_PREPARATION_ADMISSION" if cool_collapse else "NO_COLLAPSE",
        "budget": "COLLAPSE_AFTER_RESOURCE_CHANGE" if budget_collapse else "NO_COLLAPSE",
        "latch": "INTERFACE_CONSTRUCTION_FORK" if latch_collapse else "NO_COLLAPSE",
    }
    check(
        "collapse taxonomy: preparation resource and interface mutants are typed separately",
        collapse_outcomes
        == {
            "cool": "COLLAPSE_AFTER_PREPARATION_ADMISSION",
            "budget": "COLLAPSE_AFTER_RESOURCE_CHANGE",
            "latch": "INTERFACE_CONSTRUCTION_FORK",
        },
    )
    short_task = replace(BASE_TASK, max_length=1)
    horizon_outcome = (
        "HORIZON_TOO_SHORT_ALL_FAIL"
        if not realizes(direct_n, short_task) and not realizes(direct_s, short_task)
        else "UNEXPECTED_HORIZON_PROFILE"
    )
    check(
        "horizon: shortening the task horizon removes both profiles without favoring a fiber",
        horizon_outcome == "HORIZON_TOO_SHORT_ALL_FAIL",
    )

    altered_rows = tuple(
        replace(row, cost=Cost(write=2))
        if row.source == "S0" and row.action == "SET"
        else row
        for row in pull_s.transitions
    )
    altered_pull_s = replace(pull_s, transitions=altered_rows)
    check(
        "cost-fail: altered pullback cost still commutes",
        model_signature(direct_s)
        == model_signature(replace(altered_pull_s, model_id=direct_s.model_id)),
        expected=False,
    )
    omitted = tuple(
        trace for trace in s_policies if trace.actions != ("SET", "IDLE")
    )
    check(
        "closure-fail: omitted reachable policy still equals exhaustive closure",
        omitted == s_policies,
        expected=False,
    )
    check(
        "cool-fail: admitting COOL as evaluation leaves N unable at the same vector budget",
        not cool_collapse,
        expected=False,
    )
    check(
        "budget-fail: raising hold budget leaves N unable",
        not budget_collapse,
        expected=False,
    )
    check(
        "latch-fail: adding a zero-hold N interface action leaves N unable",
        not latch_collapse,
        expected=False,
    )
    quotient, quotient_transitions = coarse_union_quotient(envelope)
    q1_idle_targets = {
        target
        for source, action, target, _cost in quotient_transitions
        if source == "q1" and action == "IDLE"
    }
    check(
        "coarse-fail: state-count quotient certifies faithful N-S bisimulation",
        quotient_is_deterministic(quotient_transitions)
        and q1_idle_targets == {"q0", "q1"}
        and faithful_functional_bisimulation(direct_n, direct_s, n_to_s),
        expected=False,
    )

    def target_loaded_verifier(trace: Trace) -> bool:
        return trace.final_state.startswith("S")

    target_original = realizes(direct_s, verifier=target_loaded_verifier)
    target_relabel = realizes(relabeled_s, verifier=target_loaded_verifier)
    check(
        "verifier-fail: fiber-name verifier survives certified relabel",
        target_original == target_relabel,
        expected=False,
    )
    starts_remain_distinct = quotient["N0"] != quotient["S0"]
    quotient_valid_for_indexed_profile = (
        starts_remain_distinct and quotient_is_deterministic(quotient_transitions)
    )
    check(
        "family-fail: whole envelope and N fiber have one well-defined task profile",
        quotient_valid_for_indexed_profile,
        expected=False,
    )

    spec = {
        "states": direct_n.states,
        "starts": direct_n.starts,
        "evaluation_actions": direct_n.evaluation_actions,
        "transitions": direct_n.transitions,
        "verifier_id": direct_n.verifier_id,
        "desired_verdict": "CAPABILITY_CHANGE",
    }
    accepted = True
    try:
        validate_model_spec(spec)
    except ValueError:
        accepted = False
    check(
        "smuggling-fail: desired-verdict field is accepted into model specification",
        accepted,
        expected=False,
    )

    print("P2C-IRD-001 INDEXED RESTRICTION DIAGRAM")
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
    print(f"N policies exhausted: {len(n_policies)}; minimum hold cost: {n_min}")
    print(f"S policies exhausted: {len(s_policies)}; minimum hold cost: {s_min}")
    print(f"base vector limit: prep={BASE_LIMIT.prep}, write={BASE_LIMIT.write}, hold={BASE_LIMIT.hold}")
    print(f"whole-envelope containment: {w_contains}")
    print(f"collapse mutations: {collapse_outcomes}")
    print(f"horizon mutation: {horizon_outcome}")
    print(f"coarse quotient q1/IDLE targets: {sorted(q1_idle_targets)}")
    print(f"OUTCOME: {outcome}")
    print("CEILING: finite transition model; no physical, universal, source, or finality promotion")
    print(f"EVIDENTIAL/TEETH HEADLINE: {counts['E']} [E] + {counts['F']} [F] = {counts['E'] + counts['F']}")
    print(f"[T] theorem-consequence checks (no evidential weight): {counts['T']}")

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All raw-transition checks match preregistered expectations. Exit 0.")


if __name__ == "__main__":
    main()
