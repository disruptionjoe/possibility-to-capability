#!/usr/bin/env python3
"""Hierarchy v0.2 typed skeleton -- process-level level-typed data
plus three toy diagnoses run end-to-end.

Adopted 2026-07-16 (Joe, direct chat) with the adversarial referee's
corrections D1-D7 applied (referee report attached to
explorations/2026-07-16-northstar-unblock/lane-D-hierarchy-v02-draft.md,
which GOVERNS grades). Corrections carried in this file:
  D1: d1c retagged [E] -> [T]; the null-intervention criterion is a
      forced-frame FLAG, not a structural-circularity detector -- structural
      circularity (e.g. post-hoc task vocabulary) is NOT detected at this
      grade; a detector with bite is open work.
  D4: d3c retagged [E] -> [T] (by-construction code property, same class as
      setup2). Honest evidential headline: 8 [E] + 4 [F] = 12.
  D5: d3d now quantifies over decoders (exists g with g(f(x)) = x0), not
      merely f == projection.
  D7: d1d's fork exhibition kept; its frames are declared and pass the
      forced-frame flag, which does not certify structural non-circularity.
      Known limitation: the CAPABILITY_CHANGE (restriction) branch of
      classify_intervention is exercised by no check.

Grade: deterministic synthetic toy. This fixture demonstrates that the v0.2
typed definitions are executable; it is NOT evidence for any physical claim,
moves no source-repo claim, and issues no receiver verdict. bar(b), H59,
Krein positivity, physical issuance stay OPEN.

Design requirement I-6 (static-sheaf amputation): every level's datum here is
defined over a MORPHISM-LABELED process graph (issuance morphisms carrying
composition-compatible labels and traces), never over a state snapshot.
Formal anchors: TI E160 (composition-compatible morphism labels;
temporal-issuance/explorations/E160-holonomy-transport-functor-derivation-
fixture-2026-07-10.md, bounded toy fixture, claim_movement false), TI
RUN-0025 (temporal-issuance/FORMAL-OBJECT.md; thin-shadow warning:
morphism-level invariants can differ while the induced state order is
identical).

Prior art: d3a re-derives at 2-block scale the multiplicity content of the
already-run Lane 1 fixture 4a (tests/per_block_observability_fixture.py;
explorations/2026-07-16-per-block-observability/SYNTHESIS.md, closed
ENDPOINT_POSITIVE_TOY at exhaustive-finite-toy grade; cited at its own
grade -- no adversarial referee report attached to that run).

House rule: [T]/[E]/[F] check registry; only [E]+[F] carry evidential weight;
every [F] exercises, through the same code path, the checker it protects.
Lint: python tests/tef_check_tag_linter.py --strict <this file>
"""

from itertools import product

CHECKS = {
    "setup1: generator-extended labels are composition-compatible by construction":
        {"tag": "T"},
    "setup2: finality diagnosis emits switch-profile fields only (no operator key)":
        {"tag": "T"},
    "d1a: access-only intervention classifies ACCESS_CHANGE under the declared frame":
        {"tag": "E"},
    "d1b: admissibility-enlarging intervention classifies CAPABILITY_ENLARGEMENT":
        {"tag": "E"},
    # D1: retagged [E] -> [T]. The flag returns False for every expressible
    # frame lacking the literal forced_verdict key; this check cannot fail
    # for declarable frames and carries no evidential weight.
    "d1c: declared frames pass the null-intervention forced-frame flag":
        {"tag": "T"},
    "d1c-fail: answer-entailing frame IS flagged by the same forced-frame flag":
        {"tag": "F",
         "protects": "d1c: declared frames pass the null-intervention forced-frame flag"},
    "d1d: same intervention classifies differently under a distinct declared frame":
        {"tag": "E"},
    "d2a: thin shadows identical while the morphism-level invariant differs (I-6)":
        {"tag": "E"},
    "d2a-fail: label-degenerate twin does NOT differ under the same invariant":
        {"tag": "F",
         "protects": "d2a: thin shadows identical while the morphism-level invariant differs (I-6)"},
    "d3a: per-block injection is choice-visible; global injection is choice-invisible":
        {"tag": "E"},
    "d3a-fail: single-block model yields NO choice-sensitive flip-invariant observable":
        {"tag": "F",
         "protects": "d3a: per-block injection is choice-visible; global injection is choice-invisible"},
    "d3b: re-made per-block bits give stage-varying alignments; once-bits give fixed":
        {"tag": "E"},
    # D4: retagged [E] -> [T]. Same by-construction code-property class as
    # setup2: interior_observables is written to read only story['bits'].
    "d3c: matched-profile operators (B-fired vs C) give identical interior observables":
        {"tag": "T"},
    "d3d: no flip-invariant selector on the 2-block label space determines the absolute bit":
        {"tag": "E"},
    "d3e: compatible morphism-label injection is accepted by the composition checker":
        {"tag": "E"},
    "d3e-fail: non-composition-compatible injection REJECTED by the same checker":
        {"tag": "F",
         "protects": "d3e: compatible morphism-label injection is accepted by the composition checker"},
}

# --------------------------------------------------------------- base object


class Proc:
    """Finite process object: a graph of issuance morphisms with Z/2 labels.

    gens: mid -> (src, tgt, label_bit). Paths are composable generator
    sequences; path labels extend generator labels additively (mod 2), which
    is the composition-compatibility law (E160 positive shape).
    States appear only as sources/targets of morphisms; no level datum below
    is a function of the state set alone (I-6).
    """

    def __init__(self, objects, gens):
        self.objects = set(objects)
        self.gens = dict(gens)

    def paths(self, max_len=4):
        frontier = [((m,), s, t) for m, (s, t, _) in self.gens.items()]
        out = list(frontier)
        for _ in range(max_len - 1):
            nxt = []
            for p, s, t in frontier:
                for m, (s2, t2, _) in self.gens.items():
                    if s2 == t:
                        nxt.append((p + (m,), s, t2))
            out.extend(nxt)
            frontier = nxt
        return out

    def path_label(self, path):
        bit = 0
        for m in path:
            bit ^= self.gens[m][2]
        return bit

    def thin_shadow(self, max_len=4):
        """Induced reachability relation: the state-snapshot-forgetting map
        (RUN-0025's thin reflection)."""
        return frozenset((s, t) for _, s, t in self.paths(max_len))

    def hom_label_profile(self, max_len=4):
        """Morphism-level invariant: per (src,tgt), the multiset of path
        labels. Strictly finer than thin_shadow (RUN-0025)."""
        prof = {}
        for p, s, t in self.paths(max_len):
            prof.setdefault((s, t), []).append(self.path_label(p))
        return {k: tuple(sorted(v)) for k, v in prof.items()}


def composition_compatible(proc, labeling, max_len=3):
    """E160 checker: labeling(path) must satisfy L(p.q) = L(p) xor L(q)."""
    idx = {p: (s, t) for p, s, t in proc.paths(max_len)}
    for p, (_, pt) in idx.items():
        for q, (qs, _) in idx.items():
            if pt == qs and (p + q) in idx:
                if labeling[p + q] != labeling[p] ^ labeling[q]:
                    return False
    return True


# ------------------------------------------------- level-typed data (toy)

def make_model():
    """Base model for diagnosis 1: possibility/dynamics/records/access data
    over one process object."""
    proc = Proc(
        objects={"a", "b", "z", "w"},
        gens={"m1": ("a", "b", 0), "m2": ("b", "z", 0)},
    )
    return {
        "proc": proc,
        "agent_pos": "a",
        # possibility level: admissible-extension classes per prefix object
        "adm": {"a": {"m1"}, "b": {"m2"}},
        # records level: traces riding ON morphisms (not state facts)
        "traces": {"m2": [("reached_z", "holder1")]},
        # access level: observer-indexed inspectability of trace holders
        "obs_access": {"holder0"},
    }


def admissible_paths(model, max_len=4):
    proc, adm = model["proc"], model["adm"]
    for p, s, t in proc.paths(max_len):
        if s != model["agent_pos"]:
            continue
        ok, cur = True, s
        for m in p:
            if m not in adm.get(cur, set()):
                ok = False
                break
            cur = proc.gens[m][1]
        if ok:
            yield p, t


def task_realizable(model, task, access_set):
    kind, arg = task.split(":")
    for p, t in admissible_paths(model):
        if kind == "reach" and t == arg:
            return True
        if kind == "audit":
            for m in p:
                for prop, holder in model["traces"].get(m, []):
                    if prop == arg and holder in access_set:
                        return True
    return False


def normalized_capability(model, frame):
    """Capability level: the frame is a DECLARED parameter, never derived."""
    access = frame["access_baseline"] if frame["hold_access_fixed"] \
        else model["obs_access"]
    return frozenset(t for t in frame["task_vocab"]
                     if task_realizable(model, t, access))


def access_view(model):
    """Access level: which morphism-traces this observer can inspect."""
    return frozenset(
        (m, prop) for m, entries in model["traces"].items()
        for prop, holder in entries if holder in model["obs_access"])


def classify_intervention(base, post, frame):
    if "forced_verdict" in frame:          # an answer-entailing (circular) frame
        return frame["forced_verdict"]
    cap0, cap1 = normalized_capability(base, frame), normalized_capability(post, frame)
    if cap0 != cap1:
        return "CAPABILITY_ENLARGEMENT" if cap1 > cap0 else "CAPABILITY_CHANGE"
    if access_view(base) != access_view(post):
        return "ACCESS_CHANGE"
    return "NO_CHANGE"


def frame_is_circular(frame, base):
    """Null-intervention forced-frame FLAG (referee D1 wording): a frame is
    flagged iff it misclassifies the identity intervention. In this skeleton
    the only such frames are explicitly forced ones (literal forced_verdict
    key). Structural circularity (e.g. post-hoc task vocabulary) is NOT
    detected at this grade; a detector with bite over structurally circular
    frames is open work."""
    return classify_intervention(base, base, frame) != "NO_CHANGE"


# --------------------------------------------------- finality-level machinery

def interior_observables(story):
    """Everything the interior can see: flip-invariant relative alignments
    between block bits. Never reads story['operator'] -- checked, not assumed."""
    bits = story["bits"]
    keys = sorted(bits)
    obs = {}
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            obs[(keys[i], keys[j])] = bits[keys[i]] ^ bits[keys[j]]
    return obs


def choice_visible(n_blocks, multiplicity):
    """Is the settlement choice interior-visible? Computed over ALL choices
    admissible at the given multiplicity; observables are flip-invariant by
    construction (verified inside)."""
    blocks = [f"blk{i}" for i in range(n_blocks)]
    if multiplicity == "global":
        choices = [dict.fromkeys(blocks, c) for c in (0, 1)]
    else:
        choices = [dict(zip(blocks, tup))
                   for tup in product((0, 1), repeat=n_blocks)]
    seen = set()
    for ch in choices:
        story = {"bits": ch}
        obs = interior_observables(story)
        flipped = interior_observables({"bits": {k: v ^ 1 for k, v in ch.items()}})
        assert obs == flipped, "observable not flip-invariant"
        seen.add(tuple(sorted(obs.items())))
    return len(seen) > 1


def alignment_history(bit_history):
    return [tuple(sorted(interior_observables({"bits": b}).items()))
            for b in bit_history]


def diagnose_finality(story, n_admissible_settlements):
    """Finality diagnosis: SSB vocabulary + switch profile. By construction it
    can emit multiplicity and re-makeability, never operator identity.
    Referee D6: this function is a passthrough -- all four emitted fields are
    stipulated vocabulary at this grade (see the honesty note)."""
    return {
        "instability": n_admissible_settlements > 1,
        "susceptibility": "composition-compatible flip-odd morphism label",
        "lock_in": True,  # injected bit transported by path-label composition
        "switch_profile": {"multiplicity": story["multiplicity"],
                           "re_made": story["re_made"]},
    }


# ---------------------------------------------------------------- diagnoses

def main():
    results = []

    def check(name, value, expected=True):
        results.append((name, bool(value), expected))

    # ---- setup [T] checks (fixed by construction; no evidential weight)
    proc0 = Proc({"a", "b", "c"},
                 {"g1": ("a", "b", 1), "g2": ("b", "c", 1)})
    lab = {p: proc0.path_label(p) for p, _, _ in proc0.paths(3)}
    check("setup1: generator-extended labels are composition-compatible by construction",
          composition_compatible(proc0, lab))
    diag = diagnose_finality(
        {"multiplicity": "global", "re_made": False, "bits": {"blk0": 1}}, 2)
    check("setup2: finality diagnosis emits switch-profile fields only (no operator key)",
          "operator" not in diag and "operator" not in diag["switch_profile"])

    # ---- Diagnosis 1: access-change vs capability-enlargement (frame declared)
    base = make_model()
    frame = {"task_vocab": ["reach:z", "reach:w", "audit:reached_z"],
             "hold_access_fixed": True,
             "access_baseline": frozenset(base["obs_access"])}

    post_access = make_model()
    post_access["obs_access"] = {"holder0", "holder1"}   # access-only move
    check("d1a: access-only intervention classifies ACCESS_CHANGE under the declared frame",
          classify_intervention(base, post_access, frame) == "ACCESS_CHANGE")

    post_cap = make_model()
    post_cap["proc"].gens["m3"] = ("z", "w", 0)          # new admissible morphism
    post_cap["adm"]["z"] = {"m3"}
    check("d1b: admissibility-enlarging intervention classifies CAPABILITY_ENLARGEMENT",
          classify_intervention(base, post_cap, frame) == "CAPABILITY_ENLARGEMENT")

    frame_free = dict(frame, hold_access_fixed=False)
    check("d1c: declared frames pass the null-intervention forced-frame flag",
          not frame_is_circular(frame, base)
          and not frame_is_circular(frame_free, base))
    frame_bad = dict(frame, forced_verdict="CAPABILITY_ENLARGEMENT")
    check("d1c-fail: answer-entailing frame IS flagged by the same forced-frame flag",
          not frame_is_circular(frame_bad, base), expected=False)
    # Rank-2 fork, exhibited: the SAME intervention gets a different diagnosis
    # under a different declared frame. Both frames pass the forced-frame
    # flag; per D1 that flag does not certify structural non-circularity.
    # The frame is a parameter of the capability level, not a derived fact.
    check("d1d: same intervention classifies differently under a distinct declared frame",
          classify_intervention(base, post_access, frame) == "ACCESS_CHANGE"
          and classify_intervention(base, post_access, frame_free)
          == "CAPABILITY_ENLARGEMENT")

    # ---- Diagnosis 2: I-6 executable (thin shadow vs morphism-level datum)
    proc_a = Proc({"s", "t"}, {"p": ("s", "t", 0), "q": ("s", "t", 0)})
    proc_b = Proc({"s", "t"}, {"p": ("s", "t", 0), "q": ("s", "t", 1)})
    check("d2a: thin shadows identical while the morphism-level invariant differs (I-6)",
          proc_a.thin_shadow() == proc_b.thin_shadow()
          and proc_a.hom_label_profile() != proc_b.hom_label_profile())
    proc_b_degenerate = Proc({"s", "t"},
                             {"p": ("s", "t", 0), "q": ("s", "t", 0)})
    check("d2a-fail: label-degenerate twin does NOT differ under the same invariant",
          proc_a.hom_label_profile() != proc_b_degenerate.hom_label_profile(),
          expected=False)

    # ---- Diagnosis 3: finality switch-profile
    # Prior art: fixture 4a already ran and closed ENDPOINT_POSITIVE_TOY
    # (explorations/2026-07-16-per-block-observability/SYNTHESIS.md); d3a
    # re-derives its multiplicity content at 2-block scale.
    check("d3a: per-block injection is choice-visible; global injection is choice-invisible",
          choice_visible(2, "per-block") and not choice_visible(2, "global"))
    check("d3a-fail: single-block model yields NO choice-sensitive flip-invariant observable",
          choice_visible(1, "per-block"), expected=False)

    remade = alignment_history([{"blk0": 0, "blk1": 0}, {"blk0": 0, "blk1": 1}])
    once = alignment_history([{"blk0": 0, "blk1": 1}, {"blk0": 0, "blk1": 1}])
    check("d3b: re-made per-block bits give stage-varying alignments; once-bits give fixed",
          len(set(remade)) > 1 and len(set(once)) == 1)

    story_b = {"operator": "B-fired", "multiplicity": "global",
               "re_made": False, "bits": {"blk0": 1, "blk1": 1}}
    story_c = {"operator": "C", "multiplicity": "global",
               "re_made": False, "bits": {"blk0": 1, "blk1": 1}}
    check("d3c: matched-profile operators (B-fired vs C) give identical interior observables",
          interior_observables(story_b) == interior_observables(story_c))

    # exhaustive over all 16 boolean selectors on the 2-block label space,
    # with bit-determination quantified over decoders (referee D5): f
    # determines the absolute bit iff SOME decoder g recovers x0 from f(x).
    flip = lambda x: (x[0] ^ 1, x[1] ^ 1)
    space = list(product((0, 1), repeat=2))
    decoders = [dict(zip((0, 1), gv)) for gv in product((0, 1), repeat=2)]
    bad = []
    for tt in product((0, 1), repeat=4):
        f = dict(zip(space, tt))
        flip_invariant = all(f[x] == f[flip(x)] for x in space)
        determines_bit = any(all(g[f[x]] == x[0] for x in space)
                             for g in decoders)
        if flip_invariant and determines_bit:
            bad.append(tt)
    check("d3d: no flip-invariant selector on the 2-block label space determines the absolute bit",
          not bad)

    good_inj = {p: proc0.path_label(p) for p, _, _ in proc0.paths(3)}
    check("d3e: compatible morphism-label injection is accepted by the composition checker",
          composition_compatible(proc0, good_inj))
    bad_inj = dict(good_inj)
    bad_inj[("g1", "g2")] ^= 1               # violate L(pq) = L(p) xor L(q)
    check("d3e-fail: non-composition-compatible injection REJECTED by the same checker",
          composition_compatible(proc0, bad_inj), expected=False)

    # ------------------------------------------------------------- report
    print("HIERARCHY v0.2 TYPED SKELETON -- toy diagnoses")
    print("=" * 74)
    failures = []
    n = {"T": 0, "E": 0, "F": 0}
    for name, value, expected in results:
        tag = CHECKS[name]["tag"]
        n[tag] += 1
        ok = value == expected
        print(f"{'PASS' if ok else 'UNEXPECTED'}  [{tag}] {name}: {value}")
        if not ok:
            failures.append(name)
    print(f"\nEVIDENTIAL CHECKS (headline): {n['E']} [E] + {n['F']} [F] = {n['E'] + n['F']}")
    print(f"[T] theorem-consequence checks (no evidential weight): {n['T']}")
    print("\nWorked finality diagnosis (toy; SSB vocabulary + switch profile;")
    print("all four fields are stipulated vocabulary at this grade -- referee D6):")
    print(" ", diagnose_finality(
        {"multiplicity": "per-block", "re_made": False,
         "bits": {"blk0": 0, "blk1": 1}}, 2))
    if failures:
        print("UNEXPECTED RESULTS:", failures)
        return 1
    print("All checks match expectations. Exit 0.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
