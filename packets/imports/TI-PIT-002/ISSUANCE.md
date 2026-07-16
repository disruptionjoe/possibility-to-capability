# TI-PIT-002 Issuance Record

- **Decision:** ADOPTED-AND-ISSUED by the Temporal Issuance steward, 2026-07-16 (round-2 adjudication, RUN-0166; round 1 was RUN-0165 NOT-YET-ISSUABLE).
- **Origin:** re-proposal `system/mailboxes/temporal-issuance/20260716-tipit02-corrected-draft-v0.2-reproposal.md` (archived with processing receipt), carrying the P2C-authored corrected draft TI-PIT-02 v0.2, committed at `possibility-to-capability` commit `9652474f97681e62d0173b4cfea6e78776d52a99` (`explorations/2026-07-16-tipit02-reissuance/`).
- **Content revision (commit 1, pinned as `source.revision`):** `61fc4e6f8530d8620c0a3b66446c2e28e4fda164`
- **Semantics source revision (TI-FORMAL-OBJECT.md frozen from):** `3c7d1fc1416576635aca1550e912deb240046ae8`
- **Digests (ptc-frozen-bundle-v1):**
  - `manifest_digest`: `f96c8443dbf0baf8d8d4692b254d4fe158634600b512b532378bc4ce567919af`
  - `packet_digest`: `cbf8dceda29c14364398da2ce2c14b93385953d4592aa3c0c23d703e29b44d19`
  - `bundle_digest` (= `integrity.digest`): `9c8e4ec77ca57a2f349057f89613d4e0cb45e50979af01385353d66c19589c39`
- **Schema:** validated against the receiver's frozen-packet v0.2 semantics via `possibility-to-capability/tests/validate_frozen_packet_v0_2_contract.py::validate_packet` with this directory as `bundle_root`: zero errors.

## Corrections applied at issuance (TI steward acts, content untouched)

1. **Packet ID:** `TI-PIT-02` -> `TI-PIT-002` (the receiver contract's packet-id grammar requires three or more digits; the author left final ID and placement to TI, semantics body section 2.8).
2. **Placement:** `exports/packets/` under TI's source-issued packet convention v1 (adopted this issuance, modeled on TaF's TAF-001 prior art), not the author-suggested `interfaces/` path.
3. The semantics body is frozen byte-identical to the author's committed v0.2 draft, including its DRAFT-FOR-SOURCE-ISSUANCE header; this issuance record supersedes that draft status. Freezing the exact authored bytes preserves authorship and hash provenance (P2C remains the author of record; TI is the issuer).

## Steward verification performed before adoption (per-deficiency, against RUN-0165)

1. **Native-signature fidelity (RUN-0165 deficiency 1): cured.** Section 2.1 quotes the seven-component RUN-0081 `OnlineIssuance^LC` signature exactly (byte-checked against `FORMAL-OBJECT.md`); `Ext_n` is declared TRIVIALIZED with an honest instantiation (finite `(e, w)` pairs over the gate-clause `CandExt`, no categorical structure claimed or exercised); `Glue_n` is declared PRESENT-NOT-EXERCISED rather than dropped; gate-clause-2 witnesses `w_n : Adm_n(e_n)` are explicit per-event fields `(stage, token, w)` in `tau_n`, visible in the code and every output record. The k-free witness design is verified: `w = (novel, length, b_count)` is a function of `(e, Gamma)` alone, so projection carries it without leaking k, and all v0.1 computed values are preserved (issued 9/13; records 2/9/2/5/6; decidable 25/30/25/30/29).
2. **Reproducible artifact in hand (deficiency 2): cured.** The committed script was re-run by this steward: exit 0, empty stderr, stdout byte-identical to the section 2.4 block; `sha256(ti_pit_02_fixture.py) = 8888afc78847a2f9930ed453e2a1e16b62b2e647542cb23cc99eb15230ea4bed` (10371 LF bytes) and `sha256(output, LF) = a14642b7cd27bcce510bbe28f5112d93b13db415434ae2f3d416048ec4a62475`, both matching the author's pinned values; the inlined section 2.3 code block is byte-identical to the committed artifact; the mailbox-inlined draft is byte-identical to the committed packet file; the committed blobs match P2C commit `9652474f` exactly.
3. **Frame-blindness (deficiency 3): cured.** Full scan of packet, fixture, and mailbox message: no contending-frame citations remain; the only frame-adjacent text is the frame-blindness statement itself and the referee's quarantine carried as a frame-neutral authorship restriction (protective, not spoiling); former assumptions 2 and 3 are restated as a declared free parameter and a neutral out-of-model provenance fact.
4. **Failing-direction controls (deficiency 4): cured.** The formerly tautological ALPHA-invariance check is honestly tagged `[T]` (the compared sets are literally the same object; excluded from the evidential headline) and protected by a real `[F]` probe (k=1 vs k=2). Six `[F]` probes verified to flip their protected comparisons on the same code paths (perturbed pairings k=1/k=2 and k=0/k=1, perturbed threshold L=3, identity pairing, quiescence at stage 3, perturbed MAXLEN=5); exit 0 requires all six to fail. The receiver's `tests/tef_check_tag_linter.py --strict` passes: 1 [T], 4 [E], 6 [F], 0 untagged, 0 violations.

Minor RUN-0165 items also confirmed applied: "provably quiescent" reworded to machine-checked; files-consulted arithmetic correct.

## What issuance commits TI to

Only the machine-checked computed facts of the frozen fixture, at exploration tier, formal-only grade, on a designed finite instance that is **absorbed under the RUN-0081 gate clause 4** and carries no physical or source-issuance significance. No TI claim status changes (TI-C019 formalizing, TI-C020 parked, `Issue[S]^physical: false` all untouched). No receiver-side classification is endorsed (`authority_transfer = false`). The authorship-quarantine restriction in `nonclaims` survives issuance.
