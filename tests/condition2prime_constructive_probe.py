"""Condition 2' CONSTRUCTIVE probe (P2C swing-2 follow-up, adversarial-twin lane).

TASK (swing-2 lane 3, referee-corrected, condition 2'): DERIVE the
sector-asymmetric spectral condition from finality/issuance-native structure --
not merely exhibit dynamics that has it (that consumes the orbit bit).  A
successful derivation must be (i) SOURCE-SIDE in TI's RUN-0019 sense
(SourceRealization = (C, <=_S, Ext_S); kappa_i/G_ij/Omega_ij are readout),
(ii) COMPOSITION-COMPATIBLE on extension morphisms (E160 positive shape:
admissibility itself carries a functorial label; a supplied table is extra
data), and (iii) J-FLIP-ROBUST NON-DEFINITIONALLY (survives form -> -form,
J -> -J, labels swapped, for a reason not equivalent to
'physical = positive-norm').

THREE ATTEMPTS, each executed to its breaking point:
  A1  irreversibility-as-spectrum: represent the issuance semigroup so that
      forward extension is realizable on exactly one sector; ask whether the
      base arrow transports to the fiber.
  A2  record-count monotone as spectral functional: build the generator's
      spectrum from the growth functional Q (RUN-0028 shape); ask whether
      growth data can place bounded-below-ness on one sector.
  A3  fork-resolution asymmetry: at an SBP fork the realized branch is source
      data; ask whether it induces a global, composition-compatible sector
      selection or only relabels per history / per block.

CHECK LABELS (house style, swing-2 discipline):
  [T] theorem-consequence: outcome fixed by construction; short proof in the
      deliverable text; the code certifies instances.  Carries NO evidential
      weight for the headline; listed separately.
  [E] genuine instance test (outcome not fixed at formalization time; where an
      instance was chosen to have a property, the check is still tagged [E]
      per swing-2 precedent but the choice is disclosed inline).
  [F] failing-direction control: a deliberately broken variant FAILS,
      exercising the SAME checker code path it protects.

Krein toy conventions follow tests/krein_norm_link_probe.py (commit 96b96bc):
K = R^4, eta = J = diag(+,+,-,-), sectors K+/K-, swap S with S eta S = -eta;
the global flip acts in standard coordinates as A -> S A S.

Exit 0 iff every check matches its pre-declared expected value.  Pure numpy.
"""

from __future__ import annotations

import numpy as np

# ------------------------------------------------------------ Krein primitives

ETA4 = np.diag([1.0, 1.0, -1.0, -1.0])
J4 = ETA4.copy()
S4 = np.eye(4)[[2, 3, 0, 1]]            # e1<->e3, e2<->e4; S = S^T, S^2 = I
KP = np.diag([1.0, 1.0, 0.0, 0.0])
KM = np.diag([0.0, 0.0, 1.0, 1.0])


def expm(m: np.ndarray) -> np.ndarray:
    """Scaling-and-squaring Taylor exponential (small matrices only)."""
    m = np.asarray(m, dtype=complex)
    s = int(max(0, np.ceil(np.log2(max(1.0, np.linalg.norm(m, 2))))) + 4)
    a = m / (2.0 ** s)
    out = np.eye(m.shape[0], dtype=complex)
    term = np.eye(m.shape[0], dtype=complex)
    for k in range(1, 24):
        term = term @ a / k
        out = out + term
    for _ in range(s):
        out = out @ out
    return out


def flipK(a: np.ndarray) -> np.ndarray:
    """Global flip (form -> -form, J -> -J, labels swapped), std coordinates."""
    return S4 @ a @ S4


def sector_bounded(a: np.ndarray, proj: np.ndarray) -> bool:
    """sup_t ||e^{tA} x|| finite on the sector?  (t-grid; instances used are
    >= e^15 away from the 1e3 threshold -- disclosed numeric failure mode:
    growth rates < ~0.23 over t<=30 would be misclassified; none is used)."""
    basis = [proj[:, i] for i in range(4) if abs(proj[i, i]) > 0.5]
    sup = 0.0
    for t in np.linspace(0.0, 30.0, 61):
        e = expm(t * a)
        sup = max(sup, max(float(np.linalg.norm(e @ q)) for q in basis))
    return sup < 1e3


def c_stab(a: np.ndarray):
    """Sector on which the issuance semigroup is bounded, if exactly one."""
    bp, bm = sector_bounded(a, KP), sector_bounded(a, KM)
    if bp == bm:
        return None
    return KP if bp else KM


def restricted_spectrum(a: np.ndarray, proj: np.ndarray) -> np.ndarray:
    idx = [i for i in range(4) if abs(proj[i, i]) > 0.5]
    return np.linalg.eigvals(a[np.ix_(idx, idx)])


def c_energy(h: np.ndarray):
    """Sector on which the restricted spectrum is positive, if exactly one
    (finite-dim PROXY for 'bounded below on one sector only')."""
    pos_p = bool(np.all(restricted_spectrum(h, KP).real > 0))
    pos_m = bool(np.all(restricted_spectrum(h, KM).real > 0))
    if pos_p == pos_m:
        return None
    return KP if pos_p else KM


def c_circ(a: np.ndarray):
    """Circularity control: 'physical = positive-norm' -- returns whatever J
    calls positive, ignoring the dynamics."""
    return KP


def same_proj(p, q) -> bool:
    if p is None or q is None:
        return p is None and q is None
    return bool(np.allclose(p, q))


def j_dissipative(a: np.ndarray) -> bool:
    return float(np.max(np.linalg.eigvalsh((a + a.T) / 2))) <= 1e-10


def eta_contractive(a: np.ndarray) -> bool:
    m = ETA4 @ a + a.T @ ETA4
    return float(np.max(np.linalg.eigvalsh((m + m.T) / 2))) <= 1e-10


def eta_expansive(a: np.ndarray) -> bool:
    m = ETA4 @ a + a.T @ ETA4
    return float(np.min(np.linalg.eigvalsh((m + m.T) / 2))) >= -1e-10


# --------------------------------------------------- source layer (TI-native)

Literal = tuple[str, int]
State = frozenset


def consistent(state: State) -> bool:
    vals: dict[str, int] = {}
    for prop, sign in state:
        if sign not in (-1, 1):
            return False
        if prop in vals and vals[prop] != sign:
            return False
        vals[prop] = sign
    return True


def flip_state(s: State) -> State:
    return frozenset((p, -e) for p, e in s)


def flip_chain(ch: tuple) -> tuple:
    return tuple(flip_state(s) for s in ch)


def admissible_chain(ch: tuple) -> bool:
    """Issuance admissibility: records only accumulate; every state consistent."""
    return all(consistent(s) for s in ch) and \
        all(a.issubset(b) for a, b in zip(ch, ch[1:]))


def fingerprint(chains: tuple) -> tuple:
    """Label-free structural data: lengths, strict-growth pattern, pairwise
    endpoint compatibility."""
    lengths = tuple(len(ch[-1]) for ch in chains)
    strict = tuple(tuple(len(b) > len(a) for a, b in zip(ch, ch[1:]))
                   for ch in chains)
    compat = tuple(consistent(a[-1] | b[-1])
                   for i, a in enumerate(chains) for b in chains[i + 1:])
    return (lengths, strict, compat)


def signed_fingerprint(chains: tuple) -> tuple:
    """A sign-READING fingerprint (counts +1 literals) -- used as [F] control."""
    return tuple(sum(1 for (_, e) in ch[-1] if e == 1) for ch in chains)


# XOR / edge-signed layer (the Harary-balance encoding, ADAPTER2-01 vocabulary)

def satisfiable_xor(props: tuple, cons: dict) -> bool:
    """cons: {(p,q): parity}; parity 0 = agree, 1 = differ.  Brute force."""
    n = len(props)
    for bits in range(2 ** n):
        assign = {props[i]: 1 if (bits >> i) & 1 else -1 for i in range(n)}
        if all((assign[p] != assign[q]) == bool(par)
               for (p, q), par in cons.items()):
            return True
    return False


def xor_satisfied(assign: dict, cons: dict) -> bool:
    return all((assign[p] != assign[q]) == bool(par)
               for (p, q), par in cons.items())


# ----------------------------------------------- attempt 1: arrow -> spectrum

# Extension chain (source-side, Ext_S vocabulary): S0 c S1 c S2 c S3 with
# record counts 0,1,2,4.  tau(e) = record growth (additive under composition:
# the E160-shape composition-compatible label carried by admissibility itself).
CHAIN_A1 = (
    frozenset(),
    frozenset({("p", 1)}),
    frozenset({("p", 1), ("q", 1)}),
    frozenset({("p", 1), ("q", 1), ("r", -1), ("s", 1)}),
)
A1 = np.diag([-1.0, -2.0, 1.0, 0.5])     # candidate issuance generator


def tau(si: State, sj: State) -> float:
    return float(len(sj) - len(si))


def rep(gen: np.ndarray, si: State, sj: State) -> np.ndarray:
    """Representation R(e: si -> sj) = exp(tau(e) * gen)."""
    return expm(tau(si, sj) * gen)


def functorial(gen: np.ndarray, chain: tuple, label=tau) -> bool:
    """R(e2 o e1) = R(e2) R(e1) for all composable pairs in the chain,
    with R(e) = exp(label(e) * gen)."""
    ok = True
    for i in range(len(chain)):
        for j in range(i, len(chain)):
            for k in range(j, len(chain)):
                lhs = expm(label(chain[i], chain[k]) * gen)
                rhs = expm(label(chain[j], chain[k]) * gen) @ \
                    expm(label(chain[i], chain[j]) * gen)
                ok &= bool(np.allclose(lhs, rhs, atol=1e-8))
    return ok


def tau_sq(si: State, sj: State) -> float:      # broken, non-additive label
    return tau(si, sj) ** 2


# ------------------------------------- attempt 2: growth functional -> spectrum

# Four issuance channels; record counts over 5 stages (monotone by issuance).
COUNTS = np.array([
    [0, 0, 0, 0],
    [2, 1, 3, 1],
    [4, 2, 5, 1],
    [6, 3, 8, 2],
    [8, 4, 10, 2],
], dtype=float)
COUNTS_BROKEN = COUNTS.copy()
COUNTS_BROKEN[3, 2] = 4.0               # channel shrinks: inadmissible


def monotone_counts(c: np.ndarray) -> bool:
    return bool(np.all(np.diff(c, axis=0) >= 0)) and \
        bool(np.any(np.diff(c, axis=0) > 0))


def growth_rates(c: np.ndarray) -> np.ndarray:
    return (c[-1] - c[0]) / (len(c) - 1)


# ------------------------------------------- attempt 3: fork realization

H_PLUS = (frozenset(), frozenset({("p", 1)}))
H_MINUS = (frozenset(), frozenset({("p", -1)}))


def equivariant_alignments():
    """All maps m: {+1,-1} -> {K+,K-} with m(-e) = S m(e) S (flip-equivariant),
    plus the non-equivariant rest.  Finite exhaustive enumeration."""
    sectors = [KP, KM]
    eq, non_eq = [], []
    for a in sectors:
        for b in sectors:
            m = {1: a, -1: b}
            if same_proj(m[-1], S4 @ m[1] @ S4):
                eq.append(m)
            else:
                non_eq.append(m)
    return eq, non_eq


def components(props: tuple, cons: dict) -> int:
    """Connected components of the constraint graph = independent selection
    blocks (the (Z/2)^blocks fiber of lane-2 N4)."""
    parent = {p: p for p in props}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for (p, q) in cons:
        parent[find(p)] = find(q)
    return len({find(p) for p in props})


def parity_functorial(labels: dict) -> bool:
    """Z/2 transport-label functor check on the 3-object path x->y->z:
    labels on ('xy','yz','xz'); functorial iff xz = xy XOR yz."""
    return labels["xz"] == (labels["xy"] ^ labels["yz"])


# --------------------------------------------------------------------- main

def main() -> None:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    # ---------------- setup
    check("[T] setup: S eta S = -eta and S is an orthogonal involution",
          np.allclose(S4 @ ETA4 @ S4, -ETA4)
          and np.allclose(S4 @ S4, np.eye(4)) and np.allclose(S4, S4.T))

    # ---------------- source layer: what asymmetries does the source own?
    model = (CHAIN_A1, H_PLUS, H_MINUS)
    check("[T] s1: the fork flip is a source AUTOMORPHISM: label-free "
          "fingerprint invariant (lane-D framework theorem; instance cert.)",
          fingerprint(tuple(flip_chain(c) for c in model)) == fingerprint(model))
    check("[F] s1-fail: a sign-READING fingerprint (+1-literal count) is NOT "
          "flip-invariant on the same model (comparator can fail)",
          signed_fingerprint(tuple(flip_chain(c) for c in model))
          == signed_fingerprint(model), expected=False)
    check("[E] s2: SBP fork instance: both branches admissible and extendable "
          "(h+ and h- pass the issuance checker)",
          admissible_chain(H_PLUS) and admissible_chain(H_MINUS)
          and consistent(H_PLUS[-1] | {("q", 1)})
          and consistent(H_MINUS[-1] | {("q", 1)}))
    check("[F] s2-fail: a record-DROPPING chain is rejected by the same "
          "admissibility checker",
          admissible_chain((frozenset({("p", 1)}), frozenset())),
          expected=False)
    check("[T] s3: every strictly-growing chain's reversal is rejected -- the "
          "in-model arrow is real (two-line: strict growth breaks reverse "
          "inclusion; physical grade stays TaF-conditional, T18/T57)",
          all(not admissible_chain(tuple(reversed(c))) for c in model))
    check("[T] s3b: a constant (no-issuance) chain's reversal is ACCEPTED -- "
          "the arrow lives in strict extensions only (rejection not vacuous)",
          admissible_chain(tuple(reversed((frozenset({("p", 1)}),
                                           frozenset({("p", 1)}))))))
    # Two DISTINCT Z/2 operations on the source, only one asymmetric:
    tri = ("p", "q", "r")
    cons_bal = {("p", "q"): 0, ("q", "r"): 0, ("p", "r"): 0}
    cons_neg = {e: 1 - par for e, par in cons_bal.items()}   # edge negation
    check("[E] s4: EDGE negation is a genuinely asymmetric Z/2 on the source: "
          "balanced triangle satisfiable, all-edges-negated triangle NOT "
          "(odd-cycle frustration)",
          satisfiable_xor(tri, cons_bal) and not satisfiable_xor(tri, cons_neg))
    all_assigns = [{tri[i]: 1 if (b >> i) & 1 else -1 for i in range(3)}
                   for b in range(8)]
    check("[T] s5: the FORK flip (vertex/value negation) preserves EVERY edge "
          "constraint (exhaustive over 8 assignments x both constraint sets): "
          "the asymmetric Z/2 is not the fiber Z/2",
          all(xor_satisfied({p: -e for p, e in a.items()}, cons)
              == xor_satisfied(a, cons)
              for a in all_assigns for cons in (cons_bal, cons_neg)))

    # ---------------- ATTEMPT 1: irreversibility-as-spectrum
    check("[T] a1-1: R(e) = exp(tau(e) A) is composition-compatible on the "
          "extension chain (additive label + exponential law; E160 shape (ii))",
          functorial(A1, CHAIN_A1))
    check("[F] a1-1-fail: the non-additive label tau^2 BREAKS the same "
          "functoriality checker",
          functorial(A1, CHAIN_A1, label=tau_sq), expected=False)
    check("[E] a1-2: forward transport realizable on exactly one sector: "
          "C_stab(A1) = K+ (instance chosen to have the property; disclosed)",
          same_proj(c_stab(A1), KP))
    check("[E] a1-3: TIME-reversed transport realizable on the OTHER sector: "
          "C_stab(-A1) = K- (the arrow choice moves the selection)",
          same_proj(c_stab(-A1), KM))
    check("[T] a1-4: the arrow is issuance-discriminated but the S-twin is "
          "not: reversed source chain REJECTED, twin's source chain is the "
          "IDENTICAL accepted chain (S acts on the target only)",
          not admissible_chain(tuple(reversed(CHAIN_A1)))
          and admissible_chain(CHAIN_A1))
    twin = flipK(A1)
    check("[T] a1-5: the S-twin representation satisfies the ENTIRE "
          "constraint list (functorial; forward one-sector; reverse "
          "other-sector) -- every constraint is flip-stable",
          functorial(twin, CHAIN_A1)
          and c_stab(twin) is not None and c_stab(-twin) is not None)
    check("[T] a1-6: twin selects the SWAPPED sector: "
          "C_stab(S A1 S) = S K+ S = K- (covariance identity)",
          same_proj(c_stab(twin), S4 @ KP @ S4))
    check("[T] a1-7: flip-even battery cannot separate A1 from its twin "
          "(eigenvalue moduli, trace, ||e^{2A}||, J-dissipativity -- each item "
          "a similarity/orthogonal-invariance identity)",
          np.allclose(sorted(np.abs(np.linalg.eigvals(A1))),
                      sorted(np.abs(np.linalg.eigvals(twin))))
          and np.isclose(np.trace(A1), np.trace(twin))
          and np.isclose(np.linalg.norm(expm(2 * A1), 2),
                         np.linalg.norm(expm(2 * twin), 2))
          and j_dissipative(A1) == j_dissipative(twin))
    check("[F] a1-8: the circularity control C_circ FAILS flip-robustness on "
          "the same instance (label-reader; same same_proj criterion path)",
          same_proj(c_circ(twin), S4 @ c_circ(A1) @ S4), expected=False)

    # ---------------- ATTEMPT 2: growth functional -> spectrum
    check("[E] a2-1: the 4-channel issuance model is monotone (records "
          "accumulate) with strictly positive growth rates",
          monotone_counts(COUNTS) and bool(np.all(growth_rates(COUNTS) > 0)))
    check("[F] a2-1-fail: a shrinking channel is rejected by the same "
          "monotonicity checker",
          monotone_counts(COUNTS_BROKEN), expected=False)
    q = growth_rates(COUNTS)
    H_grow = np.diag(q)
    check("[T] a2-2: THEOREM (growth blindness): the growth-built generator "
          "H = diag(Q) has positive restricted spectrum on BOTH sectors, so "
          "C_energy is UNDEFINED -- monotone issuance forces Q >= 0 uniformly; "
          "positivity cannot land on one sector",
          c_energy(H_grow) is None)
    H_eta = ETA4 @ H_grow
    check("[E] a2-3: the eta-COUPLED generator H = eta diag(Q) selects K+ "
          "(sector asymmetry appears only after coupling growth to the form)",
          same_proj(c_energy(H_eta), KP))
    check("[T] a2-4: C_energy on H_eta is J-flip-robust "
          "(covariance identity: C_energy(S H S) = S C_energy(H) S)",
          same_proj(c_energy(flipK(H_eta)), S4 @ KP @ S4))
    check("[T] a2-5: ORBIT CONSUMED -- the flip-orbit twin S H_eta S is built "
          "from the SAME growth data, is equally admissible (eta-self-adjoint, "
          "same spectrum-as-set), and the only separator found is the "
          "flip-odd label-reader trace(J H)",
          np.allclose(ETA4 @ flipK(H_eta).T @ ETA4, flipK(H_eta))
          and np.allclose(sorted(np.linalg.eigvals(flipK(H_eta)).real),
                          sorted(np.linalg.eigvals(H_eta).real))
          and np.isclose(np.trace(J4 @ flipK(H_eta)), -np.trace(J4 @ H_eta))
          and abs(np.trace(J4 @ H_eta)) > 0.1)
    check("[T] a2-6: the 'Krein-norm rate = +growth' variant (eta-expansive "
          "class, instance A = eta) is flip-ODD: S(eta)S = -eta is "
          "eta-CONTRACTIVE -- the sign posit restated (lane-3 T-a')",
          eta_expansive(ETA4) and eta_contractive(flipK(ETA4))
          and not eta_expansive(flipK(ETA4)))
    check("[E] a2-7: and its realizability selection C_stab(eta) = K- is "
          "again a selection the twin makes oppositely: C_stab(-eta) = K+",
          same_proj(c_stab(ETA4), KM) and same_proj(c_stab(-ETA4), KP))

    # ---------------- ATTEMPT 3: fork-resolution asymmetry
    eq_maps, non_eq_maps = equivariant_alignments()
    check("[T] a3-1: exhaustive enumeration: exactly TWO flip-equivariant "
          "alignment maps literal->sector exist (the bit), and the two "
          "non-equivariant maps are the constant label-readers",
          len(eq_maps) == 2 and len(non_eq_maps) == 2
          and all(same_proj(m[1], m[-1]) for m in non_eq_maps))
    m_align = eq_maps[0] if same_proj(eq_maps[0][1], KP) else eq_maps[1]
    check("[E] a3-2: PER-HISTORY RELABELING: h+ selects K+, h- selects K- "
          "under the same alignment, and flip(h+) is structurally identical "
          "to h- (same fingerprint) -- same physics, opposite selection",
          same_proj(m_align[1], KP) and same_proj(m_align[-1], KM)
          and fingerprint((flip_chain(H_PLUS),)) == fingerprint((H_MINUS,)))
    check("[E] a3-3: BLOCK STRUCTURE: two unlinked propositions give 2 "
          "independent selection blocks ((Z/2)^2 fiber, lane-2 N4 shape); an "
          "XOR link merges them to 1; never 0",
          components(("p", "q"), {}) == 2
          and components(("p", "q"), {("p", "q"): 0}) == 1)
    check("[T] a3-4: a CONSISTENT Z/2 transport table exists but is not "
          "unique: both the trivial and the twin table pass the parity "
          "functor checker -- choosing one is imported data (E160 case 4)",
          parity_functorial({"xy": 0, "yz": 0, "xz": 0})
          and parity_functorial({"xy": 1, "yz": 1, "xz": 0}))
    check("[F] a3-5: an INCONSISTENT transport table fails the same parity "
          "functor checker (E160 case-5 analog)",
          parity_functorial({"xy": 1, "yz": 0, "xz": 0}), expected=False)

    # ---------------- meta: the equivariance wall, certified across attempts
    wall = True
    for gen, sel in ((A1, c_stab), (ETA4, c_stab), (H_eta, c_energy)):
        s = sel(gen)
        wall &= s is not None and same_proj(sel(flipK(gen)), S4 @ s @ S4)
    check("[T] m1: EQUIVARIANCE WALL certified on every attempt's generator: "
          "sel(S A S) = S sel(A) S -- each attempt's selector is covariant, "
          "so each derivation chain delivers an ORBIT, never a member",
          wall)

    # ---------------- report
    print("CONDITION 2' CONSTRUCTIVE PROBE (adversarial-twin lane)")
    print("=" * 74)
    failures = []
    n_t = n_e = n_f = 0
    for name, value, expected in checks:
        ok = value == expected
        tag = "PASS" if ok else "UNEXPECTED"
        if name.startswith("[T]"):
            n_t += 1
        elif name.startswith("[E]"):
            n_e += 1
        elif name.startswith("[F]"):
            n_f += 1
        line = f"{tag}  {name}: {value}"
        if name.startswith("[F]"):
            line += "   (failing direction: checker CAN fail)"
        print(line)
        if not ok:
            failures.append(name)
    print()
    print(f"CHECK CENSUS: {n_t} [T] theorem-certificates (no evidential "
          f"weight), {n_e} [E] instance tests, {n_f} [F] controls.")
    if failures:
        print("UNEXPECTED RESULTS:", failures)
        raise SystemExit(1)
    print("All checks match pre-declared expectations. Exit 0.")


if __name__ == "__main__":
    main()
