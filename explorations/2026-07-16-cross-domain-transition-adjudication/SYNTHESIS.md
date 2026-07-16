---
artifact_type: exploration
status: complete
governance_role: cross_domain_transition_adjudication
constitutional: false
created: 2026-07-16
---

# Cross-domain transition adjudication: TAF-001 transfer

## Question

Can P2C's existing typed change discipline classify a source-grounded
nonphysics transition without changing the hierarchy's meanings, importing a
source verdict, or collapsing source-native task reconstructibility into P2C
capability?

## Evidence Used

The run uses the already imported, source-frozen `TAF-001` packet read-only:

- source owner: Time as Finality
- packet: `packets/imports/TAF-001/`
- source status: exploration tier / formal-only finite model
- receiver status: P2C-owned provisional diagnosis only

The source packet's facts are the paired interventions over one finite record
model:

| intervention | source-side change | frozen task delta |
|---|---|---|
| ALPHA | holder access enlarged, record inventory and graph fixed | tau2 becomes achievable; tau5 becomes unachievable |
| BETA | new record-formation events, holder access fixed | tau3 becomes achievable |

TAF deliberately does not classify these under P2C's hierarchy. That is the
receiver's job and does not change TaF truth.

## Fixture

`tests/cross_domain_transition_adjudication.py` builds two receiver-owned
Transition Diagnosis v0.1 assessments from the frozen packet:

1. ALPHA is supplied as an access-level intervention with source-native task
   deltas quarantined from P2C capability.
2. BETA is supplied as record formation under fixed holder access.

The fixture then runs the unchanged `tests/classify_transition.py` evaluator,
checks label-swap neutrality, and executes three failing-direction controls:

- ALPHA capability overclaim;
- BETA access relabeling;
- finality overclaim from irreversibility/settlement vocabulary.

Result:

```text
EVIDENTIAL CHECKS (headline): 7 [E] + 3 [F] = 10
ALPHA: ACCESS_CHANGE / ['ACCESS_CHANGE']
BETA:  RECORD_FORMATION / ['RECORD_FORMATION']
```

## Verdict

`CROSS_DOMAIN_TRANSFER_PASS_SCOPED`.

At exploration tier, the same P2C transition-diagnosis machinery that supports
physical witness work can also classify a nonphysics source packet without
analogy-only substitution:

- ALPHA is an `ACCESS_CHANGE`, even though TaF-native reconstructibility has a
  nonmonotone task delta.
- BETA is `RECORD_FORMATION`, not an access edit, because new records/events
  are formed while holder access is fixed.
- Neither branch becomes P2C `CAPABILITY_ENLARGEMENT`.
- No finality verdict is licensed.

This is a real transfer check, not a broad cross-domain theorem. It transfers
the discipline to one frozen finite record-system packet.

## Limits

- The evidence is a designed finite TaF model, not a real distributed system,
  market, institution, biological case, or AI-system deployment.
- The fixture does not decide whether TaF reconstructibility should ever count
  as P2C capability under a different normalization frame.
- The ALPHA task delta remains nonmonotone and important: task achievement can
  change when access changes. This run only blocks the shortcut from that fact
  to a capability verdict.
- The result does not discharge Rank-2 successor work. It uses the same source
  packet for a different purpose: typed transfer of the hierarchy, not the
  preregistered access/capability boundary outcome.

## Next

The immediate cross-domain item is advanced for this input. The next highest
frontier returns to `P2C-REAL-PHYSICAL-WITNESS` Alternate B: topological-order /
gamma-log-D witness reach swing, unless a new source-grounded nonphysics packet
with stronger capability-side evidence arrives first.
