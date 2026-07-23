"""Reusable dependency-light capability diagnostic for Transition Diagnosis v0.1.

The classifier checks a receiver-owned witness record and computes a
provisional diagnostic outcome. It does not establish that the supplied
witnesses are true or that the hierarchy is universal.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path
from typing import Any


YES_NO = {"YES", "NO", "UNKNOWN", "CONTESTED"}
FAMILY_RELATIONS = {"SAME", "DIFFERENT", "INCOMPARABLE", "UNKNOWN", "CONTESTED"}
REPRESENTATION_RELATIONS = {"EQUIVALENT", "INEQUIVALENT", "UNKNOWN", "CONTESTED"}
TASK_RELATIONS = {"EQUAL", "SUPERSET", "SUBSET", "INCOMPARABLE", "UNKNOWN", "CONTESTED"}
FACTORIZATION = {"FACTORED", "NO_FACTOR_FOUND", "NOT_APPLICABLE", "UNKNOWN", "CONTESTED"}
ORDERING = {
    "ORDER_COMPATIBLE",
    "CO_OCCURRENT",
    "INCOMPARABLE",
    "CYCLIC",
    "UNREPRESENTABLE",
    "UNKNOWN",
    "CONTESTED",
}
ADMISSIBILITY = {"ADMISSIBLE", "INADMISSIBLE", "UNKNOWN", "CONTESTED"}
BRANCH_RELATIONS = {
    "SAME_OBJECT",
    "ALTERNATIVE_CONSTRUCTIONS",
    "INCOMPARABLE_CONSTRUCTIONS",
    "UNKNOWN",
    "CONTESTED",
}
GRADES = {"SYNTHETIC_CONTROL", "EXPLORATORY", "ARGUMENT", "COMPUTATION", "PROOF"}
VERIFICATIONS = {"UNVERIFIED", "DETERMINISTIC_SYNTHETIC", "REPLICATED", "CONTESTED"}

ELEMENTARY_OUTCOMES = {
    "FIXED_FAMILY_DISCLOSURE",
    "FIXED_FAMILY_DYNAMICS",
    "RECORD_FORMATION",
    "ACCESS_CHANGE",
    "POSSIBILITY_FAMILY_CHANGE",
    "CAPABILITY_ENLARGEMENT",
    "CAPABILITY_RESTRICTION",
    "FINALITY_CANDIDATE",
}
AGGREGATE_OUTCOMES = ELEMENTARY_OUTCOMES | {
    "NULL_NO_RELEVANT_CHANGE",
    "NULL_NO_ADMISSIBLE_CONSTRUCTION",
    "NULL_INADMISSIBLE_CONSTRUCTION",
    "MULTI_LEVEL",
    "INCOMPARABLE",
    "CONSTRUCTION_FORK",
    "UNKNOWN",
    "CONTESTED",
    "HIERARCHY_REVISION",
    "INVALID",
}
DECLARABLE_CLAIMS = ELEMENTARY_OUTCOMES | {
    "MULTI_LEVEL",
    "INCOMPARABLE",
    "HIERARCHY_REVISION",
}

WITNESS_FIELDS = {
    "possibility_family_relation": FAMILY_RELATIONS,
    "representation_relation": REPRESENTATION_RELATIONS,
    "description_change": YES_NO,
    "dynamics_change": YES_NO,
    "persistent_record": YES_NO,
    "access_change": YES_NO,
    "control_change": YES_NO,
    "raw_task_set_relation": TASK_RELATIONS,
    "normalized_task_set_relation": TASK_RELATIONS,
    "irreversible": YES_NO,
    "settlement": YES_NO,
    "preceding_layer_factorization": FACTORIZATION,
    "reopenable_by_admissible_continuation": YES_NO,
    "ordering_relation": ORDERING,
}

ASSESSMENT_FIELDS = {
    "schema_version",
    "assessment_id",
    "status",
    "question",
    "construction",
    "branch_relation",
    "branches",
    "label_neutrality",
    "assumptions",
    "evidence_grade",
    "tests",
    "falsifiers",
    "nonclaims",
    "reopening_conditions",
}
CONSTRUCTION_FIELDS = {"fork_identified", "selected_branch_id", "retention_statement"}
BRANCH_FIELDS = {
    "branch_id",
    "label",
    "admissibility",
    "witness",
    "normalization_frame",
    "factorization_search_scope",
    "declared_claims",
    "evidence_grade",
    "verification",
}
QUALIFIED_FIELDS = {"value", "evidence_refs"}
LABEL_FIELDS = {"left_label", "right_label", "required"}
ASSESSMENT_ID = re.compile(r"^[A-Z][A-Z0-9_-]*-TD-[0-9]{3,}$")
BRANCH_ID = re.compile(r"^[a-z][a-z0-9_-]*$")


def nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def nonempty_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(nonempty_string(item) for item in value)
        and len(value) == len(set(value))
    )


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return value


def witness_value(branch: dict[str, Any], field: str) -> str:
    value = branch["witness"][field]
    return value["value"]


def validate_qualified_witness(
    field: str, value: object, allowed: set[str], branch_id: str, errors: list[str]
) -> None:
    require(isinstance(value, dict), f"branch {branch_id} witness {field} must be an object", errors)
    if not isinstance(value, dict):
        return
    require(set(value) == QUALIFIED_FIELDS, f"branch {branch_id} witness {field} fields mismatch", errors)
    require(value.get("value") in allowed, f"branch {branch_id} witness {field} value invalid", errors)
    require(
        nonempty_strings(value.get("evidence_refs")),
        f"branch {branch_id} witness {field} needs unique evidence refs",
        errors,
    )


def validate_assessment(assessment: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    require(set(assessment) == ASSESSMENT_FIELDS, "assessment top-level fields mismatch", errors)
    require(assessment.get("schema_version") == "0.1", "schema_version must be 0.1", errors)
    require(bool(ASSESSMENT_ID.fullmatch(str(assessment.get("assessment_id", "")))), "assessment_id invalid", errors)
    require(assessment.get("status") == "provisional", "status must be provisional", errors)
    require(nonempty_string(assessment.get("question")), "question missing", errors)
    for field in ("assumptions", "tests", "falsifiers", "nonclaims", "reopening_conditions"):
        require(nonempty_strings(assessment.get(field)), f"{field} must be a nonempty unique string list", errors)
    require(assessment.get("evidence_grade") in GRADES, "evidence_grade invalid", errors)
    require(assessment.get("branch_relation") in BRANCH_RELATIONS, "branch_relation invalid", errors)

    construction = assessment.get("construction")
    require(isinstance(construction, dict), "construction must be an object", errors)
    if isinstance(construction, dict):
        require(set(construction) == CONSTRUCTION_FIELDS, "construction fields mismatch", errors)
        require(isinstance(construction.get("fork_identified"), bool), "fork_identified must be Boolean", errors)
        selected = construction.get("selected_branch_id")
        require(selected is None or nonempty_string(selected), "selected_branch_id must be string or null", errors)
        require(nonempty_string(construction.get("retention_statement")), "retention_statement missing", errors)

    neutrality = assessment.get("label_neutrality")
    require(isinstance(neutrality, dict), "label_neutrality must be an object", errors)
    if isinstance(neutrality, dict):
        require(set(neutrality) == LABEL_FIELDS, "label_neutrality fields mismatch", errors)
        require(nonempty_string(neutrality.get("left_label")), "left_label missing", errors)
        require(nonempty_string(neutrality.get("right_label")), "right_label missing", errors)
        require(neutrality.get("left_label") != neutrality.get("right_label"), "neutrality labels must differ", errors)
        require(neutrality.get("required") is True, "label neutrality must be required", errors)

    branches = assessment.get("branches")
    require(isinstance(branches, list) and bool(branches), "at least one branch is required", errors)
    seen: set[str] = set()
    if isinstance(branches, list):
        for index, branch in enumerate(branches):
            require(isinstance(branch, dict), f"branch {index} must be an object", errors)
            if not isinstance(branch, dict):
                continue
            branch_id = str(branch.get("branch_id", f"index-{index}"))
            require(set(branch) == BRANCH_FIELDS, f"branch {branch_id} fields mismatch", errors)
            require(bool(BRANCH_ID.fullmatch(branch_id)), f"branch {branch_id} id invalid", errors)
            require(branch_id not in seen, f"duplicate branch_id {branch_id}", errors)
            seen.add(branch_id)
            require(nonempty_string(branch.get("label")), f"branch {branch_id} label missing", errors)
            require(branch.get("admissibility") in ADMISSIBILITY, f"branch {branch_id} admissibility invalid", errors)
            require(branch.get("evidence_grade") in GRADES, f"branch {branch_id} evidence_grade invalid", errors)
            require(branch.get("verification") in VERIFICATIONS, f"branch {branch_id} verification invalid", errors)
            claims = branch.get("declared_claims")
            require(isinstance(claims, list), f"branch {branch_id} declared_claims must be an array", errors)
            if isinstance(claims, list):
                require(len(claims) == len(set(map(str, claims))), f"branch {branch_id} declared_claims duplicate", errors)
                require(all(claim in DECLARABLE_CLAIMS for claim in claims), f"branch {branch_id} declared_claim invalid", errors)
            witness = branch.get("witness")
            require(isinstance(witness, dict), f"branch {branch_id} witness must be an object", errors)
            if isinstance(witness, dict):
                require(set(witness) == set(WITNESS_FIELDS), f"branch {branch_id} witness fields mismatch", errors)
                for field, allowed in WITNESS_FIELDS.items():
                    validate_qualified_witness(field, witness.get(field), allowed, branch_id, errors)
                normalized = witness.get("normalized_task_set_relation")
                factorization = witness.get("preceding_layer_factorization")
                if isinstance(normalized, dict) and normalized.get("value") in {"EQUAL", "SUPERSET", "SUBSET", "INCOMPARABLE"}:
                    require(nonempty_string(branch.get("normalization_frame")), f"branch {branch_id} normalization_frame required", errors)
                if isinstance(factorization, dict) and factorization.get("value") == "NO_FACTOR_FOUND":
                    require(nonempty_string(branch.get("factorization_search_scope")), f"branch {branch_id} factorization search scope required", errors)

    if isinstance(construction, dict) and isinstance(branches, list):
        branch_ids = {branch.get("branch_id") for branch in branches if isinstance(branch, dict)}
        selected = construction.get("selected_branch_id")
        if selected is not None:
            require(selected in branch_ids, "selected_branch_id does not name a branch", errors)
        require(
            construction.get("fork_identified") is (len(branch_ids) > 1),
            "fork_identified must agree with branch count",
            errors,
        )
        if len(branch_ids) == 1:
            require(assessment.get("branch_relation") == "SAME_OBJECT", "single branch requires SAME_OBJECT", errors)
        elif assessment.get("branch_relation") == "SAME_OBJECT":
            errors.append("multiple branches cannot use SAME_OBJECT")
    return errors


def classify_branch(branch: dict[str, Any]) -> dict[str, Any]:
    branch_id = branch["branch_id"]
    admissibility = branch["admissibility"]
    values = {field: witness_value(branch, field) for field in WITNESS_FIELDS}
    components: list[str] = []
    alerts: list[str] = []

    if admissibility == "INADMISSIBLE":
        outcome = "NULL_INADMISSIBLE_CONSTRUCTION"
    elif admissibility == "UNKNOWN":
        outcome = "UNKNOWN"
    elif admissibility == "CONTESTED":
        outcome = "CONTESTED"
    elif values["ordering_relation"] in {"CYCLIC", "UNREPRESENTABLE"}:
        outcome = "HIERARCHY_REVISION"
        alerts.append("The declared relations cannot be represented by the provisional diagnostic hierarchy.")
    elif "CONTESTED" in values.values():
        outcome = "CONTESTED"
    else:
        if values["possibility_family_relation"] == "DIFFERENT":
            components.append("POSSIBILITY_FAMILY_CHANGE")
        if values["dynamics_change"] == "YES" and values["possibility_family_relation"] == "SAME":
            components.append("FIXED_FAMILY_DYNAMICS")
        elif values["dynamics_change"] == "YES":
            alerts.append("A dynamics change was supplied, but it was not inside an established fixed possibility family.")
        if values["persistent_record"] == "YES":
            components.append("RECORD_FORMATION")
        if values["access_change"] == "YES" or values["control_change"] == "YES":
            components.append("ACCESS_CHANGE")

        normalized = values["normalized_task_set_relation"]
        if normalized == "SUPERSET":
            components.append("CAPABILITY_ENLARGEMENT")
        elif normalized == "SUBSET":
            components.append("CAPABILITY_RESTRICTION")

        finality_witnessed = (
            values["settlement"] == "YES"
            and values["preceding_layer_factorization"] == "NO_FACTOR_FOUND"
            and values["reopenable_by_admissible_continuation"] == "NO"
        )
        if finality_witnessed:
            components.append("FINALITY_CANDIDATE")

        if values["irreversible"] == "YES" and not finality_witnessed:
            alerts.append("Irreversibility alone is not a finality witness.")
        if values["preceding_layer_factorization"] == "FACTORED" and "FINALITY_CANDIDATE" in branch["declared_claims"]:
            alerts.append("The declared finality claim factors through preceding layers.")
        if (
            values["raw_task_set_relation"] in {"SUPERSET", "SUBSET"}
            and normalized == "EQUAL"
            and any(
                claim in branch["declared_claims"]
                for claim in ("CAPABILITY_ENLARGEMENT", "CAPABILITY_RESTRICTION")
            )
        ):
            alerts.append("Raw task access changed, but normalized capability did not.")

        unknown_fields = [field for field, value in values.items() if value == "UNKNOWN"]
        if values["normalized_task_set_relation"] == "INCOMPARABLE":
            outcome = "INCOMPARABLE"
        elif values["ordering_relation"] == "INCOMPARABLE" and len(components) > 1:
            outcome = "INCOMPARABLE"
        elif not components and unknown_fields:
            outcome = "UNKNOWN"
        elif not components and (
            values["possibility_family_relation"] == "SAME"
            and values["representation_relation"] == "EQUIVALENT"
            and values["description_change"] == "YES"
        ):
            outcome = "FIXED_FAMILY_DISCLOSURE"
            components = [outcome]
        elif not components:
            outcome = "NULL_NO_RELEVANT_CHANGE"
        elif len(components) == 1:
            outcome = components[0]
        else:
            outcome = "MULTI_LEVEL"

    accepted_claims = set(components)
    if outcome in DECLARABLE_CLAIMS:
        accepted_claims.add(outcome)
    rejected = [claim for claim in branch["declared_claims"] if claim not in accepted_claims]
    return {
        "branch_id": branch_id,
        "outcome": outcome,
        "components": components,
        "alerts": alerts,
        "rejected_declared_claims": rejected,
    }


def aggregate_branches(branch_results: list[dict[str, Any]], branch_relation: str) -> str:
    if branch_relation == "CONTESTED":
        return "CONTESTED"
    if branch_relation == "UNKNOWN":
        return "UNKNOWN"
    outcomes = [result["outcome"] for result in branch_results]
    if not outcomes:
        return "INVALID"
    if all(outcome == "NULL_INADMISSIBLE_CONSTRUCTION" for outcome in outcomes):
        return "NULL_NO_ADMISSIBLE_CONSTRUCTION"
    if "HIERARCHY_REVISION" in outcomes:
        return "HIERARCHY_REVISION"
    admissible_outcomes = [outcome for outcome in outcomes if outcome != "NULL_INADMISSIBLE_CONSTRUCTION"]
    if not admissible_outcomes:
        return "NULL_NO_ADMISSIBLE_CONSTRUCTION"
    if "CONTESTED" in admissible_outcomes:
        return "CONTESTED"
    if "UNKNOWN" in admissible_outcomes:
        return "UNKNOWN"
    if len(set(admissible_outcomes)) == 1:
        return admissible_outcomes[0]
    if branch_relation == "INCOMPARABLE_CONSTRUCTIONS":
        return "INCOMPARABLE"
    return "CONSTRUCTION_FORK"


def semantic_summary(assessment: dict[str, Any]) -> tuple[str, tuple[tuple[str, tuple[str, ...]], ...]]:
    results = [classify_branch(branch) for branch in assessment["branches"]]
    aggregate = aggregate_branches(results, assessment["branch_relation"])
    branch_semantics = tuple(sorted((result["outcome"], tuple(result["components"])) for result in results))
    return aggregate, branch_semantics


def evaluate_assessment(assessment: dict[str, Any]) -> dict[str, Any]:
    errors = validate_assessment(assessment)
    if errors:
        return {
            "contract": "transition-diagnosis-v0.1",
            "assessment_id": assessment.get("assessment_id"),
            "valid": False,
            "aggregate_outcome": "INVALID",
            "branch_results": [],
            "label_invariance": {"tested": False, "invariant": False},
            "errors": errors,
            "nonclaim": "Invalidity says only that this record does not satisfy the provisional contract.",
        }

    branch_results = [classify_branch(branch) for branch in assessment["branches"]]
    aggregate = aggregate_branches(branch_results, assessment["branch_relation"])

    swapped = copy.deepcopy(assessment)
    labels = swapped["label_neutrality"]
    labels["left_label"], labels["right_label"] = labels["right_label"], labels["left_label"]
    for branch in swapped["branches"]:
        branch["label"] = f"swapped-label-{branch['branch_id']}"
    before = semantic_summary(assessment)
    after = semantic_summary(swapped)
    label_invariant = before == after

    return {
        "contract": "transition-diagnosis-v0.1",
        "assessment_id": assessment["assessment_id"],
        "valid": True,
        "aggregate_outcome": aggregate,
        "branch_relation": assessment["branch_relation"],
        "branch_results": branch_results,
        "label_invariance": {
            "tested": True,
            "invariant": label_invariant,
            "outcome_before": before[0],
            "outcome_after": after[0],
        },
        "errors": [] if label_invariant else ["classification changed under a pure label swap"],
        "nonclaim": "A classification is a provisional diagnosis of supplied witnesses, not evidence that the witnesses are true or that the hierarchy is universal.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog=(
            "A valid result classifies supplied witness statements provisionally; "
            "it does not verify their truth or establish universality."
        ),
    )
    parser.add_argument("assessment", type=Path)
    args = parser.parse_args()
    try:
        assessment = load_json(args.assessment)
        report = evaluate_assessment(assessment)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"valid": False, "aggregate_outcome": "INVALID", "errors": [str(error)]}, indent=2))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if report["valid"] and report["label_invariance"]["invariant"] else 1


if __name__ == "__main__":
    sys.exit(main())
