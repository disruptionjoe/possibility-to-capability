---
artifact_type: exploration
status: provisional
created: 2026-07-16
construction: finite_binary_block_switch_fixture
evidence_grade: exhaustive_finite_toy
governance_role: progress_synthesis
constitutional: false
---

# Per-Block Observability Fixture

## Objective

Lane 1 item `4a` asks whether the boundary-switch interpretation has any
observable content once absolute sign labels dissolve. The finite fixture
`tests/per_block_observability_fixture.py` tests the switch-profile claim: a
single global switch should be hidden by the global flip quotient, while
multiple block-local choices should be visible through relative alignment.

The model is deliberately small. A configuration is a block sign assignment
`{-1,+1}^n`. The global flip negates every block and represents absolute label
reversal. Independent per-block flips represent multiple local switch choices.
Pairwise products form the relative-alignment profile.

## Result

At finite binary toy grade, the discriminator behaves as the interpretation
requires:

- for `n=1`, the only global-flip-invariant Boolean observables are constants;
- for `n=2` and `n=3`, the pairwise relative-alignment profile separates
  global-flip orbits;
- for `n=3`, every global-flip-invariant Boolean observable factors through
  the pairwise profile;
- a pairwise alignment observable is global-flip invariant and sensitive to
  flipping either endpoint block independently; and
- independent per-block flips change the relative profile.

Interpretation: a one-global-bit switch is behind the toy opacity horizon, but
multiple block-local choices can have neutral observable content as relative
alignment.

## Controls

Three failing-direction controls price the result:

- an absolute block selector violates global invariance;
- the single-block model has no choice-sensitive invariant observable; and
- a first-pair-only profile fails to separate all `n=3` global-flip orbits.

These controls prevent the fixture from counting an absolute label, a vacuous
one-block system, or an incomplete relative profile as evidence.

## Scope

This is toy-grade and binary. It does not identify the switch operator, prove
observer agency, settle A versus B/C, establish physical issuance, move GU,
TI, TaF, or WI-069 source truth, or promote any claim. It only supports the
operator-opacity subclaim that multiplicity is the observable part of the
switch profile, not operator identity.

The fixture is compatible with the relational-dissolution result: absolute
labels still dissolve; what survives is relative block alignment.

## Next-Work Handoff

- current work: per-block observability fixture
- current disposition: `ENDPOINT_POSITIVE_TOY`
- durable priority owner: tracked progress-lane surface plus
  `steward/research-portfolio.json`
- recommendation status: advisory

| rank | eligible lane or work item | why now | dependencies / gates |
|---:|---|---|---|
| 1 | Transition-diagnosis run on GU-001-GR-001 | The concurrent decisive-tests swing made this the cheap serialization step blocking any non-provisional Rank-1 update | receiver-owned classification only; no source claim movement |
| 2 | Two-phase preregistration mechanism | Multiple recent referees flagged missing expectations-before-results discipline, and it gates future decisive tests | process upgrade only; avoid rewriting past evidence |
| 3 | Composition-compatibility descent fixture (`4b`) | This run closed `4a`; the paired A-prime claim still needs the morphism-level descent/control test | must not infer a natural source of the injected bit from descent alone |
| 4 | Weakest-oracle theorem | Relational dissolution plus per-block observability sharpen the minimal flip-odd primitive question | must distinguish "minimal selector" from "physically legitimate primitive" |

- recommended next: transition-diagnosis run on GU-001-GR-001.
- switch signal: a native physical or process-level primitive that breaks flip
  symmetry without merely carrying an orbit representative.
- strongest alternative: two-phase preregistration mechanism, because it is
  now a repeated referee repair and converges with Lane 1 housekeeping.
- overturning evidence: a failed `4a` control, a source-issued frozen return,
  or a portfolio reconciliation that explicitly re-selects the physical
  boundary adapter/witness lane.
- steward reconciliation needed: yes; `steward/research-portfolio.json` still
  names the older physical boundary adapter item as top durable portfolio work,
  while the tracked progress lanes now carry the current theorem-hardening
  queue.
