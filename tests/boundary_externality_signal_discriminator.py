"""Carrier-neutral discriminator for boundary outside/signal candidates.

This fixture implements the P2C-BOUNDARY-EXTERNALITY-DISCRIMINATOR swing at
exploration tier. It does not establish an outside universe, a source-repo
verdict, a GU firewall, or a public claim. Its only job is to make boundary
candidate classes fail differently before any future packet combination can
use "outside" or "signal" language.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
import json


CHECKS = {
    "setup: preserved intake classes are represented": {"tag": "T"},
    "setup: every candidate declares an observable null distinction": {"tag": "T"},
    "carrier neutrality: carrier labels do not change typed verdicts": {"tag": "E"},
    "condition: fixed boundary datum is not a delivered signal": {"tag": "E"},
    "completion: static global datum is absorbed as fixed-family completion": {"tag": "E"},
    "fixed point: two-ended condition remains finality-abstain": {"tag": "E"},
    "access: epistemic observer readout maps to access change only": {"tag": "E"},
    "resource: physical intervention changes resource frame before capability": {"tag": "E"},
    "feedback: autonomous closure without task delta is maintenance not capability": {"tag": "E"},
    "edge: membrane or anomaly-flow candidate stays underdefined without task delta": {"tag": "E"},
    "reservoir: enlarged-system reservoir is resource change not matched capability": {"tag": "E"},
    "stochastic: noise environment abstains unless timing and record are pinned": {"tag": "E"},
    "source sovereignty: native current waits for frozen source packet": {"tag": "E"},
    "after-fact: ensemble selection is outcome encoding not a delivered signal": {"tag": "E"},
    "positive calibration: closed matched task delta can reach capability candidate": {"tag": "E"},
    "condition-fail: bad classifier calls a fixed condition a signal": {
        "tag": "F",
        "protects": "condition: fixed boundary datum is not a delivered signal",
    },
    "completion-fail: bad classifier ignores fixed-family absorption": {
        "tag": "F",
        "protects": "completion: static global datum is absorbed as fixed-family completion",
    },
    "resource-fail: bad classifier ignores resource-frame mismatch": {
        "tag": "F",
        "protects": "resource: physical intervention changes resource frame before capability",
    },
    "after-fact-fail: bad classifier treats outcome encoding as signal": {
        "tag": "F",
        "protects": "after-fact: ensemble selection is outcome encoding not a delivered signal",
    },
    "source-fail: bad classifier imports a native source-current claim": {
        "tag": "F",
        "protects": "source sovereignty: native current waits for frozen source packet",
    },
}


LEVELS = frozenset({
    "possibility",
    "dynamics",
    "records",
    "access",
    "resources",
    "capability",
    "finality",
})


@dataclass(frozen=True)
class BoundaryCandidate:
    candidate_id: str
    carrier: str
    interface: str
    relation: str
    transfer: tuple[str, ...]
    timing: str
    closure: str
    matched_resource_frame: bool
    matched_access_frame: bool
    matched_task_delta: bool
    completion_absorbed: bool
    after_fact_encoding: bool
    source_packet_required: bool
    initiates: bool
    maintains: bool
    null_distinction: str


@dataclass(frozen=True)
class DiscriminatorReport:
    candidate_id: str
    carrier: str
    signal_status: str
    frame_status: str
    closure_status: str
    completion_status: str
    hierarchy_levels: tuple[str, ...]
    verdict: str
    null_distinction: str


def has_transfer(candidate: BoundaryCandidate) -> bool:
    return bool(set(candidate.transfer) - {"none"})


def frame_status(candidate: BoundaryCandidate) -> str:
    if not candidate.matched_resource_frame:
        return "RESOURCE_FRAME_CHANGED"
    if not candidate.matched_access_frame:
        return "ACCESS_FRAME_CHANGED"
    return "MATCHED_RESOURCE_AND_ACCESS_FRAME"


def report(
    candidate: BoundaryCandidate,
    *,
    signal_status: str,
    hierarchy_levels: tuple[str, ...],
    verdict: str,
    completion_status: str = "NOT_ABSORBED",
) -> DiscriminatorReport:
    unknown_levels = set(hierarchy_levels) - LEVELS
    if unknown_levels:
        raise ValueError(f"unknown hierarchy levels: {sorted(unknown_levels)}")
    return DiscriminatorReport(
        candidate_id=candidate.candidate_id,
        carrier=candidate.carrier,
        signal_status=signal_status,
        frame_status=frame_status(candidate),
        closure_status=candidate.closure,
        completion_status=completion_status,
        hierarchy_levels=hierarchy_levels,
        verdict=verdict,
        null_distinction=candidate.null_distinction,
    )


def classify_candidate(candidate: BoundaryCandidate) -> DiscriminatorReport:
    """Classify a boundary candidate without inspecting carrier-specific truth."""

    if candidate.source_packet_required:
        return report(
            candidate,
            signal_status="SOURCE_PACKET_REQUIRED",
            hierarchy_levels=(),
            verdict="ABSTAIN_SOURCE_SOVEREIGNTY",
            completion_status="NOT_EVALUATED",
        )

    if candidate.after_fact_encoding or candidate.timing == "after_fact":
        return report(
            candidate,
            signal_status="AFTER_FACT_OUTCOME_ENCODING",
            hierarchy_levels=("records",),
            verdict="NOT_A_DELIVERED_SIGNAL",
            completion_status="HISTORY_SELECTION_OR_ENCODING",
        )

    if candidate.completion_absorbed and not candidate.matched_task_delta:
        return report(
            candidate,
            signal_status="CONDITION_ONLY",
            hierarchy_levels=("possibility", "dynamics"),
            verdict="FIXED_FAMILY_COMPLETION",
            completion_status="ABSORBED",
        )

    if candidate.relation == "condition":
        levels = ("possibility",)
        if candidate.maintains:
            levels = ("possibility", "dynamics")
        verdict = "INITIATION_CONDITION_NOT_SIGNAL" if candidate.initiates else "BOUNDARY_CONDITION_NOT_SIGNAL"
        return report(
            candidate,
            signal_status="CONDITION_ONLY",
            hierarchy_levels=levels,
            verdict=verdict,
        )

    if candidate.relation == "fixed_point":
        return report(
            candidate,
            signal_status="NON_TEMPORAL_FIXED_POINT",
            hierarchy_levels=("finality",),
            verdict="ABSTAIN_FACTOR_SEARCH_REQUIRED",
            completion_status="FINALITY_NOT_LICENSED",
        )

    if candidate.relation == "access_readout":
        return report(
            candidate,
            signal_status="READOUT_NOT_DELIVERY",
            hierarchy_levels=("records", "access"),
            verdict="ACCESS_CHANGE_ONLY",
        )

    if candidate.relation == "signal" and not has_transfer(candidate):
        return report(
            candidate,
            signal_status="UNDERDECLARED_SIGNAL",
            hierarchy_levels=(),
            verdict="ABSTAIN_TRANSFER_UNDECLARED",
            completion_status="NOT_EVALUATED",
        )

    if not candidate.matched_resource_frame:
        return report(
            candidate,
            signal_status="DELIVERED_TRANSFER",
            hierarchy_levels=("resources",),
            verdict="RESOURCE_FRAME_CHANGED",
        )

    if candidate.timing == "scheduled":
        return report(
            candidate,
            signal_status="EXTERNALLY_SCHEDULED_SIGNAL",
            hierarchy_levels=("dynamics", "resources"),
            verdict="EXTERNALLY_DRIVEN_NOT_AUTONOMOUS",
        )

    if candidate.timing == "stochastic":
        return report(
            candidate,
            signal_status="STOCHASTIC_DRIVER",
            hierarchy_levels=("dynamics",),
            verdict="ABSTAIN_RECORD_AND_TIMING_UNPINNED",
        )

    if candidate.relation in {"feedback", "law_update"}:
        if candidate.closure != "closed":
            return report(
                candidate,
                signal_status="STATE_DEPENDENT_FEEDBACK",
                hierarchy_levels=("dynamics",),
                verdict="AUTONOMOUS_FEEDBACK_UNCLOSED",
            )
        if candidate.matched_task_delta and candidate.matched_access_frame:
            return report(
                candidate,
                signal_status="STATE_DEPENDENT_FEEDBACK",
                hierarchy_levels=("dynamics", "records", "access", "capability"),
                verdict="CAPABILITY_CHANGE_CANDIDATE_NO_FINALITY",
            )
        return report(
            candidate,
            signal_status="STATE_DEPENDENT_FEEDBACK",
            hierarchy_levels=("dynamics",),
            verdict="MAINTENANCE_CLOSURE_NOT_CAPABILITY",
        )

    if candidate.matched_task_delta and candidate.matched_access_frame:
        return report(
            candidate,
            signal_status="DELIVERED_TRANSFER",
            hierarchy_levels=("dynamics", "access", "capability"),
            verdict="CAPABILITY_CHANGE_CANDIDATE_NO_FINALITY",
        )

    return report(
        candidate,
        signal_status="UNDERDEFINED_BOUNDARY_RELATION",
        hierarchy_levels=(),
        verdict="ABSTAIN_UNDERDETERMINED",
        completion_status="NOT_EVALUATED",
    )


def candidate_inventory() -> tuple[BoundaryCandidate, ...]:
    return (
        BoundaryCandidate(
            "apparent_boundary_representation",
            "formal_language",
            "representation_map",
            "condition",
            (),
            "fixed",
            "none",
            True,
            True,
            False,
            True,
            False,
            False,
            False,
            False,
            "relabel boundary words without changing reachable tasks",
        ),
        BoundaryCandidate(
            "static_global_datum",
            "global_parameter",
            "global_condition",
            "condition",
            (),
            "fixed",
            "none",
            True,
            True,
            False,
            True,
            False,
            False,
            True,
            False,
            "preload the datum in a completed family and compare no-new-task output",
        ),
        BoundaryCandidate(
            "initial_or_boundary_condition",
            "initial_data_surface",
            "initial_condition",
            "condition",
            (),
            "initial",
            "none",
            True,
            True,
            False,
            False,
            False,
            False,
            True,
            False,
            "vary the initial condition while holding update law and task frame fixed",
        ),
        BoundaryCandidate(
            "two_ended_fixed_point_condition",
            "two_boundary_solver",
            "global_consistency_constraint",
            "fixed_point",
            (),
            "fixed",
            "none",
            True,
            True,
            False,
            False,
            False,
            False,
            False,
            True,
            "factor the settlement through earlier levels before naming finality",
        ),
        BoundaryCandidate(
            "observer_epistemic_readout",
            "observer_access_channel",
            "readout_projection",
            "access_readout",
            ("information",),
            "state_dependent",
            "none",
            True,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            "same external trace exists while only the observer projection changes",
        ),
        BoundaryCandidate(
            "physical_intervention",
            "laboratory_actuator",
            "intervention_signal",
            "signal",
            ("energy", "information"),
            "scheduled",
            "none",
            False,
            True,
            True,
            False,
            False,
            False,
            True,
            True,
            "match the resource budget; if the effect disappears, it was resource change",
        ),
        BoundaryCandidate(
            "autonomous_bulk_boundary_feedback",
            "bulk_trace_loop",
            "state_dependent_boundary",
            "feedback",
            ("information", "resource"),
            "state_dependent",
            "closed",
            True,
            True,
            False,
            False,
            False,
            False,
            False,
            True,
            "remove the return arrow and test whether maintenance still persists",
        ),
        BoundaryCandidate(
            "edge_defect_membrane_anomaly_flow",
            "edge_degree_of_freedom",
            "anomaly_inflow",
            "feedback",
            ("information",),
            "state_dependent",
            "attempted",
            True,
            True,
            False,
            False,
            False,
            False,
            False,
            True,
            "close the boundary variable and show a task delta beyond conserved inflow",
        ),
        BoundaryCandidate(
            "enlarged_system_resource_reservoir",
            "environment_reservoir",
            "resource_flow",
            "signal",
            ("energy", "resource"),
            "state_dependent",
            "none",
            False,
            True,
            True,
            False,
            False,
            False,
            False,
            True,
            "hold total resource frame fixed and check whether the task delta remains",
        ),
        BoundaryCandidate(
            "stochastic_environment_noise",
            "noise_source",
            "random_driver",
            "signal",
            ("energy",),
            "stochastic",
            "none",
            True,
            True,
            False,
            False,
            False,
            False,
            True,
            False,
            "replace noise with matched null draw and require a durable record channel",
        ),
        BoundaryCandidate(
            "native_source_current_or_law_update",
            "source_native_current",
            "native_update",
            "law_update",
            ("information",),
            "state_dependent",
            "attempted",
            True,
            True,
            True,
            False,
            False,
            True,
            False,
            True,
            "wait for a source-issued frozen packet naming the native current",
        ),
        BoundaryCandidate(
            "meta_system_or_ensemble_selection",
            "ensemble_index",
            "after_fact_selector",
            "condition",
            (),
            "after_fact",
            "none",
            True,
            True,
            False,
            True,
            True,
            False,
            False,
            False,
            "shuffle realized outcomes after the fact; no delivered signal should appear",
        ),
        BoundaryCandidate(
            "calibration_closed_matched_task_delta",
            "synthetic_carrier",
            "closed_feedback_control",
            "feedback",
            ("information",),
            "state_dependent",
            "closed",
            True,
            True,
            True,
            False,
            False,
            False,
            False,
            True,
            "remove the feedback channel under the same budget and lose the task",
        ),
        BoundaryCandidate(
            "underdeclared_signal_control",
            "empty_signal_label",
            "claimed_signal",
            "signal",
            (),
            "state_dependent",
            "none",
            True,
            True,
            False,
            False,
            False,
            False,
            False,
            False,
            "require declared transfer before treating a label as signal",
        ),
    )


def clone_on_new_carrier(candidate: BoundaryCandidate, carrier: str) -> BoundaryCandidate:
    return replace(candidate, carrier=carrier)


def bad_signal_blind_classifier(candidate: BoundaryCandidate) -> str:
    if candidate.relation in {"condition", "signal", "feedback"}:
        return "DELIVERED_SIGNAL"
    return "NO_SIGNAL"


def bad_completion_blind_classifier(candidate: BoundaryCandidate) -> str:
    if candidate.completion_absorbed or candidate.matched_task_delta:
        return "CAPABILITY_CHANGE_CANDIDATE_NO_FINALITY"
    return "ABSTAIN"


def bad_resource_blind_classifier(candidate: BoundaryCandidate) -> str:
    if has_transfer(candidate):
        return "CAPABILITY_CHANGE_CANDIDATE_NO_FINALITY"
    return "NO_TRANSFER"


def bad_after_fact_classifier(candidate: BoundaryCandidate) -> str:
    if candidate.after_fact_encoding:
        return "DELIVERED_SIGNAL"
    return "NO_SIGNAL"


def bad_source_blind_classifier(candidate: BoundaryCandidate) -> str:
    if candidate.source_packet_required:
        return "DYNAMICS_UPDATE_ACCEPTED"
    return "NO_SOURCE_CLAIM"


def main() -> None:
    candidates = {candidate.candidate_id: candidate for candidate in candidate_inventory()}
    reports = {key: classify_candidate(candidate) for key, candidate in candidates.items()}

    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    required_ids = {
        "apparent_boundary_representation",
        "static_global_datum",
        "initial_or_boundary_condition",
        "two_ended_fixed_point_condition",
        "observer_epistemic_readout",
        "physical_intervention",
        "autonomous_bulk_boundary_feedback",
        "edge_defect_membrane_anomaly_flow",
        "enlarged_system_resource_reservoir",
        "stochastic_environment_noise",
        "native_source_current_or_law_update",
        "meta_system_or_ensemble_selection",
    }

    carrier_probe = candidates["calibration_closed_matched_task_delta"]
    cloned_probe = clone_on_new_carrier(carrier_probe, "organizational_control_loop")
    carrier_report = classify_candidate(carrier_probe)
    cloned_report = classify_candidate(cloned_probe)

    check("setup: preserved intake classes are represented", required_ids <= set(candidates))
    check(
        "setup: every candidate declares an observable null distinction",
        all(candidate.null_distinction for candidate in candidates.values()),
    )
    check(
        "carrier neutrality: carrier labels do not change typed verdicts",
        carrier_report.verdict == cloned_report.verdict
        and carrier_report.hierarchy_levels == cloned_report.hierarchy_levels
        and carrier_report.signal_status == cloned_report.signal_status,
    )
    check(
        "condition: fixed boundary datum is not a delivered signal",
        reports["initial_or_boundary_condition"].signal_status == "CONDITION_ONLY"
        and reports["initial_or_boundary_condition"].verdict == "INITIATION_CONDITION_NOT_SIGNAL",
    )
    check(
        "completion: static global datum is absorbed as fixed-family completion",
        reports["static_global_datum"].verdict == "FIXED_FAMILY_COMPLETION"
        and reports["static_global_datum"].completion_status == "ABSORBED",
    )
    check(
        "fixed point: two-ended condition remains finality-abstain",
        reports["two_ended_fixed_point_condition"].hierarchy_levels == ("finality",)
        and reports["two_ended_fixed_point_condition"].verdict == "ABSTAIN_FACTOR_SEARCH_REQUIRED",
    )
    check(
        "access: epistemic observer readout maps to access change only",
        reports["observer_epistemic_readout"].verdict == "ACCESS_CHANGE_ONLY"
        and reports["observer_epistemic_readout"].hierarchy_levels == ("records", "access"),
    )
    check(
        "resource: physical intervention changes resource frame before capability",
        reports["physical_intervention"].verdict == "RESOURCE_FRAME_CHANGED"
        and reports["physical_intervention"].hierarchy_levels == ("resources",),
    )
    check(
        "feedback: autonomous closure without task delta is maintenance not capability",
        reports["autonomous_bulk_boundary_feedback"].verdict == "MAINTENANCE_CLOSURE_NOT_CAPABILITY"
        and "capability" not in reports["autonomous_bulk_boundary_feedback"].hierarchy_levels,
    )
    check(
        "edge: membrane or anomaly-flow candidate stays underdefined without task delta",
        reports["edge_defect_membrane_anomaly_flow"].verdict == "AUTONOMOUS_FEEDBACK_UNCLOSED",
    )
    check(
        "reservoir: enlarged-system reservoir is resource change not matched capability",
        reports["enlarged_system_resource_reservoir"].verdict == "RESOURCE_FRAME_CHANGED",
    )
    check(
        "stochastic: noise environment abstains unless timing and record are pinned",
        reports["stochastic_environment_noise"].verdict == "ABSTAIN_RECORD_AND_TIMING_UNPINNED",
    )
    check(
        "source sovereignty: native current waits for frozen source packet",
        reports["native_source_current_or_law_update"].verdict == "ABSTAIN_SOURCE_SOVEREIGNTY",
    )
    check(
        "after-fact: ensemble selection is outcome encoding not a delivered signal",
        reports["meta_system_or_ensemble_selection"].signal_status == "AFTER_FACT_OUTCOME_ENCODING"
        and reports["meta_system_or_ensemble_selection"].verdict == "NOT_A_DELIVERED_SIGNAL",
    )
    check(
        "positive calibration: closed matched task delta can reach capability candidate",
        reports["calibration_closed_matched_task_delta"].verdict
        == "CAPABILITY_CHANGE_CANDIDATE_NO_FINALITY"
        and reports["calibration_closed_matched_task_delta"].hierarchy_levels
        == ("dynamics", "records", "access", "capability"),
    )

    check(
        "condition-fail: bad classifier calls a fixed condition a signal",
        bad_signal_blind_classifier(candidates["initial_or_boundary_condition"]) == "CONDITION_ONLY",
        expected=False,
    )
    check(
        "completion-fail: bad classifier ignores fixed-family absorption",
        bad_completion_blind_classifier(candidates["static_global_datum"]) == "FIXED_FAMILY_COMPLETION",
        expected=False,
    )
    check(
        "resource-fail: bad classifier ignores resource-frame mismatch",
        bad_resource_blind_classifier(candidates["enlarged_system_resource_reservoir"])
        == "RESOURCE_FRAME_CHANGED",
        expected=False,
    )
    check(
        "after-fact-fail: bad classifier treats outcome encoding as signal",
        bad_after_fact_classifier(candidates["meta_system_or_ensemble_selection"])
        == "NOT_A_DELIVERED_SIGNAL",
        expected=False,
    )
    check(
        "source-fail: bad classifier imports a native source-current claim",
        bad_source_blind_classifier(candidates["native_source_current_or_law_update"])
        == "ABSTAIN_SOURCE_SOVEREIGNTY",
        expected=False,
    )

    print("BOUNDARY EXTERNALITY / SIGNAL DISCRIMINATOR")
    print("=" * 72)
    failures = []
    n_t = n_e = n_f = 0
    for name, value, expected in checks:
        ok = value == expected
        tag = CHECKS.get(name, {}).get("tag", "?")
        n_t += tag == "T"
        n_e += tag == "E"
        n_f += tag == "F"
        print(f"{'PASS' if ok else 'UNEXPECTED'}  [{tag}] {name}: {value}")
        if not ok:
            failures.append(name)

    print()
    print("candidate verdicts:")
    for key in sorted(reports):
        candidate_report = reports[key]
        print(
            f"  {key:42} signal={candidate_report.signal_status:30} "
            f"frame={candidate_report.frame_status:34} verdict={candidate_report.verdict}"
        )
    print()
    print(f"EVIDENTIAL CHECKS (headline): {n_e} [E] + {n_f} [F] = {n_e + n_f}")
    print(f"[T] theorem-consequence checks (no evidential weight): {n_t}")

    payload = {
        "artifact": "P2C-BOUNDARY-EXTERNALITY-DISCRIMINATOR",
        "claim_tier": "exploration",
        "nonclaims": [
            "no outside-universe verdict",
            "no source-repo truth movement",
            "no GU firewall construction",
            "no public or external action",
        ],
        "reports": {key: asdict(value) for key, value in reports.items()},
        "evidential_checks": {"E": n_e, "F": n_f, "total": n_e + n_f},
        "theorem_checks": n_t,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()
