---
artifact_type: referee_report
status: governs
governance_role: rank2_adjudication_referee
constitutional: false
created: 2026-07-16
---

# REFEREE REPORT — RANK2-PR-001 adjudication run (governs; corrections applied pre-commit)

Adversarial referee pass on the receiver's own Rank-2 adjudication, per the house
convention (the referee report GOVERNS and its corrected receiver update supersedes
any run headline). The referee attacked the gate runs, the check evaluations, the
outcome-mapping application, and prereg compliance, and attempted to refute the
verdict.

## Re-execution and audit receipts (2026-07-16)

- Phase-1 mechanical gates independently re-derived: both packets validate with 0
  errors under `tests/validate_frozen_packet_v0_2_contract.py::validate_packet`
  with their import directories as `bundle_root`; all 9 manifest blobs re-hash
  byte-exact; all 6 digests recomputed under `ptc-frozen-bundle-v1` match packet
  fields AND the mailbox-claimed values (mailbox treated as proposal, verified
  against the actual source trees); two-commit freeze verified in both source
  repos (packet.json absent at content-freeze commit, added at issuance; freeze
  commit a strict ancestor of issuance; issuance an ancestor of source HEAD).
- Frozen computations re-executed from scratchpad copies: TI fixture exit 0 with
  raw byte-identical stdout (4999 B); TAF computation exit 0 with stdout identical
  after CRLF/LF normalization (Windows text-mode stdout; hashed blob bytes are
  authoritative). The CRLF qualifier must appear wherever re-execution is billed
  (correction R-D5, applied).
- Harness (`rank2_adjudication_harness.py`) audited line-by-line and re-run:
  deterministic output (re-run diff empty); evidence values match the packets'
  own claim statements exactly where the packets state them (TAF ALPHA
  (1,0,0,0,1)->(1,1,0,0,0); TAF BETA ->(1,0,1,0,1); TI ALPHA decidable 25->30
  all-negative gains; TI BETA record and decidable set fixed at L2, abbb
  undecidable at L3) and extend them only by the per-completion sweeps the
  receiver contract requires. Hand spot-checks of the TAF sweep (tau3 support
  {r5,r12,r13} vs {r5}; tau4 competing-value tie at every completion containing
  {h1,h2}) confirm the computed profiles.
- Prereg mechanics: `RANK2-PR-001.expectations.json` still touched by exactly one
  commit (49baf1f) with HEAD blob equal to the registered blob; results committed
  at the pre-declared sibling path with the exact prereg_ref from the phase-1
  README; `tests/prereg_verify.py` all seven gates PASS, `valid: true`, exit 0.
  Per the mechanism's own nonclaims this is necessary, not sufficient, and the
  results artifact bills it exactly that way.

## (1) VERDICT: SOUND-WITH-CORRECTIONS (all corrections applied before the results commit)

The adjudication executed the frozen expectations faithfully, manufactured no
agreement, moved no source claim, preserved every split/miss/blocked outcome as
first-class, and honored the quarantine as a constraint rather than routing
around it. Five defects were found and corrected; none survives into the
committed record.

## (2) Defects and dispositions

**R-D1 — MODERATE — c3/S5 construal is receiver discretion not covered by a frozen
judgment call.** A strict global reading of c3 ("before seeing any case pair")
misses on the declared incidental sighting of the TI draft by Frame R's re-freeze
advocate, and outcome-mapping rule 2 then voids the entire run. The receiver's
per-scored-case-set construal (exclude the TI frame leg; run TAF-alone) has real
textual support — c2's on_miss explicitly contemplates a TaF-branch-alone run,
and S5's wording is forward-looking ("any case the frame WILL SCORE") — but the
prereg did not freeze that construal. *Correction (applied):* the citable global
verdict must be the construal-INVARIANT statement: under every admissible
construal (strict-invalid / per-branch+strict-c5 / per-branch+factor-c5-fork), NO
Rank-2 outcome is licensed. Nothing citable may depend on the receiver's
preferred construal. Refutation attempt failed: the referee could construct no
admissible construal under which any FAVORS_* outcome is licensed on this
evidence.

**R-D2 — MINOR/MODERATE — d1's counterfactual was stated candidate-side only.**
Under the factor construal, rule 4 would also fire on the TI branch (a
declared-single-factor pair completion-RELATIVE), so the counterfactual is a
SPLIT with quarantine-attenuated rival pressure, never a candidate victory.
*Correction (applied):* full split shape recorded in d1 so the preserved fork
cannot later be quoted as "we would have won."

**R-D3 — MINOR — the c4/c5 scoring asymmetry needed its principled basis stated.**
Accepting "access-structure change" for c4 while scoring c5 N/A could read as
selective. The basis: "access" is one of the five declared factors in the
lane-R2 factor vocabulary (factor-to-factor match); "capability" is not a factor
but the receiver's contested diagnosis token, so c5 as written could bind only if
a source adopted receiver diagnosis vocabulary — which both packets' nonclaims
categorically refuse, and which the receiver-side drafts never carried either
(post-classification J6 examination). This is a prereg AUTHORING defect in c5's
trigger vocabulary, curable only via a NEW prereg id per the amendment policy.
*Correction (applied):* stated in c5's detail; the reopener consequence is named
in the global verdict.

**R-D4 — MINOR — out-of-class audit probe risked an S1 misreading.** Harness
[F] e3-fail evaluates a completion outside frozen C ({h3,h4}). Cleared: it is a
J2 adequacy-audit demonstration; no scored check value ranges outside the frozen
classes. *Correction (applied):* explicit sentence added to d6.

**R-D5 — MINOR — re-execution billing.** "Byte-identical" for the TAF re-run is
true only after CRLF/LF normalization. *Correction (applied):* qualifier added
in c1's detail and the import record.

## (3) Checked and cleared (not defects)

- **c6 = FALSE is robust to the quarantine.** Even if the TI frame leg had run,
  TI BETA's frame-neutral evidence (delta_op = 0, delta(top) = 0) makes N and R
  AGREE (both NO_CHANGE), and TI ALPHA is completion-ROBUST — so no
  RELATIVE-profile-with-defended-disagreement pair exists on ANY construal. The
  c6 miss is a property of the evidence, not an artifact of the exclusion.
- **Neutrality.** No outcome was favored — none was licensed; the run's misses
  cut against the receiver's own expectations (c6) and against Frame R's
  mixed-sector-dominance forecast alike. Label-swap invariance machine-checked
  with a demonstrated failing direction.
- **No-Artificial-Success.** Nothing was combined: no joint pass, no averaged
  sectors, no transfer between branches; the factor-construal counterfactual is
  preserved as a fork, not exercised.
- **Source sovereignty.** No source file edited; no source claim moved; both
  packets' nonclaims and TI's standing quarantine honored; bar(b), H59, Krein
  positivity, physical issuance remain OPEN; ADAPTER2-01 uncontradicted.
- **Evidence discipline.** Classification computed from frozen computation blobs
  only (TaF D6 advisory honored); source-native task semantics used (no receiver
  substitution, stop S2); completion classes mechanical from source-supplied
  inventories per the frozen contract rule (stop S1), with adequacy audited and
  its interval-dependence named as an attack surface (J2).
- **Scope.** No scope additions: every computed object is required by the frozen
  construction (pair evidence, frames, controls) or licensed by J2 (audit) or the
  house [T]/[E]/[F] discipline (failing directions, all genuinely exercising
  their protected checkers through the same code paths — the burned constant-True
  class is absent; each [F] was verified to fail under the perturbation and pass
  under the real configuration).

## (4) Corrected receiver update (GOVERNS)

Rank 2 status: **UNDISCHARGED — adjudication executed, prereg exercised, NO
Rank-2 outcome licensed, construal-invariant.** Unconditionally earned, at
exploration tier:

1. Both sovereign issuances are real and verified (c1, c2 ISSUED): the
   blocked-forever null rival is partially falsified.
2. The pure-ACCESS side of the completion-robustness discriminator is now
   observed on real sovereign evidence at full frozen-class strength on two
   independent branches (c4 ROBUST_ZERO), including a non-monotone access
   enlargement (TAF ALPHA loses tau5) — receiver-owned frame-neutral facts,
   single-branch each, never combined.
3. The capability side of the discriminator is untestable on this evidence
   (c5 N/A — a prereg vocabulary defect meeting a sovereign label-refusal
   practice), and the mixed sector did not materialize (c6 FALSE, an honest
   receiver miss that equally denies Frame R its predicted dominance).
4. The TI branch's frame-discriminating leg is BLOCKED by the carried
   authorship quarantine + S5 (preserved constraint).
5. The path forward is the prereg's own amendment policy: a NEW prereg id with
   factor-vocabulary-aligned capability checks, plus a sovereign pair free of
   Frame-R-advocate contamination (or a successor advocate with no case
   exposure).

No update — not even directional pressure — toward FAVORS_CANDIDATE or
FAVORS_RIVAL is earned. A prereg-verify PASS (obtained, all gates) is necessary,
not sufficient, and confers no scientific pass.
