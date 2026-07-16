# Two-Phase Preregistration Convention v0.1

Status: provisional repo-owned process interface. It governs receiver-side
runs in this repository; it is not canon and confers no scientific pass.

## Why

Three referees across two swings independently flagged the same defect: the
receiver's expectations, judgment calls, and rival forecasts were not
mechanically provably frozen before outcomes were inspected. Rank 1's
FAVORS_CANDIDATE is conditional partly on exactly this; Ranks 2-4 are gated
on it alike. Prose claims of "preregistered" are not receipts. Git history
is.

## Construction

A preregistered run is TWO artifacts in TWO commits, hash-linked:

1. **EXPECTATIONS artifact** (`<run-id>.expectations.json`), committed in
   its own commit BEFORE any results exist. It carries:
   - `declared_checks`: every check the run will evaluate, each with a
     `check_id` and an `expected` value (the key is literally named
     "expected", per the swing-2 referee's EXPECTED_* naming demand — no
     result-shaped constant may be smuggled in under a neutral name);
   - `frozen_judgment_calls`: every discretionary construal ruled in
     advance (the class of un-preregistered discretion the Rank-1 referee
     enumerated: ownership construals, chain/branch ids, annotation
     choices, neutrality-artifact choices);
   - `rival_forecasts`: what each named rival predicts for the same checks;
   - `stop_conditions`: binding, non-vacuous stop rules (a constant-True
     detector is the burned cannot-fail class; it fails review).

2. **RESULTS artifact** (`<run-id>.results.json`), committed strictly
   afterward, carrying `prereg_ref` with the expectations file's path, its
   git BLOB id as committed, and its commit hash, plus per-check `observed`
   values and `deviations`.

Artifacts co-locate with the run they govern (spec lives with its
consumer), e.g. `explorations/<date>-<topic>/<run-id>.expectations.json`.

## Mechanical verification

`tests/prereg_verify.py` proves from git history alone (gates P1-P7):
results committed and parseable with a complete prereg_ref (P1); the
claimed expectations commit contains the expectations path (P2); the blob
at that commit equals the blob the results claim to have been tested
against (P3); the expectations commit is a STRICT ancestor of the
results-introducing commit — the same commit, or results-first, fails
(P4); the results commit does not touch the expectations path (P5);
exactly one commit in all of history touches the expectations path and the
HEAD blob still equals the registered blob — post-hoc edits, amends, and
deletions fail (P6); the expectations declare nonempty checks with
expected values, frozen judgment calls, rival forecasts, and stop
conditions (P7).

## Amendment policy

A committed expectations artifact is immutable. A revision gets a NEW file
and NEW prereg id, committed before the corresponding run; the superseded
artifact stays in history. Any other edit path is a P6 failure by design.

## Falsifiers (of the mechanism, not of any physics)

- A pair that violates temporal ordering verifies as valid.
- A post-hoc edit to a committed expectations artifact goes undetected.
- Results verified against different expectations bytes go undetected.
- History rewriting (rebase/force-push) can silently re-order the two
  commits: the verifier is sound relative to the integrity of the local
  history it reads. Pushing both commits promptly (this repo's
  commit+push default) and never force-pushing is the standing guard;
  cross-checking against the remote's reflog or a third-party timestamp
  is the escalation if that guard is ever in doubt.

## Nonclaims

- A prereg-verify PASS proves committed-order and byte identity only. It
  does not make the declared checks good science, the stop conditions
  adequate, or the observed values true.
- The mechanism does not retroactively upgrade any past run. The GU-001
  gate-run's partial ex-ante evidence (gates/evaluator committed ~17h
  before the source bundle; annotations A/B/C + pin committed before gate
  outcomes) remains historical evidence, not a two-phase receipt.
