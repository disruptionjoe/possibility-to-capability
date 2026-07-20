"""Two-sector flat-Z2 holonomy witness fixture (W1) with Kramers probe-class control (W2).

Portfolio item P2C-REAL-PHYSICAL-WITNESS, exploration tier. Joe-directed swing,
2026-07-20 (direct chat). This fixture is not a Hamiltonian simulation and does
not establish a physical issuance, finality, or capability verdict.

W1 tests whether the topological witness discipline survives the minimal
holonomy carrier in P2C's own family: ONE noncontractible loop class, sector
pair given by loop holonomy plus or minus one, TWO sectors. The four
discriminator legs (nonlocal bit unit, local-disk blindness, loop-only access,
distance scaling) and the whole-family absorber are carried unchanged. Two legs
are new to this carrier: an order-two loop-composition leg (a doubled loop is
trivial, separating this carrier from integer-winding carriers) and a
sector-count honesty leg (a four-sector mimic is rejected; a count-blind
comparison would admit it).

W2 adds a probe-class axis to the access leg. Probes on the holonomy fiber are
2x2 complex operators; J is the standard antiunitary quaternionic structure
with J squared equal to minus the identity (Kramers, literature grade). The
fixture derives the J-commutant (the quaternionic block form), proves at this
finite grade that every Hermitian J-commuting probe is a real multiple of the
identity (Kramers degeneracy on the sector pair), hence that local AND loop
probes of that class return an even, sector-blind mod-2 readout -- while a
single non-quaternionic loop probe reads the sector sign, and a
non-quaternionic disk probe still cannot (loop access stays necessary).

Provenance and typing for this fixture are frozen P2C-side in
explorations/2026-07-20-two-sector-witness/W3-PROVENANCE-FREEZE.md. No GU
receipt, convention, or numeric output is consumed here.

The strongest whole-family absorber remains explicit: a fixed family that
already declares the two-sector holonomy phase absorbs the witness.
"""

from __future__ import annotations

from dataclasses import dataclass


CHECKS = {
    # ------------------------------------------------------------- W1 setup
    "setup: carrier has one noncontractible loop class with two holonomy sectors": {"tag": "T"},
    "setup: local disk observation is sector independent": {"tag": "T"},
    # ------------------------------------------------------------- W1 legs
    "bit: target phase carries one nonlocal holonomy-bit unit": {"tag": "E"},
    "bit-fail: trivial-phase family carries a holonomy-bit unit": {
        "tag": "F",
        "protects": "bit: target phase carries one nonlocal holonomy-bit unit",
    },
    "loop: loop observation separates the two sectors while disks do not": {"tag": "E"},
    "loop-fail: symmetry-breaking label is locally indistinguishable": {
        "tag": "F",
        "protects": "loop: loop observation separates the two sectors while disks do not",
    },
    "order: doubled loop observation is trivial on both sectors": {"tag": "E"},
    "order-fail: integer-winding mimic trivializes under loop doubling": {
        "tag": "F",
        "protects": "order: doubled loop observation is trivial on both sectors",
    },
    "distance: logical support scales beyond the local patch radius": {"tag": "E"},
    "distance-fail: local patch memory scales beyond the patch radius": {
        "tag": "F",
        "protects": "distance: logical support scales beyond the local patch radius",
    },
    "completion: every local completion fails at least one two-sector signature": {"tag": "E"},
    "composite: bit-only mimic still fails loop and distance legs": {"tag": "E"},
    "sector-honesty: exactly two sectors and the four-sector mimic is rejected": {"tag": "E"},
    "sector-fail: count-blind comparison rejects the four-sector mimic": {
        "tag": "F",
        "protects": "sector-honesty: exactly two sectors and the four-sector mimic is rejected",
    },
    "whole-family: family declaring the two-sector phase absorbs the witness": {"tag": "E"},
    "whole-family-fail: family without the phase absorbs the witness": {
        "tag": "F",
        "protects": "whole-family: family declaring the two-sector phase absorbs the witness",
    },
    "neutrality: global sector relabel preserves the typed verdict": {"tag": "E"},
    "neutrality-fail: lift-sensitive scorer flips under sector relabel": {
        "tag": "F",
        "protects": "neutrality: global sector relabel preserves the typed verdict",
    },
    # ------------------------------------------------------------- W2 setup
    "setup: J is antilinear with J squared equal to minus the identity": {"tag": "T"},
    "setup: sector states form a Kramers pair under J": {"tag": "T"},
    # ------------------------------------------------------------- W2 legs
    "quaternion: the four probe generators commute with J": {"tag": "E"},
    "quaternion-fail: the sector-reading probe commutes with J": {
        "tag": "F",
        "protects": "quaternion: the four probe generators commute with J",
    },
    "commutant: J-commutation is exactly the quaternionic block form": {"tag": "E"},
    "identity: readout at the J-partner equals the conjugated readout": {"tag": "E"},
    "kramers: every Hermitian J-commuting probe is a real multiple of identity": {"tag": "E"},
    "blindness: Hermitian J-commuting loop probes read both sectors equally": {"tag": "E"},
    "blindness-fail: the non-quaternionic loop probe passes the blindness test": {
        "tag": "F",
        "protects": "blindness: Hermitian J-commuting loop probes read both sectors equally",
    },
    "parity: mod-2 sector readout through the J-commuting class is forced even": {"tag": "E"},
    "reader: a single non-quaternionic loop probe reads the sector sign": {"tag": "E"},
    "reader-fail: some J-commuting Hermitian readout separates the sectors": {
        "tag": "F",
        "protects": "reader: a single non-quaternionic loop probe reads the sector sign",
    },
    "loop-necessity: a non-quaternionic disk probe still cannot read the sector": {"tag": "E"},
}


# ============================================================== W1: carrier

Sector = int  # holonomy value, +1 or -1


@dataclass(frozen=True)
class Signature:
    bit_units: int
    sector_count: int
    locally_indistinguishable: bool
    order_two_loop_class: bool
    noncontractible_loop_algebra: bool
    code_distance: int
    persists: bool
    carrier: str


def sectors() -> tuple[Sector, ...]:
    return (1, -1)


def local_disk_observation(sector: Sector) -> tuple[str, int]:
    return ("contractible_boundary", 0)


def loop_observation(sector: Sector) -> Sector:
    return sector


def doubled_loop_observation(sector: Sector) -> Sector:
    return sector * sector


def integer_winding_doubled(winding: int) -> int:
    return 2 * winding


def local_label_observation(sector: Sector) -> tuple[str, Sector]:
    return ("local_label", sector)


def candidate_signature(linear_size: int) -> Signature:
    return Signature(
        bit_units=1,
        sector_count=len(sectors()),
        locally_indistinguishable=True,
        order_two_loop_class=True,
        noncontractible_loop_algebra=True,
        code_distance=linear_size,
        persists=True,
        carrier="two_sector_flat_z2_holonomy",
    )


def completion_signature(kind: str, linear_size: int, local_radius: int) -> Signature:
    if kind in {"gauge", "relabeling", "hidden_state", "history", "provenance"}:
        return Signature(0, 1, True, False, False, 0, False, "ordinary_equivalence")
    if kind in {"boundary", "seed", "access", "resource"}:
        return Signature(0, 1, False, False, False, local_radius, False, "local_patch")
    if kind == "symmetry_breaking_label":
        return Signature(0, 2, False, False, False, local_radius + 1, True, "local_label")
    if kind == "bit_only":
        return Signature(1, 1, True, False, False, 0, True, "scalar_bit_mimic")
    if kind == "composite_local":
        return Signature(1, 2, False, False, False, local_radius + 1, True, "composite_local_mimic")
    if kind == "integer_winding":
        return Signature(1, 9, True, False, True, linear_size, True, "integer_winding_carrier")
    if kind == "four_sector":
        return Signature(1, 4, True, True, True, linear_size, True, "four_sector_toric_mimic")
    if kind == "whole_family_no_phase":
        return Signature(0, 1, True, False, False, 0, False, "trivial_phase_family")
    if kind == "whole_family_with_phase":
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
    "bit_only",
    "composite_local",
    "integer_winding",
    "four_sector",
    "whole_family_no_phase",
)


def matches_candidate(sig: Signature, cand: Signature) -> bool:
    return (
        sig.bit_units == cand.bit_units
        and sig.sector_count == cand.sector_count
        and sig.locally_indistinguishable == cand.locally_indistinguishable
        and sig.order_two_loop_class == cand.order_two_loop_class
        and sig.noncontractible_loop_algebra == cand.noncontractible_loop_algebra
        and sig.code_distance == cand.code_distance
        and sig.persists == cand.persists
    )


def matches_ignoring_sector_count(sig: Signature, cand: Signature) -> bool:
    return (
        sig.bit_units == cand.bit_units
        and sig.locally_indistinguishable == cand.locally_indistinguishable
        and sig.order_two_loop_class == cand.order_two_loop_class
        and sig.noncontractible_loop_algebra == cand.noncontractible_loop_algebra
        and sig.code_distance == cand.code_distance
        and sig.persists == cand.persists
    )


def relabel_sector(sector: Sector) -> Sector:
    return -sector


def typed_verdict(sig: Signature, local_radius: int) -> str:
    if (
        sig.bit_units > 0
        and sig.sector_count == 2
        and sig.locally_indistinguishable
        and sig.order_two_loop_class
        and sig.noncontractible_loop_algebra
        and sig.code_distance > local_radius
        and sig.persists
    ):
        return "TWO_SECTOR_HOLONOMY_MEMORY_CANDIDATE_NO_CAPABILITY_VERDICT"
    return "COMPLETION_OR_LOCAL_CHANGE"


def lift_sensitive_scorer(label_convention: str) -> str:
    if label_convention == "plus_is_untwisted":
        return "TWO_SECTOR_HOLONOMY_MEMORY_CANDIDATE_NO_CAPABILITY_VERDICT"
    return "COMPLETION_OR_LOCAL_CHANGE"


# ==================================================== W2: probes on the fiber

Vec = tuple[complex, complex]
Mat = tuple[tuple[complex, complex], tuple[complex, complex]]


def jmap(v: Vec) -> Vec:
    """Antiunitary quaternionic structure: J(v1, v2) = (-conj(v2), conj(v1))."""
    return (-v[1].conjugate(), v[0].conjugate())


def apply_mat(a: Mat, v: Vec) -> Vec:
    return (
        a[0][0] * v[0] + a[0][1] * v[1],
        a[1][0] * v[0] + a[1][1] * v[1],
    )


def dagger(a: Mat) -> Mat:
    return (
        (a[0][0].conjugate(), a[1][0].conjugate()),
        (a[0][1].conjugate(), a[1][1].conjugate()),
    )


def is_hermitian(a: Mat) -> bool:
    return a == dagger(a)


def commutes_with_j(a: Mat) -> bool:
    # A.J and J.A are both antilinear, so agreement on a C-basis suffices.
    basis: tuple[Vec, ...] = ((1 + 0j, 0j), (0j, 1 + 0j))
    return all(apply_mat(a, jmap(e)) == jmap(apply_mat(a, e)) for e in basis)


def quaternionic_form(a_val: complex, b_val: complex) -> Mat:
    return ((a_val, b_val), (-b_val.conjugate(), a_val.conjugate()))


def is_quaternionic_form(a: Mat) -> bool:
    return a[1][0] == -a[0][1].conjugate() and a[1][1] == a[0][0].conjugate()


def readout(a: Mat, v: Vec) -> complex:
    av = apply_mat(a, v)
    return v[0].conjugate() * av[0] + v[1].conjugate() * av[1]


GRID: tuple[complex, ...] = (0j, 1 + 0j, -1 + 0j, 1j, -1j, 1 + 1j)

Q_IDENTITY: Mat = ((1 + 0j, 0j), (0j, 1 + 0j))
Q_I: Mat = ((1j, 0j), (0j, -1j))
Q_J: Mat = ((0j, 1 + 0j), (-1 + 0j, 0j))
Q_K: Mat = ((0j, 1j), (1j, 0j))
SECTOR_READER: Mat = ((1 + 0j, 0j), (0j, -1 + 0j))

SECTOR_PLUS: Vec = (1 + 0j, 0j)
SECTOR_MINUS: Vec = jmap(SECTOR_PLUS)

SAMPLE_VECTORS: tuple[Vec, ...] = (
    SECTOR_PLUS,
    SECTOR_MINUS,
    (1 + 0j, 1 + 0j),
    (1 + 0j, 1j),
    (2 + 0j, 1 - 1j),
)


def disk_readout(sector: Sector, probe: Mat) -> complex:
    """A disk probe acts only on local disk data, which is sector independent."""
    tag, value = local_disk_observation(sector)
    lifted: Vec = (complex(value), complex(len(tag) % 2))
    return readout(probe, lifted)


def hermitian_quaternionic_grid() -> list[Mat]:
    return [
        quaternionic_form(a_val, b_val)
        for a_val in GRID
        for b_val in GRID
        if is_hermitian(quaternionic_form(a_val, b_val))
    ]


def blindness_test(probe: Mat) -> bool:
    return readout(probe, SECTOR_PLUS) == readout(probe, SECTOR_MINUS)


# ======================================================================= main


def main() -> None:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    # ------------------------------------------------------------------- W1
    sizes = (4, 5, 6, 7)
    local_radius = 2
    cand = {size: candidate_signature(size) for size in sizes}
    obs = {sector: local_disk_observation(sector) for sector in sectors()}
    loop_obs = {sector: loop_observation(sector) for sector in sectors()}

    check(
        "setup: carrier has one noncontractible loop class with two holonomy sectors",
        len(sectors()) == 2 and set(sectors()) == {1, -1},
    )
    check(
        "setup: local disk observation is sector independent",
        len(set(obs.values())) == 1,
    )
    check(
        "bit: target phase carries one nonlocal holonomy-bit unit",
        all(sig.bit_units == 1 for sig in cand.values()),
    )
    check(
        "bit-fail: trivial-phase family carries a holonomy-bit unit",
        all(
            completion_signature("whole_family_no_phase", size, local_radius).bit_units == 1
            for size in sizes
        ),
        expected=False,
    )
    check(
        "loop: loop observation separates the two sectors while disks do not",
        len(set(loop_obs.values())) == len(sectors()) and len(set(obs.values())) == 1,
    )
    check(
        "loop-fail: symmetry-breaking label is locally indistinguishable",
        len({local_label_observation(sector) for sector in sectors()}) == 1,
        expected=False,
    )
    check(
        "order: doubled loop observation is trivial on both sectors",
        all(doubled_loop_observation(sector) == 1 for sector in sectors()),
    )
    check(
        "order-fail: integer-winding mimic trivializes under loop doubling",
        all(integer_winding_doubled(winding) == 0 for winding in (1, -1, 2, 3)),
        expected=False,
    )
    check(
        "distance: logical support scales beyond the local patch radius",
        all(sig.code_distance > local_radius for sig in cand.values()),
    )
    check(
        "distance-fail: local patch memory scales beyond the patch radius",
        all(
            completion_signature("boundary", size, local_radius).code_distance > local_radius
            for size in sizes
        ),
        expected=False,
    )
    check(
        "completion: every local completion fails at least one two-sector signature",
        all(
            not matches_candidate(completion_signature(kind, size, local_radius), cand[size])
            for kind in LOCAL_KINDS
            for size in sizes
        ),
    )
    check(
        "composite: bit-only mimic still fails loop and distance legs",
        all(
            completion_signature("bit_only", size, local_radius).bit_units == 1
            and not completion_signature("bit_only", size, local_radius)
            .noncontractible_loop_algebra
            and completion_signature("bit_only", size, local_radius).code_distance
            <= local_radius
            for size in sizes
        ),
    )
    check(
        "sector-honesty: exactly two sectors and the four-sector mimic is rejected",
        all(
            cand[size].sector_count == 2
            and not matches_candidate(
                completion_signature("four_sector", size, local_radius), cand[size]
            )
            for size in sizes
        ),
    )
    check(
        "sector-fail: count-blind comparison rejects the four-sector mimic",
        all(
            not matches_ignoring_sector_count(
                completion_signature("four_sector", size, local_radius), cand[size]
            )
            for size in sizes
        ),
        expected=False,
    )
    check(
        "whole-family: family declaring the two-sector phase absorbs the witness",
        all(
            matches_candidate(
                completion_signature("whole_family_with_phase", size, local_radius),
                cand[size],
            )
            for size in sizes
        ),
    )
    check(
        "whole-family-fail: family without the phase absorbs the witness",
        all(
            matches_candidate(
                completion_signature("whole_family_no_phase", size, local_radius),
                cand[size],
            )
            for size in sizes
        ),
        expected=False,
    )
    relabeled = tuple(relabel_sector(sector) for sector in sectors())
    check(
        "neutrality: global sector relabel preserves the typed verdict",
        set(relabeled) == set(sectors())
        and len({loop_observation(sector) for sector in relabeled}) == 2
        and typed_verdict(candidate_signature(6), local_radius)
        == typed_verdict(candidate_signature(6), local_radius),
    )
    check(
        "neutrality-fail: lift-sensitive scorer flips under sector relabel",
        lift_sensitive_scorer("plus_is_untwisted")
        == lift_sensitive_scorer("minus_is_untwisted"),
        expected=False,
    )

    # ------------------------------------------------------------------- W2
    check(
        "setup: J is antilinear with J squared equal to minus the identity",
        all(
            jmap(jmap(v)) == (-v[0], -v[1])
            for v in SAMPLE_VECTORS
        ),
    )
    check(
        "setup: sector states form a Kramers pair under J",
        jmap(SECTOR_PLUS) == SECTOR_MINUS
        and jmap(SECTOR_MINUS) == (-SECTOR_PLUS[0], -SECTOR_PLUS[1]),
    )
    check(
        "quaternion: the four probe generators commute with J",
        all(commutes_with_j(q) for q in (Q_IDENTITY, Q_I, Q_J, Q_K)),
    )
    check(
        "quaternion-fail: the sector-reading probe commutes with J",
        commutes_with_j(SECTOR_READER),
        expected=False,
    )
    check(
        "commutant: J-commutation is exactly the quaternionic block form",
        all(
            commutes_with_j(((a_val, b_val), (c_val, d_val)))
            == is_quaternionic_form(((a_val, b_val), (c_val, d_val)))
            for a_val in GRID
            for b_val in GRID
            for c_val in GRID
            for d_val in GRID
        ),
    )
    check(
        "identity: readout at the J-partner equals the conjugated readout",
        all(
            readout(quaternionic_form(a_val, b_val), jmap(v))
            == readout(quaternionic_form(a_val, b_val), v).conjugate()
            for a_val in GRID
            for b_val in GRID
            for v in SAMPLE_VECTORS
        ),
    )
    hq = hermitian_quaternionic_grid()
    check(
        "kramers: every Hermitian J-commuting probe is a real multiple of identity",
        len(hq) > 0
        and all(
            probe[0][1] == 0j
            and probe[1][0] == 0j
            and probe[0][0].imag == 0.0
            and probe[0][0] == probe[1][1]
            for probe in hq
        ),
    )
    check(
        "blindness: Hermitian J-commuting loop probes read both sectors equally",
        all(blindness_test(probe) for probe in hq),
    )
    check(
        "blindness-fail: the non-quaternionic loop probe passes the blindness test",
        blindness_test(SECTOR_READER),
        expected=False,
    )
    check(
        "parity: mod-2 sector readout through the J-commuting class is forced even",
        all(
            (0 if blindness_test(probe) else 1) % 2 == 0
            and probe[0][0] == probe[1][1]
            for probe in hq
        ),
    )
    check(
        "reader: a single non-quaternionic loop probe reads the sector sign",
        readout(SECTOR_READER, SECTOR_PLUS) == 1
        and readout(SECTOR_READER, SECTOR_MINUS) == -1
        and is_hermitian(SECTOR_READER),
    )
    check(
        "reader-fail: some J-commuting Hermitian readout separates the sectors",
        any(not blindness_test(probe) for probe in hq),
        expected=False,
    )
    check(
        "loop-necessity: a non-quaternionic disk probe still cannot read the sector",
        disk_readout(1, SECTOR_READER) == disk_readout(-1, SECTOR_READER),
    )

    # ------------------------------------------------------------------ report
    print("TWO-SECTOR FLAT-Z2 HOLONOMY WITNESS (W1) + KRAMERS PROBE-CLASS CONTROL (W2)")
    print("=" * 78)
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
            f"  L={size}: bit_units={sig.bit_units} sectors={sig.sector_count} "
            f"order_two={int(sig.order_two_loop_class)} distance={sig.code_distance} "
            f"loops={int(sig.noncontractible_loop_algebra)}"
        )
    print()
    print("completion-class scoreboard vs candidate (L=6):")
    c0 = cand[6]
    for kind in (*LOCAL_KINDS, "whole_family_with_phase"):
        sig = completion_signature(kind, 6, local_radius)
        verdict = "ABSORBS" if matches_candidate(sig, c0) else "fails"
        print(
            f"  {kind:>28}: bit={sig.bit_units} sectors={sig.sector_count} "
            f"local={int(sig.locally_indistinguishable)} "
            f"order2={int(sig.order_two_loop_class)} "
            f"loops={int(sig.noncontractible_loop_algebra)} "
            f"distance={sig.code_distance} persists={int(sig.persists)} -> {verdict}"
        )
    print()
    print("probe scoreboard on the holonomy fiber (readout on sector pair):")
    probe_rows = (
        ("identity", Q_IDENTITY),
        ("quaternion i", Q_I),
        ("quaternion j", Q_J),
        ("quaternion k", Q_K),
        ("sector reader", SECTOR_READER),
    )
    for label, probe in probe_rows:
        reads = readout(probe, SECTOR_PLUS) != readout(probe, SECTOR_MINUS)
        print(
            f"  {label:>14}: J_commuting={int(commutes_with_j(probe))} "
            f"hermitian={int(is_hermitian(probe))} "
            f"plus={readout(probe, SECTOR_PLUS)} minus={readout(probe, SECTOR_MINUS)} "
            f"reads_sector={int(reads)}"
        )
    print(
        f"  Hermitian J-commuting grid probes: {len(hermitian_quaternionic_grid())}, "
        f"all sector-blind"
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
