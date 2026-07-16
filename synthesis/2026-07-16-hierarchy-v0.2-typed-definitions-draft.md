---
artifact_type: provisional_synthesis
status: adopted_typed_hierarchy_draft_below_ratified_synthesis
created: 2026-07-16
adopted: 2026-07-16
adoption_provenance: >
  Joe reviewed and adopted this document as the repo's typed hierarchy draft
  on 2026-07-16 in direct chat (the trusted control channel), choosing option
  A: full adoption with ALL adversarial-referee corrections D1-D7 applied.
  This remains below ratified-synthesis standing. It is not canon. No verdicts
  move.
workflow: north-star-lane-item-2
construction: typed_partial_diagnostic_process_level
evidence_grade: definitional_draft_plus_deterministic_toy_skeleton
predecessor: synthesis/2026-07-14-coherent-story-v0.1.md
source_draft: >
  explorations/2026-07-16-northstar-unblock/lane-D-hierarchy-v02-draft.md
  (verdict SOUND-WITH-CORRECTIONS; the attached adversarial referee report
  GOVERNS grades and corrections; defects D1-D7 are applied in this copy)
verification: tests/hierarchy_v02_typed_skeleton.py (committed; exit 0, --strict lint clean, headline 8 [E] + 4 [F] = 12)
constitutional: false
---

# Hierarchy v0.2 — typed level and transition definitions (adopted draft)

**Status and guards.** Joe reviewed and adopted this document on 2026-07-16 (direct chat, trusted
control channel; option A — full adoption with the referee's corrections D1–D7 applied). It remains
below ratified-synthesis standing: not canon, no receiver verdicts, no source-claim movement. It is
the typed successor of the v0.1 plain-English candidate (`synthesis/2026-07-14-coherent-story-v0.1.md`)
and keeps v0.1's central posture: the six levels are **diagnostic types, not a chronology**. It
INSTANTIATES the charter's guiding hypothesis; it does not modify it. It issues **no receiver
verdicts**, moves **no source-repo claim** (`bar(b)`, H59, Krein positivity, physical issuance stay
OPEN), and does not claim v0.2 is validated — validation is exactly what the ranked decisive-test
program exists for (`experiments/2026-07-14-ranked-decisive-test-program-v0.1.md`; referee-corrected
receiver updates in `explorations/2026-07-16-decisive-tests/SYNTHESIS.md` govern). The
north-star/byproduct firewall stands unchanged: the repo's purpose remains the charter hypothesis; the
Bounded Fiber Theorem is a byproduct spine whose findings feed the finality level as INPUT, never as
the purpose (`explorations/2026-07-16-progress-lanes.md`).

**What changed from v0.1 to v0.2.** v0.1 gave the six types in plain English with epistemic
separation. v0.2 (a) types each level as a class of structure over a base PROCESS object, per design
requirement I-6 (static-sheaf amputation: state snapshots are defined by forgetting the issuance
process the datum rides on; register row I-6, `explorations/INTERPRETATIONS-REGISTER.md`); (b) gives
the finality level its proper internal machinery (switch profiles, operator opacity, SSB vocabulary —
register rows I-1..I-5, I-7); (c) makes the definitions executable at toy grade with [T]/[E]/[F]
discipline; (d) states per-level falsifiers feeding the program's `REVISE_HIERARCHY` outcome.

**Referee corrections applied in this copy (D1–D7).** D1: d1c retagged [T]; the null-intervention
criterion is a forced-frame flag, not a structural-circularity detector (§2.5). D2: fixture 4a's RUN
status corrected in §3, §5 (F6), and §8. D3: §2.6's susceptibility bullet corrected to
candidate-shape wording. D4: d3c retagged [T]; honest evidential headline **8 [E] + 4 [F] = 12**.
D5: d3d quantifies over decoders. D6: honesty note extended — the printed worked finality diagnosis
is stipulated vocabulary in all four fields. D7: E160 citation path fixed; d1d's "non-circular"
wording fixed (check kept).

---

## 1. The base object: a process object, not a state space

All six levels are typed over one base object. Per I-6 this base is process-level:

> **Definition (process object, draft).** A process object `P` is a finite category-like structure:
> objects are prefix/contexts (source states appear ONLY as sources and targets of morphisms);
> morphisms are **issuance acts** `e : S -> S'`; composition is path concatenation where defined; and
> morphisms may carry **labels** in a declared monoid `M`, subject to the composition-compatibility
> law `L(g∘f) = L(g)·L(f)`.

Formal anchors (both TI-owned; cited, not absorbed):

- **E160 (composition-compatible morphism labels)**
  (`temporal-issuance/explorations/E160-holonomy-transport-functor-derivation-fixture-2026-07-10.md`,
  a bounded toy fixture with `claim_movement: false`; cited at that grade — referee correction D7):
  nontrivial transport exists only when admissibility itself carries a composition-compatible label
  rule ON MORPHISMS; a label table supplied from outside is not a derivation, and inconsistent labels
  define no functor. v0.2 adopts this as the type of every level-datum that "rides" the process.
- **RUN-0025 (thin-shadow warning)** (`temporal-issuance/FORMAL-OBJECT.md`): the induced state-order
  `S <= S'` iff `Hom(S,S')` nonempty is only the thin reflection; morphism-level invariants can
  differ while the induced order is identical. Therefore **no v0.2 level datum may be defined as a
  function of the thin shadow** — that is precisely the static-sheaf amputation I-6 bans.
  (Executable demonstration: diagnosis 2 below.)

Grade of everything in §§1–3: **definitional draft**, backed only by the deterministic toy skeleton
in §4. Nothing here is a validated physical typology.

## 2. The six levels, typed

Each level is given by four fields: **DATA** (what the level's datum IS, as structure over `P`),
**PRESERVED BY** (which transformations preserve it), **CHARACTERISTIC FAILURE / ABSORBER** (how the
level classically collapses or gets absorbed), and **DIAGNOSTIC QUESTION** (what it answers).
Transitions between levels are the typed comparisons named inside each definition; v0.1's rule stands:
a case need not visit every type, types may be co-located, and `HIERARCHY_REVISION` is a first-class
outcome.

### 2.1 Possibility

- **DATA.** An admissibility structure over candidate morphisms: for each prefix object `S`, the
  class `CandExt(S)` of candidate issuance morphisms and the admissibility predicate `Adm_S` with its
  witnesses, both FORMED AT the prefix (the `OnlineIssuance^LC` shape, cited at TI's own grade —
  class-relative formal residue, not physical issuance). The datum is the admissible-morphism class,
  not a set of admissible states: "what is possible" = "which issuance acts are admissible from
  here," which a state snapshot cannot carry (I-6).
- **PRESERVED BY.** Admissibility-respecting maps of process objects: functor-like maps sending
  admissible morphisms to admissible morphisms and preserving witness structure (not merely
  preserving the induced reachable-state set).
- **CHARACTERISTIC FAILURE / ABSORBER.** The **fixed-family absorber**: a fixed completed family that
  precontains all admissible extensions, making every later "new possibility" a disclosure inside a
  static family. This is the hierarchy's null class 1 (charter Neutrality Rule item 1) and TI's
  fixed-table/fixed-oracle absorber class.
- **DIAGNOSTIC QUESTION.** *What could be issued from here — and is the admissible class itself
  prefix-formed, or precontained by a fixed family?*

### 2.2 Dynamics

- **DATA.** The composition structure of `P` itself: which admissible morphisms compose into
  realizable paths, together with the composition-compatible labels those paths carry. Crucially the
  datum is the **morphism-level path structure**, NOT the induced reachability preorder — RUN-0025
  proves those can differ while the order is identical, and diagnosis 2 makes that executable.
- **PRESERVED BY.** Label-respecting functors: maps preserving composition, identities where present,
  and path labels up to declared isomorphism of the label monoid.
- **CHARACTERISTIC FAILURE / ABSORBER.** The **thin shadow**: replacing dynamics by its induced
  state-order. If a case's every dynamical distinction is recoverable from the thin shadow, the
  process-level typing has bought nothing there (see falsifier F2).
- **DIAGNOSTIC QUESTION.** *How does issuance move within the admitted family — and does the movement
  carry morphism-level structure beyond mere reachability?*

### 2.3 Records

- **DATA.** Traces riding on morphisms: a record is a token `(proposition, value, formation-morphism,
  holder, erasure-cost)` attached to an issuance act and transported along subsequent composition
  until an explicit erasure morphism removes it. Process-level restatement of TaF's record token
  (TaF `FORMALISM.md`, cited at TaF's grade): the formation EVENT is a morphism, persistence is
  functorial transport, and erasure is itself an act — a record is never a bare state fact. TaF's D1
  profile `(A, R, B, C)` is the richest existing model of this level's local datum and is adopted as
  the level's reference structure at TaF-owned grade (componentwise preorder, no scalar collapse).
- **PRESERVED BY.** Trace-preserving maps: process maps carrying formation morphisms to formation
  morphisms, holders to holders injectively on accessible holders, and not decreasing the declared
  erasure-cost model (TaF T18's admissibility shape, cited).
- **CHARACTERISTIC FAILURE / ABSORBER.** Two classical conflations, both already dissociated at
  synthetic grade in this repo's swing suite: (i) **irreversibility ⇒ record** (irreversible dynamics
  with no inspectable trace), and (ii) **record ⇒ access** (a persisting trace nobody can inspect).
  Plus the thin-shadow special case: "records" reconstructed purely from the induced order (content
  vs form — register row I-10's live question).
- **DIAGNOSTIC QUESTION.** *Which distinctions made by issuance persist as inspectable traces — and
  is their persistence carried by morphism-level transport or merely asserted of states?*

### 2.4 Access

- **DATA.** An observer-indexed inspection structure on traces: for each observer position `o` (an
  object-with-morphisms of `P`, not a bare point), the projection `Proj_o` giving which traces can
  condition `o`'s further issuance — TaF's causal availability (formation causally prior + holder in
  the bounded access set) restated so that both relata are morphism-anchored; TI's readout-side
  residue (`Proj`, `kappa`, `Glue` are readout machinery per RUN-0019, cited). Access morphisms are
  the acts that change `Proj_o` without touching the trace set.
- **PRESERVED BY.** Access-equivariant maps: process maps commuting with the projections
  (`Proj` before = `Proj` after, up to the map).
- **CHARACTERISTIC FAILURE / ABSORBER.** **Access–capability conflation**, in both directions:
  counting a visibility/reachability change as enlargement, or normalizing away a relation that is
  constitutive. This is Rank 2's whole battleground and stays a live fork (Rank 2 is BLOCKED at the
  source-packet prerequisite; the pilot earned no directional pressure — referee-corrected).
- **DIAGNOSTIC QUESTION.** *Which persisting traces can condition which observers' further issuance —
  and did an intervention change only this relation?*

### 2.5 Capability

- **DATA.** A **frame-indexed** normalized task structure: given a DECLARED normalization frame `N`
  (task vocabulary; which of description/representation/resource/access/control factors are held
  fixed and at what baseline), the datum is the class of task-realizing issuance compositions
  available to an agent position, quotiented by `N`. **The frame is a parameter of the type, not a
  derived fact.** This is deliberate: Rank 2's construction fork lives here by design, and v0.2
  refuses to hide it — a capability diagnosis without its frame attached is ill-typed. The skeleton's
  check `d1d` exhibits the fork executably: the same intervention classifies differently under two
  distinct declared frames (each passes the forced-frame flag, which does not certify structural
  non-circularity — see absorber (i) and referee D1/D7).
- **PRESERVED BY.** `N`-frame-respecting equivalences: maps preserving the task vocabulary and the
  held-fixed factors at their declared baselines. Cross-frame comparisons are typed as comparisons of
  PAIRS (diagnosis, frame), never as frame-free facts.
- **CHARACTERISTIC FAILURE / ABSORBER.** (i) **Frame circularity** — the frame entails the verdict.
  Frame circularity is detectable by the null-intervention criterion only for frames that misclassify
  the identity intervention; in this skeleton the only such frames are explicitly forced ones —
  structural circularity (e.g. post-hoc task vocabulary) is NOT detected at this grade, and building
  a detector with bite over structurally circular frames is open work (referee correction D1);
  (ii) **access-constitutive collapse** — all admissible frames agree only after access is made
  constitutive (Rank 2's `FAVORS_RIVAL` branch); (iii) **relativist scatter** — equally admissible
  frames disagree with no invariant quotient.
- **DIAGNOSTIC QUESTION.** *Under the declared frame, did the normalized realizable task set enlarge
  or restrict — or did only visibility, reachability, or control change?*

### 2.6 Finality — the diagnosis of last resort, typed

Kept from v0.1: finality enters only as a **candidate** diagnosis when a real settlement cannot,
under a named search scope and retained constructions, be factored through the five preceding levels
and is not reopened by an admissible continuation. `FINALITY_CANDIDATE` is weaker than finality;
Located-Is-Not-Forced governs. v0.2 adds the level's internal typed structure, from register rows
I-1..I-5 and I-7 (`explorations/INTERPRETATIONS-REGISTER.md`,
`explorations/2026-07-16-boundary-switch-interpretation.md`):

- **DATA.** A **settlement**: a datum `d` riding the process as a composition-compatible flip-odd
  morphism label (the E160 port shape — injected at issuance acts, not derived from contents),
  together with its **switch profile**:

  ```text
  switch_profile(d) = (multiplicity, re-makeability)

  multiplicity   ∈ {per-slice/per-block, global}
  re-makeability ∈ {re-made, set-once}
  ```

  The operator taxonomy (register I-2..I-4) maps onto profiles, not into the datum: A-ongoing =
  (per-slice, re-made); A′ per-sheaf once-bit = (per-slice, set-once); B-live = (global, possibly
  re-made; timing/consequence side-channels only); B-fired-and-forgot and C = (global, set-once;
  behind the opacity horizon).

- **OPERATOR OPACITY (theorem-shaped bound on what the level can ever attribute).** Stated as the
  level's ceiling, at its current grade (derived 2026-07-16, register I-5: candidate mini-theorem,
  toy-executable below, NOT yet a proven theorem over any native formalism):

  > *Opacity bound (draft, toy grade).* The interior of a process object can discriminate a
  > settlement's **switch profile** — multiplicity (a single global choice is invisible because
  > flip-invariant observables see only relative alignments; multiple per-block choices produce
  > observable block-relative alignments) and re-makeability (re-made choices appear as changeable
  > relative alignments; set-once bits do not) — but **never the operator identity**: operator
  > assignments with matched switch profiles are interior-equivalent. Consequently the finality
  > level's diagnosis type is `(instability, susceptibility, lock-in, switch_profile)` and contains
  > no operator field, by construction.

  This is what makes B-type (external operator) an admissible assignment with a provable epistemic
  horizon rather than a metaphysical indulgence, and it is why the level is a diagnosis of last
  resort: even a confirmed settlement licenses profile attribution only.

- **INTERNAL VOCABULARY (the SSB split, register I-7).** Every finality diagnosis decomposes into
  three separately-establishable components — derive instability and susceptibility, never direction:
  - **instability**: the structure admits multiple settlements (the fork exists — for the founding
    case, the ℤ/2 fiber at every tier modeled);
  - **susceptibility**: WHICH injections the structure responds to (the port type — for the founding
    case, a flip-symmetry-breaking primitive (corpus link 8); the composition-compatible flip-odd
    morphism label is v0.2's typed CANDIDATE for its shape (E160 port reading; fixture 4b untested;
    non-compatible injections define nothing, E160 case-5)) — referee correction D3;
  - **lock-in**: whether a settled datum is transported without re-derivation (for the founding case,
    σ-equivariant transport without insertion at toy-family grade).
- **PRESERVED BY.** Flip-equivariant maps of labeled process objects; the settlement datum is
  preserved as an ORBIT, never as a member (the transport results forbid more).
- **CHARACTERISTIC FAILURE / ABSORBER.** (i) A defensible **factorization** through an earlier level
  (enlarged dynamics, boundary conditions, records, access, normalized capability) — Rank 3's
  tournament legs; (ii) **assumed settlement** — the finality criterion presupposing the settlement
  it purports to establish (Rank 3's trap check); (iii) **irreversibility-as-settlement** (banned by
  Rank 3's stop conditions).
- **DIAGNOSTIC QUESTION.** *Does anything remain after every preceding level has had its strongest
  hearing — and if so, what is its switch profile, and nothing more?*

## 3. The first worked finality diagnosis: the fiber corpus, at its corrected grade

The Bounded Fiber Theorem corpus (`synthesis/2026-07-16-bounded-fiber-theorem-v1.0.md`, refereed
pre-commit) is the hierarchy's first worked finality-level diagnosis. Cited AT its referee-corrected
grades, never above:

| SSB component | Finding | Grade (as refereed) |
|---|---|---|
| instability | the sign datum is a ℤ/2 fiber (per-block: (ℤ/2)^blocks under partitioned transport) undetermined at every tier modeled | toy-family exhaustive + shipped-code (T26 surface) + class-relative stipulated-vocabulary proof |
| susceptibility | deriving the orientation requires a flip-symmetry-breaking primitive, whose addition IS positing the datum; physics-side name: sector-asymmetric spectral condition (energy positivity) | class-relative toy-grade no-go (link 8) + REDUCED-toy relocation (link 11) |
| lock-in | the fiber is σ-equivariantly transported without insertion; the arrow is an independent ℤ/2 and cannot substitute | exhaustive-finite toys (links 4, 5, 10) |
| switch profile | multiplicity leg RUN at exhaustive-finite-toy grade (4a, `ENDPOINT_POSITIVE_TOY`, provisional synthesis `explorations/2026-07-16-per-block-observability/SYNTHESIS.md`; cited at its own grade — no adversarial referee report attached to that run); re-makeability leg (4b) untested; profile as a whole OPEN | 4a: exhaustive-finite toy with three failing-direction controls; 4b: untested (referee correction D2) |
| finality VERDICT | **REMAINS_UNDERDETERMINED** — under Rank 3's own discipline the corpus fires "no factor found but search coverage is weak," because coverage-weakness is judged against preregistration/independence/blinding the corpus permanently lacks; a stronger outcome needs a new §5-compliant campaign | referee-corrected receiver update, decisive-tests SYNTHESIS row 3 (which GOVERNS) |

So the worked example demonstrates the level operating exactly as typed: instability, susceptibility,
and lock-in each established at named grades; the switch profile's multiplicity leg run at toy grade
with the re-makeability leg pending; the finality verdict itself withheld — a diagnosis of last
resort that has NOT yet been earned, said out loud. `bar(b)` stays OPEN. Rank 3 stays BLOCKED.
Nothing here upgrades the corpus into a tournament pass.

## 4. Executable skeleton

Deterministic pure-Python toy: the base process object, level-typed data, and three diagnoses run
end-to-end — (1) access-change vs capability-enlargement under a declared frame, with a
null-intervention forced-frame flag (structural circularity is NOT detected at this grade; a
detector with bite is open work — referee D1) and the Rank-2 fork exhibited; (2) I-6 made executable
(identical thin shadows, distinct morphism-level datum); (3) the finality level's switch-profile
machinery (multiplicity and re-makeability interior-testable at 2-block toy scale — d3a re-derives,
and cites as prior art, the already-run Lane 1 fixture 4a
(`explorations/2026-07-16-per-block-observability/SYNTHESIS.md`, closed `ENDPOINT_POSITIVE_TOY`);
operator opacity checked; non-derivability of the absolute bit quantified over decoders; E160
composition-compatibility with its case-5 failing direction).

Honesty notes: check `d3d` is an exhaustive computation over 16 selectors × 4 decoders (referee
correction D5) — a mini-theorem check tagged [E] because its outcome was not fixed at formalization
time, but it carries toy weight only. Per referee correction D6: **all four fields of the printed
worked finality diagnosis (`instability`, `susceptibility`, `lock_in`, `switch_profile`) are
stipulated vocabulary at this grade** — `diagnose_finality` is a passthrough; the interior-testability
evidence lives in checks d3a/d3b, not in `diagnose_finality`. The `CAPABILITY_CHANGE` (restriction)
branch of `classify_intervention` is exercised by no check (noted, open — referee D7). Nothing in
this skeleton touches real physical content.

Repo path: `tests/hierarchy_v02_typed_skeleton.py` (the committed file is the corrected source;
its docstring records corrections D1/D4/D5/D7).

### 4.1 Output (verbatim, 2026-07-16, corrected file, exit 0)

```text
HIERARCHY v0.2 TYPED SKELETON -- toy diagnoses
==========================================================================
PASS  [T] setup1: generator-extended labels are composition-compatible by construction: True
PASS  [T] setup2: finality diagnosis emits switch-profile fields only (no operator key): True
PASS  [E] d1a: access-only intervention classifies ACCESS_CHANGE under the declared frame: True
PASS  [E] d1b: admissibility-enlarging intervention classifies CAPABILITY_ENLARGEMENT: True
PASS  [T] d1c: declared frames pass the null-intervention forced-frame flag: True
PASS  [F] d1c-fail: answer-entailing frame IS flagged by the same forced-frame flag: False
PASS  [E] d1d: same intervention classifies differently under a distinct declared frame: True
PASS  [E] d2a: thin shadows identical while the morphism-level invariant differs (I-6): True
PASS  [F] d2a-fail: label-degenerate twin does NOT differ under the same invariant: False
PASS  [E] d3a: per-block injection is choice-visible; global injection is choice-invisible: True
PASS  [F] d3a-fail: single-block model yields NO choice-sensitive flip-invariant observable: False
PASS  [E] d3b: re-made per-block bits give stage-varying alignments; once-bits give fixed: True
PASS  [T] d3c: matched-profile operators (B-fired vs C) give identical interior observables: True
PASS  [E] d3d: no flip-invariant selector on the 2-block label space determines the absolute bit: True
PASS  [E] d3e: compatible morphism-label injection is accepted by the composition checker: True
PASS  [F] d3e-fail: non-composition-compatible injection REJECTED by the same checker: False

EVIDENTIAL CHECKS (headline): 8 [E] + 4 [F] = 12
[T] theorem-consequence checks (no evidential weight): 4

Worked finality diagnosis (toy; SSB vocabulary + switch profile;
all four fields are stipulated vocabulary at this grade -- referee D6):
  {'instability': True, 'susceptibility': 'composition-compatible flip-odd morphism label', 'lock_in': True, 'switch_profile': {'multiplicity': 'per-block', 're_made': False}}
All checks match expectations. Exit 0.
```

### 4.2 Lint (verbatim, `tef_check_tag_linter.py --strict`, exit 0)

```json
{
  "path": "tests\\hierarchy_v02_typed_skeleton.py",
  "convention": "registry",
  "total_checks": 16,
  "tag_counts": { "T": 4, "E": 8, "F": 4 },
  "untagged_count": 0,
  "evidential_count_E_plus_F": 12,
  "T_checks_excluded_from_headline": 4,
  "violations": [],
  "advisories": []
}
```

## 5. Falsifiers

Each falsifier names evidence that would show the corresponding type is **missing, collapsed, or
construction-dependent**, feeding the program's `REVISE_HIERARCHY` receiver update (update vocabulary
and stop conditions of the ranked program are binding). These are receiver-side revision triggers, not
source claims.

- **F1 — possibility.** In real packets, the admissible class can always be re-presented as a fixed
  completed family with changing access (the fixed-family absorber wins everywhere): possibility
  collapses into access; the disclosure/enlargement distinction loses its first leg.
- **F2 — dynamics (and I-6 itself).** Morphism-level data never adds diagnostic power over the
  induced state-order in any real case — every diagnosis is recoverable from the thin shadow. Then
  the process-level typing is decoration and v0.2's central design requirement is falsified
  independently of the six types (this is v0.2's own added stake; see program falsifier).
- **F3 — records.** Record persistence proves coextensive with irreversibility or with access in all
  real cases (never dissociates outside synthetic controls): records is not a distinct type.
- **F4 — access.** No normalization frame can hold access fixed without circularity — all admissible
  frames agree only after access is made constitutive (Rank 2's `FAVORS_RIVAL` branch): the
  access/capability boundary collapses and the hierarchy's load-bearing novel discrimination dies.
- **F5 — capability.** Equally admissible declared frames yield divergent diagnoses with no invariant
  quotient across real cases (operational-context relativism / persistent `CONSTRUCTION_FORK`): the
  level is construction-dependent, and diagnoses must be permanently frame-indexed pairs or the type
  withdrawn.
- **F6 — finality.** Either (i) every real settlement factors through an earlier level under
  adequately covered, preregistered, independent search (Rank 3's defensible-factor branch): the
  level is empty as a diagnosis; or (ii) the switch profile itself proves not interior-testable
  (e.g., fixture 4a's multiplicity result — already RUN and positive at exhaustive-finite-toy grade
  (`ENDPOINT_POSITIVE_TOY`) — fails replication or scale-up, the re-makeability fixture 4b fails its
  [E] legs, or re-makeability cannot be stated without smuggling a time label): the level's internal
  vocabulary collapses and finality reverts to v0.1's untyped last-resort placeholder. (Wording
  adjusted for 4a's run status — referee correction D2.)
- **Program falsifier, v0.2-level statement.** The ranked program's falsifier stands verbatim: if
  several well-chosen real packets either cannot cross the source boundary without semantic
  distortion or repeatedly return construction-dependent, source-specific, or hierarchy-revision
  outcomes with no stable invariant, prefer a pluralist or alternative account and preserve the
  failed synthesis as the result. v0.2 adds one sharper conjunct: if F2 fires — if process-level
  typing never earns its slot over state-snapshot typing on real evidence — then even a surviving
  six-type vocabulary should be rebuilt state-level, and v0.2 (not v0.1) is the artifact that dies.

## 6. Relation to the decisive-test program (no verdicts issued here)

v0.2 changes no receiver update. Rank 1's scoped conditional FAVORS_CANDIDATE, Ranks 2–4 BLOCKED, and
all named repairs (transition-diagnosis run on GU-001-GR-001; two-phase preregistration; source-issued
Rank-2 paired cases + independent Frame R; §5-compliant Rank-3 campaign) stand exactly as the
decisive-tests SYNTHESIS states them. What v0.2 supplies to the program: (a) the typed target that
Rank 2's normalization-frame fork and Rank 4's representation-invariance challenge will test (the
frame-as-parameter design makes Rank 2's fork explicit rather than hidden); (b) the finality level's
diagnosis type that a future Rank 3 campaign would have to instantiate; (c) executable receiver-side
vocabulary with failing directions, lint-clean under the house discipline.

## 7. Nonclaims

- Not validated; not a receiver verdict; not a claim that any physical case instantiates any level.
- The six types are not claimed complete, universal, exclusive, or ontologically real (v0.1 §5 open
  claims all remain open).
- The opacity bound is a candidate mini-theorem at toy grade (register I-5), not a proven theorem
  over any native formalism.
- The forced-frame flag is not a structural-circularity detector; a detector with bite over
  structurally circular frames is open work (referee D1).
- The fiber corpus citation grades in §3 are the referees' corrected grades; nothing is cited above
  them; `bar(b)`, H59, Krein positivity, physical issuance OPEN.
- TI and TaF structures are cited at their owners' grades (E160/RUN-0025/OnlineIssuance^LC are
  TI-owned; D1/FinaliEvent machinery is TaF-owned); no cross-repo identity is asserted; no source
  claim moves.
- The skeleton is a deterministic synthetic toy; its 12 evidential checks validate instrument
  behavior under stipulated witnesses only.

## 8. Persistence (executed 2026-07-16; adjusted for referee correction D2)

- This document: `synthesis/2026-07-16-hierarchy-v0.2-typed-definitions-draft.md` (synthesis/ is
  where v0.1 lives and v0.2 is its typed successor). Joe reviewed and adopted it as the repo's typed
  hierarchy draft on 2026-07-16 in direct chat (trusted control channel; option A — full adoption
  with all referee corrections applied). Standing remains below ratified synthesis: not canon, no
  verdicts move.
- Skeleton: `tests/hierarchy_v02_typed_skeleton.py` (corrected; verified exit 0 and `--strict`-clean
  on 2026-07-16; honest headline 8 [E] + 4 [F] = 12).
- Register update (applied): I-1..I-5 rows note "engaged-by-v0.2 (finality level §2.6/§3)"; fixture
  4a has RUN and closed `ENDPOINT_POSITIVE_TOY` (statuses reflect that; 4b remains pending); I-6 and
  I-7 stay absorbed-into-v0.2.
- Progress-lanes update (applied): Lane 2 item 2 = "DRAFTED + adopted-with-corrections 2026-07-16".
