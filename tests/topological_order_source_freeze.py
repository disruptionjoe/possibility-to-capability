"""Source-freeze validator for the topological-order witness.

Lane 2 reproducibility hardening for P2C-REAL-PHYSICAL-WITNESS. The validator
checks that the literature freeze names its primary anchors, maps each source
claim to a bounded P2C witness leg, preserves nonclaim firewalls, and exposes a
reader protocol. It does not validate the physics itself.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FREEZE = ROOT / "literature" / "2026-07-19-topological-order-source-freeze.md"

CHECKS = {
    "setup: source freeze file exists": {"tag": "T"},
    "sources: four primary anchors are named": {"tag": "E"},
    "sources-fail: missing arxiv anchor is detected": {
        "tag": "F",
        "protects": "sources: four primary anchors are named",
    },
    "mapping: all witness legs are source-bounded": {"tag": "E"},
    "mapping-fail: missing loop and distance legs are detected": {
        "tag": "F",
        "protects": "mapping: all witness legs are source-bounded",
    },
    "nonclaims: verdict and source-packet firewalls remain explicit": {"tag": "E"},
    "nonclaims-fail: capability overclaim is detected": {
        "tag": "F",
        "protects": "nonclaims: verdict and source-packet firewalls remain explicit",
    },
    "protocol: reader can rerun witness and freeze checks": {"tag": "E"},
    "protocol-fail: missing source-freeze test is detected": {
        "tag": "F",
        "protects": "protocol: reader can rerun witness and freeze checks",
    },
}

SOURCE_ANCHORS = (
    "arXiv:quant-ph/9707021",
    "arXiv:quant-ph/0110143",
    "arXiv:hep-th/0510092",
    "arXiv:cond-mat/0510613",
)

WITNESS_LEGS = (
    "gamma-log-D",
    "Four sectors",
    "Local indistinguishability",
    "Noncontractible loop access",
    "Distance-scaling memory",
    "Completion rivalry",
    "Neutrality",
)

NONCLAIM_FIREWALLS = (
    "No empirical material sample is established.",
    "No source packet is imported or accepted.",
    "No capability verdict is established.",
    "No finality claim is established.",
)

PROTOCOL_COMMANDS = (
    "python tests/topological_order_witness.py",
    "python tests/topological_order_source_freeze.py",
)


def contains_all(text: str, terms: tuple[str, ...]) -> bool:
    return all(term in text for term in terms)


def main() -> None:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    check("setup: source freeze file exists", FREEZE.exists())
    text = FREEZE.read_text(encoding="utf-8")

    check("sources: four primary anchors are named", contains_all(text, SOURCE_ANCHORS))
    missing_source = text.replace("arXiv:hep-th/0510092", "")
    check(
        "sources-fail: missing arxiv anchor is detected",
        contains_all(missing_source, SOURCE_ANCHORS),
        expected=False,
    )

    check("mapping: all witness legs are source-bounded", contains_all(text, WITNESS_LEGS))
    missing_mapping = text.replace("Noncontractible loop access", "").replace(
        "Distance-scaling memory", ""
    )
    check(
        "mapping-fail: missing loop and distance legs are detected",
        contains_all(missing_mapping, WITNESS_LEGS),
        expected=False,
    )

    check(
        "nonclaims: verdict and source-packet firewalls remain explicit",
        contains_all(text, NONCLAIM_FIREWALLS),
    )
    overclaim = text.replace("No capability verdict is established.", "")
    check(
        "nonclaims-fail: capability overclaim is detected",
        contains_all(overclaim, NONCLAIM_FIREWALLS),
        expected=False,
    )

    check(
        "protocol: reader can rerun witness and freeze checks",
        contains_all(text, PROTOCOL_COMMANDS),
    )
    missing_protocol = text.replace("python tests/topological_order_source_freeze.py", "")
    check(
        "protocol-fail: missing source-freeze test is detected",
        contains_all(missing_protocol, PROTOCOL_COMMANDS),
        expected=False,
    )

    print("TOPOLOGICAL ORDER SOURCE FREEZE")
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
    print(
        f"EVIDENTIAL CHECKS (headline): {counts['E']} [E] + "
        f"{counts['F']} [F] = {counts['E'] + counts['F']}"
    )
    print(f"[T] setup checks (no evidential weight): {counts['T']}")
    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()
