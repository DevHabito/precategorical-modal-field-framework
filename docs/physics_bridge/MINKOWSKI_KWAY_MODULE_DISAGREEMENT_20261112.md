# Exact k-way disagreement functional for graph modules

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact combinatorial-probabilistic framework for arbitrary module size  
**Physical status:** internal UPO obstruction analysis for arrow-erased Minkowski causal sets  
**Novelty status:** graph modules/homogeneous sets are classical; the contribution here is the exact continuum disagreement formulation specialized to Minkowski causal graphons and splitter closure

## 1. Purpose

The component problem is now closed asymptotically:

\[
\Pr(
\text{more than one edge-containing component}
)
\to0.
\]

Therefore higher-dimensional UPO recovery has been reduced to internal non-stable modules inside the unique nontrivial component.

The remaining difficulty is that a proper non-stable module may have size growing with \(n\).

This note introduces a single \(k\)-way continuum functional that treats every module size uniformly.

## 2. k-way disagreement region

For points

\[
x_1,\ldots,x_k\in D,
\]

let

\[
A_i
=
A_{x_i}
=
\{z:z\sim x_i\}.
\]

Define the **k-way splitter region**

\[
\boxed{
\mathcal D_k(x_1,\ldots,x_k)
=
\left(
\bigcup_{i=1}^k A_i
\right)
\setminus
\left(
\bigcap_{i=1}^k A_i
\right).
}
\]

Equivalently,

\[
z\in\mathcal D_k
\]

exactly when \(z\) is adjacent to some but not all of the \(x_i\).

Define its normalized volume

\[
\boxed{
\Delta_k(x_1,\ldots,x_k)
=
\mu(\mathcal D_k(x_1,\ldots,x_k)).
}
\]

For \(k=2\),

\[
\Delta_2(x_1,x_2)
=
\mu(A_{x_1}\triangle A_{x_2}),
\]

so this extends the pairwise graphon-neighborhood distance already used in the true-twin theorem.

## 3. Exact finite-sample module probability

Condition on \(k\) sampled points

\[
X_1=x_1,\ldots,X_k=x_k.
\]

The set

\[
M=\{1,\ldots,k\}
\]

is a graph module exactly when every one of the remaining \(n-k\) sample points is adjacent either to all members of \(M\) or to none of them.

That is equivalent to requiring all outside sample points to avoid

\[
\mathcal D_k.
\]

Hence

\[
\boxed{
\Pr(
M\text{ is a module}
\mid
X_1=x_1,\ldots,X_k=x_k
)
=
(1-\Delta_k)^{n-k}.
}
\]

This identity is exact.

## 4. Expected number of non-stable k-modules

Let \(N_{k,n}^{\mathrm{ns}}\) be the number of size-\(k\) graph modules whose induced graph contains at least one edge.

Then

\[
\boxed{
\mathbb E[N_{k,n}^{\mathrm{ns}}]
=
\binom nk
\mathbb E
\left[
\mathbf1_{\{
G[X_1,\ldots,X_k]
\text{ contains an edge}
\}}
(1-\Delta_k)^{n-k}
\right].
}
\]

This is the arbitrary-\(k\) analogue of the exact true-twin identity.

For \(k=2\), it reduces to

\[
\mathbb E[T_n]
=
\binom n2
\mathbb E[
\mathbf1_{\{X_1\sim X_2\}}
(1-\Delta_2)^{n-2}
].
\]

## 5. Pointwise binary identity

Fix an outside point \(z\).

Write

\[
b_i(z)
=
\mathbf1_{\{z\sim x_i\}}
\in\{0,1\}.
\]

Let

\[
m(z)
=
\sum_{i=1}^k b_i(z).
\]

The number of unordered pairs

\[
\{i,j\}
\]

for which \(z\) distinguishes \(x_i\) and \(x_j\) is exactly

\[
\boxed{
m(z)(k-m(z)).
}
\]

Also,

\[
z\in\mathcal D_k
\iff
0<m(z)<k.
\]

For a nonconstant binary signature,

\[
k-1
\le
m(k-m)
\le
\left\lfloor\frac{k^2}{4}\right\rfloor.
\]

## 6. Pairwise-energy bounds

Integrating the pointwise identity gives

\[
\boxed{
(k-1)\Delta_k
\le
\sum_{1\le i<j\le k}
\Delta_2(x_i,x_j)
\le
\left\lfloor\frac{k^2}{4}\right\rfloor
\Delta_k.
}
\]

Equivalently,

\[
\boxed{
\frac{
\sum_{i<j}\Delta_2(x_i,x_j)
}{
\lfloor k^2/4\rfloor
}
\le
\Delta_k
\le
\frac{
\sum_{i<j}\Delta_2(x_i,x_j)
}{
k-1
}.
}
\]

Thus the arbitrary-size splitter volume is quantitatively equivalent, up to explicit \(k\)-dependent factors, to the total pairwise graphon-neighborhood energy.

## 7. Tree identity

Let \(T\) be any tree on the index set

\[
\{1,\ldots,k\}.
\]

Then

\[
\boxed{
\mathcal D_k
=
\bigcup_{\{i,j\}\in E(T)}
(A_i\triangle A_j).
}
\]

### Proof

If all binary values \(b_i(z)\) are equal, no tree edge has different endpoint values.

Conversely, if the binary signature is not constant, a connected tree must contain an edge crossing from a vertex with value \(0\) to a vertex with value \(1\).

Therefore

\[
z\in\mathcal D_k
\]

if and only if \(z\) lies in at least one symmetric difference associated with a tree edge.

No probability or approximation enters this identity.

Consequently,

\[
\boxed{
\max_{\{i,j\}\in E(T)}
\Delta_2(x_i,x_j)
\le
\Delta_k
\le
\sum_{\{i,j\}\in E(T)}
\Delta_2(x_i,x_j).
}
\]

## 8. Minimal edge-generated modules are internally connected

Start splitter closure from an edge

\[
\{x_1,x_2\}.
\]

Every newly added splitter is adjacent to at least one current member and nonadjacent to at least one current member.

Therefore each newly added vertex has an internal edge to the existing closure.

By induction, every edge-generated minimal module is connected as an induced graph.

This means the tree identity can be applied to a genuine internal spanning tree of every minimal non-stable module.

## 9. Exact outside-avoidance interpretation

For a candidate module \(M\),

\[
(n-|M|)\Delta_{|M|}(M)
\]

is the natural outside-splitter intensity.

If

\[
(n-|M|)\Delta_{|M|}\gg1,
\]

then the module event carries the exponential penalty

\[
(1-\Delta_{|M|})^{n-|M|}
\le
\exp(
-(n-|M|)\Delta_{|M|}
).
\]

Therefore a proper module with a large outside population can survive only if its k-way disagreement volume is correspondingly small.

This is the quantity that must now be controlled geometrically.

## 10. Relation to graphon homogeneous sets

Graph theory calls modules **homogeneous sets**.

Graphon literature also uses weakly homogeneous measurable sets: outside points see the entire measurable set with a constant adjacency value.

That literature establishes the concept but does not provide the finite-sample Minkowski asymptotic required here.

The continuum object

\[
\Delta_k
\]

measures how far a finite tuple is from being homogeneous in exactly the direction relevant to random sampling.

## 11. Computational regression

The finite binary identities are exhaustively checked by

tools/verify_kway_module_disagreement.py.

For every binary signature through the selected \(k\)-range, the script verifies:

\[
\sum_{i<j}
\mathbf1_{\{b_i\ne b_j\}}
=
m(k-m),
\]

the explicit lower and upper factors, and the tree-union identity for both path and star trees.

This is a regression of the combinatorial identities, not a substitute for the analytic arguments.

## 12. Current analytic target

The remaining UPO theorem can now be stated as a quantitative small-\(\Delta_k\) problem.

The target is to prove a uniform estimate of the form

\[
\Pr(
G[X_1,\ldots,X_k]
\text{ contains an edge},
\;
\Delta_k\le\varepsilon
)
\le
\mathcal B_k(\varepsilon)
\]

strong enough that

\[
\sum_{k=2}^{n-1}
\binom nk
\int
(1-\delta)^{n-k}
\,d\mathcal B_k(\delta)
\to0.
\]

The \(k=2\) and \(k=3\) levels are already controlled:

\[
\mathbb E[T_n]
\sim
\frac{9\pi}{n},
\]

and

\[
\mathbb E[M_{3,n}]
=
\Theta(n^{-2}).
\]

The unresolved step is a bound whose constants remain controlled when

\[
k\to\infty.
\]

That is now the sole internal-module frontier.
