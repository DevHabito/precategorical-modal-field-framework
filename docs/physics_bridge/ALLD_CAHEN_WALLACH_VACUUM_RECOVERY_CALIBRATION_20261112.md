# Theorem candidate: all-dimensional Cahen--Wallach calibration of the vacuum recovery response

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact internal analytic derivation + unexpanded numerical regression in \(d=4,5,6,7\); externally unverified  
**Scope:** sufficiently small centered regular diamonds in symmetric Ricci-flat plane waves, \(d\ge4\), before the first conjugate phase  
**Purpose:** obtain one exact all-dimensional linear relation among the vacuum \(L^4\) recovery coefficients

## 1. Vacuum recovery basis

For a centered sufficiently small Ricci-flat diamond, the invariant-basis theorem gives, for \(d\ge5\),

\[
\frac{K_{d,g}(D_L)}{K_d^{\rm Mink}}
=
1+
L^4
\left[
a_dE^2+b_dH^2+c_dD^2
\right]_o
+
o(L^4).
\]

The three coefficients are generically independent.

A symmetric plane wave cannot determine them separately, but it fixes one exact linear combination in every dimension.

## 2. Symmetric Ricci-flat plane wave

Use Brinkmann form

\[
ds^2
=
-2\,du\,dv
+
\delta_{AB}dx^Adx^B
+
P_{AB}x^Ax^Bdu^2,
\]

where

\[
A,B=1,\ldots,d-2,
\]

and

\[
P=P^\top,
\qquad
\operatorname{Tr}P=0.
\]

Set

\[
T_2=\operatorname{Tr}(P^2).
\]

The profile is constant, so the spacetime is a Cahen--Wallach symmetric plane wave and

\[
\nabla Riemann=0.
\]

Choose a centered timelike diamond on the central geodesic.

If \(U\) is the null-phase separation of its tips and \(L\) the proper-time half-size, then

\[
\boxed{
U=\sqrt2\,L.
}
\]

## 3. Observer invariants

For the central timelike observer, direct component conversion gives

\[
\boxed{
E^2=\frac14T_2,
}
\]

\[
\boxed{
H^2=\frac12T_2,
}
\]

and

\[
\boxed{
D^2=T_2.
}
\]

Therefore the generic vacuum recovery ansatz becomes

\[
\frac{K_{\rm PW}}{K_d^{\rm Mink}}
=
1+
L^4T_2
\left(
\frac{a_d}{4}
+
\frac{b_d}{2}
+
c_d
\right)
+
o(L^4).
\]

The exact plane-wave calculation therefore determines the combination

\[
\frac{a_d}{4}+\frac{b_d}{2}+c_d.
\]

## 4. Jacobi matrix

Let \(B(t)\) be the transverse Jacobi matrix:

\[
B''(t)=PB(t),
\]

\[
B(0)=0,
\qquad
B'(0)=I.
\]

For constant \(P\),

\[
B(t)
=
t
\left[
I+
\frac{t^2}{6}P+
\frac{t^4}{120}P^2+
O(P^3t^6)
\right].
\]

Hence

\[
\log B(t)
=
(\log t)I
+
\frac{t^2}{6}P
-
\frac{t^4}{180}P^2
+
O(P^3t^6).
\]

## 5. Thin-null coefficient

Let

\[
m=\frac d2.
\]

The universal Jacobi-determinant calculation gives

\[
\frac{c_P(r)}{c_0(r)}
=
1+
\lambda_dr^4T_2
+
O(P^3r^6),
\]

where

\[
\boxed{
\lambda_d
=
\frac1{360}
\left[
1-
2\frac{(d/2)_4}{(d)_4}
\right]
=
\frac{
d(7d+22)
}{
2880(d+1)(d+3)
}.
}
\]

This same factor controls the parent plane-wave Alexandrov volume.

## 6. Edge Hessian

At intermediate phase

\[
u=xU,
\qquad
w=(1-x)U,
\]

the edge ellipsoid is controlled by

\[
S(u)
=
B(U)
B(u)^{-1}
B(w)^{-1}.
\]

Set

\[
s_0
=
\frac{U}{uw}.
\]

Using the logarithmic Jacobi expansion,

\[
\frac{S}{s_0}
=
I
+
AP
+
CP^2
+
O(P^3U^6),
\]

where

\[
\boxed{
A=\frac{uw}{3},
}
\]

and

\[
\boxed{
C=
-\frac{
uw(u^2-uw+w^2)
}{
45
}.
}
\]

Equivalently, with

\[
q=x(1-x),
\]

\[
A=\frac{U^2q}{3},
\]

\[
C=
-\frac{
U^4q(1-3q)
}{
45
}.
\]

## 7. Coarea reduction of the intrinsic joint

The intrinsic volume-null functional contains

\[
G^{-(m+1)}dA_\Sigma,
\]

where on the plane-wave edge

\[
G
=
\frac12x^\top S^2x.
\]

Using the codimension-two coarea formula, the edge integral reduces to an ordinary transverse delta-function integral.

After changing variables from the ellipsoid to the unit sphere \(S^{d-3}\), its \(S\)-dependent part is

\[
\boxed{
\frac1{\sqrt{\det S}}
\left\langle
(y^\top Sy)^{-m}
\right\rangle_{S^{d-3}}.
}
\]

This is the all-dimensional generalization of the \(d=4\) factor

\[
\frac{S_1+S_2}{(S_1S_2)^2}.
\]

## 8. Spherical quadratic-form expansion

Let

\[
n=d-2=2m-2.
\]

For a uniform unit vector \(y\in S^{n-1}\),

\[
\left\langle
y^\top Py
\right\rangle
=
0,
\]

\[
\left\langle
y^\top P^2y
\right\rangle
=
\frac{T_2}{n},
\]

and

\[
\left\langle
(y^\top Py)^2
\right\rangle
=
\frac{
2T_2
}{
n(n+2)
}.
\]

Combining the determinant and inverse quadratic-form expansions gives the local joint correction

\[
1+
\frac{
mA^2-(2m-1)C
}{
2(m-1)
}
T_2
+
O(P^3U^6).
\]

## 9. Flat longitudinal weight

The flat edge Hessian contributes

\[
s_0^{-(2m-1)},
\]

while the two thin-null coefficients contribute

\[
[c_0(u)c_0(w)]^{-(m+1)/m}.
\]

Since

\[
c_0(r)\propto r^m,
\]

the remaining longitudinal weight is

\[
[uw]^{m-2}.
\]

Therefore

\[
x
\sim
\operatorname{Beta}(m-1,m-1)
\]

in the normalized plane-wave recovery integral.

Its required moments are

\[
\boxed{
\langle q\rangle
=
\frac{
m-1
}{
2(2m-1)
},
}
\]

\[
\boxed{
\langle q^2\rangle
=
\frac{
m(m-1)
}{
4(2m-1)(2m+1)
},
}
\]

and

\[
\boxed{
\left\langle
x^4+(1-x)^4
\right\rangle
=
\frac{
(m+1)(m+2)
}{
2(2m-1)(2m+1)
}.
}
\]

## 10. Averaged joint contribution

The averaged coarea/joint term is

\[
\boxed{
J_d^{(2)}
=
\frac1{180}
+
\frac{
m(3-m)
}{
360(2m-1)(2m+1)
}.
}
\]

In terms of \(d\),

\[
\boxed{
J_d^{(2)}
=
\frac{
7d^2+6d-8
}{
1440(d^2-1)
}.
}
\]

This is the coefficient of

\[
U^4T_2.
\]

## 11. Volume-null normalization contribution

The intrinsic volume-null gradients produce:

1. the parent factor
   \[
   [c_P(U)/c_0(U)]^{2/m};
   \]
2. two subsegment factors
   \[
   [c_P(u)c_P(w)/(c_0(u)c_0(w))]^{-(m+1)/m}.
   \]

Their combined quadratic contribution is

\[
\boxed{
N_d^{(2)}
=
\lambda_d
\left[
\frac2m
-
\frac{m+1}{m}
\frac{
(m+1)(m+2)
}{
2(2m-1)(2m+1)
}
\right].
}
\]

## 12. Exact plane-wave recovery coefficient

Adding the two pieces gives the coefficient of

\[
U^4T_2:
\]

\[
\boxed{
\kappa_d^{\rm PW}
=
\frac{
21d^4+138d^3+196d^2-200d-288
}{
4608(d-1)(d+1)^2(d+3)
}.
}
\]

Thus

\[
\boxed{
\frac{
K_{\rm PW}
}{
K_d^{\rm Mink}
}
=
1+
\kappa_d^{\rm PW}
U^4T_2
+
O(P^3U^6).
}
\]

Since

\[
U^4=4L^4,
\]

the invariant-basis relation is

\[
\boxed{
\frac{a_d}{4}
+
\frac{b_d}{2}
+
c_d
=
\rho_d,
}
\]

where

\[
\boxed{
\rho_d
=
\frac{
21d^4+138d^3+196d^2-200d-288
}{
1152(d-1)(d+1)^2(d+3)
}.
}
\]

This is one exact all-dimensional linear constraint on the three vacuum recovery coefficients.

## 13. Four-dimensional regression

For

\[
d=4,
\]

\[
\boxed{
\rho_4
=
\frac{127}{4725}.
}
\]

In \(3+1\), the physical plane wave obeys

\[
E^2=B^2=\frac14T_2.
\]

Therefore

\[
\frac{
a_4+b_4
}{4}
=
\rho_4,
\]

so

\[
\boxed{
a_4+b_4
=
\frac{508}{4725}.
}
\]

This exactly reproduces the previously derived \(d=4\) plane-wave calibration.

No coefficient was adjusted to force this regression.

## 14. Unexpanded numerical check

The repository checker

tools/derive_alld_cahen_wallach_recovery_relation.py

also evaluates the unexpanded symmetric-plane-wave recovery functional numerically.

For transverse dimension

\[
n=d-2,
\]

it uses the trace-free two-eigenvalue profile

\[
P
=
\operatorname{diag}
\left(
\epsilon,
-\frac{\epsilon}{n-1},
\ldots,
-\frac{\epsilon}{n-1}
\right).
\]

For \(d>4\),

\[
\operatorname{Tr}(P^3)
\]

need not vanish.

The numerical regression therefore symmetrizes

\[
P\to -P
\]

to remove the cubic contribution and isolate the quadratic coefficient.

The tested dimensions are

\[
d=4,5,6,7.
\]

For decreasing

\[
|\epsilon|,
\]

the measured quadratic coefficient converges toward the exact \(\kappa_d^{\rm PW}\), with the residual decreasing at the expected even-order rate.

This numerical check uses the unexpanded Jacobi functions and the exact spherical/Beta integral representation rather than the symbolic \(P^2\) expansion.

## 15. What this determines

For every fixed

\[
d\ge5,
\]

the three coefficients

\[
a_d,\quad b_d,\quad c_d
\]

remain individually unknown.

The present theorem candidate fixes one exact combination:

\[
\boxed{
\frac{a_d}{4}
+
\frac{b_d}{2}
+
c_d
=
\rho_d.
}
\]

Two additional independent vacuum calibration directions are still required.

## 16. Why this is useful

The relation eliminates one third of the higher-dimensional coefficient problem without choosing a special dimension.

It also provides:

- an exact regression target for future higher-dimensional geometries;
- an independent check on any general RNC expansion of the intrinsic edge functional;
- a clean separation between parent/thin-null normalization and the joint angular response;
- a direct continuation of the already verified \(d=4\) plane-wave result.

## 17. Next calibration targets

A practical minimal program is now:

1. **purely electric higher-dimensional LRS Kasner:** determines a combination of \(a_d\) and \(c_d\) because \(H=0\) and \(D^2/E^2\) is known;
2. **a third algebraically independent vacuum family:** required to separate the remaining \(H^2\) and spatial-Weyl directions.

The corrected all-dimensional parent-volume coefficients are already available, so the remaining difficulty lies in the intrinsic edge functional rather than the parent volume.

No individual \(a_d,b_d,c_d\) is asserted here.
