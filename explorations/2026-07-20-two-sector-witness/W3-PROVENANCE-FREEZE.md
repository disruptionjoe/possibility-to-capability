---
artifact_type: exploration
status: provisional
governance_role: provenance_typing_freeze
constitutional: false
created: 2026-07-20
workflow: BOUNDARY-TO-ISSUANCE-WITNESS / P2C-REAL-PHYSICAL-WITNESS
construction: two_sector_flat_z2_holonomy_witness + kramers_probe_class_control
lineage: DEP-NATIVE-SOURCE-DATUM
directed_by: "Joe direct chat, 2026-07-20 (cross-repo session; P2C-side W1-W3 build)"
verification: tests/two_sector_witness.py (exit 0; strict TEF lint clean; 17 [E] + 10 [F] = 27)
---

# W3 provenance and typing freeze — two-sector holonomy witness

This file is the W3 rung: it freezes the identity, assumptions, and
non-retuning declarations of the W1 fixture (two-sector flat-Z2 holonomy
witness) and the W2 fixture (Kramers probe-class control), both implemented in
`tests/two_sector_witness.py`, so that they are P2C-owned from birth. It is a
repo-owned typing freeze at exploration tier. It creates no canon, moves no
verdict, and imports no source-repository content.

## 1. Identity

- Object: the two-sector flat-Z2 holonomy witness model (W1) and its
  Kramers probe-class control (W2), as implemented at fixture grade in
  `tests/two_sector_witness.py`.
- Owner: possibility-to-capability. These are repo-owned test constructions in
  the P2C physical-witness family, sibling to
  `tests/physical_witness_discriminator.py` (superconducting ring, integer
  winding), `tests/bec_circulation_witness.py` (neutral integer winding), and
  `tests/topological_order_witness.py` (four-sector Z2 topological order).
- Lineage: `DEP-NATIVE-SOURCE-DATUM`. The witness's identity stands on P2C's
  own witness program and research questions, enumerated in Section 2. It is
  not derived from, owned by, or justified by any external repository's
  consequences.
- Carrier shape, stated honestly: ONE noncontractible loop class; sector pair
  given by loop holonomy plus one or minus one; sector count exactly TWO. No
  four-sector arithmetic, no total-quantum-dimension claim, and no
  topological-entanglement-entropy claim transfers from the four-sector
  fixture; the nonlocal unit is typed as one holonomy bit.

## 2. Native justification (why P2C builds this, in P2C's own vocabulary)

Each construction answers a question P2C had already posed to itself in its
own frozen surfaces before this swing:

1. **The minimal untested member of P2C's own carrier family.** P2C's witness
   family already spans integer-winding carriers (ring, BEC: sector group Z)
   and a four-sector carrier (topological order: two independent order-two
   loop classes). The one-loop-class, order-two carrier — where a doubled loop
   is trivial — is the minimal member of that family and was untested. The
   topological-order handoff
   (`explorations/2026-07-19-topological-order-witness/SYNTHESIS.md`)
   explicitly requested "a new completion rival that attacks the loop/distance
   leg"; the integer-winding mimic and four-sector mimic in W1 are exactly
   such rivals, and they require the order-two and sector-count legs to be
   rejected.
2. **A probe-class axis for the hierarchy's access level.** P2C's hierarchy
   types access as "which observations and actions the interface exposes."
   Every prior P2C fixture indexed access only by the geometry of support
   (local disk versus noncontractible loop). W2 tests a P2C-native question:
   whether access must additionally be typed by the algebra of admissible
   probes — whether an agent with loop-shaped access but a restricted probe
   class has the same access type as an agent with an unrestricted probe
   class. The fixture's answer at finite grade: no; the readable/unreadable
   split is (access route) x (probe algebra), and collapsing the second index
   loses a real distinction. This is a candidate refinement of the access
   level, reported to Lane 1.
3. **The IRD application demand.** The indexed-restriction-diagram handoff
   (`explorations/2026-07-19-indexed-restriction-diagram/SYNTHESIS.md`)
   directed the next high-information use toward the topological-order track
   issuing restriction data rather than another free toy. The two-sector
   carrier with its probe-class split supplies the sharpest finite restriction
   structure P2C currently owns for that track: two access routes, two probe
   classes, and an executable blindness proof for one quadrant.

## 3. Assumptions and construction fork

- W1 is a finite signature model, not a Hamiltonian simulation. Its physics
  vocabulary (holonomy sector, local disk, noncontractible loop, code
  distance) is carried at the same toy-executable grade as the prior witness
  fixtures.
- W2's antiunitary structure J with J squared equal to minus the identity is
  the standard Kramers/quaternionic structure of time-reversal for
  half-integer spin, imported at literature grade from standard quantum
  mechanics (Wigner; Kramers degeneracy). It is a standard-field construction,
  named per the Construction-Fork Discipline. A program-native alternative
  (any other antiunitary structure squaring to minus one on the fiber) is
  materially admissible; the W2 results are scoped to the standard
  construction and its unitary equivalents.
- The W2 commutant, Kramers-degeneracy, blindness, and parity results are
  proven by exact enumeration on the minimal fiber (quaternionic dimension
  one, complex dimension two) over a Gaussian-integer grid. The
  dimension-free mechanism (readout at the J-partner equals the conjugated
  readout, hence Hermitian J-commuting readouts agree on every Kramers pair)
  is checked as an exact identity on the grid; its general-dimension statement
  is a named follow-up, not a claim of this freeze.
- Blindness is scoped to Hermitian probes (real-valued observables). A
  non-Hermitian J-commuting probe can have sector-dependent complex
  expectation (the fixture displays this for the quaternion-i generator); its
  values are purely imaginary conjugate pairs and are not measurement
  outcomes. This scoping is stated here so it cannot be quietly widened.

## 4. Non-retuning declarations

Every free parameter of W1/W2 is listed here with its origin. None was chosen
by reference to any external repository's numeric output or desired
consequence:

- sector count 2, one loop class: the minimal untested member of P2C's own
  carrier family (Section 2.1);
- linear sizes (4, 5, 6, 7) and local patch radius 2: inherited unchanged
  from `tests/topological_order_witness.py`;
- completion-kind list: the house completion classes carried unchanged, plus
  the two new rivals (integer-winding mimic, four-sector mimic) that the
  order-two and sector-count legs exist to reject;
- probe grid (0, 1, -1, i, -i, 1+i): the smallest Gaussian-integer set that
  spans real/imaginary parts and mixed entries for exact arithmetic;
- J convention (J(v1, v2) = (-conj v2, conj v1)): the standard textbook form;
- sector states (1,0) and its J-partner (0,1): the canonical basis pair.

Declared for the record: no parameter of this fixture encodes, targets, or
reproduces any external repository's plane counts, energy scales, payload
accounting, commit contents, or falsifier structure. If a future edit tunes
any parameter to make an external consequence come out, that edit breaks this
freeze and requires a superseding v2 that says so.

## 5. Provenance firewall

- The frozen GU evidence packet `GU-COFLIP-HOLONOMY-FREEZE-2026-07-20`
  (gu-formalization commit `32e3603f12aae3fc76298534c47a204b5584b171`) is the
  OCCASION of this swing: it prompted the scheduling of a carrier shape P2C's
  own program had already parameterized. P2C's gates permit frozen candidate
  evidence to act as a ranking/watch trigger; a trigger is not provenance.
- The packet is NOT: provenance for W1/W2, justification for W1/W2, authority
  for this work (authority is Joe's direct-chat instruction of 2026-07-20),
  a source of imported constructions, or a consequence-target. No GU receipt,
  convention pin, plane count, or probe output is consumed by the fixture.
- Deletion test: W1/W2 remain well-posed, motivated, and true with the GU
  packet removed from history. Their justification (Section 2) cites only
  P2C-owned artifacts and standard literature.
- Honest residual, preserved not hidden: the timing correlation between the
  GU packet's arrival and this swing is real and is recorded here rather than
  laundered. Independence of JUSTIFICATION is established by this freeze;
  independence of OCCASION is not claimed and is not required by P2C's gates.
- This freeze covers W1/W2 only. It does not and cannot retroactively create
  independent provenance for the GU packet itself; the packet's own
  independent-identity gap (its Section 6, and P2C's 2026-07-20 preflight
  abstention) remains exactly where it was.

## 6. What this freeze does not establish

- No exact-Hamiltonian specimen: W1/W2 are finite signature and operator
  models, not a Hamiltonian's ground-state sectors.
- No transition adjudication: W1/W2 supply carrier and reader structure, not
  a before/after transition with matched resource and access frames, task
  delta, native response, and completion rival. The boundary-discriminator
  abstention on the GU packet is untouched.
- No capability, finality, issuance, or source-truth movement; no packet
  import; no external action; the whole-family absorber remains live.

## 7. Falsifiers and reopen conditions

This freeze is superseded (by a v2 naming the kill, never edited in place) if:

- W3-F1: any fixture parameter is shown to have been chosen to reproduce an
  external repository's numeric output (breaks Section 4);
- W3-F2: the W2 blindness result is shown to depend on the grid rather than
  the algebra (a J-commuting Hermitian probe outside the grid form that reads
  the sector at this fiber dimension);
- W3-F3: the access-level refinement (probe-class index) is shown to collapse
  — a principled argument that probe algebra is already absorbed by an
  existing hierarchy level on all admissible cases;
- W3-F4: the carrier-family claim in Section 2.1 is shown false (the
  one-loop-class order-two carrier was already covered by an existing P2C
  fixture).
