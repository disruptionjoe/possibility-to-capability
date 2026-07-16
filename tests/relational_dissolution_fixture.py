"""Relational-dissolution fixture for binary sign fibers.

Question: can a flip-invariant observable over binary orbit-member data depend
on an absolute representative, or must it factor through relative alignment?

This finite fixture models a connected binary sign fiber as assignments
{-1,+1}^n with the global flip c -> -c. Pairwise products c_i*c_j are the
relative-alignment profile. The fixture exhaustively enumerates Boolean
observables for n=3 and n=4 and checks that every global-flip-invariant
observable factors through that relative profile.

It does not establish physics, novelty, GU/TI/TaF source truth, or the
nonexistence of richer native-formalism escapes. It prices one binary toy door:
absolute representative dependence is gauge unless an anchor is supplied.
"""

from __future__ import annotations

import itertools

Sign = int
Configuration = tuple[Sign, ...]
Profile = tuple[int, ...]


CHECKS = {
    "model: global flip is an involution": {"tag": "T"},
    "e1: relative profile separates flip orbits for n=3": {"tag": "E"},
    "e2: relative profile separates flip orbits for n=4": {"tag": "E"},
    "e3: every invariant Boolean observable factors through profile for n=3": {"tag": "E"},
    "e4: every invariant Boolean observable factors through profile for n=4": {"tag": "E"},
    "e5: relative-alignment observable is invariant and nonconstant": {"tag": "E"},
    "e6: anchored separator is covariant only when anchor flips too": {"tag": "E"},
    "f1: absolute first-coordinate selector violates flip invariance": {
        "tag": "F",
        "protects": "e3: every invariant Boolean observable factors through profile for n=3",
    },
    "f2: held-fixed anchor selector violates flip invariance": {
        "tag": "F",
        "protects": "e6: anchored separator is covariant only when anchor flips too",
    },
    "f3: disconnected two-edge profile fails to separate n=4 orbits": {
        "tag": "F",
        "protects": "e2: relative profile separates flip orbits for n=4",
    },
}


def configurations(n: int) -> tuple[Configuration, ...]:
    return tuple(itertools.product((-1, 1), repeat=n))


def flip(config: Configuration) -> Configuration:
    return tuple(-bit for bit in config)


def pairwise_profile(config: Configuration) -> Profile:
    return tuple(
        config[i] * config[j]
        for i in range(len(config))
        for j in range(i + 1, len(config))
    )


def disconnected_two_edge_profile(config: Configuration) -> Profile:
    return (config[0] * config[1], config[2] * config[3])


def same_flip_orbit(left: Configuration, right: Configuration) -> bool:
    return left == right or flip(left) == right


def profile_separates_orbits(
    configs: tuple[Configuration, ...],
    profile_fn,
) -> bool:
    seen: dict[Profile, Configuration] = {}
    for config in configs:
        profile = profile_fn(config)
        prior = seen.get(profile)
        if prior is not None and not same_flip_orbit(config, prior):
            return False
        seen[profile] = config
    return True


def truth_table(configs: tuple[Configuration, ...], predicate) -> tuple[bool, ...]:
    return tuple(bool(predicate(config)) for config in configs)


def boolean_table(config_count: int, mask: int) -> tuple[bool, ...]:
    return tuple(bool((mask >> idx) & 1) for idx in range(config_count))


def is_flip_invariant(
    configs: tuple[Configuration, ...],
    table: tuple[bool, ...],
) -> bool:
    index = {config: idx for idx, config in enumerate(configs)}
    return all(table[idx] == table[index[flip(config)]]
               for idx, config in enumerate(configs))


def factors_through_profile(
    configs: tuple[Configuration, ...],
    table: tuple[bool, ...],
    profile_fn=pairwise_profile,
) -> bool:
    values: dict[Profile, bool] = {}
    for config, value in zip(configs, table):
        profile = profile_fn(config)
        if profile in values and values[profile] != value:
            return False
        values[profile] = value
    return True


def invariant_observable_summary(n: int) -> tuple[bool, int, int]:
    configs = configurations(n)
    total = 1 << len(configs)
    invariant_count = 0
    for mask in range(total):
        table = boolean_table(len(configs), mask)
        if is_flip_invariant(configs, table):
            invariant_count += 1
            if not factors_through_profile(configs, table):
                return False, invariant_count, total
    return True, invariant_count, total


def relative_alignment_observable(config: Configuration) -> bool:
    return config[0] * config[1] == 1


def absolute_first_coordinate(config: Configuration) -> bool:
    return config[0] == 1


def anchored_separator(config: Configuration, anchor: Configuration) -> bool:
    return config[0] == anchor[0]


def anchored_separator_is_covariant(n: int) -> bool:
    configs = configurations(n)
    return all(
        anchored_separator(config, anchor)
        == anchored_separator(flip(config), flip(anchor))
        for config in configs
        for anchor in configs
    )


def main() -> int:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        if name not in CHECKS:
            raise KeyError(f"check is missing from CHECKS registry: {name}")
        checks.append((name, bool(value), expected))

    configs3 = configurations(3)
    configs4 = configurations(4)
    inv3_ok, inv3_count, total3 = invariant_observable_summary(3)
    inv4_ok, inv4_count, total4 = invariant_observable_summary(4)
    relative_table = truth_table(configs4, relative_alignment_observable)
    absolute_table = truth_table(configs4, absolute_first_coordinate)
    fixed_anchor = (1, 1, 1, 1)
    fixed_anchor_table = truth_table(
        configs4,
        lambda config: anchored_separator(config, fixed_anchor),
    )

    check("model: global flip is an involution",
          all(flip(flip(config)) == config for config in configs4))
    check("e1: relative profile separates flip orbits for n=3",
          profile_separates_orbits(configs3, pairwise_profile))
    check("e2: relative profile separates flip orbits for n=4",
          profile_separates_orbits(configs4, pairwise_profile))
    check("e3: every invariant Boolean observable factors through profile for n=3",
          inv3_ok and inv3_count == 16 and total3 == 256)
    check("e4: every invariant Boolean observable factors through profile for n=4",
          inv4_ok and inv4_count == 256 and total4 == 65536)
    check("e5: relative-alignment observable is invariant and nonconstant",
          is_flip_invariant(configs4, relative_table)
          and factors_through_profile(configs4, relative_table)
          and any(relative_table)
          and not all(relative_table))
    check("e6: anchored separator is covariant only when anchor flips too",
          anchored_separator_is_covariant(4))
    check("f1: absolute first-coordinate selector violates flip invariance",
          is_flip_invariant(configs4, absolute_table),
          expected=False)
    check("f2: held-fixed anchor selector violates flip invariance",
          is_flip_invariant(configs4, fixed_anchor_table),
          expected=False)
    check("f3: disconnected two-edge profile fails to separate n=4 orbits",
          profile_separates_orbits(configs4, disconnected_two_edge_profile),
          expected=False)

    checked_names = {name for name, _, _ in checks}
    missing = set(CHECKS) - checked_names
    if missing:
        raise AssertionError(f"registry entries were not checked: {sorted(missing)}")

    failures: list[str] = []
    tag_counts = {"T": 0, "E": 0, "F": 0}
    print("RELATIONAL DISSOLUTION FIXTURE")
    print("=" * 74)
    print(f"n=3 invariant Boolean observables: {inv3_count} of {total3}")
    print(f"n=4 invariant Boolean observables: {inv4_count} of {total4}")
    for name, value, expected in checks:
        ok = value == expected
        tag = CHECKS[name]["tag"]
        tag_counts[tag] += 1
        suffix = ""
        if tag == "F" and expected is False:
            suffix = "   (failing direction: checker CAN fail)"
        print(f"{'PASS' if ok else 'UNEXPECTED'}  [{tag}] {name}: {value}{suffix}")
        if not ok:
            failures.append(name)

    evidential = tag_counts["E"] + tag_counts["F"]
    print(f"\nEVIDENTIAL CHECKS: {tag_counts['E']} [E] + {tag_counts['F']} [F] = {evidential}")
    print(f"[T] theorem-consequence checks (no evidential weight): {tag_counts['T']}")
    print("Interpretation: binary flip-invariant observables dissolve to relative alignment.")
    print("Held-fixed anchors and absolute selectors consume the missing orbit representative.")

    if failures:
        print("\nUNEXPECTED RESULTS:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("All checks match expectations. Exit 0.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
