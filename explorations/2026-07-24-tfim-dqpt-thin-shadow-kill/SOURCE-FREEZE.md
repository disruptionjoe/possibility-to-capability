---
artifact_type: third_party_source_map
status: frozen_for_receiver_test
created: 2026-07-24
repo: possibility-to-capability
lane_id: "1"
source_version: arXiv:1206.2505v2
source_claim_status: published article
---

# TFIM-Quench DQPT Source Freeze

## Source identity

- Markus Heyl, Anatoli Polkovnikov, and Stefan Kehrein, “Dynamical
  Quantum Phase Transitions in the Transverse Field Ising Model,” *Physical
  Review Letters* 110, 135704 (2013).
- DOI: <https://doi.org/10.1103/PhysRevLett.110.135704>
- Open manuscript frozen for this receiver-owned test:
  <https://arxiv.org/abs/1206.2505v2>
- Version: v2, submitted 2013-01-18. The arXiv record identifies the journal
  reference and related DOI.

This is third-party evidence, not a source-repository Frozen Packet. P2C owns
only the mapping and finite reconstruction below.

## Load-bearing source statements

The paper supplies the following exact integrable construction.

1. The transverse-field Ising Hamiltonian is

   \[
   H(g)=-\frac12\sum_i \sigma_i^z\sigma_{i+1}^z
        +\frac g2\sum_i \sigma_i^x,
   \]

   with a critical point at \(g_c=1\). After fermionization its single-particle
   dispersion is

   \[
   \epsilon_k(g)=\sqrt{(g-\cos k)^2+\sin^2 k}.
   \]

   Source: Eqs. (7)-(8) and the paragraph following them.

2. The quench prepares the ground state of \(H(g_0)\) and evolves it with the
   single fixed post-quench Hamiltonian \(H(g_1)\):

   \[
   G(t)=\langle\Psi_i|e^{-iH(g_1)t}|\Psi_i\rangle.
   \]

   Source: Eqs. (2)-(3) and the quench construction preceding Eq. (9).

3. With
   \(\phi_k=\theta_k(g_0)-\theta_k(g_1)\) and
   \(\tan(2\theta_k(g))=\sin k/(g-\cos k)\), the exact mode factor is

   \[
   A_k(t)=\cos^2\phi_k+\sin^2\phi_k\,e^{-2i\epsilon_k(g_1)t}.
   \]

   Equivalently, the return-probability factor is

   \[
   |A_k(t)|^2
   =1-\sin^2(2\phi_k)\sin^2(\epsilon_k(g_1)t).
   \]

   The first expression is Eq. (9) at \(z=it\), apart from the explicitly
   ignored global ground-state phase; the second is its modulus squared.

4. For a quench across \(g_c=1\), the Fisher-zero line crosses the imaginary
   axis at

   \[
   \cos k^*=\frac{1+g_0g_1}{g_0+g_1},\qquad
   t_n^*=\frac{\pi}{\epsilon_{k^*}(g_1)}
          \left(n+\frac12\right).
   \]

   Source: Eqs. (10), (14)-(16).

5. The paper explicitly distinguishes two senses of reconstruction:

   - at finite size, inserting the eigenbasis of the fixed \(H(g_1)\) makes
     the boundary partition function a sum of entire exponentials;
   - after a cross-critical quench, knowledge of equilibrium free energy only
     on the positive real axis does not determine evolution beyond the first
     Fisher time by a simple analytic continuation.

   Source: discussion surrounding Eqs. (3)-(6) and the final discussion.

The second statement does not negate the first. Failure of one restricted
equilibrium-data continuation is not failure of a static-Hamiltonian
representative when the initial state and full spectral data are part of the
declared reconstruction.

## Receiver construction

- Parameters: \(g_0=0.4\), \(g_1=1.3\), a cross-critical quench used by the
  source as an illustrative family.
- Finite modes:
  \(k_m=(2m+1)\pi/N\), \(m=0,\ldots,N/2-1\), the positive
  Neveu-Schwarz momentum grid.
- Direct reconstruction: multiply the two-level fixed-Hamiltonian spectral
  amplitudes \(A_k(t)\).
- Closed reconstruction: multiply the algebraically reduced probabilities
  \(1-\sin^2(2\phi_k)\sin^2(\epsilon_k t)\).
- Thermodynamic proxy: midpoint quadrature at large \(N\), used only to show
  left/right slope separation around the source critical time. It is not a
  proof of the thermodynamic limit.
- Same-phase control: \(g_0=0.4\), \(g_1=0.8\).

## Source and receiver limits

- The paper establishes a DQPT notion based on real-time nonanalyticity; it
  does not assert P2C capability, issuance, finality, or absence of a fixed
  Hamiltonian.
- The receiver test does not independently prove the paper, the
  thermodynamic-limit theorem, or experimental realization.
- The fermionic ground-state construction has a symmetry-broken-spin
  subtlety for quenches originating in the ordered phase. The paper records
  this and shows the work-distribution conclusion survives; this fixture
  remains explicitly within the fermionic mode construction.
- Nothing here generalizes from integrable TFIM to interacting, open,
  driven, anomalous-Floquet, or arbitrary DQPT constructions.
