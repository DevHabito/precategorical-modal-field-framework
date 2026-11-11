# 1+1 Minkowski UPO failure decomposition — modular criterion and exact extension to N=9

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact finite enumeration using a classical UPO characterization  
**Physical status:** causal-set-inspired structural control; not an empirical test  
**Novelty status:** the UPO/module characterization is classical; the exact random-2-order counts below are project computations and priority is not certified

## 1. Question

The previous Minkowski control asked whether the unoriented comparability relation of a finite random \(2\)-order determines its causal order up to global reversal.

The exact enumeration through

$$
N\le 7
$$

showed that some orders are recoverable and many are not.

The next question is:

> What structural obstruction causes failure?

Classical uniquely-partially-orderable graph theory provides an exact answer.

## 2. Classical connected UPO criterion

Let \(G\) be a connected comparability graph.

A vertex subset

$$
M\subset V(G)
$$

is a module (partitive set in the classical terminology used in UPO theory) when every vertex outside \(M\) is adjacent either to every vertex of \(M\) or to no vertex of \(M\).

A module is stable when it contains no internal edge.

A classical characterization states that a connected comparability graph is uniquely partially orderable exactly when every nontrivial module/partitive set is stable.

Equivalently, a nontrivial module containing a comparability edge creates internal orientation freedom that the outside connectibility pattern does not resolve.

This is classical graph theory.

## 3. Disconnected graphs

The random \(2\)-order comparability graph need not be connected.

If it contains two or more connected components with at least one edge, each nontrivial component can be globally reversed independently.

Therefore the complete graph has at least

$$
2^2=4
$$

transitive orientations.

It cannot be UPO.

Thus a nonempty general graph is UPO exactly when:

1. it has exactly one edge-containing connected component;
2. every other component is an isolated vertex;
3. the unique nontrivial component satisfies the connected UPO criterion.

This combines the classical connected theorem with elementary component independence.

## 4. Causal-connectibility interpretation

In the present reconstruction experiment, an edge means only:

$$
x\sim y
\quad\Longleftrightarrow\quad
x\prec y\ \text{or}\ y\prec x.
$$

A nontrivial module \(M\) means that every event outside \(M\) sees all members of \(M\) in the same **unoriented comparability sense**:

- comparable to all of them; or
- incomparable to all of them.

If \(M\) also contains internal comparable pairs, the exterior symmetric connectibility data do not determine all internal orientation information uniquely.

Therefore the main obstruction is not merely missing edges.

It is:

$$
\boxed{
\text{externally indistinguishable block}
+
\text{internal causal comparability}.
}
$$

This statement concerns the unoriented reconstruction contract only.

It does not say that the events are physically indistinguishable in a full causal-set model.

## 5. Exact failure taxonomy

Every relative permutation was classified into exactly one category:

### A. Empty antichain

No comparability edge exists.

There is no nontrivial causal succession to reconstruct.

### B. Multiple nontrivial components

At least two connected components contain edges.

Their orientations can be reversed independently.

### C. Internal module ambiguity

There is exactly one edge-containing component, but it contains a nontrivial non-stable module.

### D. UPO recoverable

There is exactly one edge-containing component and its nontrivial modules are all stable.

The original partial order is then determined up to global reversal.

## 6. Exact enumeration through N=9

All

$$
N!
$$

relative permutations were enumerated for

$$
N=2,\ldots,9.
$$

No Monte Carlo sampling was used.

| N | permutations | UPO recoverable | internal module ambiguity | multiple nontrivial components | empty antichain | recovery fraction |
|---:|---:|---:|---:|---:|---:|---:|
|2|2|1|0|0|1|\(1/2\)|
|3|6|4|1|0|1|\(2/3\)|
|4|24|12|10|1|1|\(1/2\)|
|5|120|38|72|9|1|\(19/60\)|
|6|720|165|494|60|1|\(11/48\)|
|7|5040|1042|3613|384|1|\(521/2520\)|
|8|40320|8464|29280|2575|1|\(529/2520\)|
|9|362880|80020|264156|18703|1|\(4001/18144\)|

For \(N\le7\), the UPO counts reproduce the earlier direct orientation enumeration exactly.

This provides an independent structural regression of the previous audit.

## 7. The finite trend is not monotone

The recovery fractions are approximately

$$
0.500000,\;
0.666667,\;
0.500000,\;
0.316667,\;
0.229167,\;
0.206746,\;
0.209921,\;
0.220514.
$$

The decrease seen through \(N=7\) does not continue monotonically.

The fraction rises at both

$$
N=8
$$

and

$$
N=9.
$$

Therefore the earlier finite sequence must not be described as evidence of monotone decay.

No asymptotic limit is inferred.

## 8. Dominant failure mode

For \(N=9\),

$$
264156
$$

of the

$$
362880
$$

permutations fail because of internal non-stable modules.

That is approximately

$$
72.79\%.
$$

By comparison,

$$
18703
$$

fail because of multiple nontrivial connected components, approximately

$$
5.15\%.
$$

The dominant obstruction in this finite ensemble is therefore internal modular ambiguity, not disconnectedness.

## 9. Minimal bad-module sizes

For the internal-module failures, the audit also records the smallest non-stable module size.

At \(N=8\), the exact histogram is:

| minimum bad-module size | count |
|---:|---:|
|2|21956|
|3|3054|
|4|1051|
|5|751|
|6|980|
|7|1488|

Thus size-two obstructions dominate.

A size-two non-stable module is an adjacent twin pair in the comparability graph: the two vertices are comparable to one another and have identical adjacency to every outside vertex.

Such a pair is exchanged by a graph automorphism.

The earlier symmetry-orientation no-go therefore applies directly to its local orientation if only the unoriented graph is retained.

## 10. Why the module theorem is physically suggestive

The UPO theorem identifies the exact kind of information lost by arrow erasure.

It is not enough that the graph contains rich incomparability.

The unoriented relation must also avoid internally structured blocks whose external comparability signatures are identical.

This suggests a useful causal-set reconstruction quantity:

> the prevalence and scale distribution of non-stable comparability modules.

That quantity is still purely combinatorial.

It becomes physically relevant only if connected to a causal-set ensemble or continuum approximation.

## 11. Relation to modular decomposition

Modern transitive-orientation algorithms use canonical modular decomposition.

Prime quotient graphs have only two transitive orientations, one the reverse of the other.

Series/parallel or decomposable structure generates additional orientation freedom.

This is established theory.

The present project should therefore stop treating UPO recovery as a black-box orientation count.

The correct structural language is modular decomposition.

## 12. Consequence for the random-2-order benchmark

The previous question

> What features make the comparability graph UPO?

now has a classical exact answer at the graph level.

The remaining project-specific question is statistical:

> Under the random \(2\)-order measure induced by a \(1+1\) Minkowski sprinkling, how frequently and at what scales do the UPO-obstructing modules occur?

This is different from asking for a new graph-theory characterization.

## 13. Next rigorous target

The next calculation should measure, as \(N\) increases:

1. probability of at least one non-stable module;
2. minimum bad-module size;
3. number and size distribution of maximal modules;
4. modular-decomposition node types;
5. conditional UPO probability after excluding simple twin-pair obstructions;
6. chain depth within the recoverable subset.

An asymptotic claim should be attempted only after this structure is understood.

## 14. Physical boundary

Even perfect UPO recovery gives only

$$
\{P,P^{\mathrm{op}}\}.
$$

It does not select future versus past.

It also does not provide:

- proper time;
- Lorentzian metric;
- continuum dimension;
- locality scale;
- empirical spacetime evidence.

The present result concerns **recoverability of ordinal causal orientation from symmetric connectibility**.

## 15. Current conclusion

The finite Minkowski control has moved from a numerical observation to a structural diagnosis.

The exact recovery condition is:

$$
\boxed{
\text{one nontrivial connected component}
+
\text{no non-stable internal module}.
}
$$

In the audited random \(2\)-order ensemble, internal modular ambiguity is the dominant reason orientation cannot be reconstructed after the arrows are erased.

The next frontier is therefore not another orientation algorithm.

It is the statistics and physical meaning of modular structure in causet-like ensembles.
