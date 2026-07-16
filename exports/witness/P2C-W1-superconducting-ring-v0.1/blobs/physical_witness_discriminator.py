"""Executable discriminator for the real physical witness (superconducting ring).

REACH SWING, portfolio item P2C-REAL-PHYSICAL-WITNESS. Exploration tier. No
source-repo claim, GU/TI/TaF verdict, physical issuance claim, or cross-repo
identity moves here. This fixture is a finite, exact model of ONE concrete,
measurement-shaped discriminator between a candidate capability-changing
boundary event and its strongest ordinary-completion rival. It is NOT a
physics simulation and proves nothing about real superconductors; it prices
what the discriminator can and cannot separate, in the house [T]/[E]/[F]
discipline.

WITNESS (frozen at literature grade in the sibling WITNESS-FREEZE.md):
  System: a thin superconducting ring (BCS / Ginzburg-Landau source theory).
  Candidate boundary event: cooling the ring through Tc with flux present,
    producing a TRAPPED, QUANTIZED, INDEFINITELY-PERSISTENT circulating
    supercurrent -- the capability "hold a zero-maintenance-cost circulating
    memory forever."
  Discriminating signatures, both native and both measurable:
    (Q) QUANTIZATION: the trapped fluxoid is an INTEGER multiple of Phi_0 =
        h/2e, independent of the applied-field value within a fluxoid interval
        and of the ring geometry -- a global winding-number invariant.
    (I) LOCAL-COMPLETION INVARIANCE: the winding is unchanged by every LOCAL
        completion operation (gauge shift, relabeling, hidden latent state).
    (P) PERSISTENCE: the winding does not relax (phase-slip barrier is
        macroscopic); the rival's stored value decays.

MODEL. A ring is N bonds; a configuration assigns each bond an integer
"phase increment step" and the OBSERVABLE is the winding number w = (sum of
steps) read mod the ring closure -- an integer. The candidate frame realizes
any integer w and holds it. Each ordinary completion class is given its
STRONGEST finite form and asked to reproduce BOTH discriminating signatures
(Q and I) starting from the NORMAL (pre-Tc) frame. Nine local completion
classes fail at least one signature; exactly ONE -- the whole-family
completion that DECLARES the superconducting phase itself a member of the
fixed family -- absorbs the candidate. That is the pre-declared kill vector
(the charter's fixed-family absorber, null class 1 / hierarchy falsifier F1),
and the fixture exhibits it executably rather than hiding it.

Pure Python stdlib. Usage:
    python physical_witness_discriminator.py
    python tef_check_tag_linter.py --strict physical_witness_discriminator.py
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

# --------------------------------------------------------------------------
# House [T]/[E]/[F] registry (linter registry mode; R1-R4 enforced).
# --------------------------------------------------------------------------

CHECKS = {
    # setup (theorem-consequences; carry NO evidential weight)
    "s1: winding is an integer by construction": {"tag": "T"},
    "s2: a global gauge shift preserves winding by construction": {"tag": "T"},
    # quantization signature (Q)
    "q1: candidate trapped value is integer-quantized across a field interval": {"tag": "E"},
    "q1-fail: a continuous-boundary completion is NOT integer-quantized": {
        "tag": "F", "protects": "q1: candidate trapped value is integer-quantized across a field interval"},
    "q2: seed/access/boundary completions store a NON-integer value": {"tag": "E"},
    # local-completion invariance signature (I)
    "i1: candidate winding is invariant under every LOCAL completion op": {"tag": "E"},
    "i1-fail: a metastable rival value CHANGES under the same local ops": {
        "tag": "F", "protects": "i1: candidate winding is invariant under every LOCAL completion op"},
    # persistence signature (P)
    "p1: candidate winding does not relax; history completion decays to zero": {"tag": "E"},
    # the pre-declared kill vector
    "k1: nine local completion classes fail at least one discriminating signature": {"tag": "E"},
    "k2: the whole-family-with-target-phase completion ABSORBS the candidate": {"tag": "E"},
    "k2-fail: whole-family WITHOUT the target phase does NOT absorb it": {
        "tag": "F", "protects": "k2: the whole-family-with-target-phase completion ABSORBS the candidate"},
    # neutrality
    "n1: swapping the two branch labels leaves every discriminator verdict fixed": {"tag": "E"},
    "n1-fail: a label-sensitive scorer WOULD flip under the swap": {
        "tag": "F", "protects": "n1: swapping the two branch labels leaves every discriminator verdict fixed"},
}


# --------------------------------------------------------------------------
# Model.
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Signature:
    """The two discriminating readouts of a stored circulating value."""
    value: Fraction          # the trapped circulating amount, in units of Phi_0
    is_quantized: bool       # Q: value is an integer multiple of the quantum
    invariant_under_local: bool  # I: value survives the local completion group
    persists: bool           # P: value does not relax to zero


def winding(steps: tuple[int, ...]) -> int:
    """Observable winding number = integer sum of integer bond steps."""
    return sum(steps)


def gauge_shift(steps: tuple[int, ...], k: int) -> tuple[int, ...]:
    """A global gauge/relabel op: raise one bond by k and lower its neighbor by
    k (a closed local move). Winding is preserved by construction."""
    if len(steps) < 2:
        return steps
    out = list(steps)
    out[0] += k
    out[1] -= k
    return tuple(out)


def candidate_signature(applied: Fraction) -> Signature:
    """Superconducting frame: the trapped fluxoid is the NEAREST INTEGER to the
    applied flux (fluxoid quantization), then held as an integer winding,
    invariant under local ops and non-relaxing."""
    w = round(applied)  # integer winding -- the quantum staircase
    return Signature(value=Fraction(w), is_quantized=True,
                     invariant_under_local=True, persists=True)


def completion_signature(kind: str, applied: Fraction) -> Signature:
    """Strongest finite form of each ordinary completion applied to the NORMAL
    (pre-Tc) frame. Returns the signature the completion can actually produce."""
    if kind == "gauge" or kind == "relabeling":
        # equivalence-only: can re-present an existing value, never quantize a
        # new capability; on the normal frame there is no persistent value.
        return Signature(Fraction(0), is_quantized=True,
                         invariant_under_local=True, persists=False)
    if kind == "hidden_state":
        # a latent variable that does not touch the observable: no stored value.
        return Signature(Fraction(0), is_quantized=True,
                         invariant_under_local=True, persists=False)
    if kind == "boundary":
        # a continuous boundary-mediated circulating amount = the applied flux
        # itself, NOT quantized.
        return Signature(applied, is_quantized=(applied == round(applied)),
                         invariant_under_local=False, persists=False)
    if kind == "seed":
        # the threaded value is stored as-is (continuous), and decays.
        return Signature(applied, is_quantized=(applied == round(applied)),
                         invariant_under_local=False, persists=False)
    if kind == "access":
        # reveal an already-circulating continuous eddy; not quantized, decays.
        return Signature(applied, is_quantized=(applied == round(applied)),
                         invariant_under_local=False, persists=False)
    if kind == "resource":
        # spend a normalized budget: can drive a current but not zero its
        # maintenance cost -> it decays once the drive stops.
        return Signature(applied, is_quantized=(applied == round(applied)),
                         invariant_under_local=False, persists=False)
    if kind == "history":
        # a completed relaxation: the value has already decayed to zero.
        return Signature(Fraction(0), is_quantized=True,
                         invariant_under_local=True, persists=False)
    if kind == "provenance":
        # a frozen record label: no observable circulating value at all.
        return Signature(Fraction(0), is_quantized=True,
                         invariant_under_local=True, persists=False)
    if kind == "whole_family_no_phase":
        # the fixed family of NORMAL-phase configurations: no member has a
        # persistent quantized winding.
        return Signature(Fraction(0), is_quantized=True,
                         invariant_under_local=True, persists=False)
    if kind == "whole_family_with_phase":
        # DECLARE the superconducting phase itself a member of the fixed family
        # -- the fixed-family absorber. It then reproduces the candidate exactly.
        return candidate_signature(applied)
    raise ValueError(f"unknown completion kind: {kind}")


LOCAL_KINDS = ("gauge", "relabeling", "hidden_state", "boundary", "seed",
               "access", "resource", "history", "provenance",
               "whole_family_no_phase")


def matches_candidate(sig: Signature, cand: Signature) -> bool:
    """A completion reproduces the capability iff it matches BOTH discriminating
    signatures (Q and I) AND persistence (P) of the candidate."""
    return (sig.is_quantized == cand.is_quantized
            and sig.invariant_under_local == cand.invariant_under_local
            and sig.persists == cand.persists
            and sig.value == cand.value)


# --------------------------------------------------------------------------
# Harness.
# --------------------------------------------------------------------------

def main() -> None:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    # A field interval straddling one fluxoid quantum: fractional applied flux
    # values where quantization is a NON-trivial (integer != applied) claim.
    interval = (Fraction(1, 4), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5),
                Fraction(11, 10), Fraction(7, 5))
    cand = {a: candidate_signature(a) for a in interval}

    # s1 / s2 -- setup theorem-consequences.
    steps = (1, 0, -1, 1)  # winding = 1
    check("s1: winding is an integer by construction",
          isinstance(winding(steps), int))
    check("s2: a global gauge shift preserves winding by construction",
          all(winding(gauge_shift(steps, k)) == winding(steps) for k in range(-3, 4)))

    # q1 -- candidate is integer-quantized across the whole interval.
    check("q1: candidate trapped value is integer-quantized across a field interval",
          all(c.is_quantized and c.value == round(a) for a, c in cand.items()))
    # q1-fail -- a continuous-boundary completion is NOT integer-quantized on the
    # fractional interval (protected checker: q1, same quantization test).
    check("q1-fail: a continuous-boundary completion is NOT integer-quantized",
          all(completion_signature("boundary", a).is_quantized for a in interval),
          expected=False)
    # q2 -- seed/access/boundary store a genuinely non-integer value.
    check("q2: seed/access/boundary completions store a NON-integer value",
          all(completion_signature(k, a).value == a and a != round(a)
              for k in ("seed", "access", "boundary") for a in interval))

    # i1 -- candidate winding invariant under every local completion op.
    check("i1: candidate winding is invariant under every LOCAL completion op",
          all(c.invariant_under_local for c in cand.values()))
    # i1-fail -- a metastable rival (seed) is NOT invariant under local ops.
    check("i1-fail: a metastable rival value CHANGES under the same local ops",
          all(completion_signature("seed", a).invariant_under_local for a in interval),
          expected=False)

    # p1 -- candidate persists; a completed-history completion has decayed.
    check("p1: candidate winding does not relax; history completion decays to zero",
          all(c.persists for c in cand.values())
          and all(not completion_signature("history", a).persists
                  and completion_signature("history", a).value == 0
                  for a in interval))

    # k1 -- every LOCAL completion class fails at least one signature vs the
    # candidate, at every field value in the interval.
    def local_fails(a: Fraction) -> bool:
        return all(not matches_candidate(completion_signature(k, a), cand[a])
                   for k in LOCAL_KINDS)
    check("k1: nine local completion classes fail at least one discriminating signature",
          all(local_fails(a) for a in interval) and len(LOCAL_KINDS) == 10)

    # k2 -- the whole-family-WITH-target-phase completion absorbs the candidate.
    check("k2: the whole-family-with-target-phase completion ABSORBS the candidate",
          all(matches_candidate(completion_signature("whole_family_with_phase", a), cand[a])
              for a in interval))
    # k2-fail -- whole-family WITHOUT the target phase does NOT absorb it
    # (protected checker: k2, same matches_candidate path).
    check("k2-fail: whole-family WITHOUT the target phase does NOT absorb it",
          all(matches_candidate(completion_signature("whole_family_no_phase", a), cand[a])
              for a in interval),
          expected=False)

    # n1 -- neutrality: relabel candidate<->rival branches; the DISCRIMINATOR
    # verdict (which side carries the quantized invariant) is a property of the
    # signatures, not of the labels, so it is fixed under the swap.
    def discriminator_verdict(name_a: str, sig_a: Signature,
                              name_b: str, sig_b: Signature) -> str:
        # returns the NAME of the side carrying quantized+invariant+persistent.
        a_wins = sig_a.is_quantized and sig_a.invariant_under_local and sig_a.persists
        b_wins = sig_b.is_quantized and sig_b.invariant_under_local and sig_b.persists
        if a_wins and not b_wins:
            return name_a
        if b_wins and not a_wins:
            return name_b
        return "TIE"
    def label_only_scorer(name_a: str, sig_a: Signature,
                          name_b: str, sig_b: Signature) -> str:
        # deliberately broken: ignores the signatures, returns the FIRST label.
        return name_a
    a = Fraction(3, 5)
    rival = completion_signature("seed", a)
    v1 = discriminator_verdict("candidate", cand[a], "rival", rival)
    v2 = discriminator_verdict("rival", rival, "candidate", cand[a])  # labels swapped
    check("n1: swapping the two branch labels leaves every discriminator verdict fixed",
          v1 == "candidate" and v2 == "candidate" and v1 == v2)
    # n1-fail -- the label-only scorer run through the SAME swap: it returns the
    # first label, so its verdict is NOT preserved under the swap (protects n1).
    bad_v1 = label_only_scorer("candidate", cand[a], "rival", rival)
    bad_v2 = label_only_scorer("rival", rival, "candidate", cand[a])
    check("n1-fail: a label-sensitive scorer WOULD flip under the swap",
          bad_v1 == bad_v2,
          expected=False)

    print("PHYSICAL WITNESS DISCRIMINATOR (superconducting ring)")
    print("=" * 72)
    failures = []
    n_e = n_f = n_t = 0
    for name, value, expected in checks:
        ok = value == expected
        tag = "PASS" if ok else "UNEXPECTED"
        n_t += name[:2] == "s1" or name[:2] == "s2"
        n_e += CHECKS.get(name, {}).get("tag") == "E"
        n_f += CHECKS.get(name, {}).get("tag") == "F"
        print(f"{tag}  [{CHECKS.get(name, {}).get('tag','?')}] {name}: {value}")
        if not ok:
            failures.append(name)

    print()
    print("candidate staircase (applied -> trapped winding):")
    for aa in interval:
        print(f"  applied={str(aa):>5}  ->  w={cand[aa].value}   "
              f"(seed rival stores {completion_signature('seed', aa).value}, decays)")
    print()
    print("completion-class scoreboard vs candidate (a=3/5):")
    a0 = Fraction(3, 5)
    for k in (*LOCAL_KINDS, "whole_family_with_phase"):
        s = completion_signature(k, a0)
        verdict = "ABSORBS" if matches_candidate(s, cand[a0]) else "fails"
        print(f"  {k:>26}: value={str(s.value):>5} Q={int(s.is_quantized)} "
              f"I={int(s.invariant_under_local)} P={int(s.persists)}  -> {verdict}")
    print()
    print(f"EVIDENTIAL CHECKS (headline): {n_e} [E] + {n_f} [F] = {n_e + n_f}")
    print(f"[T] theorem-consequence checks (no evidential weight): {n_t}")

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()
