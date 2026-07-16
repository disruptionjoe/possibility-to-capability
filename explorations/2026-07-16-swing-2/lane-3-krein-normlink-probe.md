> Part of the 2026-07-16 P2C swing 2 (four adversarially-refereed lanes). Exploration tier; no claim promotion; the attached referee report GOVERNS the grades — read it before citing the lane report.

All checks pass deterministically (exit 0), fixture committed and pushed at `96b96bc`. Deliverable follows.

---

# P2C — Krein-dynamical norm-link probe (the one open door from lane D)

Tier: exploration. Grade: **finite-dimensional toy — two-line theorems with executable certificates, plus instance tests each with a demonstrated failing direction.** No claim promotion. GU/TI/TaF remain sovereign; nothing here reopens the withdrawn `bar(b) = finality-axis polarity` identity or moves `bar(b)`, H59, Krein positivity, or physical issuance (all OPEN). Governed by ADAPTER2-01. Runnable receipt persisted in-repo: `possibility-to-capability/tests/krein_norm_link_probe.py`, commit `96b96bc`, exit 0.

## 1. Formal setup

**Krein toy.** `K = R^4` (and `C^2` for the Krein-native candidate) with indefinite form `[x,y] = <x, eta y>`, `eta = diag(+1,+1,-1,-1)`, fundamental symmetry `J = eta`, J-inner product `(x,y)_J = [Jx,y] = <x,y>` (Euclidean), sectors `K+ = span(e1,e2)`, `K- = span(e3,e4)`, `p = q = 2`.

**The global flip, made precise.** The physical flip is: form → −form, `J → −J` (note `−J` is a valid fundamental symmetry *for the flipped form*, and the J-inner product is **flip-invariant**: `(−form)(−Jx, y) = [Jx,y]` — the Hilbert structure does not flip; only the Krein form and `J` do), dynamics unchanged, sector labels swapped. With `p = q` the swap `S` (`e1↔e3, e2↔e4`; orthogonal involution, `S eta S = −eta`) is an isomorphism from the flipped presentation `(−eta, −J, A)` back to the standard presentation `(eta, J, SAS)`. So in standard coordinates the entire flip acts as `A → SAS`, with the physical identity of every subspace relabeled by `S`. A characterization `C` (dynamics ↦ sector projector) is therefore:

- **J-flip-ROBUST** iff `C(SAS) = S·C(A)·S` — it tracks the physical subspace (the fixed pass/fail criterion);
- **LABEL-READING** iff it instead returns whatever `J` calls positive (`C(SAS) = C(A)` while `S C(A) S ≠ C(A)`) — the definitional circle.

**Check-labeling discipline** (learning from the lane-D referee's D1): every check is tagged `[T]` theorem-certificate (short proof given below; the code certifies instances — a code failure would mean an implementation bug, not new physics; *not* sampled evidence), `[E]` genuine instance test, or `[F]` demonstrated failing direction of a checker used above it. No cannot-fail check is presented as a control.

## 2. Candidates, theorems, results

**(a) eta-contractive semigroup** (`d/dt [x_t,x_t] ≤ 0`, i.e. `eta A + A^T eta ⪯ 0`). Instance `A_a = diag(−1,−2,1,0.5)` is eta-contractive and distinguishes the sectors: bounded on `K+`, unbounded on `K−` (a1, a2; failing direction a1-fail: `A = eta` is rejected as eta-*expansive*).

- **Theorem T-a** (a3, 50 random certificates): for block-diagonal `A = diag(A_+, A_-)`, eta-contractive ⟺ `A_+` dissipative AND `A_-` accretive. Proof: `eta A + A^T eta = diag(A_+ + A_+^T, −(A_- + A_-^T))`. So "contract on `K+`, expand on `K−`" is the class *definition*, not a discovery.
- **Theorem T-a′** (a4/a4b): the flip reverses the class: `eta(SAS) + (SAS)^T eta = −S(eta A + A^T eta)S`, so `flip(A_a)` is eta-**expansive**. The class is **flip-odd**: declaring issuance to *decrease* rather than *increase* `[·,·]` is exactly the overall form-sign choice. **Candidate (a) is the sign posit restated at the semigroup level** — the definitional circle in a dynamical costume, proved, not vibed.

**(b) J-self-adjoint/J-dissipative generator** (probability-contraction in the flip-invariant J-norm: `A + A^T ⪯ 0`). The class IS flip-stable (b1 — the honest contrast to a4: one class survives the flip, the other does not; each check can fail). But **Theorem T-b** (b3): `A + A^T ⪯ 0` ⇒ `||e^{tA}|| ≤ 1` on the *whole* space — J-honest probability contraction is sector-blind; `C_stab` is undefined on the instance (b2). **Candidate (b) fails the "distinguishes at all" prong.** The only way to distinguish by realizability is unbounded behavior somewhere — which exits this class.

**(c) Stability/realizability characterization** `C_stab(A)` = the sector on which the restricted semigroup is bounded. Instance `A_c = diag(block[[−1,.5],[0,−2]], block[[.7,−.4],[.2,1.3]])` (spectra `{−1,−2}` / `{0.9,1.1}`):

- c1: distinguishes (bounded on `K+` only).
- c2 `[T]`: the bounded-vs-unbounded verdict is **norm-free** (identical under Euclidean and a random-SPD norm; finite-dim norm equivalence), hence **J-free** — genuinely not a restatement of "physical = positive-norm". Failing direction c2-fail: a *threshold* functional (`sup_{t≤1}||e^{tA}|| ≤ 1.1`) demonstrably differs across norms (transient growth), so norm-freeness is a property of the asymptotic verdict specifically, not of everything the checker touches.
- c3 `[E]`: **`C_stab` is J-flip-ROBUST**: `C_stab(flip A_c) = S·K+·S`. Failing direction c3-fail: the circularity control `C_circ ≡ K+(J)` ("physical = positive-norm") **fails** robustness on the same instance — it follows the label, not the physical states. The pass/fail criterion has both directions exhibited.
- c4 `[T]`: spectra do not relabel — `spec(flip A_c) = spec(A_c)` as a set.
- **Covariance lemma** (why robustness is *cheap*): any `J`-free, basis-covariant recipe automatically satisfies `C(SAS) = S C(A) S`. Robustness alone is nearly free; the selective content must live elsewhere.
- **Orbit lemma** (c5, c6, c6b): the flip fixes `(eta, J)` as matrices and fixes every flip-stable admissibility class, so `{A_c, flip(A_c)}` is a single orbit. c5: a battery of flip-even (label-free) invariants — eigenvalue moduli, J-dissipativity membership, `||e^{2A}||_2`, trace — cannot separate the orbit members. c6/c6b: separators *exist* but every one found is **flip-odd**, i.e. reads the sign datum: `trace(J A)` flips sign under the flip; eta-contractivity membership is itself flip-odd. Group-theoretically: a functional separating flip-orbit members cannot be flip-even; flip-odd data in this toy *is* the sign label. **Selecting the orbit member costs exactly one external Z/2 bit.**

**(d) Krein-native control — coupled eta-self-adjoint Hamiltonian** (`C^2`, `H = [[0,g],[−g,0]]`, `eta H† eta = H`, Krein-unitary evolution `U(t) = e^{−iHt}`):

- d1 `[T]`: Krein probability `[psi_t, psi_t]` is *exactly conserved for both sector states and mixed states* — Krein-probability conservation is sector-blind (Krein-unitarity). Failing direction d1-fail: the Euclidean (J-)norm is NOT conserved (the coupled evolution blows up), so the conservation checker can fail.
- d2 `[E]`: the coupled instability's growing mode is **eta-NEUTRAL** (`[v,v] = 0`) with *equal* `K+`/`K−` components — the instability refuses to select a sector. Failing direction d2-fail: decoupled `H` has eta-*definite* eigenvectors, so the neutrality checker can fail.
- **Theorem T-d** (d3, 100 instances certified): eta-self-adjoint `H`, `Hv = λv`, `λ` non-real ⇒ `[v,v] = 0`. Proof: `λ[v,v] = [Hv,v] = [v,Hv] = λ̄[v,v]`.
- **Meaning:** within the Krein-probability-conserving class, sector-asymmetric realizability is impossible with coupling (instabilities live on the neutral cone) and absent with real spectrum (both sectors bounded). **Krein-unitary issuance dynamics never selects a sector by stability.** The clever-Krein-native-generator door is closed at toy grade.

**(e) Task item 3 — the spectral condition itself.** `H_spec = diag(1,2,−3,−4)`: restricted spectrum positive on `K+` only (finite-dim **proxy** for "Hamiltonian bounded below in one sector only" — this is an encoding-level statement; finite dimensions cannot express unboundedness, and I say so rather than claim the formalism-level fact). `C_energy` selects `K+` (e1); it is **J-flip-robust** (e2 — spectra do not relabel, exactly as the task predicted; failing direction e2-fail: `C_circ` fails again on the same instance). But e3/e4: `flip(H_spec)` is in the *same* admissible class (eta-self-adjoint, sector-invariant, same spectrum as a set), and the only separators are flip-odd label-readers (`trace(J H)` flips sign). **The spectral asymmetry that canonizes `J` was inserted by hand; the framework admits both orbit members with equal right. The asymmetry is the external datum wearing the name "energy positivity."**

## 3. Code (full source; canonical copy in-repo at `tests/krein_norm_link_probe.py`, commit `96b96bc`)

```python
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
```

## 4. Output (verbatim, exit 0)

```
KREIN-DYNAMICAL NORM-LINK PROBE (lane D's open door)
==========================================================================
PASS  [T] setup: S eta S = -eta (S is an anti-isometry of the form): True
PASS  [T] setup: S orthogonal involution: True
PASS  [E] a1: A_a is eta-contractive: True
PASS  [F] a1-fail: A = eta is NOT eta-contractive (it is eta-expansive): False   (demonstrated failing direction: checker CAN fail)
PASS  [E] a2: A_a distinguishes sectors (K+ bounded, K- unbounded): True
PASS  [T] a3: eta-contractive block class = contract-on-K+/expand-on-K- (50 random certificates of the two-line theorem): True
PASS  [T] a4: flip(A_a) is NOT eta-contractive (class is flip-ODD): False
PASS  [T] a4b: flip(A_a) is eta-EXPANSIVE: True
PASS  [T] b1: J-dissipative class is flip-STABLE (J-inner product is flip-invariant; S orthogonal): True
PASS  [E] b2: J-dissipative instance distinguishes NOTHING (both sectors bounded; C_stab undefined): True
PASS  [T] b3: J-dissipative => globally bounded (both sectors realizable): True
PASS  [E] c1: A_c distinguishes sectors (bounded on K+ only): True
PASS  [T] c2: boundedness verdict identical in Euclidean and random-SPD norm (norm-free, hence J-free): True
PASS  [F] c2-fail: threshold functional sup_{t<=1}||e^{tA}||<=1.1 DIFFERS across norms (transient growth): False   (demonstrated failing direction: checker CAN fail)
PASS  [E] c3: C_stab is J-FLIP-ROBUST: C_stab(flip A_c) = S C_stab(A_c) S: True
PASS  [F] c3-fail: C_circ ('physical = positive-norm') FAILS robustness (follows the label, not the physical subspace): False   (demonstrated failing direction: checker CAN fail)
PASS  [T] c4: spectra do not relabel: spec(flip A_c) = spec(A_c) as a set: True
PASS  [E] c5: flip-even invariant battery cannot separate A_c from flip(A_c) (the two selections are internally indistinguishable): True
PASS  [T] c6: separators exist but are flip-ODD label-readers: trace(J A) changes sign under the flip: True
PASS  [T] c6b: eta-contractivity membership is itself flip-ODD on A_c (member vs non-member): True
PASS  [E] d0: H_coupled is eta-self-adjoint (Krein-unitary evolution): True
PASS  [T] d1: Krein probability [psi_t,psi_t] exactly conserved for BOTH sector states and mixed (Krein-unitarity: sector-blind): True
PASS  [F] d1-fail: Euclidean (J-)norm is NOT conserved by the coupled evolution (so d1's checker can fail): False   (demonstrated failing direction: checker CAN fail)
PASS  [E] d2: the coupled instability's growing mode is eta-NEUTRAL ([v,v]=0) with EQUAL sector components -- it selects no sector: True
PASS  [F] d2-fail: decoupled H eigenvectors are eta-DEFINITE, not neutral (the neutrality checker can fail): False   (demonstrated failing direction: checker CAN fail)
PASS  [T] d3: 50 random eta-self-adjoint H: every non-real-eigenvalue eigenvector is neutral (100 instances certified): True
PASS  [E] e1: C_energy(H_spec) selects K+ (restricted spectrum positive there only): True
PASS  [E] e2: C_energy is J-FLIP-ROBUST: C_energy(flip H) = S K+ S (spectra do not relabel): True
PASS  [F] e2-fail: C_circ fails robustness on the same instance: False   (demonstrated failing direction: checker CAN fail)
PASS  [E] e3: flip(H_spec) is in the SAME admissible class (eta-self-adjoint, sector-invariant): the framework admits both orbit members; selecting one is the external Z/2 datum: True
PASS  [T] e4: the orbit separator is again the flip-odd label-reader: trace(J H) flips sign: True

VERDICT INPUTS (see deliverable): J-flip-ROBUST characterizations exist (c3, e2) and are
non-circular in the stated sense (c2 norm-free; the circular control c3-fail/e2-fail fails
robustness); but the sector asymmetry is supplied by the generator (c5/e3: both orbit
members admissible and internally indistinguishable; c6/e4: every separator is a flip-odd
label-reader), the eta-monotone class is the sign posit restated (a3/a4), the J-honest
class never selects (b2/b3), and Krein-unitary instabilities are neutral-cone (d2/d3).
All checks match expectations. Exit 0.
```

## 5. The interrogation (task item 3, answered honestly)

The spectral asymmetry **does** survive the J-flip (e2 — spectra don't relabel; this is the real content of the physics folklore "J becomes canonical when the spectral condition breaks the symmetry"). And it **was inserted by hand**: `flip(H_spec)` sits in the same admissible class with the same spectrum-as-a-set (e3), the flip-even invariant battery cannot tell the two apart (c5), and every separator constructed is flip-odd, i.e. a function of the sign label (c6/e4). Within a flip-stable admissibility class, `{A, SAS}` is a single orbit and picking the orbit member costs exactly one external Z/2 bit. The spectral condition is therefore **the external datum wearing a new name** — and the probe says so rather than presenting it as a derivation.

## 6. VERDICT: **REDUCED** (option iii), toy grade

**The norm-link reduces cleanly to the spectral condition (energy positivity: the issuance generator stable / Hamiltonian spectrum positive on exactly one Krein sector).** Precisely:

1. **Not REFUTED:** J-flip-robust, non-definitional characterizations of "the issuance-supporting sector" *exist* — `C_stab` (bounded/realizable restricted semigroup) and `C_energy` (sector-positive restricted spectrum) both pass the fixed criterion, and both are provably not restatements of "physical = positive-norm" (the boundedness verdict is norm-free hence J-free, c2; the actual restatement `C_circ` demonstrably fails the same test, c3-fail/e2-fail).
2. **Not FOUND (in the anchoring sense):** the covariance lemma shows robustness is nearly free for any label-free recipe; all selective content lives in the generator's sector asymmetry, and the orbit lemma (c5/c6/e3/e4) shows the framework admits both flip-orbit members with equal right — no `eta`/`J`-internal structure selects between them. Every route that tries to generate the asymmetry internally fails in a characterized way: the `eta`-monotone class is flip-odd, i.e. the form-sign posit restated (T-a, T-a′); the J-honest probability-contractive class is sector-blind by theorem (T-b); and Krein-unitary (Krein-probability-conserving) dynamics puts its instabilities on the **neutral cone**, never on a sector (T-d, d2) — so no coupled probability-conserving issuance generator can be one-sector-realizable.
3. **Where the posit now lives:** one bit, three equivalent names — (i) the overall sign of the Krein form (`bar(b)`-grade, GU's original datum), (ii) the direction of `eta`-norm monotonicity of issuance (contractive vs expansive), (iii) the choice of flip-orbit representative for the physical generator, i.e. **which sector carries the bounded-below/stable spectrum** — the spectral condition. That is a *named prior physics posit* (Krein-QFT spectral condition / energy positivity, operationally tied to the vacuum/arrow choice), **not finality-native at current grades**: TaF's T18 is conditional-constructor only and T57 leaves arrow-direction circularity open (per ADAPTER2-01), and lane D established that the extension-order asymmetry lives on the base while this bit is again a fiber selection. Relocation, not resolution: `bar(b)`, H59, Krein positivity, and physical issuance all remain **OPEN**; nothing here reopens the withdrawn identity.

This is a Located-Is-Not-Forced result in the charter's sense: the probe locates the norm-link's true dependency (spectral asymmetry of the generator) without claiming anything selects it.

## 7. What this means for the aliveness anchor's revival conditions (lane D §6)

- **Condition 1** (source-side, composition-compatible Z/2 label on extension morphisms): untouched — still open.
- **Condition 2** (issuance realizable on exactly one Krein sector, characterized J-flip-robustly and non-definitionally): **satisfiable, and satisfied here at toy grade — but shown to be non-load-bearing as written.** Any characterization meeting it consumes precisely the sector-asymmetry bit it was supposed to derive (orbit lemma), and the probability-conserving class in which "realizability" would be principled can never supply that bit (T-b, T-d). Honest strengthening: **2′ — derive the sector-asymmetric spectral condition itself from finality/issuance structure**, not merely exhibit dynamics that has it. Meeting 2 without 2′ cannot revive the anchor.
- **Condition 3** (not a restatement of "physical = positive-norm"): the definitional circle **is breakable** — `C_stab` genuinely is not a norm restatement — but breaking it buys nothing on its own: the circle is replaced by an unclosed reduction to energy positivity.

Net: the aliveness anchor stays parked; its one open door is now REDUCED rather than open-unexamined, and the revival burden is sharper and heavier (2′ plus the unchanged conditions 1 and 3, with the arrow route currently blocked at TaF's own grades).

## 8. Honest bounds

- **Finite-dimensional toy only** (n=4 real, n=2 complex). "Bounded below in one sector" is proxied by sector-sign of the restricted spectrum — an encoding-level statement, flagged as such; finite dimensions cannot express genuine unboundedness. (In real Krein spaces all fundamental-symmetry norms are equivalent — a known theorem — so the J-freeness of the boundedness verdict plausibly survives, but our proofs are finite-dimensional.)
- **`p = q` required** for the flip to be a symmetry. When `p ≠ q`, dimension already separates the sectors label-freely — but that is an accident of the space, not a norm-link, and the GU-relevant case (both sectors on equal footing) is the symmetric one.
- The orbit lemma's "every separator is flip-odd" is a group-theoretic tautology plus a finite instance battery — **not** a completeness theorem over all functionals in richer frameworks; but any richer structure that separates the orbit *is by definition* additional external data, which is the point.
- T-d generality: diagonalizable case; Jordan-degenerate `eta`-self-adjoint cases (polynomial growth on neutral subspaces) not certified.
- `C_stab`/`C_energy` were evaluated on sector-invariant (block-diagonal) generators; coupled non-self-adjoint generators whose maximal bounded subspace is not `eta`-definite were not explored (residual).
- Negative-leaning/reduction result, first-class under the Failure-Preservation Rule. No GU/TI/TaF claim moves.

Sources: `possibility-to-capability/governance/CHARTER.md`; `explorations/2026-07-16-big-swing/lane-D-aliveness-anchor.md` (+ governing referee report) and `SYNTHESIS.md`; `gu-formalization/explorations/time-as-finality-crosswalk/adapter2-correction-polarity-fiber-not-axis-2026-07-15.md`. Fixture: `tests/krein_norm_link_probe.py` at commit `96b96bc` (pushed to `main`), rerunnable, exit 0.

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs grades)

# Referee report — LANE 3-krein-normlink-probe

## 1. VERDICT: SOUND-WITH-CORRECTIONS

I re-ran the fixture from a clean checkout (`tests/krein_norm_link_probe.py` at `96b96bc`: commit exists, is on `main`, is pushed to `origin/main`, working tree matches the commit byte-for-byte, and the embedded source in the report matches the in-repo file line-for-line). Output reproduces **verbatim**, exit 0 — the "verbatim" claim, unearned in lane D (D7a), is earned here. I verified every source citation against the actual files: lane D §4/§6 revival conditions are characterized accurately; the ADAPTER2-01 attributions (fiber-not-axis, T18 conditional-constructor, T57 arrow-direction circularity open) match the correction document exactly (lines 73–75, 104–124); the charter's Located-Is-Not-Forced and Failure-Preservation rules are invoked correctly; no GU/TI/TaF claim moves and the withdrawn identity stays withdrawn. I re-derived T-a, T-a′, T-b, and T-d by hand (all correct; d3's non-real-eigenvalue construction is airtight: `|b| = |a−d|+1` forces discriminant `(a−d)² − 4|b|² < 0`, so 50 matrices × 2 = the reported 100 instances). The headline REDUCED verdict survives. The defects below are (i) a recurrence of the burned check-labeling class in attenuated form, and (ii) one genuine mathematical overclaim in candidate (b) that I refuted with an explicit counterexample — neither reaches the verdict, because the orbit lemma, not the mislabeled checks or T-b, carries the load.

## 2. Defects

**L1 — [E]-tagged checks that cannot fail for any candidate in their class. Severity: MODERATE (the burned class, recurring).**
The report's own discipline defines `[E]` as "genuine instance test whose outcome was not fixed at formalization time." Checks **c3, e2, c5, e3, and b2** violate that definition — each is a framework theorem, not an instance experiment. I confirmed adversarially (probe: `scratchpad/referee_probe_lane3.py`, **0 violations across 300 random generators for each**):

- **c3**: `S` is orthogonal and the Euclidean norm is `S`-invariant, so `sector_bounded(SAS, K+) = sector_bounded(A, K−)` identically; `C_stab(SAS) = S·C_stab(A)·S` holds for *every* `A` with the code's fixed sector menu. Two-line proof: `e^{tSAS} = S e^{tA} S`, `‖S x‖ = ‖x‖`, `S·(K+ basis) = K− basis`.
- **e2**: `(SAS)[0:2,0:2] = A[2:4,2:4]`, so `C_energy(SAS) = S·C_energy(A)·S` is an identity.
- **c5**: all four battery items are provable flip-even identities (similarity invariance of spectrum/trace; orthogonal invariance of the spectral norm; `S(A+A^T)S` isospectral to `A+A^T`). "The battery cannot separate" is a tautology the report itself states group-theoretically two bullets later — yet tags the check `[E]`.
- **e3**: the flip preserves eta-self-adjointness and spectrum-as-set for every eta-self-adjoint `H` (verified: 300/300).
- **b2**: `A_B_SYM + A_B_SYMᵀ = −2I` by construction (confirmed), so T-b fixes b2's outcome before the instance was chosen.

Mitigation, and why this is MODERATE not MAJOR: unlike lane D's D1, every *criterion* here has a demonstrated failing direction (c3-fail/e2-fail show `C_circ` failing the same test), the covariance lemma openly concedes robustness is "nearly free," and — as with D1 — the honest restatement is *stronger* (these are theorems). But the taxonomy the report advertises as its D1-learning is not applied consistently: five of its ten `[E]` tags belong on `[T]`.

**L2 — Candidate (b) conclusion is false as stated; refuted by counterexample. Severity: MODERATE.**
"**Candidate (b) fails the 'distinguishes at all' prong.** The only way to distinguish by realizability is unbounded behavior somewhere — which exits this class." Refuted: `A = diag(−1,−1,0,0)` is J-dissipative (in class (b)), `C_stab` is undefined on it (both sectors bounded, consistent with T-b) — but the realizability-flavored characterization `C_decay` (sector on which the semigroup strictly decays vs. stays isometric) **distinguishes the sectors inside the class, without unbounded behavior, and is J-flip-robust** (probe output: all four confirmations True). T-b proves only that *boundedness-based* realizability is sector-blind in class (b); it does not close the class to sector-asymmetric dynamics. Downstream, §6.2's "the probability-conserving class in which 'realizability' would be principled can never supply that bit **(T-b, T-d)**" survives only because the *orbit lemma* — not T-b — blocks `C_decay` too (my counterexample still consumes the orbit-member choice). The attribution must be corrected. Note T-d is not touched by this: for Krein-*unitary* (conserving, not merely contracting) evolution, real diagonalizable spectrum gives oscillation with no decay in either sector, so the d-section conclusion stands at its stated grade.

**L3 — "norm-free, hence J-free" overstates. Severity: MINOR.**
`C_stab`'s *verdict* is norm-free, but the characterization consumes the fundamental decomposition `{K+, K−}` — a J-derived object — as its candidate menu. It is *sign-of-J-free* (the unordered pair is flip-invariant, so no bit is smuggled and the non-circularity conclusion survives), not J-free simpliciter. The residual bound ("evaluated on sector-invariant generators only") partially covers this; the phrase does not.

**L4 — Two [F] checks are not failing directions of "the checker used above." Severity: MINOR.**
c2-fail exercises a *different functional* (matrix-norm threshold) on a *different matrix* (2×2), not the c2 checker (`sector_bounded` under `wnorm`) — which provably cannot fail across norms in finite dimensions. d1-fail likewise tests a different conserved quantity (Euclidean norm) than d1's checker (Krein form). Both establish non-vacuity of the surrounding property and both are honestly glossed in the text, but they stretch the `[F]` definition the report itself fixes.

**L5 — `sector_bounded` numerical failure mode unexhibited. Severity: MINOR.**
The checker decides boundedness by `sup < 10³` over `t ∈ [0,30]`; a slow-growth generator (eigenvalue ≈ 0.1 gives `e³ ≈ 20`) would be misclassified as bounded. No instance used is near the threshold (growth factors ≥ e^15 or genuine contraction), so no result is affected — but this checker got no [F] control for its own numeric failure mode.

**L6 — Modal overreach in §7. Severity: MINOR.**
"Meeting 2 without 2′ **cannot** revive the anchor" — at toy grade, backed by an orbit lemma the report's own §8 concedes is "a group-theoretic tautology plus a finite instance battery — not a completeness theorem over all functionals in richer frameworks." The definitional escape ("richer separating structure is by definition external data") makes the claim defensible, but only with the grade qualifier inline.

**L7 — Cosmetic/citation. Severity: TRIVIAL.**
(a) "REDUCED (option iii)" references an option menu that appears in no cited source (lane D §6 numbers *conditions* 1–3, not options i–iii); the tasking that defined the options is not in the repo. (b) "Krein-QFT spectral condition / energy positivity, operationally tied to the vacuum/arrow choice" and the "physics folklore" line are uncited background — flagged as folklore in the text, acceptable at exploration tier, but no frozen source backs them. (c) "bar(b)-grade" is an epistemic-grade analogy, not an imported identification — correctly hedged, worth keeping that way.

## 3. Corrected wording

- **For L1** (§1 discipline paragraph, add): "Five checks tagged `[E]` (b2, c3, c5, e2, e3) are in fact theorem-consequences — their outcomes are fixed for every candidate in their class by two-line identities (orthogonal invariance of the norm and similarity invariance of the spectrum for c3/c5/e2/e3; T-b for b2) — and are retagged `[T]`. The genuinely open instance content lives in a1/a2/c1/d0/d2/e1 and in the [F] controls, which demonstrate the criteria's failing directions on `C_circ`."
- **For L2** (§2(b), replace the bolded sentences): "**Candidate (b) fails the 'distinguishes at all' prong for boundedness-based realizability** (T-b: J-honest probability contraction is bounded on the whole space, so `C_stab` is undefined throughout the class). Sector-asymmetric dynamics does exist inside the class — e.g. strict decay on one sector, isometry on the other — and such a characterization is even flip-robust; but it purchases its selection from the same orbit-member bit as every other candidate (orbit lemma), so the class supplies distinction without supplying the bit."
- **For L2, §6.2** (replace "(T-b, T-d)"): "the probability-*contracting* class never selects by boundedness (T-b), the probability-*conserving* class puts its instabilities on the neutral cone (T-d), and any sector-asymmetric refinement inside either class still consumes the orbit-selection bit (orbit lemma)."
- **For L3**: "the boundedness verdict is norm-free, hence blind to the sign of `J` (it consumes only the flip-invariant unordered sector pair, not the label)."
- **For L6**: "at this grade, meeting 2 without 2′ carries no revival force: every characterization exhibited that meets 2 consumes the orbit bit, and the orbit lemma — tautological over the toy's functionals, unproven over richer frameworks — prices any richer separator as additional external data."

## 4. Grade the main result actually earns

**Finite-dimensional toy reduction with executable certificates, exploration tier, negative-leaning, no promotion** — specifically: "in the p=q toy, J-flip-robust and label-free characterizations of the issuance-supporting sector exist (`C_stab`, `C_energy` — robustness itself being a cheap covariance theorem, not a finding); every route to generating the sector asymmetry internally fails in a characterized way (eta-monotone class flip-odd = the sign posit restated; boundedness-based realizability sector-blind in the J-dissipative class; Krein-unitary instabilities neutral in the 2×2 diagonalizable case); and selecting between the two flip-orbit members costs exactly one external Z/2 bit, whose three toy-equivalent names include the sector-asymmetric spectral condition." That is the report's own claim minus: the candidate-(b) "distinguishes at all" universal (false — counterexample above), the `[E]` epistemic framing on five theorem-checks, and the unqualified "cannot revive" modal. The REDUCED verdict, the 2′ strengthening of lane D's condition 2, and the OPEN status of `bar(b)`/H59/Krein positivity/physical issuance all stand as written. It does **not** earn: any statement about infinite-dimensional Krein-QFT (correctly bounded), completeness of the orbit lemma over richer frameworks (correctly bounded), or any movement on source claims (none attempted).

## 5. Lane 1 GO / NO-GO

**N/A — this is lane 3.** The only file write involved (the fixture at `tests/krein_norm_link_probe.py`, commit `96b96bc`) is already executed, committed, and pushed; I verified the commit, the push state, the file-report identity, and the deterministic exit-0 run. No further writes are proposed by this lane.