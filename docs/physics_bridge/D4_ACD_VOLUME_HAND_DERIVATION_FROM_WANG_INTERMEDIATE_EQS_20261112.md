# Hand derivation: d = 4 vacuum Alexandrov volume from Wang Eqs. (74) and (76)

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** short exact analytic audit  
**Purpose:** derive the corrected \(3+1\) vacuum ACD four-volume coefficients using only the printed intermediate equations and elementary \(S^2\) moments

## 1. Setup

Set the diamond half-size to

\[
l=1
\]

during the dimensionless integration and restore \(l^4\) at the end.

Write

\[
s=t/l\in[0,1].
\]

For \(d=4\), the flat upper-cone radius is

\[
r_0=1-s.
\]

The total volume is twice the upper-cone integral.

The flat four-volume is

\[
V_0=\frac{2\pi}{3}l^4.
\]

After using a normalized spherical average

\[
\langle f\rangle
=
\frac1{4\pi}\int_{S^2}f\,d\Omega,
\]

the relative quadratic-curvature correction is therefore

\[
\boxed{
\frac{\delta V}{V_0}
=
12
\int_0^1
ds\,
\langle
\delta I(s,n)
\rangle.
}
\]

For an axisymmetric representative let

\[
\mu=n_x.
\]

Only

\[
\boxed{
\langle\mu^2\rangle=\frac13,
\qquad
\langle\mu^4\rangle=\frac15
}
\]

are needed.

## 2. Moving-boundary expansion

The printed Eq. (74) has the form

\[
r^+
=
(1-s)
\left[
1+A+B+O(C^3)
\right],
\]

where \(A\) is linear and \(B\) is quadratic in Weyl curvature.

Since

\[
\int_0^{r^+}r^2dr
=
\frac{(r^+)^3}{3},
\]

the quadratic moving-boundary contribution is

\[
\boxed{
(1-s)^3
\left[
B+A^2
\right].
}
\]

The \(A^2\) term must be retained even though the spherical average of \(A\) itself vanishes.

## 3. Purely electric representative

Choose

\[
E
=
\operatorname{diag}(2,-1,-1),
\qquad
B=0.
\]

Then

\[
E^2=6.
\]

For \(n_x=\mu\),

\[
E_{nn}
=
3\mu^2-1,
\]

and

\[
(E^2)_{nn}
=
1+3\mu^2.
\]

Therefore

\[
\langle E_{nn}^2\rangle
=
\frac45,
\]

\[
\langle(E^2)_{nn}\rangle
=
2.
\]

The linear term in Eq. (74) is

\[
A=\frac{E_{nn}}6.
\]

Using the quadratic terms printed in Eq. (74), the spherical average of the complete moving-boundary density becomes

\[
\boxed{
\langle\delta I_E^{\rm boundary}\rangle
=
\frac{
(1-s)^3
\left(
6s^2-32s+31
\right)
}{
450
}.
}
\]

Hence

\[
12
\int_0^1
\langle\delta I_E^{\rm boundary}\rangle ds
=
\boxed{
\frac16
}.
\]

This value belongs to the representative with \(E^2=6\).

Therefore

\[
\boxed{
v_E^{\rm boundary}
=
\frac1{36}.
}
\]

## 4. Pure-electric RNC determinant

The printed Eq. (76) is

\[
\sqrt{|g|}
=
1
-
\frac1{180}
C^\gamma{}_\mu{}^\alpha{}_\nu
C_{\gamma\rho\alpha\sigma}
x^\mu x^\nu x^\rho x^\sigma
+\cdots.
\]

For the electric representative above, the quartic contraction is

\[
\boxed{
Q_E
=
6
\left[
3\mu^4r^4
-
3\mu^2r^4
-
3\mu^2r^2s^2
+
r^4
+
r^2s^2
+
s^4
\right].
}
\]

Averaging over \(S^2\),

\[
\boxed{
\langle Q_E\rangle
=
\frac{18}{5}r^4
+
6s^4.
}
\]

Thus the determinant contribution to the upper radial integral is

\[
-\frac1{180}
\int_0^{1-s}
r^2
\langle Q_E\rangle dr.
\]

After the remaining \(s\)-integration,

\[
12
\int_0^1ds
\left[
-\frac1{180}
\int_0^{1-s}
r^2
\langle Q_E\rangle dr
\right]
=
\boxed{
-\frac1{210}.
}
\]

Again this is for \(E^2=6\), so

\[
\boxed{
v_E^{\det g}
=
-\frac1{1260}.
}
\]

Therefore

\[
\boxed{
v_E
=
\frac1{36}
-
\frac1{1260}
=
\frac{17}{630}.
}
\]

## 5. Purely magnetic representative

Now choose

\[
E=0,
\qquad
B
=
\operatorname{diag}(2,-1,-1).
\]

Again

\[
B^2=6.
\]

Using

\[
H_{ijk}
=
\epsilon_{jkl}B_i{}^l,
\]

the only quadratic boundary contraction required from Eq. (74) reduces to

\[
\boxed{
H_i{}^m{}_j
H_{lmk}
n^in^jn^ln^k
=
9\mu^2(1-\mu^2).
}
\]

Since

\[
\left\langle
\mu^2(1-\mu^2)
\right\rangle
=
\frac13-\frac15
=
\frac2{15},
\]

the spherical-averaged moving-boundary density is simply

\[
\boxed{
\langle
\delta I_B^{\rm boundary}
\rangle
=
\frac{
(1-s)^5
}{
75
}.
}
\]

Therefore

\[
12
\int_0^1
\frac{(1-s)^5}{75}
ds
=
\boxed{
\frac{2}{75}.
}
\]

Dividing by \(B^2=6\),

\[
\boxed{
v_B^{\rm boundary}
=
\frac1{225}.
}
\]

## 6. Pure-magnetic RNC determinant

For the same magnetic representative, the quartic contraction in Eq. (76) is

\[
\boxed{
Q_B
=
18r^2(\mu^2-1)
\left(
\mu^2r^2-s^2
\right).
}
\]

Using

\[
\langle\mu^2-1\rangle=-\frac23,
\]

and

\[
\langle\mu^4-\mu^2\rangle
=
-\frac2{15},
\]

gives

\[
\boxed{
\langle Q_B\rangle
=
-\frac{12}{5}r^4
+
12r^2s^2.
}
\]

The determinant contribution is therefore

\[
12
\int_0^1ds
\left[
-\frac1{180}
\int_0^{1-s}
r^2
\langle Q_B\rangle dr
\right]
=
\boxed{
\frac1{525}.
}
\]

Dividing by \(B^2=6\),

\[
\boxed{
v_B^{\det g}
=
\frac1{3150}.
}
\]

Hence

\[
\boxed{
v_B
=
\frac1{225}
+
\frac1{3150}
=
\frac1{210}.
}
\]

## 7. Final d = 4 result

Combining the two invariant sectors,

\[
\boxed{
\frac{
V(D_L)
}{
V_{\rm Mink}(L)
}
=
1+
L^4
\left[
\frac{17}{630}E^2
+
\frac1{210}B^2
\right]
+
o(L^4).
}
\]

Equivalently,

\[
\boxed{
\frac{
V(D_L)
}{
V_{\rm Mink}(L)
}
=
1+
L^4
\left[
\frac1{63}(E^2+B^2)
+
\frac1{720}
C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}
\right]
+
o(L^4).
}
\]

## 8. Comparison with the printed Eq. (79)

The \(d=4\) specialization of Eq. (79) instead gives

\[
\frac{127}{4725}E^2
+
\frac1{105}B^2.
\]

The discrepancy is

\[
\boxed{
\Delta v_E=\frac1{9450},
\qquad
\Delta v_B=-\frac1{210}.
}
\]

The derivation above uses the formulas printed immediately before Eq. (79), standard Riemann/Weyl identities in four dimensions, and only the elementary moments

\[
\langle\mu^2\rangle=\frac13,
\qquad
\langle\mu^4\rangle=\frac15.
\]

It is therefore independently checkable without symbolic algebra software.

## 9. Reproducibility

The corresponding exact symbolic checker is

tools/audit_wang2019_d4_acd_volume_eq79.py

and verifies both the total coefficients and the boundary/determinant split.

The independent exact-geometry checks are:

- tools/derive_d4_kasner_world_function_pure_electric_calibration.py
- tools/derive_d4_plane_wave_vacuum_response.py

All three routes agree.
