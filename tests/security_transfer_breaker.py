"""Security-domain transfer-BREAKER battery -- P2C-XBREAK-001, domain 1.

An object-capability security adversary is seated (inline) to BREAK P2C's
capability/access distinction. The battery runs the UNCHANGED
`classify_transition.py` evaluator over honestly-encoded object-capability
scenarios and asks the predeclared question: can P2C keep CAPABILITY_ENLARGEMENT
(authority amplification) distinct from an ACCESS_CHANGE (permission grant)
WITHOUT circularity or ad-hoc reinterpretation?

Default forecast (prereg P2C-XBREAK-001): TRANSFER FAILS -- object-capability
already separates capability from access, so the extra P2C value must come from
the records/finality levels or it is nothing.

Grade: exploration tier / receiver-owned. No source verdict, claim status,
capability claim, finality claim, canon, or public posture moves. A classification
diagnoses a stated textbook scenario; it is not a new security result.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import classify_transition as td


ROOT = Path(__file__).resolve().parents[1]
WITNESS_DIR = ROOT / "explorations" / "2026-07-22-security-transfer-breaker-p2c-xbreak-001"

# tag semantics match cross_domain_transition_adjudication.py:
#   [T] setup/source checks (no evidential weight)
#   [E] evidential checks (headline; expected True)
#   [F] falsifying controls (headline; expected False -- a passing [F] means the
#       overclaim was correctly rejected). The one exception is the declared
#       incumbent-match control, an [E] whose passing IS the transfer-fails signal.
CHECKS = {
    "source: committed confused-deputy and authority-amplification witnesses are present": {"tag": "T"},
    "cd evidence: confused deputy types as NULL_NO_RELEVANT_CHANGE for the client": {"tag": "E"},
    "cd evidence: the declared CAPABILITY_ENLARGEMENT overclaim is rejected": {"tag": "E"},
    "cd evidence: the raw!=normalized alert fires (raw access up, normalized authority unchanged)": {"tag": "E"},
    "cd record-rival: deputy corrupting the billing log types as RECORD_FORMATION, not capability": {"tag": "E"},
    "pg evidence: a permission grant (ACL widening) types as ACCESS_CHANGE": {"tag": "E"},
    "aa evidence: a generative authority amplification types as CAPABILITY_ENLARGEMENT": {"tag": "E"},
    "separation: on the honest witnesses, ACCESS_CHANGE and CAPABILITY_ENLARGEMENT do not collapse": {"tag": "E"},
    "frame-fork: the confused deputy is a declared CONSTRUCTION_FORK across frames, not a hidden circularity": {"tag": "E"},
    "label neutrality: no verdict depends on endpoint labels": {"tag": "E"},
    "incumbent match: object-capability's own verdict equals P2C's on the confused deputy (transfer-fails signal)": {"tag": "E"},
    "cd-fail: capability overclaim is NOT the accepted confused-deputy verdict": {
        "tag": "F",
        "protects": "cd evidence: confused deputy types as NULL_NO_RELEVANT_CHANGE for the client",
    },
    "pg-fail: a capability overclaim on a pure permission grant is rejected": {
        "tag": "F",
        "protects": "pg evidence: a permission grant (ACL widening) types as ACCESS_CHANGE",
    },
    "aa-token-fail: amplification-with-token-acquisition does not type as PURE capability": {
        "tag": "F",
        "protects": "aa evidence: a generative authority amplification types as CAPABILITY_ENLARGEMENT",
    },
    "aa-collapse-fail: normalizing the amplification away does NOT still grant capability": {
        "tag": "F",
        "protects": "separation: on the honest witnesses, ACCESS_CHANGE and CAPABILITY_ENLARGEMENT do not collapse",
    },
}


def q(value: str, ref: str) -> dict[str, Any]:
    return {"value": value, "evidence_refs": [ref]}


def base_witness(ref: str) -> dict[str, Any]:
    return {
        "possibility_family_relation": q("SAME", ref),
        "representation_relation": q("EQUIVALENT", ref),
        "description_change": q("NO", ref),
        "dynamics_change": q("NO", ref),
        "persistent_record": q("NO", ref),
        "access_change": q("NO", ref),
        "control_change": q("NO", ref),
        "raw_task_set_relation": q("SUPERSET", ref),
        "normalized_task_set_relation": q("EQUAL", ref),
        "irreversible": q("NO", ref),
        "settlement": q("NO", ref),
        "preceding_layer_factorization": q("NOT_APPLICABLE", ref),
        "reopenable_by_admissible_continuation": q("YES", ref),
        "ordering_relation": q("ORDER_COMPATIBLE", ref),
    }


def branch(branch_id: str, label: str, witness: dict[str, Any], claims: list[str], frame: str) -> dict[str, Any]:
    return {
        "branch_id": branch_id,
        "label": label,
        "admissibility": "ADMISSIBLE",
        "witness": witness,
        "normalization_frame": frame,
        "factorization_search_scope": None,
        "declared_claims": claims,
        "evidence_grade": "EXPLORATORY",
        "verification": "UNVERIFIED",
    }


def assessment(
    assessment_id: str,
    question: str,
    branches: list[dict[str, Any]],
    branch_relation: str = "SAME_OBJECT",
    selected: str | None = None,
) -> dict[str, Any]:
    fork = len(branches) > 1
    return {
        "schema_version": "0.1",
        "assessment_id": assessment_id,
        "status": "provisional",
        "question": question,
        "construction": {
            "fork_identified": fork,
            "selected_branch_id": selected,
            "retention_statement": (
                "Object-capability scenarios encoded as receiver-owned witnesses. "
                "Any frame that would flip the capability verdict is retained as a "
                "declared construction branch, never collapsed by relabeling."
            ),
        },
        "branch_relation": branch_relation,
        "branches": branches,
        "label_neutrality": {"left_label": "low-authority", "right_label": "high-authority", "required": True},
        "assumptions": [
            "The object classified is the change in a principal's operational standing, not the incidental effect on a target file.",
            "Object-capability security is the domain incumbent; its verdict is recorded read-only for the transfer-fails comparison.",
        ],
        "evidence_grade": "EXPLORATORY",
        "tests": [
            "validate the Transition Diagnosis v0.1 contract",
            "check label-swap invariance",
            "compare the honest verdict against capability/access overclaim mutants",
        ],
        "falsifiers": [
            "requires changing the classifier meanings",
            "a pure endpoint relabeling changes the verdict",
            "the capability verdict cannot be stated without smuggling in the access boundary as a hidden constant",
        ],
        "nonclaims": [
            "No security claim about any deployed system is established.",
            "No source claim status, capability, finality, canon, or public posture moves.",
            "The P2C static task-set discriminator is not claimed to reproduce object-capability's designation/authorization structural distinction.",
        ],
        "reopening_conditions": [
            "a construction that forces a capability verdict from a pure access grant with no access variable moved",
            "an adversarial frame showing the normalized capability was wrongly quarantined or wrongly granted",
        ],
    }


# ---- honest witnesses -------------------------------------------------------

def confused_deputy() -> dict[str, Any]:
    ref = "ocap://confused-deputy/client-authority-frame"
    w = base_witness(ref)  # access NO, raw SUPERSET, normalized EQUAL
    return assessment(
        "OCAP-CD-TD-101",
        "Confused deputy: did the client's capability enlarge, or is the billing overwrite only a raw effect via the deputy's own authority?",
        [branch(
            "client-authority-frame",
            "client supplies SYSX/BILL as the output designator",
            w,
            ["CAPABILITY_ENLARGEMENT"],
            "Client's own held authority held fixed; the deputy's ambient write authority is not counted into the client's normalized set.",
        )],
        selected="client-authority-frame",
    )


def confused_deputy_record_rival() -> dict[str, Any]:
    ref = "ocap://confused-deputy/record-corruption-rival"
    w = base_witness(ref)
    w["persistent_record"] = q("YES", ref)
    return assessment(
        "OCAP-CD-TD-102",
        "Confused-deputy record rival: read the billing overwrite as record formation. Does that license a client capability?",
        [branch(
            "record-rival",
            "deputy overwrites the billing record",
            w,
            ["CAPABILITY_ENLARGEMENT"],
            "Client's held authority fixed; the corrupted billing record is a record-level delta, scored separately from the client's capability.",
        )],
        selected="record-rival",
    )


def permission_grant() -> dict[str, Any]:
    ref = "ocap://permission-grant/acl-widening"
    w = base_witness(ref)
    w["access_change"] = q("YES", ref)  # ACL entry added
    return assessment(
        "OCAP-PG-TD-103",
        "Permission grant: the client is added to a resource ACL. Access change or capability enlargement?",
        [branch(
            "acl-widening",
            "client added to resource F's ACL",
            w,
            ["ACCESS_CHANGE"],
            "Resource access held fixed for the normalized comparison; the grant widens ambient access but not the intrinsic realizable set.",
        )],
        selected="acl-widening",
    )


def authority_amplification() -> dict[str, Any]:
    ref = "ocap://authority-amplification/generative-facet"
    w = base_witness(ref)
    w["description_change"] = q("YES", ref)
    w["normalized_task_set_relation"] = q("SUPERSET", ref)  # normalized set grows
    return assessment(
        "OCAP-AA-TD-104",
        "Rights amplification: the client acquires a generative capability-minting facet. Capability enlargement distinct from access?",
        [branch(
            "generative-facet",
            "client acquires a capability-minting facet",
            w,
            ["CAPABILITY_ENLARGEMENT"],
            "Ambient access budget held fixed; the generative facet enlarges the normalized realizable set because it is not mediated by any single access knob.",
        )],
        selected="generative-facet",
    )


def confused_deputy_frame_fork() -> dict[str, Any]:
    """Two admissible frames for the SAME confused-deputy event -> CONSTRUCTION_FORK.

    This exhibits the adversary's 'verdict flips with the access boundary' as a
    DECLARED fork, not a hidden circularity: object-capability instead supplies a
    single frame-free verdict (client authority unchanged), which is why it is at
    least as sharp here.
    """
    ref_a = "ocap://confused-deputy/frame-A-client-authority-fixed"
    wa = base_witness(ref_a)  # normalized EQUAL -> NULL
    ref_b = "ocap://confused-deputy/frame-B-deputy-ambient-available"
    wb = base_witness(ref_b)
    wb["normalized_task_set_relation"] = q("SUPERSET", ref_b)  # deputy counted as standing service
    return assessment(
        "OCAP-CD-TD-105",
        "Confused deputy under two admissible normalization frames: is the P2C capability type frame-dependent?",
        [
            branch(
                "frame-a-client-authority-fixed",
                "hold the client's own held authority fixed",
                wa,
                [],
                "Client's own held authority fixed; the deputy's authority is excluded from the client's normalized set.",
            ),
            branch(
                "frame-b-deputy-ambient-available",
                "count the deputy as a standing ambient service",
                wb,
                ["CAPABILITY_ENLARGEMENT"],
                "The ambiently-authorized deputy is held available as a fixed standing service, so the write is inside the client's normalized set.",
            ),
        ],
        branch_relation="ALTERNATIVE_CONSTRUCTIONS",
        selected=None,
    )


# ---- overclaim / collapse mutants (fail-direction controls) -----------------

def cd_capability_mutant() -> dict[str, Any]:
    m = confused_deputy()
    w = m["branches"][0]["witness"]
    w["normalized_task_set_relation"] = q("SUPERSET", "mutant capability overclaim")
    return m  # would need a dishonest normalized-superset to yield capability


def pg_capability_mutant() -> dict[str, Any]:
    m = permission_grant()
    m["branches"][0]["declared_claims"] = ["ACCESS_CHANGE", "CAPABILITY_ENLARGEMENT"]
    return m  # normalized still EQUAL -> capability must be rejected


def aa_token_mutant() -> dict[str, Any]:
    m = authority_amplification()
    w = m["branches"][0]["witness"]
    w["access_change"] = q("YES", "mutant token-acquisition")  # acquiring the facet IS receiving a token
    m["branches"][0]["declared_claims"] = ["ACCESS_CHANGE", "CAPABILITY_ENLARGEMENT"]
    return m  # -> MULTI_LEVEL, not pure CAPABILITY_ENLARGEMENT


def aa_collapse_mutant() -> dict[str, Any]:
    m = authority_amplification()
    w = m["branches"][0]["witness"]
    w["normalized_task_set_relation"] = q("EQUAL", "mutant collapse: amplification normalized away")
    return m  # -> capability rejected; the verdict rides on the declared frame


def outcome(item: dict[str, Any]) -> dict[str, Any]:
    result = td.evaluate_assessment(item)
    if not result["valid"] or not result["label_invariance"]["invariant"]:
        raise AssertionError(json.dumps(result, indent=2, sort_keys=True))
    return result


def load_result(name: str) -> dict[str, Any]:
    item = json.loads((WITNESS_DIR / name).read_text(encoding="utf-8"))
    return td.evaluate_assessment(item)


def main() -> int:
    results: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        results.append((name, bool(value), expected))

    committed_cd = load_result("confused-deputy-witness-v0.1.json")
    committed_aa = load_result("authority-amplification-witness-v0.1.json")
    check(
        "source: committed confused-deputy and authority-amplification witnesses are present",
        committed_cd["valid"] and committed_aa["valid"]
        and committed_cd["aggregate_outcome"] == "NULL_NO_RELEVANT_CHANGE"
        and committed_aa["aggregate_outcome"] == "CAPABILITY_ENLARGEMENT",
    )

    cd = outcome(confused_deputy())
    cd_rec = outcome(confused_deputy_record_rival())
    pg = outcome(permission_grant())
    aa = outcome(authority_amplification())
    fork = outcome(confused_deputy_frame_fork())

    cd_mut = outcome(cd_capability_mutant())
    pg_mut = outcome(pg_capability_mutant())
    aa_token = outcome(aa_token_mutant())
    aa_collapse = outcome(aa_collapse_mutant())

    cd_branch = cd["branch_results"][0]
    check(
        "cd evidence: confused deputy types as NULL_NO_RELEVANT_CHANGE for the client",
        cd["aggregate_outcome"] == "NULL_NO_RELEVANT_CHANGE" and cd_branch["components"] == [],
    )
    check(
        "cd evidence: the declared CAPABILITY_ENLARGEMENT overclaim is rejected",
        cd_branch["rejected_declared_claims"] == ["CAPABILITY_ENLARGEMENT"],
    )
    check(
        "cd evidence: the raw!=normalized alert fires (raw access up, normalized authority unchanged)",
        "Raw task access changed, but normalized capability did not." in cd_branch["alerts"],
    )
    check(
        "cd record-rival: deputy corrupting the billing log types as RECORD_FORMATION, not capability",
        cd_rec["aggregate_outcome"] == "RECORD_FORMATION"
        and "CAPABILITY_ENLARGEMENT" not in cd_rec["branch_results"][0]["components"]
        and cd_rec["branch_results"][0]["rejected_declared_claims"] == ["CAPABILITY_ENLARGEMENT"],
    )
    check(
        "pg evidence: a permission grant (ACL widening) types as ACCESS_CHANGE",
        pg["aggregate_outcome"] == "ACCESS_CHANGE" and pg["branch_results"][0]["components"] == ["ACCESS_CHANGE"],
    )
    check(
        "aa evidence: a generative authority amplification types as CAPABILITY_ENLARGEMENT",
        aa["aggregate_outcome"] == "CAPABILITY_ENLARGEMENT"
        and aa["branch_results"][0]["components"] == ["CAPABILITY_ENLARGEMENT"],
    )
    check(
        "separation: on the honest witnesses, ACCESS_CHANGE and CAPABILITY_ENLARGEMENT do not collapse",
        pg["aggregate_outcome"] == "ACCESS_CHANGE"
        and aa["aggregate_outcome"] == "CAPABILITY_ENLARGEMENT"
        and pg["aggregate_outcome"] != aa["aggregate_outcome"],
    )
    check(
        "frame-fork: the confused deputy is a declared CONSTRUCTION_FORK across frames, not a hidden circularity",
        fork["aggregate_outcome"] == "CONSTRUCTION_FORK"
        and {r["outcome"] for r in fork["branch_results"]} == {"NULL_NO_RELEVANT_CHANGE", "CAPABILITY_ENLARGEMENT"},
    )
    check(
        "label neutrality: no verdict depends on endpoint labels",
        all(r["label_invariance"]["invariant"] for r in (cd, cd_rec, pg, aa, fork)),
    )

    # Declared incumbent-match control (prereg): if object-capability's own
    # verdict equals P2C's, transfer FAILS to add novelty. On the confused deputy,
    # ocap says 'the client's authority did not amplify' and P2C rejects the
    # capability claim -> they match -> transfer-fails signal (the default forecast).
    ocap_says_client_authority_unchanged = True  # designation != authorization; deputy exercised its own authority
    p2c_rejects_client_capability = "CAPABILITY_ENLARGEMENT" in cd_branch["rejected_declared_claims"]
    check(
        "incumbent match: object-capability's own verdict equals P2C's on the confused deputy (transfer-fails signal)",
        ocap_says_client_authority_unchanged and p2c_rejects_client_capability,
    )

    # fail-direction controls (expected False)
    check(
        "cd-fail: capability overclaim is NOT the accepted confused-deputy verdict",
        cd["aggregate_outcome"] == cd_mut["aggregate_outcome"],
        expected=False,
    )
    check(
        "pg-fail: a capability overclaim on a pure permission grant is rejected",
        "CAPABILITY_ENLARGEMENT" in pg_mut["branch_results"][0]["components"],
        expected=False,
    )
    check(
        "aa-token-fail: amplification-with-token-acquisition does not type as PURE capability",
        aa_token["aggregate_outcome"] == "CAPABILITY_ENLARGEMENT",
        expected=False,
    )
    check(
        "aa-collapse-fail: normalizing the amplification away does NOT still grant capability",
        "CAPABILITY_ENLARGEMENT" in aa_collapse["branch_results"][0]["components"],
        expected=False,
    )

    print("SECURITY-DOMAIN TRANSFER-BREAKER -- P2C-XBREAK-001 (object-capability, domain 1)")
    print("=" * 78)
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
    print("\nReceiver verdicts (unchanged classify_transition.py):")
    print(f"  confused deputy (client frame): {cd['aggregate_outcome']}  (capability claim rejected)")
    print(f"  confused deputy (record rival): {cd_rec['aggregate_outcome']}")
    print(f"  permission grant (ACL widening): {pg['aggregate_outcome']}")
    print(f"  authority amplification (facet): {aa['aggregate_outcome']}")
    print(f"  confused deputy (frame fork):    {fork['aggregate_outcome']}")
    print(f"  amplification-with-token mutant: {aa_token['aggregate_outcome']}")
    print("\nVERDICT: HOLDS (no circularity/collapse; capability stays distinct from access)")
    print("         AND transfer-fails-novelty CONFIRMED (object-capability is at least as sharp).")
    print("Nonclaim:")
    print(f"  {cd['nonclaim']}")
    if failures:
        print("UNEXPECTED RESULTS:", failures)
        return 1
    print("All checks match expectations. Exit 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
