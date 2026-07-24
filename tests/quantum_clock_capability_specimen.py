"""Quantum-clock capability specimen for Transition Diagnosis v0.1.

The fixture checks four receiver-owned assessments against the unchanged
capability diagnostic. Source papers supply bounded evidence; this harness
tests only the repository-owned typing and overclaim firewalls.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools import capability_diagnostic as td


SPECIMEN = ROOT / "explorations" / "2026-07-24-quantum-clock-capability-specimen"
CASES = {
    "ordinary": ("ordinary-frequency-shift-v0.1.json", "MULTI_LEVEL"),
    "single_ghz": ("single-size-ghz-v0.1.json", "MULTI_LEVEL"),
    "cascade": ("cascaded-ghz-v0.1.json", "CONSTRUCTION_FORK"),
    "history": ("coherent-history-certification-v0.1.json", "CONSTRUCTION_FORK"),
}


def load_result(filename: str) -> dict[str, object]:
    assessment = json.loads((SPECIMEN / filename).read_text(encoding="utf-8"))
    return td.evaluate_assessment(assessment)


def branch(result: dict[str, object], branch_id: str) -> dict[str, object]:
    return next(
        item
        for item in result["branch_results"]  # type: ignore[union-attr]
        if item["branch_id"] == branch_id
    )


def main() -> int:
    results = {
        name: load_result(filename)
        for name, (filename, _expected) in CASES.items()
    }
    checks: list[tuple[str, str, bool, bool]] = []

    def check(tag: str, name: str, value: bool, expected: bool = True) -> None:
        checks.append((tag, name, bool(value), expected))

    for name, (_filename, expected) in CASES.items():
        result = results[name]
        check("E", f"{name}: contract valid", result["valid"] is True)
        check("E", f"{name}: aggregate {expected}", result["aggregate_outcome"] == expected)
        check(
            "E",
            f"{name}: pure label swap invariant",
            result["label_invariance"]["invariant"] is True,  # type: ignore[index]
        )

    ordinary = branch(results["ordinary"], "ordinary-shift-record")
    check(
        "E",
        "ordinary: dynamics and record components preserved",
        ordinary["components"] == ["FIXED_FAMILY_DYNAMICS", "RECORD_FORMATION"],
    )
    check(
        "F",
        "ordinary-fail: frequency shift alone grants capability",
        "CAPABILITY_ENLARGEMENT" in ordinary["components"],  # type: ignore[operator]
        expected=False,
    )

    single = branch(results["single_ghz"], "single-size-ghz-operational")
    check(
        "E",
        "single-GHZ: capability overclaim rejected",
        "CAPABILITY_ENLARGEMENT" in single["rejected_declared_claims"],  # type: ignore[operator]
    )
    check(
        "E",
        "single-GHZ: raw-versus-normalized alert fires",
        "Raw task access changed, but normalized capability did not." in single["alerts"],  # type: ignore[operator]
    )
    check(
        "F",
        "single-GHZ-fail: short-time precision alone grants normalized capability",
        "CAPABILITY_ENLARGEMENT" in single["components"],  # type: ignore[operator]
        expected=False,
    )

    cascade = results["cascade"]
    check(
        "E",
        "cascade: whole-instrument and strict-budget outcomes remain split",
        {
            item["outcome"]
            for item in cascade["branch_results"]  # type: ignore[union-attr]
        }
        == {"MULTI_LEVEL", "INCOMPARABLE"},
    )

    history = results["history"]
    access_fixed = branch(history, "access-fixed-clock-frame")
    check(
        "E",
        "history: complete-protocol and access-fixed outcomes remain split",
        {
            item["outcome"]
            for item in history["branch_results"]  # type: ignore[union-attr]
        }
        == {"MULTI_LEVEL", "ACCESS_CHANGE"},
    )
    check(
        "E",
        "history: access-fixed capability overclaim rejected",
        "CAPABILITY_ENLARGEMENT" in access_fixed["rejected_declared_claims"],  # type: ignore[operator]
    )
    check(
        "F",
        "history-fail: new coherent control counts as intrinsic clock capability",
        "CAPABILITY_ENLARGEMENT" in access_fixed["components"],  # type: ignore[operator]
        expected=False,
    )

    failures = [
        name
        for _tag, name, actual, expected in checks
        if actual is not expected
    ]
    for tag, name, actual, expected in checks:
        status = "PASS" if actual is expected else "FAIL"
        print(f"[{tag}] {status}: {name}")

    evidential = sum(1 for tag, *_rest in checks if tag == "E")
    falsifying = sum(1 for tag, *_rest in checks if tag == "F")
    print(
        f"headline: {evidential} [E] + {falsifying} [F] = "
        f"{evidential + falsifying}"
    )
    if failures:
        print("failed checks:")
        for name in failures:
            print(f"- {name}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
