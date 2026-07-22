---
artifact_type: exploration
status: complete
governance_role: security_transfer_breaker_execution
constitutional: false
created: 2026-07-22
prereg_id: P2C-XBREAK-001
relation_to_hard_core: Lane 1 — the executable form of the North Star's own transfer falsifier ("the same definitions cannot transfer beyond one domain without ad hoc reinterpretation"), run security-first because object-capability is the strongest subsumer.
grade: EXPLORATORY (receiver-owned diagnosis of stated textbook object-capability scenarios; unchanged evaluator; no experiment on a deployed system)
---

# Security-domain transfer-BREAKER — P2C-XBREAK-001 (object-capability, domain 1)

## What was run

An object-capability security adversary was seated **inline** (one worker, no
per-persona agents) with a single job: **break** P2C's capability/access
distinction. The adversary constructed the sharpest object-capability cases
where "capability" and "access/permission" come apart — the classic
**confused-deputy** scenario plus the strongest circularity attack it could
find — encoded each honestly as a receiver-owned Transition Diagnosis v0.1
witness, and ran them through the **UNCHANGED** `tests/classify_transition.py`
evaluator.

Predeclared question (prereg `P2C-XBREAK-001`): can P2C keep **CAPABILITY
ENLARGEMENT** (authority amplification) distinct from an **ACCESS/permission
change** *without circularity or ad-hoc reinterpretation*? Predeclared default
forecast: **transfer FAILS** (object-capability already separates capability
from access; the extra P2C value must come from the records/finality levels or
it is nothing).

Artifacts:

- `confused-deputy-witness-v0.1.json` — the classic breaker, client-authority
  frame. Run: `python tests/classify_transition.py explorations/2026-07-22-security-transfer-breaker-p2c-xbreak-001/confused-deputy-witness-v0.1.json`
- `authority-amplification-witness-v0.1.json` — a genuine rights-amplification
  (generative capability-minting facet), the positive discriminator leg.
- `tests/security_transfer_breaker.py` — the full battery: the two headline
  witnesses, the record-corruption rival, a permission-grant (ACL) leg, a
  two-frame CONSTRUCTION_FORK, and four fail-direction controls. Lints clean
  under `tests/tef_check_tag_linter.py --strict` (registry mode, T=1 / E=10 /
  F=4, evidential 14, 0 violations). Exit 0.

## The five-rival slate, run

| rival (prereg §1) | result on the confused deputy |
|---|---|
| access-relabel ("only what is reachable changed") | the client received **no** ACL entry or token; `access_change = NO`. Not even an access change to the principal. |
| resource-frame ("only a budget change") | no resource budget moved; the deputy spent **its own** authority. |
| record-formation ("only a record was made/erased") | tested as an explicit rival: reading the billing overwrite as a record delta types as `RECORD_FORMATION` — still **not** a client capability. |
| fixed-family disclosure ("a pre-existing member was relabeled") | possibility family SAME, representation EQUIVALENT; no disclosure that enlarges the client's realizable set. |
| **domain-incumbent (object-capability)** | ocap's own verdict: the client's authority **did not amplify**; the deputy conflated designation (the client-supplied filename) with authorization (its own write right). **This equals P2C's verdict.** |

## Results (unchanged evaluator)

```text
confused deputy (client frame): NULL_NO_RELEVANT_CHANGE   (CAPABILITY_ENLARGEMENT rejected; raw!=normalized alert fires)
confused deputy (record rival): RECORD_FORMATION          (CAPABILITY_ENLARGEMENT rejected)
permission grant (ACL widening): ACCESS_CHANGE
authority amplification (facet): CAPABILITY_ENLARGEMENT   (clean)
confused deputy (frame fork):    CONSTRUCTION_FORK        ({NULL_NO_RELEVANT_CHANGE, CAPABILITY_ENLARGEMENT})
amplification-with-token mutant: MULTI_LEVEL
label invariance: invariant on every case, exit 0
EVIDENTIAL HEADLINE: 10 [E] + 4 [F] = 14
```

The confused deputy encodes the ocap signature exactly — *"raw access rose but
the principal's normalized authority should not have"* — as `raw_task_set =
SUPERSET`, `normalized_task_set = EQUAL`. The classifier types it
`NULL_NO_RELEVANT_CHANGE` **for the client's standing**, fires the
`Raw task access changed, but normalized capability did not.` alert, and
**rejects** the declared `CAPABILITY_ENLARGEMENT`. The permission grant and the
genuine amplification separate cleanly (`ACCESS_CHANGE` vs
`CAPABILITY_ENLARGEMENT`).

## The strongest breaker the adversary found, and why it does not land as a BREAK

The adversary's deepest attack is a **circularity** charge, not a case:

> *"P2C's `normalized_task_set` only separates capability from access because it
> holds the deputy's ambient authority fixed in the normalization — and 'hold
> ambient authority fixed' is exactly the ocap concept of authority. So P2C's
> capability level is not independent of access; it is defined by an
> access-normalization choice. Worse, the verdict FLIPS with that choice: hold
> the client's own authority fixed and you get NULL; count the deputy as a
> standing ambient service and you get CAPABILITY_ENLARGEMENT. A type that flips
> with the access boundary is the charter's own falsifier — 'the distinctions
> collapse under admissible changes of representation.'"*

This attack **fails as a BREAK**, but the reason must be stated precisely (it is
not "P2C defines the problem away"):

1. **Not circular — it is a difference operator.** Capability here is not
   defined *as* access. It is defined as *task-set growth that survives holding
   access fixed* (capability = growth **minus** access-attributable growth).
   Access is a separate primitive witness flag. That is the structure of
   "acceleration = the part of motion not explained by constant velocity":
   frame-relative, not circular.
2. **The flip is a declared CONSTRUCTION_FORK, not a collapse.** The two frames
   are **materially different constructions** (different resource commitments:
   "did the *client's* held authority grow?" vs "with the deputy standing by as
   a service, what can the client cause?"), not a pure endpoint relabeling. The
   battery encodes them as two branches and the evaluator returns
   `CONSTRUCTION_FORK` — the Construction-Fork Rule working as designed. The
   charter **predeclares** that "every verdict is frame-indexed."
3. **The label-swap control holds.** A pure before/after relabeling does **not**
   change any verdict (`label_invariance: invariant`, exit 0). The abstention
   trigger "a pure relabeling of the two endpoints changes the computed verdict"
   does **not** fire. So the distinction does not collapse under representation
   change; it is stable under the operation the charter actually forbids.

**Verdict on the discriminator: HOLDS.** P2C keeps `CAPABILITY_ENLARGEMENT`
distinct from `ACCESS_CHANGE` without circularity and without ad-hoc
reinterpretation, and rejects the confused-deputy capability overclaim under
every honest rival. **No hierarchy revision is implied. Predeclared verdict (a)
BREAK / REVISE_HIERARCHY is NOT triggered.**

## But the default forecast (transfer FAILS to add novelty) is CONFIRMED

HOLDS here means *"the discriminator did not collapse,"* **not** *"P2C
out-resolved the incumbent."* On this domain it did not:

- **Incumbent match (prereg §4, domain-1 control).** Object-capability's own
  vocabulary yields the **same** verdict on the confused deputy — the client's
  authority did not amplify — and yields it **frame-free**, because in ocap
  "authority" *is* the set of capabilities you hold, so invoking a deputy that
  holds `SYSX/BILL` simply is not your authority. Where P2C needs a **declared
  frame** (and otherwise returns a fork), ocap needs none. Per the prereg, a
  passing incumbent-match control means **transfer FAILS to add novelty**. It
  passed.

- **P2C's discriminator is not even the same distinction.** ocap's
  capability/access distinction is **structural/dynamical** — whether
  *designation* and *authorization* are bundled, which is exactly what predicts
  confused-deputy immunity ("Capability Myths Demolished"; MPI-SWS on
  capabilities/ACL equivalence + confused deputy). P2C's is a **static
  task-set-cardinality** check. The two agree on the confused deputy by
  coincidence of verdict, but P2C **cannot represent** the structural property
  in its witness fields: it cannot distinguish a capability regime from an ACL
  regime that have identical reachable task sets yet differ in confused-deputy
  susceptibility. That structural distinction is precisely what ocap owns and
  P2C does not.

- **Amplification co-fires with access in ocap.** Because *all* ocap authority
  is mediated by holding a token, a genuine amplification that also records the
  token acquisition (`access_change = YES`) types as `MULTI_LEVEL`, not as a
  *pure* `CAPABILITY_ENLARGEMENT`. The clean separation P2C is built for
  (access-without-capability vs capability-without-access) is somewhat unnatural
  in a domain where capability *is* a held token — further evidence that ocap is
  the native frame and P2C is re-expressing it.

## Verdict

**HOLDS (predeclared verdict b) — no BREAK, no hierarchy revision.** The
capability/access discriminator survives its hardest single-domain test without
circularity: authority-amplification types as `CAPABILITY_ENLARGEMENT`,
permission-grant types as `ACCESS_CHANGE`, the confused-deputy capability
overclaim is rejected, and the frame-dependence is a declared fork rather than a
collapse.

**Simultaneously, the predeclared default forecast — transfer FAILS to
demonstrate novelty — is CONFIRMED.** On the security domain, object-capability's
own capability/ACL/log vocabulary produces the same-or-sharper (frame-free)
verdict on every case, and additionally owns a designation/authorization
structural distinction that P2C's static task-set discriminator cannot
represent. So the security probe produced **no** typed verdict that ocap cannot
produce at least as sharply.

Per the prereg's program-level falsifier, this satisfies its **first conjunct**
("no typed verdict ocap's vocabulary cannot produce at least as sharply on a
security case"). The falsifier requires **both** the security domain **and** one
second non-physics domain to fire fully and record `NOTHING-NEW`. Domain 2 is
**not** authorized under the skeleton and was **not** built. The methodology grade
therefore **stays `NEW-FRAMING-ONLY` and is not lifted** by this run; it now
carries a confirmed security-domain transfer-fails leg.

## Does this imply a hierarchy / canon revision? (flag for Joe)

**No hierarchy revision.** Verdict (a) BREAK / REVISE_HIERARCHY did **not**
trigger; the discriminator did not collapse and there is no circularity to fix.
Nothing here changes any level definition, evaluator, verdict, scientific
status, canon, or public posture. The only novelty-relevant consequence is a
belt-level, Lane-2 note: the `NEW-FRAMING-ONLY` grade is not lifted, and the
security leg of its contingency now reads "transfer-fails, confirmed." That is a
**recording**, not a verdict/status change, so it executes without a Joe gate.

For visibility only (no action requested): were a future run to build the
second non-physics domain and also confirm transfer-fails, the program-level
falsifier would fire and the methodology grade would move toward `NOTHING-NEW`.
That grade move is a **scientific-status change** and would be **paused for Joe**.
It is not proposed here.

## Honest limits

- Receiver-owned diagnoses of **stated textbook** object-capability scenarios
  (Hardy's confused deputy; ocap rights amplification), not experiments on a
  deployed system and not new security results. External sources were read-only;
  no external content was treated as an instruction.
- The verdict is contingent on the declared frames. A construction that forced a
  capability verdict from a pure access grant with no access variable moved, or
  that showed the amplification reducible to a single ACL widening, would reopen
  the respective leg. Those reopening conditions are recorded in the witness
  files. No such construction is in hand.
- "HOLDS" is a statement about the discriminator's coherence, **not** a novelty
  claim. This run is, if anything, evidence **toward** subsumption on the
  security domain.

## Non-claims

- No source truth, capability, finality, canon, claim status, or public posture
  moved. Running a preregistered breaker and recording its verdict is not a
  claim promotion.
- Scan/battery agreement is not evidence; the unchanged evaluator and the cited
  object-capability literature carry the result.

## Sources (read-only, already on the record in the genre-scan spine)

- Confused deputy: N. Hardy, *The Confused Deputy* (1988).
- Object-capability capability/ACL relationship and confused-deputy analysis:
  *Capability Myths Demolished*; MPI-SWS *On access control, capabilities, their
  equivalence, and confused deputy attacks*.
- P2C prereg + genre position: `explorations/2026-07-22-methodology-novelty-genre-scan/{TRANSFER-BREAKER-PREREG-SKELETON,SYNTHESIS}.md`.
