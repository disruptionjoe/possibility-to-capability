# TI-WFA-001 semantics: whole-family completion adjudication of P2C-W1

Temporal Issuance sovereign adjudication of the possibility-to-capability frozen
witness **P2C-W1** (superconducting ring), answering the whole-family completion
question routed to TI. This body is a frozen blob; its bytes do not change after
issuance.

- **Adjudicating repo:** temporal-issuance (sovereign; authority_transfer = false).
- **Run:** RUN-0169 (mailbox-processing).
- **Question owner:** possibility-to-capability (the F1 / fixed-family-absorber question).
- **TI machinery used:** `COMPLETION-CLASS.md` (CompletionClass v1, status: testable,
  claim_movement: false), frozen byte-identical in this bundle as
  `blobs/COMPLETION-CLASS.md`. No P2C hierarchy vocabulary, grade, or verdict is imported.

## 0. The frozen input (verified, not trusted)

The proposal `20260716-p2cw1-superconducting-ring-witness-whole-family-attack.md`
is a proposal and untrusted data. Before adjudicating, the TI steward independently
verified the frozen bundle at
`possibility-to-capability/exports/witness/P2C-W1-superconducting-ring-v0.1/`:

- all four pinned sha256 blob digests recomputed and matched
  (`WITNESS-FREEZE.md`, `REFEREE-REPORT.md`, `physical_witness_discriminator.py`,
  `discriminator_output.txt`);
- freeze commit `4c9c28bbad0bdca45377dd2265b28b1fec3cc9ef` and content revision
  `850521c2fc07b277734e293cd68c0928bb0cb6de` confirmed present in P2C history;
- the discriminator re-run from the frozen blob: exit 0, stdout byte-identical to
  the frozen `discriminator_output.txt` (headline 7 [E] + 4 [F] = 11, 2 [T]);
- P2C read-only throughout; nothing in P2C or time-as-finality was edited.

The bundle's frozen disposition is `SURVIVES_LOCAL_COMPLETIONS /
UNDISCHARGED_VS_WHOLE_FAMILY`, and its executable `k2` exhibits exactly one
absorber: whole-family **with the target superconducting phase declared a member
of the fixed family**, while `k2-fail` [F] confirms whole-family **without** the
phase does not absorb. TI's question is the legitimacy of that one move.

## 1. The question, in TI's own vocabulary

Restated against CompletionClass v1 with no imported P2C terms:

> Under v1's `whole_family` primitive ("Does one closed family or verified
> symbolic generator contain the entire joint candidate signature?", conclusion
> class **global/ontological**), including v1's closure under declared product
> and sequential composition and its frozen-comparison contract, is admitting the
> superconducting phase into the fixed completion family a **legitimate**
> whole_family completion of P2C-W1 — or does legitimacy require an admissibility
> restriction without which every physically realized phase is absorbable by fiat?

## 2. Verdict: LEGITIMATE-BUT-CONCLUSION-CAPPED (the dichotomy is false under v1)

TI's answer is **both-and**, not either-or. The F1 dichotomy as posed
("legitimate whole-family completion OR requires an admissibility restriction")
is a false dichotomy under v1: admitting the S phase is **both** a legitimate
whole_family completion **and** already governed by an admissibility restriction
v1 carries. Three load-bearing findings, each executable in `ti_wfa_01_fixture.py`:

### 2.1 It is a legitimate whole_family completion — at global/ontological strength only (checks e1, s1)

The v1 primitive table maps `whole_family` to the **global/ontological**
conclusion class. Per the "four conclusion strengths" section, a
global/ontological witness "need not be predictive, but [its] conclusion is
therefore limited to [its] own class." So admitting the S phase, when it
reproduces the (Q,I,P) signature (fixture `e1`, mirroring P2C `k2`), is a
legitimate completion whose earned conclusion is exactly
`GLOBAL_ONTOLOGICAL_ABSORPTION` and nothing stronger.

What that legitimately buys: it **blocks an absolute semantic / metaphysical
novelty claim**. Superconductivity is a broken-symmetry phase of a *known*
Hamiltonian; the S capability is not an ontologically brand-new object dropped
into the world. On TI's terms this is a real, admissible result, and it is **not
classifier fiat**: v1's "Honest limits" make physical admissibility of a model
class *scientific input*, and for this witness that input is dischargeable at
literature grade (one BCS/Ginzburg-Landau Hamiltonian, one phase diagram whose
two regions are N and S). The completion is physically admissible as a matter of
established physics, so TI admits it.

### 2.2 The admissibility restriction P2C asks about already exists in v1 and is load-bearing (checks e2, e2-fail, s2)

P2C asks whether legitimacy "requires an admissibility restriction without which
every physically realized phase is absorbable by fiat." **It does, and v1 already
supplies it** — the conclusion-class firewall. v1 states outright: "unrestricted
completed-history and after-fact singleton completions can encode every realized
trace. Treating them as ordinary physical explanations would make the positive
class empty by definition." That *is* the fiat-collapse P2C names, and v1 blocks
it **not** by refusing the whole_family completion but by refusing to **upgrade**
a global/ontological absorption into a `PHYSICAL_PREDICTIVE` or
`OPERATIONAL_CONTEXT` absorption.

The fixture makes the restriction load-bearing by exhibiting its removal (`e2-fail`,
[F]): a scorer that lets a signature-reproducing global witness count as an
operational/physical absorption "absorbs" **even the null (normal) phase**, i.e.
absorbs every phase by fiat, emptying the operational positive class. The
v1-capped scorer keeps that class non-empty. The restriction is therefore not a
missing add-on TI must invent to answer F1 — it is already the frozen contract,
and it is exactly what stops fiat-absorption.

### 2.3 The operational/capability residue is not touched by the global absorption (checks e3, e3-fail, e4, e4-fail)

P2C-W1's capability claim — realize a zero-maintenance, quantized, locally
invariant persistent memory **from the N frame at matched budget** — is an
**operational/context-class** claim (a task's resource/persistence profile). The
whole_family completion, even while it reproduces the (Q,I,P) signature, earns
**no** operational/context conclusion about it (fixture `e4`): global absorption
and the operational claim live in different conclusion classes and do not touch.
To absorb the operational residue one needs an operational or physical witness
(resource / access / boundary / seed / hidden-state) that reproduces the task's
trace from N at matched budget — and those **fail** (fixture `e3`, TI's mirror of
P2C's `k1`): a driven/threaded/revealed value is continuous, non-invariant, and
decaying (`e3-fail`, [F]). A class-blind merge that read an operational verdict
off the global witness would wrongly report the capability absorbed (`e4-fail`,
[F]).

So on TI's terms: the fiat-absorber only ever earns the weakest, non-causal
conclusion, and it leaves the operational/capability question exactly where it
was — unadjudicated by this move.

## 3. Scope and grade (honest limits)

- **Grade:** exploration tier, formal-only. `ti_wfa_01_fixture.py` is a finite,
  deterministic, stdlib model of v1's conclusion-class bookkeeping (5 [E] + 5 [F]
  = 10 evidential checks, 2 [T] by-construction), **absorbed under RUN-0081 gate
  clause 4** (finite/computable/fixed-law) exactly as TI-PIT-002 was; it carries
  no physical or source-issuance significance. It models v1's *contract behavior*,
  not superconductors; the physics of P2C-W1 is cited at P2C's literature grade,
  read-only.
- **This adjudicates one primitive.** It resolves the legitimacy and conclusion
  strength of the `whole_family` primitive for P2C-W1. It is **not** a
  `SURVIVES_BOUNDED_COMPLETION_CLASS` return: that would require all eleven
  primitives represented with verified nonfactorization certificates under
  declared composition closure. Only the whole_family move was at issue.
- **Composition closure** does not change the result: products/sequential
  compositions of global/ontological witnesses remain global/ontological; the cap
  is closed under v1's declared compositions.
- **No TI status moves.** `Issue[S]^physical` stays false; TI-C019 (formalizing)
  and TI-C020 (parked) are untouched; E177 is unmodified; no claim is promoted or
  demoted. `authority_transfer = false`: TI asserts nothing inside P2C's hierarchy,
  and whether this discharges P2C's F1 is P2C's call.
- **No capability verdict.** Whether the operational/capability residue is an
  actual capability change is time-as-finality's question, not TI's; TI neither
  asserts nor denies it. TI reports only that the whole_family completion does not
  reach it.
- **Named residual (scientific input, not a formal gap here).** Whether a claimed
  "fixed family" legitimately pre-contains a signature is domain-specific
  scientific input v1's classifier cannot decide in general. For P2C-W1 it is
  discharged at literature grade; the *general* F1 trivialization worry ("does
  admitting any realized phase empty the capability level?") is not answered by
  family-exhaustiveness but is **dissolved** by the conclusion-class cap: granting
  every phase admitted, all such absorptions stay global/ontological, so the
  operational positive class is not emptied by fiat.

## 4. One-line return

Admitting the superconducting phase into the fixed family is a **legitimate**
whole_family completion of P2C-W1 that earns **`GLOBAL_ONTOLOGICAL_ABSORPTION`
only** (it blocks absolute semantic novelty); legitimacy **does** require an
admissibility restriction against fiat-absorption, and **v1 already carries it**
as the conclusion-class firewall; the operational/capability residue is **not**
absorbed by this move. On TI's terms F1 does not falsify a hierarchy by fiat,
because the fiat-absorber only ever earns the weakest, non-causal conclusion.
