---
artifact_type: run_plan_and_receipt
status: complete
run_id: RUN-20260722-204348-possibility-to-capability-progress
parent_run_id: RUN-20260722-204348-repository-work-cycle-nbl-hourly
owner_id: possibility-to-capability
workflow: repo-progress-run
workflow_revision: sha256:dc56a1de32775eaccbe13353a9cad47a134f4cf13d94c9c11b8b67055d256998
mode: execute
lane_id: 1
starting_revision: 310dd8f
---

# Capability-Diagnostic Instrument v0.1 MVP

## Formal phase packet

Selected work: `P2C-CAPABILITY-DIAGNOSTIC-INSTRUMENT`. Write boundary: this
receipt, `tools/`, the historical classifier wrapper, test and root orientation,
`steward/research-portfolio.json`, and `LANE-STATE.yaml`. Method refs: `[]`.
The checkout opened clean and even with the owner claim held. Lane 1, control,
emergency state, and the material Discovery handoff were revalidated before
each effect.

## Objective and plan

Deliver one executable v0.1 MVP from the already-tested evaluator without
changing classification semantics:

1. Move the evaluator implementation to a stable `tools/` command.
2. Preserve `tests/classify_transition.py` as the sole compatibility wrapper so
   historical commands and imports continue to work without duplicated logic.
3. Document one runnable example, evidence obligations, and nonclaims.
4. Compare canonical and compatibility JSON output and rerun the hostile
   security transfer regression.
5. Bank the MVP and remove it from repeat-hourly selection.

## Execution and validation

- `python tools/capability_diagnostic.py tests/fixtures/transition-diagnosis-v0.1-valid.json`: pass.
- `python tests/classify_transition.py tests/fixtures/transition-diagnosis-v0.1-valid.json`: pass; output exactly matches the canonical command.
- `python tests/security_transfer_breaker.py`: pass, `10 [E] + 4 [F]`, with
  label invariance and the provisional/non-universality nonclaim intact.
- JSON and YAML state parse: pass.
- Unique portfolio ranks: pass; no stale spent-fixture hourly selection remains.
- `git diff --check`: pass.

## Receipt

- Created: `2026-07-22T21:02:00-05:00`.
- Phase result / service contribution: `progressed` / `progressed`.
- Required graph attested: yes. Required flows:
  `standard-run-safety-check`, `select-lane`, `create-run-plan`,
  `revalidate-lane-selection`, `append-run-receipt`.
- Conditional flows: `rerank-next-work`, `refresh-lane-state`, and
  `classify-artifact-disposition`; exceptions: none.
- Artifact disposition: code, documentation, owner state, and this receipt are
  versioned repository knowledge. No generated output was staged.
- Method refs / effect: `[]` / `null`.
- Actual effects: one canonical reusable command, one compatibility wrapper,
  one tool README, root/test orientation, and owner state/portfolio closeout.
- Scientific boundary: no evaluator semantics, source truth, hierarchy,
  universality grade, claim status, canon, domain-2 authorization, deployment,
  publication, or public posture moved.
- Next handoff: use the command on real evidence-bearing assessments; reopen
  only on an observed input, usability, evidence-boundary, packaging, or
  regression failure, or separately authorized new-domain demand.
