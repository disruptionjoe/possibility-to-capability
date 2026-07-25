---
artifact_type: provisional_synthesis
status: complete
created: 2026-07-24
repo: possibility-to-capability
lane_id: "1"
supports: steward/research-portfolio.json#P2C-REAL-PHYSICAL-WITNESS
claim_tier: receiver-owned computation against published exact formula
verification: tests/tfim_dqpt_thin_shadow_kill.py
---

# TFIM-Quench DQPT Thin-Shadow Reconstruction Kill

## Result

**`THIN_SHADOW_RECONSTRUCTION_KILL`.** The canonical integrable
cross-critical TFIM-quench DQPT does not supply the P2C-2 target of a native
response with no fixed static-Hamiltonian representative.

For the source-pinned fermionic-mode construction, one frozen initial state and
one fixed post-quench Hamiltonian determine the complete finite-size Loschmidt
response. The harness reconstructs the same probability through:

1. explicit spectral evolution of each initial two-level mode under the fixed
   \(H(g_1)\); and
2. the source's algebraically reduced mode-product formula.

The two routes agree across three finite sizes and five times, including the
first source critical time. The continuous critical mode is maximally mixed
and its return probability vanishes at that time; a large finite midpoint
quadrature displays the expected left/right slope separation. The same-phase
control has no real critical momentum and never reaches a maximally mixed
mode.

The executable headline is **27 [E] + 5 [F] = 32**. The unchanged Transition
Diagnosis v0.1 returns fixed-family dynamics plus receiver-owned record
formation, rejects both capability and finality overclaims, and remains
label-invariant.

## What was killed

The killed proposition is narrow and exact:

> This canonical integrable TFIM-quench DQPT response has no representative
> consisting of a fixed post-quench Hamiltonian, frozen initial state, and
> their spectral overlaps.

That proposition fails constructively. The fixed representative is the one
used by the exact solution itself.

The result also separates two meanings of “reconstruction” that the source
keeps distinct:

- full spectral reconstruction from \(H(g_1)\), \(|\Psi_i\rangle\), and their
  overlaps succeeds at finite size;
- simple analytic continuation from equilibrium free-energy knowledge only
  on the positive real axis fails beyond the first Fisher time for a
  cross-critical quench.

The second is an evidence-access limitation. It does not erase the first or
create a time-dependent law.

## Typed diagnosis

Under the frozen receiver frame:

- `FIXED_FAMILY_DYNAMICS`: the state follows nontrivial post-quench evolution
  inside the declared TFIM family;
- `RECORD_FORMATION`: the computed Loschmidt rate/work-distribution object is
  a persistent receiver-owned record of that evolution;
- no `ACCESS_CHANGE`: the compared computations use the same observable and
  spectral information;
- no `CAPABILITY_ENLARGEMENT`: no matched operational task-set delta was
  supplied;
- no `FINALITY_CANDIDATE`: evolution remains unitary, continued, and
  explicitly factored through the fixed Hamiltonian and initial state.

The rate cusp and thermodynamic nonanalyticity remain genuine within the
source construction. They are not capability or finality witnesses merely by
being nonanalytic.

## Construction and grade

- Construction: fermionic TFIM ground state at \(g_0=0.4\), sudden quench to
  fixed \(H(g_1=1.3)\), positive Neveu-Schwarz modes, finite spectral/product
  comparison, and large-finite midpoint proxy.
- Source: Heyl, Polkovnikov, and Kehrein, *PRL* 110, 135704 (2013);
  `arXiv:1206.2505v2`.
- Grade: receiver-owned deterministic computation against a published exact
  formula.
- Verification: `python3 tests/tfim_dqpt_thin_shadow_kill.py`.
- Falsifiers: stable mismatch between the valid fixed-H and exact-product
  routes; hidden time-dependent retuning; or a source-grounded matched
  task/resource/access frame that produces an operational delta omitted here.

## Scope and nonclaims

- This does not refute or downgrade the DQPT result.
- It does not prove the source paper, the thermodynamic limit, or an
  experimental realization.
- It does not generalize from integrable TFIM to interacting, open, driven,
  anomalous-Floquet, or arbitrary DQPT constructions.
- It does not move source truth, packet status, capability, issuance,
  finality, universality, hierarchy semantics, methodology grade, canon, or
  public posture.
- It does not resolve or prejudge the matched-drive anomalous-Floquet
  candidate.

## Next gate

Remove canonical integrable TFIM DQPT from the live no-static-representative
candidate family for current inputs. Do not repeat it with a denser momentum
grid or reinterpret restricted Wick rotation as absence of a Hamiltonian.

The remaining P2C-2 candidate is the matched-drive-power anomalous-Floquet
specimen. Admit it only after freezing:

1. the exact before/after Floquet unitaries or generators;
2. a common drive-power, bandwidth, duration, initialization, measurement,
   and control budget;
3. an operational task delta;
4. the strongest enlarged-static-family or micromotion completion rival; and
5. the precise sense in which no static effective Hamiltonian represents the
   response.

Without that matched construction the honest result is abstention, not a
supplier claim.
