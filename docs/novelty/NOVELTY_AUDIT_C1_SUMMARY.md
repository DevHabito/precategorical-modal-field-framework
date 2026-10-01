# Novelty Audit C1 — Finite Preorder Counts and Edge-Toggle Sensitivity

**Project:** Pre-Categorical Modal Field Framework  
**Author:** Felipe Gianini Romero  
**Original search date:** 2026-07-15  
**Consolidation correction:** 2026-10-01  
**Scope:** MF-R007, MF-R008, MF-R011

## Executive verdict

| Claim | Current classification | Manuscript treatment |
|---|---|---|
| MF-R007 | Classical enumeration formula | Attribute; retain independent reproduction and corrective use |
| MF-R008 | Project-specific elementary proposition; no exact match found | Retain as a corrective named proposition, without claiming certified priority |
| MF-R011 | Exact finite reachability-sensitivity result; priority of the specific value not certified | Retain as exact combinatorics; explicitly connect it to prior random-digraph reachability and edge-influence literature |

## MF-R007

\[
N_{\mathrm{full}}(n)
=
\sum_{k=1}^{n}S(n,k)p(k)
\]

is the classical labeled-preorder / finite-topology enumeration identity.
Fischer and Makowsky explicitly state the formula as known and attribute it to
a 1973 source. The value \(N_{\mathrm{full}}(5)=6942\) is historical, not new.

**What remains project-specific:** independent exhaustive reproduction,
formal resolution of the \(5234/6942\) ambiguity, and public corrective
provenance.

## MF-R008

\[
N_{\mathrm{rep}}(n)
=
\sum_{k=1}^{n}\binom{n-1}{k-1}p(k)
\]

counts the project's lossy minimum-representative quotient-poset code. No exact
prior formulation was found in the searched literature. However, the proof is
an immediate consequence of the definition, so this should be presented as a
project-specific elementary proposition rather than a major new theorem.

## MF-R011

Define

\[
P_n
=
\frac{1}{n(n-1)2^{n(n-1)}}
\sum_{G,e}
\mathbf 1[C(G)\neq C(G\triangle e)].
\]

Exact finite values are

\[
P_2=1,\qquad
P_3=\frac34,\qquad
P_4=\frac12,\qquad
P_5=\frac{75}{256}.
\]

During Consolidation 1.0 we recovered a structural reduction that should replace
the old novelty-centered presentation. For any fixed distinct labels \(s,t\),
pair the graphs with edge \(s\to t\) absent and present. Inserting the edge
changes the full reachability relation exactly when \(t\) was not already
reachable from \(s\). Hence, in the uniform loopless labeled-digraph ensemble,

\[
P_n=2\Pr(s\not\leadsto t).
\]

Writing \(\gamma_{n,p}=\Pr(s\leadsto t)\) in the independent-edge random-digraph
model gives

\[
P_n=2\bigl(1-\gamma_{n,1/2}\bigr).
\]

This changes the literature positioning materially.

Uno and Ibaraki (1998), *Reachability Problems of Random Digraphs*, study
\(\gamma_{n,p}\) directly and present an exact computation method. Qin, Sheng,
Parkinson, and Falkner (DASFAA 2017), *Edge Influence Computation in Dynamic
Graphs*, explicitly study edge influence through reachability changes after edge
deletion.

Therefore the July wording “apparently unreported exact finite statistic” is no
longer an acceptable current classification. The general fixed-pair
reachability problem, exact computation of its probability, and the broad
edge-influence idea have clear prior art.

What remains safe to say is narrower:

- the project defines the displayed normalized statistic and verifies its exact
  small-\(n\) values under the declared ensemble;
- \(P_5=75/256\) is reproduced by independent computational and combinatorial
  routes;
- the inspected sources do not settle priority of the particular reduced value
  \(75/256\) or the exact displayed sequence;
- absence from the inspected sources is not evidence strong enough to claim
  novelty.

The detailed correction is recorded in
`docs/novelty/MF-R011_edge_flip_probability.md`.

## Consequences for the combinatorics paper

The paper should not be organized around \(6942\) as a new theorem, nor around
MF-R011 as a newly discovered general theory of graph sensitivity. A defensible
core is instead:

1. precise comparison of complete and representative encodings;
2. exact information loss and non-injectivity of the representative code;
3. exact edge-toggle statistic with its structural reduction to ordinary
   fixed-pair reachability;
4. independently checkable finite values and formal semantics;
5. careful connection to the established random-digraph literature.

Any future recurrence, bound, or asymptotic analysis for \(P_n\) should begin by
checking what is already known for \(\gamma_{n,p}\), rather than treating the
reduced quantity as a separate literature by default.

## Matrix updates

The classification matrices should replace the old MF-R011 label
`APPARENTLY UNREPORTED EXACT FINITE SENSITIVITY STATISTIC` with a conservative
status equivalent to:

`EXACT FINITE REACHABILITY-SENSITIVITY RESULT; PRIORITY OF SPECIFIC VALUE NOT CERTIFIED`.

This correction changes novelty/literature wording only. It does not alter the
archived exact integers, fractions, or ensemble definition.

## Limits of this audit

A literature search cannot prove novelty or non-novelty of a specific finite
value without locating a source that states it. This audit records the sources
examined and supplies safe publication language. Specialist review remains
appropriate, and absolute priority claims remain prohibited.
