"""Witness-consuming boundary adapter for the superconducting-ring swing.

Question: can the physical boundary/source-to-capability adapter consume the
real witness's (Q,I,P) signature vector and matched-budget frame while exposing
whole-family admission as a testable residual instead of importing a capability
or issuance verdict as an input label?

This is a finite contract fixture. It is not a superconductivity simulation and
does not adjudicate Time as Finality, Temporal Issuance, GU, or any source-repo
truth. It only checks the P2C-owned adapter behavior needed after the
2026-07-16 real physical witness swing.
"""

from __future__ import annotations

from dataclasses import dataclass


CHECKS = {
    "setup: signature vectors use only declared QIP atoms": {"tag": "T"},
    "relabel invariance: branch and intervention names do not change residual": {"tag": "T"},
    "composition: staged signature deltas equal direct signature delta": {"tag": "T"},
    "witness: QIP gain is exposed as whole-family admission residual": {"tag": "E"},
    "local completions: no local completion reproduces all QIP signatures": {"tag": "E"},
    "whole-family control: target-phase admission is necessary for absorption": {"tag": "E"},
    "residual hygiene: report asks a testable F1 question, not a verdict": {"tag": "E"},
    "resource control: changed normalized frame is not called residual capability": {"tag": "E"},
    "circularity control: verdict-carrying completion input is rejected": {"tag": "E"},
    "nonconstancy: no-change transition returns no residual": {"tag": "E"},
    "relabel-fail: name-sensitive bad profile changes under relabeling": {
        "tag": "F",
        "protects": "relabel invariance: branch and intervention names do not change residual",
    },
    "whole-family-fail: restricted family without target phase does not absorb": {
        "tag": "F",
        "protects": "whole-family control: target-phase admission is necessary for absorption",
    },
    "resource-fail: bad adapter ignoring frame mismatch would misclassify": {
        "tag": "F",
        "protects": "resource control: changed normalized frame is not called residual capability",
    },
    "circularity-fail: metadata-sensitive bad adapter would import verdict": {
        "tag": "F",
        "protects": "circularity control: verdict-carrying completion input is rejected",
    },
}


QIP_ATOMS = frozenset({"Q", "I", "P"})
LOCAL_COMPLETION_KINDS = frozenset({
    "gauge",
    "relabeling",
    "hidden_state",
    "boundary",
    "seed",
    "access",
    "resource",
    "history",
    "provenance",
    "whole_family_without_target_phase",
})
FORBIDDEN_METADATA_KEYS = frozenset({
    "desired_verdict",
    "claimed_level",
    "claimed_verdict",
    "capability_verdict",
    "issuance_verdict",
    "finality_verdict",
})


@dataclass(frozen=True)
class WitnessFrame:
    """A physical frame reduced to data the neutral adapter may inspect."""

    name: str
    normalization_frame: str
    intervention_menu: tuple[str, ...]
    qip_signatures: frozenset[str]
    metadata: tuple[tuple[str, str], ...] = ()

    def profile(self) -> frozenset[str]:
        unknown = self.qip_signatures - QIP_ATOMS
        if unknown:
            raise ValueError(f"unknown signature atoms in {self.name}: {sorted(unknown)}")
        return frozenset(self.qip_signatures)


@dataclass(frozen=True)
class CompletionAttempt:
    """An attempted ordinary completion or whole-family admission."""

    kind: str
    frame: WitnessFrame
    admits_target_phase: bool = False
    provenance: str = ""

    def label(self) -> str:
        return f"{self.kind}:{self.frame.name}"


@dataclass(frozen=True)
class AdapterReport:
    pre_profile: frozenset[str]
    post_profile: frozenset[str]
    gained: frozenset[str]
    lost: frozenset[str]
    rejected: tuple[str, ...]
    local_absorbers: tuple[str, ...]
    whole_family_absorbers: tuple[str, ...]
    residual_class: str
    residual_question: str


def has_forbidden_metadata(frame: WitnessFrame) -> bool:
    for key, value in frame.metadata:
        normalized_key = key.lower()
        normalized_value = value.lower()
        if normalized_key in FORBIDDEN_METADATA_KEYS or "verdict" in normalized_key:
            return True
        if "capability_gain" in normalized_value or "issuance" in normalized_value:
            return True
    return False


def validate_completion(completion: CompletionAttempt) -> str | None:
    if not completion.provenance:
        return "missing provenance"
    if has_forbidden_metadata(completion.frame):
        return "carries a verdict or desired level"
    if completion.admits_target_phase and completion.kind != "whole_family":
        return "target-phase admission is only a whole-family test"
    if completion.kind in {"gauge", "relabeling"} and completion.frame.profile():
        return "equivalence-only completion cannot add QIP signatures"
    return None


def completion_matches_post(completion: CompletionAttempt, post_profile: frozenset[str]) -> bool:
    return post_profile <= completion.frame.profile()


def witness_boundary_adapter(
    pre: WitnessFrame,
    post: WitnessFrame,
    completions: tuple[CompletionAttempt, ...],
) -> AdapterReport:
    """Return a neutral residual report from QIP and frame data only."""

    pre_profile = pre.profile()
    post_profile = post.profile()
    gained = post_profile - pre_profile
    lost = pre_profile - post_profile

    rejected: list[str] = []
    valid: list[CompletionAttempt] = []
    for completion in completions:
        reason = validate_completion(completion)
        if reason is None:
            valid.append(completion)
        else:
            rejected.append(f"{completion.label()} ({reason})")

    if pre.normalization_frame != post.normalization_frame:
        residual = "RESOURCE_FRAME_CHANGED"
        question = "normalize the physical frame before capability comparison"
    elif pre.intervention_menu != post.intervention_menu:
        residual = "INTERVENTION_MENU_CHANGED"
        question = "fix the intervention menu before boundary comparison"
    elif not gained and not lost:
        residual = "NO_RESIDUAL"
        question = "no changed QIP signature to adjudicate"
    else:
        local_absorbers = tuple(
            completion.label()
            for completion in valid
            if completion.kind in LOCAL_COMPLETION_KINDS
            and completion_matches_post(completion, post_profile)
        )
        whole_family_absorbers = tuple(
            completion.label()
            for completion in valid
            if completion.kind == "whole_family"
            and completion.admits_target_phase
            and completion_matches_post(completion, post_profile)
        )

        if local_absorbers:
            residual = "LOCAL_COMPLETION_ABSORBED"
            question = "which local completion reproduced the QIP vector?"
        elif whole_family_absorbers:
            residual = "WHOLE_FAMILY_ADMISSION_RESIDUAL"
            question = (
                "is admitting the target phase into the fixed family a legitimate "
                "completion or an F1 trivialization?"
            )
        else:
            residual = "LOCAL_UNEXPLAINED_RESIDUAL"
            question = "which admissible completion, if any, reproduces the QIP vector?"

        return AdapterReport(
            pre_profile=pre_profile,
            post_profile=post_profile,
            gained=frozenset(gained),
            lost=frozenset(lost),
            rejected=tuple(rejected),
            local_absorbers=local_absorbers,
            whole_family_absorbers=whole_family_absorbers,
            residual_class=residual,
            residual_question=question,
        )

    return AdapterReport(
        pre_profile=pre_profile,
        post_profile=post_profile,
        gained=frozenset(gained),
        lost=frozenset(lost),
        rejected=tuple(rejected),
        local_absorbers=(),
        whole_family_absorbers=(),
        residual_class=residual,
        residual_question=question,
    )


def apply_delta(profile: frozenset[str], report: AdapterReport) -> frozenset[str]:
    return frozenset((profile - report.lost) | report.gained)


def relabel(frame: WitnessFrame, prefix: str) -> WitnessFrame:
    return WitnessFrame(
        name=f"{prefix}_{frame.name}",
        normalization_frame=frame.normalization_frame,
        intervention_menu=tuple(f"{prefix}_{item}" for item in frame.intervention_menu),
        qip_signatures=frame.qip_signatures,
        metadata=tuple((f"{prefix}_{key}", value) for key, value in frame.metadata),
    )


def name_sensitive_bad_profile(frame: WitnessFrame) -> tuple[str, tuple[str, ...], tuple[str, ...]]:
    return (frame.name, frame.intervention_menu, tuple(sorted(frame.profile())))


def bad_resource_blind_adapter(pre: WitnessFrame, post: WitnessFrame) -> str:
    if post.profile() - pre.profile():
        return "WHOLE_FAMILY_ADMISSION_RESIDUAL"
    return "NO_RESIDUAL"


def bad_metadata_sensitive_adapter(completions: tuple[CompletionAttempt, ...]) -> str:
    for completion in completions:
        for key, value in completion.frame.metadata:
            if "verdict" in key.lower() or "capability_gain" in value.lower():
                return "CAPABILITY_GAIN"
    return "NO_VERDICT"


def build_fixture() -> tuple[WitnessFrame, WitnessFrame, tuple[CompletionAttempt, ...]]:
    menu = ("cool", "thread_flux", "probe_read", "deform")
    frame = "matched_budget_counterfactual_pair"

    normal = WitnessFrame(
        "normal_reference",
        frame,
        menu,
        frozenset(),
    )
    superconducting = WitnessFrame(
        "superconducting_ring",
        frame,
        menu,
        frozenset({"Q", "I", "P"}),
    )

    def attempt(
        kind: str,
        name: str,
        signatures: frozenset[str],
        *,
        admits_target_phase: bool = False,
        metadata: tuple[tuple[str, str], ...] = (),
    ) -> CompletionAttempt:
        return CompletionAttempt(
            kind=kind,
            frame=WitnessFrame(
                name,
                frame,
                menu,
                signatures,
                metadata=metadata,
            ),
            admits_target_phase=admits_target_phase,
            provenance=f"finite {kind} control",
        )

    completions = (
        attempt("gauge", "gauge_equivalence", frozenset()),
        attempt("relabeling", "renamed_value", frozenset()),
        attempt("hidden_state", "latent_normal_value", frozenset()),
        attempt("boundary", "continuous_boundary_value", frozenset()),
        attempt("seed", "threaded_seed_value", frozenset()),
        attempt("access", "readout_access_only", frozenset()),
        attempt("resource", "same_budget_drive", frozenset()),
        attempt("history", "metastable_history", frozenset({"Q", "I"})),
        attempt("provenance", "frozen_record_label", frozenset()),
        attempt(
            "whole_family_without_target_phase",
            "fixed_family_restricted_to_normal_phase",
            frozenset({"Q", "I"}),
        ),
        attempt(
            "whole_family",
            "fixed_family_with_target_phase",
            frozenset({"Q", "I", "P"}),
            admits_target_phase=True,
        ),
    )
    return normal, superconducting, completions


def circular_completion() -> CompletionAttempt:
    menu = ("cool", "thread_flux", "probe_read", "deform")
    frame = "matched_budget_counterfactual_pair"
    return CompletionAttempt(
        kind="whole_family",
        frame=WitnessFrame(
            "declared_capability_gain",
            frame,
            menu,
            frozenset({"Q", "I", "P"}),
            metadata=(("desired_verdict", "capability_gain"),),
        ),
        admits_target_phase=True,
        provenance="self-labeled desired conclusion",
    )


def changed_resource_frame(post: WitnessFrame) -> WitnessFrame:
    return WitnessFrame(
        name=post.name,
        normalization_frame="unmatched_before_after_temperature_path",
        intervention_menu=post.intervention_menu,
        qip_signatures=post.qip_signatures,
    )


def main() -> None:
    normal, superconducting, completions = build_fixture()

    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    witness_report = witness_boundary_adapter(normal, superconducting, completions)
    restricted_completions = tuple(
        completion for completion in completions if not completion.admits_target_phase
    )
    restricted_report = witness_boundary_adapter(normal, superconducting, restricted_completions)
    relabeled_report = witness_boundary_adapter(
        relabel(normal, "r"),
        relabel(superconducting, "r"),
        completions,
    )
    resource_report = witness_boundary_adapter(
        normal,
        changed_resource_frame(superconducting),
        completions,
    )
    circular_report = witness_boundary_adapter(
        normal,
        superconducting,
        (circular_completion(),),
    )
    no_change_report = witness_boundary_adapter(normal, normal, completions)

    q_only = WitnessFrame(
        "quantized_only_mid",
        normal.normalization_frame,
        normal.intervention_menu,
        frozenset({"Q"}),
    )
    d01 = witness_boundary_adapter(normal, q_only, ())
    d12 = witness_boundary_adapter(q_only, superconducting, ())
    d02 = witness_boundary_adapter(normal, superconducting, ())
    composed = apply_delta(apply_delta(normal.profile(), d01), d12)
    direct = apply_delta(normal.profile(), d02)

    check(
        "setup: signature vectors use only declared QIP atoms",
        normal.profile() <= QIP_ATOMS and superconducting.profile() <= QIP_ATOMS,
    )
    check(
        "relabel invariance: branch and intervention names do not change residual",
        witness_report.gained == relabeled_report.gained
        and witness_report.residual_class == relabeled_report.residual_class,
    )
    check(
        "composition: staged signature deltas equal direct signature delta",
        composed == direct == superconducting.profile(),
    )
    check(
        "witness: QIP gain is exposed as whole-family admission residual",
        witness_report.gained == frozenset({"Q", "I", "P"})
        and witness_report.residual_class == "WHOLE_FAMILY_ADMISSION_RESIDUAL",
    )
    check(
        "local completions: no local completion reproduces all QIP signatures",
        not witness_report.local_absorbers,
    )
    check(
        "whole-family control: target-phase admission is necessary for absorption",
        witness_report.whole_family_absorbers
        and restricted_report.residual_class == "LOCAL_UNEXPLAINED_RESIDUAL",
    )
    check(
        "residual hygiene: report asks a testable F1 question, not a verdict",
        "F1" in witness_report.residual_question
        and "legitimate" in witness_report.residual_question
        and "CAPABILITY" not in witness_report.residual_class,
    )
    check(
        "resource control: changed normalized frame is not called residual capability",
        resource_report.residual_class == "RESOURCE_FRAME_CHANGED"
        and not resource_report.whole_family_absorbers,
    )
    check(
        "circularity control: verdict-carrying completion input is rejected",
        circular_report.rejected
        and circular_report.residual_class == "LOCAL_UNEXPLAINED_RESIDUAL"
        and not circular_report.whole_family_absorbers,
    )
    check(
        "nonconstancy: no-change transition returns no residual",
        no_change_report.residual_class == "NO_RESIDUAL",
    )

    check(
        "relabel-fail: name-sensitive bad profile changes under relabeling",
        name_sensitive_bad_profile(normal) == name_sensitive_bad_profile(relabel(normal, "r")),
        expected=False,
    )
    check(
        "whole-family-fail: restricted family without target phase does not absorb",
        bool(restricted_report.whole_family_absorbers),
        expected=False,
    )
    check(
        "resource-fail: bad adapter ignoring frame mismatch would misclassify",
        bad_resource_blind_adapter(normal, changed_resource_frame(superconducting))
        == "RESOURCE_FRAME_CHANGED",
        expected=False,
    )
    check(
        "circularity-fail: metadata-sensitive bad adapter would import verdict",
        bad_metadata_sensitive_adapter((circular_completion(),)) == "NO_VERDICT",
        expected=False,
    )

    print("WITNESS-CONSUMING BOUNDARY ADAPTER")
    print("=" * 72)
    failures = []
    n_t = n_e = n_f = 0
    for name, value, expected in checks:
        ok = value == expected
        tag_value = CHECKS.get(name, {}).get("tag", "?")
        n_t += tag_value == "T"
        n_e += tag_value == "E"
        n_f += tag_value == "F"
        print(f"{'PASS' if ok else 'UNEXPECTED'}  [{tag_value}] {name}: {value}")
        if not ok:
            failures.append(name)

    print()
    print(f"pre profile:       {sorted(witness_report.pre_profile)}")
    print(f"post profile:      {sorted(witness_report.post_profile)}")
    print(f"gained:            {sorted(witness_report.gained)}")
    print(f"residual class:    {witness_report.residual_class}")
    print(f"residual question: {witness_report.residual_question}")
    print(f"local absorbers:   {witness_report.local_absorbers}")
    print(f"whole-family:      {witness_report.whole_family_absorbers}")
    print(f"circular rejected: {circular_report.rejected}")
    print()
    print(f"EVIDENTIAL CHECKS (headline): {n_e} [E] + {n_f} [F] = {n_e + n_f}")
    print(f"[T] theorem-consequence checks (no evidential weight): {n_t}")

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()
