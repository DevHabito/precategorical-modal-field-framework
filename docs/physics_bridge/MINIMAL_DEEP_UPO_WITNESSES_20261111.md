# Minimal deep UPO witnesses — bull and house graphs

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact finite classification inside classical UPO graph theory  
**Novelty status:** UPO theory is classical; this finite search is a project calibration, not a new graph-theory claim

## 1. Why UPO is the stricter pregeometric benchmark

The diamond audit used an additional selection principle:

> retain a transitive-orientation duality class only when the full graph automorphism group preserves that class.

This is mathematically legitimate, but it is still an extra criterion.

For an anti-ad-hoc pregeometric benchmark, a stricter target is preferable:

$$
\boxed{
|\mathrm{TO}(G)|=2.
}
$$

Then the undirected graph itself admits only

$$
O
$$

and

$$
O^{\mathrm{op}}.
$$

No other partial-order structure must be rejected by an added selection rule.

This is exactly the classical UPO property.

## 2. Finite search

Every connected labeled simple graph was exhaustively enumerated for

$$
n=2,3,4,5.
$$

For each graph the audit enumerated every edge orientation and retained those satisfying exact transitivity.

Among UPO graphs, it measured the longest directed chain.

The first UPO graphs with chain depth at least two occur at

$$
\boxed{
n=5.
}
$$

There are exactly

$$
120
$$

labeled witnesses.

They form two unlabeled isomorphism classes.

## 3. Bull graph

The first class is the bull graph.

It consists of a triangle with two pendant edges attached to two different triangle vertices.

A representative edge set is

$$
\{
01,02,12,13,24
\}.
$$

Its degree multiset is

$$
\{1,1,2,3,3\}.
$$

It has exactly two transitive orientations.

One representative is

$$
1\to0,
\qquad
0\to2,
\qquad
1\to2,
\qquad
1\to3,
\qquad
4\to2.
$$

The reverse is the only other transitive orientation.

There are directed chains of length two, for example

$$
1\to0\to2.
$$

Thus the bull supplies:

$$
\boxed{
\text{unique order class modulo reversal}
+
\text{nontrivial ordinal depth}.
}
$$

## 4. House graph

The second class is the house graph.

A representative edge set is

$$
\{
01,02,13,23,24,34
\}.
$$

Its degree multiset is

$$
\{2,2,2,3,3\}.
$$

It also has exactly two transitive orientations.

One representative is

$$
1\to0,
\qquad
1\to3,
\qquad
2\to0,
\qquad
2\to3,
\qquad
2\to4,
\qquad
4\to3.
$$

The reverse is the only other transitive orientation.

It has depth-two chains such as

$$
2\to4\to3.
$$

## 5. Exact isomorphism classification

The 120 labeled depth-two UPO witnesses at \(n=5\) split as:

| unlabeled type | labeled copies |
|---|---:|
| bull | 60 |
| house | 60 |

Each graph has an automorphism group of order 2, so

$$
\frac{5!}{2}=60
$$

labeled copies occur in each isomorphism class.

This exactly accounts for all 120 witnesses.

## 6. Minimality in the audited range

For connected labeled graphs:

- \(n=2\): UPO exists, but depth is 1;
- \(n=3\): UPO exists, but depth is 1;
- \(n=4\): all 19 UPO graphs have depth 1;
- \(n=5\): 120 UPO graphs have depth 2.

Therefore the finite enumeration establishes:

$$
\boxed{
\text{no connected UPO graph on fewer than five vertices
has transitive depth }2.
}
$$

This is an exact finite statement for simple graphs.

## 7. Why this is cleaner than the diamond criterion

The diamond has six transitive orientations.

A project-specific automorphism filter selects one reversal pair from the three available pairs.

The bull and house graphs need no such filter.

Their transitive order is unique up to global reversal by classical UPO structure.

Thus, for the purpose

> recover an order axis from unoriented finite structure without an extra selection principle,

the bull and house are cleaner witnesses.

## 8. What is actually reconstructed

From either graph one can reconstruct:

- a strict partial order;
- its global reverse;
- nontrivial chain depth.

One cannot reconstruct:

- which member is future;
- metric duration;
- a Lorentzian cone;
- locality in a spacetime sense;
- physical causality;
- continuum dimension.

The recovered object is an ordinal partial-order torsor.

## 9. Physical significance remains open

The same UPO graph can represent a purely non-temporal order:

- containment;
- dependency;
- task precedence;
- resource hierarchy;
- inclusion;
- another poset semantics.

Therefore UPO structure is not evidence of time by itself.

Its value is narrower:

$$
\boxed{
\text{unoriented relational data can, in some cases,
determine a partial order uniquely up to global reversal}.
}
$$

This is the structural property a pregeometric physical bridge would have to interpret.

## 10. Current pregeometric target

The strongest non-ad-hoc finite target is now:

> Find a physically justified unoriented primitive relation whose comparability graph is UPO, or tends toward UPO-like recoverability in an appropriate regime, and whose unique order class can be independently identified with causal order.

This removes the need for an extra mathematical rule selecting among several partial orders.

## 11. Boundary with causal-set theory

Causal-set theory begins with the partial order itself as primitive.

The present route asks a different question:

> could a weaker unoriented relational object determine that partial order up to global reversal?

For UPO comparability graphs, the mathematical answer is yes.

Whether nature supplies such an unoriented precursor is entirely open.

## 12. Current conclusion

The diamond remains useful for studying automorphism-stable selection among multiple orders.

For the stricter anti-ad-hoc programme, however, the bull and house graphs are better minimal controls.

They demonstrate the first finite stage:

$$
\boxed{
\text{unoriented structure}
\longrightarrow
\{P,P^{\mathrm{op}}\}
}
$$

with genuine order depth.

The next question is physical, not combinatorial.
