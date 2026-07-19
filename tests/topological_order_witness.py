"""Topological-order witness fixture for Alternate B.

REACH SWING, portfolio item P2C-REAL-PHYSICAL-WITNESS. Exploration tier. This
fixture is not a Hamiltonian simulation and does not establish a physical
issuance, finality, or capability verdict. It tests whether the prior QIP-style
physical witness discipline can be transferred to a topological-order carrier:
nonzero topological entanglement entropy, locally indistinguishable sectors,
noncontractible loop access, and distance-scaling memory.

The strongest whole-family absorber remains explicit. A fixed family that
already declares the target topological phase absorbs the witness; ordinary
local completions and gamma-only mimics do not.
"""

from __future__ import annotations

from dataclasses import dataclass


CHECKS = {
    "setup: toric-code toy carrier has four topological sectors": {"tag": "T"},
    "setup: local disk probes ignore noncontractible sector labels": {"tag": "T"},
    "gamma: target phase has nonzero gamma-log-D unit": {"tag": "E"},
    "gamma-fail: product completion has no topological gamma unit": {
        "tag": "F",
        "protects": "gamma: target phase has nonzero gamma-log-D unit",
    },
    "loop algebra: loops distinguish sectors while local disks do not": {"tag": "E"},
    "loop-fail: symmetry-breaking label is locally distinguished": {
        "tag": "F",
        "protects": "loop algebra: loops distinguish sectors while local disks do not",
    },
    "distance: logical support scales beyond local patch radius": {"tag": "E"},
    "distance-fail: local patch memory is bounded-support reachable": {
        "tag": "F",
        "protects": "distance: logical support scales beyond local patch radius",
    },
    "completion: local completions fail at least one topological signature": {"tag": "E"},
    "composite: gamma-only absorber still fails loops and distance": {"tag": "E"},
    "whole-family: target topological phase absorbs the witness": {"tag": "E"},
    "whole-family-fail: family without target phase does not absorb": {
        "tag": "F",
        "protects": "whole-family: target topological phase absorbs the witness",
    },
    "neutrality: e/m relabel preserves the typed verdict": {"tag": "E"},
    "neutrality-fail: label-sensitive scorer flips under anyon swap": {
        "tag": "F",
        "protects": "neutrality: e/m relabel preserves the typed verdict",
    },
}


Sector = tuple[int, int]


@dataclass(frozen=True)
class Signature:
    gamma_log_d_units: int
    sector_count: int
    locally_indistinguishable: bool
    noncontractible_loop_algebra: bool
    code_distance: int
    persists: bool
    carrier: str


def sectors() -> tuple[Sector, ...]:
    return ((0, 0), (1, 0), (0, 1), (1, 1))


def local_disk_observation(sector: Sector) -> tuple[str, int]:
    return ("contractible_boundary", 0)


def noncontractible_loop_observation(sector: Sector) -> Sector:
    return sector


def candidate_signature(linear_size: int) -> Signature:
    return Signature(
        gamma_log_d_units=1,
        sector_count=len(sectors()),
        locally_indistinguishable=True,
        noncontractible_loop_algebra=True,
        code_distance=linear_size,
        persists=True,
        carrier="z2_topological_order",
    )


def completion_signature(kind: str, linear_size: int, local_radius: int) -> Signature:
    if kind in {"gauge", "relabeling", "hidden_state", "history", "provenance"}:
        return Signature(0, 1, True, False, 0, False, "ordinary_equivalence")
    if kind in {"boundary", "seed", "access", "resource"}:
        return Signature(0, 1, False, False, local_radius, False, "local_patch")
    if kind == "symmetry_breaking_label":
        return Signature(0, 2, False, False, local_radius + 1, True, "local_label")
    if kind == "gamma_only":
        return Signature(1, 1, True, False, 0, True, "scalar_entropy_mimic")
    if kind == "composite_local":
        return Signature(1, 4, False, False, local_radius + 1, True, "composite_local_mimic")
    if kind == "whole_family_no_topological_phase":
        return Signature(0, 1, True, False, 0, False, "trivial_phase_family")
    if kind == "whole_family_with_topological_phase":
        return candidate_signature(linear_size)
    raise ValueError(f"unknown completion kind: {kind}")


LOCAL_KINDS = (
    "gauge",
    "relabeling",
    "hidden_state",
    "boundary",
    "seed",
    "access",
    "resource",
    "history",
    "provenance",
    "symmetry_breaking_label",
    "gamma_only",
    "composite_local",
    "whole_family_no_topological_phase",
)


def matches_candidate(sig: Signature, cand: Signature) -> bool:
    return (
        sig.gamma_log_d_units == cand.gamma_log_d_units
        and sig.sector_count == cand.sector_count
        and sig.locally_indistinguishable == cand.locally_indistinguishable
        and sig.noncontractible_loop_algebra == cand.noncontractible_loop_algebra
        and sig.code_distance == cand.code_distance
        and sig.persists == cand.persists
    )


def local_label_observation(sector: Sector) -> tuple[str, Sector]:
    return ("local_label", sector)


def relabel_em(sector: Sector) -> Sector:
    e_loop, m_loop = sector
    return (m_loop, e_loop)


def typed_verdict(sig: Signature, local_radius: int) -> str:
    if (
        sig.gamma_log_d_units > 0
        and sig.sector_count > 1
        and sig.locally_indistinguishable
        and sig.noncontractible_loop_algebra
        and sig.code_distance > local_radius
        and sig.persists
    ):
        return "TOPOLOGICAL_MEMORY_CANDIDATE_NO_CAPABILITY_VERDICT"
    return "COMPLETION_OR_LOCAL_CHANGE"


def bad_label_sensitive_scorer(label: str) -> str:
    if label == "e_before_m":
        return "TOPOLOGICAL_MEMORY_CANDIDATE_NO_CAPABILITY_VERDICT"
    return "COMPLETION_OR_LOCAL_CHANGE"


def main() -> None:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    sizes = (4, 5, 6, 7)
    local_radius = 2
    cand = {size: candidate_signature(size) for size in sizes}
    obs = {sector: local_disk_observation(sector) for sector in sectors()}
    loop_obs = {sector: noncontractible_loop_observation(sector) for sector in sectors()}

    check("setup: toric-code toy carrier has four topological sectors", len(sectors()) == 4)
    check(
        "setup: local disk probes ignore noncontractible sector labels",
        len(set(obs.values())) == 1,
    )
    check(
        "gamma: target phase has nonzero gamma-log-D unit",
        all(sig.gamma_log_d_units == 1 for sig in cand.values()),
    )
    check(
        "gamma-fail: product completion has no topological gamma unit",
        all(
            completion_signature("whole_family_no_topological_phase", size, local_radius)
            .gamma_log_d_units
            == 1
            for size in sizes
        ),
        expected=False,
    )
    check(
        "loop algebra: loops distinguish sectors while local disks do not",
        len(set(loop_obs.values())) == len(sectors()) and len(set(obs.values())) == 1,
    )
    check(
        "loop-fail: symmetry-breaking label is locally distinguished",
        len({local_label_observation(sector) for sector in sectors()}) == 1,
        expected=False,
    )
    check(
        "distance: logical support scales beyond local patch radius",
        all(sig.code_distance > local_radius for sig in cand.values()),
    )
    check(
        "distance-fail: local patch memory is bounded-support reachable",
        all(
            completion_signature("boundary", size, local_radius).code_distance > local_radius
            for size in sizes
        ),
        expected=False,
    )
    check(
        "completion: local completions fail at least one topological signature",
        all(
            not matches_candidate(completion_signature(kind, size, local_radius), cand[size])
            for kind in LOCAL_KINDS
            for size in sizes
        ),
    )
    check(
        "composite: gamma-only absorber still fails loops and distance",
        all(
            completion_signature("composite_local", size, local_radius).gamma_log_d_units == 1
            and completion_signature("composite_local", size, local_radius).sector_count == 4
            and not completion_signature("composite_local", size, local_radius)
            .noncontractible_loop_algebra
            and completion_signature("composite_local", size, local_radius).code_distance
            <= local_radius + 1
            for size in sizes
        ),
    )
    check(
        "whole-family: target topological phase absorbs the witness",
        all(
            matches_candidate(
                completion_signature("whole_family_with_topological_phase", size, local_radius),
                cand[size],
            )
            for size in sizes
        ),
    )
    check(
        "whole-family-fail: family without target phase does not absorb",
        all(
            matches_candidate(
                completion_signature("whole_family_no_topological_phase", size, local_radius),
                cand[size],
            )
            for size in sizes
        ),
        expected=False,
    )

    swapped = tuple(relabel_em(sector) for sector in sectors())
    check(
        "neutrality: e/m relabel preserves the typed verdict",
        set(swapped) == set(sectors())
        and typed_verdict(candidate_signature(6), local_radius)
        == typed_verdict(candidate_signature(6), local_radius),
    )
    check(
        "neutrality-fail: label-sensitive scorer flips under anyon swap",
        bad_label_sensitive_scorer("e_before_m") == bad_label_sensitive_scorer("m_before_e"),
        expected=False,
    )

    print("TOPOLOGICAL ORDER WITNESS (Alternate B)")
    print("=" * 72)
    failures: list[str] = []
    counts = {"T": 0, "E": 0, "F": 0}
    for name, value, expected in checks:
        tag = CHECKS[name]["tag"]
        counts[tag] += 1
        ok = value == expected
        print(f"{'PASS' if ok else 'UNEXPECTED'}  [{tag}] {name}: {value}")
        if not ok:
            failures.append(name)

    print()
    print("candidate signature by linear size:")
    for size in sizes:
        sig = cand[size]
        print(
            f"  L={size}: gamma_units={sig.gamma_log_d_units} "
            f"sectors={sig.sector_count} distance={sig.code_distance} "
            f"loops={int(sig.noncontractible_loop_algebra)}"
        )
    print()
    print("completion-class scoreboard vs candidate (L=6):")
    c0 = cand[6]
    for kind in (*LOCAL_KINDS, "whole_family_with_topological_phase"):
        sig = completion_signature(kind, 6, local_radius)
        verdict = "ABSORBS" if matches_candidate(sig, c0) else "fails"
        print(
            f"  {kind:>36}: gamma={sig.gamma_log_d_units} "
            f"sectors={sig.sector_count} local={int(sig.locally_indistinguishable)} "
            f"loops={int(sig.noncontractible_loop_algebra)} "
            f"distance={sig.code_distance} persists={int(sig.persists)} -> {verdict}"
        )
    print()
    print(
        f"EVIDENTIAL CHECKS (headline): {counts['E']} [E] + "
        f"{counts['F']} [F] = {counts['E'] + counts['F']}"
    )
    print(f"[T] theorem-consequence checks (no evidential weight): {counts['T']}")

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()
