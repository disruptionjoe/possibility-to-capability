# Blocked Intake Preflight Contract v0.1

Status: provisional repo-owned interface. It is not a source verdict, an
accepted packet, or a substitute for the Neutral Eight-Gate Run Contract.

## Purpose

This contract makes an absent source-issued packet a deterministic intake
result. It records what the receiver could inspect at one immutable source
revision and then stops at provenance. It exists because an informal
`NOT_YET_IMPORTABLE` note is too easy to misuse later as permission to fill in
the missing wrapper from source narratives.

The preflight is receiver-owned. It never changes the source inventory, grades,
claim register, packet status, or scientific meaning.

## Terminal semantics

The contract applies only when source issuance is absent:

- no source-issued v0.1 or v0.2 packet identifier or packet object exists;
- no source-issued canonical manifest exists;
- no source-issued manifest, packet, or bundle digest exists; and
- the receiver used one immutable commit and tracked Git objects only.

In that state:

- the provenance preflight is `RUN` and `BLOCKED`;
- a receiving independence assessment is `NOT_ADMISSIBLE`;
- a full gate run is `NOT_ADMISSIBLE`;
- transition diagnosis is `NOT_ADMISSIBLE`;
- construction through neutrality are projected `BLOCKED` and `NOT_RUN`; and
- observed method artifacts cannot be reassembled into a receiver-owned method
  count, convergence finding, or source-issued independence structure.

`BLOCKED` is not `FAIL`, `PASS`, or `INDETERMINATE`. `NOT_RUN` means no
substantive judgment occurred. This is especially important for capability,
finality, No-Artificial-Success, and neutrality: the preflight establishes no
result at those levels.

## Contract-version roles

The record keeps three facts separate:

- `source_request_contract_version` is the version actually sent to the source;
- `current_receiver_preferred_contract_version` is the version the receiver
  would prefer for a newly issued packet now; and
- `checked_contract_versions` names the versions whose identifying artifacts
  were searched for at the pinned source revision.

Checking or preferring v0.2 does not retroactively turn a v0.1 request into a
v0.2 request.

## Immutable-source rule

The inspection mode is `git_object_database_tracked_only`. A record must pin a
40-character commit and the blob identity of every inventoried artifact. A
branch name, moving `HEAD`, dirty working-tree file, untracked roadmap, mailbox
message, or local plan cannot supply source truth.

Mailbox receipts may explain why issuance was expected or deferred. They are
routing context only and are not included in the source inventory.

## Source-status preservation

The record pins source artifacts and their source metadata without assigning a
receiver grade. It separately preserves the source claim-register status and
the open/unchanged status of named residuals. A blocked wrapper is not evidence
against the source research; it is evidence that the receiver lacks the
source-owned provenance object required to assess it.

## Digest firewall

When issuance is absent, all packet, manifest, and bundle identifiers and
digests are JSON `null`, and `claimed_digest_values` is empty. A receiver may
not hash a source tree, selected artifacts, a mailbox request, or a locally
assembled JSON object and present that digest as source-issued.

## Unblocking v0.2

The source would need to issue all of the following as one frozen bundle:

1. a Frozen-Packet v0.2 JSON object with every root field required by
   `packets/schema/frozen-packet-v0.2.schema.json`;
2. every raw source, method, premise, verification, and joint-argument blob
   named by that object;
3. a canonical `ptc-frozen-bundle-v1` manifest over those raw bytes; and
4. matching source-issued `manifest_digest`, `packet_digest`, `bundle_digest`,
   and compatibility `digest` values.

The packet must carry, rather than invite the receiver to infer, the exact
source question, construction forks, assumptions, quantifiers, per-method
results and grades, premise/dependency structure, shared premises, source claim
and independence wording, alternatives, residuals, nonclaims, verification,
interfaces, and unchanged source status.

Once such a packet exists, the receiver runs the v0.2 bundle validator first,
creates a separate non-upgrading Receiving Independence Assessment only after
the source packet passes, and only then creates an Eight-Gate Run. The blocked
preflight remains as historical evidence and is superseded by a new intake
record; it is never rewritten into a pass.

## Grade, nonclaims, and reopening

- Grade: deterministic receiver-owned provenance preflight over an immutable
  tracked source snapshot.
- It establishes packet absence at the pinned revision, not timeless absence.
- It does not evaluate GU, its five methods, their convergence, independence,
  physical capability, finality, or neutrality.
- Reopen only on a newly pinned revision containing a source-issued candidate,
  or if the recorded immutable tree or blob inventory is shown incorrect.
