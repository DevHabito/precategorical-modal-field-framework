# Causal comparability as a random-free graphon

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** literature bridge and reformulation; no new graphon theorem claimed

## 1. Kernel formulation

Let

\[
(D,\mu)
\]

be a flat Alexandrov interval with normalized volume measure.

Define the symmetric causal-comparability kernel

\[
\boxed{
W(x,y)
=
\mathbf1_{\{x\sim y\}}.
}
\]

Because \(W\) takes only the values \(0\) and \(1\), it is a random-free graphon.

Sampling

\[
X_1,\ldots,X_n
\stackrel{\mathrm{iid}}{\sim}
\mu
\]

and joining \(i,j\) exactly when

\[
W(X_i,X_j)=1
\]

produces the arrow-erased Minkowski comparability graph studied in the reconstruction program.

## 2. Neighborhood metric

Graphon theory uses the neighborhood pseudometric

\[
r_W(x,y)
=
\int_D
|W(x,z)-W(y,z)|
\,d\mu(z).
\]

For the causal-comparability kernel,

\[
|W(x,z)-W(y,z)|
=
1
\]

exactly when \(z\) is comparable to one of \(x,y\) and not the other.

Therefore

\[
\boxed{
r_W(x,y)
=
\mu(A_x\triangle A_y)
=
\Delta(x,y).
}
\]

Thus the disagreement volume introduced in the UPO analysis is exactly the graphon neighborhood metric.

## 3. Twin interpretation

Two graphon points are twins when

\[
W(x,\cdot)
=
W(y,\cdot)
\]

almost everywhere.

Equivalently,

\[
r_W(x,y)=0.
\]

For generic distinct interior points of a Minkowski Alexandrov interval,

\[
\Delta(x,y)>0.
\]

The only exact continuum coincidences occur on measure-zero boundary degeneracies, so the kernel is twin-free in the measure-theoretic sense relevant to graphon theory.

Finite sampled true twins are therefore not continuum twins.

They arise because the finite sample fails to hit the positive-measure disagreement region between two distinct continuum neighborhoods.

This is exactly why their probability contains

\[
(1-\Delta)^{n-2}.
\]

## 4. The d=4 small-distance law

The proved \(3+1\) result can now be read as a statement about the small-distance geometry of the causal graphon along comparable pairs:

\[
\boxed{
\Pr(
W(X,Y)=1,\,
r_W(X,Y)\le\varepsilon
)
\sim
3\pi\varepsilon^3.
}
\]

The exponent is not the ordinary bulk spacetime dimension \(4\).

It is produced by the codimension-two null joint of the Alexandrov interval.

This boundary singularity controls the finite sampled-twin rate

\[
\boxed{
\mathbb E[T_n]
\sim
\frac{9\pi}{n}.
}
\]

## 5. What graphon theory does and does not supply

The notions used here are established:

- random-free graphons;
- twin-free graphons;
- the neighborhood metric
  \[
  r_W(x,y)=\|W(x,\cdot)-W(y,\cdot)\|_{L^1};
  \]
- sampling finite graphs from a graphon.

The project does not claim novelty for these notions.

A targeted search did not locate a theorem that directly implies:

\[
\Pr(
G_n(W)\text{ is modular-prime or UPO}
)
\to1
\]

for the present Minkowski kernel.

Twin-free alone is not enough to control arbitrary finite modules.

The global problem therefore remains genuinely stronger than pairwise twin-freeness.

## 6. Research consequence

The graphon reformulation clarifies the roles of the current objects:

\[
\Delta(x,y)
=
r_W(x,y)
\]

controls the first generation of splitter closure.

For a seed edge \(\{x,y\}\), the number of sampled first-generation splitters is

\[
\operatorname{Binomial}
\left(
n-2,\,
r_W(x,y)
\right).
\]

Hence the unresolved UPO limit can be restated as a finite-sample modular-closure problem over a random-free Lorentzian graphon.

This suggests two possible next routes:

1. prove a Minkowski-specific splitter-cascade theorem using quantitative lower bounds in \(r_W\);
2. develop or locate a graphon-level theorem controlling modules in finite samples of kernels with sufficiently nondegenerate neighborhood geometry.

At present the first route is better supported by the project-specific calculations.
