# P59 — Distributed-Simulation Engineer

## Steelman thesis

The repository is a semantics-preserving classifier for the gap between a model’s possible trajectories, an execution algorithm’s event processing, stabilized causal records, participant visibility, intervention capacity, and a rollback frontier. Its central story is that simulation progress, observable state, and irrevocability are different typed claims whose equivalence must be proved rather than assumed.

## Summary of understanding

Distributed simulation makes the candidate distinctions concrete. A model defines admissible states and events. An execution protocol—conservative synchronization, optimistic Time Warp, lockstep, or another construction—advances them. Event histories, checkpoints, anti-messages, and logs create records. Federate subscriptions and data distribution govern access. Capability concerns the interventions or model tasks that remain executable under declared compute, communication, access, and control. A notion such as global virtual time supplies only scoped finality: events before the frontier are no longer rollback-eligible under the protocol assumptions.

The arrow is therefore not a chronological claim. Record creation may precede validation and later be canceled. A federate can receive an event without gaining authority to affect it. An optimistic engine can explore trajectories unavailable to a conservative execution at that moment while implementing the same model semantics. Multiple constructions may be trace-equivalent yet operationally different. The repository is strongest when it treats these as co-located, incomparable, or forked diagnoses rather than forcing a linear sequence.

The current evidence validates a synthetic instrument, not this transfer. Thirty-five stipulated cases and boundary mutations show disciplined classification. No real frozen packet has passed intake, and the GU founding case did not proceed beyond its blocked provenance preflight.

## Strongest insight

The strongest insight is the Construction-Fork Rule. Simulation engineers know that model semantics and execution semantics are easily conflated. A result observed under Time Warp may depend on rollback, state saving, or message-cancellation behavior rather than on the modeled system. Requiring every conclusion to name its construction and prove transfer is indispensable for any cross-domain explanatory grammar.

## Strongest criticism

The taxonomy under-specifies causal time and correction semantics. “Record,” “settlement,” and “admissible continuation” mean different things under logical time, wall-clock time, partial orders, optimistic rollback, checkpoint recovery, and fault repair. A record may be stable in one time base and provisional in another. Unless the diagnostic indexes witnesses by time domain and execution protocol, finality may merely rename a chosen fossil-collection frontier.

## Hidden assumptions

- Model-level equivalence can be certified across execution algorithms.
- The event dependency graph captures all causally relevant interactions.
- A common task vocabulary survives differences in scheduling and synchronization.
- Rollback, restart, correction, and alternative continuation are separable.
- Resource normalization does not erase execution mechanisms that constitute capability.

## Rose

The repository treats hierarchy revision as instrument success. That is appropriate when cyclic dependencies, non-monotone correction, or multiple time bases cannot be represented faithfully.

## Bud

Introduce explicit model time, execution time, observation time, and commit time into the witness contract. This could reveal when a diagnosis is model-invariant and when it is only scheduler-relative.

## Thorn

A trace collected from one execution could be mistaken for evidence about the underlying physical or formal model, reproducing precisely the source/receiver leakage the packet discipline is meant to prevent.

## Confidence

8/10. The simulation-semantics reading explains the hierarchy’s construction discipline well, while real-case applicability remains open.

## Suggested experiment

Issue a frozen packet for one nontrivial model executed by both a conservative engine and an optimistic Time Warp engine. Preserve source-certified model equivalence, event dependencies, checkpoints, anti-messages, access subscriptions, and resource budgets. Preregister expected invariant diagnoses and permitted protocol-relative fields. A blinded receiver should identify the same model-level transition while assigning different scoped record and rollback-frontier statuses where warranted.

## Suggested theorem or mathematical direction

Define a diagnostic bisimulation between distributed executions. Prove that possibility and model-dynamics diagnoses are invariant under trace-preserving bisimulation, while record, access, capability, and finality may vary only through named execution morphisms. For optimistic simulation, derive sufficient conditions under which global virtual time induces a monotone settlement frontier without implying physical irreversibility.

## Suggested falsification test

Produce two source-certified trace-equivalent simulations for which the classifier gives incompatible model-level diagnoses solely because event scheduling differs. If the difference cannot be isolated to an execution-indexed field, representation invariance fails and the current hierarchy requires revision.

## Relationship classification

**Analogy.** Distributed simulation offers explicit instances of possibility, execution, records, access, intervention, and scoped rollback closure. These illuminate the candidate’s distinctions but do not establish a shared underlying mechanism with nature.
