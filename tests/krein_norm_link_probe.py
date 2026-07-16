"""Krein-dynamical norm-link probe (P2C follow-up to lane D's one open door).

Question (lane D, Section 4/6, referee-governed): is there a characterization
of "the issuance-supporting Krein sector" that (i) distinguishes the sectors
at all, (ii) is robust under the global flip INCLUDING the flip of the
fundamental symmetry J, and (iii) is not a restatement of
"physical = positive-norm"?

FORMAL FLIP.  Krein space (R^4 or C^2, [x,y] = <x, eta y>), eta = diag(+,-),
J = eta, sectors K+ / K-.  With p = q there is a swap S (orthogonal, S^2 = I)
with S eta S = -eta.  The global flip is: form -> -form, J -> -J (still a
fundamental symmetry for the flipped form; the J-inner product <x,y>_J is
flip-INVARIANT since both signs cancel), dynamics unchanged, sector labels
swapped.  Recoordinatizing the flipped presentation by S restores (eta, J) as
matrices and moves the whole flip into the generator: A -> S A S, with the
physical identity of subspaces relabeled by S.  Hence a characterization C
(returning a sector projector) is

  ROBUST        iff  C(S A S) = S C(A) S    (tracks the physical subspace)
  LABEL-READING iff  C(S A S) = C(A) while S C(A) S != C(A)
                                            (follows whatever J calls positive)

CHECK LABELS (honesty rule: no cannot-fail check presented as a control):
  [T] theorem-certificate: a short proof exists and is given in the deliverable
      text; the code certifies instances.  A failure would indicate an
      implementation bug, not new physics.  Not sampled evidence.
  [E] genuine instance test whose outcome was not fixed at formalization time.
  [F] demonstrated FAILING direction of a checker used above it (the control's
      control).

Exit 0 iff every check matches its expected value.  Pure numpy, no scipy.
"""

from __future__ import annotations

import numpy as np

rng = np.random.default_rng(20260716)

# ---------------------------------------------------------------- primitives

ETA4 = np.diag([1.0, 1.0, -1.0, -1.0])
J4 = ETA4.copy()
S4 = np.eye(4)[[2, 3, 0, 1]]          # e1<->e3, e2<->e4; S=S^T, S^2=I
KP = np.diag([1.0, 1.0, 0.0, 0.0])    # projector onto K+
KM = np.diag([0.0, 0.0, 1.0, 1.0])    # projector onto K-

ETA2 = np.diag([1.0, -1.0])


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


def flip(a: np.ndarray) -> np.ndarray:
    """Global flip (eta -> eta, J -> -J, labels swapped) in std coordinates."""
    return S4 @ a @ S4


def maxeig_sym(m: np.ndarray) -> float:
    return float(np.max(np.linalg.eigvalsh((m + m.T.conj()) / 2)))


def mineig_sym(m: np.ndarray) -> float:
    return float(np.min(np.linalg.eigvalsh((m + m.T.conj()) / 2)))


def eta_contractive(a: np.ndarray) -> bool:
    """d/dt [x_t, x_t] <= 0  <=>  eta A + A^T eta <= 0."""
    return maxeig_sym(ETA4 @ a + a.T @ ETA4) <= 1e-10


def j_dissipative(a: np.ndarray) -> bool:
    """Contraction semigroup in the (flip-invariant) J-inner product."""
    return maxeig_sym(a + a.T) <= 1e-10


def sector_bounded(a: np.ndarray, proj: np.ndarray, norm=None) -> bool:
    """Is sup_t ||e^{tA} x|| finite for x in the (A-invariant) sector?

    Decided numerically on a t-grid; cross-checkable spectrally.  norm: a
    callable vector norm (default Euclidean) -- used for the J/norm-freeness
    test, since boundedness must not depend on the norm in finite dimensions.
    """
    if norm is None:
        norm = lambda v: float(np.linalg.norm(v))
    basis = [proj[:, i] for i in range(4) if abs(proj[i, i]) > 0.5]
    sup = 0.0
    for t in np.linspace(0.0, 30.0, 61):
        e = expm(t * a)
        sup = max(sup, max(norm(e @ q) for q in basis))
    return sup < 1e3


def c_stab(a: np.ndarray):
    """Candidate characterization: the sector whose restricted issuance
    semigroup is bounded (realizable/normalizable), if exactly one is."""
    bp, bm = sector_bounded(a, KP), sector_bounded(a, KM)
    if bp == bm:
        return None
    return KP if bp else KM


def c_circ(a: np.ndarray):
    """Circularity control: 'physical = positive-norm' restated -- returns
    the J-positive sector, ignoring the dynamics."""
    return KP


def restricted_spectrum(a: np.ndarray, proj: np.ndarray) -> np.ndarray:
    idx = [i for i in range(4) if abs(proj[i, i]) > 0.5]
    return np.linalg.eigvals(a[np.ix_(idx, idx)])


def c_energy(h: np.ndarray):
    """Task item 3: the sector on which the restricted spectrum is positive
    (finite-dim PROXY for 'Hamiltonian bounded below in one sector only';
    stated as encoding-level, not formalism-level)."""
    pos_p = bool(np.all(restricted_spectrum(h, KP).real > 0))
    pos_m = bool(np.all(restricted_spectrum(h, KM).real > 0))
    if pos_p == pos_m:
        return None
    return KP if pos_p else KM


def same_proj(p, q) -> bool:
    if p is None or q is None:
        return p is None and q is None
    return bool(np.allclose(p, q))


def krein2(x: np.ndarray) -> complex:
    return complex(x.conj() @ ETA2 @ x)


# ---------------------------------------------------------------- candidates

# (a) eta-contractive issuance generator (Krein-norm monotone decreasing),
#     sector-invariant instance.
A_A = np.diag([-1.0, -2.0, 1.0, 0.5])

# (b) J-dissipative generators (probability-contractive in the J-norm).
A_B_SYM = -np.eye(4) + 0.3 * (np.outer(np.eye(4)[0], np.eye(4)[2])
                              - np.outer(np.eye(4)[2], np.eye(4)[0]))

# (c) stability/spectral candidate: stable on K+, unstable on K-.
A_C = np.zeros((4, 4))
A_C[:2, :2] = [[-1.0, 0.5], [0.0, -2.0]]     # spectrum {-1,-2}
A_C[2:, 2:] = [[0.7, -0.4], [0.2, 1.3]]      # spectrum {0.9,1.1}

# (e) task item 3: sector-signed spectrum, eta-self-adjoint (diagonal).
H_SPEC = np.diag([1.0, 2.0, -3.0, -4.0])

# (d) Krein-native: coupled eta-self-adjoint Hamiltonian, complex 2D toy.
G_COUPLE = 0.8
H_COUPLED = np.array([[0.0, G_COUPLE], [-G_COUPLE, 0.0]], dtype=complex)
H_DECOUPLED = np.diag([1.0, -2.0]).astype(complex)


def is_eta2_selfadjoint(h: np.ndarray) -> bool:
    return bool(np.allclose(ETA2 @ h.conj().T @ ETA2, h))


def main() -> None:
    checks: list[tuple[str, bool, bool]] = []  # (name, value, expected)

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    # ---------------- setup sanity
    check("[T] setup: S eta S = -eta (S is an anti-isometry of the form)",
          np.allclose(S4 @ ETA4 @ S4, -ETA4))
    check("[T] setup: S orthogonal involution",
          np.allclose(S4 @ S4, np.eye(4)) and np.allclose(S4, S4.T))

    # ---------------- candidate (a): eta-contractive semigroup
    check("[E] a1: A_a is eta-contractive", eta_contractive(A_A))
    check("[F] a1-fail: A = eta is NOT eta-contractive (it is eta-expansive)",
          eta_contractive(ETA4), expected=False)
    check("[E] a2: A_a distinguishes sectors (K+ bounded, K- unbounded)",
          sector_bounded(A_A, KP) and not sector_bounded(A_A, KM))
    # THEOREM (a): for block-diagonal A = diag(A_+, A_-),
    #   eta-contractive  <=>  A_+ dissipative  AND  A_- accretive.
    # Proof: eta A + A^T eta = diag(A_+ + A_+^T, -(A_- + A_-^T)) <= 0.
    # So the class FORCES intrinsic-norm contraction on K+ and expansion on
    # K-: the sector distinction is the class definition, not a discovery.
    thm_a = True
    for _ in range(50):
        g1, g2 = rng.normal(size=(2, 2)), rng.normal(size=(2, 2))
        ap = (g1 - g1.T) / 2 - (g1.T @ g1) / 8 - 0.1 * np.eye(2)
        am = -((g2 - g2.T) / 2 - (g2.T @ g2) / 8 - 0.1 * np.eye(2))
        a = np.zeros((4, 4)); a[:2, :2] = ap; a[2:, 2:] = am
        e1, e2 = expm(ap), expm(am)
        thm_a &= eta_contractive(a)
        thm_a &= np.linalg.norm(e1, 2) <= 1 + 1e-9            # contraction K+
        thm_a &= float(np.linalg.svd(e2)[1].min()) >= 1 - 1e-9  # expansion K-
    check("[T] a3: eta-contractive block class = contract-on-K+/expand-on-K- "
          "(50 random certificates of the two-line theorem)", thm_a)
    # THEOREM (a'): the flip maps eta-contractive to eta-expansive:
    #   eta(SAS) + (SAS)^T eta = -S(eta A + A^T eta)S.
    # The CLASS is not flip-stable: choosing 'issuance decreases [.,.]' over
    # 'increases' IS the overall form-sign choice -- the bit, restated.
    check("[T] a4: flip(A_a) is NOT eta-contractive (class is flip-ODD)",
          eta_contractive(flip(A_A)), expected=False)
    check("[T] a4b: flip(A_a) is eta-EXPANSIVE",
          mineig_sym(ETA4 @ flip(A_A) + flip(A_A).T @ ETA4) >= -1e-10)

    # ---------------- candidate (b): J-dissipative (J-norm probability)
    # THEOREM (b): A + A^T <= 0  =>  ||e^{tA}||_J <= 1 on the WHOLE space:
    # J-probability contraction is sector-blind; the class never selects.
    check("[T] b1: J-dissipative class is flip-STABLE "
          "(J-inner product is flip-invariant; S orthogonal)",
          j_dissipative(A_B_SYM) and j_dissipative(flip(A_B_SYM)))
    check("[E] b2: J-dissipative instance distinguishes NOTHING "
          "(both sectors bounded; C_stab undefined)",
          c_stab(A_B_SYM) is None)
    check("[T] b3: J-dissipative => globally bounded (both sectors realizable)",
          sector_bounded(A_B_SYM, KP) and sector_bounded(A_B_SYM, KM))

    # ---------------- candidate (c): stability / realizability
    check("[E] c1: A_c distinguishes sectors (bounded on K+ only)",
          same_proj(c_stab(A_C), KP))
    # J/norm-freeness of boundedness (finite dim: all norms equivalent).
    w_m = rng.normal(size=(4, 4)); W = w_m.T @ w_m + np.eye(4)
    wnorm = lambda v: float(np.sqrt(np.real(v.conj() @ W @ v)))
    check("[T] c2: boundedness verdict identical in Euclidean and random-SPD "
          "norm (norm-free, hence J-free)",
          sector_bounded(A_C, KP, wnorm) and not sector_bounded(A_C, KM, wnorm))
    # [F] failing direction for c2's checker: NON-asymptotic functionals DO
    # depend on the norm (so 'same in every norm' is not vacuously true of
    # everything this checker touches -- only bounded-vs-unbounded is norm-free).
    a2 = np.array([[-0.1, 3.0], [0.0, -0.2]])
    d = np.diag([1.0, 100.0])
    thr_euclid = max(np.linalg.norm(expm(t * a2), 2)
                     for t in np.linspace(0, 1, 21)) <= 1.1
    thr_dnorm = max(np.linalg.norm(d @ expm(t * a2) @ np.linalg.inv(d), 2)
                    for t in np.linspace(0, 1, 21)) <= 1.1
    check("[F] c2-fail: threshold functional sup_{t<=1}||e^{tA}||<=1.1 "
          "DIFFERS across norms (transient growth)",
          thr_euclid == thr_dnorm, expected=False)
    # The pass/fail criterion itself:
    check("[E] c3: C_stab is J-FLIP-ROBUST: C_stab(flip A_c) = S C_stab(A_c) S",
          same_proj(c_stab(flip(A_C)), S4 @ KP @ S4))
    check("[F] c3-fail: C_circ ('physical = positive-norm') FAILS robustness "
          "(follows the label, not the physical subspace)",
          same_proj(c_circ(flip(A_C)), S4 @ c_circ(A_C) @ S4), expected=False)
    check("[T] c4: spectra do not relabel: spec(flip A_c) = spec(A_c) as a set",
          np.allclose(np.sort_complex(np.linalg.eigvals(flip(A_C))),
                      np.sort_complex(np.linalg.eigvals(A_C))))
    # ORBIT LEMMA certificates: A_c and flip(A_c) agree on every flip-EVEN
    # (label-free) invariant in the battery; every separator found is
    # flip-ODD, i.e. reads the sign datum.
    battery_even = (
        np.allclose(sorted(np.abs(np.linalg.eigvals(A_C))),
                    sorted(np.abs(np.linalg.eigvals(flip(A_C)))))
        and j_dissipative(A_C) == j_dissipative(flip(A_C))
        and np.isclose(np.linalg.norm(expm(2.0 * A_C), 2),
                       np.linalg.norm(expm(2.0 * flip(A_C)), 2))
        and np.isclose(np.trace(A_C), np.trace(flip(A_C)))
    )
    check("[E] c5: flip-even invariant battery cannot separate A_c from "
          "flip(A_c) (the two selections are internally indistinguishable)",
          battery_even)
    check("[T] c6: separators exist but are flip-ODD label-readers: "
          "trace(J A) changes sign under the flip",
          np.isclose(np.trace(J4 @ flip(A_C)), -np.trace(J4 @ A_C))
          and abs(np.trace(J4 @ A_C)) > 1)
    check("[T] c6b: eta-contractivity membership is itself flip-ODD on A_c "
          "(member vs non-member)",
          eta_contractive(A_C) and not eta_contractive(flip(A_C)))

    # ---------------- candidate (d): Krein-native (eta-self-adjoint H)
    check("[E] d0: H_coupled is eta-self-adjoint (Krein-unitary evolution)",
          is_eta2_selfadjoint(H_COUPLED))
    u25 = expm(-1j * 2.5 * H_COUPLED)
    states = [np.array([1, 0], complex), np.array([0, 1], complex),
              np.array([1, 1], complex) / np.sqrt(2)]
    check("[T] d1: Krein probability [psi_t,psi_t] exactly conserved for BOTH "
          "sector states and mixed (Krein-unitarity: sector-blind)",
          all(np.isclose(krein2(u25 @ s), krein2(s), atol=1e-8) for s in states))
    check("[F] d1-fail: Euclidean (J-)norm is NOT conserved by the coupled "
          "evolution (so d1's checker can fail)",
          bool(np.isclose(np.linalg.norm(u25 @ states[0]), 1.0, atol=1e-6)),
          expected=False)
    evals, evecs = np.linalg.eig(H_COUPLED)
    k = int(np.argmax(evals.imag))          # lambda = +ig -> growing mode of U
    v = evecs[:, k]
    check("[E] d2: the coupled instability's growing mode is eta-NEUTRAL "
          "([v,v]=0) with EQUAL sector components -- it selects no sector",
          np.isclose(abs(krein2(v)), 0.0, atol=1e-9)
          and np.isclose(abs(v[0]), abs(v[1]), atol=1e-9))
    check("[F] d2-fail: decoupled H eigenvectors are eta-DEFINITE, not "
          "neutral (the neutrality checker can fail)",
          all(np.isclose(abs(krein2(np.linalg.eig(H_DECOUPLED)[1][:, i])), 0.0,
                         atol=1e-9) for i in range(2)),
          expected=False)
    # THEOREM (d): eta-self-adjoint H, H v = lambda v, lambda non-real
    #   =>  (lambda - conj(lambda)) [v,v] = 0  =>  [v,v] = 0.
    thm_d = True
    n_nonreal = 0
    for _ in range(50):
        a_, d_ = rng.normal(), rng.normal()
        b_ = (abs(a_ - d_) + 1.0) * np.exp(1j * rng.uniform(0, 2 * np.pi))
        h = np.array([[a_, b_], [-np.conj(b_), d_]], dtype=complex)
        thm_d &= is_eta2_selfadjoint(h)
        ev, evec = np.linalg.eig(h)
        for i in range(2):
            if abs(ev[i].imag) > 1e-8:
                n_nonreal += 1
                thm_d &= bool(np.isclose(abs(krein2(evec[:, i])), 0.0,
                                         atol=1e-8))
    check("[T] d3: 50 random eta-self-adjoint H: every non-real-eigenvalue "
          f"eigenvector is neutral ({n_nonreal} instances certified)",
          thm_d and n_nonreal >= 50)

    # ---------------- candidate (e): task item 3, spectral condition
    check("[E] e1: C_energy(H_spec) selects K+ (restricted spectrum positive "
          "there only)", same_proj(c_energy(H_SPEC), KP))
    check("[E] e2: C_energy is J-FLIP-ROBUST: C_energy(flip H) = S K+ S "
          "(spectra do not relabel)",
          same_proj(c_energy(flip(H_SPEC)), S4 @ KP @ S4))
    check("[F] e2-fail: C_circ fails robustness on the same instance",
          same_proj(c_circ(flip(H_SPEC)), S4 @ c_circ(H_SPEC) @ S4),
          expected=False)
    check("[E] e3: flip(H_spec) is in the SAME admissible class "
          "(eta-self-adjoint, sector-invariant): the framework admits both "
          "orbit members; selecting one is the external Z/2 datum",
          np.allclose(ETA4 @ flip(H_SPEC).T @ ETA4, flip(H_SPEC))
          and np.allclose(np.sort(np.linalg.eigvals(flip(H_SPEC)).real),
                          np.sort(np.linalg.eigvals(H_SPEC).real)))
    check("[T] e4: the orbit separator is again the flip-odd label-reader: "
          "trace(J H) flips sign",
          np.isclose(np.trace(J4 @ flip(H_SPEC)), -np.trace(J4 @ H_SPEC))
          and abs(np.trace(J4 @ H_SPEC)) > 1)

    # ---------------- report
    print("KREIN-DYNAMICAL NORM-LINK PROBE (lane D's open door)")
    print("=" * 74)
    failures = []
    for name, value, expected in checks:
        ok = value == expected
        tag = "PASS" if ok else "UNEXPECTED"
        shown = f"{tag}  {name}: {value}"
        if name.startswith("[F]"):
            shown += "   (demonstrated failing direction: checker CAN fail)"
        print(shown)
        if not ok:
            failures.append(name)
    print()
    if failures:
        print("UNEXPECTED RESULTS:", failures)
        raise SystemExit(1)
    print("VERDICT INPUTS (see deliverable): J-flip-ROBUST characterizations "
          "exist (c3, e2) and are")
    print("non-circular in the stated sense (c2 norm-free; the circular "
          "control c3-fail/e2-fail fails")
    print("robustness); but the sector asymmetry is supplied by the "
          "generator (c5/e3: both orbit")
    print("members admissible and internally indistinguishable; c6/e4: every "
          "separator is a flip-odd")
    print("label-reader), the eta-monotone class is the sign posit restated "
          "(a3/a4), the J-honest")
    print("class never selects (b2/b3), and Krein-unitary instabilities are "
          "neutral-cone (d2/d3).")
    print("All checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()
