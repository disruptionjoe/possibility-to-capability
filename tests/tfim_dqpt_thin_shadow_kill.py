"""TFIM-quench DQPT thin-shadow reconstruction kill.

This receiver-owned finite fixture compares two routes to the same exact
integrable Loschmidt probability. It tests the mapping and P2C overclaim
firewalls; it does not prove the source paper or generalize to all DQPTs.
"""

from __future__ import annotations

import cmath
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools import capability_diagnostic as td


SPECIMEN = ROOT / "explorations" / "2026-07-24-tfim-dqpt-thin-shadow-kill"
ASSESSMENT = SPECIMEN / "tfim-dqpt-v0.1.json"
CROSS_QUENCH = (0.4, 1.3)
SAME_PHASE_QUENCH = (0.4, 0.8)


def dispersion(momentum: float, field: float) -> float:
    return math.sqrt(
        (field - math.cos(momentum)) ** 2 + math.sin(momentum) ** 2
    )


def bogoliubov_angle(momentum: float, field: float) -> float:
    return 0.5 * math.atan2(
        math.sin(momentum), field - math.cos(momentum)
    )


def mode_amplitude_fixed_h(
    momentum: float, initial_field: float, final_field: float, time: float
) -> complex:
    phi = (
        bogoliubov_angle(momentum, initial_field)
        - bogoliubov_angle(momentum, final_field)
    )
    energy = dispersion(momentum, final_field)
    return math.cos(phi) ** 2 + math.sin(phi) ** 2 * cmath.exp(
        -2j * energy * time
    )


def mode_probability_closed(
    momentum: float, initial_field: float, final_field: float, time: float
) -> float:
    phi = (
        bogoliubov_angle(momentum, initial_field)
        - bogoliubov_angle(momentum, final_field)
    )
    energy = dispersion(momentum, final_field)
    return 1.0 - math.sin(2.0 * phi) ** 2 * math.sin(energy * time) ** 2


def positive_momenta(size: int) -> list[float]:
    if size <= 0 or size % 2:
        raise ValueError("size must be a positive even integer")
    return [(2 * mode + 1) * math.pi / size for mode in range(size // 2)]


def return_probability_fixed_h(
    size: int, initial_field: float, final_field: float, time: float
) -> float:
    probability = 1.0
    for momentum in positive_momenta(size):
        probability *= abs(
            mode_amplitude_fixed_h(
                momentum, initial_field, final_field, time
            )
        ) ** 2
    return probability


def return_probability_closed(
    size: int, initial_field: float, final_field: float, time: float
) -> float:
    probability = 1.0
    for momentum in positive_momenta(size):
        probability *= mode_probability_closed(
            momentum, initial_field, final_field, time
        )
    return probability


def rate_function(
    size: int, initial_field: float, final_field: float, time: float
) -> float:
    log_probability = 0.0
    for momentum in positive_momenta(size):
        probability = mode_probability_closed(
            momentum, initial_field, final_field, time
        )
        log_probability += math.log(max(probability, 1e-300))
    return -log_probability / size


def critical_momentum(
    initial_field: float, final_field: float
) -> float | None:
    denominator = initial_field + final_field
    if denominator == 0.0:
        return None
    cosine = (1.0 + initial_field * final_field) / denominator
    if cosine < -1.0 or cosine > 1.0:
        return None
    return math.acos(cosine)


def first_critical_time(
    initial_field: float, final_field: float
) -> float | None:
    momentum = critical_momentum(initial_field, final_field)
    if momentum is None:
        return None
    return math.pi / (2.0 * dispersion(momentum, final_field))


def max_mixing_weight(
    initial_field: float, final_field: float, samples: int = 20000
) -> float:
    values = []
    for index in range(samples):
        momentum = (index + 0.5) * math.pi / samples
        phi = (
            bogoliubov_angle(momentum, initial_field)
            - bogoliubov_angle(momentum, final_field)
        )
        values.append(math.sin(2.0 * phi) ** 2)
    return max(values)


def main() -> int:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    g0, g1 = CROSS_QUENCH
    momentum = critical_momentum(g0, g1)
    critical_time = first_critical_time(g0, g1)
    check("[E] e1: cross-critical quench has a real critical momentum", momentum is not None)
    check("[E] e2: cross-critical quench has a first critical time", critical_time is not None)

    assert momentum is not None
    assert critical_time is not None
    phi_star = (
        bogoliubov_angle(momentum, g0)
        - bogoliubov_angle(momentum, g1)
    )
    check(
        "[E] e3: critical mode is maximally mixed",
        math.isclose(math.sin(2.0 * phi_star) ** 2, 1.0, abs_tol=1e-12),
    )
    check(
        "[E] e4: critical-mode probability vanishes at first Fisher time",
        math.isclose(
            mode_probability_closed(momentum, g0, g1, critical_time),
            0.0,
            abs_tol=1e-12,
        ),
    )

    for size in (16, 32, 64):
        for time in (0.0, 0.37, 1.11, critical_time, 3.7):
            direct = return_probability_fixed_h(size, g0, g1, time)
            closed = return_probability_closed(size, g0, g1, time)
            check(
                f"[E] e5: N={size}, t={time:.6f}: fixed-H and closed products agree",
                math.isclose(direct, closed, rel_tol=2e-12, abs_tol=2e-14),
            )

    size = 16384
    window = 0.02
    center = rate_function(size, g0, g1, critical_time)
    left_slope = (
        center - rate_function(size, g0, g1, critical_time - window)
    ) / window
    right_slope = (
        rate_function(size, g0, g1, critical_time + window) - center
    ) / window
    check(
        "[E] e6: large-finite rate proxy separates left and right slopes",
        left_slope - right_slope > 0.15,
    )

    same_g0, same_g1 = SAME_PHASE_QUENCH
    check(
        "[E] e7: same-phase control has no source critical momentum",
        critical_momentum(same_g0, same_g1) is None,
    )
    check(
        "[E] e8: same-phase control never reaches a maximally mixed mode",
        max_mixing_weight(same_g0, same_g1) < 0.5,
    )

    assessment = json.loads(ASSESSMENT.read_text(encoding="utf-8"))
    diagnosis = td.evaluate_assessment(assessment)
    branch = diagnosis["branch_results"][0]
    check("[E] e9: Transition Diagnosis record is valid", diagnosis["valid"] is True)
    check(
        "[E] e10: diagnosis is fixed-family dynamics plus record formation",
        branch["components"]
        == ["FIXED_FAMILY_DYNAMICS", "RECORD_FORMATION"],
    )
    check("[E] e11: diagnosis is label invariant", diagnosis["label_invariance"]["invariant"] is True)
    check(
        "[E] e12: capability overclaim is rejected",
        "CAPABILITY_ENLARGEMENT" in branch["rejected_declared_claims"],
    )
    check(
        "[E] e13: finality overclaim is rejected",
        "FINALITY_CANDIDATE" in branch["rejected_declared_claims"],
    )

    check(
        "[F] e12-fail: rate cusp implies capability enlargement",
        "CAPABILITY_ENLARGEMENT" in branch["components"],
        expected=False,
    )
    check(
        "[F] e5-fail: positive-real Wick-rotation limit defeats full spectral reconstruction",
        not math.isclose(
            return_probability_fixed_h(64, g0, g1, critical_time),
            return_probability_closed(64, g0, g1, critical_time),
            rel_tol=2e-12,
            abs_tol=2e-14,
        ),
        expected=False,
    )
    check(
        "[F] e5-fail: finite-size evolution lacks a fixed generator",
        not all(
            math.isclose(
                abs(mode_amplitude_fixed_h(k, g0, g1, critical_time)) ** 2,
                mode_probability_closed(k, g0, g1, critical_time),
                rel_tol=2e-12,
                abs_tol=2e-14,
            )
            for k in positive_momenta(64)
        ),
        expected=False,
    )
    check(
        "[F] e12-fail: quench parameter change supplies normalized task growth",
        assessment["branches"][0]["witness"]["normalized_task_set_relation"]["value"]
        != "EQUAL",
        expected=False,
    )
    check(
        "[F] e13-fail: nonanalyticity alone establishes finality",
        "FINALITY_CANDIDATE" in branch["components"],
        expected=False,
    )

    failures = [
        name
        for name, actual, expected in checks
        if actual is not expected
    ]
    for name, actual, expected in checks:
        status = "PASS" if actual is expected else "FAIL"
        print(f"{status}: {name}")

    evidential = sum(1 for name, *_rest in checks if name.startswith("[E]"))
    falsifying = sum(1 for name, *_rest in checks if name.startswith("[F]"))
    print(
        f"headline: {evidential} [E] + {falsifying} [F] = "
        f"{evidential + falsifying}"
    )
    if failures:
        print("failed checks:")
        for name in failures:
            print(f"- {name}")
        return 1
    print("verdict: THIN_SHADOW_RECONSTRUCTION_KILL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
