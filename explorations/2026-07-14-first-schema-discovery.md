---
artifact_type: discovery_report
status: non_binding
created: 2026-07-14
workflow: repo-discovery-run
mode: observe
---

# Discovery: What Schema v0.1 May Be Missing

## Discovery Mode

- Bounded fleet pass or deep single-repo Discovery: bounded single-target pass
  using the normal fleet Discovery depth.
- Why this depth is appropriate: the repository has one real Progress artifact
  and one founding case; the useful question is where the first contract may be
  overfit, not a broad theory search.

This report is non-binding. It does not authorize schema changes or alter the
GU-001 intake verdict.

## Scope Inspected

- `packets/schema/frozen-packet-v0.1.schema.json`
- `tests/fixtures/frozen-packet-valid.json`
- `tests/validate_frozen_packet_contract.py`
- `packets/intake/GU-001-readiness-2026-07-14.md`
- the charter's packet, construction-fork, no-artificial-success, and neutrality
  rules

## Findings

### 1. Method count is not yet method independence

The schema records a method ledger and verifies unanimous result strings, but it
does not represent shared premises, shared positive controls, or dependency
between methods. In the GU founding case, five mathematical routes are distinct,
but W211 also identifies one shared structural lever: full-group Schur uniqueness
followed by stabilizer-induced reducibility. Counting five rows without encoding
that shared lever could overstate evidential independence.

Candidate correction: add an explicit dependency/premise graph or a
`shared_load_bearing_facts` ledger before the No-Artificial-Success gate treats
method multiplicity as independent support.

### 2. The bundle digest is specified but not reproducible

`hash_scope` and a SHA-256 digest are required, but v0.1 does not define file
ordering, path normalization, byte encoding, newline treatment, or whether the
digest covers a manifest plus blobs or only concatenated blobs. Two honest source
stewards could hash the same logical bundle differently.

Candidate correction: define a canonical digest recipe or require one immutable
archive/blob identifier whose hash semantics are already unambiguous.

### 3. The core schema may be overfit to a convergence packet

Every packet currently requires at least one construction fork and a
`joint_argument_artifact`. Those are correct for GU-001 but may manufacture a
fork or a joint synthesis for a legitimate single-result packet that has neither.

Candidate correction: separate a small core packet contract from optional
profiles such as `multi_method_convergence`, `independence_result`, or
`joint_seam_request`. The GU profile can remain strict without universalizing its
shape.

### 4. "Independent" needs a typed scope

A free-text `independence_scope` preserves wording but does not force a
distinction among proof-theoretic independence, model-relative non-forcing,
invariance under a delimited transformation class, underdetermination, and
five-method convergence. Those are materially different findings.

Candidate correction: retain the source's exact text and add a receiving-side
classification that cannot upgrade it. The classification should allow
`unknown_or_contested` rather than force a stronger category.

### 5. Source issuance protects sovereignty but may become a liveness bottleneck

The strict source-issued rule is correct for GU-001 today: GU is active and owns
the result. The rule may stall a future case whose source is closed, external, or
unable to emit the receiving schema.

Competing interpretations to preserve:

1. **Strict source issue only:** maximum sovereignty; some packets remain
   permanently `NOT_YET_IMPORTABLE`.
2. **Receiver-prepared candidate plus source countersignature:** preserves final
   source authority while reducing formatting burden.
3. **Archival snapshot profile:** permits immutable third-party evidence when no
   source steward exists, but can never be labeled source-issued.

No change is recommended until a second real case distinguishes these needs.

## Branch Re-Weighting

- **More attention:** method-dependency representation and canonical digest
  semantics; both are prerequisites for a trustworthy GU-001 gate run.
- **Less attention:** expanding the abstract possibility-to-finality hierarchy
  before one packet clears the intake and provenance gates.
- **Hold / monitor:** the WI-069 typed interface and additional physics cases;
  useful after the founding path proves the packet machinery.
- **Retire or no-go candidate:** raw method count as a proxy for independent
  evidence strength. Preserve method plurality, but do not score it without the
  shared-premise structure.
- **Best next Progress candidate:** harden Schema v0.1 with a canonical digest
  recipe and method-dependency ledger, or justify explicitly why those belong in
  a later gate artifact rather than the packet.

## Failure / No-Go Mining

- **Recent wall:** all GU method artifacts exist, but the source-owned frozen
  wrapper does not.
- **Negative result worth preserving:** five unanimous method rows do not by
  themselves establish five independent evidential units.
- **Assumption under pressure:** one universal packet shape can serve both
  single-method evidence and multi-method joint-seam results without distortion.
- **What would change the current priority:** receipt of GU-001, a source-side
  hashing convention, or a second materially different packet candidate.

## Non-Binding Recommendation

Do not broaden the research program yet. Use the GU steward's response to decide
whether digest semantics and dependency structure belong in Schema v0.1, a GU
profile, or the downstream formation/no-artificial-success gate. Any of those
can be correct; silently omitting both cannot.
