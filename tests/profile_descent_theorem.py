"""Finite proof fixture for P2C-DESCENT-001.

This checks elementary quotient/factorization claims on the frozen
P2C-XFRAME-001 calibration class.  The mathematics is conditional on the
declared finite profiles, equivalence certificates, and classifiers.  It is
not a physics theorem or a universal hierarchy result.
"""

from __future__ import annotations

import itertools
import json
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Iterable

import cross_frame_descent_or_fork as xframe


CHECKS = {
    "setup: theorem target was frozen before the proof fixture": {"tag": "T"},
    "import: executed cross-frame outcome and calibration matrix are unchanged": {"tag": "E"},
    "descent-a: primitive profile is constant on certified equivalence classes": {"tag": "T"},
    "descent-b: every frame verdict factors through the descended profile": {"tag": "T"},
    "joint-carrier: signature quotient is the coarsest carrier retaining every frame output": {"tag": "T"},
    "no-go: no faithful common top label commutes on access and mechanism witnesses": {"tag": "T"},
    "refinement: primitive facts and R subtypes retain the access-mechanism distinction": {"tag": "T"},
    "index: one-context whole-family case is a material profile fork": {"tag": "T"},
    "augmented: bisimulation preservation choice retains the N-R construction question": {"tag": "T"},
    "profile-fail: changing a primitive under alleged relabel breaks descent": {
        "tag": "F",
        "protects": "descent-a: primitive profile is constant on certified equivalence classes",
    },
    "classifier-fail: representation-sensitive scoring breaks verdict descent": {
        "tag": "F",
        "protects": "descent-b: every frame verdict factors through the descended profile",
    },
    "smuggling-fail: desired-verdict primitive is accepted": {
        "tag": "F",
        "protects": "joint-carrier: signature quotient is the coarsest carrier retaining every frame output",
    },
    "distinction-fail: collapsing N access and capability removes the obstruction": {
        "tag": "F",
        "protects": "no-go: no faithful common top label commutes on access and mechanism witnesses",
    },
    "fork-fail: forcing paired and one-context cases gives a well-defined profile quotient": {
        "tag": "F",
        "protects": "index: one-context whole-family case is a material profile fork",
    },
}


@dataclass(frozen=True)
class AugmentedView:
    kernel: str
    observation: str
    controls: tuple[str, ...]
    verifier: str


def root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(*parts: str) -> dict:
    return json.loads(root().joinpath(*parts).read_text(encoding="utf-8"))


def profile_key(profile: xframe.PrimitiveProfile) -> tuple[bool, ...]:
    return tuple(asdict(profile).values())


def signature(profile: xframe.PrimitiveProfile) -> tuple[str, str, str]:
    read = xframe.frame_read(profile)
    return (read.n, read.r, read.w)


def set_partitions(items: tuple[str, ...]) -> Iterable[tuple[frozenset[str], ...]]:
    """Enumerate every set partition of a small tuple, canonically."""
    if not items:
        yield ()
        return
    head, *tail = items
    for partition in set_partitions(tuple(tail)):
        yield (frozenset((head,)), *partition)
        for index in range(len(partition)):
            merged = list(partition)
            merged[index] = frozenset((*merged[index], head))
            # Sort blocks by their least member to remove insertion duplicates.
            yield tuple(sorted(merged, key=lambda block: min(block)))


def canonical_partitions(items: tuple[str, ...]) -> tuple[tuple[frozenset[str], ...], ...]:
    seen: set[tuple[tuple[str, ...], ...]] = set()
    result = []
    for partition in set_partitions(items):
        key = tuple(sorted((tuple(sorted(block)) for block in partition)))
        if key not in seen:
            seen.add(key)
            result.append(tuple(frozenset(block) for block in key))
    return tuple(result)


def partition_retains_outputs(
    partition: tuple[frozenset[str], ...],
    signatures: dict[str, tuple[str, str, str]],
) -> bool:
    return all(len({signatures[item] for item in block}) == 1 for block in partition)


def top_n(label: str) -> str:
    if label == "ACCESS_CHANGE":
        return "ACCESS"
    if label.startswith("CAPABILITY_CHANGE"):
        return "CAPABILITY"
    return label


def top_r(label: str) -> str:
    if label.startswith("CAPABILITY_CHANGE"):
        return "CAPABILITY"
    return label


def commuting_assignments(require_n_distinction: bool) -> tuple[tuple[int, int, int], ...]:
    """All u_N(A), u_N(C), u_R(C) assignments into a three-token codomain."""
    solutions = []
    for u_n_access, u_n_capability, u_r_capability in itertools.product(range(3), repeat=3):
        commutes_access = u_n_access == u_r_capability
        commutes_capability = u_n_capability == u_r_capability
        faithful_n = u_n_access != u_n_capability
        if commutes_access and commutes_capability and (
            faithful_n or not require_n_distinction
        ):
            solutions.append((u_n_access, u_n_capability, u_r_capability))
    return tuple(solutions)


def main() -> None:
    target = root().joinpath(
        "explorations", "2026-07-19-profile-descent-theorem", "THEOREM-TARGET.md"
    ).read_text(encoding="utf-8")
    exp = load_json(
        "explorations",
        "2026-07-19-cross-frame-descent-or-fork",
        "P2C-XFRAME-001.expectations.json",
    )
    result = load_json(
        "explorations",
        "2026-07-19-cross-frame-descent-or-fork",
        "P2C-XFRAME-001.results.json",
    )
    cases = xframe.calibration_profiles(exp)

    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    check(
        "setup: theorem target was frozen before the proof fixture",
        "status: conjecture_frozen_before_fixture" in target
        and "theorem_id: P2C-DESCENT-001" in target
        and result["preregistration_commit"] == "3d297f9",
    )
    expected_matrix = {
        case_id: asdict(xframe.frame_read(profile))
        for case_id, profile in cases.items()
    }
    check(
        "import: executed cross-frame outcome and calibration matrix are unchanged",
        result["status"] == "EXECUTED"
        and result["outcome"] == "INDEXED_CONSTRUCTION_FORK"
        and all(
            result["frame_reads"][case_id]
            == {
                "N_TWO_CONTEXT_NORMALIZED": reads["n"],
                "R_ACCESS_CONSTITUTIVE": reads["r"],
                "W_ONE_CONTEXT_WHOLE_FAMILY": reads["w"],
            }
            for case_id, reads in expected_matrix.items()
        ),
    )

    operational = cases["P2C_W1_OPERATIONAL"]
    relabel = cases["REPRESENTATION_RELABEL_CONTROL"]
    equivalence_classes = (
        ("P2C_W1_OPERATIONAL", "REPRESENTATION_RELABEL_CONTROL"),
        ("IDENTITY_CONTROL",),
        ("ACCESS_ONLY_CONTROL",),
        ("RESOURCE_ONLY_CONTROL",),
        ("P2C_W1_ONE_CONTEXT",),
    )
    check(
        "descent-a: primitive profile is constant on certified equivalence classes",
        all(len({profile_key(cases[item]) for item in eq_class}) == 1 for eq_class in equivalence_classes),
    )
    check(
        "descent-b: every frame verdict factors through the descended profile",
        all(len({signature(cases[item]) for item in eq_class}) == 1 for eq_class in equivalence_classes),
    )

    # The signature kernel is the finite J=P/~_Lambda quotient.  Enumerating
    # all 203 partitions of the six calibration presentations verifies both
    # that J retains every frame output and that no valid partition has fewer
    # blocks.
    item_ids = tuple(cases)
    signatures = {case_id: signature(cases[case_id]) for case_id in item_ids}
    partitions = canonical_partitions(item_ids)
    valid = tuple(p for p in partitions if partition_retains_outputs(p, signatures))
    signature_class_count = len(set(signatures.values()))
    check(
        "joint-carrier: signature quotient is the coarsest carrier retaining every frame output",
        len(partitions) == 203
        and valid
        and min(len(partition) for partition in valid) == signature_class_count
        and signature_class_count == 5,
    )

    access = cases["ACCESS_ONLY_CONTROL"]
    check(
        "no-go: no faithful common top label commutes on access and mechanism witnesses",
        top_n(xframe.classify_n(access)) == "ACCESS"
        and top_r(xframe.classify_r(access)) == "CAPABILITY"
        and top_n(xframe.classify_n(operational)) == "CAPABILITY"
        and top_r(xframe.classify_r(operational)) == "CAPABILITY"
        and not commuting_assignments(require_n_distinction=True),
    )
    check(
        "refinement: primitive facts and R subtypes retain the access-mechanism distinction",
        profile_key(access) != profile_key(operational)
        and xframe.classify_r(access) == "CAPABILITY_CHANGE_CONSERVATIVE_INTERFACE_EXTENSION"
        and xframe.classify_r(operational) == "CAPABILITY_CHANGE_NONCONSERVATIVE",
    )
    whole = cases["P2C_W1_ONE_CONTEXT"]
    check(
        "index: one-context whole-family case is a material profile fork",
        operational.pair_defined
        and not whole.pair_defined
        and profile_key(operational) != profile_key(whole)
        and xframe.classify_w(whole) == "GLOBAL_CONTAINMENT_ONLY",
    )

    hidden = AugmentedView("same_kernel", "hidden_bit", ("act",), "outcome")
    revealed = AugmentedView(
        "same_kernel", "revealed_bit", ("act", "conditional_act"), "outcome_and_bit"
    )
    kernel_preserving = hidden.kernel == revealed.kernel
    observation_preserving = hidden == revealed
    check(
        "augmented: bisimulation preservation choice retains the N-R construction question",
        kernel_preserving
        and not observation_preserving
        and xframe.classify_n(access) == "ACCESS_CHANGE"
        and xframe.classify_r(access).endswith("CONSERVATIVE_INTERFACE_EXTENSION"),
    )

    changed_relabel = replace(relabel, resource_delta=True)
    check(
        "profile-fail: changing a primitive under alleged relabel breaks descent",
        profile_key(changed_relabel) == profile_key(operational),
        expected=False,
    )

    def bad_representation_classifier(representation_name: str) -> str:
        return "CAPABILITY" if representation_name == "original" else "ACCESS"

    check(
        "classifier-fail: representation-sensitive scoring breaks verdict descent",
        bad_representation_classifier("original")
        == bad_representation_classifier("renamed"),
        expected=False,
    )
    verdict_carrying = xframe.base_values()
    verdict_carrying["desired_verdict"] = "CAPABILITY"  # type: ignore[assignment]
    accepted = True
    try:
        xframe.build_profile(verdict_carrying)
    except ValueError:
        accepted = False
    check(
        "smuggling-fail: desired-verdict primitive is accepted",
        accepted,
        expected=False,
    )
    check(
        "distinction-fail: collapsing N access and capability removes the obstruction",
        not commuting_assignments(require_n_distinction=False),
        expected=False,
    )
    check(
        "fork-fail: forcing paired and one-context cases gives a well-defined profile quotient",
        profile_key(operational) == profile_key(whole),
        expected=False,
    )

    print("P2C-DESCENT-001 FINITE PROOF FIXTURE")
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
    print(f"finite presentations: {len(item_ids)}")
    print(f"enumerated partitions: {len(partitions)}")
    print(f"joint-carrier classes: {signature_class_count}")
    print(f"faithful commuting top-label assignments: {len(commuting_assignments(True))}")
    print(f"unfaithful commuting assignments after N collapse: {len(commuting_assignments(False))}")
    print("THEOREM RESULT: PROFILE_DESCENT_AND_FAITHFUL_TOP_LABEL_NON_DESCENT")
    print("AUGMENTED-DYNAMICS RESULT: COMMON_CARRIER_NOT_CANONICAL_ADJUDICATOR")
    print(f"EVIDENTIAL/TEETH HEADLINE: {counts['E']} [E] + {counts['F']} [F] = {counts['E'] + counts['F']}")
    print(f"[T] theorem-consequence checks (no evidential weight): {counts['T']}")

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All finite theorem checks match the frozen target. Exit 0.")


if __name__ == "__main__":
    main()
