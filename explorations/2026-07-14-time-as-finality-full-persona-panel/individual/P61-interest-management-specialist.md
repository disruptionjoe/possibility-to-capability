# P61 — Interest-Management Specialist

## Steelman thesis

The repository is fundamentally about separating world state from relevance-filtered world views: what exists or can occur, what changes, what is retained, what reaches an observer, what the observer can actually do, and what can no longer be reopened are distinct diagnostics. Its strongest contribution is refusing to promote information delivery into capability without a demonstrated causal change in the normalized action set.

## Summary of understanding

Interest management decides which state updates, entities, and events a participant receives under finite compute and network budgets. Area-of-interest filters, relevance scores, subscriptions, occlusion, and priority queues do not normally determine what exists in the authoritative world. They determine which records become accessible to which consumers and when. Yet this boundary is not absolute: a subscription can drive server-side simulation, bandwidth allocation, persistence, or authority delegation, making access constitutive rather than merely observational.

The repository’s typed partial diagnostic is well suited to exposing that fork. Possibility describes the admissible state or event family. Dynamics describes authoritative transformations. Records stabilize distinctions. Access captures delivery, query, observability, reachability, or control. Capability asks whether the normalized task set changes after the chosen comparison factors are held fixed. Candidate finality requires more than an update becoming stale or falling outside a relevance window; settlement must resist factorization and admissible reopening.

The arrow should not be read as a pipeline. Access may occur without a separately identified record, records may persist without distribution, and interest rules may change access and resource allocation simultaneously. The synthetic suite proves only that the current classifier can preserve such stipulated distinctions. There is still no accepted real packet, and GU-001 stopped before physical gates.

## Strongest insight

The strongest insight is the access-constitutive construction fork. It prevents the repo from assuming that access is always a removable observational layer. In distributed worlds, relevance filtering can alter simulation load, update frequency, control latency, and even whether an entity remains active. Keeping both the noninterfering and constitutive constructions live is more honest than choosing one normalization globally.

## Strongest criticism

“Hold access fixed” can be operationally incoherent under a bounded system. Access consumes bandwidth and compute, and those resources compete with authoritative simulation and control. Changing who sees what can alter latency, scheduling, and downstream state transitions. Unless the comparison frame includes backpressure and resource coupling, a claimed access-only intervention may quietly change capability or dynamics.

## Hidden assumptions

- An authoritative state exists independently of each observer’s interest view.
- Relevance filters can be changed without altering simulation scheduling.
- Dropped or delayed updates do not change task semantics.
- Resource normalization accounts for bandwidth, compute, queueing, and latency coupling.
- Observer-specific views can be compared through a common invariant vocabulary.

## Rose

The classifier already treats record without access and access without normalized capability as legitimate outcomes. Those are essential controls against view-centric ontology.

## Bud

Add an explicit noninterference witness for access: demonstrate that modifying an interest relation leaves authoritative transitions, resource allocation, and normalized control outcomes unchanged. If it fails, classify the branch as constitutive rather than access-only.

## Thorn

The most dangerous failure is observer laundering—treating whatever enters a participant’s relevance window as newly possible, or treating a culling boundary as a physical boundary.

## Confidence

9/10. The repository’s access/capability distinction directly targets the central error interest-management systems create, though physical transfer remains untested.

## Suggested experiment

Freeze a real or production-faithful multi-user simulation trace. First vary subscriptions and relevance thresholds while reserving enough bandwidth and compute to keep authoritative state and control latency constant. Then repeat without reserved headroom so that backpressure changes tick quality or input delivery. Blind classifiers should return access-only in the first construction and a multi-level or capability-changing diagnosis in the second, with predictive task outcomes.

## Suggested theorem or mathematical direction

Formalize an interest filter as a projection from authoritative event histories to observer histories. Prove a capability-preservation theorem under noninterference conditions: bounded delay, sufficient channel capacity, unchanged authority, and control-equivalent observations. Characterize the failure boundary where queue coupling makes the projection dynamically constitutive.

## Suggested falsification test

Identify source-certified observer projections that satisfy the proposed noninterference conditions yet produce different normalized task outcomes. If capability still changes, either the conditions omit a load-bearing coupling or access and capability cannot be separated in that domain.

## Relationship classification

**Homology.** Under a noninterfering interest-filter construction, the same relational pattern genuinely recurs: authoritative events produce records, selective access changes views, and capability can remain invariant. The classification is conditional, not universal; resource-coupled filtering breaks the homology and must remain a construction fork.
