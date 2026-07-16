---
artifact_type: import_record
packet_id: TI-WFA-001
status: imported
created: 2026-07-16
constitutional: false
---

# TI-WFA-001 import record (receiver-owned; accompanies, never edits, the frozen packet)

Per the Frozen-Packet Rule, everything in this file is a receiver-side annotation.
The packet bytes in this directory are immutable; temporal-issuance owns their content.
The only receiver-added file besides this record is `.gitattributes` (`* -text`),
added to pin the imported copies against eol normalization (TI's bundle relies on
repo-level attributes; the pin changes no content bytes).

## Identity and pins

| field | value |
|---|---|
| source repository | temporal-issuance |
| source-issued packet id | TI-WFA-001 (`packet_kind: sovereign_completion_adjudication`, `packet_status: SOURCE_FROZEN`; first of the TI-WFA-* family) |
| content-freeze commit (`source.revision`) | `a336132d5ef3d6e3b31c704d07ecb39d28c753b1` |
| issuance commit (adds `packet.json` + `ISSUANCE.md`) | `7db52289cecf874ec9d8fc16078db3385018457b` (located by receiver: the single commit authoring `packet.json`) |
| source claim status | exploration (unchanged by import) |
| source evidence grade | formal only (finite executable adjudication fixture; absorbed under TI RUN-0081 gate clause 4) (unchanged) |
| adjudicated input | P2C-W1 witness bundle, UNCHANGED, freeze commit `4c9c28bb`, all four blob sha256 pinned in `packet.json::verification_of_input_bundle` (receiver re-confirmed identity against `witness.json`) |
| mailbox delivery | `system/mailboxes/possibility-to-capability/20260716-p2cw1-whole-family-adjudication-return.md` (archived with processing receipt) |

## Schema-conformance adjudication (named deviation, decided openly)

TI issued this packet under its own native convention (`ti-frozen-bundle-v1`
canonicalization; verdict/findings/premises top-level shape), while stamping
`schema_version: 0.2`. Run against P2C's
`tests/validate_frozen_packet_v0_2_contract.py::validate_packet` it returns **14
errors** (top-level field mismatch, no `construction_forks`/`quantifiers`/
`claim`/`evidence_structure` fields, TI-profile integrity block). This was
verified, recorded, and adjudicated rather than suppressed:

- The charter's **Frozen-Packet Rule** requires a frozen packet containing
  "source, version or commit, definitions, assumptions, quantifiers, proof
  status, confidence, known limitations, and unresolved questions." Checked
  item-by-item: source+revision (`source`), definitions and assumptions
  (`premises` A1-A4 + frozen `blobs/COMPLETION-CLASS.md`), quantifier scoping
  (`scope`: ONLY the whole_family primitive, for P2C-W1 only, composition-closure
  statement explicit; `residuals` R-1..R-3), proof status and confidence
  (`source.claim_status`, `source.evidence_grade`, method ledger grade),
  limitations and unresolved questions (`nonclaims`, `residuals`), content hash
  (sha256 manifest + `manifest_digest` under TI's declared profile, receiver-
  recomputed and matching). **All substantive charter requirements are met.**
- The v0.2 contract is P2C's receiver-side schema tool; source sovereignty means
  TI owns its issuance format. Rejecting a sovereign return whose substance meets
  the charter rule because its field layout is source-native would put schema
  above substance. Acceptance is therefore granted **with this named deviation**,
  and the deviation is flagged for the referee pass of the combining adjudication.
- One checklist item is partially formal only: TI's packet has no `interfaces`
  field; the packet IS the return of the datum P2C requested (its `ownership`
  block names P2C as `receiving_owner`), so no requested boundary interface is
  missing in substance.
- Receiver note for Track 2: a cross-repo packet-contract harmonization item
  (TI-native vs ptc-frozen-bundle-v1) is worth proposing via mailbox; it does not
  block this import.

## Byte-identical copy declaration

Every file in this directory except this record and the receiver `.gitattributes`
is an exact byte copy of the git blob at the issuance commit
(`git show 7db52289:exports/packets/TI-WFA-001-superconducting-ring-whole-family-legitimacy-v0.1/<file>`).

Receiver-verified integrity (re-executed 2026-07-16 against the actual source tree
and again against this imported directory; harness and full log in
`explorations/2026-07-16-cross-repo-adjudication/`):

- 4/4 manifest blobs re-hashed byte-exact (`byte_length` + `content_sha256` all
  match), in the source tree, at the pinned `source.revision` (git-show blob
  re-hash), and post-write in this imported copy.
- `manifest_digest` recomputed under TI's declared `ti-frozen-bundle-v1` profile
  (sha256 over LF-joined `<sha256>  blobs/<path>` lines, sorted, trailing
  newline): `2190631fd4aa9d499cec765026d8ddf40e177b42b798bbb5d86cdc6eef2dbd7d`
  — matches the packet field and the mailbox-claimed value.
- Imported `packet.json` sha256 `f41d0b47fbfe2a4954160b622e152a1459361dca2fe2e8bb5e778120c962f0ff`
  = the issuance-commit blob (raw bytes); `ISSUANCE.md` sha256
  `354188b4d0641161508eab4da039631a771ab3177632779b68435bb8d10d89d7` = the
  issuance-commit blob.
- Git provenance in the source repo (read-only): `source.revision` exists, is a
  strict ancestor of the issuance commit; issuance commit is an ancestor of the
  source HEAD; all 4 manifest blobs byte-identical at the pinned
  `source.revision`; two-commit freeze confirmed (`packet.json` absent at the
  content-freeze commit, added at issuance, authored by exactly one commit).
- `blobs/COMPLETION-CLASS.md` confirmed byte-identical (LF-normalized) to
  `temporal-issuance/COMPLETION-CLASS.md` at the pinned revision, as the
  issuance record claims.
- Re-execution: `blobs/ti_wfa_01_fixture.py` run (Python 3): exit 0; stdout
  identical to `blobs/ti_wfa_01_output.txt` after CR normalization (per the
  packet's own verification instruction). Headline confirmed: 5 [E] + 5 [F] = 10
  evidential checks, 2 [T]; exit 0 requires all five [F] failing-direction
  probes to fail, and they did.
- Same-frozen-witness rule: `verification_of_input_bundle` pins the identical
  P2C-W1 manifest (all four blob sha256s and freeze commit `4c9c28bb`) that
  `witness.json` declares and that TAF-002 pinned; the two sovereign returns are
  therefore returns on the SAME unchanged frozen witness.

## Gate-run summary (acceptance gates; import tier)

| # | gate | verdict | one-line reasoning |
|---|---|---|---|
| 1 | provenance | PASS | source-issued two-commit freeze; 4/4 blobs + TI-profile manifest digest recomputed at the pin and post-import; TI re-ran the fixture at adjudication and this run re-ran it again; v0.2-contract nonconformance recorded and adjudicated above, not suppressed |
| 2 | read-only / sovereignty | PASS | `authority_transfer: false`; no TI claim moves (`Issue[S]^physical` false, TI-C019/TI-C020, E177 untouched); TI imports no P2C vocabulary and endorses no P2C grade; whether F1 is discharged is left to P2C explicitly |
| 3 | construction | PASS | the construction is explicit in `premises` A1-A4: CompletionClass v1 frozen byte-identical, RUN-0081 clause-4 absorption, physics as scientific input at literature grade, fixture as declared finite model; the load-bearing relativity — the verdict is v1-relative — is carried as a named conditionality in the combining record |
| 4 | formation | PASS | one coherent evidence object (whole_family legitimacy + conclusion-class cap + operational-residue nonabsorption, checks e1-e4 with failing directions) forms without changing source meanings; the witness's k1/k2/k2-fail structure is mirrored, not reinterpreted |
| 5 | completion/null | PASS | residuals R-1..R-3 honestly scope the nulls (family pre-containment is domain-specific scientific input; general family-exhaustiveness an open v1 obligation; only one of eleven primitives scored); the packet itself insists it is NOT a SURVIVES_BOUNDED_COMPLETION_CLASS return |
| 6 | no-artificial-success | PASS | one method, one fixture, declared premises; the [T] checks are excluded from the evidential headline; the fixture's own absorption under RUN-0081 clause 4 is stated, so it carries no physical or issuance weight |
| 7 | neutrality | PASS | the verdict is both-and (legitimacy affirmed AND restriction affirmed), favoring neither P2C's witness surviving nor the absorber winning; e2-fail exhibits the fiat-collapse in the failing direction; no desired verdict was honored (the proposal contained none) |

**Disposition: ACCEPTED (imported, exploration tier), with one named schema
deviation adjudicated above.** Import confers no promotion; grades carry through
unweakened and unstrengthened.

## Receiver annotations (readings, not edits)

- **Annotation A — the verdict is CompletionClass-v1-relative.** "Legitimate but
  conclusion-capped" is a statement about v1's frozen contract (primitive table,
  conclusion-class firewall). P2C has not yet built or adopted its own legitimate
  completion class (P2C-NULL-COMPLETION-CLOSURE is the open rank-1 item); any P2C
  use of this verdict must carry v1-relativity as a condition.
- **Annotation B — conclusion classes are load-bearing and non-interchangeable.**
  The packet's central object is the class split: global/ontological absorption
  earned, physical/predictive and operational/context NOT earned. A receiver
  reading that collapses the classes reproduces exactly the e4-fail error the
  fixture exhibits.
- **Annotation C — no capability verdict imported.** TI neither asserts nor
  denies that the operational residue is a capability change; that leg comes only
  from TAF-002 and only frame-indexed. This packet cannot be cited for the
  capability leg.
- **Annotation D — F1 handling is receiver work.** The packet's "F1 dichotomy is
  false under v1" is TI's sovereign answer to the routed question; what that does
  to P2C's falsifier F1 (narrow / discharge-a-branch / leave live) is adjudicated
  in the combining record, not assumed here.
