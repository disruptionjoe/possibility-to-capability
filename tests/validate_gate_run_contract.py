"""Deterministic positive, negative, blocked, split, and adversarial controls."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

from evaluate_gate_run import GATE_IDS, evaluate_gate_run


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "interfaces" / "gate-run-v0.1.schema.json"
FIXTURE_ROOT = ROOT / "tests" / "fixtures"
RUN_PATH = FIXTURE_ROOT / "gate-run-v0.1-positive.json"
CASES_PATH = FIXTURE_ROOT / "gate-run-v0.1-cases.json"
PACKET_PATH = FIXTURE_ROOT / "frozen-packet-v0.2-valid.json"
ASSESSMENT_PATH = FIXTURE_ROOT / "receiving-independence-v0.2-valid.json"


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict), f"fixture root must be an object: {path}"
    return value


def pointer_parent(document: object, pointer: str) -> tuple[object, str]:
    assert pointer.startswith("/")
    tokens = [token.replace("~1", "/").replace("~0", "~") for token in pointer[1:].split("/")]
    assert tokens
    current = document
    for token in tokens[:-1]:
        if isinstance(current, dict):
            current = current[token]
        elif isinstance(current, list):
            current = current[int(token)]
        else:
            raise AssertionError(f"cannot traverse mutation pointer: {pointer}")
    return current, tokens[-1]


def apply_mutation(document: dict[str, Any], mutation: dict[str, Any]) -> None:
    parent, token = pointer_parent(document, mutation["pointer"])
    operation = mutation["operation"]
    if operation == "set":
        if isinstance(parent, dict):
            parent[token] = mutation["value"]
        elif isinstance(parent, list):
            parent[int(token)] = mutation["value"]
        else:
            raise AssertionError(f"set parent is not a container: {mutation}")
    elif operation == "remove":
        if isinstance(parent, dict):
            del parent[token]
        elif isinstance(parent, list):
            del parent[int(token)]
        else:
            raise AssertionError(f"remove parent is not a container: {mutation}")
    else:
        raise AssertionError(f"unknown mutation operation: {operation}")


def main() -> None:
    schema = load_json(SCHEMA_PATH)
    base = load_json(RUN_PATH)
    cases = load_json(CASES_PATH)
    packet = load_json(PACKET_PATH)
    assessment = load_json(ASSESSMENT_PATH)
    checks = 0

    assert schema["properties"]["schema_version"]["const"] == "0.1"
    assert schema["properties"]["gate_results"]["minItems"] == 8
    assert schema["properties"]["gate_results"]["maxItems"] == 8
    assert set(schema["$defs"]["gate_outcome"]["enum"]) == {
        "PASS",
        "FAIL",
        "BLOCKED",
        "INDETERMINATE",
    }
    assert schema["properties"]["outcome_model"]["properties"]["malformed_outcome"]["const"] == "INVALID"
    checks += 1

    packet_before = copy.deepcopy(packet)
    assessment_before = copy.deepcopy(assessment)
    positive = evaluate_gate_run(copy.deepcopy(base), packet, assessment)
    assert positive["valid"], positive["errors"]
    assert positive["computed_aggregate"] == "PASS"
    assert list(positive["gate_statuses"]) == GATE_IDS
    assert set(positive["gate_statuses"].values()) == {"PASS"}
    assert positive["source_packet_unchanged"] is True
    assert positive["receiver_assessment_unchanged"] is True
    assert packet == packet_before
    assert assessment == assessment_before
    checks += 1

    assert cases.get("base_fixture") == RUN_PATH.name
    case_list = cases.get("cases")
    assert isinstance(case_list, list) and case_list
    seen: set[str] = set()
    valid_aggregate_coverage = {"PASS"}
    for case in case_list:
        assert isinstance(case, dict)
        case_id = case["case_id"]
        assert case_id not in seen
        seen.add(case_id)
        candidate = copy.deepcopy(base)
        for mutation in case["mutations"]:
            apply_mutation(candidate, mutation)
        result = evaluate_gate_run(candidate, packet, assessment)
        assert result["valid"] is case["expected_valid"], (
            f"case {case_id} validity mismatch: {result['errors']}"
        )
        assert result["computed_aggregate"] == case["expected_aggregate"], (
            f"case {case_id} aggregate mismatch: {result}"
        )
        if result["valid"]:
            valid_aggregate_coverage.add(result["computed_aggregate"])
        else:
            assert result["errors"], f"invalid case {case_id} returned no errors"
        assert packet == packet_before
        assert assessment == assessment_before
        checks += 1

    assert valid_aggregate_coverage == {
        "PASS",
        "FAIL",
        "BLOCKED",
        "INDETERMINATE",
    }
    checks += 1

    source_tamper = copy.deepcopy(packet)
    source_tamper["claim"]["independence_scope"] = "receiver-strengthened source wording"
    result = evaluate_gate_run(copy.deepcopy(base), source_tamper, assessment)
    assert result["valid"] is False
    assert any("changed source independence wording" in error for error in result["errors"])
    checks += 1

    assessment_tamper = copy.deepcopy(assessment)
    assessment_tamper["source_wording"]["source_claim_status"] = "proved"
    result = evaluate_gate_run(copy.deepcopy(base), packet, assessment_tamper)
    assert result["valid"] is False
    assert any("digest mismatch" in error for error in result["errors"])
    assert any("changed source claim status" in error for error in result["errors"])
    checks += 1

    duplicate_ref = copy.deepcopy(base)
    duplicate_ref["gate_results"][0]["source_evidence_refs"].append("/integrity")
    result = evaluate_gate_run(duplicate_ref, packet, assessment)
    assert result["valid"] is False
    assert any("source_evidence_refs duplicates" in error for error in result["errors"])
    checks += 1

    fake_swap = copy.deepcopy(base)
    fake_swap["neutrality_control"]["label_permutation"]["left_after"] = "branch-A"
    result = evaluate_gate_run(fake_swap, packet, assessment)
    assert result["valid"] is False
    assert any("distinct exact swap" in error for error in result["errors"])
    checks += 1

    wrong_aggregate = copy.deepcopy(base)
    wrong_aggregate["declared_aggregate"] = "FAIL"
    result = evaluate_gate_run(wrong_aggregate, packet, assessment)
    assert result["valid"] is False
    assert any("declared aggregate" in error for error in result["errors"])
    checks += 1

    print(
        f"PASS: {checks}/{checks} Neutral Gate Run v0.1 groups; "
        f"{len(case_list)} table-driven cases"
    )


if __name__ == "__main__":
    main()
