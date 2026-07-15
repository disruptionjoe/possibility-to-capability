"""Deterministic and adversarial checks for Frozen-Packet Contract v0.2."""

from __future__ import annotations

import copy
import hashlib
import json
import re
import shutil
import tempfile
import unicodedata
from pathlib import Path, PurePosixPath
from typing import Callable

from validate_frozen_packet_contract import validate as validate_v01


ROOT = Path(__file__).resolve().parents[1]
PACKET_SCHEMA_PATH = ROOT / "packets" / "schema" / "frozen-packet-v0.2.schema.json"
ASSESSMENT_SCHEMA_PATH = (
    ROOT / "packets" / "schema" / "receiving-independence-assessment-v0.2.schema.json"
)
PACKET_FIXTURE_PATH = ROOT / "tests" / "fixtures" / "frozen-packet-v0.2-valid.json"
ASSESSMENT_FIXTURE_PATH = (
    ROOT / "tests" / "fixtures" / "receiving-independence-v0.2-valid.json"
)
BUNDLE_ROOT = ROOT / "tests" / "fixtures" / "bundle-v0.2"
V01_FIXTURE_PATH = ROOT / "tests" / "fixtures" / "frozen-packet-valid.json"

HEX_64 = re.compile(r"[0-9a-f]{64}")
GIT_REVISION = re.compile(r"[0-9a-f]{7,40}")
PACKET_ID = re.compile(r"[A-Z][A-Z0-9_-]*-[0-9]{3,}")
ASSESSMENT_ID = re.compile(r"[A-Z][A-Z0-9_-]*-IA-[0-9]{3,}")
ZERO_DIGEST = "0" * 64
DOMAIN_SEPARATOR = b"ptc-frozen-bundle-v1\x00"

INDEPENDENCE_TYPES = {
    "proof_theoretic_independence",
    "model_relative_non_forcing",
    "transformation_class_invariance",
    "cohomological_nonselection",
    "fixed_point_nonselection",
    "internal_logic_nonselection",
    "inverse_variational_underdetermination",
    "empirical_underdetermination",
    "generic_underdetermination",
    "multi_method_convergence",
    "unknown_or_contested",
    "not_applicable",
}

TOP_LEVEL_REQUIRED = {
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


class DuplicateKeyError(ValueError):
    """Raised when JSON parsing would otherwise silently overwrite a key."""


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> dict[str, object]:
    value = json.loads(
        path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_keys
    )
    if not isinstance(value, dict):
        raise TypeError(f"expected object at {path}")
    return value


def canonical_json_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def sha256_hex(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def nonempty_strings(value: object) -> bool:
    return isinstance(value, list) and bool(value) and all(
        nonempty_string(item) for item in value
    )


def all_strings_are_nfc(value: object) -> bool:
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value) == value
    if isinstance(value, list):
        return all(all_strings_are_nfc(item) for item in value)
    if isinstance(value, dict):
        return all(
            all_strings_are_nfc(key) and all_strings_are_nfc(item)
            for key, item in value.items()
        )
    return True


def canonical_bundle_path(path: object) -> bool:
    if not nonempty_string(path):
        return False
    assert isinstance(path, str)
    if unicodedata.normalize("NFC", path) != path:
        return False
    if "\\" in path or ":" in path or any(ord(char) < 32 for char in path):
        return False
    candidate = PurePosixPath(path)
    if candidate.is_absolute() or str(candidate) != path:
        return False
    return all(part not in {"", ".", ".."} for part in candidate.parts)


def manifest_projection(packet: dict[str, object]) -> dict[str, object]:
    integrity = packet["integrity"]
    assert isinstance(integrity, dict)
    return {
        "canonicalization_profile": integrity["canonicalization_profile"],
        "entries": integrity["manifest"],
    }


def packet_digest_projection(packet: dict[str, object]) -> dict[str, object]:
    projection = copy.deepcopy(packet)
    integrity = projection["integrity"]
    assert isinstance(integrity, dict)
    integrity["packet_digest"] = ZERO_DIGEST
    integrity["bundle_digest"] = ZERO_DIGEST
    integrity["digest"] = ZERO_DIGEST
    return projection


def expected_digests(packet: dict[str, object]) -> tuple[str, str, str]:
    manifest_digest = sha256_hex(canonical_json_bytes(manifest_projection(packet)))
    working = copy.deepcopy(packet)
    integrity = working["integrity"]
    assert isinstance(integrity, dict)
    integrity["manifest_digest"] = manifest_digest
    packet_digest = sha256_hex(canonical_json_bytes(packet_digest_projection(working)))
    bundle_digest = sha256_hex(
        DOMAIN_SEPARATOR
        + bytes.fromhex(packet_digest)
        + bytes.fromhex(manifest_digest)
    )
    return manifest_digest, packet_digest, bundle_digest


def refresh_digests(packet: dict[str, object]) -> None:
    manifest_digest, packet_digest, bundle_digest = expected_digests(packet)
    integrity = packet["integrity"]
    assert isinstance(integrity, dict)
    integrity["manifest_digest"] = manifest_digest
    integrity["packet_digest"] = packet_digest
    integrity["bundle_digest"] = bundle_digest
    integrity["digest"] = bundle_digest


def validate_packet(
    packet: dict[str, object], bundle_root: Path | None = None
) -> list[str]:
    errors: list[str] = []
    require(set(packet) == TOP_LEVEL_REQUIRED, "top-level fields must match v0.2", errors)
    require(packet.get("schema_version") == "0.2", "schema_version must be 0.2", errors)
    require(
        packet.get("packet_status") == "SOURCE_FROZEN",
        "packet must be source-frozen",
        errors,
    )
    require(
        bool(PACKET_ID.fullmatch(str(packet.get("packet_id", "")))),
        "packet_id is invalid",
        errors,
    )
    require(all_strings_are_nfc(packet), "all packet strings must already be NFC", errors)

    source = packet.get("source")
    source_paths: list[str] = []
    require(isinstance(source, dict), "source must be an object", errors)
    if isinstance(source, dict):
        required = {
            "repository",
            "revision",
            "source_packet_id",
            "artifact_paths",
            "issued_at",
            "claim_status",
            "evidence_grade",
        }
        require(set(source) == required, "source fields must match v0.2", errors)
        require(
            bool(GIT_REVISION.fullmatch(str(source.get("revision", "")))),
            "source revision must be a Git hash",
            errors,
        )
        require(nonempty_strings(source.get("artifact_paths")), "source artifacts missing", errors)
        if isinstance(source.get("artifact_paths"), list):
            source_paths = [str(path) for path in source["artifact_paths"]]
            require(len(source_paths) == len(set(source_paths)), "source artifacts duplicate", errors)
        for field in (
            "repository",
            "source_packet_id",
            "issued_at",
            "claim_status",
            "evidence_grade",
        ):
            require(nonempty_string(source.get(field)), f"source.{field} must be nonempty", errors)

    ownership = packet.get("ownership")
    require(isinstance(ownership, dict), "ownership must be an object", errors)
    if isinstance(ownership, dict):
        require(
            set(ownership) == {"source_owner", "receiving_owner", "authority_transfer"},
            "ownership fields mismatch",
            errors,
        )
        require(nonempty_string(ownership.get("source_owner")), "source owner missing", errors)
        require(
            ownership.get("receiving_owner") == "possibility-to-capability",
            "receiving owner mismatch",
            errors,
        )
        require(ownership.get("authority_transfer") is False, "authority cannot transfer", errors)

    require(nonempty_strings(packet.get("assumptions")), "assumptions must be explicit", errors)
    require(nonempty_strings(packet.get("quantifiers")), "quantifiers must be explicit", errors)
    require(nonempty_strings(packet.get("nonclaims")), "nonclaims must be explicit", errors)

    forks = packet.get("construction_forks")
    require(isinstance(forks, list) and bool(forks), "construction forks missing", errors)
    if isinstance(forks, list):
        for index, fork in enumerate(forks):
            require(isinstance(fork, dict), f"construction fork {index} must be an object", errors)
            if isinstance(fork, dict):
                require(
                    set(fork) == {"name", "selected", "alternatives", "transfer_status"},
                    f"construction fork {index} fields mismatch",
                    errors,
                )

    methods = packet.get("method_ledger")
    method_ids: list[str] = []
    method_paths: list[str] = []
    method_premises: dict[str, set[str]] = {}
    results: list[str] = []
    require(isinstance(methods, list) and bool(methods), "method ledger cannot be empty", errors)
    if isinstance(methods, list):
        required = {
            "method_id",
            "label",
            "artifact_path",
            "artifact_revision",
            "result",
            "grade",
            "verification",
            "premise_ids",
        }
        for index, method in enumerate(methods):
            require(isinstance(method, dict), f"method {index} must be an object", errors)
            if not isinstance(method, dict):
                continue
            require(set(method) == required, f"method {index} fields mismatch", errors)
            method_id = str(method.get("method_id", ""))
            method_ids.append(method_id)
            method_paths.append(str(method.get("artifact_path", "")))
            results.append(str(method.get("result", "")))
            premise_ids = method.get("premise_ids")
            require(nonempty_strings(premise_ids), f"method {index} premises missing", errors)
            premise_values = [str(item) for item in premise_ids] if isinstance(premise_ids, list) else []
            require(
                len(premise_values) == len(set(premise_values)),
                f"method {index} premises duplicate",
                errors,
            )
            method_premises[method_id] = set(premise_values)
            require(
                bool(GIT_REVISION.fullmatch(str(method.get("artifact_revision", "")))),
                f"method {index} revision invalid",
                errors,
            )
            for field in required - {"artifact_revision", "premise_ids"}:
                require(nonempty_string(method.get(field)), f"method {index}.{field} missing", errors)
        require(len(method_ids) == len(set(method_ids)), "method ids must be unique", errors)

    evidence = packet.get("evidence_structure")
    premise_ids: list[str] = []
    premise_paths: list[str] = []
    premise_methods: dict[str, set[str]] = {}
    shared_ids: set[str] = set()
    require(isinstance(evidence, dict), "evidence_structure must be an object", errors)
    if isinstance(evidence, dict):
        required = {
            "premise_ledger",
            "method_dependency_edges",
            "shared_load_bearing_premise_ids",
            "raw_method_count",
            "raw_method_count_is_independence_count",
        }
        require(set(evidence) == required, "evidence_structure fields mismatch", errors)
        premises = evidence.get("premise_ledger")
        require(isinstance(premises, list) and bool(premises), "premise ledger cannot be empty", errors)
        if isinstance(premises, list):
            premise_required = {
                "premise_id",
                "exact_statement",
                "premise_type",
                "source_artifact_path",
                "load_bearing_for_method_ids",
                "source_status",
            }
            for index, premise in enumerate(premises):
                require(isinstance(premise, dict), f"premise {index} must be an object", errors)
                if not isinstance(premise, dict):
                    continue
                require(set(premise) == premise_required, f"premise {index} fields mismatch", errors)
                premise_id = str(premise.get("premise_id", ""))
                premise_ids.append(premise_id)
                premise_paths.append(str(premise.get("source_artifact_path", "")))
                load_bearing = premise.get("load_bearing_for_method_ids")
                require(nonempty_strings(load_bearing), f"premise {index} method map missing", errors)
                mapped = [str(item) for item in load_bearing] if isinstance(load_bearing, list) else []
                require(len(mapped) == len(set(mapped)), f"premise {index} method map duplicates", errors)
                premise_methods[premise_id] = set(mapped)
                require(nonempty_string(premise.get("exact_statement")), f"premise {index} statement missing", errors)
                require(nonempty_string(premise.get("source_artifact_path")), f"premise {index} artifact missing", errors)
                require(
                    premise.get("source_status")
                    in {"asserted_in_source", "conditional_in_source", "unknown_or_contested"},
                    f"premise {index} source status invalid",
                    errors,
                )
            require(len(premise_ids) == len(set(premise_ids)), "premise ids must be unique", errors)

        for method_id, references in method_premises.items():
            for premise_id in references:
                require(premise_id in premise_methods, f"method {method_id} references unknown premise {premise_id}", errors)
                if premise_id in premise_methods:
                    require(
                        method_id in premise_methods[premise_id],
                        f"premise map is asymmetric for {method_id}/{premise_id}",
                        errors,
                    )
        for premise_id, references in premise_methods.items():
            for method_id in references:
                require(method_id in method_premises, f"premise {premise_id} references unknown method {method_id}", errors)
                if method_id in method_premises:
                    require(
                        premise_id in method_premises[method_id],
                        f"premise map is asymmetric for {method_id}/{premise_id}",
                        errors,
                    )

        expected_shared = {
            premise_id for premise_id, references in premise_methods.items() if len(references) > 1
        }
        shared = evidence.get("shared_load_bearing_premise_ids")
        require(isinstance(shared, list), "shared premise ids must be a list", errors)
        shared_values = [str(item) for item in shared] if isinstance(shared, list) else []
        shared_ids = set(shared_values)
        require(len(shared_values) == len(shared_ids), "shared premise ids duplicate", errors)
        require(shared_ids == expected_shared, "shared premise ledger is not exact", errors)
        require(
            shared_values == sorted(shared_values, key=lambda item: item.encode("utf-8")),
            "shared premise ids must be UTF-8 sorted",
            errors,
        )

        edges = evidence.get("method_dependency_edges")
        require(isinstance(edges, list), "method dependency edges must be a list", errors)
        edge_keys: list[tuple[str, str, str]] = []
        if isinstance(edges, list):
            edge_required = {
                "dependent_method_id",
                "antecedent_method_id",
                "dependency_type",
                "exact_statement",
            }
            for index, edge in enumerate(edges):
                require(isinstance(edge, dict), f"dependency edge {index} must be an object", errors)
                if not isinstance(edge, dict):
                    continue
                require(set(edge) == edge_required, f"dependency edge {index} fields mismatch", errors)
                dependent = str(edge.get("dependent_method_id", ""))
                antecedent = str(edge.get("antecedent_method_id", ""))
                relation = str(edge.get("dependency_type", ""))
                require(dependent in method_ids, f"dependency edge {index} dependent method unknown", errors)
                require(antecedent in method_ids, f"dependency edge {index} antecedent method unknown", errors)
                require(dependent != antecedent, f"dependency edge {index} cannot be self-referential", errors)
                require(nonempty_string(edge.get("exact_statement")), f"dependency edge {index} statement missing", errors)
                edge_keys.append((dependent, antecedent, relation))
            require(len(edge_keys) == len(set(edge_keys)), "dependency edges duplicate", errors)

        require(
            evidence.get("raw_method_count") == len(method_ids),
            "raw method count must match the ledger",
            errors,
        )
        require(
            evidence.get("raw_method_count_is_independence_count") is False,
            "raw method count cannot be an independence count",
            errors,
        )

    claim = packet.get("claim")
    joint_path = ""
    require(isinstance(claim, dict), "claim must be an object", errors)
    if isinstance(claim, dict):
        required = {
            "statement",
            "scope",
            "independence_scope",
            "independence_type",
            "method_count",
            "convergence",
            "joint_argument_artifact",
            "source_status_unchanged",
        }
        require(set(claim) == required, "claim fields must match v0.2", errors)
        require(claim.get("method_count") == len(method_ids), "claim method count mismatch", errors)
        require(claim.get("source_status_unchanged") is True, "source status must remain unchanged", errors)
        require(claim.get("independence_type") in INDEPENDENCE_TYPES, "independence type invalid", errors)
        require(nonempty_string(claim.get("independence_scope")), "source independence wording missing", errors)
        joint_path = str(claim.get("joint_argument_artifact", ""))
        require(nonempty_string(joint_path), "joint argument artifact is required", errors)
        if claim.get("convergence") == "unanimous":
            require(bool(results) and len(set(results)) == 1, "unanimity requires identical results", errors)

    verification = packet.get("verification")
    verification_paths: list[str] = []
    require(isinstance(verification, dict), "verification must be an object", errors)
    if isinstance(verification, dict):
        require(set(verification) == {"artifacts", "replication_status"}, "verification fields mismatch", errors)
        require(nonempty_strings(verification.get("artifacts")), "verification artifacts missing", errors)
        if isinstance(verification.get("artifacts"), list):
            verification_paths = [str(path) for path in verification["artifacts"]]
        require(nonempty_string(verification.get("replication_status")), "replication status missing", errors)

    integrity = packet.get("integrity")
    manifest_paths: list[str] = []
    require(isinstance(integrity, dict), "integrity must be an object", errors)
    if isinstance(integrity, dict):
        required = {
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
        require(set(integrity) == required, "integrity fields must match v0.2", errors)
        require(integrity.get("hash_algorithm") == "sha256", "hash algorithm must be sha256", errors)
        require(
            integrity.get("canonicalization_profile") == "ptc-frozen-bundle-v1",
            "canonicalization profile mismatch",
            errors,
        )
        require(integrity.get("frozen") is True, "packet must be frozen", errors)
        manifest = integrity.get("manifest")
        require(isinstance(manifest, list) and bool(manifest), "manifest cannot be empty", errors)
        casefold_paths: list[str] = []
        if isinstance(manifest, list):
            for index, entry in enumerate(manifest):
                require(isinstance(entry, dict), f"manifest entry {index} must be an object", errors)
                if not isinstance(entry, dict):
                    continue
                require(
                    set(entry) == {"path", "byte_length", "content_sha256"},
                    f"manifest entry {index} fields mismatch",
                    errors,
                )
                path = str(entry.get("path", ""))
                manifest_paths.append(path)
                casefold_paths.append(path.casefold())
                require(canonical_bundle_path(path), f"manifest path is not canonical: {path}", errors)
                require(
                    isinstance(entry.get("byte_length"), int)
                    and not isinstance(entry.get("byte_length"), bool)
                    and entry["byte_length"] >= 0,
                    f"manifest entry {index} byte length invalid",
                    errors,
                )
                require(
                    bool(HEX_64.fullmatch(str(entry.get("content_sha256", "")))),
                    f"manifest entry {index} content digest invalid",
                    errors,
                )
            require(len(manifest_paths) == len(set(manifest_paths)), "manifest paths duplicate", errors)
            require(
                len(casefold_paths) == len(set(casefold_paths)),
                "manifest paths collide under case folding",
                errors,
            )
            require(
                manifest_paths == sorted(manifest_paths, key=lambda item: item.encode("utf-8")),
                "manifest paths must be UTF-8 sorted",
                errors,
            )

        require(
            integrity.get("hash_scope") == manifest_paths,
            "hash_scope must equal the canonical manifest path sequence",
            errors,
        )

        covered_paths = set(manifest_paths)
        required_paths = set(
            source_paths
            + method_paths
            + premise_paths
            + verification_paths
            + ([joint_path] if joint_path else [])
        )
        require(required_paths <= covered_paths, "referenced artifacts are missing from the manifest", errors)

        if all(key in integrity for key in required):
            manifest_digest, packet_digest, bundle_digest = expected_digests(packet)
            require(
                integrity.get("manifest_digest") == manifest_digest,
                "manifest digest mismatch",
                errors,
            )
            require(integrity.get("packet_digest") == packet_digest, "packet digest mismatch", errors)
            require(integrity.get("bundle_digest") == bundle_digest, "bundle digest mismatch", errors)
            require(integrity.get("digest") == bundle_digest, "digest alias must equal bundle digest", errors)

        if bundle_root is not None and isinstance(manifest, list):
            for index, entry in enumerate(manifest):
                if not isinstance(entry, dict) or not canonical_bundle_path(entry.get("path")):
                    continue
                path = bundle_root.joinpath(*PurePosixPath(str(entry["path"])).parts)
                require(path.is_file(), f"manifest blob missing: {entry['path']}", errors)
                if not path.is_file():
                    continue
                data = path.read_bytes()
                require(len(data) == entry.get("byte_length"), f"blob byte length mismatch: {entry['path']}", errors)
                require(sha256_hex(data) == entry.get("content_sha256"), f"blob digest mismatch: {entry['path']}", errors)

    return errors


def validate_assessment(
    assessment: dict[str, object], packet: dict[str, object]
) -> list[str]:
    errors: list[str] = []
    required = {
        "schema_version",
        "assessment_id",
        "assessment_status",
        "receiving_owner",
        "source_packet_ref",
        "source_wording",
        "classification",
        "guards",
        "nonclaims",
        "falsifiers",
    }
    require(set(assessment) == required, "assessment fields must match v0.2", errors)
    require(assessment.get("schema_version") == "0.2", "assessment schema version mismatch", errors)
    require(
        bool(ASSESSMENT_ID.fullmatch(str(assessment.get("assessment_id", "")))),
        "assessment id invalid",
        errors,
    )
    status = assessment.get("assessment_status")
    require(status in {"provisional", "unknown", "contested"}, "assessment status invalid", errors)
    require(
        assessment.get("receiving_owner") == "possibility-to-capability",
        "assessment receiving owner mismatch",
        errors,
    )
    require(all_strings_are_nfc(assessment), "all assessment strings must already be NFC", errors)

    packet_source = packet.get("source")
    packet_claim = packet.get("claim")
    packet_integrity = packet.get("integrity")
    packet_methods = packet.get("method_ledger")
    packet_evidence = packet.get("evidence_structure")
    assert isinstance(packet_source, dict)
    assert isinstance(packet_claim, dict)
    assert isinstance(packet_integrity, dict)
    assert isinstance(packet_methods, list)
    assert isinstance(packet_evidence, dict)

    reference = assessment.get("source_packet_ref")
    require(isinstance(reference, dict), "source packet reference must be an object", errors)
    if isinstance(reference, dict):
        require(
            set(reference) == {"packet_id", "packet_digest", "source_revision"},
            "source packet reference fields mismatch",
            errors,
        )
        require(reference.get("packet_id") == packet.get("packet_id"), "packet id reference mismatch", errors)
        require(
            reference.get("packet_digest") == packet_integrity.get("packet_digest"),
            "packet digest reference mismatch",
            errors,
        )
        require(
            reference.get("source_revision") == packet_source.get("revision"),
            "source revision reference mismatch",
            errors,
        )

    wording = assessment.get("source_wording")
    require(isinstance(wording, dict), "source wording must be an object", errors)
    if isinstance(wording, dict):
        require(
            set(wording)
            == {"exact_independence_scope", "source_independence_type", "source_claim_status"},
            "source wording fields mismatch",
            errors,
        )
        require(
            wording.get("exact_independence_scope") == packet_claim.get("independence_scope"),
            "source independence wording changed",
            errors,
        )
        require(
            wording.get("source_independence_type") == packet_claim.get("independence_type"),
            "source independence type changed",
            errors,
        )
        require(
            wording.get("source_claim_status") == packet_source.get("claim_status"),
            "source claim status changed",
            errors,
        )

    method_ids = {
        str(method.get("method_id", ""))
        for method in packet_methods
        if isinstance(method, dict)
    }
    premises = packet_evidence.get("premise_ledger")
    premise_ids = {
        str(premise.get("premise_id", ""))
        for premise in premises
        if isinstance(premises, list) and isinstance(premise, dict)
    }
    shared = packet_evidence.get("shared_load_bearing_premise_ids")
    shared_ids = set(str(item) for item in shared) if isinstance(shared, list) else set()

    classification = assessment.get("classification")
    require(isinstance(classification, dict), "classification must be an object", errors)
    if isinstance(classification, dict):
        require(
            set(classification)
            == {"independence_type", "basis_method_ids", "limiting_premise_ids", "rationale"},
            "classification fields mismatch",
            errors,
        )
        receiver_type = classification.get("independence_type")
        source_type = packet_claim.get("independence_type")
        require(receiver_type in INDEPENDENCE_TYPES, "receiving independence type invalid", errors)
        if status == "provisional":
            require(
                receiver_type in {source_type, "unknown_or_contested"},
                "receiving classification is stronger or different than source type",
                errors,
            )
            if source_type == "unknown_or_contested":
                require(
                    receiver_type == "unknown_or_contested",
                    "unknown source type cannot be upgraded",
                    errors,
                )
        else:
            require(
                receiver_type == "unknown_or_contested",
                "unknown or contested assessment must use unknown_or_contested",
                errors,
            )
        basis = classification.get("basis_method_ids")
        require(nonempty_strings(basis), "classification basis methods missing", errors)
        basis_ids = set(str(item) for item in basis) if isinstance(basis, list) else set()
        require(basis_ids <= method_ids, "classification references unknown method", errors)
        require(
            isinstance(basis, list) and len(basis) == len(basis_ids),
            "classification basis methods duplicate",
            errors,
        )
        limiting = classification.get("limiting_premise_ids")
        require(nonempty_strings(limiting), "limiting premises missing", errors)
        limiting_ids = set(str(item) for item in limiting) if isinstance(limiting, list) else set()
        require(limiting_ids <= premise_ids, "classification references unknown premise", errors)
        require(shared_ids <= limiting_ids, "shared load-bearing premises must remain limiting", errors)
        require(
            isinstance(limiting, list) and len(limiting) == len(limiting_ids),
            "limiting premises duplicate",
            errors,
        )
        require(nonempty_string(classification.get("rationale")), "classification rationale missing", errors)

    guards = assessment.get("guards")
    require(isinstance(guards, dict), "assessment guards must be an object", errors)
    if isinstance(guards, dict):
        require(
            set(guards)
            == {
                "source_wording_preserved",
                "source_status_unchanged",
                "authority_transfer",
                "no_strength_upgrade",
            },
            "assessment guard fields mismatch",
            errors,
        )
        require(guards.get("source_wording_preserved") is True, "source wording guard failed", errors)
        require(guards.get("source_status_unchanged") is True, "source status guard failed", errors)
        require(guards.get("authority_transfer") is False, "assessment cannot transfer authority", errors)
        require(guards.get("no_strength_upgrade") is True, "no-strength-upgrade guard failed", errors)

    require(nonempty_strings(assessment.get("nonclaims")), "assessment nonclaims missing", errors)
    require(nonempty_strings(assessment.get("falsifiers")), "assessment falsifiers missing", errors)
    return errors


def assert_packet_failure(
    fixture: dict[str, object],
    name: str,
    mutation: Callable[[dict[str, object]], None],
    expected_error: str,
    refresh: bool = True,
) -> None:
    candidate = copy.deepcopy(fixture)
    mutation(candidate)
    if refresh:
        refresh_digests(candidate)
    errors = validate_packet(candidate, BUNDLE_ROOT)
    assert any(expected_error in error for error in errors), (
        f"adversarial packet case did not trigger {expected_error!r}: {name}; errors={errors}"
    )


def assert_assessment_failure(
    fixture: dict[str, object],
    packet: dict[str, object],
    name: str,
    mutation: Callable[[dict[str, object]], None],
    expected_error: str,
) -> None:
    candidate = copy.deepcopy(fixture)
    mutation(candidate)
    errors = validate_assessment(candidate, packet)
    assert any(expected_error in error for error in errors), (
        f"adversarial assessment case did not trigger {expected_error!r}: {name}; errors={errors}"
    )


def main() -> None:
    packet_schema = load_json(PACKET_SCHEMA_PATH)
    assessment_schema = load_json(ASSESSMENT_SCHEMA_PATH)
    packet = load_json(PACKET_FIXTURE_PATH)
    assessment = load_json(ASSESSMENT_FIXTURE_PATH)
    v01_fixture = load_json(V01_FIXTURE_PATH)

    assert set(packet_schema["required"]) == TOP_LEVEL_REQUIRED
    assert packet_schema["properties"]["schema_version"]["const"] == "0.2"
    assert assessment_schema["properties"]["receiving_owner"]["const"] == "possibility-to-capability"
    assert set(packet_schema["$defs"]["independence_type"]["enum"]) == INDEPENDENCE_TYPES
    assert set(assessment_schema["$defs"]["independence_type"]["enum"]) == INDEPENDENCE_TYPES

    checks = 0
    assert validate_v01(v01_fixture) == []
    checks += 1
    assert validate_packet(packet, BUNDLE_ROOT) == []
    checks += 1
    assert validate_assessment(assessment, packet) == []
    checks += 1

    unknown = copy.deepcopy(assessment)
    unknown["assessment_status"] = "unknown"
    unknown["classification"]["independence_type"] = "unknown_or_contested"
    assert validate_assessment(unknown, packet) == []
    checks += 1

    contested = copy.deepcopy(assessment)
    contested["assessment_status"] = "contested"
    contested["classification"]["independence_type"] = "unknown_or_contested"
    assert validate_assessment(contested, packet) == []
    checks += 1

    packet_cases: list[
        tuple[str, Callable[[dict[str, object]], None], str, bool]
    ] = [
        (
            "path traversal",
            lambda p: p["integrity"]["manifest"][0].__setitem__("path", "../escape.txt"),
            "manifest path is not canonical",
            True,
        ),
        (
            "unsorted manifest",
            lambda p: (
                p["integrity"]["manifest"].__setitem__(
                    slice(None),
                    [p["integrity"]["manifest"][1], p["integrity"]["manifest"][0], p["integrity"]["manifest"][2]],
                ),
                p["integrity"].__setitem__(
                    "hash_scope",
                    ["artifacts/method-a.txt", "artifacts/joint-analysis.txt", "artifacts/method-b.txt"],
                ),
            ),
            "manifest paths must be UTF-8 sorted",
            True,
        ),
        (
            "case-fold collision",
            lambda p: p["integrity"]["manifest"].append(
                {
                    "path": "ARTIFACTS/method-a.txt",
                    "byte_length": 26,
                    "content_sha256": "2fde8b5092f64ed56b5856844ebd300e73ee89c402e2463e5f4823f2eecd767b",
                }
            ),
            "manifest paths collide under case folding",
            True,
        ),
        (
            "byte length",
            lambda p: p["integrity"]["manifest"][0].__setitem__("byte_length", 40),
            "blob byte length mismatch",
            True,
        ),
        (
            "content hash",
            lambda p: p["integrity"]["manifest"][0].__setitem__("content_sha256", "a" * 64),
            "blob digest mismatch",
            True,
        ),
        (
            "hash scope mismatch",
            lambda p: p["integrity"]["hash_scope"].pop(),
            "hash_scope must equal",
            True,
        ),
        (
            "uncovered method artifact",
            lambda p: p["method_ledger"][0].__setitem__("artifact_path", "artifacts/missing.txt"),
            "referenced artifacts are missing",
            True,
        ),
        (
            "raw count mismatch",
            lambda p: p["evidence_structure"].__setitem__("raw_method_count", 5),
            "raw method count must match",
            True,
        ),
        (
            "raw count promoted",
            lambda p: p["evidence_structure"].__setitem__("raw_method_count_is_independence_count", True),
            "raw method count cannot be",
            True,
        ),
        (
            "unknown premise",
            lambda p: p["method_ledger"][0]["premise_ids"].append("P9"),
            "references unknown premise",
            True,
        ),
        (
            "asymmetric premise map",
            lambda p: p["evidence_structure"]["premise_ledger"][0]["load_bearing_for_method_ids"].remove("M2"),
            "premise map is asymmetric",
            True,
        ),
        (
            "hidden shared premise",
            lambda p: p["evidence_structure"].__setitem__("shared_load_bearing_premise_ids", []),
            "shared premise ledger is not exact",
            True,
        ),
        (
            "unknown dependency endpoint",
            lambda p: p["evidence_structure"]["method_dependency_edges"][0].__setitem__("antecedent_method_id", "M9"),
            "antecedent method unknown",
            True,
        ),
        (
            "self dependency",
            lambda p: p["evidence_structure"]["method_dependency_edges"][0].__setitem__("antecedent_method_id", "M2"),
            "cannot be self-referential",
            True,
        ),
        (
            "false unanimity",
            lambda p: p["method_ledger"][1].__setitem__("result", "OTHER"),
            "unanimity requires identical",
            True,
        ),
        (
            "non-NFC packet string",
            lambda p: p["claim"].__setitem__("scope", "Cafe\u0301"),
            "strings must already be NFC",
            True,
        ),
        (
            "manifest digest tamper",
            lambda p: p["integrity"].__setitem__("manifest_digest", "a" * 64),
            "manifest digest mismatch",
            False,
        ),
        (
            "packet digest tamper",
            lambda p: p["claim"].__setitem__("statement", "tampered statement"),
            "packet digest mismatch",
            False,
        ),
        (
            "bundle digest tamper",
            lambda p: p["integrity"].__setitem__("bundle_digest", "a" * 64),
            "bundle digest mismatch",
            False,
        ),
        (
            "digest alias divergence",
            lambda p: p["integrity"].__setitem__("digest", "a" * 64),
            "digest alias must equal",
            False,
        ),
    ]

    for name, mutation, expected, refresh in packet_cases:
        assert_packet_failure(packet, name, mutation, expected, refresh)
        checks += 1

    with tempfile.TemporaryDirectory() as temporary:
        tampered_root = Path(temporary) / "bundle"
        shutil.copytree(BUNDLE_ROOT, tampered_root)
        target = tampered_root / "artifacts" / "method-a.txt"
        target.write_bytes(target.read_bytes() + b"tamper")
        errors = validate_packet(packet, tampered_root)
        assert any("blob byte length mismatch" in error for error in errors)
        assert any("blob digest mismatch" in error for error in errors)
        checks += 1

    assessment_cases: list[
        tuple[str, Callable[[dict[str, object]], None], str]
    ] = [
        (
            "source wording rewrite",
            lambda a: a["source_wording"].__setitem__("exact_independence_scope", "stronger wording"),
            "source independence wording changed",
        ),
        (
            "source type rewrite",
            lambda a: a["source_wording"].__setitem__("source_independence_type", "proof_theoretic_independence"),
            "source independence type changed",
        ),
        (
            "source status upgrade",
            lambda a: a["source_wording"].__setitem__("source_claim_status", "proved"),
            "source claim status changed",
        ),
        (
            "packet digest substitution",
            lambda a: a["source_packet_ref"].__setitem__("packet_digest", "a" * 64),
            "packet digest reference mismatch",
        ),
        (
            "stronger receiving type",
            lambda a: a["classification"].__setitem__("independence_type", "proof_theoretic_independence"),
            "stronger or different",
        ),
        (
            "unknown status with specific type",
            lambda a: a.__setitem__("assessment_status", "unknown"),
            "unknown or contested assessment",
        ),
        (
            "contested status with specific type",
            lambda a: a.__setitem__("assessment_status", "contested"),
            "unknown or contested assessment",
        ),
        (
            "unknown basis method",
            lambda a: a["classification"]["basis_method_ids"].append("M9"),
            "unknown method",
        ),
        (
            "unknown limiting premise",
            lambda a: a["classification"]["limiting_premise_ids"].append("P9"),
            "unknown premise",
        ),
        (
            "shared premise omitted",
            lambda a: a["classification"].__setitem__("limiting_premise_ids", ["P2"]),
            "shared load-bearing premises",
        ),
        (
            "status guard disabled",
            lambda a: a["guards"].__setitem__("source_status_unchanged", False),
            "source status guard failed",
        ),
        (
            "upgrade guard disabled",
            lambda a: a["guards"].__setitem__("no_strength_upgrade", False),
            "no-strength-upgrade guard failed",
        ),
    ]

    for name, mutation, expected in assessment_cases:
        assert_assessment_failure(assessment, packet, name, mutation, expected)
        checks += 1

    print(f"PASS: {checks}/{checks} Frozen-Packet Contract v0.2 checks")


if __name__ == "__main__":
    main()
