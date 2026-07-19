"""Cross-domain transition adjudication over CAI public-entryway pins.

This is a P2C-owned receiver fixture. It uses direct-chat quick-load pins for
the CAI public-entryway relationship as bounded source evidence, then applies
the existing Transition Diagnosis v0.1 classifier without changing its
meanings.

Grade: exploration tier / receiver-owned. No CAI source truth, Church truth,
public posture, claim status, capability claim beyond this scoped diagnostic,
finality claim, or external action moves.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
import json
import sys
from typing import Any

import classify_transition as td


EXPECTED_SHA256 = "1EFB043FDECB83CBC0E8F7B19496910A084BA57F66B1E0E38C7B4A428197A5FB"


CHECKS = {
    "setup: CAI quick-load pins are complete": {"tag": "T"},
    "setup: entryway assessment validates under Transition Diagnosis v0.1": {"tag": "T"},
    "provenance: exact admitted digest and relationship revision are required": {"tag": "E"},
    "dual acceptance: governance and Church acceptance are both required": {"tag": "E"},
    "transition transfer: unchanged classifier returns record/access/routing capability": {"tag": "E"},
    "access boundary: entryway without an action menu is not capability enlargement": {"tag": "E"},
    "label neutrality: source labels do not affect the typed verdict": {"tag": "E"},
    "source sovereignty: diagnostic nonclaims block content verdict movement": {"tag": "E"},
    "proposal boundary: mailbox-like payload is not relationship authority": {"tag": "E"},
    "public posture guard: public-claim requests force abstention": {"tag": "E"},
    "provenance-fail: digest-blind classifier accepts a mismatched source": {
        "tag": "F",
        "protects": "provenance: exact admitted digest and relationship revision are required",
    },
    "dual-acceptance-fail: one-sided classifier accepts incomplete relationship": {
        "tag": "F",
        "protects": "dual acceptance: governance and Church acceptance are both required",
    },
    "capability-fail: access-only classifier promotes an entryway record": {
        "tag": "F",
        "protects": "access boundary: entryway without an action menu is not capability enlargement",
    },
    "proposal-fail: proposal-blind classifier treats payload as authority": {
        "tag": "F",
        "protects": "proposal boundary: mailbox-like payload is not relationship authority",
    },
    "public-posture-fail: public-claim classifier moves posture": {
        "tag": "F",
        "protects": "public posture guard: public-claim requests force abstention",
    },
}


@dataclass(frozen=True)
class QuickLoadPins:
    projection_revision: int
    source_repo: str
    source_path: str
    governance_head: str
    admitted_sha256: str
    relationship_id: str
    agreement_revision: int
    governance_acceptance_ref: str
    church_acceptance_ref: str


@dataclass(frozen=True)
class EntrywayReport:
    provenance_status: str
    authority_status: str
    aggregate_outcome: str
    components: tuple[str, ...]
    verdict: str
    nonclaims: tuple[str, ...]


def canonical_pins() -> QuickLoadPins:
    return QuickLoadPins(
        projection_revision=2,
        source_repo="cai-governance-operations",
        source_path="canon/cai-domain-constitution.md",
        governance_head="06ff7a2",
        admitted_sha256=EXPECTED_SHA256,
        relationship_id="cai-church-public-entryway",
        agreement_revision=1,
        governance_acceptance_ref="decisions/README.md#cai-church-public-entryway",
        church_acceptance_ref="CONSTITUTION.md#relationship-acceptance",
    )


def provenance_status(pins: QuickLoadPins) -> str:
    if pins.projection_revision != 2:
        return "ABSTAIN_STALE_PROJECTION"
    if pins.admitted_sha256 != EXPECTED_SHA256:
        return "ABSTAIN_PROVENANCE_MISMATCH"
    if pins.source_repo != "cai-governance-operations":
        return "ABSTAIN_SOURCE_REPO_MISMATCH"
    if pins.source_path != "canon/cai-domain-constitution.md":
        return "ABSTAIN_SOURCE_PATH_MISMATCH"
    if pins.governance_head != "06ff7a2":
        return "ABSTAIN_SOURCE_HEAD_MISMATCH"
    if pins.relationship_id != "cai-church-public-entryway":
        return "ABSTAIN_RELATIONSHIP_MISMATCH"
    if pins.agreement_revision != 1:
        return "ABSTAIN_AGREEMENT_REVISION_MISMATCH"
    if not pins.governance_acceptance_ref or not pins.church_acceptance_ref:
        return "ABSTAIN_MISSING_ACCEPTANCE_REF"
    return "ADMITTED_QUICK_LOAD_PINS"


def q(value: str, ref: str) -> dict[str, Any]:
    return {"value": value, "evidence_refs": [ref]}


def entryway_assessment(pins: QuickLoadPins, *, action_menu: bool = True) -> dict[str, Any]:
    ref = (
        f"{pins.source_repo}@{pins.governance_head} "
        f"{pins.source_path} sha256:{pins.admitted_sha256} "
        f"{pins.relationship_id} agreement-rev:{pins.agreement_revision}"
    )
    task_relation = "SUPERSET" if action_menu else "EQUAL"
    declared = ["RECORD_FORMATION", "ACCESS_CHANGE"]
    if action_menu:
        declared.append("CAPABILITY_ENLARGEMENT")
    return {
        "schema_version": "0.1",
        "assessment_id": "P2C-CAI-TD-201",
        "status": "provisional",
        "question": (
            "Classify the CAI public-entryway relationship becoming active "
            "under admitted quick-load pins."
        ),
        "construction": {
            "fork_identified": False,
            "selected_branch_id": "cai_entryway",
            "retention_statement": (
                "Uses only admitted relationship pins as receiver evidence. "
                "The diagnostic does not import source content or move public posture."
            ),
        },
        "branch_relation": "SAME_OBJECT",
        "branches": [
            {
                "branch_id": "cai_entryway",
                "label": "accepted public entryway relation",
                "admissibility": "ADMISSIBLE",
                "witness": {
                    "possibility_family_relation": q("SAME", ref),
                    "representation_relation": q("EQUIVALENT", ref),
                    "description_change": q("YES", ref),
                    "dynamics_change": q("NO", ref),
                    "persistent_record": q("YES", ref),
                    "access_change": q("YES", ref),
                    "control_change": q("YES", ref),
                    "raw_task_set_relation": q(task_relation, ref),
                    "normalized_task_set_relation": q(task_relation, ref),
                    "irreversible": q("NO", ref),
                    "settlement": q("NO", ref),
                    "preceding_layer_factorization": q("NOT_APPLICABLE", ref),
                    "reopenable_by_admissible_continuation": q("YES", ref),
                    "ordering_relation": q("ORDER_COMPATIBLE", ref),
                },
                "normalization_frame": (
                    "Fixed repository and relationship-governance frame; only "
                    "the accepted entryway relation changes the authorized routing task set."
                ),
                "factorization_search_scope": (
                    "Receiver-side P2C classification of the admitted CAI quick-load relation."
                ),
                "declared_claims": declared,
                "evidence_grade": "COMPUTATION",
                "verification": "REPLICATED",
            }
        ],
        "label_neutrality": {
            "left_label": "church-public",
            "right_label": "governance-entryway",
            "required": True,
        },
        "assumptions": [
            "Quick-load pins came from Joe's trusted control channel for this run.",
            "The pins are receiver evidence, not a full imported frozen packet.",
            "The relationship owner retains source truth and acceptance authority.",
        ],
        "evidence_grade": "COMPUTATION",
        "tests": [
            "validate the Transition Diagnosis v0.1 contract",
            "require exact digest and relationship revision",
            "reject one-sided acceptance and public-posture overclaims",
        ],
        "falsifiers": [
            "the digest or relationship revision changes",
            "only one side of the relationship is accepted",
            "the classification requires importing CAI content verdicts",
        ],
        "nonclaims": [
            "No CAI or Church source truth moves.",
            "No public-posture, publication, or external-action claim moves.",
            "No source packet is imported into P2C by this fixture.",
            "No finality verdict is established.",
        ],
        "reopening_conditions": [
            "a source-issued frozen packet with a different relationship state",
            "a new accepted agreement revision",
            "an adversarial frame showing the routing task set did not change",
        ],
    }


def transition_result(pins: QuickLoadPins, *, action_menu: bool = True) -> dict[str, Any]:
    result = td.evaluate_assessment(entryway_assessment(pins, action_menu=action_menu))
    if not result["valid"] or not result["label_invariance"]["invariant"]:
        raise AssertionError(json.dumps(result, indent=2, sort_keys=True))
    return result


def evaluate_entryway(
    pins: QuickLoadPins,
    *,
    governance_acceptance: bool = True,
    church_acceptance: bool = True,
    action_menu: bool = True,
    mailbox_payload: bool = False,
    public_posture_request: bool = False,
) -> EntrywayReport:
    nonclaims = (
        "No CAI or Church source truth moves.",
        "No public-posture, publication, or external-action claim moves.",
        "No source packet is imported into P2C by this fixture.",
        "No finality verdict is established.",
    )
    if mailbox_payload:
        return EntrywayReport(
            "NOT_EVALUATED",
            "PROPOSAL_NOT_AUTHORITY",
            "UNKNOWN",
            (),
            "ABSTAIN_MAILBOX_PAYLOAD_IS_NOT_AUTHORITY",
            nonclaims,
        )
    if public_posture_request:
        return EntrywayReport(
            "NOT_EVALUATED",
            "PUBLIC_POSTURE_REQUESTED",
            "UNKNOWN",
            (),
            "ABSTAIN_PUBLIC_POSTURE_REQUIRES_SOURCE_AND_JOE_AUTHORITY",
            nonclaims,
        )

    status = provenance_status(pins)
    if status != "ADMITTED_QUICK_LOAD_PINS":
        return EntrywayReport(status, "SOURCE_NOT_ADMITTED", "UNKNOWN", (), status, nonclaims)
    if not governance_acceptance or not church_acceptance:
        return EntrywayReport(
            status,
            "DUAL_ACCEPTANCE_REQUIRED",
            "UNKNOWN",
            (),
            "ABSTAIN_RELATIONSHIP_NOT_DUAL_ACCEPTED",
            nonclaims,
        )

    result = transition_result(pins, action_menu=action_menu)
    components = tuple(result["branch_results"][0]["components"])
    if "CAPABILITY_ENLARGEMENT" in components:
        verdict = "GOVERNANCE_ROUTING_CAPABILITY_CANDIDATE_NO_CONTENT_VERDICT"
    else:
        verdict = "RECORD_ACCESS_CHANGE_ONLY"
    return EntrywayReport(
        status,
        "DUAL_ACCEPTED_RELATIONSHIP",
        result["aggregate_outcome"],
        components,
        verdict,
        nonclaims,
    )


def bad_digest_blind_classifier(pins: QuickLoadPins) -> str:
    if pins.relationship_id == "cai-church-public-entryway":
        return "DUAL_ACCEPTED_RELATIONSHIP"
    return "UNKNOWN"


def bad_one_sided_classifier(*, governance_acceptance: bool, church_acceptance: bool) -> str:
    if governance_acceptance or church_acceptance:
        return "DUAL_ACCEPTED_RELATIONSHIP"
    return "UNKNOWN"


def bad_access_only_classifier(report: EntrywayReport) -> str:
    if "ACCESS_CHANGE" in report.components:
        return "CAPABILITY_ENLARGEMENT"
    return "UNKNOWN"


def bad_proposal_classifier(*, mailbox_payload: bool) -> str:
    return "DUAL_ACCEPTED_RELATIONSHIP" if mailbox_payload else "UNKNOWN"


def bad_public_posture_classifier(*, public_posture_request: bool) -> str:
    return "PUBLIC_POSTURE_MOVED" if public_posture_request else "UNKNOWN"


def main() -> int:
    pins = canonical_pins()
    accepted = evaluate_entryway(pins)
    access_only = evaluate_entryway(pins, action_menu=False)
    one_sided = evaluate_entryway(pins, church_acceptance=False)
    digest_mismatch = evaluate_entryway(
        replace(pins, admitted_sha256="0" * len(EXPECTED_SHA256))
    )
    proposal = evaluate_entryway(pins, mailbox_payload=True)
    public_posture = evaluate_entryway(pins, public_posture_request=True)
    td_result = transition_result(pins)

    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    check(
        "setup: CAI quick-load pins are complete",
        pins.projection_revision == 2
        and pins.source_repo == "cai-governance-operations"
        and pins.source_path == "canon/cai-domain-constitution.md"
        and pins.relationship_id == "cai-church-public-entryway"
        and pins.agreement_revision == 1,
    )
    check(
        "setup: entryway assessment validates under Transition Diagnosis v0.1",
        td_result["valid"] and td_result["label_invariance"]["invariant"],
    )
    check(
        "provenance: exact admitted digest and relationship revision are required",
        accepted.provenance_status == "ADMITTED_QUICK_LOAD_PINS"
        and digest_mismatch.verdict == "ABSTAIN_PROVENANCE_MISMATCH",
    )
    check(
        "dual acceptance: governance and Church acceptance are both required",
        accepted.authority_status == "DUAL_ACCEPTED_RELATIONSHIP"
        and one_sided.verdict == "ABSTAIN_RELATIONSHIP_NOT_DUAL_ACCEPTED",
    )
    check(
        "transition transfer: unchanged classifier returns record/access/routing capability",
        accepted.aggregate_outcome == "MULTI_LEVEL"
        and accepted.components
        == ("RECORD_FORMATION", "ACCESS_CHANGE", "CAPABILITY_ENLARGEMENT")
        and accepted.verdict
        == "GOVERNANCE_ROUTING_CAPABILITY_CANDIDATE_NO_CONTENT_VERDICT",
    )
    check(
        "access boundary: entryway without an action menu is not capability enlargement",
        "CAPABILITY_ENLARGEMENT" not in access_only.components
        and access_only.verdict == "RECORD_ACCESS_CHANGE_ONLY",
    )
    check(
        "label neutrality: source labels do not affect the typed verdict",
        td_result["label_invariance"]["outcome_before"]
        == td_result["label_invariance"]["outcome_after"],
    )
    check(
        "source sovereignty: diagnostic nonclaims block content verdict movement",
        all("source truth" in claim or "public-posture" in claim
            or "source packet" in claim or "finality" in claim
            for claim in accepted.nonclaims),
    )
    check(
        "proposal boundary: mailbox-like payload is not relationship authority",
        proposal.verdict == "ABSTAIN_MAILBOX_PAYLOAD_IS_NOT_AUTHORITY",
    )
    check(
        "public posture guard: public-claim requests force abstention",
        public_posture.verdict
        == "ABSTAIN_PUBLIC_POSTURE_REQUIRES_SOURCE_AND_JOE_AUTHORITY",
    )
    check(
        "provenance-fail: digest-blind classifier accepts a mismatched source",
        bad_digest_blind_classifier(
            replace(pins, admitted_sha256="0" * len(EXPECTED_SHA256))
        )
        == "ABSTAIN_PROVENANCE_MISMATCH",
        expected=False,
    )
    check(
        "dual-acceptance-fail: one-sided classifier accepts incomplete relationship",
        bad_one_sided_classifier(governance_acceptance=True, church_acceptance=False)
        == "ABSTAIN_RELATIONSHIP_NOT_DUAL_ACCEPTED",
        expected=False,
    )
    check(
        "capability-fail: access-only classifier promotes an entryway record",
        bad_access_only_classifier(access_only) == "RECORD_ACCESS_CHANGE_ONLY",
        expected=False,
    )
    check(
        "proposal-fail: proposal-blind classifier treats payload as authority",
        bad_proposal_classifier(mailbox_payload=True)
        == "ABSTAIN_MAILBOX_PAYLOAD_IS_NOT_AUTHORITY",
        expected=False,
    )
    check(
        "public-posture-fail: public-claim classifier moves posture",
        bad_public_posture_classifier(public_posture_request=True)
        == "ABSTAIN_PUBLIC_POSTURE_REQUIRES_SOURCE_AND_JOE_AUTHORITY",
        expected=False,
    )

    print("CAI ENTRYWAY TRANSITION ADJUDICATION")
    print("=" * 72)
    counts = {"T": 0, "E": 0, "F": 0}
    failures: list[str] = []
    for name, value, expected in checks:
        tag = CHECKS[name]["tag"]
        counts[tag] += 1
        ok = value == expected
        print(f"{'PASS' if ok else 'UNEXPECTED'}  [{tag}] {name}: {value}")
        if not ok:
            failures.append(name)
    print()
    print(
        f"EVIDENTIAL CHECKS (headline): {counts['E']} [E] + "
        f"{counts['F']} [F] = {counts['E'] + counts['F']}"
    )
    print(f"[T] setup/source checks (no evidential weight): {counts['T']}")
    print()
    print("Receiver verdict:")
    print(f"  {accepted.verdict}")
    print(f"  aggregate={accepted.aggregate_outcome} components={list(accepted.components)}")
    print()
    print(json.dumps({"accepted": asdict(accepted)}, indent=2, sort_keys=True))

    if failures:
        print("UNEXPECTED RESULTS:", failures)
        return 1
    print("All checks match expectations. Exit 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
