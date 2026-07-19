---
artifact_type: exploration
status: complete
created: 2026-07-19
workflow: BOUNDARY-TO-ISSUANCE-WITNESS / P2C-REAL-PHYSICAL-WITNESS
construction: z2_topological_order_gamma_log_d
evidence_grade: literature_grade_physics + finite_executable_discriminator
verification: tests/topological_order_witness.py (exit 0; strict TEF lint clean; 7 [E] + 5 [F] = 12)
---

# Topological-Order Witness

This is an exploration-tier Alternate B swing for
`P2C-REAL-PHYSICAL-WITNESS`. It does not establish a real physical issuance,
finality, or capability verdict, and it does not move source-repo truth.

The physical carrier is the standard `Z2` topological-order pattern familiar
from the toric-code/topological-entanglement-entropy literature: a target
phase with total quantum dimension `D = 2`, topological entanglement entropy
`gamma = log D`, locally indistinguishable sectors, and noncontractible loop
operators.

## Question

Can the physical witness program test a harder, intrinsically topological
carrier where the key signature is not persistent circulation, but a
nonlocal memory structure disclosed by `gamma = log D`, sector
indistinguishability under local disk probes, and loop-only access?

This is the promised Alternate B. Its value is not a new physics claim. Its
value is that the witness pressure test now has a carrier whose local
invariance leg is sharper than the superconducting ring and BEC circulation
cases.

## Executable Result

The companion fixture is:

```text
tests/topological_order_witness.py
```

It models four finite signatures:

- `gamma`: a nonzero `gamma-log-D` unit for the target topological phase;
- `sectors`: four topological sectors for the `Z2` toy carrier;
- `local indistinguishability`: contractible disk probes cannot read the
  sector label;
- `loop access and distance`: noncontractible loops distinguish sectors, and
  logical support scales beyond the bounded local patch radius.

Ordinary local completions fail at least one signature. A composite local
mimic can reproduce a `gamma` scalar and sector count, but it still fails the
loop algebra and distance leg. This keeps the run honest: a scalar entropy
headline is not enough to become typed capability evidence.

Whole-family admission with the target topological phase still absorbs the
witness. The run therefore preserves the same fixed-family F1 seam rather than
declaring a capability verdict.

## Verdict

`TOPOLOGICAL_MEMORY_WITNESS / UNDISCHARGED_VS_WHOLE_FAMILY`.

Compared with P2C-W1 and the BEC replication, this swing gives P2C a stronger
local-invariance stress test. The survivor is still only an exploration-tier
topological-memory candidate under the declared frame. It is not a source
packet, not an empirical validation, not a public claim, and not a general
capability-enlargement theorem.

## Controls

The fixture includes failing-direction controls for:

- product completion with no `gamma` term;
- symmetry-breaking local labels that would make sectors locally visible;
- bounded-support local patch memory;
- whole-family without the target topological phase; and
- an anyon-label-sensitive scorer that flips under `e/m` relabeling.

Those controls prevent the test from collapsing into "interesting
topological words." The model must preserve the typed distinction between
local descriptions, access by local probes, nonlocal loop access, and
operational memory structure.

## Validation

Executed:

```powershell
python tests/topological_order_witness.py
python tests/tef_check_tag_linter.py --strict tests/topological_order_witness.py
```

The fixture passed with this evidential headline:

```text
7 [E] + 5 [F] = 12
```

The two `[T]` setup checks are excluded from the headline.

## Nonclaims

- No physical issuance, finality, or capability verdict is established.
- No empirical claim about a concrete material sample is established.
- No source-repository truth or cross-repo packet status moves.
- No public posture, publication, or external action is authorized.
- The fixed-family absorber remains live.

## Handoff

Alternate B is advanced at exploration tier for current inputs. Do not repeat
this finite topological-order toy model without a new source-grounded specimen,
a finer Hamiltonian/literature-grade freeze, a failed reader-reproducibility
control, or a new completion rival that attacks the loop/distance leg.

The next useful frontier should be one of:

- a source-issued nonphysics packet with operational capability-side evidence;
- a finer physical witness freeze that turns this topological-order carrier
  into a less toy-localized specimen; or
- a Lane 2 reproducibility/literature hardening pass if reader trust becomes
  the blocker.
