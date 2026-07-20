---
artifact_type: referee_report
status: governs
created: 2026-07-19
experiment_id: P2C-IRD-001
verdict: ACCEPT_HARDENED_FINITE_SCOPE
---

# Referee report — P2C-IRD-001

## Verdict

Accept `RESTRICTION_PROFILE_SEPARATION_SCOPED` for the declared finite
transition model after hardening. Accept the restriction/profile-preservation
theorem only for the explicit deterministic functional correspondences and
frozen task contract exercised here.

## Hardening performed before acceptance

The first passing implementation was not accepted as-is. The adversarial audit
required and obtained:

- explicit state embeddings instead of prefix-inferred pullbacks;
- a task contract carrying vector budget, horizon, error tolerance, hold
  actions, and verifier semantics;
- direct policy enumeration of W containment;
- a constructed coarse quotient with its nondeterministic `q1/IDLE` targets;
- an explicit start-index-erasure failure; and
- narrower treatment of the latch as an interface-labelled action extension,
  not a proved unchanged-carrier interface factorization.

## Binding scope corrections

1. The restriction is typed by state embedding, evaluation stage, action menu,
   task, resources, observations, verifier, horizon, and error tolerance. A
   pullback by starting state alone would admit `COOL` and is a different
   construction.
2. W containment is a global existential fact. It is not realizability from N
   under the restricted evaluation contract.
3. The tested “faithful bisimulation” is a bijective functional deterministic
   correspondence. The fixture does not enumerate arbitrary relational
   bisimulations.
4. The latch mutation changes the transition/action model and task contract.
   It demonstrates an interface-labelled construction fork, not a pure
   boundary reassignment on one unchanged carrier.
5. The verifier is carrier-name neutral but action-word dependent. Generic C1
   task semantics remain unproved.
6. Horizon one is tested, but the S self-loop has no physical metastability
   clock. No persistence claim beyond the finite fixture is licensed.
7. Error tolerance is exact zero; there is no noise distribution or recovery
   model.
8. After `COOL`, current carrier identity changes to S. The trace retains the N
   start, but origin and current carrier are not separate compositional state
   coordinates. A refined source-grounded model should make both explicit.
9. Seven `[E]` checks are finite designed-model executions, not seven
   independent empirical findings. Five `[T]` checks carry no evidential
   weight; nine `[F]` controls demonstrate teeth.
10. Rejecting the explicit coarse quotient does not reject all augmented-
    dynamics reductions. It shows that “put everything in one state space” is
    not itself a canonical quotient rule.

## What would kill the scoped result

- a faithful typed pullback that equalizes the two base profiles;
- a carrier-neutral verifier fixed independently of the target that gives equal
  profiles at the same vector contract;
- a source-grounded transition law in which the N base fiber has a zero-hold
  accepting policy;
- proof that the stage/action restriction is illegitimate rather than a valid
  operational question; or
- a choice-free quotient preserving starts, costs, observations, tasks, and
  interventions while merging the fibers.

## Research disposition

The toy has done its job. Further local progress should be source-grounded or
should harden an immediate source-grounded application. Do not claim physical
separation, universal capability, finality, or novelty from this result.
