---
artifact_type: exploration
status: provisional
claim_grade: source-grounded preflight
created: 2026-07-20
lane: 1
---

# Co-flip / holonomy boundary preflight

## Result

`ABSTAIN_PACKET_NOT_ADJUDICABLE`.

The frozen GU packet `GU-COFLIP-HOLONOMY-FREEZE-2026-07-20` at commit
`32e3603f12aae3fc76298534c47a204b5584b171` is a valid qualified candidate
input, but it cannot yet be encoded honestly in the existing P2C boundary
discriminator. This is a bounded negative result about discriminator
admissibility, not a rejection of GU's matrix-grade result.

## Construction and assumptions

The preflight uses only the packet's explicit identity and gap ledger. It does
not rerun GU's source probe, import the packet as P2C truth, or construct the
proposed W1-W3 ladder. The source packet is treated as frozen GU-owned evidence.

The existing discriminator requires settled Boolean values for matched
resource frame, matched access frame, matched task delta, and completion
absorption. The packet expressly supplies no transition frame, intervention
menu or resource budget, native response, task delta, or completion-rival
adjudication. Encoding those unknowns as `true` would invent a matched frame;
encoding them as `false` would misstate absence of evidence as a demonstrated
frame change. Neither branch is neutral.

## Gate read

- Provenance: source freeze and immutable revision are present; independent
  source identity remains absent by the packet's own statement.
- Construction: the matrix-grade holonomy construction is named, but no P2C
  before/after transition construction is supplied.
- Formation: blocked on the missing transition and task frame.
- Completion/null: not evaluated; no strongest completion rival is supplied.
- Capability: not evaluated; no matched task delta exists.
- Finality: not reached.
- Neutrality and no-artificial-success: preserved by abstaining before filling
  missing fields with favorable or unfavorable defaults.

## Verification

`tests/coflip_holonomy_boundary_preflight.py` deterministically checks the
source pin, the seven missing adjudication fields, the Hamiltonian nonclaim,
and the required abstention. Two failing-direction controls show that an
unfrozen source is rejected and a complete packet proceeds rather than
abstaining. Expected headline: `10 [E] + 2 [F] = 12`, exit 0.

## Scope and reopen condition

This result does not move GU source truth, packet-import status, capability,
finality, canon, claim status, or public posture. It would be falsified or
reopened by a frozen input that supplies independent identity plus a declared
before/after transition, matched resource and access frames, task delta, native
response, and strongest completion rival. A P2C-owned preregistration may
specify those fields, but it must not claim that doing so retroactively creates
source-independent provenance for this GU packet.
