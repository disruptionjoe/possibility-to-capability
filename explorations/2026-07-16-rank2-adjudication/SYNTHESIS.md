---
artifact_type: exploration
status: complete
governance_role: rank2_adjudication_synthesis
constitutional: false
created: 2026-07-16
---

# 2026-07-16 Rank-2 adjudication — synthesis (referee-corrected; the attached REFEREE-REPORT.md GOVERNS)

The run the runway was built for: the preregistered Rank-2 access-versus-capability
paired-intervention adjudication (RANK2-PR-001), executed on sovereign-issued frozen
evidence after Joe's pre-authorization (direct chat, 2026-07-16) and TI's sovereign
adoption completed the runway's last open step.

Grade: EXPLORATORY, receiver-owned. No source claim moves. bar(b), H59, Krein
positivity, and physical issuance remain OPEN. ADAPTER2-01 governs.

## What ran

| phase | artifact | receipt |
|---|---|---|
| 1. Packet acceptance | TAF-001 accepted + imported (`packets/imports/TAF-001/`); TI-PIT-002 accepted + imported (`packets/imports/TI-PIT-002/`) | all acceptance gates PASS per both import records; commit b28d28e |
| 2. Adjudication | `rank2_adjudication_harness.py` on the frozen blobs; results at the pre-declared path `explorations/2026-07-16-rank2-preregistration/RANK2-PR-001.results.json` | 9 [E] + 4 [F] all passing, 2 [T] excluded from headline; commit ff5e7fc |
| 2b. Mechanism | `tests/prereg_verify.py` against the real repo | ALL SEVEN GATES PASS, `valid: true`, exit 0 — necessary, NOT sufficient |
| 3. Referee | `REFEREE-REPORT.md` (governs) | SOUND-WITH-CORRECTIONS; five corrections R-D1..R-D5 applied before the results commit |

## Check-by-check (frozen expectations vs observed)

| check | expected | observed | verdict |
|---|---|---|---|
| c1 TaF issuance | ISSUED | ISSUED (verified two-commit freeze) | PASS |
| c2 TI issuance | ISSUED | ISSUED (verified two-commit freeze) | PASS |
| c3 Frame R independent re-freeze | FROZEN_INDEPENDENT | FROZEN_INDEPENDENT for every case the frame scores; TI frame leg excluded (S5 + carried quarantine) | PASS with declared exception (R-D1) |
| c4 access-pair profile | ROBUST_ZERO | ROBUST_ZERO on both branches, full frozen classes | PASS |
| c5 capability-pair profile | ROBUST_NONZERO | NOT_APPLICABLE (no sovereign declaration matches the trigger vocabulary) | N/A — construal fork preserved (S3) |
| c6 mixed sector present | TRUE | FALSE on admissible evidence (robust to the quarantine) | MISS, preserved |
| c7 frame functionality | TRUE | TRUE | PASS |
| c8 label neutrality | TRUE | TRUE (with demonstrated failing direction) | PASS |
| c9 shared vocabulary | TRUE | TRUE (per branch) | PASS |

## The verdict (per the frozen outcome mapping; referee-corrected citable form)

**No Rank-2 outcome is licensed, and this is construal-invariant.** Rule 3
(FAVORS_CANDIDATE — reachable only via the completion-robustness discriminator)
does not fire because c5 is NOT_APPLICABLE; rule 4 (FAVORS_RIVAL) does not fire
because robustness failed on no declared-pure pair; rule 5 (CONSTRUCTION_FORK /
operational-context relativism) does not fire because no admissible
RELATIVE-with-disagreement pair exists; rules 6 and 7 do not fire (c9 TRUE;
pairs distinguishable). Under the strict-global c3 reading the run is instead
invalid before scoring; under the factor-construal of c5 the counterfactual is a
preserved SPLIT (TAF: FAVORS_CANDIDATE pure-sector-only; TI: quarantine-attenuated
FAVORS_RIVAL pressure) that stop S3 forbids resolving. Every path ends at: **Rank
2 remains undischarged; no verdict favors anyone.**

## What IS established (exploration tier, receiver-owned, single-branch each)

1. **The interface works end-to-end on real sovereign evidence.** Two sovereign
   repositories issued conforming frozen packets that survived the full
   acceptance-gate chain, and the preregistered receiver machinery (frozen
   expectations -> sovereign evidence -> mechanical classification -> frozen
   outcome mapping -> mechanical prereg verification) executed without manual
   discretion at any scored step. The blocked-forever null rival is partially
   falsified.
2. **Sources can issue genuinely pure access pairs** — the evidential content
   the prereg's c4 note named. Both declared access pairs are completion-ROBUST
   zero at full frozen-class strength, on two independent branches.
3. **A non-monotone access fact**: TAF ALPHA's access ENLARGEMENT destroys a
   task (tau5) while creating another — access widening is not monotone under a
   threshold-with-competing-values reconstruction rule. Receiver-owned,
   frame-neutral, single-branch.
4. **A non-monotone completion-relativity fact**: TI BETA's profile is 0 at the
   actual completion, nonzero at the middle completion, and 0 again at the top —
   the delta is visible only at an INTERMEDIATE access level. Frame-neutral,
   quarantine-restricted to neutral use, single-branch.
5. **The prereg mechanism did its job in both directions**: it blocked the
   receiver from selecting a favorable c5 construal after seeing that the
   construal choice decides between "no outcome" and "split with a
   candidate-favoring sector" — precisely the discipline the mechanism exists to
   impose.

## What is NOT established

- No access/capability boundary claim, in either direction. The capability side
  of the discriminator was never exercised.
- No credit or debit to Frame N or Frame R. Frame R's central prediction remains
  untested on its own stated scope (realistic interventions; the designed-pure
  fixtures are outside it; the one RELATIVE pair is zero-credit under R's own
  P4 rule).
- No mixed-sector existence claim. c6 missed; equally, Frame R's
  mixed-sector-dominance forecast found no admissible support.
- Nothing about physics, GU-001, bar(b), H59, Krein positivity, or physical
  issuance. No source claim status moved anywhere.
- The prereg-verify PASS is committed-order and byte-identity proof only.

## Why no new-prereg was smuggled in

The frozen expectations anticipated exactly this failure mode (retained fork 2:
mismatched checks are scored NOT_APPLICABLE, never reinterpreted; reopener 1:
material semantic mismatch requires a NEW prereg id committed before the next
run). This run therefore ends the RANK2-PR-001 lifecycle: exercised, verified,
not superseded in place. Any successor capability-side test requires
`RANK2-PR-002` (or later) with factor-vocabulary-aligned checks, committed
phase-1 before its run, plus evidence free of the Frame-R-advocate quarantine.

## Receiver-state consequences (only as the frozen mapping licenses)

- Rank-2 status moves from "BLOCKED at the sovereign-issuance prerequisite" to
  "adjudication executed; UNDISCHARGED; no outcome licensed; prerequisite gap
  narrowed to (i) factor-vocabulary-aligned prereg, (ii) uncontaminated
  rival-frame/case pairing." Recorded in `steward/research-portfolio.json`.
- Per `governance/HARD-CORE.md` lane doctrine: the Rank-2 runway was the belt
  lane that legitimately LED; it is now RESOLVED. **Priority reverts to the core
  wager: P2C-REAL-PHYSICAL-WITNESS** (already rank 1 in the portfolio). The next
  Progress swing belongs to the real physical witness, not to Rank-2 successor
  machinery; the successor prereg is banked as a belt item to be picked up when
  a matching sovereign pair exists.
- No decisive-tests scorecard rewrite: the 2026-07-16 decisive-tests SYNTHESIS
  remains the frozen record of its own swing; this file is the current state.

## Deviations and preserved constraints (full list in results.json)

d1 c5 construal fork preserved (S3); d2 c6 miss preserved; d3 TI frame leg
quarantine-blocked (preserved constraint, not routed around); d4 c3 construal
declared with construal-invariant verdict (R-D1); d5 TAF non-monotone access
delta noted; d6 completion-class interval-dependence audited and named as attack
surface (J2), out-of-class probe audit-only.
