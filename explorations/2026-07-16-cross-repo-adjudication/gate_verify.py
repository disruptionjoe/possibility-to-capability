"""Receiver-side Phase-1 gate verification for TAF-002 and TI-WFA-001 (2026-07-16).

Read-only against source trees (git -C ... show / merge-base only). Produces a
receipt log on stdout. Exit 0 only if every REQUIRED check passes; the P2C
v0.2-contract validation of TI-WFA-001 is recorded as an OBSERVATION (TI issued
under its own ti-frozen-bundle-v1 convention), not a required check -- the
acceptance decision on that packet is adjudicated in the import record against
the charter's Frozen-Packet Rule checklist, not silently here.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

P2C = Path(r"C:\Users\joe\JB\CapacityOS\repos\public\possibility-to-capability")
TAF = Path(r"C:\Users\joe\JB\CapacityOS\repos\public\time-as-finality")
TI = Path(r"C:\Users\joe\JB\CapacityOS\repos\public\temporal-issuance")

TAF_BUNDLE = TAF / "exports/packets/TAF-002-p2cw1-capability-adjudication-v0.1"
TI_BUNDLE = TI / "exports/packets/TI-WFA-001-superconducting-ring-whole-family-legitimacy-v0.1"
W1 = P2C / "exports/witness/P2C-W1-superconducting-ring-v0.1"

sys.path.insert(0, str(P2C / "tests"))
from validate_frozen_packet_v0_2_contract import (  # noqa: E402
    expected_digests,
    load_json,
    validate_packet,
)

FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)


def observe(name: str, detail: str) -> None:
    print(f"[OBS ] {name} -- {detail}")


def git(repo: Path, *args: str, binary: bool = False):
    result = subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True
    )
    if binary:
        return result.returncode, result.stdout
    return result.returncode, result.stdout.decode("utf-8", "replace").strip()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def is_ancestor(repo: Path, anc: str, desc: str) -> bool:
    code, _ = git(repo, "merge-base", "--is-ancestor", anc, desc)
    return code == 0


def blob_at(repo: Path, rev: str, path: str) -> bytes | None:
    code, data = git(repo, "show", f"{rev}:{path}", binary=True)
    return data if code == 0 else None


def run_fixture(script: Path) -> tuple[int, bytes]:
    result = subprocess.run(
        [sys.executable, str(script)], capture_output=True, cwd=str(script.parent)
    )
    return result.returncode, result.stdout


def norm_lf(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def verify_manifest(bundle: Path, manifest: list[dict]) -> None:
    for entry in manifest:
        path = bundle.joinpath(*entry["path"].split("/"))
        data = path.read_bytes()
        check(
            f"blob re-hash {entry['path']}",
            len(data) == entry["byte_length"] and sha256(data) == entry["content_sha256"],
        )


print("=" * 72)
print("SECTION 0: P2C-W1 witness bundle self-re-verification")
print("=" * 72)
w1 = json.loads((W1 / "witness.json").read_text(encoding="utf-8"))
verify_manifest(W1, w1["integrity"]["manifest"])
code, _ = git(P2C, "cat-file", "-e", "4c9c28bbad0bdca45377dd2265b28b1fec3cc9ef^{commit}")
check("P2C freeze commit 4c9c28b exists", code == 0)
code, _ = git(P2C, "cat-file", "-e", "850521c2fc07b277734e293cd68c0928bb0cb6de^{commit}")
check("P2C content revision 850521c exists", code == 0)
check(
    "witness.json pinned content_revision matches",
    w1["source"]["content_revision"] == "850521c2fc07b277734e293cd68c0928bb0cb6de",
)
rc, out = run_fixture(W1 / "blobs" / "physical_witness_discriminator.py")
frozen = (W1 / "blobs" / "discriminator_output.txt").read_bytes()
check(
    "P2C-W1 discriminator re-run exit 0 + stdout matches frozen output",
    rc == 0 and norm_lf(out) == norm_lf(frozen),
)

print()
print("=" * 72)
print("SECTION 1: TAF-002 (time-as-finality)")
print("=" * 72)
packet = load_json(TAF_BUNDLE / "packet.json")
REV1 = "0749ce51c2eb542defe4010341787f1974a56a7d"  # content freeze (source.revision)
REV2 = "e0b5773d7ede2e72cc1afb1e367ee581418fed75"  # issuance
check("packet.json source.revision == claimed commit 1", packet["source"]["revision"] == REV1)
code, _ = git(TAF, "cat-file", "-e", f"{REV1}^{{commit}}")
check("commit 1 exists in TaF", code == 0)
code, _ = git(TAF, "cat-file", "-e", f"{REV2}^{{commit}}")
check("commit 2 exists in TaF", code == 0)
check("commit 1 is strict ancestor of commit 2", is_ancestor(TAF, REV1, REV2) and REV1 != REV2)
_, head = git(TAF, "rev-parse", "HEAD")
check("commit 2 is ancestor of TaF HEAD", is_ancestor(TAF, REV2, head), f"HEAD={head[:12]}")
rel = "exports/packets/TAF-002-p2cw1-capability-adjudication-v0.1"
check(
    "two-commit freeze: packet.json ABSENT at commit 1",
    blob_at(TAF, REV1, f"{rel}/packet.json") is None,
)
pj2 = blob_at(TAF, REV2, f"{rel}/packet.json")
check(
    "packet.json byte-identical to commit-2 blob",
    pj2 is not None and pj2 == (TAF_BUNDLE / "packet.json").read_bytes(),
)
iss2 = blob_at(TAF, REV2, f"{rel}/ISSUANCE.md")
check(
    "ISSUANCE.md byte-identical to commit-2 blob",
    iss2 is not None and iss2 == (TAF_BUNDLE / "ISSUANCE.md").read_bytes(),
)
manifest = packet["integrity"]["manifest"]
verify_manifest(TAF_BUNDLE, manifest)
for entry in manifest:
    blob = blob_at(TAF, REV1, f"{rel}/{entry['path']}")
    check(
        f"blob byte-identical at pinned commit 1: {entry['path']}",
        blob is not None
        and len(blob) == entry["byte_length"]
        and sha256(blob) == entry["content_sha256"],
    )
md, pd, bd = expected_digests(packet)
check("manifest_digest recomputed", md == packet["integrity"]["manifest_digest"], md)
check("packet_digest recomputed", pd == packet["integrity"]["packet_digest"], pd)
check(
    "bundle_digest/digest recomputed",
    bd == packet["integrity"]["bundle_digest"] == packet["integrity"]["digest"],
    bd,
)
check(
    "mailbox-claimed digests match",
    md == "6826fc19dfbddaaab6b2226620a41b70b0a9d936efe509ebe908142ec0255487"
    and pd == "4bf8c8efe8ad6f9bbeb9a7b7b920bd613e2bcb4439b1c040a374992c54159c72"
    and bd == "0237f93b6e075968600b065b08dbd2ee334290dd428b3821eb4c57502e17ed79",
)
errors = validate_packet(packet, TAF_BUNDLE)
check("P2C v0.2-contract validate_packet: 0 errors", errors == [], "; ".join(errors))
rc, out = run_fixture(TAF_BUNDLE / "blobs" / "taf002_p2cw1_adjudication.py")
frozen = (TAF_BUNDLE / "blobs" / "taf002_output.txt").read_bytes()
check(
    "TAF-002 fixture re-run exit 0 + stdout matches frozen output",
    rc == 0 and norm_lf(out) == norm_lf(frozen),
)
check(
    "TAF-002 bundle-verification section pins the SAME P2C-W1 manifest",
    all(
        e["content_sha256"] in (TAF_BUNDLE / "blobs" / "taf002_semantics.md").read_text(encoding="utf-8")
        for e in w1["integrity"]["manifest"]
    ),
)

print()
print("=" * 72)
print("SECTION 2: TI-WFA-001 (temporal-issuance)")
print("=" * 72)
ti_packet = json.loads((TI_BUNDLE / "packet.json").read_text(encoding="utf-8"))
TREV1 = "a336132d5ef3d6e3b31c704d07ecb39d28c753b1"  # content freeze (source.revision)
check("packet.json source.revision == claimed commit 1", ti_packet["source"]["revision"] == TREV1)
code, _ = git(TI, "cat-file", "-e", f"{TREV1}^{{commit}}")
check("commit 1 exists in TI", code == 0)
trel = "exports/packets/TI-WFA-001-superconducting-ring-whole-family-legitimacy-v0.1"
# locate commit 2: first commit touching packet.json
_, log = git(TI, "log", "--format=%H", "--follow", "--", f"{trel}/packet.json")
tcommits = log.split()
check("packet.json has exactly one authoring commit (frozen)", len(tcommits) == 1, log)
TREV2 = tcommits[-1] if tcommits else ""
print(f"       issuance commit (commit 2) located: {TREV2}")
check(
    "two-commit freeze: packet.json ABSENT at commit 1",
    blob_at(TI, TREV1, f"{trel}/packet.json") is None,
)
check(
    "commit 1 is strict ancestor of commit 2",
    bool(TREV2) and is_ancestor(TI, TREV1, TREV2) and TREV1 != TREV2,
)
_, thead = git(TI, "rev-parse", "HEAD")
check("commit 2 is ancestor of TI HEAD", bool(TREV2) and is_ancestor(TI, TREV2, thead), f"HEAD={thead[:12]}")
pj2 = blob_at(TI, TREV2, f"{trel}/packet.json") if TREV2 else None
check(
    "packet.json byte-identical to commit-2 blob",
    pj2 is not None and norm_lf(pj2) == norm_lf((TI_BUNDLE / "packet.json").read_bytes()),
)
tmanifest = ti_packet["integrity"]["manifest"]
verify_manifest(TI_BUNDLE, tmanifest)
for entry in tmanifest:
    blob = blob_at(TI, TREV1, f"{trel}/{entry['path']}")
    check(
        f"blob byte-identical at pinned commit 1: {entry['path']}",
        blob is not None
        and len(blob) == entry["byte_length"]
        and sha256(blob) == entry["content_sha256"],
    )
# ti-frozen-bundle-v1 manifest digest: sha256 over LF-joined "sha256  blobs/<path>"
# lines, paths sorted lexicographically, trailing newline.
lines = [
    f"{e['content_sha256']}  {e['path']}"
    for e in sorted(tmanifest, key=lambda e: e["path"])
]
ti_md = sha256(("\n".join(lines) + "\n").encode("utf-8"))
check(
    "ti-frozen-bundle-v1 manifest_digest recomputed",
    ti_md == ti_packet["integrity"]["manifest_digest"]
    == "2190631fd4aa9d499cec765026d8ddf40e177b42b798bbb5d86cdc6eef2dbd7d",
    ti_md,
)
# COMPLETION-CLASS.md byte-identity with TI repo root copy at pinned revision
cc_pin = blob_at(TI, TREV1, "COMPLETION-CLASS.md")
cc_bundle = (TI_BUNDLE / "blobs" / "COMPLETION-CLASS.md").read_bytes()
check(
    "blobs/COMPLETION-CLASS.md byte-identical to temporal-issuance/COMPLETION-CLASS.md at pin",
    cc_pin is not None and norm_lf(cc_pin) == norm_lf(cc_bundle),
)
rc, out = run_fixture(TI_BUNDLE / "blobs" / "ti_wfa_01_fixture.py")
tfrozen = (TI_BUNDLE / "blobs" / "ti_wfa_01_output.txt").read_bytes()
check(
    "TI-WFA-001 fixture re-run exit 0 + stdout matches frozen output (CR-normalized)",
    rc == 0 and norm_lf(out) == norm_lf(tfrozen),
)
check(
    "TI-WFA-001 verification_of_input_bundle pins the SAME P2C-W1 manifest",
    all(
        e["content_sha256"] in json.dumps(ti_packet["verification_of_input_bundle"])
        for e in w1["integrity"]["manifest"]
    )
    and ti_packet["verification_of_input_bundle"]["freeze_commit"]
    == "4c9c28bbad0bdca45377dd2265b28b1fec3cc9ef",
)
# OBSERVATION, not required: P2C v0.2-contract shape conformance
try:
    ti_errors = validate_packet(ti_packet, TI_BUNDLE)
except Exception as exc:  # noqa: BLE001
    ti_errors = [f"validator exception: {exc}"]
observe(
    "P2C v0.2-contract validate_packet on TI-WFA-001",
    f"{len(ti_errors)} errors (TI-native schema; adjudicated in import record): "
    + "; ".join(ti_errors[:12]),
)

print()
print("=" * 72)
if FAILURES:
    print(f"RESULT: FAIL ({len(FAILURES)} required checks failed)")
    for name in FAILURES:
        print(f"  - {name}")
    sys.exit(1)
print("RESULT: ALL REQUIRED CHECKS PASS")
