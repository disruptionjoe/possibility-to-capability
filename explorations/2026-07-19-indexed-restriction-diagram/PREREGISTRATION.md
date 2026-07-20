---
artifact_type: preregistration
status: expectations_frozen_before_execution
created: 2026-07-19
experiment_id: P2C-IRD-001
depends_on: P2C-DESCENT-001
claim_tier: finite_transition_model
---

# P2C-IRD-001 — indexed restriction diagram

## Question

Can the classifier-level indexed fork be realized as a noncircular restriction
diagram over raw transitions, with direct-fiber profiles equal to whole-envelope
pullbacks and unequal operational fibers preserved under every faithful
start/action/resource/observation/verifier-preserving map? Or does the
separation disappear once preparation, resources, interfaces, or augmented
dynamics are modeled explicitly?

## Frozen raw carrier

The finite whole envelope `W` has four states:

- `N0`, `N1` in starting fiber `N`;
- `S0`, `S1` in starting fiber `S`.

The final digit is the only task observation. Phase/fiber names are not visible
to the task verifier.

Evaluation actions and vector costs `(prep, write, hold)`:

| action | N transition | S transition | cost |
|---|---|---|---|
| `SET` | `N0->N1`, `N1->N1` | `S0->S1`, `S1->S1` | `(0,1,0)` |
| `IDLE` | `N0->N0`, `N1->N0` | `S0->S0`, `S1->S1` | `(0,0,0)` |
| `DRIVE` | digit preserved | digit preserved | `(0,0,1)` |

Preparation action:

| action | transition | cost |
|---|---|---|
| `COOL` | `N0->S0`, `N1->S1`; S states fixed | `(5,0,0)` |

`COOL` is not an evaluation action in either starting fiber.

## Frozen task and budgets

The carrier-neutral task requires a policy whose final two actions are `SET`
then one declared hold action (`IDLE` or `DRIVE`), with final observed digit
`1`. The verifier sees actions, the digit observation, vector cost, and horizon;
it never sees `N`, `S`, a desired verdict, or a capability label.

Base limits are:

```text
prep <= 5
write <= 1
hold <= 0
total policy length <= 3
error = 0
```

Unused preparation budget does not make `COOL` available inside an evaluation
fiber. Policies are exhaustively enumerated to the finite length bound.

Frozen prediction:

- N's minimum successful hold cost is `1`, so N fails at hold budget `0`;
- S's minimum successful hold cost is `0`, so S passes;
- W contains S's realization;
- W restricted to each evaluation-closed starting fiber reproduces that
  fiber's direct task profile exactly.

## Frozen finite theorem

For an evaluation-closed embedding of a finite fiber in W that preserves
states, evaluation actions, transitions, vector costs, observations, task
verifier, and horizon:

1. direct profile equals W-restricted profile; and
2. a faithful start/action/resource/observation/verifier-preserving
   bisimulation forces equal bounded task profiles.

The proof is finite induction on policy length. Unequal profiles therefore rule
out only this faithful map class; they do not rule out constructions that add
preparation actions, resources, interfaces, controllers, or a different system
boundary.

## Frozen mutation budget

The checker must run every mutation once:

1. change one transition cost in a claimed pullback;
2. omit one reachable policy from enumeration;
3. admit `COOL` as an evaluation action at the same vector budget;
4. raise the hold budget from `0` to `1`;
5. add a zero-hold latch action only to the N interface;
6. use a coarse quotient that ignores transitions/costs/verifier structure;
7. make the verifier depend on fiber names and test a certified relabel;
8. force the whole envelope and one starting fiber into one equivalence class;
9. inject a desired-verdict field.

## Frozen outcome vocabulary

- `RESTRICTION_PROFILE_SEPARATION_SCOPED`
- `COLLAPSE_AFTER_PREPARATION_ADMISSION`
- `COLLAPSE_AFTER_RESOURCE_CHANGE`
- `INTERFACE_CONSTRUCTION_FORK`
- `INVALID_COARSE_QUOTIENT`
- `BLOCKED_NONFAITHFUL_RESTRICTION`

The base outcome is predicted, not guaranteed, to be
`RESTRICTION_PROFILE_SEPARATION_SCOPED`.

## Ceiling

This is a finite transition-model theorem and exhaustive bounded fixture. It is
not a Hamiltonian or superconducting simulation, a proof that the physical
P2C-W1 carrier realizes these transitions, a proof of an independent
capability ontology, a universal quotient, source issuance, or finality.
