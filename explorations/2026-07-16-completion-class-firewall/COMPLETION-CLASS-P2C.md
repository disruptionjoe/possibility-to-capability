---
artifact_type: formal_contract
status: testable
governance_role: p2c_owned_completion_class
version: completion_class_p2c_v0.1
constitutional: false
claim_movement: false
created: 2026-07-16
work_item: P2C-NULL-COMPLETION-CLOSURE
executable: tests/p2c_completion_class_closure.py
governing_referee_report: REFEREE-REPORT.md (in this directory; GOVERNS)
---

# CompletionClass-P2C v0.1

P2C's own legitimate-completion class: the null class against which a
candidate capability witness's strongest ordinary rival is given its
strongest hearing. This is a P2C-OWNED standard. It consumes nothing from
TI's CompletionClass v1 except as a frozen, read-only comparison point; no
source claim, grade, or verdict moves.

Tier: exploration. This contract is testable, not canon. Nothing here is
`proved` or `resolved` in the repo-canon sense; the theorem below is a
theorem OF THE FINITE MODEL, with its physical force scoped in "Honest
limits."

## 1. Constructor inventory

**Channel-type constructors** (act on rival-frame state; must respect the
declared frame and budget):

| kind | strongest admissible form |
| --- | --- |
| `seed` | thread a chosen value into the physical channel |
| `boundary` | boundary-mediate a value into the physical channel |
| `resource` | transiently drive a value (no persistent maintenance at matched budget) |
| `access` | open the observer aperture onto an existing register |
| `hidden_state` | store any outcome-independent function of the declared setup in a latent register (including round(a) — the steelman) |
| `history` | assert completed relaxation of the physical channel |
| `provenance` | attach a name or label; no channel effect |
| `relabeling` | equivalence-only re-presentation |
| `gauge` | equivalence-only re-presentation |

**Containment-type constructors** (claims of family membership; stateless):

| kind | certification datum |
| --- | --- |
| `whole_family(certified)` | family declared from pre-event physics, outcome-independently (for P2C-W1: the fixed BCS/GL Hamiltonian's phase diagram, N and S regions, at literature grade) |
| `whole_family(hull)` | family declared around the realized signature after the fact (always available; never certified) |

`completed_history` in the global sense is subsumed: as a channel move it is
`history` (relaxation); as a containment move it is a family/hull claim.

## 2. Admissibility axioms

Each axiom has pre-existing P2C provenance; none was introduced to protect
the witness, and none mentions any constructor type.

- **A-FRAME (frame/budget preservation).** An admissible completion acts
  within the witness's declared normalization frame and matched budget. A
  move that changes the frame or spends outside the budget is typed
  `FRAME_CHANGED`, not absorption.
  *Provenance:* the frozen witness's `frame_declaration` (bundle freeze
  `4c9c28b`) and the boundary adapter's `RESOURCE_FRAME_CHANGED` typing
  (`tests/witness_boundary_adapter.py`, commit `850521c`) — both predate this
  swing and predate the TI-WFA-001 import.
- **A-UNIF (outcome-independence / uniformity).** Both the completion's
  content and the strength it earns must be functions of its type and its
  verified, outcome-independent properties — never of the realized outcome's
  identity or of a desired verdict. Verdict-carrying inputs are rejected.
  *Provenance:* the adapter's circularity control (verdict-carrying
  completion input rejected, commit `850521c`).
- **A-CAL (calibration non-constancy).** The class's verdict map must not be
  constant in either direction: a class that absorbs nothing is trivially
  narrow, and a class that absorbs everything makes every witness impossible
  by definition. *Provenance:* this is verbatim the item's own pre-declared
  kill condition (`steward/research-portfolio.json`,
  `P2C-NULL-COMPLETION-CLOSURE.kill_condition`), declared before this swing.

## 3. Strength classes and discharge

Three claim classes: `REPRESENTATIONAL`, `CONTAINMENT`, `OPERATIONAL`.

- A channel-type completion (or admissible composite) that reproduces a
  target's full trace in the rival frame at matched budget earns
  `OPERATIONAL` absorption — the class that can absorb a capability claim.
- A certified containment witness earns `CONTAINMENT` absorption: it blocks
  absolute semantic/metaphysical novelty claims. It discharges no
  operational claim (that is the firewall, section 5 — derived, not
  stipulated).
- An uncertified (after-fact hull) containment witness earns
  `REPRESENTATIONAL` strength only, by A-UNIF: its family declaration is
  outcome-dependent.
- Equivalence-only moves (`relabeling`, `gauge`, `provenance`) earn
  `REPRESENTATIONAL` strength.

## 4. Composition

Declared composition is finite sequential composition of admissible
completions (products over independent channels are subsumed by sequences in
the state model). A composite is admissible iff each component is and the
composite preserves the frame. The class is closed under this composition,
and the closure is a verified fixpoint: in the executable model, depth 4
adds no profile beyond depth 3 (check `c4`), so every result about the
enumerated closure extends to all finite composites.

Composite strength: a composite's operational force is carried entirely by
its channel part — containment components are stateless (check `t1`), so a
mixed composite operationally absorbs iff its channel sub-composite does.

## 5. The derived firewall (theorem of the model)

**Theorem (conclusion-class firewall, CompletionClass-P2C v0.1).** Under
A-FRAME, A-UNIF, and A-CAL, no containment-type witness discharges an
operational claim. Specifically:

1. The after-fact hull is TOTAL (contains every realizable signature —
   check `f1`). If containment discharged operational claims, then by
   A-UNIF (uniformity) the hull would discharge every operational claim, so
   the operational verdict map would be constant — violating A-CAL
   (exhibited: `f2-fail`). So uncertified containment caps at
   `REPRESENTATIONAL` and no containment-as-such upgrade to `OPERATIONAL`
   exists.
2. The certified family genuinely contains the witness (checks `w1`, `f3` —
   the P2C-owned mirror of the frozen `k2` and TI's `e1`), but its only
   would-be operational realizers are outside the A-FRAME-respecting channel
   menu: within the frame, no channel composite reproduces the trace at any
   depth (checks `c1`, `c2`, `c4`). Dropping A-FRAME re-admits an unbudgeted
   feedback servo and the capability-positive class empties (exhibited:
   `f3-fail`). So certified containment earns `CONTAINMENT` and cannot be
   upgraded in-frame.

The axioms mention no constructor type; the cap is derived from constructor
FACTS (hull totality; statelessness; in-frame unrealizability) plus
instrument admissibility. This is the difference from stipulation: TI's v1
assigns the global/ontological cap to `whole_family` by table; v0.1 proves
the separation for containment-type constructors from type-free axioms.

## 6. Escape shape (the theorem-shaped no-go)

**Carrier dichotomy (model theorem, check `c2`).** Every locally-invariant
composite readout is the null value: any applied-flux-tracking carrier in
the rival frame is either physical (decays; perturbable) or latent
(perturbable — latent perturbation is a member of the frozen witness's
local-op group). Hence local-op invariance is unreachable together with
value tracking at any composition depth. The composite frontier reaches
{staircase, persistence} (`hidden_state` then `access` — check `c3`, a
strictly composite absorption no single kind achieves), so the witness's
escape hangs on exactly ONE signature: local-op invariance (exhibited:
`c1-fail`).

## 7. Honest limits

- The theorem is a theorem of the finite model. Its physical force rests on
  the carrier-exhaustiveness commitment (a normal conductor has no locally
  invariant, flux-tracking, zero-maintenance channel), which is
  literature-grade — the SAME grade as the frozen witness's `k1`, not a new
  measurement.
- The model is coarse: only three distinct composite profiles exist, so the
  819-composite enumeration is exhaustive but not combinatorially deep. The
  content is the closure structure and the derivation exhibits, not search
  difficulty.
- A-CAL's authority is the item's own pre-declared kill condition. A rival
  legitimacy standard may reject A-CAL (or A-FRAME, or A-UNIF); the
  executable exhibits show any such standard is a constant or
  verdict-carrying instrument, but "instrument admissibility" is itself a
  methodological commitment. The firewall's derivation therefore binds every
  standard that functions as a non-constant, outcome-independent,
  frame-preserving diagnostic — not every conceivable standard.
- Certification of family membership is scientific input (literature grade
  for P2C-W1), as in TI v1's honest limits. General family-exhaustiveness is
  not proved here.
- No physical measurement backs this contract; D-Q/D-I remain cited at
  literature grade from the frozen witness bundle.
