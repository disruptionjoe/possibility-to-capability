---
artifact_type: rival_frame
status: frozen
version: v0.2
supersedes: lane-C Frame R v0.1 (explorations/2026-07-16-northstar-unblock/lane-C-frame-r-and-ti-case.md, Deliverable 1)
governance_role: rank2_prerequisite_candidate
constitutional: false
created: 2026-07-16
grade: philosophical-argument
tier: experiment-proposal (charter: experiments remain proposals until owners, packets, and execution authority are resolved)
---

# FRAME R — The Access-Constitutive Normalization Frame, v0.2 (independent advocate re-freeze)

## R.-1 Re-freeze provenance, independence, and quarantine

**What this is.** The lane-C referee (report attached to the lane file; verdict SOUND-WITH-CORRECTIONS,
firewall INDEPENDENT) ruled that Frame R earns candidate standing for the Rank-2 prerequisite
"strongest access-constitutive construction" **conditional on adoption/re-freezing by an advocate
independent of any case it will be scored on** (defect D1: lane C co-authored both Frame R v0.1 and the
TI-PIT-02 case draft, so lane C cannot be R's advocate against that case). This artifact is that
adoption. Its author is a separate run acting solely as Frame R's advocate.

**Advocate independence (declared).**

- This advocate did **not** author, revise, or repair TI-PIT-02, TAF-001, or any other case, and takes
  no position on any case's merits. Scoring cases is the preregistered Rank-2 run's job, not this
  artifact's.
- This advocate did **not** read: the repo mailbox (`system/mailboxes/possibility-to-capability/`),
  the Time as Finality repository, the Temporal Issuance repository,
  `explorations/2026-07-16-rank2-preregistration/` (the receiver's frozen expectations),
  the lane-B file (TAF-001 evidence), lane-A, lane-D, or the swing GOVERN file.
- Complete declared-reads list: §R.8.
- **Interleaving handled as follows.** The source file interleaves Frame R v0.1 with the TI-PIT-02
  draft and the referee report in one document; this advocate therefore incidentally saw the case text
  while reading its assigned Frame R source. That sighting is declared here rather than hidden. No
  TI-PIT-02 content — fixture, numbers, signature components, computed facts, or structure — is
  carried into this artifact, and v0.1's one textual dependence on the case (inside P4) has been
  removed and replaced with a case-free statement (§R.4). This advocate remains ineligible to author,
  issue, or score TI-PIT-02.

**Quarantine clause (referee D1 correction, adopted verbatim in substance).** Frame R and TI-PIT-02
may not be used together as a frame-discriminating pair in any Rank-2 run unless the run's
independent-reviewer and blind-issuer requirements are each satisfied by parties other than lane C.
Frame R earns **zero** predictive credit from any case authored by any of its advocates (v0.1's lane C
included, and this re-freezing advocate included, should either ever author a case).

**What changed from v0.1 (advocate's ledger).**

- Kept unchanged in substance: R.0 role, R.1 definition and its three consequences, Rules R1 and R3,
  the three-layer grounding (R.3), predictions P1, P2, P5, concession conditions C1–C4,
  anti-strawman clauses (R.5), and all four falsifiers R.6(a)–(d).
- Strengthened (all in R's favor as a rival, none against it): P4 rewritten case-free with an explicit
  zero-credit rule (voiding the false "in advance" claim the referee caught — a genuinely
  pre-committed P4 is stronger, not weaker); P3 scoped so that globally-patchable-by-construction case
  families neither support it nor cheaply fire R.6(c) against it (§R.4); Rule R2 hardened against the
  R.6(d) self-application attack (§R.2); R.6(c) restated at case-domain level with an enrichment
  opportunity for R's advocate (§R.6); C4's protocol tied to the repo's adopted preregistration
  mechanism (§R.4).
- Removed: every reference to TI-PIT-02 and its computed facts.

**Grade and status.** Every claim in this document is philosophical-argument grade unless marked
otherwise. Nothing here is a theorem; nothing here moves any source-repository claim; no receiver
verdict, gate outcome, or update-vocabulary term is issued or implied. Frame R is frozen as of this
commit; any future edit is a new version and voids the freeze.

## R.0 Role statement

Frame R is the strongest construction of operational-context relativism, authored and now re-frozen by
its own advocates, to serve as the "context-constitutive alternative" required by the Rank-2
paired-intervention test's prerequisites ("at least two independently defended normalization frames,
including the strongest access-constitutive construction"). R is offered frozen and in advance of any
outcome classification. R roots for itself, not for the receiver's hierarchy, and states its own
concession and falsification conditions below.

## R.1 Definition of capability (access-constitutive)

**Definition (R-capability).** Let S be a system and let I be an *interface*: a declared, jointly
specified triple of (a) observation channels (what about S can be registered), (b) control channels
(what can be done to S), and (c) a verification procedure (how task success is certified). Then

> Cap_R(S | I) = the set of task-instances (t, v) such that t can be *posed* through I's control
> channels and success *certified* through I's verification procedure v, and S succeeds.

There is no Cap_R(S). The unrelativized "task set the system can perform" is not an idealization of
Cap_R(S | I); it is a different kind of object — a God's-eye task ontology — and R holds that no
operational content attaches to it. The point is not epistemic ("we can only *know* capability through
access") but constitutive: a task is *individuated* by its verification conditions, verification is
access, therefore the task ontology inherits access-relativity before any question of knowledge
arises. "Capability minus access" is not capability purified; it is a change of subject.

Three consequences fix R's shape:

1. **No canonical completion.** Any "normalized" capability requires a canonical or maximal interface
   I* against which access differences are quotiented out. Either I* is a specific interface (then
   normalization is relative to a choice, and the choice is access), or I* is a limit over all
   interfaces (then its existence and uniqueness are exactly what must be proven, by universal
   property, not assumed).
2. **Coupled-system attribution.** Capability is a property of the pair (S, I), the way an affordance
   is a property of an animal-environment pair, not of the cliff or the animal alone.
3. **Facts, not just reports, are interface-relative** in R's strong reading (see R.3): what a system
   "did" is itself only defined relative to an interaction context.

## R.2 Classification rule for any paired intervention

Given a paired intervention (before-state B, after-state A) over a declared shared task vocabulary V,
with declared interfaces I_B, I_A:

**Rule R1 (primary).** If the *verified success profile* differs — i.e.,
Cap_R(S|I_A)∩V ≠ Cap_R(S|I_B)∩V — then the intervention is a **CAPABILITY_CHANGE**. This includes
every intervention the rival frame would call "access-only": enlarging observation or control channels
enlarges what can be posed and certified, hence enlarges capability. R does not possess ACCESS_CHANGE
as a contrast class at the same level. This is not evasion; it is R's substantive claim.

**Rule R2 (R's own internal distinction — the honest replacement).** R does draw a distinction, but a
different one, drawn entirely in interface-relative terms:

- An intervention is a **CONSERVATIVE INTERFACE EXTENSION** iff I_B ≤ I_A (channel-wise inclusion of
  declared channels) and the after-profile *restricted to the before-interface* equals the
  before-profile: Cap_R(S|I_A)|_{I_B} = Cap_R(S|I_B). New things are doable/certifiable; nothing
  formerly doable changed.
- An intervention is a **NON-CONSERVATIVE CHANGE** iff the restriction fails, or iff the profiles
  differ at a fixed interface (I_B = I_A but profiles differ).

**Rule R2′ (hardening against the self-application attack, new in v0.2).** The lane-C referee
correctly observed that R2's "channel-wise inclusion" risks inheriting the same mechanism/channel
decomposition parameter that P1 attacks in the rival — exactly the symmetry-breaker R.6(d) names. R's
advocate answers it now rather than waiting: R2 is a comparison between **two declared interfaces
given as data**, not a quotient over all interfaces. Inclusion I_B ≤ I_A is decidable from the two
declarations alone; no privileged background interface, maximal observer, or canonical completion is
consulted. Where a decomposition parameter genuinely re-enters is in the cross-leg identity posit —
the modeling claim that both legs concern "the same S." R takes the pair (S, I) as primitive, so for R
this posit is an explicitly declared input to the comparison; but the rival frame needs the *same*
posit (its "mechanism held fixed" leg is precisely a cross-leg identity claim), so the posit cannot
asymmetrically indict R. R.6(d) therefore fails against R2 unless it is shown that R2 needs a
privileged interface **beyond** the two declared ones and the shared identity posit. R's advocate
accepts that showing as a genuine falsifier (R.6(d) stands, unweakened); this clause narrows what
would count as showing it, in R's favor, honestly.

R predicts the receiver's ACCESS_CHANGE/CAPABILITY_CHANGE boundary, wherever it is stable, will turn
out to be a *relabeling* of conservative-extension/non-conservative-change — a distinction R already
owns without any God's-eye ontology — and that where the two boundaries diverge, the receiver's labels
will be completion-dependent (see R.4).

**Rule R3 (ill-formedness).** R declares the question "same capability, different access?" **not
well-formed** when no common interface exists through which V can be both posed and certified in B and
in A — i.e., when the comparison requires evaluating S's success on tasks that cannot be verified in
one of the two conditions. In that case there is no shared measurement context, and the classification
question has no truth-value rather than an unknown one. (This is R's analogue of the Rank-2 outcome
"no shared task comparison is meaningful.") Note carefully what R does *not* say: R does not declare
ill-formedness merely because access differs — that would trivialize the test. Ill-formedness requires
failure of common posability/certifiability of V itself.

**Rule R4 (out-of-model access audit).** When the paired cases are *formal models*, R requires the
classifier to declare which facts are certified only by God's-eye access to the model definition
(e.g., "the such-and-such structure was held fixed") versus facts certified through an in-model
interface. R predicts the "held fixed" leg of every paired intervention over formal models is
certifiable only from outside every in-model interface — which is R's point made flesh. (v0.1
illustrated this rule with a co-authored case; that illustration is removed. The rule stands on its
own and is tested per P4 below.)

## R.3 Strongest philosophical grounding

R's advocate has four candidate foundations and ranks them; the strongest is a three-layer argument
with **Bridgmanian operationalism as the semantic core, relational quantum mechanics as the physical
precedent, and a contextuality (Kochen–Specker-style) obstruction as the formal weapon.** Enactivism
and Gibsonian affordances are supporting precedents, not the load-bearing layer, because both concern
organism-scale cognition and invite the (unfair but effective) charge of biologism; R declines to rest
on them.

**Layer 1 — semantic (Bridgman, properly reconstructed).** Bridgman's claim, in its defensible modern
form, is not the crude verificationism that died with logical positivism; it is that a *concept
applied beyond the operations that define it is a new concept requiring new warrant*. "Length" defined
by rods and "length" defined by light-signals are distinct concepts that happen to agree in an overlap
regime; extrapolating either past its operational domain is a substantive posit, not an analytic
continuation. Apply this to "capability": the concept is anchored in test procedures — pose a task,
grant resources, certify success. A "capability the system has, independent of any procedure by which
the task could be posed or certified" extends the concept past every operation that gives it content.
The rival normalization frame does exactly this extension when it "subtracts access": it assumes the
concept survives the subtraction with its identity intact. Bridgman's razor says: show the new
operations that define the subtracted concept, or admit you have changed the subject. The
analytic-metaphysics literature on dispositions independently corroborates this: finks and masks show
that even "intrinsic disposition" resists context-free analysis — the simple conditional analysis
fails precisely because test-context contributions cannot be cleanly subtracted.

**Layer 2 — physical precedent (relational QM).** RQM (Rovelli) holds that the values of physical
variables are relative to interactions: there is no interaction-free fact of the matter about a
variable's value, and this is a statement about *facts*, not about knowledge. This matters to R
because the receiver's program is physics-adjacent (frozen packets about operators, spectral sections,
issuance). If the best available reading of our most tested physical theory already relativizes
*value-facts* to interaction contexts, then a normalization frame that posits interaction-free
*capability-facts* is asserting something the physics does not supply and arguably resists. R does not
claim RQM is proven; R claims the burden of proof is inverted — the separation frame, not R, is the
one importing a metaphysical extra.

**Layer 3 — formal weapon (contextuality obstruction).** The Kochen–Specker theorem: for Hilbert
dimension ≥ 3, there is no noncontextual assignment of definite values to all observables consistent
with the functional relations QM imposes. Structural analogy, stated as a precise prediction rather
than a metaphor: an access-subtracted capability profile is a *global assignment* of
doable/not-doable to all tasks in V, required to be independent of the measurement (interface) context
in which each task is embedded, and required to restrict correctly to every actually-available
interface. KS shows that in at least one physically real regime, globally consistent noncontextual
assignments of this logical shape *do not exist*, even though every single context has perfectly
definite local facts. R therefore predicts (P3) that sufficiently rich paired-case families will
exhibit contextuality-like obstructions: locally classifiable everywhere, globally unclassifiable — no
single access-independent capability assignment consistent with all interface restrictions.

Grade of R.3: philosophical-argument grade; the KS analogy is a structural claim whose bite in any
given case family is an empirical/formal question, and R stakes falsifiable content on it rather than
treating it as decoration.

## R.4 Predictions

For a **generic access-enlargement** (a paired case whose access-side leg widens observation/control
with the underlying mechanism nominally fixed), R predicts the receiver will find:

- **P1 (free parameter).** Every operationalization of "normalized task capability held equal"
  contains an undischarged canonical-interface assumption, visible as a free parameter: a completion
  class, a maximal-access stipulation, or a privileged decomposition of the system into "mechanism"
  and "channel." The receiver will be able to state the assumption but not derive it.
- **P2 (label flipping under admissible completions).** For at least some paired cases, two admissible
  completions of the interface (both consistent with the frozen evidence) will assign *different*
  labels — ACCESS_CHANGE under one, CAPABILITY_CHANGE under the other — i.e., no invariant quotient.
  This maps to the Rank-2 outcome "equally admissible frames disagree with no invariant quotient."
- **P3 (contextuality signature — scoped, sharpened in v0.2).** In case families rich enough to embed
  **incompatible interface contexts** (contexts that cannot be jointly refined into one declared
  interface), local classification will succeed in every context while global access-subtracted
  assignment fails (R.3, Layer 3). Scope discipline, stated by R's advocate in advance: a case family
  that is *globally patchable by construction* — compatible contexts with a definable global truth,
  e.g. deterministic single-observer families where every context-decided fact restricts a single
  global profile — is **outside P3's scope**. Such families provide no support for P3, and R claims
  none from them; symmetrically, no single such family fires R.6(c) against P3 (see R.6 for the
  domain-level condition that does).
- **P4 (out-of-model certification — rewritten case-free in v0.2, per referee D1).** In formal paired
  cases specifically, the "structure held fixed" certificate for the fixed-mechanism leg will be
  checkable only by God's-eye access to the model text, never through any in-model observer interface;
  and the changed-mechanism leg will admit parameter regimes in which a genuine structure change is
  *invisible* through every declared in-model interface. Where that occurs, the capability/access
  separation is being adjudicated entirely at a level no access in the model reaches — which is R's
  thesis, exhibited rather than refuted. **Credit rule (pre-committed):** P4 is testable only on cases
  that none of R's advocates authored. Frame R earns zero predictive credit from any advocate-authored
  case, however well it fits; on such cases P4 is postdiction by construction. This voids v0.1's
  "flagged in advance" claim on its co-authored case, permanently.
- **P5 (conservative-extension coincidence).** Where the receiver's labels are stable, they will
  coincide extensionally with R's conservative-extension/non-conservative distinction (R.2, Rule R2),
  showing the stable content never required the God's-eye ontology.

**What evidence would make R concede that a completion-stable capability/access separation exists
(concession conditions, stated by R's advocate in advance):**

R concedes — for the tested class, which is the only scope the claim can have — if the receiver
exhibits all of:

- **C1.** An explicitly characterized class **𝒞** of admissible interface completions (not one
  preferred completion), with a stated closure/exhaustion rationale, such that the ACCESS/CAPABILITY
  classification of every preregistered paired case is **invariant under all of 𝒞** and under
  admissible representation changes.
- **C2.** At least one nontrivial case landing stably in *each* class (a stable ACCESS_CHANGE and a
  stable CAPABILITY_CHANGE), with genuinely distinct preregistered predictions that came out as
  predicted.
- **C3.** The classifying invariant is constructed **without a privileged interface** — e.g., defined
  by a universal property (limit/colimit over the interface category) rather than by choosing a
  maximal observer — or, if a privileged interface is used, a proof that the classification is
  independent of which admissible privileged interface is chosen.
- **C4.** Survival of adversarial completion: R's advocate (or a successor) is granted a
  preregistered, bounded adversarial budget to construct completions in 𝒞 attempting to flip a label,
  and fails, with the exhaustion protocol (budget, search space, stopping rule) declared before the
  attempt — using the repo's adopted two-phase preregistration mechanism, so the declaration is
  mechanically prior to the outcome rather than merely asserted to be.

If C1–C4 hold, R concedes the separation is well-formed and completion-stable *for class 𝒞*, and
retreats to the class-relative remark that 𝒞-relativity is itself a form of context-relativity. R's
advocate acknowledges this retreat position is substantially weaker and says so now, so that a C1–C4
success cannot later be relabeled a draw.

## R.5 What R is not (anti-strawman clauses)

- R is **not** verificationism about all discourse; it is operationalism about *capability
  attributions* specifically, where the concept's content demonstrably comes from test procedures.
- R is **not** the triviality "everything is relative": Rule R2 gives R a sharp internal distinction
  with empirical bite, and Rule R3's ill-formedness verdict has strict conditions.
- R is **not** committed to denying the *usefulness* of fixed-mechanism modeling; it denies that
  fixed-mechanism talk picks out an access-independent capability fact rather than a convenient
  completion choice.
- R does **not** predict all paired cases are unclassifiable; it predicts classification is
  completion-relative, which is compatible with high local stability.

## R.6 R's own falsification conditions (by R's best advocate)

R is falsified or forced into major revision if any of the following is established:

- **(a) Universal-property construction succeeds.** A capability quotient defined by categorical
  universality over interfaces (hence choice-free in the relevant sense) exists, is nontrivial, and
  classifies real paired cases — this defeats P1 at the root rather than instance-by-instance.
- **(b) Adversarial completion exhaustion.** Under a preregistered exhaustion protocol (bounded
  budget, declared search space, declared stopping rule), R's advocate cannot construct any admissible
  completion that flips any label on the preregistered case set — defeating P2 in the strongest fair
  form available to a universally quantified claim.
- **(c) Contextuality prediction fails (restated at domain level in v0.2).** For the studied case
  families, globally consistent access-subtracted capability assignments exist and restrict correctly
  to every context — the KS analogy demonstrably fails to bite where R said it would (P3). Scope
  discipline, both directions: a single globally-patchable-by-construction family neither supports P3
  nor fires this falsifier — such families cannot exhibit the obstruction and so test nothing about
  it. R.6(c) fires at the level of the receiver's studied case **domain**: if, after R's advocate has
  been given one bounded, preregistered opportunity to propose incompatible-context enrichments of the
  case domain (e.g., multi-observer variants with non-jointly-refinable interfaces), the domain as
  enriched still yields globally consistent access-subtracted assignments everywhere, that is genuine
  evidence against R and R's advocate will treat it as such — it would mean the case domain is
  relevantly *unlike* the one regime where noncontextual global assignment is known to fail, and that
  R's formal weapon has no bite where R chose to fight.
- **(d) Self-application failure.** It is shown that R's own Rule R2 (conservative-extension test)
  cannot be stated without smuggling a privileged background interface — i.e., R's internal
  distinction has the same alleged defect as the rival's. R's advocate accepts this as a genuine
  symmetry-breaker against R, not a tu-quoque draw. (R2′ narrows what counts as the showing: the two
  declared interfaces and the shared cross-leg identity posit are not "smuggled background"; a
  privileged interface *beyond* those is.)

**What does NOT falsify R:** single cases where labels agree across the frames actually on the table
(agreement among frames sharing a completion convention is predicted by R); classifications stable
only under one preferred completion; the mere formal definability of a normalized capability
(definability is cheap; completion-stable definability is the test); or a single globally-patchable
family failing to exhibit the P3 obstruction (outside P3's scope, per above).

## R.7 Construction, assumptions, verification status, and reopening (repo artifact discipline)

- **Construction:** interface-relative capability (R.1) with the conservative-extension internal
  distinction (R.2); the construction fork against the receiver's normalization frame is the whole
  point of the artifact and is preserved, not resolved, here.
- **Assumptions:** the (S, I)-pair primitivity posit (R.2′); the three-layer grounding's readings of
  Bridgman, RQM, and KS as stated in R.3, at philosophical-argument grade.
- **Grade:** philosophical-argument grade throughout; no theorem, no computation, no empirical claim.
- **Verification status:** unverified rival frame, frozen for preregistered adjudication; the lane-C
  referee's audit (SOUND-WITH-CORRECTIONS; firewall INDEPENDENT) covers v0.1's content, and every
  referee correction bearing on Frame R (D1's P4/quarantine corrections) is applied in this version.
- **What would falsify it:** R.6(a)–(d).
- **What would reopen the freeze:** a Rank-2 run establishing any of R.6(a)–(d) or C1–C4; or a
  successor advocate producing a strictly stronger access-constitutive construction, which would
  supersede rather than edit this one.
- **What this artifact cannot do:** issue or influence any gate verdict; upgrade any source claim;
  serve as evidence about any specific case; or be scored against any case authored by its advocates.

## R.8 Complete declared-reads list (this re-freeze run; firewall per the house declared-reads method)

Read in full:

- `AGENTS.md`, `governance/CHARTER.md`, `steward/README.md`, `steward/research-portfolio.json`
- `explorations/2026-07-16-northstar-unblock/SYNTHESIS.md`
- `explorations/2026-07-16-northstar-unblock/lane-C-frame-r-and-ti-case.md` — the assigned source,
  including its attached referee report and, unavoidably (one interleaved file), the TI-PIT-02 draft
  text; handling declared in §R.-1
- `interfaces/README.md`, `experiments/README.md`

Filename listings only (no content): repo root, `interfaces/`, `experiments/`; `git status`/`git log
--oneline -5` (commit subject lines only — two subjects name the Rank-2 prereg commits; no prereg file
was opened).

**Not read (forbidden set, honored):** `system/mailboxes/possibility-to-capability/` (any file); the
Time as Finality repository; the Temporal Issuance repository;
`explorations/2026-07-16-rank2-preregistration/` (any file); lane-A, lane-B, lane-D, and GOVERN files
of the northstar-unblock swing; `experiments/2026-07-14-ranked-decisive-test-program-v0.1.md` (the
Rank-2 prerequisite wording used in R.0 is quoted via lane C's own quotation, not from the program
file); anything under `tests/`, `packets/`, `synthesis/`, `hypotheses/`, `evidence/`, `results/`,
`literature/`, `papers/`; no web fetches; no delegated reads by any agent.

**Contamination self-verdict:** none beyond the declared interleaved sighting of TI-PIT-02 inside the
assigned source file, which is inherent to the assignment and handled by content exclusion plus the
§R.-1 quarantine clause. The re-freeze is offered as **uncontaminated** on those declared terms; the
eventual Rank-2 run's independence assessment remains the receiver's to make and is not strengthened
by this self-verdict.
