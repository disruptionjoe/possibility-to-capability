"""Cross-domain transition adjudication over the frozen TAF-001 packet.

This is a P2C-owned receiver fixture. It reads the imported TaF packet as
source-grounded evidence, then applies the existing Transition Diagnosis v0.1
classifier without changing its meanings.

Grade: exploration tier / receiver-owned. No source verdict, claim status,
capability claim, finality claim, or public posture moves.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import classify_transition as td


ROOT = Path(__file__).resolve().parents[1]
TAF001 = ROOT / "packets" / "imports" / "TAF-001"

CHECKS = {
    "source: TAF-001 imported packet and frozen output are present": {"tag": "T"},
    "alpha evidence: access edit creates tau2 and destroys tau5": {"tag": "E"},
    "beta evidence: formation edit creates tau3 with access fixed": {"tag": "E"},
    "alpha transfer: unchanged classifier returns ACCESS_CHANGE": {"tag": "E"},
    "beta transfer: unchanged classifier returns RECORD_FORMATION": {"tag": "E"},
    "task-delta quarantine: source-native reconstructibility is not promoted to capability": {"tag": "E"},
    "label neutrality: branch labels do not affect either verdict": {"tag": "E"},
    "source sovereignty: diagnostics remain receiver-owned nonclaims": {"tag": "E"},
    "alpha-fail: capability overclaim is NOT the accepted transfer verdict": {
        "tag": "F",
        "protects": "alpha transfer: unchanged classifier returns ACCESS_CHANGE",
    },
    "beta-fail: access relabeling is NOT the accepted transfer verdict": {
        "tag": "F",
        "protects": "beta transfer: unchanged classifier returns RECORD_FORMATION",
    },
    "finality-fail: irreversibility/settlement overclaim is rejected": {
        "tag": "F",
        "protects": "source sovereignty: diagnostics remain receiver-owned nonclaims",
    },
}


def load_text(*parts: str) -> str:
    return (TAF001.joinpath(*parts)).read_text(encoding="utf-8")


def q(value: str, ref: str) -> dict[str, Any]:
    return {"value": value, "evidence_refs": [ref]}


def base_witness(ref: str) -> dict[str, Any]:
    return {
        "possibility_family_relation": q("SAME", ref),
        "representation_relation": q("EQUIVALENT", ref),
        "description_change": q("YES", ref),
        "dynamics_change": q("NO", ref),
        "persistent_record": q("NO", ref),
        "access_change": q("NO", ref),
        "control_change": q("NO", ref),
        "raw_task_set_relation": q("INCOMPARABLE", ref),
        "normalized_task_set_relation": q("EQUAL", ref),
        "irreversible": q("NO", ref),
        "settlement": q("NO", ref),
        "preceding_layer_factorization": q("NOT_APPLICABLE", ref),
        "reopenable_by_admissible_continuation": q("YES", ref),
        "ordering_relation": q("ORDER_COMPATIBLE", ref),
    }


def branch(
    branch_id: str,
    label: str,
    witness: dict[str, Any],
    claims: list[str],
    frame: str,
) -> dict[str, Any]:
    return {
        "branch_id": branch_id,
        "label": label,
        "admissibility": "ADMISSIBLE",
        "witness": witness,
        "normalization_frame": frame,
        "factorization_search_scope": "TAF-001 finite W0 intervention class only",
        "declared_claims": claims,
        "evidence_grade": "COMPUTATION",
        "verification": "REPLICATED",
    }


def assessment(assessment_id: str, question: str, branch_obj: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "0.1",
        "assessment_id": assessment_id,
        "status": "provisional",
        "question": question,
        "construction": {
            "fork_identified": False,
            "selected_branch_id": branch_obj["branch_id"],
            "retention_statement": (
                "Uses TaF-native reconstructibility deltas as evidence while "
                "quarantining them from P2C capability unless the normalized "
                "task frame independently establishes capability change."
            ),
        },
        "branch_relation": "SAME_OBJECT",
        "branches": [branch_obj],
        "label_neutrality": {
            "left_label": "ordinary",
            "right_label": "impressive",
            "required": True,
        },
        "assumptions": [
            "TAF-001 remains source-owned and exploration-tier.",
            "P2C classification is receiver-owned and does not change source status.",
            "Source-native reconstructibility is not automatically P2C capability.",
        ],
        "evidence_grade": "COMPUTATION",
        "tests": [
            "validate the Transition Diagnosis v0.1 contract",
            "check label-swap invariance",
            "compare positive verdict against overclaim mutants",
        ],
        "falsifiers": [
            "requires changing the classifier meanings",
            "collapses source-native task reconstructibility into P2C capability",
            "attributes the receiver verdict to TaF",
        ],
        "nonclaims": [
            "No TaF claim status moves.",
            "No real-world distributed-system or market claim is established.",
            "No capability enlargement or finality verdict is established.",
        ],
        "reopening_conditions": [
            "a source packet with factor-vocabulary-aligned capability evidence",
            "an adversarial frame showing normalized capability was wrongly quarantined",
        ],
    }


def alpha_assessment() -> dict[str, Any]:
    ref = "TAF-001 facts 1 and 3"
    witness = base_witness(ref)
    witness["access_change"] = q("YES", ref)
    return assessment(
        "P2C-TD-101",
        "Classify TAF-001 ALPHA: enlarged holder access with record inventory fixed.",
        branch(
            "alpha",
            "TAF-001 ALPHA access edit",
            witness,
            ["ACCESS_CHANGE"],
            "Fixed TaF task vocabulary; source-native reconstructibility deltas are "
            "recorded but not promoted to P2C capability.",
        ),
    )


def beta_assessment() -> dict[str, Any]:
    ref = "TAF-001 facts 2 and 3"
    witness = base_witness(ref)
    witness["persistent_record"] = q("YES", ref)
    return assessment(
        "P2C-TD-102",
        "Classify TAF-001 BETA: new record formation under fixed holder access.",
        branch(
            "beta",
            "TAF-001 BETA formation edit",
            witness,
            ["RECORD_FORMATION"],
            "Fixed TaF task vocabulary; record formation is separated from access "
            "and capability by the receiver hierarchy.",
        ),
    )


def alpha_capability_mutant() -> dict[str, Any]:
    mutated = alpha_assessment()
    w = mutated["branches"][0]["witness"]
    w["normalized_task_set_relation"] = q("SUPERSET", "mutant overclaim control")
    mutated["branches"][0]["declared_claims"] = ["ACCESS_CHANGE", "CAPABILITY_ENLARGEMENT"]
    return mutated


def beta_access_mutant() -> dict[str, Any]:
    mutated = beta_assessment()
    w = mutated["branches"][0]["witness"]
    w["persistent_record"] = q("NO", "mutant relabel control")
    w["access_change"] = q("YES", "mutant relabel control")
    mutated["branches"][0]["declared_claims"] = ["ACCESS_CHANGE"]
    return mutated


def finality_mutant() -> dict[str, Any]:
    mutated = alpha_assessment()
    w = mutated["branches"][0]["witness"]
    w["irreversible"] = q("YES", "mutant finality control")
    w["settlement"] = q("YES", "mutant finality control")
    w["preceding_layer_factorization"] = q("FACTORED", "mutant finality control")
    w["reopenable_by_admissible_continuation"] = q("NO", "mutant finality control")
    mutated["branches"][0]["declared_claims"] = ["ACCESS_CHANGE", "FINALITY_CANDIDATE"]
    return mutated


def outcome(item: dict[str, Any]) -> dict[str, Any]:
    result = td.evaluate_assessment(item)
    if not result["valid"] or not result["label_invariance"]["invariant"]:
        raise AssertionError(json.dumps(result, indent=2, sort_keys=True))
    return result


def main() -> int:
    semantics = load_text("blobs", "taf001_semantics.md")
    output = load_text("blobs", "taf001_output.txt")
    packet = json.loads((TAF001 / "packet.json").read_text(encoding="utf-8"))

    results: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        results.append((name, bool(value), expected))

    check(
        "source: TAF-001 imported packet and frozen output are present",
        packet["packet_id"] == "TAF-001" and "W_A = (1, 1, 0, 0, 0)" in output,
    )
    check(
        "alpha evidence: access edit creates tau2 and destroys tau5",
        "ALPHA newly achievable: ['tau2']" in output
        and "ALPHA newly unachievable: ['tau5']" in output
        and "record inventory fixed" in semantics,
    )
    check(
        "beta evidence: formation edit creates tau3 with access fixed",
        "BETA  newly achievable: ['tau3']" in output
        and "BETA  newly unachievable: []" in output
        and "access set byte-identical" in semantics,
    )

    alpha = outcome(alpha_assessment())
    beta = outcome(beta_assessment())
    alpha_mutant = outcome(alpha_capability_mutant())
    beta_mutant = outcome(beta_access_mutant())
    finality = outcome(finality_mutant())

    check(
        "alpha transfer: unchanged classifier returns ACCESS_CHANGE",
        alpha["aggregate_outcome"] == "ACCESS_CHANGE"
        and alpha["branch_results"][0]["components"] == ["ACCESS_CHANGE"],
    )
    check(
        "beta transfer: unchanged classifier returns RECORD_FORMATION",
        beta["aggregate_outcome"] == "RECORD_FORMATION"
        and beta["branch_results"][0]["components"] == ["RECORD_FORMATION"],
    )
    check(
        "task-delta quarantine: source-native reconstructibility is not promoted to capability",
        "CAPABILITY_ENLARGEMENT" not in alpha["branch_results"][0]["components"]
        and "CAPABILITY_RESTRICTION" not in alpha["branch_results"][0]["components"]
        and alpha_mutant["aggregate_outcome"] == "MULTI_LEVEL",
    )
    check(
        "label neutrality: branch labels do not affect either verdict",
        alpha["label_invariance"]["invariant"] and beta["label_invariance"]["invariant"],
    )
    check(
        "source sovereignty: diagnostics remain receiver-owned nonclaims",
        "endorses no receiver-side conclusion" in semantics
        and "A classification is a provisional diagnosis" in alpha["nonclaim"]
        and finality["branch_results"][0]["rejected_declared_claims"] == ["FINALITY_CANDIDATE"],
    )
    check(
        "alpha-fail: capability overclaim is NOT the accepted transfer verdict",
        alpha["aggregate_outcome"] == alpha_mutant["aggregate_outcome"],
        expected=False,
    )
    check(
        "beta-fail: access relabeling is NOT the accepted transfer verdict",
        beta["aggregate_outcome"] == beta_mutant["aggregate_outcome"],
        expected=False,
    )
    check(
        "finality-fail: irreversibility/settlement overclaim is rejected",
        finality["branch_results"][0]["outcome"] == "FINALITY_CANDIDATE",
        expected=False,
    )

    print("CROSS-DOMAIN TRANSITION ADJUDICATION -- TAF-001 transfer")
    print("=" * 72)
    counts = {"T": 0, "E": 0, "F": 0}
    failures: list[str] = []
    for name, value, expected in results:
        tag = CHECKS[name]["tag"]
        counts[tag] += 1
        ok = value == expected
        print(f"{'PASS' if ok else 'UNEXPECTED'}  [{tag}] {name}: {value}")
        if not ok:
            failures.append(name)
    print(f"\nEVIDENTIAL CHECKS (headline): {counts['E']} [E] + {counts['F']} [F] = {counts['E'] + counts['F']}")
    print(f"[T] setup/source checks (no evidential weight): {counts['T']}")
    print("\nReceiver verdicts:")
    print(f"  ALPHA: {alpha['aggregate_outcome']} / {alpha['branch_results'][0]['components']}")
    print(f"  BETA:  {beta['aggregate_outcome']} / {beta['branch_results'][0]['components']}")
    print("\nNonclaim:")
    print(f"  {alpha['nonclaim']}")
    if failures:
        print("UNEXPECTED RESULTS:", failures)
        return 1
    print("All checks match expectations. Exit 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
