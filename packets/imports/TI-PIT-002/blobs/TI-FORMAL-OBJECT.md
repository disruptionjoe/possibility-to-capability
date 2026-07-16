---
artifact_type: formal_object
status: speculative
governance_role: mathematical_seed
claim_refs:
  - TI-C003
constitutional: false
---

# Formal Object

Initial object:

```text
IssuanceSystem = (
  R,          realized events / constraints
  <,          realization-dependency order
  mu,         issuance measure on realized structure
  dR,         frontier between unrealized and realized
  O_i,        observer sites
  kappa_i,    local record-keeping cadence for each observer
  A_i,        access relation: what observer i can inspect
  G,          gluing / reconciliation rules across observers
)
```

## Current Pressure Result

RUN-0012 weakened this object. RUN-0019 weakened the RUN-0014 survivor further. The current working target is no longer the launch object as written, and the local gluing survivor should be treated as readout-side until proven otherwise.

See `FORMAL-OBJECT-PRESSURE-RESULTS.md`.

RUN-0012 working sketch:

```text
LocalIssuancePatch_i = (
  R_i,
  <=_i,
  A_i,
  kappa_i,
  G_ij
)
```

`mu` is demoted to an unresolved measure candidate. Global `dR` remains killed.

RUN-0019 bridge sketch:

```text
SourceRealization = (
  C,
  <=_S,
  Ext_S
)

ObserverReadout_i = (
  A_i,
  kappa_i,
  Rec_i
)

ProjectionAndReconciliation = (
  pi_TaF,
  G_ij,
  Omega_ij
)
```

`kappa_i`, `G_ij`, and `Omega_ij` survive as observer-readout, reconciliation, and audit machinery. They should not be treated as source-side primitives unless a future model shows that they constrain source extensions rather than projected records.

RUN-0021 ontology-resolution correction:

Do not treat `SourceRealization` as one survivor. Treat its source-side components independently:

```text
C
<=_S
Ext_S
```

Each component needs its own absorber threats, kill criteria, resurrection criteria, and status. The next research run should use `explorations/E003-source-residue-ontology-competition-brief.md` to compare source-side ontology competitors, including `NULL-SURVIVOR`.

RUN-0022 steelman correction:

The strongest constructive reading treats `Ext_S` as the likely load-bearing component:

```text
source-side constraints become admissibly extended,
and observer histories are lossy projections of that extension.
```

Use `HYPOTHESIS-STEELMAN.md` as the strongest target and `explorations/E005-ontology-competition-fixture-suite.md` as the shared test surface for ontology competition.

RUN-0024 ontology competition result:

The fixture-based competition in `explorations/E006-ontology-survivor-competition-results.md` separates the source-side components:

| Component | RUN-0024 status | Formal consequence |
| --- | --- | --- |
| `C` | weakened, carrier only | Must be typed by the next `Ext_S` model; not an independent survivor. |
| `<=_S` | killed as independent source-side primitive | Preserve only as a derived invariant or shadow of a successful extension rule. |
| `Ext_S` | formalizing next test target | Must be specified with a typed carrier, projection map, quotient, witness or invariant, transformation consequence, absorber comparison, and kill condition. |

The next formal pass after RUN-0024 should not defend source order first. RUN-0028 attempted the minimal realization branch and showed that a nontrivial `F` requires a weight `Q`. The remaining `Ext_S` no-go now turns on whether `Q` can be source-defined rather than absorbed by transition-system, proof, computation, constructor/resource, thermodynamic, information-theoretic, variational, or time-as-finality accounting.

RUN-0025 category-first correction:

`Ext_S` should be modeled first as a category or category-like structure:

```text
objects: typed source states or constraint states C
morphisms: admissible extensions e: S -> S'
```

The relation `<=_S` is then the thin reflection:

```text
S <=_S S' iff Hom_Ext(S, S') is nonempty
```

If identities and composition are present, this relation is a preorder. It becomes a partial order only after quotienting mutual reachability or imposing antisymmetry conditions. RUN-0025 proves that morphism-level extension invariants can differ while the induced order is identical, so future formal work should not replace `Ext_S` with `<=_S`.

RUN-0026 conditional Lorentzian realization target:

If the source-extension object tries to touch mass-energy, the formal object is not `E = mc^2`. RUN-0026 made the next object a realization functor:

```text
F: ExtCat -> LorHist(M, eta, A)
```

where `LorHist(M, eta, A)` is a category of Lorentzian histories with action `A`. The functor must preserve extension composition as history composition. If `A` is Poincare-invariant and Noether currents exist, ordinary relativistic energy-momentum follows for timelike realized extensions. This is a conditional theorem target, not a substrate claim.

RUN-0028 minimal realization result:

A minimal nontrivial realization functor can be constructed only after adding a morphism-level source invariant:

```text
Q: Mor(ExtCat) -> ([0, infinity), +)
```

The toy target is metric-sensitive Lorentzian history:

```text
F: TI_Ext^Q -> LorHist_g(M)
Tau(F(e)) = alpha Q(e)
```

This preserves same-order/different-extension distinctions when `LorHist_g(M)` remembers proper time. It fails if the target is reduced to causal preorder alone. The result is a kinematic control model, not a physical bridge: `Q`, `(M, g)`, action, Poincare symmetry, and Noether machinery are not derived.

RUN-0049 predictive/accessibility fixture interface:

This is an optional `TI-C020` physical-bridge interface. It does not replace `Ext_S`,
`OnlineSchemaSys`, D-FORK, or the MLTT `Compat_G` formalization. It exists to test whether a
predictive-to-accessible transition is fixed-H readout or H-growing issuance.

```text
P_n       predictive state/process space at stage n
A_n       accessible record or observable algebra at stage n
rho_n     readout/projection map P_n -> A_n
H_fixed   null model: one fixed Hilbert/state/observable space with changing access or values
H_grow    success model: non-isomorphic growth of admissible observable algebra, predicate,
          or construction space
```

Formal discriminator:

```text
fixed-H absorbed:
  exists H_infty and access maps alpha_n such that every A_n and rho_n factors through H_infty

H-growing candidate:
  no fixed H_infty / A_infty / Mu_infty can factor all A_n, rho_n, and admissibility updates
  while preserving records, morphisms, and observer reconstruction
```

Orch-OR, microtubule superradiance, anesthetic perturbation, and GU signed-readout comparisons
belong here only as fixture sources. They do not by themselves supply `H_grow`.

RUN-0081 OnlineIssuance verdict:

The current strongest formal source object is the narrowed class-relative residue:

```text
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
```

The load-bearing source gate is:

```text
Issue[S](Gamma_n, e_n, w_n) is source-side only if:

1. Gamma_n, CandExt(Gamma_n), and Adm_n are formed at prefix n.
2. e_n : CandExt(Gamma_n) and w_n : Adm_n(e_n).
3. the issued target is unavailable in Gamma_n.
4. no internally formed future-schema oracle, fixed latent graph, fixed stochastic law, or
   completed extension diagram precontains all future admissible witnesses.
5. the step emits a recordable trace tau_n for projection/finality audit.
```

Absorber verdict:

```text
finite/computable/fixed-law/adaptive-search/fixed-latent growth: absorbed
category/context/fibration/sheaf/colimit structure: absorbed as presentation
external Platonist completion: absorbs as navigation, not internal source issuance
local constructive productive witness: survives class-relatively
```

This is not a physical bridge, not a new category-theoretic primitive, and not a proof that
reality issues. It is the current narrow formal target for `TI-C019`.

RUN-0097 small-calculus machine check:

The E090 local constructive witness schema has executable support in a small symbolic calculus.

Checked schema:

```text
Gamma_n forms Code_n, Cand_n, Adm_n, and Enum_n.
Diag(Enum_n) is formed against Enum_n.
w_diag : Adm_n(Diag(Enum_n)) is formed.
Iss_n(Gamma_n, Diag(Enum_n), w_diag) = Gamma_{n+1}.
tau_diag records the source trace.
Omega_future is rejected as an internal source object.
```

Result:

```yaml
schema_machine_checked: true
proof_assistant_used: false
full_theorem_prover_verification: false
local_constructive_witness_passes: true
internal_future_oracle_rejected: true
external_platonist_absorber_still_available: true
physical_source_issuance_established: false
```

Effect typing:

```yaml
Issue[S]^LC: true
Issue[S]^physical: false
```

This strengthens the class-relative formal residue. It does not promote a physical claim and
does not defeat external Platonist completion outside the local constructive source class.

RUN-0099 physical adapter contract:

A physical candidate can only interface with `OnlineIssuance^LC` through:

```text
Adapter_P:
  physical candidate trace ->
    Gamma_n, Adm_n, e_n, w_n, Gamma_{n+1}, tau_n
```

Acceptance rule:

```text
all adapter fields map
+ at least one of W1/W2/W3 source-growth core
+ W4/W5/W6 absorber controls
+ fixed-source absorber defeat
+ no hidden completed oracle
+ source-generated new class
```

Result:

```yaml
adapter_contract_exists: true
negative_fixed_h_control_rejected: true
schematic_positive_shape_admitted: true
schematic_positive_is_real_candidate: false
Issue[S]^physical: false
TI_C020_reopened: false
```

`Adapter_P` is a gate, not evidence. TI-C020 remains parked until a real candidate passes it.

RUN-0102 Assembly source adapter fixture:

Assembly Theory can instantiate a formal/local subtype of the `Adapter_P` witness:

```text
AssemblySourceTrace =
(
  Gamma_n,          source assembly prefix
  AI_src,n(x),      source assembly index at prefix n
  e_n,              source-generated constructor
  w_n,              proof/computation that AI_src,n(x) is undefined and AI_src,n+1(x) is defined
  Gamma_{n+1},      successor source assembly prefix
  tau_n             constructor provenance and index-computation record
)
```

Executable result:

```yaml
AI_src,n(ABC): undefined
AI_src,n+1(ABC): 2
source_generated_constructor: bind_c(AB, C) -> ABC
projection_access_negative_rejected: true
fixed_complete_assembly_space_negative_rejected: true
experimenter_added_schema_negative_rejected: true
fixed_search_process_negative_rejected: true
Issue[S]^assembly_local: true
Issue[S]^physical: false
```

This adds a formal/local W2/W3 witness shape. It does not pass full `Adapter_P` because W1
non-isomorphic algebra growth and W4 physical perturbation non-factorization remain absent.

RUN-0103 Assembly W4-W6 physical protocol fixture:

The physical-lift attempt for Assembly is currently absorbed:

```yaml
real_physical_attempts:
  - chemical_reaction_network_trace
  - high_throughput_search_trace
  - evolutionary_biosynthesis_trace
  - instrument_schema_update_trace
all_real_physical_attempts_absorbed: true
w1_real_physical_candidate_found: false
w4_real_physical_protocol_found: false
w5_record_preservation_available_for_real_attempts: true
w6_real_physical_absorber_defeat_found: false
Issue[S]^assembly_local: true
Issue[S]^physical: false
```

Formal status:

```text
AssemblySourceTrace remains a formal/local W2/W3 subtype.
It is not a current physical Adapter_P witness.
```

The next formal object work should harden `OnlineIssuance^LC`, not keep using Assembly as a
physical bridge without new W1/W4 evidence.

RUN-0123 OnlineIssuance^LC Lean theorem contract (integration, no status promotion):

The `OnlineIssuance^LC` hardening called for above is now done at a bounded Lean tier. This
integration records the theorem contract established across E120/E121/E127-E132 and hostile-
reviewed in E134. It is a citation record, not a claim promotion and not a physical result.

Safe headline (the strongest sentence the formal object earns):

```text
Inside the current PA-O2-faithful finite-prefix Lean model, a present enumerator can be
diagonalized; the diagonal candidate is not prior-disclosed by that enumerator; concrete and
bounded-internal admissibility-witness routes exist; the source trace can be typed as IssueLC;
and a completed future oracle is rejected as an internal source object.
```

Minimum citation set (Lean surfaces under `formal/lean/OnlineIssuance/`):

| Layer | Primary theorem surface | Safe citation |
| --- | --- | --- |
| Core object language | `no_internal_completed_future_oracle`, `finite_non_disclosure`, `issue_lc_from_diagonal_witness` | Pass-one LC object language proves finite non-disclosure from visible assumptions and rejects a completed future oracle as internal source machinery. |
| PA-O2 presence | `EnumeratorPresent(.enumerator_symbol/.value_symbol/.total_for_candidate)` | Present enumerator carries registration, kind, registered values, and finite present-prefix totality. |
| Diagonal productivity | `diagName_not_mem`, `diagonalFormed_derived` | Finite diagonal non-enumeration is derived over arbitrary enumerator value lists, not assumed. |
| Admissibility witness | `AdmDef`, `adm_witness_diagonal_derived`, `issue_lc_all_derived` | `IssueLC` is reachable from `EnumeratorPresent` for the concrete `AdmDef`; universal predicate-free self-encoding is refuted. |
| Internal predicate syntax | `InternalPredicate`, `selfQuote_internal_witness`, `no_universal_internal_acceptance` | Bounded internal predicate-code witness formation exists; universal internal-code acceptance is false. |
| Total-family comparator | `stage_diag_escape`, `diag_absorbed_by_extension`, `no_fixed_point_of_absorption` | Total Nat-indexed family diagonalization and absorption / no-fixed-point are machine-checked in the stated total-family model only. |
| c.e. ceiling | `no_absolute_ce_escape`, `ce_prefix_fresh_escape`, `ce_prefix_escape_absorbed` | Finite-prefix freshness survives, but whole-c.e. positive escape is absorbed by singleton enumeration in the c.e.-presentation model. |
| Name-level absorption | `diagName_absorbed`, `no_diagName_whole_family_escape` | The concrete `diagName` construction has a fixed binary-name absorber at the bounded name tier. |

Scope limits that travel with every citation (unsafe readings — do NOT cite):

```text
- OnlineIssuance^LC does NOT prove Platonism false (external completed-structure ontology is
  outside the internal source-object exclusion; E132).
- OnlineIssuance^LC does NOT establish physical source issuance; TI-C020 stays parked.
- The c.e. tier gives NO positive whole-family escape theorem.
- AdmDef does NOT prove predicate-free or arbitrary admissibility.
- The name-tier absorber does NOT cover arbitrary name constructors.
- The Lean model is a bounded finite-prefix fixture, not a full recursive-function,
  category-theory, physics, or metaphysics formalization.
```

Earned status: `OnlineIssuance^LC` is a Lean-hardened, class-relative formal source residue —
the current narrow formal target for `TI-C019`. This integration changes no claim status; see
the `RUN-0123 Claim Update` block in `CLAIM-LEDGER.md`.

RUN-0090 RecordTableSystem candidate:

`RecordTableSystem` is a working reconstruction/readout candidate from E100/E101. It does not
replace `OnlineIssuance^LC` and does not promote a physical-source claim.

```text
RecordTableSystem =
(
  Col,          record fields / dimensions / observables; excludes primitive time
  Row,          compatible assignments over available fields
  Compat,       admissibility predicate for row compatibility
  Append,       operation/relation by which compatible rows enter history
  Order,        induced dependency/finality order over appended rows
  Render_i,     observer i's rendering of selected fields and row order
  Finality_mu,  reversal/deletion cost over appended rows
  MatterCrit,   persistence/action-constraint criterion over rendered rows
  Leak_i,       optional non-4D access/leakage visible to observer i
  Adapter_B?    optional boundary/adapter candidate for GU/external-record links
)
```

Guard:

```text
time notin Col
```

First discriminator:

```text
Can temporal queries, past/future distinction, and observer-local coordinate-time renderings be
recovered from Append/Order/Finality without adding a time column?
```

The object is absorbed if ordinary append-log/database semantics, fixed completed table,
fixed richer source plus changing access, fixed-H readout, or Minkowski/GR-first import
reproduces all named behavior.

RUN-0092 TaF-boundary correction:

`RecordTableSystem` is narrowed to `RecordTableSystem^TI`: a schema/admissibility and append
object with explicit downstream handoff to Time as Finality. Temporal order reconstruction from
finalized records is not the TI novelty target; TaF T48/T49 already own that baseline.

```text
RecordTableSystem^TI =
(
  Schema_n,      finite/currently formed column schema at prefix n
  Col_n,         columns available in Schema_n; primitive time excluded
  Row_n,         rows already admitted under Schema_n
  Cand_n,        candidate row/extensions formable from the current prefix
  Compat_n,      compatibility/admissibility predicate formed at prefix n
  Append_n,      witnessed transition Row_n -> Row_{n+1}
  Witness_n,     evidence that candidate row c satisfies Compat_n(c)
  Trace_n,       record emitted for downstream finality/reconstruction
  Project_i,n,   observer i access/render map into record/finality layer
  TaF_i,n,       downstream TaF reconstruction/finality process
  Absorb         fixed-table/fixed-access/fixed-H/database/TaF null maps
)
```

Guard:

```text
time notin Col_n for all n
```

Handoff:

```text
Trace_n -> TaF_i,n
```

TI surplus can only appear before or at `Append_n`: in `Schema_n`, `Cand_n`, `Compat_n`,
`Witness_n`, or failure of a fixed absorber map. If all temporal behavior appears only after
`Trace_n -> TaF_i,n`, the result is TaF reconstruction, not TI source-side evidence.

RUN-0093 fixture result:

The first executable `RecordTableSystem^TI` fixture compared:

```text
A_fixed_schema:
  fixed columns, candidates, and compatibility from prefix 0

B_prefix_formed:
  join candidate and join compatibility predicate formed at prefix 2
```

Both models emit the same TaF-reconstructable trace:

```text
e_alpha_lock -> e_join_lock
e_beta_lock  -> e_join_lock
e_alpha_lock || e_beta_lock
```

Result:

```yaml
TaF_absorbs_temporal_order: true
admissibility_provenance_difference: true
fixed_completed_table_absorbs_external_behavior: true
source_side_residue_found: false
```

So the live object narrows again:

```text
RecordTableSystem^TI is only interesting if admissibility-formation records cannot be
precontained by a fixed table/schema/access/oracle absorber.
```

RUN-0095 no-fixed-schema gauntlet result:

The follow-up fixture made admissibility formation first-class:

```text
form_schema
form_candidate
form_compat
form_witness
```

It then tested four fixed-precontainment absorbers:

```text
fixed universal schema
fixed proof registry
fixed latent completed table
fixed richer source plus changing access
```

Result:

```yaml
formation_records_first_class: true
absorber_count: 4
absorbing_count: 4
prefix_availability_preserved_by_absorbers: true
witness_dependencies_preserved_by_absorbers: true
source_side_residue_found: false
demote_record_table_ti_as_independent_source_route: true
```

Therefore `RecordTableSystem^TI` no longer survives as an independent source-side formal
object. Its remaining honest role is as vocabulary or an interface for `OnlineIssuance^LC`:

```text
Schema_n  -> Gamma_n
Cand_n    -> CandExt(Gamma_n)
Compat_n  -> Adm_n
Append_n  -> Iss_n / e_n
Witness_n -> w_n : Adm_n(e_n)
Trace_n   -> tau_n
```

If that mapping adds no formal surplus over E091, record-table TI should be archived as
TaF/log/database/OnlineIssuance interface vocabulary.

RUN-0096 OnlineIssuance lift-or-demote result:

The mapping succeeds:

```text
Schema_n             -> Gamma_n
Cand_n               -> CandExt(Gamma_n)
Compat_n             -> Adm_n
Append_n             -> Iss_n / e_n
Witness_n            -> w_n : Adm_n(e_n)
Trace_n              -> tau_n
Project_i,n/TaF_i,n  -> Proj_{o,n} / Glue_n
```

But it adds no formal surplus:

```yaml
component_mapping_total: true
record_table_is_online_issuance_interface: true
fails_no_hidden_oracle_gate: true
productive_self_encoding_witness_present: false
adds_formal_surplus_over_e091: false
record_table_archive_as_vocabulary: true
source_side_residue_found: false
```

So the final formal status is:

```text
RecordTableSystem^TI is retained as interface vocabulary.
It is not an independent source-side formal object.
```

Ownership:

```text
source-side residue:  OnlineIssuance^LC
temporal reconstruction: Time as Finality
record-table language: interface/explanatory layer
```

## RUN-0157 CompletionClass v1 contract

The current completion barrier is now explicitly bounded by
`COMPLETION-CLASS.md`:

```text
CompletionClass_v1(Pi) = closure under declared product, sequential
composition, and representation equivalence of:

  hidden state
  initial condition
  boundary condition
  fixed source
  stochastic seed
  name/provenance
  resource/capability
  whole family
  completed history
  observer information/access
  relabeling/gauge
```

`Pi` is the frozen comparison contract over source law, action, records,
interventions, access, resources, costs, boundaries, task success, holdouts,
and quotient data.

The four possible absorption conclusions are distinct:

```text
PHYSICAL_PREDICTIVE_ABSORPTION
OPERATIONAL_CONTEXT_ABSORPTION
REPRESENTATIONAL_SURPLUS_ABSORPTION
GLOBAL_ONTOLOGICAL_ABSORPTION
```

An omitted or unresolved primitive returns `INCOMPLETE_NULL_CLASS`. A packet
with verified nonfactorization for every represented primitive and declared
composition closure may return `SURVIVES_BOUNDED_COMPLETION_CLASS`. That is a
bounded contract-review trigger, not physical source issuance.

This integration does not convert the E172/E173 proof contract into a universal
theorem. It does not prove physical exhaustiveness of the eleven families,
validate domain-specific certificate content, reopen `TI-C020`, move claims,
or modify E177 v1.

## Component Pressures

`R`: What is realized? Events, constraints, records, facts, boundary conditions, or equivalence classes?

`<`: Is the dependency order causal, logical, informational, physical, or something else?

`mu`: What does the measure count? Entropy, action, volume, information, probability mass, constraint density, or a new invariant?

`dR`: Is the frontier meaningful in a relativistic setting, or does it reintroduce a preferred foliation?

`O_i`: What makes an observer site? Physical subsystem, measurement channel, record-keeping process, or access boundary?

`kappa_i`: Can local cadence be defined without smuggling in ordinary time?

`A_i`: What can an observer inspect? Records, events, constraints, histories, summaries, or proofs?

`G`: What reconciliation rules glue observer-local records into global structure?

## First Formal Test

The object must survive these questions before being strengthened:

1. Can each component be defined without circular reference to ordinary time?
2. Does the object reduce to a known framework under clear conditions?
3. Does anything remain after known frameworks absorb it?
4. Can the object generate a theorem, no-go result, model, or discriminator?
