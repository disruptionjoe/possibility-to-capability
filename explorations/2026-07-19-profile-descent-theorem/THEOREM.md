---
artifact_type: theorem
status: proved_finite_conditional
created: 2026-07-19
theorem_id: P2C-DESCENT-001
result: PROFILE_DESCENT_AND_FAITHFUL_TOP_LABEL_NON_DESCENT
governing_referee_report: REFEREE-REPORT.md
---

# P2C-DESCENT-001 — finite profile descent and top-label non-descent

## Definitions

Let `C` be a finite set of declared constructions. For each `c in C`, let:

- `X_c` be a finite set of case presentations;
- `E_c` be a certified representation-equivalence relation on `X_c`;
- `P` be a finite verdict-free primitive-profile space;
- `p_c: X_c -> P` extract the primitive profile; and
- `lambda_c: P -> L_c_bottom` be a deterministic extended classifier, with a
  construction-owned bottom or ill-formed output where it is inapplicable.

Assume `p_c` is constant on every `E_c` class, every presentation diagnosis is
`lambda_c(p_c(x))`, and `P` carries no desired verdict or frame winner.

## Theorem A — profile and frame-verdict descent

For each construction `c`, there are unique maps

```text
pbar_c: X_c / E_c -> P
dbar_c: X_c / E_c -> L_c_bottom
```

such that `p_c = pbar_c o q_c` and
`dbar_c([x]) = lambda_c(pbar_c([x]))`, where `q_c` is the quotient map.

### Proof

Define `pbar_c([x]) = p_c(x)`. This is well-defined because `p_c` is constant
on certified equivalence classes. Surjectivity of `q_c` gives uniqueness.
Composition with deterministic `lambda_c` gives `dbar_c`; uniqueness follows
again from quotient surjectivity. Therefore a certified representation relabel
cannot change either the primitive profile or the construction-specific
verdict. QED.

## Theorem B — minimal joint carrier

Define an equivalence relation on `P` by

```text
p ~ p'  iff  lambda_c(p) = lambda_c(p') for every c in C.
```

Then `J = P / ~` is the coarsest carrier retaining every declared frame output.
Every `lambda_c` factors uniquely through the quotient `pi: P -> J`. If all
classifiers also factor through a surjection `h: P -> K`, there is a unique map
`g: K -> J` satisfying `pi = g o h`.

### Proof

The relation is the intersection of the kernels of all extended classifiers.
Each classifier is therefore constant on its classes and factors through `J`.
If every classifier factors through `h`, then `h(p)=h(p')` implies equality of
every classifier output, hence `p~p'`. Thus `g(h(p))=[p]` is well-defined and
unique. QED.

`J` is a minimal joint diagnostic carrier. The theorem does not identify it
with one frame-free English label or a universal physical quotient.

## Theorem C — two-witness faithful top-label non-descent

Let `x_A` be the access-only conservative-extension profile and `x_C` the
fixed-interface nonconservative mechanism-change profile. At top-label level:

```text
             x_A          x_C
Frame N      ACCESS       CAPABILITY
Frame R      CAPABILITY   CAPABILITY
```

Suppose maps `u_N` and `u_R` to a common label carrier commute on both
witnesses. On `x_A`, commutation gives

```text
u_N(ACCESS) = u_R(CAPABILITY).
```

On `x_C`, it gives

```text
u_N(CAPABILITY) = u_R(CAPABILITY).
```

Therefore `u_N(ACCESS) = u_N(CAPABILITY)`. Any common top-label quotient that
makes N and R commute on both witnesses collapses N's Access/Capability
distinction. No faithful single Access/Capability head descends across these
two constructions on this class. QED.

The primitive profile and R's conservative/nonconservative subtype retain the
distinction. The negative result concerns only the top-level semantic head.

## Construction-index corollary

Absent a supplied commuting cross-construction transport, the total diagnosis
lives naturally on the construction-indexed coproduct of the within-frame
quotients. Shared evidence or coincident labels do not create an equivalence.

For P2C-XFRAME-001:

- P2C-W1 and its certified relabel descend to one profile class with identical
  N/R/W outputs;
- N and R agree on the fixed-interface P2C-W1 point;
- the access-only point proves family-wide faithful top-label non-descent; and
- W changes `pair_defined` and remains a material one-context construction
  fork, not a contradictory verdict.

The finite calibration has six presentations, 203 set partitions, and five
classes in its minimal joint carrier. Exhaustive enumeration finds zero
faithful common top-label assignments in a three-token codomain; when N's
Access/Capability distinction is deliberately collapsed, three commuting
assignments appear. The algebraic proof above is cardinality-independent; the
enumeration is a finite proof fixture and teeth check.

## Augmented-dynamics corollary

An augmented state model can carry mechanism, interface, controller, resource,
record, and verifier data and reproduce both frame projections. But a
kernel-preserving quotient that forgets observation structure and an
observation-preserving quotient that retains it produce different
individuations. Choosing which structure a bisimulation must preserve is
precisely part of the N/R construction question.

For the tested finite model, augmented dynamics is therefore a common carrier,
not a canonical adjudicator. This does not rule out a later choice-free
universal construction that fixes the preservation regime independently.

## Grade and nonclaims

The quotient and no-go statements are theorem-grade elementary finite
mathematics relative to the stated assumptions. The P2C application remains a
finite conditional corollary over receiver-defined profiles and classifiers.
It does not establish new physics, discharge C1 task semantics, force a
two-context individuation, prove an access-independent capability object,
validate the universal hierarchy, reach finality, or move source truth.
