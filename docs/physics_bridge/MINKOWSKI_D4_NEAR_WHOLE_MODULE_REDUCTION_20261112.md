# Theorem: reduction of d=4 UPO failure to near-whole internal modules

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic reduction theorem combining edge escalation, splitter concentration, component uniqueness, and causal-graphon primeness  
**Physical status:** final large-scale reduction for arrow-erased \(3+1\)-dimensional Minkowski causal orientation recovery  
**Novelty status:** each imported graph-theoretic/graphon tool is classical; no equivalent Minkowski reconstruction reduction was located in the targeted review

## 1. Setting

Let

\[
G_n=G_{4,n}
\]

be the unoriented comparability graph of an iid size-\(n\) sprinkling into a fixed flat Alexandrov interval of \(\mathbb M^4\).

Let

\[
C_n
\]

be its unique edge-containing component on the high-probability event supplied by the non-isolated giant theorem.

The UPO question is then internal to

\[
C_n.
\]

Isolated vertices outside \(C_n\) are orientation-neutral and must not be confused with an internal modular obstruction.

## 2. Imported established project theorems

The reduction uses four results already proved in the repository.

### 2.1 One nontrivial component

\[
\Pr(
G_n
\text{ has more than one edge-containing component}
)
\to0.
\]

Thus all non-isolated vertices lie in \(C_n\) asymptotically.

### 2.2 Edge escalation

There exists a fixed

\[
\delta_0>0
\]

such that, with probability tending to one, every transitive-orientation implication class contains an edge

\[
e
\]

with

\[
\Delta(e)\ge\delta_0.
\]

### 2.3 Splitter interpretation

For an edge

\[
e=\{x,y\},
\]

the continuum splitter region is

\[
A_x\triangle A_y
\]

and has normalized volume

\[
\Delta(e).
\]

Every sampled point in this region is a splitter of \(e\).

Any graph module containing \(e\) must contain every such sampled splitter.

### 2.4 Balanced-module exclusion

For every fixed

\[
\varepsilon\in(0,1/2),
\]

\[
\Pr\!\left(
\exists\text{ module }M:
\varepsilon n\le |M|\le(1-\varepsilon)n
\right)
\to0.
\]

This follows from primeness of the Minkowski causal graphon and coloured-graphon compactness.

## 3. Uniform splitter concentration for core edges

Condition on a sampled core edge

\[
e
\]

with

\[
\Delta(e)=\delta\ge\delta_0.
\]

Among the remaining \(n-2\) sampled vertices, the number of splitters is

\[
S_e
\sim
\operatorname{Binomial}(n-2,\delta).
\]

A Chernoff bound gives

\[
\Pr\!\left(
S_e<\frac{\delta_0 n}{3}
\mid e
\right)
\le
e^{-c_{\delta_0}n}
\]

for all sufficiently large \(n\).

There are at most

\[
\binom n2
\]

sampled edges.

Therefore a union bound yields

\[
\boxed{
\Pr\!\left(
\exists e:
\Delta(e)\ge\delta_0,\;
S_e<\frac{\delta_0 n}{3}
\right)
\to0.
}
\]

Thus every sampled core edge has a linear number of sampled splitters simultaneously.

## 4. A core edge forces a linear module

Let \(M\) be any graph module of \(C_n\) containing a core edge

\[
e=\{x,y\}.
\]

Every splitter of \(e\) must belong to \(M\).

Hence, on the concentration event,

\[
|M|
\ge
2+S_e
\ge
\frac{\delta_0 n}{3}.
\]

Define

\[
c_0=\frac{\delta_0}{4}.
\]

Then, for all sufficiently large \(n\),

\[
\boxed{
|M|\ge c_0n.
}
\]

This bound is uniform over every module containing a core edge.

## 5. Every internal UPO obstruction contains a core edge

Suppose \(C_n\) is not UPO.

By the classical modular criterion for connected comparability graphs, \(C_n\) contains a proper non-stable module \(M\).

Choose an internal edge

\[
e_0\subset M.
\]

Every splitter-forcing step beginning with an edge of \(M\) remains inside \(M\): an outside vertex cannot distinguish two members of a module.

Therefore the entire implication class of \(e_0\) lies inside \(M\).

By the edge-escalation theorem, that implication class contains a core edge

\[
e
\]

with

\[
\Delta(e)\ge\delta_0.
\]

Hence \(M\) contains a core edge and therefore

\[
\boxed{
|M|\ge c_0n.
}
\]

Thus every remaining UPO obstruction is already macroscopic on one side.

## 6. Balanced macroscopic modules are impossible

Fix any

\[
\varepsilon\in(0,\min\{c_0,1/2\}).
\]

The balanced-module theorem gives

\[
\Pr\!\left(
\exists M:
c_0n\le |M|\le(1-\varepsilon)n
\right)
\to0.
\]

Consequently, on UPO failure, every witnessing proper non-stable module satisfies

\[
|M|>(1-\varepsilon)n
\]

with probability tending to one.

Because \(\varepsilon>0\) is arbitrary,

\[
\boxed{
n-|M|
=
o_p(n).
}
\]

In words:

> any surviving internal orientation obstruction must be a near-whole module.

## 7. Component-size correction

The modular criterion is applied inside \(C_n\), while the balanced-module theorem is stated for \(G_n\).

This causes no problem.

Every isolated vertex of \(G_n\) is anticomplete to every subset of \(C_n\).

Therefore a module

\[
M\subset C_n
\]

of \(C_n\) is also a module of the full graph \(G_n\).

Moreover,

\[
|C_n|=n-I_n,
\]

and in \(d=4\),

\[
I_n=O_p(1)
\]

at the level needed here because

\[
\mathbb E[I_n]\to3\pi.
\]

Thus

\[
n-|M|=o_p(n)
\]

is equivalent to

\[
|C_n|-|M|=o_p(n).
\]

## 8. Final remaining obstruction

Let

\[
R_n=C_n\setminus M.
\]

The current theory now shows that a \(d=4\) UPO failure can survive only through a structure satisfying

\[
\boxed{
|R_n|=o(n),
\qquad
|M|=|C_n|-o(n).
}
\]

Because \(C_n\) is connected and \(M\) is a module, at least one vertex of \(R_n\) must be complete to \(M\).

Other vertices of \(R_n\) may be either complete or anticomplete to \(M\).

Thus the last unresolved configuration is a sublinear exceptional set whose vertices split into two external types relative to an almost-whole homogeneous block.

No small, fixed, sub-square-root, balanced-linear, or multiple-component obstruction remains.

## 9. Relation to previous finite audits

The finite splitter-closure audits already showed that observed proper modules increasingly collapse to size two and three at accessible \(n\), with no persistent population of large residual modules.

Those observations are consistent with the theorem but are not used in its proof.

The reduction is analytic.

## 10. Current theorem frontier

The full \(3+1\) orientation-recovery theorem

\[
p_4^{\mathrm{UPO}}(n)\to1
\]

is now equivalent, up to events of probability tending to zero, to excluding the near-whole module regime

\[
\boxed{
M=C_n\setminus R_n,
\qquad
|R_n|=o(n).
}
\]

Two routes remain plausible:

1. a direct quantitative bound on the polarized exceptional set \(R_n\);
2. a uniform finite-sample discretization of the connected continuum forcing graph, which would make the near-whole analysis unnecessary.

The project should not state the UPO limit as proved until one of these routes is closed.
