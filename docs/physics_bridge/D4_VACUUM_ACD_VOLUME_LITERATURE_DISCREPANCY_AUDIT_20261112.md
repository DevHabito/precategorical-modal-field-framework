# Audit note: tension with the published d = 4 vacuum Alexandrov-volume coefficient

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** unresolved literature discrepancy supported by two exact vacuum checks  
**Scope:** total four-volume of sufficiently small \(3+1\)-dimensional Alexandrov intervals in vacuum  
**Purpose:** separate a potential literature issue from the project-specific orientation-recovery calculation

## 1. Published reference formula

Jinzhao Wang, *Geometry of small causal diamonds*, Phys. Rev. D 100, 064020 (2019), gives in Eq. (79)

\[
V^{(d)}
=
\frac{
2\Omega_{d-2}l^d
}{
d(d-1)
}
+
\Omega_{d-2}l^{d+4}
\frac{
(7d^3+58d^2+146d+108)E^2
+
6(d+2)(d+6)H^2
-
\frac32(d+2)D^2
}{
90(d-1)(d+1)(d+2)(d+3)(d+4)
}
+\cdots.
\]

The same paper places the two ACD tips at Riemann-normal coordinates

\[
(\pm l,0,\ldots,0),
\]

so \(l\) is the geodesic half proper-time separation of the tips.

In four dimensions,

\[
D^2=4E^2,
\qquad
H^2=2B^2.
\]

Dividing Eq. (79) by the flat four-volume

\[
V_0=\frac{2\pi}{3}l^4
\]

therefore gives

\[
\boxed{
\left.
\frac{\delta V}{V_0}
\right|_{\rm Wang}
=
l^4
\left[
\frac{127}{4725}E^2
+
\frac1{105}B^2
\right].
}
\]

This note tests that specialization against two exact Ricci-flat geometries.

## 2. Exact check A: LRS Kasner

Use

\[
ds^2
=
-dt^2
+
t^{-2/3}dx^2
+
t^{4/3}(dy^2+dz^2),
\]

with centered tips

\[
t=1\pm L.
\]

The central line is geodesic, so \(L\) is exactly the half proper-time separation.

At the midpoint,

\[
B^2=0,
\qquad
E^2=\frac8{27}.
\]

Direct integration of the exact null-cone equations, expanded with exact rational algebra, gives

\[
\boxed{
\frac{V_{\rm Kasner}}{V_0}
=
1+
\frac{68}{8505}L^4
+
O(L^6).
}
\]

Equivalently,

\[
\boxed{
\left.
\frac{\delta V}{V_0}
\right|_{\rm Kasner}
=
\frac{17}{630}E^2L^4.
}
\]

The Wang specialization would give

\[
\frac{127}{4725}E^2L^4.
\]

The difference is

\[
\boxed{
\frac{17}{630}
-
\frac{127}{4725}
=
\frac1{9450}.
}
\]

Thus the two predictions differ by

\[
\frac1{9450}E^2L^4.
\]

The direct Kasner calculation is reproduced by

tools/derive_d4_kasner_world_function_pure_electric_calibration.py

and was also checked against a separate numerical integration of the unexpanded Kasner null cones.

## 3. Kasner edge-area control

The same exact Kasner calculation gives

\[
\boxed{
\frac{\delta A}{A_0}
=
\frac2{135}E^2L^4.
}
\]

This agrees with Wang's \(d=4\) purely electric ACD edge-area formula.

Therefore the discrepancy is not a blanket mismatch in:

- the definition of the centered diamond;
- the half-size \(L\);
- the electric Weyl normalization;
- or the Kasner curvature convention.

It is localized to the total four-volume comparison.

## 4. Exact check B: symmetric vacuum plane wave

Consider the symmetric Ricci-flat plane wave

\[
ds^2
=
-2\,du\,dv
+
dx_1^2+dx_2^2
+
H_{ij}x^ix^j\,du^2,
\]

with

\[
H
=
\operatorname{diag}
(-\omega^2,+\omega^2).
\]

For centered tips on the central timelike geodesic,

\[
U=\sqrt2L,
\qquad
z=\omega U.
\]

The exact causal cross-section calculation gives

\[
V
=
\pi U^2\delta^2F(z),
\]

where

\[
F(z)
=
\frac16
\left[
1+\frac{z^4}{252}+O(z^8)
\right].
\]

For the centered diamond, \(\delta=U\), so

\[
\boxed{
\frac{V_{\rm PW}}{V_0}
=
1+
\frac{z^4}{252}
+
O(z^8).
}
\]

The central observer measures

\[
E^2=B^2=\frac{\omega^4}{2},
\]

and

\[
z^4=4\omega^4L^4.
\]

Hence

\[
\boxed{
\left.
\frac{\delta V}{V_0}
\right|_{\rm PW}
=
\frac1{63}
(E^2+B^2)L^4
}
\]

when restricted to the type-N relation \(E^2=B^2\).

Equivalently, the coefficient multiplying \(\omega^4L^4\) is

\[
\boxed{
\frac1{63}
=
\frac{75}{4725}.
}
\]

## 5. Published formula on the same type-N field

The \(d=4\) Wang formula predicts

\[
L^4
\left[
\frac{127}{4725}E^2
+
\frac1{105}B^2
\right].
\]

For

\[
E^2=B^2=\frac{\omega^4}{2},
\]

this becomes

\[
\boxed{
\frac{86}{4725}\omega^4L^4.
}
\]

The exact plane-wave volume gives

\[
\boxed{
\frac{75}{4725}\omega^4L^4.
}
\]

The difference is

\[
\boxed{
-\frac{11}{4725}\omega^4L^4.
}
\]

This is a second independent disagreement.

## 6. Why the plane-wave check is especially restrictive

The constant-profile plane wave is a Cahen--Wallach symmetric spacetime.

Its curvature is covariantly constant:

\[
\nabla Riemann=0.
\]

Therefore the mismatch cannot be explained by neglected first or second derivatives of curvature in a generic time-dependent vacuum.

The exact volume formula is obtained directly from the two Jacobi channels:

\[
B_1(r)=\frac{\sin(\omega r)}{\omega},
\qquad
B_2(r)=\frac{\sinh(\omega r)}{\omega},
\]

and the resulting causal ellipse at every intermediate null phase.

The repository checker

tools/derive_d4_plane_wave_vacuum_response.py

already verifies symbolically that

\[
F(z)
=
\frac16
\left[
1+\frac{z^4}{252}
\right]
+
O(z^8).
\]

## 7. A possible point of failure in the published derivation

Wang's derivation first obtains the angle-dependent lightcone boundary and then argues that, after averaging, the upper and lower cone contributions can be replaced by equal contributions before writing the final total-volume integral.

The paper also states that an abridged version of the lightcone-boundary expansion is used, omitting terms judged irrelevant after angular integration.

The two exact counterchecks show that this simplification deserves re-examination.

This observation is not yet a proof that a specific algebraic step in the paper is wrong.

The exact missing term has not been traced to one published line.

## 8. Current scientific status

The repository now has:

1. an exact direct Kasner calculation;
2. a separate numerical Kasner regression;
3. an exact symmetric-plane-wave calculation;
4. agreement with Wang's ACD edge area in the Kasner test;
5. disagreement with Wang Eq. (79) for the total ACD volume in both vacuum geometries.

This is strong internal evidence that the \(d=4\) specialization of Eq. (79) should be independently rechecked.

It is still premature to call the published formula erroneous without:

- an independent RNC rederivation of the four-volume;
- an external calculation by another researcher;
- or a response/erratum from the original author.

## 9. Impact on the recovery project

The orientation-recovery coefficient does not depend on accepting Wang Eq. (79).

The independent Kasner calculation directly supplies its own parent-volume term and reproduces

\[
a_4=\frac{683}{9450}
\]

without using the disputed volume formula.

Therefore the literature tension does not invalidate the current recovery coefficient.

Instead, it identifies a separate small-causal-diamond geometry question that may itself be scientifically useful.

## 10. Next audit target

The clean next step is to derive the generic \(d=4\) vacuum Alexandrov four-volume directly from the RNC world-function expansion while retaining all local angular terms until the final integration.

The target is to determine whether the correct universal coefficients are:

\[
\frac{127}{4725},\quad \frac1{105},
\]

or a different pair consistent with both exact Kasner and plane-wave tests.

Two exact geometries already provide two linear constraints, so in \(3+1\) they are sufficient to infer a candidate corrected pair before the full tensor derivation.
