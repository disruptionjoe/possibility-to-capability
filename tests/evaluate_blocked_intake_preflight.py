"""Dependency-light evaluator for Blocked Intake Preflight v0.1."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


SHA1 = re.compile(r"^[0-9a-f]{40}$")
TOP_LEVEL = {
    "schema_version",
    "preflight_id",
    "packet_candidate",
    "receiver_owner",
    "observed_at",
    "source_observation",
    "source_issuance",
    "tracked_source_inventory",
    "source_status_preservation",
    "method_evidence_boundary",
    "provenance_preflight",
    "admissibility",
    "downstream_gate_projection",
    "unblock_contract",
    "result",
}
DOWNSTREAM_GATES = [
    "construction",
    "formation",
    "completion_null",
    "capability",
    "finality",
    "no_artificial_success",
    "neutrality",
]
V02_ROOT_FIELDS = {
    "schema_version",
    "packet_id",
    "packet_status",
    "source",
    "question",
    "ownership",
    "construction_forks",
    "assumptions",
    "quantifiers",
    "method_ledger",
    "evidence_structure",
    "claim",
    "verification",
    "alternatives",
    "residuals",
    "nonclaims",
    "interfaces",
    "integrity",
}
V02_INTEGRITY_FIELDS = {
    "hash_algorithm",
    "canonicalization_profile",
    "hash_scope",
    "manifest",
    "manifest_digest",
    "packet_digest",
    "bundle_digest",
    "digest",
    "frozen",
}
V02_METHOD_FIELDS = {
    "method_id",
    "label",
    "artifact_path",
    "artifact_revision",
    "result",
    "grade",
    "verification",
    "premise_ids",
}
V02_NESTED_FIELDS = {
    "source.repository",
    "source.revision",
    "source.source_packet_id",
    "source.artifact_paths",
    "source.issued_at",
    "source.claim_status",
    "source.evidence_grade",
    "question.exact_question",
    "question.decision_type",
    "ownership.source_owner",
    "ownership.receiving_owner",
    "ownership.authority_transfer",
    "construction_forks[].name",
    "construction_forks[].selected",
    "construction_forks[].alternatives",
    "construction_forks[].transfer_status",
    "evidence_structure.premise_ledger",
    "evidence_structure.method_dependency_edges",
    "evidence_structure.shared_load_bearing_premise_ids",
    "evidence_structure.raw_method_count",
    "evidence_structure.raw_method_count_is_independence_count",
    "evidence_structure.premise_ledger[].premise_id",
    "evidence_structure.premise_ledger[].exact_statement",
    "evidence_structure.premise_ledger[].premise_type",
    "evidence_structure.premise_ledger[].source_artifact_path",
    "evidence_structure.premise_ledger[].load_bearing_for_method_ids",
    "evidence_structure.premise_ledger[].source_status",
    "evidence_structure.method_dependency_edges[].dependent_method_id",
    "evidence_structure.method_dependency_edges[].antecedent_method_id",
    "evidence_structure.method_dependency_edges[].dependency_type",
    "evidence_structure.method_dependency_edges[].exact_statement",
    "claim.statement",
    "claim.scope",
    "claim.independence_scope",
    "claim.independence_type",
    "claim.method_count",
    "claim.convergence",
    "claim.joint_argument_artifact",
    "claim.source_status_unchanged",
    "verification.artifacts",
    "verification.replication_status",
    "interfaces[].target_repository",
    "interfaces[].requested_datum",
    "interfaces[].ownership_status",
    "integrity.manifest[].path",
    "integrity.manifest[].byte_length",
    "integrity.manifest[].content_sha256",
}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def is_nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_nonempty_string_list(value: object) -> bool:
    return isinstance(value, list) and bool(value) and all(
        is_nonempty_string(item) for item in value
    )


def evaluate_preflight(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    require(set(record) == TOP_LEVEL, "top-level fields must match v0.1", errors)
    require(record.get("schema_version") == "0.1", "schema_version must be 0.1", errors)
    for field in ("preflight_id", "packet_candidate", "receiver_owner", "observed_at"):
        require(is_nonempty_string(record.get(field)), f"{field} must be nonempty", errors)

    source = record.get("source_observation")
    required_source = {
        "repository",
        "immutable_revision",
        "revision_kind",
        "inspection_mode",
        "working_tree_used",
        "untracked_files_used",
        "mutable_refs_used",
        "tree_queries",
    }
    require(isinstance(source, dict), "source_observation must be an object", errors)
    if isinstance(source, dict):
        require(set(source) == required_source, "source_observation fields mismatch", errors)
        require(
            bool(SHA1.fullmatch(str(source.get("immutable_revision", "")))),
            "source revision must be one immutable 40-character commit",
            errors,
        )
        require(source.get("revision_kind") == "git_commit", "revision kind must be git_commit", errors)
        require(
            source.get("inspection_mode") == "git_object_database_tracked_only",
            "inspection must use tracked Git objects only",
            errors,
        )
        require(source.get("working_tree_used") is False, "working tree use is forbidden", errors)
        require(source.get("untracked_files_used") is False, "untracked source use is forbidden", errors)
        require(source.get("mutable_refs_used") == [], "mutable refs are forbidden", errors)
        queries = source.get("tree_queries")
        require(isinstance(queries, list) and bool(queries), "tree queries are required", errors)
        if isinstance(queries, list):
            for query in queries:
                require(isinstance(query, dict), "tree query must be an object", errors)
                if isinstance(query, dict):
                    require(set(query) == {"query", "tracked_matches"}, "tree query fields mismatch", errors)
                    require(is_nonempty_string(query.get("query")), "tree query text missing", errors)
                    require(query.get("tracked_matches") == [], "absent issuance requires zero tracked matches", errors)

    issuance = record.get("source_issuance")
    issuance_fields = {
        "status",
        "source_request_contract_version",
        "current_receiver_preferred_contract_version",
        "checked_contract_versions",
        "source_issued_v0_1_present",
        "source_issued_v0_2_present",
        "source_packet_id",
        "source_packet_path",
        "manifest_path",
        "manifest_digest",
        "packet_digest",
        "bundle_digest",
        "claimed_digest_values",
    }
    require(isinstance(issuance, dict), "source_issuance must be an object", errors)
    if isinstance(issuance, dict):
        require(set(issuance) == issuance_fields, "source_issuance fields mismatch", errors)
        require(issuance.get("status") == "ABSENT", "blocked preflight requires absent source issuance", errors)
        checked_versions = issuance.get("checked_contract_versions")
        require(
            isinstance(checked_versions, list)
            and bool(checked_versions)
            and len(checked_versions) == len(set(checked_versions))
            and set(checked_versions).issubset({"0.1", "0.2"}),
            "checked contract versions must be a nonempty unique supported set",
            errors,
        )
        require(
            issuance.get("source_request_contract_version") in checked_versions
            if isinstance(checked_versions, list)
            else False,
            "source request contract version must be among checked versions",
            errors,
        )
        require(
            issuance.get("current_receiver_preferred_contract_version")
            in checked_versions
            if isinstance(checked_versions, list)
            else False,
            "receiver-preferred contract version must be among checked versions",
            errors,
        )
        require(issuance.get("source_issued_v0_1_present") is False, "v0.1 source packet cannot be present", errors)
        require(issuance.get("source_issued_v0_2_present") is False, "v0.2 source packet cannot be present", errors)
        for field in (
            "source_packet_id",
            "source_packet_path",
            "manifest_path",
            "manifest_digest",
            "packet_digest",
            "bundle_digest",
        ):
            require(issuance.get(field) is None, f"{field} must be null when issuance is absent", errors)
        require(issuance.get("claimed_digest_values") == [], "receiver-created or fake digests are forbidden", errors)

    inventory = record.get("tracked_source_inventory")
    require(isinstance(inventory, list) and bool(inventory), "tracked source inventory is required", errors)
    if isinstance(inventory, list):
        paths: list[object] = []
        for item in inventory:
            require(isinstance(item, dict), "inventory item must be an object", errors)
            if not isinstance(item, dict):
                continue
            expected = {
                "role",
                "path",
                "blob_oid",
                "artifact_type",
                "source_status_class",
                "source_grade_class",
                "preservation",
            }
            require(set(item) == expected, "inventory item fields mismatch", errors)
            paths.append(item.get("path"))
            for field in ("role", "path", "artifact_type", "source_status_class", "source_grade_class"):
                require(is_nonempty_string(item.get(field)), f"inventory {field} missing", errors)
            require(bool(SHA1.fullmatch(str(item.get("blob_oid", "")))), "inventory blob_oid invalid", errors)
            require(
                item.get("preservation") == "immutable_reference_no_receiver_regrade",
                "inventory must forbid receiver regrading",
                errors,
            )
        require(len(paths) == len(set(paths)), "inventory paths must be unique", errors)

    status = record.get("source_status_preservation")
    status_fields = {
        "source_register_artifact",
        "source_register_blob_oid",
        "source_claim_register_status",
        "named_residual_statuses",
        "source_status_upgraded",
        "receiver_claim_status_assigned",
        "source_wording_rewritten",
    }
    require(isinstance(status, dict), "source_status_preservation must be an object", errors)
    if isinstance(status, dict):
        require(set(status) == status_fields, "source status fields mismatch", errors)
        require(is_nonempty_string(status.get("source_register_artifact")), "source register missing", errors)
        require(bool(SHA1.fullmatch(str(status.get("source_register_blob_oid", "")))), "source register blob invalid", errors)
        require(is_nonempty_string(status.get("source_claim_register_status")), "source claim-register status missing", errors)
        residuals = status.get("named_residual_statuses")
        require(isinstance(residuals, list) and bool(residuals), "named residual statuses missing", errors)
        if isinstance(residuals, list):
            names: list[object] = []
            for item in residuals:
                require(isinstance(item, dict) and set(item) == {"residual", "source_status"}, "residual status fields mismatch", errors)
                if isinstance(item, dict):
                    names.append(item.get("residual"))
                    require(is_nonempty_string(item.get("residual")), "residual name missing", errors)
                    require(is_nonempty_string(item.get("source_status")), "residual source status missing", errors)
            require(len(names) == len(set(names)), "named residuals must be unique", errors)
        require(status.get("source_status_upgraded") is False, "source status upgrade is forbidden", errors)
        require(status.get("receiver_claim_status_assigned") is False, "receiver claim status is forbidden", errors)
        require(status.get("source_wording_rewritten") is False, "source wording rewrite is forbidden", errors)

    methods = record.get("method_evidence_boundary")
    require(isinstance(methods, dict), "method_evidence_boundary must be an object", errors)
    if isinstance(methods, dict):
        require(
            set(methods)
            == {
                "method_artifacts_observed",
                "source_issued_independence_structure_available",
                "receiver_method_count",
                "receiver_convergence_assessment",
                "receiver_reassembly_permitted",
            },
            "method boundary fields mismatch",
            errors,
        )
        require(isinstance(methods.get("method_artifacts_observed"), int), "observed method artifacts must be an integer", errors)
        require(methods.get("source_issued_independence_structure_available") is False, "source-issued independence cannot be available", errors)
        require(methods.get("receiver_method_count") is None, "receiver method count is inadmissible", errors)
        require(methods.get("receiver_convergence_assessment") == "NOT_RUN", "receiver convergence must be NOT_RUN", errors)
        require(methods.get("receiver_reassembly_permitted") is False, "receiver method reassembly is forbidden", errors)

    provenance = record.get("provenance_preflight")
    require(
        provenance
        == {
            "execution_status": "RUN",
            "outcome": "BLOCKED",
            "reason_code": "SOURCE_ISSUANCE_ABSENT",
            "judgment_owner": record.get("receiver_owner"),
        },
        "provenance preflight must run and block on absent source issuance",
        errors,
    )
    require(
        record.get("admissibility")
        == {
            "receiving_independence_assessment": "NOT_ADMISSIBLE",
            "full_gate_run": "NOT_ADMISSIBLE",
            "transition_diagnosis": "NOT_ADMISSIBLE",
        },
        "receiving assessment and downstream runs must be inadmissible",
        errors,
    )

    gates = record.get("downstream_gate_projection")
    require(isinstance(gates, list) and len(gates) == 7, "exactly seven downstream gates are required", errors)
    if isinstance(gates, list):
        require([gate.get("gate") for gate in gates if isinstance(gate, dict)] == DOWNSTREAM_GATES, "downstream gate order or membership mismatch", errors)
        for gate in gates:
            require(
                isinstance(gate, dict)
                and set(gate) == {"gate", "outcome", "execution_status", "blocked_by"},
                "downstream gate fields mismatch",
                errors,
            )
            if isinstance(gate, dict):
                require(gate.get("outcome") == "BLOCKED", f"{gate.get('gate')} must remain BLOCKED", errors)
                require(gate.get("execution_status") == "NOT_RUN", f"{gate.get('gate')} must remain NOT_RUN", errors)
                require(gate.get("blocked_by") == "provenance", f"{gate.get('gate')} must be blocked by provenance", errors)

    unblock = record.get("unblock_contract")
    require(isinstance(unblock, dict), "unblock_contract must be an object", errors)
    if isinstance(unblock, dict):
        require(
            set(unblock)
            == {
                "required_source_artifacts",
                "required_v0_2_root_fields",
                "required_v0_2_integrity_fields",
                "required_v0_2_method_fields",
                "required_v0_2_nested_fields",
                "next_receiver_steps",
            },
            "unblock contract fields mismatch",
            errors,
        )
        require(is_nonempty_string_list(unblock.get("required_source_artifacts")), "required source artifacts missing", errors)
        require(set(unblock.get("required_v0_2_root_fields", [])) == V02_ROOT_FIELDS, "v0.2 root-field unblock list is incomplete", errors)
        require(set(unblock.get("required_v0_2_integrity_fields", [])) == V02_INTEGRITY_FIELDS, "v0.2 integrity-field unblock list is incomplete", errors)
        require(set(unblock.get("required_v0_2_method_fields", [])) == V02_METHOD_FIELDS, "v0.2 method-field unblock list is incomplete", errors)
        require(set(unblock.get("required_v0_2_nested_fields", [])) == V02_NESTED_FIELDS, "v0.2 nested-field unblock list is incomplete", errors)
        require(is_nonempty_string_list(unblock.get("next_receiver_steps")), "next receiver steps missing", errors)

    result = record.get("result")
    require(isinstance(result, dict), "result must be an object", errors)
    if isinstance(result, dict):
        expected = {
            "verdict",
            "grade",
            "wrapper_absence_is_source_refutation",
            "source_result_assessed",
            "assumptions",
            "verification",
            "falsifiers",
            "nonclaims",
            "reopening_conditions",
        }
        require(set(result) == expected, "result fields mismatch", errors)
        require(result.get("verdict") == "NOT_YET_IMPORTABLE", "verdict must remain NOT_YET_IMPORTABLE", errors)
        require(is_nonempty_string(result.get("grade")), "result grade missing", errors)
        require(result.get("wrapper_absence_is_source_refutation") is False, "wrapper absence cannot refute the source", errors)
        require(result.get("source_result_assessed") is False, "source result cannot be assessed", errors)
        for field in ("assumptions", "verification", "falsifiers", "nonclaims", "reopening_conditions"):
            require(is_nonempty_string_list(result.get(field)), f"result {field} missing", errors)

    return {"valid": not errors, "errors": errors, "verdict": "INVALID" if errors else "NOT_YET_IMPORTABLE"}


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: evaluate_blocked_intake_preflight.py <record.json>")
    record = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if not isinstance(record, dict):
        raise SystemExit("preflight root must be a JSON object")
    outcome = evaluate_preflight(record)
    print(json.dumps(outcome, indent=2, sort_keys=True))
    raise SystemExit(0 if outcome["valid"] else 1)


if __name__ == "__main__":
    main()
