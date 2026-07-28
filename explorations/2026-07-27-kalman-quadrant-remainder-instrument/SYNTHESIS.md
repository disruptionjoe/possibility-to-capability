---
artifact_type: exploration
status: executed_scoped
created: 2026-07-27
experiment_id: P2C-KQRI-001
outcome: CONJUNCTIVE_KALMAN_READING_COINCIDES__EDGE_FREE_AND_DISJUNCTIVE_FAIL
directed_by: "Joe direct-chat session, 2026-07-27 (orchestrated build arm)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
grade: exploration-tier calibration instrument (implements known mathematics)
verification: >-
  tests/kalman_quadrant_remainder_instrument.py (exit 0; 6 [E] + 3 [F] = 9
  evidential; 3 [T] setup; lints clean under tef_check_tag_linter.py --strict)
---

# Kalman-quadrant remainder instrument — synthesis

## Framing guard (read before anything else)

This artifact claims **zero novel typing**. P2C's own methodology novelty scan
(`explorations/2026-07-22-methodology-novelty-genre-scan/SYNTHESIS.md`)
recorded the access/capability distinction as **SUBSUMED** by control theory's
reachability/observability duality and the Kalman decomposition ("Not
novel"), and the same folder's `TRANSFER-BREAKER-PREREG-SKELETON.md` row 2
forecasts "TRANSFER FAILS — Kalman decomposition already types this" for the
computation/systems domain. This fixture **depends on** that verdict rather
than contesting it: it takes the known mathematics and makes it executable as
a calibration instrument — a fully specified toy world with exact ground
truth, where the reconstruction remainder is *computed against the answer
key* instead of argued about. An instrument, not an ontology and not a
novelty claim.

## What was built

`tests/kalman_quadrant_remainder_instrument.py` — pure stdlib Python,
deterministic, no randomness, exhaustive enumeration (no sampling).

**Construction.** A finite directed influence graph. Ten cells each carry a
static ground-truth parameter (the reconstruction target) and a dynamic
excitation state (packets). One agent node `AGT` emits actions; one record
node `REC` collects the agent's verified interaction records; the agent
accumulates only those records. Four declared sectors implement the mailbox
spec's typed structure:

| sector | cells | typing (computed by graph closures) |
|---|---|---|
| collision geometry | wall, hinge, latch | reachable AND observable |
| render-mesh analog | mesh_a, mesh_b | reachable, NOT observable (probing excites them; nothing from them ever feeds records) |
| sealed-room analog | room_a, room_b, vent | NOT reachable, observable (agent actions can never reach them; if the initial excitation differs there, later records differ — free response through the vent) |
| inert | rock, slab | neither |

**Definitions used here, to block the equivocation failure mode** (these are
this fixture's meanings and no one else's): a *capability edge* is a directed
influence edge of the world graph (an arc, including action edges `AGT->c`
and record edges `c->REC`); *reachable* is forward closure of `AGT`;
*observable* is backward closure of `REC`; *recoverable(c, T)* means every
world in the declared class whose record-stream prefix of length T matches
the true world's agrees with it on cell c's parameter (posterior-at-the-truth
collapses to a singleton — the single recoverability definition used
everywhere in the file); the *remainder* R(T) is the set of unrecoverable
cells. The six-arm-swing correction's phrase "a capability edge is a cycle,
not an arc" names exactly the conjunctive reading the fixture vindicates:
recoverability needs the round trip, not any single arc.

**The remainder is computed two ways by disjoint code paths.** (i) Directly:
enumerate every world in the class (1,536 under known-init; 49,152 under
unknown-init), simulate each, and match record streams against the true
world's. (ii) By formula: `~(reachable & observable)` from graph closures
alone, with no simulation. The code paths share only the world declaration.

## Results (script output, horizon T = 8)

**Remainder, two ways:**

| computation | remainder | size |
|---|---|---|
| formula `~(reachable & observable)` | mesh_a, mesh_b, rock, room_a, room_b, slab, vent | 7 |
| direct, KNOWN-INIT (1,536 worlds) | mesh_a, mesh_b, rock, room_a, room_b, slab, vent | 7 |
| direct, UNKNOWN-INIT (49,152 worlds) | mesh_a, mesh_b, rock, room_b, slab | 5 |

Under the known-initial-state declaration the two computations **coincide
exactly** — the positive, conjunctive/Kalman reading. Dropping the
declaration lets the sealed room's free response reach the records: room_a
and vent are recovered, and room_b is only *partly* constrained (its
posterior shrinks from {0,1,2} to {0,2} through the declared lossy parity
vent but is not pinned, so it stays in the remainder). This two-regime split
is the **known-initial-state caveat** implemented: the caveat is load-bearing
— the exact `~(reachable & observable)` identity is a fact about the
known-initial-state regime, and the `~reachable & observable` cell is exactly
where the regimes diverge.

**Graded R-curve** (remainder size vs record length; floor = structural
floor):

| T | R known-init | newly recovered | R unknown-init | newly recovered |
|---|---|---|---|---|
| 0 | 10 | — | 10 | — |
| 1 | 9 | wall | 9 | wall |
| 2 | 9 | — | 7 | room_a, vent |
| 3 | 7 | hinge, latch | 5 | hinge, latch |
| 4–8 | 7 | — | 5 | — |

R is non-increasing (a prefix-nesting consequence, tagged [T], not counted as
evidence) and plateaus at the structural floor at finite T = 3; no further
records help through T = 8. A symbolic discharge in the script output shows
the known-init floor is policy-independent: every delivered stamp names a
cell in `REACH & OBS` for *any* policy and horizon, so the floor is
topological, not a probing artifact.

**Teeth-controls** — deliberately wrong readings, each asserted to FAIL (a
passing tooth aborts the run with nonzero exit):

- **T1, edge-free hypothesis** ("remainder = cells with no capability
  edges") predicts {rock, slab}. FAILS: room_a is in the remainder while
  carrying the dispositional edge `room_a -> vent`.
- **T2, the ORIGINAL disjunctive downstream-only conjecture** (the mailbox
  spec's form: "remainder = exactly the causally-downstream-only structure")
  predicts {mesh_a, mesh_b}. FAILS: the sealed room is in the remainder and
  is not downstream-only. This executes, as a machine witness inside P2C,
  the counterexample shape recorded in the 2026-07-27 six-arm-swing
  correction (H3 refuted; only the conjunctive/Kalman reading survives).
- **T3, render-mesh-observable control** FAILS on both legs: mesh_a is not
  in the backward closure of `REC`, and exhaustive parameter variation of
  both mesh cells changes no record stream in either regime — while the
  same simulation confirms agent actions do excite the mesh ("moving
  changes it").

**Anti-vacuity receipts.** Each check has a demonstrated failing direction.
Three mutation probes were run on scratch copies during construction, and
each drove the fixture to nonzero exit: (a) making a collision-sector stamp
lossy with a conflatable true value broke the coincidence and floor checks
(the declared A2 falsifier surface, detected); (b) replacing the T2
hypothesis with the extensionally correct formula tripped the T2 tooth; (c)
wiring `mesh_b -> REC` tripped the setup typing check, the mesh check, and
the T3 tooth simultaneously. The probes are described here for
reproducibility; they are not committed.

## Assumptions (the instrument's class; outside it, nothing is claimed)

1. Finite, deterministic, known dynamics and wiring; no noise; fixed probing
   policy exercising every action edge. Below the floor, recoverability is
   policy-relative; the floor itself is not (symbolic discharge).
2. Records are maximally informative interaction outcomes (faithful stamps),
   except the declared lossy sealed-room parity channel. Faithful stamps on
   the reachable-and-observable sector are required for exactness — a lossy
   collision channel breaks the coincidence, and the fixture detects that
   (probe (a)). Because records are best-case, the computed remainder is a
   *structural floor*: it comes from reach/influence topology, not record
   poverty.
3. The reconstruction target is ground-truth parameters; identifying the
   dynamics/rules themselves is a different experiment, out of scope.
4. The unknown-init regime varies initial excitation only on the unreachable
   sector — a declared modeling choice (the agent can never re-prepare that
   sector, while the reachable sector relaxes to rest in this pulse world),
   pinned by a setup check to equal the computed unreachable set.
5. Free-response recovery is contingent on the true initial state actually
   differing from rest: a sealed room initialized at rest emits nothing and
   stays unrecovered even in the unknown-init regime. The demonstration uses
   an excited true room; this dispositional contingency is part of the
   caveat, not hidden.

## Grade and verification status

**Grade:** exploration-tier calibration instrument. It implements known
mathematics (the Kalman-decomposition typing, in finite graph-closure form)
and executes one recorded refutation as a machine witness. It is not a
theorem about any native formalism, any physical system, or any source
repository's objects, and it does not lift the novelty grade recorded by the
genre scan.

**Verification status:** script exit 0 on the committed run; all three teeth
fail as required; both positive checks pass (coincidence; finite floor);
6 [E] + 3 [F] = 9 evidential checks, 3 [T] setup checks excluded from the
headline; `tef_check_tag_linter.py --strict` reports zero violations and
zero advisories in registry mode. Expectations are declared in-file before
execution; no external preregistration receipt exists for this fixture.

## Falsifiers (what would break or reopen this)

- A world in the declared class (finite, deterministic, faithful stamps on
  the reachable-and-observable sector, known-init) where the direct and
  formula remainder computations diverge would break the instrument.
- A world in the class where R(T) increases with T, or where the known-init
  plateau differs from `~(reachable & observable)`, would break it.
- A demonstration that the coincidence depends on the specific probing
  policy (i.e., a policy exercising every action edge under which some
  `REACH & OBS` cell stays unrecoverable at every horizon, or a policy that
  recovers a cell outside `REACH & OBS` under known-init) would break the
  symbolic discharge.
- Showing the fixture's definitions of capability edge / reachable /
  observable silently shift between the teeth and the positive check (the
  equivocation failure mode) would invalidate the teeth results.
- If the six-arm-swing correction's H3 entry is itself revised at source,
  T2's *framing* (which conjecture it executes the refutation of) must be
  re-examined; the fixture's computation stands independently either way.

## Citations and crosswalks

- **Queued spec (proposal, not instruction):**
  `repos/private/system-runtime/mailboxes/possibility-to-capability/20260727-game-worlds-as-a-calibrated-remainder-instrument.md`,
  item 1. Its "downstream-only conjecture" is the ORIGINAL disjunctive form;
  this fixture executes the recorded refutation of that form (tooth T2)
  rather than adopting it. The mailbox message remains a proposal; nothing
  in it was treated as a directive.
- **Framing-guard sources (this artifact depends on them):**
  `explorations/2026-07-22-methodology-novelty-genre-scan/SYNTHESIS.md`
  (access/capability distinction SUBSUMED by the Kalman decomposition; "Not
  novel") and `TRANSFER-BREAKER-PREREG-SKELETON.md` row 2 ("TRANSFER FAILS —
  Kalman decomposition already types this").
- **Refutation record (source-owned, unratified thinking; status not moved
  here):** Joe Thinking Wiki (private),
  `joe-thinking-wiki#map/explorations/q0064-capability-indexed-certification.md`,
  six-arm adversarial swing correction of 2026-07-27 — H3 (downstream-only)
  refuted by counterexample; remainder is `~(reachable & observable)`, three
  quadrants, not one; "a capability edge is a cycle, not an arc". This
  fixture is an independent machine witness of that counterexample shape
  inside P2C; it does not change the source record's status.
- **Kalman decomposition:** standard linear-systems-theory material
  (reachable/observable canonical structure and minimal realization), cited
  generically. Per this session's E-0048 flag, the primary 1962/63 wording
  was not verified, so no quotation or primary-source citation is made here.
- **Crosswalk (landed 2026-07-27):** dynamic-unity
  `explorations/presentation-invariant-operational-kernel-and-query-separation-2026-07-27.md`,
  strongest-absorber section, independently cites Kalman minimal
  realization ("the controllable and observable part of a linear system
  from fixed input/output behavior, only up to similarity") as an absorber
  of a related schema. Convergent absorber, separately arrived at.
- **Genre ancestor:** time-as-finality
  `models/reconstruction_without_background_time.py` — the existing
  reconstruction-from-records fixture family this instrument's style
  descends from (finite witness, declared hypotheses, anti-scalar-style
  negative controls). Source-owned; nothing imported from it.

## What this does not claim

- **No novel typing.** The SUBSUMED verdict stands; this fixture's entire
  framing depends on it. Nothing here is presented as a new distinction,
  new mathematics, or evidence against the genre scan.
- **No physics.** The toy world models no physical system; the game-world
  reading is a calibration instrument — a setting where ground truth is
  available — not an ontology and not a claim that game worlds model
  reality.
- **No claim movement anywhere.** No source claim status, canon, grade,
  Lane state, or public posture changes. The six-arm-swing correction and
  the mailbox proposal keep their own statuses; the mailbox item is not
  hereby graded, adopted, or archived.
- **Not a test of H2.** The null-player/Shapley characterization (H2 of the
  same swing) is not implemented or evaluated here; only the H3
  counterexample shape is executed.
- **Not "proved" or "resolved".** The coincidence and refutation results
  are exhaustive-finite facts about this declared toy class under its
  declared definitions, nothing stronger.
