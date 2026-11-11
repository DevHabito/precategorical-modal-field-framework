# Random 2-order UPO recovery in permutation-block language

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** derived structural characterization for the audited random-2-order representation + exact independent regression through N=9  
**Novelty status:** permutation graphs, modular decomposition, common intervals, and UPO theory are classical. No originality claim is attached to the characterization without a dedicated prior-art audit.

## 1. Motivation

The modular diagnosis showed that unoriented causal connectibility recovers the original random \(2\)-order up to global reversal exactly when:

1. there is one edge-containing connected component;
2. every proper nontrivial module of that component is stable.

For random \(2\)-orders, the same structure can be expressed directly in the relative permutation.

This gives a more useful route toward substitution decomposition and possible asymptotic analysis.

## 2. Relative permutation representation

Fix the first light-cone order as

$$
0<1<\cdots<N-1
$$

and let

$$
\pi\in S_N
$$

be the second order.

The \(2\)-order comparability relation is

$$
i\prec j
\quad\Longleftrightarrow\quad
i<j
\ \text{and}\
\pi(i)<\pi(j).
$$

Thus the unoriented comparability graph has an edge for an increasing pair of the relative permutation.

Its complement is the usual inversion graph of the permutation.

Both are permutation graphs.

## 3. Common intervals

A block/common interval of \(\pi\) is a consecutive set of positions

$$
\{a,a+1,\ldots,b\}
$$

whose set of values is also consecutive.

In the permutation diagram this is a block appearing consecutively on both lines.

For the comparability graph used here, every such block is a graph module:

an outside point lies uniformly on one side of the block in each total order and therefore has the same adjacency relation to every member of the block.

## 4. Stable common intervals

Inside a common interval, comparability edges are the increasing pairs.

Therefore the corresponding module is stable exactly when the induced relative permutation is strictly decreasing.

Hence:

$$
\boxed{
\text{common interval stable}
\iff
\text{induced block is decreasing}.
}
$$

A proper common interval containing any increasing pair is therefore a direct UPO obstruction.

## 5. Converse obstruction through modular decomposition

Classical modular decomposition of permutation graphs supplies the converse at the level needed here.

If a connected comparability graph has a proper non-stable module, its canonical modular decomposition contains either:

- a proper strong module with internal edges; or
- a decomposable/series node whose children generate a proper non-stable module.

Strong modules occur consecutively in both orders of every permutation representation.

At a decomposable node, a consecutive union of appropriate children likewise gives a common interval carrying internal comparability.

Thus existence of a proper non-stable module is witnessed by a proper non-decreasing common interval in the relative permutation representation.

This step uses classical modular-decomposition structure.

## 6. Connected-component correction

The criterion must be applied to the unique nontrivial connected component, not blindly to the full permutation.

A UPO graph may consist of:

- one nontrivial UPO component;
- any number of isolated vertices.

The nontrivial component is itself a proper module of the full graph and contains edges, but reversing that entire component is exactly the one allowed global orientation reversal.

It is therefore not an additional ambiguity.

For the permutation criterion:

1. identify the unique edge-containing connected component;
2. restrict the two orders to those vertices;
3. renormalize the induced relative permutation;
4. inspect proper common intervals only inside that component.

## 7. Derived criterion

For the random \(2\)-order representation used by the project:

$$
\boxed{
\text{nontrivial UPO recovery}
}
$$

holds exactly when

$$
\boxed{
\begin{array}{l}
\text{there is exactly one nontrivial connected component,}\\[1mm]
\text{and every proper common interval of its induced permutation}\\
\text{is decreasing.}
\end{array}
}
$$

This is a permutation-language restatement of the classical modular UPO criterion.

It is not proposed as a new graph-theory theorem.

## 8. Independent exact regression

A second implementation was written directly in permutation language.

It does not enumerate transitive orientations and does not enumerate arbitrary graph modules.

Instead it:

- finds the unique nontrivial comparability component;
- constructs its induced relative permutation;
- enumerates common intervals;
- rejects the case if any proper common interval is not decreasing.

The result was compared with the independent graph-module classifier for every permutation through

$$
N=9.
$$

The number of discrepancies was

$$
\boxed{0}.
$$

At \(N=9\), both implementations classify exactly

$$
\boxed{80020}
$$

of

$$
362880
$$

permutations as recoverable.

## 9. Simple permutations are only the prime core

A simple permutation has no proper nontrivial common interval.

Therefore it automatically passes the internal-block condition once the relevant connectedness requirement is satisfied.

The exact simple-permutation counts in the tested range are:

| N | simple permutations | UPO-recoverable random 2-orders |
|---:|---:|---:|
|4|2|12|
|5|6|38|
|6|46|165|
|7|338|1042|
|8|2926|8464|
|9|28146|80020|

At \(N=9\), simple permutations account for only about

$$
35.17\%
$$

of the recoverable cases.

Thus orientation recovery is not restricted to prime/simple structure.

## 10. What extra structure is allowed

The recoverable non-simple cases contain modules.

The important restriction is that those proper modules do not themselves contain comparability edges.

In permutation language, they are decreasing blocks.

Such a block represents a collection of mutually incomparable elements that the outside graph treats as one module.

Because there is no internal comparability edge to orient, this substitution introduces no new orientation choice.

This gives a direct structural explanation for why these modules are harmless.

## 11. Substitution-decomposition interpretation

The emerging picture is:

- prime/simple quotient structure can carry the nontrivial order skeleton;
- decreasing inflations can replace some vertices by internally incomparable blocks without adding orientation ambiguity;
- series-like/non-decreasing blocks create extra orientation degrees of freedom and destroy UPO recovery.

This is precisely the language in which a future enumeration should be formulated.

## 12. Why this matters for the physics question

The causal interpretation becomes:

> A cluster of events may be externally indistinguishable in symmetric comparability data without harming global orientation recovery, provided the cluster itself contains no causal comparability that must be oriented.

In contrast:

> an externally modular cluster with internal causal comparability hides additional orientation information.

This is a sharper statement than “incomparability helps.”

## 13. Relation to simple-permutation asymptotics

Simple permutations have a classical asymptotic enumeration.

Their fraction among all permutations is known to approach a positive constant.

However the project recovery class is larger because it permits decreasing modular inflations.

Therefore the asymptotic UPO-recovery probability cannot be identified with the simple-permutation probability.

A separate substitution-decomposition enumeration is required.

## 14. Current status of asymptotics

No asymptotic formula is currently established.

The exact recovery probabilities through \(N=9\) are nonmonotone.

The permutation-block characterization gives a plausible route to a recurrence or generating-function description, but none has yet been derived.

The project must not extrapolate the finite sequence.

## 15. Next mathematical target

The next rigorous problem is:

> Enumerate permutations whose unique nontrivial comparability component has only decreasing proper common intervals.

A useful route is to express the class through substitution decomposition:

- identify admissible prime skeletons;
- characterize allowed decreasing inflations;
- handle isolated/skew components correctly;
- avoid multiple counting from non-unique inflation descriptions.

Only after a correct recurrence or canonical decomposition is proved should asymptotic recovery probability be studied.

## 16. Current conclusion

The random-\(2\)-order orientation problem now has two equivalent working descriptions:

### Graph language

$$
\text{UPO}
=
\text{one nontrivial component}
+
\text{no proper non-stable module}.
$$

### Permutation language

$$
\text{UPO}
=
\text{one nontrivial component}
+
\text{all proper common intervals decreasing}.
$$

The second language is the better route toward enumeration.

The next obstacle is combinatorial counting, not physical interpretation.
