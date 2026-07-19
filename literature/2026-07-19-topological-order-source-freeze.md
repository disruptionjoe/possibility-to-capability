---
artifact_type: literature_freeze
status: complete
created: 2026-07-19
repo: possibility-to-capability
lane_id: "2"
supports: steward/research-portfolio.json#P2C-REAL-PHYSICAL-WITNESS
claim_tier: source-backed reproducibility hardening
verification: tests/topological_order_source_freeze.py
---

# Topological-Order Source Freeze

This freeze backs the 2026-07-19 Alternate B topological-order witness with
primary literature anchors. It does not replace the executable fixture in
`tests/topological_order_witness.py`, and it does not upgrade that fixture into
a source packet, empirical claim, capability verdict, or finality claim.

## Source Anchors

| ID | Source | P2C use |
|---|---|---|
| KITA-2003 | A. Yu. Kitaev, "Fault-tolerant quantum computation by anyons," arXiv:quant-ph/9707021; Annals of Physics 303 (2003), 2-30. URL: https://arxiv.org/abs/quant-ph/9707021 | Toric-code and anyonic-computation lineage for the Z2 topological-order carrier. |
| DKLP-2002 | Eric Dennis, Alexei Kitaev, Andrew Landahl, John Preskill, "Topological quantum memory," arXiv:quant-ph/0110143; Journal of Mathematical Physics 43 (2002), 4452-4505. URL: https://arxiv.org/abs/quant-ph/0110143 | Surface-code/topological-memory backing for nontrivial topology, homology-cycle operations, and distance-style memory pressure. |
| KP-2006 | Alexei Kitaev and John Preskill, "Topological entanglement entropy," arXiv:hep-th/0510092; Physical Review Letters 96 (2006), 110404. URL: https://arxiv.org/abs/hep-th/0510092 | Primary source for the universal topological-entanglement-entropy constant used as the gamma leg. |
| LW-2006 | Michael Levin and Xiao-Gang Wen, "Detecting topological order in a ground state wave function," arXiv:cond-mat/0510613; Physical Review Letters 96 (2006), 110405. URL: https://arxiv.org/abs/cond-mat/0510613 | Independent source for detecting topological order through topological entropy tied to total quantum dimension. |

## Witness Mapping

The source-backed topological evidence supports only the carrier vocabulary and
reader-reproducibility spine. P2C's finite fixture owns the classification test.

| Witness leg | Source backing | P2C finite-model representation |
|---|---|---|
| `gamma-log-D` | KP-2006 and LW-2006 back a universal topological entropy term for gapped 2D topological order. | `gamma_log_d_units = 1` for the Z2 target carrier, plus controls rejecting product and gamma-only mimics. |
| Four sectors | KITA-2003 and DKLP-2002 back the toric/surface-code family on nontrivial topology. | `sectors() == ((0,0), (1,0), (0,1), (1,1))` as a finite Z2 toy carrier. |
| Local indistinguishability | The topological-memory literature motivates protection from local readout of global encoded structure. | Local disk observations ignore sector labels; a symmetry-breaking local-label control fails. |
| Noncontractible loop access | DKLP-2002 backs encoded operations tied to nontrivial homology cycles. | Noncontractible loop observations distinguish sectors while local probes do not. |
| Distance-scaling memory | Surface-code memory supplies the source vocabulary for distance-style protection. | The fixture requires code distance to exceed the bounded local patch radius across tested sizes. |
| Completion rivalry | This is P2C-owned, not a source verdict. | Ordinary local completions fail; whole-family admission with the target topological phase still absorbs. |
| Neutrality | This is P2C-owned, not a source verdict. | The typed verdict is invariant under `e/m` relabeling, and a label-sensitive scorer fails. |

## Reader Protocol

1. Verify the source anchors above before treating the witness as
   source-backed.
2. Run:

```text
python tests/topological_order_witness.py
python tests/topological_order_source_freeze.py
```

3. Check that any stronger claim names the missing bridge from this literature
   freeze to an exact Hamiltonian, finite-size regime, material or simulation
   implementation, measurement protocol, thermal/noise model, resource budget,
   before/after task set, and completion-rival family.

## Nonclaims

- No empirical material sample is established.
- No source packet is imported or accepted.
- No source-repository truth moves.
- No capability verdict is established.
- No finality claim is established.
- No publication, public posture, or external action is authorized.

## Reopen Conditions

Reopen the topological-order witness for one of these, not for another copy of
the same toy fixture:

- a source-grounded Hamiltonian or material/simulation specimen with declared
  boundary conditions and measurement protocol;
- a finer literature-grade freeze that changes the loop, distance, or entropy
  leg;
- a new completion rival that attacks loop access or distance scaling rather
  than only the gamma scalar;
- a source-issued nonphysics packet that changes the cross-domain priority; or
- a failed independent-reader reproduction of the current fixture or this
  source freeze.
