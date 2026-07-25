"""Exact admission preflight for the ideal four-step anomalous-Floquet drive.

The finite permutation fixture verifies the source-mapped ideal construction
and the admission firewall. It does not prove the cited papers, compute the
thermodynamic winding invariant, or establish capability or finality.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
SPECIMEN = (
    ROOT / "explorations" / "2026-07-25-anomalous-floquet-admission"
)
ADMISSION = SPECIMEN / "anomalous-floquet-admission-v0.1.json"
FORWARD_STEPS = ((1, 0), (0, 1), (-1, 0), (0, -1))

Site = tuple[str, int, int]


def sites(size: int) -> list[Site]:
    if size < 3:
        raise ValueError("size must be at least three")
    return [
        (sublattice, x, y)
        for sublattice in ("A", "B")
        for x in range(size)
        for y in range(size)
    ]


def quarter_step(
    site: Site, direction: tuple[int, int], size: int, periodic: bool
) -> Site:
    sublattice, x, y = site
    dx, dy = direction
    if sublattice == "A":
        partner = ("B", x + dx, y + dy)
    else:
        partner = ("A", x - dx, y - dy)
    if periodic:
        return (partner[0], partner[1] % size, partner[2] % size)
    if 0 <= partner[1] < size and 0 <= partner[2] < size:
        return partner
    return site


def one_period(
    site: Site,
    size: int,
    periodic: bool,
    steps: Iterable[tuple[int, int]] = FORWARD_STEPS,
) -> Site:
    result = site
    for direction in steps:
        result = quarter_step(result, direction, size, periodic)
    return result


def period_map(
    size: int,
    periodic: bool,
    steps: Iterable[tuple[int, int]] = FORWARD_STEPS,
) -> dict[Site, Site]:
    frozen_steps = tuple(steps)
    return {
        site: one_period(site, size, periodic, frozen_steps)
        for site in sites(size)
    }


def is_boundary(site: Site, size: int) -> bool:
    _, x, y = site
    return x in (0, size - 1) or y in (0, size - 1)


def inverse_map(mapping: dict[Site, Site]) -> dict[Site, Site]:
    return {destination: source for source, destination in mapping.items()}


def main() -> int:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    for size in (3, 4, 5, 7):
        periodic = period_map(size, periodic=True)
        check(
            f"[E] e1: N={size} periodic bulk propagator is identity",
            all(source == destination for source, destination in periodic.items()),
        )

        opened = period_map(size, periodic=False)
        moved = [
            source
            for source, destination in opened.items()
            if source != destination
        ]
        check(
            f"[E] e2: N={size} open propagator is bijective",
            len(set(opened.values())) == len(opened),
        )
        check(
            f"[E] e3: N={size} open boundary carries motion",
            bool(moved),
        )
        check(
            f"[E] e4: N={size} moved sources are boundary sites",
            all(is_boundary(site, size) for site in moved),
        )
        check(
            f"[E] e5: N={size} every interior site remains localized",
            all(
                opened[site] == site
                for site in sites(size)
                if not is_boundary(site, size)
            ),
        )

        reversed_drive = period_map(
            size, periodic=False, steps=reversed(FORWARD_STEPS)
        )
        check(
            f"[E] e6: N={size} reversed drive inverts edge permutation",
            reversed_drive == inverse_map(opened),
        )

    admission = json.loads(ADMISSION.read_text(encoding="utf-8"))
    required = admission["required_fields"]
    missing = {
        field
        for field, status in required.items()
        if status in {"MISSING", "PARTIAL"}
    }
    check(
        "[E] e7: missing-field list is exact",
        set(admission["missing_admission_fields"]) == missing,
    )
    check(
        "[E] e8: common control budget remains partial",
        required["common_control_budget"] == "PARTIAL",
    )
    check(
        "[E] e9: matched physical power remains missing",
        required["matched_physical_power"] == "MISSING",
    )
    check(
        "[E] e10: operational task delta remains missing",
        required["operational_before_after_task_delta"] == "MISSING",
    )
    check(
        "[E] e11: strongest completion rival is retained",
        required["strongest_completion_rival"] == "PRESENT",
    )
    check(
        "[E] e12: synthetic-dimension completion is admissible",
        any(
            fork["fork_id"] == "synthetic-dimension-static-completion"
            and fork["status"] == "ADMISSIBLE_COMPLETION"
            for fork in admission["representation_forks"]
        ),
    )
    check(
        "[E] e13: incomplete matched frame returns abstention",
        admission["verdict"] == "ABSTAIN_MATCHED_RESOURCE_AND_TASK"
        and admission["admission"] is False,
    )

    check(
        "[F] e3-fail: periodic bulk identity implies open identity",
        all(
            source == destination
            for source, destination in period_map(5, periodic=False).items()
        ),
        expected=False,
    )
    check(
        "[F] e7-fail: edge motion completes the matched-resource ledger",
        not missing,
        expected=False,
    )
    check(
        "[F] e12-fail: fixed-phase H_F=0 represents full micromotion",
        all(
            fork["status"] != "FAILS_TO_REPRESENT_FULL_OBJECT"
            for fork in admission["representation_forks"]
            if fork["fork_id"] == "fixed-phase-same-dimensional"
        ),
        expected=False,
    )
    check(
        "[F] e12-fail: no static completion is retained",
        not any(
            fork["status"] == "ADMISSIBLE_COMPLETION"
            for fork in admission["representation_forks"]
        ),
        expected=False,
    )
    check(
        "[F] e13-fail: anomalous topology alone licenses capability admission",
        admission["admission"],
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
    print("verdict: ABSTAIN_MATCHED_RESOURCE_AND_TASK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
