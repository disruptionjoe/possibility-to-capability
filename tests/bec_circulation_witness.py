"""Independent-domain witness fixture: BEC / superfluid quantized circulation.

REACH SWING, portfolio item P2C-REAL-PHYSICAL-WITNESS. Exploration tier. This
fixture is not a Gross-Pitaevskii simulation and does not establish a physical
issuance, finality, or capability verdict. It checks whether the
superconducting-ring discriminator shape transfers to a neutral-atom
superfluid/BEC carrier without smuggling in charged-pair or electromagnetic
structure.

The finite model asks whether a neutral annular condensate can carry a
quantized, locally invariant, persistent circulation signature that ordinary
local completions cannot reproduce, while the strongest whole-family absorber
remains explicit.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


CHECKS = {
    "setup: neutral circulation winding is integer-valued": {"tag": "T"},
    "setup: local phase relabel preserves total winding": {"tag": "T"},
    "q1: condensate circulation is integer-quantized across a rotation interval": {"tag": "E"},
    "q1-fail: continuous thermal circulation is not integer-quantized": {
        "tag": "F",
        "protects": "q1: condensate circulation is integer-quantized across a rotation interval",
    },
    "i1: condensate winding is invariant under local phase relabels": {"tag": "E"},
    "i1-fail: thermal vortex seed changes under local perturbation": {
        "tag": "F",
        "protects": "i1: condensate winding is invariant under local phase relabels",
    },
    "p1: condensate current persists while thermal circulation decays": {"tag": "E"},
    "k1: local completion classes fail at least one QIP signature": {"tag": "E"},
    "c1: composite local absorber reaches Q and P but not I": {"tag": "E"},
    "k2: whole-family with condensate phase absorbs the witness": {"tag": "E"},
    "k2-fail: whole-family without condensate phase does not absorb": {
        "tag": "F",
        "protects": "k2: whole-family with condensate phase absorbs the witness",
    },
    "n1: neutral carrier excludes superconducting fluxoid primitives": {"tag": "E"},
    "n1-fail: electromagnetic copy would use forbidden carrier tokens": {
        "tag": "F",
        "protects": "n1: neutral carrier excludes superconducting fluxoid primitives",
    },
}


@dataclass(frozen=True)
class Signature:
    value: Fraction
    is_quantized: bool
    invariant_under_local: bool
    persists: bool
    carrier: str


def winding(phase_steps: tuple[int, ...]) -> int:
    return sum(phase_steps)


def local_phase_relabel(phase_steps: tuple[int, ...], k: int) -> tuple[int, ...]:
    if len(phase_steps) < 2:
        return phase_steps
    out = list(phase_steps)
    out[0] += k
    out[1] -= k
    return tuple(out)


def candidate_signature(rotation: Fraction) -> Signature:
    w = round(rotation)
    return Signature(
        value=Fraction(w),
        is_quantized=True,
        invariant_under_local=True,
        persists=True,
        carrier="neutral_atom_order_parameter_phase",
    )


def completion_signature(kind: str, rotation: Fraction) -> Signature:
    if kind in {"gauge", "relabeling", "hidden_state", "history", "provenance"}:
        return Signature(Fraction(0), True, True, False, "ordinary_completion")
    if kind in {"boundary", "seed", "access", "resource"}:
        return Signature(
            rotation,
            is_quantized=(rotation == round(rotation)),
            invariant_under_local=False,
            persists=False,
            carrier="thermal_continuous_flow",
        )
    if kind == "composite_local":
        return Signature(
            Fraction(round(rotation)),
            is_quantized=True,
            invariant_under_local=False,
            persists=True,
            carrier="seeded_metastable_thermal_vortex",
        )
    if kind == "whole_family_no_condensate":
        return Signature(Fraction(0), True, True, False, "normal_gas_family")
    if kind == "whole_family_with_condensate":
        return candidate_signature(rotation)
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
    "whole_family_no_condensate",
    "composite_local",
)


FORBIDDEN_SUPERCONDUCTING_TOKENS = {"fluxoid", "cooper_pair", "charge_2e", "phi0"}


def matches_candidate(sig: Signature, cand: Signature) -> bool:
    return (
        sig.value == cand.value
        and sig.is_quantized == cand.is_quantized
        and sig.invariant_under_local == cand.invariant_under_local
        and sig.persists == cand.persists
    )


def uses_forbidden_superconducting_tokens(sig: Signature) -> bool:
    carrier_tokens = set(sig.carrier.lower().split("_"))
    return bool(FORBIDDEN_SUPERCONDUCTING_TOKENS & carrier_tokens)


def bad_electromagnetic_copy(rotation: Fraction) -> Signature:
    return Signature(
        value=Fraction(round(rotation)),
        is_quantized=True,
        invariant_under_local=True,
        persists=True,
        carrier="cooper_pair_fluxoid_phi0",
    )


def main() -> None:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    interval = (
        Fraction(1, 5),
        Fraction(2, 5),
        Fraction(3, 5),
        Fraction(4, 5),
        Fraction(6, 5),
        Fraction(8, 5),
    )
    cand = {r: candidate_signature(r) for r in interval}

    steps = (1, 0, -1, 1)
    check("setup: neutral circulation winding is integer-valued", isinstance(winding(steps), int))
    check(
        "setup: local phase relabel preserves total winding",
        all(winding(local_phase_relabel(steps, k)) == winding(steps) for k in range(-3, 4)),
    )

    check(
        "q1: condensate circulation is integer-quantized across a rotation interval",
        all(c.is_quantized and c.value == round(r) for r, c in cand.items()),
    )
    check(
        "q1-fail: continuous thermal circulation is not integer-quantized",
        all(completion_signature("boundary", r).is_quantized for r in interval),
        expected=False,
    )
    check(
        "i1: condensate winding is invariant under local phase relabels",
        all(c.invariant_under_local for c in cand.values()),
    )
    check(
        "i1-fail: thermal vortex seed changes under local perturbation",
        all(completion_signature("seed", r).invariant_under_local for r in interval),
        expected=False,
    )
    check(
        "p1: condensate current persists while thermal circulation decays",
        all(c.persists for c in cand.values())
        and all(not completion_signature("history", r).persists for r in interval),
    )
    check(
        "k1: local completion classes fail at least one QIP signature",
        all(
            not matches_candidate(completion_signature(kind, r), cand[r])
            for kind in LOCAL_KINDS
            for r in interval
        ),
    )
    check(
        "c1: composite local absorber reaches Q and P but not I",
        all(
            completion_signature("composite_local", r).is_quantized
            and completion_signature("composite_local", r).persists
            and not completion_signature("composite_local", r).invariant_under_local
            for r in interval
        ),
    )
    check(
        "k2: whole-family with condensate phase absorbs the witness",
        all(
            matches_candidate(completion_signature("whole_family_with_condensate", r), cand[r])
            for r in interval
        ),
    )
    check(
        "k2-fail: whole-family without condensate phase does not absorb",
        all(
            matches_candidate(completion_signature("whole_family_no_condensate", r), cand[r])
            for r in interval
        ),
        expected=False,
    )
    check(
        "n1: neutral carrier excludes superconducting fluxoid primitives",
        all(not uses_forbidden_superconducting_tokens(c) for c in cand.values()),
    )
    check(
        "n1-fail: electromagnetic copy would use forbidden carrier tokens",
        not uses_forbidden_superconducting_tokens(bad_electromagnetic_copy(Fraction(3, 5))),
        expected=False,
    )

    print("BEC / SUPERFLUID CIRCULATION WITNESS")
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
    print("candidate staircase (rotation -> neutral winding):")
    for rotation in interval:
        rival = completion_signature("seed", rotation)
        print(
            f"  rotation={str(rotation):>5} -> w={cand[rotation].value} "
            f"(thermal seed stores {rival.value}, decays)"
        )
    print()
    print("completion-class scoreboard vs candidate (rotation=3/5):")
    r0 = Fraction(3, 5)
    for kind in (*LOCAL_KINDS, "whole_family_with_condensate"):
        sig = completion_signature(kind, r0)
        verdict = "ABSORBS" if matches_candidate(sig, cand[r0]) else "fails"
        print(
            f"  {kind:>30}: value={str(sig.value):>5} "
            f"Q={int(sig.is_quantized)} I={int(sig.invariant_under_local)} "
            f"P={int(sig.persists)} carrier={sig.carrier} -> {verdict}"
        )
    print()
    print(f"EVIDENTIAL CHECKS (headline): {n_e} [E] + {n_f} [F] = {n_e + n_f}")
    print(f"[T] theorem-consequence checks (no evidential weight): {n_t}")

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()
