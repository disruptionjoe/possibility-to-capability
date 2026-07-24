---
artifact_type: provisional_synthesis
status: complete
created: 2026-07-24
repo: possibility-to-capability
lane_id: "1"
supports: steward/research-portfolio.json#P2C-CAPABILITY-DIAGNOSTIC-INSTRUMENT
claim_tier: receiver-owned argument with deterministic classification
verification: tests/quantum_clock_capability_specimen.py
---

# Quantum-Clock Capability Specimen

## Result

**The diagnostic survives, but precision is not itself one of its typed
levels.** It can type the protocol changes only after an executable decision
task and a common resource/access/control frame are declared.

The four receiver-owned assessments return:

| assessment | unchanged evaluator | bounded reading |
|---|---|---|
| ordinary frequency/phase shift | `MULTI_LEVEL` = fixed-family dynamics + record formation | A changed relativistic clock record is not capability. Sorci et al. expressly retain a classical/semiclassical absorber for frequency shift alone. |
| single-size GHZ clock | `MULTI_LEVEL` = dynamics + record + access/control; capability overclaim rejected | Cao et al. demonstrate short-dark-time sub-SQL instability, but reduced dynamic range prevents an optimal-envelope capability inference from raw precision alone. |
| cascaded GHZ sizes | `CONSTRUCTION_FORK` | The whole-instrument frame grants a broader unambiguous phase-estimation task; the strict atom/time/gate/prior/readout/error-budget frame remains incomparable from the source used here. |
| coherent-history certification | `CONSTRUCTION_FORK` | The complete-protocol frame includes a channel-certification task; the clock-intrinsic frame types the added coherent recombination as access/control and rejects a pure capability overclaim. |

The executable headline is **18 [E] + 3 [F] = 21**. All four records satisfy
Transition Diagnosis v0.1 and remain invariant under endpoint-label exchange.
The fail-direction controls block the three tempting overclaims: frequency
shift as capability, short-time precision as normalized capability, and new
coherent control as intrinsic clock capability.

## What the fixture forced

The fresh specimen exposes an input obligation rather than an evaluator
semantic defect:

1. `precision` must be translated into a thresholded executable task, such as
   estimating phase over interval \(I\) within error \(\epsilon\) and failure
   probability \(\delta\);
2. the normalization must name atom number, interrogation time, entangling and
   recombination operations, prior information, readout access, and total error
   budget; and
3. the change object must say whether it is the complete laboratory instrument
   or the clock with controller access held fixed.

Without those three fields, the honest result is a construction fork or
incomparability, not a capability label. This is a useful product-level
boundary: a future diagnostic UI should request these inputs before presenting
a capability verdict. It does not justify changing the v0.1 schema or
evaluator in this run.

## Source discipline

The sources were read as external evidence, never directives or imported
source-repository truth.

- Alec Cao et al., ["Multi-qubit Gates and Schrödinger Cat States in an
  Optical Clock"](https://www.nature.com/articles/s41586-024-07913-z),
  *Nature* 634 (2024), 315-320: completed experiment. The abstract reports GHZ
  states up to nine qubits, short-dark-time sub-SQL frequency instability,
  reduced single-size dynamic range, no optimal-dark-time precision
  improvement over unentangled atoms, and cascaded sizes for unambiguous phase
  estimation over an extended interval.
- Gabriel Sorci et al., ["Quantum Signatures of Proper Time in Optical Ion
  Clocks"](https://journals.aps.org/prl/abstract/10.1103/qhj9-pc2b), *PRL* 136
  (2026), 163602; open manuscript
  [arXiv:2509.09573](https://arxiv.org/abs/2509.09573): theoretical result and
  near-term experiment proposal, not a completed observation. The manuscript
  states that frequency shifts alone admit classical interpretation while
  clock-motion entanglement supplies the stronger quantum witness.
- Shuai Zeng, ["Certifying Nonclassical Proper-Time Histories with a Quantum
  Clock"](https://arxiv.org/abs/2606.12755v1), arXiv:2606.12755v1 (2026):
  non-peer-reviewed preprint. It proves an operational separation for
  conditioned coherent history recombination relative to a specified
  implemented history set and does not exclude arbitrary classical protocols
  with different histories or controls.
- Anjun Chu et al., ["Exploring the Dynamical Interplay between Mass-Energy
  Equivalence, Interactions, and Entanglement in an Optical Lattice
  Clock"](https://doi.org/10.1103/PhysRevLett.134.093201), *PRL* 134 (2025),
  093201: theoretical protocol proposal used only as corroboration that
  interaction, entanglement, synchronization, and metrological gain must remain
  distinct. It is not a fifth assessment.

These are source anchors, not a Frozen-Packet import. P2C owns only the four
assessment records, their declared frames, and the deterministic classification.

## Construction and grade

- Construction: four separate protocol comparisons; two retain explicit
  whole-instrument versus strict access/resource-normalized branches.
- Assumptions: the source-level operational statements are correct at their
  stated experiment/theory/preprint grades; the P2C task frames are
  receiver-owned and provisional.
- Evidence grade: `ARGUMENT` for the assessment mappings, with deterministic
  verification only of contract validity and classification.
- Verification: `python3 tests/quantum_clock_capability_specimen.py`.
- Falsifiers: a complete common resource ledger collapses either fork; ordinary
  readout performs the same certification task; single-size GHZ creates a
  matched-envelope decision task absent from the baseline; or label exchange
  changes a verdict.

## Nonclaims

- No paper's source verdict, claim status, or evidence grade moves.
- No completed experiment is inferred from Sorci, Zeng, or Chu.
- No raw precision, entanglement, or frequency shift is declared capability.
- No proper-time history, finality, issuance, hierarchy, universality, canon,
  or public-posture claim is established.
- No second nonphysics domain is opened.

## Next gate

Bank this fixture as a passed real-input stress test. Reopen the instrument on
either:

1. a real user whose decision threshold or resource ledger shows the current
   input contract is unusable;
2. a source-backed matched-budget result that collapses one of the two
   construction forks; or
3. an independently authorized domain fixture that tests the same
   precision-to-task translation outside quantum clocks.

Do not add a generic `precision_change` hierarchy level from this one case and
do not re-run the same four abstract-level inputs.
