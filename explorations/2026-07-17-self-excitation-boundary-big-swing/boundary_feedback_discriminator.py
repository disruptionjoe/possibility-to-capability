"""Exploration-tier discriminator for selector, driver, feedback, and closure.

This is a deliberately small nonlinear-dynamics fixture. It does not model GU,
cosmology, a cell, or a physical firewall. Its only job is to make four concepts
fail differently while sharing the same damped bulk oscillator.
"""

from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass


GAMMA = 0.4
MU = 1.0
ETA = 0.1
ACTIVITY_SCALE = 0.1


@dataclass(frozen=True)
class Case:
    name: str
    external_clock: bool = False
    state_dependent_boundary: bool = False
    constraint_regenerated: bool = False
    positive_power_allowed: bool = True
    selector_value: float = 0.0
    driver_phase: float = 0.0


@dataclass
class Result:
    case: str
    late_mean: float
    late_std: float
    late_range: float
    late_upcrossings: int
    late_constraint_mean: float
    boundary_work: float
    bulk_dissipation: float
    oscillator_energy_change: float
    ledger_residual: float
    sustained_oscillation: bool
    classification: str


def boundary_output(case: Case, t: float, x: float, v: float, q: float) -> float:
    if case.name.startswith("selector"):
        raw = case.selector_value
    elif case.name == "driver":
        raw = 0.9 * math.cos(t + case.driver_phase)
    elif case.state_dependent_boundary:
        raw = q * (GAMMA + MU * (1.0 - x * x)) * v
    else:
        raw = 0.0

    if not case.positive_power_allowed and raw * v > 0.0:
        return 0.0
    return raw


def derivative(case: Case, t: float, x: float, v: float, q: float) -> tuple[float, float, float]:
    control = boundary_output(case, t, x, v, q)
    if case.constraint_regenerated:
        activity = v * v / (ACTIVITY_SCALE + v * v)
        q_dot = ETA * (activity - q)
    elif case.name == "closure_no_regeneration":
        q_dot = -ETA * q
    else:
        q_dot = 0.0
    return v, -x - GAMMA * v + control, q_dot


def simulate(
    case: Case,
    *,
    x0: float = 0.05,
    v0: float = 0.0,
    q0: float = 1.0,
    duration: float = 240.0,
    dt: float = 0.005,
    late_window: float = 40.0,
) -> Result:
    x, v, q = x0, v0, q0
    initial_energy = 0.5 * (x * x + v * v)
    boundary_work = 0.0
    bulk_dissipation = 0.0
    late_x: list[float] = []
    late_q: list[float] = []
    late_upcrossings = 0
    previous_x = x

    for step in range(int(duration / dt)):
        t = step * dt
        u0 = boundary_output(case, t, x, v, q)

        k1 = derivative(case, t, x, v, q)
        k2 = derivative(
            case,
            t + dt / 2.0,
            x + dt * k1[0] / 2.0,
            v + dt * k1[1] / 2.0,
            q + dt * k1[2] / 2.0,
        )
        k3 = derivative(
            case,
            t + dt / 2.0,
            x + dt * k2[0] / 2.0,
            v + dt * k2[1] / 2.0,
            q + dt * k2[2] / 2.0,
        )
        k4 = derivative(
            case,
            t + dt,
            x + dt * k3[0],
            v + dt * k3[1],
            q + dt * k3[2],
        )

        next_x = x + dt * (k1[0] + 2.0 * k2[0] + 2.0 * k3[0] + k4[0]) / 6.0
        next_v = v + dt * (k1[1] + 2.0 * k2[1] + 2.0 * k3[1] + k4[1]) / 6.0
        next_q = q + dt * (k1[2] + 2.0 * k2[2] + 2.0 * k3[2] + k4[2]) / 6.0

        u1 = boundary_output(case, t + dt, next_x, next_v, next_q)
        boundary_work += 0.5 * dt * (u0 * v + u1 * next_v)
        bulk_dissipation += 0.5 * dt * GAMMA * (v * v + next_v * next_v)

        if t >= duration - late_window:
            late_x.append(next_x)
            late_q.append(next_q)
            if previous_x < 0.0 <= next_x:
                late_upcrossings += 1

        previous_x = next_x
        x, v, q = next_x, next_v, next_q

    final_energy = 0.5 * (x * x + v * v)
    energy_change = final_energy - initial_energy
    ledger_residual = energy_change - (boundary_work - bulk_dissipation)
    late_mean = sum(late_x) / len(late_x)
    late_constraint_mean = sum(late_q) / len(late_q)
    late_std = math.sqrt(sum((value - late_mean) ** 2 for value in late_x) / len(late_x))
    late_range = max(late_x) - min(late_x)
    sustained = late_range > 1.0 and late_upcrossings >= 3

    if not sustained:
        classification = "NO_SUSTAINED_OSCILLATION"
    elif case.external_clock:
        classification = "EXTERNALLY_DRIVEN_OSCILLATION"
    elif case.constraint_regenerated:
        classification = "AUTONOMOUS_FEEDBACK_WITH_CONSTRAINT_CLOSURE"
    elif case.state_dependent_boundary:
        classification = "AUTONOMOUS_FEEDBACK_WITH_FIXED_CONSTRAINT"
    else:
        classification = "UNCLASSIFIED_SUSTAINED_OSCILLATION"

    return Result(
        case=case.name,
        late_mean=late_mean,
        late_std=late_std,
        late_range=late_range,
        late_upcrossings=late_upcrossings,
        late_constraint_mean=late_constraint_mean,
        boundary_work=boundary_work,
        bulk_dissipation=bulk_dissipation,
        oscillator_energy_change=energy_change,
        ledger_residual=ledger_residual,
        sustained_oscillation=sustained,
        classification=classification,
    )


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def main() -> None:
    cases = {
        "off": Case("off"),
        "selector_plus": Case("selector_plus", selector_value=0.35),
        "selector_minus": Case("selector_minus", selector_value=-0.35),
        "driver": Case("driver", external_clock=True),
        "fixed_feedback": Case("fixed_feedback", state_dependent_boundary=True),
        "feedback_no_injection": Case(
            "feedback_no_injection",
            state_dependent_boundary=True,
            positive_power_allowed=False,
        ),
        "closure_live": Case(
            "closure_live",
            state_dependent_boundary=True,
            constraint_regenerated=True,
        ),
        "closure_no_regeneration": Case(
            "closure_no_regeneration",
            state_dependent_boundary=True,
        ),
    }

    results = {name: simulate(case) for name, case in cases.items()}
    zero_seed = simulate(cases["fixed_feedback"], x0=0.0, v0=0.0)
    closure_unseeded = simulate(cases["closure_live"], q0=0.0)
    closure_subthreshold = simulate(cases["closure_live"], q0=0.75)
    closure_superthreshold = simulate(cases["closure_live"], q0=0.80)
    feedback_large_seed = simulate(cases["fixed_feedback"], x0=3.0)
    feedback_fine_step = simulate(cases["fixed_feedback"], dt=0.002)
    closure_subthreshold_fine_step = simulate(cases["closure_live"], q0=0.75, dt=0.002)
    closure_superthreshold_fine_step = simulate(cases["closure_live"], q0=0.80, dt=0.002)

    for result in results.values():
        require(abs(result.ledger_residual) < 1.0e-5, f"energy ledger failed: {result.case}")

    require(not results["off"].sustained_oscillation, "uncontrolled damped bulk must decay")
    require(not results["selector_plus"].sustained_oscillation, "selector must not become an oscillator")
    require(abs(results["selector_plus"].late_mean - 0.35) < 1.0e-6, "positive selector equilibrium")
    require(abs(results["selector_minus"].late_mean + 0.35) < 1.0e-6, "negative selector equilibrium")
    require(results["driver"].classification == "EXTERNALLY_DRIVEN_OSCILLATION", "driver classification")
    require(
        results["fixed_feedback"].classification == "AUTONOMOUS_FEEDBACK_WITH_FIXED_CONSTRAINT",
        "fixed feedback classification",
    )
    require(not zero_seed.sustained_oscillation, "exact zero is an invariant state, not creation from nothing")
    require(not results["feedback_no_injection"].sustained_oscillation, "positive resource flow is necessary")
    require(
        results["closure_live"].classification == "AUTONOMOUS_FEEDBACK_WITH_CONSTRAINT_CLOSURE",
        "closure classification",
    )
    require(results["closure_live"].late_constraint_mean > 0.7, "activity must maintain boundary constraint")
    require(not closure_unseeded.sustained_oscillation, "closure requires an initial viable boundary state")
    require(not closure_subthreshold.sustained_oscillation, "subthreshold closure seed must die")
    require(closure_superthreshold.sustained_oscillation, "superthreshold closure seed must live")
    require(
        not results["closure_no_regeneration"].sustained_oscillation,
        "fixed initial boundary must decay when regeneration is removed",
    )
    require(
        abs(results["fixed_feedback"].late_range - feedback_large_seed.late_range) < 1.0e-5,
        "small and large seeds must converge to the same attracting cycle",
    )
    require(
        abs(results["fixed_feedback"].late_range - feedback_fine_step.late_range) < 1.0e-5,
        "feedback cycle must survive step-size refinement",
    )
    require(not closure_subthreshold_fine_step.sustained_oscillation, "subthreshold result must survive refinement")
    require(closure_superthreshold_fine_step.sustained_oscillation, "superthreshold result must survive refinement")

    payload = {
        "model_scope": "toy discriminator only; no GU, biological, or cosmological claim",
        "shared_bulk": "x_dot=v; v_dot=-x-GAMMA*v+boundary_output",
        "results": {name: asdict(result) for name, result in results.items()},
        "controls": {
            "zero_seed_feedback": asdict(zero_seed),
            "closure_q0_0_00": asdict(closure_unseeded),
            "closure_q0_0_75": asdict(closure_subthreshold),
            "closure_q0_0_80": asdict(closure_superthreshold),
            "large_seed_feedback": asdict(feedback_large_seed),
            "fine_step_feedback": asdict(feedback_fine_step),
            "fine_step_closure_q0_0_75": asdict(closure_subthreshold_fine_step),
            "fine_step_closure_q0_0_80": asdict(closure_superthreshold_fine_step),
        },
        "headline": {
            "selector_is_not_excitation": True,
            "timed_drive_is_not_autonomous": True,
            "state_dependent_boundary_feedback_can_create_an_attracting_cycle": True,
            "positive_resource_transfer_is_required_in_this_model": True,
            "constraint_closure_can_maintain_but_does_not_explain_initial_viability": True,
        },
        "checks": 26,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
