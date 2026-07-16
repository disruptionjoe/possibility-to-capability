---
artifact_type: exploration
status: provisional
governance_role: physical_witness_freeze
constitutional: false
created: 2026-07-16
workflow: BOUNDARY-TO-ISSUANCE-WITNESS / P2C-REAL-PHYSICAL-WITNESS
construction: superconducting_ring_persistent_supercurrent
evidence_grade: literature_grade_physics + definitional_hierarchy_mapping + toy_executable_discriminator
verification: tests/physical_witness_discriminator.py (exit 0; --strict lint clean; headline 7 [E] + 4 [F] = 11)
---

# Witness freeze — superconducting ring, quantized persistent supercurrent

**Tier and guards.** Exploration. No source-repo claim, GU/TI/TaF verdict,
physical-issuance claim, finality claim, public posture, or cross-repository
identity moves here. Physics is cited at **literature grade** (textbook /
established-consensus); the hierarchy mapping is **definitional draft**; the
discriminator fixture is **toy-executable** at the grade its own [T]/[E]/[F]
headline states. The attached `REFEREE-REPORT.md` GOVERNS grades and
corrections — read it before citing.

This is a REACH swing (portfolio `reach_swing_cadence`). Failure is a
first-class result. Per Joe's binding frontier constraint (direct chat,
2026-07-16) the candidate was chosen as the STRONGEST real capability-change I
would defend to a skeptical physicist, not a toy chosen to make the completion
comparison tractable, accepting that it may die under the completion attack.

Selection rationale, the scored shortlist, and the alternates live in the
sibling `SYNTHESIS.md`. This file freezes the chosen system.

---

## 0. The frozen system

A thin, singly-connected **superconducting ring** (a loop of a conventional
BCS superconductor — e.g. an aluminium or niobium micro-ring — of cross
section small compared with the penetration depth), threaded by an external
magnetic flux and cooled through its critical temperature `Tc`.

### 0.1 Source theory (cited, not absorbed; literature grade)

- **BCS microscopic theory** (Bardeen–Cooper–Schrieffer 1957): a phonon-mediated
  attractive interaction opens a gap `Δ` and condenses electrons into Cooper
  pairs of charge `2e`.
- **Ginzburg–Landau (GL) theory** (1950) and the **London equations** (1935):
  a complex order parameter `ψ = |ψ| e^{iθ}` whose phase `θ` is the load-bearing
  degree of freedom; the supercurrent is `j_s ∝ |ψ|^2 (ħ∇θ − (2e/c)A)`.
- **Fluxoid quantization** (F. London 1948; Deaver–Fairbank and Doll–Näbauer,
  1961): single-valuedness of `ψ` around the closed ring forces the **fluxoid**
  `Φ' = Φ + (m*c/e*)∮ v_s·dl` to be an integer multiple of the flux quantum
  `Φ_0 = h/2e ≈ 2.07×10^{-15} Wb`. In the thick-ring limit the trapped magnetic
  flux itself is quantized in units of `Φ_0`.
- **Persistent supercurrent** and **phase slips**: a circulating supercurrent in
  the ring decays only by a phase-slip event that must push `|ψ|→0` somewhere,
  crossing a free-energy barrier `ΔF` that is macroscopic for a
  above-nanoscale ring; the resulting lifetime is astronomically long (many
  times the age of the universe for laboratory rings), i.e. **effectively
  non-decaying**.

These are established textbook results (Tinkham, *Introduction to
Superconductivity*; Annett, *Superconductivity, Superfluids and Condensates*).
No GU/TI/TaF import is used; nothing here is upgraded above literature grade.

### 0.2 Region (the frozen state space)

The control region is the plane of two parameters: temperature `T` and applied
flux `Φ_app` (in units of `Φ_0`). Two phases share this region across the line
`T = Tc`:
- **N (normal):** `T > Tc`. Finite resistivity `ρ > 0`; `ψ = 0`; no order.
- **S (superconducting):** `T < Tc`. `ψ ≠ 0`; the ring's phase winding
  `n = (1/2π)∮∇θ·dl ∈ ℤ` is a well-defined integer.

The critical temperature `Tc`, the gap `Δ(T)`, and the penetration depth
`λ(T)` are frozen material data of the chosen ring.

### 0.3 Intervention menu (fixed) and budget

The fixed menu of interventions, each with a declared resource cost, is:
- `COOL(T→T')`: change temperature. Cost: the free energy / entropy budget of
  the refrigerator to reach `T'` from `T`.
- `THREAD(Φ_app)`: change the external flux through the ring. Cost: the field
  source's energy to establish `Φ_app`.
- `PROBE_READ`: measure the trapped flux / circulating current
  (SQUID magnetometry, or transport). Cost: a fixed metrology budget, identical
  for N and S.
- `DEFORM`: a smooth local geometric deformation of the ring that does not cut
  it (a declared local operation). Cost: mechanical, bounded.

**Budget normalization (the matched-frame rule).** All before/after comparisons
are made at a **fixed final temperature `T_f < Tc`** and a **fixed total
energy budget**. The candidate frame (ring in S) and the null/completion frames
(a ring held in N — e.g. a non-superconducting reference conductor of matched
geometry at the same `T_f`, or the same ring above `Tc`) are compared **after
the same `COOL` and `THREAD` budget has been spent on both**. The cooling energy
is therefore a MATCHED resource, not a difference between the branches.

**Honest labeling (referee correction R-D1, applied).** There are two distinct
comparisons and the freeze must not conflate them:
- the **literal single-system before/after** — the SAME ring at `T > Tc` (N)
  versus `T < Tc` (S) — which is NOT budget-matched (the branches sit at
  different temperatures); and
- the **budget-matched counterfactual pair** — the ring in S versus a reference
  normal conductor at the same `T_f` and the same spent budget — which IS
  matched but compares two systems, not one system's two times.
The capability claim below is a **frame-indexed** claim (Hierarchy v0.2 §2.5:
the normalization frame is a parameter of the Capability type, not a derived
fact); its declared frame `N` is the matched-budget counterfactual pair. The
resource-completion attack is answered WITHIN that declared frame, and the
freeze claims nothing frame-free. This is load-bearing (see §3) and is the
single substantive correction the referee required.

### 0.4 Resources and costs (native)

- Cooling free energy (matched across branches, per §0.3).
- Flux-threading energy (matched).
- **Maintenance cost of the stored circulating current** — the native resource
  quantity that DISTINGUISHES the branches:
  - In **N**: maintaining a circulating current `I` dissipates `I²R` continuously;
    holding it for time `t` costs energy `∝ I²R·t → ∞` as `t→∞`, and the current
    decays with time constant `L/R` (nanoseconds–microseconds).
  - In **S**: maintaining the persistent current costs **zero** ongoing energy
    (`R = 0`) and the lifetime is effectively infinite.

### 0.5 Records (native)

The **trapped fluxoid** is itself the record: an integer `n·Φ_0` circulating
supercurrent whose value is a stored datum, readable non-destructively by
`PROBE_READ`, transported without erosion, and erased only by heating through
`Tc` (an explicit erasure act). It is a record in the charter's sense: a token
`(proposition = "winding n", value = n, formation = the cooling-through-Tc act,
holder = the ring, erasure-cost = heat above Tc)`.

### 0.6 Access (native)

`PROBE_READ` projects the record to an observer without altering it (SQUID
readout is a weak, non-demolition measurement of the flux). Access is
symmetric across N and S — the metrology budget is identical — so no
access asymmetry is smuggled into the capability claim.

### 0.7 Observable response (native, and the discriminating signatures)

The native response to `THREAD(Φ_app)` then `PROBE_READ`, at fixed `T_f`:
- In **S**: the trapped fluxoid is the **nearest integer** to `Φ_app` (a
  quantized staircase), robust to the exact `Φ_app` within a fluxoid interval,
  to `DEFORM`, and to time. Three native discriminating signatures:
  - **(Q) quantization** — trapped value ∈ ℤ·`Φ_0`, a global winding invariant;
  - **(I) local-operation invariance** — `n` unchanged by `DEFORM` / gauge /
    any local latent-state change;
  - **(P) persistence** — `n` does not relax (macroscopic phase-slip barrier).
- In **N**: any circulating current equals whatever was driven (continuous, NOT
  quantized), is not invariant under the driving details, and decays in `L/R`.

---

## 1. The candidate capability-changing boundary event

> **Candidate.** Cooling the ring from N to S through `Tc` while flux is present
> (`COOL(T>Tc → T_f<Tc)` with `THREAD` active) is a **capability-enlarging
> boundary event**: at the matched final budget it makes realizable the task
>
> > **hold a quantized circulating memory indefinitely at zero maintenance
> > cost, robust to local perturbation** (a persistent-current / flux-qubit
> > backbone),
>
> which is **not realizable in the N frame at any budget**, because in N the
> same task demands unbounded maintenance energy (`I²R·t→∞`) and still decays.

Matched before/after descriptions (both at `T_f`, matched cooling+threading
budget, identical `PROBE_READ`):
- **before / null frame:** ring in N (or matched normal metal). Task set: drive
  a current, which decays; no quantized, no zero-cost-persistent memory.
- **after / candidate frame:** ring in S. Task set additionally contains the
  quantized zero-cost persistent memory task, with signatures (Q),(I),(P).

The enlargement is in the **resource profile of a task**, not merely in which
region of the phase diagram the system sits: the maintenance cost of the
holding task drops from strictly positive-and-divergent to exactly zero, and
the value stored acquires a topological quantization and a local-perturbation
invariance it provably lacks in N.

### 1.1 Construction fork (named, per Construction-Fork Discipline)

- **Construction chosen:** GL/London **macroscopic order-parameter** picture,
  with fluxoid quantization from single-valuedness of `ψ` and persistence from
  the macroscopic phase-slip barrier. Conclusions below are scoped to it.
- **Materially admissible alternates retained (not silently defaulted):**
  (a) the BCS **microscopic** picture (gap + Cooper-pair condensate) — same
  fluxoid quantization, derived from pairing rather than from a postulated
  `ψ`; (b) a **topological/TQFT** reading (winding number as a homotopy
  invariant of the phase map `S^1→U(1)`); (c) a purely **thermodynamic**
  reading (two coexisting phases across a second-order line, order parameter as
  a Landau field). The capability claim is stated so as to transfer across (a)
  and (b); the discriminator in §3 is where (c) — the thermodynamic /
  whole-family reading — becomes the candidate's most dangerous rival, so (c)
  is not merely retained but weaponized as the steelman rival.

---

## 2. The strongest ordinary-completion rival (steelman, full strength)

Built with the repo's declared completion-class machinery
(`tests/physical_completion_closure.py`: hidden-state, boundary, seed,
provenance, resource, whole-family, history, access, relabeling, gauge). Each
class is given its strongest finite form and asked to reproduce the candidate's
capability from the N frame at matched budget. The full steelman is the
**disjunction assembled at maximal strength**:

1. **resource:** "the capability is the cooling you paid for" (or "pump a
   current with a normalized budget"). — Countered by the matched-frame rule
   (§0.3): both branches paid the same cooling; a normal conductor cooled to
   `T_f` still cannot hold the current. And a pumped current in N — even if its
   VALUE happened to be integer — still fails signatures (I) and (P): it is not
   invariant under local ops and it decays in `L/R`. Resource is matched and
   value-integer-ness is not the sole defeater (referee R-D2), so this leg alone
   does not carry the capability.
2. **seed / boundary:** "the stored value is just the flux you threaded — a
   boundary datum copied in, exactly like the ferromagnet's fallen direction."
   — Real and partially conceded: **which** integer `n` is stored IS a seed set
   by `Φ_app` at cool-through (a genuine fiber, mirroring the founding-case
   Z/2). But the seed sets only the value, not the three signatures
   (Q),(I),(P): a seed/boundary copy yields a CONTINUOUS, non-invariant,
   decaying value.
3. **access:** "you only changed what you can read." — Countered: `PROBE_READ`
   budget is symmetric across N and S (§0.6); the difference is in the held
   datum's persistence and quantization, not in readout.
4. **history:** "the persistent current is a completed relaxation into a
   metastable well; given enough time it decays — a finite-lifetime history,
   not a settlement." — The **strongest single leg.** Persistence in S is
   finite in principle (phase slips are not literally forbidden); the candidate
   leans on "astronomically long" not "infinite." Honestly conceded as a
   grade-limiting caveat (§4).
5. **whole-family:** "N and S are two regions of ONE fixed phase diagram of the
   fixed Hamiltonian; the S capability was always a latent member of that fixed
   family, so reaching it is **disclosure within a fixed family**, not
   enlargement." — The **decisive leg**, and the charter's fixed-family
   absorber (Neutrality Rule null class 1; hierarchy falsifier F1). If the
   completion class is permitted to declare the S phase itself a member of the
   fixed family, it reproduces the candidate exactly (see §3, check `k2`).
6. hidden-state / provenance / relabeling / gauge: each is local and
   equivalence-only; none can manufacture (Q),(I),(P) from N (see §3, `k1`).

The steelman rival is therefore: **whole-family disclosure (leg 5) backed by
the seed reading of the stored value (leg 2) and the metastability reading of
persistence (leg 4)**, at matched resource (leg 1 neutralized as matched).

---

## 3. The discriminator (concrete, measurement-shaped, and executable)

Executable form: `tests/physical_witness_discriminator.py` (exit 0; `--strict`
lint clean; headline **7 [E] + 4 [F] = 11**, 2 [T]). It models the ring's
winding as an integer observable and scores each completion class on the three
signatures. Verbatim output is reproduced in `SYNTHESIS.md` §4.

**Physical (measurement-shaped) discriminator.** Sweep `Φ_app` across a fluxoid
interval at fixed `T_f` and `PROBE_READ` the trapped value:
- **D-Q (quantization).** Candidate predicts an **integer staircase** (trapped
  value jumps in units of `Φ_0`, flat between); every continuous completion
  (seed/boundary/access/resource) predicts a **straight line** (trapped =
  applied). *This is the Deaver–Fairbank / Doll–Näbauer experiment.* Observed
  physics: the staircase. Continuous completions are **falsified** by it.
- **D-I (local invariance).** `DEFORM` the ring smoothly and re-`PROBE_READ`.
  Candidate predicts `n` unchanged (homotopy invariant); a seed/boundary copy
  predicts the stored value tracks the deformation. Physics: `n` is unchanged.
- **D-P (persistence).** Measure the decay time. Candidate predicts a lifetime
  super-exponential in the barrier (effectively infinite); the metastability
  (history) leg predicts an ordinary `exp(−ΔF/kT)` decay. Physics: effectively
  infinite for macroscopic rings, but **finite in principle** — this is where
  the history leg is not fully killed (§4).

**The one completion that survives all three:** `whole_family_with_phase` —
declaring the S phase itself a member of the fixed family. The fixture exhibits
it executably: nine local completion classes (including whole-family
*restricted to N configurations*) FAIL at least one signature (`k1`), and
exactly one — whole-family *with the target phase declared in* — ABSORBS the
candidate (`k2`), while whole-family *without* it does not (`k2-fail`).

> **Discriminator verdict (scoped to this construction).** The candidate is
> **NOT reducible** to unpredictability, irreversibility, hidden state, changed
> resources (matched), changed access (symmetric), stochastic seed (sets the
> value, not the signatures), or a completed-history description **by any LOCAL
> completion class**. It survives nine of the ten declared completion classes on
> two independent measurable signatures (Q and I). Its survival is
> **conditional on refusing exactly one move**: admitting the target
> superconducting phase itself as a declared member of the fixed completion
> family. Under that admission the candidate is disclosure, not enlargement.

---

## 4. Honest grade and the live kill

- **Physics (§0):** literature grade. Established, non-toy, macroscopic.
- **Capability mapping (§1):** definitional draft — the identification of "zero
  maintenance cost + quantized + locally invariant persistent memory" with the
  hierarchy's Capability level under the matched-budget frame is repo-owned and
  provisional; it is exactly a v0.2 §2.5 frame-indexed capability claim, with
  the matched-budget frame as its declared normalization `N`.
- **Discriminator (§3):** the local-vs-quantized separation is toy-executable
  (fixture) AND backed by literature-grade real experiments (fluxoid
  quantization). The whole-family absorption is toy-executable and is the
  pre-declared kill vector.

**Two live kill vectors, stated out loud (Failure-Preservation Rule):**

1. **Whole-family absorption (fixed-family absorber, falsifier F1).** If the
   legitimate completion class is entitled to declare the S phase a member of a
   fixed phase diagram that "pre-contained" it, the candidate is disclosure. The
   candidate does NOT by itself defeat this; it converts the question into a
   sharp, adjudicable one: *is admitting the target phase into the fixed family
   a legitimate completion, or does it trivialize the Capability level (make
   every phase transition disclosure by fiat, emptying F1)?* That adjudication
   is a **capability question owned by Time as Finality** and a
   **completion-legitimacy question owned by Temporal Issuance**, reachable only
   by frozen sovereign return — NOT resolvable inside P2C. This is the honest
   frontier: the candidate is **UNKILLED by local completions but UNDISCHARGED
   against the whole-family completion**.
2. **Metastability (history leg).** Persistence is astronomically long, not
   provably infinite at finite ring size; the "zero-maintenance-cost forever"
   claim is a thermodynamic-limit idealization. At finite size it is
   "unmeasurably long," which the history leg can always relabel as an ordinary
   metastable well. This caps the persistence signature (P) at literature-grade
   "effectively infinite," not "provably infinite."

**Net honest disposition:** `SURVIVES_LOCAL_COMPLETIONS / UNDISCHARGED_VS_WHOLE_FAMILY`.
Neither a clean survival of a weak candidate (the candidate is genuinely strong
and beats nine classes on measurable signatures) nor a clean kill (it is not
reduced by any local class); the kill, if it comes, comes from the fixed-family
absorber, and that adjudication is cross-repo, not P2C-local. That is the
maximally informative outcome a REACH swing of this item can produce without a
sovereign return.

---

## 5. Nonclaims

- No claim that superconductivity "is" finality, issuance, or a GU/TI/TaF
  object; no source claim moves; `bar(b)`, H59, Krein positivity, physical
  issuance remain OPEN and untouched.
- No claim the candidate is validated as capability enlargement — it is
  explicitly UNDISCHARGED against the whole-family completion.
- The discriminator fixture is a finite instrument; its 11 evidential checks
  validate instrument behavior under stipulated witnesses, not real
  superconductors. The real-experiment backing for D-Q/D-I is cited at
  literature grade, not re-run here.
- No cross-repo action is taken. A future frozen-witness proposal to TaF/TI (to
  adjudicate the whole-family question) is noted as intended Track-belt
  follow-up, not drafted here (per this swing's scope).
