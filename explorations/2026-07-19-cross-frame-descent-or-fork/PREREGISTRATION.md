---
artifact_type: preregistration
status: expectations_frozen_before_execution
created: 2026-07-19
experiment_id: P2C-XFRAME-001
target_revision: 362a94fefe8ae281df51827336ad103b4613bff3
claim_tier: experiment_proposal
---

# P2C-XFRAME-001 Preregistration

## Question

Does the unchanged P2C-W1 witness support a nontrivial diagnosis that survives
representation transport and remains coherent across the two-context
normalized, access-constitutive, and one-context whole-family constructions?
Or does the capability label collapse, remain permanently construction-indexed,
or fail equivalence invariance?

The machine-readable expectations are frozen in
`P2C-XFRAME-001.expectations.json`. They govern the executable checker and the
later synthesis.

## Load-Bearing Distinction

This run separates two questions that prior work sometimes placed next to one
another without transporting them explicitly:

1. **Equivalence invariance:** does a meaning-preserving representation change
   preserve the evidence profile and the verdict inside one construction?
2. **Construction descent:** do materially different definitions of system,
   interface, task, and comparison admit one frame-free diagnostic quotient?

A failure of the first is an F5 equivalence failure. A failure of the second
may be an honest construction fork rather than a contradiction. The run must
not call inequivalent constructions equivalent merely to manufacture a
falsifier.

## Common Refinement Candidate

Before computing any frame verdict, every case is represented by a primitive
profile containing only declared facts:

- whether a pair exists;
- evidence and representation identity;
- common task and interface availability;
- interface and resource deltas;
- task-profile change under a common comparison interface;
- verified task-profile change under the native interface;
- whether the change is a conservative interface extension;
- whole-family containment; and
- the persistence cap.

The profile contains no capability label or desired winner. Each frame receives
the same profile and applies its own frozen rule.

## Frozen Frames

- `N_TWO_CONTEXT_NORMALIZED` treats a strict task-profile change under a
  common interface and matched resources as capability, and an interface-only
  change with the underlying task profile fixed as access.
- `R_ACCESS_CONSTITUTIVE` treats verified tasks as properties of the
  system-interface pair. It calls both conservative interface extension and
  nonconservative profile change capability, while preserving those subtypes.
- `W_ONE_CONTEXT_WHOLE_FAMILY` removes the before/after pair and reports global
  containment. It cannot issue an operational verdict merely by containing the
  target phase.

No equivalence among these constructions is asserted.

## Frozen Expectations

1. P2C-W1 remains a nonconservative operational change under both N and R,
   conditional on the already-declared C1 task-semantics mapping.
2. The access-only control receives different top-level N and R labels but the
   same primitive profile: N `ACCESS_CHANGE`, R conservative capability
   extension.
3. The one-context construction is a material individuation fork and produces
   containment, not an operational contradiction.
4. Equivalent relabels preserve every primitive fact and frame-specific
   output; any failure triggers `F5_EQUIVALENCE_FAILURE`.
5. The most likely bounded result is an indexed diagnostic with a common
   refinement rather than a single frame-free English label. This expectation
   is frozen as a prediction, not a desired result; the mutation suite must be
   able to reject it.

## Adversarial Budget

The checker must exercise identity, access-only, resource-only, whole-family,
representation-relabel, verdict-carrying, and no-common-interface controls. It
must mutate every load-bearing primitive field named in the expectations file
and demonstrate that a desired-verdict input is rejected.

The exhaustion claim is bounded to those declared cases and mutations. A new
post-result countermodel is a reopening condition, not something the synthesis
may pretend was already searched.

## Interpretation Ceiling

Even a fully passing execution can establish only a finite, receiver-owned
transport result over frozen stipulated witness facts. It cannot establish a
new physical capability, universal hierarchy, absolute finality, equivalence
among material constructions, or source-repository verdict.

