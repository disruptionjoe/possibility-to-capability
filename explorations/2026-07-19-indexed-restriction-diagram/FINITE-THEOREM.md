---
artifact_type: theorem
status: proved_for_finite_declared_model
created: 2026-07-19
theorem_id: P2C-IRD-001-T
depends_on: P2C-IRD-001
governing_referee_report: REFEREE-REPORT.md
---

# Finite evaluation-restriction and profile-preservation theorem

## Statement

Let `W` be a finite deterministic transition model with typed stages, vector
costs, observations, and a fixed task contract. Let `F` be an
evaluation-closed restriction selected by an explicit state embedding and the
declared evaluation-action set. If a direct model `D` and `F` have identical
states, starts, actions, transition targets, stage labels, vector costs,
observations, verifier semantics, budgets, horizon, and error tolerance, then:

1. direct and restricted policy closures are identical;
2. their bounded verified-task profiles are identical; and
3. any bijective functional transition correspondence preserving all the same
   structure preserves the bounded verified-task profile.

Consequently, two unequal profiles cannot be related by such a faithful
functional correspondence.

## Proof

For policies of length zero, corresponding starts, zero costs, and observations
agree. Assume corresponding policies of length `k` have identical action
words, observations, and accumulated vector costs. Structure preservation gives
one corresponding transition for the next action with the same stage, target
observation, and vector cost. The length `k+1` traces therefore agree. Finite
induction through the frozen horizon gives a cost/observation-preserving
bijection of policy closures. Because the task contract and verifier semantics
are also preserved, acceptance agrees on every corresponding trace. Existential
bounded realizability and the minimum hold-cost profile agree. The contrapositive
gives the unequal-profile obstruction. QED.

## P2C-IRD-001 instance

The explicit N and S restrictions of W are evaluation-closed and byte-for-byte
equal in raw signature to their independently constructed direct models. Each
has 40 policies through length three.

- N's minimum successful hold cost is `1`; it fails the base hold limit `0`.
- S's minimum successful hold cost is `0`; it passes.
- W, enumerated directly from both declared starts, contains a passing policy.
- The N-to-S digit-preserving map fails the theorem's correspondence condition:
  `IDLE` maps `N1->N0` but `S1->S1`.
- A carrier relabel `S0,S1 -> T0,T1` is a faithful functional correspondence
  and preserves all policies, costs, observations, and acceptance.

Thus the instance earns
`RESTRICTION_PROFILE_SEPARATION_SCOPED`.

## Construction-changing collapses

The same raw envelope also proves the limitation constructively:

- admitting `COOL` as evaluation gives N-start policy
  `COOL,SET,IDLE` and produces `COLLAPSE_AFTER_PREPARATION_ADMISSION`;
- raising the hold limit to `1` gives N policy `SET,DRIVE` and produces
  `COLLAPSE_AFTER_RESOURCE_CHANGE`;
- adding the interface-labelled `LATCH_HOLD` action gives N policy
  `SET,LATCH_HOLD` and produces `INTERFACE_CONSTRUCTION_FORK`; and
- shortening the horizon to one makes both fibers fail.

These do not contradict the base theorem because each changes a preserved
component of its contract.

## Coarse quotient obstruction

The explicit quotient `N0~S0=q0`, `N1~S1=q1` forgets the starting-fiber index.
Under `IDLE`, `q1` has targets `{q0,q1}`. It is not a deterministic quotient of
the declared models and the paired N/S relation is not a bisimulation. It also
identifies the two distinct start embeddings. Therefore it cannot erase the
profile difference while claiming to preserve the base structure.

## Grade

The theorem is elementary finite transition-system mathematics, and the
instance is an exhaustive bounded fixture. “Faithful” here means the explicit
bijective functional correspondence tested by the fixture, not every possible
relational bisimulation. No physical transition law, universal capability
ontology, source claim, unbounded horizon, issuance, or finality follows.
