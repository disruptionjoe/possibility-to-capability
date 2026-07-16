---
artifact_type: exploration
status: complete
governance_role: witness_consuming_boundary_adapter_swing
constitutional: false
created: 2026-07-16
workflow: BOUNDARY-TO-ISSUANCE-WITNESS / P2C-BOUNDARY-ADAPTER
construction: superconducting_ring_qip_adapter
evidence_grade: finite_contract_fixture + witness_mapping_from_prior_swing
verification: tests/witness_boundary_adapter.py (exit 0; --strict lint clean; headline 7 [E] + 4 [F] = 11)
---

# Witness-consuming boundary adapter

**Tier and guards.** Exploration / finite contract fixture. This does not
establish superconductivity as capability enlargement, physical issuance,
finality, or a GU/TI/TaF result. It changes no source-repo claim, canon,
status, or public posture. It only tests whether P2C's adapter can consume the
2026-07-16 superconducting-ring witness without importing the desired verdict.

## 1. Selected objective

The portfolio selected `P2C-BOUNDARY-ADAPTER`: define the smallest
source-neutral physical boundary/source-to-capability adapter that consumes the
real witness's `(Q,I,P)` signature vector and matched-budget counterfactual
frame, then exposes the whole-family admission question as a testable residual.

This is not the failed GU-sign/finality-polarity adapter. It is a physical
boundary adapter over a concrete witness:

- `Q`: quantized fluxoid staircase;
- `I`: local-operation invariance of the winding;
- `P`: persistence / zero-maintenance-cost holding, at the witness swing's
  stated grade;
- frame: matched-budget counterfactual pair with fixed intervention menu.

## 2. Adapter contract

`tests/witness_boundary_adapter.py` reduces the witness to data the neutral
adapter is allowed to inspect:

- a pre-frame profile;
- a post-frame profile;
- the normalization frame;
- the intervention menu;
- attempted completion frames and whether a whole-family attempt explicitly
  admits the target phase.

The adapter does **not** consume capability, issuance, finality, or desired
verdict labels. Verdict-carrying metadata is rejected.

Given the superconducting-ring witness, the adapter returns:

```text
gained:            ['I', 'P', 'Q']
residual class:    WHOLE_FAMILY_ADMISSION_RESIDUAL
residual question: is admitting the target phase into the fixed family a legitimate completion or an F1 trivialization?
local absorbers:   ()
whole-family:      ('whole_family:fixed_family_with_target_phase',)
```

## 3. Controls

The fixture passed 14 checks:

- 3 `[T]` theorem-consequence checks for QIP atom validity, relabel
  invariance, and delta composition.
- 7 `[E]` checks showing that the witness QIP gain is exposed as a
  whole-family-admission residual, no local completion reproduces all QIP
  signatures, target-phase admission is necessary for absorption, the residual
  question is testable rather than a verdict, resource-frame changes are not
  miscalled capability, verdict-carrying input is rejected, and no-change
  transitions return no residual.
- 4 `[F]` controls showing that name-sensitive, restricted-family,
  resource-blind, and metadata-sensitive bad adapters fail in the intended
  direction.

## 4. Result

**Disposition: `ENDPOINT_POSITIVE_CONTRACT / F1_EXPOSED_NOT_ADJUDICATED`.**

The adapter swing satisfies the portfolio success condition at finite contract
grade:

- it is nonconstant;
- it respects relabel invariance and composition;
- it consumes physical transition data, not a verdict label;
- it rejects circular desired-verdict metadata;
- it refuses to hide resource-frame changes; and
- it exposes the whole-family target-phase admission as the residual that must
  be adjudicated.

The result is deliberately not a capability verdict. The adapter makes the F1
question sharper: whether admitting the superconducting phase itself into the
fixed family is a legitimate completion or a move that trivializes the
Capability level. That question remains outside this run's authority.

## 5. What this closes and what it leaves open

Closed for now:

- the immediate adapter task from `steward/research-portfolio.json`;
- the risk that the adapter only works by carrying `capability_gain` as an
  input label;
- the risk that the witness's QIP vector cannot be represented by a neutral
  finite adapter at all.

Still open:

- the legitimacy rule for whole-family admission;
- the finite-size history/metastability caveat in the witness;
- any TaF capability adjudication;
- any TI completion-legitimacy adjudication;
- Alternate B / C witness escalation.

## 6. Next-work handoff

Durable priority owner remains `steward/research-portfolio.json`; this is a
reranking signal, not a separate queue.

| rank | item | why now | gate |
|---:|---|---|---|
| 1 | `P2C-NULL-COMPLETION-CLOSURE` | The adapter exposed `whole_family_with_target_phase` as the exact F1 residual. The next local swing should formalize when target-phase admission is a legitimate completion and when it trivializes capability. | must not allow arbitrary target admission for free |
| 2 | `P2C-BOUNDARY-ADAPTER` (continue only after closure) | The adapter now exists at contract grade; its next improvement should consume the stricter completion rule, not repeat this fixture. | wait for a closed target-admission rule or a counterexample |
| 3 | `P2C-REAL-PHYSICAL-WITNESS` | Escalate to topological entanglement entropy or independent-domain replication only after the completion rule is sharpened, unless a reach-swing cadence requires it. | no capability verdict without F1 adjudication |
| 4 | `P2C-CROSS-REPO-ADJUDICATION` | Still gated on frozen sovereign returns for the same construction. | no cross-repo action was taken here |
