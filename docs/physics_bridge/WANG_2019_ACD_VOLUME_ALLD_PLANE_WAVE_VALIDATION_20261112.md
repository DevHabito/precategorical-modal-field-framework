# All-dimensional exact plane-wave validation of the re-integrated ACD volume

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact analytic cross-check in a covariantly constant Ricci-flat family  
**Scope:** centered Alexandrov intervals in \(d\ge4\) symmetric Brinkmann plane waves  
**Purpose:** test the arbitrary-dimensional ACD volume coefficient without using Wang's RNC integration

## 1. Why this check matters

The direct re-integration of Wang's printed Eqs. (74) and (76) produced

\[
\frac{\delta V}{V_0}
=
L^4
\left[
v_E(d)E^2+
v_H(d)H^2+
v_D(d)D^2
\right]
+O(L^5),
\]

with

\[
v_E(d)
=
\frac{
d(7d^2+44d+58)
}{
180(d+1)(d+3)(d+4)
},
\]

\[
v_H(d)
=
\frac{
d(d+6)
}{
60(d+1)(d+3)(d+4)
},
\]

\[
v_D(d)
=
-\frac{
d
}{
120(d+1)(d+3)(d+4)
}.
\]

Those coefficients differ from the printed Eq. (79).

A check in a single dimension would not establish that the disagreement persists in the full arbitrary-dimensional formula.

A symmetric plane wave supplies an exact Ricci-flat family in every dimension and has covariantly constant curvature.

Its parent causal-diamond volume can be computed directly from the Jacobi propagator.

## 2. Symmetric Ricci-flat plane wave

Consider

\[
ds^2
=
-2\,du\,dv
+
\delta_{ij}dx^idx^j
+
\mathsf A_{ij}x^ix^j\,du^2,
\]

where the transverse dimension is

\[
n=d-2,
\]

and

\[
\mathsf A_{ij}
\]

is a constant symmetric trace-free matrix.

Define

\[
T_2
=
\operatorname{tr}(\mathsf A^2).
\]

The spacetime is Ricci flat because

\[
\operatorname{tr}\mathsf A=0.
\]

The curvature is covariantly constant.

## 3. Jacobi channels

Diagonalize the constant transverse profile.

Writing

\[
\kappa_i=-\mathsf A_i,
\]

the Jacobi channel joining two points separated by null phase \(r\) obeys

\[
B_i''+\kappa_iB_i=0,
\]

with

\[
B_i(0)=0,
\qquad
B_i'(0)=1.
\]

Its small-curvature expansion is

\[
\boxed{
B_i(r)
=
r
-
\frac{\kappa_i}{6}r^3
+
\frac{\kappa_i^2}{120}r^5
+
O(\kappa_i^3r^7).
}
\]

Therefore

\[
\ln B_i(r)
=
\ln r
-
\frac{\kappa_i}{6}r^2
-
\frac{\kappa_i^2}{180}r^4
+
O(\kappa_i^3r^6).
\]

## 4. Exact causal cross-section determinant

Let the two tips have null-phase separation

\[
U.
\]

At an intermediate phase

\[
u,
\qquad
0<u<U,
\]

define

\[
w=U-u.
\]

For each transverse channel the causal-ellipse Hessian is

\[
S_i(u)
=
\frac{
B_i(U)
}{
B_i(u)B_i(w)
}.
\]

Hence

\[
\ln S_i
=
\ln\frac{U}{uw}
-
\frac{\kappa_i}{3}uw
-
\frac{\kappa_i^2}{180}
\left(
U^4-u^4-w^4
\right)
+
O(\kappa_i^3U^6).
\]

Because the profile is trace free,

\[
\sum_i\kappa_i=0.
\]

Therefore the entire term linear in curvature cancels in

\[
\ln\det S.
\]

The first surviving correction is

\[
\boxed{
[\det S]^{-1/2}
=
\left(
\frac{uw}{U}
\right)^{n/2}
\left[
1+
\frac{
T_2
}{
360
}
\left(
U^4-u^4-w^4
\right)
+
O(\mathsf A^3U^6)
\right].
}
\]

## 5. Parent volume ratio

All dimension-dependent constants from integration over the transverse ellipsoid and the conjugate-null direction cancel in the ratio to the flat parent diamond.

Thus

\[
\frac{V_{\rm PW}}{V_0}
=
\frac{
\int_0^Udu\,[\det S(u)]^{-1/2}
}{
\int_0^Udu\,
\left(
\frac{u(U-u)}{U}
\right)^{n/2}
}.
\]

Set

\[
x=\frac{u}{U},
\qquad
a=\frac d2.
\]

The flat weight is proportional to

\[
x^{a-1}(1-x)^{a-1}.
\]

Hence

\[
\boxed{
\frac{V_{\rm PW}}{V_0}
=
1+
\Lambda_d
T_2U^4
+
O(\mathsf A^3U^6),
}
\]

where

\[
\boxed{
\Lambda_d
=
\frac1{360}
\left[
1-
2
\frac{
(d/2)_4
}{
(d)_4
}
\right].
}
\]

Here

\[
(a)_4=a(a+1)(a+2)(a+3)
\]

is the rising factorial.

## 6. Convert to the physical half-size

On the central timelike geodesic,

\[
U=\sqrt2\,L.
\]

Therefore

\[
\frac{\delta V_{\rm PW}}{V_0}
=
4\Lambda_d
T_2L^4
+
O(\mathsf A^3L^6).
\]

The rational coefficient simplifies exactly:

\[
\boxed{
4\Lambda_d
=
\frac{
d(7d+22)
}{
720(d+1)(d+3)
}.
}
\]

Thus the direct exact-geometry result is

\[
\boxed{
\frac{\delta V_{\rm PW}}{V_0}
=
\frac{
d(7d+22)
}{
720(d+1)(d+3)
}
T_2L^4
+
O(\mathsf A^3L^6).
}
\]

## 7. Weyl invariants measured by the central observer

Introduce the orthonormal longitudinal spatial direction associated with the two null coordinates.

The only independent curvature matrix is \(\mathsf A\).

Direct component conversion gives

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

These relations hold in every \(d\ge4\) for this plane-wave family.

## 8. Test the re-integrated coefficients

Insert the re-integrated coefficients into

\[
v_EE^2+v_HH^2+v_DD^2.
\]

For the plane wave,

\[
\begin{aligned}
v_{\rm PW}^{\rm reintegrated}
&=
\frac14v_E
+
\frac12v_H
+
v_D
\\
&=
\boxed{
\frac{
d(7d+22)
}{
720(d+1)(d+3)
}
}.
\end{aligned}
\]

This is exactly

\[
4\Lambda_d.
\]

Therefore

\[
\boxed{
v_{\rm PW}^{\rm exact}
=
v_{\rm PW}^{\rm Eqs.(74)+(76)}
}
\]

for symbolic arbitrary dimension \(d\).

## 9. Test the printed Eq. (79)

The printed Eq. (79) instead gives, on the same plane wave,

\[
v_{\rm PW}^{(79)}
=
\frac{
d
\left(
7d^3+70d^2+236d+240
\right)
}{
720
(d+1)(d+2)(d+3)(d+4)
}.
\]

The exact difference is

\[
\boxed{
v_{\rm PW}^{\rm exact}
-
v_{\rm PW}^{(79)}
=
-
\frac{
d(3d^2+24d+32)
}{
360
(d+1)(d+2)(d+3)(d+4)
}.
}
\]

For every

\[
d\ge4,
\]

this difference is nonzero.

Thus the discrepancy is not peculiar to four dimensions.

## 10. Four-dimensional check

For

\[
d=4,
\]

\[
4\Lambda_4=\frac1{126}.
\]

Since

\[
T_2=2\omega^4,
\]

the correction is

\[
\frac{\delta V}{V_0}
=
\frac1{63}\omega^4L^4,
\]

which reproduces the previously derived exact \(3+1\) plane-wave result.

## 11. Significance

The arbitrary-dimensional re-integration is now supported by two logically different calculations:

1. angular integration of the published RNC intermediate equations;
2. exact Jacobi-determinant geometry of a symmetric Ricci-flat plane wave.

The second calculation:

- does not use Eq. (74);
- does not use Eq. (76);
- does not use Eq. (79);
- does not rely on a Schwarzschild or Kasner specialization;
- has covariantly constant curvature, so curvature-derivative ambiguities are absent.

This is strong internal evidence that the re-integrated all-dimensional coefficient formula is geometrically correct.

## 12. Reproducibility

The symbolic checker is

\`tools/verify_wang_acd_volume_all_d_with_symmetric_plane_wave.py\`.

It verifies

\[
4\Lambda_d
=
\frac14v_E+\frac12v_H+v_D
\]

symbolically and checks concrete dimensions

\[
4\le d\le12.
\]

## 13. Current epistemic boundary

This result strengthens the internal mathematical case but does not by itself create a published correction.

The remaining external tasks are:

- obtain or inspect the supplemental Section C calculation;
- obtain an independent review by another researcher;
- verify whether the author has an unpublished correction or convention not visible in the public article.

Until then, the appropriate claim is an exact internally reproducible inconsistency between the public intermediate equations, the public final equation, and an independent exact family of spacetimes.
