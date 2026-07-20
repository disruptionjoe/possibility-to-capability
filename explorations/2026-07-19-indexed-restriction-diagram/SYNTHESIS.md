---
artifact_type: exploration
status: executed_scoped
created: 2026-07-19
experiment_id: P2C-IRD-001
outcome: RESTRICTION_PROFILE_SEPARATION_SCOPED
governing_referee_report: REFEREE-REPORT.md
---

# Indexed restriction diagram — synthesis

## Result

The raw-transition swing returns
**`RESTRICTION_PROFILE_SEPARATION_SCOPED`**.

At one frozen task, vector budget, horizon, observation, verifier, and
evaluation action set, the N and S starting restrictions have unequal reachable
task profiles:

| object | policies exhausted | minimum hold cost | passes hold limit 0 |
|---|---:|---:|---:|
| N evaluation fiber | 40 | 1 | no |
| S evaluation fiber | 40 | 0 | yes |
| whole envelope W | 80 | contains S realization | yes |

The independently built direct fibers exactly equal W's explicit
evaluation-stage restrictions. A carrier relabel preserves the full policy and
cost profile. The proposed N/S correspondence fails on a raw transition:
`N1 --IDLE--> N0`, while `S1 --IDLE--> S1`.

This is the first P2C result in the sequence whose indexed diagram is computed
from raw transitions rather than only from a classifier table.

## What the collapses say

The separation is real inside the declared construction and explicitly not
frame-free:

| mutation | result | what changed |
|---|---|---|
| allow `COOL` during evaluation | both pass | preparation/action-stage construction |
| hold budget `0 -> 1` | both pass | resource frame |
| N-only `LATCH_HOLD` action | N passes | interface-labelled action menu and verifier contract |
| horizon `3 -> 1` | both fail | task horizon |
| forget costs/transitions/start index | invalid quotient | required comparison structure |

Every successful equalization pays a declared price. That is not evidence for
an intrinsic, context-free capability. It is evidence for a typed reachability
profile whose truth depends on the system boundary, starting restriction,
action stages, interface, resources, task, verifier, and horizon.

## Strongest coherent-story update

The hierarchy can now be told more precisely as a semantics over augmented
dynamics rather than a list of independent substances:

```text
possibility = which typed transitions are admitted
dynamics    = how those transitions compose
records     = which state distinctions persist through allowed continuations
access      = which observations and actions the interface exposes
capability  = whether an accepted path exists under a task/resource contract
finality    = whether the relevant result is stable under every admitted continuation
```

On this reading, capability is derivable as a reachability projection of an
augmented transition system. That does not make it empty. The projection keeps
the starting fiber, interface, resources, task, verifier, and horizon as typed
indices. A larger model that merely places everything into “dynamics” has not
resolved the disagreement until it supplies a principled rule for which of
those structures its quotient must preserve.

The clean plain-English story is:

> What can happen globally, what can happen from here, and what can be done from
> here under this interface and budget are different questions. One world can
> answer all three without contradiction by keeping track of the maps between
> them.

W contains the successful realization. N, under its fixed evaluation contract,
cannot reach it at zero hold cost. S can. Adding cooling, maintenance resource,
or a latch changes which question is being asked and can honestly change the
answer.

## Coarse augmented-dynamics reduction fails

The explicit N/S-forgetting quotient sends both zero states to `q0` and both
one states to `q1`. But `q1 --IDLE-->` has two targets, `q0` and `q1`. The
quotient is not deterministic, the N/S relation is not a bisimulation, and the
two start embeddings are erased. It is therefore not a faithful collapse of
the base model.

This rejects one coarse reduction. It does not prove that no independently
motivated canonical augmented-dynamics quotient exists.

## Strongest next action

Do not repeat this four-state toy. The next high-information use is to require a
source-grounded specimen—preferably the exact-Hamiltonian topological-order
track or a more physical P2C-W1 transition model—to issue the same data:

- explicit state and starting-context identities;
- preparation versus evaluation actions;
- vector resources and multiple horizons;
- a carrier-neutral observation/verifier contract;
- exact restriction maps; and
- the strongest interface, resource, and whole-family attacks.

A smaller belt refinement is also available: preserve origin and current
carrier as separate state coordinates so `COOL` becomes a precise fork between
rooted-policy pullback and current-carrier restriction. That is useful only if
it supports the source-grounded application rather than becoming another free
toy.

## Ceiling

The model is finite, designed, deterministic, and exact-error. The task
verifier uses the declared action word as well as the digit observation. There
is no physical transition law, noise model, metastability clock, unbounded
horizon, or source-issued task-semantics map. No physical capability,
access-independent ontology, universal hierarchy, issuance, source claim, or
finality status moves.
