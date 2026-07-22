---
artifact_type: exploration
status: complete
governance_role: methodology_novelty_genre_scan
constitutional: false
created: 2026-07-22
relation_to_hard_core: Lane 2 legitimacy (literature position / novelty) feeding Lane 1 — runs the North Star's own falsifier at the methodology level before any domain fixture is built.
grade: EXPLORATORY (adversarial-referee-governed literature scan; no experiment run)
---

# Methodology-level novelty / genre scan of the P2C agent-capability methodology

## What is being scanned

Not the math core (already near-`NOTHING-NEW` per the repo's own position) but
the **agent-capability methodology**: the claim that an agent can determine
**what kind of change occurred** in a system by running a
**source-grounded, matched-frame, completion-rival, preregistered, abstaining
typed-change battery** over the ladder

> possibility -> dynamics -> records -> access -> capability -> finality.

The genre question: is this methodology **subsumed** by an existing body of
work? Six candidate subsumers were scanned, an adversarial referee governs the
grade, and scan/council agreement is explicitly *not* treated as evidence — the
literature disposes.

## Method

Read-only literature scan (WebSearch/WebFetch, July 2026). For each candidate
subsumer: (a) name its canonical inferential primitive; (b) ask whether that
primitive already performs P2C's load-bearing move; (c) decide subsumption of
that *primitive*, not of the whole battery. The referee then asks the harder
question: does any *single* prior package the whole battery for the
"what-kind-of-change" question across heterogeneous domains?

## Per-primitive subsumption table (related-work spine)

| P2C load-bearing primitive | Strongest prior that subsumes the *primitive* | Referee finding |
|---|---|---|
| **access vs capability distinction** | Control theory: **reachability (≈capability) / observability (≈access) duality** and the **Kalman decomposition** (a 4-way typed split: reachable-observable / reachable-unobservable / ...). Object-capability security: **capability = unforgeable token that both designates and authorizes** vs **ACL / ambient authority (access)**; the **confused-deputy** failure is precisely "raw access rose but the principal's normalized authority should not have." | **SUBSUMED as a distinction.** P2C's signature reject — "raw task access changed, but normalized capability did not" — is the observable-not-reachable / confused-deputy pattern re-expressed. Not novel. |
| **matched-frame / normalization / counterfactual** | **Halpern-Pearl actual causation** (structural-equation counterfactuals) and Halpern's "actual causation and the art of modeling" (verdicts are sensitive to the chosen variables/frame). | **SUBSUMED.** P2C's frame-indexing = HP's model/variable-choice sensitivity, applied as an explicit normalization step. Borrowed, not invented. |
| **completion-rival (strongest-rival steelman)** | **Platt strong inference** (enumerate and exclude multiple competing hypotheses); **Mayo severe testing** (a claim earns support only by surviving a demanding attempt to expose its falsity). | **SUBSUMED.** P2C's "the kill gets a defense attorney" completion-rival = severity + strong inference. Borrowed. |
| **preregistration / predeclared falsifiers** | **COS preregistration & registered reports**; the confirmatory-vs-exploratory demarcation; predeclared hypotheses/measures. | **SUBSUMED.** P2C's expectations-JSON + `prereg_verify` is a direct application of an established methodology. Borrowed. |
| **abstention as a first-class output** | Reject-option / abstaining classification (ML); agent-eval suites that already score **abstention** as its own category (e.g. BEAM). | **SUBSUMED.** Honest abstention is a recognized eval dimension, not a new primitive. Borrowed. |
| **a typed taxonomy of change** | Process-mining **change taxonomy** ("where / what / how" a process changed); categorical **causal abstraction**; BFO/DOLCE occurrent/continuant vocabulary (but BFO is *silent about what sorts of change exist*). | **PARTIALLY SUBSUMED.** Change taxonomies exist, but none is the possibility->...->finality ladder, and none carries the *records* and *finality* levels. This is the closest thing to an original element. |
| **"agent can determine what kind of change" framing** | 2025-26 agent evaluation moving "beyond task completion" to multi-dimensional / adversarial measurement; the LLM-judge bias literature (position/length/agreeableness bias). | **NOT PACKAGED elsewhere**, but the *eval-dimension* ideas (multidimensional, adversarial, abstaining) are established. The framing is fresh; the machinery is not. |

## Adversarial referee verdict: **NEW-FRAMING-ONLY**

Reasoning, stated so the strict reading and its rebuttal are both on the record:

**Strict push toward `NOTHING-NEW`.** Every load-bearing inferential *primitive*
of the methodology is subsumed by a mature literature: the access/capability
distinction by control theory *and* object-capability security (two independent,
precise priors); the matched frame by Halpern-Pearl; the completion-rival by
Mayo/Platt; preregistration by COS; abstention by reject-option ML and agent
eval. On the primitives alone, the methodology introduces **no new inferential
move**.

**Rebuttal that holds the line at `NEW-FRAMING-ONLY` (not `NOTHING-NEW`).** No
*single* prior packages these primitives into one **domain-neutral** instrument
that (a) spans possibility / dynamics / records / access / capability / finality
in a single diagnostic, (b) is designed to run *identically* on physics **and**
security **and** institutions, and (c) treats "what kind of change occurred" as
an **agent capability** tested with preregistered completion-rivals and honest
abstention. Control theory is dynamical-systems-bound; object-capability is
security-bound; Halpern-Pearl answers single-outcome causation, not
change-typing; process-mining taxonomies are model-drift-bound. The *records*
and *finality* levels, and the cross-domain agent-capability framing, are not
found packaged anywhere. That integration is a real but **modest** contribution
— a **new framing**, not a new methodology, because it invents no new
inferential primitive.

**Why not `NOVEL-METHODOLOGY`.** A `NOVEL-METHODOLOGY` grade would require at
least one inferential primitive that existing frameworks cannot supply. None was
found. Integration + a specific ladder + a framing does not clear that bar.

## The decisive contingency (this is the point of the gate)

The `NEW-FRAMING-ONLY` grade is **not** a standing property of the methodology.
Its entire novelty-value is **contingent on transfer evidence**. The framing is
worth something *only if* the *same* instrument classifies a change in a domain
where a mature subsumer already has a precise vocabulary — and produces a verdict
that the subsumer's own vocabulary cannot already produce more directly. Until
that is shown, the honest default is **"transfer fails"**: on any single domain
the P2C reading collapses into whichever established framework already owns that
domain (control theory for dynamics, object-capability for security, HP for
causation).

This is exactly the North Star's own predeclared falsifier — "the definitions
can't transfer beyond one domain without ad hoc reinterpretation" — restated at
the methodology level. It has never been run. The genre gate says: it is now the
highest-value thing to run, and it should be run **security-first**, because
object-capability security is the *strongest* subsumer and therefore the
cheapest possible falsification (or the first real evidence of non-subsumption).

## Consequence for the campaign

- **Do NOT** treat the methodology as established/novel. Grade is
  `NEW-FRAMING-ONLY`, adversarially governed.
- **Fixtures are conditionally warranted, security-first only.** The genre gate
  does not green-light a general fixture build. It green-lights *one* cheap
  security-domain transfer-breaker run (the prereg skeleton is in this folder)
  whose default forecast is "transfer fails." A pass there is the first evidence
  that lifts the grade off `NEW-FRAMING-ONLY`; a fail confirms `NOTHING-NEW` and
  fires the North Star falsifier honestly.
- **Related-work spine is now on the record** and must be cited by any future
  methodology write-up: control-theoretic reachability/observability + Kalman
  decomposition; object-capability security (capability vs ambient authority,
  confused deputy); Halpern-Pearl actual causation + the art-of-modeling
  frame-sensitivity; Platt strong inference + Mayo severe testing; COS
  preregistration / registered reports; process-mining change taxonomy +
  categorical causal abstraction; 2025-26 agent-evaluation-beyond-task-completion
  and the LLM-judge-bias literature.

## Non-claims

- No experiment was run; this is a literature-position scan at EXPLORATORY grade.
- Scan agreement is not evidence; the cited literatures, not any council, carry
  the grade.
- No source truth, capability, finality, canon, claim status, or public posture
  moved. A novelty verdict and a prereg skeleton are not claim promotions.

## Sources

- Halpern & Pearl, *Causes and Explanations: A Structural-Model Approach* (structural-equation actual causation); Halpern, *Actual Causation and the Art of Modeling* (arXiv:1106.2652); *A Modification of the Halpern-Pearl Definition of Causality*.
- Control theory: Kalman decomposition (reachable/observable subspaces); *Reachability and Observability* (Lewis); Antoulas/Sontag/Yamamoto, *Controllability and Observability*; *On the Duality between Observability and Reachability* (also used in formal software development).
- Object-capability security: *On access control, capabilities, their equivalence, and confused deputy attacks* (MPI-SWS); *Capability Myths Demolished*; *Confused deputy problem*.
- Process/event ontology: BFO (continuant/occurrent; *Towards Representing Change in the BFO*); DOLCE (endurant/perdurant); *Capabilities: An Ontology* (arXiv:2405.00183).
- Preregistration: COS Preregistration & Registered Reports; *Preregistration of exploratory research* (PLOS Biology).
- Severe testing / strong inference: Mayo, *Statistical Inference as Severe Testing* (2018); Platt, *Strong Inference*.
- Agent evaluation: *AI Agent Evaluation and Benchmarking: Beyond Task Completion*; BEAM (abstention/contradiction categories); LLM-judge bias audits (position/length/agreeableness bias).
- Change taxonomy / causal abstraction: process-mining change classification (where/what/how); *Causal Abstractions, Categorically Unified* (arXiv:2510.05033).
