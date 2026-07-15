---
artifact_type: provisional_results_report
status: provisional
created: 2026-07-14
workflow: repo-progress-run
evidence_grade: deterministic_synthetic
verification: local_standard_library_test_suite
---

# Transition Diagnosis v0.1: Adversarial Results

## Provisional result

The possibility -> dynamics -> records -> access -> capability -> finality
ladder survives this synthetic test only as a **typed diagnostic hierarchy**,
not as a strict temporal, causal, or prerequisite sequence.

That is a narrower and more falsifiable result than a universal ladder. The
types remained mechanically distinguishable across the suite, but valid cases
included skipped types, co-located types, incomparable types, construction-
relative diagnoses, and an explicit hierarchy-revision outcome. A contract that
required every case to advance linearly would misclassify those controls.

This is a repo-owned provisional result about a synthetic instrument. It is not
a result about GU, TI, TaF, WI-069, nature, or any source claim.

## Question and construction

Question: can explicitly qualified witnesses distinguish disclosure, dynamics,
record formation, access, normalized operational capability, and a candidate
for non-reducible finality without manufacturing a strict ladder?

Construction:

- one machine-readable assessment contract;
- every load-bearing witness carries one or more evidence references;
- raw task availability is separated from task-set comparison under a named
  common normalization frame;
- finality is only a candidate when settlement, bounded non-factorization, and
  no admissible reopening are all witnessed;
- admissible construction branches remain separate;
- `MULTI_LEVEL`, `INCOMPARABLE`, `CONSTRUCTION_FORK`, `UNKNOWN`, `CONTESTED`,
  null, and `HIERARCHY_REVISION` are first-class outcomes; and
- human labels are excluded from classification and permuted in a metamorphic
  test.

## Evidence and test result

Command:

```text
python tests/validate_transition_diagnosis_contract.py
```

Observed result:

```text
PASS: 44/44 Transition Diagnosis v0.1 groups; 35 synthetic cases; 16 aggregate outcomes
```

The suite contains 31 single-construction cases and four multi-construction
cases. It covers:

- fixed-family relabeling and disclosure;
- fixed-family dynamics;
- record formation with and without access;
- access and control changes with normalized capability held equal;
- strict normalized capability enlargement and restriction;
- incomparable task sets;
- possibility-family change without an inferred capability verdict;
- finality candidates, incomplete finality evidence, and factorization through
  capability restriction;
- multi-level co-location and partial-order pressure;
- unknown, contested, inadmissible, and no-change nulls;
- alternative and incomparable construction branches; and
- cyclic or unrepresentable relations that trigger hierarchy revision.

Every valid case retained the same semantic diagnosis after a pure label swap.
Malformed controls also rejected missing evidence references, missing
normalization frames, missing factorization-search scopes, false fork metadata,
and degenerate label controls.

## What the suite supports

At deterministic-synthetic grade, the suite supports these limited claims:

1. The v0.1 witness vocabulary can encode and mechanically distinguish the six
   named diagnostic regions without making them mutually exclusive.
2. A normalized operational task-set comparison blocks the tested false
   inference from changed access to intrinsic capability enlargement.
3. Persistent record and changed access remain separately reportable.
4. Irreversibility does not pass the finality rule without settlement,
   non-factorization under a named scope, and failure of admissible reopening.
5. Construction forks, nulls, negative claims, unknowns, and disputes survive
   classification instead of being aggregated into success.
6. The implemented diagnoses are invariant under the tested pure relabeling.

## What the suite refutes

Within this synthetic construction, the suite refutes four tempting rules:

1. **New description implies new capability.** Equivalent fixed-family
   relabeling remained disclosure and rejected the capability claim.
2. **A record implies access.** A persistent trace with no access witness
   remained record formation.
3. **More executable tasks imply intrinsic capability growth.** When raw task
   growth disappeared after access-normalization, the diagnosis was access
   change.
4. **Irreversibility implies finality.** Irreversible dynamics and irreversible
   records without the other finality witnesses remained at their preceding
   diagnostic types.

It also refutes using a strict linear order as the v0.1 contract's semantics.
The accepted controls include access without a record, a record without a
separately asserted dynamics witness, simultaneous record/access, incomparable
record/access ordering, and competing construction-relative diagnoses. This is
not an empirical refutation of every possible temporal hierarchy; it is a
counterexample to making such a hierarchy a prerequisite of the neutral
classifier.

## What remains unresolved

- No real frozen packet has passed through this classifier.
- The common normalization used to distinguish access from capability may be
  impossible or theory-laden in some physical domains.
- Evidence references are checked for presence, not truth or sufficiency.
- `NO_FACTOR_FOUND` is bounded by its declared search scope and cannot establish
  absolute non-reducibility.
- The suite does not test every admissible reformulation, only pure labels and
  the tabled construction changes.
- Possibility-family change and normalized capability change may require a
  richer relation than the current set vocabulary.
- The typed hierarchy may omit an explanatory kind that a real case exposes.

## Assumptions

- The supplied synthetic witness values are stipulated for classifier testing.
- A common task vocabulary and normalization frame can be declared without
  already deciding the case.
- The six type names are useful diagnostic hypotheses, not ontological facts.
- Co-location does not imply temporal order or causal production.

## Falsifiers

The provisional result fails or requires revision if:

- a pure admissible reformulation changes the diagnosis;
- a real case makes record/access or access/capability separation incoherent;
- a justified capability comparison is neither equal, superset, subset, nor
  incomparable;
- a finality discriminator cannot be represented without circularly assuming
  finality;
- a real case classified `HIERARCHY_REVISION` reveals a stable missing type; or
- the classification changes when a retained construction branch is restored.

## Nonclaims

- The hierarchy is not proved universal, complete, fundamental, causal, or
  temporally ordered.
- No physical finality, capability change, or possibility-family change has
  been established.
- Synthetic coverage is not empirical validation.
- A classifier result cannot promote source or repo-owned claim status.
- The result does not alter GU-001 readiness or any source-repository verdict.

## Reopening conditions and next decisive test

Reopen v0.1 when the first real frozen packet is available, when a case treats
access as constitutive of capability, when an admissible reformulation is richer
than label exchange, when a capability relation is non-monotone or
resource-relative, or whenever the classifier returns `HIERARCHY_REVISION`.

The next decisive test is not a larger synthetic suite. It is a preregistered
classification of one real frozen packet with independently reviewed witness
and normalization choices. Until then, the strongest warranted statement is:

> The hierarchy is operationally coherent as a fallible typed diagnostic
> language; the suite gives no warrant to treat it as a universal sequence.
