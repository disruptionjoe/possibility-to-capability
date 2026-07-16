---
artifact_type: formal_contract
status: testable
governance_role: completion_null_class
version: completion_class_v1
claim_movement: false
---

# CompletionClass v1

## Purpose

`CompletionClass v1` is the bounded null class against which a candidate source
event is tested. It prevents finite-prefix novelty, unpredictability, changed
access, changed resources, new names, and post hoc descriptions from being
reported as source issuance.

This contract does not prove that its inventory contains every physically
legitimate completion. It does not establish physical source issuance when the
inventory survives. Its strongest positive return is
`SURVIVES_BOUNDED_COMPLETION_CLASS`.

## Frozen comparison contract

A candidate packet must freeze, before the candidate verdict is evaluated:

- the source state and source law on both sides of the event;
- the candidate action, witness, provenance, and record trace;
- the observer region and access schedule;
- the intervention menu and perturbation protocol;
- the resource, control, work, memory, transport, storage, and cost budgets;
- the physical boundary and admissible initial and boundary data;
- the task definition and success predicate;
- the record-preservation comparison;
- the representation, relabeling, and gauge quotient;
- calibration cases and untouched holdouts.

A completion witness absorbs a candidate only when it reproduces the joint
action, record, task, capability, and perturbation trace while preserving this
contract. Search failure is not a nonfactorization proof.

## Primitive inventory

The v1 inventory is exactly:

| ID | Completion question | Conclusion class |
| --- | --- | --- |
| `hidden_state` | Does a pre-existing latent state determine the event? | physical/predictive |
| `initial_condition` | Does admitted initial data determine the event? | physical/predictive |
| `boundary_condition` | Does admitted one-sided or two-sided boundary data determine the event? | physical/predictive |
| `fixed_source` | Does one fixed source, law, state space, algebra, or instrument family contain the event? | physical/predictive |
| `stochastic_seed` | Does a fixed stochastic law plus latent random tape or seed determine the realized branch? | physical/predictive |
| `name_provenance` | Is the novelty only a name, provenance label, or after-fact singleton? | representational |
| `resource_capability` | Is the task change fixed by available resources, controls, costs, or a pre-existing capability schedule? | operational/context |
| `whole_family` | Does one closed family or verified symbolic generator contain the entire joint candidate signature? | global/ontological |
| `completed_history` | Does a completed-history description extensionally contain the realized trace? | global/ontological |
| `observer_information_access` | Is the event fixed-source disclosure under changed information, aperture, or access? | operational/context |
| `relabel_gauge` | Does the difference vanish under the declared representation or gauge quotient? | representational |

The class is closed under declared product and sequential composition. Defeating
each primitive separately is insufficient if a hybrid completion, such as a
fixed stochastic seed plus an access schedule, reproduces the trace.

## Four conclusion strengths

### `PHYSICAL_PREDICTIVE_ABSORPTION`

A predeclared, physically admissible completion reproduces the trace while
preserving the frozen comparison contract. The packet does not establish
physical source issuance relative to v1.

### `OPERATIONAL_CONTEXT_ABSORPTION`

The apparent novelty is explained by changed access, information, resources,
controls, costs, or an already available capability. This establishes
disclosure or ordinary capability activation, not source issuance.

### `REPRESENTATIONAL_SURPLUS_ABSORPTION`

The difference is only naming, provenance description, relabeling, or gauge.
This removes representational novelty. It does not by itself provide a causal
physical explanation of the event.

### `GLOBAL_ONTOLOGICAL_ABSORPTION`

A whole-family or completed-history object contains the trace. This blocks an
absolute semantic or metaphysical novelty claim. It does not by itself show
that an ordinary causal mechanism generated the event.

The four conclusions are not interchangeable. In particular, unrestricted
completed-history and after-fact singleton completions can encode every
realized trace. Treating them as ordinary physical explanations would make the
positive class empty by definition.

## Admissibility

Physical/predictive and operational/context witnesses must be predeclared,
outcome-independent, physically admissible, quotient-respecting, and verified
on all frozen interventions and holdouts. Representational and
global/ontological witnesses need not be predictive, but their conclusions are
therefore limited to their own class.

Each primitive must be either:

1. absorbed by a verified completion witness;
2. defeated by a verified nonfactorization certificate; or
3. unresolved.

Omitted and unresolved primitives return `INCOMPLETE_NULL_CLASS`. A certificate
identifier without a verifier-backed result remains unresolved.

## Bounded theorem scope

Let `Pi` be a frozen comparison contract and let `K_v1(Pi)` be the closure under
declared product, sequential composition, and representation equivalence of
the eleven completion constructors above.

For a finite, fully explicit, E177-compatible packet, if an admitted physical
or operational witness in `K_v1(Pi)` reproduces the packet's joint signature
under every preregistered intervention and holdout while respecting `Pi`, then
the packet does not establish physical source issuance relative to
`K_v1(Pi)`. A representational or global witness earns only its corresponding
weaker conclusion.

Conversely, failure to find a witness does not establish issuance. The packet
may return `SURVIVES_BOUNDED_COMPLETION_CLASS` only when every primitive is
represented, composition closure is declared, and every primitive has a
verified nonfactorization result. That return triggers review of the bounded
contract. It does not establish physical source issuance, reopen `TI-C020`, or
move a claim.

## Relationship to E177

E177 remains immutable as
`three_world_issuance_disclosure_discriminator_v1`. CompletionClass v1 is a new
contract that audits its controls and supplies the wider null inventory for a
future versioned discriminator. It does not alter the E177 protocol digest.

## Honest limits

- The inventory is complete only relative to these eleven declared families
  and their declared compositions.
- Physical legitimacy of a model class is scientific input, not something the
  Python classifier can decide.
- General gauge quotienting and family-exhaustiveness certificates remain
  domain-specific proof obligations.
- The fixture verifier checks contract behavior, not all physics or all
  metaphysical completions.
- No real physical packet currently survives this bounded class.
