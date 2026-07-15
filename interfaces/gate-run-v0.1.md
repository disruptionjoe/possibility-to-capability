# Neutral Eight-Gate Run Contract v0.1

Status: provisional repo-owned interface. It is not canon, a source verdict, or
a physical result.

## Purpose and scope

This contract records a receiving-side evaluation of one valid
Frozen-Packet v0.2 object beside one separate receiving assessment. It answers
whether the supplied receiver judgments form a complete, auditable, neutral
gate chain. It does not decide whether those judgments are scientifically
correct.

The gate order is fixed:

1. provenance;
2. construction;
3. formation;
4. completion/null;
5. capability;
6. finality;
7. no-artificial-success; and
8. neutrality.

Every gate depends on all preceding gates. A non-passing prerequisite forces
later gates to `BLOCKED`; it cannot be skipped or averaged away.

## Outcome lattice

Gate outcomes are intentionally not Boolean:

- `PASS`: the receiver judges the gate satisfied under its named assumptions,
  construction, evidence, grade, and verification.
- `FAIL`: the receiver judges the gate contradicted or unsatisfied.
- `BLOCKED`: the gate cannot currently be evaluated, either because its own
  required input is unavailable or a prerequisite did not pass.
- `INDETERMINATE`: the available evidence reaches the gate but does not select
  pass or fail.
- `INVALID`: reserved for the evaluator's report when the run itself is
  malformed. It is not a gate outcome and cannot be declared by an author.

For a structurally valid run, aggregate precedence is `FAIL`, then
`INDETERMINATE`, then `BLOCKED`; only eight passes produce aggregate `PASS`.
The distinctions remain visible in every gate result even when the aggregate
uses that deterministic precedence.

## Source/receiver boundary

The gate run contains only references to the frozen source packet and its
separate receiver assessment. It carries four constant source-preservation
guards and may not copy-edit the source claim, change its status, or transfer
authority.

Each gate must include:

- resolvable JSON Pointers into the source packet;
- resolvable JSON Pointers into the receiving assessment;
- a distinctly receiver-owned judgment with grade and verification;
- at least one falsifier; and
- at least one explicit nonclaim.

This makes source evidence and local interpretation visible without pretending
that either one entails the other.

The receiving-assessment digest is SHA-256 over UTF-8 canonical JSON with keys
sorted, no insignificant whitespace, NFC strings already required by the
upstream assessment contract, and `ensure_ascii=false`. The frozen packet is
identified by its own v0.2 `packet_digest` rather than re-hashed here.

## No-Artificial-Success

The first six substantive gates may pass only as individual receiver
judgments. Gate seven asks the additional joint question. It passes only when:

- all six passed;
- every one uses the same `argument_chain_id`;
- every one uses the same `construction_branch_id`;
- every one uses the same `argument_ref`; and
- those three values equal the declared one-chain control.

Mixing successful legs from different arguments or construction branches is a
valid negative test result, not a malformed run. In that case gate seven must
be `FAIL`, gate eight must be `BLOCKED`, and aggregate success is impossible.

## Neutrality

Gate eight is evaluated only after gate seven passes. The run must name two
distinct labels, record their exact swap, give the verdict before and after,
and state whether the verdict is invariant. The evaluator independently checks
that the permutation is a real reversal and that `label_invariant` agrees with
verdict equality. A label-sensitive verdict makes neutrality `FAIL` and the
aggregate `FAIL`.

This is a syntactic metamorphic control. A real gate run still needs a
substantive, reviewable relabeling artifact; merely filling the fields does not
establish physical neutrality.

## Deterministic evaluator

`tests/evaluate_gate_run.py` uses only the Python standard library. It checks:

- exact top-level and nested fields;
- source and receiving-assessment identities and preservation guards;
- all source and assessment JSON Pointers;
- exact gate membership, order, ordinals, and cumulative prerequisites;
- downstream blocking;
- one-chain and branch consistency;
- label-swap and verdict-invariance consistency; and
- the declared aggregate against the computed aggregate.

Example:

```text
python tests/evaluate_gate_run.py \
  tests/fixtures/gate-run-v0.1-positive.json \
  tests/fixtures/frozen-packet-v0.2-valid.json \
  tests/fixtures/receiving-independence-v0.2-valid.json
```

Exit zero means the run is structurally and semantically consistent with this
contract. It does not mean the source claim or any receiver judgment is true.

## Construction, assumptions, and grade

- Construction: a strict cumulative prerequisite chain with two explicit
  metamorphic controls at the end.
- Assumption: Frozen-Packet v0.2 and Receiving Independence Assessment v0.2
  were validated before this evaluator is invoked.
- Assumption: JSON Pointers identify evidence locations, not inferential
  sufficiency.
- Grade: provisional interface plus deterministic synthetic controls.
- Verification: positive, fail, blocked, indeterminate, split-chain,
  label-sensitive, malformed, and tampering cases in
  `tests/validate_gate_run_contract.py`.

## Nonclaims

- The engine does not establish any physics.
- A structural `PASS` does not promote a receiver judgment, source claim, or
  source claim status.
- The engine does not show that evidence references are sufficient, only that
  they exist at the declared frozen locations.
- A label-swap test does not prove invariance under every admissible
  reformulation.
- The schema does not establish that the hierarchy is complete or universal.

## Reopening conditions

Reopen v0.1 if a real packet exposes a gate that is not cumulative, a justified
multi-chain proof that is not artificial aggregation, a neutrality test that
cannot be represented as a label permutation, a source/receiver evidence type
not expressible by JSON Pointer, or an outcome not faithfully represented by
the four-state lattice.
