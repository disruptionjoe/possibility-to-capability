# TI-PIT-02 re-issuance folder (2026-07-16)

Receipt for the re-authoring run that cures TI's sovereign NOT-YET-ISSUABLE
return of 2026-07-16 (four named blocking deficiencies) on the TI-PIT-02
draft-for-source-issuance.

## Contents

- `TI-PIT-02-draft-v0.2.md` — the corrected packet draft. Supersedes the
  TI-PIT-02 section of
  `explorations/2026-07-16-northstar-unblock/lane-C-frame-r-and-ti-case.md`
  (v0.1) as the proposal text; the v0.1 file remains unedited as the
  historical record with its governing referee report.
- `ti_pit_02_fixture.py` — the executable fixture, committed and pinned by
  content hash inside the packet
  (`sha256 8888afc78847a2f9930ed453e2a1e16b62b2e647542cb23cc99eb15230ea4bed`).
  Run: `python explorations/2026-07-16-tipit02-reissuance/ti_pit_02_fixture.py`
  (stdlib only, deterministic, exit 0). Lints clean under
  `python tests/tef_check_tag_linter.py --strict`.

## Cures applied (map in the packet's "Deficiency-cure map" section)

1. Seven-component RUN-0081 `OnlineIssuance^LC` signature quoted exactly, with
   a declared instantiated/trivialized map; `w_n` witnesses are explicit
   per-event trace fields.
2. Script inlined verbatim (splice-verified byte-identical to the committed
   file); true unabridged output embedded; real content hashes pinned.
3. Frame-blind: no frame cited, scored, or advocated; provenance facts
   restated neutrally; D1 quarantine carried as a frame-neutral authorship
   restriction.
4. Tautological check tagged [T] with no evidential weight; 4 [E] + 6 [F]
   checks including perturbation probes that flip every substantive
   comparison.

Blindness preserved: `experiments/rival-frames/` and
`explorations/2026-07-16-rank2-preregistration/` were not read by this run.

## Runway step status (Rank-2 runway, per SYNTHESIS.md)

- Step 1 (TaF and TI stewards adopt/issue their packets): **TI half
  re-proposed** — corrected draft re-dropped to the TI mailbox 2026-07-16
  after TI's first return; TI retains full sovereign authority to adopt,
  reject, or return again. TaF half unchanged by this run.
- Step 2 (independent advocate re-freezes Frame R): done per repo commit
  `f00a5c3` (not read by this run; blindness preserved).
- Step 3 (receiver expectations through the two-phase mechanism): phase-1
  receipt committed per `4c84e2f` (not read by this run).
- Step 4 (preregistered Rank-2 run): still gated on step 1 source issuance.

Rank 2 remains `BLOCKED` at the source-packet prerequisite until a source
steward issues. This run moves no claim, performs no classification, and
writes nothing outside this repo except the mailbox re-proposal.
