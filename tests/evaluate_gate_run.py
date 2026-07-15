"""Dependency-light semantic evaluator for Neutral Gate Run v0.1.

This evaluator checks contract consistency. It does not assess the scientific
sufficiency of evidence and cannot establish a physical result.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


GATE_IDS = [
    "provenance",
    "construction",
    "formation",
    "completion-null",
    "capability",
    "finality",
    "no-artificial-success",
    "neutrality",
]
GATE_OUTCOMES = {"PASS", "FAIL", "BLOCKED", "INDETERMINATE"}
RUN_ID = re.compile(r"^[A-Z][A-Z0-9_-]*-GR-[0-9]{3,}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
REVISION = re.compile(r"^[0-9a-f]{7,40}$")

TOP_LEVEL_FIELDS = {
    "schema_version",
    "run_id",
    "evaluation_status",
    "receiving_owner",
    "source_packet_ref",
    "receiver_assessment_ref",
    "source_preservation",
    "outcome_model",
    "one_chain_control",
    "neutrality_control",
    "gate_results",
    "declared_aggregate",
    "assumptions",
    "nonclaims",
    "reopening_conditions",
}
GATE_FIELDS = {
    "gate_id",
    "ordinal",
    "prerequisite_gate_ids",
    "status",
    "status_reason",
    "argument_chain_id",
    "construction_branch_id",
    "argument_ref",
    "source_evidence_refs",
    "receiver_assessment_refs",
    "receiver_judgment",
    "falsifiers",
    "nonclaims",
}


def canonical_json_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def sha256_json(value: object) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return value


def nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def nonempty_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(nonempty_string(item) for item in value)
    )


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def resolve_json_pointer(document: object, pointer: object) -> tuple[bool, object | None]:
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        return False, None
    current: object = document
    for raw_token in pointer[1:].split("/"):
        token = raw_token.replace("~1", "/").replace("~0", "~")
        if isinstance(current, dict):
            if token not in current:
                return False, None
            current = current[token]
        elif isinstance(current, list):
            if not token.isdigit():
                return False, None
            index = int(token)
            if index >= len(current):
                return False, None
            current = current[index]
        else:
            return False, None
    return True, current


def semantic_aggregate(gates: object) -> str:
    if not isinstance(gates, list) or len(gates) != len(GATE_IDS):
        return "INVALID"
    statuses = [
        gate.get("status") if isinstance(gate, dict) else None for gate in gates
    ]
    if any(status not in GATE_OUTCOMES for status in statuses):
        return "INVALID"
    if "FAIL" in statuses:
        return "FAIL"
    if "INDETERMINATE" in statuses:
        return "INDETERMINATE"
    if "BLOCKED" in statuses:
        return "BLOCKED"
    return "PASS" if all(status == "PASS" for status in statuses) else "INVALID"


def validate_source_boundary(
    run: dict[str, Any], packet: dict[str, Any], assessment: dict[str, Any]
) -> list[str]:
    errors: list[str] = []
    packet_integrity = packet.get("integrity")
    packet_source = packet.get("source")
    packet_ownership = packet.get("ownership")
    packet_claim = packet.get("claim")
    require(packet.get("schema_version") == "0.2", "source packet must be v0.2", errors)
    require(packet.get("packet_status") == "SOURCE_FROZEN", "source packet is not SOURCE_FROZEN", errors)
    require(isinstance(packet_integrity, dict), "source packet integrity missing", errors)
    require(isinstance(packet_source, dict), "source packet source block missing", errors)
    require(isinstance(packet_ownership, dict), "source packet ownership missing", errors)
    require(isinstance(packet_claim, dict), "source packet claim missing", errors)
    if isinstance(packet_integrity, dict):
        require(packet_integrity.get("frozen") is True, "source packet is not frozen", errors)
        require(
            bool(SHA256.fullmatch(str(packet_integrity.get("packet_digest", "")))),
            "source packet digest is invalid",
            errors,
        )
    if isinstance(packet_ownership, dict):
        require(packet_ownership.get("authority_transfer") is False, "source packet transfers authority", errors)
        require(
            packet_ownership.get("receiving_owner") == "possibility-to-capability",
            "source packet receiving owner mismatch",
            errors,
        )
    if isinstance(packet_claim, dict):
        require(packet_claim.get("source_status_unchanged") is True, "source packet status guard failed", errors)

    source_ref = run.get("source_packet_ref")
    require(isinstance(source_ref, dict), "source_packet_ref must be an object", errors)
    if isinstance(source_ref, dict):
        require(
            set(source_ref) == {"packet_id", "packet_digest", "source_revision"},
            "source_packet_ref fields mismatch",
            errors,
        )
        require(source_ref.get("packet_id") == packet.get("packet_id"), "source packet id mismatch", errors)
        if isinstance(packet_integrity, dict):
            require(
                source_ref.get("packet_digest") == packet_integrity.get("packet_digest"),
                "source packet digest reference mismatch",
                errors,
            )
        if isinstance(packet_source, dict):
            require(
                source_ref.get("source_revision") == packet_source.get("revision"),
                "source revision reference mismatch",
                errors,
            )
        require(bool(SHA256.fullmatch(str(source_ref.get("packet_digest", "")))), "source packet ref digest invalid", errors)
        require(bool(REVISION.fullmatch(str(source_ref.get("source_revision", "")))), "source revision ref invalid", errors)

    preservation = run.get("source_preservation")
    expected_preservation = {
        "source_packet_frozen": True,
        "source_content_modified": False,
        "source_status_unchanged": True,
        "authority_transfer": False,
    }
    require(preservation == expected_preservation, "source preservation guards mismatch", errors)

    require(assessment.get("schema_version") == "0.2", "receiving assessment must be v0.2", errors)
    require(
        assessment.get("receiving_owner") == "possibility-to-capability",
        "receiving assessment owner mismatch",
        errors,
    )
    assessment_ref = run.get("receiver_assessment_ref")
    require(isinstance(assessment_ref, dict), "receiver_assessment_ref must be an object", errors)
    if isinstance(assessment_ref, dict):
        require(
            set(assessment_ref) == {"assessment_id", "assessment_sha256"},
            "receiver_assessment_ref fields mismatch",
            errors,
        )
        require(
            assessment_ref.get("assessment_id") == assessment.get("assessment_id"),
            "receiving assessment id mismatch",
            errors,
        )
        require(
            assessment_ref.get("assessment_sha256") == sha256_json(assessment),
            "receiving assessment digest mismatch",
            errors,
        )

    assessment_source_ref = assessment.get("source_packet_ref")
    require(isinstance(assessment_source_ref, dict), "assessment source reference missing", errors)
    if isinstance(assessment_source_ref, dict) and isinstance(source_ref, dict):
        require(
            assessment_source_ref.get("packet_id") == source_ref.get("packet_id"),
            "assessment points to another packet id",
            errors,
        )
        require(
            assessment_source_ref.get("packet_digest") == source_ref.get("packet_digest"),
            "assessment points to another packet digest",
            errors,
        )
        require(
            assessment_source_ref.get("source_revision") == source_ref.get("source_revision"),
            "assessment points to another source revision",
            errors,
        )

    wording = assessment.get("source_wording")
    if isinstance(wording, dict) and isinstance(packet_claim, dict) and isinstance(packet_source, dict):
        require(
            wording.get("exact_independence_scope") == packet_claim.get("independence_scope"),
            "assessment changed source independence wording",
            errors,
        )
        require(
            wording.get("source_independence_type") == packet_claim.get("independence_type"),
            "assessment changed source independence type",
            errors,
        )
        require(
            wording.get("source_claim_status") == packet_source.get("claim_status"),
            "assessment changed source claim status",
            errors,
        )
    else:
        errors.append("assessment source wording missing")

    expected_guards = {
        "source_wording_preserved": True,
        "source_status_unchanged": True,
        "authority_transfer": False,
        "no_strength_upgrade": True,
    }
    require(assessment.get("guards") == expected_guards, "assessment guards mismatch", errors)
    return errors


def validate_gate_shape(
    gate: object,
    index: int,
    packet: dict[str, Any],
    assessment: dict[str, Any],
    errors: list[str],
) -> None:
    label = GATE_IDS[index]
    require(isinstance(gate, dict), f"gate {label} must be an object", errors)
    if not isinstance(gate, dict):
        return
    require(set(gate) == GATE_FIELDS, f"gate {label} fields mismatch", errors)
    require(gate.get("gate_id") == label, f"gate order mismatch at {index + 1}: expected {label}", errors)
    require(gate.get("ordinal") == index + 1, f"gate {label} ordinal mismatch", errors)
    require(
        gate.get("prerequisite_gate_ids") == GATE_IDS[:index],
        f"gate {label} prerequisites must be the exact preceding sequence",
        errors,
    )
    require(gate.get("status") in GATE_OUTCOMES, f"gate {label} status invalid", errors)
    for field in ("status_reason", "argument_chain_id", "construction_branch_id", "argument_ref"):
        require(nonempty_string(gate.get(field)), f"gate {label} {field} missing", errors)
    for field in ("source_evidence_refs", "receiver_assessment_refs", "falsifiers", "nonclaims"):
        require(nonempty_strings(gate.get(field)), f"gate {label} {field} missing", errors)
        values = gate.get(field)
        if isinstance(values, list):
            require(len(values) == len(set(map(str, values))), f"gate {label} {field} duplicates", errors)

    source_refs = gate.get("source_evidence_refs")
    if isinstance(source_refs, list):
        for pointer in source_refs:
            resolved, _ = resolve_json_pointer(packet, pointer)
            require(resolved, f"gate {label} unresolved source evidence pointer: {pointer}", errors)
    receiver_refs = gate.get("receiver_assessment_refs")
    if isinstance(receiver_refs, list):
        for pointer in receiver_refs:
            resolved, _ = resolve_json_pointer(assessment, pointer)
            require(resolved, f"gate {label} unresolved assessment pointer: {pointer}", errors)

    judgment = gate.get("receiver_judgment")
    require(isinstance(judgment, dict), f"gate {label} receiver judgment missing", errors)
    if isinstance(judgment, dict):
        require(
            set(judgment) == {"owner", "statement", "grade", "verification"},
            f"gate {label} receiver judgment fields mismatch",
            errors,
        )
        require(judgment.get("owner") == "possibility-to-capability", f"gate {label} judgment owner mismatch", errors)
        for field in ("statement", "grade", "verification"):
            require(nonempty_string(judgment.get(field)), f"gate {label} judgment {field} missing", errors)


def validate_gate_semantics(run: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    gates = run.get("gate_results")
    if not isinstance(gates, list) or len(gates) != len(GATE_IDS):
        return ["exactly eight gate results are required"]
    if not all(isinstance(gate, dict) for gate in gates):
        return ["every gate result must be an object"]

    statuses = [gate.get("status") for gate in gates]
    for index, gate in enumerate(gates):
        if any(statuses[prior] != "PASS" for prior in range(index)):
            require(
                gate.get("status") == "BLOCKED",
                f"gate {GATE_IDS[index]} must be BLOCKED because a prerequisite did not pass",
                errors,
            )

    control = run.get("one_chain_control")
    expected_control_fields = {
        "required_argument_chain_id",
        "required_construction_branch_id",
        "single_argument_ref",
    }
    require(isinstance(control, dict), "one_chain_control must be an object", errors)
    if isinstance(control, dict):
        require(set(control) == expected_control_fields, "one_chain_control fields mismatch", errors)
        for field in expected_control_fields:
            require(nonempty_string(control.get(field)), f"one_chain_control {field} missing", errors)

    first_six_pass = all(status == "PASS" for status in statuses[:6])
    if first_six_pass and isinstance(control, dict):
        one_chain = (
            {gate.get("argument_chain_id") for gate in gates[:6]}
            == {control.get("required_argument_chain_id")}
            and {gate.get("construction_branch_id") for gate in gates[:6]}
            == {control.get("required_construction_branch_id")}
            and {gate.get("argument_ref") for gate in gates[:6]}
            == {control.get("single_argument_ref")}
        )
        expected_no_artificial = "PASS" if one_chain else "FAIL"
        require(
            gates[6].get("status") == expected_no_artificial,
            f"no-artificial-success must be {expected_no_artificial} for the declared chain",
            errors,
        )
        if gates[6].get("status") == "PASS":
            require(
                gates[6].get("argument_chain_id") == control.get("required_argument_chain_id")
                and gates[6].get("construction_branch_id")
                == control.get("required_construction_branch_id")
                and gates[6].get("argument_ref") == control.get("single_argument_ref"),
                "no-artificial-success gate must itself remain on the declared chain",
                errors,
            )

    neutrality = run.get("neutrality_control")
    neutrality_fields = {
        "label_permutation",
        "verdict_before",
        "verdict_after",
        "label_invariant",
        "artifact_ref",
    }
    require(isinstance(neutrality, dict), "neutrality_control must be an object", errors)
    control_pass = False
    if isinstance(neutrality, dict):
        require(set(neutrality) == neutrality_fields, "neutrality_control fields mismatch", errors)
        permutation = neutrality.get("label_permutation")
        permutation_fields = {"left_before", "right_before", "left_after", "right_after"}
        require(isinstance(permutation, dict), "label_permutation must be an object", errors)
        swapped = False
        if isinstance(permutation, dict):
            require(set(permutation) == permutation_fields, "label_permutation fields mismatch", errors)
            for field in permutation_fields:
                require(nonempty_string(permutation.get(field)), f"label_permutation {field} missing", errors)
            distinct = permutation.get("left_before") != permutation.get("right_before")
            swapped = (
                distinct
                and permutation.get("left_after") == permutation.get("right_before")
                and permutation.get("right_after") == permutation.get("left_before")
            )
            require(swapped, "neutrality labels must be a distinct exact swap", errors)
        require(nonempty_string(neutrality.get("verdict_before")), "neutrality verdict_before missing", errors)
        require(nonempty_string(neutrality.get("verdict_after")), "neutrality verdict_after missing", errors)
        require(nonempty_string(neutrality.get("artifact_ref")), "neutrality artifact_ref missing", errors)
        verdict_equal = neutrality.get("verdict_before") == neutrality.get("verdict_after")
        require(
            neutrality.get("label_invariant") is verdict_equal,
            "label_invariant must equal verdict equality",
            errors,
        )
        control_pass = swapped and verdict_equal and neutrality.get("label_invariant") is True

    first_seven_pass = all(status == "PASS" for status in statuses[:7])
    if first_seven_pass:
        expected_neutrality = "PASS" if control_pass else "FAIL"
        require(
            gates[7].get("status") == expected_neutrality,
            f"neutrality must be {expected_neutrality} for the declared label control",
            errors,
        )
        if gates[7].get("status") == "PASS" and isinstance(control, dict):
            require(
                gates[7].get("argument_chain_id") == control.get("required_argument_chain_id")
                and gates[7].get("construction_branch_id")
                == control.get("required_construction_branch_id")
                and gates[7].get("argument_ref") == control.get("single_argument_ref"),
                "neutrality gate must itself remain on the declared chain",
                errors,
            )

    return errors


def evaluate_gate_run(
    run: dict[str, Any], packet: dict[str, Any], assessment: dict[str, Any]
) -> dict[str, Any]:
    packet_before = canonical_json_bytes(packet)
    assessment_before = canonical_json_bytes(assessment)
    errors: list[str] = []

    require(set(run) == TOP_LEVEL_FIELDS, "gate run top-level fields mismatch", errors)
    require(run.get("schema_version") == "0.1", "gate run schema version mismatch", errors)
    require(bool(RUN_ID.fullmatch(str(run.get("run_id", "")))), "gate run id invalid", errors)
    require(run.get("evaluation_status") == "provisional", "evaluation status must be provisional", errors)
    require(run.get("receiving_owner") == "possibility-to-capability", "receiving owner mismatch", errors)
    require(
        run.get("outcome_model")
        == {
            "gate_outcomes": ["PASS", "FAIL", "BLOCKED", "INDETERMINATE"],
            "malformed_outcome": "INVALID",
            "success_rule": "ALL_EIGHT_PASS_ONE_CHAIN_LABEL_INVARIANT",
        },
        "outcome model mismatch",
        errors,
    )
    for field in ("assumptions", "nonclaims", "reopening_conditions"):
        require(nonempty_strings(run.get(field)), f"gate run {field} missing", errors)

    errors.extend(validate_source_boundary(run, packet, assessment))

    gates = run.get("gate_results")
    require(isinstance(gates, list), "gate_results must be an array", errors)
    if isinstance(gates, list):
        require(len(gates) == len(GATE_IDS), "exactly eight gate results are required", errors)
        if len(gates) == len(GATE_IDS):
            for index, gate in enumerate(gates):
                validate_gate_shape(gate, index, packet, assessment, errors)
            errors.extend(validate_gate_semantics(run))

    aggregate = semantic_aggregate(gates)
    require(run.get("declared_aggregate") in GATE_OUTCOMES, "declared aggregate invalid", errors)
    require(run.get("declared_aggregate") == aggregate, "declared aggregate does not match computed aggregate", errors)

    source_unchanged = packet_before == canonical_json_bytes(packet)
    assessment_unchanged = assessment_before == canonical_json_bytes(assessment)
    require(source_unchanged, "evaluator mutated the source packet", errors)
    require(assessment_unchanged, "evaluator mutated the receiving assessment", errors)

    statuses = {
        gate.get("gate_id", f"index-{index}"): gate.get("status")
        for index, gate in enumerate(gates)
        if isinstance(gate, dict)
    } if isinstance(gates, list) else {}
    return {
        "contract": "neutral-gate-run-v0.1",
        "run_id": run.get("run_id"),
        "valid": not errors,
        "computed_aggregate": aggregate if not errors else "INVALID",
        "semantic_aggregate": aggregate,
        "gate_statuses": statuses,
        "source_packet_unchanged": source_unchanged,
        "receiver_assessment_unchanged": assessment_unchanged,
        "errors": errors,
        "nonclaim": "Contract validity does not establish any source claim, receiver judgment, or physical result.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("gate_run", type=Path)
    parser.add_argument("source_packet", type=Path)
    parser.add_argument("receiving_assessment", type=Path)
    args = parser.parse_args()
    try:
        report = evaluate_gate_run(
            load_json(args.gate_run),
            load_json(args.source_packet),
            load_json(args.receiving_assessment),
        )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"valid": False, "computed_aggregate": "INVALID", "errors": [str(error)]}, indent=2))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
