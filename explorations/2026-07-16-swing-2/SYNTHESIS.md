---
artifact_type: exploration
status: complete
governance_role: swing_synthesis
constitutional: false
created: 2026-07-16
---

# 2026-07-16 swing 2 — synthesis (referee-corrected grades)

Four lanes executing the swing-1 ranked list, each independently adversarially refereed. All four referee
verdicts: SOUND-WITH-CORRECTIONS; the attached referee reports **govern the grades**. Exploration tier
throughout; no source claim moves; `bar(b)`, H59, Krein positivity, physical issuance all remain OPEN;
ADAPTER2-01 untouched by every lane (each referee checked explicitly).

## Scorecard

| Lane | Post-referee outcome | Executed? |
|---|---|---|
| **1 — GU-001 import (Deliverables 1B + 1C)** | Referee: **GO**, conditional on five mechanical corrections — ALL APPLIED at write time (git-blob byte copies, verified scratchpad artifacts, D1-corrected hash row, D3/D4/D7 wording fixes, backticked README replacement, post-write evaluator re-run). **The founding packet is now IMPORTED** (`packets/imports/GU-001/`, six files) and the **first 8-gate run PASSES (8/8, contract-valid, exit 0 on the written repo paths)** — with two disclosed grade qualifiers: neutrality at recorded-metamorphic grade; finality pass definition-relative (owner = typed joint seam; object-level identification OPEN). Receiver finding worth keeping: the frozen bundle is byte-frozen but **not runtime-closed** (W210 imports a file outside hash_scope — Annotation E, first-class bounding note). | **YES — Deliverables 1B and 1C are DONE.** |
| **2 — Gate #1 enriched-toy lift** (referee retitled from "native-tier") | Discharges all four named defects from swing-1's lane-B referee (non-thin source with a non-thin-only failing direction; multi-observer target; R<A exercised; strict-growth cases with teeth). Core survival: the branch-preserving field functor and flip-equivariance survive the non-thin lift (exhaustive-finite on two enriched toys). **Genuinely new bounding content (N4): under partitioned transport the undetermined fiber is (ℤ/2)^blocks — strictly LARGER than one global bit — so the anchor burden gets heavier, per-block, not lighter.** Referee corrections: several patch-layer positives are definitional (no independent weight); "every check has a failing direction" false as heading (18 real TEETH on M1); one expectation revised post-first-run (disclosed, no pre-registration receipt); T26's actual patch/overlap machinery still unmodeled — that is the remaining hiding place. Native tier remains open. | Fixture persisted: `tests/gate1_enriched_toy_nonthin_multiobserver.py` (exit 0 reproduced in-repo). |
| **3 — Krein norm-link probe** | **REDUCED, toy grade** — the strongest conceptual result of the swing. Not refuted: J-flip-robust, non-circular characterizations of "the issuance-supporting sector" exist (`C_stab`, `C_energy`). Not found-as-anchor: robustness is nearly free (covariance lemma); ALL selective content lives in the generator's sector asymmetry, and the **orbit lemma** shows no η/J-internal structure selects between the two flip-orbit members. Internal-generation routes fail characterizedly: η-monotone class = the sign posit restated; probability-contracting class sector-blind by boundedness (T-b); Krein-unitary dynamics puts instabilities on the **neutral cone** (T-d). **Where the posit now lives: one bit, three equivalent names — the Krein form's overall sign (bar(b)-grade) = the direction of η-norm monotonicity of issuance = which sector carries the bounded-below spectrum (the spectral condition / energy positivity).** Referee refinement (L2, with counterexample): sector-asymmetric dynamics DOES exist inside the probability-contracting class (`C_decay`), but it too consumes the orbit bit — the load-bearing blocker is the orbit lemma, not T-b. Lane D's revival condition 2 is strengthened to **2′: derive the sector-asymmetric spectral condition itself from finality/issuance structure** — exhibiting dynamics that has it is not enough. | Fixture already committed by the lane at `96b96bc` (`tests/krein_norm_link_probe.py`; referee re-ran from clean checkout, verbatim reproduction, exit 0). |
| **4 — Citation spine** | **Split grade:** the 20 arXiv entries are verified-metadata-plus-abstract (referee independently re-fetched all 20: zero discrepancies); the five classical-core entries (Harary, Zaslavsky, Toulouse, FHS, Altafini) are registrar-verified metadata with **textbook-grade characterizations — not text-verified** (publisher pages block fetching). Four headline corrections CONFIRMED (Knott sole-author demotion; Blume-Kohout–Zurek authorship; FHS = Phys. Rev. B 18, 4789 (1978); Abramsky et al. has NO "Theorem 1" — the chain is Theorem 6.1). Referee resolved the mystery pii: lane C's broken link was **Toulouse & Vannimenus, Phys. Rep. 67 (1980)** — mislabeled, topical, retainable under correct attribution. **Usable for program steering; NOT yet citation-grade for external writeup** until the five core texts are text-verified. | Spine recorded in the lane document. |

## The program picture after swing 2

1. **The charter's founding deliverables are complete.** GU-001 is imported at receiver-verified grade and
   has survived the full 8-gate sequence — the first worked joint-seam specimen, end to end, with honest
   qualifiers on gates 6 and 8. P2C is no longer a program-about-to-start.
2. **The fiber picture keeps hardening in the same direction from every angle.** Swing 1: value-blind
   targets collapse the fork; the field functor transports but cannot determine the fiber. Swing 2: the
   non-thin lift preserves that result, and partitioned transport makes the undetermined fiber *bigger*
   ((ℤ/2)^blocks). Nothing anywhere has produced sign-selecting structure.
3. **The bit has been chased to a named home.** Lane 3's reduction: the norm-link posit = the sector-
   asymmetric spectral condition (energy positivity). Combined with lane D (aliveness = base asymmetry,
   not fiber selection) and ADAPTER2-01 (fiber over profile), the honest map is now:
   **bar(b)-shaped bit ≡ which Krein sector carries the bounded-below spectrum — a named prior physics
   posit, relocated, not resolved, and not finality-native at current grades (T18 conditional, T57 open).**
4. **Anchor burden, restated:** any future anchor must (1) be source-side and composition-compatible
   (E160 shape), (2′) *derive* the sector-asymmetric spectral condition from finality/issuance structure,
   and (3) do so non-definitionally — and per N4, potentially per-block under partitioned transport.

## Ranked next work (supersedes swing-1 SYNTHESIS ranking)

1. **T26-native patch/overlap machinery** — the one remaining unmodeled hiding place for sign-selecting
   transport data (lane 2 referee F3): model TaF's actual `D1RestrictionSystem` overlap tests and
   non-pairwise patch constraints and re-run the flip-automorphism question.
2. **Condition 2′ attempt or no-go** — can any finality/issuance structure *derive* a sector-asymmetric
   spectral condition, or is there a clean toy no-go (which would honestly bound the program's fiber scope
   for good)?
3. **Text-verify the five classical-core citations** (library/alternate access) to lift the spine to
   citation grade.
4. **Source-side housekeeping to GU (mailbox, not edits):** Annotation E (bundle not runtime-closed —
   suggest adding `gen_sector_bridge.py` to hash_scope in any v0.3), the issued_at anachronism, and the
   packets/ stale-wording-sweep gap.

## Process note

Second consecutive swing where the adversarial-referee stage caught real defects in every lane — including
one outright false mathematical claim (lane 3's candidate-(b) universal, refuted by referee counterexample)
and a corrupted hash row that would have been written into the one table whose job is byte-exactness
(lane 1 D1). The two-stage structure stays mandatory. New pattern to adopt from lane 3's referee: tag every
check `[T]`heorem-consequence vs `[E]`xperiment vs `[F]`ailing-direction-control, and count only [E]/[F]
as evidence.
