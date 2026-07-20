# Tests

This directory is reserved for deterministic checks and adversarial fixtures
owned by this repository. Source-repo test suites remain in their source repos.

## Blocked intake preflight

- `evaluate_blocked_intake_preflight.py` enforces the provenance stop,
  tracked-only immutable-source rule, null digest firewall, source-status
  preservation flags, assessment/gate inadmissibility, and exact v0.2 unblock
  field lists.
- `validate_blocked_intake_preflight.py` validates the real receiver-owned
  GU-001 preflight and pins its immutable source revision, blob inventory,
  source register, and unchanged named residuals.
- `fixtures/blocked-intake-preflight-v0.1-cases.json` rejects artificial source
  completion, downstream passes or failures after provenance blocks, source
  status upgrades, mutable and untracked references, fake digests, receiver
  method reassembly, and treating wrapper absence as a source refutation.

Run from the repository root:

```text
python tests/validate_blocked_intake_preflight.py
python tests/evaluate_blocked_intake_preflight.py packets/intake/GU-001-blocked-preflight-v0.1-2026-07-14.json
```

The valid verdict is `NOT_YET_IMPORTABLE`. It is not a failed GU result or a
partial eight-gate run.

## Frozen-packet contract

- `validate_frozen_packet_contract.py` protects the unchanged v0.1 contract.
- `validate_frozen_packet_v0_2_contract.py` verifies v0.1 coexistence, the v0.2
  positive bundle and receiving assessment, and adversarial cases covering
  path normalization, raw-byte integrity, all digest layers, artifact coverage,
  premise-map symmetry, shared premises, dependency edges, false unanimity,
  method-count inflation, source-wording drift, status upgrades, and unknown or
  contested receiving classifications.
- `fixtures/bundle-v0.2/` contains controlled raw bytes. `.gitattributes`
  disables text conversion for those files so the fixture digest is portable.

Run both contracts from the repository root:

```text
python tests/validate_frozen_packet_contract.py
python tests/validate_frozen_packet_v0_2_contract.py
```

## Neutral eight-gate contract

- `evaluate_gate_run.py` is the dependency-light reference evaluator for
  `interfaces/gate-run-v0.1.schema.json`. It checks contract consistency, not
  scientific truth.
- `validate_gate_run_contract.py` runs a synthetic all-pass control plus valid
  fail, blocked, indeterminate, split-chain, and label-sensitive cases and
  malformed/tampering controls.
- `fixtures/gate-run-v0.1-positive.json` is the complete synthetic positive
  run over the v0.2 packet and separate assessment fixtures.
- `fixtures/gate-run-v0.1-cases.json` is a deterministic mutation table. It
  makes negative and adversarial expectations machine-readable without
  duplicating the large positive object.

Run from the repository root:

```text
python tests/validate_gate_run_contract.py
python tests/evaluate_gate_run.py tests/fixtures/gate-run-v0.1-positive.json tests/fixtures/frozen-packet-v0.2-valid.json tests/fixtures/receiving-independence-v0.2-valid.json
```

An evaluator `PASS` means only that one run is complete and internally
consistent with the neutral gate contract. It does not establish physics,
promote a source claim, or validate the receiver judgments' substance.

## Transition diagnosis contract

- `classify_transition.py` validates and classifies a provisional
  Transition Diagnosis v0.1 witness record using only the Python standard
  library.
- `validate_transition_diagnosis_contract.py` materializes and checks 35
  synthetic adversarial cases, including disclosure/capability, record/access,
  access/capability, and irreversibility/finality false positives; null,
  unknown, contested, multi-level, incomparable, construction-fork, and
  hierarchy-revision outcomes; and a label-swap metamorphic control on every
  valid case.
- `fixtures/transition-diagnosis-v0.1-valid.json` is a complete access-only
  example that rejects a declared capability-enlargement claim.
- `fixtures/transition-diagnosis-v0.1-cases.json` is the machine-readable
  adversarial case table.
- `cross_domain_transition_adjudication.py` applies the same classifier to the
  imported `TAF-001` nonphysics packet as a receiver-owned transfer test. It
  classifies ALPHA as access change and BETA as record formation while rejecting
  capability, access-relabeling, and finality overclaim controls.

Run from the repository root:

```text
python tests/validate_transition_diagnosis_contract.py
python tests/classify_transition.py tests/fixtures/transition-diagnosis-v0.1-valid.json
python tests/cross_domain_transition_adjudication.py
```

A classification diagnoses supplied receiver witnesses. It does not establish
their truth, promote a source claim, or prove the hierarchy complete.

## Coherent-story ledger

- `validate_coherent_story_ledger.py` checks the provisional synthesis ledger's
  five epistemic claim classes, open-question posture, typed-partial semantics,
  GU/source firewall, finality and access-capability controls, four live
  rivals, construction-fork preservation, and confidence/nonclaim posture.
- Its embedded adversarial suite rejects promotion overclaim, chronology,
  circular or upgraded finality, access-capability collapse, blocked-source
  leakage, artificial joint success, construction suppression, and a weakened
  rival.

Run from the repository root:

```text
python tests/validate_coherent_story_ledger.py
```

A pass means the ledger retains those structural and epistemic boundaries. It
does not establish novelty, physics, source truth, or the candidate story.

## Physical boundary adapter

- `physical_boundary_adapter.py` defines a finite source-neutral adapter from
  physical transition data to canonical response-profile deltas. It checks
  relabel invariance, delta composition, positive residual behavior,
  circular-verdict rejection, resource controls, and completion absorption.
- `physical_completion_closure.py` turns the adapter's completion hook into a
  finite declared middle completion closure. It checks class coverage,
  composition, omission mutants, circularity rejection, resource bounds, and an
  escape target that remains unexplained by the declared closure.
- `witness_boundary_adapter.py` consumes the superconducting-ring and
  BEC/superfluid witnesses' `(Q,I,P)` signature vectors and matched-budget
  frames under CompletionClass-P2C v0.1. It checks carrier neutrality,
  relabel invariance, composition, local-completion failure, certified
  containment versus after-fact hull capping, resource-frame controls, and
  circular verdict rejection.
- `p2c_second_standard_adjudication.py` locally re-reads unchanged P2C-W1
  under CompletionClass-P2C v0.1 and the carrier-neutral adapter, using
  imported TAF-002 and TI-WFA-001 packets as read-only evidence. It checks
  C1-C4, the derived firewall substitution, D2 local-composition closure,
  class-split preservation, source-sovereignty hygiene, and finality
  nonreach.
- `bec_circulation_witness.py` is an independent-domain reach fixture for a
  neutral superfluid/BEC circulation carrier. It checks quantized circulation,
  local phase-relabel invariance, persistence, local-completion failure,
  whole-family absorption, and a carrier-independence control that rejects
  superconducting fluxoid primitives.
- `topological_order_witness.py` is the Alternate B reach fixture for a
  topological-order carrier. It checks `gamma = log D`, locally
  indistinguishable sectors, noncontractible loop access, distance-scaling
  memory, local-completion failure, whole-family absorption, and anyon-label
  neutrality.
- `topological_order_source_freeze.py` checks the Lane 2 source-freeze record
  for the topological-order witness. It requires primary literature anchors,
  source-bounded witness-leg mapping, nonclaim firewalls, and a reader rerun
  protocol.
- `cross_frame_descent_or_fork.py` executes preregistration P2C-XFRAME-001 on
  unchanged P2C-W1. It separates certified representation relabels from
  materially different N/R/W constructions, rejects verdict-carrying inputs,
  and exercises the declared mutation budget before selecting an outcome.

Run from the repository root:

```text
python tests/physical_boundary_adapter.py
python tests/physical_completion_closure.py
python tests/witness_boundary_adapter.py
python tests/p2c_second_standard_adjudication.py
python tests/bec_circulation_witness.py
python tests/topological_order_witness.py
python tests/topological_order_source_freeze.py
python tests/cross_frame_descent_or_fork.py
```

A pass means the adapter prototype satisfies the finite contract in that file.
The completion closure pass means ordinary residual absorption is bounded by
declared completions. The witness adapter pass means both QIP witnesses are
carried as data and whole-family admission is retyped through the certified
containment / after-fact hull split without becoming an operational verdict.
The second-standard adjudication pass means unchanged P2C-W1's scoped-survivor
chain survives the P2C-owned completion-standard substitution while preserving
C1-C4 and source verdict boundaries.
The BEC witness pass means the local-completion discriminator has a neutral
carrier replication at finite-model/exploration tier. The topological-order
witness pass means Alternate B has a finite loop/gamma/distance stress test
with the fixed-family absorber still explicit. The source-freeze pass means the
reader-facing literature spine names its primary anchors and keeps the witness
mapping bounded. The cross-frame pass means the finite common primitive profile
is representation-invariant while top-level labels remain construction-indexed;
it does not prove a universal quotient or equate the constructions. None of
these tests establishes a real physical witness or
promotes an unexplained residual into a proved capability enlargement.

## Relational-dissolution fixture

- `relational_dissolution_fixture.py` exhaustively checks finite binary
  global-flip orbits. It verifies that flip-invariant Boolean observables for
  `n=3` and `n=4` factor through pairwise relative alignment, with failing
  controls for absolute selectors, held-fixed anchors, and disconnected
  incomplete profiles.

Run from the repository root:

```text
python tests/relational_dissolution_fixture.py
```

A pass is toy-grade evidence that binary absolute representative dependence
dissolves to relative alignment unless an extra anchor is supplied. It does
not rule out richer native-formalism or physical doors.

## Per-block observability fixture

- `per_block_observability_fixture.py` checks the finite boundary-switch
  profile claim. It verifies that a single global switch has no neutral
  observable content, while multi-block relative alignments are global-flip
  invariant and sensitive to independent per-block choices.

Run from the repository root:

```text
python tests/per_block_observability_fixture.py
```

A pass is toy-grade evidence for operator opacity: multiplicity can be visible
through relative alignment, while absolute labels and operator identity remain
unsettled. It does not establish observer agency, physical issuance, or any
source-repo verdict.
