# Capability Diagnostic

`capability_diagnostic.py` is the reusable command-line surface for Transition
Diagnosis v0.1. It validates an evidence-bearing assessment, classifies each
declared construction branch, aggregates the result, checks a pure label swap,
and emits machine-readable JSON.

From the repository root:

```text
python tools/capability_diagnostic.py tests/fixtures/transition-diagnosis-v0.1-valid.json
```

The documented example returns a valid, label-invariant provisional diagnosis.
The historical command remains compatible:

```text
python tests/classify_transition.py tests/fixtures/transition-diagnosis-v0.1-valid.json
```

## Input boundary

The command does not infer or verify evidence. Every qualified witness value
must carry explicit evidence references, materially different constructions
must remain separate branches, and missing or contested facts must remain
`UNKNOWN` or `CONTESTED`. A valid classification says only what follows from
the supplied record under Transition Diagnosis v0.1.

It does not establish that the witnesses are true, that a source repository
accepted them, that capability changed in the world, or that the P2C hierarchy
is universal. Domain-native vocabulary may be sharper than this coarse
diagnostic and must not be overwritten by its output.
