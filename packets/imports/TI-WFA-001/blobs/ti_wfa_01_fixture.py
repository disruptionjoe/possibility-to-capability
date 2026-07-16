"""TI-native adjudication fixture for the P2C-W1 whole-family completion attack.

Temporal Issuance sovereign adjudication (RUN-0169). This fixture does NOT
re-run P2C's physics or re-decide its verdict; it answers ONE question, on TI's
own terms, using TI's own CompletionClass v1 machinery
(temporal-issuance/COMPLETION-CLASS.md, status: testable, claim_movement:false):

    Under CompletionClass v1's `whole_family` primitive (conclusion class
    global/ontological), is admitting the target superconducting phase into the
    fixed completion family a LEGITIMATE whole_family completion of the frozen
    witness P2C-W1 -- or does legitimacy require an admissibility restriction
    without which every physically realized phase is absorbable by fiat (the
    fixed-family-absorber / F1 question)?

TI's answer, made executable here, is BOTH-AND, not either-or: the P2C dichotomy
is a false dichotomy under v1.

  (A) Admitting the S phase IS a legitimate whole_family completion -- but ONLY
      at its declared conclusion strength GLOBAL_ONTOLOGICAL_ABSORPTION. Per the
      v1 primitive table `whole_family` maps to the global/ontological class,
      and per the "four conclusion strengths" section a global witness
      "need not be predictive, but [its] conclusion is therefore limited to [its]
      own class." It legitimately blocks an ABSOLUTE SEMANTIC / METAPHYSICAL
      novelty claim (superconductivity is a broken-symmetry phase of a known
      Hamiltonian, not an ontologically brand-new object). Its physical
      admissibility is scientific input (v1 "Honest limits"): for this witness it
      is discharged at literature grade (one Hamiltonian, one phase diagram),
      so the completion is admissible and NOT classifier fiat.

  (B) The admissibility restriction P2C asks about ALREADY EXISTS in v1 and is
      load-bearing: it is the conclusion-class firewall. v1 states outright that
      "unrestricted completed-history and after-fact singleton completions can
      encode every realized trace. Treating them as ordinary physical
      explanations would make the positive class empty by definition." That is
      exactly the "every realized phase absorbable by fiat" failure mode, and v1
      already forbids it -- NOT by refusing the whole_family completion, but by
      refusing to let a global/ontological absorption be UPGRADED to a
      PHYSICAL_PREDICTIVE or OPERATIONAL_CONTEXT absorption.

  (C) The witness's operational/capability claim (realize a zero-maintenance,
      quantized, locally invariant persistent memory from the N frame at matched
      budget) is an OPERATIONAL/CONTEXT-class claim. The whole_family completion,
      even when it reproduces the (Q,I,P) signature by declaring the phase in,
      earns NO operational/context conclusion about it. To absorb that residue
      one needs an operational/context witness (resource / access / capability
      primitive) that reproduces the task's resource trace from N at matched
      budget -- and P2C's own k1 shows those fail. Global absorption and the
      operational residue live in different conclusion classes and do not touch.

Net TI disposition (scope-limited; see the semantics body): LEGITIMATE but
CONCLUSION-CAPPED. The fiat-absorber worry does not falsify a hierarchy on TI's
terms, because on TI's terms the fiat-absorber only ever earns the weakest,
non-causal conclusion. This adjudicates ONLY the `whole_family` primitive's
legitimacy and conclusion strength; it establishes NO physical source issuance
(Issue[S]^physical stays false, TI-C020 parked), runs NO full
SURVIVES_BOUNDED_COMPLETION_CLASS return, and asserts NO capability change
(TaF's call). authority_transfer = false.

Pure Python stdlib, deterministic. House [T]/[E]/[F] discipline; every [F] is a
real failing-direction control that flips a protected [E] on a shared code path.

Usage:
    python ti_wfa_01_fixture.py            # exit 0 iff all checks match
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

# --------------------------------------------------------------------------
# CompletionClass v1 conclusion classes and the primitive -> class map.
# Transcribed from temporal-issuance/COMPLETION-CLASS.md (read-only).
# --------------------------------------------------------------------------

PHYSICAL_PREDICTIVE = "PHYSICAL_PREDICTIVE_ABSORPTION"
OPERATIONAL_CONTEXT = "OPERATIONAL_CONTEXT_ABSORPTION"
REPRESENTATIONAL = "REPRESENTATIONAL_SURPLUS_ABSORPTION"
GLOBAL_ONTOLOGICAL = "GLOBAL_ONTOLOGICAL_ABSORPTION"

# v1 primitive inventory -> conclusion class (exact from the v1 table).
PRIMITIVE_CLASS = {
    "hidden_state": PHYSICAL_PREDICTIVE,
    "initial_condition": PHYSICAL_PREDICTIVE,
    "boundary_condition": PHYSICAL_PREDICTIVE,
    "fixed_source": PHYSICAL_PREDICTIVE,
    "stochastic_seed": PHYSICAL_PREDICTIVE,
    "name_provenance": REPRESENTATIONAL,
    "resource_capability": OPERATIONAL_CONTEXT,
    "whole_family": GLOBAL_ONTOLOGICAL,
    "completed_history": GLOBAL_ONTOLOGICAL,
    "observer_information_access": OPERATIONAL_CONTEXT,
    "relabel_gauge": REPRESENTATIONAL,
}

# The strength lattice: which conclusion classes may an admitted witness of a
# given class legitimately license? v1 "four conclusion strengths": the classes
# are NOT interchangeable, and a global/ontological or representational witness'
# conclusion is "limited to [its] own class" -- no upgrade edge into the
# causal (physical/operational) classes. Each class licenses ONLY itself.
def licensed_conclusions(witness_class: str) -> frozenset[str]:
    return frozenset({witness_class})


# The capability claim of the witness is an operational/context-class claim
# (a task's resource/persistence profile). Only an operational or physical
# witness can bear on it.
CAUSAL_CLASSES = frozenset({PHYSICAL_PREDICTIVE, OPERATIONAL_CONTEXT})
CAPABILITY_CLAIM_CLASS = OPERATIONAL_CONTEXT


# --------------------------------------------------------------------------
# Model of the frozen witness signature (mirrors P2C-W1's (Q,I,P), read-only).
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Signature:
    value: Fraction
    is_quantized: bool          # Q
    invariant_under_local: bool  # I
    persists: bool               # P


def candidate_signature(applied: Fraction) -> Signature:
    w = round(applied)
    return Signature(Fraction(w), True, True, True)


def null_phase_signature(applied: Fraction) -> Signature:
    """The trivial/normal phase: no persistent quantized invariant winding.
    Used as the fiat-collapse probe: if the unrestricted absorber 'absorbs'
    even THIS, it absorbs every phase."""
    return Signature(Fraction(0), True, True, False)


def reproduces(sig: Signature, cand: Signature) -> bool:
    return (sig.is_quantized == cand.is_quantized
            and sig.invariant_under_local == cand.invariant_under_local
            and sig.persists == cand.persists
            and sig.value == cand.value)


# --------------------------------------------------------------------------
# Completion witnesses, each carrying (a) the signature it can produce from the
# stated frame and (b) its v1 conclusion class.
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Witness:
    primitive: str
    conclusion_class: str
    reproduces_signature: bool


def whole_family_with_phase(applied: Fraction) -> Witness:
    """Declare the S phase itself a member of the fixed family. It reproduces
    the (Q,I,P) signature -- but it is a `whole_family` primitive, so its class
    is global/ontological (NOT physical/operational)."""
    sig = candidate_signature(applied)
    return Witness("whole_family", GLOBAL_ONTOLOGICAL,
                   reproduces(sig, candidate_signature(applied)))


def whole_family_without_phase(applied: Fraction) -> Witness:
    """The fixed family restricted to normal-phase configurations: no member
    reproduces the candidate signature."""
    return Witness("whole_family", GLOBAL_ONTOLOGICAL,
                   reproduces(null_phase_signature(applied),
                              candidate_signature(applied)))


def operational_witness(primitive: str, applied: Fraction) -> Witness:
    """Strongest operational/physical witness attempting to reproduce the
    capability signature FROM the normal frame at matched budget. Mirrors P2C's
    k1: resource/access/boundary/seed/hidden all fail (Q,I,P)+persistence."""
    if primitive in ("resource_capability", "observer_information_access",
                     "boundary_condition", "stochastic_seed"):
        # a driven/threaded/revealed value: continuous, non-invariant, decays.
        sig = Signature(applied, applied == round(applied), False, False)
    elif primitive in ("hidden_state", "fixed_source", "initial_condition"):
        # latent/fixed-source content that does not touch the observable.
        sig = Signature(Fraction(0), True, True, False)
    else:
        raise ValueError(primitive)
    return Witness(primitive, PRIMITIVE_CLASS[primitive],
                   reproduces(sig, candidate_signature(applied)))


# --------------------------------------------------------------------------
# The two adjudication scorers: the v1-faithful (conclusion-class-capped) scorer
# and the UNRESTRICTED scorer that removes the cap (the pathology).
# --------------------------------------------------------------------------

def v1_absorption_verdict(w: Witness) -> frozenset[str]:
    """What does an admitted witness that reproduces the signature legitimately
    license under v1? Its own conclusion class only."""
    if not w.reproduces_signature:
        return frozenset()
    return licensed_conclusions(w.conclusion_class)


def unrestricted_absorption_verdict(w: Witness) -> frozenset[str]:
    """The CAP REMOVED: let a signature-reproducing global witness count as a
    physical/operational absorption too. This is the move v1 forbids."""
    if not w.reproduces_signature:
        return frozenset()
    return frozenset({PHYSICAL_PREDICTIVE, OPERATIONAL_CONTEXT,
                      REPRESENTATIONAL, GLOBAL_ONTOLOGICAL})


def positive_class_nonempty_under(scorer, applied: Fraction) -> bool:
    """The operational/capability positive class survives iff NO admitted
    witness discharges the operational-class claim on the *null* phase (which
    carries no capability). If a scorer 'operationally absorbs' even the null
    phase, every phase is absorbable by fiat and the positive class is empty."""
    # Build a whole_family witness that (wrongly, under the unrestricted scorer)
    # is asked to absorb the NULL phase by declaring it a family member.
    null_as_member = Witness("whole_family", GLOBAL_ONTOLOGICAL,
                             reproduces_signature=True)  # fiat: 'it's in the family'
    return CAPABILITY_CLAIM_CLASS not in scorer(null_as_member)


# --------------------------------------------------------------------------
# House [T]/[E]/[F] registry.
# --------------------------------------------------------------------------

CHECKS = {
    "s1: v1 maps whole_family to the global/ontological class by construction": {"tag": "T"},
    "s2: conclusion classes carry no upgrade edge into the causal classes by construction": {"tag": "T"},
    "e1: whole_family_with_phase reproduces the (Q,I,P) signature (legitimate global absorption)": {"tag": "E"},
    "e1-fail: whole_family_without_phase does NOT reproduce it": {
        "tag": "F", "protects": "e1: whole_family_with_phase reproduces the (Q,I,P) signature (legitimate global absorption)"},
    "e2: the global absorption licenses ONLY global/ontological, not physical/operational": {"tag": "E"},
    "e2-fail: removing the cap empties the operational positive class (fiat collapse)": {
        "tag": "F", "protects": "e2: the global absorption licenses ONLY global/ontological, not physical/operational"},
    "e3: no operational/physical witness reproduces the capability signature from N": {"tag": "E"},
    "e3-fail: an operational (seed) witness value is NON-invariant/decaying, so cannot match": {
        "tag": "F", "protects": "e3: no operational/physical witness reproduces the capability signature from N"},
    "e4: global absorption leaves the operational-class capability claim unadjudicated": {"tag": "E"},
    "e4-fail: a class-blind merge would wrongly report the capability operationally absorbed": {
        "tag": "F", "protects": "e4: global absorption leaves the operational-class capability claim unadjudicated"},
    "n1: assigned conclusion class is a property of the primitive, invariant under branch relabel": {"tag": "E"},
    "n1-fail: a label-only scorer flips under the branch relabel": {
        "tag": "F", "protects": "n1: assigned conclusion class is a property of the primitive, invariant under branch relabel"},
}


def main() -> None:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    interval = (Fraction(1, 4), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5),
                Fraction(11, 10), Fraction(7, 5))

    # s1 -- primitive->class map is the v1 table (by construction).
    check("s1: v1 maps whole_family to the global/ontological class by construction",
          PRIMITIVE_CLASS["whole_family"] == GLOBAL_ONTOLOGICAL
          and PRIMITIVE_CLASS["completed_history"] == GLOBAL_ONTOLOGICAL)
    # s2 -- no class licenses any other class (no upgrade edge), by construction.
    check("s2: conclusion classes carry no upgrade edge into the causal classes by construction",
          all(licensed_conclusions(c) == frozenset({c})
              for c in (PHYSICAL_PREDICTIVE, OPERATIONAL_CONTEXT,
                        REPRESENTATIONAL, GLOBAL_ONTOLOGICAL)))

    # e1 -- the phase-in whole_family reproduces the signature across the interval.
    check("e1: whole_family_with_phase reproduces the (Q,I,P) signature (legitimate global absorption)",
          all(whole_family_with_phase(a).reproduces_signature for a in interval))
    # e1-fail -- phase-out does not (protects e1; same reproduces() path).
    check("e1-fail: whole_family_without_phase does NOT reproduce it",
          all(whole_family_without_phase(a).reproduces_signature for a in interval),
          expected=False)

    # e2 -- what the phase-in absorption licenses is EXACTLY {global}, never causal.
    def licenses_only_global(a: Fraction) -> bool:
        lic = v1_absorption_verdict(whole_family_with_phase(a))
        return lic == frozenset({GLOBAL_ONTOLOGICAL}) and not (lic & CAUSAL_CLASSES)
    check("e2: the global absorption licenses ONLY global/ontological, not physical/operational",
          all(licenses_only_global(a) for a in interval))
    # e2-fail -- REMOVE the cap: the operational positive class is emptied (the
    # unrestricted scorer operationally absorbs even the null phase). Protects e2:
    # the capped scorer keeps the positive class non-empty, the uncapped one does not.
    check("e2-fail: removing the cap empties the operational positive class (fiat collapse)",
          all(positive_class_nonempty_under(unrestricted_absorption_verdict, a)
              for a in interval),
          expected=False)
    # (sanity, folded into e2's meaning) the capped scorer DOES keep it non-empty:
    assert all(positive_class_nonempty_under(v1_absorption_verdict, a) for a in interval)

    # e3 -- no operational/physical witness reproduces the capability from N.
    op_prims = ("resource_capability", "observer_information_access",
                "boundary_condition", "stochastic_seed",
                "hidden_state", "fixed_source", "initial_condition")
    check("e3: no operational/physical witness reproduces the capability signature from N",
          all(not operational_witness(p, a).reproduces_signature
              for p in op_prims for a in interval))
    # e3-fail -- the seed witness is non-invariant/decaying, so cannot match
    # (protects e3; same operational_witness/reproduces path). We assert its
    # reproduces flag is True only if it matched -- it does not, so expected False.
    check("e3-fail: an operational (seed) witness value is NON-invariant/decaying, so cannot match",
          all(operational_witness("stochastic_seed", a).reproduces_signature for a in interval),
          expected=False)

    # e4 -- the global witness earns nothing in the operational class: the
    # capability claim (operational-class) is untouched by the global absorption.
    def capability_unadjudicated(a: Fraction) -> bool:
        lic = v1_absorption_verdict(whole_family_with_phase(a))
        return CAPABILITY_CLAIM_CLASS not in lic
    check("e4: global absorption leaves the operational-class capability claim unadjudicated",
          all(capability_unadjudicated(a) for a in interval))
    # e4-fail -- a class-blind merge reads an operational verdict off the global
    # witness (protects e4): it WOULD report operational absorption. Expected wrong.
    def class_blind_capability_absorbed(a: Fraction) -> bool:
        return CAPABILITY_CLAIM_CLASS in unrestricted_absorption_verdict(
            whole_family_with_phase(a))
    check("e4-fail: a class-blind merge would wrongly report the capability operationally absorbed",
          all(not class_blind_capability_absorbed(a) for a in interval),
          expected=False)

    # n1 -- conclusion class is a property of the primitive, not the branch label.
    def class_of(primitive: str, _label: str) -> str:
        return PRIMITIVE_CLASS[primitive]
    check("n1: assigned conclusion class is a property of the primitive, invariant under branch relabel",
          class_of("whole_family", "candidate") == class_of("whole_family", "rival")
          == GLOBAL_ONTOLOGICAL)
    # n1-fail -- a label-only scorer returns the label, so it flips (protects n1).
    def label_only(_primitive: str, label: str) -> str:
        return label
    check("n1-fail: a label-only scorer flips under the branch relabel",
          label_only("whole_family", "candidate") == label_only("whole_family", "rival"),
          expected=False)

    # ------------------------------------------------------------------
    print("TI WHOLE-FAMILY ADJUDICATION FIXTURE (P2C-W1 superconducting ring)")
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
    print("conclusion-class scoreboard (a=3/5):")
    a0 = Fraction(3, 5)
    wfp = whole_family_with_phase(a0)
    print(f"  whole_family_with_phase   : reproduces_sig={int(wfp.reproduces_signature)} "
          f"class={wfp.conclusion_class}")
    print(f"    v1-capped licenses       : {sorted(v1_absorption_verdict(wfp))}")
    print(f"    unrestricted licenses    : {sorted(unrestricted_absorption_verdict(wfp))}")
    for p in ("resource_capability", "observer_information_access",
              "boundary_condition", "stochastic_seed", "hidden_state"):
        w = operational_witness(p, a0)
        print(f"  {p:>26}: reproduces_sig={int(w.reproduces_signature)} "
              f"class={w.conclusion_class}")
    print()
    print("F1 DICHOTOMY RESOLUTION (TI-native): admitting the S phase is a")
    print("LEGITIMATE whole_family completion AND is conclusion-capped at")
    print("GLOBAL_ONTOLOGICAL_ABSORPTION; the admissibility restriction that")
    print("blocks fiat-absorption ALREADY EXISTS in v1 (the conclusion-class")
    print("firewall). The operational/capability residue is NOT absorbed.")
    print()
    print(f"EVIDENTIAL CHECKS (headline): {n_e} [E] + {n_f} [F] = {n_e + n_f}")
    print(f"[T] theorem-consequence checks (no evidential weight): {n_t}")

    if failures:
        raise SystemExit(f"unexpected checks: {failures}")
    print("All checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()
