---
artifact_type: exploration
status: provisional
created: 2026-07-20
workflow: BOUNDARY-TO-ISSUANCE-WITNESS / P2C-REAL-PHYSICAL-WITNESS
construction: two_sector_flat_z2_holonomy_witness + kramers_probe_class_control
evidence_grade: finite_executable_discriminator + definitional_hierarchy_mapping
verification: tests/two_sector_witness.py (exit 0; strict TEF lint clean; 17 [E] + 10 [F] = 27)
provenance_freeze: W3-PROVENANCE-FREEZE.md
directed_by: "Joe direct chat, 2026-07-20 (cross-repo session; adjudication + P2C-side W1-W3 build)"
---

# Two-sector holonomy witness — adjudication and W1-W3 synthesis

Authority note. This swing was directed by Joe in direct chat, 2026-07-20.
The mailbox proposal and the GU packet are frozen evidence and proposal data;
neither is authority for anything done here, per this repo's AGENTS.md and the
2026-07-20 Lane A finding that the GU freeze is "not an accepted P2C witness
or authority to execute W1-W3."

## 1. Adjudication of GU-COFLIP-HOLONOMY-FREEZE-2026-07-20

Packet: gu-formalization
`explorations/source-packet-coflip-holonomy-freeze-2026-07-20.md`, frozen at
commit `32e3603f12aae3fc76298534c47a204b5584b171`. Mailbox proposal received
and archived with a processing receipt by
`RUN-20260720-063650-repository-work-cycle-cai-hourly`; boundary preflight
executed by the 2026-07-20 hourly cycle
(`explorations/2026-07-20-coflip-holonomy-boundary-preflight/`). This
adjudication is consistent with both and re-runs neither.

**Admitted AS (unchanged from the standing dispositions, now stated in one
place):**

- Frozen, commit-pinned, GU-owned **qualified candidate evidence** for the
  Lane 1 source-grounded-specimen gate — an upgrade of the earlier ETA/Z2
  habitat signal from mailbox-only ranking evidence to matrix-grade candidate
  evidence with typed grades, explicit nonclaims, pre-declared falsifiers,
  and independently re-runnable receipts.
- A **specification and verification target** for what a faithful two-sector
  holonomy carrier must look like (one loop class, order-two holonomy,
  reader-class split), usable as design pressure on P2C-owned constructions.
- A **ranked watch/trigger input**: legitimate occasion for scheduling
  P2C-native work that P2C's own program had already parameterized.

**NOT admitted as:**

- Not an imported packet (no acceptance-gate run; imported-packet discipline
  not invoked).
- Not a source-grounded specimen or witness. The portfolio's next-swing
  language demands a "source-grounded exact-Hamiltonian topological
  specimen"; the packet declares itself kinematic and Hamiltonian-free. The
  gap is categorical, not incremental.
- Not adjudicable by the boundary discriminator: the 2026-07-20 preflight's
  `ABSTAIN_PACKET_NOT_ADJUDICABLE` stands — seven frame fields (independent
  identity, transition frame, matched resource budget, matched access frame,
  task delta, native response, completion rival) are absent by the packet's
  own statement.
- Not provenance, justification, or authority for any P2C construction
  (Section 5 of `W3-PROVENANCE-FREEZE.md`).
- Not movement of any source truth, claim status, capability, finality,
  canon, or public posture, in either direction.

**Exactly which P2C-side constructions would upgrade it** (and their status
after this swing):

1. A P2C-owned two-sector carrier with the discriminator legs at fixture
   grade — **built this swing (W1)**.
2. A P2C-owned operationalization of the reader class (blind probe algebra
   versus reading probe) — **built this swing (W2)**.
3. P2C-side identity, assumptions, and non-retuning frozen in P2C's own
   vocabulary, so the constructions are source-owned from birth — **built
   this swing (W3, `W3-PROVENANCE-FREEZE.md`)**.
4. Still missing after this swing, stated honestly: an exact-Hamiltonian or
   otherwise physically grounded realization of the two-sector carrier
   (standard-field grounding exists in the literature: order-two flat
   holonomy sectors on multiply-connected spaces; a Lane 2 source-spine
   freeze for this carrier is the natural bounded follow-up); a before/after
   TRANSITION on that carrier with matched resource and access frames, task
   delta, native response, and strongest completion rival (this is what the
   boundary discriminator needs to lift its abstention); and, for anything to
   RETURN as a GU-relevant instance, a GU-side source-owned packet satisfying
   GU's own interface contract — which P2C cannot and does not build.

Net disposition in P2C terms: **qualified candidate evidence, bounded below
witness-import status; the packet's descendant becomes gate-eligible only
through the chain above, of which rungs 1-3 now exist at exploration tier.**

## 2. Question

Two questions, both P2C-native (justification frozen in
`W3-PROVENANCE-FREEZE.md` Section 2):

1. Does the witness discipline survive the minimal holonomy carrier in P2C's
   own family — one noncontractible loop class, two sectors, order-two
   holonomy — including rivals (integer-winding mimic, four-sector mimic)
   that no previous fixture could reject?
2. Must the hierarchy's access level be typed by probe algebra as well as by
   the geometry of access — can an agent hold loop-shaped access and still be
   provably unable to read the sector because its probe class is
   quaternionic?

## 3. W1 — two-sector flat-Z2 holonomy witness

The fixture (`tests/two_sector_witness.py`, W1 sections) models a carrier
with sector pair holonomy plus one / minus one and carries the four
discriminator legs unchanged: a nonlocal holonomy-bit unit, local-disk
blindness, loop-only access, and distance scaling beyond the local patch
radius. Two legs are new to this carrier:

- **order-two loop composition**: a doubled loop is trivial on both sectors.
  The integer-winding mimic (a ring/BEC-type carrier) passes bit, loop,
  local, distance, and persistence legs but fails doubling — the first
  executable separation of order-two holonomy carriers from integer-winding
  carriers in the P2C family;
- **sector-count honesty**: the carrier declares exactly two sectors; a
  four-sector toric-type mimic differs from the candidate ONLY in sector
  count, and a count-blind comparison admits it (failing-direction control).
  The two-sector pin therefore has teeth and is load-bearing.

Ordinary local completions fail at least one signature. The bit-only mimic
reproduces the scalar unit but fails loop and distance. Whole-family
admission with the two-sector phase declared in still absorbs the witness:
the F1 fixed-family seam is preserved, not adjudicated. Neutrality holds
under global sector relabel (the choice of which sector is called plus one is
a lift convention); a lift-sensitive scorer fails as intended.

## 4. W2 — Kramers probe-class control

Probes on the holonomy fiber are exact 2x2 complex operators; J is the
standard antiunitary quaternionic structure with J squared equal to minus the
identity; the sector states form a Kramers pair under J. At this finite
grade the fixture PROVES, by exact enumeration:

- **commutant**: J-commutation is exactly the quaternionic block form
  (checked over the full four-parameter Gaussian-integer grid, 1296
  operators);
- **mechanism identity** (dimension-free in form): readout at the J-partner
  equals the conjugated readout, for every quaternionic probe and every
  sample state;
- **Kramers**: every Hermitian J-commuting probe on the fiber is a real
  multiple of the identity — doubly degenerate spectrum;
- **blindness**: therefore every Hermitian J-commuting probe — local or
  loop — reads both sectors equally, and the mod-2 sector readout through
  that class is forced even;
- **reader split**: a single non-quaternionic Hermitian loop probe reads the
  sector sign exactly; the same non-quaternionic probe composed with disk
  data still reads nothing (loop access remains necessary). Reading requires
  BOTH the loop route AND the non-quaternionic algebra.

This operationalizes "the reader is the non-quaternionic object" as a
P2C-owned, executable statement about probe classes, with no external
convention consumed. Scoping preserved out loud: blindness is a statement
about Hermitian (observable) probes; the anti-Hermitian quaternion-i
generator has sector-dependent purely imaginary expectation, which is not a
measurement outcome — the fixture displays this rather than hiding it.

## 5. W3 — provenance and typing freeze

`W3-PROVENANCE-FREEZE.md` (sibling file) freezes identity, lineage
(`DEP-NATIVE-SOURCE-DATUM`), native justification, assumptions, construction
fork, non-retuning declarations, the provenance firewall (occasion versus
justification, with the deletion test), explicit non-establishments, and
four named falsifiers W3-F1..F4. W1/W2 are source-owned from birth under that
freeze; the GU packet's own provenance gap is explicitly NOT cured by it.

## 6. Five-lens council (inline)

**P2C steward.** In-bounds: new files only, no source-repo edit, no packet
import, no verdict movement; the Lane A qualified-candidate boundary and the
Lane 1 preflight abstention both stand unchanged. The swing is Lane 1 work
under P2C-REAL-PHYSICAL-WITNESS (carrier family extension) with a Lane 1
finding (probe-class access refinement) reported upward. LANE-STATE and
portfolio annotations for this swing are PROPOSED in Section 9 and not
executed; existing steward files are untouched this session. Flag: the swing
was Joe-directed outside the hourly cycle; the hourly steward should
reconcile Section 9 on its next pass rather than treating this exploration as
unregistered drift.

**Topological-order theorist.** The two-sector honesty is the load-bearing
physics point. What transfers from the four-sector fixture: local-disk
blindness, loop-only access, distance scaling, the whole-family absorber, the
completion-class sweep. What does NOT transfer and is correctly absent: the
four-sector arithmetic, any total-quantum-dimension or
topological-entanglement-entropy claim (the nonlocal unit here is one
holonomy bit, honestly renamed), and the e/m anyon relabel (replaced by the
lift relabel, the correct neutrality operation for a flat holonomy sector
pair). What is genuinely new: the order-two doubling leg — the previous
fixtures literally could not express "doubling a loop kills the signal,"
which is the signature separating Z/2 holonomy from integer winding. Honest
ceiling: a flat-holonomy sector pair is not topological ORDER in the
Hamiltonian sense (no local topological degeneracy claim, no anyons); the
carrier is kinematic, which is exactly what the fixture types it as.

**Provenance auditor.** Attacked the W3 freeze for GU contamination; findings
and fixes, all applied:

1. *Occasion contamination.* The swing was scheduled because a GU packet
   arrived. Fix: occasion/justification split with a deletion test (freeze
   Section 5); the justification cites only P2C-owned handoffs
   (topological-order handoff's completion-rival request, IRD application
   demand) and a P2C-native access-level question. Residual preserved: the
   timing correlation is recorded, not laundered.
2. *Vocabulary leakage.* An early draft described W2 in source-native terms.
   Fix: the fixture and freeze use only P2C/standard vocabulary (holonomy
   sector, Kramers pair, quaternionic probe class); grep-level check: no
   source-native token, receipt, or convention pin appears in
   `tests/two_sector_witness.py`.
3. *Sector-count retuning.* "Two sectors because the packet says two" would
   be construction-from-consequence. Fix: two sectors reframed and frozen as
   the minimal untested member of P2C's own carrier family, with the
   four-sector and integer-winding rivals kept in the sweep so the choice is
   a completed family sweep, not a match to an external target; non-retuning
   declarations enumerate every parameter's origin (freeze Section 4).
4. *J-structure origin.* Fix: J imported at literature grade from standard
   quantum mechanics (Kramers/Wigner), named as the standard-field branch of
   a construction fork; the commutant is DERIVED inside the fixture rather
   than cited from any external no-go.
5. *Retroactive-provenance overreach.* The preflight synthesis warned that a
   P2C preregistration "must not claim that doing so retroactively creates
   source-independent provenance for this GU packet." Fix: explicit nonclaim
   in freeze Section 5 — W3 covers W1/W2 only.

Auditor's verdict: the firewall holds at declaration grade. What declaration
cannot supply — independent standard-field grounding of the carrier in
primary literature — is named in Section 1 item 4 as the honest remaining
rung, not papered over.

**Condensed-matter builder.** Fixture quality: deterministic, stdlib-only,
exact Gaussian-integer arithmetic (no float tolerance anywhere), registry
convention with 10 failing-direction controls, strict TEF lint clean, exit 0.
The Kramers claims are computed, not asserted: the commutant by full grid
enumeration, Hermitian-quaternionic scalarity by direct test, blindness on
the enumerated Hermitian class, and the conjugation identity as an exact
complex equality. Weak point flagged honestly: the fiber is quaternionic
dimension one, where "Hermitian J-commuting implies scalar" is the strongest
possible degeneracy; in higher-dimensional fibers the right statement is
per-Kramers-pair degeneracy via the conjugation identity, which the fixture
checks in exact form but only instantiates minimally. That generalization is
the named M-tier follow-up, not a claim.

**Adversarial referee.** Does W1/W2 exceed the existing witness, or is it a
re-skin? Specifics: the bit leg, disk blindness, distance leg, whole-family
absorber, and completion sweep are deliberate re-parameterizations of
`tests/topological_order_witness.py` — family continuity is what makes the
absorber comparable across carriers, and the referee does not count it as
new evidence. The net-new content is exactly three things: (1) the order-two
loop-composition leg, inexpressible in every prior P2C fixture (integer
winding never trivializes under doubling; the four-sector fixture had no
composition check at all), with the integer-winding mimic as its
failing-direction rival; (2) the probe-class axis — no prior P2C fixture
types access by probe algebra, and W2's blindness result is a finite
theorem, not a signature stipulation: the sector is unreadable BY A CLASS
even through the correct access route; (3) the sector-count honesty control
with executable teeth (count-blind comparison admits the mimic). Verdict:
EXCEEDS on legs (1) and (2), which are the two legs the GU-side ladder
actually needed operationalized; re-skins elsewhere by design. The referee
also confirms the fixture does NOT overclaim its strongest number: 27
evidential checks include 10 controls, and the whole-family absorber still
absorbs — no capability verdict is licensed anywhere in the run.

## 7. Validation

Executed 2026-07-20:

```powershell
python tests/two_sector_witness.py
python tests/tef_check_tag_linter.py --strict tests/two_sector_witness.py
```

Fixture: exit 0, all checks match expectations, headline:

```text
17 [E] + 10 [F] = 27
```

Four `[T]` setup checks are excluded from the headline. Strict lint: registry
convention, zero violations, zero advisories.

## 8. Verdict and nonclaims

`TWO_SECTOR_HOLONOMY_WITNESS / KRAMERS_READER_SPLIT /
UNDISCHARGED_VS_WHOLE_FAMILY`.

- No physical issuance, capability, or finality verdict is established; the
  whole-family absorber remains live and absorbing.
- No exact-Hamiltonian specimen exists; the carrier is kinematic and typed
  so.
- No GU truth, claim status, packet-import status, canon, or public posture
  moves; the GU packet remains frozen qualified candidate evidence and the
  boundary-discriminator abstention stands.
- The access-level probe-class refinement is a candidate refinement reported
  to Lane 1, not a hierarchy revision.
- No external action; new files only.

## 9. Handoff and proposed steward annotations (proposal only, not executed)

For the hourly steward's next reconciliation pass, this swing proposes:

- portfolio `P2C-REAL-PHYSICAL-WITNESS`: record a
  `swing_2026_07_20_two_sector` entry — W1-W3 built at exploration tier per
  Joe direct-chat direction; carrier family now spans integer-winding,
  four-sector, and one-loop-class order-two carriers; do not repeat this
  fixture without an exact-Hamiltonian grounding, a failed control, or a new
  completion rival attacking the order-two or probe-class legs.
- portfolio next-swing language: the source-grounded exact-Hamiltonian demand
  is unchanged; the natural bounded Lane 2 follow-up is a source-spine
  literature freeze for order-two flat-holonomy carriers, mirroring
  `literature/2026-07-19-topological-order-source-freeze.md`.
- Lane 1 finding upward: candidate access-level refinement (probe-algebra
  index), with `W3-PROVENANCE-FREEZE.md` W3-F3 as its kill condition.
- The GU-facing position is unchanged: re-open GU-adjacent adjudication only
  on a frozen input satisfying the seven preflight fields or a GU-side
  source-owned packet under GU's interface contract. Any notification to GU
  is a mailbox proposal decision for the steward/Joe, not taken here.
