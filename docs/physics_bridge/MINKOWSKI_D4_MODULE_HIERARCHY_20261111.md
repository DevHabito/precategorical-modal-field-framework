# Size-three module hierarchy after the d=4 twin theorem

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact expectation identity + analytic scaling order + reproducible finite-n audit  
**Physical status:** causal-set reconstruction after arrow erasure  
**Novelty status:** no equivalent causal-set module hierarchy was located in the targeted review; absolute priority is not certified

## 1. Motivation

The d=4 true-twin theorem gives

\[
\mathbb E[T_n]
\sim
\frac{9\pi}{n},
\]

where \(T_n\) counts adjacent true-twin pairs in the arrow-erased comparability graph.

True twins are the minimal size-two non-stable modules and dominate the observed finite UPO failures.

The next question is:

> what is the first obstruction after true-twin pairs are absent?

Finite audits show that the next recurrent minimal obstruction is an induced \(P_3\) graph module.

Its two leaves are incomparable false twins, while the center is comparable to both.

## 2. Size-three non-stable module

Let

\[
M=\{x,y,z\}.
\]

The set \(M\) is a graph module when every vertex outside \(M\) is adjacent either to all three vertices or to none of them.

If the induced graph \(G[M]\) is a path \(P_3\), then \(M\) contains edges and is therefore non-stable.

Such a module obstructs unique partial orderability.

If a size-three module induces a triangle, it already contains true-twin pairs.

Thus, after conditioning away adjacent true twins, the induced \(P_3\) is the first genuinely new size-three obstruction.

## 3. Exact three-point disagreement volume

For three continuum events \(x_1,x_2,x_3\), define

\[
\Delta_3(x_1,x_2,x_3)
=
\mu
\left\{
w:
\bigl(
\mathbf1_{w\sim x_1},
\mathbf1_{w\sim x_2},
\mathbf1_{w\sim x_3}
\bigr)
\text{ is not constant}
\right\}.
\]

Equivalently,

\[
\Delta_3
=
\mu
\left[
(A_{x_1}\triangle A_{x_2})
\cup
(A_{x_1}\triangle A_{x_3})
\right].
\]

A sampled outside event preserves the module condition exactly when it lies outside this disagreement region.

Let \(M_{3,n}\) be the number of induced-\(P_3\) modules in an iid size-\(n\) sprinkling.

Then

\[
\boxed{
\mathbb E[M_{3,n}]
=
\binom n3
\mathbb E
\left[
\mathbf1_{\{\text{induced }P_3\}}
(1-\Delta_3)^{n-3}
\right].
}
\]

This identity is exact.

## 4. Joint scaling in d=4

Near the codimension-two null joint set

\[
\lambda=\sqrt{\varepsilon}.
\]

Each event has two null-depth coordinates of order \(O(\lambda)\).

For three events, the six null-depth coordinates therefore contribute

\[
\lambda^6.
\]

Fix the global angular direction of one event.

The other two must have relative angular displacements of order \(O(\lambda)\) in order to keep their comparability neighborhoods close while maintaining a local induced-\(P_3\) pattern.

In \(3+1\) spacetime each relative angular displacement lies on a two-dimensional joint sphere and contributes

\[
\lambda^2.
\]

There are two such independent relative angular displacements, so the angular contribution is

\[
\lambda^4.
\]

The full joint configuration measure is therefore

\[
\lambda^{10}.
\]

Since

\[
\varepsilon=\lambda^2,
\]

the resulting small-disagreement scale is

\[
\boxed{
\varepsilon^5.
}
\]

The induced-\(P_3\) causal pattern occupies an open set in the blown-up local variables: one event can be timelike related to both others while the two leaves remain mutually spacelike.

## 5. Bulk is subleading

If

\[
\Delta_3\le\varepsilon,
\]

then every pairwise disagreement satisfies

\[
\Delta(x_i,x_j)\le\varepsilon,
\]

because each pairwise symmetric difference is contained in the three-way disagreement region.

Away from the null joint, the pairwise disagreement map has a nonzero linear response.

Thus each of the two additional events must lie within an ordinary \(O(\varepsilon)\) four-dimensional displacement of the first event.

The two relative displacements contribute

\[
O(\varepsilon^8),
\]

which is smaller than the joint contribution:

\[
\varepsilon^8=o(\varepsilon^5).
\]

The same compactness argument used in the true-twin theorem rules out a second lower-order sector away from the joint.

## 6. Size-three tail law

Define

\[
G_{P_3}(\varepsilon)
=
\Pr
\left(
\text{the three sampled events induce }P_3,
\;
\Delta_3\le\varepsilon
\right).
\]

The joint blow-up and the bulk estimate give

\[
\boxed{
G_{P_3}(\varepsilon)
=
\Theta(\varepsilon^5)
\qquad
(\varepsilon\downarrow0).
}
\]

The exponent is determined analytically.

The leading constant has not yet been evaluated.

## 7. Expected module count

Insert the tail order into the exact expectation identity.

The Laplace-Stieltjes scaling gives

\[
\mathbb E
\left[
\mathbf1_{\{P_3\}}
(1-\Delta_3)^{n-3}
\right]
=
\Theta(n^{-5}).
\]

Since

\[
\binom n3=\Theta(n^3),
\]

we obtain

\[
\boxed{
\mathbb E[M_{3,n}]
=
\Theta(n^{-2}).
}
\]

Therefore the first genuinely new size-three obstruction vanishes one full power of \(n\) faster than the true-twin obstruction:

\[
\mathbb E[T_n]=\Theta(n^{-1}),
\]

\[
\mathbb E[M_{3,n}]=\Theta(n^{-2}).
\]

## 8. Reproducible finite-n audit

The repository tool

tools/minkowski_module_hierarchy_audit.py

counts true-twin pairs and induced-\(P_3\) modules directly from Minkowski comparability graphs.

An independent \(d=4\) audit gave:

| \(n\) | samples | mean \(P_3\) modules | Monte Carlo SE | \(n^2\) times mean |
|---:|---:|---:|---:|---:|
|24|12000|0.07167|0.00259|41.28|
|32|10000|0.04310|0.00220|44.13|
|48|8000|0.01925|0.00157|44.35|
|64|6000|0.01317|0.00155|53.93|
|96|3500|0.00629|0.00140|57.93|
|128|2200|0.00318|0.00120|52.13|

The large-\(n\) rows are rare-event estimates and therefore noisy.

No leading constant is inferred from the table.

The finite data are used only as a regression against the analytic order \(n^{-2}\).

## 9. Residual-failure structure

A separate UPO audit classified failures after removing samples containing a true-twin pair.

At moderate sizes, most of those remaining failures contained a size-three non-stable module.

Every size-three module found in the true-twin-free residual sample induced exactly two internal edges:

\[
P_3.
\]

No triangle survives this conditioning because an induced triangle module contains adjacent true twins.

Some residual failures contained no size-three module.

Therefore the \(P_3\) mechanism is not the entire remaining UPO problem.

It is the next identifiable level of the hierarchy.

## 10. Fixed-size module hierarchy suggested by the joint geometry

For a fixed number \(k\) of events whose external comparability signatures become indistinguishable near one null-joint direction in \(d=4\):

- the \(2k\) null-depth coordinates contribute \(\lambda^{2k}\);
- the \(k-1\) relative two-dimensional angular displacements contribute \(\lambda^{2(k-1)}\).

Hence the joint configuration measure has order

\[
\lambda^{4k-2}.
\]

Since

\[
\varepsilon=\lambda^2,
\]

the candidate fixed-\(k\) disagreement exponent is

\[
\boxed{
2k-1.
}
\]

Combining the corresponding \(n^{-(2k-1)}\) rare-event probability with the \(\Theta(n^k)\) possible \(k\)-sets suggests

\[
\boxed{
\mathbb E[M_{k,n}]
=
O(n^{1-k})
}
\]

for fixed-size joint-localized module families satisfying the same nondegeneracy assumptions.

For \(k=2\), this reproduces the proved \(n^{-1}\) true-twin result.

For \(k=3\), it reproduces the \(n^{-2}\) \(P_3\) result.

The general \(k\) statement is currently a scaling program, not a completed theorem for every graph-module type.

## 11. Consequence for UPO recovery

The first two levels are now separated asymptotically:

\[
\boxed{
\text{true-twin pair}
\sim
n^{-1}
}
\]

in expectation, while

\[
\boxed{
P_3\text{ module}
=
\Theta(n^{-2}).
}
\]

This supports a sharper route toward

\[
p_4^{\mathrm{UPO}}(n)
\stackrel{?}{\longrightarrow}
1.
\]

That conclusion still requires control of:

1. all fixed module sizes \(k\ge4\);
2. modules whose size grows with \(n\);
3. non-module mechanisms that can produce multiple implication classes;
4. multiple nontrivial connected components.

The next difficult step is therefore a uniform bound that remains valid when the obstructing structure is allowed to grow with \(n\).

## 12. Literature boundary

True and false twin vertices, graph modules, modular decomposition, and UPO theory are classical graph theory.

Recent work also studies false-twin witness counts in abstract graphs. Those results do not use the geometry-induced Minkowski sprinkling measure and do not address recovery of a causal orientation after arrow erasure.

The project therefore does not claim novelty for twin or module terminology.

The candidate contribution is the Lorentzian asymptotic hierarchy generated by this specific causal-set ensemble and reconstruction contract.

A targeted search did not locate an existing result equivalent to

\[
\mathbb E[M_{3,n}]
=
\Theta(n^{-2})
\]

for induced-\(P_3\) modules in Minkowski-sprinkled comparability graphs.

This remains limited negative evidence only.
