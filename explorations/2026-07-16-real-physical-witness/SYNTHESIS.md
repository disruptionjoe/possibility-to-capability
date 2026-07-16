---
artifact_type: exploration
status: complete
governance_role: real_physical_witness_swing
constitutional: false
created: 2026-07-16
workflow: BOUNDARY-TO-ISSUANCE-WITNESS / P2C-REAL-PHYSICAL-WITNESS
swing_type: REACH (portfolio reach_swing_cadence; failure is first-class)
construction: superconducting_ring_persistent_supercurrent
evidence_grade: literature_grade_physics + definitional_hierarchy_mapping + toy_executable_discriminator
verification: tests/physical_witness_discriminator.py (exit 0; --strict lint clean; 7 [E] + 4 [F] = 11)
---

# Real physical witness swing — superconducting ring

**Tier and guards.** Exploration. No source-repo claim, GU/TI/TaF verdict,
physical-issuance claim, finality claim, or cross-repository identity moves.
The attached `REFEREE-REPORT.md` GOVERNS grades and corrections. The frozen
system spec is `WITNESS-FREEZE.md`; read it for the full construction. This
file records the survey, the scoring, the pick, the alternates, and the run's
honest disposition.

**Selected item.** `P2C-REAL-PHYSICAL-WITNESS` (rank 1, the core wager's most
direct form), selected per the portfolio selection contract after the Rank-2
runway belt lane resolved and priority reverted to the core. This swing also
discharges the `reach_swing_cadence` obligation. Per Joe's binding frontier
constraint (direct chat, 2026-07-16): pick the STRONGEST real candidate
defensible as a genuine capability change, not a toy chosen to make the rival
comparison tractable; a well-documented kill of a strong candidate is valuable,
a survival of a weak candidate is worthless.

---

## 1. The survey (real shortlist, diverse physical domains)

Eight candidate physical systems were enumerated across distinct physical
domains, then scored against (a) the item's success condition (matched
before/after, fixed intervention menu + budget, native response, concrete
discriminator from the strongest completion rival) and (b) the item's kill
conditions = the ten declared completion classes already mapped in
`tests/physical_completion_closure.py` and
`explorations/2026-07-16-null-completion-closure/SYNTHESIS.md`
(hidden-state, boundary, seed, provenance, resource, whole-family, history,
access, relabeling, gauge), plus the relational-dissolution / fiber-closure
finding that an orientation datum reduces to a seed/relabel fiber.

Scoring axes (each 1–5): **cap-strength** (how defensible the capability claim
is to a skeptic), **local-completion resistance** (survives the nine LOCAL
classes?), **matched-budget cleanliness** (can before/after be built at matched
resource?), **discriminator sharpness** (is the discriminator quantized /
invariant / measurable, not rhetorical?), **founding-seam information** (does it
test the hierarchy where it is hardest / most novel?). "Kill exposure" names the
completion class most likely to reduce it.

| # | System (domain) | source theory | cap-strength | local-compl. resist | matched-budget | discriminator sharpness | founding-seam info | dominant kill exposure |
|---|---|---|---:|---:|---:|---:|---:|---|
| **1** | **Superconducting ring — quantized persistent supercurrent** (condensed matter, U(1) SSB + topology) | BCS / Ginzburg–Landau / fluxoid quantization | **5** | **5** | **4** | **5** | **4** | **whole-family (fixed phase diagram)** |
| 2 | Ferromagnet — spontaneous magnetization / broken ergodicity (condensed matter, Z2 SSB) | Ising / Landau mean-field | 4 | 3 | 3 | 3 | **5** | seed+history (direction is a fiber) |
| 3 | Topological order — protected qubit (toric code / topological SC, Majorana) | Kitaev / TQFT / BdG | 5 | **5** | 3 | 4 | 4 | whole-family + "toy-adjacent" (toric code) |
| 4 | Superfluid / BEC — dissipationless flow, quantized circulation (quantum fluids) | Gross–Pitaevskii / two-fluid | 4 | 4 | 3 | 4 | 3 | resource (cooling) + whole-family |
| 5 | Percolation / gelation — spanning-cluster load bearing (soft matter, geometric transition) | percolation theory | 3 | 2 | 2 | 3 | 2 | resource (added bonds) + history |
| 6 | Laser threshold — coherent emission (quantum optics, non-eq. phase transition) | Haken laser / rate eqns | 3 | 2 | 2 | 3 | 2 | resource (pump) |
| 7 | Catalysis — opening a reaction pathway (chemistry) | transition-state theory | 3 | 2 | 3 | 2 | 2 | access + resource (barrier) |
| 8 | Excitable medium / neuron firing — action-potential propagation (biophysics) | Hodgkin–Huxley | 2 | 2 | 2 | 2 | 2 | seed + completed-history (threshold bifurcation) |

### 1.1 Why #1 (recorded reasons)

The superconducting ring wins on the two axes Joe's constraint privileges —
**cap-strength** and **discriminator sharpness** — while also being the least
toy-adjacent (universally accepted, macroscopic, textbook physics):

- **The capability is a resource-profile change, not just a region move.** In
  the normal phase, holding a circulating-current memory costs `I²R·t → ∞` and
  decays in `L/R`; in the superconducting phase it costs **zero** ongoing energy
  and is effectively non-decaying. "Hold a circulating memory forever at zero
  maintenance cost" is a task genuinely absent in N **at any budget** — this
  survives the resource attack in a way a mere cooling/region move does not
  (a normal metal cooled to the same `T_f` still cannot do it).
- **The discriminating signatures are QUANTIZED and INVARIANT, not continuous.**
  Fluxoid quantization (`Φ_0 = h/2e`) gives an integer staircase — a global
  winding invariant no LOCAL completion (seed/boundary/access/resource, all
  continuous) can fake, and no gauge/relabel/hidden-state op can change. This is
  the sharpest measurable discriminator available among the eight, and it is a
  real experiment (Deaver–Fairbank, Doll–Näbauer 1961), not a rhetorical one.
- **It still lands on the founding seam.** The stored winding value is set by a
  seed (the threaded flux at cool-through) — a genuine fiber mirroring the
  founding-case Z/2 grading-sign fiber. The candidate deliberately separates the
  *value* (a conceded seed/fiber) from the *capability* (the quantized,
  invariant, persistent holding), and claims capability only for the latter.

### 1.2 Alternates preserved (named, not discarded)

- **Alternate A — Ferromagnet (broken ergodicity).** The tightest mirror of the
  founding-case Z/2 fiber; retained because a kill of #1 that turns on "the
  stored value is a seed" transfers directly to #2, and because #2 is the
  cleaner arena if the reach target becomes "existence-of-memory vs
  direction-of-memory." Weaker than #1 only in discriminator sharpness (its
  order parameter is continuous; no quantized invariant).
- **Alternate B — Topological order (protected qubit).** Equal cap-strength and
  local-completion resistance to #1 (topological protection is a theorem against
  local operations), and its discriminator (topological entanglement entropy
  `γ = log D`, a universal invariant zero in any trivial phase) is arguably even
  harder. Retained as the escalation target if #1's whole-family kill is
  adjudicated legitimate: `γ` is the natural next weapon. Ranked below #1 ONLY
  on Joe's "not toy-adjacent" constraint (its cleanest exactly-solvable form,
  the toric code, reads as a toy; the real-material forms — FQH, Kitaev
  materials, Majorana wires — are heavier to freeze at literature grade in one
  swing).
- **Alternate C — Superfluid / BEC quantized circulation.** Physically almost
  isomorphic to #1 (quantized circulation `κ = h/m`, persistent flow) in a
  different domain; retained as the independent-domain replication of #1's
  discriminator, valuable precisely because a shared kill across #1 and #4 would
  indicate the kill is about the whole-family absorber, not about
  superconductivity specifically.

The lower four (#5–#8) are preserved as scored-and-set-aside: each is dominated
on cap-strength or discriminator sharpness and each has a cheaper dominant kill
(resource or completed-history) that a skeptic wins early.

---

## 2. The witness (summary; full freeze in WITNESS-FREEZE.md)

- **System:** thin superconducting ring, threaded by flux, cooled through `Tc`.
- **Candidate boundary event:** cooling N→S with flux present makes realizable
  "hold a quantized circulating memory indefinitely at zero maintenance cost,
  robust to local perturbation," a task not realizable in N at any budget.
- **Matched frame:** both branches compared at fixed final `T_f < Tc` and
  matched cooling+threading budget; cooling is a MATCHED resource, neutralizing
  the resource leg. This frame is a **budget-matched counterfactual pair** (ring
  in S vs. a reference normal conductor at the same `T_f` and budget), NOT a
  literal single-system before/after (which would sit at two temperatures and be
  unmatched); the capability claim is frame-indexed to it per Hierarchy v0.2
  §2.5 (referee correction R-D1, applied).
- **Strongest completion rival (steelman):** whole-family disclosure ("N and S
  are two regions of one fixed phase diagram; the S capability was a latent
  member of a fixed family") backed by the seed reading of the stored value and
  the metastability reading of persistence, at matched resource.
- **Discriminator:** the quantized fluxoid staircase (D-Q), local-deformation
  invariance of the winding (D-I), and persistence (D-P) — the first two
  measurable and real (fluxoid-quantization experiments), separating the
  candidate from every LOCAL completion; the whole-family completion survives
  D-Q/D-I only by declaring the target phase itself a family member.

---

## 3. Construction-fork discipline

The chosen construction is the **GL/London macroscopic order-parameter**
picture. Materially admissible alternates retained and scoped: BCS microscopic
(same fluxoid quantization from pairing), topological/TQFT (winding as homotopy
invariant), and thermodynamic (two phases across a Landau line). The capability
claim is stated to transfer across BCS and TQFT; the thermodynamic reading is
where the whole-family rival lives and is weaponized as the steelman, not
silently defaulted. Every conclusion below is scoped to the GL/London
construction unless transfer is stated.

---

## 4. Executable discriminator — verbatim output

`tests/physical_witness_discriminator.py` (exit 0; `tef_check_tag_linter.py
--strict` clean; registry mode; headline **7 [E] + 4 [F] = 11**, 2 [T]):

```text
PHYSICAL WITNESS DISCRIMINATOR (superconducting ring)
========================================================================
PASS  [T] s1: winding is an integer by construction: True
PASS  [T] s2: a global gauge shift preserves winding by construction: True
PASS  [E] q1: candidate trapped value is integer-quantized across a field interval: True
PASS  [F] q1-fail: a continuous-boundary completion is NOT integer-quantized: False
PASS  [E] q2: seed/access/boundary completions store a NON-integer value: True
PASS  [E] i1: candidate winding is invariant under every LOCAL completion op: True
PASS  [F] i1-fail: a metastable rival value CHANGES under the same local ops: False
PASS  [E] p1: candidate winding does not relax; history completion decays to zero: True
PASS  [E] k1: nine local completion classes fail at least one discriminating signature: True
PASS  [E] k2: the whole-family-with-target-phase completion ABSORBS the candidate: True
PASS  [F] k2-fail: whole-family WITHOUT the target phase does NOT absorb it: False
PASS  [E] n1: swapping the two branch labels leaves every discriminator verdict fixed: True
PASS  [F] n1-fail: a label-sensitive scorer WOULD flip under the swap: False

candidate staircase (applied -> trapped winding):
  applied=  1/4  ->  w=0   (seed rival stores 1/4, decays)
  applied=  2/5  ->  w=0   (seed rival stores 2/5, decays)
  applied=  3/5  ->  w=1   (seed rival stores 3/5, decays)
  applied=  4/5  ->  w=1   (seed rival stores 4/5, decays)
  applied=11/10  ->  w=1   (seed rival stores 11/10, decays)
  applied=  7/5  ->  w=1   (seed rival stores 7/5, decays)

completion-class scoreboard vs candidate (a=3/5):
                       gauge: value=    0 Q=1 I=1 P=0  -> fails
                  relabeling: value=    0 Q=1 I=1 P=0  -> fails
                hidden_state: value=    0 Q=1 I=1 P=0  -> fails
                    boundary: value=  3/5 Q=0 I=0 P=0  -> fails
                        seed: value=  3/5 Q=0 I=0 P=0  -> fails
                      access: value=  3/5 Q=0 I=0 P=0  -> fails
                    resource: value=  3/5 Q=0 I=0 P=0  -> fails
                     history: value=    0 Q=1 I=1 P=0  -> fails
                  provenance: value=    0 Q=1 I=1 P=0  -> fails
       whole_family_no_phase: value=    0 Q=1 I=1 P=0  -> fails
     whole_family_with_phase: value=    1 Q=1 I=1 P=1  -> ABSORBS

EVIDENTIAL CHECKS (headline): 7 [E] + 4 [F] = 11
[T] theorem-consequence checks (no evidential weight): 2
All checks match expectations. Exit 0.
```

Reading: on the fractional field interval, the candidate stores an integer
staircase (0,0,1,1,1,1) while every continuous completion stores the raw
fractional value and decays. Nine LOCAL completion classes fail at least one of
the (Q,I,P) signatures; exactly one class — whole-family with the target phase
declared in — absorbs the candidate. `k2-fail` confirms whole-family restricted
to normal-phase members does NOT absorb it, so the absorption is caused
specifically by admitting the target phase, not by whole-family completion per
se. `n1`/`n1-fail` confirm the discriminator verdict is label-invariant.

---

## 5. Honest disposition and the live kill

**Disposition: `SURVIVES_LOCAL_COMPLETIONS / UNDISCHARGED_VS_WHOLE_FAMILY`.**

- The candidate is a **strong**, non-toy, literature-grade capability claim that
  is **not reduced** by unpredictability, irreversibility, hidden state, changed
  resources (matched), changed access (symmetric), stochastic seed (sets value,
  not signatures), or completed-history **by any LOCAL completion class**, on
  two independent measurable signatures (quantization and local invariance).
- It is **UNDISCHARGED**, not victorious: its survival is conditional on
  refusing exactly one completion — admitting the superconducting phase itself
  as a member of a fixed phase diagram. That is the charter's **fixed-family
  absorber** (Neutrality Rule null class 1; hierarchy falsifier **F1**). Whether
  that refusal is legitimate — or whether admitting any physically realized
  phase into the fixed family is always allowed, which would EMPTY the
  Capability level and confirm F1 — is a **capability question owned by Time as
  Finality** and a **completion-legitimacy question owned by Temporal
  Issuance**, resolvable only through a frozen sovereign return, NOT inside P2C.
- Second live caveat: persistence (P) is "effectively infinite" at literature
  grade, not "provably infinite" at finite ring size, so the history leg is
  capped but not fully killed (metastability reading survives at finite size).

**Why this is the correct REACH-swing result, not a hedge.** The swing did not
de-risk the selection to guarantee a clean run: it picked the strongest
candidate, built the rival at full strength, and found the exact seam where the
candidate either lives or dies. That seam is a **sharp, pre-declared,
executably-exhibited fixed-family question**, handed to the right owners rather
than resolved by fiat. This both instantiates the hard core (diagnosing
capability-vs-disclosure on a real physical case) and sharpens F1 into a
concrete cross-repo adjudication target. A weaker candidate would have died to a
cheap resource/history leg and taught nothing.

---

## 6. Next-work handoff (reranked after this swing)

Durable priority owner remains `steward/research-portfolio.json`; this is a
reranking signal, not a replacement queue.

| rank | item | why now | gate |
|---:|---|---|---|
| 1 | `P2C-BOUNDARY-ADAPTER` (rank 2 → lead) | The real witness has now disciplined the definitions, exactly as the 2026-07-16 rerank intended; the adapter should be built to consume THIS witness's (Q,I,P)-signature vector and matched-budget frame, and to expose the whole-family admission as its testable residual. | must not carry the capability verdict as input; test the whole-family admission as a residual, not a label |
| 2 | `P2C-REAL-PHYSICAL-WITNESS` (continue) | Escalate to Alternate B's `γ = log D` discriminator (topological entanglement entropy) or Alternate C (BEC quantized circulation) as an independent-domain replication, IF a second swing is spent here before a sovereign return. | keep literature-grade citation discipline; do not import TQFT truth |
| 3 | `P2C-NULL-COMPLETION-CLOSURE` (continue) | The swing exposes a needed sharpening: the completion closure must make the "admit the target phase into the fixed family" move an EXPLICIT, auditable completion candidate with its own admissibility rule, so F1 can be tested rather than assumed. | the closure must not be able to admit an arbitrary target phase for free |
| 4 | `P2C-CROSS-REPO-ADJUDICATION` (gated) | Now has a concrete frozen witness whose single open question (whole-family admission) is precisely a TaF-capability + TI-completion adjudication. Intended mailbox proposals noted below; drafting them is Track-belt follow-up, not this swing. | activation still requires frozen sovereign returns for the SAME construction |

**Intended cross-repo returns (noted only; NOT drafted this swing, per scope):**
- To **Time as Finality:** freeze this witness and ask whether "hold a quantized
  zero-cost persistent memory" is an invariant capability enlargement or a
  fixed-family disclosure — no desired verdict included.
- To **Temporal Issuance:** freeze this witness and ask whether admitting a
  realized phase into the fixed completion family is a legitimate whole-family
  completion — no source-issuance asserted.

No cross-repo action is taken by this swing. No source claim moves. `bar(b)`,
H59, Krein positivity, physical issuance remain OPEN.
