"""P2C RANK-4 fixture: diagnosis stability under a representation change --
ternary value alphabet with the Z/2 flip embedded as a transposition.

Exploration tier. No claim promotion. Nothing here reopens the withdrawn
ADAPTER2-01 identity or moves any source-repo claim. bar(b), H59, Krein
positivity, physical issuance: ALL OPEN.

RANK-4 QUESTION PROBED (ranked-decisive-test-program v0.1, Rank 4): does the
same frozen fork content receive the same DIAGNOSIS under a substantively
different representation? The bounded-fiber synthesis (link 6) proved, over
the BINARY alphabet V = {-1,+1}, the classification lemma
    {label-free} = {flip-even} EXACTLY at every arity,
and flagged its binary-alphabet dependence as escape door 1: "for larger
alphabets 'label-free' is strictly stronger than any single-involution
evenness." That caveat is exactly a Rank-4 representation-dependence RISK.

RE-ENCODING TESTED HERE: enlarge the alphabet to V3 = {-1, 0, +1} and embed
the same Z/2 flip as the TRANSPOSITION tau = (-1 <-> +1), fixing 0. This
keeps the frozen content (one Z/2 fork between two sign-labelled branches,
plus an inert third value) while changing the formalism (the flip is no
longer the full relabelling group of V). The three transpositions of V3 are
conjugate under relabelling, so tau is representative. A 3-CYCLE embedding is
deliberately OUT OF SCOPE: a 3-cycle is not an involution, so it changes the
datum's group from Z/2 to Z/3 -- different physical content, not an
equivalent representation of the SAME fork (noted as a nonclaim; the
"cyclic-orientation door" remains a door).

DIAGNOSIS WHOSE STABILITY IS TESTED: "no label-free patch predicate can
select the sign; sign selection requires a label-naming (flip-symmetry-
breaking) ingredient." Two separable parts:
  (i)  the LEMMA's biconditional (label-free <=> flip-even): predicted by
       door 1 to BREAK at |V| = 3 (flip-even but label-naming predicates
       should exist, e.g. "x0 == 0");
  (ii) the DIAGNOSIS-BEARING direction (label-free => flip-even, hence no
       flip-odd label-free predicate, hence no label-free sign selector):
       predicted to SURVIVE, because label-freeness (invariance under every
       uniform bijection of V) still contains invariance under tau.
A failure of (ii) would be a first-class REVISE_HIERARCHY signal, reported
as the result, not hidden. A failure of (i)-breaking (i.e. the biconditional
surviving) would falsify door 1's premise and also be reported.

DEFINITIONS (identical in form to gate1_t26_actual_patch_machinery.py):
  LABEL-FREE: f depends only on the EQUALITY PATTERN of its input tuple
  (the partition of sites induced by x_i == x_j); equivalently f is
  invariant under every bijection of V applied uniformly to all sites
  (pattern classes are exactly the Sym(V)-orbits at every alphabet size,
  since an injection between used-value sets extends to a bijection of V).
  FLIP-EVEN: f(tau(x)) == f(x) for all x.  FLIP-ODD: not flip-even.
  SIGN-SELECTOR: f separates some all-signed tuple x in {-1,+1}^k from
  tau(x) (the fork content lives on the signed subalphabet).

CHECK DISCIPLINE (house style): [T] theorem-consequence (no evidential
weight, never in a headline), [E] genuine experiment, [F] failing-direction
control through the SAME code path as the check it protects. Where an [E] is
algebra-forced by the accompanying hand proof, that is disclosed inline and
graded as machine-verification of the proof. Expectations are pre-declared
in EXPECT; exit 0 iff every check matches its declared expectation and every
[F] fires.
"""

from __future__ import annotations

import sys
from itertools import combinations, product

CHECKS = {
    "setup_tau_is_involutive_bijection_of_V3": {"tag": "T"},
    "setup_labelfree_implies_flipeven_k1_exhaustive": {"tag": "T"},
    "setup_binary_sublemma_reproduced_k2": {"tag": "T"},
    "e1_k1_no_flipodd_labelfree_predicate": {"tag": "E"},
    "e2_k1_flipeven_but_labelnaming_predicates_exist": {"tag": "E"},
    "e2b_k1_exemplar_x0_eq_zero_flipeven_and_labelnaming": {"tag": "E"},
    "e3_k2_no_flipodd_labelfree_predicate": {"tag": "E"},
    "e3b_k2_labelfree_strictly_inside_flipeven": {"tag": "E"},
    "e4_k2_patternclass_family_equals_bruteforce_labelfree": {"tag": "E"},
    "e4b_k3_all_32_labelfree_predicates_are_flipeven": {"tag": "E"},
    "e5_sign_selectors_are_flipodd_and_labelnaming": {"tag": "E"},
    "e6_pattern_class_splits_into_multiple_flip_orbits": {"tag": "E"},
    "f1_broken_flip_misclassifies_through_same_is_flip_even_path": {
        "tag": "F", "protects": "e3_k2_no_flipodd_labelfree_predicate"},
    "f2_broken_pattern_misclassifies_through_same_is_label_free_path": {
        "tag": "F",
        "protects": "e4_k2_patternclass_family_equals_bruteforce_labelfree"},
    "f3_nonselector_control_through_same_selects_sign_path": {
        "tag": "F", "protects": "e5_sign_selectors_are_flipodd_and_labelnaming"},
}

# Pre-declared expectations (True = check-condition holds; [F] checks assert
# the broken variant AGREES with truth, expected False = the control fires).
EXPECT = {name: (meta["tag"] != "F") for name, meta in CHECKS.items()}

V3 = (-1, 0, 1)
results: list = []
META: dict = {}


def check(name: str, value: bool) -> None:
    results.append((name, bool(value), EXPECT[name]))


def tau(x: tuple) -> tuple:
    """The transposition (-1 <-> +1), fixing 0 (== negation on {-1,0,+1})."""
    return tuple(-v for v in x)


def broken_flip(x: tuple) -> tuple:
    """BROKEN involution: transposes only coordinate 0."""
    return (-x[0],) + tuple(x[1:])


def pattern(x: tuple) -> tuple:
    """Equality pattern: which site pairs carry equal values."""
    return tuple(x[i] == x[j] for i, j in combinations(range(len(x)), 2))


def pattern_dropping_first_pair(x: tuple) -> tuple:
    """BROKEN pattern extractor: forgets the (0,1) equality bit."""
    return pattern(x)[1:]


def is_flip_even(fset: frozenset, inputs: tuple, flip=tau) -> bool:
    return all((x in fset) == (flip(x) in fset) for x in inputs)


def is_label_free(fset: frozenset, inputs: tuple, pat=pattern) -> bool:
    by_pat: dict = {}
    for x in inputs:
        by_pat.setdefault(pat(x), set()).add(x in fset)
    return all(len(v) == 1 for v in by_pat.values())


def classify_arity(k: int, alphabet=V3, flip=tau, pat=pattern):
    """Exhaustive census over all 2^(|alphabet|^k) k-site predicates."""
    inputs = tuple(product(alphabet, repeat=k))
    n_funcs = 2 ** len(inputs)
    flip_even = label_free = odd_and_free = even_and_naming = 0
    for mask in range(n_funcs):
        fset = frozenset(x for i, x in enumerate(inputs) if (mask >> i) & 1)
        fe = is_flip_even(fset, inputs, flip)
        lf = is_label_free(fset, inputs, pat)
        flip_even += fe
        label_free += lf
        odd_and_free += (not fe) and lf
        even_and_naming += fe and (not lf)
    return n_funcs, flip_even, label_free, odd_and_free, even_and_naming


def label_free_family(k: int, alphabet=V3):
    """ALL label-free k-site predicates, exhaustively, via pattern classes
    (label-free predicates are exactly the unions of pattern classes, by
    the declared definition)."""
    inputs = tuple(product(alphabet, repeat=k))
    classes: dict = {}
    for x in inputs:
        classes.setdefault(pattern(x), []).append(x)
    keys = sorted(classes)
    family = []
    for mask in range(2 ** len(keys)):
        fset = frozenset(
            x for i, kk in enumerate(keys) if (mask >> i) & 1
            for x in classes[kk])
        family.append(fset)
    return inputs, family, len(keys)


def selects_sign(fset: frozenset, k: int) -> bool:
    """Does f separate some all-signed tuple from its flip? (The fork
    content lives on the signed subalphabet {-1,+1}^k.)"""
    return any((x in fset) != (tau(x) in fset)
               for x in product((-1, 1), repeat=k))


def main() -> int:
    # ---- setup [T] checks (algebra-forced; no evidential weight) ----------
    check("setup_tau_is_involutive_bijection_of_V3",
          all(tau(tau((v,))) == (v,) for v in V3)
          and sorted(tau((v,))[0] for v in V3) == sorted(V3))

    inputs1 = tuple(product(V3, repeat=1))
    all_preds_k1 = []
    for mask in range(2 ** len(inputs1)):
        fset = frozenset(x for i, x in enumerate(inputs1) if (mask >> i) & 1)
        all_preds_k1.append(fset)
    # label-free => flip-even is forced: tau is one of the uniform bijections
    # quantified over in the label-free definition. Verified anyway ([T]).
    check("setup_labelfree_implies_flipeven_k1_exhaustive",
          all(is_flip_even(f, inputs1) for f in all_preds_k1
              if is_label_free(f, inputs1)))

    # binary sublemma (link 6, known result) reproduced inside this fixture
    # as a regression anchor; [T]: already established by the link-6 fixture.
    _, fe2b, lf2b, oaf2b, ean2b = classify_arity(2, alphabet=(-1, 1))
    META["binary_k2"] = {"flip_even": fe2b, "label_free": lf2b,
                         "odd_and_free": oaf2b, "even_and_naming": ean2b}
    check("setup_binary_sublemma_reproduced_k2",
          oaf2b == 0 and ean2b == 0 and fe2b == lf2b)

    # ---- k = 1 exhaustive census ([E]) ------------------------------------
    n1, fe1, lf1, oaf1, ean1 = classify_arity(1)
    META["ternary_k1"] = {"n_predicates": n1, "flip_even": fe1,
                          "label_free": lf1, "odd_and_free": oaf1,
                          "even_and_naming": ean1}
    # oaf1 == 0 is algebra-forced by the setup theorem (disclosed: this [E]
    # is machine-verification of the hand proof, not independent discovery).
    check("e1_k1_no_flipodd_labelfree_predicate", oaf1 == 0)
    # NOT forced by this fixture's construction: door 1 predicted the
    # biconditional breaks at |V| = 3. This is the diagnosis-CHANGE probe.
    check("e2_k1_flipeven_but_labelnaming_predicates_exist", ean1 > 0)

    x0_eq_zero = frozenset(x for x in inputs1 if x[0] == 0)
    check("e2b_k1_exemplar_x0_eq_zero_flipeven_and_labelnaming",
          is_flip_even(x0_eq_zero, inputs1)
          and not is_label_free(x0_eq_zero, inputs1))

    # ---- k = 2 exhaustive census ([E]) ------------------------------------
    inputs2 = tuple(product(V3, repeat=2))
    n2, fe2, lf2, oaf2, ean2 = classify_arity(2)
    META["ternary_k2"] = {"n_predicates": n2, "flip_even": fe2,
                          "label_free": lf2, "odd_and_free": oaf2,
                          "even_and_naming": ean2}
    check("e3_k2_no_flipodd_labelfree_predicate", oaf2 == 0)
    check("e3b_k2_labelfree_strictly_inside_flipeven",
          lf2 < fe2 and ean2 == fe2 - lf2 and ean2 > 0)

    # pattern-class family vs brute force at k = 2 (validates the k = 3
    # shortcut on a tier where brute force is feasible)
    _, fam2, n_classes2 = label_free_family(2)
    brute_lf2 = set()
    for mask in range(2 ** len(inputs2)):
        fset = frozenset(x for i, x in enumerate(inputs2) if (mask >> i) & 1)
        if is_label_free(fset, inputs2):
            brute_lf2.add(fset)
    check("e4_k2_patternclass_family_equals_bruteforce_labelfree",
          set(fam2) == brute_lf2 and len(fam2) == lf2)

    # ---- k = 3: ALL label-free predicates (exhaustive via classes) --------
    inputs3, fam3, n_classes3 = label_free_family(3)
    META["ternary_k3"] = {"n_pattern_classes": n_classes3,
                          "n_labelfree_predicates": len(fam3)}
    check("e4b_k3_all_32_labelfree_predicates_are_flipeven",
          n_classes3 == 5 and len(fam3) == 32
          and all(is_flip_even(f, inputs3) for f in fam3))

    # ---- diagnosis stability: sign selectors ([E]) -------------------------
    all_plus = frozenset({(1, 1)})
    x0_plus = frozenset(x for x in inputs2 if x[0] == 1)
    majority_sign = frozenset(x for x in inputs2 if sum(x) > 0)
    selectors = {"all_plus": all_plus, "x0_plus": x0_plus,
                 "majority_sign": majority_sign}
    META["selectors"] = {
        name: {"selects_sign": selects_sign(f, 2),
               "flip_even": is_flip_even(f, inputs2),
               "label_free": is_label_free(f, inputs2)}
        for name, f in selectors.items()}
    check("e5_sign_selectors_are_flipodd_and_labelnaming",
          all(selects_sign(f, 2)
              and not is_flip_even(f, inputs2)
              and not is_label_free(f, inputs2)
              for f in selectors.values()))

    # ---- mechanism: why the biconditional breaks ([E]) ----------------------
    # the "all sites equal" pattern class at k = 2 contains {(-1,-1),(0,0),
    # (1,1)}: over binary every pattern class is ONE flip orbit; here it
    # splits into >= 2 (this is the structural reason label-free became
    # strictly stronger than flip-even).
    eq_class = [x for x in inputs2 if pattern(x) == (True,)]
    orbits = set()
    for x in eq_class:
        orbits.add(frozenset({x, tau(x)}))
    META["eq_class_flip_orbits"] = sorted(
        sorted(o) for o in orbits)
    check("e6_pattern_class_splits_into_multiple_flip_orbits",
          len(orbits) >= 2)

    # ---- failing-direction controls [F] ------------------------------------
    eq01 = frozenset(x for x in inputs2 if x[0] == x[1])
    # f1: eq01 is truly flip-even; the broken involution (coordinate-0-only
    # transposition), through the SAME is_flip_even path, must MISclassify it.
    check("f1_broken_flip_misclassifies_through_same_is_flip_even_path",
          is_flip_even(eq01, inputs2, flip=broken_flip))
    # f2: eq01 is truly label-free; the broken pattern extractor, through the
    # SAME is_label_free path, must MISclassify it as label-naming.
    check("f2_broken_pattern_misclassifies_through_same_is_label_free_path",
          is_label_free(eq01, inputs2, pat=pattern_dropping_first_pair))
    # f3: the selector detector, on the label-free non-selector eq01 through
    # the SAME selects_sign path, must report NOT-a-selector (not vacuous).
    check("f3_nonselector_control_through_same_selects_sign_path",
          selects_sign(eq01, 2))

    # ---- report -------------------------------------------------------------
    print("RANK-4 TERNARY-ALPHABET REPRESENTATION PROBE")
    print("=" * 74)
    failures = []
    n_t = n_e = n_f = 0
    for name, value, expected in results:
        tag = CHECKS[name]["tag"]
        n_t += tag == "T"
        n_e += tag == "E"
        n_f += tag == "F"
        ok = value == expected
        print(f"{'PASS' if ok else 'UNEXPECTED'}  [{tag}] {name}: "
              f"{value} (expected {expected})")
        if not ok:
            failures.append(name)
    print("\nMETA (census numbers):")
    for key, val in META.items():
        print(f"  {key}: {val}")
    print(f"\nEVIDENTIAL CHECKS (headline): {n_e} [E] + {n_f} [F] "
          f"= {n_e + n_f}")
    print(f"[T] theorem-consequence checks (no evidential weight): {n_t}")
    if failures:
        print("\nUNEXPECTED RESULTS (first-class; report, never hide):",
              failures)
        print("A diagnosis change under this re-encoding is a REVISE_HIERARCHY")
        print("signal for the receiver program, not a fixture bug per se.")
        return 1
    print("\nRESULT: the binary biconditional {label-free} = {flip-even}")
    print("BREAKS at |V| = 3 (flip-even-but-label-naming predicates exist,")
    print("e.g. 'x0 == 0'), exactly as door 1 predicted -- the LEMMA is")
    print("representation-dependent. The DIAGNOSIS-BEARING direction")
    print("(label-free => flip-even; no flip-odd label-free predicate at")
    print("k = 1, 2 exhaustively and over ALL label-free predicates at")
    print("k = 3; every exhibited sign selector is label-naming) SURVIVES")
    print("the re-encoding. Diagnosis: STABLE under this transformation.")
    print("Scope: transposition-embedded flip only; 3-cycle (Z/3) actions,")
    print("physically motivated alphabets, and native-tier vocabularies")
    print("remain open doors. All checks match expectations. Exit 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
