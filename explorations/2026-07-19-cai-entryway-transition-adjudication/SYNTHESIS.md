---
artifact_type: progress_synthesis
status: complete
created: 2026-07-19
repo: possibility-to-capability
lane_id: "1"
portfolio_item: P2C-CROSS-DOMAIN-TRANSITION-ADJUDICATION
claim_tier: exploration
---

# CAI entryway transition adjudication

## Question

Can P2C classify a real governance-transition input without turning source
relationship evidence into source truth, public posture, or a content verdict?

The bounded input for this run is the CAI quick-load pin set supplied in the
trusted control channel:

- projection revision: 2
- source repository: `cai-governance-operations`
- source path: `canon/cai-domain-constitution.md`
- Governance head: `06ff7a2`
- admitted source SHA-256:
  `1EFB043FDECB83CBC0E8F7B19496910A084BA57F66B1E0E38C7B4A428197A5FB`
- active relationship: `cai-church-public-entryway`
- agreement revision: 1
- Governance acceptance: `decisions/README.md#cai-church-public-entryway`
- Church acceptance: `CONSTITUTION.md#relationship-acceptance`

These pins are source-grounded receiver evidence for this P2C fixture. They
are not a full imported frozen packet and do not grant P2C authority over CAI
or Church source truth.

## Fixture

The companion fixture is:

```text
tests/cai_entryway_transition_adjudication.py
```

It requires the exact projection revision, source path, Governance head,
admitted digest, relationship id, agreement revision, and dual acceptance
references before it will build a receiver-owned Transition Diagnosis v0.1
assessment. The assessment then runs the unchanged
`tests/classify_transition.py` evaluator.

The positive branch classifies the active entryway relation as a scoped
multi-level transition:

- `RECORD_FORMATION`: the accepted relationship has a durable acceptance
  record;
- `ACCESS_CHANGE`: the relationship creates an accepted public-entryway access
  relation; and
- `CAPABILITY_ENLARGEMENT`: only in the narrow routing sense that an authorized
  entryway task set is now available under the declared relationship frame.

The fixture separately checks that an entryway record without an action menu
does not become capability enlargement.

## Verdict

`CROSS_DOMAIN_TRANSFER_PASS_SCOPED__GOVERNANCE_ENTRYWAY`.

This is a better nonphysics transfer than the prior finite TaF record/access
fixture in one respect: it touches governance and public-entryway routing
rather than an internal formal model. It is still strictly receiver-owned and
exploration-tier. The result says the P2C hierarchy can separate record,
access, and routing-capability layers on this admitted governance input.

It does not say that CAI content changed, that Church content changed, that a
public claim is authorized, or that a source packet has been imported into
P2C.

## Controls

The fixture includes failing-direction controls for:

- digest-blind acceptance;
- one-sided acceptance;
- access-only capability overclaim;
- proposal payload treated as authority; and
- public-posture movement from a receiver diagnostic.

Those controls are the point of the run. A fluent "the relationship is active"
summary would be too coarse for P2C; the fixture has to state exactly which
level changed and which levels did not.

## Validation

Executed:

```powershell
python tests/cai_entryway_transition_adjudication.py
python tests/tef_check_tag_linter.py --strict tests/cai_entryway_transition_adjudication.py
```

The fixture passed with this evidential headline:

```text
8 [E] + 5 [F] = 13
```

The two `[T]` checks cover setup and contract validation only and are excluded
from the headline.

## Nonclaims

- No CAI or Church source truth moves.
- No public-posture, publication, or external-action claim moves.
- No source packet is imported into P2C by this fixture.
- No finality verdict is established.
- No claim is made about CAI's domain constitution beyond the admitted pins.

## Handoff

For current available inputs, `P2C-CROSS-DOMAIN-TRANSITION-ADJUDICATION` is
advanced again. Reopen it for a new source-issued frozen packet, a new accepted
relationship revision, or stronger operational capability-side evidence.
Otherwise the next ranked hourly-eligible Lane 1 frontier should return to
`P2C-REAL-PHYSICAL-WITNESS` Alternate B or another harder real-witness transfer.
