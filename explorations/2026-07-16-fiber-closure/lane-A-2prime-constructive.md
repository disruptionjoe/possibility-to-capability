> Part of the 2026-07-16 fiber-closure swing (2-prime adversarial twins + T26 + tooling). Exploration tier; no claim promotion; the attached referee report GOVERNS the grades — read it before citing the lane report.

> Adversarial-twin lane: CONSTRUCTIVE direction on condition 2′. Exploration tier; no claim promotion; the referee stage (if run) governs grades.

---

# P2C — Condition 2′, constructive attempt: derive the sector-asymmetric spectral condition from finality/issuance structure

Tier: exploration. Grade: **finite-dimensional toy with executable certificates; negative-leaning; first-class under the Failure-Preservation Rule.** No source claim moves. `bar(b)`, H59, Krein positivity, physical issuance: **all remain OPEN**. Nothing here reopens the withdrawn `bar(b) = finality-axis polarity` identity (ADAPTER2-01 governs). Fixture persisted in-repo: `possibility-to-capability/tests/condition2prime_constructive_probe.py`, commit `a193a3b` (pushed to `main`), deterministic exit 0.

## 0. VERDICT: **FAILED-ALL-ATTEMPTS** — characterized per attempt, with three new bounding byproducts

I attempted the three tasked constructions plus a systematic search for the escape premise. Every attempt satisfies conditions (i) source-side and (ii) composition-compatible, and every attempt's selector is J-flip-robust in the covariance sense — and **every attempt delivers only the flip-orbit of a sector, never a member**. The consumption point is exhibited exactly, per attempt, and a sharply-hypothesized "equivariance wall" statement (Section 5) makes the twin comparison mechanically decidable. This feeds the twin no-go lane as intended.

**Honesty receipts up front:** all expected values were written into the fixture before the first run; the first run passed with zero deviations (no post-run expectation revision occurred). Check census: 17 [T] (theorem-certificates, no evidential weight, listed as such), 9 [E], 6 [F]; every [F] exercises the same checker code path it protects (comparator, admissibility, functoriality, robustness criterion, monotonicity, parity-functor — one each, named inline). The headline rests on proofs certified by [T] checks plus [F]-verified checker teeth, not on [T] counts as evidence.

## 1. Setup (shared)

Krein toy as in lane 3 (`96b96bc`): `K = R^4`, `eta = J = diag(+,+,−,−)`, sectors `K±`, swap `S` (orthogonal involution, `S eta S = −eta`); the global flip (form → −form, `J → −J`, labels swapped) acts in standard coordinates as `A → SAS`. Robust selector criterion: `C(SAS) = S·C(A)·S`; label-reader: `C_circ ≡ K+`.

Source side (TI RUN-0019 survivor vocabulary): constraint states = consistent finite literal sets, extension chains monotone under inclusion (`Ext_S`-shaped); the fork flip negates all literal values. Composition-compatibility target: E160's positive shape — the label carried by admissibility must itself be functorial under extension composition; a supplied table is extra data (case 4), an inconsistent table is not a functor (case 5).

## 2. Attempt 1 — irreversibility-as-spectrum

**Construction.** Extension chain `∅ ⊂ {p+} ⊂ {p+,q+} ⊂ {p+,q+,r−,s+}`; morphism label `τ(e) = record growth` (additive under composition — the E160 shape); representation `R(e) = e^{τ(e)A}` with `A1 = diag(−1,−2,1,0.5)`. Then: forward transport is realizable (bounded) on exactly `K+` (a1-2, [E]); **time-reversed** transport is realizable on exactly `K−` (a1-3, [E]) — so, given the representation, the selected sector is a genuine function of the arrow. The arrow is issuance-real in-model: reversal of any strictly-growing chain is rejected by the admissibility checker (s3, [T]; [F] s2-fail shows the checker has teeth; s3b honestly shows constant chains reverse freely; physical arrow grade stays TaF-conditional — T18 conditional-constructor, T57 circularity open, stated, not papered over).

**Where it breaks: orbit-bit consumption, exhibited.** The S-twin representation `R'(e) = e^{τ(e)·SA1S}` satisfies the *entire* issuance-native constraint list — functorial (same τ, same chain), forward-realizable-on-exactly-one-sector, reverse-on-the-other (a1-5, [T]: every constraint used is flip-stable) — and selects the swapped sector (a1-6). The flip-even battery cannot separate `A1` from its twin (a1-7); `C_circ` fails robustness on the same instance (a1-8, [F]). Crucially (a1-4, [T]): **the source discriminates time-reversal twins (reversed chain inadmissible) but is literally blind to sector twins (the twin's source chain is the identical accepted chain — `S` acts on the target only).** Conditions (i) and (ii): satisfied. Condition (iii): the selector is robust, but non-definitionality fails at the class level — choosing `R` over `S·R·S` is one external Z/2.

**Byproduct 1 (new, bounding): the arrow bit and the sector bit are independent Z/2 degrees of freedom at representation level.** The base asymmetry (extension direction) pays for the T-twin ambiguity and cannot touch the S-twin ambiguity, because the two Z/2s act on different data (source vs target). Corollary at this grade: **even a completed TaF physical arrow (T57 resolved) would not close condition 2′** — the selected sector is a joint function of (arrow bit, orbit bit), and deriving the first leaves the second free. This sharpens lane D's base-vs-fiber diagnosis: transport fails not for lack of a base asymmetry but because the base asymmetry is flip-even.

## 3. Attempt 2 — record-count monotone as spectral functional

**Construction.** Four issuance channels with monotone record counts; growth functional `Q` = per-channel rates (RUN-0028's `Q: Mor → [0,∞)` shape; note honestly: whether `Q` can be *source-defined* is itself TI-open — even granting it, the attempt fails). Generator `H = diag(Q)`.

**Where it breaks: before condition (iii) — growth alone yields no asymmetry at all.** **Growth-blindness theorem (a2-2, [T], two lines):** monotone issuance forces `Q ≥ 0` uniformly across channels, so the restricted spectrum is positive on *both* sectors and `C_energy` is undefined. The exact property that makes the functional issuance-native (positivity via monotonicity) is the property that makes it sector-blind — positivity cannot land on one sector because it lands on all of them. Asymmetry appears only after coupling growth to the form: `H_eta = eta·diag(Q)` selects `K+` (a2-3, [E]), robustly (a2-4, [T] covariance) — **and the orbit-lemma question the task requires asking is answered YES: the flip-orbit twin `S·H_eta·S` is built from the SAME growth data, is equally admissible (eta-self-adjoint, same spectrum-as-set), and the only separator found is the flip-odd label-reader `trace(JH)`** (a2-5, [T]). The insertion point is exactly the coupling coefficient `eta` vs `−eta` — the bit. The variant "Krein-norm rate = +growth" (eta-expansive class, instance `A = eta`) is flip-odd — lane 3's T-a′, the sign posit restated (a2-6, [T]; its selection `C_stab(eta) = K−` is made oppositely by the twin, a2-7 [E]).

## 4. Attempt 3 — fork-resolution asymmetry

**Construction.** SBP fork `∅ → {p+}` vs `∅ → {p−}`; both branches admissible and extendable (s2, [E]). "The realized branch" is genuinely source-side (`Ext_S` data). To turn it into a sector it needs an alignment map literal → sector.

**Where it breaks: (ii) and (iii) jointly — per-history relabeling plus imported transport.** Exhaustive enumeration (a3-1, [T]): exactly **two** flip-equivariant alignment maps exist — choosing between them is the bit — and the two non-equivariant maps are the constant label-readers (`C_circ` in disguise). Under either alignment, history `h+` selects `K+` and `h−` selects `K−`, while `flip(h+)` is structurally identical to `h−` (same label-free fingerprint): same physics, opposite selection — **the D3 trap confirmed executably: realized-branch selection is per-history relabeling and induces nothing global** (a3-2, [E]). Globalization across forks requires a coherent Z/2 transport table; a consistent table exists but is not unique (trivial and twin tables both pass the parity-functor checker — E160 case 4: imported data, one bit per block), and an inconsistent table fails the same checker (a3-4 [T], a3-5 [F]). Block structure matches lane-2 N4: unlinked propositions give independent selection blocks (`(Z/2)^2`), an XOR link merges them, never to zero (a3-3, [E]) — fork realization never reduces the fiber below one bit per component.

## 5. The equivariance wall (the derived statement; sharp boundaries for the twin comparison)

**Statement (toy grade).** Hypotheses:

- **(H1)** the fork flip acts on the source structure by isomorphisms (certified here: label-free fingerprint invariance, s1; the [F] control s1-fail shows the comparator can fail);
- **(H2)** every constraint defining the admissible representation/generator class is flip-stable (invariant under `A → SAS`);
- **(H3)** the sector selection is a covariant/natural function of (source data, representation).

Conclusion: the selection delivers, for each admissible derivation, only the unordered orbit `{sector, S-swapped sector}`; picking a member costs exactly one external Z/2 **per transport block**. Certified across all three attempts' generators in one loop (m1, [T]).

**Mechanical membership test for any claimed construction** (per adversarial-twin protocol): (1) does the flip permute its source models preserving its own structural fingerprints? (2) is each stated admissibility constraint invariant under `A → SAS`? (3) does its selector satisfy `sel(SAS) = S·sel(A)·S`? Three yeses → the wall applies → the construction consumed the bit; demand the insertion point. A genuine condition-2′ construction must violate exactly one of H1–H3, and each violation route carries a named burden:

- **H1 escape** — a source structure on which the fork flip is *not* an isomorphism. I searched: TaF D1 profiles are sign-blind (ADAPTER2-01: "opposite proposition values still have the same D1 profile"); growth/count data is sign-blind; the arrow is flip-even (lane D check 4). **Byproduct 3 (new):** there *does* exist a genuinely asymmetric Z/2 on source structure — **edge negation** (all-relative-polarity negation): the balanced triangle is satisfiable, its all-edges-negated twin is not (odd-cycle frustration; s4, [E]) — but the fork flip (vertex/value negation) preserves every edge constraint (s5, [T], exhaustive), so **the asymmetric Z/2 and the fiber Z/2 are different groups acting on different data**: anything built from relative-polarity/constraint-graph structure is flip-even and cannot separate the fork orbit. This bounds a whole family of future attempts. At current TI/TaF grades, no H1-escaping source structure exists.
- **H2 escape** — a flip-odd admissibility constraint. Then the construction owes a proof that the constraint is not the sign posit restated; the two flip-odd classes exhibited here (eta-contractive, eta-expansive) are both exactly that (lane 3 T-a/T-a′; a2-6).
- **H3 escape** — a non-natural selector. Exhibited failure mode: presentation-dependence = label-reading; `C_circ` fails robustness (a1-8, a3-1's constant maps).

**Residual (not closed by this lane):** lane 2's referee F3 hiding place — TaF's actual T26 `D1RestrictionSystem` overlap/patch machinery — is not modeled here; my a3-4 table-nonuniqueness is consistent with, but does not decide, whether native patch constraints force a unique transport. That remains the program's ranked item 1.

## 6. Honest bounds

- Finite-dimensional toy (`R^4`, p = q); "bounded below on one sector" proxied by sector-sign of restricted spectrum (encoding-level, flagged). `sector_bounded` numeric failure mode disclosed in-source (growth rates < ~0.23 over t ≤ 30 misclassified; all instances used are ≥ e^15 from threshold).
- The wall is a covariance/orbit statement over the toy's functionals plus exhaustive-finite enumerations — not a completeness theorem over richer frameworks; per lane 3's pricing, any richer separator is by definition additional external data, and per H2 it then owes the not-the-posit proof.
- In-model arrow is posited by construction (monotone chains); physical arrow stays TaF-conditional (T18/T57) — stated wherever used.
- `Q`'s source-definability is TI-open (RUN-0028); attempt 2's failure is unconditional on that (it fails even granting it).
- FAILED-ALL-ATTEMPTS is first-class under Failure-Preservation; no GU/TI/TaF claim moves; ADAPTER2-01 untouched.

## 7. Code (full source; canonical in-repo at `tests/condition2prime_constructive_probe.py`, commit `a193a3b`)

```python
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
```

## 8. Output (verbatim, exit 0, first run)

```
CONDITION 2' CONSTRUCTIVE PROBE (adversarial-twin lane)
==========================================================================
PASS  [T] setup: S eta S = -eta and S is an orthogonal involution: True
PASS  [T] s1: the fork flip is a source AUTOMORPHISM: label-free fingerprint invariant (lane-D framework theorem; instance cert.): True
PASS  [F] s1-fail: a sign-READING fingerprint (+1-literal count) is NOT flip-invariant on the same model (comparator can fail): False   (failing direction: checker CAN fail)
PASS  [E] s2: SBP fork instance: both branches admissible and extendable (h+ and h- pass the issuance checker): True
PASS  [F] s2-fail: a record-DROPPING chain is rejected by the same admissibility checker: False   (failing direction: checker CAN fail)
PASS  [T] s3: every strictly-growing chain's reversal is rejected -- the in-model arrow is real (two-line: strict growth breaks reverse inclusion; physical grade stays TaF-conditional, T18/T57): True
PASS  [T] s3b: a constant (no-issuance) chain's reversal is ACCEPTED -- the arrow lives in strict extensions only (rejection not vacuous): True
PASS  [E] s4: EDGE negation is a genuinely asymmetric Z/2 on the source: balanced triangle satisfiable, all-edges-negated triangle NOT (odd-cycle frustration): True
PASS  [T] s5: the FORK flip (vertex/value negation) preserves EVERY edge constraint (exhaustive over 8 assignments x both constraint sets): the asymmetric Z/2 is not the fiber Z/2: True
PASS  [T] a1-1: R(e) = exp(tau(e) A) is composition-compatible on the extension chain (additive label + exponential law; E160 shape (ii)): True
PASS  [F] a1-1-fail: the non-additive label tau^2 BREAKS the same functoriality checker: False   (failing direction: checker CAN fail)
PASS  [E] a1-2: forward transport realizable on exactly one sector: C_stab(A1) = K+ (instance chosen to have the property; disclosed): True
PASS  [E] a1-3: TIME-reversed transport realizable on the OTHER sector: C_stab(-A1) = K- (the arrow choice moves the selection): True
PASS  [T] a1-4: the arrow is issuance-discriminated but the S-twin is not: reversed source chain REJECTED, twin's source chain is the IDENTICAL accepted chain (S acts on the target only): True
PASS  [T] a1-5: the S-twin representation satisfies the ENTIRE constraint list (functorial; forward one-sector; reverse other-sector) -- every constraint is flip-stable: True
PASS  [T] a1-6: twin selects the SWAPPED sector: C_stab(S A1 S) = S K+ S = K- (covariance identity): True
PASS  [T] a1-7: flip-even battery cannot separate A1 from its twin (eigenvalue moduli, trace, ||e^{2A}||, J-dissipativity -- each item a similarity/orthogonal-invariance identity): True
PASS  [F] a1-8: the circularity control C_circ FAILS flip-robustness on the same instance (label-reader; same same_proj criterion path): False   (failing direction: checker CAN fail)
PASS  [E] a2-1: the 4-channel issuance model is monotone (records accumulate) with strictly positive growth rates: True
PASS  [F] a2-1-fail: a shrinking channel is rejected by the same monotonicity checker: False   (failing direction: checker CAN fail)
PASS  [T] a2-2: THEOREM (growth blindness): the growth-built generator H = diag(Q) has positive restricted spectrum on BOTH sectors, so C_energy is UNDEFINED -- monotone issuance forces Q >= 0 uniformly; positivity cannot land on one sector: True
PASS  [E] a2-3: the eta-COUPLED generator H = eta diag(Q) selects K+ (sector asymmetry appears only after coupling growth to the form): True
PASS  [T] a2-4: C_energy on H_eta is J-flip-robust (covariance identity: C_energy(S H S) = S C_energy(H) S): True
PASS  [T] a2-5: ORBIT CONSUMED -- the flip-orbit twin S H_eta S is built from the SAME growth data, is equally admissible (eta-self-adjoint, same spectrum-as-set), and the only separator found is the flip-odd label-reader trace(J H): True
PASS  [T] a2-6: the 'Krein-norm rate = +growth' variant (eta-expansive class, instance A = eta) is flip-ODD: S(eta)S = -eta is eta-CONTRACTIVE -- the sign posit restated (lane-3 T-a'): True
PASS  [E] a2-7: and its realizability selection C_stab(eta) = K- is again a selection the twin makes oppositely: C_stab(-eta) = K+: True
PASS  [T] a3-1: exhaustive enumeration: exactly TWO flip-equivariant alignment maps literal->sector exist (the bit), and the two non-equivariant maps are the constant label-readers: True
PASS  [E] a3-2: PER-HISTORY RELABELING: h+ selects K+, h- selects K- under the same alignment, and flip(h+) is structurally identical to h- (same fingerprint) -- same physics, opposite selection: True
PASS  [E] a3-3: BLOCK STRUCTURE: two unlinked propositions give 2 independent selection blocks ((Z/2)^2 fiber, lane-2 N4 shape); an XOR link merges them to 1; never 0: True
PASS  [T] a3-4: a CONSISTENT Z/2 transport table exists but is not unique: both the trivial and the twin table pass the parity functor checker -- choosing one is imported data (E160 case 4): True
PASS  [F] a3-5: an INCONSISTENT transport table fails the same parity functor checker (E160 case-5 analog): False   (failing direction: checker CAN fail)
PASS  [T] m1: EQUIVARIANCE WALL certified on every attempt's generator: sel(S A S) = S sel(A) S -- each attempt's selector is covariant, so each derivation chain delivers an ORBIT, never a member: True

CHECK CENSUS: 17 [T] theorem-certificates (no evidential weight), 9 [E] instance tests, 6 [F] controls.
All checks match pre-declared expectations. Exit 0.
```

## 9. Summary for the head-to-head comparison

| Attempt | (i) source-side | (ii) composition-compatible | (iii) robust non-definitional | Consumption point |
|---|---|---|---|---|
| 1 arrow → spectrum | YES (`Ext_S` chains) | YES (additive τ, functorial) | robust, but orbit-bit consumed at representation choice | `R` vs `S·R·S`: identical source, identical constraints, swapped selection |
| 2 growth → spectrum | conditional (`Q` source-definability TI-open) | YES | never reached asymmetry: growth-blind theorem; asymmetry only via `eta`-coupling | coupling coefficient `±eta` = the bit; flip-orbit twin has EQUAL RIGHT (said explicitly) |
| 3 fork realization | YES (realized branch is `Ext_S` data) | NO without imported table (E160 case 4); blocks don't cohere | per-history relabeling (D3 trap confirmed) | one of exactly two equivariant alignments = the bit, per block |

**What the twin no-go lane may take:** the equivariance wall with hypothesis class H1–H3 (Section 5), the mechanical membership test, the arrow-bit/sector-bit independence result (even a resolved TaF arrow leaves condition 2′ open at this grade), the growth-blindness theorem, and the two-Z/2 separation (the one genuinely asymmetric source Z/2 — edge negation/frustration — is provably not the fiber Z/2). **What no construction was found to escape:** H1 has no known TI/TaF-native violation; H2 violations exhibited are the sign posit restated; H3 violations are label-readers. Residual not closed: TaF T26 native patch/overlap machinery (lane-2 F3) — unmodeled here, still the last hiding place.

Fixture: `tests/condition2prime_constructive_probe.py`, commit `a193a3b`, pushed to `origin/main`, rerunnable, exit 0.

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs grades)

All probes complete. I have everything needed for the verdict.

---

# Referee report — LANE A-2prime-construct (condition 2′, constructive twin)

## 1. VERDICT: **SOUND-WITH-CORRECTIONS**

Reproduction and provenance are fully earned: commit `a193a3b` exists, is on `main`, is pushed to `origin/main`, the working tree is clean, the embedded source matches the in-repo file and the commit byte-for-byte, and the run reproduces the reported output **verbatim**, exit 0, including the census line. Cross-citations verified against the actual files: the ADAPTER2-01 quote ("opposite proposition values still have the same D1 profile") is verbatim at `adapter2-correction-polarity-fiber-not-axis-2026-07-15.md` lines 69–70; T18-conditional/T57-open attributions match; lane-D "checks 4" (arrow is flip-even, label-independent) matches lane-D §269; lane-2 referee F3 is quoted accurately (TaF T26 `D1RestrictionSystem` overlap/patch machinery unmodeled — and this lane honestly does **not** model it, so the T26 encoding-vs-formalism question is N/A here and correctly carved out as the residual); E160's case-4 ("a supplied transport table... remains extra data") and case-5 (inconsistent labels not a functor) match; RUN-0019 `SourceRealization = (C, <=_S, Ext_S)` and RUN-0028 `Q: Mor(ExtCat) -> ([0,∞),+)` match TI's files. No ADAPTER2-01 contradiction; no source claim moves; the withdrawn identity stays withdrawn. I re-derived the wall covariance argument, a1-4/a1-7, a2-6, a3-1, s3, s5 by hand — all correct. **But I refuted one exported "theorem" by counterexample inside the lane's own admissible class, and the burned check-labeling class recurs**, so the grades below govern.

## 2. Defects

**C1 (MODERATE) — The "growth-blindness theorem" (a2-2) is false as stated; refuted by counterexample.** Stated: "monotone issuance forces Q ≥ 0 uniformly, so the restricted spectrum is positive on *both* sectors and `C_energy` is undefined... positivity cannot land on one sector." Monotone issuance forces only `Q ≥ 0`, not `Q > 0`. Probe (re-run against the lane's own functions): `COUNTS_ZERO` with rates `Q = (1,1,0,0)` passes `monotone_counts` (the lane's own admissibility predicate; s3b even certifies zero-issuance as admissible), yet `c_energy(diag(Q)) = K+` — **defined**, no η-coupling. The two-line proof has a hole (it needs strict positivity on every channel, which a2-1 checks for the chosen instance but the class does not force). Downstream: the *verdict* survives, because the wall covers the counterexample (verified: `c_energy(flip) = K−`, covariance holds) and the selection rides entirely on the channel→sector assignment — i.e., attempt 3's alignment bit relocated, not escaped. But the summary-table row ("never reached asymmetry... asymmetry only via eta-coupling") and the exported byproduct ("the growth-blindness theorem" in §9's take-list for the twin) are false in letter. The twin no-go lane must not import it unrepaired.

**C2 (MODERATE) — [E]-census inflation: the burned check-labeling class recurs (lane-3 L1 pattern).** Of 9 checks tagged `[E]`, roughly six have outcomes fixed at formalization time: **a2-3** (probe: `c_energy(η·diag(Q)) = K+` for 300/300 random strictly positive Q — a class theorem, exactly the retagged-b2 pattern), **a2-7** (η is canonical, not a chosen instance; outcome computable in one line), **a3-2** (worst case: `flip_chain(H_PLUS) == H_MINUS` is *literal object identity* — probe confirms — so the fingerprint clause compares an object with itself and cannot fail for any model; the alignment clauses just read the map's definition), **a3-3** (union-find on two nodes; definitional), **s4** (classical odd-cycle-frustration/Harary theorem, fixed before any run), **s2** (fixed for every single-literal fork by trivial consistency). The genuinely open instance content is a1-2/a1-3/a2-1 (chosen-instance, disclosed — acceptable per the swing-2 precedent the docstring cites) plus the [F] controls. The honesty receipt "9 [E]" therefore overstates the instance-test count; the headline does not rest on it (it rests on proofs + the wall), which is why this is MODERATE, not MAJOR — but the taxonomy advertised as the lane's swing-2 learning is again not applied consistently.

**C3 (MODERATE) — H1 universal negative graded above evidence.** "At current TI/TaF grades, no H1-escaping source structure exists" is a universal over source structures, supported by a finite search of three named families (D1 profiles, growth/count data, the arrow) plus the edge-negation separation (s4/s5 — which is sound and genuinely bounding). The evidence supports "none found among the families searched"; nonexistence is not established at any grade. The mechanical membership test does not repair this: it tests *offered* constructions, it does not enumerate source structures.

**C4 (MINOR) — Blanket [F] same-code-path claim stretched for s1-fail (lane-3 L4 pattern).** The receipt says "every [F] exercises the same checker code path it protects." `s1-fail` runs `signed_fingerprint` — a *different function* from `fingerprint`; only the `==` comparison is shared (the inline name "comparator" hedges exactly this). Probe: `fingerprint` flip-invariance is a cannot-fail framework theorem (0 violations / 300 random models), so the checker s1 actually uses is never exhibited failing and provably cannot fail. s1 is honestly tagged [T]; the blanket receipt sentence is what overreaches. The other five [F]s genuinely share their checker's code path (verified: `admissible_chain`, `functorial`, `same_proj`-criterion, `monotone_counts`, `parity_functorial`).

**C5 (MINOR) — "Makes the twin comparison mechanically decidable" overstates for H2.** Membership steps (1) and (3) are mechanically checkable on finite models/instances. Step (2) — flip-stability of *every stated admissibility constraint* — is a universally quantified property over generators; in this lane it is discharged by hand proofs (correct ones), and m1 certifies covariance on exactly three generators. For an arbitrary future construction, H2 is a proof obligation, not a decision procedure. The boundaries are mechanically decidable *for the constraint classes exhibited*, which is what the pair adjudication needs — but say that, not more.

**C6 (MINOR) — Unverifiable process claims.** "All expected values were written into the fixture before the first run; the first run passed with zero deviations" and "I attempted... plus a systematic search" are single-commit process claims with no auditable artifact separating pre-run from post-run state. Fine to assert, but they are not receipts and should not be labeled "honesty receipts" as if artifact-backed.

**C7 (MINOR) — a2-5's "insertion point is exactly ±η" is imprecise, and "the only separator found" is a one-item search.** Probe: the certified twin `S·H_η·S = diag(−2.5,−0.5,2,1)` is **not** the literal same-assignment coupling twin `−η·diag(Q) = diag(−2,−1,2.5,0.5)`; the latter has a *different* spectrum-as-set. The S-twin differs from `H_η` by −η coupling **plus** the S-permutation of channel→basis assignment. "Built from the SAME growth data" is defensible only with the assignment-swap made explicit — at which point the insertion point is the (coupling sign, channel alignment) pair, whose alignment half is attempt 3's bit. Also, only `trace(JH)` was tested as a separator; "only separator found" should read "the one separator exhibited."

**C8 (TRIVIAL) —** (a) "all instances used are ≥ e^15 from threshold": the sup *reaches* e^15; the margin over the 10³ threshold is a factor ≈ e^8 (3269×). No result affected (threshold-rate ~0.2303 confirmed matches "~0.23"). (b) "three new bounding byproducts" but only Byproducts 1 and 3 are labeled; the unlabeled second is precisely the defective a2-2 theorem. (c) 17/9/6 census arithmetic confirmed correct.

**Verified clean (hunted, not found):** no [T] counted as evidence for the headline (the header disclaimer is honored in the argument structure); no source-sovereignty violation (fixture lives in P2C's own `tests/`; GU/TI/TaF untouched); no ADAPTER2-01 contradiction (fiber-not-axis picture is reinforced, arrow stays TaF-conditional everywhere it is used); no encoding-level fact passed off as T26 formalism-level fact (T26 is explicitly unmodeled and named as the residual — consistent with lane-2 F3 verbatim); a3-1's enumeration boundary (maps into the two-projector menu) is stated and decidable; s3b is a genuinely honest anti-vacuity disclosure.

## 3. Corrected wording

- **a2-2 / headline of attempt 2 (for C1):** "Growth-blindness, corrected scope: for issuance models with *strictly positive growth on every channel*, `H = diag(Q)` has positive restricted spectrum on both sectors and `C_energy` is undefined. Monotone issuance alone forces only `Q ≥ 0`: with zero-growth channels, `C_energy(diag(Q))` **can** be defined (e.g. `Q = (1,1,0,0)` selects K+) — but the selection is then carried entirely by the channel→sector assignment, i.e. attempt 3's alignment bit relocated, and remains wall-covariant. Either way, growth data never pays for the bit; it pays for it least visibly in the strictly-positive case."
- **§9 table row 2:** "conditional (`Q` source-definability TI-open) | YES | strictly-positive case: no asymmetry at all (growth-blind); zero-growth-channel case: asymmetry appears but rides the channel→sector alignment bit; η-coupling case: rides the coupling-sign bit | the bit enters as (coupling sign × channel alignment); the flip-orbit twin has equal right."
- **Census sentence (for C2):** "9 [E]" → "3 [E] chosen-instance tests (a1-2, a1-3, a2-1; choices disclosed) and 6 further checks previously tagged [E] that are in fact theorem- or definition-fixed (s2, s4, a2-3, a2-7, a3-2, a3-3), retagged [T]; a3-2's fingerprint clause is object identity (`flip(h+)` *is* `h−`), which strengthens the same-physics claim and empties the check."
- **H1 sentence (for C3):** "At current TI/TaF grades, no H1-escaping source structure exists" → "No H1-escaping source structure was found in the families searched (D1 profiles, growth/count data, the extension arrow, relative-polarity/constraint-graph data); byproduct 3 bounds the last family. Nonexistence over TI/TaF source structures is not established at any grade."
- **[F] receipt (for C4):** "every [F] exercises the same checker code path it protects" → "five of six [F]s exercise the same checker function they protect; s1-fail exercises only the shared comparison against a deliberately sign-reading fingerprint, because s1's own fingerprint invariance is a cannot-fail framework theorem (hence s1's [T] tag)."
- **Section 0/5 (for C5):** "makes the twin comparison mechanically decidable" → "makes the twin comparison mechanically checkable for any offered construction: H1 and H3 are decidable on finite models/instances; H2 is a per-constraint proof obligation, discharged here for every exhibited constraint class."

## 4. Grade the main result actually earns

**Finite-dimensional toy, executable certificates, negative-leaning, exploration tier, no promotion — FAILED-ALL-ATTEMPTS stands.** Specifically earned: (i) all three constructions consume the orbit bit at an exhibited insertion point, with the a1 consumption point (source blind to S-twins because S acts on the target only) proved cleanly; (ii) the equivariance wall as a covariance *schema* with hypothesis class H1–H3, certified on three generators, tautological over the toy's functionals, not a completeness theorem — as the lane itself prices; (iii) byproduct 1 (arrow-bit ⊥ sector-bit at representation level, so a resolved TaF arrow would not close 2′ *at this grade*) stands; (iv) byproduct 3 (edge-negation Z/2 ≠ fork-flip Z/2; anything flip-even built from relative-polarity data cannot separate the orbit) stands and is the lane's best new bounding result. **Not earned as stated:** the growth-blindness theorem (needs the strict-positivity hypothesis; the zero-rate counterexample is inside the lane's own admissible class and relocates rather than removes the bit); the H1 nonexistence universal (search-bounded only); the "9 [E]" instance-census; "mechanically decidable" for H2. The residual (TaF T26 native patch machinery as the last hiding place) is honestly preserved and remains ranked item 1.

## 5. Implication for the OTHER twin (2′ no-go lane) — for pair adjudication

This lane's corrected result predicts the no-go twin should be able to prove, at the same toy grade, exactly: *under H1–H3, every derivation delivers the unordered flip-orbit, never a member, at one external Z/2 per transport block.* The pair is **consistent** iff the no-go lane's impossibility statement carries **exactly the H1–H3 hypothesis class and the toy's scope** — no more, no less. Mechanical conflict tests for the orchestrator:

1. **Hypothesis match:** if the no-go twin claims impossibility *without* assuming H2 (flip-stable constraints) or H3 (natural selector), it overclaims — this lane exhibits that flip-odd constraints (a2-6) and label-readers (a1-8, a3-1's constant maps) *do* select, at the price of restating the posit. Its theorem must leave those escape routes open as priced, not excluded.
2. **Growth-functional clause:** if the no-go twin asserts "no growth/issuance-built selector is ever defined" (the uncorrected a2-2 shape), it inherits my counterexample: `Q = (1,1,0,0)` yields a defined, wall-covariant `C_energy` whose bit lives in the channel→sector alignment. The correct joint statement is "defined or undefined, any growth-built selector is wall-covariant, so it prices the alignment/coupling bit; it never derives the member."
3. **Scope match:** the no-go twin may not claim more than the wall — i.e., nothing about richer-than-toy frameworks except the definitional pricing move ("a richer separator is by definition additional external data"), and nothing about H1-escape *nonexistence* (this lane only establishes none-found plus the byproduct-3 bound on relative-polarity structures).
4. **Expected joint verdict if both hold:** constructive twin FAILED-ALL + no-go twin proving the wall under H1–H3 = a coherent pair locating condition 2′'s obstruction at the (arrow ⊥ sector) independence, with exactly three named escape routes, each carrying a burden; T26 native patch machinery remains the sole unadjudicated hiding place *for this pair* (a later commit, `6ed76a5`, purports to address it — outside this lane's scope and not usable to support either twin here).

Files: report subject fixture `C:/Users/joe/JB/CapacityOS/repos/public/possibility-to-capability/tests/condition2prime_constructive_probe.py` (commit `a193a3b`, verified); referee probe `C:/Users/joe/AppData/Local/Temp/claude/C--Users-joe-JB/38a54106-9cc3-428a-92e4-2bb753410f40/scratchpad/referee_probe_2prime_construct.py` (counterexample and re-derivations, all outputs quoted above).