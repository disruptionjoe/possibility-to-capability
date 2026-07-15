---
artifact_type: packet_contract
status: provisional
schema_version: "0.2"
verification: tests/validate_frozen_packet_v0_2_contract.py
---

# Frozen-Packet Contract v0.2

Frozen-Packet Contract v0.2 hardens three boundaries left open by v0.1:

1. the same bytes and metadata now produce the same bundle digest on every
   conforming implementation;
2. method multiplicity now carries an explicit premise and dependency
   structure, so row count cannot stand in for evidential independence; and
3. independence interpretation is a separate receiver-owned assessment that
   may preserve the source's type or weaken it to `unknown_or_contested`, but
   cannot strengthen it.

This is a receiving-repository contract. It does not issue a source packet,
upgrade a source claim, or make any source result importable.

## Contract Artifacts

- `frozen-packet-v0.2.schema.json` defines the source-issued packet.
- `receiving-independence-assessment-v0.2.schema.json` defines the separate,
  receiver-owned assessment.
- `../../tests/fixtures/frozen-packet-v0.2-valid.json` and its bundle provide a
  reproducible positive control.
- `../../tests/validate_frozen_packet_v0_2_contract.py` implements semantic,
  integrity, compatibility, and adversarial checks.

## Canonical Bundle Profile

The profile identifier is `ptc-frozen-bundle-v1`. The following rules are
normative.

### JSON and strings

- Decode JSON as UTF-8 and reject duplicate object keys.
- Every decoded string and key must already be Unicode NFC. Implementations
  reject non-NFC input; they do not silently normalize source wording.
- Canonical JSON uses recursively sorted object keys, preserves array order,
  emits UTF-8 without a BOM or trailing newline, emits no insignificant
  whitespace, does not ASCII-escape non-ASCII characters, and rejects NaN and
  infinity. In Python terms, this is equivalent to
  `json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True,
  separators=(",", ":")).encode("utf-8")` for the schema's data types.

### Paths and blobs

- Manifest paths are relative POSIX paths in NFC.
- Absolute paths, backslashes, drive or URI colons, control characters, empty
  segments, `.`, and `..` are invalid.
- Paths are unique both exactly and after Unicode case folding, preventing
  cross-platform extraction collisions.
- Entries are sorted by the unsigned UTF-8 byte sequence of `path`.
- `byte_length` is the exact length of the blob as stored.
- `content_sha256` hashes the raw stored bytes. There is no newline, encoding,
  archive, or text normalization.
- `hash_scope` equals the manifest path sequence exactly. All source artifact,
  method artifact, premise artifact, verification artifact, and joint-argument
  paths must occur in the manifest.

The repository marks the synthetic bundle fixture `-text` in `.gitattributes`
so checkout settings cannot alter its controlled bytes.

### Digests

Let `C(x)` be the canonical JSON encoding above and `H(x)` be SHA-256 returned
as lowercase hexadecimal.

1. Form the manifest projection:

   ```json
   {
     "canonicalization_profile": "ptc-frozen-bundle-v1",
     "entries": ["the sorted integrity.manifest entries"]
   }
   ```

2. `manifest_digest = H(C(manifest_projection))`.
3. For the packet-digest projection, use the complete packet with the computed
   `manifest_digest`, but replace `integrity.packet_digest`,
   `integrity.bundle_digest`, and `integrity.digest` with 64 lowercase zeroes.
4. `packet_digest = H(C(packet_digest_projection))`.
5. Decode `packet_digest` and `manifest_digest` from hexadecimal to their
   32-byte forms. Then:

   ```text
   bundle_digest = H(
     UTF8("ptc-frozen-bundle-v1") || 0x00 ||
     bytes(packet_digest) || bytes(manifest_digest)
   )
   ```

6. `integrity.digest` is a compatibility alias and must equal
   `bundle_digest`.

The manifest digest commits the ordered blob inventory; each entry commits the
raw blob bytes; the packet digest commits packet metadata and the manifest; and
the domain-separated bundle digest binds the packet and manifest together.

## Method Dependence Contract

Every method names at least one `premise_id`. Every premise names every method
for which it is load-bearing. The two directions must be exact inverses.

`shared_load_bearing_premise_ids` is not commentary. It must equal exactly the
set of premise IDs used by more than one method. Direct method-to-method
dependencies are represented separately in `method_dependency_edges`.

`raw_method_count` and `claim.method_count` must both equal the method-ledger
cardinality. `raw_method_count_is_independence_count` is always `false`.
Neither convergence nor identical result strings alter that rule.

The dependency graph does not itself calculate an "effective number" of
independent methods. Such a scalar would require a defended model of dependence
that this contract does not assume.

## Receiving Independence Assessment

The assessment is stored beside, never inside or in place of, the immutable
source packet. It is owned by `possibility-to-capability` and pinned to the
packet and source revision.

The validator enforces:

- the copied source independence wording is exactly equal after JSON decoding;
- the source independence type and source claim status are unchanged;
- a `provisional` receiving type is either the identical source type or
  `unknown_or_contested`;
- an `unknown` or `contested` assessment uses `unknown_or_contested`;
- a source `unknown_or_contested` type can never be strengthened;
- every basis method and limiting premise exists in the source packet; and
- every shared load-bearing premise remains explicit as a limiting premise.

The types are deliberately non-ordered. For example, model-relative
non-forcing, proof-theoretic independence, transformation-class invariance,
and empirical underdetermination are not treated as interchangeable or as a
strength ladder.

## Compatibility and Migration

v0.2 is backward-compatible by coexistence and information preservation, not
by pretending the version field did not change:

- v0.1 remains frozen and valid under its own schema and validator.
- Every v0.1 top-level field and its meaning is retained in v0.2.
- `integrity.hash_scope` and `integrity.digest` remain, with `digest` now the
  alias of the reproducible bundle digest.
- A v0.1 consumer may continue reading v0.1 packets. A v0.2 consumer must not
  claim v0.2 guarantees for a v0.1 packet.
- Migration creates a new source-issued v0.2 packet; it never rewrites a frozen
  v0.1 packet in place.

To migrate, the source steward inventories exact raw blobs, emits the sorted
manifest, maps every method to its premises and direct dependencies, types the
source's own exact independence wording, and computes the three digests. The
receiver then creates its assessment separately. Missing information produces
`NOT_YET_IMPORTABLE`, `unknown`, or `contested`, not inferred completion.

GU-001's existing `NOT_YET_IMPORTABLE` receipt is unchanged by this contract.

## Nonclaims

- Two or five method rows are not two or five independent evidential units.
- A shared premise does not make methods worthless; it limits what their
  agreement establishes.
- Reproducible hashing establishes identity and tamper evidence, not truth.
- A receiving classification is not a proof of the source result.
- Matching a source type does not upgrade the source's grade or claim status.
- The contract does not prove that its independence taxonomy is complete.
- The contract does not create, accept, or reconstruct GU-001.

## Falsifiers and Reopening Conditions

Revise or reject this contract if any of the following occurs:

- two conforming implementations compute different digests for identical
  decoded packet data and identical raw blobs;
- an admissible path or Unicode case produces extraction ambiguity not caught
  by the profile;
- a packet passes while omitting a referenced or load-bearing artifact;
- method counts can influence a receiving independence type without the typed
  source ceiling and premise structure;
- a receiving assessment can rewrite source wording, status, or type and still
  pass;
- a real second packet cannot express its dependency structure without
  manufacturing premises or dependencies; or
- the typed independence categories collapse under a defensible source case.

The last two outcomes are evidence about the contract, not source-repository
failures.
