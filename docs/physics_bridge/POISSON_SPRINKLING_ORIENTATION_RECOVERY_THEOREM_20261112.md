# Theorem: Poisson-sprinkling orientation-recovery law and discreteness-length scaling

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** probabilistic transfer theorem  
**Physical status:** translates the fixed-cardinality recovery law into the standard Poisson sprinkling ensemble of causal-set theory  
**Novelty status:** Poisson conditioning is classical; the project-specific content is the resulting recovery-error law

## 1. Motivation

The previous recovery theorems condition on a fixed number of sprinkled points

\[
n.
\]

Standard causal-set sprinkling instead uses a Poisson point process of density

\[
\rho.
\]

For a finite causal diamond \(D\) of physical volume

\[
V_D,
\]

the random cardinality is

\[
\boxed{
N\sim
\operatorname{Poisson}(\lambda),
\qquad
\lambda=\rho V_D.
}
\]

Conditioned on

\[
N=n,
\]

the Poisson points are iid uniform with respect to normalized physical volume.

Therefore the fixed-\(n\) theorem transfers by conditioning.

## 2. General transfer lemma

Suppose

\[
f(n)
=
1-p^{\rm UPO}(n)
\]

satisfies

\[
\boxed{
f(n)
\sim
K n^{-\alpha}
}
\]

for some

\[
K>0,
\qquad
\alpha>0.
\]

Define the Poisson-ensemble failure probability

\[
F_{\rm Pois}(\lambda)
=
\mathbb E[
f(N)
].
\]

Then

\[
\boxed{
F_{\rm Pois}(\lambda)
\sim
K\lambda^{-\alpha}.
}
\]

## 3. Proof

Fix

\[
\delta\in(0,1).
\]

On the concentration event

\[
A_\delta
=
\{
|N-\lambda|
\le
\delta\lambda
\},
\]

we have

\[
N
=
\lambda[1+O(\delta)].
\]

For sufficiently large \(\lambda\), every \(N\) on \(A_\delta\) lies in the asymptotic regime and

\[
f(N)
=
K
N^{-\alpha}
[1+o_\lambda(1)].
\]

Hence uniformly on \(A_\delta\),

\[
f(N)
=
K
\lambda^{-\alpha}
[1+O(\delta)+o_\lambda(1)].
\]

Poisson concentration gives

\[
\Pr(A_\delta^c)
\le
2e^{-c_\delta\lambda}.
\]

Since

\[
0\le f(N)\le1,
\]

the tail contributes at most

\[
2e^{-c_\delta\lambda}
=
o(\lambda^{-\alpha}).
\]

Therefore

\[
F_{\rm Pois}(\lambda)
=
K\lambda^{-\alpha}
[1+O(\delta)+o_\lambda(1)].
\]

Letting

\[
\lambda\to\infty
\]

and then

\[
\delta\downarrow0
\]

proves

\[
\boxed{
F_{\rm Pois}(\lambda)
\sim
K\lambda^{-\alpha}.
}
\]

The exponentially small cases \(N=0,1,\ldots\) do not affect the asymptotic.

## 4. Regular curved d = 3

For a regular curved \(2+1\) diamond,

\[
1-p_{3,g}^{\rm UPO}(n)
\sim
K_{3,g}(D)n^{-1}.
\]

Thus the Poisson sprinkling obeys

\[
\boxed{
\Pr_{\rho,D}(
\text{orientation recovery fails}
)
\sim
\frac{
K_{3,g}(D)
}{
\rho V_D
}.
}
\]

For the flat unit diamond,

\[
K_{3,\eta}
=
\frac{32\pi}{3}.
\]

## 5. Regular curved d >= 4

For every fixed

\[
d\ge4,
\]

\[
1-p_{d,g}^{\rm UPO}(n)
\sim
K_{d,g}(D)
n^{-4/d}.
\]

Therefore

\[
\boxed{
\Pr_{\rho,D}(
\text{orientation recovery fails}
)
\sim
K_{d,g}(D)
(
\rho V_D
)^{-4/d}.
}
\]

This includes the flat result as a special case.

## 6. Discreteness length

Define the Poisson discreteness length

\[
\boxed{
\ell_\rho
=
\rho^{-1/d}.
}
\]

Then

\[
\rho^{-4/d}
=
\ell_\rho^4.
\]

Hence for

\[
d\ge4,
\]

\[
\boxed{
\Pr_{\rho,D}(
\text{failure}
)
\sim
K_{d,g}(D)
V_D^{-4/d}
\ell_\rho^4.
}
\]

This is a dimension-independent quartic power of the discreteness length.

The dimension dependence remains in:

- the dimensionless coefficient \(K_{d,g}(D)\);
- the volume factor \(V_D^{-4/d}\).

## 7. Single geometric length scale

Suppose a family of geometrically similar causal diamonds has characteristic proper scale \(L\), so

\[
V_D
=
v_{d,g}(D)L^d,
\]

where \(v_{d,g}(D)\) is dimensionless.

Then for

\[
d\ge4,
\]

\[
(\rho V_D)^{-4/d}
=
v_{d,g}(D)^{-4/d}
\left(
\frac{
\ell_\rho
}{
L
}
\right)^4.
\]

Thus

\[
\boxed{
\Pr_{\rm fail}
\sim
\widetilde K_{d,g}(D)
\left(
\frac{
\ell_\rho
}{
L
}
\right)^4,
\qquad
d\ge4,
}
\]

with

\[
\widetilde K_{d,g}
=
K_{d,g}
v_{d,g}^{-4/d}.
\]

The quartic exponent is universal across all fixed dimensions at least four under the regularity assumptions.

## 8. d = 3 contrast

In

\[
d=3,
\]

\[
\rho^{-1}
=
\ell_\rho^3.
\]

Therefore

\[
\boxed{
\Pr_{\rm fail}
\sim
\widetilde K_{3,g}(D)
\left(
\frac{
\ell_\rho
}{
L
}
\right)^3.
}
\]

Thus the dimensional transition has a direct discreteness-scale form:

\[
\boxed{
\begin{array}{c|c}
d=3
&
(\ell/L)^3
\\[4pt]
d\ge4
&
(\ell/L)^4
\end{array}
}
\]

for the leading orientation-recovery error.

## 9. Flat 3+1 example

For the unit flat \(3+1\) diamond,

\[
K_{4,\eta}
=
9\pi.
\]

Therefore

\[
\boxed{
\Pr_{\rho,D}(
\text{failure}
)
\sim
9\pi
(
\rho V_D
)^{-1}.
}
\]

If the parent diamond has proper-time scale \(L\), this is a constant multiple of

\[
\left(
\frac{
\ell_\rho
}{
L
}
\right)^4.
\]

## 10. Physical interpretation

The result should be interpreted narrowly.

It does not say that physical spacetime discreteness is known to have density \(\rho\).

It says:

> if the declared causal-set sprinkling model is Poisson with density \(\rho\), then the loss of causal arrows produces a reconstruction error controlled by a universal power of the discreteness-to-diamond scale.

For \(d\ge4\), the fourth power comes from the codimension-two null-edge true-twin mechanism.

## 11. Importance for comparison with causal-set literature

Most causal-set work phrases the continuum approximation in terms of sprinkling density rather than conditioning on a fixed cardinality.

The theorem places the orientation-recovery result in that standard language:

\[
\boxed{
\text{fixed }n
\quad\leftrightarrow\quad
\text{Poisson mean }\rho V_D.
}
\]

No new assumption beyond ordinary Poisson sprinkling is introduced.
