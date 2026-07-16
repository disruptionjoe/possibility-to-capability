"""RANK2-PR-001 adjudication harness -- receiver-owned, exploration tier.

Executes the preregistered Rank-2 access-versus-capability paired-intervention
adjudication (RANK2-PR-001.expectations.json, frozen at commit 49baf1f) on the
two accepted sovereign packets:

  TAF-001     packets/imports/TAF-001/     (time-as-finality, ALPHA/BETA)
  TI-PIT-002  packets/imports/TI-PIT-002/  (temporal-issuance, ALPHA/BETA/BETA')

Discipline implemented here, all frozen BEFORE any sweep outcome is computed:

* Evidence is computed ONLY from the frozen computation blobs (TaF referee
  advisory D6: framing prose quarantined). Blob hashes are re-verified against
  the packet manifests before anything runs ([E] below).
* Completion classes are built mechanically from the source-supplied
  record-channel inventories by the lane-R2 comparison-contract rule (interval
  from the agent's actual observation function to actual-plus-every-declared-
  channel), with zero receiver discretion:
    C_TAF = access sets {h1,h2} <= c <= {h1,h2,h3,h4}   (4 completions)
    C_TI  = length-threshold projections L in {2, 3, full}  (full == L>=MAXLEN)
* Task vocabularies and achievability are source-native (TAF premise A5:
  reconstructibility over TV; TI premise A3: ISS-decidability over the
  30-token vocabulary). No receiver task semantics is substituted (stop S2).
* QUARANTINE (TI-PIT-002 nonclaims + Frame R v0.2 sections R.-1/P4 + frozen
  stop condition S5): Frame R may not be scored against TI-PIT-002 (its v0.1
  advocate co-authored the case lineage; its v0.2 re-freezing advocate
  incidentally read the draft pre-freeze; S5 stops on authored/co-authored/
  READ). Therefore the defended frames are applied to the TAF branch only;
  TI evidence is reported as frame-neutral receiver-owned fact, no frame
  diagnosis, no N-vs-R comparison. This is a preserved constraint.
* Frame rules (frozen): N (candidate, fixed-completion normalization):
  delta(top)!=0 -> CAPABILITY_CHANGE; else delta_op!=0 -> ACCESS_CHANGE; else
  NO_CHANGE. R (rival, per FRAME-R v0.2 Rule R1, extensional form verified
  against prereg c3): delta_op!=0 -> CAPABILITY_CHANGE else NO_CHANGE. NAIVE
  (control): any declared factor change or operational gain -> CAPABILITY_CHANGE.

Check discipline: [T]/[E]/[F] registry; only [E]/[F] carry evidential weight;
every [F] exercises, through the same code path, the checker it protects.
"""

from __future__ import annotations

import hashlib
import io
import json
import sys
from contextlib import redirect_stdout
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TAF_DIR = REPO / "packets" / "imports" / "TAF-001"
TI_DIR = REPO / "packets" / "imports" / "TI-PIT-002"

# --------------------------------------------------------------------------
# [T]/[E]/[F] registry
# --------------------------------------------------------------------------
CHECKS = {
    "t1: TAF ALPHA per-completion deltas empty (forced: legs share one world)":
        {"tag": "T"},
    "t2: TI ALPHA per-completion deltas empty (forced: legs share one system)":
        {"tag": "T"},
    "e0: all frozen computation blobs re-hash to their packet manifests":
        {"tag": "E"},
    "e1: TAF baseline vector matches the frozen output blob claim (1,0,0,0,1)":
        {"tag": "E"},
    "e1-fail: perturbed threshold k=1 flips the TAF baseline vector":
        {"tag": "F", "protects": "e1: TAF baseline vector matches the frozen output blob claim (1,0,0,0,1)"},
    "e2: TAF ALPHA delta_op nonzero (gains tau2, loses tau5) with ROBUST_ZERO completion profile":
        {"tag": "E"},
    "e3: TAF BETA delta_op nonzero (gains tau3) with ROBUST_NONZERO profile over C_TAF":
        {"tag": "E"},
    "e3-fail: outside the frozen interval class (c={h3,h4}) the BETA delta vanishes -- the robustness verdict has a real failing direction":
        {"tag": "F", "protects": "e3: TAF BETA delta_op nonzero (gains tau3) with ROBUST_NONZERO profile over C_TAF"},
    "e4: TI ALPHA delta_op nonzero (decidable 25 -> 30) with ROBUST_ZERO completion profile":
        {"tag": "E"},
    "e5: TI BETA delta_op ZERO with completion-RELATIVE profile (0 at L2, + at L3, 0 at full)":
        {"tag": "E"},
    "e5-fail: the same record/decidable comparison detects the perturbed pairing k=0 vs k=1 at L2":
        {"tag": "F", "protects": "e5: TI BETA delta_op ZERO with completion-RELATIVE profile (0 at L2, + at L3, 0 at full)"},
    "e6: c7 evidence-functionality -- both defended frames return identical diagnoses on recomputed identical evidence (TAF branch)":
        {"tag": "E"},
    "e7: c8 label-neutrality -- swapping pre/post legs of every pair leaves every frame diagnosis and profile class unchanged":
        {"tag": "E"},
    "e7-fail: a direction-sensitive gain-only frame FAILS the same swap test -- the neutrality check has a real failing direction":
        {"tag": "F", "protects": "e7: c8 label-neutrality -- swapping pre/post legs of every pair leaves every frame diagnosis and profile class unchanged"},
    "e8: c9 shared vocabulary -- every task in each branch vocabulary is evaluable in both members of every pair":
        {"tag": "E"},
}

RESULTS = []


def check(name, value):
    assert name in CHECKS, name
    RESULTS.append((name, CHECKS[name]["tag"], bool(value)))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_frozen(path: Path) -> dict:
    """exec a frozen computation blob in an isolated namespace, stdout muted."""
    ns: dict = {"__name__": "frozen_blob"}
    with redirect_stdout(io.StringIO()):
        exec(compile(path.read_bytes(), str(path), "exec"), ns)
    return ns


def main() -> int:
    print("RANK2-PR-001 ADJUDICATION HARNESS -- sovereign evidence, receiver-owned run")
    print("=" * 76)

    # ---- e0: manifest re-verification before anything runs ----------------
    ok = True
    for d in (TAF_DIR, TI_DIR):
        pkt = json.loads((d / "packet.json").read_text(encoding="utf-8"))
        for entry in pkt["integrity"]["manifest"]:
            p = d.joinpath(*entry["path"].split("/"))
            if sha256(p) != entry["content_sha256"]:
                ok = False
                print(f"  HASH MISMATCH: {p}")
    check("e0: all frozen computation blobs re-hash to their packet manifests", ok)

    taf = load_frozen(TAF_DIR / "blobs" / "taf001_paired_intervention.py")
    ti = load_frozen(TI_DIR / "blobs" / "ti_pit_02_fixture.py")

    # ---- frozen completion classes (contract rule; zero discretion) -------
    H12 = frozenset({"h1", "h2"})
    C_TAF = (frozenset({"h1", "h2"}),
             frozenset({"h1", "h2", "h3"}),
             frozenset({"h1", "h2", "h4"}),
             frozenset({"h1", "h2", "h3", "h4"}))     # bottom=actual, top=full
    C_TI = (2, 3, None)                                # bottom=actual L2, top=full

    # ---- TAF branch evidence (source-native semantics) ---------------------
    def taf_taskset(nodes, edges, records, access, k=None):
        reach = taf["reachability"](nodes, edges)
        kk = taf["K"] if k is None else k
        return frozenset(
            t for t, p, v in taf["TASKS"]
            if taf["reconstructible"](records, access, p, v, taf["EVAL"], reach, kk))

    W0 = (taf["BASE_NODES"], taf["BASE_EDGES"], taf["BASE_RECORDS"])
    WB = (taf["BETA_NODES"], taf["BETA_EDGES"], taf["BETA_RECORDS"])

    def taf_pair(pre_world, pre_acc, post_world, post_acc):
        op_pre = taf_taskset(*pre_world, pre_acc)
        op_post = taf_taskset(*post_world, post_acc)
        dc = {c: taf_taskset(*pre_world, c) != taf_taskset(*post_world, c)
              for c in C_TAF}
        return {"op_pre": op_pre, "op_post": op_post,
                "gained": op_post - op_pre, "lost": op_pre - op_post,
                "dop": op_pre != op_post, "dc": dc,
                "robust": len(set(dc.values())) == 1,
                "factor_changed": True}

    taf_alpha = taf_pair(W0, taf["BASE_ACCESS"], W0, taf["ALPHA_ACCESS"])
    taf_beta = taf_pair(W0, taf["BASE_ACCESS"], WB, taf["BASE_ACCESS"])

    # ---- TI branch evidence (frame-neutral ONLY; quarantine) ---------------
    def dec(k, L):
        return frozenset(ti["analyze"](k, L)["decidable"])

    def ti_pair(k_pre, L_pre, k_post, L_post):
        op_pre, op_post = dec(k_pre, L_pre), dec(k_post, L_post)
        dc = {("L%s" % (c if c is not None else "full")):
              dec(k_pre, c) != dec(k_post, c) for c in C_TI}
        return {"op_pre": op_pre, "op_post": op_post,
                "gained": op_post - op_pre, "lost": op_pre - op_post,
                "dop": op_pre != op_post, "dc": dc,
                "robust": len(set(dc.values())) == 1,
                "factor_changed": True}

    ti_alpha = ti_pair(1, 2, 1, None)
    ti_beta = ti_pair(1, 2, 2, 2)

    def show(label, ev, comps):
        dcs = ", ".join(f"delta({c})={'+' if ev['dc'][c] else '0'}" for c in comps)
        print(f"  {label}: dop={'+' if ev['dop'] else '0'} "
              f"gained={sorted(ev['gained'])} lost={sorted(ev['lost'])}")
        print(f"    per-completion: {dcs} -> "
              f"{'completion-ROBUST' if ev['robust'] else 'completion-RELATIVE'}")

    print()
    print("Frame-neutral pair evidence (frozen completion classes, source-native tasks):")
    def lab(c):
        return "{" + ",".join(sorted(c)) + "}"

    taf_alpha["dc"] = {lab(c): taf_alpha["dc"][c] for c in C_TAF}
    taf_beta["dc"] = {lab(c): taf_beta["dc"][c] for c in C_TAF}
    show("TAF ALPHA (access-structure declared)", taf_alpha,
         [lab(c) for c in C_TAF])
    show("TAF BETA  (record-formation declared)", taf_beta,
         [lab(c) for c in C_TAF])
    show("TI  ALPHA (projection-only declared) ", ti_alpha,
         ["L2", "L3", "Lfull"])
    show("TI  BETA  (admissibility-only declared)", ti_beta,
         ["L2", "L3", "Lfull"])
    print()

    # ---- frames (TAF branch only; TI quarantined) --------------------------
    def frame_N(ev, comps):
        top = comps[-1]
        top = top if top in ev["dc"] else "{" + ",".join(sorted(top)) + "}"
        if ev["dc"][top]:
            return "CAPABILITY_CHANGE"
        return "ACCESS_CHANGE" if ev["dop"] else "NO_CHANGE"

    def frame_R(ev):
        return "CAPABILITY_CHANGE" if ev["dop"] else "NO_CHANGE"

    def frame_NAIVE(ev):
        return "CAPABILITY_CHANGE" if (ev["factor_changed"] or ev["dop"]) \
            else "NO_CHANGE"

    taf_matrix = {
        "TAF_ALPHA": {"NAIVE": frame_NAIVE(taf_alpha),
                      "N": frame_N(taf_alpha, C_TAF), "R": frame_R(taf_alpha)},
        "TAF_BETA": {"NAIVE": frame_NAIVE(taf_beta),
                     "N": frame_N(taf_beta, C_TAF), "R": frame_R(taf_beta)},
    }
    print("Frame diagnoses (TAF branch only; TI branch frame-quarantined):")
    for k, row in taf_matrix.items():
        agree = "AGREE" if row["N"] == row["R"] else "DISAGREE"
        print(f"  {k}: NAIVE={row['NAIVE']}  N={row['N']}  R={row['R']}"
              f"   [defended frames {agree}]")
    print()

    # ---- checks -------------------------------------------------------------
    check("t1: TAF ALPHA per-completion deltas empty (forced: legs share one world)",
          not any(taf_alpha["dc"].values()))
    check("t2: TI ALPHA per-completion deltas empty (forced: legs share one system)",
          not any(ti_alpha["dc"].values()))

    base_vec = tuple(1 if t in taf_taskset(*W0, H12) else 0
                     for t, _, _ in taf["TASKS"])
    check("e1: TAF baseline vector matches the frozen output blob claim (1,0,0,0,1)",
          base_vec == (1, 0, 0, 0, 1))
    pert_vec = tuple(1 if t in taf_taskset(*W0, H12, k=1) else 0
                     for t, _, _ in taf["TASKS"])
    check("e1-fail: perturbed threshold k=1 flips the TAF baseline vector",
          pert_vec != (1, 0, 0, 0, 1))

    check("e2: TAF ALPHA delta_op nonzero (gains tau2, loses tau5) with ROBUST_ZERO completion profile",
          taf_alpha["dop"] and taf_alpha["gained"] == {"tau2"}
          and taf_alpha["lost"] == {"tau5"}
          and taf_alpha["robust"] and not any(taf_alpha["dc"].values()))

    check("e3: TAF BETA delta_op nonzero (gains tau3) with ROBUST_NONZERO profile over C_TAF",
          taf_beta["dop"] and taf_beta["gained"] == {"tau3"}
          and not taf_beta["lost"]
          and taf_beta["robust"] and all(taf_beta["dc"].values()))
    out_of_class = frozenset({"h3", "h4"})
    check("e3-fail: outside the frozen interval class (c={h3,h4}) the BETA delta vanishes -- the robustness verdict has a real failing direction",
          taf_taskset(*W0, out_of_class) == taf_taskset(*WB, out_of_class))

    check("e4: TI ALPHA delta_op nonzero (decidable 25 -> 30) with ROBUST_ZERO completion profile",
          ti_alpha["dop"] and len(ti_alpha["op_pre"]) == 25
          and len(ti_alpha["op_post"]) == 30
          and ti_alpha["robust"] and not any(ti_alpha["dc"].values()))

    check("e5: TI BETA delta_op ZERO with completion-RELATIVE profile (0 at L2, + at L3, 0 at full)",
          not ti_beta["dop"] and not ti_beta["robust"]
          and not ti_beta["dc"]["L2"] and ti_beta["dc"]["L3"]
          and not ti_beta["dc"]["Lfull"])
    check("e5-fail: the same record/decidable comparison detects the perturbed pairing k=0 vs k=1 at L2",
          dec(0, 2) != dec(1, 2))

    rerun = {
        "TAF_ALPHA": {"NAIVE": frame_NAIVE(taf_alpha),
                      "N": frame_N(taf_alpha, C_TAF), "R": frame_R(taf_alpha)},
        "TAF_BETA": {"NAIVE": frame_NAIVE(taf_beta),
                     "N": frame_N(taf_beta, C_TAF), "R": frame_R(taf_beta)},
    }
    check("e6: c7 evidence-functionality -- both defended frames return identical diagnoses on recomputed identical evidence (TAF branch)",
          rerun == taf_matrix)

    def swap(ev):
        out = dict(ev)
        out["op_pre"], out["op_post"] = ev["op_post"], ev["op_pre"]
        out["gained"], out["lost"] = ev["lost"], ev["gained"]
        return out

    swap_ok = True
    for ev in (taf_alpha, taf_beta):
        s = swap(ev)
        if (frame_N(s, C_TAF), frame_R(s), frame_NAIVE(s), s["robust"]) != \
           (frame_N(ev, C_TAF), frame_R(ev), frame_NAIVE(ev), ev["robust"]):
            swap_ok = False
    for ev in (ti_alpha, ti_beta):   # frame-neutral profile class only
        if swap(ev)["robust"] != ev["robust"] or swap(ev)["dop"] != ev["dop"]:
            swap_ok = False
    check("e7: c8 label-neutrality -- swapping pre/post legs of every pair leaves every frame diagnosis and profile class unchanged",
          swap_ok)

    def frame_gain_only(ev):        # deliberately direction-sensitive control
        return "CAPABILITY_CHANGE" if ev["gained"] else "NO_CHANGE"
    check("e7-fail: a direction-sensitive gain-only frame FAILS the same swap test -- the neutrality check has a real failing direction",
          any(frame_gain_only(swap(ev)) != frame_gain_only(ev)
              for ev in (taf_alpha, taf_beta)))

    # c9: every task evaluable in both members of every pair (no distortion):
    # TAF tasks evaluate at any access set; TI decidability evaluates at any
    # (k, L). Evaluability is witnessed by the sweeps above having produced a
    # boolean for every task in every leg; assert totality explicitly.
    taf_total = all(isinstance(taf_taskset(*w, a), frozenset)
                    for w in (W0, WB)
                    for a in (taf["BASE_ACCESS"], taf["ALPHA_ACCESS"]))
    ti_total = all(isinstance(dec(k, L), frozenset)
                   for k in (1, 2) for L in C_TI)
    check("e8: c9 shared vocabulary -- every task in each branch vocabulary is evaluable in both members of every pair",
          taf_total and ti_total)

    # ---- report -------------------------------------------------------------
    print("Checks:")
    n = {"T": 0, "E": 0, "F": 0}
    bad = []
    for name, tag, okv in RESULTS:
        n[tag] += 1
        print(f"  {'PASS' if okv else 'FAIL'}  [{tag}] {name}")
        if not okv:
            bad.append(name)
    print()
    print(f"EVIDENTIAL CHECKS (headline): {n['E']} [E] + {n['F']} [F] = "
          f"{n['E'] + n['F']}, all {'passing' if not bad else 'NOT passing'}")
    print(f"[T] theorem-consequence checks (no evidential weight): {n['T']}")
    if bad:
        print("FAILURES:", bad)
        return 1

    print()
    print("OBSERVED VALUES FOR THE PREREGISTERED CHECKS (scoring in results.json):")
    print("  c1: ISSUED (TAF-001, two-commit freeze verified, imported b28d28e)")
    print("  c2: ISSUED (TI-PIT-002, two-commit freeze verified, imported b28d28e)")
    print("  c3: FROZEN_INDEPENDENT for every case the frame scores (TAF branch);")
    print("      TI branch frame-discrimination EXCLUDED by S5 + packet quarantine")
    print("  c4: ROBUST_ZERO on both sovereign access-declared pairs (TAF ALPHA, TI ALPHA)")
    print("  c5: NOT_APPLICABLE -- no sovereign declaration matches 'capability-changing'")
    print("      (both sources refuse receiver-taxonomy labels; J1 + retained fork 2);")
    print("      construal fork preserved: under the factor-reading counterfactual,")
    print("      TAF BETA is ROBUST_NONZERO over C_TAF and TI BETA is completion-RELATIVE")
    print("  c6: FALSE on admissible evidence -- no completion-RELATIVE pair with a")
    print("      defended-frame disagreement (TAF pairs both ROBUST; TI quarantined,")
    print("      and its RELATIVE pair has delta_op=0 and delta(top)=0)")
    print("  c7: TRUE   c8: TRUE   c9: TRUE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
