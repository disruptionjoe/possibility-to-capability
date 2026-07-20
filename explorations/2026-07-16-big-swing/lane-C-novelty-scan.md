> Part of the 2026-07-16 P2C big swing (four adversarially-verified lanes). Exploration tier; no claim promotion; the attached referee report GOVERNS the grades — read it before citing the lane report.

# P2C Novelty Scan — Surviving Hard Core vs. the Literature

**Object under test:** "Observer/record networks carry a Z/2 consistency invariant (Harary balance = no negative cycle = XOR-SAT = Z/2 cocycle exactness) recurring as a common predicate across independently-motivated formalisms; the sign VALUE is a fiber the consistency layer cannot fix; the residual freedom is a global relabeling."

**Method note:** adversarial default ("already known") applied. The object decomposes into three components, graded separately:
- **(A)** the four-way equivalence (balance = no negative cycle = XOR-SAT = cocycle exactness);
- **(B)** "the sign value is an unfixable fiber; residual freedom is a global flip";
- **(C)** "this predicate recurs across independently-motivated observer/record formalisms."

---

## Component pre-verdicts (before the neighbors)

**(A) is textbook mathematics — SUBSUMED.** Harary (1953) proved balance = bipartition = every cycle positive; the XOR-SAT reading (bond signs as parity constraints, satisfiability iff no odd-negative cycle) and the Z/2 cocycle reading (a signed graph is balanced iff the sign function is a coboundary; frustration class lives in H^1(G; Z/2)) are standard in signed-graph theory (Zaslavsky's dynamic survey) and statistical physics. No referee will accept any part of (A) as new. [Signed graph — Wikipedia](https://en.wikipedia.org/wiki/Signed_graph)

**(B) is the 1977 spin-glass gauge picture — SUBSUMED.** Toulouse's frustration and the Z/2 lattice-gauge formulation say exactly this: cycle products (frustration) are gauge-invariant; individual bond/spin signs are gauge (switching) choices; on a connected balanced graph the residual symmetry is precisely one global Z/2 flip. "The consistency layer cannot fix the sign value; only relabeling freedom remains" is the definition of a gauge orbit. Referee citations: Toulouse 1977; [Fradkin–Huberman–Shenker line of work on spin glasses and gauge theories](https://www.sciencedirect.com/science/article/abs/pii/0370157380900782); [gauge-invariant frustration / vortex characterisation](https://arxiv.org/pdf/1012.3699); [history of frustrated spin systems](https://arxiv.org/html/2411.12826).

**(C) is the only component where novelty could live.** Assessed against neighbors below.

---

## Literature map and per-neighbor verdicts

### 1. Relational QM + cross-perspective links (Adlam–Rovelli) — OVERLAPS-PARTIAL (motivational only)

- [Adlam & Rovelli, "Information is Physical: Cross-Perspective Links in RQM" (arXiv:2203.13342)](https://arxiv.org/abs/2203.13342); [journal version](https://philosophyofphysics.lse.ac.uk/articles/10.31389/pop.8); critical replies: [arXiv:2310.18008](https://arxiv.org/pdf/2310.18008), [arXiv:2312.07056](https://arxiv.org/pdf/2312.07056).
- **Overlap:** the *problem* is the same — when do observer-relative records cohere into intersubjective agreement across a network of observers? The cross-perspective-links postulate is a pairwise record-consistency constraint, and the reply literature probes whether it is globally consistent — i.e., exactly a "local consistency vs. global obstruction" question, stated informally.
- **Not there:** no signed-graph structure, no Z/2 invariant, no balance predicate, no fiber/gauge statement. RQM's consistency discussion is qualitative.
- **Referee throw:** "Your 'observer/record network consistency' is the RQM cross-perspective-links debate; cite Adlam–Rovelli 2022 and the consistency critiques, and show your predicate does work theirs doesn't."

### 2. Quantum Darwinism (Zurek) — OVERLAPS-PARTIAL (weak)

- [Zurek, redundancy/branches (quant-ph/0505031)](https://arxiv.org/pdf/quant-ph/0505031); [generic emergence of objectivity (arXiv:1811.09062)](https://arxiv.org/pdf/1811.09062); [Quantum Theory of the Classical (arXiv:1807.02092)](https://arxiv.org/pdf/1807.02092).
- **Overlap:** consensus among many observers reading redundant records; "many observers agree" is the sociological cousin of balance. Also note: QD's consensus fixes the *outcome relative to a basis* but the einselected structure, not the record content, is what's derived — loosely parallel to "consistency layer fixes the predicate, not the value."
- **Not there:** QD's machinery is quantum mutual information and channel redundancy, not parity constraints; there is no invariant/fiber decomposition and no residual global symmetry statement.
- **Referee throw:** "Observer consensus about records is Quantum Darwinism's core claim; what does a Z/2 predicate add that mutual-information redundancy doesn't already capture?"

### 3. Consistent/decoherent histories — OVERLAPS-PARTIAL (weak-to-moderate)

- [SEP, Consistent Histories](https://plato.stanford.edu/entries/qm-consistent-histories/); [consistency conditions overview (Riedel)](https://blog.jessriedel.com/2014/03/18/consistency-conditions-in-consistent-histories/).
- **Overlap:** structurally the closest *shape*-match among the four named: a consistency condition (decoherence functional orthogonality) licenses classical probability assignment, and the single-framework rule says the formalism does not select among incompatible consistent sets — i.e., "consistency layer holds; the choice is not fixed by it." That is the same *logical form* as "the predicate holds; the fiber value is free."
- **Not there:** the CH freedom is a choice among frameworks (a large, non-group-structured family), not a Z/2 fiber with a clean global-flip residual; the consistency condition is bilinear in amplitudes, not a parity condition on a signed graph. No cocycle formulation exists in CH.
- **Referee throw:** "Your 'located-not-forced' residual freedom is the framework-choice freedom of consistent histories (Griffiths 1984; Gell-Mann–Hartle 1990); distinguish your Z/2 fiber from set-selection freedom or concede it's a special case dressed up."

### 4. DHR superselection (AQFT) — OVERLAPS-PARTIAL (strong structural analogy, disjoint mathematics)

- [nLab, DHR superselection theory](https://ncatlab.org/nlab/show/DHR+superselection+theory); [AQFT introduction (arXiv:1904.04051)](https://arxiv.org/pdf/1904.04051); [Giulini, Superselection Rules](https://philsci-archive.pitt.edu/3585/1/SSR-QMC-NetVersion.pdf).
- **Overlap:** this is the canonical "value is a fiber over the observable layer" theorem in physics. Sectors are inequivalent representations of one observable algebra; the observable (consistency) layer cannot fix which sector; the sector labels form representations of a global gauge group reconstructed from the observables. For a Z/2 gauge group (e.g., univalence superselection), DHR literally gives "observables fix everything except a Z/2 label, with a global gauge freedom." Emergent/einselection variants ([Giulini–Kiefer–Zeh, gr-qc/9410029](https://arxiv.org/abs/gr-qc/9410029); [Einselection](https://en.wikipedia.org/wiki/Einselection)) cover the "consistency layer dynamically produces the fiber structure" reading too.
- **Not there:** DHR is C*-algebraic and works on nets of local algebras, not finite signed graphs of records; the P2C object is combinatorial and applies to non-quantum record networks. But the *conceptual* claim "the sign is a superselection-like fiber, not derivable from the consistency structure" is anticipated in full.
- **Referee throw:** "Your fiber-over-consistency-layer picture is superselection theory in miniature (Doplicher–Haag–Roberts; Giulini); also compare Bartlett–Rudolph–Spekkens on superselection as absence of a shared reference frame — your 'no canonical anchor between two globally-flipped choices' is their 'sign convention without a shared reference frame.'"

### 5. Sheaf-theoretic contextuality (Abramsky et al.) — **SUBSUMED for component (C) at the generic level. Closest prior work.**

- [Abramsky–Barbosa–Kishida–Lal–Mansfield, "Contextuality, Cohomology and Paradox" (arXiv:1502.03097)](https://arxiv.org/pdf/1502.03097); [Abramsky–Mansfield–Barbosa, "The Cohomology of Non-Locality and Contextuality" (arXiv:1111.3620)](https://arxiv.org/abs/1111.3620); [AvN for stabiliser states (arXiv:1705.08459)](https://arxiv.org/pdf/1705.08459); [comparison of cohomological obstructions (arXiv:2212.09382)](https://arxiv.org/pdf/2212.09382); [cohomology in constraint satisfaction (arXiv:2206.15253)](https://arxiv.org/pdf/2206.15253).
- **Overlap — near-total on the recurrence thesis.** This program's explicit thesis ("contextual semantics") is that ONE invariant — local consistency without a global section, witnessed by a Čech-cohomological obstruction, with the Z/2 case realized as inconsistent XOR theories — recurs across independently-motivated formalisms: quantum empirical models, relational databases, constraint satisfaction, and semantic paradoxes. Their Liar cycles ARE negative cycles; their All-vs-Nothing arguments ARE unsatisfiable Z/2 linear systems; their obstruction IS cocycle non-exactness. The adjacent parity-game literature ([Cleve–Mittal, arXiv:1209.2729](https://arxiv.org/abs/1209.2729); [Arkhipov, arXiv:1209.3819](https://arxiv.org/pdf/1209.3819)) further develops exactly the classical-vs-quantum satisfiability of Z/2 constraint systems. So "a Z/2 consistency predicate recurring as a common invariant across independently-motivated formalisms" is not merely known — it is the *advertised headline* of an established research program.
- **Not there:** the *specific* fiber statement (B) is less emphasized (they focus on the obstruction, not on the residual global-flip freedom of the satisfiable case — that part is the spin-glass gauge picture instead), and GU/TI/TaF are obviously not among their instances.
- **Referee throw:** the fatal one. "Theorem 1 of Abramsky et al. 2015: your invariant, your equivalences, your cross-domain recurrence claim. What is left?"

### 6. Signed-graph consensus (Altafini) — SUBSUMED for the "consensus network with residual global relabeling" reading

- Altafini 2013 (IEEE TAC) via: [tutorial on dynamic social networks, Part II (arXiv:1801.06719)](https://arxiv.org/pdf/1801.06719); [bipartite consensus via balancing sets (arXiv:2011.14105)](https://arxiv.org/pdf/2011.14105).
- **Overlap:** bipartite consensus on a structurally balanced signed network converges to opinions *equal in modulus, opposite in sign* — the Z/2 fiber left unfixed by the network's consistency structure, with gauge transformations doing the switching. This is components (A)+(B) instantiated in agent networks, published and standard.
- **Referee throw:** "Balance-gated consensus with a residual sign ambiguity is Altafini's theorem."

---

## What in the P2C framing is NOT already in the literature

After the adversarial pass, exactly one thing survives, and it is conditional:

**The program-specific crosswalk fact:** that GU's Gate-2a consistency check, TaF's T39, and the TI encoding — three formalisms with independent motivations *within this research ecosystem* — all reduce to the same Harary predicate *on one shared signed-graph encoding*, with the Krein-sign question landing precisely in the known unfixable fiber. No external paper contains this because no external paper contains GU, TI, or TaF. Its value as a contribution is therefore **derivative**: it is a contribution to the external literature only if/when the source formalisms are, and per the ADAPTER2-01 correction it is currently a shared *encoding-level* predicate, not an isomorphism of native objects. Additionally, the combination "(A)+(B) stated together as one package — invariant + fiber + global-flip residual — applied to observer/record networks" does not appear verbatim anywhere I found, but every joint of the package is individually standard and the assembly is short.

---

## Verdicts

| Neighbor | Verdict |
|---|---|
| Relational QM + cross-perspective links | OVERLAPS-PARTIAL (problem, not math) |
| Quantum Darwinism | OVERLAPS-PARTIAL (weak) |
| Consistent/decoherent histories | OVERLAPS-PARTIAL (logical form of "consistency doesn't select") |
| DHR superselection | OVERLAPS-PARTIAL (fiber picture anticipated conceptually; math disjoint) |
| Sheaf/cohomological contextuality (Abramsky et al.) | **SUBSUMED** (the recurrence thesis itself) |
| Spin-glass frustration/gauge (Toulouse, FHS) | **SUBSUMED** (fiber + global flip) |
| Signed-network consensus (Altafini) | **SUBSUMED** (balance-gated consensus with sign ambiguity) |

**OVERALL VERDICT: (ii) NEW-FRAMING-ONLY** — and near the boundary with (i) NOTHING-NEW for the object as stated. Every mathematical component (the four-way equivalence, the fiber structure, the global-flip residual, and even the meta-claim "this Z/2 invariant recurs across independently-motivated formalisms") exists in mature published form. What the P2C framing does is *organize* known pieces (Abramsky's obstruction + Toulouse's gauge fiber + Altafini's consensus instance) around a new set of instances (GU/TI/TaF). The only candidate-novel item is the program-internal crosswalk (three named in-house formalisms sharing one encoding, with bar(b) located in the fiber), which cannot be claimed as an external contribution at the current grade and does not upgrade any source claim.

**Strongest single closest prior work:** Abramsky, Barbosa, Kishida, Lal, Mansfield, *"Contextuality, Cohomology and Paradox"* (CSL 2015, [arXiv:1502.03097](https://arxiv.org/pdf/1502.03097)) — Z/2 Čech-cohomological obstruction to global consistency, inconsistent XOR theories, negative (Liar) cycles, and an explicit cross-domain recurrence thesis spanning quantum models, databases, constraints, and paradoxes. Second-closest, for the fiber/global-flip half: Toulouse (1977) and the [spin-glass ↔ Z/2 gauge theory correspondence](https://www.sciencedirect.com/science/article/abs/pii/0370157380900782).

**Program implication (consistent with charter's Failure-Preservation rule):** this is a *bounding* result and should be recorded as a success. It tells the program: (a) do not write up the hard core as a standalone contribution; (b) the Gate #1 milestone (native branch-preserving functor, or its disproof) is where any genuine contribution must come from, because the consistency-layer story is fully occupied territory; (c) when Gate #1 work is written up, the mandatory related-work spine is Abramsky et al. 1502.03097, Toulouse/FHS, Altafini, DHR/Giulini, Adlam–Rovelli — a referee will demand all five.

Sources: [arXiv:2203.13342](https://arxiv.org/abs/2203.13342) | [arXiv:2310.18008](https://arxiv.org/pdf/2310.18008) | [arXiv:2312.07056](https://arxiv.org/pdf/2312.07056) | [PoP journal](https://philosophyofphysics.lse.ac.uk/articles/10.31389/pop.8) | [arXiv:1111.3620](https://arxiv.org/abs/1111.3620) | [arXiv:1502.03097](https://arxiv.org/pdf/1502.03097) | [arXiv:1705.08459](https://arxiv.org/pdf/1705.08459) | [arXiv:2212.09382](https://arxiv.org/pdf/2212.09382) | [arXiv:2206.15253](https://arxiv.org/pdf/2206.15253) | [arXiv:1701.00656](https://arxiv.org/pdf/1701.00656) | [quant-ph/0505031](https://arxiv.org/pdf/quant-ph/0505031) | [arXiv:1811.09062](https://arxiv.org/pdf/1811.09062) | [arXiv:1807.02092](https://arxiv.org/pdf/1807.02092) | [SEP Consistent Histories](https://plato.stanford.edu/entries/qm-consistent-histories/) | [Riedel on consistency conditions](https://blog.jessriedel.com/2014/03/18/consistency-conditions-in-consistent-histories/) | [nLab DHR](https://ncatlab.org/nlab/show/DHR+superselection+theory) | [arXiv:1904.04051](https://arxiv.org/pdf/1904.04051) | [Giulini SSR](https://philsci-archive.pitt.edu/3585/1/SSR-QMC-NetVersion.pdf) | [gr-qc/9410029](https://arxiv.org/abs/gr-qc/9410029) | [Einselection](https://en.wikipedia.org/wiki/Einselection) | [FHS spin glass gauge](https://www.sciencedirect.com/science/article/abs/pii/0370157380900782) | [arXiv:1012.3699](https://arxiv.org/pdf/1012.3699) | [arXiv:2411.12826](https://arxiv.org/html/2411.12826) | [Signed graph](https://en.wikipedia.org/wiki/Signed_graph) | [arXiv:1209.2729](https://arxiv.org/abs/1209.2729) | [arXiv:1209.3819](https://arxiv.org/pdf/1209.3819) | [arXiv:1310.3794](https://arxiv.org/abs/1310.3794) | [arXiv:1801.06719](https://arxiv.org/pdf/1801.06719) | [arXiv:2011.14105](https://arxiv.org/pdf/2011.14105)

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs grades)

# Referee Report — Lane C-novelty-scan

## 1. VERDICT: **SOUND-WITH-CORRECTIONS**

The scan's negative/bounding conclusion survives adversarial review. Its direction of error is safe (it tested a *stronger* object than the surviving hard core, which biases toward subsumption, and the verdict is negative). But it contains two moderate overclaims — one of which repeats, in miniature, exactly the ADAPTER2-01 error class (stating an encoding-level fact as a formalism-level fact) — plus citation-hygiene defects.

**What I verified independently:**
- **Component (A)/(B) math, re-derived by brute force** (300 random signed graphs, n≤7): balance ⇔ XOR-SAT satisfiability held in all cases; every connected balanced instance had exactly 2 satisfying assignments related by global flip. 0 mismatches. The SUBSUMED grades for (A) and (B) are correct and correctly cited (Harary balance theorem, switching/gauge-orbit picture are textbook).
- **Abramsky et al. arXiv:1502.03097 fetched and confirmed**: title, authors, All-vs-Nothing cohomological obstructions, and the explicit cross-domain scope ("in other fields as well, for example database theory... unified view of contextuality"). The "closest prior work" designation is well-supported.
- **arXiv:2310.18008 fetched and confirmed** as a genuine RQM-consistency critique (Lawrence–Markiewicz–Żukowski).
- **No source-sovereignty violation**: the report upgrades no GU/TI/TaF claim, and its program implications match the Gate-1 milestone doc (`explorations/2026-07-16-research-program-state-and-gate-1-milestone.md`).
- **No mislabeled control / cannot-fail test in the scan method itself**: the scan structure permitted a "novel" outcome; it returned negative on evidence.

## 2. Defects

**D1 — MODERATE — Object-under-test inflated above the surviving hard core; embeds a cannot-fail structure.**
The surviving core per the program-state doc and ADAPTER2-01 is: the Harary predicate "recurs across the GU (Gate 2a), TaF (T39), and TI **encodings** *on a shared signed-graph input*" — explicitly *not* an isomorphism of native objects. The report's headline object says the invariant "recur[s] as a common predicate across **independently-motivated formalisms**." Two inflations: (a) "formalisms" for "encodings on one shared input"; (b) "independently-motivated" — the shared encoding was built by one crosswalk session, so three encodings constructed to share a signed-graph input **cannot fail** to share the Harary predicate. The GU/TI/TaF recurrence is partly by construction; only recurrence in the *external* neighbors is informative. Mitigation: the inflation makes subsumption easier, so the negative verdict is unharmed — but the "candidate-novel item" that survives is correspondingly weaker than stated.

**D2 — MODERATE — Direct tension with ADAPTER2-01 in the survivor paragraph.**
"...all **reduce to** the same Harary predicate... with the Krein-sign question **landing precisely in the known unfixable fiber**." ADAPTER2-01 downgrades both halves: "Agreement of three algorithms on one shared graph is not an isomorphism of the complete native GU, TI, and TaF objects," and "The Krein sign is not presently identified with finality-axis polarity" — the fiber picture is the *best-supported shape at finite structural grade in a toy enrichment*; whether native bar(b) is that fiber point is exactly the OPEN bridge (two-adapter precondition not met). The report self-corrects one sentence later ("shared encoding-level predicate, not an isomorphism"), but the survivor claim as worded asserts what is open.

**D3 — MINOR — Unverified theorem attribution.**
"Theorem 1 of Abramsky et al. 2015: your invariant, your equivalences, your cross-domain recurrence claim." The cross-domain recurrence is that paper's program-level thesis, not a single numbered theorem; I could not verify any "Theorem 1" carrying all three. Rhetorically fine as a referee-throw, embarrassing if quoted forward.

**D4 — MINOR — Citation hygiene.**
(a) The link labeled "Fradkin–Huberman–Shenker" is a Physics Reports pii (0370-1573...); FHS "Gauge symmetries in random magnetic systems" is *Phys. Rev. B* 18, 4789 (1978). The link returned 403 and is unverifiable — it likely points to a different (review) article. Must be resolved before this list is used as the "mandatory related-work spine." (b) Orphan sources in the footer never cited in the body: arXiv:1701.00656, arXiv:1310.3794. (c) Several per-neighbor one-line characterizations (e.g., 1705.08459 as "AvN for stabiliser states") were not spot-checked here.

**D5 — MINOR — Evidence for the residual "(A)+(B) package not verbatim anywhere" is weak.**
"Does not appear verbatim anywhere I found" is absence-of-evidence from one search pass; given Toulouse+Altafini each state most of the package, this residual should not be carried as even a soft novelty candidate.

## 3. Corrected wording

- Object under test → "Three **program-internal encodings** (GU Gate-2a, TaF T39, TI) **evaluated on one shared signed-graph input** all compute the Harary-balance predicate; the sign value is a fiber the consistency layer cannot fix; the residual freedom is a global relabeling. The shared-input agreement is partly by construction of the common encoding."
- Survivor paragraph → "…three encodings **agree on one shared signed-graph input** (agreement partly guaranteed by the encoding choice), with the Krein-sign question **conjecturally located** in the unfixable fiber **at toy/exploration grade** — the native identification is OPEN per ADAPTER2-01."
- Referee-throw → "Abramsky et al. 2015 already state your invariant, your equivalences, and your cross-domain recurrence thesis" (drop the theorem number).

## 4. Grade the main result actually earns

**Bounding result, exploration/literature-scan grade — usable for program steering; not yet citation-grade.** Specifically:
- The verdict **NEW-FRAMING-ONLY (near NOTHING-NEW)** is earned, not overclaimed — after D1/D2 corrections the externally-stateable object tips *further* toward NOTHING-NEW; NEW-FRAMING-ONLY survives only for the program-internal organization of known pieces around GU/TI/TaF instances.
- The program implications (don't write up the hard core standalone; any contribution must come through Gate #1's native branch-preserving functor or its disproof) are consistent with the charter's Failure-Preservation Rule and with the Gate-1 milestone doc, and stand as recorded.
- The proposed five-citation related-work spine is directionally right but **not verified**: the FHS link must be resolved (D4a) and each entry individually confirmed before it is treated as mandatory.

Files consulted: `./governance/CHARTER.md`, `./explorations/2026-07-16-research-program-state-and-gate-1-milestone.md`, `../gu-formalization/explorations/time-as-finality-crosswalk/adapter2-correction-polarity-fiber-not-axis-2026-07-15.md`.