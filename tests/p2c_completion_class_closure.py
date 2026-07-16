"""CompletionClass-P2C v0.1: composition closure and the derived conclusion-class firewall.

Portfolio item P2C-NULL-COMPLETION-CLOSURE (rank 1). Exploration tier. No
source-repo claim, GU/TI/TaF verdict, physical issuance claim, or canon moves
here. This fixture is a finite, exact model of P2C's OWN legitimate-completion
class -- built to give the frozen witness P2C-W1's strongest rival its
strongest hearing -- and of two questions the cross-repo adjudication left
open:

  (1) FIREWALL DERIVABILITY (condition C2 / falsifier F1 live remainder (a)):
      is TI's conclusion-class firewall (whole-family absorption caps below
      operational strength) DERIVABLE in a P2C-owned class from admissibility
      requirements the class needs anyway -- or only stipulable?
  (2) COMPOSITION GAP (referee D2): the witness survived every completion
      class taken SINGLY; does some COMPOSITE of local completions absorb the
      (Q,I,P) operational delta where no single one does?

THE CLASS (CompletionClass-P2C v0.1; definition doc in
explorations/2026-07-16-completion-class-firewall/COMPLETION-CLASS-P2C.md):

  Channel-type constructors (act on N-frame state at matched budget):
    seed, boundary, resource, access, hidden_state, history, provenance,
    relabeling, gauge  -- nine local kinds, matching the frozen witness's
    local sweep (`k1`).
  Containment-type constructors (claims of family membership; stateless):
    whole_family with an outcome-independent certification datum (certified
    family = N-reachable signatures + the literature-certified target phase),
    and the after-fact hull (family declared around the realized signature).

  Admissibility axioms -- each with PRE-EXISTING P2C provenance, none invented
  for this swing:
    A-FRAME  frame/budget preservation. Witness frame_declaration (frozen,
             4c9c28b) + adapter RESOURCE_FRAME_CHANGED typing (850521c).
    A-UNIF   outcome-independent, uniform strength assignment; no
             verdict-carrying input. Adapter circularity control (850521c).
    A-CAL    the verdict map must not be constant in either direction. This
             is the item's own pre-declared kill condition (portfolio: class
             "trivially narrow" = constant-reject, or "unrestricted enough to
             make every witness impossible by definition" = constant-absorb).

MODEL. N-frame state has exactly two value-bearing carriers at matched
budget: a PHYSICAL circulating channel (decays under free evolution; readout
changes under local perturbation) and a LATENT register channel (persists as
bookkeeping; readout changes under latent perturbation, which is a member of
the frozen witness's local-op group -- see the frozen discriminator's I
signature: "gauge shift, relabeling, hidden latent state"). Carrier
exhaustiveness at this granularity is a literature-grade modeling commitment,
the SAME grade as the frozen `k1`: a normal conductor has no locally
invariant, applied-flux-tracking, zero-maintenance channel. hidden_state is
given its STRONGEST admissible form (it may store any outcome-independent
function of the applied flux, including round(a) -- the steelman), because
anything stronger (storing the realized outcome) violates A-UNIF.

Pure Python stdlib. Usage:
    python p2c_completion_class_closure.py
    python tef_check_tag_linter.py --strict p2c_completion_class_closure.py
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
from itertools import product

# --------------------------------------------------------------------------
# House [T]/[E]/[F] registry (linter registry mode; R1-R4 enforced).
# --------------------------------------------------------------------------

CHECKS = {
    # setup (theorem-consequences; carry NO evidential weight)
    "t1: containment completions are stateless, so mixed composites prune to their channel part": {"tag": "T"},
    "t2: relabeling and gauge are equivalence-only by construction": {"tag": "T"},
    # frozen-witness agreement
    "w1: every single local kind fails the witness; only the certified family contains it": {"tag": "E"},
    # composition closure (referee D2)
    "c1: no sequential composite of local completions absorbs the witness staircase": {"tag": "E"},
    "c1-fail: composites still fail with the local-invariance signature dropped": {
        "tag": "F", "protects": "c1: no sequential composite of local completions absorbs the witness staircase"},
    "c2: carrier dichotomy -- every locally-invariant composite carries only the null readout": {"tag": "E"},
    "c3: composition strictly exceeds singles -- the register target needs depth 2": {"tag": "E"},
    "c4: composition closure reaches a fixpoint by depth 3 (depth 4 adds no new profile)": {"tag": "E"},
    # kill-condition controls, both directions
    "p1: ordinary-novelty controls are absorbed (eddy, register, relaxed)": {"tag": "E"},
    "p2: the alien staircase stays an unabsorbed residual (class is not unrestricted)": {"tag": "E"},
    # the firewall derivation
    "f1: the after-fact hull is total while the certified family excludes the alien target": {"tag": "E"},
    "f2: the capped scorer keeps the operational verdict map non-constant (A-CAL holds)": {"tag": "E"},
    "f2-fail: the uncapped mutant keeps the operational verdict map non-constant": {
        "tag": "F", "protects": "f2: the capped scorer keeps the operational verdict map non-constant (A-CAL holds)"},
    "f3: the certified whole-family earns containment on the witness, never operational strength": {"tag": "E"},
    "f3-fail: the capability-positive class stays non-empty under the unbudgeted-servo mutant": {
        "tag": "F", "protects": "f3: the certified whole-family earns containment on the witness, never operational strength"},
    "f4: outcome-independent certification keeps the containment verdict map non-constant (A-UNIF holds)": {"tag": "E"},
    "f4-fail: admitting after-fact hulls keeps the containment verdict map non-constant": {
        "tag": "F", "protects": "f4: outcome-independent certification keeps the containment verdict map non-constant (A-UNIF holds)"},
}


# --------------------------------------------------------------------------
# Model: N-frame state at matched budget, channel completions, composites.
# --------------------------------------------------------------------------

# Same applied-flux interval as the frozen discriminator (fractional values
# where the staircase is a nontrivial claim).
INTERVAL = (Fraction(1, 4), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5),
            Fraction(11, 10), Fraction(7, 5))

CHANNEL_KINDS = ("hidden_state", "boundary", "seed", "provenance", "resource",
                 "history", "access", "relabeling", "gauge")
CONTAINMENT_KINDS = ("whole_family_certified", "whole_family_hull")


@dataclass(frozen=True)
class NState:
    """N-frame state at matched budget: the two value-bearing carriers."""
    phys: Fraction | None    # physical circulating value (decays; perturbable)
    latent: Fraction | None  # latent register (persists; perturbable, and its
                             # perturbation is IN the witness's local-op group)
    revealed: bool           # PROBE_READ aperture opened onto the latent register


EMPTY = NState(phys=None, latent=None, revealed=False)


def apply_kind(kind: str, s: NState, a: Fraction) -> NState:
    """One completion step, strongest admissible form, at matched budget."""
    if kind in ("seed", "boundary", "resource"):
        # thread / boundary-mediate / transiently drive the applied value into
        # the physical channel; at matched budget none of the three can
        # maintain it (A-FRAME), so all share the physical carrier's fate.
        return replace(s, phys=a)
    if kind == "hidden_state":
        # STRONGEST admissible form: store any outcome-independent function of
        # the applied flux -- here round(a), the steelman for the staircase.
        return replace(s, latent=Fraction(round(a)))
    if kind == "access":
        return replace(s, revealed=True)
    if kind == "history":
        # completed relaxation: the physical channel has already decayed.
        return replace(s, phys=None)
    if kind == "provenance":
        return s  # a name/label; no channel effect.
    if kind in ("relabeling", "gauge"):
        return s  # equivalence-only; may re-present, never create.
    if kind in CONTAINMENT_KINDS:
        return s  # containment claims are stateless (t1).
    raise ValueError(f"unknown completion kind: {kind}")


def run_composite(seq: tuple[str, ...], a: Fraction) -> NState:
    s = EMPTY
    for kind in seq:
        s = apply_kind(kind, s, a)
    return s


def readout(s: NState) -> Fraction:
    """The circulating-memory readout the task names. The physical channel is
    directly observable; the latent register only through an opened aperture."""
    if s.phys is not None:
        return s.phys
    if s.revealed and s.latent is not None:
        return s.latent
    return Fraction(0)


def invariant_under_local(s: NState) -> bool:
    """The frozen witness's I signature: readout unchanged under the local-op
    group (gauge shift, relabeling, hidden latent-state change, local physical
    perturbation). Gauge/relabel are value-preserving by construction (t2)."""
    r0 = readout(s)
    if s.phys is not None and readout(replace(s, phys=s.phys + Fraction(1, 7))) != r0:
        return False
    if s.latent is not None and readout(replace(s, latent=s.latent + Fraction(1, 7))) != r0:
        return False
    return True


def evolve(s: NState) -> NState:
    """Free evolution at matched budget: every N-frame circulating value
    decays (L/R relaxation; a transient drive stops). The latent register is
    bookkeeping and persists."""
    return replace(s, phys=None)


def persists(s: NState) -> bool:
    return readout(evolve(s)) == readout(s)


# --------------------------------------------------------------------------
# Targets: per-a profiles (value, invariant, persists). Exact-trace matching,
# as in the frozen discriminator's matches_candidate.
# --------------------------------------------------------------------------

def witness_target(a: Fraction):
    """P2C-W1 operational delta: the (Q,I,P) staircase."""
    return (Fraction(round(a)), True, True)


def eddy_target(a: Fraction):
    """Ordinary novelty: a revealed continuous eddy (decays, perturbable)."""
    return (a, False, False)


def register_target(a: Fraction):
    """Ordinary novelty: a quantized persistent register memory that is NOT
    locally invariant (a snapshot record of the staircase)."""
    return (Fraction(round(a)), False, True)


def relaxed_target(a: Fraction):
    """Ordinary novelty: a fully relaxed trace."""
    return (Fraction(0), True, True)


def alien_target(a: Fraction):
    """Escape control: a third-quantum staircase no declared family contains
    (fractional quantization foreign to both phases)."""
    return (Fraction(round(3 * a), 3), True, True)


ZOO = {
    "witness": witness_target,
    "eddy": eddy_target,
    "register": register_target,
    "relaxed": relaxed_target,
    "alien": alien_target,
}


def profile(seq: tuple[str, ...]):
    """Fingerprint of a composite: its full trace over the interval."""
    out = []
    for a in INTERVAL:
        s = run_composite(seq, a)
        out.append((readout(s), invariant_under_local(s), persists(s)))
    return tuple(out)


def target_profile(target) -> tuple:
    return tuple(target(a) for a in INTERVAL)


def matches(seq: tuple[str, ...], target, require_invariance: bool = True) -> bool:
    for a in INTERVAL:
        s = run_composite(seq, a)
        value, inv, per = target(a)
        if readout(s) != value or persists(s) != per:
            return False
        if require_invariance and invariant_under_local(s) != inv:
            return False
    return True


def composites_up_to(depth: int) -> list[tuple[str, ...]]:
    seqs: list[tuple[str, ...]] = []
    for d in range(1, depth + 1):
        seqs.extend(product(CHANNEL_KINDS, repeat=d))
    return seqs


# --------------------------------------------------------------------------
# CompletionClass-P2C v0.1 scoring: strength classes and the two scorers.
# --------------------------------------------------------------------------

def op_absorbed(target, seqs) -> bool:
    """OPERATIONAL absorption: some admissible channel composite reproduces
    the full trace in the N frame at matched budget."""
    return any(matches(seq, target) for seq in seqs)


def channel_reachable_profiles(seqs) -> set:
    return {profile(seq) for seq in seqs}


# The certified family is declared STRUCTURALLY and outcome-independently:
# all N-reachable signatures plus the literature-certified S-phase signature
# (the quantized/invariant/persistent staircase, fixed by the phase's physics
# before any candidate is scored). No target is admitted by name or verdict.
S_PHASE_PROFILE = tuple((Fraction(round(a)), True, True) for a in INTERVAL)


def certified_contains(target, reachable: set) -> bool:
    """Certified whole-family containment: membership is profile membership in
    (N-reachable signatures) union (certified S-phase signature). A-UNIF
    admits this declaration because it is fixed by pre-event physics."""
    tp = target_profile(target)
    return tp == S_PHASE_PROFILE or tp in reachable


def hull_contains(name: str, target) -> bool:
    """After-fact hull: a family declared around whatever was realized.
    Total by construction; outcome-DEPENDENT, so A-UNIF caps it at
    representational strength in v0.1."""
    return True


# --------------------------------------------------------------------------
# Harness.
# --------------------------------------------------------------------------

def main() -> None:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    seqs3 = composites_up_to(3)
    reachable3 = channel_reachable_profiles(seqs3)

    # t1 -- containment completions are stateless: appending one changes no
    # composite state, so mixed composites prune to their channel part.
    check("t1: containment completions are stateless, so mixed composites prune to their channel part",
          all(run_composite(seq + (ck,), a) == run_composite(seq, a)
              for seq in composites_up_to(2)[:100]
              for ck in CONTAINMENT_KINDS for a in INTERVAL))

    # t2 -- relabeling/gauge equivalence-only: no channel effect.
    check("t2: relabeling and gauge are equivalence-only by construction",
          all(apply_kind(k, run_composite(seq, a), a) == run_composite(seq, a)
              for seq in composites_up_to(2)[:100]
              for k in ("relabeling", "gauge") for a in INTERVAL))

    # w1 -- frozen-witness agreement: every SINGLE local kind fails the
    # witness (frozen k1); the witness is NOT channel-reachable (mirror of
    # k2-fail: the family without the target phase does not contain it); the
    # certified family (with the phase) DOES contain it (mirror of k2 / TI e1).
    check("w1: every single local kind fails the witness; only the certified family contains it",
          all(not matches((k,), witness_target) for k in CHANNEL_KINDS)
          and target_profile(witness_target) not in reachable3
          and certified_contains(witness_target, reachable3))

    # c1 -- referee D2 target: NO sequential composite of local completions
    # (exhaustive to depth 3) reproduces the witness's (Q,I,P) staircase.
    check("c1: no sequential composite of local completions absorbs the witness staircase",
          all(not matches(seq, witness_target) for seq in seqs3))
    # c1-fail -- drop the local-invariance signature from the SAME matcher:
    # a composite absorber appears (hidden_state then access reaches the
    # quantized persistent staircase). The exhaustive search has teeth, and
    # the witness's escape hangs on exactly one signature: I.
    check("c1-fail: composites still fail with the local-invariance signature dropped",
          all(not matches(seq, witness_target, require_invariance=False) for seq in seqs3),
          expected=False)

    # c2 -- carrier dichotomy, the theorem-shaped escape: any composite whose
    # readout is locally invariant carries no value-bearing channel, so its
    # readout is the null value. Hence local-op invariance is unreachable
    # TOGETHER WITH applied-flux tracking, at any composition depth.
    invariant_states = [(seq, a) for seq in seqs3 for a in INTERVAL
                        if invariant_under_local(run_composite(seq, a))]
    check("c2: carrier dichotomy -- every locally-invariant composite carries only the null readout",
          len(invariant_states) > 0  # non-vacuity guard
          and all(readout(run_composite(seq, a)) == 0 for seq, a in invariant_states))

    # c3 -- the composition machinery is not vacuous: the register target
    # (quantized, persistent, NOT invariant) is absorbed at depth 2 and by no
    # single kind. Composition strictly enlarges absorption power.
    check("c3: composition strictly exceeds singles -- the register target needs depth 2",
          any(matches(seq, register_target) for seq in composites_up_to(2))
          and all(not matches((k,), register_target) for k in CHANNEL_KINDS))

    # c4 -- the closure is a genuine fixpoint: depth 4 produces no profile
    # depth 3 has not already produced, so c1/c2 extend to ALL finite
    # sequential composites, not only the enumerated bound.
    reachable4 = channel_reachable_profiles(composites_up_to(4))
    check("c4: composition closure reaches a fixpoint by depth 3 (depth 4 adds no new profile)",
          reachable4 == reachable3)

    # p1 -- kill-direction-1 control (class not trivially narrow): ordinary
    # novelty is absorbed, including a target only a composite reaches.
    check("p1: ordinary-novelty controls are absorbed (eddy, register, relaxed)",
          op_absorbed(eddy_target, seqs3)
          and op_absorbed(register_target, seqs3)
          and op_absorbed(relaxed_target, seqs3))

    # p2 -- kill-direction-2 control (class not unrestricted): an undeclared
    # third-quantum staircase is NOT absorbed and NOT certified-contained; it
    # remains a first-class unexplained residual rather than being swallowed.
    check("p2: the alien staircase stays an unabsorbed residual (class is not unrestricted)",
          not op_absorbed(alien_target, seqs3)
          and not certified_contains(alien_target, reachable3))

    # f1 -- the derivation's two constructor facts: the after-fact hull is
    # TOTAL (contains every zoo member, witness and alien included), while the
    # certified family has bite (excludes the alien target).
    check("f1: the after-fact hull is total while the certified family excludes the alien target",
          all(hull_contains(n, t) for n, t in ZOO.items())
          and not certified_contains(alien_target, reachable3))

    # f2 -- A-CAL under the v0.1-capped scorer: the operational verdict map
    # over the zoo separates (ordinary novelty absorbed; witness and alien
    # not). The capped class functions as a discriminating instrument.
    op_map = {n: op_absorbed(t, seqs3) for n, t in ZOO.items()}
    check("f2: the capped scorer keeps the operational verdict map non-constant (A-CAL holds)",
          len(set(op_map.values())) > 1
          and op_map["eddy"] and op_map["register"] and op_map["relaxed"]
          and not op_map["witness"] and not op_map["alien"])
    # f2-fail -- the UNCAPPED mutant (containment counts as operational, per
    # A-UNIF-blind totality of the hull): every zoo member is "absorbed"; the
    # verdict map goes constant; the instrument dies by the item's own
    # pre-declared kill condition. This is the derivation, exhibited.
    uncapped_map = {n: (op_absorbed(t, seqs3) or hull_contains(n, t)) for n, t in ZOO.items()}
    check("f2-fail: the uncapped mutant keeps the operational verdict map non-constant",
          len(set(uncapped_map.values())) > 1,
          expected=False)

    # f3 -- the firewall, derived: the certified whole-family CONTAINS the
    # witness (a real containment result, blocking absolute-novelty claims)
    # yet earns no operational absorption, because the only in-model
    # realizers of the staircase-with-invariance are outside the
    # A-FRAME-respecting channel menu (c1/c2). Containment strength and
    # operational strength provably separate.
    check("f3: the certified whole-family earns containment on the witness, never operational strength",
          certified_contains(witness_target, reachable3)
          and not op_absorbed(witness_target, seqs3))
    # f3-fail -- drop A-FRAME: an unbudgeted feedback servo (maintenance cost
    # unbounded, so inadmissible at matched budget) can pin any declared
    # invariant-persistent profile; the capability-positive class over the zoo
    # (invariant-persistent targets not absorbed) empties -- witness AND alien
    # both fall. A-FRAME is load-bearing for the firewall.
    def servo_absorbs(target) -> bool:
        return all(target(a)[1] and target(a)[2] for a in INTERVAL)
    positive_class_mutant = [n for n, t in ZOO.items()
                             if all(t(a)[1] and t(a)[2] for a in INTERVAL)
                             and not (op_absorbed(t, seqs3) or servo_absorbs(t))]
    check("f3-fail: the capability-positive class stays non-empty under the unbudgeted-servo mutant",
          len(positive_class_mutant) > 0,
          expected=False)

    # f4 -- A-UNIF's load: only outcome-independent family declarations earn
    # containment strength, so the containment verdict map still separates
    # (witness contained, alien not).
    cert_map = {n: certified_contains(t, reachable3) for n, t in ZOO.items()}
    check("f4: outcome-independent certification keeps the containment verdict map non-constant (A-UNIF holds)",
          len(set(cert_map.values())) > 1 and cert_map["witness"] and not cert_map["alien"])
    # f4-fail -- admit after-fact hulls as containment: the containment map
    # goes constant (everything "contained"), and the containment class loses
    # its content (blocking absolute novelty becomes vacuous).
    hull_map = {n: hull_contains(n, t) for n, t in ZOO.items()}
    check("f4-fail: admitting after-fact hulls keeps the containment verdict map non-constant",
          len(set(hull_map.values())) > 1,
          expected=False)

    # ---------------------------------------------------------------- report
    print("COMPLETIONCLASS-P2C v0.1: COMPOSITION CLOSURE AND DERIVED FIREWALL")
    print("=" * 72)
    failures = []
    n_e = n_f = n_t = 0
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
    print(f"channel composites enumerated (depth <= 3): {len(seqs3)}; "
          f"distinct profiles: {len(reachable3)} (fixpoint at depth 3)")
    print()
    print("composite frontier vs the witness's three signatures at a=3/5:")
    a0 = Fraction(3, 5)
    frontier = {}
    for seq in seqs3:
        s = run_composite(seq, a0)
        key = (readout(s) == round(a0), invariant_under_local(s), persists(s))
        frontier.setdefault(key, seq)
    for (q, i, p), seq in sorted(frontier.items(), reverse=True):
        print(f"  staircase={int(q)} I={int(i)} P={int(p)}  e.g. {' o '.join(seq)}")
    print()
    print("zoo verdicts under CompletionClass-P2C v0.1 (capped scorer):")
    for n, t in ZOO.items():
        op = op_absorbed(t, seqs3)
        cont = certified_contains(t, reachable3)
        if op:
            verdict = "OPERATIONAL_ABSORPTION"
        elif cont:
            verdict = "CONTAINMENT_ABSORPTION_ONLY (firewalled)"
        else:
            verdict = "UNABSORBED_RESIDUAL"
        print(f"  {n:>9}: {verdict}")
    print()
    print(f"EVIDENTIAL CHECKS (headline): {n_e} [E] + {n_f} [F] = {n_e + n_f}")
    print(f"[T] theorem-consequence checks (no evidential weight): {n_t}")

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()
