---
artifact_type: exploration
status: phase-1 complete (expectations frozen; awaiting sovereign issuance)
governance_role: rank2_preregistration_receipt
constitutional: false
created: 2026-07-16
---

# RANK2-PR-001 — receiver expectations for the Rank-2 adjudication (phase 1 executed)

Runway status: this executes step (3) of the Rank-2 runway named in
`explorations/2026-07-16-northstar-unblock/SYNTHESIS.md` — the receiver's
expectations artifact went through phase 1 of
`interfaces/two-phase-preregistration-v0.1.md` BEFORE any sovereign outcome
was seen. Steps (1) TaF/TI sovereign adoption and (2) independent Frame-R
re-freeze remain open and are owned elsewhere; step (4), the preregistered
run itself, may execute only after (1)-(3) and must commit its results to the
pre-declared path below.

## Frozen artifact

- Expectations: `RANK2-PR-001.expectations.json`
- Phase-1 commit: `49baf1fa9094554a06cf27a8444ca2ec4a5ecf86` (sole commit
  touching the file; it is immutable — any revision is a NEW file with a NEW
  prereg id)
- Git blob: `55c260dd35c93236d3fd387f06ad388b9df4a693`
- Pre-declared results path (future run only):
  `explorations/2026-07-16-rank2-preregistration/RANK2-PR-001.results.json`

The future results artifact MUST carry this `prereg_ref`:

```json
{
  "prereg_id": "RANK2-PR-001",
  "expectations_path": "explorations/2026-07-16-rank2-preregistration/RANK2-PR-001.expectations.json",
  "expectations_git_blob": "55c260dd35c93236d3fd387f06ad388b9df4a693",
  "expectations_commit": "49baf1fa9094554a06cf27a8444ca2ec4a5ecf86"
}
```

## Verifier receipts (verbatim, 2026-07-16)

`python tests/prereg_verify.py --selftest` — exit 0:

```
PREREG VERIFY SELF-TEST
==========================================================================
PASS  setup: selftest fixture repos build with distinct commits: True
PASS  g1: compliant two-phase pair verifies with every gate PASS: True
PASS  g1-fail-same-commit: joint expectations+results commit is rejected (protects: g1 via the strict-ordering and separation gates, same verify_prereg path): False
PASS  g1-fail-amended: post-results edit to expectations is detected (protects: g1 via the immutability gate, same verify_prereg path): False
PASS  g1-fail-wrong-blob: results citing a different expectations blob are rejected (protects: g1 via the blob-match gate, same verify_prereg path): False

EVIDENTIAL CHECKS (headline): 1 [E] + 3 [F] = 4
[T] theorem-consequence checks (no evidential weight): 1
All checks match expectations. Exit 0.
```

Full verifier against the pre-declared results path in the REAL repo — exit 1
with `P1 RESULTS_COMMITTED: FAIL, "results path has no commit history"`,
`valid: false`. This FAIL is the CORRECT phase-1 state: it is the mechanical
proof that no results existed when the expectations were frozen. A phase-1
"PASS" here would mean the prereg was contaminated.

Rehearsal proof of the expectations-side gates (throwaway clone at the session
scratchpad, placeholder results committed there only, never in the real repo):
all seven gates PASS, `valid: true`, exit 0 — P2/P3 (blob at commit matches),
P4 (strict ordering), P5 (separation), P6 (immutable, sole commit
`49baf1f...`), P7 (shape: nonempty declared checks with `expected` values,
frozen judgment calls, rival forecasts, stop conditions). The rehearsal clone
is disposable evidence that the frozen artifact will verify once real results
land; it confers nothing else.

Billing per the mechanism's Nonclaims: a prereg-verify PASS is NECESSARY, NOT
SUFFICIENT. Nothing here is a scientific pass; Rank 2 remains `BLOCKED` at the
sovereign-issuance prerequisite; no source claim moves; bar(b), H59, Krein
positivity, and physical issuance remain OPEN; ADAPTER2-01 governs.

## Firewall declaration (house method: declared reads)

Statement: no file under `system/mailboxes/possibility-to-capability/` (or any
other CapacityOS mailbox), no file in the Time-as-Finality repository, and no
file in the Temporal-Issuance repository was read by this run. Additionally,
the receiver-side draft evidence files
`explorations/2026-07-16-northstar-unblock/lane-B-taf-source-packet.md` and
`explorations/2026-07-16-northstar-unblock/lane-C-frame-r-and-ti-case.md` were
deliberately NOT read, so these expectations are blind both to sovereign
returns and to the draft evidence bytes (frozen judgment call J6).

Declared reads (complete, in order):

1. `AGENTS.md`
2. `governance/CHARTER.md`
3. `steward/README.md`
4. `interfaces/two-phase-preregistration-v0.1.md`
5. `tests/prereg_verify.py`
6. `explorations/2026-07-16-northstar-unblock/SYNTHESIS.md`
7. `explorations/2026-07-16-decisive-tests/lane-R2-access-capability-pilot.md`
   (comparison contract + governing referee report)
8. `explorations/2026-07-16-northstar-unblock/lane-A-prereg-and-transition.md`
   (partial: lines 1-983)
9. `experiments/2026-07-14-ranked-decisive-test-program-v0.1.md`
   (partial: Rank-2 section, lines 100-179, plus a grep for Rank-2 mentions)

Directory listings/globs touched only file NAMES (repo root, `experiments/`,
`explorations/2026-07-16-*` lane filenames) plus git metadata (log/status/
branch/remote). No mailbox path was listed or read. If any of the above had
contained sovereign TaF/TI return content, this prereg would have been
declared contaminated and aborted instead of committed.

## What reopens this

Per the artifact's `reopeners`: material sovereign changes to case semantics
or record-channel inventory, a non-equivalent independently frozen Frame R, or
a revised Rank-2 outcome menu — each requires a NEW prereg id committed before
the run; `RANK2-PR-001.expectations.json` stays in history untouched either
way.
