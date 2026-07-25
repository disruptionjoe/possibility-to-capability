---
artifact_type: preregistration
status: frozen_before_test_implementation
created: 2026-07-24
repo: possibility-to-capability
lane_id: "1"
test_id: P2C-TFIM-DQPT-001
---

# P2C-TFIM-DQPT-001 Preregistration

## Question

Does the canonical cross-critical TFIM-quench DQPT furnish the P2C-2 target:
a native response with no fixed static-Hamiltonian representative?

## Construction and comparison frame

The assessed object is the fermionic-mode quench frozen in
`SOURCE-FREEZE.md`. The initial state, post-quench Hamiltonian, mode grid,
observable, and time are identical in both computations.

- Construction A (“fixed-H spectral”): evolve each initial two-level mode in
  the eigenbasis of the single fixed \(H(g_1)\), then multiply amplitudes.
- Construction B (“closed product”): evaluate the exact reduced
  return-probability factor supplied by the same source construction.

These are not rival physical models. They are independently coded algebraic
routes to the same declared object. A mismatch is a receiver implementation
failure or evidence that the source mapping was wrong.

## Predeclared verdicts

1. `THIN_SHADOW_RECONSTRUCTION_KILL`
   if the two routes agree over the frozen grid and times, the source critical
   momentum/time equations pass, the cross-critical thermodynamic proxy shows
   slope separation, and the same-phase control lacks a maximally mixed
   critical mode.
2. `NO_STATIC_REPRESENTATIVE_SURVIVES`
   only if both routes are valid implementations of the frozen construction
   yet disagree materially, or the fixed-H spectral route cannot reproduce
   the source product without time-dependent retuning.
3. `ABSTAIN_SOURCE_MAPPING`
   if the source equations, momentum sector, or initial-state convention
   cannot be mapped consistently.

Verdict 1 removes this TFIM construction from the no-static-representative
candidate family. It does not deny the DQPT, its nonanalytic rate function, or
the restricted analytic-continuation result.

## Evidential controls [E]

- The continuous critical momentum exists for \(g_0=0.4\to g_1=1.3\) and
  satisfies \(\sin^2(2\phi_{k^*})=1\).
- At the source first critical time, the continuous critical-mode probability
  vanishes.
- Direct fixed-H spectral and closed-product probabilities agree to numerical
  tolerance over multiple sizes and times.
- The large finite midpoint quadrature has distinct left and right slopes at
  the first critical time.
- The same-phase \(0.4\to0.8\) control has no real critical momentum and its
  maximum mixing weight remains strictly below one.
- The unchanged Transition Diagnosis v0.1 accepts the receiver-owned
  assessment, returns fixed-family dynamics plus record formation, and is
  label invariant.

## Fail-direction controls [F]

- A Loschmidt-rate cusp is not, by itself, a capability enlargement.
- Failure of simple Wick rotation from positive-real equilibrium free energy
  is not failure of reconstruction from \(H(g_1)\), \(|\Psi_i\rangle\), and
  the full spectral overlaps.
- A thermodynamic-limit nonanalyticity is not absence of a finite-size
  Hamiltonian generator.
- A quench parameter change is not normalized task-set enlargement.
- Nonanalyticity or irreversibility alone is not finality.

## Grade, falsifiers, and reopen conditions

- Grade: receiver-owned computation against a published exact formula.
- Verification target: deterministic standard-library harness plus the
  unchanged Transition Diagnosis v0.1.
- Falsifiers: stable route mismatch after correcting implementation errors; a
  required time-dependent retuning hidden in the fixed-H route; or a
  source-grounded operational task delta under matched resources/access that
  the preregistered frame omitted.
- Reopen TFIM only on a materially different construction that defeats the
  fixed-\(H\)+initial-state spectral reconstruction.
- Do not infer the separately banked anomalous-Floquet result from this test.
