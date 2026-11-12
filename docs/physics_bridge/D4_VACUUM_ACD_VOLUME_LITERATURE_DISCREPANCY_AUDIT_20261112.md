> **LATEST AUDIT STATUS — 2026-11-12:** the immediately preceding “missing factor 2” Kasner diagnosis was itself too quick and is superseded. A new direct numerical integration of the physical centered Kasner volume, with the flat normalization built into \(V/V_{\rm flat}\) and the past/future cone crossing solved separately for every direction, extrapolates to
> \[
> \frac{\delta V}{V_{\rm flat}L^4}
> \to
> \frac{68}{8505}.
> \]
> Thus there is currently **no numerical evidence that the physical Kasner coefficient should double**. The symbolic Kasner parent-volume checker is now marked diagnostic and must be reconciled with this independent integral before Kasner is used again as an exact calibration. Until then: keep the Schwarzschild and plane-wave results separate; treat Kasner as unresolved rather than confirmed or refuted.

> **CORRECTION — 2026-11-12:** the Kasner evidence quoted in older sections of this audit is superseded. The Kasner parent-volume code omitted the factor \(2\) needed to normalize its flat directional integral from \(1/2\) to \(1\). Its corrected coefficient is \(17/315\) in the purely electric sector, not \(17/630\). Therefore statements below that use “two exact geometries” or Kasner as support for the pair \(17/630,1/210\) must not be used. What remains valid and independent of Kasner is: (i) the exact symmetric-plane-wave volume check, and (ii) the direct re-integration of Wang's printed intermediate Eqs. (74) and (76), which implies \(17/630,1/210\) in \(d=4\). The pure-electric geometric status is now reopened.

> **Audit update (2026-11-12):** the discrepancy has now been localized further. Direct exact integration of Wang's own published Eqs. (74) and (76) in \(d=4\) gives
> \[
> v_E=\frac{17}{630},\qquad v_B=\frac1{210},
> \]
> not the \(d=4\) specialization of Eq. (79). The null-boundary formula (74) and the RNC volume-density formula (76) independently pass an exact symmetric-plane-wave RNC check. The inconsistency therefore lies in the final integration/algebra leading from the intermediate formulas to Eq. (79), unless an unprinted convention in the supplemental derivation changes those equations. See \`tools/audit_wang2019_d4_acd_volume_eq79.py\`.

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


## 11. Two-geometry candidate corrected coefficient pair

Assume the centered \(3+1\) Ricci-flat ACD four-volume has no independent scalar sector at order \(L^4\) beyond

\[
E^2,
\qquad
B^2.
\]

Write

\[
\frac{V}{V_0}
=
1+
L^4
\left[
v_EE^2+v_BB^2
\right]
+
o(L^4).
\]

The exact Kasner calibration is purely electric and gives

\[
\boxed{
v_E=\frac{17}{630}.
}
\]

The exact type-N plane wave satisfies

\[
E^2=B^2=\frac{\omega^4}{2}
\]

and gives

\[
\frac{\delta V}{V_0}
=
\frac1{63}\omega^4L^4.
\]

Therefore

\[
\frac{v_E+v_B}{2}
=
\frac1{63},
\]

so

\[
v_E+v_B
=
\frac2{63}.
\]

Substituting the Kasner value gives

\[
\boxed{
v_B
=
\frac2{63}
-
\frac{17}{630}
=
\frac1{210}.
}
\]

Thus the two exact geometries force the candidate corrected pair

\[
\boxed{
\frac{V}{V_0}
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

Relative to the \(d=4\) specialization of Wang Eq. (79), the coefficient shifts would be

\[
\boxed{
\Delta v_E
=
\frac1{9450},
}
\]

and

\[
\boxed{
\Delta v_B
=
-\frac1{210}.
}
\]

The magnetic shift is large enough that the generic RNC rederivation is essential before this pair is presented as a correction to the literature.

The status of this pair is therefore:

\[
\boxed{
\text{two-exact-geometry candidate, not yet a general theorem.}
}
\]


## 12. Direct internal-consistency audit of Eqs. (74), (76), and (79)

The two-exact-geometry argument above is no longer the only evidence for the candidate pair.

A direct symbolic audit starts from the formulas printed immediately before Eq. (79).

### Purely electric representative

Choose the algebraic Weyl tensor

\[
E=\operatorname{diag}(2,-1,-1),
\qquad
B=0.
\]

Then

\[
E^2=6.
\]

Insert this tensor into the published \(d=4\) upper-cone boundary Eq. (74), retain the full quadratic contribution from the moving radial boundary, and add the RNC determinant contribution from Eq. (76).

The normalized angular and time integrals give

\[
\frac{\delta V}{V_0}
=
\frac{17}{105}L^4.
\]

Dividing by \(E^2=6\),

\[
\boxed{
v_E=\frac{17}{630}.
}
\]

### Purely magnetic representative

Choose instead

\[
E=0,
\qquad
B=\operatorname{diag}(2,-1,-1),
\]

so

\[
B^2=6.
\]

Using

\[
H_{ijk}=\epsilon_{jkl}B_i{}^l
\]

in Eq. (74), together with the same Eq. (76) determinant term, gives

\[
\frac{\delta V}{V_0}
=
\frac1{35}L^4.
\]

Therefore

\[
\boxed{
v_B=\frac1{210}.
}
\]

### Comparison with Eq. (79)

The printed Eq. (79), specialized to \(d=4\), instead gives

\[
v_E^{(79)}=\frac{127}{4725},
\qquad
v_B^{(79)}=\frac1{105}.
\]

Hence

\[
\boxed{
v_E-v_E^{(79)}
=
\frac1{9450},
}
\]

and

\[
\boxed{
v_B-v_B^{(79)}
=
-\frac1{210}.
}
\]

These are exactly the shifts already inferred independently from Kasner and the symmetric plane wave.

## 13. Plane-wave localization of the failure

The symmetric Cahen--Wallach wave provides a stronger audit of the intermediate equations.

Its exponential map gives exact Riemann normal coordinates around the diamond midpoint.

For the two transverse channels,

\[
F_1(U)
=
\frac{\sin(\omega U)}{\omega U},
\qquad
F_2(U)
=
\frac{\sinh(\omega U)}{\omega U}.
\]

The exact RNC volume density is the exponential-map Jacobian,

\[
\sqrt{|g_{\rm RNC}|}
=
F_1(U)F_2(U).
\]

Expanding,

\[
\boxed{
\sqrt{|g_{\rm RNC}|}
=
1-\frac{\omega^4}{90}U^4+O(\omega^8U^8).
}
\]

Since

\[
U=\frac{t-z}{\sqrt2},
\]

this is

\[
\boxed{
\sqrt{|g_{\rm RNC}|}
=
1-\frac{\omega^4}{360}(t-z)^4+\cdots.
}
\]

That is exactly the specialization of the published Eq. (76).

The exact plane-wave null cone transformed to RNC also reproduces Eq. (74) through the angularly relevant terms. The difference between the exact boundary and the abridged printed boundary is

\[
\Delta r^{(4)}
=
-\frac{
\omega^4l^5
}{
180
}
n_z(n_z^2-1)(s-2)(s-1),
\qquad
s=\frac tl,
\]

which is odd in \(n_z\) and integrates to zero over the sphere.

Therefore the abridgment made in Eq. (74) is legitimate for this volume calculation.

Finally, directly integrating Eq. (74) together with Eq. (76) gives

\[
\boxed{
\left.
\frac{\delta V}{V_0}
\right|_{\rm type\,N}
=
\frac1{63}\omega^4L^4,
}
\]

the same result as the independent exact plane-wave causal-volume calculation.

The \(d=4\) specialization of Eq. (79) instead gives

\[
\frac{86}{4725}\omega^4L^4.
\]

Thus, in this exact geometry, the inconsistency occurs only after the valid intermediate formulas have already been established.

## 14. Revised status of the candidate pair

The pair

\[
\boxed{
v_E=\frac{17}{630},
\qquad
v_B=\frac1{210}
}
\]

is now supported by three logically distinct routes:

1. exact LRS-Kasner causal-volume integration;
2. exact symmetric-plane-wave causal-volume integration;
3. direct integration of Wang's published intermediate RNC formulas (74) and (76).

Accordingly, inside this repository the pair is no longer merely a two-geometry numerical or heuristic candidate.

It is an **internally derived exact \(d=4\) coefficient pair**, subject to external review and to checking the original supplemental derivation for any convention or omitted term not visible in the published equations.

The repository still does not claim an external erratum on behalf of the original author.
