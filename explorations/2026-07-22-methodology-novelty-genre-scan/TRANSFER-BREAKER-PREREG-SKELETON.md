---
artifact_type: exploration
status: preregistration-skeleton
governance_role: transfer_breaker_battery_prereg
constitutional: false
created: 2026-07-22
relation_to_hard_core: Lane 1 — the executable form of the North Star's own falsifier ("definitions can't transfer beyond one domain without ad hoc reinterpretation").
grade: PREREGISTRATION_SKELETON (no fixture built; defaults declared before any run)
prereg_id: P2C-XBREAK-001
---

# Transfer-BREAKER battery — preregistration skeleton (domain-neutral)

A transfer **breaker**, not a transfer demo: it is built to make the same
typed-change instrument **fail** in each new domain, and only records a
non-subsumption if it survives that attempt. Default forecast for every domain
is **TRANSFER FAILS**. Security is domain 1 because object-capability security
is the strongest subsumer identified in the genre scan; if the instrument adds
nothing over ocap on a security case, that is the cheapest falsification.

## 0. Shared, domain-neutral vocabulary (fixed before any domain is chosen)

- **Frame:** the declared observer/model choice — the variable set, the
  before/after pair, and the normalization that holds one axis fixed while
  another is compared. Every verdict is frame-indexed. (Prior: Halpern-Pearl
  modeling choice.)
- **Resource:** the budget consumed to realize a task (time, energy, tokens,
  privilege, capital, attention). Normalization holds the resource frame fixed.
- **Task:** an operationally checkable capability — an input/goal pair with a
  pass/fail oracle. `raw_task_set` counts tasks with access unrestricted;
  `normalized_task_set` counts them with access/resource held fixed.
- **Typed outcome vocabulary (unchanged from `classify_transition.py`):**
  `POSSIBILITY_FAMILY_CHANGE`, `FIXED_FAMILY_DYNAMICS`, `RECORD_FORMATION`,
  `ACCESS_CHANGE`, `CAPABILITY_ENLARGEMENT/RESTRICTION`, `FINALITY_CANDIDATE`,
  plus the null/unknown/contested/multi-level/fork/hierarchy-revision aggregates.

## 1. Completion-rival slate (declared before running each case)

Each case must survive **all** applicable rivals or the typed verdict is
withheld:

1. **Access-relabel rival** — "this is only a change in what is readable/
   reachable" (the ocap ambient-authority / observability rival).
2. **Resource-frame rival** — "this is only a change in budget."
3. **Record-formation rival** — "this only created/erased a record; access and
   capability are unchanged."
4. **Fixed-family disclosure rival** — "nothing changed; a pre-existing family
   member was merely disclosed/relabeled."
5. **Domain-incumbent rival (per domain)** — the established framework that
   already owns the domain produces the verdict *without* the P2C ladder (ocap
   for security, control theory for dynamics, HP for causation, ...). **If the
   incumbent's own vocabulary yields the same or a sharper verdict, transfer
   FAILS by definition** — the ladder added nothing.

## 2. Abstention-forcing evidence list (must ABSTAIN if any is missing)

Honest abstention is required — not a low-confidence guess — when any of:

- no matched before/after pair at a fixed frame;
- no fixed resource budget / normalization frame;
- no operational task oracle (task is narrative, not checkable);
- the strongest completion rival cannot be run on the available evidence;
- a pure relabeling of the two endpoints changes the computed verdict;
- the domain-incumbent rival is not even representable in the supplied evidence.

## 3. [E] / [F] controls (evidential vs falsifying checks)

- **[E] evidential checks** (must pass, headline count): typed verdict computed;
  label-swap invariance holds; the normalized-vs-raw task split is explicit; each
  declared rival was actually run; abstention triggers fire on withheld cases.
- **[F] falsifying controls** (must *fail* as designed — a passing [F] kills the
  run): access-relabel overclaim rejected; resource-frame overclaim rejected;
  record/access conflation rejected; incumbent-produces-same-verdict control
  (if this control *passes*, transfer FAILS); finality-from-irreversibility
  overclaim rejected.
- Headline is reported as `N [E] + M [F]` with the strict TEF linter, matching
  existing P2C fixtures.

## 4. Per-domain rival forecasts (default: TRANSFER FAILS)

| # | Domain | Incumbent rival (subsumer) | Candidate case shape | Default forecast |
|---|---|---|---|---|
| **1** | **SECURITY** | **object-capability** (capability vs ambient authority; confused deputy) | granting/revoking a capability token vs widening an ACL vs minting a record/log; does the instrument separate `ACCESS_CHANGE` (ACL/ambient) from `CAPABILITY_ENLARGEMENT` (unforgeable authority) *and* from `RECORD_FORMATION` (audit log) in a way ocap's 2-way capability/ACL split does not? | **TRANSFER FAILS** — ocap already separates capability from access; the extra P2C value must come from the *records/finality* levels or it is nothing. |
| 2 | COMPUTATION / SYSTEMS | control theory (reachability/observability) | adding a sensor (observability↑) vs adding an actuator (reachability↑) vs logging state | TRANSFER FAILS — Kalman decomposition already types this. |
| 3 | INSTITUTIONS / GOVERNANCE | HP causation + records law | a rule change that alters who-can-do-what vs what-is-recorded vs what-is-settled/final | TRANSFER FAILS — pending a `FINALITY_CANDIDATE` the incumbents can't type. |
| 4 | BIOLOGY | dynamical-systems / information theory | a regulatory switch: fixed-family dynamics vs possibility-family change | TRANSFER FAILS. |

Domains 2-4 are named for completeness; **only domain 1 is authorized to run**
under this skeleton (genre gate: security-first, cheapest falsification).

## 5. Program-level falsifier (declared now, before any run)

> **If, on the SECURITY domain, the P2C instrument produces no typed verdict
> that object-capability security's own capability/ACL/log vocabulary cannot
> produce at least as sharply — AND the same holds on one second non-physics
> domain — then the methodology adds no cross-domain diagnostic power. Record
> `NOTHING-NEW` (methodology), fire the North Star's transfer falsifier, and do
> not build domains 2-4.**

Conversely, a single security case where the instrument cleanly types a
`RECORD_FORMATION` / `ACCESS_CHANGE` / `CAPABILITY_ENLARGEMENT` three-way split,
or a `FINALITY_CANDIDATE`, that ocap's native vocabulary conflates or cannot
express, is the first evidence lifting the grade off `NEW-FRAMING-ONLY`. That
case — and only that case — would justify building the remaining domains.

## Non-claims

- This is a skeleton: no fixture is built, no case is run, no verdict is
  reached. The defaults above are predeclared so a later run cannot HARK them.
- Producing this skeleton is not a claim promotion and moves no source truth,
  capability, finality, canon, or public posture.
