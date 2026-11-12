# Edge-seeded splitter closure as the global UPO obstruction reduction

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact graph-theoretic reduction + exact random-2-order regression + higher-dimensional diagnostic  
**Physical status:** causal-orientation reconstruction after arrow erasure  
**Novelty status:** splitter closure and minimal modules are classical modular-decomposition theory; the contribution here is their use as a reduction of the Minkowski UPO reconstruction problem

## 1. Why fixed module sizes are not enough

The current \(3+1\) analysis controls the first two finite obstruction levels:

\[
\mathbb E[T_n]
\sim
\frac{9\pi}{n}
\]

for adjacent true-twin pairs, and

\[
\mathbb E[M_{3,n}]
=
\Theta(n^{-2})
\]

for induced-\(P_3\) modules.

These results strongly suggest a fixed-size hierarchy.

They do not by themselves prove

\[
p_4^{\mathrm{UPO}}(n)\to1,
\]

because a proper non-stable module could in principle have size increasing with \(n\).

There is no general bounded-size witness theorem for graph modules: a minimal proper module may induce a prime graph and can have arbitrarily many vertices.

The correct reduction therefore has to work uniformly over module size.

## 2. Splitters

Let \(G=(V,E)\) be a graph and \(S\subseteq V\).

A vertex

\[
z\in V\setminus S
\]

is a **splitter** of \(S\) when there exist \(x,y\in S\) such that

\[
zx\in E
\]

and

\[
zy\notin E.
\]

Equivalently, \(z\) is adjacent to some but not all vertices of \(S\).

A set \(S\) is a graph module exactly when it has no splitter.

A classical lemma of modular-decomposition theory states:

> if \(z\) splits \(S\), then every module containing \(S\) must also contain \(z\).

Therefore repeated splitter addition computes the unique minimal module containing the initial set.

## 3. Edge-generated modular closure

For an edge

\[
e=\{x,y\},
\]

define the closure sequence

\[
S_0=\{x,y\},
\]

and

\[
S_{j+1}
=
S_j
\cup
\{\text{all splitters of }S_j\}.
\]

Because the graph is finite, the process stabilizes.

Write

\[
\operatorname{cl}(x,y)
\]

for the fixed point.

Then

\[
\boxed{
\operatorname{cl}(x,y)
=
\text{the unique minimal graph module containing }x,y.
}
\]

This is a classical modular-decomposition fact.

## 4. Exact reduction for connected comparability graphs

Let \(G\) be a connected nonempty comparability graph.

The classical UPO criterion says that \(G\) is uniquely partially orderable exactly when every proper nontrivial module is stable.

A non-stable module contains at least one edge.

Hence:

### Proposition

\[
\boxed{
G\text{ is UPO}
\iff
\operatorname{cl}(x,y)=V(G)
\quad
\text{for every edge }\{x,y\}\in E(G).
}
\]

### Proof

If some edge has a proper closure, then that closure is a proper module and contains an edge. It is therefore non-stable, so \(G\) is not UPO.

Conversely, if \(G\) is not UPO, there is a proper non-stable module \(M\). Choose any edge \(\{x,y\}\subseteq M\). By minimality of modular closure,

\[
\operatorname{cl}(x,y)\subseteq M\subsetneq V(G).
\]

Therefore that edge has a proper closure.

\(\square\)

This reduces all possible module sizes to edge-seeded closure processes.

## 5. General disconnected graph

A nonempty comparability graph is UPO precisely when:

1. exactly one connected component contains an edge;
2. every other connected component is an isolated vertex;
3. the unique edge-containing component satisfies the connected closure criterion above.

Thus higher-dimensional reconstruction has two logically distinct failure mechanisms:

\[
\boxed{
\text{component ambiguity}
}
\]

and

\[
\boxed{
\text{proper edge-generated modular closure}.
}
\]

Both can now be audited without enumerating transitive orientations.

## 6. Exact regression against random 2-orders

The closure classifier was independently compared with the Gallai implication-class classifier on every relative permutation through \(n=6\).

The two methods agreed on every permutation.

The exact UPO counts were:

\[
1,\ 4,\ 12,\ 38,\ 165
\]

for

\[
n=2,\ldots,6,
\]

matching the previously established random-2-order results.

This is important because the closure algorithm does not use permutation substitution structure.

It is a generic graph-theoretic classifier.

## 7. Higher-dimensional diagnostic

An independent \(d=4\) audit separated finite failures hierarchically.

The following run used fresh iid sprinklings and classified failures in this order:

1. UPO;
2. presence of at least one adjacent true-twin pair;
3. induced-\(P_3\) module after excluding true twins;
4. multiple nontrivial components without the previous defects;
5. larger internal edge-generated module.

Representative results were:

| \(n\) | samples | UPO | true-twin failure | \(P_3\) failure | multi-component residual | larger internal-module residual |
|---:|---:|---:|---:|---:|---:|---:|
|32|5000|0.7178|0.2474|0.0236|0.0084|0.0028|
|48|5000|0.7902|0.1928|0.0138|0.0024|0.0008|
|64|4000|0.82375|0.16525|0.00925|0.00175|0|
|96|2500|0.8680|0.1260|0.0056|0.0004|0|
|128|1500|0.89133|0.1080|0.00067|0|0|

These are finite Monte Carlo observations.

The zero entries at larger \(n\) are non-detections in finite samples, not proofs that those event classes are impossible.

## 8. What the residual data say

The hierarchy is becoming increasingly concentrated at the smallest local obstructions.

At \(n=96\), among 2500 independent \(3+1\) sprinklings:

\[
86.8\%
\]

were UPO,

\[
12.6\%
\]

contained a true-twin obstruction,

\[
0.56\%
\]

failed first at the induced-\(P_3\) level,

and only

\[
0.04\%
\]

remained as a multiple-nontrivial-component failure after those two levels were removed.

No larger internal proper module was observed in that run after excluding twins and \(P_3\) modules.

At \(n=128\), the same audit found no residual large-module or multiple-component case in 1500 samples.

Again, this is statistical evidence only.

## 9. Continuum meaning of the first closure step

For a comparable seed pair \(x\sim y\), the first splitter region is exactly

\[
A_x\triangle A_y.
\]

Its normalized volume is

\[
\Delta(x,y).
\]

Conditioned on \(x,y\), the number of first-generation splitters among the remaining \(n-2\) sampled events is

\[
\boxed{
N_1\mid x,y
\sim
\operatorname{Binomial}
\left(
n-2,\Delta(x,y)
\right).
}
\]

Thus the true-twin event is exactly

\[
N_1=0.
\]

This recovers the previous identity

\[
\mathbb E[T_n]
=
\binom n2
\mathbb E
\left[
\mathbf1_{\{X\sim Y\}}
(1-\Delta(X,Y))^{n-2}
\right].
\]

For larger closures, the new splitters generated after the first layer define a genuine growth process in comparability-neighborhood space.

## 10. The new global problem

The UPO limit question can now be restated without mentioning arbitrary modules:

> For a random edge in the unique nontrivial component of a \(3+1\) Minkowski sprinkling, does splitter closure either stop at a small module with vanishing probability or expand to the entire component with probability tending to one?

Equivalently, the remaining theorem target is to control

\[
\Pr\!\left(
2<
|\operatorname{cl}(X,Y)|
<
|C_n|
\right)
\]

uniformly over all sampled edges.

This is a bootstrap/closure problem induced by Lorentzian comparability geometry.

## 11. Why this reduction is useful

A direct union bound over every subset \(M\subseteq V\) is hopeless because there are exponentially many candidate modules.

The closure formulation has only

\[
O(n^2)
\]

possible seeds.

More importantly, each seed has a continuum first-layer intensity

\[
n\,\Delta(x,y),
\]

which is already analytically understood near its most dangerous \(d=4\) degeneracy.

The two possible regimes are now visible:

- if \(n\Delta(x,y)\ll1\), the closure can stop at a tiny local module;
- if \(n\Delta(x,y)\gg1\), the first generation already contains many splitters, making a macroscopic cascade plausible.

The unresolved regime is the transition between those two behaviors.

## 12. Literature boundary

Minimal modules, splitters, closure by splitters, forcing graphs, and modular decomposition are established graph theory.

Habib and Paul’s survey on algorithmic modular decomposition describes the classical closure-by-splitter approach and minimal modules containing vertex pairs.

The present project does not claim that construction as new.

What is project-specific is its role as the exact reduction of the geometry-induced Minkowski orientation-recovery problem:

\[
\text{Lorentzian sprinkling}
\to
\text{arrow erasure}
\to
\text{comparability graph}
\to
\text{edge-seeded splitter closure}.
\]

A targeted literature search did not locate an analysis of this closure process under Minkowski sprinkling measure.

This is limited negative evidence only.

## 13. Next theorem target

The strongest route now visible is a two-regime estimate.

### Microscopic seeds

Use the proved small-\(\Delta\) law

\[
F_4(\varepsilon)
\sim
3\pi\varepsilon^3
\]

to control edges with

\[
\Delta=O(1/n).
\]

These produce the fixed-size hierarchy.

### Mesoscopic and macroscopic seeds

Show that once the first splitter generation exceeds a suitable threshold, the iterative disagreement region grows enough that splitter closure reaches the whole nontrivial component with probability tending to one.

If such a cascade lemma can be proved uniformly, the exponentially large module search disappears and the final UPO limit becomes accessible.

That is the current global frontier.
