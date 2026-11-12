# Theorem: local orientation-recovery universality in every smooth Lorentzian spacetime of fixed d >= 3

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** analytic local-universality theorem
**Physical status:** tangent-space limit of the curved arrow-erasure recovery law

## 1. Statement

Let

\[
(M,g)
\]

be any smooth time-oriented Lorentzian spacetime of fixed integer dimension

\[
d\ge3.
\]

Fix

\[
o\in M
\]

and a future-directed unit timelike vector

\[
T\in T_oM.
\]

For sufficiently small \(L>0\), define

\[
p_L=\exp_o(-LT),
\qquad
q_L=\exp_o(LT),
\]

and

\[
D_L=I_g(p_L,q_L).
\]

Then there exists \(L_0>0\) such that for every fixed

\[
0<L<L_0,
\]

the arrow-erased causal-comparability graph of an iid size-\(n\) physical-volume sprinkling into \(D_L\) satisfies

\[
\boxed{
p_{d,g,L}^{\mathrm{UPO}}(n)\to1
}
\]

as

\[
n\to\infty.
\]

More sharply,

\[
\boxed{
1-p_{d,g,L}^{\mathrm{UPO}}(n)
\sim
K_{d,L}
n^{-\rho_d},
}
\]

where

\[
\boxed{
\rho_d
=
\begin{cases}
1, & d=3,\\[4pt]
4/d, & d\ge4.
\end{cases}
}
\]

The finite-diamond coefficient \(K_{d,L}\) is the intrinsic curved coefficient from the regular curved theorem.

Finally,

\[
\boxed{
K_{d,L}
\longrightarrow
K_d^{\mathrm{flat}}
}
\]

as

\[
L\downarrow0.
\]

Therefore

\[
\boxed{
\lim_{L\downarrow0}
\lim_{n\to\infty}
n^{\rho_d}
\left(
1-p_{d,g,L}^{\mathrm{UPO}}(n)
\right)
=
K_d^{\mathrm{flat}}.
}
\]

## 2. Scaled normal-coordinate metric

Choose Riemann normal coordinates at \(o\), with \(T\) aligned with the coordinate time axis.

Define

\[
F_L(X)
=
\exp_o(LX).
\]

The rescaled metric is

\[
\boxed{
\widehat g_L
=
L^{-2}
F_L^*g.
}
\]

The positive constant conformal factor does not change causal relations.

In normal coordinates,

\[
\widehat g_{L,\mu\nu}(X)
=
\eta_{\mu\nu}
-
\frac13
R_{\mu\alpha\nu\beta}(o)
L^2
X^\alpha X^\beta
+
O(L^3)
\]

on fixed scaled compact sets.

Smoothness of \(g\) gives

\[
\boxed{
\widehat g_L
\to
\eta
}
\]

in \(C^4\) on every fixed bounded scaled neighborhood.

## 3. Fixed scaled diamond endpoints

The physical endpoints have normal coordinates

\[
\pm LT.
\]

After rescaling they become the fixed endpoints

\[
\widehat p=-T,
\qquad
\widehat q=T.
\]

Let

\[
\widehat D_L
=
I_{\widehat g_L}(\widehat p,\widehat q).
\]

For \(L\) small, \(\widehat D_L\) remains in a common bounded neighborhood of the unit Minkowski diamond.

## 4. Exact equivalence of causal samples

The diffeomorphism \(F_L\) maps

\[
\widehat D_L
\]

onto

\[
D_L.
\]

Since

\[
\widehat g_L
=
L^{-2}F_L^*g,
\]

the causal relations agree under the map.

In dimension \(d\),

\[
d\operatorname{Vol}_{\widehat g_L}
=
L^{-d}
F_L^*
d\operatorname{Vol}_{g}.
\]

The total diamond volumes obey the same factor.

Thus normalized sprinkling measures correspond exactly.

Therefore the random sampled partial orders are distributionally identical:

\[
\boxed{
p_{d,g,L}^{\mathrm{UPO}}(n)
=
p_{d,\widehat g_L}^{\mathrm{UPO}}(n).
}
\]

## 5. Minkowski reference geometry

The limit

\[
\widehat g_L\to\eta
\]

has the fixed reference diamond

\[
D_{\mathrm{flat}}
=
I_\eta(-T,T).
\]

That diamond satisfies the regular all-dimensional recovery hypotheses with strict margins:

- smooth transverse spherical joint;
- no null cut/conjugate points;
- regular volume-null coordinates;
- regular causal cap;
- nondegenerate bulk volume-time gradient;
- nondegenerate tip gradients;
- regular tip middle bands.

## 6. Apply all-dimensional openness

The all-dimensional recovery-openness theorem gives a \(C^4\) neighborhood of the Minkowski reference metric in which the full regular curved error law holds.

Since

\[
\widehat g_L\to\eta
\]

in \(C^4\), there exists \(L_0>0\) such that every

\[
0<L<L_0
\]

lies in that neighborhood.

Thus every sufficiently small physical diamond satisfies the regular curved recovery theorem.

## 7. Local error exponent

For \(d=3\),

\[
\boxed{
1-p_{3,g,L}^{\mathrm{UPO}}(n)
\sim
K_{3,L}n^{-1}.
}
\]

For \(d\ge4\),

\[
\boxed{
1-p_{d,g,L}^{\mathrm{UPO}}(n)
\sim
K_{d,L}n^{-4/d}.
}
\]

The exponent is therefore universal at sufficiently small scale.

## 8. Scale invariance of the curved coefficients

The \(d=3\) coefficient is

\[
K_{3,g}
=
\frac{
2\pi
}{
V_D
}
\int_D
[-g^{-1}(d\Phi,d\Phi)]^{-3/2}
\,d\mu.
\]

The \(d\ge4\) coefficient is

\[
K_{d,g}
=
\frac{
2^{d/2-1}
\omega_{d-2}
}{
V_D^2
}
\left(
\int_\Sigma
\chi^{d/2+1}
\,dA_\Sigma
\right)
\left[
\left(
1+\frac2d
\right)
L_{d/2}
\Gamma\left(
1+\frac2d
\right)
\right]^2.
\]

Both are invariant under:

- diffeomorphisms;
- constant positive metric rescalings.

Therefore

\[
K_{d,L}
=
K(
\widehat D_L,
\widehat g_L
).
\]

## 9. Continuity to the tangent-space coefficient

The curved coefficients depend continuously on the metric inside the regular class.

Since

\[
\widehat g_L\to\eta,
\]

\[
\boxed{
K_{d,L}
\to
K_d^{\mathrm{flat}}.
}
\]

For \(d=3\),

\[
\boxed{
K_3^{\mathrm{flat}}
=
\frac{32\pi}{3}.
}
\]

For \(d\ge4\),

\[
\boxed{
K_d^{\mathrm{flat}}
=
2^{d-2}
\frac{
d^2(d-1)^2
}{
d-2
}
\frac{
S_{d-3}
}{
S_{d-2}
}
\left[
\left(
1+\frac2d
\right)
L_{d/2}
\Gamma\left(
1+\frac2d
\right)
\right]^2.
}
\]

In particular,

\[
\boxed{
K_4^{\mathrm{flat}}
=
9\pi.
}
\]

## 10. Iterated universality limit

For every fixed small \(L\),

\[
\lim_{n\to\infty}
n^{\rho_d}
\left(
1-p_{d,g,L}^{\mathrm{UPO}}(n)
\right)
=
K_{d,L}.
\]

Taking the geometric small-diamond limit afterward gives

\[
\boxed{
\lim_{L\downarrow0}
\lim_{n\to\infty}
n^{\rho_d}
\left(
1-p_{d,g,L}^{\mathrm{UPO}}(n)
\right)
=
K_d^{\mathrm{flat}}.
}
\]

This is the local universality law.

## 11. Dimension-specific geometric mechanism

### d = 3

The finite curved coefficient is controlled by the bulk volume-time gradient.

As \(L\to0\), it converges to

\[
32\pi/3.
\]

### d >= 4

The finite curved coefficient is controlled by the optical geometry of the codimension-two null joint.

As \(L\to0\), the scaled joint converges to the flat spherical joint and the optical functional converges to the flat coefficient.

Thus the tangent-space limit is universal even though the finite-diamond geometric origin differs by dimension.

## 12. Genuinely curved spacetimes

No conformal-flatness hypothesis is used.

For \(d=3\), the Cotton tensor at \(o\) may be nonzero.

For \(d\ge4\), the Weyl tensor at \(o\) may be nonzero.

These curvature tensors appear only in the \(O(L^2)\) and higher corrections to the scaled normal-coordinate metric.

Therefore sufficiently small diamonds in genuinely nonconformally-flat spacetimes still satisfy the recovery law.

## 13. Order of limits

The theorem proves an iterated limit:

\[
n\to\infty
\]

for each fixed small physical diamond, followed by

\[
L\to0.
\]

It does not prove a joint double-scaling law with

\[
n=n(L)\to\infty.
\]

Such a theorem would require recovery estimates uniform in \(L\), including uniform control of the crossover between curvature corrections and the rare-event scale

\[
1/n.
\]

## 14. Scientific consequence

For every smooth Lorentzian spacetime of every fixed dimension

\[
d\ge3,
\]

every point possesses arbitrarily small timelike Alexandrov neighborhoods in which symmetric causal comparability asymptotically determines the sampled directed causal order up to global reversal.

The first-order reconstruction error approaches a dimension-dependent universal tangent-space law.
