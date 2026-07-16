---
artifact_type: exploration
status: complete
governance_role: second_standard_local_read
constitutional: false
created: 2026-07-16
work_item: P2C-CROSS-REPO-ADJUDICATION
tier: provisional_synthesis
verification: tests/p2c_second_standard_adjudication.py
---

# Second-standard local read: P2C-W1 under CompletionClass-P2C v0.1

**Tier and guards.** Exploration / finite fixture synthesis. This changes no
source-repo claim, verdict, canon, public posture, finality claim, or source
status. The imported TAF-002 and TI-WFA-001 packets are read-only evidence;
the receiver-owned move here is the local substitution of
CompletionClass-P2C v0.1 for the earlier TI-v1-relative completion leg.

## Objective

Run the re-armed `P2C-CROSS-REPO-ADJUDICATION` checkpoint named by the
portfolio: re-read the unchanged P2C-W1 chain under P2C's own derived
completion firewall and the carrier-neutral adapter.

The checkpoint is local. It sends no proposals, requests no new source return,
and does not rerun the superconducting/BEC adapter or BEC witness swing.

## Inputs

- Frozen witness: `exports/witness/P2C-W1-superconducting-ring-v0.1/`.
- Imported sovereign returns:
  `packets/imports/TAF-002/` and `packets/imports/TI-WFA-001/`.
- Prior combining adjudication:
  `explorations/2026-07-16-cross-repo-adjudication/`.
- P2C completion class:
  `explorations/2026-07-16-completion-class-firewall/` and
  `tests/p2c_completion_class_closure.py`.
- Carrier-neutral adapter:
  `explorations/2026-07-16-witness-boundary-adapter/` and
  `tests/witness_boundary_adapter.py`.

## Executable read

`tests/p2c_second_standard_adjudication.py` performs the local read:

- confirms that TAF-002, TI-WFA-001, and the witness bundle still name the
  unchanged P2C-W1 object;
- preserves source sovereignty and import non-promotion;
- keeps C1 task-semantics transfer as a condition, not a silent upgrade;
- substitutes CompletionClass-P2C v0.1 for the C2 completion leg;
- checks that certified containment does not become operational absorption;
- checks that the local-completion D2 gap is closed at the same finite-model
  grade at which it was opened;
- carries the tau_P metastability cap;
- keeps the context-individuation fork open; and
- keeps finality as `NOT_REACHED`.

Validation result:

```text
disposition: SECOND_STANDARD_CONFIRMED_SCOPED_SURVIVOR_CLASS_SPLIT
completion leg: PASS_P2C_DERIVED_FIREWALL
adapter residual: CERTIFIED_CONTAINMENT_ONLY
composite local absorbers: 0
finality: NOT_REACHED
```

The headline is 11 `[E]` + 5 `[F]` = 16 evidential checks, with one `[T]`
setup check excluded.

## Result

**Disposition: `SECOND_STANDARD_CONFIRMED_SCOPED_SURVIVOR_CLASS_SPLIT`.**

The earlier scoped survivor does not depend only on TI v1's table. Under
P2C's own model-relative derived firewall:

- the certified whole-family contains the witness but does not operationally
  absorb it;
- after-fact hull totality remains capped below operational strength;
- no sequential composite of local completions absorbs the P2C-W1 QIP
  staircase at the declared model granularity;
- the adapter reports `CERTIFIED_CONTAINMENT_ONLY`, not a capability verdict;
  and
- the class split remains intact: operational survival and containment
  absorption are different conclusion classes.

This confirms the local C2 substitution and closes the prior D2 composition
gap at the same finite-model / literature-grade level. It does not prove a
real capability enlargement, does not eliminate C1 or C4, and does not reach
finality.

## Conditions that remain binding

- **C1 task semantics:** TaF's native reconstructibility semantics still map
  into P2C's Capability type only at definitional-draft grade.
- **C2 standard relativity:** narrowed from TI-v1-relative to P2C's three
  instrument-admissibility axioms: A-FRAME, A-UNIF, and A-CAL. A rival
  standard may reject those axioms, but then it is outside this diagnostic
  instrument.
- **C3 tau_P:** persistence remains metastability-capped; tau_Q and tau_I are
  still the stronger carriers.
- **C4 individuation fork:** the one-context whole-family reading remains
  materially admissible. This run does not force the two-context frame.
- **F5 watch:** the result is still frame-indexed; it does not yet provide an
  invariant quotient across materially admissible frames.

## What this closes

- The re-armed local second-standard read of unchanged P2C-W1 is complete for
  current inputs.
- The old D2 local-composition attack is no longer an untested gap at this
  model grade.
- The C2 flank no longer rests solely on TI's v1 table; P2C now has a local
  derived firewall with the same class split.

## What remains open

- No new frozen witness with sovereign returns exists yet.
- C1 task-semantics transfer has not been independently tested.
- C4 cross-frame transfer remains live.
- The topological-order Alternate B witness remains the cleanest next reach
  swing for testing whether the local-invariance leg survives a harder domain.

## Next-work handoff

Durable priority owner remains `steward/research-portfolio.json`.

| rank | eligible lane or work item | why now | dependencies / gates |
|---:|---|---|---|
| 1 | `P2C-REAL-PHYSICAL-WITNESS` Alternate B | current P2C-W1 local chain is second-standard confirmed; next Progress should test a harder physical witness / cross-frame transfer | literature-grade freeze; preserve no-verdict posture |
| 2 | C1 task-semantics mapping test | cheap Track-2 de-risking of the remaining receiver-owned mapping condition | must not promote TaF semantics into P2C canon |
| 3 | `P2C-CROSS-REPO-ADJUDICATION` new input only | current unchanged P2C-W1 read is complete | re-open only for a new frozen witness with sovereign returns or a failed C1/C4 transfer |
