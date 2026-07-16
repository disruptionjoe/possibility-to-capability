"""Executed-neutrality harness (upgrade of the recorded-metamorphic control).

CONTEXT.  Gate-run v0.1's neutrality_control records a label swap and two
AUTHORED verdict strings; nothing is computed under the swapped labels
(swing-2 lane-1 referee defect D3).  This harness upgrades the control from
RECORDED to EXECUTED: given (i) a subject object containing branch labels,
(ii) a declared branch-label swap map, and (iii) a runnable evaluation
callable, it

  (a) executes the evaluation under the original labels,
  (b) executes the SAME evaluation under the swapped labels,
  (c) verifies verdict_before == verdict_after AND that at least one
      intermediate quantity actually CHANGED under the swap (the swap was
      not a no-op -- the failing direction of the control itself),
  (d) emits a receipt block for embedding alongside gate-run JSONs.

SCHEMA PLACEMENT (non-breaking).  gate-run-v0.1 is closed-world:
interfaces/gate-run-v0.1.schema.json sets additionalProperties:false and
tests/evaluate_gate_run.py enforces exact field-set equality on both the top
level and neutrality_control.  A new inline field would therefore be a
BREAKING change.  The receipt is emitted as a SIDECAR JSON document
(schema "neutrality-execution-receipt-v0.1") that the gate run references
from its existing free-text neutrality_control.artifact_ref string.  A
future gate-run v0.2 may inline it; v0.1 runs remain valid either way.

WHAT AN EXECUTED PASS MEANS (and does not).  executed_label_invariant=true
means: THIS evaluation callable, run twice, produced equal verdicts from
genuinely different intermediate state.  It is evidence about the evaluation
that was run, at the grade of that evaluation -- it does not promote any
source claim, select any branch, or reopen ADAPTER2-01.

CHECK DISCIPLINE (house style, swing 2):
  [T] theorem-consequence: outcome fixed by construction; NO evidential
      weight; listed separately and excluded from the headline.
  [E] genuine experiment: outcome not fixed at formalization time.
  [F] failing-direction control: a deliberately broken variant that FAILS,
      exercising the SAME checker code path it protects.
Only [E] and [F] count as evidence.

Pure Python stdlib.  Exit 0 iff every check matches its expectation.
"""

from __future__ import annotations

import copy
import hashlib
import json
from typing import Any, Callable

RECEIPT_SCHEMA = "neutrality-execution-receipt-v0.1"

# --------------------------------------------------------------- canonical

def canonical_json_bytes(value: object) -> bytes:
    """Same canonicalization as tests/evaluate_gate_run.py."""
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def sha256_json(value: object) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


# --------------------------------------------------------------- label swap

class SwapMapError(ValueError):
    """The declared swap map is not an admissible exact branch-label swap."""


def validate_swap_map(swap_map: dict[str, str]) -> None:
    if not isinstance(swap_map, dict) or not swap_map:
        raise SwapMapError("swap map must be a nonempty dict")
    for k, v in swap_map.items():
        if not (isinstance(k, str) and isinstance(v, str) and k and v):
            raise SwapMapError("swap map keys/values must be nonempty strings")
        if k == v:
            raise SwapMapError(f"swap map fixes label {k!r}: not a swap")
        if swap_map.get(v) != k:
            raise SwapMapError(f"swap map is not an involution at {k!r}")
    labels = list(swap_map)
    for a in labels:
        for b in labels:
            if a != b and a in b:
                raise SwapMapError(
                    f"label {a!r} is a substring of {b!r}: replacement ambiguous"
                )


def _swap_string(text: str, swap_map: dict[str, str]) -> str:
    """Simultaneous replacement via private-use placeholders."""
    placeholders = {
        label: chr(0xE000) + str(i) + chr(0xE001)  # private-use
        for i, label in enumerate(swap_map)
    }
    for label, ph in placeholders.items():
        text = text.replace(label, ph)
    for label, ph in placeholders.items():
        text = text.replace(ph, swap_map[label])
    return text


def apply_label_swap(obj: Any, swap_map: dict[str, str]) -> Any:
    """Deep, simultaneous swap of branch-label strings in a JSON-able object.

    Swaps inside BOTH values and dict keys: a label used as a key is part of
    the labeled presentation too.
    """
    if isinstance(obj, str):
        return _swap_string(obj, swap_map)
    if isinstance(obj, list):
        return [apply_label_swap(item, swap_map) for item in obj]
    if isinstance(obj, dict):
        return {
            _swap_string(k, swap_map) if isinstance(k, str) else k:
                apply_label_swap(v, swap_map)
            for k, v in obj.items()
        }
    return obj


# ----------------------------------------------------------------- harness

def run_executed_neutrality(
    evaluation: Callable[[Any], dict[str, Any]],
    subject: Any,
    swap_map: dict[str, str],
    evaluation_id: str,
    subject_ref: str,
) -> dict[str, Any]:
    """Execute the evaluation under original and swapped labels.

    evaluation(subject) must return
        {"verdict": <str>, "intermediates": <JSON-able dict>}
    and must be a pure function of its argument (it is called twice on
    independently deep-copied subjects; mutation of the input is detected).

    Returns a receipt dict (schema neutrality-execution-receipt-v0.1).
    Never raises on a FAILING control outcome -- a neutrality failure or a
    no-op swap is a reported result, not an exception -- but an inadmissible
    swap map raises SwapMapError (that is a harness-usage error, not a
    neutrality verdict).
    """
    validate_swap_map(swap_map)

    original = copy.deepcopy(subject)
    swapped = apply_label_swap(copy.deepcopy(subject), swap_map)
    digest_original = sha256_json(original)
    digest_swapped = sha256_json(swapped)
    swap_changed_subject = digest_original != digest_swapped

    # round-trip integrity: swapping twice must restore the subject exactly
    round_trip_ok = sha256_json(
        apply_label_swap(copy.deepcopy(swapped), swap_map)
    ) == digest_original

    result_before = evaluation(copy.deepcopy(original))
    result_after = evaluation(copy.deepcopy(swapped))

    verdict_before = str(result_before["verdict"])
    verdict_after = str(result_after["verdict"])
    inter_before = result_before.get("intermediates", {})
    inter_after = result_after.get("intermediates", {})
    digest_inter_before = sha256_json(inter_before)
    digest_inter_after = sha256_json(inter_after)

    changed_keys = sorted(
        set(
            k
            for k in set(inter_before) | set(inter_after)
            if sha256_json(inter_before.get(k)) != sha256_json(inter_after.get(k))
        )
    )
    swap_changed_intermediates = digest_inter_before != digest_inter_after
    verdict_equal = verdict_before == verdict_after

    executed_label_invariant = (
        verdict_equal
        and swap_changed_subject
        and swap_changed_intermediates
        and round_trip_ok
    )
    failure_reasons: list[str] = []
    if not verdict_equal:
        failure_reasons.append("verdict changed under label swap")
    if not swap_changed_subject:
        failure_reasons.append(
            "swap was a no-op on the subject (labels absent): control vacuous"
        )
    if not swap_changed_intermediates:
        failure_reasons.append(
            "no intermediate quantity changed under the swap: the evaluation "
            "never read the swapped material; control vacuous"
        )
    if not round_trip_ok:
        failure_reasons.append("double swap did not restore the subject")

    return {
        "schema": RECEIPT_SCHEMA,
        "mode": "EXECUTED",
        "harness": "tests/neutrality_executed_harness.py",
        "evaluation_id": evaluation_id,
        "subject_ref": subject_ref,
        "subject_digest_before": digest_original,
        "subject_digest_after": digest_swapped,
        "swap_map": dict(swap_map),
        "verdict_before": verdict_before,
        "verdict_after": verdict_after,
        "verdict_equal": verdict_equal,
        "intermediates_digest_before": digest_inter_before,
        "intermediates_digest_after": digest_inter_after,
        "swap_changed_subject": swap_changed_subject,
        "swap_changed_intermediates": swap_changed_intermediates,
        "changed_intermediate_keys": changed_keys,
        "round_trip_restores_subject": round_trip_ok,
        "executed_label_invariant": executed_label_invariant,
        "failure_reasons": failure_reasons,
        "nonclaim": (
            "An executed label-invariant verdict is a property of the "
            "evaluation that was run, at that evaluation's grade; it does "
            "not select a branch, promote any source claim, or establish "
            "invariance under evaluations that were not run."
        ),
    }


# ---------------------------------------------- synthetic worked evaluation
#
# Full-strength demonstration: the verdict is COMPUTED from label-attached
# numeric dynamics, not authored.  Two sectors evolve under x' = r x
# (discretized); the evaluation decides realizability (boundedness of the
# trajectory sup) per sector and selects a sector only if exactly one is
# realizable.  Pure stdlib.

def _trajectory_stats(rate: float, x0: float = 1.0) -> tuple[float, float]:
    """(sup |x_t|, final |x_t|) for x' = r x, forward Euler, t in [0, 30].

    DEFECT DISCLOSURE (first run): the initial version returned only the
    sup, which for any decaying trajectory from x0=1 is identically 1.0 --
    so the intermediates were label-symmetric and the harness's own vacuity
    guard (swap_changed_intermediates) correctly REFUSED to certify the
    synthetic example.  The evaluation (not the expectation) was revised to
    also record the per-label final values, which genuinely differ across
    rates.  The failed first run is embedded in the exploration notes.
    """
    x, sup, dt = x0, abs(x0), 0.05
    for _ in range(600):
        x = x * (1.0 + rate * dt)
        sup = max(sup, abs(x))
    return sup, abs(x)


def sector_boundedness_evaluation(subject: dict[str, Any]) -> dict[str, Any]:
    stats = {
        label: _trajectory_stats(float(spec["rate"]))
        for label, spec in subject["sectors"].items()
    }
    bounded = {label: s[0] < 1e3 for label, s in stats.items()}
    selected = [label for label, ok in bounded.items() if ok]
    if len(selected) == 1:
        verdict = f"SELECTED:{selected[0]}"
    elif not selected:
        verdict = "NO_REALIZABLE_SECTOR"
    else:
        verdict = "NO_BRANCH_SELECTED"
    return {
        "verdict": verdict,
        "intermediates": {
            "trajectory_sups": {k: round(s[0], 9) for k, s in stats.items()},
            "final_values": {k: f"{s[1]:.6e}" for k, s in stats.items()},
            "bounded_by_label": bounded,
        },
    }


def fastest_decay_label_reader(subject: dict[str, Any]) -> dict[str, Any]:
    """Deliberately branch-SELECTING evaluation (for the [F] control): it
    reports the label of the fastest-decaying sector (smallest final value),
    so its verdict tracks the labels and must flip under the swap."""
    stats = {
        label: _trajectory_stats(float(spec["rate"]))
        for label, spec in subject["sectors"].items()
    }
    winner = min(stats, key=lambda k: (stats[k][1], k))
    return {
        "verdict": f"SELECTED:{winner}",
        "intermediates": {
            "final_values": {k: f"{s[1]:.6e}" for k, s in stats.items()},
        },
    }


# ------------------------------------------- GU-001 receiver-side evaluation
#
# Receiver-side re-run of the GU-001 neutrality control in EXECUTED mode,
# from the frozen packet JSON alone (no GU code imported or executed).
# Branch labels: the packet's own machine-readable branch tokens
# "C_good" / "C_path".  The evaluation COMPUTES a branch-selection verdict
# from the packet's fields:
#   - every JSON pointer whose string mentions each label (occurrence map),
#   - decision_type,
#   - whether any construction fork's `selected` field names either branch.
# Verdict: NO_BRANCH_SELECTED iff decision_type == "not_forced" and no
# fork's selected field names either branch label; otherwise
# SELECTED:<labels found in selection position>.
#
# GRADE DISCLOSURE: this executes the RECEIVER's verdict derivation under
# both labelings.  It does NOT re-execute the SOURCE's load-bearing
# computation (see the first-class finding in main()).

GU_LABELS = ("C_good", "C_path")


def _walk_pointers(obj: Any, pointer: str = "") -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    if isinstance(obj, str):
        out.append((pointer or "/", obj))
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            out.extend(_walk_pointers(item, f"{pointer}/{i}"))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            token = str(k).replace("~", "~0").replace("/", "~1")
            out.extend(_walk_pointers(v, f"{pointer}/{token}"))
    return out


def _label_sites(text: str, label: str) -> list[int]:
    sites, start = [], 0
    while True:
        i = text.find(label, start)
        if i < 0:
            return sites
        sites.append(i)
        start = i + len(label)


def gu001_receiver_branch_evaluation(packet: dict[str, Any]) -> dict[str, Any]:
    strings = _walk_pointers(packet)
    # Occurrence sites at CHARACTER granularity ("<pointer>@<offset>").
    # DEFECT DISCLOSURE (first run): pointer-granularity occurrence sets are
    # swap-SYMMETRIC in this packet -- every packet string that mentions one
    # branch label also mentions the other -- so the intermediates did not
    # change under the swap and the harness's vacuity guard refused to
    # certify.  Character offsets break the symmetry (the two labels sit at
    # different positions inside each string); the evaluation was revised
    # accordingly.  The co-occurrence fact itself is recorded below as a
    # first-class intermediate.
    occurrences = {
        label: sorted(
            f"{ptr}@{off}"
            for ptr, text in strings
            for off in _label_sites(text, label)
        )
        for label in GU_LABELS
    }
    counts = {label: len(sites) for label, sites in occurrences.items()}
    pointer_sets = {
        label: sorted({site.split("@", 1)[0] for site in occurrences[label]})
        for label in GU_LABELS
    }
    labels_always_co_occur = pointer_sets[GU_LABELS[0]] == pointer_sets[GU_LABELS[1]]
    decision_type = packet.get("question", {}).get("decision_type")
    selected_hits = sorted(
        {
            label
            for fork in packet.get("construction_forks", [])
            for label in GU_LABELS
            if label in str(fork.get("selected", ""))
        }
    )
    if decision_type == "not_forced" and not selected_hits:
        verdict = "NO_BRANCH_SELECTED"
    elif selected_hits:
        verdict = "SELECTED:" + ",".join(selected_hits)
    else:
        verdict = f"DECISION_TYPE:{decision_type}"
    return {
        "verdict": verdict,
        "intermediates": {
            "label_occurrence_sites": occurrences,
            "label_occurrence_counts": counts,
            "labels_always_co_occur_at_pointer_granularity":
                labels_always_co_occur,
            "decision_type": decision_type,
            "selected_field_label_hits": selected_hits,
        },
    }


# -------------------------------------------------------------- self-test

def main() -> None:
    import sys
    from pathlib import Path

    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    # ---- synthetic subject: two decaying sectors, distinct rates, neither
    # ---- selected (both realizable); labels physically asymmetric enough
    # ---- that intermediates MUST change under the swap.
    subject = {
        "sectors": {"K_plus": {"rate": -1.0}, "K_minus": {"rate": -2.0}},
        "note": "sector K_plus is listed first; K_minus decays faster",
    }
    swap = {"K_plus": "K_minus", "K_minus": "K_plus"}

    check("[T] swap-map validation accepts the exact swap",
          validate_swap_map(swap) is None)
    try:
        validate_swap_map({"a": "a"})
        fixed_ok = True
    except SwapMapError:
        fixed_ok = False
    check("[F] swap-map validator REJECTS a label-fixing map "
          "(protects: swap-map validation, same validate_swap_map path)",
          fixed_ok, expected=False)
    try:
        validate_swap_map({"C_good": "C_good_prime", "C_good_prime": "C_good"})
        substr_ok = True
    except SwapMapError:
        substr_ok = False
    check("[F] swap-map validator REJECTS substring-ambiguous labels "
          "(protects: swap-map validation)", substr_ok, expected=False)

    receipt_syn = run_executed_neutrality(
        sector_boundedness_evaluation, subject, swap,
        evaluation_id="synthetic-sector-boundedness-v1",
        subject_ref="inline synthetic subject (this file)",
    )
    check("[E] synthetic: executed verdict equal under swap AND "
          "intermediates changed (executed_label_invariant)",
          receipt_syn["executed_label_invariant"])
    check("[T] synthetic: double swap restores subject",
          receipt_syn["round_trip_restores_subject"])
    check("[E] synthetic: the changed intermediates are the label-keyed "
          "numeric quantities (per-label final values moved)",
          "final_values" in receipt_syn["changed_intermediate_keys"])

    # ---- [F] no-op swap: labels absent from the subject; SAME
    # ---- run_executed_neutrality path must refuse to certify.
    receipt_noop = run_executed_neutrality(
        sector_boundedness_evaluation, subject,
        {"Q_left": "Q_right", "Q_right": "Q_left"},
        evaluation_id="synthetic-noop-swap-control",
        subject_ref="inline synthetic subject (this file)",
    )
    check("[F] no-op swap is NOT certified (subject unchanged detected; "
          "protects: executed_label_invariant, same run_executed_neutrality "
          "path)", receipt_noop["executed_label_invariant"], expected=False)
    check("[T] no-op swap failure reason names the vacuity",
          any("no-op" in r for r in receipt_noop["failure_reasons"]))

    # ---- [F] label-reading (branch-selecting) evaluation: verdict must
    # ---- flip under the swap and the harness must report the failure.
    receipt_reader = run_executed_neutrality(
        fastest_decay_label_reader, subject, swap,
        evaluation_id="synthetic-label-reader-control",
        subject_ref="inline synthetic subject (this file)",
    )
    check("[F] branch-selecting evaluation FAILS executed neutrality "
          "(verdict flips under swap; protects: executed_label_invariant)",
          receipt_reader["executed_label_invariant"], expected=False)
    check("[T] label-reader verdicts differ exactly by the swapped label",
          receipt_reader["verdict_before"] == "SELECTED:K_minus"
          and receipt_reader["verdict_after"] == "SELECTED:K_plus")

    # ---- GU-001 worked example (receiver-side, frozen packet only)
    repo_root = (
        Path(sys.argv[1]).resolve()
        if len(sys.argv) > 1
        else Path(__file__).resolve().parent.parent
    )
    packet_path = repo_root / (
        "packets/imports/GU-001/GU-001-grading-sign-barb-v0.2.json"
    )
    gu_receipt = None
    if packet_path.is_file():
        packet = json.loads(packet_path.read_text(encoding="utf-8"))
        gu_swap = {"C_good": "C_path", "C_path": "C_good"}
        gu_receipt = run_executed_neutrality(
            gu001_receiver_branch_evaluation, packet, gu_swap,
            evaluation_id="gu001-receiver-branch-selection-v1",
            subject_ref=(
                "packets/imports/GU-001/GU-001-grading-sign-barb-v0.2.json "
                "(frozen packet, read-only)"
            ),
        )
        check("[E] GU-001: receiver-side verdict derivation is executed-"
              "label-invariant (NO_BRANCH_SELECTED both ways, intermediates "
              "changed)  [disclosure: packet content was known before this "
              "evaluator was written; regression-grade [E], see notes]",
              gu_receipt["executed_label_invariant"]
              and gu_receipt["verdict_before"] == "NO_BRANCH_SELECTED")
        check("[T] GU-001: both branch labels occur in the packet "
              "(swap not vacuous by construction of the label choice)",
              all(gu_receipt["swap_map"]) and gu_receipt["swap_changed_subject"])

        # [F] on the SAME GU path: a mutated COPY (never written anywhere)
        # in which a fork's selected field names a branch must fail.
        broken = copy.deepcopy(packet)
        broken["construction_forks"][1]["selected"] = (
            "the C_good branch is hereby chosen"
        )
        receipt_broken = run_executed_neutrality(
            gu001_receiver_branch_evaluation, broken, gu_swap,
            evaluation_id="gu001-broken-selection-control",
            subject_ref="in-memory mutated copy (control only; not persisted)",
        )
        check("[F] GU-001 control: a packet-copy that SELECTS a branch fails "
              "executed neutrality (SELECTED:C_good -> SELECTED:C_path; "
              "protects: the GU-001 [E] check, same evaluation + harness "
              "path)", receipt_broken["executed_label_invariant"],
              expected=False)
        check("[T] GU-001 control verdicts flip as predicted",
              receipt_broken["verdict_before"] == "SELECTED:C_good"
              and receipt_broken["verdict_after"] == "SELECTED:C_path")
    else:
        check("[E] GU-001 packet present at expected path", False)

    # ------------------------------------------------------------- report
    print("EXECUTED-NEUTRALITY HARNESS SELF-TEST")
    print("=" * 74)
    failures = []
    n_t = n_e = n_f = 0
    for name, value, expected in checks:
        ok = value == expected
        if name.startswith("[T]"):
            n_t += 1
        elif name.startswith("[E]"):
            n_e += 1
        elif name.startswith("[F]"):
            n_f += 1
        print(f"{'PASS' if ok else 'UNEXPECTED'}  {name}: {value}")
        if not ok:
            failures.append(name)
    print()
    print(f"EVIDENTIAL CHECKS (headline): {n_e} [E] + {n_f} [F] = {n_e + n_f}")
    print(f"[T] theorem-consequence checks (no evidential weight): {n_t}")
    if gu_receipt is not None:
        print()
        print("GU-001 EXECUTED-NEUTRALITY RECEIPT (sidecar; reference from")
        print("neutrality_control.artifact_ref in a future gate run):")
        print(json.dumps(gu_receipt, ensure_ascii=False, indent=2,
                         sort_keys=True))
    if failures:
        print("\nUNEXPECTED RESULTS:", failures)
        raise SystemExit(1)
    print("\nAll checks match expectations. Exit 0.")
    sys.exit(0)


if __name__ == "__main__":
    main()
