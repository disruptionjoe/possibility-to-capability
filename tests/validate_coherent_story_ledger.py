#!/usr/bin/env python3
"""Validate the provisional coherent-story ledger and adversarial controls.

This checks epistemic and boundary structure. It does not establish physics,
source truth, novelty, universality, or the truth of any rival.
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = ROOT / "hypotheses" / "2026-07-14-coherent-story-ledger-v0.1.json"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("ledger root must be an object")
    return value


def validate(ledger: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    require(ledger.get("artifact_type") == "provisional_hypothesis_evidence_rival_ledger", "artifact type must remain provisional ledger")
    require(ledger.get("status") == "provisional", "ledger status must remain provisional")
    require(ledger.get("construction") == "typed_partial_diagnostic", "construction must be typed partial diagnostic")

    hypothesis = ledger.get("guiding_hypothesis", {})
    question = hypothesis.get("question", "")
    require(hypothesis.get("is_question") is True and isinstance(question, str) and question.endswith("?"), "guiding hypothesis must be a question")
    require(hypothesis.get("verdict") == "OPEN", "guiding hypothesis verdict must remain OPEN")
    require(hypothesis.get("promotion_status") == "NOT_PROMOTED", "guiding hypothesis must not be promoted")
    require(hypothesis.get("evidence_ceiling") == "synthetic_plus_blocked_real_intake", "evidence ceiling must preserve synthetic plus blocked real intake")

    candidate = ledger.get("candidate_story", {})
    require(candidate.get("relation_type") == "typed_partial_diagnostic", "candidate relation must remain a typed partial diagnostic")
    require(candidate.get("is_chronology") is False, "candidate must not become a chronology")
    require(candidate.get("is_causal_sequence") is False, "candidate must not become a causal sequence")
    require(candidate.get("is_total_order") is False, "candidate must not become a total order")
    require(candidate.get("allows_skipped_types") is True, "candidate must preserve skipped types")
    require(candidate.get("allows_multi_level") is True, "candidate must preserve multi-level cases")
    require(candidate.get("allows_incomparable_types") is True, "candidate must preserve incomparable cases")
    require(candidate.get("allows_construction_fork") is True, "candidate must preserve construction forks")
    require(candidate.get("allows_hierarchy_revision") is True, "candidate must preserve hierarchy revision")

    expected_finality_controls = {
        "settlement_witness",
        "named_factorization_search_scope",
        "no_factor_found_under_scope",
        "no_reopening_by_admissible_continuation",
    }
    require(candidate.get("finality_status") == "FINALITY_CANDIDATE_ONLY", "finality must remain candidate-only")
    require(set(candidate.get("finality_minimum_controls", [])) == expected_finality_controls, "finality must retain settlement, scoped factorization, and reopening controls")
    require("does not establish absolute" in candidate.get("finality_nonclaim", ""), "finality must explicitly reject absolute proof from bounded search")

    boundary = candidate.get("access_capability_boundary", {})
    require(boundary.get("access") != boundary.get("capability"), "access and capability definitions must remain distinct")
    require(set(boundary.get("normalization_must_hold_fixed", [])) == {"description", "representation", "resources", "access", "control"}, "capability normalization frame is incomplete")
    require(boundary.get("constitutive_access_fork_retained") is True, "access-constitutive capability fork must remain live")
    require(bool(boundary.get("reopening_condition")), "access-capability boundary needs a reopening condition")

    evidence = ledger.get("evidence_state", {})
    require(evidence.get("accepted_real_packets") == 0, "accepted real packet count must remain zero")
    require(evidence.get("completed_real_eight_gate_runs") == 0, "completed real gate-run count must remain zero")
    require(evidence.get("physical_finality_gate_results") == 0, "physical finality result count must remain zero")
    gu = evidence.get("gu_001", {})
    require(gu.get("role") == "founding_motivation_only", "GU-001 role must remain founding motivation only")
    require(gu.get("import_status") == "NOT_YET_IMPORTABLE", "GU-001 must remain NOT_YET_IMPORTABLE")
    require(gu.get("provenance_preflight") == "BLOCKED", "GU-001 provenance must remain BLOCKED")
    require(gu.get("receiving_independence_assessment") == "NOT_ADMISSIBLE_NOT_RUN", "GU receiving assessment must remain not admissible and not run")
    require(gu.get("full_gate_run") == "NOT_ADMISSIBLE_NOT_RUN", "GU full gate run must remain not admissible and not run")
    require(gu.get("downstream_gates") == "BLOCKED_NOT_RUN", "GU downstream gates must remain blocked and not run")
    require(gu.get("may_support_candidate_story") is False, "blocked GU evidence must not support candidate story")
    require(gu.get("may_support_rival_story") is False, "blocked GU evidence must not support rival story")
    require(gu.get("receiver_method_count") is None, "receiver must not assign GU method count")
    require(gu.get("receiver_convergence_verdict") is None, "receiver must not assign GU convergence verdict")
    require(gu.get("receiver_independence_verdict") is None, "receiver must not assign GU independence verdict")

    classes = ledger.get("claim_classes", {})
    expected_classes = {
        "widely_known_conceptual_ingredients",
        "repo_new_assembly_and_machinery",
        "provisional_synthetic_results",
        "blocked_founding_motivation",
        "genuinely_open_claims",
    }
    require(set(classes) == expected_classes, "claim classes must preserve the five epistemic categories")
    for item in classes.get("widely_known_conceptual_ingredients", []):
        require(item.get("novelty_claimed") is False, f"{item.get('id', 'known ingredient')} must not claim novelty")
    for item in classes.get("provisional_synthetic_results", []):
        require(item.get("grade") == "deterministic_synthetic", f"{item.get('id', 'synthetic result')} grade must remain deterministic synthetic")
        require(item.get("physical_claim") is False, f"{item.get('id', 'synthetic result')} must not become physical claim")
    require(any(item.get("status") == "NOT_YET_IMPORTABLE" for item in classes.get("blocked_founding_motivation", [])), "blocked founding motivation must preserve NOT_YET_IMPORTABLE")
    require(len(classes.get("genuinely_open_claims", [])) >= 5, "ledger must retain a substantial open-claim set")
    for item in classes.get("genuinely_open_claims", []):
        require(str(item.get("status", "")).startswith("OPEN"), f"{item.get('id', 'open claim')} must remain open")

    rivals = ledger.get("rivals", [])
    require(isinstance(rivals, list) and len(rivals) >= 3, "at least three strong rivals are required")
    rival_ids = [item.get("id") for item in rivals if isinstance(item, dict)]
    require(len(rival_ids) == len(set(rival_ids)), "rival ids must be unique")
    ranks = [item.get("rank_as_rival") for item in rivals if isinstance(item, dict)]
    require(ranks == list(range(1, len(rivals) + 1)), "rival ranks must be contiguous and ordered")
    for rival in rivals:
        require(rival.get("status") == "LIVE", f"{rival.get('id', 'rival')} must remain live")
        require(len(rival.get("steelman", "")) >= 120, f"{rival.get('id', 'rival')} steelman is too weak")
        require(len(rival.get("observations_favoring_rival", [])) >= 3, f"{rival.get('id', 'rival')} needs at least three exact favoring observations")
        require(len(rival.get("observations_favoring_candidate_over_rival", [])) >= 2, f"{rival.get('id', 'rival')} needs candidate discriminators")

    safeguards = ledger.get("safeguards", {})
    source = safeguards.get("source_sovereignty", {})
    require(source.get("gu_ti_taf_truth_frozen") is True, "source truth must remain frozen")
    require(source.get("source_claim_status_changes") is False, "source claim status changes are forbidden")
    require(source.get("blocked_source_used_as_support") is False, "blocked source cannot be used as support")
    artificial = safeguards.get("no_artificial_success", {})
    require(artificial.get("joint_real_gate_status") == "NOT_RUN", "no real joint gate may be reported as run")
    require(artificial.get("cross_repo_partial_aggregation") is False, "cross-repo partial aggregation is forbidden")
    require(artificial.get("one_argument_chain_required_for_success") is True, "one-chain success guard must remain")
    forks = safeguards.get("construction_forks", {})
    require(forks.get("retained") is True, "construction forks must be retained")
    require(forks.get("transfer_without_test") is False, "conclusions must not transfer across constructions without test")
    circularity = safeguards.get("finality_anti_circularity", {})
    require(circularity.get("irreversibility_sufficient") is False, "irreversibility must not imply finality")
    require(circularity.get("no_factor_found_equals_absolute_proof") is False, "no-factor-found must not become absolute proof")
    require(circularity.get("candidate_label_required") is True, "finality candidate label must remain required")
    collapse = safeguards.get("access_capability_anti_collapse", {})
    require(collapse.get("raw_task_availability_equals_capability") is False, "raw task availability must not equal capability")
    require(collapse.get("normalization_frame_required") is True, "capability normalization frame must remain required")
    require(collapse.get("constitutive_access_fork_retained") is True, "access-constitutive fork must remain")

    require(ledger.get("numeric_likelihood_assigned") is False, "numeric likelihood must not be assigned from current evidence")
    confidence = {item.get("target"): item for item in ledger.get("confidence_calibration", [])}
    require(confidence.get("universality_or_completeness", {}).get("level") == "low_and_unsupported", "universality confidence must remain low and unsupported")
    require(confidence.get("physical_irreducibility_of_finality", {}).get("level") == "not_assessable", "physical finality confidence must remain not assessable")
    require(confidence.get("gu_as_confirmation", {}).get("level") == "not_admissible", "GU confirmation confidence must remain not admissible")

    require(len(ledger.get("candidate_killers", [])) >= 5, "candidate needs explicit killers")
    require(len(ledger.get("falsifiers", [])) >= 5, "candidate needs explicit falsifiers")
    require(len(ledger.get("nonclaims", [])) >= 5, "candidate needs explicit nonclaims")
    require(len(ledger.get("reopening_conditions", [])) >= 5, "candidate needs explicit reopening conditions")

    refs: list[str] = []
    for key in ("decisive_test_program_ref", "adversarial_validation_ref", "synthesis_ref"):
        value = ledger.get(key)
        require(isinstance(value, str) and bool(value), f"{key} is required")
        if isinstance(value, str):
            refs.append(value)
    for ref in refs:
        require(not Path(ref).is_absolute(), f"public artifact reference must be relative: {ref}")
        require(not re.match(r"^[A-Za-z]:", ref), f"public artifact reference leaks a drive path: {ref}")
        require((ROOT / ref).is_file(), f"referenced artifact does not exist: {ref}")

    return errors


def run_adversarial_cases(base: dict[str, Any]) -> tuple[int, int, list[str]]:
    Mutator = Callable[[dict[str, Any]], None]
    cases: list[tuple[str, Mutator, str]] = []

    def add(name: str, mutator: Mutator, expected: str) -> None:
        cases.append((name, mutator, expected))

    add("overclaim-promoted", lambda x: x["guiding_hypothesis"].update({"verdict": "ACCEPTED", "promotion_status": "PROMOTED"}), "must remain OPEN")
    add("chronology-smuggle", lambda x: x["candidate_story"].update({"is_chronology": True}), "must not become a chronology")
    add("circular-finality", lambda x: x["safeguards"]["finality_anti_circularity"].update({"no_factor_found_equals_absolute_proof": True}), "must not become absolute proof")
    add("finality-upgrade", lambda x: x["candidate_story"].update({"finality_status": "FINALITY_ESTABLISHED"}), "finality must remain candidate-only")
    add("access-capability-collapse", lambda x: x["safeguards"]["access_capability_anti_collapse"].update({"raw_task_availability_equals_capability": True}), "raw task availability must not equal capability")
    add("source-leakage", lambda x: x["evidence_state"]["gu_001"].update({"may_support_candidate_story": True}), "must not support candidate story")
    add("artificial-success", lambda x: x["safeguards"]["no_artificial_success"].update({"joint_real_gate_status": "PASS", "cross_repo_partial_aggregation": True}), "no real joint gate may be reported as run")
    add("construction-suppression", lambda x: x["safeguards"]["construction_forks"].update({"retained": False}), "construction forks must be retained")
    add("weak-rival", lambda x: x["rivals"][0].update({"observations_favoring_rival": []}), "needs at least three exact favoring observations")

    passed = 0
    failures: list[str] = []
    for name, mutator, expected in cases:
        candidate = copy.deepcopy(base)
        mutator(candidate)
        errors = validate(candidate)
        if any(expected in error for error in errors):
            passed += 1
        else:
            failures.append(f"{name}: expected error containing {expected!r}; got {errors}")
    return passed, len(cases), failures


def main() -> int:
    try:
        ledger = load_json(LEDGER_PATH)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL: could not load ledger: {exc}")
        return 1

    errors = validate(ledger)
    adversarial_passed, adversarial_total, adversarial_failures = run_adversarial_cases(ledger)
    errors.extend(adversarial_failures)

    if errors:
        print(f"FAIL: {len(errors)} coherent-story ledger error(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    groups = 10
    print(
        "PASS: "
        f"{groups}/{groups} coherent-story boundary groups; "
        f"{adversarial_passed}/{adversarial_total} adversarial mutations rejected; "
        f"{len(ledger['rivals'])} live rivals"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
