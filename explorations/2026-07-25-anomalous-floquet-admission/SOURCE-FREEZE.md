---
artifact_type: third_party_source_map
status: frozen_for_receiver_admission_test
created: 2026-07-25
repo: possibility-to-capability
lane_id: "1"
source_claim_status: published_theory_and_experiment
---

# Anomalous-Floquet Source Freeze

## Source identity

1. Mark S. Rudner, Netanel H. Lindner, Erez Berg, and Michael Levin,
   “Anomalous Edge States and the Bulk-Edge Correspondence for Periodically
   Driven Two-Dimensional Systems,” *Physical Review X* 3, 031005 (2013).
   DOI: <https://doi.org/10.1103/PhysRevX.3.031005>.
2. Sebabrata Mukherjee et al., “Experimental observation of anomalous
   topological edge modes in a slowly driven photonic lattice,” *Nature
   Communications* 8, 13918 (2017).
   DOI: <https://doi.org/10.1038/ncomms13918>.
3. Lukas J. Maczewsky et al., “Observation of photonic anomalous Floquet
   topological insulators,” *Nature Communications* 8, 13756 (2017).
   DOI: <https://doi.org/10.1038/ncomms13756>.
4. Peng Xu, Wei Zheng, and Hui Zhai, “Topological micromotion of Floquet
   quantum systems,” *Physical Review B* 105, 045139 (2022).
   DOI: <https://doi.org/10.1103/PhysRevB.105.045139>;
   open manuscript: <https://arxiv.org/abs/2106.14628>.

These are third-party primary sources, not source-repository Frozen Packets.
P2C owns only the receiver mapping, finite permutation check, and admission
verdict below.

## Exact source object

The frozen specimen is the ideal four-step bipartite square-lattice drive used
as the simplest anomalous-Floquet construction.

- The period \(T\) is divided into four equal intervals.
- In each interval, only one directional family of nearest-neighbor A-B bonds
  is active: right, up, left, then down.
- At the ideal point, the active bond performs complete transfer in one
  interval, so \(JT/4=\pi/2\) in the equal-coupling convention.
- With periodic boundaries, a localized bulk state traverses a loop and
  returns to its starting site after one period. Thus \(U_{\mathrm{bulk}}(T)=I\)
  and the ideal bulk effective Floquet Hamiltonian may be chosen as zero.
- With an open boundary, the loop is cut and boundary states undergo chiral
  translation while the bulk remains localized.
- The bulk Floquet-band Chern numbers at the ideal point are zero; the full
  within-period evolution carries the relevant winding information.

Rudner et al. establish the driven bulk-edge distinction and winding invariant.
Mukherjee et al. give the exact four-step ideal construction and state
\(U(T)=I\) in the bulk with chiral edge propagation under open boundaries.
Maczewsky et al. independently realize the four-section photonic construction
and report localized bulk loops with chiral edge transport.

## Receiver finite construction

The executable receiver fixture uses a finite bipartite lattice with sites
\((s,x,y)\), \(s\in\{A,B\}\). During directional step \(d\), each present
\(A(x,y)\) is swapped with \(B(x+d_x,y+d_y)\). A missing open-boundary partner
leaves the site unchanged for that step.

This is a discrete perfect-transfer representative of the source's ideal
point. It verifies:

1. the four-step map is a permutation;
2. periodic-boundary evolution is exactly identity;
3. open-boundary evolution is nontrivial only on boundary sites;
4. reversing the step order reverses the boundary permutation while leaving
   the admission result unchanged.

It does not simulate fabrication disorder, quasienergy spectra, interacting
physics, or the thermodynamic invariant.

## Representation fork

Two distinct “static representative” questions must remain separate.

1. **Fixed-phase, same-dimensional Floquet Hamiltonian.** At the ideal bulk
   point \(U(T)=I\), a branch choice gives \(H_F=0\). It does not reconstruct
   the nontrivial within-period path or the open-edge permutation. The cited
   anomalous-Floquet literature establishes that band Chern numbers or one
   fixed-phase \(H_F\) do not carry the full edge information.
2. **Full-micromotion completion.** The entire path \(U(k,t)\), not only
   \(U(k,T)\), carries the winding data. Xu, Zheng, and Zhai explicitly provide
   a static description in one extra synthetic dimension spanning the
   micromotion parameter. This is a materially admissible enlarged
   representation and defeats any unqualified claim that the object has “no
   static representative” at all.

The candidate can therefore test failure of a fixed-phase,
same-dimensional effective-Hamiltonian description. It cannot, on these
sources, establish absence of every static completion.

## Admission ledger

| required field | frozen status | source-grounded content |
|---|---|---|
| before/after Floquet objects | present | periodic-bulk \(U(T)=I\) and open-boundary edge permutation for the same four-step drive |
| drive amplitude and duration | present | four equal steps with ideal \(JT/4=\pi/2\) |
| drive bandwidth / schedule | present | exactly one directional bond family active per quarter-period |
| initialization | present | localized single-site excitation |
| measurement / access | present | site-resolved output intensity or localized-particle position |
| control budget | partial | the driven protocol is explicit, but no source freezes a common static-rival control menu |
| matched drive power | missing | the papers do not supply a static comparator with an equal physical power/energy ledger |
| matched noise / error budget | missing | experimental imperfections are reported, but no common rival budget is defined |
| operational before/after task delta | missing | edge propagation is demonstrated, but no matched-resource static before-case and task-set relation is source-defined |
| strongest completion rival | present | full micromotion \(U(k,t)\), including a \(d+1\)-dimensional static synthetic-dimension representation |

## Receiver limits

- The source papers establish anomalous Floquet topology and experimental edge
  transport in their own terms. They do not assert P2C capability, issuance,
  finality, or a matched task-set enlargement.
- A changed time-dependent control schedule is not a matched-resource
  capability comparison by itself.
- \(H_F=0\) failing to encode micromotion is not absence of a full static
  completion once the synthetic-dimension rival is admitted.
- The correct present admission verdict is
  `ABSTAIN_MATCHED_RESOURCE_AND_TASK`: the exact anomalous micromotion specimen
  is source-grounded, but the P2C-2 capability-side comparison is not.
