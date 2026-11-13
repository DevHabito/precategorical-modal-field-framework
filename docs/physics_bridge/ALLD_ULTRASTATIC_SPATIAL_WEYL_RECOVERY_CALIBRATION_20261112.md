# Theorem candidate: all-dimensional ultrastatic calibration of the pure spatial-Weyl recovery coefficient

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact internal geometric derivation using classical small-ball geometry; externally unverified  
**Scope:** centered sufficiently small regular diamonds in ultrastatic Ricci-flat spacetimes, \(d\ge5\)  
**Purpose:** isolate the \(D^2\) coefficient \(c_d\) in the first vacuum recovery response

## 1. Vacuum response basis

For a centered sufficiently small Ricci-flat diamond in fixed dimension

\[
d\ge5,
\]

the invariant-basis theorem gives

\[
\frac{
K_{d,g}(D_L)
}{
K_d^{\rm Mink}
}
=
1+
L^4
\left[
a_dE^2+b_dH^2+c_dD^2
\right]_o
+
o(L^4).
\]

The present calibration isolates \(c_d\).

## 2. Ultrastatic Ricci-flat geometry

Take

\[
\boxed{
g=-dt^2+h,
}
\]

where

\[
(M^{d-1},h)
\]

is a non-flat Ricci-flat Riemannian manifold.

Relative to

\[
T=\partial_t,
\]

the only nonzero spacetime curvature components are purely spatial.

Therefore

\[
\boxed{
E_{ij}=0,
}
\]

\[
\boxed{
H_{ijk}=0,
}
\]

and

\[
\boxed{
D_{ijkl}
=
R_{ijkl}(h).
}
\]

Hence

\[
\frac{
K_{d,g}
}{
K_d^{\rm Mink}
}
=
1+
c_dD^2L^4
+
o(L^4).
\]

The construction is non-vacuous for every \(d\ge5\).

For \(d=5\), one may use a local region of the four-dimensional Eguchi--Hanson Ricci-flat metric.

For \(d>5\), a product with Euclidean factors preserves Ricci-flatness and supplies the required spatial dimension.

## 3. Exact causal geometry

Let \(r(x)\) be Riemannian distance from a chosen spatial center \(o\), inside its convex normal neighborhood.

Choose the diamond tips

\[
p=(-L,o),
\qquad
q=(+L,o).
\]

Because the metric is ultrastatic, null curves obey

\[
|dt|=ds_h.
\]

Thus the two null sheets are exactly

\[
\alpha
=
t+L-r
=
0,
\]

and

\[
\beta
=
L-t-r
=
0.
\]

Their joint is

\[
\boxed{
\Sigma
=
\{t=0,\ r=L\},
}
\]

the Riemannian geodesic sphere of radius \(L\).

## 4. Exact cross-normalization

Since

\[
d\alpha
=
dt-dr,
\]

and

\[
d\beta
=
-dt-dr,
\]

while

\[
|dr|_h^2=1,
\]

we have

\[
\begin{aligned}
g^{-1}(d\alpha,d\beta)
&=
(-1)(1)(-1)
+
h^{-1}(-dr,-dr)
\\
&=
1+1
\\
&=
\boxed{2}.
\end{aligned}
\]

Therefore the geometric crossing normalization is exactly the flat one.

There is no independent \(D^2\) cross-angle correction.

## 5. Classical Ricci-flat small-ball coefficient

Let

\[
N=d-1
\]

be the Riemannian spatial dimension.

The classical Gray--Vanhecke expansion for a small Riemannian geodesic ball is

\[
\frac{
\operatorname{Vol}_h(B_r)
}{
\omega_Nr^N
}
=
1
-
\frac{
R
}{
6(N+2)
}
r^2
+
\frac{
-3|Riem|^2
+8|Ric|^2
+5R^2
-18\Delta R
}{
360(N+2)(N+4)
}
r^4
+
O(r^6).
\]

For Ricci-flat \(h\),

\[
Ric=0,
\qquad
R=0,
\]

and

\[
|Riem|^2=D^2.
\]

Hence

\[
\boxed{
\frac{
\operatorname{Vol}_h(B_r)
}{
\omega_Nr^N
}
=
1
-
\frac{
D^2
}{
120(N+2)(N+4)
}
r^4
+
O(r^6).
}
\]

This parent-volume input is independent of the Lorentzian ACD formula audited elsewhere in the repository.

## 6. Parent Alexandrov volume

The ultrastatic diamond is foliated by spatial geodesic balls:

\[
D_L\cap\{t=\tau\}
=
B_{L-|\tau|}(o).
\]

Therefore

\[
V_D
=
2
\int_0^L
\operatorname{Vol}_h(B_r)
\,dr.
\]

Using the Ricci-flat small-ball expansion,

\[
\boxed{
\frac{
V_D
}{
V_D^{\rm flat}
}
=
1
-
\frac{
d
}{
120(d+1)(d+3)(d+4)
}
D^2L^4
+
O(L^6).
}
\]

The recovery functional contains the parent factor

\[
V_D^{2/m}
=
V_D^{4/d},
\]

where

\[
m=\frac d2.
\]

Thus the parent contribution to the normalized recovery response is

\[
\boxed{
P_d
=
-\frac1{
30(d+1)(d+3)(d+4)
}.
}
\]

## 7. Edge geodesic-sphere area

Differentiate the geodesic-ball volume:

\[
A_h(S_r)
=
\frac{d}{dr}
\operatorname{Vol}_h(B_r).
\]

For Ricci-flat \(h\),

\[
\boxed{
\frac{
A_h(S_L)
}{
A_h^{\rm flat}(S_L)
}
=
1
-
\frac{
D^2L^4
}{
120N(N+2)
}
+
O(L^6).
}
\]

Since

\[
N=d-1,
\]

the edge-area contribution is

\[
\boxed{
A_d^{\rm edge}
=
-\frac1{
120(d-1)(d+1)
}.
}
\]

## 8. Screen tidal matrix

Fix a radial unit vector

\[
n\in T_oM
\]

and a screen orthogonal to \(n\).

The null optical tidal matrix is

\[
\boxed{
Q_{AB}(n)
=
D_{AnBn}.
}
\]

Because the spatial metric is Ricci flat,

\[
\operatorname{Tr}Q
=
Ric_h(n,n)
=
0.
\]

Thus its first nonzero thin-null effect is quadratic.

The standard spherical fourth-moment identity together with the algebraic Riemann symmetries gives

\[
\boxed{
\left\langle
\operatorname{Tr}(Q^2)
\right\rangle_{S^{N-1}}
=
\frac{
3
}{
2N(N+2)
}
D^2.
}
\]

Equivalently,

\[
\boxed{
\left\langle
\operatorname{Tr}(Q^2)
\right\rangle
=
\frac{
3
}{
2(d-1)(d+1)
}
D^2.
}
\]

## 9. Universal thin-null contribution

The universal vacuum thin-null theorem gives

\[
\frac{
c_Q(L)
}{
c_0(L)
}
=
1+
\lambda_d
L^4
\operatorname{Tr}(Q^2)
+
O(L^6),
\]

where

\[
\boxed{
\lambda_d
=
\frac{
d(7d+22)
}{
2880(d+1)(d+3)
}.
}
\]

On the centered ultrastatic edge, the incoming and outgoing coefficients are equal.

The recovery integrand carries

\[
[c_+c_-]^{-(m+1)/m}
=
c_Q^{-2(m+1)/m}.
\]

Since

\[
\frac{
2(m+1)
}{m}
=
\frac{
2(d+2)
}{d},
\]

the averaged thin-null contribution is

\[
\boxed{
T_d
=
-
\frac{
(d+2)(7d+22)
}{
960(d-1)(d+1)^2(d+3)
}.
}
\]

## 10. No first-order covariance problem

In this ultrastatic Ricci-flat calibration:

- the Ricci scalar vanishes;
- the Ricci tensor vanishes;
- the cross normalization is exactly constant;
- the area and thin-null corrections begin directly at \(D^2L^4\).

There are therefore no local \(O(CL^2)\) anisotropies whose products could produce an additional \(C^2L^4\) covariance term.

The \(D^2\) response is the direct sum of:

1. parent normalization;
2. edge area;
3. thin-null focusing.

## 11. Exact pure-spatial-Weyl coefficient

Thus

\[
c_d
=
P_d
+
A_d^{\rm edge}
+
T_d.
\]

That is,

\[
\begin{aligned}
c_d
={}&
-\frac1{
30(d+1)(d+3)(d+4)
}
\\
&-
\frac1{
120(d-1)(d+1)
}
\\
&-
\frac{
(d+2)(7d+22)
}{
960(d-1)(d+1)^2(d+3)
}.
\end{aligned}
\]

The expression simplifies to

\[
\boxed{
c_d
=
-\frac{
3d^3+32d^2+68d+48
}{
192(d-1)(d+1)^2(d+3)(d+4)
},
\qquad
d\ge5.
}
\]

This is the first individually determined higher-dimensional coefficient in the vacuum recovery basis.

## 12. Concrete dimensions

For \(d=5\),

\[
\boxed{
c_5
=
-\frac{
521
}{
663552
}.
}
\]

For \(d=6\),

\[
\boxed{
c_6
=
-\frac{
47
}{
88200
}.
}
\]

The coefficient is negative for every

\[
d\ge5.
\]

Thus, in the pure-spatial-Weyl ultrastatic sector, local vacuum curvature decreases the normalized leading recovery-error coefficient at order \(L^4\).

This statement concerns the recovery coefficient \(K\), not the recovery probability at fixed finite \(n\) outside its asymptotic regime.

## 13. Reproducibility

The exact symbolic checker is

tools/derive_alld_ultrastatic_spatial_weyl_recovery.py.

It verifies separately:

1. the Ricci-flat small-ball parent term;
2. the \(V_D^{4/d}\) recovery normalization;
3. the geodesic-sphere area term;
4. the spherical screen-tidal contraction;
5. the universal thin-null term;
6. the exact cancellation-free sum for \(c_d\);
7. the \(d=5,6\) rational specializations.

## 14. Literature boundary

The small-geodesic-ball input is classical.

Relevant references include:

- Alfred Gray and Lieven Vanhecke, *Riemannian geometry as determined by the volumes of small geodesic balls*, Acta Mathematica **142** (1979), 157--198.
- Tohru Eguchi and Andrew J. Hanson, *Asymptotically flat self-dual solutions to Euclidean gravity*, Physics Letters B **74** (1978), 249--251, DOI 10.1016/0370-2693(78)90566-X.

The Gray--Vanhecke expansion supplies the Riemannian parent-volume coefficient.

The Eguchi--Hanson geometry supplies a concrete non-flat four-dimensional Ricci-flat Riemannian example for the \(d=5\) ultrastatic calibration.

The project-specific step is the insertion of these classical geometric ingredients into the arrow-erasure recovery functional.

No claim is made that the underlying Riemannian formulas are new.

## 15. Combination with the Cahen--Wallach relation

The independent symmetric-plane-wave calibration gives

\[
\frac{a_d}{4}
+
\frac{b_d}{2}
+
c_d
=
\rho_d,
\]

where

\[
\rho_d
=
\frac{
21d^4+138d^3+196d^2-200d-288
}{
1152(d-1)(d+1)^2(d+3)
}.
\]

Subtracting the present \(c_d\) gives

\[
\boxed{
\frac{a_d}{4}
+
\frac{b_d}{2}
=
\frac{
21d^5
+222d^4
+766d^3
+776d^2
-680d
-864
}{
1152(d-1)(d+1)^2(d+3)(d+4)
}.
}
\]

Therefore only **one additional independent calibration** is now required to determine the complete triple

\[
a_d,\quad b_d,\quad c_d
\]

for every fixed \(d\ge5\).

## 16. Next target

The natural final calibration is a vacuum family with

\[
H=0,
\qquad
E\ne0,
\]

and a known ratio

\[
D^2/E^2.
\]

Two candidates are especially useful:

1. higher-dimensional LRS Kasner, whose null geodesics are already implemented for parent-volume regressions;
2. Schwarzschild--Tangherlini, which is purely electric and static.

Once that calibration fixes \(a_d\), the Cahen--Wallach relation determines \(b_d\) algebraically.

That would close the complete all-dimensional \(L^4\) vacuum recovery response.
