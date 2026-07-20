---
artifact_type: literature_verification
status: complete
created: 2026-07-20
repo: possibility-to-capability
lane_id: "2"
supports: explorations/2026-07-20-discrete-gfe-specimen/SYNTHESIS.md
claim_tier: primary-source formula verification
---

# Discrete-GfE Primary-Equation Verification

This bounded check verifies the two load-bearing formulas used by the
discrete-GfE specimen against the primary arXiv PDF. It does not rerun the
fixture or upgrade the specimen's qualified evidence status.

## Primary Source

- Ginestra Bianconi, "Quantum entropy couples matter with geometry,"
  arXiv:2404.08556v4, 14 August 2024.
- Abstract: https://arxiv.org/abs/2404.08556
- PDF: https://arxiv.org/pdf/2404.08556
- HTML: https://arxiv.org/html/2404.08556
- Checked: 2026-07-20.

## Formula Check

1. The current v4 PDF's Eq. (6) defines the gauge-coupled boundary operator
   as

   ```text
   B_[n]^(A) = B_[n]^(+) exp(-i e_n Ahat^(n))
             + B_[n]^(-) exp(+i e_n Ahat^(n)).
   ```

   This confirms the specimen's use of the same diagonal gauge field with
   opposite phases on the positive and negative incidence parts.

2. The current v4 PDF's Eq. (10) defines the weighted exterior derivative as

   ```text
   d = G^(-1/2) M(B_[1]^(A), B_[2]^(A)) G^(1/2),
   ```

   where the nonzero block-subdiagonal entries of `M` are the adjoints of the
   gauge-coupled boundary operators. This confirms the metric conjugation and
   block placement. The PDF's Eq. (12) gives the `d_[1]`/`d_[2]`
   decomposition, and Eq. (13) defines `D = d + d^dagger`.

## Numbering Correction

The arXiv HTML rendering labels the same two displays as Eq. (12) and Eq.
(22). The current v4 PDF numbers them Eq. (6) and Eq. (10). The original
exploration inherited the HTML labels. Future citations should use the v4 PDF
numbers and may record the HTML-label divergence when needed.

## Disposition

- The formulas are confirmed; the extraction's load-bearing mathematical use
  is unchanged.
- The equation citations are corrected, not the fixture construction.
- This verification does not make `D` a source-native Hamiltonian. The paper
  supplies a self-adjoint Dirac operator and variational equations, not a
  Hamiltonian time-evolution role for the specimen.
- No dynamical before/after transition, capability verdict, issuance claim,
  finality claim, source packet, or empirical implementation is established.

## Next Gate

The source-formula verification gap is closed. The next admissible Lane 1
input remains a frozen source-grounded transition with independent identity,
matched resource and access frames, task delta, native response, and a
strongest completion rival.
