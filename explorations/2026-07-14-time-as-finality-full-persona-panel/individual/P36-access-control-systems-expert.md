## Steelman thesis

The repository’s real story is that existence, visibility, authority, effective action, and closure are different security judgments and must not be inferred from one another. The hierarchy is strongest as an authorization-aware audit language that asks exactly which relation changed and under whose declared security model.

## Summary of understanding

In an access-control system, possibility is the space of subjects, objects, actions, and policy-consistent states. Dynamics covers policy updates, delegation, revocation, and state transitions. Records include audit logs, credentials, grants, and durable attestations. Access is the authorization relation determining what a principal may observe, reach, invoke, or control. Capability is the normalized set of operational tasks actually achievable under fixed representation, resources, access, and control. Candidate finality resembles an authorization or revocation outcome that cannot be reopened under the declared delegation, recovery, or policy-continuation rules. The typed approach properly admits co-location and forks: an authorization change can create a record, alter access, and change effective task power at once, while inheritance semantics can make the diagnosis construction-relative.

## Strongest insight

The access/capability distinction targets a classic security error: confusing possession or visibility of an object with authority to accomplish a task. A log entry can exist without being readable; a user can read a resource without being able to transform it; an API permission can exist without the environmental preconditions for successful use. Requiring explicit witnesses for each judgment is sound.

## Strongest criticism

“Capability” has a load-bearing technical meaning in capability-based security: an unforgeable reference both designates an object and conveys authority. In such systems, access is not an external factor that can always be normalized away; it partly constitutes capability. Holding access fixed may erase the very mechanism being classified. The framework preserves this fork verbally, but until a real access-constitutive case is run, its central separation may be architecture-specific rather than general.

## Hidden assumptions

- Principals, resources, actions, and success criteria have stable identities across constructions.
- Authorization semantics are separable from resource and control semantics.
- The permission lattice faithfully represents contextual conditions and negative permissions.
- Revocation and delegation horizons can be fixed without favoring a finality verdict.
- Effective authority can be derived from policy without unmodeled side channels or confused deputies.
- Source and receiver agree on whether “may,” “can,” and “is authorized” are distinct.

## Rose

The source-sovereignty rule is itself a well-designed authorization boundary. The receiver may annotate and evaluate but may not escalate source claims, forge source identity, or mutate the protected object.

## Bud

Develop paired cases spanning role-based access control, attribute-based control, and object-capability systems. The same task should be analyzed under inheritance, delegation, revocation, and attenuation to reveal whether an invariant capability quotient exists.

## Thorn

A normalization chosen by the classifier can become a privilege-escalation mechanism: by declaring access “held fixed,” it may attribute authority to an intrinsic capability that exists only because of the access relation.

## Confidence

9/10. The authorization lens exposes both the repository’s most valuable distinction and its most dangerous ambiguity.

## Suggested experiment

Freeze two real authorization interventions over the same task vocabulary: one changes discoverability or read access only; the other grants a new attenuated authority that enables a previously impossible state-changing task. Have independent reviewers preregister RBAC and object-capability constructions, then classify each branch separately.

## Suggested theorem or mathematical direction

Represent principals and permissions as a security lattice and tasks as an action relation. Seek necessary and sufficient conditions for quotienting access changes away while preserving effective-task semantics. Where no such quotient exists, prove that capability must be indexed by the authorization construction.

## Suggested falsification test

Revise the candidate if all admissible security models make effective capability exactly the closure of access and delegation, or if nominally equivalent policy representations yield different diagnoses because the proposed normalization omits authority semantics.

## Relationship classification

`homology`. The candidate and access-control systems share structural distinctions among object existence, recorded grants, authorization, effective power, and revocation closure. The mapping is not reduction because physical capability need not be constituted by institutional authority.
