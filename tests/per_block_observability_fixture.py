"""Per-block observability fixture for the boundary-switch profile.

Question: can a global flip hide every absolute label while independent
per-block choices still leave neutral observable content in relative block
alignment?

This finite fixture models block switch values as sign assignments {-1,+1}^n.
The global flip negates every block and is treated as the unobservable absolute
label reversal. Independent per-block flips are the toy stand-in for multiple
block-local switch choices. Pairwise products are the relative-alignment
profile.

The fixture does not identify the switch operator, prove observer agency,
establish physics, or move GU/TI/TaF source truth. It tests one toy-grade
consequence of the boundary-switch interpretation: multiplicity can be visible
through relative structure even when the absolute bit is not.
"""

from __future__ import annotations

import itertools

Sign = int
Configuration = tuple[Sign, ...]
Profile = tuple[int, ...]


CHECKS = {
    "model: global flip is an involution": {"tag": "T"},
    "e1: single-block invariant observables are constants": {"tag": "E"},
    "e2: pairwise profile separates n=2 global-flip orbits": {"tag": "E"},
    "e3: pairwise profile separates n=3 global-flip orbits": {"tag": "E"},
    "e4: relative alignment is global-invariant and block-choice-sensitive": {"tag": "E"},
    "e5: independent per-block flips change the relative profile": {"tag": "E"},
    "e6: every n=3 invariant Boolean observable factors through pairwise profile": {"tag": "E"},
    "f1: absolute block selector violates global invariance": {
        "tag": "F",
        "protects": "e4: relative alignment is global-invariant and block-choice-sensitive",
    },
    "f2: single-block model has a choice-sensitive invariant observable": {
        "tag": "F",
        "protects": "e1: single-block invariant observables are constants",
    },
    "f3: first-pair-only profile separates all n=3 global-flip orbits": {
        "tag": "F",
        "protects": "e3: pairwise profile separates n=3 global-flip orbits",
    },
}


def configurations(n: int) -> tuple[Configuration, ...]:
    return tuple(itertools.product((-1, 1), repeat=n))


def global_flip(config: Configuration) -> Configuration:
    return tuple(-bit for bit in config)


def flip_block(config: Configuration, block: int) -> Configuration:
    return tuple(-bit if idx == block else bit for idx, bit in enumerate(config))


def pairwise_profile(config: Configuration) -> Profile:
    return tuple(
        config[i] * config[j]
        for i in range(len(config))
        for j in range(i + 1, len(config))
    )


def first_pair_only_profile(config: Configuration) -> Profile:
    return (config[0] * config[1],)


def same_global_orbit(left: Configuration, right: Configuration) -> bool:
    return left == right or global_flip(left) == right


def profile_separates_global_orbits(
    configs: tuple[Configuration, ...],
    profile_fn,
) -> bool:
    seen: dict[Profile, Configuration] = {}
    for config in configs:
        profile = profile_fn(config)
        prior = seen.get(profile)
        if prior is not None and not same_global_orbit(config, prior):
            return False
        seen[profile] = config
    return True


def boolean_table(config_count: int, mask: int) -> tuple[bool, ...]:
    return tuple(bool((mask >> idx) & 1) for idx in range(config_count))


def truth_table(configs: tuple[Configuration, ...], predicate) -> tuple[bool, ...]:
    return tuple(bool(predicate(config)) for config in configs)


def is_global_invariant(
    configs: tuple[Configuration, ...],
    table: tuple[bool, ...],
) -> bool:
    index = {config: idx for idx, config in enumerate(configs)}
    return all(table[idx] == table[index[global_flip(config)]]
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
        if is_global_invariant(configs, table):
            invariant_count += 1
            if not factors_through_profile(configs, table):
                return False, invariant_count, total
    return True, invariant_count, total


def table_is_sensitive_to_block_flip(
    configs: tuple[Configuration, ...],
    table: tuple[bool, ...],
    block: int,
) -> bool:
    index = {config: idx for idx, config in enumerate(configs)}
    return any(table[idx] != table[index[flip_block(config, block)]]
               for idx, config in enumerate(configs))


def global_invariant_choice_sensitive_exists(n: int) -> bool:
    configs = configurations(n)
    for mask in range(1 << len(configs)):
        table = boolean_table(len(configs), mask)
        if is_global_invariant(configs, table) and any(
            table_is_sensitive_to_block_flip(configs, table, block)
            for block in range(n)
        ):
            return True
    return False


def relative_alignment_01(config: Configuration) -> bool:
    return config[0] * config[1] == 1


def absolute_block_0_positive(config: Configuration) -> bool:
    return config[0] == 1


def main() -> int:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        if name not in CHECKS:
            raise KeyError(f"check is missing from CHECKS registry: {name}")
        checks.append((name, bool(value), expected))

    configs1 = configurations(1)
    configs2 = configurations(2)
    configs3 = configurations(3)
    inv1_ok, inv1_count, total1 = invariant_observable_summary(1)
    inv3_ok, inv3_count, total3 = invariant_observable_summary(3)
    relative_table = truth_table(configs3, relative_alignment_01)
    absolute_table = truth_table(configs3, absolute_block_0_positive)

    check("model: global flip is an involution",
          all(global_flip(global_flip(config)) == config for config in configs3))
    check("e1: single-block invariant observables are constants",
          inv1_ok and inv1_count == 2 and total1 == 4
          and not global_invariant_choice_sensitive_exists(1))
    check("e2: pairwise profile separates n=2 global-flip orbits",
          profile_separates_global_orbits(configs2, pairwise_profile))
    check("e3: pairwise profile separates n=3 global-flip orbits",
          profile_separates_global_orbits(configs3, pairwise_profile))
    check("e4: relative alignment is global-invariant and block-choice-sensitive",
          is_global_invariant(configs3, relative_table)
          and table_is_sensitive_to_block_flip(configs3, relative_table, 0)
          and table_is_sensitive_to_block_flip(configs3, relative_table, 1)
          and not table_is_sensitive_to_block_flip(configs3, relative_table, 2))
    check("e5: independent per-block flips change the relative profile",
          all(
              pairwise_profile(flip_block(config, block)) != pairwise_profile(config)
              for config in configs3
              for block in range(3)
          ))
    check("e6: every n=3 invariant Boolean observable factors through pairwise profile",
          inv3_ok and inv3_count == 16 and total3 == 256)
    check("f1: absolute block selector violates global invariance",
          is_global_invariant(configs3, absolute_table),
          expected=False)
    check("f2: single-block model has a choice-sensitive invariant observable",
          global_invariant_choice_sensitive_exists(1),
          expected=False)
    check("f3: first-pair-only profile separates all n=3 global-flip orbits",
          profile_separates_global_orbits(configs3, first_pair_only_profile),
          expected=False)

    checked_names = {name for name, _, _ in checks}
    missing = set(CHECKS) - checked_names
    if missing:
        raise AssertionError(f"registry entries were not checked: {sorted(missing)}")

    failures: list[str] = []
    tag_counts = {"T": 0, "E": 0, "F": 0}
    print("PER-BLOCK OBSERVABILITY FIXTURE")
    print("=" * 74)
    print(f"n=1 invariant Boolean observables: {inv1_count} of {total1}")
    print(f"n=3 invariant Boolean observables: {inv3_count} of {total3}")
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
    print("Interpretation: one global switch has no neutral observable content;")
    print("multiple block-local choices can be visible as relative alignment.")

    if failures:
        print("\nUNEXPECTED RESULTS:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("All checks match expectations. Exit 0.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
