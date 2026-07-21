---
artifact_type: exploration
status: executed_scoped
created: 2026-07-20
experiment_id: P2C-TRIT-ACCESS-001
outcome: C-FAILS
directed_by: "Joe direct chat, 2026-07-20 (cross-repo: trit-access closure check, pre-registered)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
verification: tests/trit_access_closure.py (exit 0; 5 [E] + 4 [F] = 9; 4 [T])
---

# Trit-access closure check — synthesis

## The pre-registered question (bound in GU before looking)

Is GU's external **trit** — the Z/3 half of the minimal generation-forcing
input Z/6, established **unoriented / S_3** on **three interchangeable copies**
— the natural cyclic **CLOSURE** of P2C's own nested access-restriction chain
`{world >= access >= standpoint}`?

The binding is GU `explorations/prereg-trit-symmetry-and-fork-2026-07-20.md`
(commit `cafcbc7`), refined by the trit triage (`af7425f`), which found: every
structural home for the trit's "three" is a **nesting**, while the trit itself
is a **cycle**, and the one surviving way for the access reading to win is for
the unoriented Z/3 to be the cyclic closure of P2C's 3-question chain. The
mailbox pointer is
`system-runtime/mailboxes/possibility-to-capability/archive/20260720-trit-interpretation-lead-points-at-access-layers.md`.
Nothing in those receipts is an instruction to P2C; this exploration is the
steward-side decision to run the cheap decisive test, adjudicated entirely in
P2C terms.

## Result

The check returns **`C-FAILS`**: the closure is **not natural**, is
**oriented (Z/3, not S_3)**, and **does not reproduce** three interchangeable
sectors. **All three legs fail (0/3).** This is the pre-declared honest
negative — the access-layer interpretation of the trit is wrong *as stated*;
the trit's cyclicity has no home in P2C's access chain.

## P2C's access structure, extracted from its own machinery

Read directly off `tests/indexed_restriction_diagram.py` (fixture P2C-IRD-001).
The IRD synthesis states the three questions plainly: *"What can happen
globally, what can happen from here, and what can be done from here under this
interface and budget are different questions."* That triple is a nested
restriction chain. Its layers, with the admissible-policy count as the order
invariant (computed live, not stipulated):

| layer | question | policies | realizes at base budget |
|---|---|---:|---|
| `world` | what can happen globally (whole envelope W) | 80 | yes |
| `access` | what can happen from here (restriction to one starting context) | 40 | yes |
| `standpoint` | what can be done from here under the interface/budget contract | 2 | yes |

Three structural facts fall straight out:

1. **It is a strict chain.** `80 > 40 > 2`. Each rung is a strictly narrower
   restriction of the one above. The restriction maps are directed and
   non-invertible; the IRD collapse table shows that reversing the direction
   (COOL / raise budget / add a latch) *"changes which question is being
   asked"* and pays a declared price — there is no free upward map.
2. **Its order-automorphism group is trivial (order 1).** With all three
   policy counts distinct, the only permutation preserving the invariant is the
   identity. The layers are **not interchangeable**; they are told apart by an
   *intrinsic computable* invariant, not by an external label.
3. **It is oriented.** The strict inequality *is* an orientation: world above
   access above standpoint. Any closure that follows the restriction direction
   is a **directed** cycle.

## The trit, cited (frozen GU facts, read-only)

- **Node A** (`66d44d6`): the trit's symmetry group is **S_3** (order 6),
  the full symmetric group on three sectors — **unoriented**. A directed
  3-cycle would give only Z/3; the extra generator is frozen complex
  conjugation. The trit is the symmetry of an *undirected* triangle.
- **Node B1** (`9571e9b`): the three sectors each carry the identical invariant
  triple `(dim 64, Krein signature +32, -32)`; all three **coincide**, so they
  are pairwise isomorphic and **interchangeable up to an external S_3 label**.

## The closure test — three legs

**(a) NATURAL — FAILS.** A natural closure would need a canonical order-3 wrap
`standpoint -> world` supplied by P2C's own restriction maps or a canonical
symmetry of the chain. Neither exists: the restriction maps are strictly
narrowing (upward motion is a priced, question-changing mutation), and the
chain's automorphism group is trivial, so there is no canonical order-3
identification to build the wrap from. Any closure is an **arbitrary external
gluing**, not a canonical construction.

**(b) UNORIENTED — FAILS.** Because the layers are strictly ordered by the
policy invariant, the closure that follows the restriction direction is a
**directed** 3-cycle. Its symmetry group is **Z/3** (order 3, rotations only).
The trit is **S_3** (order 6). `Z/3 != S_3`: the closure is oriented where the
trit is not. This is exactly the pre-registered *directed-chain control*
firing on P2C's actual structure.

**(c) REPRODUCE — FAILS.** The trit's three sectors have equal invariants
(interchangeable); P2C's three layers have distinct invariants `80/40/2`
(distinguishable). The closure therefore cannot reproduce three interchangeable
sectors — P2C's layers are separated by intrinsic structure, the trit's copies
only by an external label. The two are opposite in exactly the property the
trit requires.

## Controls (bound; demonstrated two-sided power)

The symmetry classifier is not rigged to any single verdict:

- **CONTROL-DIRECTED** — a directed-chain closure (oriented 3-cycle) registers
  **Z/3** and fails the S_3 match. This is the planted failing plant, and it is
  precisely what P2C's chain closure is.
- **CONTROL-SYMMETRIC** — a genuinely 3-symmetric structure (identical blocks,
  no distinguishing invariant / undirected triangle) registers **S_3** and
  passes. The classifier *can* return S_3 when the structure truly carries it,
  so the C-FAILS verdict is a real discrimination, not a floor.
- **CONTROL-ORIENTATION** — an orientation-blind classifier (one that always
  adjoins a transposition) *misregisters* the directed plant as S_3, the
  known-wrong answer; the orientation-sensitive classifier separates directed
  (Z/3) from undirected (S_3). The orientation datum is load-bearing.
- **CONTROL-REPRODUCE** — equal-invariant layers yield automorphism order 6
  (interchangeable). The reproduce-test has two-sided power: it returns
  "interchangeable" when the invariants coincide.

Both directions fire as pre-declared: the closure of a directed chain is Z/3,
a truly symmetric structure is S_3, and P2C's chain is the former.

## What it means for the trit-access interpretation

The LEAD is **not** confirmed. P2C's access structure is arity-compatible with
the trit (`3 = 3`, as the triage already found) but **structure-incompatible**
in all three ways that matter: it is a directed, strict, non-interchangeable
chain, whereas the trit is an unoriented, symmetric, interchangeable triple.
Closing the chain does not repair the mismatch — it *inherits* the orientation
the chain already carries, producing Z/3 rather than the trit's S_3. The
triage's honest residue stands and is sharpened by a computation: **the trit's
cyclicity has no natural home in P2C's access chain.** The access reading is
demoted from LEAD to falsified-as-stated; what survives is only the count
coincidence, which the triage already held.

This does **not** kill the trit channel in GU (that is GU's to adjudicate); it
removes P2C's access chain as the trit's structural home. If any home exists it
must be a structure that is *natively* unoriented and interchangeable — which
P2C's restriction hierarchy, by its own IRD result, is not.

## Five-lens council (inline)

**P2C steward.** In-bounds: new files only, no edit to any P2C ledger, gate,
or existing fixture; no packet import; no verdict, claim, capability, or
finality movement; GU read-only. The extraction reuses P2C's own IRD machinery
without re-running its `main()`. The result lands as a steward-ratifiable
proposal (Section below), not an executed status change. The GU pointer is
occasion, not authority — consistent with the standing Lane A disposition that
GU freezes are not P2C authority to execute.

**Order-theory / lattice specialist.** The chain is a bounded strict order of
length 3; its automorphism group in **Ord** is trivial, and a chain has no
canonical cyclic quotient — the only order-preserving self-maps are the
identity and the collapses, none order-3. The cited IRD "coarse union
quotient" that would identify rungs is exactly the one P2C already proved
non-faithful (non-deterministic, erasing the start embeddings). So even the
degenerate wrap is a known-invalid quotient. Passed.

**Representation theorist (S_3).** The decisive invariant is edge orientation.
`Aut(directed triangle) = Z/3` (the rotation subgroup); `Aut(undirected
triangle) = S_3`; the extra coset is the reflection/conjugation class. P2C's
chain, being strictly ordered, supplies the orientation that cuts S_3 down to
Z/3. The trit's frozen conjugation-admissibility (Node A) is exactly the
generator P2C's structure cannot provide. Passed.

**Capability-access theorist.** The narrowing is the whole content of the P2C
hierarchy: capability is a reachability *projection* under a task/resource
contract, strictly below "from here," strictly below "globally." That
directionality is the program's core finding, not an artifact — you cannot
un-restrict without changing the question and paying a price. An unoriented
wrap would erase the very asymmetry P2C exists to type. So the mismatch is
principled, not incidental. Passed.

**Adversarial referee.** Tried three escapes. (i) *Pick a different fiber /
budget so the counts coincide?* Any nontrivial restriction is strictly smaller
(the IRD separation is scoped-real); equal counts require the collapse
mutations that change the contract — smuggling, blocked by the fixture's own
forbidden-field guard. (ii) *Call the chain unoriented by fiat?* Then leg-b's
directed plant and the orientation-blind control both misregister — the
classifier's power is demonstrated, so the fiat is the known-wrong move. (iii)
*Declare partial success on the 3=3 arity?* Arity is not one of the three
closure legs; it was already banked by the triage and is not a match. Verdict:
**C-FAILS is clean**, 0/3, no leg rescuable without an invalid quotient or a
smuggled contract change. Passed.

## Receipts

- `tests/trit_access_closure.py` — deterministic, exit 0, `5 [E] + 4 [F] = 9`
  evidential/teeth checks + `4 [T]` theorem/setup; HEADLINE
  `C-FAILS (0/3 legs) | chain-closure=Z/3 != trit=S_3 | controls:
  directed->Z/3 fail, symmetric->S_3 pass`.
- P2C machinery imported live (read-only, no `main()` run):
  `tests/indexed_restriction_diagram.py` (fixture P2C-IRD-001) — world=80,
  access=40, standpoint=2, chain Aut order 1.
- P2C structural context read:
  `explorations/2026-07-19-indexed-restriction-diagram/SYNTHESIS.md`
  (the three-question nesting, the priced collapses, the non-faithful coarse
  quotient) and `explorations/2026-07-20-two-sector-witness/SYNTHESIS.md`
  (P2C-native access typing; not load-bearing here, cited as the sibling
  access-structure fixture).
- GU receipts (read-only, cited not recomputed):
  `prereg-trit-symmetry-and-fork-2026-07-20.md` (binding),
  `trit-symmetry-node-a-2026-07-20.md` (S_3, unoriented),
  `trit-copies-node-b1-2026-07-20.md` (three equal-invariant copies),
  `trit-triage-2026-07-20.md` (the closure lead + arity finding).

## Boundary / ceiling

Exploration-tier structural comparison of two frozen facts: P2C's access chain
(computed) and GU's trit symmetry (cited). No physical model, no dynamics, no
capability or finality verdict, no source-grounded specimen. No P2C claim,
canon, gate, ledger, verdict, or public posture moves; no GU truth moves; GU
was read-only; no files outside `possibility-to-capability` were touched; no
commits or external actions. The negative is scoped to the interpretation *as
stated* (the trit is the closure of P2C's `{world >= access >= standpoint}`
chain); a referee proposing a *different* P2C structure as the trit's home
would file a NEW node.

## PROPOSAL TO STEWARD (not executed)

For the hourly steward's next reconciliation pass, this swing proposes:

1. Record `P2C-TRIT-ACCESS-001` in the exploration register with outcome
   `C-FAILS`: the cross-repo trit-access closure hypothesis is **falsified as
   stated** — P2C's access chain is directed/strict/non-interchangeable, its
   cyclic closure is Z/3, and the trit is S_3.
2. Demote the "P2C access chain is the trit's structural home" reading from
   *candidate cross-repo lead* to *falsified-as-stated*; retain only the
   already-banked arity coincidence (`3 = 3`) with no structural match.
3. Optional mailbox awareness note back to gu-formalization (steward/Joe
   decision, not taken here): the pre-registered closure test was run P2C-side
   and returned `C-FAILS`; P2C's access chain is removed as the trit's home;
   any surviving trit interpretation must be natively unoriented and
   interchangeable. Provenance stays P2C-native; this is a finding, not a
   packet.

No status is moved by this document; it records a computed negative and awaits
steward ratification.
