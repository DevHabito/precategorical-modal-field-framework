# MF-R011 — Edge-Toggle Sensitivity of the Reachability-Preorder Map

**Novelty audit:** C1, corrected during formal consolidation  
**Original search date:** 2026-07-15  
**Correction date:** 2026-09-18  
**Current classification:** `KNOWN_PIVOTALITY_FRAMEWORK_PROJECT_SPECIFIC_EXACT_VALUE_NOVELTY_NOT_CERTIFIED`

## Exact definition

Let

\[
m=n(n-1)
\]

and let \(\mathcal D_n\) be the \(2^m\) loopless labeled digraphs on
\([n]\). Let \(C(G)\) be the full reflexive reachability preorder of \(G\).
Define

\[
P_n
=
\frac{1}{m2^m}
\sum_{G\in\mathcal D_n}
\sum_e
\mathbf 1\!\left[C(G)\neq C(G\triangle e)\right],
\]

where \(G\triangle e\) toggles one directed non-loop edge.

As a function on the graph hypercube this is an average edge-boundary density
of the vector-valued map

\[
C:\{0,1\}^{m}\longrightarrow\{\text{preorders on }[n]\}
\]

under the discrete metric on its codomain.

That description is mathematically valid, but the audit below shows that the
pivotality underlying MF-R011 belongs to classical reliability / influence
language and must not be presented as a new abstract sensitivity concept.

## Exact finite results retained

Independent exhaustive enumeration gives

\[
P_2=1,\qquad
P_3=\frac34,\qquad
P_4=\frac12,\qquad
P_5=\frac{75}{256}.
\]

For \(n=5\),

\[
m2^m=20\cdot 2^{20}=20\,971\,520
\]

ordered graph-edge pairs, of which

\[
6\,144\,000
\]

change the full reachability preorder. Therefore

\[
P_5
=
\frac{6\,144\,000}{20\,971\,520}
=
\frac{75}{256}.
\]

This numerical statement remains an exact finite result. The present correction
changes its literature positioning, not its arithmetic value.

## Structural reduction

Fix a directed non-loop edge \(e=(a,b)\). If \(H\) does not contain \(e\),
then

\[
C(H+e)\neq C(H)
\quad\Longleftrightarrow\quad
a\not\leadsto_H b.
\]

If \(a\leadsto_H b\), every use of the added edge in a path can be replaced by
an already-existing path from \(a\) to \(b\), so the complete reachability
relation is unchanged. If \(a\not\leadsto_H b\), the pair \((a,b)\) itself
becomes newly reachable.

Pairing the absent and present members of every edge-toggle pair gives

\[
P_n=2\Pr_G[a\not\leadsto_G b]
\]

for any fixed distinct labels \(a,b\) in the uniform loopless labeled-digraph
ensemble. This identity is currently a consolidation target; the finite
five-vertex semantic bridge is being formalized in Lean and must not be labeled
kernel-complete until the pinned build and checker gates pass.

## Classical reliability interpretation: Birnbaum structural importance

For the fixed ordered pair \((a,b)\), define the coherent binary system

\[
\phi_{a,b}(G)=\mathbf 1[a\leadsto_G b].
\]

Treat each possible directed non-loop arc as a binary component and distinguish
the direct component \(e=(a,b)\). The component is critical/pivotal exactly
when changing its state changes \(\phi_{a,b}\).

For this particular direct edge,

\[
\phi_{a,b}(H+e)-\phi_{a,b}(H)=1
\quad\Longleftrightarrow\quad
a\not\leadsto_H b,
\]

and the same condition is equivalent to changing the entire reachability
preorder. Therefore the fixed-edge MF-R011 probability is exactly the
**Birnbaum structural importance** of the direct arc in this two-terminal
directed reliability system: the fraction of the \(2^{m-1}\) states of the
other arcs for which the distinguished arc is critical.

Consequently, MF-R011 must not be advertised as a newly invented general
notion of pivotality or structural sensitivity.

## Connection to random-digraph reachability

Uno and Ibaraki (1998), *Reachability Problems of Random Digraphs*, study the
independent-edge random digraph and denote by \(\gamma_{n,p}\) the probability
that a fixed vertex reaches another. They give an exact computation method for
that probability.

At \(p=1/2\), our uniform graph ensemble is exactly their independent-edge
model, so the structural reduction yields

\[
\boxed{P_n=2\bigl(1-\gamma_{n,1/2}\bigr)}.
\]

This is a project-side identification obtained by combining the MF-R011
pivotal-edge reduction with the classical reachability probability. It is not a
claim that Uno and Ibaraki used the MF-R011 notation or studied the full
preorder-valued map.

More generally, for \(p<1\), forcing the direct arc \(a\to b\) on makes the
terminal reachability event certain. Hence its Birnbaum reliability importance
satisfies

\[
I^B_{a\to b}(p)
=
\frac{1-\gamma_{n,p}}{1-p}.
\]

The \(p=1/2\) specialization is MF-R011. This general-\(p\) identity is recorded
as an interpretation, not as a novelty claim.

## Other close prior work

### Edge influence under deletion

Qin, Sheng, Parkinson, and Falkner (DASFAA 2017), *Edge Influence Computation
in Dynamic Graphs*, explicitly study the influence of a graph edge through
reachability changes caused by deleting that edge. Their observable counts
changed node-pair reachabilities in a given dynamic graph, rather than the
binary event that the complete preorder changes under a toggle averaged over
the uniform graph ensemble. It is therefore close prior art, not an identical
statistic.

### Initially connected digraphs

The auxiliary rooted-reachability counts used in the reachable-set
decomposition are classical counts of initially connected digraphs. Liskovets
studied their enumeration in the early literature. They must not be presented
as project-original sequences or formulas merely because they arise naturally
inside the MF-R011 derivation.

### Dynamic SCC / reachability and graph-algorithm sensitivity

The earlier audit located related work on dynamic SCC/reachability algorithms,
directed-network susceptibility, and average sensitivity of graph algorithms.
Those references remain relevant context, but they are no longer the closest
conceptual prior art after the Birnbaum and random-digraph reachability links
were identified.

## Corrected novelty conclusion

The July 2026 wording “apparently unreported exact finite statistic” is no
longer an adequate basis for a novelty claim.

What is established or under verification is narrower:

1. the project has an independently reproduced exact finite value
   \(P_5=75/256\);
2. the toggle criterion reduces to direct-edge pivotality for the two-terminal
   reachability event;
3. that pivotality is a classical Birnbaum structural-importance quantity;
4. in the uniform ensemble it is directly expressible through the classical
   fixed-pair random-digraph reachability probability;
5. the project is building a kernel-checked finite certificate connecting the
   executable five-vertex computation to the semantic preorder statement.

No priority claim is presently supported for the general statistic, the
pivotality concept, the reachability probability, or the auxiliary sequence.
Whether the exact value \(75/256\), the particular full-preorder formulation,
or the specific formalization has appeared previously is a separate
claim-specific bibliographic question and is **not certified** here.

## Safe manuscript wording

> For the uniform loopless labeled digraph on five vertices, exhaustive exact
> computation gives an edge-toggle probability \(P_5=75/256\) for changing the
> full reflexive reachability preorder. A fixed edge \(a\to b\) is pivotal for
> the preorder exactly when \(a\) does not already reach \(b\) without that
> edge. Thus the statistic is a two-terminal pivotality / Birnbaum structural
> importance specialization and, at edge probability \(1/2\), satisfies
> \(P_n=2(1-\gamma_{n,1/2})\), where \(\gamma\) is the classical fixed-pair
> random-digraph reachability probability. We make no novelty claim for the
> general pivotality framework or reachability probability.

## Wording to avoid

- “We invented a new graph-sensitivity concept.”
- “No one has studied this kind of edge pivotality before.”
- “The general law is novel.”
- “The initially-connected-digraph sequence is new.”
- “\(75/256\) is a universal constant.”
- “The result has physical significance without an additional physical model.”

## Editorial decision

Retain \(75/256\) as an exact finite project result and formalization target.
Present the structural reduction as a bridge to classical reliability and
random-digraph theory. Novelty remains uncertified and must stay separate from
mathematical correctness.
