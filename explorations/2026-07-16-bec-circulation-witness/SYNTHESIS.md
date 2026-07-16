---
artifact_type: exploration
status: complete
created: 2026-07-16
workflow: BOUNDARY-TO-ISSUANCE-WITNESS / P2C-REAL-PHYSICAL-WITNESS
construction: bec_superfluid_quantized_circulation
evidence_grade: literature_grade_physics + finite_executable_discriminator
verification: tests/bec_circulation_witness.py (exit 0; strict TEF lint clean; 7 [E] + 4 [F] = 11)
---

# BEC / Superfluid Circulation Witness

This is an exploration-tier independent-domain reach swing for
`P2C-REAL-PHYSICAL-WITNESS`. It does not establish a real physical issuance,
finality, or capability verdict, and it does not move source-repo truth.

## Question

Can the superconducting-ring witness pattern transfer to a neutral-atom
superfluid/BEC carrier without depending on charged-pair, fluxoid, or
electromagnetic structure?

The tested witness is an annular condensate/superfluid circulation case:
after condensation, the target phase can carry a quantized, locally invariant,
persistent circulation signature. The ordinary thermal rival can carry a
continuous angular-flow seed or a decaying vortex trace, but not the full
`(Q,I,P)` signature at matched local-completion strength.

## Executable Result

`tests/bec_circulation_witness.py` models a neutral order-parameter phase
carrier and checks the same discriminator family used for the superconducting
ring:

- `Q`: integer circulation winding across a rotation interval.
- `I`: invariance under local phase relabels.
- `P`: persistence of the current signature.

Local completions fail at least one signature. The strongest composite local
absorber reaches `Q` and `P` but still fails `I`, preserving the completion
firewall's warning that the survivor is one-signature deep. Whole-family
admission with the condensate phase still absorbs the witness, so the same F1
fixed-family question remains live rather than hidden.

The fixture also contains a carrier-independence control: the neutral witness
must not use the superconducting-ring tokens `fluxoid`, `cooper_pair`,
`charge_2e`, or `phi0`. A deliberately bad electromagnetic copy fails this
control.

## Disposition

`INDEPENDENT_DOMAIN_REPLICATION / UNDISCHARGED_VS_WHOLE_FAMILY`.

The result supports transfer of the local-completion discriminator from a
charged superconducting carrier to a neutral superfluid/BEC carrier. It does
not discharge the whole-family absorber and does not license an enlargement
verdict. The honest gain is narrower and useful: the previous witness's local
invariance leg is not merely an electromagnetic artifact.

## Next-Work Handoff

- current work: `P2C-REAL-PHYSICAL-WITNESS`
- current disposition: `ENDPOINT_POSITIVE`
- durable priority owner: `steward/research-portfolio.json`
- recommendation status: advisory

| rank | eligible lane or work item | why now | dependencies / gates |
|---:|---|---|---|
| 1 | `P2C-BOUNDARY-ADAPTER` | the adapter can now consume both the superconducting witness and a neutral-domain replication under the derived completion firewall | must not import a capability verdict or source-repo truth |
| 2 | `P2C-REAL-PHYSICAL-WITNESS` Alternate B | topological entanglement entropy remains the harder escalation if a second independent reach swing is needed | literature-grade freeze needed before executable modeling |
| 3 | `P2C-CROSS-REPO-ADJUDICATION` second-standard local read | P2C's derived completion class can be applied to the frozen P2C-W1 bundle | confirmatory unless an axiom fails on contact |

- recommended next: rerun or extend the witness boundary adapter against the
  derived completion class and the BEC replication.
- switch signal: the reach obligation was discharged with an independent-domain
  neutral carrier, and the same F1 seam remains.
- strongest alternative: Alternate B topological order if the next run should
  spend another core reach swing before adapter consolidation.
- overturning evidence: a finer BEC model where local perturbations reproduce
  quantized persistent winding without target-phase admission.
- steward reconciliation needed: no; portfolio updated in this run.
