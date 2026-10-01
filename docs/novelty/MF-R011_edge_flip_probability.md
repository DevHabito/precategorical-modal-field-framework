# MF-R011 — Edge-Toggle Sensitivity of the Reachability-Preorder Map

**Novelty audit:** C1  
**Original search date:** 2026-07-15  
**Consolidation correction:** 2026-10-01  
**Current classification:** `EXACT_FINITE_REACHABILITY_SENSITIVITY_RESULT_PRIORITY_NOT_CERTIFIED`

## Exact definition

Let

\[
m=n(n-1)
\]

and let \(\mathcal D_n\) be the \(2^m\) loopless labeled digraphs on
\([n]\). Let \(C(G)\) be the full reflexive-transitive reachability relation of
\(G\). Define

\[
P_n
=
\frac{1}{m2^m}
\sum_{G\in\mathcal D_n}
\sum_e
\mathbf 1\!\left[C(G)\neq C(G\triangle e)\right],
\]

where \(G\triangle e\) toggles one directed non-loop edge.

This is an exact finite statistic on the declared uniform graph-edge ensemble.
It may also be viewed as the normalized edge-boundary density of the map from
edge masks to full reachability relations, using the discrete metric on the
codomain.

## Structural reduction

Fix distinct labels \(s,t\) and the directed edge \(e=(s,t)\). Pair each graph
with \(e\) absent with the graph obtained by inserting \(e\).

If \(t\) is already reachable from \(s\), inserting \(e\) does not change the
full reachability relation: every path using the new edge can replace that edge
by the pre-existing path from \(s\) to \(t\). If \(t\) is not reachable from
\(s\), insertion changes at least the reachability fact \(s\leadsto t\).

Hence a fixed-edge pair is sensitive exactly when, on its edge-absent side,
\(s\not\leadsto t\). Counting both orientations of the toggle pair gives

\[
P_n=2\Pr(s\not\leadsto t)
\]

in the uniform loopless labeled-digraph ensemble. If
\(\gamma_{n,1/2}=\Pr(s\leadsto t)\), then equivalently

\[
P_n=2\bigl(1-\gamma_{n,1/2}\bigr).
\]

The generic reachability statement behind the insertion step is now isolated
in `formal/lean/PrecategoryFormal/EdgeAdditionReachability.lean`; its CI/kernel
status must be read from the active formalization PR rather than assumed from
this document.

## Exact finite values

Independent finite enumeration gives

\[
P_2=1,\qquad
P_3=\frac34,\qquad
P_4=\frac12,\qquad
P_5=\frac{75}{256}.
\]

For \(n=5\),

\[
20\cdot2^{20}=20971520
\]

ordered graph-edge pairs are tested, and exactly

\[
6144000
\]

of them change the full reachability relation. Therefore

\[
P_5
=
\frac{6144000}{20971520}
=
\frac{75}{256}.
\]

A separate exact counting derivation is recorded in
`consolidation/MF_R011_INDEPENDENT_DERIVATION.md`. It obtains

\[
\Pr(s\not\leadsto t)=\frac{153600}{1048576}=\frac{75}{512}
\]

and therefore the same \(P_5=75/256\) without enumerating graph-edge pairs one
by one.

## Literature correction

The July 2026 audit was incomplete. Its wording that the statistic was
"apparently unreported" should not be retained as the current classification.

### Random-digraph reachability

Yushi Uno and Toshihide Ibaraki, *Reachability Problems of Random Digraphs*,
IEICE Transactions on Fundamentals, E81-A(12), 2694–2702 (1998), study the
independent-edge random-digraph model and define the fixed-pair reachability
probability \(\gamma_{n,p}\). They explicitly present a method for computing
its exact value for given \(n\) and \(p\).

This is directly relevant because the structural identity above reduces the
present statistic at \(p=1/2\) to

\[
P_n=2(1-\gamma_{n,1/2}).
\]

Therefore fixed-pair random-digraph reachability and its exact computation are
prior art and must not be claimed as project discoveries.

### Edge influence and dynamic reachability

Yongrui Qin, Quan Z. Sheng, Simon Parkinson, and Nickolas J. G. Falkner,
*Edge Influence Computation in Dynamic Graphs*, DASFAA 2017, pp. 649–660,
DOI `10.1007/978-3-319-55699-4_41`, explicitly study the influence of an edge
through changes in graph reachability caused by edge deletion.

This is substantially closer prior work to the reachability-change observable
than the sources emphasized in the original C1 audit.

### Other related literature

Dynamic SCC/reachability algorithms, directed-network susceptibility, Boolean
influence, and reliability/importance theory remain relevant context. They are
not needed to establish the exact finite value, but they further weaken any
claim that edge sensitivity itself is a new general concept.

## What the literature check does and does not establish

The updated search establishes that we must **not** claim novelty for:

- fixed-pair reachability probability in random digraphs;
- exact computation of that probability in general;
- the general idea of edge influence through reachability changes;
- the structural pivotality interpretation by itself.

The sources checked so far do **not** certify whether the particular reduced
fraction

\[
\frac{75}{256}
\]

or the exact sequence

\[
1,\frac34,\frac12,\frac{75}{256}
\]

has appeared explicitly before. Absence from the inspected sources is not a
proof of novelty. The correct status is therefore:

> the exact finite value is established for the declared ensemble; priority of
> the specific value and phrasing is not certified.

## Mathematical role after correction

The useful content of MF-R011 is now clearer than in the original audit:

1. a precisely declared finite sensitivity statistic;
2. an exact structural reduction to fixed-pair non-reachability;
3. exact small-\(n\) values, including \(P_5=75/256\);
4. independent computational and combinatorial verification routes;
5. a clean connection to established random-digraph reachability literature.

The structural reduction is more informative than simply pushing enumeration
to a larger \(n\). Future work, if pursued after consolidation, should start
from the known theory of \(\gamma_{n,p}\) rather than rediscovering it under a
new name.

## Safe manuscript wording

> For the uniform loopless labeled-digraph ensemble we consider the probability
> that toggling one directed edge changes the full reachability relation. A
> pairing argument gives \(P_n=2(1-\gamma_{n,1/2})\), where
> \(\gamma_{n,p}\) is the classical fixed-pair reachability probability for a
> random digraph. Exact computation gives \(P_5=75/256\). We make no priority
> claim for the general reachability probability, edge-influence framework, or
> the specific finite value.

## Wording to avoid

- “We discovered the general law of edge sensitivity in random digraphs.”
- “Fixed-pair reachability probability is new to this framework.”
- “\(75/256\) is a universal constant.”
- “The value \(75/256\) is definitely new.”
- “The value \(75/256\) was definitely known before” unless a source stating it
  explicitly is located.
- “The result has physical significance” without a separate operational model
  connecting this finite ensemble to a physical system.

## Editorial decision

Keep MF-R011 as an exact finite/combinatorial result and as a useful bridge to
classical random-digraph reachability. Remove the old "apparently unreported"
classification. Do not build a novelty claim around the general sensitivity
framework. Preserve the exact integers and fractions exactly as computed.
