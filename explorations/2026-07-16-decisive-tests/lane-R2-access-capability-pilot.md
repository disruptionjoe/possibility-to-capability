> Part of the 2026-07-16 decisive-tests swing (north-star lane; ranked program v0.1, ranks 1-4). Exploration tier; receiver updates only; the attached referee report GOVERNS — its corrected receiver update supersedes the lane headline.

# RANK 2 — PREPARATION + SYNTHETIC PILOT: Access-versus-Capability Paired Intervention Test

**Grade: PROVISIONAL / PREPARATION.** No source-issued packet exists for Rank 2; per the program's fan-out posture this is preparation plus an honestly-labeled synthetic pilot. **No receiver verdict is issued.** All program update vocabulary below appears only as conditional forecast. Nothing here moves any source-repository claim; bar(b), H59, Krein positivity, and physical issuance remain OPEN; ADAPTER2-01 governs.

---

## DELIVERABLE 1 — PREREGISTRATION DOCUMENT (proposed content, v0.1)

Proposed path (not written): `experiments/2026-07-16-rank2-access-capability-preregistration-v0.1.md`

```yaml
artifact_type: preregistration_proposal
status: preparation_provisional
created: 2026-07-16
program: experiments/2026-07-14-ranked-decisive-test-program-v0.1.md (Rank 2)
constitutional: false
```

### 1. Decisive question (verbatim from the program)

Can independently specified cases distinguish an access-only intervention from a normalized capability change **without the normalization frame entailing the answer**?

### 2. The comparison contract

**Declared factor vocabulary.** Every case pair must declare, for pre- and post-intervention: **description** (how the task is stated), **representation** (state/observable encoding), **resource** (budgets: steps, energy, samples), **access** (observation function, record reachability, control-channel addressing), **control** (action repertoire actually exercisable). A capability claim is admissible only relative to this declaration.

**Shared task vocabulary.** A single task list `V`, fixed before any classification, each task specified as (success condition over trajectories, admissible start set, resource budget), interpretable in both members of every pair. If no common vocabulary is admissible, the correct output is the program's "no shared task comparison is meaningful" branch (favors plurality) — not a forced vocabulary.

**Declared access-completion class `C`.** A lattice of access levels from the agent's actual observation function (bottom) to actual-observation-plus-every-declared-record-channel (top), **frozen before any outcome is inspected**. All normalization computations range only over `C`. Enriching `C` after outcomes are seen is a stop-condition violation.

**Frame-neutral pair evidence** (computable identically under every frame; frames may only differ in what they *call* it):
- `Δop` — did the operationally achievable subset of `V` change at actual access?
- `Δ(c)` for every `c ∈ C` — did the achievable subset change when both sides are evaluated at completion `c` (repertoires and resources per intervention, access counterfactually set to `c`)?
- `robust` — is the nonzero/zero value of `Δ(c)` constant across `C`?

### 3. The two defended normalization frames (plus one control)

**Frame N — fixed-completion normalization (candidate-side).** Capability of an agent = the subset of `V` achievable at the **top** of `C` with the agent's actual repertoire and resources. Diagnosis rule: `Δ(top) ≠ 0 → CAPABILITY_CHANGE`; else `Δop ≠ 0 → ACCESS_CHANGE`; else `NO_CHANGE`. *Defense:* access is exactly the factor whose counterfactual saturation is well-defined (grant all declared record channels); what survives saturation cannot be an artifact of what the agent happened to see; this implements the charter's capability-gate intent ("changes capability rather than only representation, access, or description").

**Frame R — operational-context relativism, access-constitutive (the strongest rival, stated at full strength, not strawmanned).** Capability *is* ability-in-actual-operational-context. "Agent X can do T" is true iff, in X's actual context — actual observation, actual records, actual control — a policy achieves T. Diagnosis rule: `Δop ≠ 0 → CAPABILITY_CHANGE`; `Δop = 0 → NO_CHANGE`. Its full-strength arguments, which the receiver must answer rather than dismiss: (i) **No privileged completion** — Frame N's "top" is one context among many; the lattice has no God's-eye element that nature certifies, and choosing the top is itself a normalization decision that entails Frame N's answers on contested cases. (ii) **Latent capability is a category error** — a disposition indexed to a context the agent does not occupy ("could do T if it could see h") is a counterfactual about a *different agent-context pair*, not a property of this one; ability talk that outruns operational context is exactly the possibility/capability conflation this repository exists to police, turned against the candidate. (iii) **Access is constitutive** — observing, reaching records, and addressing controls are not scaffolding around capability; they are part of what capability *is*; "normalizing access away" amputates the phenomenon and then reports on the stump. (iv) **Prediction**: no completion-stable, frame-neutral fact will separate "access-only" from "capability" once realistic (mixed) interventions are admitted; the boundary will flip with the completion chosen, revealing it as frame-relative.

**Frame NAIVE — surface counter (control, not defended).** Any new action or any operational gain → `CAPABILITY_CHANGE`. Included only so the discriminator has a demonstrated fool-able baseline (adversarial case c).

*Independence requirement for the real run:* Frame R must be authored and frozen by an independent operational-context reviewer **before** that reviewer sees any case pair or diagnostic label, per the program's owner boundaries. (The pilot below fails this by construction; see honest reading.)

### 4. Preregistered predictions that DIFFER between ACCESS_CHANGE and capability enlargement

These are predictions about **frame-neutral evidence**, so their success or failure is not adjudicated by either frame's own vocabulary:

| Pair type (declared by source, blind to receiver labels) | Frame N predicts | Frame R predicts |
|---|---|---|
| Access-only intervention (repertoire, resources fixed; observation/record-reachability changed) | `Δ(c) = 0` for **every** `c ∈ C`; `Δop` may be ≠ 0 | agrees `Δ(c) = 0` (trivial when repertoire fixed) but predicts the *diagnosis* still flips with frame — i.e., the separation is verbal |
| Capability intervention (access, resources fixed; repertoire/dynamics changed) | `Δ(c) ≠ 0` for **every** `c ∈ C` (enlargement survives access saturation) | no stable prediction that `Δ(c)` is completion-constant; predicts realistic repertoire changes will be completion-**relative** |
| Mixed interventions (access manufactured by an action; enlargement gated behind absent access) | `Δ(c)` completion-relative; N resolves by its declared top rule | completion-relativity here is the **proof** that the boundary is frame-relative |

Discriminating observable: **completion-robustness of the `Δ(c)` profile on independently issued pure pairs.** If source-issued access-only and capability pairs each come out completion-ROBUST with opposite profiles (`≡0` vs `≡+`), Frame R's central empirical prediction (no completion-stable separation) fails on that sector → maps to `FAVORS_CANDIDATE`. If robustness fails on pairs the sources declared pure, or holds only after access is made constitutive, → `FAVORS_RIVAL`. If equally admissible frames disagree with no invariant quotient → operational-context relativism / `CONSTRUCTION_FORK`. If pairs are empirically indistinguishable → `REMAINS_UNDERDETERMINED`. Missing prerequisites → `BLOCKED`.

### 5. Classification procedure (mechanical)

Frames are pure functions of (frozen pair evidence, pre-declared completion class). Every diagnosis must be reproducible by rerunning the frame function; any frame that returns different diagnoses on identical evidence is disqualified (evidence-functionality test — the executable form of the "normalization chosen after seeing the desired answer" stop condition).

### 6. Stop conditions (binding; program's own plus local)

1. **STOP** if any normalization frame or completion class is selected or modified after seeing the desired answer (detector: evidence-functionality test + frozen-before-outcomes timestamps).
2. **STOP** if source and receiver evidence blend — receiver-authored task semantics substituted for source-issued ones, or receiver labels visible to the issuer.
3. **STOP** (do not average) if construction branches disagree: report the fork; `CONSTRUCTION_FORK` is a first-class outcome, never blended into a pass.
4. **STOP** if the shared vocabulary is achievable only by semantically distorting either case (route to the "no common vocabulary" branch).

### 7. Spec a real source-issued case must meet (exact)

A Rank-2-admissible packet, per case pair, must contain — source-issued, frozen, digest-matched, issued **blind to receiver diagnostic labels**:
1. Pre/post system specification sufficient to decide task achievability (dynamics, observation function, action repertoire, resource budgets) or, for physical sources, the measured achievability table itself with error discipline.
2. The declared factor vocabulary values (description/representation/resource/access/control) for both members, with the source's own statement of *which single factor the intervention targeted* — the source's intent label, kept sealed from the receiver until after classification.
3. The record-channel inventory from which the receiver's completion class is built (the receiver may not invent channels).
4. Task semantics in the shared vocabulary, or the source's proof that no shared vocabulary is admissible.
5. Provenance: source repo, pinned revision, packet identifier, digests (`ptc-frozen-bundle-v1` conventions as in GU-001).
6. An independently authored, frozen Frame-R construction from the operational-context reviewer (who owns no source truth), dated before case exposure.

---

## DELIVERABLE 2 — EXECUTABLE PILOT HARNESS (full source + output)

Proposed path (not written): `tests/rank2_access_capability_pilot.py`. Pure Python stdlib. Lints clean under `tests/tef_check_tag_linter.py --strict` (registry mode, 0 violations, 0 advisories; tag counts T=2, E=11, F=5; evidential count 16). Currently exists only at scratchpad path `<local-scratchpad>/rank2_access_capability_pilot.py`.

```python
"""Rank-2 PILOT harness: access-versus-capability paired-intervention discriminator.

STATUS: SYNTHETIC PILOT / PREPARATION (ranked-decisive-test-program v0.1, Rank 2).
This is NOT a receiver verdict on real evidence. No source-issued packet exists
for Rank 2; every world, task, frame, and expectation below was authored by one
process (independence gap named in the accompanying honest reading). Nothing
here moves any source-repository claim; bar(b), H59, Krein positivity, and
physical issuance remain OPEN.

MODEL. Worlds are finite deterministic POMDPs over a shared state schema
(pos, h) with pos in 0..3 and hidden bit h in {0,1}. An agent has a repertoire
of actions (control), an observation function (access), and a per-task step
budget (resource). A task is achievable iff a single policy (branching only on
the observation history) guarantees the task for every admissible start state
within budget. The task VOCABULARY is shared and fixed across all four case
pairs before any classification (the program's shared-task-vocabulary
prerequisite, satisfied synthetically).

COMPLETION CLASS (declared before outcomes): the access lattice for these
worlds is {"pos" (actual coarse observation), "full" (pos plus the h record
channel)}. Frame N normalizes at the top of this class; the invariance probe
computes the task-set delta at EVERY member.

FRAMES (preregistered; N and R are the two defended frames, NAIVE is a control):
  N  (candidate, fixed-completion normalization): capability = task set at the
     top completion with actual repertoire and resources. delta(top) nonzero
     => CAPABILITY_CHANGE; else operational delta nonzero => ACCESS_CHANGE.
  R  (rival, operational-context relativism at full strength): capability IS
     ability-in-actual-context; operational delta nonzero => CAPABILITY_CHANGE,
     else NO_CHANGE. Latent "capability" without the access to use it is, on
     this frame, a category error.
  NAIVE (control, not defended): any new action or any operational gain counts
     as capability. Exists to demonstrate a fool-able discriminator.

CHECK DISCIPLINE: [T]/[E]/[F] registry below; only [E] and [F] carry evidential
weight; every [F] exercises, through the same code path, the checker it
protects.
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# [T]/[E]/[F] registry (linter: tests/tef_check_tag_linter.py --strict)
# --------------------------------------------------------------------------
CHECKS = {
    "t1: case-a repertoires identical":
        {"tag": "T"},
    "t2: case-a per-completion deltas empty (forced by t1)":
        {"tag": "T"},
    "e1: solver achieves reach2 in minimal world":
        {"tag": "E"},
    "e1-fail: zero-budget variant cannot reach2":
        {"tag": "F", "protects": "e1: solver achieves reach2 in minimal world"},
    "e2: coarse observation blocks anti2 in case-a baseline":
        {"tag": "E"},
    "e2-fail: budget-ignoring broken solver wrongly achieves anti2":
        {"tag": "F", "protects": "e2: coarse observation blocks anti2 in case-a baseline"},
    "e3: case-a operational gain is exactly anti2":
        {"tag": "E"},
    "e4: case-a hidden bit derivable pre and post (report_h achievable)":
        {"tag": "E"},
    "e5: case-b enlargement present at every completion":
        {"tag": "E"},
    "e6: case-b operational gain is exactly reach3":
        {"tag": "E"},
    "e7: case-c fools the naive frame while frame-N reads it as access":
        {"tag": "E"},
    "e8: case-c diagnosis is completion-relative":
        {"tag": "E"},
    "e8-fail: frame-N with truncated completion class flips case-c to capability":
        {"tag": "F", "protects": "e8: case-c diagnosis is completion-relative"},
    "e9: case-d latent enlargement: no operational change, top-completion change":
        {"tag": "E"},
    "e9-fail: frame-N with truncated completion class is blind to case-d":
        {"tag": "F", "protects": "e9: case-d latent enlargement: no operational change, top-completion change"},
    "e10: full classification matrix matches preregistration":
        {"tag": "E"},
    "e10-fail: post-hoc frame is not a function of the evidence (stop-condition detector)":
        {"tag": "F", "protects": "e10: full classification matrix matches preregistration"},
    "e11: robustness signature separates pure from mixed pairs as preregistered":
        {"tag": "E"},
}

# --------------------------------------------------------------------------
# Shared state schema, actions, observations
# --------------------------------------------------------------------------

def act_r(s):
    p, h = s
    return (min(p + 1, 2), h)          # step right; wall before pos 3

def act_l(s):
    p, h = s
    return (max(p - 1, 0), h)          # step left

def act_a(s):                          # record-consult: pos becomes 2*h.
    p, h = s                           # h is derivable via A + pos-observation.
    return (2 * h, h)

def act_j3(s):                         # unconditional jump 2 -> 3
    p, h = s
    return (3, h) if p == 2 else (p, h)

def act_jc(s):                         # h-conditional jump 2 -> 3, else stall
    p, h = s
    if p == 2:
        return (3, h) if h == 1 else (2, h)
    return (p, h)

ACTIONS = {"R": act_r, "L": act_l, "A": act_a, "O": act_a, "J3": act_j3,
           "JC": act_jc}

OBS = {"pos": lambda s: s[0], "full": lambda s: s}
COMPLETIONS = ("pos", "full")   # declared access-completion class (bottom, top)

# --------------------------------------------------------------------------
# Shared task vocabulary (fixed before classification)
#   kind "goal":   every admissible trajectory must VISIT the goal set within
#                  budget under one policy.
#   kind "report": the belief must become h-uniform within budget (the agent
#                  can then report h).
# --------------------------------------------------------------------------
STARTS = ((1, 0), (1, 1))

VOCAB = {
    "V1_reach2":   {"kind": "goal", "goal": frozenset({(2, 0), (2, 1)}),
                    "starts": STARTS, "budget": 2},
    "V2_reach0":   {"kind": "goal", "goal": frozenset({(0, 0), (0, 1)}),
                    "starts": STARTS, "budget": 2},
    "V3_report_h": {"kind": "report", "goal": frozenset(),
                    "starts": STARTS, "budget": 1},
    "V4_anti2":    {"kind": "goal", "goal": frozenset({(2, 0), (0, 1)}),
                    "starts": STARTS, "budget": 2},
    "V4b_anti3":   {"kind": "goal", "goal": frozenset({(2, 0), (0, 1)}),
                    "starts": STARTS, "budget": 3},
    "V5_reach3":   {"kind": "goal", "goal": frozenset({(3, 0), (3, 1)}),
                    "starts": STARTS, "budget": 3},
    "V6_cond3":    {"kind": "goal", "goal": frozenset({(3, 1), (0, 0)}),
                    "starts": STARTS, "budget": 3},
}

# --------------------------------------------------------------------------
# Achievability solver (exact belief-space search, deterministic POMDP)
# --------------------------------------------------------------------------

def solve(rep, obs_name, task, budget=None, ignore_budget=False):
    """True iff one observation-history policy guarantees the task."""
    obs = OBS[obs_name]
    b0 = task["budget"] if budget is None else budget
    if ignore_budget:          # deliberately broken variant for the [F] control
        b0 = 9
    goal = task["goal"]
    report = task["kind"] == "report"
    memo = {}

    def success(belief):
        if report:
            return len({cur[1] for cur, _ in belief}) == 1
        return all(done for _, done in belief)

    def ach(belief, b):
        key = (belief, b)
        if key in memo:
            return memo[key]
        if success(belief):
            memo[key] = True
            return True
        if b == 0:
            memo[key] = False
            return False
        out = False
        for name in rep:
            fn = ACTIONS[name]
            branches = {}
            for cur, done in belief:
                nxt = fn(cur)
                branches.setdefault(obs(nxt), set()).add(
                    (nxt, done or nxt in goal))
            if all(ach(frozenset(v), b - 1) for v in branches.values()):
                out = True
                break
        memo[key] = out
        return out

    init = {}
    for s in task["starts"]:
        init.setdefault(obs(s), set()).add((s, s in goal))
    return all(ach(frozenset(v), b0) for v in init.values())


def taskset(rep, obs_name):
    return frozenset(n for n, t in VOCAB.items() if solve(rep, obs_name, t))

# --------------------------------------------------------------------------
# The four preregistered synthetic case pairs
# --------------------------------------------------------------------------
CASES = {
    # (a) access-only: observation refined; repertoire identical; h was always
    #     derivable via A within a larger envelope.
    "a_access_only": {
        "pre":  {"rep": ("R", "L", "A"), "obs": "pos"},
        "post": {"rep": ("R", "L", "A"), "obs": "full"}},
    # (b) capability: new action J3 opens pos 3; observation and everything
    #     else held fixed; enlargement survives every completion.
    "b_capability": {
        "pre":  {"rep": ("R", "L"), "obs": "pos"},
        "post": {"rep": ("R", "L", "J3"), "obs": "pos"}},
    # (c) adversarial: new ACTION O that only manufactures access (oracle);
    #     looks like capability to a naive frame; redundant at top completion.
    "c_adversarial": {
        "pre":  {"rep": ("R", "L"), "obs": "pos"},
        "post": {"rep": ("R", "L", "O"), "obs": "pos"}},
    # (d) frame-dependence: new action JC exploitable only with access the
    #     agent lacks; latent enlargement; frames genuinely disagree.
    "d_frame_dependence": {
        "pre":  {"rep": ("R", "L"), "obs": "pos"},
        "post": {"rep": ("R", "L", "JC"), "obs": "pos"}},
}

# --------------------------------------------------------------------------
# Frame-neutral pair evidence, then the three frames
# --------------------------------------------------------------------------

def pair_evidence(case):
    pre, post = case["pre"], case["post"]
    op_pre = taskset(pre["rep"], pre["obs"])
    op_post = taskset(post["rep"], post["obs"])
    dc = {c: taskset(pre["rep"], c) != taskset(post["rep"], c)
          for c in COMPLETIONS}
    return {
        "op_pre": op_pre, "op_post": op_post,
        "gained": op_post - op_pre, "lost": op_pre - op_post,
        "dop": op_pre != op_post,
        "dc": dc,
        "rep_changed": set(pre["rep"]) != set(post["rep"]),
        "robust": len(set(dc.values())) == 1,
    }


def frame_naive(ev):
    return "CAPABILITY_CHANGE" if (ev["rep_changed"] or ev["dop"]) \
        else "NO_CHANGE"


def frame_candidate(ev, completions=COMPLETIONS):
    top = completions[-1]
    if ev["dc"][top]:
        return "CAPABILITY_CHANGE"
    if ev["dop"]:
        return "ACCESS_CHANGE"
    return "NO_CHANGE"


def frame_rival(ev):
    return "CAPABILITY_CHANGE" if ev["dop"] else "NO_CHANGE"


def frame_posthoc(ev, desired):
    """The FORBIDDEN move: normalization chosen after seeing the desired
    answer. Exists only so the stop-condition detector has a live target."""
    return desired


def evidence_functionality_violated(ev):
    """Stop-condition detector: a frame must be a function of the evidence
    (and pre-declared completion class) alone. The post-hoc frame returns
    different diagnoses on identical evidence, so it is flagged."""
    return frame_posthoc(ev, "ACCESS_CHANGE") != \
        frame_posthoc(ev, "CAPABILITY_CHANGE")

# --------------------------------------------------------------------------
# Preregistered expectations (authored with the design; see honesty header)
# --------------------------------------------------------------------------
PREREG_MATRIX = {
    "a_access_only":       {"NAIVE": "CAPABILITY_CHANGE",
                            "N": "ACCESS_CHANGE",
                            "R": "CAPABILITY_CHANGE"},
    "b_capability":        {"NAIVE": "CAPABILITY_CHANGE",
                            "N": "CAPABILITY_CHANGE",
                            "R": "CAPABILITY_CHANGE"},
    "c_adversarial":       {"NAIVE": "CAPABILITY_CHANGE",
                            "N": "ACCESS_CHANGE",
                            "R": "CAPABILITY_CHANGE"},
    "d_frame_dependence":  {"NAIVE": "CAPABILITY_CHANGE",
                            "N": "CAPABILITY_CHANGE",
                            "R": "NO_CHANGE"},
}

PREREG_SIGNATURES = {
    # (dop, dc[pos], dc[full], robust)
    "a_access_only":      (True,  False, False, True),
    "b_capability":       (True,  True,  True,  True),
    "c_adversarial":      (True,  True,  False, False),
    "d_frame_dependence": (False, False, True,  False),
}

# --------------------------------------------------------------------------
# Main run
# --------------------------------------------------------------------------

def main():
    results = []

    def check(name, value):
        assert name in CHECKS, name
        results.append((name, CHECKS[name]["tag"], bool(value)))

    ev = {k: pair_evidence(v) for k, v in CASES.items()}

    print("RANK-2 SYNTHETIC PILOT -- access vs capability paired interventions")
    print("=" * 74)
    print("STATUS: PREPARATION / PROVISIONAL. Synthetic. Not a receiver")
    print("verdict. Update vocabulary applies only as a FORECAST.")
    print()
    print("Frame-neutral pair evidence (shared vocabulary, declared "
          "completion class):")
    for k, e in ev.items():
        dc = ", ".join(f"delta({c})={'+' if e['dc'][c] else '0'}"
                       for c in COMPLETIONS)
        print(f"  {k}:")
        print(f"    operational: pre={sorted(e['op_pre'])}")
        print(f"                 post={sorted(e['op_post'])}")
        print(f"    gained={sorted(e['gained'])} lost={sorted(e['lost'])} "
              f"dop={'+' if e['dop'] else '0'}")
        print(f"    per-completion: {dc}  -> "
              f"{'completion-ROBUST' if e['robust'] else 'completion-RELATIVE'}")
    print()

    matrix = {k: {"NAIVE": frame_naive(e),
                  "N": frame_candidate(e),
                  "R": frame_rival(e)} for k, e in ev.items()}
    print("Classification matrix (frame -> diagnosis):")
    for k, row in matrix.items():
        agree = "AGREE" if row["N"] == row["R"] else "DISAGREE"
        print(f"  {k}: NAIVE={row['NAIVE']}  N={row['N']}  R={row['R']}"
              f"   [defended frames {agree}]")
    print()

    # ---- checks -----------------------------------------------------------
    a, b, c, d = (ev["a_access_only"], ev["b_capability"],
                  ev["c_adversarial"], ev["d_frame_dependence"])

    check("t1: case-a repertoires identical",
          set(CASES["a_access_only"]["pre"]["rep"]) ==
          set(CASES["a_access_only"]["post"]["rep"]))
    check("t2: case-a per-completion deltas empty (forced by t1)",
          not any(a["dc"].values()))

    check("e1: solver achieves reach2 in minimal world",
          solve(("R", "L"), "pos", VOCAB["V1_reach2"]))
    check("e1-fail: zero-budget variant cannot reach2",
          not solve(("R", "L"), "pos", VOCAB["V1_reach2"], budget=0))

    check("e2: coarse observation blocks anti2 in case-a baseline",
          not solve(("R", "L", "A"), "pos", VOCAB["V4_anti2"])
          and solve(("R", "L", "A"), "full", VOCAB["V4_anti2"]))
    check("e2-fail: budget-ignoring broken solver wrongly achieves anti2",
          solve(("R", "L", "A"), "pos", VOCAB["V4_anti2"],
                ignore_budget=True))

    check("e3: case-a operational gain is exactly anti2",
          a["gained"] == frozenset({"V4_anti2"}) and not a["lost"])
    check("e4: case-a hidden bit derivable pre and post (report_h achievable)",
          "V3_report_h" in a["op_pre"] and "V3_report_h" in a["op_post"])

    check("e5: case-b enlargement present at every completion",
          all(b["dc"].values()))
    check("e6: case-b operational gain is exactly reach3",
          b["gained"] == frozenset({"V5_reach3"}) and not b["lost"])

    check("e7: case-c fools the naive frame while frame-N reads it as access",
          matrix["c_adversarial"]["NAIVE"] == "CAPABILITY_CHANGE"
          and matrix["c_adversarial"]["N"] == "ACCESS_CHANGE"
          and c["rep_changed"])
    check("e8: case-c diagnosis is completion-relative",
          c["dc"]["pos"] and not c["dc"]["full"] and not c["robust"])
    check("e8-fail: frame-N with truncated completion class flips case-c to capability",
          frame_candidate(c, completions=("pos",)) == "CAPABILITY_CHANGE")

    check("e9: case-d latent enlargement: no operational change, top-completion change",
          not d["dop"] and d["dc"]["full"] and not d["dc"]["pos"])
    check("e9-fail: frame-N with truncated completion class is blind to case-d",
          frame_candidate(d, completions=("pos",)) == "NO_CHANGE")

    check("e10: full classification matrix matches preregistration",
          matrix == PREREG_MATRIX)
    check("e10-fail: post-hoc frame is not a function of the evidence (stop-condition detector)",
          all(evidence_functionality_violated(e) for e in ev.values()))

    sig = {k: (e["dop"], e["dc"]["pos"], e["dc"]["full"], e["robust"])
           for k, e in ev.items()}
    check("e11: robustness signature separates pure from mixed pairs as preregistered",
          sig == PREREG_SIGNATURES
          and sig["a_access_only"] != sig["b_capability"])

    # ---- report -----------------------------------------------------------
    print("Checks:")
    n = {"T": 0, "E": 0, "F": 0}
    bad = []
    for name, tag, ok in results:
        n[tag] += 1
        print(f"  {'PASS' if ok else 'FAIL'}  [{tag}] {name}")
        if not ok:
            bad.append(name)
    print()
    print(f"EVIDENTIAL CHECKS (headline): {n['E']} [E] + {n['F']} [F] "
          f"= {n['E'] + n['F']}, all "
          f"{'passing' if not bad else 'NOT passing'}")
    print(f"[T] theorem-consequence checks (no evidential weight, "
          f"listed separately): {n['T']}")
    if bad:
        print("FAILURES:", bad)
        return 1
    print()
    print("PILOT FORECAST (conditional, synthetic -- see honest reading):")
    print("  pure pairs (a,b): completion-ROBUST signatures separate access")
    print("    from capability; frames disagree only on the WORD, not the")
    print("    evidence -> forecasts FAVORS_CANDIDATE on this sector.")
    print("  mixed pairs (c,d): diagnosis is completion-RELATIVE; defended")
    print("    frames genuinely disagree -> forecasts CONSTRUCTION_FORK /")
    print("    REVISE_HIERARCHY pressure on this sector.")
    print("  No receiver update is issued. Real source-issued packets are")
    print("  required before any Rank-2 verdict.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### Output (verbatim, exit 0)

```
RANK-2 SYNTHETIC PILOT -- access vs capability paired interventions
==========================================================================
STATUS: PREPARATION / PROVISIONAL. Synthetic. Not a receiver
verdict. Update vocabulary applies only as a FORECAST.

Frame-neutral pair evidence (shared vocabulary, declared completion class):
  a_access_only:
    operational: pre=['V1_reach2', 'V2_reach0', 'V3_report_h', 'V4b_anti3']
                 post=['V1_reach2', 'V2_reach0', 'V3_report_h', 'V4_anti2', 'V4b_anti3']
    gained=['V4_anti2'] lost=[] dop=+
    per-completion: delta(pos)=0, delta(full)=0  -> completion-ROBUST
  b_capability:
    operational: pre=['V1_reach2', 'V2_reach0', 'V4b_anti3']
                 post=['V1_reach2', 'V2_reach0', 'V4b_anti3', 'V5_reach3']
    gained=['V5_reach3'] lost=[] dop=+
    per-completion: delta(pos)=+, delta(full)=+  -> completion-ROBUST
  c_adversarial:
    operational: pre=['V1_reach2', 'V2_reach0', 'V4b_anti3']
                 post=['V1_reach2', 'V2_reach0', 'V3_report_h', 'V4b_anti3']
    gained=['V3_report_h'] lost=[] dop=+
    per-completion: delta(pos)=+, delta(full)=0  -> completion-RELATIVE
  d_frame_dependence:
    operational: pre=['V1_reach2', 'V2_reach0', 'V4b_anti3']
                 post=['V1_reach2', 'V2_reach0', 'V4b_anti3']
    gained=[] lost=[] dop=0
    per-completion: delta(pos)=0, delta(full)=+  -> completion-RELATIVE

Classification matrix (frame -> diagnosis):
  a_access_only: NAIVE=CAPABILITY_CHANGE  N=ACCESS_CHANGE  R=CAPABILITY_CHANGE   [defended frames DISAGREE]
  b_capability: NAIVE=CAPABILITY_CHANGE  N=CAPABILITY_CHANGE  R=CAPABILITY_CHANGE   [defended frames AGREE]
  c_adversarial: NAIVE=CAPABILITY_CHANGE  N=ACCESS_CHANGE  R=CAPABILITY_CHANGE   [defended frames DISAGREE]
  d_frame_dependence: NAIVE=CAPABILITY_CHANGE  N=CAPABILITY_CHANGE  R=NO_CHANGE   [defended frames DISAGREE]

Checks:
  PASS  [T] t1: case-a repertoires identical
  PASS  [T] t2: case-a per-completion deltas empty (forced by t1)
  PASS  [E] e1: solver achieves reach2 in minimal world
  PASS  [F] e1-fail: zero-budget variant cannot reach2
  PASS  [E] e2: coarse observation blocks anti2 in case-a baseline
  PASS  [F] e2-fail: budget-ignoring broken solver wrongly achieves anti2
  PASS  [E] e3: case-a operational gain is exactly anti2
  PASS  [E] e4: case-a hidden bit derivable pre and post (report_h achievable)
  PASS  [E] e5: case-b enlargement present at every completion
  PASS  [E] e6: case-b operational gain is exactly reach3
  PASS  [E] e7: case-c fools the naive frame while frame-N reads it as access
  PASS  [E] e8: case-c diagnosis is completion-relative
  PASS  [F] e8-fail: frame-N with truncated completion class flips case-c to capability
  PASS  [E] e9: case-d latent enlargement: no operational change, top-completion change
  PASS  [F] e9-fail: frame-N with truncated completion class is blind to case-d
  PASS  [E] e10: full classification matrix matches preregistration
  PASS  [F] e10-fail: post-hoc frame is not a function of the evidence (stop-condition detector)
  PASS  [E] e11: robustness signature separates pure from mixed pairs as preregistered

EVIDENTIAL CHECKS (headline): 11 [E] + 5 [F] = 16, all passing
[T] theorem-consequence checks (no evidential weight, listed separately): 2

PILOT FORECAST (conditional, synthetic -- see honest reading):
  pure pairs (a,b): completion-ROBUST signatures separate access
    from capability; frames disagree only on the WORD, not the
    evidence -> forecasts FAVORS_CANDIDATE on this sector.
  mixed pairs (c,d): diagnosis is completion-RELATIVE; defended
    frames genuinely disagree -> forecasts CONSTRUCTION_FORK /
    REVISE_HIERARCHY pressure on this sector.
  No receiver update is issued. Real source-issued packets are
  required before any Rank-2 verdict.
```

Linter (`tests/tef_check_tag_linter.py --strict`): convention `registry`, 18 checks (T=2, E=11, F=5), evidential 16, 0 violations, 0 advisories, exit 0.

---

## DELIVERABLE 3 — HONEST READING

**What the pilot establishes (all at synthetic-toy grade):**
1. **The comparison contract is executable.** Shared vocabulary + declared completion class + frames-as-functions-of-evidence yields mechanical, reproducible classification with a working stop-condition detector (evidence-functionality test) and demonstrated failing directions for both the solver (budget-ignoring variant flips a verdict) and the discriminator (truncated completion class flips case c and blinds case d — Frame N's verdict provably depends on completion-class adequacy, which is exactly where a real run could be quietly rigged).
2. **The normalization frame does not entail the answer on pure pairs.** The separating observable — the completion-robust `Δ(c)` profile (`≡0` for access-only, `≡+` for capability) — is frame-neutral arithmetic both frames can compute. On the toy pure pairs, Frame R's central prediction (no completion-stable separation) is false, and Frame N's diagnosis of case (a) as access-only follows from a fact ranging over *every* member of the completion class, not from privileging the top. This is the pilot's existence proof that the Rank-2 question is answerable without circularity.
3. **The adversarial case is dischargeable.** An action-mediated access change (oracle action) that fools the naive frame is correctly read by the normalization machinery ( `Δ(top)=0` while the operational set grew).
4. **A genuine frame-dependence sector exists.** On mixed pairs — access manufactured by actions (c), enlargement gated behind absent access (d) — the diagnosis is provably completion-relative, and the defended frames disagree substantively (on case d they disagree about whether *anything* changed). This disagreement is not verbal and no invariant quotient resolves it in the toy. The rival is strongest exactly here, and the pilot preserves that rather than defining it away.

**What the pilot does NOT establish — the independence gaps, named:**
- **Single-author frames.** Frame R was authored by the same process that authored Frame N, the worlds, and the discriminator. A same-author "strongest rival" is structurally suspect no matter how carefully steelmanned; the program requires an independent operational-context reviewer freezing Frame R blind to cases. Not satisfied and not satisfiable by this pilot.
- **No true preregistration.** `PREREG_MATRIX`/`PREREG_SIGNATURES` sit in the same file as the cases and were authored with hand-verified achievability analysis during design; there is no two-phase expectation commit (same limitation the Bounded Fiber Theorem §4 records for its own fixtures). The pilot's "matches preregistration" check is internal-consistency evidence, not preregistration evidence. (The harness did pass on its first execution, but that is an assertion, not a mechanized receipt.)
- **Synthetic cases were designed to be separable.** Pure pairs were constructed pure. Real interventions may be predominantly mixed — in which case the pilot itself predicts the frame-dependence sector dominates.
- **Tiny completion class.** Two completions, one binary record channel, deterministic dynamics, tiny budgets. Richness of the real completion lattice (and who certifies the record-channel inventory) is untested and is a known attack surface (the [F] controls show truncation flips verdicts).
- **No source evidence touched.** Nothing here bears on GU-001, bar(b), or any source claim.

**Forecast (conditional; a forecast is not a verdict and is never averaged into a pass).** If real source-issued pairs behave like the synthetic ones:
- Pairs the sources issue as *pure* would yield stable, completion-robust, distinct access/capability diagnoses with differing preregistered predictions → maps to **`FAVORS_CANDIDATE`** over operational-context collapse on that sector.
- Pairs that are *mixed* would yield completion-relative diagnoses and genuine frame disagreement → maps to **`CONSTRUCTION_FORK`** / **`REVISE_HIERARCHY`** pressure: the pilot suggests the binary access/capability boundary may need to be typed as a *signature* (`Δop`, `Δ(c)`-profile, robustness bit) rather than a label, with the mixed sector held as an explicit fork rather than forced either way. If real pure pairs turn out not to exist, or robustness fails on them, the honest mapping is **`FAVORS_RIVAL`** or **`REMAINS_UNDERDETERMINED`**.
- Current actual status of Rank 2: **`BLOCKED`** at the source-packet prerequisite; this deliverable discharges the receiver-side preparation the program's fan-out posture permits.

**Real-case spec:** Section 7 of the preregistration document above (six numbered requirements, including the sealed source intent label and the independently frozen Frame-R construction).

**Proposed repo paths (not written):**
- `experiments/2026-07-16-rank2-access-capability-preregistration-v0.1.md` — Deliverable 1 content + this honest reading.
- `tests/rank2_access_capability_pilot.py` — the harness (currently at scratchpad path `<local-scratchpad>/rank2_access_capability_pilot.py`; lints clean under `tests/tef_check_tag_linter.py --strict`).
- Optional: `experiments/2026-07-16-rank2-real-case-spec-v0.1.md` if the source-facing spec should be separable for mailbox handoff to issuers.

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs; corrected receiver update supersedes)

All checks complete. Here is the referee report.

---

# REFEREE REPORT — Lane R2-access-capability-prep-pilot

**Referee re-execution receipts (2026-07-16, Python 3, repo pin per session snapshot):**
- Scratchpad file `rank2_access_capability_pilot.py` matches the embedded source byte-for-byte at line level (read and compared in full).
- Re-run: exit 0; output matches the report's "verbatim" block exactly, including all 18 PASS lines and the headline `11 [E] + 5 [F] = 16`.
- `tests/tef_check_tag_linter.py --strict`: convention `registry`, 18 checks, T=2/E=11/F=5, evidential 16, 0 violations, 0 advisories, exit 0 — matches the lane's claim.
- Repo not written to: no `rank2*` file exists in `experiments/` or `tests/`; `git status` clean. "Proposed paths (not written)" is accurate.
- Solver spot-audits by hand (case-a anti2 blocked at coarse obs / achievable at full; case-c report_h via O in budget 1; case-d V6_cond3 achievable only at full with JC): all consistent with the printed evidence tables.
- Adversarial probe of the stop-condition detector: `evidence_functionality_violated(None)` → True, `evidence_functionality_violated(42)` → True (it never reads its argument); a genuinely post-hoc constant frame passes it undetected. See D1.

## (1) VERDICT: **SOUND-WITH-CORRECTIONS**

No receiver verdict is issued, no source claim moves, ADAPTER2-01 is uncontradicted, the code reproduces exactly, [T]-checks are excluded from the evidential headline, and the independence gaps are self-declared. But four claims overstate what the synthetic pilot establishes, one [F]-control is defective, and one forecast term exceeds the Rank-2 outcome menu.

## (2) Defects

**D1 — MODERATE — Vacuous stop-condition detector; e10-fail does not exercise its protected checker.**
`evidence_functionality_violated(ev)` ignores `ev` entirely: it compares `frame_posthoc(ev,"ACCESS_CHANGE") != frame_posthoc(ev,"CAPABILITY_CHANGE")`, i.e., two string literals — constant-True on any input (referee probe: True on `None` and `42`). It cannot detect the actual forbidden move: a real post-hoc frame is presented *as* a fixed function chosen after peeking (probe: a constant frame chosen after outcomes passes undetected). It also never touches the code path of e10 (`matrix == PREREG_MATRIX`), so its `protects:` pointer is false and the harness docstring's "every [F] exercises, through the same code path, the checker it protects" is falsified by this one check. The other four [F]-controls (e1-fail, e2-fail, e8-fail, e9-fail) genuinely exercise their checkers and are fine.
*Corrected wording:* Honest-reading point 1 must replace "a working stop-condition detector (evidence-functionality test)" with: "an illustrative demonstration that an answer-parameterized frame violates evidence-functionality; runtime testing cannot detect real post-hoc frame selection — detection rests entirely on the frozen-before-outcomes timestamps of stop condition 1." Prereg §5's "the executable form of the 'normalization chosen after seeing the desired answer' stop condition" gets the same correction. Re-point or repair the [F]: either perturb `PREREG_MATRIX` and show e10 fails (genuine failing direction through e10's code path), or retag e10-fail as a demonstration with no evidential weight, dropping the headline to 15.

**D2 — MODERATE — Rival mis-scored against its own stated scope (synthetic result creeping toward scoring the rival).**
Honest-reading point 2: "On the toy pure pairs, Frame R's central prediction (no completion-stable separation) is false." This contradicts the lane's own §4 table, where R *agrees* Δ(c)=0 on access-only pairs ("trivial when repertoire fixed" — indeed forced, per [T] t2) and hedges completion-relativity to *realistic* repertoire changes. Case (b) is a designed-pure synthetic change, so R's hedged prediction is untestable here — not false. Declaring it false on cases built by the same author to be robust is a subtle strawman of the full-strength rival, and the strongest overreach in the lane.
*Corrected wording:* "The toy shows the §4 discriminating observable is computable and comes out opposite on designed-pure pairs. It does not falsify Frame R's prediction, which is scoped to realistic/mixed interventions; only source-issued pairs can test it."

**D3 — MODERATE — Contested disagreement resolved by receiver fiat ("only on the WORD").**
Pilot output and honest reading: "frames disagree only on the WORD, not the evidence → forecasts FAVORS_CANDIDATE." On case (a), N says ACCESS_CHANGE and R says CAPABILITY_CHANGE — and whether that disagreement is verbal or substantive is *exactly* what R's constitutive argument (iii) denies. Declaring it verbal receiver-side is the Rank-2 analogue of representation-equivalence-by-fiat (the move Rank 4 explicitly bans: "no receiver may declare two source constructions equivalent merely because that makes the diagnoses agree"). The defensible FAVORS_CANDIDATE route is solely R's failed robustness prediction on independently issued pure pairs.
*Corrected wording:* delete "frames disagree only on the WORD, not the evidence"; condition the FAVORS_CANDIDATE forecast on the §4 discriminator alone.

**D4 — MINOR/MODERATE — Forecast term exceeds the Rank-2 outcome menu.**
The Rank-2 menu is: FAVORS_CANDIDATE; FAVORS_RIVAL (+ revise normalization rule); favors operational-context relativism or CONSTRUCTION_FORK; favors plurality/new type; REMAINS_UNDERDETERMINED. `REVISE_HIERARCHY` (printed forecast and honest reading: "CONSTRUCTION_FORK / REVISE_HIERARCHY pressure") is program-level vocabulary attached to Ranks 1/4/5, not a Rank-2 outcome. Even at forecast grade, forecasts must range over the rank's own menu.
*Corrected wording:* mixed-sector forecast maps to "favors operational-context relativism / CONSTRUCTION_FORK"; the signature-not-label idea may be recorded as a candidate future hierarchy revision, not as a Rank-2 outcome.

**D5 — MINOR — "Preregistration" strings without an artifact-backed preregistration.**
`PREREG_MATRIX`/`PREREG_SIGNATURES` and check name e10 ("matches preregistration") embed prereg language while the lane itself concedes no two-phase commit exists. Honestly disclosed, but the strings will outlive the disclosure once committed and can later be quoted as prereg evidence.
*Corrected wording:* rename to `EXPECTED_MATRIX`/`EXPECTED_SIGNATURES` and "matches co-authored expectation matrix (not a preregistration)" before any repo commit.

**D6 — MINOR — "Action O only manufactures access" is vocabulary- and start-set-relative, not dynamics-true.**
`O = act_a` physically relocates the agent (`pos ← 2h`). Δ(full)=0 for case (c) holds only because from the fixed starts (1,·) every O-target is R/L-reachable in one step and no task in the 7-task V exploits the teleport. With a start such as (3,0) and a tight-budget reach-0 task, O helps at full access and case (c) becomes mixed. So "the adversarial case is dischargeable" (honest reading point 3) is a V-indexed result.
*Corrected wording:* "O is access-only *relative to the declared V and start set*; the discharge of the adversarial case is vocabulary-indexed, which is itself an attack surface for the real run alongside completion-class adequacy."

**D7 — MINOR — Independence-contamination hazard in the proposed commit.**
Deliverable 1 §3 contains a fully specified receiver-authored Frame R; §7 requirement 6 requires an *independently authored* frozen Frame R. Committing §3 as written risks anchoring the future independent reviewer.
*Corrected wording:* mark §3's Frame R as a receiver-side placeholder the independent reviewer must author without reading (quarantine annex), and add that condition to §7 requirement 6.

**Checked and cleared (not defects):** output-verbatim and linter claims (reproduced exactly); [T]-checks excluded from headline (t1/t2 correctly forced, zero-weight); [F]-controls e1/e2/e8/e9-fail genuinely exercise their checkers through the same code paths; no borrowed factorization legs (Rank-3 machinery untouched); no source claim movement; bar(b)/H59/Krein/physical-issuance stated OPEN; no ADAPTER2-01 contradiction; serialization respected (no gates run, no receiver verdict, no packet substituted); the honest-reading gap list (single-author frames, no true prereg, designed separability, tiny completion class) is accurate and complete on its own terms; §7 real-case spec is consistent with the program's Rank-2 prerequisites and owner boundaries.

## (3) Receiver update the evidence ACTUALLY earns

In the program's vocabulary, Rank 2 status: **`BLOCKED`** at the source-packet prerequisite. That is the only unconditional update. Additionally earned, at preparation grade only:

- Receiver-side preparation for Rank 2 is discharged at synthetic-toy grade: an executable comparison contract exists (shared vocabulary, declared completion class, frames as pure functions, mechanical classification), with demonstrated failing directions for the solver (budget) and the discriminator (completion-class truncation). This is process evidence about the receiver's tooling, not evidence about any rival.
- Conditional forecasts admissible after corrections D2–D4: **if** independently issued pure pairs show completion-robust opposite Δ(c) profiles under an independently frozen Frame R → `FAVORS_CANDIDATE` on that sector; **if** robustness fails on source-declared-pure pairs or holds only after access is made constitutive → `FAVORS_RIVAL`; **if** equally admissible frames disagree with no invariant quotient (the mixed sector the pilot itself predicts) → favors operational-context relativism / `CONSTRUCTION_FORK`; **if** pairs are empirically indistinguishable → `REMAINS_UNDERDETERMINED`.
- No update — not even directional pressure — toward `FAVORS_CANDIDATE` is earned by the pilot itself: the pure-pair separations are forced (case a, by [T] t2) or designed (case b), and the rival's testable prediction is scoped to cases the pilot does not contain.

## (4) Stop conditions

**Respected.** No receiver verdict issued while the prerequisite is absent (program Rank-2 stop honored); no source/receiver evidence blending (all material synthetic and labeled as such); the case-(d) construction fork is preserved as a fork, not averaged into a pass; the lane stops at `BLOCKED` rather than substituting synthetic results for the missing packet. Two caveats, both disclosed but restated with referee force: (i) "frozen before outcomes" is asserted, not mechanized — the executable detector offered as its enforcement is vacuous (D1), so within-pilot compliance with stop condition 1 rests on author assertion alone; (ii) the frames and cases are single-author, so the fan-out posture's distinct-owner condition for rival-forecast drafting is not met — acceptable only because nothing here is carried forward as the rival's authored position (enforce via D7).