---
artifact_type: exploration
status: complete
governance_role: swing_synthesis
constitutional: false
created: 2026-07-16
---

# 2026-07-16 big swing — synthesis (referee-corrected grades)

Four parallel lanes, each independently adversarially refereed. All four referee verdicts:
SOUND-WITH-CORRECTIONS. The referee reports are attached to each lane file and **govern the grades**;
the headline grades below are the post-correction ones, not the lanes' own headlines. Exploration tier
throughout; no source claim moves; `bar(b)`, H59, Krein positivity, physical issuance all remain OPEN.

## Scorecard

| Lane | Post-referee verdict | What it changes |
|---|---|---|
| **A — GU-001 packet provenance** | **IMPORTABLE, at receiver-verified grade** (referee extended verification: 16/16 manifest hashes recomputed, digests recomputed under `ptc-frozen-bundle-v1`, v0.2 schema 0 errors, tests re-run exit 0). Import pin `77879e5`; carry annotations A/B/C plus: the same correction-supremacy annotation governs `claim.statement`'s "TaF-owned finality activation" apposition; log the `issued_at` anachronism (packet says 12:00, evidence pin committed 14:14). | Deliverable 1B is executable NOW. Charter's `NOT_YET_IMPORTABLE` trigger demonstrably not met. |
| **B — Gate #1 functor** | **SPLIT, demoted one grade from its headline:** (a) profiles-only collapse is a **definitional lemma** (any map factoring through the value-stripping quotient collapses the fork; premises verified exhaustively on two thin-inclusion toys; the collapse-or-smuggle dichotomy is relative to the σ-invariance/Neutrality criterion) — NOT an absolute disproof about TaF's native D1; (b) a branch-preserving functor into **D1Field exists** (functor laws + equivariance exhaustive-finite on the image), with the fiber **σ-equivariantly transported and undetermined by flip-invariant target structure** (definition-relative). Two controls were vacuous as coded (constant-functor rejection; decorated naive-branch leg); the profile-forgetful rejection and decoration-detection legs are genuine. **Native-tier obligations (1)–(2) remain OPEN** (RUN-0025 thin-shadow caveat). | Toy-tier corroboration + sharpening of ADAPTER2-01's fiber picture, with the burned bug class genuinely excluded (SOURCE_/TARGET_ disjoint code paths). Fixture persisted: `tests/gate1_branch_preserving_functor.py` (exit 0 reproduced in-repo). |
| **C — Novelty scan** | **NEW-FRAMING-ONLY, near NOTHING-NEW** — and the referee notes the tested object was *inflated above* the surviving hard core (three program-internal **encodings on one shared input**, agreement partly by construction — not "independent formalisms"), which only strengthens the negative. Closest prior work: **Abramsky et al. 2015 (arXiv:1502.03097)** — cohomological/sheaf contextuality with explicit cross-domain recurrence thesis. Harary balance, switching orbits: textbook. Citation spine directionally right but NOT verified (FHS link broken). | **Do not write up the hard core standalone.** Any external contribution must come through native-tier Gate #1 work or a genuine anchor. |
| **D — Aliveness anchor** | **FAILS-NEUTRALITY (at this formalization grade), with a located diagnosis** — referee upgraded the mechanism from "sampled in 3 models" to **framework theorem**: the rule is built solely from sign-symmetric primitives, so flip-equivariance is provable, not sampled (0/20,000 violations in the referee's probe). The rule relabels; it does not select. Reusable diagnosis: aliveness names a real asymmetry **of the base** (future-open vs past-fixed extension), but the fiber needs transport data of the E160 shape, and aliveness is a unary, readout-side (RUN-0019 `kappa_i`-typed) predicate — wrong type. **The one untested door:** the Krein-dynamical norm-link — exhibit an issuance generator realizable (probability-conserving) on exactly one Krein sector, characterized robustly under the flip *including the flip of `J`*, non-definitionally. | The anchor conjecture is honestly parked with a precise 3-part revival condition. Fixture persisted: `tests/aliveness_neutrality_test.py` (exit 0 reproduced in-repo). |

## The program picture after the swing

1. **The consistency layer is settled and unoriginal** (C): Harary balance + switching orbits + fiber freedom
   is known mathematics; its value here is organizational.
2. **The fiber picture is now corroborated at toy grade from both directions** (B): value-blind targets
   collapse the fork *by definition*; the field-valued rescue transports the fiber equivariantly and cannot
   determine it from flip-invariant structure. This strengthens ADAPTER2-01 without reopening anything.
3. **The first candidate anchor is dead at its stated grade** (D), with the failure *located* (base/fiber
   mismatch + readout-side typing) — which is reusable: any future anchor candidate must be source-side,
   composition-compatible (E160 shape), and `J`-flip-robust.
4. **The founding deliverable is unblocked** (A): GU-001 is source-frozen, receiver-verified, and importable
   at pin `77879e5` with three annotations.

## Ranked next work (supersedes the ranking in `2026-07-16-research-program-state-and-gate-1-milestone.md`)

1. **Execute the GU-001 import** (Deliverable 1B): copy the frozen packet byte-identical, write the
   receiver-side import record with annotations A/B/C + the `claim.statement` annotation + the `issued_at`
   log line, then run the charter's 8-gate sequence (Deliverable 1C) on it. Everything needed is in
   `lane-A-packet-provenance.md`.
2. **Native-tier Gate #1** (the real remaining mathematics): lift the toy functor question to TI's non-thin
   `Ext_S` morphisms and TaF's `D1RestrictionSystem`/multi-observer D1Field (per-proposition sites → real
   observer sites; exercise R as a distinct axis; strictly-increasing monotone cases). The toy fixture and
   the referee's defect list (D2, D7, D8) are the spec.
3. **Krein-dynamical norm-link probe** (the one open door from D): attempt or refute the
   sector-realizability characterization with `J`-flip robustness as the pass/fail criterion.
4. **Verify the citation spine** from C (fix the FHS reference; confirm per-neighbor characterizations)
   before any external-facing writeup uses it.

## Process note

The adversarial-referee stage caught, in every single lane, at least one instance of the exact error class
that produced ADAPTER2-01 (cannot-fail checks presented as passing controls; claims graded above evidence;
encoding-level facts stated as formalism-level facts). None survived into the governing grades. The
two-stage research→refute structure should be the default for all future P2C swings.
