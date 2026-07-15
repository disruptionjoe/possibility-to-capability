"""Real GU-001 blocked preflight and adversarial contract checks."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

from evaluate_blocked_intake_preflight import (
    DOWNSTREAM_GATES,
    V02_NESTED_FIELDS,
    evaluate_preflight,
)


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "interfaces" / "blocked-intake-preflight-v0.1.schema.json"
RECORD_PATH = ROOT / "packets" / "intake" / "GU-001-blocked-preflight-v0.1-2026-07-14.json"
CASES_PATH = ROOT / "tests" / "fixtures" / "blocked-intake-preflight-v0.1-cases.json"
V02_SCHEMA_PATH = ROOT / "packets" / "schema" / "frozen-packet-v0.2.schema.json"

EXPECTED_REVISION = "ec149a2feadb1f141f464d327b09e5ee213ac7f7"
EXPECTED_REGISTER = (
    "RESEARCH-STATUS.md",
    "5fca4fc8466b0f59f66cc10f92f45a1b114c8519",
    "exploration-tier; LOCATED-NOT-FORCED / GODEL-INDEPENDENT; verdict-stable",
)
EXPECTED_INVENTORY = {
    "explorations/W202-signature-crux-bach-branch-2026-07-14.md": "63916b61f880a6c0be8c659bce28aa7186c09491",
    "explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md": "6b67b2c068be3892ab3f05f567493f0476b2abc0",
    "explorations/W206-decisive-bit-counterfactual-invariance-2026-07-14.md": "b002b65de7030da1ac3903cee64b58b2aa905751",
    "explorations/W207-decisive-bit-brst-cohomology-2026-07-14.md": "9c0ca3f3f73201e10dd4cfa70b6f9abbf2dc9271",
    "explorations/W208-decisive-bit-lawvere-fixed-point-2026-07-14.md": "db743d22b73f1f3cd30891540e5a3b35eeebb265",
    "explorations/W209-decisive-bit-topos-internal-logic-2026-07-14.md": "63b3a0e18e2b4988acdf2abfe66334bb4d38549e",
    "explorations/W210-decisive-bit-helmholtz-inverse-variational-2026-07-14.md": "8a1f27386331cb34ba182d5bda304047150a2734",
    "explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md": "d404d0612f9c8fb7a51f0ffb7e8f9dca21c8a690",
}
EXPECTED_STATUS_GRADE = {
    "explorations/W202-signature-crux-bach-branch-2026-07-14.md": (
        "exploration",
        "exploration; strong on exact machine-checked signature/Krein facts; structural on the Bach reading",
    ),
    "explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md": (
        "exploration",
        "exploration; strong on the machine-checked coefficient pin and Krein consequence; structural on the branch-3 mapping",
    ),
    "explorations/W206-decisive-bit-counterfactual-invariance-2026-07-14.md": (
        "exploration",
        "exploration; strong on the decisive machine-checked linear algebra",
    ),
    "explorations/W207-decisive-bit-brst-cohomology-2026-07-14.md": (
        "exploration",
        "exact finite-dimensional group-cohomology facts; structural BRST lift; argued spectral-section identification",
    ),
    "explorations/W208-decisive-bit-lawvere-fixed-point-2026-07-14.md": (
        "exploration",
        "exploration; strong, with two decisive exact machine-checked linear-algebra facts and a structural GU lift",
    ),
    "explorations/W209-decisive-bit-topos-internal-logic-2026-07-14.md": (
        "no explicit status key; artifact_type is exploration and posture is exploration grade / conditional register",
        "exploration / conditional register; exact deterministic controls; structural / modelling site identification",
    ),
    "explorations/W210-decisive-bit-helmholtz-inverse-variational-2026-07-14.md": (
        "exploration",
        "exploration; strong on two exact machine-checked load-bearing facts; structural on the Helmholtz and stabilizer lift",
    ),
    "explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md": (
        "exploration synthesis",
        "exploration / synthesis; aggregates five machine-checked cores; structural on same-datum localization",
    ),
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict), f"JSON root must be an object: {path}"
    return value


def pointer_parent(document: object, pointer: str) -> tuple[object, str]:
    assert pointer.startswith("/")
    tokens = [token.replace("~1", "/").replace("~0", "~") for token in pointer[1:].split("/")]
    current = document
    for token in tokens[:-1]:
        current = current[int(token)] if isinstance(current, list) else current[token]
    return current, tokens[-1]


def apply_mutation(document: dict[str, Any], mutation: dict[str, Any]) -> None:
    parent, token = pointer_parent(document, mutation["pointer"])
    assert mutation["operation"] == "set"
    if isinstance(parent, list):
        parent[int(token)] = mutation["value"]
    else:
        parent[token] = mutation["value"]


def gu_snapshot_errors(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if record.get("source_observation", {}).get("immutable_revision") != EXPECTED_REVISION:
        errors.append("GU immutable revision changed")
    issuance = record.get("source_issuance", {})
    version_roles = (
        issuance.get("source_request_contract_version"),
        issuance.get("current_receiver_preferred_contract_version"),
        issuance.get("checked_contract_versions"),
    )
    if version_roles != ("0.1", "0.2", ["0.1", "0.2"]):
        errors.append("GU contract-version roles changed")
    observed_inventory = {
        item.get("path"): item.get("blob_oid")
        for item in record.get("tracked_source_inventory", [])
        if isinstance(item, dict)
    }
    if observed_inventory != EXPECTED_INVENTORY:
        errors.append("GU tracked source inventory changed")
    observed_status_grade = {
        item.get("path"): (item.get("source_status_class"), item.get("source_grade_class"))
        for item in record.get("tracked_source_inventory", [])
        if isinstance(item, dict)
    }
    if observed_status_grade != EXPECTED_STATUS_GRADE:
        errors.append("GU source grade ledger changed")
    status = record.get("source_status_preservation", {})
    register = (
        status.get("source_register_artifact"),
        status.get("source_register_blob_oid"),
        status.get("source_claim_register_status"),
    )
    if register != EXPECTED_REGISTER:
        errors.append("GU source claim-register status changed")
    residuals = {
        item.get("residual"): item.get("source_status")
        for item in status.get("named_residual_statuses", [])
        if isinstance(item, dict)
    }
    if residuals != {"bar (b)": "OPEN_UNCHANGED", "H59": "OPEN_UNCHANGED"}:
        errors.append("GU named residual status changed")
    return errors


def main() -> None:
    schema = load_json(SCHEMA_PATH)
    packet_schema = load_json(V02_SCHEMA_PATH)
    base = load_json(RECORD_PATH)
    cases = load_json(CASES_PATH)
    checks = 0

    assert schema["properties"]["schema_version"]["const"] == "0.1"
    assert schema["properties"]["source_issuance"]["properties"]["status"]["const"] == "ABSENT"
    assert schema["properties"]["downstream_gate_projection"]["minItems"] == 7
    assert schema["properties"]["downstream_gate_projection"]["maxItems"] == 7
    unblock = base["unblock_contract"]
    assert set(unblock["required_v0_2_root_fields"]) == set(packet_schema["required"])
    assert set(unblock["required_v0_2_integrity_fields"]) == set(
        packet_schema["properties"]["integrity"]["required"]
    )
    assert set(unblock["required_v0_2_method_fields"]) == set(
        packet_schema["properties"]["method_ledger"]["items"]["required"]
    )
    assert set(unblock["required_v0_2_nested_fields"]) == V02_NESTED_FIELDS
    checks += 1

    positive = evaluate_preflight(copy.deepcopy(base))
    assert positive["valid"], positive["errors"]
    assert positive["verdict"] == "NOT_YET_IMPORTABLE"
    assert not gu_snapshot_errors(base)
    assert [gate["gate"] for gate in base["downstream_gate_projection"]] == DOWNSTREAM_GATES
    assert {gate["outcome"] for gate in base["downstream_gate_projection"]} == {"BLOCKED"}
    assert {gate["execution_status"] for gate in base["downstream_gate_projection"]} == {"NOT_RUN"}
    checks += 1

    case_list = cases.get("cases")
    assert isinstance(case_list, list) and case_list
    seen: set[str] = set()
    for case in case_list:
        case_id = case["case_id"]
        assert case_id not in seen
        seen.add(case_id)
        candidate = copy.deepcopy(base)
        for mutation in case["mutations"]:
            apply_mutation(candidate, mutation)
        errors = evaluate_preflight(candidate)["errors"] + gu_snapshot_errors(candidate)
        assert errors, f"adversarial case passed: {case_id}"
        assert any(case["expected_error"] in error for error in errors), (
            f"case {case_id} missed expected error {case['expected_error']!r}: {errors}"
        )
        checks += 1

    assert {
        "artificial_source_completion",
        "source_request_rewritten_as_v0_2",
        "downstream_capability_pass_after_provenance_block",
        "source_status_upgrade",
        "source_grade_upgrade",
        "mutable_branch_reference",
        "untracked_roadmap_used",
        "fake_packet_digest",
        "receiver_reassembles_method_count",
    }.issubset(seen)
    checks += 1

    print(
        f"PASS: {checks}/{checks} Blocked Intake Preflight v0.1 groups; "
        f"{len(case_list)} adversarial cases"
    )


if __name__ == "__main__":
    main()
