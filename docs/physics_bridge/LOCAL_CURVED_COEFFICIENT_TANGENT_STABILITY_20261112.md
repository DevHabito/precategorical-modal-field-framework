# Theorem: tangent-space stability of the local curved orientation-recovery coefficient

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic stability theorem  
**Purpose:** make the limit \(K_{d,g}(D_L)\to K_d^{\rm Mink}\) rigorous under small-diamond rescaling

## 1. Setting

Let

\[
(M^d,g)
\]

be a smooth Lorentzian spacetime and let

\[
o\in M
\]

be a strongly causal point.

Choose a future unit timelike vector \(T\in T_oM\) and define, for sufficiently small \(L>0\),

\[
p_L=\exp_o(-LT),
\qquad
q_L=\exp_o(LT),
\]

\[
D_L=I(p_L,q_L).
\]

Use Riemann normal coordinates centered at \(o\) and rescale

\[
x=L\bar x.
\]

After removing the overall metric factor \(L^2\), define the dimensionless rescaled metric

\[
\bar g_L(\bar x)
=
g(L\bar x).
\]

On every fixed compact subset,

\[
\boxed{
\bar g_L
\longrightarrow
\eta
}
\]

in \(C^k\) for every finite \(k\) allowed by the smoothness of \(g\).

The rescaled diamonds converge to the unit Minkowski diamond

\[
D_0
=
I_\eta((-T),(T)).
\]

## 2. Goal

Let

\[
K_{d,g}(D_L)
\]

be the leading orientation-recovery error coefficient of the local curved theorem.

Then

\[
\boxed{
K_{d,g}(D_L)
\longrightarrow
K_d^{\rm Mink}
}
\]

as

\[
L\downarrow0.
\]

## 3. Stability of the causal diamond geometry

For sufficiently small \(L\):

- the rescaled null boundary sheets are smooth;
- their codimension-two edge \(E_L\) is a smooth perturbation of the Minkowski edge \(E_0\);
- the edge can be identified with \(E_0\) by a smooth family of diffeomorphisms;
- double-null metric coefficients converge in \(C^k\);
- null-Fermi/Jacobi data along the edge generators converge uniformly to their flat values.

These statements follow from smooth dependence of geodesics and Jacobi fields on the metric coefficients and initial data.

## 4. d = 3 bulk coefficient

For \(d=3\),

\[
K_{3,g}(D_L)
=
\frac{
2\pi
}{
V(D_L)
}
\int_{D_L}
\kappa_L(x)^{-3}
\,d\mu_L(x),
\]

where

\[
\kappa_L
=
\sqrt{
-g^{-1}(d\Phi_L,d\Phi_L)
}.
\]

After the coordinate and volume normalization to the unit rescaled diamond, write the dimensionless expression as

\[
K_{3,L}
=
2\pi
\int_{\bar D_L}
\bar\kappa_L(\bar x)^{-3}
\,d\bar\mu_L(\bar x).
\]

All scale powers cancel because \(K_{3,L}\) is dimensionless.

## 5. Pointwise convergence in d = 3

The rescaled finite-diamond volume functions converge on compact interior subsets:

\[
\bar\Phi_L
\longrightarrow
\Phi_0
\]

in \(C^1\).

Therefore

\[
\bar\kappa_L
\longrightarrow
\kappa_0
\]

pointwise throughout the interior away from the limiting null edge.

The moving edge has measure zero.

## 6. Uniform integrable domination in d = 3

Choose optical coordinates

\[
(a_L,b_L,s_L)
\]

varying smoothly with \(L\) and identified with the flat edge chart.

The regular thin-null estimates are uniform for all sufficiently small \(L\).

Hence

\[
\boxed{
\bar\kappa_L^{-3}
\le
C
(a_Lb_L)^{-3/4}
}
\]

near the edge, with \(C\) independent of small \(L\).

After identifying the edge charts with the fixed flat coordinates,

\[
(a_Lb_L)^{-3/4}
\le
C'
(ab)^{-3/4}.
\]

Since

\[
(ab)^{-3/4}
\in L^1_{\rm loc},
\]

we have an \(L\)-independent integrable majorant.

Away from the edge, \(\bar\kappa_L\) is uniformly bounded below.

Dominated convergence therefore gives

\[
\boxed{
K_{3,g}(D_L)
\to
K_{3,\eta}.
}
\]

The flat theorem gives

\[
\boxed{
K_{3,\eta}
=
\frac{32\pi}{3}.
}
\]

## 7. d >= 4 edge coefficient

For \(d\ge4\),

\[
K_{d,g}(D_L)
=
\frac12
\Gamma\!\left(
3+\frac4d
\right)
C_{d,g}^{\rm joint}(D_L),
\]

with

\[
C_{d,g}^{\rm joint}
=
2
\int_{E_L}
\mathcal A_{d,L}(s)
\mathcal S_{d,L}(s)
\,dA_{E_L}(s).
\]

The optical-normalization audit proves that the integrand is coordinate invariant.

## 8. Smooth convergence of edge data

Under the smooth metric rescaling,

\[
E_L\to E_0
\]

smoothly.

After identifying the edge manifolds:

\[
dA_{E_L}
\to
dA_{E_0}
\]

uniformly.

The double-null coefficient satisfies

\[
\Omega_L\to\Omega_0.
\]

The Penrose-Fermi thin-null coefficients satisfy

\[
c_{\pm,L}\to c_{\pm,0}
\]

uniformly because:

1. the null-Fermi metrics converge smoothly;
2. the rescaled Alexandrov domains converge;
3. their limiting plane-wave profiles converge to the flat profile as \(L\to0\).

Hence

\[
\mathcal A_{d,L}
\mathcal S_{d,L}
\longrightarrow
\mathcal A_{d,0}
\mathcal S_{d,0}
\]

uniformly on the compact edge.

Therefore

\[
\boxed{
C_{d,g}^{\rm joint}(D_L)
\to
C_d^{\rm Mink}.
}
\]

Consequently,

\[
\boxed{
K_{d,g}(D_L)
\to
K_d^{\rm Mink}.
}
\]

## 9. Explicit checks

### d = 3

\[
\boxed{
K_{3,g}(D_L)
\to
\frac{32\pi}{3}.
}
\]

### d = 4

The normalization audit gives

\[
C_4^{\rm Mink}
=
3\pi,
\]

and hence

\[
\boxed{
K_{4,g}(D_L)
\to
9\pi.
}
\]

### d > 4

The limit is the previously derived flat true-twin constant

\[
\boxed{
K_d^{\rm Mink}
=
K_d^{\rm twin}.
}
\]

## 10. No hidden coordinate dependence

Because the edge coefficient is invariant under

\[
a\mapsto\lambda(s)a,
\qquad
b\mapsto\mu(s)b,
\]

the convergence above does not depend on choosing a special normalization of the optical functions as \(L\) varies.

Thus the tangent-space limit is geometric rather than gauge dependent.

## 11. Consequence

The local curved theorem now has a rigorous tangent-space interpretation:

\[
\boxed{
\text{curved coefficient}
\longrightarrow
\text{Minkowski coefficient}
}
\]

as the physical diamond shrinks.

The exponent is already \(L\)-independent.

Hence the flat laws are the universal tangent limits of the local curved orientation-recovery laws.
