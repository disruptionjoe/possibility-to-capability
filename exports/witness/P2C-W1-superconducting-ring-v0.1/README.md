---
artifact_type: witness_freeze_bundle
status: frozen
governance_role: cross_repo_witness_export
constitutional: false
created: 2026-07-16
witness_id: P2C-W1
---

# P2C-W1 — frozen witness bundle: superconducting ring, quantized persistent supercurrent

This bundle is the frozen form of the P2C-REAL-PHYSICAL-WITNESS reach-swing
result (`explorations/2026-07-16-real-physical-witness/`), exported for
independent sovereign adjudication by Time as Finality and Temporal Issuance.
It mirrors the `exports/packets/` convention those repositories established
(TAF-001), adapted to a witness freeze whose source and owner is this
repository.

**Frozen content.** `witness.json` is the manifest. The blobs are byte-exact,
sha256-pinned copies of the artifacts as they exist at content revision
`850521c2fc07b277734e293cd68c0928bb0cb6de`:

| blob | sha256 |
| --- | --- |
| `blobs/WITNESS-FREEZE.md` | `694443cacddfcd784a81e01a6e059557b5b1e6aaeea8c0a7616a4f0ac6b71b51` |
| `blobs/REFEREE-REPORT.md` (GOVERNS grades) | `dfd966259d9e8e2f58bc3725f53f5751c08e0f6b4015c01c333548e09eca0113` |
| `blobs/physical_witness_discriminator.py` | `42f647eb7a1f6533e26ae9f6f321824693a77517540259fe505ce968d59ea9eb` |
| `blobs/discriminator_output.txt` (true byte output, deterministic) | `b917f59b2e5f6ee3221a08260ce3f22043c7b843c89343a0fe7e778eb84db45f` |

**Immutability.** Nothing in this bundle may be edited after the freezing
commit. Corrections require a new version (`-v0.2`) and re-proposal; a modified
bundle is a different witness.

**Same-frozen-witness rule.** Both sovereigns are tested on THIS bundle,
unchanged. Per the portfolio's `return_activation` contract, sovereign returns
are combined only if each return identifies this bundle by its hash manifest.
Split, negative, declined, or ignored returns are first-class outcomes.

**Frame.** The capability claim inside is frame-indexed (referee correction
R-D1; Hierarchy v0.2 §2.5): its declared frame is the budget-matched
counterfactual pair (ring in S versus a matched reference normal conductor at
the same `T_f` and spent budget). No frame-free claim is made.

**Disposition frozen at export:** `SURVIVES_LOCAL_COMPLETIONS /
UNDISCHARGED_VS_WHOLE_FAMILY`. No capability-enlargement verdict is licensed.
The single open question routed for adjudication is falsifier F1: whether
admitting the target superconducting phase into the fixed completion family is
a legitimate completion.

**Verification.** `python blobs/physical_witness_discriminator.py` exits 0 and
its stdout byte-compares to `blobs/discriminator_output.txt`. Headline: 7 [E] +
4 [F] = 11 evidential checks, 2 [T] no-weight theorem-consequence checks;
strict TEF lint clean.
