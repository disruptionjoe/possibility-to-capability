---
artifact_type: exploration
status: complete
governance_role: swing_synthesis
constitutional: false
created: 2026-07-16
---

# 2026-07-16 north-star unblock swing — synthesis (referee-corrected)

Four lanes, four referees (all SOUND-WITH-CORRECTIONS; referee reports attached to each lane file and
GOVERN). The swing's design premise — that Rank 2's independence requirements are satisfiable by
construction with firewalled agents — was executed and audited: **both firewalled lanes verdicted
INDEPENDENT** (declaration audits clean; no receiver vocabulary leakage found on comparison against the
actual forbidden files). Receiver updates: Rank 2 remains `BLOCKED` (nothing is source-issued until the
source stewards adopt); Rank 1's scoped conditional FAVORS_CANDIDATE and the other blocks stand untouched.

## What landed

| Lane | Deliverable | Referee-corrected status |
|---|---|---|
| **A — prereg mechanism + transition diagnosis** | `interfaces/two-phase-preregistration-v0.1.md` + `tests/prereg_verify.py` (P1–P7 gates proved from git history; [F] controls fail through the verifier's own code path; live-tamper demo receipted on a throwaway git repo) + `packets/imports/GU-001/GU-001-TD-001-transition-diagnosis-v0.1.json` (the skipped serialization step, executed). | Mechanism earns adoption as a **provisional repo process interface**, billed correctly: a prereg-verify PASS is **necessary, not sufficient** for prerequisite (v). Transition diagnosis: contract-valid; prospective-selection branch robust (honest UNKNOWNs, no fiat). Repairs 1a + 1b: **DONE**. |
| **B — TAF-001 source packet (firewalled)** | Paired record-access vs record-formation interventions in TaF's own T22/T46 vocabulary, machine-checked before/after evidence, NO diagnostic pre-labels. | **FIREWALL: INDEPENDENT.** Grade: formal-only, computation-confirmed, corrections applied per referee (one fact narrowed to one-directional). Rank 2 stays BLOCKED until **TaF's steward adopts and issues** the bundle (draft-for-source-issuance; proposed to TaF by mailbox). |
| **C — Frame R + TI-PIT-02 (quarantined)** | The access-constitutive rival at full strength (own predictions, concession conditions C1–C4, falsifiers R.6a–d, genuinely pre-committed) + a TI-native paired case (fixture referee-re-run). | **FIREWALL: INDEPENDENT.** Frame R earns candidate standing for the "strongest access-constitutive construction" prerequisite, **conditional on adoption/re-freezing by an advocate independent of any case it scores** (this lane cannot advocate for its own co-authored TI case — referee D1). TI-PIT-02: draft-for-source-issuance (TI steward's call). |
| **D — Hierarchy v0.2 draft** | Process-level typed definitions for all six levels (per the amputation requirement); finality level built on the operator taxonomy + opacity bound + SSB vocabulary; executable skeleton (exit 0, lints clean). | Grade: **definitional draft + deterministic toy skeleton**, conditional on referee corrections D1–D7 (evidential headline corrected to 8 [E] + 4 [F]; "frame-circularity detector" withdrawn to "forced-frame flag with an open detector-with-bite obligation"; two content misstatements must be fixed before any synthesis/ promotion). Lane 2 item 2: **DRAFTED, Joe review pending, corrections pending application.** |

## The Rank-2 runway (what now exists vs what remains)

Now in hand: mechanized preregistration (A), a firewalled source-evidence draft (B), an independently
authored rival frame + second case draft (C), and the receiver's comparison contract (prior swing).
Remaining before the real Rank-2 run: (1) TaF and TI stewards adopt/issue their packets (mailbox proposals
filed — source-sovereignty preserved; receiver cannot self-issue); (2) an independent advocate re-freezes
Frame R (cannot be lane C for TI-PIT-02); (3) the receiver's expectations artifact goes through the
two-phase mechanism BEFORE outcomes; (4) then the preregistered Rank-2 run executes. Every piece is now
either built or a named, owned, single step.

## Process note

Fifth consecutive swing with real referee catches in every lane (this time including the prereg lane
being held to its own standard — billing narrowed to necessary-not-sufficient — and a rival-authoring
lane blocked from advocating for its own co-authored case). The firewall-audit pattern (declared-reads +
vocabulary-leakage scan against the actual forbidden files) worked and is now the house method for
independence-requiring work.
