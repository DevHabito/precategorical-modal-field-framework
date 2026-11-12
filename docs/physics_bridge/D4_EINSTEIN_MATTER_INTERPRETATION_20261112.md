# Physics bridge: the d = 4 curvature response under Einstein's equation

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** interpretation corollary of the candidate curvature-response theorem  
**Scope:** small regular centered \(3+1\)-dimensional diamonds  
**Novelty status:** Einstein's equation and the stress-energy decomposition are standard; the project-specific object is the orientation-recovery coefficient \(K_4\)

## 1. Geometric result

For a sufficiently small regular centered \(3+1\) causal diamond,

\[
1-p_{4,g,L}^{\rm UPO}(n)
\sim
\frac{
K_{4,g}(D_L)
}{
n
}.
\]

The candidate first curvature response derived in the repository is

\[
\boxed{
K_{4,g}(D_L)
=
9\pi
\left[
1+
L^2
\left(
-\frac19R
+
\frac13R_{TT}
\right)_o
+
o(L^2)
\right].
}
\]

Here

\[
R_{TT}
=
R_{\mu\nu}T^\mu T^\nu
\]

for the unit timelike vector \(T\) defining the central diamond axis.

This note does not modify that geometric theorem.

It only rewrites its curvature combination using Einstein's equation.

## 2. Einstein equation

Assume

\[
\boxed{
G_{\mu\nu}
+
\Lambda g_{\mu\nu}
=
8\pi G
T_{\mu\nu}.
}
\]

Use signature

\[
(-,+,+,+).
\]

Define the observer energy density

\[
\boxed{
\rho_T
=
T_{\mu\nu}T^\mu T^\nu.
}
\]

Let the stress-energy trace be

\[
\mathcal T
=
T^\mu{}_\mu.
\]

## 3. Trace equation

Taking the four-dimensional trace gives

\[
-R+4\Lambda
=
8\pi G\mathcal T.
\]

Hence

\[
\boxed{
R
=
4\Lambda
-
8\pi G\mathcal T.
}
\]

## 4. Timelike contraction

Contract Einstein's equation with

\[
T^\mu T^\nu.
\]

Because

\[
g_{\mu\nu}T^\mu T^\nu=-1,
\]

\[
R_{TT}
+
\frac12R
-
\Lambda
=
8\pi G\rho_T.
\]

Therefore

\[
\boxed{
R_{TT}
=
8\pi G\rho_T
-
\Lambda
+
4\pi G\mathcal T.
}
\]

## 5. Recovery-response matter combination

Substitute into

\[
-\frac19R+\frac13R_{TT}.
\]

One obtains

\[
\boxed{
-\frac19R
+
\frac13R_{TT}
=
\frac{
8\pi G
}{3}
\rho_T
+
\frac{
20\pi G
}{9}
\mathcal T
-
\frac79\Lambda.
}
\]

Thus

\[
\boxed{
\frac{
K_{4,g}(D_L)
}{
9\pi
}
=
1
+
L^2
\left[
\frac{
8\pi G
}{3}
\rho_T
+
\frac{
20\pi G
}{9}
\mathcal T
-
\frac79\Lambda
\right]_o
+
o(L^2).
}
\]

## 6. Perfect fluid

For a perfect fluid,

\[
T_{\mu\nu}
=
(\rho+p)U_\mu U_\nu
+
pg_{\mu\nu}.
\]

If the diamond axis is aligned with the fluid four-velocity,

\[
T=U,
\]

then

\[
\rho_T=\rho,
\]

and

\[
\mathcal T
=
-\rho+3p.
\]

Therefore

\[
\boxed{
-\frac19R
+
\frac13R_{TT}
=
\frac{
4\pi G
}{9}
(\rho+15p)
-
\frac79\Lambda.
}
\]

The recovery coefficient becomes

\[
\boxed{
K_{4,g}(D_L)
=
9\pi
\left[
1
+
L^2
\left(
\frac{
4\pi G
}{9}
(\rho+15p)
-
\frac79\Lambda
\right)_o
+
o(L^2)
\right].
}
\]

Equivalently,

\[
\boxed{
K_{4,g}(D_L)
=
9\pi
+
L^2
\left[
4\pi^2G(\rho+15p)
-
7\pi\Lambda
\right]_o
+
o(L^2).
}
\]

## 7. Special cases

### Pure cosmological constant

If

\[
T_{\mu\nu}=0
\]

and

\[
\Lambda=3H^2,
\]

then

\[
\boxed{
\frac{
K_{4,g}
}{
9\pi
}
=
1
-
\frac73H^2L^2
+
o(L^2).
}
\]

This agrees with the independent exact de Sitter conformal-density regression.

### Pressureless dust with Lambda = 0

For

\[
p=0,
\]

\[
\boxed{
\frac{
K_{4,g}
}{
9\pi
}
=
1
+
\frac{
4\pi G
}{9}
\rho L^2
+
o(L^2).
}
\]

Within the candidate theorem, positive dust density increases the leading finite-\(n\) reconstruction-error coefficient relative to the tangent Minkowski value.

### Radiation with Lambda = 0

For

\[
p=\frac{\rho}{3},
\]

\[
\rho+15p=6\rho.
\]

Hence

\[
\boxed{
\frac{
K_{4,g}
}{
9\pi
}
=
1
+
\frac{
8\pi G
}{3}
\rho L^2
+
o(L^2).
}
\]

## 8. What this does not mean

The formula does **not** derive Einstein's equation.

Einstein's equation is an additional physical assumption used to reinterpret the geometric curvature response.

The result also does not say:

- matter creates time;
- pressure is a universal cause of causal orientation;
- \(K_4\) is a new stress-energy observable already measured in nature.

The precise statement is narrower:

> if general relativity holds and the candidate recovery-response theorem survives external review, the first small-diamond correction to the arrow-erasure recovery coefficient is sensitive to the displayed local combination of stress-energy variables.

## 9. Why pressure appears strongly

The coefficient multiplying pressure in the comoving perfect-fluid expression is larger than the coefficient multiplying energy density:

\[
\rho+15p.
\]

This is not inserted by hand.

It follows algebraically from the distinct coefficients of

\[
R
\quad\text{and}\quad
R_{TT}
\]

in the recovery response.

Whether this weighting has a deeper operational or information-geometric meaning is currently open.

No such interpretation is asserted.

## 10. Research use

This corollary gives a concrete bridge for future tests:

1. choose exact or numerical GR solutions;
2. compute the local matter variables and curvature;
3. simulate finite sprinklings in sufficiently small diamonds;
4. compare the measured true-twin/UPO error coefficient with the predicted \(K_4(D_L)\);
5. test when higher-order tidal or caustic effects become visible.

This is a route from the abstract reconstruction theorem to falsifiable finite-geometry calculations.
