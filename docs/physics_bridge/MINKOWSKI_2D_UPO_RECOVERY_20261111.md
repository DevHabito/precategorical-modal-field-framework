# 1+1 Minkowski finite control — recovering causal order from unoriented connectibility

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact finite random-2-order control  
**Physical status:** causal-set-inspired calibration; not an empirical test  
**Novelty status:** random 2D orders, Minkowski sprinklings, comparability graphs, and UPO theory are classical. No exact combined prior was located in the targeted search; absolute novelty is not certified.

## 1. Question

Suppose the primitive data do not contain a future/past arrow.

Instead, retain only the symmetric relation

$$
x\sim y
\quad\Longleftrightarrow\quad
x\prec y\ \text{or}\ y\prec x.
$$

For a finite partial order, this is exactly its comparability graph.

The question is:

> When does this unoriented relation contain enough information to reconstruct the original partial order up to global duality?

For a nontrivial UPO comparability graph, the answer is exactly yes.

## 2. Why 1+1 Minkowski is a controlled physical benchmark

A finite causet faithfully embedded in a flat \(1+1\)-dimensional causal interval can be described in light-cone coordinates

$$
u=t+x,
\qquad
v=t-x.
$$

For generic points,

$$
p\prec q
$$

iff both light-cone coordinates increase.

A sprinkling of \(N\) independent uniform points into a flat causal diamond is therefore equivalent, conditioned on \(N\), to the intersection of two independent random total orders.

After relabeling one total order to the identity, the second is a uniformly random permutation

$$
\pi\in S_N.
$$

Thus an exact enumeration over all

$$
N!
$$

permutations gives the finite probability distribution of this random-2-order model for any isomorphism-invariant property.

This equivalence is established causal-set literature.

## 3. Order from a permutation

Fix vertices

$$
0,\ldots,N-1
$$

in increasing \(u\)-order.

For a permutation \(\pi\), define

$$
i\prec_\pi j
$$

when

$$
i<j
\quad\text{and}\quad
\pi(i)<\pi(j).
$$

The unoriented connectibility graph has edge

$$
\{i,j\}
$$

exactly when the pair is comparable under \(\prec_\pi\).

The original orientation is one transitive orientation of this graph.

## 4. Recovery criterion

Let

$$
\mathrm{TO}(G)
$$

be the set of transitive orientations of the connectibility graph.

### Nontrivial orientation-torsor recovery

If

$$
|\mathrm{TO}(G)|=2
$$

and the two are global reverses, then the causal order is recoverable up to one global time reversal.

This is the nontrivial UPO case used here.

### Self-dual empty control

The antichain has an empty comparability graph.

It has one empty orientation, which equals its own reverse.

The order is trivially reconstructible but contains no causal arrow.

It is reported separately rather than counted as a nontrivial time-orientation torsor.

## 5. Exact enumeration

All permutations were enumerated for

$$
N=2,\ldots,7.
$$

No random sampling was used.

The number of nontrivial UPO permutations is:

| N | permutations | nontrivial UPO | exact fraction | decimal |
|---:|---:|---:|---:|---:|
|2|2|1|\(1/2\)|0.500000|
|3|6|4|\(2/3\)|0.666667|
|4|24|12|\(1/2\)|0.500000|
|5|120|38|\(19/60\)|0.316667|
|6|720|165|\(11/48\)|0.229167|
|7|5040|1042|\(521/2520\)|0.206746|

These are exact finite probabilities under the uniform relative-permutation model.

## 6. Depth among recoverable orders

The UPO cases do not all contain extended chains.

Their exact depth histograms are:

### N = 5

$$
34
$$

have depth 1 and

$$
4
$$

have depth 2.

### N = 6

$$
98
$$

have depth 1 and

$$
67
$$

have depth 2.

### N = 7

$$
294
$$

have depth 1,

$$
664
$$

have depth 2, and

$$
84
$$

have depth 3.

Thus orientation recoverability and causal depth are separate properties.

## 7. Total-chain control

Take

$$
\pi=(0,1,\ldots,N-1).
$$

Every pair is comparable.

The unoriented graph is

$$
K_N.
$$

Every total ordering of the vertices is a transitive orientation of \(K_N\).

Therefore

$$
\boxed{
|\mathrm{TO}(K_N)|=N!.
}
$$

For

$$
N\ge3,
$$

the symmetric connectibility relation completely fails to identify the original sequence up to global reversal.

This is an important obstruction.

A purely chain-like universe loses almost all ordering information when the arrow is erased.

## 8. Antichain control

For the reverse permutation

$$
\pi=(N-1,\ldots,0),
$$

no pair is comparable.

The connectibility graph is empty.

Its order is trivially self-dual, but it carries no causal succession.

Therefore neither extreme is useful for emergent orientation:

- total comparability contains too many possible directions;
- total incomparability contains no directed structure to orient.

## 9. Incomparability carries reconstructive information

For a nontrivial UPO graph with more than two vertices, the graph cannot be complete.

Therefore some incomparable pair must exist.

Under this specific reconstruction contract,

$$
\boxed{
\text{some incomparability is necessary for nontrivial order recovery}.
}
$$

In a causal interpretation, incomparability corresponds to spacelike separation.

This does **not** prove that physical space is necessary for time.

It says only:

> if the only primitive input is symmetric causal connectibility, a total chain does not contain enough information to reconstruct its temporal order; patterns of incomparability can carry the missing relational information.

## 10. Relation to causal-set theory

Standard causal-set theory takes the directed partial order itself as primitive.

The present control deliberately weakens that input.

It asks whether one could instead begin from the undirected relation

$$
x\sim y
$$

meaning only that the two events are causally comparable.

When the resulting graph is UPO, the directed causet is recovered up to duality.

This is not the standard CST ontology.

It is a pregeometric reconstruction experiment motivated by CST.

## 11. Relation to Lorentzian time orientability

A connected time-orientable Lorentzian manifold has two global time orientations.

The UPO reconstruction pattern has the same abstract two-fold form:

$$
G
\longrightarrow
\{P,P^{\mathrm{op}}\}.
$$

The analogy is structural only.

A UPO graph does not supply:

- a Lorentzian metric;
- null cones;
- manifold topology;
- dimension;
- proper time.

## 12. Finite trend must not be extrapolated

The finite UPO fractions in this audit decrease from \(N=3\) through \(N=7\), apart from the initial small-size oscillation.

No asymptotic conclusion follows.

Möhring's theorem that almost all comparability graphs are UPO uses a different ensemble: roughly speaking, uniform counting over comparability graphs, not the random-2-order measure induced by a Minkowski sprinkling.

Therefore there is no contradiction.

The two measures weight graph structures differently.

## 13. Literature-search boundary

Targeted searches located:

- the random-2-order/Minkowski-sprinkling equivalence;
- classical UPO graph theory;
- permutation/comparability graph theory;
- causal-set use of partial orders.

No exact source was located that studies the probability that the comparability graph of a finite random 2D causal order is UPO specifically for the purpose of recovering causal orientation from symmetric connectibility.

This is only limited negative evidence.

No novelty or priority claim is made.

## 14. Current conclusion

The first physical-like control gives a mixed result.

### Positive

Some finite Minkowski \(1+1\) random orders contain enough unoriented connectibility information to reconstruct their causal order up to global reversal.

### Negative

Many do not.

At \(N=7\), the exact nontrivial recovery fraction is only

$$
\boxed{
\frac{521}{2520}\approx0.206746.
}
$$

Thus manifold-like origin does not automatically imply orientation recoverability after the arrow is erased.

## 15. Next question

The next rigorous question is:

> What structural features of a causal order make its unoriented comparability relation UPO, and are those features enhanced or suppressed in physically motivated causal-set ensembles as \(N\) grows?

That question belongs first to order/comparability theory and causal-set statistics.

It should be answered before any claim that time orientation generically emerges from unoriented causal connectibility.
