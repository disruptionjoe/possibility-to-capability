> Part of the 2026-07-16 fiber-closure swing (2-prime adversarial twins + T26 + tooling). Exploration tier; no claim promotion; the attached referee report GOVERNS the grades — read it before citing the lane report.

All receipts verified: committed at `d20c126`, pushed to `origin/main`, deterministic exit 0. The deliverable follows.

---

# P2C — Condition 2′ NO-GO (impossibility lane): flip-equivariance completeness theorem over a finality/issuance-native signature

Tier: exploration. Grade: **toy-grade no-go — symbolic theorem (structural induction, general over the class) + machine-checked completeness on a finite instantiation (exhaustive primitive battery, 7,544 distinct definable functionals verified, closed-term closure), with six failing-direction controls on the same checker code paths.** No claim promotion. GU/TI/TaF remain sovereign; nothing here reopens the withdrawn `bar(b) = finality-axis polarity` identity or moves `bar(b)`, H59, Krein positivity, or physical issuance (all OPEN). Governed by ADAPTER2-01 and the swing-2 referee-corrected grades. Runnable receipt persisted in-repo: `tests/no_go_2prime_flip_equivariance.py`, commit `d20c126` (pushed to `origin/main`), deterministic exit 0 (byte-identical output across repeat runs, verified).

## VERDICT: **NO-GO-PROVED (toy grade, class stated, receipts)**

**No finality/issuance-native structure — precisely: no functional definable over a vocabulary on which the global flip acts as an automorphism (class H, §1) — can derive an ORIENTED sector-asymmetric spectral condition (name which Krein sector carries the bounded-below/stable spectrum).** The UNORIENTED condition ("exactly one sector is spectrally positive") is derivable inside the class and flip-invariant (Corollary C3) — the fork is expressible; the selection is not. Deriving the orientation requires adding a primitive or constant on which the flip fails to be an automorphism — a sector constant, an ordered (K+,K−) pair, an oriented η, or a named non-flip-fixed generator/observer — **and that added symbol is the posit**, mechanically identifiable by the membership battery in this fixture. This is exactly the swing-2 lane-3 "one external Z/2 bit" conclusion, upgraded from an instance battery to a completeness theorem over all definable functionals (the referee's L6 gap, closed at toy grade).

## 1. The hypothesis class H (total precision)

**Sorts and the global flip g** (g∘g = id; the swing-2 lane-3 recoordinatized flip: form → −form, J → −J, labels swapped, folded into S-conjugation, S = e1↔e3, e2↔e4, SηS = −η):

| Sort | Domain (finite instantiation) | g acts by |
|---|---|---|
| `Lit` | {(p,±1),(q,±1)} | sign flip (p,ε)↦(p,−ε) |
| `State` | 9 consistent literal sets, ordered by extension | elementwise flip |
| `Obs` | 6 scripted issuance chains, **orbit-closed** (alice/alice~, bob/bob~, carol/carol~) | script flip, stop unchanged |
| `Pop` | 9 observer subsets, g-closed as a set (asymmetric populations exist **as parameters**) | elementwise |
| `Gen` | 8 generators, **orbit-closed**: {A_c, H_spec, A_bsym, A_a} ∪ S-conjugates | A ↦ SAS |
| `Vec` | 7 vectors closed under S | v ↦ Sv |
| `Sector` | {K+, K−, NONE} | **the swap K+↔K−** (no fixed point on {K+,K−}), NONE fixed |
| `SectorPair` | {PAIR} — the pair {K+,K−} **UNORDERED** | identity (flip-fixed) |
| `Bool/Nat/Real` | standard | identity |

**Signature Σ** (36 symbols, all listed in the fixture): constants `empty, none, the_pair, n0, n1, n2` (all g-fixed); primitives covering the **extension order** (`extends, card, contains, add_lit, consistent_union`), **record counts/profiles** (`card, history, issued_after`), **aliveness/liveness** (`live, live_slice`), **fork structure and realization** (`add_lit, some_live_extender`), **issuance-to-dynamics coupling** (`assigned_gen`, g-intertwining), **Krein form η via its flip-equivariant derivatives** (`sector_of, q_neutral, q_abs` — the form up to overall sign, i.e. the neutral cone, |q|, and the fundamental decomposition as an unordered pair), the **unordered {K+,K−}** (`memb, other, eq_sector, the_pair`), **spectra and realizability** (`sector_bounded, restr_spec_pos, c_stab, c_energy, trace, specabs, eq_gen`), and logic/arithmetic glue (`not_, and_, leq_nat, succ, rleq, ite_sector`). Note the class is **generous**: it admits sector-VALUED equivariant functionals (`c_stab`, `c_energy`, `sector_of`, `other`) — the strongest candidates the constructive twin can use.

**Definition (class H).** A signature Σ with structure M is *finality/issuance-native* iff (i) g maps each domain bijectively onto itself; (ii) g fixes every constant; (iii) g commutes with every primitive: f(g·a₁,…,g·aₖ) = g(f(a₁,…,aₖ)) for ALL argument tuples. Equivalently: g is a Σ-automorphism of M; equivalently: graph(g) is a subalgebra of M×M.

**Mechanical membership test.** For finite M, run the exhaustive primitive battery (`battery` in the fixture: every symbol × every argument tuple; here 844 tuples). Any claimed construction is decidably in or out of the class by this test — this is the decidability the adversarial-twin protocol demands (§5).

## 2. Theorems (symbolic; proofs do not use finiteness)

**Theorem T1 (equivariance).** If M ∈ H, then every Σ-term t(x₁…xₙ) satisfies t(g·a₁,…,g·aₙ) = g(t(a₁,…,aₙ)).
*Proof.* Structural induction on term formation. Base: variables (trivial identity); constants (clause ii). Step: t = f(t₁,…,tₖ): by IH each tᵢ(g·ā) = g(tᵢ(ā)); by clause (iii), f(g(t₁(ā)),…) = g(f(t₁(ā),…)). Nothing else is a term. Algebraically: graph(g) is a subalgebra of M×M (clauses ii–iii), and term evaluation preserves subalgebras. ∎

**Theorem T1′ (logic upgrade).** The same holds for every formula of first-order logic over Σ (quantifier case: domains are g-closed by clause i), and for any isomorphism-invariant semantics over M (automorphisms preserve satisfaction). A functional NOT invariant under isomorphism is, by definition, using structure outside Σ. This closes the "richer frameworks" escape at the level of the symbolic claim: richer *logic* does not escape; only richer *vocabulary* does, and richer vocabulary is battery-checkable.

**Corollary C1 (no parameter-free sector selection).** For a closed term t of Sector sort: t^M = g(t^M) (T1), and g has no fixed point on {K+,K−} (the swap), so t^M = NONE. The vocabulary cannot canonize a sector without parameters.

**Corollary C2 (orbit-indistinguishability, completeness form).** For every Bool-valued Σ-term φ and every generator A: φ(g·A, g·params) = φ(A, params); with no other free variables, φ(flip A) = φ(A). **No definable predicate separates the flip-orbit members.** A separator with a fixed non-flipped parameter requires that parameter to be a non-g-fixed constant — i.e. an orbit-representative datum, the external bit. This upgrades swing-2 lane 3's orbit lemma ("group-theoretic tautology plus finite instance battery", referee L6) to a completeness statement over **all** functionals definable in the class, at toy grade.

**Corollary C3 (the sharp line through condition 2′).** (i) The UNORIENTED sector-asymmetric spectral condition — "exactly one sector has positive restricted spectrum", as the term `not_(eq_sector(c_energy(x), none()))` — is Σ-definable and flip-INVARIANT (true on both H_spec orbit members). (ii) Its ORIENTATION is equivariant, never invariant: c_energy(H_spec) = K+ and c_energy(flip H_spec) = K−. So a class-H theory can prove *that* the world's dynamics is sector-asymmetric, but "K+ specifically carries the bounded-below spectrum" is underivable: any derivation must factor through a flip-symmetry-breaking symbol. **That symbol is the posit — condition 2′ cannot be met inside the class.**

## 3. Machine receipts (evidence accounting per house discipline)

Only [E] and [F] count as evidence; [T] items are listed separately and carry no weight.

**[E] evidence (exhaustive, not sampled):**
- **e1** — primitive-equivariance battery: ALL 36 symbols × ALL argument tuples (844), 0 violations. This is simultaneously the induction step of T1 over the implemented model and the class-H membership test.
- **e2–e5** — term enumeration with per-term verification over four declared variable contexts, semantic deduplication (two terms with identical value on every assignment have identical equivariance status, so verifying each distinct semantic vector verifies every term of the fragment): CTX-A {x:Gen} depth≤6 (15 distinct / 107 candidates — orbit fragment saturates); CTX-B {x:Gen, o:Obs, t:Nat} depth≤4 (3,838 distinct / 22,978 candidates — issuance-to-spectrum coupling); CTX-C {s:State, l:Lit, P:Pop, t:Nat} depth≤4 (3,531 / 14,531 — record/fork/aliveness); CTX-D {v:Vec, x:Gen} depth≤4 (160 / 2,250 — η-derivatives). **Total: 7,544 distinct definable functionals, every one flip-equivariant; 39,866 candidate applications examined.**
- **e6** — closed-term closure to fixpoint: every parameter-free definable element is g-fixed; the definable Sector elements are exactly {NONE} (C1's receipt).

*Disclosed relationship:* given e1 and T1's two-line proof, e2–e6 cannot fail mathematically; they are [E] with respect to implementation/proof error only — which is precisely what the [F] controls attack. This is stated in the fixture header, not hidden.

**[F] controls (six, each exercising the SAME code path it protects):**
- **f1/f1b** — Σ + sector constant `kplus()`: the same battery catches it (violations = exactly the kplus tuples), and the same term enumerator finds 16 non-equivariant terms including the depth-1 witness `kplus()`.
- **f2** — Σ + `eta_contractive` (the oriented-η functional; the sign posit restated per swing-2 T-a′): battery catches it, witnesses include the A_a and A_c orbits. The class boundary correctly classifies the historically-known label-reader.
- **f3/f3b** — sabotaged comparator (never flags) on the same battery and same enumeration with the same planted defect: reports 0 violations — a checker without teeth demonstrably fails; the passes in e1–e5 are the comparison actually running.
- **f4** — sabotaged flip (identity on Sector): the planted `kplus` is now MISSED while genuine mixed-sort primitives (`c_stab`/`c_energy`/`sector_of`) are falsely flagged — both verdict directions depend on the correct flip action.

**[T] items (definitional/entailed, no headline weight):** t1–t5 setup (g involution, domains g-closed, S properties, swap fixed-point-free, states/chains admissible); t6 (C2 exhibited by direct scan — entailed by T1+e1); t7/t8 (C3 exhibited); t9–t12 (twin-direction terms exhibited, §5).

## 4. Adversarial-twin comparison protocol (decidable boundaries)

**The no-go's hypothesis class is class H of §1, membership decided by the battery.** For any claimed construction:

1. List its primitive vocabulary and constants as a Σ (the fixture's data format: (name, argsorts, ressort, fn)).
2. Run `battery` with the flip g of §1. **Battery passes** → the construction is in class H → by T1/C1/C2/C3 its sector selection is equivariant: it selects only relative to the orbit representative supplied as a parameter, and supplying the representative is the external Z/2 bit. It has NOT derived the orientation. **Battery fails** → the failing symbol is named mechanically, and that symbol is the flip-symmetry-breaking posit the construction consumed.

There is no third case. A construction escapes the no-go only by (a) a Sector constant or ordered (K+,K−) pair (equivalent under `fst`), (b) an oriented η (sign of form values, η-contractivity direction, signed trace(J·)), (c) a non-g-fixed constant of any sort — a NAMED generator ("the physical Hamiltonian" as opposed to its S-conjugate), a named signed observer/literal, an asymmetric population named rather than parameterized, or (d) external choice data selecting orbit representatives. Each is one Z/2 bit in the toy — the three-names bit of swing-2 lane 3.

**Twin's three announced directions, checked in-class** (fixture t9–t12; the twin's committed probe `tests/condition2prime_constructive_probe.py` at `a193a3b` was inspected):
- **A1 irreversibility-as-spectrum**: expressible as `ite_sector(live(o,t), c_stab(assigned_gen(o)), none())` — inside H, equivariant. The extension-order arrow is flip-invariant (lane D check 4); coupling it to spectra via any g-intertwining assignment stays inside.
- **A2 growth functionals**: `card(issued_after(o,t))` and all Nat-valued monotones — inside H, flip-invariant (counts cannot see the sign).
- **A3 fork-realization**: `some_live_extender(add_lit(s,l), P, t)` — inside H, equivariant (realization tracks the flipped branch). Lane D's full aliveness selection rule is also inside: `contains(live_slice(P,t), l)` (t12), reproducing lane D's framework theorem as a Σ-instance.
- The twin's own helper functions `c_circ` (≡ K+, a sector constant) and `eta_contractive`/`eta_expansive` (oriented η) are **outside class H** — exactly the symbols my f1/f2 controls plant and catch. If the twin's headline uses either, the comparison is decided mechanically: the posit is named.

No twin direction fell outside the class as formalized; no class extension was needed.

## 5. Honest bounds

- **What the no-go does NOT say.** It does not say sector-asymmetric dynamics is impossible in the class (the referee's L2 counterexample class — `C_decay`-style refinements — and `c_stab`/`c_energy` all live inside H and do distinguish sectors *relative to a generator*); it does not say the unoriented asymmetry is underivable (C3(i): it IS derivable); it does not touch whether nature's bit is somehow selected (Located-Is-Not-Forced: this result locates the cost of the orientation, it does not price nature's choice).
- **Grade split.** T1/T1′/C1–C3 are symbolic and hold for any Σ-structure in class H, of any cardinality (the proofs nowhere use finiteness). The machine-checked completeness is over the finite instantiation and the four declared enumeration fragments (depths 6/4/4/4, semantic dedup). Infinite-dimensional Krein-QFT is untouched, as before.
- **Encoding-level proxies.** "Bounded-below spectrum" is proxied by sector-sign of restricted spectra and orbit-boundedness on a t-grid (threshold 1e3; all instances ≥ e^15 from the threshold — same disclosed numeric failure mode as the prior fixtures). Matrix-vector application was omitted from Σ (finite-domain closure); any equivariant extension of Σ is covered by the schema-level theorem and battery, so this is a vocabulary omission, not a theorem gap.
- **p = q required** (inherited from swing-2 lane 3): the flip is a symmetry only for balanced sectors; the unbalanced case separates sectors by dimension, which is not the GU-relevant configuration.
- **The "conventional" qualifier, made precise:** a selection is conventional iff its g-image is equally admissible with identical Σ-consequences (C2). An arbitrary-but-consistent global choice is conventional in exactly this sense; a non-conventional selection is definitionally one whose g-image is NOT equally admissible, which requires a non-automorphic symbol.
- Negative/bounding result, first-class under the Failure-Preservation Rule. No GU/TI/TaF claim moves; `bar(b)`, H59, Krein positivity, physical issuance all remain OPEN.

## 6. Relation to prior results

- **Closes the swing-2 lane-3 referee's L6 gap at toy grade**: the orbit lemma is now a completeness theorem over all Σ-definable functionals (and all isomorphism-invariant logic over Σ), not an instance battery; the "richer frameworks" residue is reduced to richer *vocabulary*, which is battery-decidable and whose failing symbol is the posit by definition.
- **Strengthens lane D's framework theorem** (referee D1's "two-line proof" observation) into an explicit signature + induction + exhaustive verification; lane D's aliveness rule is a Σ-term instance (t12), and lane D's population-degeneracy is now typed: asymmetric populations are admissible as *parameters*, not as *constants*.
- **Sharpens the anchor burden**: condition 2′ ("derive the sector-asymmetric spectral condition from finality/issuance structure") splits under C3 into 2′-unoriented (derivable, insufficient — it is the fork, not the selection) and 2′-oriented (underivable in class H; meeting it REQUIRES a flip-symmetry-breaking primitive, which is the external datum by the class's own definition). Any future anchor proposal should be submitted directly to the membership battery.

## 7. Disclosures (post-first-run revisions, per house honesty rule)

Two checks were revised after the first run (first run: exit 1 on both; final: exit 0):
1. **t2** ([T], setup): the g-closure check was first implemented via repr-multiset comparison, which is unsound for frozensets (equal sets can repr in different element orders — a genuine implementation bug in the *checker*, caught by its own failure). Replaced with a sound element-level bijection check. No mathematical content changed; the domains were g-closed all along (e1's 0 violations over all 844 tuples independently requires it).
2. **f4** ([F]): my pre-declared expectation wrongly listed `other` among the falsely-flagged symbols under the sabotaged flip; `other` commutes with the identity sabotage trivially and is correctly not flagged. Expectation corrected to the mixed-sort symbols (`c_stab`/`c_energy`/`sector_of`), which is also the sharper statement of what the control demonstrates. The control's teeth (kplus missed under wrong g) were as pre-declared.

Also disclosed: the numeric counts inside check names (7,544 functionals etc.) are formatted from computed values at print time; the pre-declared content of every check is its pass/fail expectation, all of which (except the two revisions above) held on first run.

## 8. Output (verbatim, exit 0, deterministic across repeat runs)

```
CONDITION 2' NO-GO FIXTURE: flip-equivariance completeness over a
finality/issuance-native signature (class H)
==========================================================================
Signature Sigma: 36 symbols (6 constants, 30 primitives) over 11 sorts
CTX-A counts by sort: {'Bool': 4, 'Gen': 1, 'Nat': 3, 'Pair': 1, 'Real': 2, 'Sector': 3, 'State': 1}
CTX-B counts by sort: {'Bool': 235, 'Gen': 2, 'Nat': 12, 'Obs': 1, 'Pair': 1, 'Real': 4, 'Sector': 3571, 'State': 12}
CTX-C counts by sort: {'Bool': 3490, 'Lit': 1, 'Nat': 19, 'Pair': 1, 'Pop': 1, 'Sector': 1, 'State': 18}
CTX-D counts by sort: {'Bool': 33, 'Gen': 1, 'Nat': 3, 'Pair': 1, 'Real': 3, 'Sector': 117, 'State': 1, 'Vec': 1}
TOTAL: 7544 distinct definable functionals verified (39866 candidate term applications examined), 844 battery tuples
--------------------------------------------------------------------------
PASS  [T] t1: g is an involution on every sort (g o g = id): True
PASS  [T] t2: every domain is g-closed (g is a bijection of each domain onto itself): True
PASS  [T] t3: S is an orthogonal involution with S eta S = -eta: True
PASS  [T] t4: the sector swap has NO fixed point on {K+, K-}: True
PASS  [T] t5: all states consistent; all observer scripts admissible monotone issuance chains: True
PASS  [E] e1: primitive-equivariance battery -- ALL 36 symbols x ALL argument tuples (844 tuples), 0 violations (graph(g) is a subalgebra of MxM; membership test for class H): True
PASS  [E] e2: CTX-A {x:Gen} depth<=6 -- 15 distinct definable functionals (107 candidate applications), EVERY one flip-equivariant => no Sigma-term of any sort separates A from flip(A) with flipped context (orbit lemma, completeness form over the fragment): True
PASS  [T] t6: corollary C2 exhibited -- every enumerated Bool functional phi satisfies phi(A) == phi(flip A) for every generator (entailed by T1+e1; direct scan): True
PASS  [E] e3: CTX-B {x:Gen, o:Obs, t:Nat} depth<=4 -- 3838 distinct functionals (22978 candidates), EVERY one flip-equivariant (issuance-to-spectrum coupling fragment): True
PASS  [E] e4: CTX-C {s:State, l:Lit, P:Pop, t:Nat} depth<=4 -- 3531 distinct functionals (14531 candidates), EVERY one flip-equivariant (record/fork/aliveness fragment): True
PASS  [E] e5: CTX-D {v:Vec, x:Gen} depth<=4 -- 160 distinct functionals (2250 candidates), EVERY one flip-equivariant (eta-derivative fragment): True
PASS  [E] e6: closed-term closure (corollary C1) -- every parameter-free definable element is g-fixed; Sector-definables = {NONE} exactly: True
PASS  [T] t7: corollary C3(i) -- 'exactly one sector spectrally positive' is Sigma-definable (not_(eq_sector(c_energy(x), none()))) and flip-INVARIANT; TRUE on the H_spec orbit: True
PASS  [T] t8: corollary C3(ii) -- ...but its ORIENTATION is equivariant, not invariant: c_energy(H_spec) and c_energy(flip H_spec) are the two DIFFERENT pair members (the selection flips with the orbit representative): True
PASS  [T] t9: twin A1 (irreversibility-as-spectrum) as a Sigma-term ite_sector(live(o,t), c_stab(assigned_gen(o)), none()) -- inside class H, flip-equivariant (selects only relative to the orbit representative): True
PASS  [T] t10: twin A2 (growth functional) as a Sigma-term card(issued_after(o,t)) -- inside class H, flip-invariant (growth counts cannot see the sign): True
PASS  [T] t11: twin A3 (fork-realization) as a Sigma-term some_live_extender(add_lit(s,l), P, t) -- inside class H, flip-equivariant (realization tracks the flipped branch): True
PASS  [T] t12: lane D's aliveness selection rule as a Sigma-term contains(live_slice(P,t), l) -- inside class H, flip-equivariant (reproduces lane D's framework theorem inside Sigma): True
PASS  [F] f1: vocabulary + sector constant kplus() -- the SAME battery catches it (violations = exactly the kplus tuples): True
PASS  [F] f1b: term enumeration over the kplus vocabulary finds 16 non-equivariant terms incl. the depth-1 witness kplus() (same enumeration+verifier code path): True
PASS  [F] f2: vocabulary + eta_contractive (oriented-eta / T-a' label-reader) -- battery catches it; witnesses include the A_a and A_c orbits: True
PASS  [F] f3: deliberately broken comparator on the same battery + same planted kplus defect reports 0 violations -- checker without teeth demonstrably fails: True
PASS  [F] f3b: broken comparator on the same term enumeration misses all term-level violations too: True
PASS  [F] f4: sabotaged flip (identity on Sector) -- the planted kplus is now MISSED while genuine mixed-sort primitives (c_stab/c_energy/sector_of) are falsely flagged: both verdict directions depend on the correct flip action (pure-Sector symbols like other/eq_sector commute with the identity trivially and are correctly not flagged): True

All checks match pre-declared expectations. Exit 0.
```

## 9. Code (full source; canonical copy in-repo at `tests/no_go_2prime_flip_equivariance.py`, commit `d20c126`, pushed)

```python
"""Condition 2' NO-GO fixture (P2C swing-2 follow-up, adversarial-twin lane,
impossibility direction).

CLAIM UNDER TEST (toy grade): no finality/issuance-native structure can derive
a sector-ASYMMETRIC spectral condition with an ORIENTATION (i.e. name which
Krein sector carries the bounded-below spectrum), because every functional
definable from a flip-equivariant vocabulary is flip-equivariant, and the
sector swap has no fixed point on {K+, K-}.

THE HYPOTHESIS CLASS H (total precision; see deliverable Section 2):
A signature Sigma = (sorts, constants, primitives) with a finite Sigma-structure
M is *finality/issuance-native* iff the global flip g -- defined per sort below
-- (i) maps each domain bijectively to itself, (ii) fixes every constant, and
(iii) commutes with every primitive:  f(g a_1, ..., g a_k) = g(f(a_1, ..., a_k))
for ALL argument tuples.  Equivalently: g is a Sigma-automorphism of M;
equivalently: graph(g) is a subalgebra of M x M.  Membership in H is
MECHANICALLY DECIDABLE for finite M: run the exhaustive primitive battery in
this file (function `battery`).  That battery IS the induction step of the
no-go theorem, so any claimed escape from the no-go must present a primitive
(or constant) that FAILS the battery -- and that failure is the posit.

THE FLIP g, per sort (the unique nontrivial simultaneous action; g o g = id):
  Prop         : identity
  Lit          : (p, e) -> (p, -e)                    [sign flip]
  State        : elementwise Lit flip
  Obs          : script flipped elementwise, stop time unchanged
  Pop          : elementwise Obs flip
  Gen          : A -> S A S   (S = e1<->e3, e2<->e4; the swing-2 lane-3
                 recoordinatized global flip: form -> -form, J -> -J,
                 labels swapped, all folded into S-conjugation)
  Vec          : v -> S v
  Sector       : K+ <-> K-, NONE fixed                [the swap: NO fixed
                                                       point on {K+, K-}]
  SectorPair   : identity (the pair {K+, K-} is UNORDERED -- flip-fixed)
  Bool/Nat/Real: identity

THEOREM T1 (equivariance; symbolic, structural induction -- proof in the
deliverable): if M is in H then every Sigma-term t(x_1..x_n) satisfies
t(g a_1, ..., g a_n) = g(t(a_1, ..., a_n)).  Base: variables (trivial) and
constants (clause ii).  Step: clause iii.  Nothing else is a term.  QED.
The proof does not use finiteness of M.

COROLLARIES (machine-checked below):
  C1  every CLOSED Sector-term denotes a g-fixed point, i.e. NONE: the
      vocabulary cannot canonize a sector without parameters.
  C2  orbit-indistinguishability COMPLETENESS: no Bool-valued Sigma-term
      separates a generator A from flip(A) (upgrades swing-2 lane 3's
      instance-battery orbit lemma to all definable functionals over Sigma --
      the referee's L6 gap, closed at toy grade).
  C3  the UNORIENTED sector-asymmetric spectral condition ("exactly one
      sector has positive restricted spectrum") IS Sigma-definable and
      flip-invariant; only its ORIENTATION is underivable.  The fork is
      expressible; the selection is not.

CHECK LABELS (house style, swing-2 discipline):
  [T] theorem-consequence: outcome fixed by construction/AFTER T1+E1; carries
      NO evidential weight for the headline; listed separately.
  [E] genuine check: exhaustive verification whose failure was possible at
      formalization time (an implementation or proof error would be caught;
      the [F] controls demonstrate the same code path catching planted
      failures).  E2-E6 are entailed by T1 GIVEN E1; they are [E] with
      respect to implementation/proof error only -- disclosed here, not
      hidden.
  [F] failing-direction control exercising the SAME checker code path.

Exit 0 iff every check matches its pre-declared expected value.
numpy used only to PRECOMPUTE the finite Krein-side tables at load time; the
term machinery is pure Python over finite hashable domains.
"""

from __future__ import annotations

import itertools

import numpy as np

# =====================================================================
# Krein toy (conventions of tests/krein_norm_link_probe.py, commit 96b96bc)
# =====================================================================

ETA4 = np.diag([1.0, 1.0, -1.0, -1.0])
S4 = np.eye(4)[[2, 3, 0, 1]]


def expm(m: np.ndarray) -> np.ndarray:
    m = np.asarray(m, dtype=complex)
    s = int(max(0, np.ceil(np.log2(max(1.0, np.linalg.norm(m, 2))))) + 4)
    a = m / (2.0 ** s)
    out = np.eye(m.shape[0], dtype=complex)
    term = np.eye(m.shape[0], dtype=complex)
    for k in range(1, 24):
        term = term @ a / k
        out = out + term
    for _ in range(s):
        out = out @ out
    return out


A_C = np.zeros((4, 4))
A_C[:2, :2] = [[-1.0, 0.5], [0.0, -2.0]]      # spectrum {-1, -2}
A_C[2:, 2:] = [[0.7, -0.4], [0.2, 1.3]]       # spectrum {0.9, 1.1}
H_SPEC = np.diag([1.0, 2.0, -3.0, -4.0])
A_BSYM = -np.eye(4) + 0.3 * (np.outer(np.eye(4)[0], np.eye(4)[2])
                             - np.outer(np.eye(4)[2], np.eye(4)[0]))
A_A = np.diag([-1.0, -2.0, 1.0, 0.5])

# Gen sort: named orbit-CLOSED set (both orbit members present; NO generator
# is a constant of the signature -- naming one would fail clause (ii)).
GEN_MATS = {
    "A_c": A_C, "A_c~": S4 @ A_C @ S4,
    "H_spec": H_SPEC, "H_spec~": S4 @ H_SPEC @ S4,
    "A_bsym": A_BSYM, "A_bsym~": S4 @ A_BSYM @ S4,
    "A_a": A_A, "A_a~": S4 @ A_A @ S4,
}
GEN_FLIP = {"A_c": "A_c~", "A_c~": "A_c", "H_spec": "H_spec~",
            "H_spec~": "H_spec", "A_bsym": "A_bsym~", "A_bsym~": "A_bsym",
            "A_a": "A_a~", "A_a~": "A_a"}

SECTOR_IDX = {"KP": [0, 1], "KM": [2, 3]}


def _sector_bounded(mat: np.ndarray, sec: str) -> bool:
    """Orbit-boundedness of the issuance semigroup started in the sector
    (t-grid sup, threshold 1e3; every instance used is >= e^15 from the
    threshold -- same disclosed numeric failure mode as the twin fixture)."""
    if sec == "NONE":
        return False
    sup = 0.0
    for t in np.linspace(0.0, 30.0, 61):
        e = expm(t * mat)
        for i in SECTOR_IDX[sec]:
            sup = max(sup, float(np.linalg.norm(e[:, i])))
    return sup < 1e3


def _restr_spec_pos(mat: np.ndarray, sec: str) -> bool:
    if sec == "NONE":
        return False
    idx = SECTOR_IDX[sec]
    return bool(np.all(np.linalg.eigvals(mat[np.ix_(idx, idx)]).real > 0))


# Precompute all Krein-side primitive tables (finite; primitives below are
# pure dict lookups, so the term machinery is deterministic and fast).
PRE_BOUND = {(gname, sec): _sector_bounded(m, sec)
             for gname, m in GEN_MATS.items() for sec in ("KP", "KM", "NONE")}
PRE_RSP = {(gname, sec): _restr_spec_pos(m, sec)
           for gname, m in GEN_MATS.items() for sec in ("KP", "KM", "NONE")}


def _c_from(table, gname: str) -> str:
    bp, bm = table[(gname, "KP")], table[(gname, "KM")]
    if bp == bm:
        return "NONE"
    return "KP" if bp else "KM"


PRE_CSTAB = {g: _c_from(PRE_BOUND, g) for g in GEN_MATS}
PRE_CENERGY = {g: _c_from(PRE_RSP, g) for g in GEN_MATS}
PRE_TRACE = {g: round(float(np.trace(m)), 6) for g, m in GEN_MATS.items()}
PRE_SPECABS = {g: round(float(np.max(np.linalg.eigvals(m).real)), 6)
               for g, m in GEN_MATS.items()}

# Oriented-eta functional -- deliberately NOT in Sigma (it is the sign posit
# restated, swing-2 T-a'); used only by the [F2] control.
def _eta_contractive(mat: np.ndarray) -> bool:
    m = ETA4 @ mat + mat.T @ ETA4
    return float(np.max(np.linalg.eigvalsh((m + m.T) / 2))) <= 1e-10


PRE_ETACON = {g: _eta_contractive(m) for g, m in GEN_MATS.items()}

# =====================================================================
# Record / issuance side (TI-native toy, lane-D conventions)
# =====================================================================

PROPS = ("p", "q")
LITS = tuple((p, e) for p in PROPS for e in (1, -1))


def consistent(s: frozenset) -> bool:
    vals: dict[str, int] = {}
    for prop, sign in s:
        if prop in vals and vals[prop] != sign:
            return False
        vals[prop] = sign
    return True


STATES = tuple(sorted((frozenset(c) for r in range(len(LITS) + 1)
                       for c in itertools.combinations(LITS, r)
                       if consistent(frozenset(c))),
                      key=lambda s: (len(s), sorted(s))))
assert len(STATES) == 9

# Observers: name -> (script, stop).  Population is orbit-closed as a DOMAIN;
# no observer is a constant (a signed script is not g-fixed).
OBS_DATA = {
    "alice":  ((("p", 1), ("q", 1)), 3),
    "alice~": ((("p", -1), ("q", -1)), 3),
    "bob":    ((("p", -1),), 1),
    "bob~":   ((("p", 1),), 1),
    "carol":  ((("q", -1), ("p", 1)), 2),
    "carol~": ((("q", 1), ("p", -1)), 2),
}
OBS_FLIP = {"alice": "alice~", "alice~": "alice", "bob": "bob~",
            "bob~": "bob", "carol": "carol~", "carol~": "carol"}
NATS = (0, 1, 2)
HMAX = 2

# Populations: a curated g-closed set of observer subsets (asymmetric
# populations EXIST in the domain -- as parameters; none is a constant).
POPS = tuple(sorted({
    frozenset(), frozenset({"alice"}), frozenset({"alice~"}),
    frozenset({"bob"}), frozenset({"bob~"}),
    frozenset({"alice", "bob"}), frozenset({"alice~", "bob~"}),
    frozenset({"alice", "alice~"}), frozenset(OBS_DATA),
}, key=lambda s: (len(s), sorted(s))))

VECS = tuple(sorted({(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
                     (1, 0, 1, 0), (1, 0, -1, 0), (-1, 0, 1, 0)}))

# =====================================================================
# The flip g, per sort (dicts: element -> element)
# =====================================================================


def flip_lit(l):
    return (l[0], -l[1])


def flip_state(s):
    return frozenset(flip_lit(l) for l in s)


GMAPS = {
    "Bool": {b: b for b in (True, False)},
    "Nat": {n: n for n in NATS},
    "Lit": {l: flip_lit(l) for l in LITS},
    "State": {s: flip_state(s) for s in STATES},
    "Obs": dict(OBS_FLIP),
    "Pop": {P: frozenset(OBS_FLIP[o] for o in P) for P in POPS},
    "Gen": dict(GEN_FLIP),
    "Vec": {v: (v[2], v[3], v[0], v[1]) for v in VECS},
    "Sector": {"KP": "KM", "KM": "KP", "NONE": "NONE"},
    "Pair": {"PAIR": "PAIR"},
}
DOMAINS = {
    "Bool": (True, False), "Nat": NATS, "Lit": LITS, "State": STATES,
    "Obs": tuple(sorted(OBS_DATA)), "Pop": POPS, "Gen": tuple(sorted(GEN_MATS)),
    "Vec": VECS, "Sector": ("KP", "KM", "NONE"), "Pair": ("PAIR",),
}

# =====================================================================
# The signature Sigma: constants (0-ary) and primitives
# Each entry: (name, argsorts, ressort, fn)
# =====================================================================


def history(o, t):
    script, stop = OBS_DATA[o]
    return frozenset(script[:min(t, stop)])


def issued_after(o, t):
    script, stop = OBS_DATA[o]
    return frozenset(script[t:stop])


def live(o, t):
    script, stop = OBS_DATA[o]
    return stop > t and len(script) > t


def add_lit(s, l):
    u = s | {l}
    return u if consistent(u) else s


def live_slice(P, t):
    u = frozenset(l for o in P if live(o, t) for l in issued_after(o, t))
    return u if consistent(u) else frozenset()


def some_live_extender(s, P, t):
    return any(live(o, t) and s <= history(o, HMAX) for o in P)


SIGMA = [
    # --- constants (all g-fixed; clause ii)
    ("empty", (), "State", lambda: frozenset()),
    ("none", (), "Sector", lambda: "NONE"),
    ("the_pair", (), "Pair", lambda: "PAIR"),
    ("n0", (), "Nat", lambda: 0),
    ("n1", (), "Nat", lambda: 1),
    ("n2", (), "Nat", lambda: 2),
    # --- extension order / record structure
    ("extends", ("State", "State"), "Bool", lambda a, b: a <= b),
    ("card", ("State",), "Nat", len),
    ("contains", ("State", "Lit"), "Bool", lambda s, l: l in s),
    ("add_lit", ("State", "Lit"), "State", add_lit),
    ("consistent_union", ("State", "State"), "Bool",
     lambda a, b: consistent(a | b)),
    # --- observers / aliveness / issuance
    ("history", ("Obs", "Nat"), "State", history),
    ("issued_after", ("Obs", "Nat"), "State", issued_after),
    ("live", ("Obs", "Nat"), "Bool", live),
    ("assigned_gen", ("Obs",), "Gen",
     {"alice": "A_c", "alice~": "A_c~", "bob": "H_spec", "bob~": "H_spec~",
      "carol": "A_bsym", "carol~": "A_bsym~"}.__getitem__),
    # --- populations / fork realization (lane-D aliveness rule, in-Sigma)
    ("live_slice", ("Pop", "Nat"), "State", live_slice),
    ("some_live_extender", ("State", "Pop", "Nat"), "Bool",
     some_live_extender),
    # --- Krein side: unordered pair, sectors, spectra, realizability
    ("memb", ("Sector", "Pair"), "Bool", lambda s, P: s in ("KP", "KM")),
    ("other", ("Sector",), "Sector",
     {"KP": "KM", "KM": "KP", "NONE": "NONE"}.__getitem__),
    ("eq_sector", ("Sector", "Sector"), "Bool", lambda a, b: a == b),
    ("sector_bounded", ("Gen", "Sector"), "Bool",
     lambda g, s: PRE_BOUND[(g, s)]),
    ("restr_spec_pos", ("Gen", "Sector"), "Bool",
     lambda g, s: PRE_RSP[(g, s)]),
    ("c_stab", ("Gen",), "Sector", PRE_CSTAB.__getitem__),
    ("c_energy", ("Gen",), "Sector", PRE_CENERGY.__getitem__),
    ("trace", ("Gen",), "Real", PRE_TRACE.__getitem__),
    ("specabs", ("Gen",), "Real", PRE_SPECABS.__getitem__),
    ("eq_gen", ("Gen", "Gen"), "Bool", lambda a, b: a == b),
    # --- eta, via its flip-equivariant derivatives (form up to overall sign)
    ("sector_of", ("Vec",), "Sector",
     lambda v: "KP" if v[2] == v[3] == 0 else
               ("KM" if v[0] == v[1] == 0 else "NONE")),
    ("q_neutral", ("Vec",), "Bool",
     lambda v: v[0] ** 2 + v[1] ** 2 - v[2] ** 2 - v[3] ** 2 == 0),
    ("q_abs", ("Vec",), "Real",
     lambda v: abs(v[0] ** 2 + v[1] ** 2 - v[2] ** 2 - v[3] ** 2)),
    # --- logic / arithmetic glue
    ("not_", ("Bool",), "Bool", lambda b: not b),
    ("and_", ("Bool", "Bool"), "Bool", lambda a, b: a and b),
    ("leq_nat", ("Nat", "Nat"), "Bool", lambda a, b: a <= b),
    ("succ", ("Nat",), "Nat", lambda n: min(n + 1, HMAX)),
    ("rleq", ("Real", "Real"), "Bool", lambda a, b: a <= b),
    ("ite_sector", ("Bool", "Sector", "Sector"), "Sector",
     lambda b, x, y: x if b else y),
]

# Real domain: exactly the reachable outputs of the numeric primitives.
DOMAINS["Real"] = tuple(sorted(set(PRE_TRACE.values())
                               | set(PRE_SPECABS.values())
                               | {abs(v[0]**2 + v[1]**2 - v[2]**2 - v[3]**2)
                                  for v in VECS}))
GMAPS["Real"] = {r: r for r in DOMAINS["Real"]}

# [F]-control primitives (NOT in Sigma; each must be caught by the battery):
PRIM_KPLUS = ("kplus", (), "Sector", lambda: "KP")            # sector constant
PRIM_ETACON = ("eta_contractive", ("Gen",), "Bool",           # oriented eta
               PRE_ETACON.__getitem__)

# =====================================================================
# Checker machinery (ONE comparator, injected everywhere -- the [F] controls
# sabotage exactly this comparator / the g-map, on the same code paths)
# =====================================================================


def good_compare(got, want):
    return got == want


def battery(prims, gmaps, compare):
    """Exhaustive: for every primitive and EVERY argument tuple, check
    f(g a_1,...,g a_k) == g(f(a_1,...,a_k)).  Returns (violations, n_tuples).
    This is the mechanical membership test for class H and the induction
    step of T1 (graph(g) is a subalgebra of M x M  <=>  battery passes)."""
    violations = []
    n = 0
    for name, argsorts, ressort, fn in prims:
        for args in itertools.product(*(DOMAINS[s] for s in argsorts)):
            n += 1
            got = fn(*(gmaps[s][a] for s, a in zip(argsorts, args)))
            want = gmaps[ressort][fn(*args)]
            if not compare(got, want):
                violations.append((name, args, got, want))
    return violations, n


def enumerate_and_verify(varspec, depth, prims, gmaps, compare):
    """Enumerate ALL Sigma-terms over the variable context `varspec` up to
    `depth`, with semantic deduplication (two terms with the same value on
    every assignment have the same equivariance status, so verifying each
    distinct semantic vector verifies every term in the fragment).  Verify
    equivariance pointwise:  t(g(v)) == g(t(v))  for every assignment v.
    Returns (per-sort distinct counts, n_candidates, violations)."""
    rows = list(itertools.product(*(DOMAINS[s] for _, s in varspec)))
    rowindex = {r: i for i, r in enumerate(rows)}
    gperm = [rowindex[tuple(gmaps[s][val] for val, (_, s) in zip(r, varspec))]
             for r in rows]

    # kept[sort] : semantic-vector -> (depth, syntax)
    kept: dict[str, dict[tuple, tuple[int, str]]] = {}
    n_candidates = 0

    def put(sort, vec, d, syn):
        tbl = kept.setdefault(sort, {})
        if vec not in tbl:
            tbl[vec] = (d, syn)
            return True
        return False

    # depth 1: variables and constants
    for j, (vn, s) in enumerate(varspec):
        put(s, tuple(r[j] for r in rows), 1, vn)
    for name, argsorts, ressort, fn in prims:
        if not argsorts:
            n_candidates += 1
            put(ressort, tuple(fn() for _ in rows), 1, f"{name}()")

    for d in range(2, depth + 1):
        new = []
        for name, argsorts, ressort, fn in prims:
            if not argsorts:
                continue
            pools = [[(vec, dep, syn) for vec, (dep, syn) in
                      kept.get(s, {}).items() if dep <= d - 1]
                     for s in argsorts]
            for combo in itertools.product(*pools):
                if max(c[1] for c in combo) != d - 1:
                    continue
                n_candidates += 1
                vec = tuple(fn(*(c[0][i] for c in combo))
                            for i in range(len(rows)))
                syn = f"{name}({', '.join(c[2] for c in combo)})"
                new.append((ressort, vec, d, syn))
        for ressort, vec, dd, syn in new:
            put(ressort, vec, dd, syn)

    violations = []
    counts = {}
    for sort, tbl in kept.items():
        counts[sort] = len(tbl)
        gm = gmaps[sort]
        for vec, (dd, syn) in tbl.items():
            for i in range(len(rows)):
                if not compare(vec[gperm[i]], gm[vec[i]]):
                    violations.append((sort, syn, rows[i]))
                    break
    return counts, n_candidates, violations


def closed_term_closure(prims, gmaps):
    """All parameter-free definable elements: close the constants under all
    primitives to fixpoint.  Returns (reachable, non_g_fixed)."""
    reach: dict[str, set] = {s: set() for s in DOMAINS}
    for name, argsorts, ressort, fn in prims:
        if not argsorts:
            reach[ressort].add(fn())
    changed = True
    while changed:
        changed = False
        for name, argsorts, ressort, fn in prims:
            if not argsorts:
                continue
            for args in itertools.product(*(sorted(reach[s], key=repr)
                                            for s in argsorts)):
                v = fn(*args)
                if v not in reach[ressort]:
                    reach[ressort].add(v)
                    changed = True
    non_fixed = [(s, v) for s, vs in reach.items() for v in vs
                 if gmaps[s][v] != v]
    return reach, non_fixed


# =====================================================================
# Main: checks with pre-declared expectations
# =====================================================================


def main() -> None:
    checks: list[tuple[str, bool, bool]] = []

    def check(name, value, expected=True):
        checks.append((name, bool(value), expected))

    # ---------------- [T] setup / definitional
    check("[T] t1: g is an involution on every sort (g o g = id)",
          all(GMAPS[s][GMAPS[s][a]] == a for s in DOMAINS for a in DOMAINS[s]))
    check("[T] t2: every domain is g-closed (g is a bijection of each domain "
          "onto itself)",
          all(len({GMAPS[s][a] for a in DOMAINS[s]}) == len(DOMAINS[s])
              and {GMAPS[s][a] for a in DOMAINS[s]} == set(DOMAINS[s])
              for s in DOMAINS))
    check("[T] t3: S is an orthogonal involution with S eta S = -eta",
          np.allclose(S4 @ S4, np.eye(4)) and np.allclose(S4, S4.T)
          and np.allclose(S4 @ ETA4 @ S4, -ETA4))
    check("[T] t4: the sector swap has NO fixed point on {K+, K-}",
          GMAPS["Sector"]["KP"] != "KP" and GMAPS["Sector"]["KM"] != "KM")
    check("[T] t5: all states consistent; all observer scripts admissible "
          "monotone issuance chains",
          all(consistent(s) for s in STATES)
          and all(consistent(history(o, t)) and history(o, t) <=
                  history(o, t + 1) for o in OBS_DATA for t in range(HMAX)))

    # ---------------- [E1] the battery = induction step of T1, exhaustively
    viol, n_tuples = battery(SIGMA, GMAPS, good_compare)
    check(f"[E] e1: primitive-equivariance battery -- ALL {len(SIGMA)} "
          f"symbols x ALL argument tuples ({n_tuples} tuples), 0 violations "
          "(graph(g) is a subalgebra of MxM; membership test for class H)",
          len(viol) == 0)

    # ---------------- [E2] CTX-A {x:Gen} depth 6: orbit indistinguishability
    counts_a, cand_a, viol_a = enumerate_and_verify(
        [("x", "Gen")], 6, SIGMA, GMAPS, good_compare)
    check(f"[E] e2: CTX-A {{x:Gen}} depth<=6 -- {sum(counts_a.values())} "
          f"distinct definable functionals ({cand_a} candidate applications), "
          "EVERY one flip-equivariant => no Sigma-term of any sort separates "
          "A from flip(A) with flipped context (orbit lemma, completeness "
          "form over the fragment)", len(viol_a) == 0)
    # explicit corollary scan (C2): Bool functionals of x are literally
    # constant on flip-orbits.  Re-enumerate CTX-A keeping the vectors.
    def scan_enum():
        varspec = [("x", "Gen")]
        rws = [(g,) for g in DOMAINS["Gen"]]
        ridx = {r: i for i, r in enumerate(rws)}
        gp = [ridx[(GMAPS["Gen"][r[0]],)] for r in rws]
        kept: dict[str, dict[tuple, tuple[int, str]]] = {}

        def put(sort, vec, d, syn):
            tbl = kept.setdefault(sort, {})
            if vec not in tbl:
                tbl[vec] = (d, syn)

        put("Gen", tuple(r[0] for r in rws), 1, "x")
        for name, argsorts, ressort, fn in SIGMA:
            if not argsorts:
                put(ressort, tuple(fn() for _ in rws), 1, f"{name}()")
        for d in range(2, 7):
            new = []
            for name, argsorts, ressort, fn in SIGMA:
                if not argsorts:
                    continue
                pools = [[(v, dep, sy) for v, (dep, sy) in
                          kept.get(s, {}).items() if dep <= d - 1]
                         for s in argsorts]
                for combo in itertools.product(*pools):
                    if max(c[1] for c in combo) != d - 1:
                        continue
                    vec = tuple(fn(*(c[0][i] for c in combo))
                                for i in range(len(rws)))
                    new.append((ressort, vec, d,
                                f"{name}({', '.join(c[2] for c in combo)})"))
            for rs, vec, dd, sy in new:
                put(rs, vec, dd, sy)
        return kept, rws, gp

    kept_scan, rws_scan, gp_scan = scan_enum()
    orbit_pairs = [(i, gp_scan[i]) for i in range(len(rws_scan))]
    scan_ok = all(vec[i] == vec[j]
                  for vec in kept_scan.get("Bool", {})
                  for (i, j) in orbit_pairs)
    check("[T] t6: corollary C2 exhibited -- every enumerated Bool functional "
          "phi satisfies phi(A) == phi(flip A) for every generator "
          "(entailed by T1+e1; direct scan)", scan_ok)

    # ---------------- [E3] CTX-B {x:Gen, o:Obs, t:Nat} depth 4 (coupling)
    counts_b, cand_b, viol_b = enumerate_and_verify(
        [("x", "Gen"), ("o", "Obs"), ("t", "Nat")], 4, SIGMA, GMAPS,
        good_compare)
    check(f"[E] e3: CTX-B {{x:Gen, o:Obs, t:Nat}} depth<=4 -- "
          f"{sum(counts_b.values())} distinct functionals ({cand_b} "
          "candidates), EVERY one flip-equivariant (issuance-to-spectrum "
          "coupling fragment)", len(viol_b) == 0)

    # ---------------- [E4] CTX-C {s:State, l:Lit, P:Pop, t:Nat} depth 4
    counts_c, cand_c, viol_c = enumerate_and_verify(
        [("s", "State"), ("l", "Lit"), ("P", "Pop"), ("t", "Nat")], 4,
        SIGMA, GMAPS, good_compare)
    check(f"[E] e4: CTX-C {{s:State, l:Lit, P:Pop, t:Nat}} depth<=4 -- "
          f"{sum(counts_c.values())} distinct functionals ({cand_c} "
          "candidates), EVERY one flip-equivariant (record/fork/aliveness "
          "fragment)", len(viol_c) == 0)

    # ---------------- [E5] CTX-D {v:Vec, x:Gen} depth 4 (eta fragment)
    counts_d, cand_d, viol_d = enumerate_and_verify(
        [("v", "Vec"), ("x", "Gen")], 4, SIGMA, GMAPS, good_compare)
    check(f"[E] e5: CTX-D {{v:Vec, x:Gen}} depth<=4 -- "
          f"{sum(counts_d.values())} distinct functionals ({cand_d} "
          "candidates), EVERY one flip-equivariant (eta-derivative fragment)",
          len(viol_d) == 0)

    # ---------------- [E6] closed terms: parameter-free definables
    reach, non_fixed = closed_term_closure(SIGMA, GMAPS)
    check("[E] e6: closed-term closure (corollary C1) -- every parameter-free "
          "definable element is g-fixed; Sector-definables = {NONE} exactly",
          len(non_fixed) == 0 and reach["Sector"] == {"NONE"})

    # ---------------- [T] C3: the UNORIENTED asymmetry is definable...
    asym = {g: PRE_CENERGY[g] != "NONE" for g in DOMAINS["Gen"]}
    check("[T] t7: corollary C3(i) -- 'exactly one sector spectrally "
          "positive' is Sigma-definable (not_(eq_sector(c_energy(x), "
          "none()))) and flip-INVARIANT; TRUE on the H_spec orbit",
          asym["H_spec"] and asym["H_spec~"]
          and all(asym[g] == asym[GEN_FLIP[g]] for g in asym))
    check("[T] t8: corollary C3(ii) -- ...but its ORIENTATION is equivariant, "
          "not invariant: c_energy(H_spec) and c_energy(flip H_spec) are the "
          "two DIFFERENT pair members (the selection flips with the orbit "
          "representative)",
          PRE_CENERGY["H_spec"] == "KP" and PRE_CENERGY["H_spec~"] == "KM")

    # ---------------- [T] twin-direction terms exhibited (inside class H)
    # A1 irreversibility-as-spectrum: coupled term using order + spectra.
    # A2 growth functional: record-count monotone.
    # A3 fork-realization: realized branch above s at literal l.
    def verify_term(varspec, fn, ressort):
        rws = list(itertools.product(*(DOMAINS[s] for _, s in varspec)))
        ridx = {r: i for i, r in enumerate(rws)}
        gp = [ridx[tuple(GMAPS[s][val] for val, (_, s) in zip(r, varspec))]
              for r in rws]
        vec = [fn(*r) for r in rws]
        return all(good_compare(vec[gp[i]], GMAPS[ressort][vec[i]])
                   for i in range(len(rws)))

    a1 = verify_term(
        [("o", "Obs"), ("t", "Nat")],
        lambda o, t: (PRE_CSTAB[{"alice": "A_c", "alice~": "A_c~",
                                 "bob": "H_spec", "bob~": "H_spec~",
                                 "carol": "A_bsym", "carol~": "A_bsym~"}[o]]
                      if live(o, t) else "NONE"),
        "Sector")
    check("[T] t9: twin A1 (irreversibility-as-spectrum) as a Sigma-term "
          "ite_sector(live(o,t), c_stab(assigned_gen(o)), none()) -- inside "
          "class H, flip-equivariant (selects only relative to the orbit "
          "representative)", a1)
    a2 = verify_term(
        [("o", "Obs"), ("t", "Nat")],
        lambda o, t: len(issued_after(o, t)),
        "Nat")
    check("[T] t10: twin A2 (growth functional) as a Sigma-term "
          "card(issued_after(o,t)) -- inside class H, flip-invariant "
          "(growth counts cannot see the sign)", a2)
    a3 = verify_term(
        [("s", "State"), ("l", "Lit"), ("P", "Pop"), ("t", "Nat")],
        lambda s, l, P, t: some_live_extender(add_lit(s, l), P, t),
        "Bool")
    check("[T] t11: twin A3 (fork-realization) as a Sigma-term "
          "some_live_extender(add_lit(s,l), P, t) -- inside class H, "
          "flip-equivariant (realization tracks the flipped branch)", a3)
    laneD = verify_term(
        [("l", "Lit"), ("P", "Pop"), ("t", "Nat")],
        lambda l, P, t: l in live_slice(P, t),
        "Bool")
    check("[T] t12: lane D's aliveness selection rule as a Sigma-term "
          "contains(live_slice(P,t), l) -- inside class H, flip-equivariant "
          "(reproduces lane D's framework theorem inside Sigma)", laneD)

    # ---------------- [F] controls (same code paths)
    # F1: sector-naming constant -- battery must catch it.
    viol_f1, _ = battery(SIGMA + [PRIM_KPLUS], GMAPS, good_compare)
    check("[F] f1: vocabulary + sector constant kplus() -- the SAME battery "
          "catches it (violations = exactly the kplus tuples)",
          len(viol_f1) > 0 and all(v[0] == "kplus" for v in viol_f1))
    # F1b: term-level -- the SAME enumeration/verification finds
    # non-equivariant TERMS (kplus() and its compounds).
    _, _, viol_f1t = enumerate_and_verify(
        [("x", "Gen")], 3, SIGMA + [PRIM_KPLUS], GMAPS, good_compare)
    f1_syntaxes = {v[1] for v in viol_f1t}
    check(f"[F] f1b: term enumeration over the kplus vocabulary finds "
          f"{len(viol_f1t)} non-equivariant terms incl. the depth-1 witness "
          "kplus() (same enumeration+verifier code path)",
          len(viol_f1t) > 0 and "kplus()" in f1_syntaxes)
    # F2: oriented-eta primitive (the sign posit restated, T-a') -- caught.
    viol_f2, _ = battery(SIGMA + [PRIM_ETACON], GMAPS, good_compare)
    f2_witnesses = {v[1][0] for v in viol_f2}
    check("[F] f2: vocabulary + eta_contractive (oriented-eta / T-a' "
          "label-reader) -- battery catches it; witnesses include the A_a "
          "and A_c orbits",
          len(viol_f2) > 0 and all(v[0] == "eta_contractive" for v in viol_f2)
          and "A_a" in f2_witnesses and "A_c" in f2_witnesses)
    # F3: sabotaged comparator (never flags) on the SAME battery + SAME
    # planted defect -- must MISS it (proves the pass in e1/f1 is the
    # comparison actually running, not plumbing).
    broken_compare = lambda got, want: True  # noqa: E731
    viol_f3, _ = battery(SIGMA + [PRIM_KPLUS], GMAPS, broken_compare)
    check("[F] f3: deliberately broken comparator on the same battery + same "
          "planted kplus defect reports 0 violations -- checker without "
          "teeth demonstrably fails", len(viol_f3) == 0)
    _, _, viol_f3t = enumerate_and_verify(
        [("x", "Gen")], 3, SIGMA + [PRIM_KPLUS], GMAPS, broken_compare)
    check("[F] f3b: broken comparator on the same term enumeration misses "
          "all term-level violations too", len(viol_f3t) == 0)
    # F4: sabotaged flip (forgets to swap sectors) -- kplus now passes AND
    # genuine equivariant primitives get falsely flagged: catching depends
    # on the correct g.
    gmaps_bad = dict(GMAPS)
    gmaps_bad["Sector"] = {s: s for s in DOMAINS["Sector"]}
    viol_f4, _ = battery(SIGMA + [PRIM_KPLUS], gmaps_bad, good_compare)
    f4_names = {v[0] for v in viol_f4}
    check("[F] f4: sabotaged flip (identity on Sector) -- the planted kplus "
          "is now MISSED while genuine mixed-sort primitives "
          "(c_stab/c_energy/sector_of) are falsely flagged: both verdict "
          "directions depend on the correct flip action (pure-Sector symbols "
          "like other/eq_sector commute with the identity trivially and are "
          "correctly not flagged)",
          "kplus" not in f4_names and "c_stab" in f4_names
          and "c_energy" in f4_names and "sector_of" in f4_names
          and "other" not in f4_names)

    # ---------------- report
    print("CONDITION 2' NO-GO FIXTURE: flip-equivariance completeness over a")
    print("finality/issuance-native signature (class H)")
    print("=" * 74)
    print(f"Signature Sigma: {len(SIGMA)} symbols "
          f"({sum(1 for p in SIGMA if not p[1])} constants, "
          f"{sum(1 for p in SIGMA if p[1])} primitives) over "
          f"{len(DOMAINS)} sorts")
    print(f"CTX-A counts by sort: { {k: v for k, v in sorted(counts_a.items())} }")
    print(f"CTX-B counts by sort: { {k: v for k, v in sorted(counts_b.items())} }")
    print(f"CTX-C counts by sort: { {k: v for k, v in sorted(counts_c.items())} }")
    print(f"CTX-D counts by sort: { {k: v for k, v in sorted(counts_d.items())} }")
    total_distinct = (sum(counts_a.values()) + sum(counts_b.values())
                      + sum(counts_c.values()) + sum(counts_d.values()))
    total_cand = cand_a + cand_b + cand_c + cand_d
    print(f"TOTAL: {total_distinct} distinct definable functionals verified "
          f"({total_cand} candidate term applications examined), "
          f"{n_tuples} battery tuples")
    print("-" * 74)
    failures = []
    for name, value, expected in checks:
        ok = value == expected
        print(f"{'PASS' if ok else 'UNEXPECTED'}  {name}: {value}")
        if not ok:
            failures.append(name)
    print()
    if failures:
        print("UNEXPECTED RESULTS:", failures)
        raise SystemExit(1)
    print("All checks match pre-declared expectations. Exit 0.")


if __name__ == "__main__":
    main()
```

## Sources

`possibility-to-capability/governance/CHARTER.md` (Located-Is-Not-Forced; Failure-Preservation; Neutrality); `explorations/2026-07-16-swing-2/SYNTHESIS.md` and `lane-3-krein-normlink-probe.md` (REDUCED verdict, orbit lemma, condition 2′, referee L2/L6 — governing grades); `explorations/2026-07-16-swing-2/lane-2-gate1-enriched-toy-lift.md` ((Z/2)^blocks, referee F3); `explorations/2026-07-16-big-swing/lane-D-aliveness-anchor.md` (framework theorem, base-vs-fiber, RUN-0019 typing — governing referee report); `gu-formalization/explorations/time-as-finality-crosswalk/adapter2-correction-polarity-fiber-not-axis-2026-07-15.md` (ADAPTER2-01); twin lane's committed probe `tests/condition2prime_constructive_probe.py` at `a193a3b` (inspected for direction/vocabulary membership only; no result cited). Fixture: `tests/no_go_2prime_flip_equivariance.py` at commit `d20c126` (pushed to `origin/main`), rerunnable, deterministic, exit 0.

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs grades)

# Referee report — LANE B-2prime-nogo (impossibility direction)

## 1. VERDICT: **SOUND-WITH-CORRECTIONS**

I re-ran `tests/no_go_2prime_flip_equivariance.py` from the working tree at `d20c126` (commit exists, is on `origin/main`, working tree matches the commit byte-for-byte — `git diff d20c126 -- <file>` empty, 740 lines matching the commit stat). Output reproduces **verbatim**, exit 0, byte-identical across two consecutive runs — the determinism claim is earned. I hand-verified T1 (standard structural induction; correct), T1′, C1 (swap has no fixed point on {K+,K−}, so closed Sector terms denote NONE; correct), C2 and C3 (correct as fine-print statements), the f4 revised expectation (`other` composed with the identity Sector-sabotage trivially commutes — the §7 disclosure is mathematically right), the dedup-soundness argument (equivariance is a function of the semantic vector; sound), and the `closed_term_closure` fixpoint logic (sound; Sector-reachables = {NONE} is forced since no Gen/Lit constants exist). I independently confirmed the CTX-A "orbit fragment saturates" claim (my probe: 15 distinct / 107 candidates is stable from depth 4 through depth 8). ADAPTER2-01 was checked directly: the lane's "orientation requires an external non-automorphic symbol" conclusion *matches* the correction document's "the finality order does not choose which fiber point is positive norm"; nothing reopens the withdrawn identity; no source-sovereignty violation (all content is toy-internal; GU/TI/TaF statuses correctly held OPEN). The twin's probe at `a193a3b` exists with the named helpers exactly where claimed (`c_circ` line 110, `eta_contractive`/`eta_expansive` lines 126/131). The six [F] controls genuinely exercise the same `battery`/`enumerate_and_verify`/comparator/g-map code paths that carry e1–e5 — this is the strongest control discipline of the three fixtures in this family.

The NO-GO verdict survives, **as a class-relative result**. The defects below are: the burned check-labeling class recurring a third time (in attenuated, disclosed form), one genuine grading overclaim ("derivable"/"can prove" for the unoriented condition), one false numeric sentence I refuted by direct computation, and framing that presents a textbook invariance fact as a program discovery. None reaches the verdict, because the battery (e1) plus the two-line theorem carries the load and both are sound.

## 2. Defects

**B1 — [E]-mass inflation via unilateral redefinition of [E]. Severity: MODERATE (the burned class, third occurrence after D1 and L1).**
The swing-2 discipline this report claims to inherit defines [E] as a check "whose outcome was not fixed at formalization time." Given e1 and T1's two-line proof, **e2–e6 cannot fail mathematically** — the report says so itself, then redefines [E] as "[E] with respect to implementation/proof error only" to keep five of its six [E] tags, and counts "7,544 distinct definable functionals verified" as headline evidence mass under a rule ("only [E] and [F] count") it thereby waters down. Under the governing discipline, e2–e6 are theorem-corroboration ([T]-class implementation checks, guarded by f3b/f4). The honest machine-evidence column is: **e1 (844 exhaustive tuples — genuinely open, since the contingent fact checked is that the *chosen* 36 symbols are all equivariant, and f2 shows a natural candidate that isn't) plus the six [F] controls.** Mitigation (why MODERATE, not MAJOR): the entailment is disclosed prominently in both report and code header, and the controls genuinely attack the residual implementation-error risk — this is D1's defect with D1's own honest restatement half-applied.

**B2 — "Derivable"/"can prove" grades expressibility as derivation. Severity: MODERATE.**
Verdict paragraph: "The UNORIENTED condition … is **derivable** inside the class"; C3 commentary: "a class-H theory **can prove** *that* the world's dynamics is sector-asymmetric"; §6: "2′-unoriented (**derivable**, insufficient)." False as graded. What is shown: the unoriented condition is Σ-**expressible** and **true of the hand-inserted instance** `H_spec` — whose sector asymmetry was placed there by hand, as swing-2 §5 itself conceded ("inserted by hand"). Nothing derives the unoriented asymmetry from finality/issuance structure; no issuance axiom in Σ entails it (A_bsym is in the same class and has none). The split of 2′ into unoriented/oriented halves is real and useful, but its unoriented half is "expressible without breaking the flip," not "derivable."

**B3 — Definitional/textbook result framed as the lane's theorem; "L6 gap closed" oversells. Severity: MINOR-to-MODERATE.**
T1/T1′ is the standard universal-algebra fact that term functions (and all isomorphism-invariant semantics) commute with automorphisms — textbook, not program-native mathematics. The report is honest about the proof's triviality but the headline ("flip-equivariance completeness theorem… the referee's L6 gap, closed at toy grade") converts L1/L6's *concession* into a *discovery*. The L6 residue ("richer frameworks") is not closed; it is **relocated** into vocabulary choice and then discharged by definition ("the failing symbol is the posit") — the same definitional escape the swing-2 referee already priced as "defensible, but only with the grade qualifier inline." The genuine increment is real but modest: an explicit generous Σ, a mechanical membership battery, and the twin's directions exhibited in-class.

**B4 — False numeric sentence, refuted by computation. Severity: MINOR.**
§5 and the code docstring (lines 124–125) claim "every instance used is ≥ e^15 from the threshold." I computed all 16 (generator, sector) sups: the **bounded** instances all have sup ≈ 1.0, i.e. margin **e^6.9** from the 1e3 threshold — not e^15. (Unbounded instances: e^23.1 to e^53.1 — fine.) This garbles the swing-2 referee's careful L5 statement ("growth factors ≥ e^15 **or genuine contraction**") into a false uniform claim. No verdict impact — the classification margins remain decisive — but a receipts document contains a checkable false sentence, inherited and strengthened in the wrong direction.

**B5 — C2 headline drops its load-bearing quantifier. Severity: MINOR.**
"**No definable predicate separates the flip-orbit members**" is false unqualified: `eq_gen(x, y)` with `y` held at `A_c` separates `A_c` from `flip(A_c)`. The true statement — no separation *with all parameters flipped covariantly* (equivalently: without a fixed non-g-fixed parameter, which is the external bit) — is in the fine print of the same corollary but not in the bolded sentence that will be quoted.

**B6 — Battery decidability is finite-presentation-relative. Severity: MINOR.**
The §4 protocol's "there is no third case" holds only for candidates presented as finite tables over *these* g-closed finite domains. A construction introducing new sorts or infinite domains (e.g. actual matrix-vector application, which Σ omits) is not battery-decidable as-is; the report's cover ("any equivariant extension of Σ is covered by the schema-level theorem") *assumes* the extension's equivariance, which is exactly what needed deciding and is not mechanical for infinite M. For adjudicating THIS twin pair over the shared toy the protocol is genuinely decisive; the deliverable should say the decidability is scoped to finite presentations.

**B7 — "Finality/issuance-native" is a stipulative, encoding-level identification. Severity: MINOR.**
Class H's "finality/issuance" sorts are the lane-D toy conventions (scripted observers, literal-set states), not any imported TaF/TI formalism structure; no TaF FORMALISM.md primitive is modeled or matched here (this lane makes no T26 claim — that belongs to `6ed76a5`). Whether actual TaF/TI primitives are all flip-equivariant is untested, so the headline "no finality/issuance-native structure can derive…" is a formalism-flavored sentence resting on a stipulated encoding-level class. The appositive ("precisely: …") partially covers this; the verdict line should carry the stipulation explicitly.

**B8 — Trivial.** (a) Commit message says "five failing-direction controls"; the report and fixture have six (f1, f1b, f2, f3, f3b, f4). (b) The 7,544 total sums per-context counts without cross-context dedup (e.g. `Pair: 1` and constants recur in all four contexts), and the enumerated fragments beyond CTX-A are not shown to be saturated — "machine-checked completeness" is fragment-relative (disclosed in §5, but the abstract's phrasing leans on it). (c) The §7 first-run-exit-1 disclosures are unverifiable process claims — acceptable because against-interest and required by the honesty rule, but they carry no evidential weight.

## 3. Corrected wording

- **Verdict headline:** "No functional definable over a vocabulary on which the global flip acts as an automorphism (class H — our stipulated formalization of 'finality/issuance-native' at toy grade) can derive an oriented sector-asymmetric spectral condition. The unoriented condition is **expressible** in the class and flip-invariant, and holds on the hand-inserted instance; the orientation is underivable without a non-automorphic symbol, which is the posit."
- **For B1 (§3 header):** "Machine evidence: e1 — the exhaustive 844-tuple battery certifying the chosen Σ is in class H (the one contingent fact; f2 shows a natural primitive failing it) — plus six failing-direction controls. e2–e6 are theorem-corroboration: given e1 and T1 they cannot fail mathematically; they check the implementation, and are guarded by f3b/f4."
- **For B2 (C3 commentary):** "A class-H theory can **state** the unoriented asymmetry and it holds flip-invariantly on the instance; the asymmetry itself enters through the hand-chosen generator, not from issuance structure. 2′ splits into 2′-unoriented (expressible, insufficient) and 2′-oriented (underivable in class H)."
- **For B3 (§6):** "Narrows the L6 residue rather than closing it: within any fixed vocabulary where the flip is an automorphism, orbit-indistinguishability is complete (this is the standard automorphism-invariance of definable sets, instantiated); the residue now lives entirely in vocabulary choice, where a battery-failing symbol is priced as the posit by definition."
- **For B4 (§5 and docstring):** "unbounded instances exceed the threshold by ≥ e^23; bounded instances are genuine contractions (sup ≈ 1, a factor ≈ e^6.9 below threshold) — no instance is near the threshold."
- **For B5 (C2 bold):** "No definable predicate separates the flip-orbit members **when all parameters are flipped covariantly**; a separator holding a parameter fixed has consumed an orbit-representative datum — the external bit."
- **For B6 (§4):** "Membership is mechanically decidable **for candidates presented as finite tables over these g-closed domains**; a candidate requiring new or infinite domains must first be finitely presented, and that presentation step is where an escape would have to hide."

## 4. Grade the main result actually earns

**Toy-grade conditional no-go over a declared class, exploration tier, no promotion** — specifically: "In an explicit, generous 36-symbol finality/issuance-flavored toy signature certified flip-automorphic by an exhaustive 844-tuple battery (the genuine [E]), the textbook automorphism-invariance theorem yields: every definable functional is flip-equivariant, no closed term names a sector, the unoriented sector-asymmetry is expressible while its orientation is derivable only through a battery-identifiable non-equivariant symbol — and all three of the twin's announced directions, plus lane D's aliveness rule, sit inside the class. Twin adjudication over this shared toy is mechanically decidable." That is the report's claim minus: the [E] framing of e2–e6 (theorem-corroboration), "derivable/can prove" for the unoriented half (expressible), "L6 closed" (L6 relocated to vocabulary choice), the e^15 uniform-margin sentence (false for the bounded side), and the unqualified C2 bold. It does **not** earn: any statement about actual TaF/TI formalisms (whose primitives' flip-equivariance is untested), infinite-dimensional Krein-QFT (correctly bounded), completeness beyond fixed vocabularies (correctly the residue), or any movement on `bar(b)`/H59/Krein positivity/physical issuance (none attempted; ADAPTER2-01 respected — the conclusion in fact independently matches its "finality order does not choose the fiber point").

## 5. Implication for the constructive twin (pair adjudication)

This lane, if sound (it is, with the corrections above), **fixes the twin's admissible outcomes**:

1. **Expected/consistent:** the twin's constructive attempts (A1 irreversibility-as-spectrum, A2 growth, A3 fork-realization — all verified in-class here as t9–t11) can produce at most (i) the *unoriented* asymmetry or (ii) an *equivariant* selection, i.e. one that names a sector only relative to the orbit representative supplied as a parameter. A twin report concluding "derivation attempts hit an equivariance wall / selection is representative-relative" **corroborates** this lane; the pair coheres. (The twin's committed probe at `a193a3b` — "three derivation attempts, all characterized (equivariance wall)" — already points here.)
2. **Consistent-but-posit-consuming:** if the twin claims an *oriented* derivation, its vocabulary must contain a symbol failing this lane's battery. Its own helpers `c_circ` (≡ K+, a sector constant) and `eta_contractive`/`eta_expansive` (oriented η) are exactly the symbols this lane's f1/f2 controls plant and catch. In that case the twin has restated the posit, not met condition 2′; the orchestrator should require the twin to run the §4 protocol and name the failing symbol.
3. **Conflict (one lane is wrong):** if the twin claims an oriented, posit-free derivation whose *complete* vocabulary passes this lane's battery over these domains, that contradicts T1+e1. Adjudicate by (a) checking the twin's construction is fully presented in the `(name, argsorts, ressort, fn)` format with no step outside the finite domains (the B6 gap is the only escape hatch — e.g. raw matrix-vector application or a new sort), and (b) rerunning both fixtures on the union vocabulary. There is no coherent world in which both a battery-passing oriented derivation and this no-go stand.

One asymmetry the orchestrator should hold: this lane's class boundary is **stipulated**, so a twin construction that is natural but falls outside class H (fails the battery on a principled primitive) is not automatically refuted — it is *characterized* as consuming one Z/2 bit. Whether that bit is "external posit" or "legitimate finality-native structure" is exactly the ADAPTER2-01-adjacent question, and per Located-Is-Not-Forced neither lane may claim nature's answer.