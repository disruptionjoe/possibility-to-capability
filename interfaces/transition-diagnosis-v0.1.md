# Transition Diagnosis Contract v0.1

Status: provisional repo-owned interface and falsifiable research instrument.
It is not canon, a source verdict, or evidence that the hierarchy is universal.

## Question

Can the possibility -> dynamics -> records -> access -> capability -> finality
vocabulary classify supplied transition witnesses without confusing description
with capability, records with access, access with capability, or irreversibility
with finality—and without presuming those types form a strict temporal ladder?

## Construction

The contract is a **typed diagnostic hierarchy**, not a chronology. A record
locates which transition types have witnesses. It does not assert that every
case visits every type, that lower rows cause higher rows, or that the rows are
totally ordered. One branch can carry multiple types; two types can be
incomparable; admissible constructions can disagree; and the correct outcome
can be `HIERARCHY_REVISION`.

Each load-bearing witness is a value plus one or more evidence references. The
dependency-light classifier verifies the record and applies these rules:

| Diagnostic type | Minimum discriminating witness |
| --- | --- |
| Fixed-family disclosure | Same possibility family, equivalent representation, changed description, and no witnessed dynamics/record/access/capability/finality change |
| Fixed-family dynamics | A changed state trajectory, transition kernel, or law inside the assessed family |
| Record formation | A new persistent, discriminable record; persistence is not automatically access |
| Access change | Changed conditioning, reachability, observability, or control relation; access is not automatically normalized capability |
| Capability enlargement/restriction | A strict superset/subset of operational tasks after a named common normalization holds description, representation, resources, access, and control fixed as declared |
| Finality candidate | Settlement, no factor found through preceding layers under a named search scope, and no reopening by admissible continuation |

`FINALITY_CANDIDATE` is deliberately weaker than finality. A finite
factorization search cannot prove absolute non-reducibility. Irreversibility by
itself is insufficient.

## Capability normalization

Raw task availability and normalized capability are separate witnesses. If a
door is unlocked and tasks become executable, raw task availability may grow
while the agent's normalized capability remains equal when access is held
fixed. That is `ACCESS_CHANGE`, not capability enlargement. A capability
verdict requires a named normalization frame so that a new description,
resource grant, access right, or relabeling cannot silently create the result.

This construction is provisional. Some domains may make access constitutive of
capability rather than a factor to normalize. Such a case is a reopening
condition, not permission to force the present answer.

## Non-linear and failure outcomes

- `MULTI_LEVEL`: one construction has witnesses for more than one diagnostic
  type. No causal or temporal order is inferred.
- `INCOMPARABLE`: a task-set relation or declared ordering cannot be reduced to
  superset/subset or a total sequence.
- `CONSTRUCTION_FORK`: retained admissible constructions produce different
  classifications.
- `UNKNOWN` and `CONTESTED`: load-bearing witnesses are unavailable or disputed.
- Null outcomes: no relevant change, an inadmissible construction, or no
  admissible construction survives.
- `HIERARCHY_REVISION`: the supplied relation is cyclic or unrepresentable in
  the current diagnostic vocabulary.
- `INVALID`: the record violates the interface; it is not a scientific verdict.

## Label invariance

Branch identifiers and human labels are excluded from classification. The
reference evaluator performs a pure label permutation and requires the semantic
summary to remain unchanged. This is a syntactic metamorphic control, not proof
of invariance under every admissible reformulation.

## Assumptions and evidence grade

- Construction: rule-based classification over explicitly qualified receiver
  witnesses, with construction branches retained.
- Assumption: evidence references identify the support used by the receiver;
  the evaluator does not establish its truth or sufficiency.
- Assumption: the declared normalization frame makes raw access and normalized
  operational capability meaningfully comparable.
- Evidence grade: provisional interface plus deterministic synthetic controls.
- Verification: the adversarial suite exercises positive, negative, null,
  unknown, contested, forked, incomparable, label-swapped, and revision cases.

## Falsifiers

Revise or reject v0.1 if a well-specified case:

- changes classification under a pure relabeling;
- makes record and access, or access and normalized capability, inseparable
  without a source-specific stipulation;
- requires a capability relation not expressible as equal, superset, subset,
  or incomparable under a common frame;
- establishes a finality discriminator that does not use settlement,
  non-factorization, and admissible-continuation tests;
- exposes a meaningful transition type that is neither represented nor
  honestly classified as hierarchy revision; or
- shows that the same evidence must be forced into a temporal sequence to be
  scientifically meaningful.

## Nonclaims

- The six names are not proved complete, universal, fundamental, or temporally
  ordered.
- `PASS` from the test harness establishes only deterministic contract behavior.
- A receiver-supplied witness is not source truth and does not promote a claim.
- A `FINALITY_CANDIDATE` is not proof of physical finality.
- Multi-level co-location is not a causal chain.

## Reopening conditions

Reopen the contract after the first real frozen-packet classification, after a
case with access constitutive of capability, after a justified non-monotone
capability comparison, after a finality proposal with a different
non-reducibility test, or whenever a case returns `HIERARCHY_REVISION`.

## Reference implementation

```text
python tests/classify_transition.py tests/fixtures/transition-diagnosis-v0.1-valid.json
python tests/validate_transition_diagnosis_contract.py
```

The implementation uses only the Python standard library. Its output is a
provisional diagnosis of the supplied record, not a physical result.
