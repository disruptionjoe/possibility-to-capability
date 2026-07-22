---
artifact_type: exploration
status: complete
governance_role: mipt_access_prekill_triage
constitutional: false
created: 2026-07-22
relation_to_hard_core: Lane 1 falsifier hygiene — pre-kills a candidate witness family for the P2C-2 dynamical-transition search before any fixture is built.
---

# MIPT measurement-induced transition: ACCESS_CHANGE pre-kill (P2C-2 STEP 0 triage)

## Purpose

Wave-1 steering (P2C-2) predicted that a measurement-induced entanglement phase
transition (MIPT: volume-law to area-law in a monitored quantum circuit) would
pre-kill as `ACCESS_CHANGE_ONLY` under the existing transition-diagnosis
classifier, removing one candidate witness family from the P2C-2 dynamical-
transition search. This is a ~10-minute triage to confirm or deny, run before
building any MIPT fixture.

## What was run

The unchanged `tests/classify_transition.py` evaluator was run on one honestly
encoded receiver-owned witness, `mipt-witness-v0.1.json` (Transition Diagnosis
v0.1). Command from repo root:

```text
python tests/classify_transition.py explorations/2026-07-22-mipt-access-prekill/mipt-witness-v0.1.json
```

## Load-bearing framing choices (the honest part)

The classifier only reflects the witness it is given, so the triage lives or
dies on how the MIPT is encoded. The encoding used the most defensible P2C
reading:

- **possibility_family_relation = SAME, representation_relation = EQUIVALENT.**
  The Hilbert space and the unitary gate ensemble are the same object on both
  sides of the transition.
- **dynamics_change = NO.** This is the pivotal judgment. In a monitored
  circuit the intrinsic dynamical law (the unitary gate ensemble) is held
  fixed; the *only* control parameter is the measurement / monitoring rate.
  Tuning a readout rate is not a change of the dynamical law.
- **access_change = YES.** The measurement / monitoring rate *is* the readout
  access control parameter. This is what P2C types as access.
- **persistent_record = NO.** Measurement records exist in *both* phases, so
  record formation is not the before/after delta.
- **raw_task_set_relation = SUPERSET, normalized_task_set_relation = EQUAL.**
  Higher monitoring yields more heralding/readout tasks (raw superset), but with
  measurement access held fixed the intrinsic unitary-realizable set is
  unchanged (normalized equal).
- **declared_claims = ["CAPABILITY_ENLARGEMENT"].** The witness deliberately
  advances the literature's "volume-law phase is a protected quantum code"
  capability reading so the classifier has to accept or reject it.

## Result

```text
aggregate_outcome: ACCESS_CHANGE
branch outcome:    ACCESS_CHANGE  (components: [ACCESS_CHANGE])
rejected_declared_claims: [CAPABILITY_ENLARGEMENT]
alert: "Raw task access changed, but normalized capability did not."
label_invariance: invariant (volume-law <-> area-law swap), exit 0
```

**Verdict: CONFIRMED.** The predicted `ACCESS_CHANGE_ONLY` pre-kill holds. The
classifier types the MIPT as an `ACCESS_CHANGE` and explicitly *rejects* the
declared `CAPABILITY_ENLARGEMENT` claim, because the raw task growth is
mediated entirely by the measurement/monitoring rate (access) and vanishes once
that access is normalized. The apparent "protected code capability" is scored
relative to the very access knob that drives the transition, so it does not
license a capability type.

## Consequence for P2C-2

MIPT is removed as a candidate witness family for the P2C-2 dynamical-transition
search. It cannot serve as "a native response with no static-Hamiltonian
representative" that is a genuine task-set delta, because its non-static-ness
comes from measurement (access), which P2C types as `ACCESS_CHANGE`, not as a
dynamical/capability delta. The TFIM-quench DQPT and matched-drive anomalous-
Floquet specimens named in the steering are unaffected by this note and remain
the live P2C-2 candidates.

## Honest limits

- This is a receiver-owned diagnosis of one *stated* MIPT framing, not a physics
  result about measurement-induced criticality and not a claim that the
  quantum-error-correcting-code interpretation is wrong physics.
- The verdict is contingent on `dynamics_change = NO`. A construction that made
  the intrinsic unitary law itself (not the monitoring rate) change across the
  transition, or that enlarged a normalized task set with measurement access
  held fixed, would reopen this. Those reopening conditions are recorded in the
  witness file. No such construction is currently in hand, so the pre-kill
  stands.
- No source truth, capability, finality, canon, or public posture moved.
