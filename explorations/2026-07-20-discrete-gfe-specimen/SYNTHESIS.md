---
artifact_type: exploration
status: provisional
created: 2026-07-20
workflow: BOUNDARY-TO-ISSUANCE-WITNESS / P2C-REAL-PHYSICAL-WITNESS
construction: discrete_gfe_two_sector_specimen_candidate (arXiv:2404.08556 instantiation)
evidence_grade: primary-literature extraction + primary-PDF formula verification + finite exact-arithmetic instantiation
verification: literature/2026-07-20-discrete-gfe-primary-equation-verification.md; tests/discrete_gfe_specimen.py (exit 0; strict TEF lint clean; 16 [E] + 6 [F] = 22)
provenance: literature-native (arXiv:2404.08556) + P2C-native justification; see Section 8
directed_by: "Joe direct chat, 2026-07-20 (cross-repo session; discrete-GfE specimen lead)"
---

# Discrete GfE specimen candidate — two-sector holonomy on Bianconi's entropic cell-complex model

Authority note. This swing was directed by Joe in direct chat, 2026-07-20,
extending the same-day two-sector witness program
(`explorations/2026-07-20-two-sector-witness/`). The mailbox note
`system/mailboxes/possibility-to-capability/archive/20260720-toe-transcripts-and-discrete-gfe-specimen-lead.md`
is an untrusted evidence pointer and is the OCCASION of this work only; it is
not authority, provenance, or justification (Section 8). The receiving hourly
cycle (`RUN-20260720-103623`) had already routed arXiv:2404.08556 to exactly
this bounded primary-paper gate: "requiring an explicit Hamiltonian and
realizable order-two sector before any W1-W3 mapping." This exploration is
that gate's execution.

## 1. Pre-declared kill conditions (declared before the build)

Recorded here before any construction was attempted, as fixed in the
directing instruction:

- **K-a** — the paper's construction has no two-sector structure on a
  loop-class complex (the entropic action or Dirac structure kills the
  holonomy datum). Lead dead; record why.
- **K-b** — two sectors exist but fail witness legs (e.g., locally readable,
  or absorbed by a local completion). Wrong type; record which leg failed.
- **K-c** — passes legs but nothing is an exact Hamiltonian in the required
  sense. Specimen-shaped but gate-incomplete; state exactly what is missing.
- **K-d** (success) — two-sector, witness-passing, exact-Hamiltonian: a
  genuine specimen CANDIDATE for the Lane 1 gate. Adjudication remains the
  steward's; this exploration proposes and never admits.

## 2. Primary-paper extraction (arXiv:2404.08556, J. Phys. A 57, 365002, 2024)

Source: G. Bianconi, "Quantum entropy couples matter with geometry." Read via
the arXiv HTML full text (v3), 2026-07-20, in three targeted extraction
passes. The GU-side transcript and claim-mining rows were NOT consumed; the
paper is the source. Honest reading note: extraction was performed through an
automated web-fetch summarizer over the arXiv HTML, with cross-checks between
passes. A later primary-source pass verified the two load-bearing formulas
against the current arXiv v4 PDF; see
`literature/2026-07-20-discrete-gfe-primary-equation-verification.md`. The HTML
labels those displays Eq. (12) and Eq. (22), while the v4 PDF numbers the same
formulas Eq. (6) and Eq. (10). Future citations use the PDF numbers.

The construction, as extracted:

1. **Carrier.** A cell complex K of dimension d with N0 nodes, N1 edges, N2
   two-cells. Boundary operators B_[n] (N_{n-1} x N_n, entries 0, +1, -1 by
   incidence and orientation coherence; Eq. 10 region).
2. **Topological spinor.** Phi = (chi, psi, xi) in C^{N0} + C^{N1} + C^{N2}
   (direct sum): matter lives on ALL cells, not only nodes. Total dimension
   N = N0 + N1 + N2.
3. **Discrete Dirac operator.** D = d + d^dagger, self-adjoint, with d built
   from the gauge-coupled boundary operators conjugated by the metric,
   d = G^{-1/2} (block subdiagonal of B_[n]^(A) daggers) G^{1/2} (v4 PDF
   Eq. 10; HTML Eq. 22). gamma_0 = diag(+I_{N0}, -I_{N1}, +I_{N2}) anticommutes with D
   (Eq. 34): the spectrum is symmetric about zero.
4. **Metric degrees of freedom.** G = diag(G_0, G_1, G_2), one Hermitian
   positive block per cell dimension (in general non-diagonal within a
   block). The vacuum-entropy term of the action is built from G alone.
5. **Gauge coupling (load-bearing detail).** Minimal substitution (v4 PDF
   Eq. 6; HTML Eq. 12):
   B_[n]^(A) = B_[n]^(+) e^{-i e_n A^(n)} + B_[n]^(-) e^{+i e_n A^(n)},
   where B^(+)/B^(-) are the positive/negative incidence parts and A^(n) is
   a DIAGONAL matrix of gauge-field values on n-cells. The SAME field enters
   both incidence parts with opposite phases. Two structural consequences,
   both verified exactly in the fixture:
   - the phase e^{i A_e} acts as a HALF-LINK transporter: a full node-to-node
     passage through an edge picks up e^{2i A_e}, so the node sector
     effectively carries charge 2 relative to the naive reading;
   - consequently the naive "Z2 field" A_e in {0, pi} (link signs sigma_e =
     -1) has TRIVIAL full-link holonomy and carries no sector datum at all;
     the genuine order-two sector variable is the full-link loop holonomy
     h = prod_loop e^{2i A_e} in {+1, -1}, realized exactly by the
     quarter-turn alphabet e^{i A_e} in {1, i, -1, -i} (Gaussian integers).
6. **Induced metric.** Bosonic: G_B = I + sum_n a_n eta o (D_[n]|Phi><Phi|D_[n])
   + m_B^2 theta o (|Phi><Phi|), with eta/theta locality masks (Hadamard
   products restricting to incident / diagonal entries; Eq. 43). Fermionic
   analogue Eq. 50; combined with gauge term Eq. 52. The induced metric is
   LOCAL by construction.
7. **Entropic action.** S = sigma Tr ln G + Tr G (ln G - ln G_ind) - Tr G
   (Eq. 41; Eq. 42 is the variant with + ln G_ind). First term: entropy of
   the geometry in vacuum (log-volume); second: quantum relative entropy
   between the network metric and the matter-induced metric.
8. **Equations of motion.** All obtained by setting the variation of S to
   zero: matter (Eq. 53), metric (Eq. 56: sigma G^{-1} + ln G = T), gauge
   (Eq. 65: a diagonal constraint). PURELY VARIATIONAL.

**What is Hamiltonian and what is only variational (extraction verdict):**

- The word "Hamiltonian" does not appear in the paper. There is no time
  evolution, no Schrodinger-type equation, no dynamics. Everything is a
  static variational principle.
- The discrete Dirac operator D is nevertheless an EXACT finite self-adjoint
  operator of the model (Hermitian matrix on C^N), and the fermionic
  equation of motion is a stationary Dirac eigen-equation in D. Reading
  H := D (or H := D^2) as a Hamiltonian is a standard-field completion
  (any finite Hermitian matrix generates unitary evolution); the paper
  licenses the operator but does not perform that reading. This fork is
  named per the Construction-Fork Discipline and is load-bearing for K-c vs
  K-d (Sections 6, 9).
- The paper does not discuss gauge transformations, gauge invariance, Wilson
  loops, holonomy, flux, or boundary conditions anywhere (verified in a
  dedicated extraction pass). Whatever sector structure exists must be
  established by computation on the printed construction, not cited.

**Faithfulness boundaries of this instantiation, stated before the build:**

- The paper's worked examples are 2d and 3d complexes; the definitions are
  stated for general d. The primary specimen below instantiates d = 1
  (a ring: N2 = 0, spinor (chi, psi)) and d = 2 (a discretized cylinder,
  the paper's own example class). The d = 1 case is a specialization within
  the paper's definitions but outside its worked examples — an honest
  truncation, flagged as such.
- The metric is taken diagonal with exact rational square roots for the
  robustness sweep (the paper allows general Hermitian positive blocks);
  baseline G = I.
- Coupling constants e_n = 1; A^(2) = 0 (no gauge field on 2-cells).

## 3. The specimen candidate (construction)

Carrier shape: ONE noncontractible loop class, matching the two-sector
witness carrier (`W3-PROVENANCE-FREEZE.md` Section 1).

- **Ring R_n (primary, d = 1).** n nodes, n edges, cyclic. D is the 2n x 2n
  Hermitian matrix with the gauged 0-1 block. Gauge alphabet: u_e = e^{i A_e}
  in {1, i, -1, -i} — closed under the model's exact arithmetic, and the
  full-link holonomy h = prod u_e^2 is automatically in {+1, -1}: the
  quarter-turn alphabet IS the two-sector family (no external restriction
  imposed; u^2 in {+1,-1} identically). Sector representatives:
  A_plus = all ones (h = +1); A_minus = single edge with u = i (h = -1).
  All entries of D are Gaussian integers: exact.
- **Cylinder C_{nx x 2} (secondary, d = 2).** 2 node-rows, nx columns,
  periodic in x: 2nx nodes, 3nx edges, nx square 2-cells. D is 6nx x 6nx
  with the gauged 0-1 block and the ungauged 1-2 block. Flatness = all
  plaquette full-link fluxes +1. Sector representatives: all-ones vs a seam
  column of u = i on both horizontal edges.
- **Witness legs** are carried over from `tests/two_sector_witness.py` in
  operator form where the model permits: sector unit (one holonomy bit),
  local blindness (disk-restricted submatrix equality across sectors via
  exactly-exhibited unitary moves), loop-only access, order-two doubling,
  sector-count honesty (two-loop-class rival with four sectors), distance
  scaling (first sector-sensitive exact spectral moment sits at wrap order
  2n and scales with n), whole-family absorber (unchanged, still absorbing),
  plus failing-direction controls including the integer-winding mimic and
  the naive sigma-field pair.
- **Kill-condition probes**: the naive-Z2 unitary equivalence (K-a probe on
  the printed substitution), metric-deformation robustness (K-a probe on
  the entropic/metric sector), local readability and gauge non-closure on
  the cylinder (K-b probes), Hamiltonian-role audit (K-c probe).

## 4. Results per kill condition

Fixture: `tests/discrete_gfe_specimen.py` — deterministic, stdlib-only, exact
arithmetic throughout (Gaussian integers; Fractions for metric variants; no
floats), exit 0, strict TEF lint clean, 16 [E] + 6 [F] = 22 evidential checks
(4 [T] setup checks excluded from the headline).

**K-a — does NOT fire, with a sharp near-miss finding.** The obvious "Z2
field" embedding A_e in {0, pi} (link signs) is EXACTLY datum-free: on the
ring, D(sigma) = S D(+) S with an explicit diagonal sign unitary, and its
full-link holonomy is +1 — the paper's double-sided substitution kills that
holonomy datum completely (`sector-fail` control, exact equality). This is
precisely the failure K-a warned about, and it is real — but it is the
failure of ONE embedding, not of the construction: the surviving order-two
datum is the full-link holonomy h = prod e^{2iA} in {+1, -1}, realized
exactly by the quarter-turn alphabet, and it has operator content (below).
The metric sector does not kill it either: separation survives an exact
rational metric deformation unchanged at wrap order (`metric` leg), and the
paper's induced-metric coupling is exactly sector-blind on matched local
data (`induced` leg) — the entropic coupling neither erases nor locally
leaks the bit; the bit lives in the gauge sector, which the metric equation
of motion does not alter.

**K-b — FIRES for the paper's own 2d example class; does NOT fire for the
d=1 ring.** On the cylinder: (i) canonical sector representatives are
already separated at exact moment order 4 — LOCAL order, far below the wrap
order — so the seam is readable at trace grade by local response data;
(ii) same-class flat deformations (seam composed with u = -1 on one
vertical edge: same flux, same holonomy) also change exact moments at order
4: the model has NO gauge quotient on the 2-complex — the 1-2 block
obstructs the diagonal moves that work on the ring, so physically distinct
configurations populate one holonomy class. Blindness-as-compatibility
still holds there (a trivial-class double-seam twin matches the seam
configuration exactly on a local disk), but the protected-sector reading
fails. On the ring all legs pass (Section 5).

**K-c — the residue that remains, stated exactly.** The ring specimen's
sector datum is carried by an exact self-adjoint operator OF THE MODEL: D
is a finite Hermitian Gaussian-integer matrix, and the two sectors'
spectral moment vectors are exactly equal below order 2n and first differ
AT wrap order 2n (n = 4, 5, 6: orders 8, 10, 12; deltas -32, +40, -48).
What the paper does not supply is the Hamiltonian ROLE: no time evolution,
no dynamics, the word "Hamiltonian" absent; reading H := D as a Hamiltonian
(it generates unitary evolution as any finite Hermitian matrix does, and it
is exactly what a tight-binding treatment would call the single-particle
Hamiltonian) is a standard-field completion the paper licenses structurally
but does not perform.

**K-d — proposed, QUALIFIED (proposal only; adjudication is the
steward's).** The d=1 ring instantiation is two-sector, witness-passing,
and its sector datum is carried by an exact self-adjoint matter operator of
a published model. The qualifications are the honest gap in Section 7.

## 5. Witness-leg table (ring specimen) and transition frame fields

Legs, all exact, all with the two-sector witness's discipline:

- **bit/sector unit**: exhaustive over the quarter-turn alphabet — flat
  configurations split into exactly two full-link holonomy classes
  (128/128 on the n=4 ring; 16384/16384 among the 32768 flat cylinder
  configurations). Control: the naive sigma pair is datum-free.
- **hamiltonian/distance**: first sector-sensitive exact moment order =
  2n, scaling with loop length; local-patch mimic control fails to scale.
- **local blindness**: every proper arc admits sector representatives with
  IDENTICAL restricted operator submatrices (exact equality), with the
  moved representatives exactly unitarily equivalent to the canonical one
  via explicit diagonal unitaries in {1, i, -1, -i} (constructed, not
  asserted). Control: raw-entry reading flags a pure-convention difference
  on the datum-free sigma pair — the unitary-quotient reading is
  load-bearing.
- **loop-only access**: the full-loop holonomy reads the sector exactly;
  arc data leaves it undetermined (exhibited, not declared).
- **order-two doubling**: doubled-loop holonomy is +1 on both sectors;
  integer-winding mimic control fails doubling.
- **sector-count honesty**: exactly two sectors on one loop class; the
  two-loop rival (disjoint rings n=4, n=5) carries four sector pairs with
  pairwise-distinct exact moment vectors; count-blind comparison admits it
  (control), so the two-sector pin has teeth.
- **whole-family absorber**: a family declaring the two-sector holonomy
  absorbs the specimen — preserved, still absorbing, exactly as in the
  witness family. No capability verdict is licensed.

Transition frame fields (the seven the boundary-discriminator abstention
named), for THIS P2C-owned specimen — explicitly NOT a retroactive cure of
any external packet's own gaps:

1. independent identity — built (this exploration; literature-native +
   P2C-native, Section 8);
2. transition frame — built, kinematic: before/after = the two canonical
   gauge representatives (threading the half-flux);
3. matched resource budget — built: same complex, same metric, same probe
   alphabet, exactly matched local data (blindness legs);
4. matched access frame — built: disk vs loop access defined identically
   across sectors;
5. task delta — built: store/read one holonomy bit;
6. native response — PARTIAL: a static native response exists (first
   sector-sensitive exact moment at wrap order); a DYNAMICAL response is
   unbuildable from the paper alone — the paper has no time axis;
7. completion rival — built: the whole-family absorber remains the
   strongest rival and still absorbs.

Remaining unbuildable from the paper alone: the transition as a PROCESS
(adiabatic flux threading, response theory) — any such reading is
standard-field, not paper-native.

## 6. Five-lens council (inline)

**P2C steward (gate fidelity).** In-bounds: new files only; no edits to any
existing file; no packet import; no verdict movement; Section 10 is
proposal-only. The bounded gate recorded by the hourly receipt demanded "an
explicit Hamiltonian and realizable order-two sector before any W1-W3
mapping": delivered as an exact self-adjoint operator + an exhaustively
verified order-two sector + the full leg mapping, with the Hamiltonian-ROLE
fork flagged instead of silently assumed. Whether that satisfies
"exact-Hamiltonian" is exactly the K-c/K-d boundary and is the steward's
call, not this session's.

**Discrete-geometry theorist (faithfulness attack).** (1) d=1 is within the
paper's definitions but outside its worked examples (2d/3d); the specimen
claim must always carry the d=1 flag — it does. (2) The load-bearing
extraction is the v4 PDF Eq. 6 double-sided substitution (HTML Eq. 12); it was confirmed in two
independent extraction passes, and the fixture's internal consequences
(naive-sigma triviality, half-link/charge-2 behavior) are exactly what that
form implies — self-consistent, and the later v4 PDF pass confirms the two
load-bearing formulas while correcting their citations. (3) Declared
truncations: A^(2) = 0, e_n = 1, diagonal metric blocks in the robustness
sweep (the paper allows non-diagonal; the sweep is a sample, not a
theorem). (4) At d=1 the directional Dirac operator equals the total D, so
the induced-metric leg is faithful; the cylinder legs use total D and are
structural findings, not specimen claims. Verdict: faithful at declared
truncation; extraction risk is concentrated and named.

**Condensed-matter builder (leg quality).** The wrap-order result is the
discrete analog of periodic/antiperiodic ring spectra under flux threading,
with the model's own half-link twist; moments equal below 2n is
theorem-grade at these sizes (computed exactly, not sampled). The strongest
new control in the family is the naive-sigma kill: an entire plausible
instantiation proven datum-free by exact unitary equivalence — a trap no
prior fixture could even express. Weak points, honest: blindness quantified
over all arcs at n=5 only; the absorber stays declaration-grade (as in the
whole family); cylinder local readability is documented at trace grade
(order-4 moments) — a matrix-element disk certificate is a named follow-up,
not a claim.

**Provenance auditor (GU-contamination sweep).** Findings and fixes in
Section 8; verdict there. Summary: occasion is GU-correlated and recorded;
justification is P2C-native and survives the deletion test; no external
receipt, convention pin, or numeric output is consumed; the sector count
and carrier shape are pinned by P2C's own frozen carrier family, not by any
external packet; the fixture contains no source-native token.

**Adversarial referee (re-skin or specimen?).** Net-new beyond
`tests/two_sector_witness.py`, with specifics: (1) the carrier is a
published model's exact operator — source-groundedness is the one thing
W1-W3 could not supply and is supplied here; (2) the naive-embedding kill
is a new executable result ABOUT THE PAPER, not a re-parameterization;
(3) the distance leg is upgraded from declared signature to computed
operator statement (moment equality below wrap order); (4) the cylinder
nonclosure and order-4 readability findings are new boundary data about the
model family. Re-skinned by design: completion sweep, absorber, count
controls (family continuity keeps the absorber comparable). Verdict:
EXCEEDS; not a re-skin. Referee's flag, adopted: the pass is a property of
the d=1 member; the paper's own 2d example class FAILS the blindness leg at
moment grade — this exploration must never be cited as "the 2404.08556
model passes the witness."

## 7. Honest gap versus the gate

1. **Hamiltonian ROLE** (the K-c residue): the paper is purely variational;
   H := D is a standard-field completion. If the gate's "exact-Hamiltonian"
   means "sector datum carried by an exact self-adjoint operator of the
   model," the ring specimen satisfies it; if it means "the source itself
   treats the operator as a Hamiltonian generating dynamics," it does not.
2. **No dynamical transition**: frame field 6 is static-only from this
   source; the before/after pair is kinematic juxtaposition.
3. **d=1 specialization**: inside the definitions, outside the worked
   examples; and the worked-example class (d=2) fails K-b — the specimen
   is the d=1 member, full stop.
4. **Extraction grade**: the two load-bearing formulas are hand-verified
   against the current arXiv v4 PDF. Broader prose extraction remains
   cross-checked HTML reading and is not a line-by-line published-version audit.
5. **The whole-family absorber still absorbs**: no physical issuance,
   capability, or finality verdict is licensed, exactly as across the
   witness family.

## 8. Provenance (occasion/justification split, with self-attack)

- **Occasion.** The mailbox note (archived with a processing receipt by
  `RUN-20260720-103623`) pointed at arXiv:2404.08556. That note is an
  untrusted third-party pointer; it is the OCCASION of this swing and
  nothing else. The timing correlation with the sender's activity is real
  and recorded here, not laundered.
- **Justification (P2C-native, each item frozen before this swing).**
  (1) The portfolio's own next-swing language demands a "source-grounded
  exact-Hamiltonian topological specimen" — a P2C gate, not an external
  request. (2) The two-sector synthesis (Section 1 item 4) had already
  named the missing rung: "standard-field grounding exists in the
  literature: order-two flat holonomy sectors on multiply-connected
  spaces," with a Lane 2 source-spine freeze as the natural bounded
  follow-up. (3) P2C's own hourly receipt routed this exact paper to this
  exact bounded gate before this session ran. The carrier shape (one loop
  class, two sectors) is pinned by `W3-PROVENANCE-FREEZE.md` Section 2.1 —
  P2C's own carrier family — not by any external packet.
- **Deletion test.** Remove the external transcripts and the mailbox note
  from history: the P2C gate, the named missing rung, and the paper (public
  literature) all still exist, and this construction remains well-posed and
  motivated. What does NOT survive deletion is the fact that P2C's
  attention landed on THIS paper TODAY — that is occasion, and P2C's gates
  do not require occasion independence (same ruling as the W3 freeze).
- **Self-attack for GU-shaped contamination, findings and dispositions:**
  1. *The suggestion coincidence.* The mailbox note suggested checking this
     paper against the two-sector legs, and that is what happened. Fix:
     authority is Joe's direct-chat instruction; the executed gate is the
     one P2C's own receipt had already defined; the note's other
     suggestions (entropic discriminator leg, the second paper) were NOT
     executed — the work tracks the P2C gate, not the note's menu.
  2. *Sector-count retuning.* "Two sectors because the sender's packet has
     two" would be construction-from-consequence. Fix: two sectors is the
     frozen minimal member of P2C's carrier family (W3 Section 2.1), and
     the quarter-turn alphabet's h in {+1, -1} is FORCED by the paper's
     v4 PDF Eq. 6 (HTML Eq. 12) plus exact arithmetic — verified as a closure theorem in the
     fixture, not chosen.
  3. *Vocabulary/receipt leakage.* Grep-level check: no external
     repository's token, receipt, convention pin, plane count, or numeric
     output appears in the fixture or this synthesis; the only external
     object consumed is the published paper.
  4. *Retroactive-provenance overreach.* Explicit nonclaim: the frame
     fields in Section 5 belong to this P2C-owned specimen; they do not
     cure any external packet's independent-identity gap, and the standing
     preflight abstention on that packet is untouched.
  - Auditor's verdict: firewall holds at declaration grade; the occasion
    correlation and the PDF/HTML equation-number divergence are named, not
    hidden. The load-bearing formulas are now primary-PDF verified.

## 9. Validation

Executed 2026-07-20:

```powershell
python tests/discrete_gfe_specimen.py
python tests/tef_check_tag_linter.py --strict tests/discrete_gfe_specimen.py
```

Fixture: exit 0, all checks match expectations, runtime under one second,
headline:

```text
16 [E] + 6 [F] = 22
```

Four `[T]` setup checks excluded from the headline. Strict lint: registry
convention, zero violations, zero advisories.

## 10. Proposed steward disposition (proposal only, not executed)

- Record this exploration as **K-d qualified: specimen CANDIDATE at
  exploration tier** — the d=1 ring instantiation of arXiv:2404.08556 is a
  two-sector, witness-passing carrier whose sector datum is carried by an
  exact self-adjoint matter operator of a published model — with the K-c
  residue (Hamiltonian ROLE is a standard-field completion) attached
  inseparably. The steward adjudicates whether the gate's
  "exact-Hamiltonian" accepts that reading; this session proposes and does
  not admit.
- Bounded next steps, in order of information per cost: (a) seek a frozen
  source-grounded before/after transition with matched frames; (b) fold this
  specimen into a future source spine only if that directly supports the
  transition gate; (c) preserve the Hamiltonian-ROLE fork; (d) optional
  matrix-element disk certificate for the cylinder's order-4 readability.
- The cylinder findings (no gauge quotient; local readability at moment
  order 4; the naive-sigma datum-free embedding) are boundary data worth
  keeping visible: they are the exact reasons this model family cannot be
  cited wholesale as a witness-passing carrier.
- No notification to any external repository is taken or implied here;
  that remains a steward/Joe mailbox decision. The GU-facing position of
  the two-sector synthesis Section 9 is unchanged.
