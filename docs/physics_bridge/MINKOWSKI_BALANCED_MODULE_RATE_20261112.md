# Theorem: balanced modules are superpolynomially rare in Minkowski graphon samples

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** quantitative graphon-transfer theorem  
**Physical status:** rate bound for macroscopic internal modular obstructions after causal-arrow erasure  
**Novelty status:** weakly homogeneous graphon sets and graphon sampling lemmas are established; the project-specific input is primeness of the Minkowski causal-comparability graphon

## 1. Statement

Fix an integer spacetime dimension

\[
d\ge2.
\]

Let

\[
W_d(x,y)
=
\mathbf1_{\{x\sim y\}}
\]

be the causal-comparability graphon of a fixed flat Minkowski Alexandrov interval.

For every fixed

\[
\varepsilon\in(0,1/2),
\]

there exists

\[
n_0(d,\varepsilon)
\]

such that, for all

\[
n\ge n_0,
\]

\[
\boxed{
\Pr\!\left(
G(n,W_d)
\text{ contains a graph module }M
\text{ with }
\varepsilon n\le|M|\le(1-\varepsilon)n
\right)
\le
\exp\!\left(
-\frac{n}{2\log n}
\right).
}
\]

Thus balanced macroscopic modules are superpolynomially rare.

## 2. The balanced homogeneous-set class

For fixed \(\varepsilon>0\), let

\[
\mathcal H_\varepsilon
\]

be the class of graphons that admit a weakly homogeneous measurable set \(S\) satisfying

\[
\varepsilon
\le
\mu(S)
\le
1-\varepsilon.
\]

The causal-comparability graphon \(W_d\) is prime:

\[
W_d\notin\mathcal H_\varepsilon.
\]

The issue is whether graphons in \(\mathcal H_\varepsilon\) can nevertheless approach \(W_d\) arbitrarily closely in cut distance.

They cannot.

## 3. Positive cut-distance gap

Define

\[
\rho_{d,\varepsilon}
=
\inf_{U\in\mathcal H_\varepsilon}
\delta_\square(U,W_d).
\]

Then

\[
\boxed{
\rho_{d,\varepsilon}>0.
}
\]

### Proof by contradiction

Assume

\[
\rho_{d,\varepsilon}=0.
\]

Then there exists a sequence

\[
U_m\in\mathcal H_\varepsilon
\]

with

\[
\delta_\square(U_m,W_d)\to0.
\]

For each \(m\), choose a weakly homogeneous set

\[
S_m
\]

with

\[
\varepsilon
\le
\mu(S_m)
\le
1-\varepsilon.
\]

Colour \(S_m\) red and its complement blue.

Finite-colour graphon compactness gives a convergent coloured subsequence.

The uncoloured limit is weakly isomorphic to \(W_d\).

The limiting red density may be mixed, so write it as

\[
f:D\to[0,1],
\]

with

\[
\varepsilon
\le
\int f\,d\mu
\le
1-\varepsilon.
\]

## 4. Zero splitter density survives the limit

Because \(S_m\) is homogeneous, the coloured splitter density is exactly zero:

there is no triple

\[
x,y\in S_m,
\qquad
z\notin S_m
\]

for which \(z\) is adjacent to exactly one of \(x,y\).

The coloured counting lemma transfers this zero density to the limit:

\[
\int
f(x)f(y)(1-f(z))
\mathbf1_{\{
W_d(z,x)\ne W_d(z,y)
\}}
\,d\mu(x)d\mu(y)d\mu(z)
=
0.
\]

Let

\[
R=\{x:f(x)>0\}.
\]

If

\[
\mu(R)<1,
\]

then for almost every

\[
z\notin R
\]

the row

\[
W_d(z,\cdot)
\]

is constant almost everywhere on \(R\).

Thus \(R\) is a nontrivial weakly homogeneous set of \(W_d\), contradicting causal-graphon primeness.

If

\[
\mu(R)=1,
\]

the upper mass bound

\[
\int f\le1-\varepsilon
\]

implies that

\[
\{z:f(z)<1\}
\]

has positive measure.

For almost every such \(z\), the zero splitter density forces

\[
W_d(z,\cdot)
\]

to be constant almost everywhere on all of \(D\).

But almost every interior Minkowski point has

\[
0<Q_d(z)<1,
\]

so its comparability row is not constant.

This is again a contradiction.

Therefore

\[
\rho_{d,\varepsilon}>0.
\]

## 5. Finite graph modules produce homogeneous step graphons

Let \(G\) be a finite graph on \(n\) vertices.

If

\[
M\subseteq V(G)
\]

is a module, then in the empirical step graphon \(W_G\), the union of the vertex intervals corresponding to \(M\) is a strongly homogeneous measurable set.

If

\[
\varepsilon n
\le
|M|
\le
(1-\varepsilon)n,
\]

then

\[
W_G\in\mathcal H_\varepsilon.
\]

Hence

\[
\boxed{
\delta_\square(W_G,W_d)
\ge
\rho_{d,\varepsilon}.
}
\]

## 6. Second Sampling Lemma

The Second Sampling Lemma for graphons gives the following standard estimate.

For

\[
G_n=G(n,W_d),
\]

with probability at least

\[
1-
\exp\!\left(
-\frac{n}{2\log n}
\right),
\]

\[
\boxed{
\delta_\square(G_n,W_d)
\le
\frac{22}{\sqrt{\log n}}.
}
\]

Choose \(n_0\) so large that

\[
\frac{22}{\sqrt{\log n}}
<
\rho_{d,\varepsilon}
\]

for all \(n\ge n_0\).

On the sampling-good event, the sampled graphon therefore cannot belong to

\[
\mathcal H_\varepsilon.
\]

Consequently,

\[
\boxed{
\Pr(
G_n
\text{ contains an }\varepsilon\text{-balanced module}
)
\le
\exp\!\left(
-\frac{n}{2\log n}
\right).
}
\]

## 7. Quantitative consequence for d >= 4

For every fixed

\[
d\ge4,
\]

the verified comparable true-twin scale is

\[
n^{-4/d}.
\]

The balanced-module probability satisfies

\[
\exp\!\left(
-\frac{n}{2\log n}
\right)
=
o(n^{-m})
\]

for every fixed \(m>0\).

Therefore

\[
\boxed{
\Pr(
\text{balanced macroscopic module}
)
=
o(
n^{-4/d}
).
}
\]

Balanced modules cannot contribute to the leading UPO failure constant.

## 8. Literature boundary

The proof uses established graphon machinery.

Hatami and Norin define weakly homogeneous graphon sets as the measurable analogue of finite homogeneous sets/modules.

The graphon Second Sampling Lemma appears as Lemma 10.16 in Lovász's *Large Networks and Graph Limits*, based on sampling results of Borgs, Chayes, Lovász, Sós, and Vesztergombi.

The project-specific statement is the positive cut-distance separation from the Minkowski causal graphon, which follows from the previously proved causal-graphon primeness theorem.

No new graphon sampling inequality is claimed here.

## 9. Remaining quantitative obstruction

After combining:

- true-twin occurrence,
- the fixed-size module hierarchy,
- the subleading non-twin escalation theorem,
- and the present balanced-module bound,

a competing contribution at order

\[
n^{-4/d}
\]

can only come from an **unbalanced growing module**, equivalently a near-whole module with a sublinear complement.

That is now the only unresolved regime for a matching upper bound on

\[
1-p_d^{\mathrm{UPO}}(n).
\]
