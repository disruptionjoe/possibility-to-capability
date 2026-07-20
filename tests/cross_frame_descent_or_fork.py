"""Preregistered cross-frame descent-or-fork trial P2C-XFRAME-001.

This receiver-owned finite fixture transports the unchanged P2C-W1 evidence
profile through three explicitly nonequivalent constructions.  It tests
representation invariance and construction descent separately.  It does not
adjudicate source truth, establish a physical capability, equate the frames,
or reach finality.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Any


CHECKS = {
    "setup: preregistration and primitive schema are frozen": {"tag": "T"},
    "evidence: unchanged P2C-W1 manifest bytes match the frozen identity": {"tag": "E"},
    "sovereignty: imported source packet identities and no-transfer flags survive": {"tag": "E"},
    "p1: operational witness is capability-shaped in N and nonconservative in R": {"tag": "E"},
    "p2: access-only control has one profile and construction-indexed top labels": {"tag": "E"},
    "p3: one-context whole-family construction reports containment, not operation": {"tag": "E"},
    "p4: certified representation relabel preserves profile and frame outputs": {"tag": "E"},
    "p5: common primitive refinement survives while one English label does not descend": {"tag": "E"},
    "adversary: identity, resource, and missing-interface controls are not laundered": {"tag": "E"},
    "outcome: frozen decision rule selects indexed construction fork": {"tag": "E"},
    "pair-fail: flipping pair existence changes operational adjudicability": {
        "tag": "F",
        "protects": "p1: operational witness is capability-shaped in N and nonconservative in R",
    },
    "interface-fail: flipping interface delta changes the common primitive profile": {
        "tag": "F",
        "protects": "p5: common primitive refinement survives while one English label does not descend",
    },
    "resource-fail: flipping resource delta blocks capability classification": {
        "tag": "F",
        "protects": "adversary: identity, resource, and missing-interface controls are not laundered",
    },
    "mechanism-fail: removing the common-interface task delta defeats N capability": {
        "tag": "F",
        "protects": "p1: operational witness is capability-shaped in N and nonconservative in R",
    },
    "conservative-fail: flipping extension type changes the R subtype": {
        "tag": "F",
        "protects": "p2: access-only control has one profile and construction-indexed top labels",
    },
    "containment-fail: removing family containment changes the W result": {
        "tag": "F",
        "protects": "p3: one-context whole-family construction reports containment, not operation",
    },
    "verdict-input-fail: desired-verdict metadata is rejected before classification": {
        "tag": "F",
        "protects": "outcome: frozen decision rule selects indexed construction fork",
    },
}


@dataclass(frozen=True)
class PrimitiveProfile:
    pair_defined: bool
    source_evidence_same: bool
    representation_equivalent: bool
    common_task_vocabulary: bool
    common_interface_available: bool
    interface_delta: bool
    resource_delta: bool
    mechanism_task_delta_under_common_interface: bool
    verified_task_delta_under_native_interface: bool
    conservative_extension: bool
    target_contained_in_declared_family: bool
    persistence_capped: bool


@dataclass(frozen=True)
class FrameRead:
    n: str
    r: str
    w: str


def root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(*parts: str) -> dict[str, Any]:
    return json.loads(root().joinpath(*parts).read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def profile_fields() -> tuple[str, ...]:
    return tuple(PrimitiveProfile.__dataclass_fields__)


def build_profile(values: dict[str, Any]) -> PrimitiveProfile:
    expected = set(profile_fields())
    supplied = set(values)
    unknown = supplied - expected
    missing = expected - supplied
    if unknown:
        raise ValueError(f"forbidden or unknown primitive fields: {sorted(unknown)}")
    if missing:
        raise ValueError(f"missing primitive fields: {sorted(missing)}")
    if not all(isinstance(values[field], bool) for field in expected):
        raise TypeError("every primitive field must be boolean")
    return PrimitiveProfile(**values)


def base_values() -> dict[str, bool]:
    return {
        "pair_defined": True,
        "source_evidence_same": True,
        "representation_equivalent": True,
        "common_task_vocabulary": True,
        "common_interface_available": True,
        "interface_delta": False,
        "resource_delta": False,
        "mechanism_task_delta_under_common_interface": False,
        "verified_task_delta_under_native_interface": False,
        "conservative_extension": False,
        "target_contained_in_declared_family": False,
        "persistence_capped": True,
    }


def calibration_profiles(expectations: dict[str, Any]) -> dict[str, PrimitiveProfile]:
    cases: dict[str, PrimitiveProfile] = {}
    for case in expectations["calibration_cases"]:
        # The relabel entry is a partial overlay on the operational witness,
        # as frozen by P4; generic controls are partial overlays on the neutral
        # baseline.  This prevents an omitted, unchanged fact (notably family
        # containment) from being silently altered by representation transport.
        if case["id"] == "REPRESENTATION_RELABEL_CONTROL":
            values = asdict(cases["P2C_W1_OPERATIONAL"])
        else:
            values = base_values()
        values.update(case["expected_primitive"])
        cases[case["id"]] = build_profile(values)
    return cases


def classify_n(p: PrimitiveProfile) -> str:
    if not p.pair_defined:
        return "NOT_ADJUDICABLE_NO_PAIR"
    if p.resource_delta:
        return "RESOURCE_FRAME_CHANGED"
    if not p.common_task_vocabulary or not p.common_interface_available:
        return "INDETERMINATE_NO_COMMON_SEMANTICS"
    if p.mechanism_task_delta_under_common_interface:
        return "CAPABILITY_CHANGE_NONCONSERVATIVE"
    if p.interface_delta:
        return "ACCESS_CHANGE"
    return "NO_TYPED_CHANGE"


def classify_r(p: PrimitiveProfile) -> str:
    if not p.pair_defined:
        return "NOT_ADJUDICABLE_NO_PAIR"
    if p.resource_delta:
        return "RESOURCE_FRAME_CHANGED"
    if not p.common_task_vocabulary or not p.common_interface_available:
        return "ILL_FORMED_NO_COMMON_INTERFACE"
    if p.verified_task_delta_under_native_interface:
        subtype = "CONSERVATIVE_INTERFACE_EXTENSION" if p.conservative_extension else "NONCONSERVATIVE"
        return f"CAPABILITY_CHANGE_{subtype}"
    return "NO_TYPED_CHANGE"


def classify_w(p: PrimitiveProfile) -> str:
    if p.target_contained_in_declared_family:
        return "GLOBAL_CONTAINMENT_ONLY"
    return "NOT_CONTAINED"


def frame_read(p: PrimitiveProfile) -> FrameRead:
    return FrameRead(classify_n(p), classify_r(p), classify_w(p))


def decide_outcome(cases: dict[str, PrimitiveProfile]) -> str:
    operational = cases["P2C_W1_OPERATIONAL"]
    relabel = cases["REPRESENTATION_RELABEL_CONTROL"]
    access = cases["ACCESS_ONLY_CONTROL"]
    whole = cases["P2C_W1_ONE_CONTEXT"]

    if not operational.source_evidence_same:
        return "BLOCKED"
    if not operational.common_task_vocabulary or not operational.common_interface_available:
        return "INDETERMINATE_NO_COMMON_SEMANTICS"
    if asdict(operational) != asdict(relabel) or frame_read(operational) != frame_read(relabel):
        return "F5_EQUIVALENCE_FAILURE"
    if not operational.mechanism_task_delta_under_common_interface:
        return "CAPABILITY_COLLAPSE_SCOPED"

    p2c_read = frame_read(operational)
    access_read = frame_read(access)
    whole_read = frame_read(whole)
    common_refinement_survives = (
        access.interface_delta
        and not access.mechanism_task_delta_under_common_interface
        and access.verified_task_delta_under_native_interface
        and access.conservative_extension
    )
    material_fork_retained = (
        not whole.pair_defined and whole_read.w == "GLOBAL_CONTAINMENT_ONLY"
    )
    labels_do_not_descend = access_read.n == "ACCESS_CHANGE" and access_read.r.startswith(
        "CAPABILITY_CHANGE_"
    )
    operational_agreement = p2c_read.n.startswith("CAPABILITY_CHANGE_") and p2c_read.r == (
        "CAPABILITY_CHANGE_NONCONSERVATIVE"
    )
    if common_refinement_survives and material_fork_retained and labels_do_not_descend:
        return "INDEXED_CONSTRUCTION_FORK"
    if common_refinement_survives and material_fork_retained and operational_agreement:
        return "INVARIANT_DESCENT_SCOPED"
    return "BLOCKED"


def evidence_identity(expectations: dict[str, Any], witness: dict[str, Any]) -> bool:
    identity = expectations["evidence_identity"]
    bundle = root() / "exports" / "witness" / "P2C-W1-superconducting-ring-v0.1"
    actual = []
    for entry in witness["integrity"]["manifest"]:
        path = bundle / entry["path"]
        digest = sha256(path)
        if digest != entry["content_sha256"] or path.stat().st_size != entry["byte_length"]:
            return False
        actual.append(digest)
    return (
        witness["witness_id"] == identity["witness_id"]
        and witness["source"]["content_revision"] == identity["witness_content_revision"]
        and actual == identity["witness_manifest_sha256"]
    )


def main() -> None:
    exp = load_json(
        "explorations",
        "2026-07-19-cross-frame-descent-or-fork",
        "P2C-XFRAME-001.expectations.json",
    )
    witness = load_json("exports", "witness", "P2C-W1-superconducting-ring-v0.1", "witness.json")
    taf = load_json("packets", "imports", "TAF-002", "packet.json")
    ti = load_json("packets", "imports", "TI-WFA-001", "packet.json")
    cases = calibration_profiles(exp)
    forbidden = set(exp["primitive_profile"]["forbidden_fields"])

    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    check(
        "setup: preregistration and primitive schema are frozen",
        exp["schema_version"] == "p2c-cross-frame-prereg-v0.1"
        and exp["experiment_id"] == "P2C-XFRAME-001"
        and exp["status"] == "EXPECTATIONS_FROZEN_BEFORE_EXECUTION"
        and tuple(exp["primitive_profile"]["fields"]) == profile_fields()
        and forbidden == {"desired_verdict", "capability_label", "frame_winner", "finality_label"},
    )
    check(
        "evidence: unchanged P2C-W1 manifest bytes match the frozen identity",
        evidence_identity(exp, witness),
    )
    identity = exp["evidence_identity"]
    check(
        "sovereignty: imported source packet identities and no-transfer flags survive",
        taf["packet_id"] == identity["taf_packet_id"]
        and taf["source"]["revision"] == identity["taf_source_revision"]
        and ti["packet_id"] == identity["ti_packet_id"]
        and ti["source"]["revision"] == identity["ti_source_revision"]
        and not taf["ownership"]["authority_transfer"]
        and not ti["ownership"]["authority_transfer"],
    )

    operational = cases["P2C_W1_OPERATIONAL"]
    access = cases["ACCESS_ONLY_CONTROL"]
    whole = cases["P2C_W1_ONE_CONTEXT"]
    relabel = cases["REPRESENTATION_RELABEL_CONTROL"]
    check(
        "p1: operational witness is capability-shaped in N and nonconservative in R",
        classify_n(operational) == "CAPABILITY_CHANGE_NONCONSERVATIVE"
        and classify_r(operational) == "CAPABILITY_CHANGE_NONCONSERVATIVE"
        and operational.persistence_capped,
    )
    check(
        "p2: access-only control has one profile and construction-indexed top labels",
        classify_n(access) == "ACCESS_CHANGE"
        and classify_r(access) == "CAPABILITY_CHANGE_CONSERVATIVE_INTERFACE_EXTENSION"
        and access.interface_delta
        and not access.mechanism_task_delta_under_common_interface,
    )
    check(
        "p3: one-context whole-family construction reports containment, not operation",
        classify_n(whole) == "NOT_ADJUDICABLE_NO_PAIR"
        and classify_r(whole) == "NOT_ADJUDICABLE_NO_PAIR"
        and classify_w(whole) == "GLOBAL_CONTAINMENT_ONLY",
    )
    check(
        "p4: certified representation relabel preserves profile and frame outputs",
        relabel.representation_equivalent
        and asdict(relabel) == asdict(operational)
        and frame_read(relabel) == frame_read(operational),
    )
    common_refinement = asdict(access)
    check(
        "p5: common primitive refinement survives while one English label does not descend",
        set(common_refinement) == set(profile_fields())
        and not forbidden.intersection(common_refinement)
        and classify_n(access) != classify_r(access),
    )

    identity_control = cases["IDENTITY_CONTROL"]
    resource = cases["RESOURCE_ONLY_CONTROL"]
    missing_values = base_values()
    missing_values["common_interface_available"] = False
    missing_interface = build_profile(missing_values)
    check(
        "adversary: identity, resource, and missing-interface controls are not laundered",
        frame_read(identity_control).n == "NO_TYPED_CHANGE"
        and frame_read(identity_control).r == "NO_TYPED_CHANGE"
        and classify_n(resource) == "RESOURCE_FRAME_CHANGED"
        and classify_r(resource) == "RESOURCE_FRAME_CHANGED"
        and classify_n(missing_interface) == "INDETERMINATE_NO_COMMON_SEMANTICS"
        and classify_r(missing_interface) == "ILL_FORMED_NO_COMMON_INTERFACE",
    )
    outcome = decide_outcome(cases)
    check(
        "outcome: frozen decision rule selects indexed construction fork",
        outcome == "INDEXED_CONSTRUCTION_FORK",
    )

    check(
        "pair-fail: flipping pair existence changes operational adjudicability",
        frame_read(replace(operational, pair_defined=False)) == frame_read(operational),
        expected=False,
    )
    check(
        "interface-fail: flipping interface delta changes the common primitive profile",
        asdict(replace(operational, interface_delta=True)) == asdict(operational),
        expected=False,
    )
    check(
        "resource-fail: flipping resource delta blocks capability classification",
        classify_n(replace(operational, resource_delta=True))
        == classify_n(operational),
        expected=False,
    )
    check(
        "mechanism-fail: removing the common-interface task delta defeats N capability",
        classify_n(replace(operational, mechanism_task_delta_under_common_interface=False))
        == classify_n(operational),
        expected=False,
    )
    check(
        "conservative-fail: flipping extension type changes the R subtype",
        classify_r(replace(access, conservative_extension=False)) == classify_r(access),
        expected=False,
    )
    check(
        "containment-fail: removing family containment changes the W result",
        classify_w(replace(whole, target_contained_in_declared_family=False))
        == classify_w(whole),
        expected=False,
    )
    verdict_carrying = base_values()
    verdict_carrying["desired_verdict"] = "CAPABILITY_CHANGE"  # type: ignore[assignment]
    rejected = False
    try:
        build_profile(verdict_carrying)
    except ValueError:
        rejected = True
    check(
        "verdict-input-fail: desired-verdict metadata is rejected before classification",
        not rejected,
        expected=False,
    )

    print("P2C-XFRAME-001 CROSS-FRAME DESCENT-OR-FORK TRIAL")
    print("=" * 76)
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
    for case_id in (
        "IDENTITY_CONTROL",
        "ACCESS_ONLY_CONTROL",
        "RESOURCE_ONLY_CONTROL",
        "P2C_W1_OPERATIONAL",
        "P2C_W1_ONE_CONTEXT",
        "REPRESENTATION_RELABEL_CONTROL",
    ):
        read = frame_read(cases[case_id])
        print(f"{case_id:>30}: N={read.n}; R={read.r}; W={read.w}")
    print()
    print(f"OUTCOME: {outcome}")
    print("CEILING: finite receiver-owned transport over frozen stipulated facts; finality not reached")
    print(f"EVIDENTIAL CHECKS (headline): {counts['E']} [E] + {counts['F']} [F] = {counts['E'] + counts['F']}")
    print(f"[T] theorem-consequence checks (no evidential weight): {counts['T']}")

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All checks match preregistered expectations. Exit 0.")


if __name__ == "__main__":
    main()
