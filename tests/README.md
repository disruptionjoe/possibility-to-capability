# Tests

This directory is reserved for deterministic checks and adversarial fixtures
owned by this repository. Source-repo test suites remain in their source repos.

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

Run from the repository root:

```text
python tests/validate_transition_diagnosis_contract.py
python tests/classify_transition.py tests/fixtures/transition-diagnosis-v0.1-valid.json
```

A classification diagnoses supplied receiver witnesses. It does not establish
their truth, promote a source claim, or prove the hierarchy complete.
