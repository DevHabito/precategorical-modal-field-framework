# Theorem: tangent-space convergence of the local curved recovery coefficient

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic coefficient-convergence theorem  
**Purpose:** justify the statement that the local curved recovery constant tends to the Minkowski constant as the physical diamond shrinks

## 1. Setting

Let

\[
(M^d,g)
\]

be smooth and time oriented, with fixed

\[
d\ge3.
\]

Fix a strongly causal point

\[
o\in M
\]

and a future unit timelike vector

\[
T\in T_oM.
\]

For small \(L>0\), set

\[
p_L=\exp_o(-LT),
\qquad
q_L=\exp_o(LT),
\]

and

\[
D_L=I(p_L,q_L).
\]

Let

\[
K_{d,g}(D_L)
\]

be the leading orientation-recovery coefficient of the local curved theorem.

## 2. Rescaled metric

Use Riemann normal coordinates centered at \(o\).

Write

\[
x=LX.
\]

Pull back the metric under this dilation and divide by the constant conformal factor \(L^2\).

The resulting dimensionless metric is

\[
\widehat g_L(X).
\]

Constant conformal rescaling does not change causal relations, and the overall volume factor cancels from normalized sprinkling probabilities.

In normal coordinates,

\[
\widehat g_{L,\mu\nu}(X)
=
\eta_{\mu\nu}
-
\frac{L^2}{3}
R_{\mu\alpha\nu\beta}(o)
X^\alpha X^\beta
+
O(L^3)
\]

on every fixed compact coordinate set.

Therefore

\[
\boxed{
\widehat g_L
\to
\eta
}
\]

smoothly on compact sets as

\[
L\to0.
\]

## 3. Rescaled diamonds

The endpoints become

\[
\widehat p_L=-T,
\qquad
\widehat q_L=T.
\]

The null boundaries of the rescaled diamond are the zero sets of the corresponding world functions.

Smooth convergence of the metrics and world functions, together with transversality of the flat null sheets, gives convergence of:

- the two null boundary hypersurfaces;
- their codimension-two edge;
- the induced edge metric;
- the regular double-null coordinate coefficients.

After a family of diffeomorphic identifications converging to the identity,

\[
\boxed{
\widehat D_L
\to
D_{\rm Mink}
}
\]

and

\[
\boxed{
\widehat E_L
\to
E_{\rm Mink}
}
\]

in the regular local sense used by the coefficient formulas.

## 4. d >= 4

For

\[
d\ge4,
\]

the coefficient is an edge integral:

\[
K_{d,g}(D_L)
=
\frac12
\Gamma\left(
3+\frac4d
\right)
C_{d,g}(D_L),
\]

with

\[
C_{d,g}(D_L)
=
2
\int_{\widehat E_L}
\mathcal A_{d,L}(s)
\mathcal S_{d,L}(s)
\,dA_{\widehat E_L}(s).
\]

The ingredients are:

- the double-null metric coefficient \(\Omega_L\);
- the edge metric \(h_L\);
- the thin-null coefficients \(c_{\pm,L}\);
- the fixed scalar integral \(L_m\).

Smooth metric convergence gives convergence of the null geodesic and Jacobi equations on the compact generator families.

Hence the Penrose-limit endpoint coefficients satisfy

\[
c_{\pm,L}
\to
c_{\pm,0}
\]

uniformly along the identified edge.

Likewise,

\[
\Omega_L\to\Omega_0,
\]

and the edge area forms converge.

All coefficients are bounded above and below by positive constants for small \(L\).

Therefore ordinary dominated convergence on the compact edge gives

\[
\boxed{
K_{d,g}(D_L)
\longrightarrow
K_d^{\rm Mink}
\qquad
(d\ge4).
}
\]

## 5. d = 3

For

\[
d=3,
\]

the coefficient is

\[
K_{3,g}(D_L)
=
\frac{
2\pi
}{
V_{\widehat g_L}(\widehat D_L)
}
\int_{\widehat D_L}
\kappa_L(X)^{-3}
\,d\widehat\mu_L(X),
\]

where

\[
\kappa_L
=
\sqrt{
-\widehat g_L^{-1}
(
d\Phi_L,d\Phi_L
)
}.
\]

On compact subsets separated from the null edge,

\[
\Phi_L\to\Phi_0
\]

in \(C^1\), so

\[
\kappa_L^{-3}
\to
\kappa_0^{-3}
\]

uniformly.

The issue is the edge singularity.

## 6. Uniform edge majorant in d = 3

Use regular optical coordinates

\[
(a,b,s)
\]

that vary continuously with \(L\).

The thin-null coefficients stay uniformly bounded above and below for all sufficiently small \(L\).

The joint calculation therefore gives a uniform comparison

\[
\boxed{
\kappa_L^{-3}
\le
C
(ab)^{-3/4}
}
\]

in one fixed edge neighborhood, with \(C\) independent of small \(L\).

The volume densities are uniformly bounded in the same charts.

Since

\[
\int_0^\eta
\int_0^\eta
(ab)^{-3/4}
\,da\,db
<
\infty,
\]

this is an \(L\)-independent integrable dominator.

Thus dominated convergence extends through the edge.

## 7. d = 3 conclusion

We obtain

\[
\boxed{
K_{3,g}(D_L)
\longrightarrow
K_3^{\rm Mink}
=
\frac{32\pi}{3}.
}
\]

## 8. d = 4 check

The all-dimensional edge formula gives

\[
\boxed{
K_{4,g}(D_L)
\longrightarrow
9\pi.
}
\]

This is consistent with the independently audited flat coefficient.

## 9. General conclusion

For every fixed

\[
d\ge3,
\]

\[
\boxed{
\lim_{L\downarrow0}
K_{d,g}(D_L)
=
K_d^{\rm Mink}.
}
\]

Thus the universal flat constants are genuine tangent-space limits of the curved local recovery law.

## 10. About the convergence rate

Riemann normal coordinates give

\[
\widehat g_L-\eta
=
O(L^2)
\]

on fixed compact sets.

This strongly suggests

\[
K_{d,g}(D_L)
=
K_d^{\rm Mink}
+
O(L^2)
\]

under sufficient curvature regularity.

However, the present theorem proves only convergence.

A quantitative \(O(L^2)\) statement requires differentiating the coefficient functionals through:

- the null-geodesic/Jacobi dependence of \(c_\pm\);
- the moving edge;
- in \(d=3\), the integrable edge singularity of \(\kappa^{-3}\).

That rate is left as the next curvature-correction problem rather than asserted without proof.
