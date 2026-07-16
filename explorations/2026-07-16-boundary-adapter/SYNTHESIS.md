---
artifact_type: exploration
status: complete
governance_role: boundary_adapter_swing
constitutional: false
created: 2026-07-16
---

# Boundary/source-to-capability adapter swing

Tier: exploration. No source-repo claim moves. No GU/TI/TaF verdict, `bar(b)`,
H59, Krein positivity, physical issuance, or cross-repository identity is
changed here.

## Selected portfolio item

This run executes `P2C-BOUNDARY-ADAPTER`, the highest-ranked unblocked internal
item in `steward/research-portfolio.json`.

Goal: define the smallest source-neutral physical boundary/source-to-capability
adapter on explicit physical inputs, state its composition and invariance laws,
and test one positive control plus one circularity control without carrying the
desired capability or issuance verdict as an input label.

## Adapter constructed

The fixture `tests/physical_boundary_adapter.py` defines a finite physical
frame:

- a resource budget;
- intervention channels with costs;
- exact observable response distributions; and
- optional metadata, which is deliberately ignored by the adapter.

The object map sends a frame to its available effect profile: the set of exact
response-distribution signatures available under the budget, quotiented by
outcome names and intervention names. A boundary report compares pre/post
profiles and records gained effects, lost effects, and a neutral residual
class.

Residual classes in the fixture:

- `NO_RESIDUAL`;
- `RESOURCE_FRAME_CHANGED`;
- `COMPLETION_ABSORBED`;
- `RESTRICTION_RESIDUAL`; and
- `UNEXPLAINED_EFFECT_RESIDUAL`.

The last class is intentionally not called a proved capability enlargement. It
means only that, at this finite-adapter tier, the post-boundary frame has an
available observable effect not present in the pre-boundary profile and not
absorbed by the supplied completion or resource controls.

## Executable laws and controls

Validation command:

```text
python tests/physical_boundary_adapter.py
```

The script checks:

- relabel invariance: outcome names do not change gained effects;
- a failing direction for name-sensitive profiles;
- composition: sequential deltas equal the direct delta on concrete profiles;
- a positive same-resource residual;
- nonconstancy between positive and circular cases;
- circularity control: verdict metadata and duplicate channels are ignored;
- a failing direction for metadata-sensitive bad adapters;
- resource control: budget changes are not silently called capability; and
- completion control: a whole-family completion absorbs the residual.

## Result

`P2C-BOUNDARY-ADAPTER` now has a finite, executable adapter prototype that is
nonconstant, acts on physical transition data, respects declared relabeling and
composition laws, and exposes a testable residual without importing a polarity,
capability, or issuance verdict label.

This is not yet a real physical witness. It is also not a full null/completion
closure theorem. The model is intentionally small: exact response signatures
stand in for observable effects, and the completion control is a supplied
whole-family rival rather than a generated closure over the full physically
legitimate middle class.

## Next-work handoff

Reranked after this swing:

1. `P2C-NULL-COMPLETION-CLOSURE` - use the adapter's completion hook to build
   the legitimate middle completion class and omission mutants. This is now the
   best immediate falsification pressure on the adapter's `UNEXPLAINED` class.
2. `P2C-REAL-PHYSICAL-WITNESS` - select one real physical system and freeze the
   source theory, region, interventions, resources, costs, records, access, and
   observable response, then run the adapter plus the strongest completion
   rival.
3. `P2C-CROSS-REPO-ADJUDICATION` - remains gated on a frozen P2C witness plus
   sovereign returns for the same construction.

No cross-repo action is requested by this swing.
