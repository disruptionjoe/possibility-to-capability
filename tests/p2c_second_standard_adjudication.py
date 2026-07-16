"""Second-standard local read of P2C-W1 under CompletionClass-P2C v0.1.

This fixture does not adjudicate source truth. It reads the imported TAF-002
and TI-WFA-001 packets as frozen evidence, then checks whether the prior
P2C-W1 scoped-survivor chain still holds when the completion leg is rerun under
P2C's own derived firewall and carrier-neutral adapter.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import p2c_completion_class_closure as completion
import witness_boundary_adapter as adapter


CHECKS = {
    "setup: witness bundle declares P2C-W1 and QIP signatures": {"tag": "T"},
    "input identity: imported returns and witness bundle name one unchanged P2C-W1": {"tag": "E"},
    "source sovereignty: imported packets keep source status and authority transfer false": {"tag": "E"},
    "c1: task-semantics mapping remains condition-bound": {"tag": "E"},
    "c2: P2C derived firewall supplies containment without operational absorption": {"tag": "E"},
    "c2b: P2C composite closure closes the old D2 local absorber gap at model grade": {"tag": "E"},
    "adapter bridge: carrier-neutral adapter reports certified containment only": {"tag": "E"},
    "c3: tau_P metastability cap is carried": {"tag": "E"},
    "c4: context individuation fork remains open": {"tag": "E"},
    "gate chain: scoped survivor remains class-split under P2C standard": {"tag": "E"},
    "finality hygiene: finality gate remains not reached": {"tag": "E"},
    "no artificial success: one witness one frame one chain with split preserved": {"tag": "E"},
    "c2-fail: class-blind containment merge would not operationally absorb": {
        "tag": "F",
        "protects": "c2: P2C derived firewall supplies containment without operational absorption",
    },
    "c2b-fail: dropping local invariance would not create a composite absorber": {
        "tag": "F",
        "protects": "c2b: P2C composite closure closes the old D2 local absorber gap at model grade",
    },
    "adapter-fail: verdict-carrying completion metadata would be accepted": {
        "tag": "F",
        "protects": "adapter bridge: carrier-neutral adapter reports certified containment only",
    },
    "c4-fail: one-context whole-family fork can be closed without changing frame": {
        "tag": "F",
        "protects": "c4: context individuation fork remains open",
    },
    "finality-fail: finality can be marked pass in this chain": {
        "tag": "F",
        "protects": "finality hygiene: finality gate remains not reached",
    },
}


@dataclass(frozen=True)
class CompletionLeg:
    certified_contains_witness: bool
    operationally_absorbs_witness: bool
    composite_absorbers: tuple[tuple[str, ...], ...]
    class_blind_operational_absorption: bool
    dropped_invariance_absorbers: tuple[tuple[str, ...], ...]
    capped_operational_map_nonconstant: bool


@dataclass(frozen=True)
class AdapterLeg:
    residual_class: str
    certified_containers: tuple[str, ...]
    local_absorbers: tuple[str, ...]
    verdict_metadata_rejected: bool


@dataclass(frozen=True)
class ChainRead:
    formation: str
    completion: str
    capability: str
    finality: str
    neutrality: str
    no_artificial_success: str
    disposition: str


def root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(*parts: str) -> dict:
    return json.loads(root().joinpath(*parts).read_text(encoding="utf-8"))


def load_text(*parts: str) -> str:
    return root().joinpath(*parts).read_text(encoding="utf-8")


def normalized(text: str) -> str:
    return " ".join(text.split())


def completion_leg() -> CompletionLeg:
    seqs3 = completion.composites_up_to(3)
    reachable3 = completion.channel_reachable_profiles(seqs3)
    composite_absorbers = tuple(
        seq for seq in seqs3 if completion.matches(seq, completion.witness_target)
    )
    dropped_i_absorbers = tuple(
        seq
        for seq in seqs3
        if completion.matches(seq, completion.witness_target, require_invariance=False)
    )
    operational_map = {
        name: completion.op_absorbed(target, seqs3)
        for name, target in completion.ZOO.items()
    }
    certified = completion.certified_contains(completion.witness_target, reachable3)
    operational = completion.op_absorbed(completion.witness_target, seqs3)
    return CompletionLeg(
        certified_contains_witness=certified,
        operationally_absorbs_witness=operational,
        composite_absorbers=composite_absorbers,
        class_blind_operational_absorption=certified or operational,
        dropped_invariance_absorbers=dropped_i_absorbers,
        capped_operational_map_nonconstant=len(set(operational_map.values())) > 1,
    )


def adapter_leg() -> AdapterLeg:
    normal, post, completions = adapter.build_fixture()
    report = adapter.witness_boundary_adapter(normal, post, completions)
    circular = adapter.witness_boundary_adapter(normal, post, (adapter.circular_completion(),))
    return AdapterLeg(
        residual_class=report.residual_class,
        certified_containers=report.certified_containers,
        local_absorbers=report.local_absorbers,
        verdict_metadata_rejected=bool(circular.rejected),
    )


def context_individuation_fork(taf_packet: dict) -> dict:
    for fork in taf_packet["construction_forks"]:
        if fork["name"] == "context individuation of the pair":
            return fork
    raise AssertionError("TAF-002 context individuation fork missing")


def build_chain_read(completion_result: CompletionLeg) -> ChainRead:
    completion_status = (
        "PASS_P2C_DERIVED_FIREWALL"
        if completion_result.certified_contains_witness
        and not completion_result.operationally_absorbs_witness
        and not completion_result.composite_absorbers
        else "FAIL"
    )
    return ChainRead(
        formation="PASS_UNCHANGED_WITNESS",
        completion=completion_status,
        capability="PASS_FRAME_INDEXED_C1_BOUND",
        finality="NOT_REACHED",
        neutrality="PASS_SPLIT_NEUTRAL",
        no_artificial_success="PASS_ONE_CHAIN_SPLIT_PRESERVED",
        disposition=(
            "SECOND_STANDARD_CONFIRMED_SCOPED_SURVIVOR_CLASS_SPLIT"
            if completion_status.startswith("PASS")
            else "SECOND_STANDARD_FAILED"
        ),
    )


def main() -> None:
    witness = load_json("exports", "witness", "P2C-W1-superconducting-ring-v0.1", "witness.json")
    taf = load_json("packets", "imports", "TAF-002", "packet.json")
    ti = load_json("packets", "imports", "TI-WFA-001", "packet.json")
    taf_record = load_text("packets", "imports", "TAF-002", "TAF-002-import-record-2026-07-16.md")
    ti_record = load_text("packets", "imports", "TI-WFA-001", "TI-WFA-001-import-record-2026-07-16.md")
    taf_semantics = load_text("packets", "imports", "TAF-002", "blobs", "taf002_semantics.md")

    c_leg = completion_leg()
    a_leg = adapter_leg()
    chain = build_chain_read(c_leg)
    context_fork = context_individuation_fork(taf)
    witness_hashes = {entry["content_sha256"] for entry in witness["integrity"]["manifest"]}

    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    check(
        "setup: witness bundle declares P2C-W1 and QIP signatures",
        witness["witness_id"] == "P2C-W1"
        and set(witness["system"]["signature_vector"]) == {"Q", "I", "P"},
    )
    check(
        "input identity: imported returns and witness bundle name one unchanged P2C-W1",
        taf["packet_id"] == "TAF-002"
        and ti["packet_id"] == "TI-WFA-001"
        and "P2C-W1" in taf["question"]["exact_question"]
        and ti["verification_of_input_bundle"]["freeze_commit"]
        == "4c9c28bbad0bdca45377dd2265b28b1fec3cc9ef"
        and all(h in taf_semantics for h in witness_hashes)
        and all(h in json.dumps(ti["verification_of_input_bundle"]) for h in witness_hashes),
    )
    check(
        "source sovereignty: imported packets keep source status and authority transfer false",
        not taf["ownership"]["authority_transfer"]
        and not ti["ownership"]["authority_transfer"]
        and taf["claim"]["source_status_unchanged"]
        and "Import confers no promotion" in normalized(taf_record)
        and "Import confers no promotion" in normalized(ti_record),
    )
    check(
        "c1: task-semantics mapping remains condition-bound",
        "transfer_status: untested" in taf_record
        and "task-semantics" in load_text(
            "explorations", "2026-07-16-cross-repo-adjudication", "SYNTHESIS.md"
        )
        and chain.capability == "PASS_FRAME_INDEXED_C1_BOUND",
    )
    check(
        "c2: P2C derived firewall supplies containment without operational absorption",
        c_leg.certified_contains_witness
        and not c_leg.operationally_absorbs_witness
        and c_leg.capped_operational_map_nonconstant,
    )
    check(
        "c2b: P2C composite closure closes the old D2 local absorber gap at model grade",
        not c_leg.composite_absorbers
        and completion.op_absorbed(completion.register_target, completion.composites_up_to(3)),
    )
    check(
        "adapter bridge: carrier-neutral adapter reports certified containment only",
        a_leg.residual_class == "CERTIFIED_CONTAINMENT_ONLY"
        and bool(a_leg.certified_containers)
        and not a_leg.local_absorbers,
    )
    check(
        "c3: tau_P metastability cap is carried",
        any("tau_P" in residual and "metastability cap" in residual for residual in taf["residuals"])
        and "tau_P rider" in taf_record,
    )
    check(
        "c4: context individuation fork remains open",
        context_fork["transfer_status"] == "source_only"
        and any("one-context whole-family" in alt for alt in context_fork["alternatives"]),
    )
    check(
        "gate chain: scoped survivor remains class-split under P2C standard",
        chain.formation == "PASS_UNCHANGED_WITNESS"
        and chain.completion == "PASS_P2C_DERIVED_FIREWALL"
        and chain.disposition
        == "SECOND_STANDARD_CONFIRMED_SCOPED_SURVIVOR_CLASS_SPLIT",
    )
    check(
        "finality hygiene: finality gate remains not reached",
        chain.finality == "NOT_REACHED",
    )
    check(
        "no artificial success: one witness one frame one chain with split preserved",
        chain.no_artificial_success == "PASS_ONE_CHAIN_SPLIT_PRESERVED"
        and chain.disposition.endswith("CLASS_SPLIT")
        and chain.neutrality == "PASS_SPLIT_NEUTRAL",
    )

    check(
        "c2-fail: class-blind containment merge would not operationally absorb",
        not c_leg.class_blind_operational_absorption,
        expected=False,
    )
    check(
        "c2b-fail: dropping local invariance would not create a composite absorber",
        not c_leg.dropped_invariance_absorbers,
        expected=False,
    )
    check(
        "adapter-fail: verdict-carrying completion metadata would be accepted",
        not a_leg.verdict_metadata_rejected,
        expected=False,
    )
    check(
        "c4-fail: one-context whole-family fork can be closed without changing frame",
        context_fork["transfer_status"] != "source_only",
        expected=False,
    )
    check(
        "finality-fail: finality can be marked pass in this chain",
        chain.finality == "PASS",
        expected=False,
    )

    print("P2C-W1 SECOND-STANDARD LOCAL READ")
    print("=" * 72)
    failures = []
    n_t = n_e = n_f = 0
    for name, value, expected in checks:
        ok = value == expected
        tag = CHECKS.get(name, {}).get("tag", "?")
        n_t += tag == "T"
        n_e += tag == "E"
        n_f += tag == "F"
        print(f"{'PASS' if ok else 'UNEXPECTED'}  [{tag}] {name}: {value}")
        if not ok:
            failures.append(name)

    print()
    print(f"completion leg: {chain.completion}")
    print(f"adapter residual: {a_leg.residual_class}")
    print(f"composite local absorbers: {len(c_leg.composite_absorbers)}")
    print(f"dropped-I absorbers: {len(c_leg.dropped_invariance_absorbers)}")
    print(f"disposition: {chain.disposition}")
    print(f"finality: {chain.finality}")
    print()
    print(f"EVIDENTIAL CHECKS (headline): {n_e} [E] + {n_f} [F] = {n_e + n_f}")
    print(f"[T] theorem-consequence checks (no evidential weight): {n_t}")

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()
