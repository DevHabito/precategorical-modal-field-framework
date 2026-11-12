# Theorem capsule: known pieces of the 3+1 Ricci-flat L^4 recovery response

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact partial decomposition; one geometric term remains unresolved  
**Physical status:** combines independently established Alexandrov-diamond geometry with the project-specific thin-null Jacobi response  
**Literature basis:** ACD edge area and spacetime volume from Jinzhao Wang (2019); thin-null response from the present repository

## 1. Goal

In Ricci-flat \(3+1\) spacetime, the local recovery coefficient has invariant form

\[
K_4(D_L)
=
9\pi
+
L^4
\left[
C_E E^2
+
C_B B^2
\right]
+
o(L^4).
\]

Equivalently,

\[
\frac{
K_4(D_L)
}{
9\pi
}
=
1
+
L^4
\left[
\widehat C_E E^2
+
\widehat C_B B^2
\right]
+
o(L^4),
\]

with

\[
C_E=9\pi\widehat C_E,
\qquad
C_B=9\pi\widehat C_B.
\]

The curved edge formula shows that four geometric ingredients contribute:

1. codimension-two edge area;
2. parent Alexandrov spacetime volume;
3. the two thin-null endpoint coefficients;
4. the double-null cross-normalization factor.

This note closes the first three.

## 2. Four-dimensional Weyl identities

Wang uses

\[
E_{ij}=C_{0i0j},
\]

\[
H_{ijk}=C_{0ijk},
\]

\[
D_{ijkl}=C_{ijkl},
\]

and in four dimensions defines

\[
B_{ij}
=
\frac12
\epsilon_{jkl}
H_i{}^{kl}.
\]

The four-dimensional identities are

\[
\boxed{
D^2=4E^2,
}
\]

and

\[
\boxed{
H^2=2B^2.
}
\]

The Bel-Robinson superenergy density is therefore

\[
W=E^2+B^2.
\]

These identities are explicitly stated in Wang's paper and are not project results.

## 3. Alexandrov edge-area contribution

For the Alexandrov interval causal diamond, Wang gives in vacuum

\[
\delta A
=
\Omega_{d-2}
L^{d+2}
\frac{
(14d^2-32d-4)E^2
+
6(d-4)H^2
-
3D^2
}{
360(d-1)(d+1)
}.
\]

Set

\[
d=4.
\]

Then

\[
14d^2-32d-4
=
92,
\]

the explicit \(H^2\) term vanishes, and

\[
-3D^2
=
-12E^2.
\]

Hence

\[
\delta A
=
\Omega_2
L^6
\frac{
80E^2
}{
5400
}
=
\Omega_2
L^6
\frac{
2E^2
}{
135
}.
\]

The flat edge area is

\[
A_0=\Omega_2L^2.
\]

Therefore

\[
\boxed{
\delta\ln A_E
=
\frac{
2
}{
135
}
E^2L^4.
}
\]

There is no \(B^2\) term in the ACD edge area at this order.

## 4. Parent Alexandrov spacetime volume

Wang's vacuum ACD spacetime-volume formula is

\[
V^{(d)}
=
\frac{
2\Omega_{d-2}L^d
}{
d(d-1)
}
+
\Omega_{d-2}L^{d+4}
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

For

\[
d=4,
\]

the numerator becomes

\[
2068E^2
+
360H^2
-
9D^2.
\]

Using

\[
H^2=2B^2,
\qquad
D^2=4E^2,
\]

this is

\[
2032E^2
+
720B^2.
\]

The denominator is

\[
453600.
\]

The flat volume is

\[
V_0
=
\frac{
\Omega_2L^4
}{
6
}.
\]

Thus

\[
\boxed{
\delta\ln V_D
=
\left[
\frac{
127
}{
4725
}
E^2
+
\frac{
1
}{
105
}
B^2
\right]
L^4.
}
\]

Because the recovery edge coefficient contains

\[
V_D^{-2},
\]

the parent-volume contribution to

\[
\delta\ln K_4
\]

is

\[
\boxed{
-2\delta\ln V_D
=
-
\left[
\frac{
254
}{
4725
}
E^2
+
\frac{
2
}{
105
}
B^2
\right]
L^4.
}
\]

## 5. Angular average of the optical Weyl tidal matrix

Let

\[
k=T+n
\]

be a future null direction and let

\[
\mathcal H_{AB}
=
C_{AkBk}
\]

be the screen-projected optical tidal matrix.

This is the same projected Weyl tensor entering the shear evolution equation in Wang's light-cone calculation.

In vacuum, Wang obtains the light-cone-cut area density correction

\[
-\frac{
\mathcal H_{AB}\mathcal H^{AB}
}{
180
}
L^4.
\]

Comparing its angular integral with his closed area formula gives, in \(d=4\),

\[
\boxed{
\left\langle
\mathcal H_{AB}\mathcal H^{AB}
\right\rangle_{S^2}
=
\frac85
(E^2+B^2).
}
\]

This is consistent with the explicit four-dimensional identities above.

## 6. Thin-null endpoint response

The project plane-wave lemma proves, for one regular null generator,

\[
\boxed{
\delta\ln c_{\rm thin}
=
\frac{
L^4
}{
504
}
\mathcal H_{AB}\mathcal H^{AB}
}
\]

at quadratic Weyl order.

Averaging over the edge directions gives

\[
\left\langle
\delta\ln c_{\rm thin}
\right\rangle
=
\frac{
L^4
}{
504
}
\frac85
(E^2+B^2).
\]

Hence

\[
\boxed{
\left\langle
\delta\ln c_{\rm thin}
\right\rangle
=
\frac{
L^4
}{
315
}
(E^2+B^2).
}
\]

The past and future null sheets contribute equally at this order, so

\[
\boxed{
\left\langle
\delta\ln c_+
+
\delta\ln c_-
\right\rangle
=
\frac{
2L^4
}{
315
}
(E^2+B^2).
}
\]

## 7. Thin-null contribution to the recovery coefficient

For

\[
d=4,
\]

the scalar edge factor contains

\[
c_+^{-3/2}
c_-^{-3/2}.
\]

Therefore

\[
\delta\ln K_4
\big|_{\rm thin}
=
-\frac32
\left\langle
\delta\ln c_+
+
\delta\ln c_-
\right\rangle.
\]

Thus

\[
\boxed{
\delta\ln K_4
\big|_{\rm thin}
=
-
\frac{
1
}{
105
}
(E^2+B^2)
L^4.
}
\]

## 8. Sum of the three known pieces

Add:

### Edge area

\[
+
\frac{
2
}{
135
}
E^2L^4.
\]

### Parent volume

\[
-
\left[
\frac{
254
}{
4725
}
E^2
+
\frac{
2
}{
105
}
B^2
\right]
L^4.
\]

### Thin-null coefficients

\[
-
\frac{
1
}{
105
}
(E^2+B^2)
L^4.
\]

For the electric coefficient,

\[
\frac2{135}
-
\frac{254}{4725}
-
\frac1{105}
=
\boxed{
-\frac{
229
}{
4725
}
}.
\]

For the magnetic coefficient,

\[
-\frac2{105}
-
\frac1{105}
=
\boxed{
-\frac1{35}.
}
\]

Therefore

\[
\boxed{
\delta\ln K_4
\big|_{\rm known}
=
-
\left[
\frac{
229
}{
4725
}
E^2
+
\frac{
1
}{
35
}
B^2
\right]
L^4.
}
\]

## 9. The remaining term

The curved edge formula also contains the double-null cross-normalization factor

\[
\Omega_{\rm null}^{6}.
\]

Thus the full response is

\[
\boxed{
\delta\ln K_4
=
6
\left\langle
\delta\ln\Omega_{\rm null}
\right\rangle
-
\left[
\frac{
229
}{
4725
}
E^2
+
\frac{
1
}{
35
}
B^2
\right]
L^4
+
o(L^4).
}
\]

The quantity

\[
\left\langle
\delta\ln\Omega_{\rm null}
\right\rangle
\]

is the only unresolved geometric contribution to the \(L^4\) vacuum coefficient in this decomposition.

Because optical coordinate changes redistribute terms between

\[
\Omega_{\rm null}
\]

and

\[
c_\pm,
\]

this term should be computed in the same optical gauge used by the thin-null coefficient or, preferably, through a manifestly gauge-invariant combination.

## 10. Bel-Robinson question reduced to one equality

Without the cross-normalization term, the known coefficients are unequal:

\[
-\frac{229}{4725}
\ne
-\frac1{35}.
\]

Thus the currently known pieces are not proportional to

\[
E^2+B^2.
\]

A Bel-Robinson response can emerge only if the remaining cross-normalization contribution supplies precisely the required electric/magnetic difference.

No symmetry currently forces that cancellation.

Therefore the correct status remains:

\[
\boxed{
C_E=C_B
\quad\text{open}.
}
\]

## 11. Literature boundary

The ACD edge-area and total-volume formulas are due to Jinzhao Wang, *Physical Review D* 100, 064020 (2019).

Wang explicitly states in four dimensions:

\[
D^2=4E^2,
\qquad
H^2=2B^2,
\]

and emphasizes that a direct Bel-Robinson proportionality is observable dependent.

The thin-null contribution is a project result derived from the constant-profile plane-wave Jacobi equation.

No Wang coefficient is being reinterpreted as a recovery coefficient without the explicit multiplicative bookkeeping above.

## 12. Regression

The repository script

tools/verify_d4_vacuum_l4_known_terms.py

uses exact rational arithmetic and verifies

\[
-\frac{229}{4725}
\]

and

\[
-\frac1{35}.
\]

## 13. Next target

The vacuum \(L^4\) problem has now been reduced to one local geometric observable:

\[
\boxed{
\left\langle
\delta\ln\Omega_{\rm null}
\right\rangle.
}
\]

The next proof should express this quantity invariantly in terms of the two null sheets, ideally using Synge's world function:

\[
\Omega_{\rm null}^{-2}
\propto
-g^{-1}
(
d\sigma(p,\cdot),
d\sigma(\cdot,q)
)
\]

after the optical normalization is fixed.

That route can be compared directly with the Riemann-normal-coordinate ACD boundary expansion.
