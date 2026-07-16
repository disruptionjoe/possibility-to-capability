---
artifact_type: exploration
status: provisional
created: 2026-07-16
construction: finite_binary_flip_orbit_fixture
evidence_grade: exhaustive_finite_toy
governance_role: progress_synthesis
constitutional: false
---

# Relational-Dissolution Fixture

## Objective

Lane 1 of the standing progress surface asks whether an observable can depend
on the absolute orbit member rather than relative alignment. The finite
fixture `tests/relational_dissolution_fixture.py` tests the binary case that
feeds the Bounded Fiber Theorem's first door.

The model is deliberately small: configurations are sign assignments
`{-1,+1}^n`, the global flip sends every sign to its opposite, and pairwise
products are the relative-alignment profile.

## Result

For `n=3` and `n=4`, every global-flip-invariant Boolean observable factors
through the pairwise relative-alignment profile. The fixture exhaustively
enumerates all Boolean tables on those configuration spaces:

- `n=3`: 16 invariant observables out of 256 total Boolean tables.
- `n=4`: 256 invariant observables out of 65,536 total Boolean tables.

The pairwise profile separates global-flip orbits in both cases. A deliberately
disconnected two-edge profile fails to separate `n=4` orbits, because it leaves
an independent flip per component, so the test is not merely checking a
vacuous quotient.

## Controls

Two failing-direction controls show what counts as smuggling the missing datum:

- an absolute first-coordinate selector is not global-flip invariant;
- an anchor-based separator is covariant only if the anchor flips with the
  configuration, and violates invariance when the anchor is held fixed.

This prices the representative-selection move: a fixed anchor is exactly an
extra orbit-member datum, not a relation extracted from the invariant layer.

## Scope

This is toy-grade and binary. It does not rule out richer alphabets, native
formalism tiers, physically motivated new primitives, or the physical spectral
door named in the Bounded Fiber Theorem. It does not move GU, TI, TaF, or P2C
claim status.

## Next-Work Handoff

- current work: relational-dissolution fixture
- current disposition: `ENDPOINT_POSITIVE_TOY`
- durable priority owner: current tracked selection surface plus
  `steward/research-portfolio.json`
- recommendation status: advisory

| rank | eligible lane or work item | why now | dependencies / gates |
|---:|---|---|---|
| 1 | Weakest-oracle theorem | The relational fixture says invariant observables factor through relative alignment; the next sharper question is the minimal flip-odd primitive that breaks the quotient | must not call the primitive natural merely because it selects |
| 2 | Cyclic-orientation fixture | This is the most concrete non-binary/arity escape candidate from the standing lane list | requires explicit alphabet/arity semantics and neutrality controls |
| 3 | Native-tier battery | Highest eventual value, but wider surface and source-adjacent formalism risk make it less suited immediately after a finite toy closure | keep source truth and native formalism ownership separate |
| 4 | Real physical witness | Still central to the North Star lane, but should not be conflated with the theorem-hardening byproduct lane | requires a frozen physical system, resources, records, access, and completion rival |

Recommended next: the weakest-oracle theorem, unless a later run chooses to
return to the North Star witness lane for portfolio balance.
