# P58 — MMO Network Architect

## Steelman thesis

The repository is an authority-boundary architecture for explanations: it asks whether a change occurred in the world’s admissible state, the authoritative simulation, the durable event record, a client’s view, the actions a player may execute, or the commit horizon after which correction is no longer admissible. Its real value is preventing client-visible change from being mistaken for server-side capability or scoped settlement from being promoted to absolute finality.

## Summary of understanding

An MMO is never one state seen equally by all participants. The authoritative server advances a simulation; event logs and persistence layers stabilize selected distinctions; replication and visibility rules determine which clients learn them; permissions, inventory, cooldowns, latency, and control channels determine executable actions; and rollback, reconciliation, or shard transfer rules determine which results are treated as settled.

The candidate hierarchy maps cleanly onto these engineering questions while remaining a diagnostic rather than a chronology. Possibility is the legal world-state and action family. Dynamics is the tick, event, or rules engine. Records are authoritative logs, snapshots, or durable object state. Access is replication, query, visibility, and control. Capability is the normalized set of tasks a player or service can perform once representation, resources, access, and control are held under a declared comparison. Candidate finality resembles a scoped commit point only after rollback and lawful continuation have been tested.

Cases naturally skip or co-locate types. A server may authorize a hidden action before the client can observe it. A combat log may persist without being replicated. A visibility patch may expose opportunities without changing authority. A migration may change shard capability and record topology simultaneously. This is why the partial diagnostic is stronger than a universal ladder. Yet all present positive evidence is synthetic, and GU-001 stopped at provenance before physical evaluation.

## Strongest insight

The strongest insight is separating records from access and access from authority-backed capability. Live-service incidents repeatedly arise when teams infer server truth from client presentation or infer permissions from UI affordances. The repository’s typed vocabulary demands separate witnesses and makes the normalization frame inspectable. It also preserves construction forks, which is essential when client prediction, server reconciliation, and persistence each present a different legitimate view.

## Strongest criticism

The finality concept is too singular for layered online worlds. A transaction can be final for the client UI, reversible in the zone server, pending in persistence, and compensatable by customer support. Cross-shard operations may use eventual reconciliation rather than one commit horizon. Without scope-indexed settlement domains and fault models, a single finality gate could either flatten these layers or misclassify ordinary operational commitments as something physically irreducible.

## Hidden assumptions

- There is a stable authoritative construction against which other views can be normalized.
- Equivalent representations preserve the action and task semantics that matter.
- Resource, latency, and control budgets can be held fixed rather than being constitutive of play.
- Rollback and compensation are distinguishable forms of reopening.
- One coherent argument chain can cover services with heterogeneous consistency models.

## Rose

The explicit refusal to infer capability from raw task availability is excellent. It matches the practical distinction between a button becoming visible and the server accepting a newly valid command.

## Bud

Index records, capability, and settlement by authority domain: client, zone, shard, persistence, economy, and external service. Then test transfer maps between domains instead of seeking an unqualified global verdict.

## Thorn

The hierarchy could become an elegant postmortem taxonomy that cannot classify live multi-authority systems without choosing whichever server layer makes the desired story true.

## Confidence

8/10. Authority and commit boundaries give a strong interpretation of the repository’s purpose, not evidence that the physical hierarchy is universal.

## Suggested experiment

Freeze two complete MMO incident traces with authoritative logs, client replication, permissions, rollback windows, and shard-reconciliation data. One intervention changes only interest/visibility; the other changes server-authorized operations under the same declared resources and control. Replay each under immediate persistence, delayed persistence, and compensating-transaction constructions. Blind classification should preserve domain-indexed forks and predict which actions succeed.

## Suggested theorem or mathematical direction

Model the world as a family of authority domains connected by refinement maps. Prove conditions under which client-observable access changes are noninterfering with server capability, and characterize a lattice of settlement scopes ordered by admissible rollback and compensation. Global finality would require a meet preserved across all retained domains, not a convenient single-layer commit.

## Suggested falsification test

Find trace-equivalent deployments whose source-certified authority semantics are the same but whose diagnoses change solely because replication or persistence topology was rewritten. If the vocabulary has no invariant quotient, it is architecture-relative and must retain that limitation or revise the hierarchy.

## Relationship classification

**Analogy.** MMO architecture instantiates closely related separations among authoritative possibility, records, visibility, action, and scoped commit. It is still an engineered system with chosen rollback and authority rules, not a reduction of physical finality or capability.
