"""Deterministic adversarial controls for Transition Diagnosis v0.1."""

from __future__ import annotations

import copy
import json
import re
from pathlib import Path
from typing import Any

from classify_transition import WITNESS_FIELDS, evaluate_assessment


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "interfaces" / "transition-diagnosis-v0.1.schema.json"
VALID_PATH = ROOT / "tests" / "fixtures" / "transition-diagnosis-v0.1-valid.json"
CASES_PATH = ROOT / "tests" / "fixtures" / "transition-diagnosis-v0.1-cases.json"

DEFAULT_WITNESS = {
    "possibility_family_relation": "SAME",
    "representation_relation": "EQUIVALENT",
    "description_change": "NO",
    "dynamics_change": "NO",
    "persistent_record": "NO",
    "access_change": "NO",
    "control_change": "NO",
    "raw_task_set_relation": "EQUAL",
    "normalized_task_set_relation": "EQUAL",
    "irreversible": "NO",
    "settlement": "NO",
    "preceding_layer_factorization": "NOT_APPLICABLE",
    "reopenable_by_admissible_continuation": "YES",
    "ordering_relation": "ORDER_COMPATIBLE",
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict), f"fixture root must be an object: {path}"
    return value


def qualified_witness(case_id: str, overrides: dict[str, str]) -> dict[str, Any]:
    values = DEFAULT_WITNESS | overrides
    assert set(values) == set(WITNESS_FIELDS)
    return {
        field: {
            "value": value,
            "evidence_refs": [f"synthetic://{case_id}/{field}"],
        }
        for field, value in values.items()
    }


def safe_branch_id(case_id: str) -> str:
    return re.sub(r"[^a-z0-9_-]", "-", case_id.lower())


def make_branch(
    case_id: str,
    branch_id: str,
    overrides: dict[str, str],
    declared_claims: list[str] | None = None,
    admissibility: str = "ADMISSIBLE",
) -> dict[str, Any]:
    values = DEFAULT_WITNESS | overrides
    return {
        "branch_id": branch_id,
        "label": f"synthetic label for {branch_id}",
        "admissibility": admissibility,
        "witness": qualified_witness(case_id, overrides),
        "normalization_frame": "Common synthetic task vocabulary; description, resources, access, and control held fixed for normalized comparison.",
        "factorization_search_scope": (
            "All preceding-layer factorizations enumerated by this bounded synthetic control."
            if values["preceding_layer_factorization"] == "NO_FACTOR_FOUND"
            else None
        ),
        "declared_claims": declared_claims or [],
        "evidence_grade": "SYNTHETIC_CONTROL",
        "verification": "DETERMINISTIC_SYNTHETIC",
    }


def make_assessment(
    case_id: str,
    branches: list[dict[str, Any]],
    branch_relation: str,
) -> dict[str, Any]:
    numeric = sum((index + 1) * ord(char) for index, char in enumerate(case_id)) % 900 + 100
    return {
        "schema_version": "0.1",
        "assessment_id": f"CASE-TD-{numeric}",
        "status": "provisional",
        "question": f"What transition diagnosis follows for synthetic case {case_id}?",
        "construction": {
            "fork_identified": len(branches) > 1,
            "selected_branch_id": branches[0]["branch_id"] if len(branches) == 1 else None,
            "retention_statement": "Every supplied synthetic construction remains visible; no branch verdict is merged into another.",
        },
        "branch_relation": branch_relation,
        "branches": branches,
        "label_neutrality": {"left_label": "alpha", "right_label": "beta", "required": True},
        "assumptions": ["The case's synthetic witness values are stipulated only to test classifier behavior."],
        "evidence_grade": "SYNTHETIC_CONTROL",
        "tests": ["Compute the expected diagnosis and repeat after a pure label swap."],
        "falsifiers": ["A computed diagnosis differs from the tabled expectation."],
        "nonclaims": ["This synthetic case establishes no physical transition or source claim."],
        "reopening_conditions": ["A real frozen case exposes an unrepresented distinction."],
    }


def main() -> None:
    schema = load_json(SCHEMA_PATH)
    valid_fixture = load_json(VALID_PATH)
    tables = load_json(CASES_PATH)
    checks = 0

    assert schema["properties"]["schema_version"]["const"] == "0.1"
    assert schema["properties"]["branches"]["minItems"] == 1
    assert schema["properties"]["label_neutrality"]["properties"]["required"]["const"] is True
    assert set(schema["$defs"]["witness"]["required"]) == set(WITNESS_FIELDS)
    checks += 1

    valid_result = evaluate_assessment(copy.deepcopy(valid_fixture))
    assert valid_result["valid"], valid_result["errors"]
    assert valid_result["aggregate_outcome"] == "ACCESS_CHANGE"
    assert valid_result["branch_results"][0]["rejected_declared_claims"] == ["CAPABILITY_ENLARGEMENT"]
    assert valid_result["label_invariance"]["invariant"] is True
    checks += 1

    outcome_coverage: set[str] = {valid_result["aggregate_outcome"]}
    case_list = tables["cases"]
    assert isinstance(case_list, list) and len(case_list) >= 30
    seen: set[str] = set()
    false_positive_cases = {
        "new-description-not-new-capability",
        "record-is-not-access",
        "access-called-capability",
        "irreversibility-not-finality",
    }
    for case in case_list:
        case_id = case["case_id"]
        assert case_id not in seen
        seen.add(case_id)
        branch = make_branch(
            case_id,
            safe_branch_id(case_id),
            case.get("witness", {}),
            case.get("declared_claims", []),
            case.get("admissibility", "ADMISSIBLE"),
        )
        assessment = make_assessment(case_id, [branch], "SAME_OBJECT")
        result = evaluate_assessment(assessment)
        assert result["valid"], f"case {case_id}: {result['errors']}"
        assert result["aggregate_outcome"] == case["expected_outcome"], (case_id, result)
        branch_result = result["branch_results"][0]
        assert branch_result["outcome"] == case.get("expected_branch_outcome", case["expected_outcome"]), (case_id, result)
        assert branch_result["components"] == case["expected_components"], (case_id, result)
        assert branch_result["rejected_declared_claims"] == case["expected_rejected_claims"], (case_id, result)
        if "expected_alert_contains" in case:
            assert any(case["expected_alert_contains"] in alert for alert in branch_result["alerts"]), (case_id, result)
        assert result["label_invariance"]["tested"] is True
        assert result["label_invariance"]["invariant"] is True
        outcome_coverage.add(result["aggregate_outcome"])
        checks += 1

    assert false_positive_cases <= seen
    assert {"MULTI_LEVEL", "INCOMPARABLE", "UNKNOWN", "CONTESTED", "HIERARCHY_REVISION"} <= outcome_coverage
    checks += 1

    fork_cases = tables["fork_cases"]
    assert isinstance(fork_cases, list) and len(fork_cases) >= 4
    for case in fork_cases:
        branches = [
            make_branch(case["case_id"], item["branch_id"], item["witness"])
            for item in case["branches"]
        ]
        assessment = make_assessment(case["case_id"], branches, case["branch_relation"])
        result = evaluate_assessment(assessment)
        assert result["valid"], f"fork case {case['case_id']}: {result['errors']}"
        assert result["aggregate_outcome"] == case["expected_outcome"], (case["case_id"], result)
        assert [item["outcome"] for item in result["branch_results"]] == [
            item["expected_outcome"] for item in case["branches"]
        ]
        assert result["label_invariance"]["invariant"] is True
        outcome_coverage.add(result["aggregate_outcome"])
        checks += 1

    malformed = copy.deepcopy(valid_fixture)
    malformed["branches"][0]["witness"]["access_change"]["evidence_refs"] = []
    result = evaluate_assessment(malformed)
    assert result["valid"] is False
    assert any("needs unique evidence refs" in error for error in result["errors"])
    checks += 1

    missing_frame = copy.deepcopy(valid_fixture)
    missing_frame["branches"][0]["normalization_frame"] = None
    result = evaluate_assessment(missing_frame)
    assert result["valid"] is False
    assert any("normalization_frame required" in error for error in result["errors"])
    checks += 1

    finality = make_branch(
        "missing-factorization-scope",
        "missing-factorization-scope",
        {
            "settlement": "YES",
            "preceding_layer_factorization": "NO_FACTOR_FOUND",
            "reopenable_by_admissible_continuation": "NO",
        },
    )
    finality["factorization_search_scope"] = None
    result = evaluate_assessment(make_assessment("missing-factorization-scope", [finality], "SAME_OBJECT"))
    assert result["valid"] is False
    assert any("factorization search scope required" in error for error in result["errors"])
    checks += 1

    fake_fork = copy.deepcopy(valid_fixture)
    fake_fork["construction"]["fork_identified"] = True
    result = evaluate_assessment(fake_fork)
    assert result["valid"] is False
    assert any("fork_identified must agree" in error for error in result["errors"])
    checks += 1

    bad_labels = copy.deepcopy(valid_fixture)
    bad_labels["label_neutrality"]["right_label"] = bad_labels["label_neutrality"]["left_label"]
    result = evaluate_assessment(bad_labels)
    assert result["valid"] is False
    assert any("neutrality labels must differ" in error for error in result["errors"])
    checks += 1

    required_outcomes = {
        "FIXED_FAMILY_DISCLOSURE",
        "FIXED_FAMILY_DYNAMICS",
        "RECORD_FORMATION",
        "ACCESS_CHANGE",
        "POSSIBILITY_FAMILY_CHANGE",
        "CAPABILITY_ENLARGEMENT",
        "CAPABILITY_RESTRICTION",
        "FINALITY_CANDIDATE",
        "MULTI_LEVEL",
        "INCOMPARABLE",
        "CONSTRUCTION_FORK",
        "UNKNOWN",
        "CONTESTED",
        "HIERARCHY_REVISION",
        "NULL_NO_RELEVANT_CHANGE",
        "NULL_NO_ADMISSIBLE_CONSTRUCTION",
    }
    assert required_outcomes <= outcome_coverage, sorted(required_outcomes - outcome_coverage)
    checks += 1

    total_cases = len(case_list) + len(fork_cases)
    print(
        f"PASS: {checks}/{checks} Transition Diagnosis v0.1 groups; "
        f"{total_cases} synthetic cases; {len(outcome_coverage)} aggregate outcomes"
    )


if __name__ == "__main__":
    main()
