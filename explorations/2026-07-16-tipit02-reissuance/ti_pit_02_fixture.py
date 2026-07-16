#!/usr/bin/env python3
"""TI-PIT-02 paired-intervention fixture, draft v0.2 (DRAFT-FOR-SOURCE-ISSUANCE).

Finite instance of Temporal Issuance's OnlineIssuance^LC signature, quoted
exactly from TI FORMAL-OBJECT.md RUN-0081:

    OnlineIssuance^LC =
    (
      Gamma_n,     prefix-presented constructive context
      Adm_n,       admissibility predicate formed at prefix n
      Ext_n,       witness-bearing extension category available at n
      Iss_n,       source extension step
      Proj_{o,n},  observer projection/readout
      Glue_n,      downstream reconciliation/finality operation
      tau_n        recordable source trace
    )

Instantiation map (which components are instantiated vs trivialized):
  Gamma_n     INSTANTIATED: set of issued tokens; Gamma_0 = {"a"}.
  Adm_n       INSTANTIATED: Adm_k(e) <=> e not in Gamma and |e| <= MAXLEN
              and #b(e) <= k (admissibility parameter k).
  Ext_n       TRIVIALIZED: the witness-bearing extension category is
              represented by the finite set of pairs (e, w) with
              e in CandExt(Gamma_n) = { t+c : t in Gamma_n, c in {a,b} }
              (the gate-clause candidate object) and w an explicit
              admissibility witness record; no nontrivial categorical
              structure (morphisms, composition) is exercised.
  Iss_n       INSTANTIATED: issue ALL admissible candidates, deterministic,
              sorted order.
  Proj_{o,n}  INSTANTIATED: length-threshold readout; the observer receives
              exactly the trace events whose token length <= L. Witness
              fields are functions of the token and prior context alone
              (k-free), so carrying them through the projection leaks
              nothing about k.
  Glue_n      PRESENT IN THE SIGNATURE, NOT EXERCISED: single observer;
              reconciliation is identity. Declared, not dropped.
  tau_n       INSTANTIATED: ordered event list (stage, token, w) with the
              admissibility witness w carried as an explicit per-event
              field (RUN-0081 gate clause 2: w_n : Adm_n(e_n)).

Check discipline: every check is tagged [T]/[E]/[F] per the receiving repo's
house rule (tests/tef_check_tag_linter.py). [T] = holds by construction, no
evidential weight; [E] = genuine experiment; [F] = failing-direction control
proving the checker it protects has teeth on the same code path.
"""

from itertools import product

ALPH = "ab"
N_STAGES = 4
MAXLEN = 4
HYP = [0, 1, 2, 3]


def witness(e, gamma):
    """k-free admissibility witness data for candidate e at the current prefix.

    w = (novel, length, b_count). For parameter k, w certifies Adm_k(e)
    exactly when novel and length <= MAXLEN and b_count <= k. The record is
    a function of (e, gamma) alone, so it carries no information about k.
    """
    return (e not in gamma, len(e), e.count("b"))


def run_system(k, n_stages=N_STAGES, maxlen=MAXLEN):
    """Deterministic issuance run; trace events are (stage, token, w)."""
    gamma = {"a"}
    trace = []
    stage_counts = []
    for n in range(1, n_stages + 1):
        cands = sorted({t + c for t in gamma for c in ALPH})
        issued = []
        for e in cands:
            w = witness(e, gamma)
            novel, length, b_count = w
            if novel and length <= maxlen and b_count <= k:
                issued.append((e, w))
        trace.extend((n, e, w) for (e, w) in issued)
        stage_counts.append(len(issued))
        gamma |= {e for (e, _) in issued}
    return {e for (_, e, _) in trace}, trace, stage_counts


def project(trace, L):
    """Observer readout Proj_L: trace events whose token length <= L.

    L is None for the full (identity) projection."""
    if L is None:
        return list(trace)
    return [(n, e, w) for (n, e, w) in trace if len(e) <= L]


def toklen(s):
    return (len(s), s)


VOC = sorted(("".join(p) for l in range(1, MAXLEN + 1)
              for p in product(ALPH, repeat=l)), key=toklen)
SYS = {k: run_system(k) for k in HYP}


def analyze(true_k, L):
    """Observer analysis: reconstruction model per packet section 2.1.

    The observer knows Gamma_0, CandExt, Iss, the stage count, the
    projection rule, and that Adm = Adm_k for some k in HYP; it does not
    know k. A task ISS(s) is decidable iff every k in HYP whose projected
    trace equals the observed one agrees on ISS(s)."""
    obs = project(SYS[true_k][1], L)
    consistent = [k for k in HYP if project(SYS[k][1], L) == obs]
    decid = [s for s in VOC if len({s in SYS[k][0] for k in consistent}) == 1]
    return {"issued": sorted(SYS[true_k][0], key=toklen),
            "record": obs, "consistent_k": consistent, "decidable": decid}


CONDS = {
    "BASE  (k=1, L=2)": (1, 2),
    "ALPHA (k=1, full)": (1, None),
    "BETA  (k=2, L=2)": (2, 2),
    "BASE' (k=1, L=3)": (1, 3),
    "BETA' (k=2, L=3)": (2, 3),
}
R = {name: analyze(*args) for name, args in CONDS.items()}


def fmt_events(events):
    return "[" + ", ".join(
        "({0},{1!r},w=({2},{3},{4}))".format(n, e, int(w[0]), w[1], w[2])
        for n, e, w in events) + "]"


def fmt_set(tokens):
    return "[" + ", ".join(repr(t) for t in sorted(tokens, key=toklen)) + "]"


def same_record(k_a, L_a, k_b, L_b):
    return project(SYS[k_a][1], L_a) == project(SYS[k_b][1], L_b)


RESULTS = []


def check(name, value, expected=True):
    RESULTS.append((name, bool(value), expected))


def main():
    print("TI-PIT-02 fixture v0.2 (draft for TI source issuance)")
    print("=" * 72)
    for name, res in R.items():
        print("== " + name)
        print("   IssuedSet ({0} tokens): {1}".format(
            len(res["issued"]), fmt_set(res["issued"])))
        print("   ProjRecord ({0} events): {1}".format(
            len(res["record"]), fmt_events(res["record"])))
        print("   consistent k under HYP: {0}".format(res["consistent_k"]))
        print("   DecidableSet ({0} of {1}): {2}".format(
            len(res["decidable"]), len(VOC), fmt_set(res["decidable"])))
    print()
    print("== Pairwise deltas (added, removed)")
    for label, (a, b) in {
        "BASE  -> ALPHA": ("BASE  (k=1, L=2)", "ALPHA (k=1, full)"),
        "BASE  -> BETA ": ("BASE  (k=1, L=2)", "BETA  (k=2, L=2)"),
        "BASE' -> BETA'": ("BASE' (k=1, L=3)", "BETA' (k=2, L=3)"),
    }.items():
        ia, ib = set(R[a]["issued"]), set(R[b]["issued"])
        da, db = set(R[a]["decidable"]), set(R[b]["decidable"])
        print(" {0}: issued +{1} -{2}".format(
            label, fmt_set(ib - ia), fmt_set(ia - ib)))
        print(" {0}: decidable +{1} -{2}".format(
            " " * len(label), fmt_set(db - da), fmt_set(da - db)))
        print(" {0}: projRecord identical: {1}".format(
            " " * len(label), R[a]["record"] == R[b]["record"]))
    print()
    print("== Checks ([T] no evidential weight; [E]/[F] evidential)")

    base = R["BASE  (k=1, L=2)"]
    alpha = R["ALPHA (k=1, full)"]
    beta = R["BETA  (k=2, L=2)"]
    basep = R["BASE' (k=1, L=3)"]
    betap = R["BETA' (k=2, L=3)"]

    check("[T] alpha_iss: ALPHA leaves the source issuance set fixed"
          " -- holds by construction of the fixture (the issued set is a"
          " function of k alone and both legs use k=1); theorem-consequence,"
          " no evidential weight",
          set(base["issued"]) == set(alpha["issued"]))
    check("[F] alpha_iss-fail: the same set comparison detects a genuine"
          " issuance change under the perturbed pairing k=1 vs k=2",
          set(base["issued"]) == set(beta["issued"]), expected=False)

    check("[E] beta_rec: BETA leaves the L=2 projected record fixed"
          " (the admissibility change is invisible through Proj_{L=2})",
          same_record(1, 2, 2, 2))
    check("[F] beta_rec-fail: the same record comparison at the same"
          " threshold L=2 detects the perturbed pairing k=0 vs k=1"
          " (event (1,'ab') present only for k>=1)",
          same_record(0, 2, 1, 2), expected=False)

    check("[E] beta_dec: BETA leaves the L=2 observer decidable set fixed",
          base["decidable"] == beta["decidable"])
    check("[F] beta_dec-fail: the same decidable-set comparison flips at the"
          " perturbed threshold L=3 ('abbb' becomes undecidable)",
          basep["decidable"] == betap["decidable"], expected=False)

    check("[E] betap_rec: BETA' changes the L=3 projected record (the same"
          " admissibility change is observer-visible under the wider fixed"
          " projection)",
          not same_record(1, 3, 2, 3))
    check("[F] betap_rec-fail: the same difference test reports no change on"
          " the identity pairing k=1 vs k=1 at L=3",
          not same_record(1, 3, 1, 3), expected=False)

    ext = {k: run_system(k, n_stages=6) for k in HYP}
    check("[E] quiesce: an extended-horizon run (6 stages) issues zero events"
          " at stages 4-6 for every k in HYP -- machine-checked quiescence"
          " (trivially provable from the MAXLEN bound; proof not written)",
          all(ext[k][2][3:] == [0, 0, 0] for k in HYP))
    check("[F] quiesce-fail: the same stage-count predicate fails at stage 3,"
          " where issuance events do occur",
          all(ext[k][2][2] == 0 for k in HYP), expected=False)
    check("[F] quiesce_bound-fail: perturbing the length bound to MAXLEN=5"
          " produces issuance events at stage 4, where the unperturbed"
          " fixture is quiescent (same counting code path; protects:"
          " quiesce)",
          run_system(1, n_stages=6, maxlen=5)[2][3] == 0, expected=False)

    n_t = n_e = n_f = 0
    failures = []
    for name, value, expected in RESULTS:
        ok = value == expected
        n_t += name.startswith("[T]")
        n_e += name.startswith("[E]")
        n_f += name.startswith("[F]")
        print("{0}  {1}: {2}".format("PASS" if ok else "UNEXPECTED",
                                     name, value))
        if not ok:
            failures.append(name)
    print()
    print("EVIDENTIAL CHECKS: {0} [E] + {1} [F] = {2}; [T]"
          " theorem-consequence checks (no evidential weight): {3}".format(
              n_e, n_f, n_e + n_f, n_t))
    if failures:
        print("UNEXPECTED RESULTS: {0}".format(failures))
        return 1
    print("All checks match expectations. Exit 0.")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
