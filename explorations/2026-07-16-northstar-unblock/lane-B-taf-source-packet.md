> Part of the 2026-07-16 north-star unblock swing. Exploration tier; the attached referee report GOVERNS (grades + corrections + firewall verdict). Firewalled lanes (B, C) were audited INDEPENDENT.

# TAF-001: Paired Record-Access / Record-Formation Intervention Evidence Packet (source-issued, v0.1)

**Deliverable status:** content-only proposal. Nothing has been written to any repo. Grades explicit; exploration tier; no TaF claim movement.

---

## Proposed TaF-side path and issuance mechanics

- **Packet directory (new, source-owned):** `exports/packets/TAF-001-paired-record-intervention-v0.1/` in `time-as-finality`. TaF has no `exports/` area today; `results/` holds internal test results and `technical-reports/` holds internal reports, and a source-ISSUED packet is neither — it is an outbound artifact whose bytes must stay frozen independently of internal iteration. If the TaF steward prefers reusing an existing area, the fallback is `results/TAF-001-paired-record-intervention-v0.1/` with a `frozen: true` marker; the `exports/` split is the recommendation.
- **Bundle contents:**
  - `packet.json` — the frozen-packet metadata (field mapping below), `schema_version: "0.2"` per the receiver's contract
  - `blobs/taf001_paired_intervention.py` — the evidence computation (exact bytes as run; SHA-256 `e945cd89fc59e4ab644ec49d4513742ca17911edf760d239eabaebb2e1c8b34c`, 8181 bytes)
  - `blobs/taf001_output.txt` — its captured output (SHA-256 `c3ada0d8367f76638f1ffba7889a748bd355b8fcd4c67262236b08a496f060d0`, 2038 bytes)
  - `blobs/taf001_semantics.md` — the packet body below (before/after objects, task vocabulary, assumptions, grades, residuals, nonclaims); hash computed at issuance
- **Freezing per the `ptc-frozen-bundle-v1` contract:** blobs stored raw with `-text` in `.gitattributes`; manifest entries `(path, byte_length, content_sha256)` sorted by UTF-8 bytes of path, relative POSIX paths, NFC, unique after case folding; `manifest_digest = H(C({canonicalization_profile, entries}))`; `packet_digest` over the packet with the three digest fields zeroed; `bundle_digest = H(UTF8("ptc-frozen-bundle-v1") || 0x00 || bytes(packet_digest) || bytes(manifest_digest))`; `integrity.digest` aliases `bundle_digest`; `hash_scope` equals the manifest path sequence. Digests are computed at issuance time after the TaF steward pins the issuing commit; the two blob hashes above are already final for the exact bytes reproduced in this deliverable.
- **Issuance pin:** `source.repository = time-as-finality`, `source.revision =` the commit containing the bundle (current TaF HEAD for semantics referenced: `8df3cf138855571538768d57e94ca36320f3830b`), `source.source_packet_id = TAF-001`, `packet_status = SOURCE_FROZEN`, `source.claim_status = exploration`, `source.evidence_grade = formal only (finite executable toy model)`.

---

## Packet body (would be frozen as `blobs/taf001_semantics.md`)

### 1. Exact question

Given one fixed finite baseline world W0 in the TaF T1/FORMALISM record model and one shared finite task vocabulary TV, what are the exact task-achievability consequences, under TaF's own reconstruction rule, of (ALPHA) enlarging one observer's bounded holder-access set with the causal record graph held byte-identical, versus (BETA) adding record-formation events to the causal record graph with the observer's access set held byte-identical?

`question.decision_type: other` (this packet decides a computed consequence, not an independence or forcing claim).

### 2. Semantics used (all TaF-owned, none invented)

- **Causal record graph** `G = (E, A)`: finite DAG whose reachability induces `<_c` (FORMALISM, "Causal Record Graph").
- **Record token** `r = (id, proposition, value, event, holder, erasure_cost)`.
- **Causal availability**: a record is available to observer O at event e iff (1) its formation event is `<=_c e` and (2) its holder is in O's bounded access set. Access loss/gain changes condition 2 without creating or deleting records; record formation changes the token inventory and graph. TaF treats these as different operations by definition — that pre-existing distinction is what this packet exercises.
- **Reconstruction rule**: (p, v) is reconstructible for O at e iff accessible support reaches the fixed threshold k and no competing value for p reaches k.
- **D1 profile** `F_O,e(x) = (A, R, B, C)`: accessible support; distinct accessible holders; causal antichain width of accessible supporting formation events; minimum accessible supporting erasures to drop below k. Reported per task; componentwise preorder, no scalarization.
- **Observer level**: reconciler (TaF observer taxonomy). No conscious-observer claim.
- **T46 `RecordAccessSystem` framing**: ALPHA acts on the observer-access side (who can inspect which holders); BETA acts on the generation/propagation side (which records form, where, on what causal paths). The packet uses T46's distinction only as vocabulary; it does not import T46's market/Spanner witnesses.

### 3. Shared baseline world W0 (exact, enumerable)

- Events: `src, a1, a2, b1, b2, c1, d1, d2, f1, f2, f3, f4, e_obs`; edges as in the computation (all formation events causally precede `e_obs`; `a1 <_c a2`; all others pairwise incomparable).
- Holders: `h1, h2, h3, h4`. Observer O access set `{h1, h2}`. Threshold `k = 2`, fixed before evaluation. Evaluation event `e_obs`. Uniform `erasure_cost = 1` (so `C_therm` coincides with `C`; divergence not exercised here).
- Record tokens r1–r11 exactly as in the computation source below (p1=1 at h1,h2 chained; p2=1 at h1,h3; p3=1 at h4 only; p4 split 1@h1 / 0@h2; p5=1 at h1,h2 with p5=0 twice at h3).

### 4. Shared task vocabulary TV (finite, reconstruction-rule sense)

TV = { τ1:(p1,1), τ2:(p2,1), τ3:(p3,1), τ4:(p4,1), τ5:(p5,1) }. A task is achieved in a world iff its pair is reconstructible for O at `e_obs` under k=2. TV is identical for both interventions; that identity is load-bearing for the receiver's comparison and is guaranteed by construction (same proposition-value pairs, same observer, same threshold, same evaluation event).

### 5. Intervention ALPHA — access structure changes, record inventory fixed

- **Before:** W0 with access set `{h1, h2}`.
- **After (W_A):** identical events, edges, and record tokens (byte-identical graph and inventory); access set enlarged to `{h1, h2, h3}`. In T46 terms: an observer-access-side change in `RecordAccessSystem`; in T1 terms: condition 2 of causal availability changes for records held at h3; nothing forms, propagates, or erases.

### 6. Intervention BETA — record formation changes, access fixed

- **Before:** W0 with access set `{h1, h2}`.
- **After (W_B):** access set held byte-identical at `{h1, h2}`; four new record-formation events `n1–n4` (causally after `src`, before `e_obs`) add tokens r12:(p3,1)@h1, r13:(p3,1)@h2, r14:(p4,1)@h2, r15:(p4,0)@h1. In T46 terms: a generation-side change in `RecordAccessSystem`; the causal record graph gains events and tokens at holders already inside the fixed access set.

### 7. Machine-checkable evidence

Computation (pure Python 3, stdlib only, deterministic; exact bytes hashed above):

```python
# TAF-001 evidence computation v0.1
# Pure Python, stdlib only, deterministic. Implements the Time as Finality
# T1/FORMALISM record model: finite causal record graph (DAG), record tokens
# (id, proposition, value, event, holder, erasure_cost), bounded observer
# access sets, the reconstruction rule (fixed threshold + no competing value
# at threshold), and the observer-indexed D1 profile (A, R, B, C).
# Evaluation uses causal reachability only; no topological ordering, metric
# time, or global clock enters the computation (invariance asserted below).

from collections import namedtuple
from itertools import combinations

Record = namedtuple("Record", "id prop value event holder erasure_cost")


def reachability(nodes, edges):
    """Transitive closure of the DAG as a set of ordered pairs (a, b), a <_c b."""
    reach = set(edges)
    changed = True
    while changed:
        changed = False
        for (a, b) in list(reach):
            for (c, d) in list(reach):
                if b == c and (a, d) not in reach:
                    reach.add((a, d))
                    changed = True
    return reach


def causally_leq(a, b, reach):
    return a == b or (a, b) in reach


def accessible_supporting(records, access_set, prop, value, eval_event, reach):
    """Active records supporting (prop, value) causally available to the
    observer at eval_event: formation event <=_c eval_event AND holder in the
    observer's bounded access set (FORMALISM, Causal Record Graph, conds 1-2)."""
    return [r for r in records
            if r.prop == prop and r.value == value
            and r.holder in access_set
            and causally_leq(r.event, eval_event, reach)]


def antichain_width(events, reach):
    """Width of the largest causal antichain among the given formation events."""
    ev = sorted(set(events))
    best = 0
    for n in range(len(ev), 0, -1):
        for combo in combinations(ev, n):
            if all(not causally_leq(x, y, reach) and not causally_leq(y, x, reach)
                   for x, y in combinations(combo, 2)):
                return n
    return best


def d1_profile(records, access_set, prop, value, eval_event, reach, k):
    """F_O,e(x) = (A, R, B, C) per FORMALISM 'Observer-Indexed Finality Profile'."""
    supp = accessible_supporting(records, access_set, prop, value, eval_event, reach)
    A = len(supp)
    R = len({r.holder for r in supp})
    B = antichain_width([r.event for r in supp], reach) if supp else 0
    C = (A - k + 1) if A >= k else 0  # min accessible supporting erasures to drop below k
    return (A, R, B, C)


def reconstructible(records, access_set, prop, value, eval_event, reach, k):
    """FORMALISM 'Reconstruction Rule': accessible support reaches the fixed
    threshold AND no competing value for the same proposition reaches it."""
    A = len(accessible_supporting(records, access_set, prop, value, eval_event, reach))
    if A < k:
        return False
    competing_values = {r.value for r in records if r.prop == prop and r.value != value}
    for v2 in competing_values:
        A2 = len(accessible_supporting(records, access_set, prop, v2, eval_event, reach))
        if A2 >= k:
            return False
    return True


# ---------------------------------------------------------------------------
# Shared baseline world W0
# ---------------------------------------------------------------------------
EVAL = "e_obs"
K = 2  # reconstruction threshold, fixed before evaluation (FORMALISM primitive 6)

BASE_NODES = ["src", "a1", "a2", "b1", "b2", "c1", "d1", "d2",
              "f1", "f2", "f3", "f4", EVAL]
BASE_EDGES = [
    ("src", "a1"), ("a1", "a2"),            # a1 <_c a2 (chained formation)
    ("src", "b1"), ("src", "b2"),
    ("src", "c1"),
    ("src", "d1"), ("src", "d2"),
    ("src", "f1"), ("src", "f2"), ("src", "f3"), ("src", "f4"),
    ("a2", EVAL), ("b1", EVAL), ("b2", EVAL), ("c1", EVAL),
    ("d1", EVAL), ("d2", EVAL),
    ("f1", EVAL), ("f2", EVAL), ("f3", EVAL), ("f4", EVAL),
]
BASE_RECORDS = [
    Record("r1",  "p1", 1, "a1", "h1", 1),
    Record("r2",  "p1", 1, "a2", "h2", 1),
    Record("r3",  "p2", 1, "b1", "h1", 1),
    Record("r4",  "p2", 1, "b2", "h3", 1),
    Record("r5",  "p3", 1, "c1", "h4", 1),
    Record("r6",  "p4", 1, "d1", "h1", 1),
    Record("r7",  "p4", 0, "d2", "h2", 1),
    Record("r8",  "p5", 1, "f1", "h1", 1),
    Record("r9",  "p5", 1, "f2", "h2", 1),
    Record("r10", "p5", 0, "f3", "h3", 1),
    Record("r11", "p5", 0, "f4", "h3", 1),
]
BASE_ACCESS = frozenset({"h1", "h2"})

# Shared task vocabulary TV: five reconstruction tasks in the FORMALISM
# reconstruction-rule sense. A task is achieved in a world iff its
# proposition-value pair is reconstructible for O at e_obs under threshold K.
TASKS = [("tau1", "p1", 1), ("tau2", "p2", 1), ("tau3", "p3", 1),
         ("tau4", "p4", 1), ("tau5", "p5", 1)]

# ---------------------------------------------------------------------------
# Intervention ALPHA: access-structure change only (T46 RecordAccessSystem
# observer-access side). Holder-access set {h1,h2} -> {h1,h2,h3}. The causal
# record graph and record inventory are byte-identical to W0.
# ---------------------------------------------------------------------------
ALPHA_ACCESS = frozenset({"h1", "h2", "h3"})

# ---------------------------------------------------------------------------
# Intervention BETA: record-formation change under fixed access. The observer
# access set stays {h1,h2}. Four new record-formation events (n1-n4) and four
# new record tokens are added to the causal graph (T46 generation/propagation
# side): new propositions' support forms at holders already inside the fixed
# access set.
# ---------------------------------------------------------------------------
BETA_NODES = BASE_NODES + ["n1", "n2", "n3", "n4"]
BETA_EDGES = BASE_EDGES + [
    ("src", "n1"), ("src", "n2"), ("src", "n3"), ("src", "n4"),
    ("n1", EVAL), ("n2", EVAL), ("n3", EVAL), ("n4", EVAL),
]
BETA_RECORDS = BASE_RECORDS + [
    Record("r12", "p3", 1, "n1", "h1", 1),
    Record("r13", "p3", 1, "n2", "h2", 1),
    Record("r14", "p4", 1, "n3", "h2", 1),
    Record("r15", "p4", 0, "n4", "h1", 1),
]


def evaluate(label, nodes, edges, records, access):
    reach = reachability(nodes, edges)
    # Topological-order invariance guard: reachability is computed from the
    # edge set alone; recompute with reversed edge insertion order and assert
    # identity, per the FORMALISM invariance requirement.
    assert reach == reachability(list(reversed(nodes)), list(reversed(edges)))
    print(f"== {label} | access set = {sorted(access)} | threshold k = {K} ==")
    vector = []
    for tname, p, v in TASKS:
        prof = d1_profile(records, access, p, v, EVAL, reach, K)
        ok = reconstructible(records, access, p, v, EVAL, reach, K)
        comp = {v2: len(accessible_supporting(records, access, p, v2, EVAL, reach))
                for v2 in sorted({r.value for r in records
                                  if r.prop == p and r.value != v})}
        vector.append(1 if ok else 0)
        print(f"  {tname} ({p},{v}): D1=(A={prof[0]},R={prof[1]},"
              f"B={prof[2]},C={prof[3]}) competing_accessible_support={comp} "
              f"reconstructible={ok}")
    print(f"  achievability vector over TV = {tuple(vector)}")
    print()
    return tuple(vector)


w0 = evaluate("W0  baseline", BASE_NODES, BASE_EDGES, BASE_RECORDS, BASE_ACCESS)
wa = evaluate("W_A ALPHA (access change, records/graph fixed)",
              BASE_NODES, BASE_EDGES, BASE_RECORDS, ALPHA_ACCESS)
wb = evaluate("W_B BETA (record formation added, access fixed)",
              BETA_NODES, BETA_EDGES, BETA_RECORDS, BASE_ACCESS)

print("summary:")
print(f"  W0  = {w0}")
print(f"  W_A = {wa}")
print(f"  W_B = {wb}")
print(f"  ALPHA newly achievable: "
      f"{[t[0] for t, x, y in zip(TASKS, w0, wa) if y > x]}")
print(f"  ALPHA newly unachievable: "
      f"{[t[0] for t, x, y in zip(TASKS, w0, wa) if y < x]}")
print(f"  BETA  newly achievable: "
      f"{[t[0] for t, x, y in zip(TASKS, w0, wb) if y > x]}")
print(f"  BETA  newly unachievable: "
      f"{[t[0] for t, x, y in zip(TASKS, w0, wb) if y < x]}")
```

Captured output (exact bytes hashed above):

```text
== W0  baseline | access set = ['h1', 'h2'] | threshold k = 2 ==
  tau1 (p1,1): D1=(A=2,R=2,B=1,C=1) competing_accessible_support={} reconstructible=True
  tau2 (p2,1): D1=(A=1,R=1,B=1,C=0) competing_accessible_support={} reconstructible=False
  tau3 (p3,1): D1=(A=0,R=0,B=0,C=0) competing_accessible_support={} reconstructible=False
  tau4 (p4,1): D1=(A=1,R=1,B=1,C=0) competing_accessible_support={0: 1} reconstructible=False
  tau5 (p5,1): D1=(A=2,R=2,B=2,C=1) competing_accessible_support={0: 0} reconstructible=True
  achievability vector over TV = (1, 0, 0, 0, 1)

== W_A ALPHA (access change, records/graph fixed) | access set = ['h1', 'h2', 'h3'] | threshold k = 2 ==
  tau1 (p1,1): D1=(A=2,R=2,B=1,C=1) competing_accessible_support={} reconstructible=True
  tau2 (p2,1): D1=(A=2,R=2,B=2,C=1) competing_accessible_support={} reconstructible=True
  tau3 (p3,1): D1=(A=0,R=0,B=0,C=0) competing_accessible_support={} reconstructible=False
  tau4 (p4,1): D1=(A=1,R=1,B=1,C=0) competing_accessible_support={0: 1} reconstructible=False
  tau5 (p5,1): D1=(A=2,R=2,B=2,C=1) competing_accessible_support={0: 2} reconstructible=False
  achievability vector over TV = (1, 1, 0, 0, 0)

== W_B BETA (record formation added, access fixed) | access set = ['h1', 'h2'] | threshold k = 2 ==
  tau1 (p1,1): D1=(A=2,R=2,B=1,C=1) competing_accessible_support={} reconstructible=True
  tau2 (p2,1): D1=(A=1,R=1,B=1,C=0) competing_accessible_support={} reconstructible=False
  tau3 (p3,1): D1=(A=2,R=2,B=2,C=1) competing_accessible_support={} reconstructible=True
  tau4 (p4,1): D1=(A=2,R=2,B=2,C=1) competing_accessible_support={0: 2} reconstructible=False
  tau5 (p5,1): D1=(A=2,R=2,B=2,C=1) competing_accessible_support={0: 0} reconstructible=True
  achievability vector over TV = (1, 0, 1, 0, 1)

summary:
  W0  = (1, 0, 0, 0, 1)
  W_A = (1, 1, 0, 0, 0)
  W_B = (1, 0, 1, 0, 1)
  ALPHA newly achievable: ['tau2']
  ALPHA newly unachievable: ['tau5']
  BETA  newly achievable: ['tau3']
  BETA  newly unachievable: []
```

**Computed facts the packet asserts (nothing more):**
1. ALPHA changes the achievability vector from (1,0,0,0,1) to (1,1,0,0,0) with zero change to the record inventory or causal graph: τ2 becomes achievable (previously-formed records at h3 become causally available), and τ5 becomes UNachievable (enlarged access makes a competing value reach threshold). Access enlargement is not monotone in task achievability under TaF's own reconstruction rule.
2. BETA changes the vector from (1,0,0,0,1) to (1,0,1,0,1) with the access set byte-identical: τ3 becomes achievable via new record-formation events at already-accessible holders; τ4 stays unachievable because the added formation events also raise a competing value to threshold (the no-competing-value clause binds).
3. The two interventions produce different achievability deltas over the same TV ({τ2 on, τ5 off} vs {τ3 on}), and each delta is unreachable by the other intervention within this world family: τ3's only supporting record in W0/W_A sits at h4, outside even the enlarged access set; τ2's second record sits at h3, outside BETA's fixed access set.
4. Per-task D1 profiles (A,R,B,C) before/after are as printed; the profile remains a componentwise preorder throughout (no scalarization was used to decide anything).
5. Results are invariant under evaluation order: reconstruction is computed from causal reachability alone; the invariance assertion in `evaluate` passes.

### 8. Assumptions (all load-bearing, all explicit)

- A1 (definition): TaF T1/FORMALISM record model — causal record graph, record tokens, causal-availability conditions 1–2, reconstruction rule, D1 profile.
- A2 (construction_choice): threshold k=2, fixed before evaluation; evaluation event `e_obs` causally after all formation events; uniform erasure_cost=1.
- A3 (construction_choice): the specific finite worlds W0, W_A, W_B and TV above. These are designed witnesses, not sampled or physically measured systems.
- A4 (implementation): the embedded Python program correctly implements A1 over A3.
- A5 (definition): "task achievability" means reconstructibility under the reconstruction rule — TaF's native notion, chosen because it is the only task semantics TaF owns. If the receiver's normalization frame uses a different task semantics, mapping is the receiver's work.

### 9. Grades

- Overall packet: **exploration tier**; `source.evidence_grade = formal only` in TaF's T22 confidence vocabulary (finite executable toy model; no physical substrate).
- Method M1 (ALPHA evaluation): computation grade — deterministic, stdlib-only, output embedded and hashed; verification = rerun script, byte-compare output.
- Method M2 (BETA evaluation): same grade, same verification.
- Argument grade for fact 3 (delta non-interchangeability): direct finite inspection, stated in the output; argument only, no general theorem.
- Nothing here is "physically supported" or "partially supported" in TaF's ledger sense, and this packet does not change the status of any TaF claim (R1, A1, PO1, CS1, D1, T46 verdicts all untouched).

### 10. Evidence structure (v0.2 dependency honesty)

- `method_ledger`: M1, M2. `raw_method_count = 2`; `raw_method_count_is_independence_count = false`.
- `premise_ledger`: A1–A5, with A1, A2, A3, A4 load-bearing for BOTH methods; A5 load-bearing for both.
- `shared_load_bearing_premise_ids = [A1, A2, A3, A4, A5]` — the two methods share their entire premise base and implementation; they are two evaluations of one model, not two independent evidential legs.
- `method_dependency_edges`: M1→M2 and M2→M1 `shares_implementation` and `shares_data` (same baseline W0).
- `claim.independence_scope` (source's exact wording, to be copied byte-for-byte by any receiving assessment): "The ALPHA and BETA evaluations share one implementation, one baseline world, and one task vocabulary; they are not evidentially independent methods, and this packet asserts no independence result of any type." `independence_type: not_applicable`. `convergence: not_applicable`.

### 11. Residuals

- R-1: Whether the fact-3 non-interchangeability generalizes beyond this witness family is open; a different world could let an access change and a formation change produce identical deltas.
- R-2: The τ5 non-monotonicity depends on the no-competing-value clause; under a task semantics without that clause the ALPHA delta would be monotone. Sensitivity to the clause is not swept here.
- R-3: `C_therm` vs `C` divergence is not exercised (uniform erasure costs). A receiver needing cost-ordering evidence needs a further packet.
- R-4: Interventions are evaluated separately from W0; the composite ALPHA∘BETA world is not computed.
- R-5: T46's open-causal vs closed-synchronization scarcity distinction is used as vocabulary only; neither witness models propagation delay or quorum rules.

### 12. Nonclaims (what TaF does NOT claim)

- TaF does not classify either intervention under any receiver taxonomy. In particular this packet deliberately assigns no diagnostic label of any kind to ALPHA or BETA; "changes the access structure" and "changes record formation under fixed access" are mechanical descriptions of which TaF object was edited, not classifications of what kind of change occurred. Labeling is the receiver's job; any label the receiver assigns is receiver-owned and must not be attributed to TaF.
- No claim that reconstructibility is the correct or unique normalization of "task capability" — only that it is TaF's native task semantics (A5).
- No physics: nothing here derives relativity, `c`, measurement, thermodynamic cost, or real market/consensus behavior (T46's own constraint list is inherited).
- No TaF claim status changes; no statement about GU, Temporal Issuance, or any other repository.
- Two methods are not two independent evidential units (Section 10).
- The designed witnesses do not establish that real systems exhibit these deltas.

### 13. Source-sovereignty statement

Time as Finality owns the semantics (record model, reconstruction rule, D1 profile, T46 access vocabulary), the witness worlds, the computation, and every statement in this packet, at the pinned revision. The receiving repository (`possibility-to-capability`) owns any classification, normalization framing, gate verdict, or diagnosis built on this packet, and owns it separately — nothing the receiver concludes upgrades, downgrades, or reinterprets any TaF claim, and TaF's issuance of this packet endorses no receiver-side conclusion. `ownership.authority_transfer = false`. This packet was authored without access to the receiver's diagnostic frames, expectation matrices, or forecasts (firewalled lane; see audit declaration below).

### 14. Interfaces

- `target_repository: possibility-to-capability`; `requested_datum:` classification of the ALPHA/BETA pair under the receiver's preregistered frames; `ownership_status: target_owned`.
- No datum is requested from GU or Temporal Issuance by this packet.

---

## Files consulted (audit declaration)

Read in full or in part; nothing else was read, and no agent read anything on my behalf:

1. `C:/Users/joe/JB/CapacityOS/repos/public/possibility-to-capability/governance/CHARTER.md` (full)
2. `C:/Users/joe/JB/CapacityOS/repos/public/possibility-to-capability/experiments/2026-07-14-ranked-decisive-test-program-v0.1.md` — heading lines only via regex `^#{1,3} ` (to locate section boundaries), then lines 104–169 (the Rank 2 section) only
3. `C:/Users/joe/JB/CapacityOS/repos/public/possibility-to-capability/packets/README.md` (full)
4. `C:/Users/joe/JB/CapacityOS/repos/public/possibility-to-capability/packets/schema/` — directory listing; `frozen-packet-v0.2.md` (full); `frozen-packet-v0.2.schema.json` (full)
5. `C:/Users/joe/JB/CapacityOS/repos/public/time-as-finality/` — top-level directory listing; `git rev-parse HEAD`; `results/` and `technical-reports/` directory listings (names only); a filename-level grep for "packet" (paths only, no contents opened)
6. `C:/Users/joe/JB/CapacityOS/repos/public/time-as-finality/FORMALISM.md` (full)
7. `C:/Users/joe/JB/CapacityOS/repos/public/time-as-finality/tests/` — directory listing (names only); `tests/T46-open-causal-scarcity-synchronization-boundary.md` (full)
8. Scratchpad only (written and executed, outside all repos): `C:\Users\joe\AppData\Local\Temp\claude\C--Users-joe-JB\38a54106-9cc3-428a-92e4-2bb753410f40\scratchpad\taf001_paired_intervention.py` and `taf001_output.txt`

Not read: anything under P2C `explorations/`, `synthesis/`, `tests/`, `packets/intake/`, `packets/imports/`, other ranks of the test-program file, or any file whose name contains 'R2', 'access-capability', 'pilot', 'decisive-tests', 'fiber', or 'lane'. TaF's TESTS.md was listed as permitted but was not needed and was not opened; no other TaF file was opened (the grep in item 5 returned paths only, none opened).

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs)

# REFEREE REPORT — Lane B-taf-source-packet (TAF-001)

**Referee re-execution receipts (2026-07-16):**
- Scratchpad blobs exist and match the packet's claims exactly: `taf001_paired_intervention.py` SHA-256 `e945cd89…b34c`, 8181 bytes; `taf001_output.txt` SHA-256 `c3ada0d8…60d0`, 2038 bytes.
- Embedded source block compared line-by-line against the hash-verified blob: identical.
- Re-run: exit 0; rerun output SHA-256 equals the blob's hash — byte-identical reproduction.
- TaF repo verified at claimed HEAD `8df3cf138855571538768d57e94ca36320f3830b`, working tree clean, no `exports/` directory, no TAF-001 file anywhere. P2C tree clean, no TAF-001 written. "Content-only, nothing written" is accurate.
- Semantics audited against `time-as-finality/FORMALISM.md` and `tests/T46-…md`: record token tuple, causal-availability conditions 1–2, reconstruction rule (threshold + no-competing-value), D1 = (A,R,B,C) including C = A−k+1 for A≥k, componentwise preorder with no scalarization, reconciler observer level, T22 vocabulary ("formal only") — all faithful. T46's RecordAccessSystem / open-causal vs closed-synchronization / NYSE-Spanner scope accurately represented and correctly used as vocabulary only.
- Adversarial probes (`referee_taf001_probe.py`, receipts above): **P1** a formation-only intervention inside W0 (add `(p2,1)@h2`, `(p5,0)@h1`, `(p5,0)@h2`, access fixed `{h1,h2}`) reproduces ALPHA's exact vector `(1,1,0,0,0)`. **P1b** exhaustive sweep of all 16 access sets: none reproduces BETA's vector. **P2** `reachability()` never reads its `nodes` parameter; closure is identical with reversed inputs and with `nodes=[]` — the "invariance guard" assert cannot fail on any input.
- Schema audit against `packets/schema/frozen-packet-v0.2.schema.json` and the `ptc-frozen-bundle-v1` profile: digest mechanics quoted correctly; field enums used (`decision_type: other`, `independence_type/convergence: not_applicable`, `shares_implementation`/`shares_data`) all valid; but the field mapping is incomplete (D4).
- ADAPTER2-01 (GU-owned fiber-not-axis correction): the packet makes no bar(b), axis-polarity, or cross-repo identity claim and explicitly nonclaims GU/TI statements. No contradiction possible; none found.

## (1) VERDICT: **SOUND-WITH-CORRECTIONS**

The evidence core is real, mechanized, byte-reproducible, semantically faithful to TaF, correctly graded exploration/formal-only, and honest about its two-methods-one-model dependency structure. But one mechanized receipt is a cannot-fail control, one computed-facts claim overstates in exactly the direction that would flatter the receiver's access/capability boundary, the "source-issued" status outruns what exists, and the schema-conformance implication is not yet earned.

## (2) Defects

**D1 — MODERATE — Cannot-fail control presented as a mechanized invariance receipt.**
The "topological-order invariance guard" in `evaluate` asserts `reach == reachability(reversed(nodes), reversed(edges))`. `reachability` ignores `nodes` entirely, and the transitive closure of an identical edge *set* is unique; the assert compares a deterministic pure function's output with itself (probe: identical even with `nodes=[]`). It can never fail, so packet fact 5's "the invariance assertion in `evaluate` passes" is a receipt-shaped non-receipt — the precise pattern this swing exists to end. The underlying claim is nonetheless true *by construction* (the code never consumes any event ordering), which is verifiable by inspection, not by this assert.
*Corrected wording (fact 5):* "Reconstruction is computed from causal reachability alone; no topological ordering, timestamp, or clock is consumed anywhere in the implementation, so FORMALISM's topological-invariance requirement is satisfied by construction (verifiable by code inspection). The embedded assert is a tautological guard and carries no evidential weight." Or replace it with a real control: an order-consuming evaluation variant checked against the order-free one.

**D2 — MODERATE — Fact 3 overstates delta non-interchangeability; R-1 mis-scopes the open question.**
"Each delta is unreachable by the other intervention within this world family" reads as type-level non-interchangeability. Probe P1: a BETA-type intervention (record formation only, access byte-identical at `{h1,h2}`) reproduces ALPHA's *entire* delta {τ2 on, τ5 off} inside W0 itself. The non-interchangeability is one-directional: no access set over W0 yields BETA's delta (P1b, exhaustive), but formation edits under fixed access *can* simulate this access edit's task-delta. R-1's "a different world could let an access change and a formation change produce identical deltas" is therefore wrong in scope — it is demonstrably true in W0, no different world needed. This is not pedantry: the direction of simulability is factorization-relevant for the receiver (whether access-deltas factor through formation-deltas bears directly on whether the access/capability boundary has independent explanatory value), and the current wording leans the packet toward the boundary-friendly reading. Additionally, the grade note "direct finite inspection, stated in the output" overreaches: the deltas are in the output; the unreachability argument is prose only.
*Corrected wording (fact 3):* "The two specific interventions produce different deltas ({τ2 on, τ5 off} vs {τ3 on}). Asymmetry: no access-set change of W0 can produce BETA's delta (p3 has a single token, so its accessible support is ≤1 under every access set), but a different formation-only intervention under the same fixed access set reproduces ALPHA's delta exactly (add (p2,1)@h2, (p5,0)@h1, (p5,0)@h2). Access-edits and formation-edits are not symmetric intervention classes in this world: formation subsumes this access delta; the converse fails." Delete or rewrite R-1 accordingly.

**D3 — MODERATE — "Source-issued" above evidence; identifier and freeze status not yet TaF's.**
The title says "(source-issued, v0.1)" and the mechanics assert `packet_status = SOURCE_FROZEN`, `source_packet_id = TAF-001`, `claim_status`, `evidence_grade` as source facts, while no TaF steward act exists (verified: clean tree, no bundle, no commit). The program's boundary rule — no receiver may create a source-issued identifier or digest — applies with full force to a P2C-program lane drafting *as* the source, however well firewalled: the identifier, freeze status, and grades become source-issued only upon TaF-side adoption at a pinned commit. The body mostly hedges correctly ("content-only proposal", "would be frozen", "TaF steward pins"); the title and metadata assertions outrun the hedges.
*Corrected wording:* retitle "source-issuable draft packet, v0.1 (pending TaF steward adoption at a pinned commit)"; mark `TAF-001` as a proposed identifier the TaF steward may reassign; state that `SOURCE_FROZEN` and all `source.*` fields attach only at TaF-side issuance.

**D4 — MINOR/MODERATE — Conformance implied, mapping incomplete.**
"`packet.json` — the frozen-packet metadata (field mapping below), `schema_version: "0.2"` per the receiver's contract" implies validity, but the deliverable never supplies required v0.2 fields: `construction_forks` (minItems 1, with `transfer_status` — substantive here: k=2, the designed witness family, and reconstructibility-as-task-semantics are exactly such forks), `quantifiers`, the `claim` block (`statement`, `scope`, `method_count`, `joint_argument_artifact`, `source_status_unchanged`), `verification` (`artifacts`, `replication_status`), `source.artifact_paths`, `source.issued_at`, `alternatives`; per-method `artifact_path`/`artifact_revision` and per-premise `source_artifact_path` are also unstated. As drafted the packet would fail `frozen-packet-v0.2.schema.json` validation.
*Corrected wording:* "partial field mapping; the full v0.2 required field set (enumerated) is completed at issuance; this draft does not yet validate against the schema."

**D5 — MINOR — Over-cited "by definition" for the access/formation distinction.**
FORMALISM's explicit different-operations sentence contrasts access *loss* (condition 2) with *erasure/deactivation*, not with record formation, and says nothing about access *gain*. The packet's "Access loss/gain… record formation… TaF treats these as different operations by definition" extends the citation beyond its text. The distinction is genuinely present in the model's structure (condition-2 membership vs token inventory/graph), so the fix is attribution, not substance.
*Corrected wording:* "the model's structure separates these operations (condition-2 membership vs token inventory and graph); FORMALISM states the loss-vs-erasure case explicitly, and the gain and formation cases follow from the same primitives."

**D6 — ADVISORY (no fault under the lane's own constraints) — Intent framing travels in the clear.**
Section headers and fact-1 glosses announce which TaF object each intervention edited ("access structure changes" / "record formation under fixed access"). These are TaF-native mechanical descriptions, no receiver taxonomy label appears anywhere, and the nonclaims section explicitly fences labeling as receiver-owned — the packet is **not** spoiled. But a careful receiver run should classify from the frozen blobs with the framing prose quarantined, since the source's factor-targeting intent otherwise arrives unsealed. The lane could not have known any receiver-side sealing convention (firewalled), so this is a handling note for the receiver, not a defect charged to the source.

**Checked and cleared:** hashes and byte lengths (exact); rerun (byte-identical); FORMALISM fidelity including C = A−k+1 and the componentwise preorder with no scalarization; the no-competing-value mechanism behind the τ5 flip and the τ4 BETA result (both recomputed, correct); T46 scope and constraint inheritance; T22 "formal only" grading; the v0.2 dependency-honesty block (M1/M2 correctly declared non-independent, `raw_method_count_is_independence_count = false`, independence `not_applicable` — exemplary use of the contract); no TaF claim movement (none claimed, none moved); no ADAPTER2-01 contradiction; no receiver-fiat move (all classification explicitly deferred, `authority_transfer = false`); nothing written to any repo; the `exports/` placement reasoning matches the actual TaF layout (verified: no exports dir; `results/` and `technical-reports/` exist as described).

## (3) What the deliverable actually earns

**Grade: exploration tier, formal-only (TaF T22 vocabulary), computation grade for the two evaluations — confirmed as claimed, with D1–D5 corrections applied.** The packet's computed facts 1, 2, 4 stand as verified machine-checked facts about TaF's own record model on designed finite witnesses; fact 3 stands only in its corrected one-directional form; fact 5 stands as a by-construction property, not a mechanized receipt.

**Receiver update in program vocabulary:** Rank 2 remains **`BLOCKED`** at the source-packet prerequisite — this deliverable does not change that, because nothing is source-issued until the TaF steward adopts and commits the bundle (D3). Conditionally: **if** TaF issues this packet (corrections applied, full v0.2 field set, pinned commit, computed digests), it discharges the "a source-issued frozen packet for each case" prerequisite for *one formal case pair*, with the shared-TV prerequisite satisfied by construction. It cannot by itself open a Rank-2 run: the program still requires at least two independently defended normalization frames including an independently frozen access-constitutive rival, and preregistered receiver predictions — all absent and correctly not attempted here. No `FAVORS_*` movement of any kind is earned or claimed.

Two genuinely receiver-valuable formal facts ride along at toy grade: (i) access enlargement is **non-monotone** in task achievability under TaF's no-competing-value semantics (τ5), which stress-tests any receiver normalization that treats access saturation as capability-revealing; (ii) the corrected simulability asymmetry (formation edits can reproduce this access edit's delta; no access edit can reproduce the formation delta), which is directly relevant to whether access-deltas factor through formation-deltas. Both are consequences the receiver must classify; neither is a diagnosis.

## (4) Stop-condition compliance

**Respected.** Program Rank-2 stops: no normalization frame was chosen at all (none authored — the packet correctly declares task-semantics mapping receiver work, A5); no source/receiver evidence blending (every evidential object is TaF-native; the receiver's contract is used only as packaging format, which is its purpose). Issuer blindness to receiver diagnostic labels: satisfied via the firewall (see below). Charter rules: source-sovereignty respected in substance with the D3 issuance correction required before anything is represented as issued; frozen-packet rule followed in mechanics; nothing written, nothing published, no external action (both repo trees verified clean). One caveat with referee force: "no agent read anything on my behalf" and the files-consulted list are self-reports — the process discipline is honest but not mechanized, the same receipt gap this program is trying to close on all lanes.

## (5) FIREWALL VERDICT: **INDEPENDENT**

Evidence:
- **(a) Declaration audit:** every listed item is permitted. The experiments file was accessed as heading-locations plus lines 104–169 only — the program's Rank-2 section, which the firewall explicitly allows. `packets/README.md` and the schema files are not on the forbidden list and contain no Rank-2 receiver material. TaF files are the lane's own source domain. Nothing listed touches `explorations/`, `synthesis/`, other program ranks, or any forbidden filename pattern.
- **(b) Tell-tale scan against `lane-R2-access-capability-pilot.md` (read by this referee in full):** none of the receiver's frame names (Frame N / Frame R / NAIVE), diagnosis labels (`ACCESS_CHANGE` / `CAPABILITY_CHANGE` / `NO_CHANGE`), or machinery terms (completion class, `Δop`, `Δ(c)`, completion-ROBUST/RELATIVE, declared factor vocabulary, record-channel inventory, evidence-functionality, sealed intent label, POMDP worlds) appears anywhere in the lane B deliverable. Every shared term it does use — "shared task vocabulary", "normalization frame", "diagnostic labels", "preregistered" — occurs verbatim in the permitted Rank-2 section. Design divergence is further positive evidence: lane B built reconstruction-rule task semantics (not POMDP policy semantics), supplied no completion-lattice sweep (the receiver pilot's central instrument), and constructed an access intervention that is *non-monotone* — a case type the receiver's pilot never contemplated and one that actually stresses the receiver's Frame-N saturation intuition. A contaminated lane would be expected to match the receiver's machinery; this one cuts across it.
- **One near-miss, examined and dismissed:** §13's phrase "expectation matrices" does not occur in the permitted Rank-2 section. It appears solely inside the negative access declaration — exactly where the lane's own firewall tasking vocabulary would surface — and carries zero accompanying content from the forbidden file (no frame names, no matrix entries, no forecast wording). Not contamination evidence.
- **Caveat:** the declaration itself is self-reported and cannot be mechanized post hoc; the INDEPENDENT verdict (rather than UNVERIFIABLE) rests on the complete absence of vocabulary and design traces where contamination would be expected to leave them.