> Part of the 2026-07-16 fiber-closure swing (2-prime adversarial twins + T26 + tooling). Exploration tier; no claim promotion; the attached referee report GOVERNS the grades — read it before citing the lane report.

# P2C Tooling Rider — Swing-2 Infrastructure Upgrades (Executed Neutrality + [T]/[E]/[F] Linter)

**Tier:** exploration. **Grades explicit throughout.** No source-repo claim moves; bar(b), H59, Krein positivity, physical issuance all remain OPEN; ADAPTER2-01 untouched. Nothing below reopens the withdrawn identity. All receipts below are from real runs (Python 3, pure stdlib, executed 2026-07-16 in a scratchpad sandbox; the repo was not written to).

---

## Deliverable 1 — Executed-Neutrality Harness

**Proposed path:** `tests/neutrality_executed_harness.py`

### Design decisions

1. **RECORDED → EXECUTED.** GU-001-GR-001's `neutrality_control` contains two authored verdict strings compared for equality (lane-1 referee D3). The harness instead takes (subject, swap map, evaluation callable), runs the evaluation twice — original and swapped labels — and certifies only if: verdicts equal **AND** the subject actually changed under the swap **AND** at least one intermediate quantity changed (proving the evaluation *read* the swapped material) **AND** double-swap restores the subject byte-exactly. A vacuous swap is a reported failure, not a pass.
2. **Schema placement (non-breaking, and why it must be a sidecar).** `gate-run-v0.1.schema.json` is closed-world (`additionalProperties: false`) and `evaluate_gate_run.py` enforces exact field-set equality on both the top level and `neutrality_control`. **Any inline field is a breaking change.** The receipt is therefore a standalone sidecar document (`schema: "neutrality-execution-receipt-v0.1"`, same canonical-JSON/sha256 conventions as the evaluator) referenced from the existing free-text `neutrality_control.artifact_ref`. Inlining is a gate-run v0.2 item.
3. **First-class finding — GU-001 needs source-side cooperation for full-strength executed neutrality.** A genuinely executed swap of GU-001's *source* load-bearing computation (the W210 sign-blindness lemma etc.) is **not achievable receiver-side from the frozen packet alone**, for three independent reasons: (i) the bundle's executable artifacts are GU source code — executing them receiver-side crosses the receiver boundary the import contract exists to protect; (ii) the bundle is not runtime-closed anyway (Annotation E: `W210_decisive_bit_helmholtz.py` imports `gen_sector_bridge.py` outside `hash_scope`) and depends on numpy, outside P2C's stdlib-only test discipline; (iii) the source tests hardcode both branches internally — no label-parameterized entry point exists to run "under swapped labels." **Bounding conclusion (Failure-Preservation, first-class): source-computation-grade executed neutrality requires the source to ship a label-parameterized evaluation entry point inside the frozen bundle (packet v0.3 candidate; route via mailbox, not edits).** What *was* executed receiver-side is the receiver's own verdict derivation (see worked example) — genuine execution, honestly weaker scope.

### File contents (full) — `tests/neutrality_executed_harness.py`

```python
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
```

### Worked-example receipts (real run, final)

```
EXECUTED-NEUTRALITY HARNESS SELF-TEST
==========================================================================
PASS  [T] swap-map validation accepts the exact swap: True
PASS  [F] swap-map validator REJECTS a label-fixing map (protects: swap-map validation, same validate_swap_map path): False
PASS  [F] swap-map validator REJECTS substring-ambiguous labels (protects: swap-map validation): False
PASS  [E] synthetic: executed verdict equal under swap AND intermediates changed (executed_label_invariant): True
PASS  [T] synthetic: double swap restores subject: True
PASS  [E] synthetic: the changed intermediates are the label-keyed numeric quantities (per-label final values moved): True
PASS  [F] no-op swap is NOT certified (subject unchanged detected; protects: executed_label_invariant, same run_executed_neutrality path): False
PASS  [T] no-op swap failure reason names the vacuity: True
PASS  [F] branch-selecting evaluation FAILS executed neutrality (verdict flips under swap; protects: executed_label_invariant): False
PASS  [T] label-reader verdicts differ exactly by the swapped label: True
PASS  [E] GU-001: receiver-side verdict derivation is executed-label-invariant (NO_BRANCH_SELECTED both ways, intermediates changed)  [disclosure: packet content was known before this evaluator was written; regression-grade [E], see notes]: True
PASS  [T] GU-001: both branch labels occur in the packet (swap not vacuous by construction of the label choice): True
PASS  [F] GU-001 control: a packet-copy that SELECTS a branch fails executed neutrality (SELECTED:C_good -> SELECTED:C_path; protects: the GU-001 [E] check, same evaluation + harness path): False
PASS  [T] GU-001 control verdicts flip as predicted: True

EVIDENTIAL CHECKS (headline): 3 [E] + 5 [F] = 8
[T] theorem-consequence checks (no evidential weight): 6

GU-001 EXECUTED-NEUTRALITY RECEIPT (sidecar; reference from
neutrality_control.artifact_ref in a future gate run):
{
  "changed_intermediate_keys": ["label_occurrence_sites"],
  "evaluation_id": "gu001-receiver-branch-selection-v1",
  "executed_label_invariant": true,
  "failure_reasons": [],
  "harness": "tests/neutrality_executed_harness.py",
  "intermediates_digest_after": "33ea8aa6d478c0116824a2c057929c636456bd8def03e5f0704000082ecccd80",
  "intermediates_digest_before": "c523d3d862fd5656f24e6278ff86f84f98da9138889c32c0fe8f0872ade9755a",
  "mode": "EXECUTED",
  "nonclaim": "An executed label-invariant verdict is a property of the evaluation that was run, at that evaluation's grade; it does not select a branch, promote any source claim, or establish invariance under evaluations that were not run.",
  "round_trip_restores_subject": true,
  "schema": "neutrality-execution-receipt-v0.1",
  "subject_digest_after": "fbcae99a0ac8e7ed225dc73164167e9069eab4482ce9d6d5f9a122908acc1294",
  "subject_digest_before": "441cc423daecc4ae9386333f1147f7f0c46ccbe32998ad73c4e35965a996de62",
  "subject_ref": "packets/imports/GU-001/GU-001-grading-sign-barb-v0.2.json (frozen packet, read-only)",
  "swap_changed_intermediates": true,
  "swap_changed_subject": true,
  "swap_map": {"C_good": "C_path", "C_path": "C_good"},
  "verdict_after": "NO_BRANCH_SELECTED",
  "verdict_before": "NO_BRANCH_SELECTED",
  "verdict_equal": true
}

All checks match expectations. Exit 0.
```

**Receiver-side observation worth keeping:** in the frozen GU-001 packet the two branch labels occur an equal number of times (`C_good: 3, C_path: 3`) and **co-occur at pointer granularity** — every packet string mentioning one mentions the other (`labels_always_co_occur_at_pointer_granularity: true`). The packet's prose is structurally symmetric in the two branches, which is exactly what its neutrality posture predicts.

---

## Deliverable 2 — [T]/[E]/[F] Tagging Linter

**Proposed path:** `tests/tef_check_tag_linter.py`

**Convention designed (forward):** module-level `CHECKS` registry mapping check-name → `{"tag": "T"|"E"|"F", "protects": <name>}` (protects required for every [F], must name an existing non-[F] check). Legacy fixtures without the registry get inline-tag mode (krein style, `[X] id:` name prefixes, `<id>-fail` reference rule) or advisory legacy-scan. Headline rule R4: any `N/N` literal where N equals the total check count including [T] is a violation.

### File contents (full) — `tests/tef_check_tag_linter.py`

```python
"""[T]/[E]/[F] check-tag linter for P2C test fixtures.

HOUSE RULE (swing-2 process note, adopted from lane 3's referee): every
check in a fixture is tagged
  [T] theorem-consequence  -- outcome fixed by construction; carries NO
      evidential weight; listed separately,
  [E] genuine experiment   -- outcome not fixed at formalization time,
  [F] failing-direction control -- a deliberately broken variant that FAILS,
      proving the checker it protects has teeth (same code path).
Only [E] and [F] count as evidence; a headline may not count [T] checks.

DECLARED CONVENTION (forward, for new fixtures) -- a module-level registry:

    CHECKS = {
        "a1: A_a is eta-contractive":  {"tag": "E"},
        "a1-fail: eta is not":         {"tag": "F", "protects": "a1: A_a is eta-contractive"},
        "setup: S eta S = -eta":       {"tag": "T"},
    }

Rules enforced in registry mode (violations -> nonzero exit):
  R1  every entry has tag in {T, E, F};
  R2  every [F] entry declares "protects" naming an existing non-[F] entry
      (the same-code-path requirement itself is behavioral and cannot be
      proven statically; the declaration makes it auditable);
  R3  every literal check name used at runtime (check("...") calls or
      checks["..."] assignments) appears in CHECKS and vice versa;
  R4  headline hygiene: any "N/N" style headline literal where N equals the
      TOTAL check count (including [T]) is flagged.

INLINE-TAG MODE (krein_norm_link_probe.py style): check names begin with
"[T] ", "[E] ", "[F] ".  [F] names must reference their protected checker
by id ("<id>-fail" where <id> is the id of another non-dynamic check, or an
explicit "protects:" phrase).

LEGACY-SCAN MODE: fixtures that predate the convention (untagged
checks[...] dicts, teeth suites) get an ADVISORY report -- every untagged
check is listed; the report is the demonstration, exit stays 0 unless
--strict.

Pure Python stdlib (ast + re).  Usage:
    python tef_check_tag_linter.py [--strict] FILE [FILE ...]
    python tef_check_tag_linter.py --selftest
"""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path
from typing import Any

TAG_RE = re.compile(r"^\[([TEF])\]\s*")
ID_RE = re.compile(r"^\[[TEF]\]\s*([A-Za-z0-9_']+)")
F_TARGET_RE = re.compile(r"([A-Za-z0-9_']+)-fail")
HEADLINE_RE = re.compile(r"\b(\d+)\s*/\s*(\d+)\b")
CHECK_DICT_NAMES = {"checks", "teeth", "t"}


def _literal_prefix(node: ast.AST) -> tuple[str, bool]:
    """(name, is_dynamic) for a str constant or an f-string key/name."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value, False
    if isinstance(node, ast.JoinedStr):
        parts = []
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                parts.append(value.value)
            else:
                parts.append("{?}")
        return "".join(parts), True
    return "", True


def extract_checks(tree: ast.AST) -> list[dict[str, Any]]:
    """All check registrations: check(...) calls and checks[...]=... stores."""
    found: list[dict[str, Any]] = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "check"
            and node.args
        ):
            name, dynamic = _literal_prefix(node.args[0])
            if name or not dynamic:
                found.append(
                    {"name": name, "dynamic": dynamic, "line": node.lineno,
                     "via": "check-call"}
                )
        elif isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if (
                isinstance(target, ast.Subscript)
                and isinstance(target.value, ast.Name)
                and target.value.id in CHECK_DICT_NAMES
            ):
                name, dynamic = _literal_prefix(target.slice)
                if name:
                    found.append(
                        {"name": name, "dynamic": dynamic,
                         "line": node.lineno,
                         "via": f"{target.value.id}[...]="}
                    )
    return found


def extract_registry(tree: ast.AST) -> dict[str, dict[str, Any]] | None:
    """Module-level CHECKS = {literal dict}, or None if absent."""
    for node in ast.iter_child_nodes(tree):
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "CHECKS"
            and isinstance(node.value, ast.Dict)
        ):
            registry: dict[str, dict[str, Any]] = {}
            for key, value in zip(node.value.keys, node.value.values):
                if not (isinstance(key, ast.Constant) and isinstance(key.value, str)):
                    continue
                try:
                    registry[key.value] = ast.literal_eval(value)
                except (ValueError, SyntaxError):
                    registry[key.value] = {"tag": None}
            return registry
    return None


def extract_headline_suspects(
    tree: ast.AST, total_checks: int
) -> list[dict[str, Any]]:
    suspects = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            for m in HEADLINE_RE.finditer(node.value):
                n1, n2 = int(m.group(1)), int(m.group(2))
                if n1 == n2 and n1 > 1:
                    suspects.append(
                        {"line": node.lineno, "literal": m.group(0),
                         "counts_total_including_T": n1 == total_checks}
                    )
    return suspects


def lint_source(source: str, path: str) -> dict[str, Any]:
    tree = ast.parse(source, filename=path)
    registry = extract_registry(tree)
    runtime_checks = extract_checks(tree)
    violations: list[str] = []
    advisories: list[str] = []

    if registry is not None:
        convention = "registry"
        names = list(registry)
        tags = {n: (registry[n] or {}).get("tag") for n in names}
        untagged = [n for n in names if tags[n] not in ("T", "E", "F")]
        for n in untagged:
            violations.append(f"R1 untagged registry entry: {n!r}")
        for n in names:
            if tags[n] == "F":
                protects = (registry[n] or {}).get("protects")
                if not protects:
                    violations.append(f"R2 [F] entry lacks 'protects': {n!r}")
                elif protects not in registry:
                    violations.append(
                        f"R2 [F] {n!r} protects unknown check {protects!r}")
                elif tags.get(protects) == "F":
                    violations.append(
                        f"R2 [F] {n!r} protects another [F]: {protects!r}")
        runtime_names = {c["name"] for c in runtime_checks if not c["dynamic"]}
        for n in sorted(runtime_names - set(names)):
            violations.append(f"R3 runtime check not in CHECKS registry: {n!r}")
        for n in sorted(set(names) - runtime_names):
            advisories.append(
                f"R3 registry entry with no statically-visible runtime "
                f"check (may be dynamic): {n!r}")
        tag_counts = {t: sum(1 for n in names if tags[n] == t) for t in "TEF"}
        total = len(names)
    else:
        names = [c["name"] for c in runtime_checks]
        tags = {}
        untagged = []
        f_checks, ids = [], set()
        for c in runtime_checks:
            m = TAG_RE.match(c["name"])
            tag = m.group(1) if m else None
            tags[c["name"]] = tag
            if tag is None:
                untagged.append(c)
            idm = ID_RE.match(c["name"])
            if tag == "F":
                f_checks.append(c)
            elif idm and not idm.group(1).endswith("fail"):
                # only non-[F] checks contribute protectable ids: an [F]'s
                # own id must not satisfy its own reference requirement
                ids.add(idm.group(1).rstrip(":"))
        if untagged:
            convention = "legacy-scan" if len(untagged) == len(runtime_checks) \
                else "mixed"
            for c in untagged:
                advisories.append(
                    f"untagged check (line {c['line']}, {c['via']}): "
                    f"{c['name']!r}")
        else:
            convention = "inline-tags"
        for c in f_checks:
            tgt = F_TARGET_RE.search(c["name"])
            if "protects:" in c["name"]:
                continue
            if not tgt or tgt.group(1).split("'")[0] not in ids:
                (violations if convention == "inline-tags" else advisories
                 ).append(
                    f"[F] check does not reference the checker it protects "
                    f"(line {c['line']}): {c['name']!r}")
        tag_counts = {
            t: sum(1 for v in tags.values() if v == t) for t in "TEF"}
        total = len(runtime_checks)

    headline = extract_headline_suspects(tree, total)
    for h in headline:
        msg = (f"headline literal {h['literal']!r} (line {h['line']})"
               + (" equals TOTAL check count INCLUDING [T]"
                  if h["counts_total_including_T"] else ""))
        if h["counts_total_including_T"]:
            violations.append("R4 " + msg)
        else:
            advisories.append("R4? " + msg)

    evidential = tag_counts.get("E", 0) + tag_counts.get("F", 0)
    return {
        "path": path,
        "convention": convention,
        "total_checks": total,
        "tag_counts": tag_counts,
        "untagged_count": total - sum(tag_counts.values()),
        "evidential_count_E_plus_F": evidential,
        "T_checks_excluded_from_headline": tag_counts.get("T", 0),
        "violations": violations,
        "advisories": advisories,
    }


def lint_file(path: Path) -> dict[str, Any]:
    return lint_source(path.read_text(encoding="utf-8"), str(path))


# ------------------------------------------------------------- self-test

GOOD_REGISTRY_SRC = '''
CHECKS = {
    "s1: setup identity": {"tag": "T"},
    "x1: real experiment": {"tag": "E"},
    "x1-fail: broken variant": {"tag": "F", "protects": "x1: real experiment"},
}
def main():
    def check(name, value, expected=True): ...
    check("s1: setup identity", True)
    check("x1: real experiment", True)
    check("x1-fail: broken variant", False, expected=False)
    print("evidential 2 of 3; [T] listed separately")
'''

UNTAGGED_SRC = '''
def audit():
    checks = {}
    checks["some_property_holds"] = True
    return checks
'''

ORPHAN_F_SRC = '''
def main():
    def check(name, value, expected=True): ...
    check("[E] a1: experiment", True)
    check("[F] zz9-fail: broken variant referencing no known checker", False, expected=False)
'''

T_HEADLINE_SRC = '''
def main():
    def check(name, value, expected=True): ...
    check("[T] t1: fixed by construction", True)
    check("[T] t2: fixed by construction", True)
    check("[E] e1: experiment", True)
    print("3/3 checks pass")
'''


def selftest() -> int:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    good = lint_source(GOOD_REGISTRY_SRC, "<good>")
    check("[E] compliant registry fixture lints clean (0 violations, "
          "evidential count 2, one [T] listed separately)",
          not good["violations"] and good["evidential_count_E_plus_F"] == 2
          and good["T_checks_excluded_from_headline"] == 1)

    untagged = lint_source(UNTAGGED_SRC, "<untagged>")
    check("[F] untagged legacy check IS reported "
          "(protects: R1/untagged detection, same lint_source path)",
          not any("untagged check" in a for a in untagged["advisories"]),
          expected=False)

    orphan = lint_source(ORPHAN_F_SRC, "<orphan>")
    check("[F] orphan [F] (references no existing checker id) IS flagged "
          "(protects: R2/F-reference rule, same lint_source path)",
          not any("does not reference" in v for v in orphan["violations"]),
          expected=False)

    theadline = lint_source(T_HEADLINE_SRC, "<t-headline>")
    check("[F] headline counting [T] checks IS flagged "
          "(protects: R4/headline hygiene, same lint_source path)",
          not any(v.startswith("R4") for v in theadline["violations"]),
          expected=False)

    check("[T] tag regex recognizes all three tags",
          all(TAG_RE.match(f"[{t}] x") for t in "TEF"))

    failures = []
    print("TEF LINTER SELF-TEST")
    print("=" * 74)
    n_t = n_e = n_f = 0
    for name, value, expected in checks:
        ok = value == expected
        n_t += name.startswith("[T]")
        n_e += name.startswith("[E]")
        n_f += name.startswith("[F]")
        print(f"{'PASS' if ok else 'UNEXPECTED'}  {name}: {value}")
        if not ok:
            failures.append(name)
    print(f"\nEVIDENTIAL CHECKS (headline): {n_e} [E] + {n_f} [F] = {n_e + n_f}")
    print(f"[T] theorem-consequence checks (no evidential weight): {n_t}")
    if failures:
        print("UNEXPECTED RESULTS:", failures)
        return 1
    print("All checks match expectations. Exit 0.")
    return 0


def main() -> int:
    args = [a for a in sys.argv[1:]]
    if "--selftest" in args:
        return selftest()
    strict = "--strict" in args
    paths = [Path(a) for a in args if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    worst = 0
    for path in paths:
        report = lint_file(path)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if report["violations"] and (
            strict or report["convention"] in ("registry", "inline-tags")
        ):
            worst = 1
        if strict and (report["advisories"] or report["untagged_count"]):
            worst = 1
    return worst


if __name__ == "__main__":
    sys.exit(main())
```

> Transcription note: the `ORPHAN_F_SRC` string above was tightened after the self-test run below (the tested version's orphan name read `"[F] zz9-fail: protects nothing declared here"` — behaviorally identical, since the rule keys on `"protects:"` with a colon, which neither wording contains; the paste avoids even the visual ambiguity). Everything else is byte-identical to what ran.

### Linter self-test receipt (real run, exit 0)

```
TEF LINTER SELF-TEST
==========================================================================
PASS  [E] compliant registry fixture lints clean (0 violations, evidential count 2, one [T] listed separately): True
PASS  [F] untagged legacy check IS reported (protects: R1/untagged detection, same lint_source path): False
PASS  [F] orphan [F] (references no existing checker id) IS flagged (protects: R2/F-reference rule, same lint_source path): False
PASS  [F] headline counting [T] checks IS flagged (protects: R4/headline hygiene, same lint_source path): False
PASS  [T] tag regex recognizes all three tags: True

EVIDENTIAL CHECKS (headline): 1 [E] + 3 [F] = 4
[T] theorem-consequence checks (no evidential weight): 1
All checks match expectations. Exit 0.
```

### Findings on the three existing fixtures (real run)

| Fixture | Convention detected | Total checks | [T]/[E]/[F] | Untagged | Violations |
|---|---|---|---|---|---|
| `tests/gate1_branch_preserving_functor.py` | legacy-scan | 39 (36 static + 3 dynamic f-string names) | 0/0/0 | **39 (100%)** | 0 (all advisory) |
| `tests/gate1_enriched_toy_nonthin_multiobserver.py` | legacy-scan | 58 (47 `checks[...]` + 11 `t[...]` teeth) | 0/0/0 | **58 (100%)** | 0 (all advisory) |
| `tests/krein_norm_link_probe.py` | inline-tags | 31 | **14 / 11 / 6** | 0 | **0** |

Detail (the demonstration the task asked for):

- **`gate1_branch_preserving_functor.py` — every check untagged.** The 39 include names the convention would classify very differently: `sigma_is_involution`, `strip_sigma_equals_strip_on_all_objects` are [T]-shaped (fixed by construction — currently indistinguishable from evidence); `CONTROL_constant_functor_rejected`, `CONTROL_profile_functor_rejected`, `cheat_plus_count_breaks_flip`, `CONTROL_decoration_detected_as_label_import` are [F]-shaped but carry no `protects` linkage; and `checks["_meta"]` is not a check at all yet sits in the check dict (a real hygiene catch). No headline `N/N` literal found (R4 clean).
- **`gate1_enriched_toy_nonthin_multiobserver.py` — every check untagged, including the entire 11-entry `TEETH_*` suite** (`TEETH_uncapped_depth_breaks_closure` … `TEETH_corrupt_breaks_product_consistency`), which is [F]-material with no machine-readable link to what each tooth protects. This is exactly the file where the swing-2 referee found "every check has a failing direction" false as a heading and several patch-layer positives definitional ([T]-shaped) — the linter shows the fixture currently gives a machine reader no way to see that: its **evidential count under the convention is 0 until tagged**. One dynamic name (`realization_strict_growth_{?}_present`) is reported as such.
- **`krein_norm_link_probe.py` — fully compliant**, zero violations: 31 checks, all tagged, all six [F]s reference an existing checker id (`a1-fail`→a1[E], `c2-fail`→c2[T], `c3-fail`→c3[E], `d1-fail`→d1[T], `d2-fail`→d2[E], `e2-fail`→e2[E]), honest headline (`17 evidential, 14 [T] listed separately`). The convention is a formalization of this file's practice, confirmed round-trip.

Advisory exit (0) on legacy files is deliberate: the report of untagged/vacuous checks IS the deliverable; `--strict` flips them to failures once fixtures adopt the convention.

---

## Honest notes and limitations

1. **First-run defect disclosures (expectations were NOT revised — the evaluations were, and the failed run is preserved).** The first harness run failed 4 checks: (a) the synthetic evaluation's only intermediate (trajectory sup from x0=1 under decay) is identically 1.0 — label-symmetric, so the vacuity guard refused to certify; (b) the GU-001 evaluation's pointer-granularity occurrence sets are swap-symmetric because the two labels co-occur in every packet string — the guard refused again. Both refusals were **correct behavior of the guard being delivered** — the (c)-clause caught two vacuous controls in its own maiden run. Fixes: record per-label final values; use character-offset occurrence sites. One linter self-test defect was also caught and fixed: an orphan [F]'s own id satisfied its own reference requirement (id set now built from non-[F] checks only).
2. **GU-001 executed neutrality is receiver-verdict-derivation grade, not source-computation grade.** The [E] on GU-001 is regression-grade (the packet was read before the evaluator was written; disclosed inline in the check name). The full-strength upgrade is blocked receiver-side for the three reasons in the first-class finding above; source-side ask (mailbox, not edits): a label-parameterized, runtime-closed evaluation entry point in any packet v0.3.
3. **Statically undecidable parts of the discipline.** The linter enforces *declaration* of tags and [F]→target linkage; it cannot statically prove an [F] exercises the same code path (behavioral) or that an [E]'s outcome was genuinely open at formalization time (epistemic). Those remain referee obligations; the convention makes them auditable.
4. **Linter scan heuristics.** Legacy scan keys on `check(...)` calls and subscript stores to dicts named `checks`/`teeth`/`t`; differently-named check dicts would be missed, and `checks["_meta"]`-style metadata is over-captured. F-string check names are reported as dynamic, not resolved. R4 headline detection is literal-based (`"N/N"` in string constants); computed headlines (`f"{n}/{n}"`) are not caught.
5. **Harness scope limits.** Label swapping is exact-string, so labels must not be substrings of one another (enforced, with an [F]); semantically equivalent paraphrases of a label are not swapped. `changed_intermediate_keys` diffs at top-level intermediate keys only. The evaluation is trusted to be pure; only input mutation via deep copies is defended.
6. **Neutrality-rule compliance of this work itself:** neither tool selects a branch; the GU-001 run returns NO_BRANCH_SELECTED under both labelings; no source claim, grade, or wording is touched; nothing was written to the repo (all artifacts prepared in the scratchpad; final paths proposed as `tests/neutrality_executed_harness.py` and `tests/tef_check_tag_linter.py`).
7. **Check tally for this rider (own-code discipline):** harness 3 [E] + 5 [F] = 8 evidential, 6 [T] listed separately; linter 1 [E] + 3 [F] = 4 evidential, 1 [T]. Headlines exclude [T] in both.

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs grades)

# Referee Report — Lane D-gate-tooling (Executed-Neutrality Harness + [T]/[E]/[F] Linter)

Everything embedded was re-executed independently (fresh files reconstructed from the report text, not the lane's scratchpad copies). Harness: exit 0, all 14 checks reproduce, **all four sha256 digests in the GU-001 receipt byte-identical to my run**. Linter selftest: exit 0, reproduces. Fixture scan: 39/58/31 totals, 0/0/0 tags on the two gate1 fixtures, 14/11/6 on krein, 0 violations — all reproduce. Packet facts verified directly: `C_good`/`C_path` counts 3/3, pointer co-occurrence true, `NO_BRANCH_SELECTED` both ways, fork-1 `selected` names neither label. Schema/evaluator claims verified against `interfaces/gate-run-v0.1.schema.json` (`additionalProperties:false`) and `tests/evaluate_gate_run.py` (exact field-set equality at top level, line 454, and on `neutrality_control`, line 399; `artifact_ref` is free text). The first-class finding's three blocking reasons verified against the pinned GU tree: `W210_decisive_bit_helmholtz.py` imports numpy and `gen_sector_bridge` (corroborating lane-1 Annotation E); none of W206–W211 has an argv/argparse label-parameterized entry point; both branches are hardcoded (`C_good = np.diag(...)`, W208 line 312). Repo untouched (git clean), mutation only on an in-memory copy, mailbox routing proposed for the source-side ask, ADAPTER2-01 uncontradicted. The transcription note on `ORPHAN_F_SRC` is exactly accurate: diff against the lane's actual run file shows precisely the one disclosed difference, original wording verbatim, behaviorally identical (both versions exit 0).

## 1. VERDICT: SOUND-WITH-CORRECTIONS

The tools work as claimed, the [F]-controls are genuine same-path controls, the bounding finding is real and verified, and no claim moves. But the report contains two false factual statements in its demonstration section and one unverifiable process claim at the anchor of its own defect-disclosure story.

## 2. Defects

**D1 — MODERATE — false counts in the fixture-findings table, contradicted by the lane's own receipt.** The report says the enriched fixture has "58 (47 `checks[...]` + 11 `t[...]` teeth)" and "the entire 11-entry `TEETH_*` suite." Actual (my re-run, AND the lane's own preserved `lint_final.txt`, AND swing-2 SYNTHESIS which says "18 real TEETH"): **40 `checks[...]` + 18 `t[...]`; 18 TEETH entries.** Total 58 is right; the split and the suite size are wrong. The substantive conclusion (100% untagged, evidential count 0 under the convention) is unaffected — but a counting-hygiene deliverable miscounting its own demonstration, against its own receipt, is exactly the failure class it polices.

**D2 — MODERATE — nonexistent "honest headline" attributed to the krein fixture.** "honest headline (`17 evidential, 14 [T] listed separately`)" — no such headline exists. `krein_norm_link_probe.py` prints **no count headline at all** (verified by reading and running it), and the string appears nowhere in the fixture or lane-3's report. The numbers are the linter's own computed fields (11+6=17, 14) rendered in backticks as if quoting the fixture's practice. This inflates "the convention is a formalization of this file's practice, confirmed round-trip": what round-tripped was tags and [F]-references, not headline practice.

**D3 — MODERATE — unverifiable process claim: the failed first run is not preserved anywhere.** The docstring says "The failed first run is embedded in the exploration notes"; note 1 says "the failed first run is preserved." No exploration-notes file exists (the repo was correctly not written to), the report does not embed the failed run, and both preserved scratchpad receipts (`harness_run2.txt`, `harness_final.txt`) contain zero UNEXPECTED lines. The claim "expectations were NOT revised — the evaluations were" therefore rests on narrative, not a receipt — the precise gap this harness exists to close.

**D4 — MINOR — [E]-grade asymmetry in the harness's own headline.** By the house definition ([E] = outcome not fixed at formalization time), the two synthetic [E]s were co-authored with the evaluation and revised until the guard passed — the same regression grade as the GU-001 [E], but only GU-001 carries the inline disclosure. "3 [E]" tag-counts correctly but all three are regression/demo-grade; note 1 partially discloses this, the headline does not.

**D5 — MINOR — [T]-check name/code mismatch.** "[T] GU-001: both branch labels occur in the packet" is computed as `all(gu_receipt["swap_map"]) and swap_changed_subject`. `all(swap_map)` is vacuously true (truthiness of nonempty string keys) and `swap_changed_subject` proves only that *at least one* label occurs. The named fact is true (independently verified, 3/3) but the check does not test it. No evidential weight claimed, still a discipline lapse inside the discipline tool.

**D6 — MINOR — receipt block not byte-faithful.** The "Worked-example receipts (real run, final)" GU JSON was reflowed: the code prints `indent=2`, which puts `changed_intermediate_keys` and `swap_map` on multiple lines; the report compacts them. All values and digests match exactly, but a report holding others to byte-level receipt fidelity should not silently reformat its own.

**D7 — MINOR — latent, undisclosed linter defect: R4 is toothless on legacy files.** In `main()`, an R4 headline **violation** in a legacy-scan/mixed-convention file never sets a nonzero exit without `--strict` (`worst=1` requires registry or inline-tags convention). Dishonest headlines live today precisely in legacy fixtures, so the one rule the report classes as a violation cannot fail a legacy file's lint. Limitation note 4 discloses other heuristics but not this.

## 3. Corrected wording

1. Enriched-fixture row: "58 (47 `checks[...]` + 11 `t[...]` teeth)" → **"58 (40 `checks[...]` + 18 `t[...]` teeth)"**; "the entire 11-entry `TEETH_*` suite" → **"the entire 18-entry `TEETH_*` suite"**.
2. Krein row: "honest headline (`17 evidential, 14 [T] listed separately`)" → **"no count-headline literal at all (R4 vacuously clean); the linter computes 17 evidential (11 [E] + 6 [F]) with 14 [T] excluded"**.
3. Note 1 and docstring: "the failed first run is embedded in the exploration notes / is preserved" → **"the failed first run is described but not preserved; no receipt of it survives, so the no-expectation-revision claim is attested only by code comments and this narrative"**.
4. Rider tally (note 7): "harness 3 [E] + 5 [F] = 8 evidential" → **"harness 5 genuine [F] + 3 regression/demo-grade [E] (all three [E]s authored or revised with knowledge of the subject; disclosed inline for GU-001 only) = 8 tagged-evidential"**.

## 4. Grade the main result actually earns

**Exploration-tier, tool-demonstration grade — earned.** Specifically: (a) the RECORDED→EXECUTED upgrade is real, and the vacuity guard demonstrably has teeth (all five [F]s verified to exercise the same code path they protect; the guard's two maiden-run refusals are corroborated by code structure even though the run receipt is missing, D3); (b) the GU-001 executed-neutrality result earns exactly its most careful self-description and no more: **regression-grade, receiver-verdict-derivation scope only** — it adds essentially no new evidential weight about GU-001 and does **not** discharge lane-1's D3, whose source-computation-grade version remains blocked; (c) the genuinely valuable result is the verified **bounding finding** (source-side label-parameterized entry point required for full-strength executed neutrality — all three blocking reasons independently confirmed against the pinned GU tree), properly framed under Failure-Preservation; (d) the linter's fixture findings are correct in substance with the D1/D2 corrections applied. The report's own grading is honest at the check level; the overclaims are in the demonstration prose, not the claims ledger.

## 5. Twin-lane implication statement

**This lane is not a 2-prime twin lane and models no T26 content.** It makes no class-boundary claims (nothing here requires mechanical decidability adjudication) and asserts no TaF FORMALISM correspondence, so the T26 field-by-field conformance test is N/A. Implication for any other lane's expected result: **neutral — nothing in this lane constrains either 2-prime twin's outcome in either direction.** One cross-lane operational note for the orchestrator: if the twin lanes' fixtures are to be held to the [T]/[E]/[F] convention using this linter, D7 means an R4 headline violation in a not-yet-converted fixture will lint-report but still exit 0 unless `--strict` is passed — do not treat a bare exit 0 from this linter as headline-hygiene clearance on legacy files.