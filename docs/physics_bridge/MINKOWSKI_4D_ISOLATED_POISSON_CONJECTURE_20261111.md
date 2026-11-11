# 3+1 Minkowski isolated-vertex Poisson limit — conjecture and proof program

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** superseded for the Poisson sprinkling ensemble by `MINKOWSKI_4D_ISOLATED_POISSON_THEOREM_20261111.md`; retained as the fixed-cardinality/binomial conjecture and as a record of the factorial-moment route  
**Claim level:** the Poisson-process version is now proved in the project (external review pending); the fixed-(n) version remains unproved

## 1. Question

Let \(C_{4,n}\) be \(n\) iid uniform points in the standard \(3+1\)-dimensional Minkowski Alexandrov interval, and let \(G_n\) be the undirected graph that joins two sampled events exactly when they are causally comparable.

Let

\[
I_n
\]

be the number of isolated vertices of \(G_n\).

The repository has already derived

\[
\boxed{
E[I_n]\to3\pi.
}
\]

The stronger question is whether the complete distribution converges.

For fixed-cardinality/binomial sprinklings, the remaining conjecture is

\[
\boxed{
I_n
\ \xrightarrow{d}\
\operatorname{Poisson}(3\pi).
}
\]

If true, then

\[
P(I_n=0)
\longrightarrow
e^{-3\pi}
\approx
8.06995\times10^{-5}.
\]

This would be a statement about connected causal support in a finite Alexandrov interval.

It would not be a statement about UPO recovery itself, because isolated vertices carry no orientation choice.

## 2. Exact mean identity

For a continuum point \(x\), let

\[
Q_4(x)
\]

be the normalized volume of the set of events causally comparable to \(x\).

Conditioned on \(x\), the other \(n-1\) points are independent, so

\[
P(
x\text{ is isolated}
\mid x
)
=
(1-Q_4(x))^{n-1}.
\]

Hence

\[
\boxed{
E[I_n]
=
n
E[
(1-Q_4(X))^{n-1}
].
}
\]

In the null-waist coordinates

\[
a=\delta+t,
\qquad
b=\delta-t,
\]

with

\[
a=\frac{2A}{\sqrt n},
\qquad
b=\frac{2B}{\sqrt n},
\]

the exact comparable-volume fraction satisfies

\[
nQ_4
\longrightarrow
A^2+B^2.
\]

The one-point measure satisfies

\[
n\,d\mu_4
\longrightarrow
12\,dA\,dB\,d\sigma,
\]

where \(d\sigma\) is normalized area measure on \(S^2\).

Therefore the limiting isolated-point intensity suggested by the one-point calculation is

\[
\boxed{
12
e^{-(A^2+B^2)}
\,dA\,dB\,d\sigma.
}
\]

Its total mass is

\[
12
\left(
\int_0^\infty e^{-A^2}dA
\right)^2
=
12
\left(
\frac{\sqrt\pi}{2}
\right)^2
=
\boxed{3\pi}.
\]

This recovers the expectation asymptotic.

## 3. Exact factorial-moment identity

For fixed \(k\), write

\[
(I_n)_k
=
I_n(I_n-1)\cdots(I_n-k+1).
\]

Choose \(k\) distinguished sampled points \(x_1,\ldots,x_k\).

They can all be isolated only if they are pairwise incomparable.

Let

\[
S_x
=
\{z:z\sim x\}
\]

be the continuum comparability region of \(x\).

Conditioned on the distinguished points, every remaining point must avoid

\[
\bigcup_{i=1}^{k}S_{x_i}.
\]

Therefore

\[
\boxed{
E[(I_n)_k]
=
(n)_k
E\left[
\mathbf 1_{\{
x_i\not\sim x_j\ \forall i\ne j
\}}
\left(
1-\mu\left(
\bigcup_{i=1}^{k}S_{x_i}
\right)
\right)^{n-k}
\right].
}
\]

This is the natural starting point for a method-of-factorial-moments proof.

## 4. Generic separated-angle limit

Put each distinguished event in waist scaling:

\[
a_i=\frac{2A_i}{\sqrt n},
\qquad
b_i=\frac{2B_i}{\sqrt n},
\qquad
\sigma_i\in S^2.
\]

For fixed pairwise distinct angular directions

\[
\sigma_i\ne\sigma_j,
\]

the selected events become pairwise spacelike for large \(n\).

The expected limiting behavior is

\[
n\,
\mu\left(
\bigcup_{i=1}^{k}S_{x_i}
\right)
\longrightarrow
\sum_{i=1}^{k}
(A_i^2+B_i^2).
\]

If this convergence can be dominated uniformly outside shrinking angular collision neighborhoods, then

\[
E[(I_n)_k]
\longrightarrow
\left[
12
\int_0^\infty
\int_0^\infty
e^{-(A^2+B^2)}
\,dA\,dB
\int_{S^2}d\sigma
\right]^k
=
(3\pi)^k.
\]

Those are exactly the factorial moments of \(\operatorname{Poisson}(3\pi)\).

## 5. The real obstruction: angular collisions

The limiting factorization can fail only when two or more isolated candidates approach the same null generator quickly enough that their small causal-comparability regions overlap at leading order.

Two different scales must be distinguished.

### Direct comparability of the selected events

For two waist-scaled events to become causally comparable, their angular separation must shrink roughly on the coordinate scale

\[
\theta=O(n^{-1/2}).
\]

### Overlap of their endpoint Alexandrov regions

The long thin intervals from the diamond endpoints have a larger transverse width.

A potentially non-negligible overlap can occur on an angular scale of order

\[
\theta=O(n^{-1/4}).
\]

On \(S^2\), a cap of angular radius \(n^{-1/4}\) has area

\[
O(n^{-1/2}).
\]

For fixed \(k\), the union of all pairwise collision caps therefore has vanishing angular measure.

This is the geometric reason Poisson factorization is plausible.

The missing proof must show that the radial integral cannot compensate for this vanishing angular measure.

## 6. Finite factorial-moment evidence

For a Poisson random variable,

\[
\frac{E[(I)_2]}{E[I]^2}
=
\frac{E[(I)_3]}{E[I]^3}
=
\frac{\operatorname{Var}(I)}{E[I]}
=
1.
\]

The reproducible \(3+1\) audit gives:

| \(n\) | trials | mean | Fano | \(E[(I)_2]/E[I]^2\) | \(E[(I)_3]/E[I]^3\) |
|---:|---:|---:|---:|---:|---:|
|128|1500|8.4073|1.5102|1.0606|1.1862|
|256|1000|8.5450|1.4090|1.0477|1.1382|
|512|1000|9.0060|1.3011|1.0333|1.1022|
|1024|500|8.9960|1.1486|1.0163|1.0436|
|2048|500|9.4400|1.1347|1.0140|1.0366|

The analytic limiting mean is

\[
3\pi\approx9.42478.
\]

The moment ratios move toward their Poisson values over the audited range.

The event \(I_n=0\) is too rare for these direct blocks to test efficiently because its conjectured limiting probability is only

\[
e^{-3\pi}\approx8.07\times10^{-5}.
\]

## 7. Relation to the now-completed Poisson-process proof

The Poisson sprinkling version has now been closed in `MINKOWSKI_4D_ISOLATED_POISSON_THEOREM_20261111.md` by combining Penrose's general coupling theorem with a Lorentzian endpoint-overlap bound. The discussion below is retained because it explains why the more convenient homogeneous theorem could not be invoked directly and why a geometry-specific proof was necessary.

## 8. Relation to Penrose's Poisson-approximation theory

Mathew D. Penrose's 2018 paper

> *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*  
> Journal of Applied Probability 55(1), 112–136  
> DOI 10.1017/jpr.2018.9

is directly relevant methodological prior art.

It proves general Poisson-approximation results for isolated vertices and other small components in inhomogeneous random graphs.

However, its convenient Theorem 2.1 does **not** apply directly here.

The reasons are structural:

1. the Minkowski comparability kernel is deterministic,
   \[
   \phi(x,y)\in\{0,1\},
   \]
   so \(\sup\phi=1\);
2. the theorem assumes the connection function is uniformly bounded away from \(1\);
3. the theorem also uses uniform \(\varepsilon\)-homogeneity, whereas here
   \[
   Q_4(x)\to0
   \]
   at the null waist.

This boundary degeneracy is precisely what creates the finite nonzero isolated count.

Penrose's general Poisson-process coupling theorem and factorial-moment method remain relevant, but a geometry-specific verification is required.

## 9. Poisson sprinkling version

Let the physical sprinkling intensity be \(\rho\), and set

\[
\lambda
=
\rho\,\operatorname{vol}(A).
\]

Campbell-Mecke gives

\[
\boxed{
E[I_\rho]
=
\lambda
E[
e^{-\lambda Q_4(X)}
].
}
\]

The same waist scaling yields

\[
\boxed{
E[I_\rho]\to3\pi.
}
\]

A distributional proof may be cleaner in this Poisson ensemble because Palm/Mecke calculus applies directly.

The fixed-\(n\) result can then be treated by depoissonization.

## 10. Consequence for connectedness

If

\[
I_n
\Rightarrow
\operatorname{Poisson}(3\pi),
\]

then

\[
P(I_n=0)
\to
e^{-3\pi}.
\]

Since connectedness requires no isolated vertices,

\[
\limsup_{n\to\infty}
P(G_n\text{ connected})
\le
e^{-3\pi}
\approx8.07\times10^{-5}.
\]

This would explain why connected-UPO can remain extremely rare in \(3+1\) even while almost all vertices belong to the unique nontrivial UPO component.

It does not reduce logical orientation recoverability: isolated events have no directed relation to reconstruct.

## 11. Relationship to adjacent twins

The isolated-vertex and adjacent-twin effects come from the same null-waist geometry but encode opposite structures.

Current candidate laws in \(3+1\) are

\[
E[I_n]\to3\pi
\]

and

\[
E[T_n]
\sim
\frac{9\pi}{n}.
\]

Thus the boundary can retain a finite cloud of completely disconnected events while size-two orientation ambiguities disappear.

## 12. Remaining fixed-cardinality proof target

The theorem-sized target is:

> **4D fixed-cardinality isolated limit.**  
> For a binomial sprinkling of exactly \(n\) iid points in a fixed flat \(3+1\)-dimensional Alexandrov interval,
> \[
> I_n
> \Rightarrow
> \operatorname{Poisson}(3\pi).
> \]

A proof should establish:

1. localization of isolated candidates to \(a,b=O(n^{-1/2})\);
2. convergence of the rescaled one-point intensity;
3. factorization for separated angular directions;
4. an \(o(1)\) bound for the angular-collision region;
5. convergence of every fixed factorial moment, or an equivalent Stein/Palm bound;
6. a direct factorial-moment argument or a justified depoissonization/conditioning step from the now-proved Poisson ensemble.

Until those steps are closed, the result remains a conjecture.

## 13. Current status

The evidence hierarchy is:

\[
\boxed{E[I_n]\to3\pi}
\]

— analytic expectation asymptotic;

\[
\boxed{\text{normalized factorial moments approach }1}
\]

— finite Monte Carlo evidence;

\[
\boxed{I_n\Rightarrow\operatorname{Poisson}(3\pi)}
\]

— proved for the Poisson sprinkling ensemble; still conjectural for fixed cardinality.

No stronger claim is made.
