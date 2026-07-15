# Interfaces

This directory is reserved for neutral contracts that describe how frozen
packets may be evaluated across construction, formation, completion,
capability, physical-response, and synthesis gates.

An interface may transport evidence and questions. It may not copy a verdict
from one repository into another or manufacture a joint pass from partial
passes.

## Active provisional contracts

- `blocked-intake-preflight-v0.1.schema.json` records a receiver-owned
  provenance stop when no source-issued packet, manifest, or digest exists. It
  forbids mutable/untracked source refs, receiver-created packet identity,
  status upgrades, method reassembly, and downstream gate execution.
- `blocked-intake-preflight-v0.1.md` defines why `BLOCKED`/`NOT_RUN` is a
  first-class result and names the exact source artifacts needed to reopen.
- `gate-run-v0.1.schema.json` is the machine-readable receiver-side record for
  the charter's ordered eight-gate evaluation.
- `gate-run-v0.1.md` defines outcome, source/receiver separation,
  prerequisite, one-chain, label-neutrality, aggregate, nonclaim, and
  reopening semantics.
- `transition-diagnosis-v0.1.schema.json` is the machine-readable witness
  contract for distinguishing fixed-family disclosure, dynamics, records,
  access, normalized capability change, and finality candidates while
  retaining nulls, forks, incomparability, uncertainty, and hierarchy failure.
- `transition-diagnosis-v0.1.md` defines the hierarchy as a provisional typed
  diagnostic vocabulary rather than a presumed temporal sequence.

The reference evaluator lives under `tests/` so its successful execution
cannot be confused with source evidence or a promoted research conclusion.
