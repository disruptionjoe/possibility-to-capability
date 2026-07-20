"""Preflight the frozen GU co-flip packet for the P2C boundary discriminator.

This fixture tests packet-to-discriminator admissibility.  It does not import
GU truth, execute the proposed W1-W3 ladder, or classify capability/finality.
"""

from __future__ import annotations

from dataclasses import dataclass


SOURCE_PACKET = "GU-COFLIP-HOLONOMY-FREEZE-2026-07-20"
SOURCE_COMMIT = "32e3603f12aae3fc76298534c47a204b5584b171"


@dataclass(frozen=True)
class PacketFacts:
    frozen_source_identity: bool
    independent_source_identity: bool
    hamiltonian: bool
    transition_frame: bool
    matched_resource_budget: bool
    matched_access_frame: bool
    matched_task_delta: bool
    native_response: bool
    completion_rival: bool


FACTS = PacketFacts(
    frozen_source_identity=True,
    independent_source_identity=False,
    hamiltonian=False,
    transition_frame=False,
    matched_resource_budget=False,
    matched_access_frame=False,
    matched_task_delta=False,
    native_response=False,
    completion_rival=False,
)


CHECKS = {
    "source freeze is pinned": {"tag": "E"},
    "preflight abstains": {"tag": "E"},
    "independent identity remains missing": {"tag": "E"},
    "transition frame remains missing": {"tag": "E"},
    "resource frame remains missing": {"tag": "E"},
    "access frame remains missing": {"tag": "E"},
    "task delta remains missing": {"tag": "E"},
    "native response remains missing": {"tag": "E"},
    "completion rival remains missing": {"tag": "E"},
    "Hamiltonian nonclaim is preserved": {"tag": "E"},
    "freeze-fail: unfrozen source is rejected": {
        "tag": "F",
        "protects": "source freeze is pinned",
    },
    "abstention-fail: complete packet reaches discriminator": {
        "tag": "F",
        "protects": "preflight abstains",
    },
}


REQUIRED_FOR_ADJUDICATION = (
    "independent_source_identity",
    "transition_frame",
    "matched_resource_budget",
    "matched_access_frame",
    "matched_task_delta",
    "native_response",
    "completion_rival",
)


def missing_fields(facts: PacketFacts) -> tuple[str, ...]:
    return tuple(name for name in REQUIRED_FOR_ADJUDICATION if not getattr(facts, name))


def preflight(facts: PacketFacts) -> str:
    if not facts.frozen_source_identity:
        return "REJECT_UNFROZEN_SOURCE"
    if missing_fields(facts):
        return "ABSTAIN_PACKET_NOT_ADJUDICABLE"
    return "READY_FOR_BOUNDARY_DISCRIMINATOR"


def main() -> None:
    missing = missing_fields(FACTS)
    checks: list[tuple[str, bool]] = []

    def check(name: str, passed: bool) -> None:
        checks.append((name, passed))

    check("source freeze is pinned", FACTS.frozen_source_identity)
    check("preflight abstains", preflight(FACTS) == "ABSTAIN_PACKET_NOT_ADJUDICABLE")
    check("independent identity remains missing", "independent_source_identity" in missing)
    check("transition frame remains missing", "transition_frame" in missing)
    check("resource frame remains missing", "matched_resource_budget" in missing)
    check("access frame remains missing", "matched_access_frame" in missing)
    check("task delta remains missing", "matched_task_delta" in missing)
    check("native response remains missing", "native_response" in missing)
    check("completion rival remains missing", "completion_rival" in missing)
    check("Hamiltonian nonclaim is preserved", not FACTS.hamiltonian)
    check(
        "freeze-fail: unfrozen source is rejected",
        preflight(PacketFacts(False, False, False, False, False, False, False, False, False))
        == "REJECT_UNFROZEN_SOURCE",
    )
    check(
        "abstention-fail: complete packet reaches discriminator",
        preflight(PacketFacts(True, True, True, True, True, True, True, True, True))
        == "READY_FOR_BOUNDARY_DISCRIMINATOR",
    )
    failures = [name for name, passed in checks if not passed]

    print("CO-FLIP / HOLONOMY BOUNDARY PREFLIGHT")
    print(f"source={SOURCE_PACKET}@{SOURCE_COMMIT}")
    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'} [{CHECKS[name]['tag']}] {name}")
    print(f"verdict={preflight(FACTS)}")
    print(f"missing={','.join(missing)}")
    n_e = sum(CHECKS[name]["tag"] == "E" for name, _ in checks)
    n_f = sum(CHECKS[name]["tag"] == "F" for name, _ in checks)
    print(f"EVIDENTIAL CHECKS (headline): {n_e} [E] + {n_f} [F] = {n_e + n_f}")

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()
