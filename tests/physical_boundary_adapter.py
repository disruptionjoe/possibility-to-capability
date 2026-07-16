"""Finite physical boundary/source-to-capability adapter.

Question: can P2C define a smallest source-neutral adapter that consumes
physical transition data and returns a testable residual without importing a
capability or issuance verdict as an input label?

This fixture is deliberately finite and exact. A physical frame contains a
budget and intervention channels. Each channel has a resource cost and an
observable response distribution. The adapter maps a frame to the set of exact
response signatures available under the budget, modulo outcome relabeling and
intervention names. A boundary delta is the gained/lost signature set.

The fixture is not a real physical witness. It is a contract-grade adapter
prototype with controls for invariance, composition, nonconstancy, circular
verdict labels, resource changes, and ordinary whole-family completions.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

Effect = tuple[Fraction, ...]


@dataclass(frozen=True)
class Channel:
    name: str
    cost: int
    response: tuple[tuple[str, Fraction], ...]
    metadata: tuple[tuple[str, str], ...] = ()

    def effect(self) -> Effect:
        totals: dict[str, Fraction] = {}
        for outcome, weight in self.response:
            if weight < 0:
                raise ValueError(f"negative probability in {self.name}")
            totals[outcome] = totals.get(outcome, Fraction(0)) + weight
        total = sum(totals.values(), Fraction(0))
        if total != 1:
            raise ValueError(f"response for {self.name} sums to {total}, not 1")
        return tuple(sorted(weight for weight in totals.values() if weight))


@dataclass(frozen=True)
class Frame:
    name: str
    budget: int
    channels: tuple[Channel, ...]

    def profile(self) -> frozenset[Effect]:
        """Available observable effects, ignoring names and verdict metadata."""
        return frozenset(ch.effect() for ch in self.channels if ch.cost <= self.budget)


@dataclass(frozen=True)
class BoundaryReport:
    pre_profile: frozenset[Effect]
    post_profile: frozenset[Effect]
    gained: frozenset[Effect]
    lost: frozenset[Effect]
    residual_class: str


def boundary_adapter(
    pre: Frame,
    post: Frame,
    completions: tuple[Frame, ...] = (),
) -> BoundaryReport:
    """Return a neutral residual class from physical input data only."""
    pre_profile = pre.profile()
    post_profile = post.profile()
    gained = post_profile - pre_profile
    lost = pre_profile - post_profile

    if not gained and not lost:
        residual = "NO_RESIDUAL"
    elif pre.budget != post.budget:
        residual = "RESOURCE_FRAME_CHANGED"
    elif gained and any(gained <= (completion.profile() - pre_profile)
                        or gained <= completion.profile()
                        for completion in completions):
        residual = "COMPLETION_ABSORBED"
    elif lost and not gained:
        residual = "RESTRICTION_RESIDUAL"
    else:
        residual = "UNEXPLAINED_EFFECT_RESIDUAL"

    return BoundaryReport(
        pre_profile=pre_profile,
        post_profile=post_profile,
        gained=frozenset(gained),
        lost=frozenset(lost),
        residual_class=residual,
    )


def apply_delta(profile: frozenset[Effect], report: BoundaryReport) -> frozenset[Effect]:
    return frozenset((profile - report.lost) | report.gained)


def relabel(frame: Frame, prefix: str) -> Frame:
    """Rename every record outcome. A valid adapter must be invariant to this."""
    channels = []
    for idx, channel in enumerate(frame.channels):
        mapping = {
            outcome: f"{prefix}_{idx}_{pos}"
            for pos, (outcome, _) in enumerate(channel.response)
        }
        channels.append(
            Channel(
                name=f"{prefix}_{channel.name}",
                cost=channel.cost,
                response=tuple((mapping[outcome], weight)
                               for outcome, weight in channel.response),
                metadata=channel.metadata,
            )
        )
    return Frame(name=f"{prefix}_{frame.name}", budget=frame.budget,
                 channels=tuple(channels))


def verdict_sensitive_bad_profile(frame: Frame) -> frozenset[tuple[Effect, tuple[tuple[str, str], ...]]]:
    """A deliberately bad profile used only as a circularity control."""
    return frozenset(
        (ch.effect(), ch.metadata)
        for ch in frame.channels
        if ch.cost <= frame.budget
    )


def name_sensitive_bad_profile(frame: Frame) -> frozenset[tuple[tuple[str, Fraction], ...]]:
    """A deliberately bad profile used only as a relabeling control."""
    return frozenset(
        tuple(sorted(ch.response))
        for ch in frame.channels
        if ch.cost <= frame.budget
    )


def effect_text(effects: frozenset[Effect]) -> str:
    def one(effect: Effect) -> str:
        return "[" + ",".join(str(x) for x in effect) + "]"

    return "{" + ", ".join(one(e) for e in sorted(effects)) + "}"


def build_frames() -> dict[str, Frame]:
    hold = Channel("hold", 1, (("dark", Fraction(1)),))
    coin = Channel("coin", 1, (("left", Fraction(1, 2)),
                               ("right", Fraction(1, 2))))
    trit = Channel("trit", 1, (("a", Fraction(1, 3)),
                               ("b", Fraction(1, 3)),
                               ("c", Fraction(1, 3))))
    high_cost_trit = Channel("high_cost_trit", 2, trit.response)
    verdict_duplicate = Channel(
        "declared_capability_gain",
        1,
        coin.response,
        metadata=(("desired_verdict", "capability_gain"),),
    )

    return {
        "base": Frame("base", 1, (hold, coin)),
        "positive": Frame("positive", 1, (hold, coin, trit)),
        "circular": Frame("circular", 1, (hold, coin, verdict_duplicate)),
        "resource_pre": Frame("resource_pre", 1, (hold, coin, high_cost_trit)),
        "resource_post": Frame("resource_post", 2, (hold, coin, high_cost_trit)),
        "completion_family": Frame("completion_family", 1, (hold, coin, trit)),
        "mid": Frame("mid", 1, (hold, coin, trit)),
        "final": Frame("final", 1, (
            hold,
            coin,
            trit,
            Channel("quart", 1, (("w", Fraction(1, 4)),
                                  ("x", Fraction(1, 4)),
                                  ("y", Fraction(1, 4)),
                                  ("z", Fraction(1, 4)))),
        )),
    }


def main() -> None:
    frames = build_frames()
    base = frames["base"]
    positive = frames["positive"]
    circular = frames["circular"]

    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    positive_report = boundary_adapter(base, positive)
    circular_report = boundary_adapter(base, circular)
    relabeled_report = boundary_adapter(relabel(base, "r"), relabel(positive, "r"))
    resource_report = boundary_adapter(frames["resource_pre"], frames["resource_post"])
    completion_report = boundary_adapter(
        base,
        positive,
        completions=(frames["completion_family"],),
    )

    # Invariance and composition laws.
    check("[T] relabel invariance: outcome names do not change gained effects",
          positive_report.gained == relabeled_report.gained
          and positive_report.residual_class == relabeled_report.residual_class)
    check("[F] relabel-fail: a name-sensitive profile would change under relabeling",
          name_sensitive_bad_profile(base) == name_sensitive_bad_profile(relabel(base, "r")),
          expected=False)
    d01 = boundary_adapter(base, frames["mid"])
    d12 = boundary_adapter(frames["mid"], frames["final"])
    d02 = boundary_adapter(base, frames["final"])
    composed_profile = apply_delta(apply_delta(base.profile(), d01), d12)
    direct_profile = apply_delta(base.profile(), d02)
    check("[T] composition: sequential boundary deltas equal the direct delta",
          composed_profile == direct_profile == frames["final"].profile())

    # Nonconstancy and controls.
    check("[E] positive control: same-budget new response leaves a residual",
          positive_report.gained
          and positive_report.residual_class == "UNEXPLAINED_EFFECT_RESIDUAL")
    check("[E] nonconstancy: positive and circular transitions have different reports",
          positive_report.residual_class != circular_report.residual_class
          and positive_report.gained != circular_report.gained)
    check("[E] circularity control: verdict metadata and duplicate channels are ignored",
          not circular_report.gained
          and circular_report.residual_class == "NO_RESIDUAL")
    check("[F] circularity-fail: a metadata-sensitive bad adapter would see a fake gain",
          verdict_sensitive_bad_profile(base) == verdict_sensitive_bad_profile(circular),
          expected=False)
    check("[E] resource control: budget change is not silently called capability",
          resource_report.gained
          and resource_report.residual_class == "RESOURCE_FRAME_CHANGED")
    check("[E] completion control: an ordinary whole-family completion absorbs the residual",
          completion_report.gained
          and completion_report.residual_class == "COMPLETION_ABSORBED")

    print("FINITE PHYSICAL BOUNDARY ADAPTER")
    print("=" * 72)
    failures = []
    for name, value, expected in checks:
        ok = value == expected
        tag = "PASS" if ok else "UNEXPECTED"
        suffix = "   (demonstrated failing direction)" if name.startswith("[F]") else ""
        print(f"{tag}  {name}: {value}{suffix}")
        if not ok:
            failures.append(name)
    print()
    print(f"base profile:     {effect_text(base.profile())}")
    print(f"positive gained:  {effect_text(positive_report.gained)}")
    print(f"positive class:   {positive_report.residual_class}")
    print(f"circular class:   {circular_report.residual_class}")
    print(f"resource class:   {resource_report.residual_class}")
    print(f"completion class: {completion_report.residual_class}")
    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()
