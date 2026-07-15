"""Dependency-light semantic checks for Frozen-Packet Schema v0.1."""

from __future__ import annotations

import copy
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "packets" / "schema" / "frozen-packet-v0.1.schema.json"
FIXTURE_PATH = ROOT / "tests" / "fixtures" / "frozen-packet-valid.json"

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
    "claim",
    "verification",
    "alternatives",
    "residuals",
    "nonclaims",
    "interfaces",
    "integrity",
}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def nonempty_strings(value: object) -> bool:
    return isinstance(value, list) and bool(value) and all(
        isinstance(item, str) and bool(item.strip()) for item in value
    )


def validate(packet: dict[str, object]) -> list[str]:
    errors: list[str] = []
    require(set(packet) == TOP_LEVEL_REQUIRED, "top-level fields must match v0.1", errors)
    require(packet.get("schema_version") == "0.1", "schema_version must be 0.1", errors)
    require(packet.get("packet_status") == "SOURCE_FROZEN", "packet must be source-frozen", errors)
    require(bool(re.fullmatch(r"[A-Z][A-Z0-9_-]*-[0-9]{3,}", str(packet.get("packet_id", "")))), "packet_id is invalid", errors)

    source = packet.get("source")
    require(isinstance(source, dict), "source must be an object", errors)
    if isinstance(source, dict):
        source_required = {
            "repository", "revision", "source_packet_id", "artifact_paths",
            "issued_at", "claim_status", "evidence_grade",
        }
        require(set(source) == source_required, "source fields must match v0.1", errors)
        require(bool(re.fullmatch(r"[0-9a-f]{7,40}", str(source.get("revision", "")))), "source revision must be a Git hash", errors)
        require(nonempty_strings(source.get("artifact_paths")), "source artifacts must be nonempty", errors)
        for field in ("repository", "source_packet_id", "issued_at", "claim_status", "evidence_grade"):
            require(isinstance(source.get(field), str) and bool(source[field].strip()), f"source.{field} must be nonempty", errors)

    ownership = packet.get("ownership")
    require(isinstance(ownership, dict), "ownership must be an object", errors)
    if isinstance(ownership, dict):
        require(ownership.get("receiving_owner") == "possibility-to-capability", "receiving owner mismatch", errors)
        require(ownership.get("authority_transfer") is False, "source authority cannot transfer", errors)
        require(isinstance(ownership.get("source_owner"), str) and bool(ownership["source_owner"].strip()), "source owner missing", errors)

    require(nonempty_strings(packet.get("assumptions")), "assumptions must be explicit", errors)
    require(nonempty_strings(packet.get("quantifiers")), "quantifiers must be explicit", errors)
    require(nonempty_strings(packet.get("nonclaims")), "nonclaims must be explicit", errors)

    forks = packet.get("construction_forks")
    require(isinstance(forks, list) and bool(forks), "at least one construction fork is required", errors)
    if isinstance(forks, list):
        for index, fork in enumerate(forks):
            require(isinstance(fork, dict), f"construction fork {index} must be an object", errors)
            if isinstance(fork, dict):
                require(set(fork) == {"name", "selected", "alternatives", "transfer_status"}, f"construction fork {index} fields mismatch", errors)

    methods = packet.get("method_ledger")
    require(isinstance(methods, list) and bool(methods), "method ledger cannot be empty", errors)
    method_ids: list[str] = []
    results: list[str] = []
    if isinstance(methods, list):
        method_required = {"method_id", "label", "artifact_path", "artifact_revision", "result", "grade", "verification"}
        for index, method in enumerate(methods):
            require(isinstance(method, dict), f"method {index} must be an object", errors)
            if not isinstance(method, dict):
                continue
            require(set(method) == method_required, f"method {index} fields mismatch", errors)
            method_ids.append(str(method.get("method_id", "")))
            results.append(str(method.get("result", "")))
            require(bool(re.fullmatch(r"[0-9a-f]{7,40}", str(method.get("artifact_revision", "")))), f"method {index} revision invalid", errors)
            for field in method_required - {"artifact_revision"}:
                require(isinstance(method.get(field), str) and bool(method[field].strip()), f"method {index}.{field} must be nonempty", errors)
        require(len(method_ids) == len(set(method_ids)), "method ids must be unique", errors)

    claim = packet.get("claim")
    require(isinstance(claim, dict), "claim must be an object", errors)
    if isinstance(claim, dict):
        claim_required = {
            "statement", "scope", "independence_scope", "method_count",
            "convergence", "joint_argument_artifact", "source_status_unchanged",
        }
        require(set(claim) == claim_required, "claim fields must match v0.1", errors)
        require(claim.get("method_count") == len(method_ids), "claim method_count must match ledger", errors)
        require(claim.get("source_status_unchanged") is True, "packet must preserve source status", errors)
        require(isinstance(claim.get("joint_argument_artifact"), str) and bool(claim["joint_argument_artifact"].strip()), "joint argument artifact is required", errors)
        if claim.get("convergence") == "unanimous":
            require(bool(results) and len(set(results)) == 1, "unanimity requires identical method results", errors)

    integrity = packet.get("integrity")
    require(isinstance(integrity, dict), "integrity must be an object", errors)
    if isinstance(integrity, dict):
        require(integrity.get("hash_algorithm") == "sha256", "hash algorithm must be sha256", errors)
        require(nonempty_strings(integrity.get("hash_scope")), "hash scope must be explicit", errors)
        require(bool(re.fullmatch(r"[0-9a-f]{64}", str(integrity.get("digest", "")))), "sha256 digest invalid", errors)
        require(integrity.get("frozen") is True, "packet must be frozen", errors)

    return errors


def main() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    assert set(schema["required"]) == TOP_LEVEL_REQUIRED

    checks = 0
    assert validate(fixture) == []
    checks += 1

    cases: list[tuple[str, callable]] = [
        ("authority transfer", lambda p: p["ownership"].__setitem__("authority_transfer", True)),
        ("unfrozen", lambda p: p["integrity"].__setitem__("frozen", False)),
        ("bad source revision", lambda p: p["source"].__setitem__("revision", "mutable-main")),
        ("missing nonclaims", lambda p: p.__setitem__("nonclaims", [])),
        ("duplicate method", lambda p: p["method_ledger"][1].__setitem__("method_id", "M1")),
        ("method count", lambda p: p["claim"].__setitem__("method_count", 5)),
        ("false unanimity", lambda p: p["method_ledger"][1].__setitem__("result", "OTHER")),
        ("no joint argument", lambda p: p["claim"].__setitem__("joint_argument_artifact", "")),
        ("status upgrade", lambda p: p["claim"].__setitem__("source_status_unchanged", False)),
    ]

    for name, mutate in cases:
        candidate = copy.deepcopy(fixture)
        mutate(candidate)
        assert validate(candidate), f"adversarial case unexpectedly passed: {name}"
        checks += 1

    print(f"PASS: {checks}/10 frozen-packet contract checks")


if __name__ == "__main__":
    main()
