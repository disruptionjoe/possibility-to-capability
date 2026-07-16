"""Finite null/completion closure for the physical boundary adapter.

Question: can the boundary adapter's supplied completion hook be replaced with
a small, declared closure class that absorbs ordinary novelty while remaining
too restricted to manufacture a capability or issuance verdict?

This fixture is not a real physical witness and does not adjudicate TI, TaF, or
GU truth. It is a receiver-owned finite pressure test for the middle
completion class named by the P2C portfolio.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from physical_boundary_adapter import Channel, Effect, Frame, boundary_adapter, effect_text


COMPLETION_KINDS = (
    "hidden_state",
    "boundary",
    "seed",
    "provenance",
    "resource",
    "whole_family",
    "history",
    "access",
    "relabeling",
    "gauge",
)

EQUIVALENCE_ONLY_KINDS = {"relabeling", "gauge"}
FORBIDDEN_METADATA_KEYS = {
    "desired_verdict",
    "claimed_level",
    "claimed_verdict",
    "capability_verdict",
    "issuance_verdict",
}


@dataclass(frozen=True)
class CompletionCandidate:
    kind: str
    channel: Channel
    provenance: str
    note: str

    def label(self) -> str:
        return f"{self.kind}:{self.channel.name}"


@dataclass(frozen=True)
class ClosureResult:
    frame: Frame
    added: tuple[str, ...]
    noops: tuple[str, ...]
    rejected: tuple[str, ...]

    def generated_profile(self, base: Frame) -> frozenset[Effect]:
        return self.frame.profile() - base.profile()


def has_forbidden_metadata(channel: Channel) -> bool:
    for key, value in channel.metadata:
        normalized_key = key.lower()
        normalized_value = value.lower()
        if normalized_key in FORBIDDEN_METADATA_KEYS:
            return True
        if "verdict" in normalized_key:
            return True
        if "capability_gain" in normalized_value or "issuance" in normalized_value:
            return True
    return False


def validate_candidate(
    seed: Frame,
    current_profile: frozenset[Effect],
    candidate: CompletionCandidate,
) -> str | None:
    if candidate.kind not in COMPLETION_KINDS:
        return "unknown completion kind"
    if not candidate.provenance:
        return "missing provenance"
    if candidate.channel.cost > seed.budget:
        return "changes the normalized resource frame"
    if has_forbidden_metadata(candidate.channel):
        return "carries a verdict or desired level"

    effect = candidate.channel.effect()
    if candidate.kind in EQUIVALENCE_ONLY_KINDS and effect not in current_profile:
        return "equivalence completion cannot add a new observable effect"
    if candidate.kind == "resource":
        if ("resource_audit", "same_budget") not in candidate.channel.metadata:
            return "resource completion lacks same-budget audit"
    if candidate.kind == "provenance":
        if ("provenance", "frozen") not in candidate.channel.metadata:
            return "provenance completion is not frozen"
    return None


def close_frame(
    seed: Frame,
    candidates: tuple[CompletionCandidate, ...],
    omitted_kinds: frozenset[str] = frozenset(),
) -> ClosureResult:
    """Close a frame under admissible finite middle completions."""
    channels = list(seed.channels)
    current_profile = seed.profile()
    added: list[str] = []
    noops: list[str] = []
    rejected: list[str] = []

    for candidate in candidates:
        if candidate.kind in omitted_kinds:
            continue

        label = candidate.label()
        reason = validate_candidate(seed, current_profile, candidate)
        if reason is not None:
            rejected.append(f"{label} ({reason})")
            continue

        effect = candidate.channel.effect()
        if effect in current_profile:
            noops.append(label)
            continue

        channels.append(candidate.channel)
        current_profile = frozenset(set(current_profile) | {effect})
        added.append(label)

    return ClosureResult(
        frame=Frame(f"{seed.name}_completion_closure", seed.budget, tuple(channels)),
        added=tuple(added),
        noops=tuple(noops),
        rejected=tuple(rejected),
    )


def channel(
    name: str,
    weights: tuple[Fraction, ...],
    metadata: tuple[tuple[str, str], ...] = (),
    cost: int = 1,
) -> Channel:
    response = tuple((f"{name}_{idx}", weight) for idx, weight in enumerate(weights))
    return Channel(name=name, cost=cost, response=response, metadata=metadata)


def build_fixture() -> tuple[Frame, Frame, Frame, tuple[CompletionCandidate, ...]]:
    hold = channel("hold", (Fraction(1),))
    coin = channel("coin", (Fraction(1, 2), Fraction(1, 2)))
    trit = channel("trit", (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)))
    quart = channel("quart", (
        Fraction(1, 4),
        Fraction(1, 4),
        Fraction(1, 4),
        Fraction(1, 4),
    ))

    base = Frame("base", 1, (hold, coin))
    ordinary_post = Frame("ordinary_post", 1, (hold, coin, trit))
    escape_post = Frame("escape_post", 1, (hold, coin, quart))

    candidates = (
        CompletionCandidate(
            "hidden_state",
            channel("hidden_refinement", (Fraction(1, 2), Fraction(1, 2))),
            "declared latent-state refinement",
            "Does not change the observable profile.",
        ),
        CompletionCandidate(
            "boundary",
            channel("boundary_medium", (Fraction(1, 2), Fraction(1, 4), Fraction(1, 4))),
            "declared boundary environment",
            "Adds an ordinary boundary-mediated response.",
        ),
        CompletionCandidate(
            "seed",
            channel("seed_coin", (Fraction(1, 2), Fraction(1, 2))),
            "declared stochastic seed",
            "Does not turn stochastic availability into capability by itself.",
        ),
        CompletionCandidate(
            "provenance",
            channel("provenance_hold", (Fraction(1),), metadata=(("provenance", "frozen"),)),
            "frozen receiver provenance",
            "Records that provenance completions can be no-ops.",
        ),
        CompletionCandidate(
            "resource",
            channel(
                "resource_normalized",
                (Fraction(2, 3), Fraction(1, 3)),
                metadata=(("resource_audit", "same_budget"),),
            ),
            "same-budget resource audit",
            "Adds only after resource accounting is normalized.",
        ),
        CompletionCandidate(
            "whole_family",
            channel("whole_family_trit", (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))),
            "declared whole-family rival",
            "The load-bearing ordinary rival for the positive residual.",
        ),
        CompletionCandidate(
            "history",
            channel("history_hold", (Fraction(1),)),
            "declared completed history",
            "A completed history cannot add a new response here.",
        ),
        CompletionCandidate(
            "access",
            channel("access_coin", (Fraction(1, 2), Fraction(1, 2))),
            "declared access expansion",
            "Access-only change duplicates an already available effect.",
        ),
        CompletionCandidate(
            "relabeling",
            channel("renamed_coin", (Fraction(1, 2), Fraction(1, 2))),
            "declared record relabeling",
            "Equivalence-only completions may not create new effects.",
        ),
        CompletionCandidate(
            "gauge",
            channel("gauge_coin", (Fraction(1, 2), Fraction(1, 2))),
            "declared gauge representative",
            "Gauge completions preserve the observable profile.",
        ),
    )

    return base, ordinary_post, escape_post, candidates


def circular_candidate() -> CompletionCandidate:
    return CompletionCandidate(
        "whole_family",
        channel(
            "declared_capability_gain",
            (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)),
            metadata=(("desired_verdict", "capability_gain"),),
        ),
        "self-labeled verdict",
        "Rejected because the desired conclusion is carried as metadata.",
    )


def expensive_escape_candidate() -> CompletionCandidate:
    return CompletionCandidate(
        "whole_family",
        channel(
            "unbudgeted_quart",
            (Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(1, 4)),
            cost=2,
        ),
        "unbudgeted family extension",
        "Rejected because it changes the normalized resource frame.",
    )


def omission_table(
    base: Frame,
    ordinary_post: Frame,
    candidates: tuple[CompletionCandidate, ...],
) -> dict[str, str]:
    table: dict[str, str] = {}
    for kind in COMPLETION_KINDS:
        closure = close_frame(base, candidates, omitted_kinds=frozenset({kind}))
        report = boundary_adapter(base, ordinary_post, completions=(closure.frame,))
        table[kind] = report.residual_class
    return table


def main() -> None:
    base, ordinary_post, escape_post, candidates = build_fixture()

    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    closure = close_frame(base, candidates)
    reversed_closure = close_frame(base, tuple(reversed(candidates)))
    split_closure = close_frame(close_frame(base, candidates[:5]).frame, candidates[5:])
    ordinary_report = boundary_adapter(base, ordinary_post, completions=(closure.frame,))
    escape_report = boundary_adapter(base, escape_post, completions=(closure.frame,))
    circular_closure = close_frame(base, (circular_candidate(),))
    circular_report = boundary_adapter(base, ordinary_post, completions=(circular_closure.frame,))
    expensive_closure = close_frame(base, (expensive_escape_candidate(),))
    expensive_report = boundary_adapter(base, escape_post, completions=(expensive_closure.frame,))
    omissions = omission_table(base, ordinary_post, candidates)

    covered_kinds = {
        label.split(":", maxsplit=1)[0]
        for label in (*closure.added, *closure.noops)
    }

    check("[T] class coverage: every declared middle completion class is represented",
          covered_kinds == set(COMPLETION_KINDS))
    check("[T] no legitimate candidate is rejected", not closure.rejected)
    check("[T] composition: order reversal preserves the generated profile",
          closure.frame.profile() == reversed_closure.frame.profile())
    check("[T] composition: staged closure equals one-shot closure",
          closure.frame.profile() == split_closure.frame.profile())
    check("[E] ordinary residual absorbed by declared whole-family closure",
          ordinary_report.residual_class == "COMPLETION_ABSORBED")
    check("[E] omission mutant: removing whole_family reopens the residual",
          omissions["whole_family"] == "UNEXPLAINED_EFFECT_RESIDUAL")
    check("[E] omission mutant: other single omissions keep this residual absorbed",
          all(
              residual == "COMPLETION_ABSORBED"
              for kind, residual in omissions.items()
              if kind != "whole_family"
          ))
    check("[E] escape target: undeclared quart response remains unexplained",
          escape_report.residual_class == "UNEXPLAINED_EFFECT_RESIDUAL")
    check("[E] circularity rejection: verdict-carrying completion is rejected",
          circular_closure.rejected
          and circular_report.residual_class == "UNEXPLAINED_EFFECT_RESIDUAL")
    check("[E] resource bound: unbudgeted completion cannot absorb the escape",
          expensive_closure.rejected
          and expensive_report.residual_class == "UNEXPLAINED_EFFECT_RESIDUAL")

    print("FINITE PHYSICAL NULL/COMPLETION CLOSURE")
    print("=" * 72)
    failures = []
    for name, value, expected in checks:
        ok = value == expected
        tag = "PASS" if ok else "UNEXPECTED"
        print(f"{tag}  {name}: {value}")
        if not ok:
            failures.append(name)

    print()
    print(f"base profile:       {effect_text(base.profile())}")
    print(f"closure generated:  {effect_text(closure.generated_profile(base))}")
    print(f"ordinary class:     {ordinary_report.residual_class}")
    print(f"escape class:       {escape_report.residual_class}")
    print("omission mutants:")
    for kind in COMPLETION_KINDS:
        print(f"  - omit {kind}: {omissions[kind]}")
    print(f"rejected circular:  {tuple(circular_closure.rejected)}")
    print(f"rejected resource:  {tuple(expensive_closure.rejected)}")

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()
