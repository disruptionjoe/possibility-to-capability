> Part of the 2026-07-16 north-star unblock swing. Exploration tier; the attached referee report GOVERNS (grades + corrections + firewall verdict). Firewalled lanes (B, C) were audited INDEPENDENT.

Fixture exits 0 and lints clean under `--strict` (registry mode, 0 violations, 0 advisories). The complete deliverable follows.

---

```markdown
---
artifact_type: provisional_synthesis
status: draft_for_joe_review
created: 2026-07-16
workflow: north-star-lane-item-2
construction: typed_partial_diagnostic_process_level
evidence_grade: definitional_draft_plus_deterministic_toy_skeleton
predecessor: synthesis/2026-07-14-coherent-story-v0.1.md
verification: tests/hierarchy_v02_typed_skeleton.py (proposed; embedded below, exit 0, --strict lint clean)
constitutional: false
---

# Hierarchy v0.2 — typed level and transition definitions (DRAFT)

**Status and guards.** This is a DRAFT for Joe's review. It is the typed successor of the v0.1
plain-English candidate (`synthesis/2026-07-14-coherent-story-v0.1.md`) and keeps v0.1's central
posture: the six levels are **diagnostic types, not a chronology**. It INSTANTIATES the charter's
guiding hypothesis; it does not modify it. It issues **no receiver verdicts**, moves **no source-repo
claim** (`bar(b)`, H59, Krein positivity, physical issuance stay OPEN), and does not claim v0.2 is
validated — validation is exactly what the ranked decisive-test program exists for
(`experiments/2026-07-14-ranked-decisive-test-program-v0.1.md`; referee-corrected receiver updates in
`explorations/2026-07-16-decisive-tests/SYNTHESIS.md` govern). The north-star/byproduct firewall stands
unchanged: the repo's purpose remains the charter hypothesis; the Bounded Fiber Theorem is a byproduct
spine whose findings feed the finality level as INPUT, never as the purpose
(`explorations/2026-07-16-progress-lanes.md`).

**What changed from v0.1 to v0.2.** v0.1 gave the six types in plain English with epistemic
separation. v0.2 (a) types each level as a class of structure over a base PROCESS object, per design
requirement I-6 (static-sheaf amputation: state snapshots are defined by forgetting the issuance
process the datum rides on; register row I-6, `explorations/INTERPRETATIONS-REGISTER.md`); (b) gives
the finality level its proper internal machinery (switch profiles, operator opacity, SSB vocabulary —
register rows I-1..I-5, I-7); (c) makes the definitions executable at toy grade with [T]/[E]/[F]
discipline; (d) states per-level falsifiers feeding the program's `REVISE_HIERARCHY` outcome.

---

## 1. The base object: a process object, not a state space

All six levels are typed over one base object. Per I-6 this base is process-level:

> **Definition (process object, draft).** A process object `P` is a finite category-like structure:
> objects are prefix/contexts (source states appear ONLY as sources and targets of morphisms);
> morphisms are **issuance acts** `e : S -> S'`; composition is path concatenation where defined; and
> morphisms may carry **labels** in a declared monoid `M`, subject to the composition-compatibility
> law `L(g∘f) = L(g)·L(f)`.

Formal anchors (both TI-owned; cited, not absorbed — `temporal-issuance/FORMAL-OBJECT.md`):

- **E160 (composition-compatible morphism labels):** nontrivial transport exists only when
  admissibility itself carries a composition-compatible label rule ON MORPHISMS; a label table
  supplied from outside is not a derivation, and inconsistent labels define no functor. v0.2 adopts
  this as the type of every level-datum that "rides" the process.
- **RUN-0025 (thin-shadow warning):** the induced state-order `S <= S'` iff `Hom(S,S')` nonempty is
  only the thin reflection; morphism-level invariants can differ while the induced order is
  identical. Therefore **no v0.2 level datum may be defined as a function of the thin shadow** — that
  is precisely the static-sheaf amputation I-6 bans. (Executable demonstration: diagnosis 2 below.)

Grade of everything in §§1–3: **definitional draft**, backed only by the deterministic toy skeleton
in §4. Nothing here is a validated physical typology.

## 2. The six levels, typed

Each level is given by four fields: **DATA** (what the level's datum IS, as structure over `P`),
**PRESERVED BY** (which transformations preserve it), **CHARACTERISTIC FAILURE / ABSORBER** (how the
level classically collapses or gets absorbed), and **DIAGNOSTIC QUESTION** (what it answers).
Transitions between levels are the typed comparisons named inside each definition; v0.1's rule stands:
a case need not visit every type, types may be co-located, and `HIERARCHY_REVISION` is a first-class
outcome.

### 2.1 Possibility

- **DATA.** An admissibility structure over candidate morphisms: for each prefix object `S`, the
  class `CandExt(S)` of candidate issuance morphisms and the admissibility predicate `Adm_S` with its
  witnesses, both FORMED AT the prefix (the `OnlineIssuance^LC` shape, cited at TI's own grade —
  class-relative formal residue, not physical issuance). The datum is the admissible-morphism class,
  not a set of admissible states: "what is possible" = "which issuance acts are admissible from
  here," which a state snapshot cannot carry (I-6).
- **PRESERVED BY.** Admissibility-respecting maps of process objects: functor-like maps sending
  admissible morphisms to admissible morphisms and preserving witness structure (not merely
  preserving the induced reachable-state set).
- **CHARACTERISTIC FAILURE / ABSORBER.** The **fixed-family absorber**: a fixed completed family that
  precontains all admissible extensions, making every later "new possibility" a disclosure inside a
  static family. This is the hierarchy's null class 1 (charter Neutrality Rule item 1) and TI's
  fixed-table/fixed-oracle absorber class.
- **DIAGNOSTIC QUESTION.** *What could be issued from here — and is the admissible class itself
  prefix-formed, or precontained by a fixed family?*

### 2.2 Dynamics

- **DATA.** The composition structure of `P` itself: which admissible morphisms compose into
  realizable paths, together with the composition-compatible labels those paths carry. Crucially the
  datum is the **morphism-level path structure**, NOT the induced reachability preorder — RUN-0025
  proves those can differ while the order is identical, and diagnosis 2 makes that executable.
- **PRESERVED BY.** Label-respecting functors: maps preserving composition, identities where present,
  and path labels up to declared isomorphism of the label monoid.
- **CHARACTERISTIC FAILURE / ABSORBER.** The **thin shadow**: replacing dynamics by its induced
  state-order. If a case's every dynamical distinction is recoverable from the thin shadow, the
  process-level typing has bought nothing there (see falsifier F2).
- **DIAGNOSTIC QUESTION.** *How does issuance move within the admitted family — and does the movement
  carry morphism-level structure beyond mere reachability?*

### 2.3 Records

- **DATA.** Traces riding on morphisms: a record is a token `(proposition, value, formation-morphism,
  holder, erasure-cost)` attached to an issuance act and transported along subsequent composition
  until an explicit erasure morphism removes it. Process-level restatement of TaF's record token
  (TaF `FORMALISM.md`, cited at TaF's grade): the formation EVENT is a morphism, persistence is
  functorial transport, and erasure is itself an act — a record is never a bare state fact. TaF's D1
  profile `(A, R, B, C)` is the richest existing model of this level's local datum and is adopted as
  the level's reference structure at TaF-owned grade (componentwise preorder, no scalar collapse).
- **PRESERVED BY.** Trace-preserving maps: process maps carrying formation morphisms to formation
  morphisms, holders to holders injectively on accessible holders, and not decreasing the declared
  erasure-cost model (TaF T18's admissibility shape, cited).
- **CHARACTERISTIC FAILURE / ABSORBER.** Two classical conflations, both already dissociated at
  synthetic grade in this repo's swing suite: (i) **irreversibility ⇒ record** (irreversible dynamics
  with no inspectable trace), and (ii) **record ⇒ access** (a persisting trace nobody can inspect).
  Plus the thin-shadow special case: "records" reconstructed purely from the induced order (content
  vs form — register row I-10's live question).
- **DIAGNOSTIC QUESTION.** *Which distinctions made by issuance persist as inspectable traces — and
  is their persistence carried by morphism-level transport or merely asserted of states?*

### 2.4 Access

- **DATA.** An observer-indexed inspection structure on traces: for each observer position `o` (an
  object-with-morphisms of `P`, not a bare point), the projection `Proj_o` giving which traces can
  condition `o`'s further issuance — TaF's causal availability (formation causally prior + holder in
  the bounded access set) restated so that both relata are morphism-anchored; TI's readout-side
  residue (`Proj`, `kappa`, `Glue` are readout machinery per RUN-0019, cited). Access morphisms are
  the acts that change `Proj_o` without touching the trace set.
- **PRESERVED BY.** Access-equivariant maps: process maps commuting with the projections
  (`Proj` before = `Proj` after, up to the map).
- **CHARACTERISTIC FAILURE / ABSORBER.** **Access–capability conflation**, in both directions:
  counting a visibility/reachability change as enlargement, or normalizing away a relation that is
  constitutive. This is Rank 2's whole battleground and stays a live fork (Rank 2 is BLOCKED at the
  source-packet prerequisite; the pilot earned no directional pressure — referee-corrected).
- **DIAGNOSTIC QUESTION.** *Which persisting traces can condition which observers' further issuance —
  and did an intervention change only this relation?*

### 2.5 Capability

- **DATA.** A **frame-indexed** normalized task structure: given a DECLARED normalization frame `N`
  (task vocabulary; which of description/representation/resource/access/control factors are held
  fixed and at what baseline), the datum is the class of task-realizing issuance compositions
  available to an agent position, quotiented by `N`. **The frame is a parameter of the type, not a
  derived fact.** This is deliberate: Rank 2's construction fork lives here by design, and v0.2
  refuses to hide it — a capability diagnosis without its frame attached is ill-typed. The skeleton's
  check `d1d` exhibits the fork executably: the same intervention classifies differently under two
  distinct declared, non-circular frames.
- **PRESERVED BY.** `N`-frame-respecting equivalences: maps preserving the task vocabulary and the
  held-fixed factors at their declared baselines. Cross-frame comparisons are typed as comparisons of
  PAIRS (diagnosis, frame), never as frame-free facts.
- **CHARACTERISTIC FAILURE / ABSORBER.** (i) **Frame circularity** — the frame entails the verdict
  (detectable: a circular frame classifies the null intervention as a change; the skeleton carries a
  real detector with a failing direction); (ii) **access-constitutive collapse** — all admissible
  frames agree only after access is made constitutive (Rank 2's `FAVORS_RIVAL` branch); (iii)
  **relativist scatter** — equally admissible frames disagree with no invariant quotient.
- **DIAGNOSTIC QUESTION.** *Under the declared frame, did the normalized realizable task set enlarge
  or restrict — or did only visibility, reachability, or control change?*

### 2.6 Finality — the diagnosis of last resort, typed

Kept from v0.1: finality enters only as a **candidate** diagnosis when a real settlement cannot,
under a named search scope and retained constructions, be factored through the five preceding levels
and is not reopened by an admissible continuation. `FINALITY_CANDIDATE` is weaker than finality;
Located-Is-Not-Forced governs. v0.2 adds the level's internal typed structure, from register rows
I-1..I-5 and I-7 (`explorations/INTERPRETATIONS-REGISTER.md`,
`explorations/2026-07-16-boundary-switch-interpretation.md`):

- **DATA.** A **settlement**: a datum `d` riding the process as a composition-compatible flip-odd
  morphism label (the E160 port shape — injected at issuance acts, not derived from contents),
  together with its **switch profile**:

  ```text
  switch_profile(d) = (multiplicity, re-makeability)

  multiplicity   ∈ {per-slice/per-block, global}
  re-makeability ∈ {re-made, set-once}
  ```

  The operator taxonomy (register I-2..I-4) maps onto profiles, not into the datum: A-ongoing =
  (per-slice, re-made); A′ per-sheaf once-bit = (per-slice, set-once); B-live = (global, possibly
  re-made; timing/consequence side-channels only); B-fired-and-forgot and C = (global, set-once;
  behind the opacity horizon).

- **OPERATOR OPACITY (theorem-shaped bound on what the level can ever attribute).** Stated as the
  level's ceiling, at its current grade (derived 2026-07-16, register I-5: candidate mini-theorem,
  toy-executable below, NOT yet a proven theorem over any native formalism):

  > *Opacity bound (draft, toy grade).* The interior of a process object can discriminate a
  > settlement's **switch profile** — multiplicity (a single global choice is invisible because
  > flip-invariant observables see only relative alignments; multiple per-block choices produce
  > observable block-relative alignments) and re-makeability (re-made choices appear as changeable
  > relative alignments; set-once bits do not) — but **never the operator identity**: operator
  > assignments with matched switch profiles are interior-equivalent. Consequently the finality
  > level's diagnosis type is `(instability, susceptibility, lock-in, switch_profile)` and contains
  > no operator field, by construction.

  This is what makes B-type (external operator) an admissible assignment with a provable epistemic
  horizon rather than a metaphysical indulgence, and it is why the level is a diagnosis of last
  resort: even a confirmed settlement licenses profile attribution only.

- **INTERNAL VOCABULARY (the SSB split, register I-7).** Every finality diagnosis decomposes into
  three separately-establishable components — derive instability and susceptibility, never direction:
  - **instability**: the structure admits multiple settlements (the fork exists — for the founding
    case, the ℤ/2 fiber at every tier modeled);
  - **susceptibility**: WHICH injections the structure responds to (the port type — for the founding
    case, exactly the composition-compatible flip-odd morphism label; non-compatible injections
    define nothing, E160 case-5);
  - **lock-in**: whether a settled datum is transported without re-derivation (for the founding case,
    σ-equivariant transport without insertion at toy-family grade).
- **PRESERVED BY.** Flip-equivariant maps of labeled process objects; the settlement datum is
  preserved as an ORBIT, never as a member (the transport results forbid more).
- **CHARACTERISTIC FAILURE / ABSORBER.** (i) A defensible **factorization** through an earlier level
  (enlarged dynamics, boundary conditions, records, access, normalized capability) — Rank 3's
  tournament legs; (ii) **assumed settlement** — the finality criterion presupposing the settlement
  it purports to establish (Rank 3's trap check); (iii) **irreversibility-as-settlement** (banned by
  Rank 3's stop conditions).
- **DIAGNOSTIC QUESTION.** *Does anything remain after every preceding level has had its strongest
  hearing — and if so, what is its switch profile, and nothing more?*

## 3. The first worked finality diagnosis: the fiber corpus, at its corrected grade

The Bounded Fiber Theorem corpus (`synthesis/2026-07-16-bounded-fiber-theorem-v1.0.md`, refereed
pre-commit) is the hierarchy's first worked finality-level diagnosis. Cited AT its referee-corrected
grades, never above:

| SSB component | Finding | Grade (as refereed) |
|---|---|---|
| instability | the sign datum is a ℤ/2 fiber (per-block: (ℤ/2)^blocks under partitioned transport) undetermined at every tier modeled | toy-family exhaustive + shipped-code (T26 surface) + class-relative stipulated-vocabulary proof |
| susceptibility | deriving the orientation requires a flip-symmetry-breaking primitive, whose addition IS positing the datum; physics-side name: sector-asymmetric spectral condition (energy positivity) | class-relative toy-grade no-go (link 8) + REDUCED-toy relocation (link 11) |
| lock-in | the fiber is σ-equivariantly transported without insertion; the arrow is an independent ℤ/2 and cannot substitute | exhaustive-finite toys (links 4, 5, 10) |
| switch profile | OPEN. The per-block observability fixture (Lane 1 item 4a) is the multiplicity discriminator at toy grade; 4b tests A′ descent; neither has run | untested |
| finality VERDICT | **REMAINS_UNDERDETERMINED** — under Rank 3's own discipline the corpus fires "no factor found but search coverage is weak," because coverage-weakness is judged against preregistration/independence/blinding the corpus permanently lacks; a stronger outcome needs a new §5-compliant campaign | referee-corrected receiver update, decisive-tests SYNTHESIS row 3 (which GOVERNS) |

So the worked example demonstrates the level operating exactly as typed: instability, susceptibility,
and lock-in each established at named grades; the switch profile open pending fixtures; the finality
verdict itself withheld — a diagnosis of last resort that has NOT yet been earned, said out loud.
`bar(b)` stays OPEN. Rank 3 stays BLOCKED. Nothing here upgrades the corpus into a tournament pass.

## 4. Executable skeleton

Deterministic pure-Python toy: the base process object, level-typed data, and three diagnoses run
end-to-end — (1) access-change vs capability-enlargement under a declared frame, with a real
frame-circularity detector and the Rank-2 fork exhibited; (2) I-6 made executable (identical thin
shadows, distinct morphism-level datum); (3) the finality level's switch-profile machinery
(multiplicity and re-makeability interior-testable, operator opacity checked, non-derivability of the
absolute bit at 2-block toy scale, E160 composition-compatibility with its case-5 failing direction).

Honesty notes: check `d3d` is an exhaustive computation over 16 selectors — a mini-theorem check
tagged [E] because its outcome was not fixed at formalization time, but it carries toy weight only.
The `lock_in` field in `diagnose_finality` is carried by setup1's composition transport ([T]) and is
vocabulary, not evidence. Nothing in this skeleton touches real physical content.

Proposed repo path: `tests/hierarchy_v02_typed_skeleton.py`.

### 4.1 Source

```python
#!/usr/bin/env python3
"""Hierarchy v0.2 typed skeleton (DRAFT) -- process-level level-typed data
plus three toy diagnoses run end-to-end.

Proposed repo path: tests/hierarchy_v02_typed_skeleton.py

Grade: deterministic synthetic toy. This fixture demonstrates that the v0.2
typed definitions are executable; it is NOT evidence for any physical claim,
moves no source-repo claim, and issues no receiver verdict. bar(b), H59,
Krein positivity, physical issuance stay OPEN.

Design requirement I-6 (static-sheaf amputation): every level's datum here is
defined over a MORPHISM-LABELED process graph (issuance morphisms carrying
composition-compatible labels and traces), never over a state snapshot.
Formal anchors: TI E160 (composition-compatible morphism labels), TI RUN-0025
(thin-shadow warning: morphism-level invariants can differ while the induced
state order is identical).

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
    "d1c: declared frames pass the frame-circularity detector":
        {"tag": "E"},
    "d1c-fail: answer-entailing frame IS flagged by the same detector":
        {"tag": "F",
         "protects": "d1c: declared frames pass the frame-circularity detector"},
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
    "d3c: matched-profile operators (B-fired vs C) give identical interior observables":
        {"tag": "E"},
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
    """A frame entails the answer iff it classifies the NULL intervention as
    a change. Real detector: passes declared frames, flags forced ones."""
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
    can emit multiplicity and re-makeability, never operator identity."""
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
    check("d1c: declared frames pass the frame-circularity detector",
          not frame_is_circular(frame, base)
          and not frame_is_circular(frame_free, base))
    frame_bad = dict(frame, forced_verdict="CAPABILITY_ENLARGEMENT")
    check("d1c-fail: answer-entailing frame IS flagged by the same detector",
          not frame_is_circular(frame_bad, base), expected=False)
    # Rank-2 fork, exhibited: the SAME intervention gets a different diagnosis
    # under a different declared (non-circular) frame. The frame is a
    # parameter of the capability level, not a derived fact.
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

    # exhaustive over all 16 boolean selectors on the 2-block label space
    flip = lambda x: (x[0] ^ 1, x[1] ^ 1)
    space = list(product((0, 1), repeat=2))
    bad = []
    for tt in product((0, 1), repeat=4):
        f = dict(zip(space, tt))
        flip_invariant = all(f[x] == f[flip(x)] for x in space)
        determines_bit = all(f[x] == x[0] for x in space)
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
    print("\nWorked finality diagnosis (toy; SSB vocabulary + switch profile):")
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
```

### 4.2 Output (verbatim, 2026-07-16, exit 0)

```text
HIERARCHY v0.2 TYPED SKELETON -- toy diagnoses
==========================================================================
PASS  [T] setup1: generator-extended labels are composition-compatible by construction: True
PASS  [T] setup2: finality diagnosis emits switch-profile fields only (no operator key): True
PASS  [E] d1a: access-only intervention classifies ACCESS_CHANGE under the declared frame: True
PASS  [E] d1b: admissibility-enlarging intervention classifies CAPABILITY_ENLARGEMENT: True
PASS  [E] d1c: declared frames pass the frame-circularity detector: True
PASS  [F] d1c-fail: answer-entailing frame IS flagged by the same detector: False
PASS  [E] d1d: same intervention classifies differently under a distinct declared frame: True
PASS  [E] d2a: thin shadows identical while the morphism-level invariant differs (I-6): True
PASS  [F] d2a-fail: label-degenerate twin does NOT differ under the same invariant: False
PASS  [E] d3a: per-block injection is choice-visible; global injection is choice-invisible: True
PASS  [F] d3a-fail: single-block model yields NO choice-sensitive flip-invariant observable: False
PASS  [E] d3b: re-made per-block bits give stage-varying alignments; once-bits give fixed: True
PASS  [E] d3c: matched-profile operators (B-fired vs C) give identical interior observables: True
PASS  [E] d3d: no flip-invariant selector on the 2-block label space determines the absolute bit: True
PASS  [E] d3e: compatible morphism-label injection is accepted by the composition checker: True
PASS  [F] d3e-fail: non-composition-compatible injection REJECTED by the same checker: False

EVIDENTIAL CHECKS (headline): 10 [E] + 4 [F] = 14
[T] theorem-consequence checks (no evidential weight): 2

Worked finality diagnosis (toy; SSB vocabulary + switch profile):
  {'instability': True, 'susceptibility': 'composition-compatible flip-odd morphism label', 'lock_in': True, 'switch_profile': {'multiplicity': 'per-block', 're_made': False}}
All checks match expectations. Exit 0.
```

### 4.3 Lint (verbatim, `tef_check_tag_linter.py --strict`, exit 0)

```json
{
  "path": "hierarchy_v02_typed_skeleton.py",
  "convention": "registry",
  "total_checks": 16,
  "tag_counts": { "T": 2, "E": 10, "F": 4 },
  "untagged_count": 0,
  "evidential_count_E_plus_F": 14,
  "T_checks_excluded_from_headline": 2,
  "violations": [],
  "advisories": []
}
```

## 5. Falsifiers

Each falsifier names evidence that would show the corresponding type is **missing, collapsed, or
construction-dependent**, feeding the program's `REVISE_HIERARCHY` receiver update (update vocabulary
and stop conditions of the ranked program are binding). These are receiver-side revision triggers, not
source claims.

- **F1 — possibility.** In real packets, the admissible class can always be re-presented as a fixed
  completed family with changing access (the fixed-family absorber wins everywhere): possibility
  collapses into access; the disclosure/enlargement distinction loses its first leg.
- **F2 — dynamics (and I-6 itself).** Morphism-level data never adds diagnostic power over the
  induced state-order in any real case — every diagnosis is recoverable from the thin shadow. Then
  the process-level typing is decoration and v0.2's central design requirement is falsified
  independently of the six types (this is v0.2's own added stake; see program falsifier).
- **F3 — records.** Record persistence proves coextensive with irreversibility or with access in all
  real cases (never dissociates outside synthetic controls): records is not a distinct type.
- **F4 — access.** No normalization frame can hold access fixed without circularity — all admissible
  frames agree only after access is made constitutive (Rank 2's `FAVORS_RIVAL` branch): the
  access/capability boundary collapses and the hierarchy's load-bearing novel discrimination dies.
- **F5 — capability.** Equally admissible declared frames yield divergent diagnoses with no invariant
  quotient across real cases (operational-context relativism / persistent `CONSTRUCTION_FORK`): the
  level is construction-dependent, and diagnoses must be permanently frame-indexed pairs or the type
  withdrawn.
- **F6 — finality.** Either (i) every real settlement factors through an earlier level under
  adequately covered, preregistered, independent search (Rank 3's defensible-factor branch): the
  level is empty as a diagnosis; or (ii) the switch profile itself proves not interior-testable
  (e.g., the per-block observability fixture 4a fails its [E] legs, or re-makeability cannot be
  stated without smuggling a time label): the level's internal vocabulary collapses and finality
  reverts to v0.1's untyped last-resort placeholder.
- **Program falsifier, v0.2-level statement.** The ranked program's falsifier stands verbatim: if
  several well-chosen real packets either cannot cross the source boundary without semantic
  distortion or repeatedly return construction-dependent, source-specific, or hierarchy-revision
  outcomes with no stable invariant, prefer a pluralist or alternative account and preserve the
  failed synthesis as the result. v0.2 adds one sharper conjunct: if F2 fires — if process-level
  typing never earns its slot over state-snapshot typing on real evidence — then even a surviving
  six-type vocabulary should be rebuilt state-level, and v0.2 (not v0.1) is the artifact that dies.

## 6. Relation to the decisive-test program (no verdicts issued here)

v0.2 changes no receiver update. Rank 1's scoped conditional FAVORS_CANDIDATE, Ranks 2–4 BLOCKED, and
all named repairs (transition-diagnosis run on GU-001-GR-001; two-phase preregistration; source-issued
Rank-2 paired cases + independent Frame R; §5-compliant Rank-3 campaign) stand exactly as the
decisive-tests SYNTHESIS states them. What v0.2 supplies to the program: (a) the typed target that
Rank 2's normalization-frame fork and Rank 4's representation-invariance challenge will test (the
frame-as-parameter design makes Rank 2's fork explicit rather than hidden); (b) the finality level's
diagnosis type that a future Rank 3 campaign would have to instantiate; (c) executable receiver-side
vocabulary with failing directions, lint-clean under the house discipline.

## 7. Nonclaims

- Not validated; not a receiver verdict; not a claim that any physical case instantiates any level.
- The six types are not claimed complete, universal, exclusive, or ontologically real (v0.1 §5 open
  claims all remain open).
- The opacity bound is a candidate mini-theorem at toy grade (register I-5), not a proven theorem
  over any native formalism.
- The fiber corpus citation grades in §3 are the referees' corrected grades; nothing is cited above
  them; `bar(b)`, H59, Krein positivity, physical issuance OPEN.
- TI and TaF structures are cited at their owners' grades (E160/RUN-0025/OnlineIssuance^LC are
  TI-owned; D1/FinaliEvent machinery is TaF-owned); no cross-repo identity is asserted; no source
  claim moves.
- The skeleton is a deterministic synthetic toy; its 14 evidential checks validate instrument
  behavior under stipulated witnesses only.

## 8. Proposed persistence (for the orchestrator; nothing written by this draft)

- This document: `synthesis/2026-07-16-hierarchy-v0.2-typed-definitions-draft.md` (synthesis/ is
  where v0.1 lives and v0.2 is its typed successor; `status: draft_for_joe_review` keeps it below
  ratified-synthesis standing until Joe reviews).
- Skeleton: `tests/hierarchy_v02_typed_skeleton.py` (verbatim §4.1; verified exit 0 and
  `--strict`-clean on 2026-07-16).
- Register update (one row edit, if accepted): I-1..I-5 rows may note "engaged-by-v0.2-draft
  (finality level §2.6/§3)" — statuses stay as-is until fixtures 4a/4b run; I-6 and I-7 stay
  absorbed-into-v0.2.
- Progress-lanes update (if accepted): Lane 2 item 2 gains "DRAFTED 2026-07-16 (v0.2, Joe review
  pending)".
```

---

**Summary for the orchestrator:** Complete Hierarchy v0.2 draft above. All six levels typed process-level over a morphism-labeled issuance graph (I-6 satisfied; E160/RUN-0025 anchored), capability carries the normalization frame as a declared parameter (Rank-2 fork by design), finality typed with switch profiles + operator-opacity bound + SSB vocabulary (register I-1..I-5, I-7 engaged), fiber corpus cited as first worked diagnosis at referee-corrected grades only (finality verdict REMAINS_UNDERDETERMINED per decisive-tests SYNTHESIS row 3). Skeleton verified: exit 0, 10 [E] + 4 [F] + 2 [T], every [F] declares protects, lints clean under `C:/Users/joe/JB/CapacityOS/repos/public/possibility-to-capability/tests/tef_check_tag_linter.py --strict` (0 violations, 0 advisories; verified copy at `C:\Users\joe\AppData\Local\Temp\claude\C--Users-joe-JB\38a54106-9cc3-428a-92e4-2bb753410f40\scratchpad\hierarchy_v02_typed_skeleton.py`). Proposed paths: `synthesis/2026-07-16-hierarchy-v0.2-typed-definitions-draft.md` and `tests/hierarchy_v02_typed_skeleton.py`. No repo writes performed; no receiver verdicts; charter hypothesis unmodified; bar(b)/H59/Krein positivity/physical issuance OPEN.

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs)

# Referee report — Lane D-hierarchy-v02 (Hierarchy v0.2 typed definitions draft)

Re-run receipts: extracted §4.1 byte-for-byte, diffed against the lane's scratchpad copy (IDENTICAL), executed (exit 0, output matches §4.2 verbatim), linted with the repo's `tef_check_tag_linter.py --strict` (registry mode, 0 violations, 0 advisories — §4.3 confirmed). All cited anchors were source-verified: TI E160 (five cases incl. case-5 inconsistent-labels; "supplied table is not a derivation"; composition-compatible label rule — faithful), TI RUN-0025 (`FORMAL-OBJECT.md` line 121, verbatim match), RUN-0019 readout-side (`kappa_i`/`Proj_{o,n}`/`Glue_n` confirmed readout machinery), TaF record token `(id, proposition, value, event, holder, erasure_cost)`, D1 `(A,R,B,C)` componentwise preorder, T18 non-decrease rule — all as cited. Decisive-tests SYNTHESIS rows 1–4 match the draft's §3/§6 characterizations exactly, including Rank 3's `REMAINS_UNDERDETERMINED` conditional. ADAPTER2-01: respected (fiber-not-axis language throughout). No repo writes: confirmed (`tests/hierarchy_v02_typed_skeleton.py` absent from the repo).

## (1) VERDICT: SOUND-WITH-CORRECTIONS

The typed definitions, I-6 process-level compliance, firewall language, and §3's finality-verdict row survive attack. But the swing's own stated purpose — ending process claims without mechanized receipts and cannot-fail controls — is violated once in the burned class, and the draft misstates the current repo state of fixture 4a.

## (2) Defects

**D1 — MAJOR (cannot-fail control, the burned class): the frame-circularity "detector" is structurally incapable of detecting circularity, and d1c is a cannot-fail check tagged [E].**
`frame_is_circular(frame, base)` = `classify_intervention(base, base, frame) != "NO_CHANGE"`. `classify_intervention` and `normalized_capability` are pure functions; on identical arguments they return `NO_CHANGE` for **every** frame lacking the literal `forced_verdict` key. Mechanized receipt: I probed three structurally loaded frames, including a post-hoc answer-entailing vocabulary frame — detector returns False on all (`PROBE A: [False, False, False]`). The detector's positive class is inhabited **only by frames that self-declare** via the `forced_verdict` key — a strawman. So: (a) d1c ("declared frames pass") can never fail for any expressible frame — it is [T]-grade, not [E]; (b) d1c-fail's teeth prove only that a self-flag propagates; (c) §2.5's prose "detectable: a circular frame classifies the null intervention as a change; the skeleton carries a **real detector** with a failing direction" is a claim above evidence. This is exactly the class the R2 referee killed ("the stop-condition detector was vacuous — the burned class") in a subtler costume: constant-False on the declarable-frame class instead of constant-True.
*Corrected wording (§2.5 absorber i):* "frame circularity is detectable by the null-intervention criterion only for frames that misclassify the identity intervention; in this skeleton the only such frames are explicitly forced ones — structural circularity (e.g. post-hoc task vocabulary) is NOT detected at this grade, and building a detector with bite over structurally circular frames is open work." Retag d1c → [T] (or rebuild frames as functions of the intervention so the null test has content); headline becomes 8 [E] + 4 [F] (see D4).

**D2 — MODERATE (factual repo-state error): "neither has run — untested" for fixtures 4a/4b is false for 4a.**
`explorations/2026-07-16-per-block-observability/SYNTHESIS.md` + `tests/per_block_observability_fixture.py` exist at repo HEAD (commit `9f38bc4`, 2026-07-16 08:14 — the repo's most recent commit): 4a ran, closed `ENDPOINT_POSITIVE_TOY` at exhaustive-finite-toy grade with three failing-direction controls ("This run closed 4a"). The draft's §3 switch-profile row ("untested"), §8's register proposal ("statuses stay as-is until fixtures 4a/4b run"), and F6's phrasing all contradict the repo state they report on. The error is conservative in direction (understates evidence) but it is a misstatement in a governance-relevant table, and the skeleton's `choice_visible` machinery substantially re-derives 4a's content without citing the already-run fixture.
*Corrected wording (§3 row 4):* "switch profile: multiplicity leg RUN at exhaustive-finite-toy grade (4a, `ENDPOINT_POSITIVE_TOY`, provisional synthesis `explorations/2026-07-16-per-block-observability/SYNTHESIS.md`; cited at its own grade — no adversarial referee report attached to that run); re-makeability leg (4b) untested; profile as a whole OPEN." Adjust §8 and F6 accordingly; d3a should cite 4a as prior art, not implicit novelty.

**D3 — MODERATE (claim above corpus grade): §2.6's susceptibility bullet asserts the founding case's port is "exactly the composition-compatible flip-odd morphism label."**
The corpus (link 8) establishes: a flip-symmetry-breaking **primitive** is required, class-relative. That the primitive has the E160 morphism-label shape is the A′/boundary-switch **interpretation** (register I-1/I-3, interpretation-tier, "checked, not asserted"), whose descent test is precisely the unrun fixture 4b. §3's susceptibility row states it correctly; §2.6's "exactly" upgrades an interpretation into the level's established internal vocabulary.
*Corrected wording:* "for the founding case, a flip-symmetry-breaking primitive (corpus link 8); the composition-compatible flip-odd morphism label is v0.2's typed candidate for its shape (E160 port reading; fixture 4b untested; non-compatible injections define nothing, E160 case-5)."

**D4 — MODERATE (evidential inflation via inconsistent tagging): d3c is the same by-construction code-property class as setup2, which is tagged [T].**
`interior_observables(story_b) == interior_observables(story_c)` with identical `bits` tests only that the function ignores the `operator` key — precisely what setup2 tests of `diagnose_finality`, tagged [T]. By parity, d3c is [T] (outcome fixed once `interior_observables` is written to read only `bits`). With D1's retag the honest headline is **8 [E] + 4 [F] = 12**, not 14. (d3b is borderline demonstrative arithmetic on hand-picked histories; flag, tolerable at toy grade with the honesty note extended.)

**D5 — MINOR (check weaker than its name): d3d's `determines_bit` tests only `f == projection` (1 of 16 selectors), not bit-determination.**
"Determines the absolute bit" should mean a decoder exists: ∃g with g(f(x)) = x₀. I ran the decoder-quantified version exhaustively (16 f × 4 g): zero counterexamples — the named theorem is true, but the shipped check under-tests it. *Correction:* quantify over decoders in the code, or rename the check "…equals the absolute-bit projection."

**D6 — MINOR (stipulated outputs presented as diagnosis): `diagnose_finality` is a passthrough** — `instability` from a passed parameter, `multiplicity`/`re_made` copied from input, `lock_in` hardcoded (disclosed). The honesty note covers `lock_in` only. *Correction:* extend the note: all four fields of the printed "worked finality diagnosis" are stipulated vocabulary at this grade; the interior-testability evidence lives in d3a/d3b, not in `diagnose_finality`.

**D7 — MINOR (citation path): §1 attributes both anchors to `temporal-issuance/FORMAL-OBJECT.md`; RUN-0025 is there, but E160 lives at `temporal-issuance/explorations/E160-holonomy-transport-functor-derivation-fixture-2026-07-10.md`** (a bounded toy fixture, `claim_movement: false` — cite at that grade). Also: the `CAPABILITY_CHANGE` (restriction) branch of `classify_intervention` is exercised by no check, though §2.5's diagnostic question names restriction; and d1d's "non-circular" certification of `frame_free` rests on the D1-vacuous detector (the fork exhibition itself is genuine computation — fix the wording, keep the check).

**Not defects (attacks that failed):** I-6 compliance is real (all level data ride the morphism graph; d2a is a genuine executable RUN-0025 instantiation with a real failing direction); no receiver verdict is issued anywhere; no source claim moves; north-star/byproduct firewall language is correct and matches progress-lanes; §3's finality-verdict row cites the referee-corrected `REMAINS_UNDERDETERMINED` exactly and names the SYNTHESIS as governing; d3e's composition checker has genuine teeth; d1a/d1b/d1d/d2a/d3a are honest computations; the opacity bound is properly hedged as a candidate mini-theorem at toy grade; register/lanes updates are proposed, not executed.

## (3) What the deliverable actually earns

**Grade: definitional draft + deterministic toy skeleton, conditional on the D1–D7 corrections** — i.e. the draft's own claimed grade (`definitional_draft_plus_deterministic_toy_skeleton`) survives, with the evidential headline corrected downward to **8 [E] + 4 [F] = 12** and the "real frame-circularity detector" claim withdrawn to "forced-frame flag with an open detector-with-bite obligation."

**Receiver update in program vocabulary: none, and none claimed** — correctly. This is Lane 2 item 2 drafting, not a rank execution; Rank 1's scoped conditional `FAVORS_CANDIDATE` and Ranks 2–4 `BLOCKED` stand untouched. What it earns operationally: Lane 2 item 2 may be marked "DRAFTED 2026-07-16 (v0.2, Joe review pending)" **only after** the corrections above are applied (the §3 table and §2.6 susceptibility bullet as shipped misstate the corpus/repo state and should not enter `synthesis/` uncorrected). The falsifier set (§5), including the sharpened F2 conjunct making v0.2 itself the artifact that dies, is well-formed `REVISE_HIERARCHY` feed and is a genuine contribution.

## (4) Stop-condition compliance

- **No rank executed, no rank stop condition triggered.** No normalization chosen after seeing an answer in any real case (Rank 2 stop) — though D1 shows the shipped circularity guard could not have detected it if there were one; no post-hoc factorization pass claimed (Rank 3 stop); no favorable-branch-only publishing (Rank 4 stop).
- **House discipline:** [T]/[E]/[F] registry + `--strict` lint mechanically satisfied and independently reproduced; tag **semantics** violated once (D1: cannot-fail as [E]) and inconsistently applied once (D4) — the exact pattern this swing exists to end, hence the corrections are mandatory, not cosmetic.
- **Charter rules:** source sovereignty held (all TI/TaF citations verified faithful and grade-carrying); Located-Is-Not-Forced held; Failure-Preservation respected (falsifiers first-class); no publication act; frozen-packet rule not implicated (no packet touched).
- **ADAPTER2-01:** no contradiction found; fiber-not-axis maintained throughout.
- **Persistence posture:** compliant — nothing written, `draft_for_joe_review` gating correct, register/lanes edits proposed to the orchestrator rather than executed.