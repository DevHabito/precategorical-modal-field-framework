> **Additional supersession — parent volume:** this historical decomposition also used the \(d=4\) parent-volume coefficients obtained by specializing Wang (2019) Eq. (79),
> \[
> \frac{127}{4725}E^2+\frac1{105}B^2.
> \]
> A direct re-integration of Wang's printed Eqs. (74)+(76), independently checked by exact Cahen--Wallach geometry, Lean-certified rational reductions, and the exact Kasner pure-electric parent checker, instead supports
> \[
> \boxed{
> \frac{\delta V}{V_0}
> =
> L^4\left[
> \frac{17}{630}E^2+\frac1{210}B^2
> \right]+o(L^4).
> }
> \]
> Therefore the numerical sums later in this file are retained only as an audit trail and must not be used as current coefficients.

> **Supersession warning (2026-11-12):** the factorized \(L^4\) bookkeeping below is incomplete. A later RNC/world-function audit found nonzero first-order local anisotropies
> \[
> q_1=-\frac13L^2E_{nn},
> \qquad
> a_1=\frac16L^2E_{nn},
> \]
> whose separate spherical averages vanish but whose products contribute at order \(C^2L^4\). In particular,
> \[
> \left\langle \frac92q_1^2-3a_1q_1\right\rangle
> =
> \frac{4}{45}E^2L^4.
> \]
> Therefore the edge integral cannot be replaced at this order by total area times separately averaged logarithmic factors. Keep the individual geometric inputs below only as provisional components; do not use Sections 9--14 as a complete coefficient derivation. See \`D4_RNC_WORLD_FUNCTION_EDGE_ANISOTROPY_20261112.md\`.

# Theorem capsule: invariant decomposition of the 3+1 Ricci-flat L^4 recovery response

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** corrected exact partial decomposition; one world-function cross term remains unresolved  
**Physical status:** combines Alexandrov-diamond geometry, thin-null focusing, and the invariant intersection angle of the two null sheets  
**Correction note:** this version supersedes the earlier bookkeeping that treated the parent-volume factor as \(V_D^{-2}\) after the normalized thin coefficients had already absorbed \(V_D^{-1}\)

## 1. Goal

In Ricci-flat \(3+1\) spacetime,

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

The curved edge theorem is most safely rewritten using **physical** thin-null coefficients rather than normalized ones.

## 2. Normalized versus physical thin coefficients

Write the physical thin-null laws

\[
V(p,x)
=
c_+^{\rm phys} a^2[1+o(1)],
\]

\[
V(x,q)
=
c_-^{\rm phys} b^2[1+o(1)].
\]

The normalized coefficients used in the curved edge theorem are

\[
c_\pm
=
\frac{
c_\pm^{\rm phys}
}{
V_D
}.
\]

For \(d=4\), the scalar edge factor contains

\[
c_+^{-3/2}c_-^{-3/2}.
\]

Hence

\[
c_+^{-3/2}c_-^{-3/2}
=
V_D^3
\left(
c_+^{\rm phys}c_-^{\rm phys}
\right)^{-3/2}.
\]

The pair-density factor contributes

\[
V_D^{-2}.
\]

Therefore the net parent-volume dependence is

\[
\boxed{
V_D^{+1},
}
\]

not \(V_D^{-2}\).

This is the correction to the earlier bookkeeping.

## 3. World-function optical gauge

Let

\[
S_+(x)
=
2\sigma(p,x),
\]

\[
S_-(x)
=
2\sigma(x,q).
\]

On the null edge,

\[
S_+=S_-=0.
\]

Let \(L_+\) and \(L_-\) be the affinely normalized null-generator lengths from the past/future tips to the edge point.

Choose the natural conjugate-null optical coordinates

\[
\boxed{
a
=
\frac{
S_+
}{
2L_+
},
\qquad
b
=
\frac{
S_-
}{
2L_-
}.
}
\]

At the edge, derivatives of \(L_\pm\) do not contribute to \(da,db\), because they are multiplied by \(S_\pm=0\).

Therefore

\[
da
=
\frac{
dS_+
}{
2L_+
},
\qquad
db
=
\frac{
dS_-
}{
2L_-
}.
\]

Define the invariant null-sheet cross scalar

\[
\boxed{
\chi
=
-g^{-1}
(
dS_+,
dS_-
).
}
\]

In double-null form

\[
g
=
-2\Omega^2 da\,db
+
h_{AB}ds^Ads^B
\]

one has

\[
-g^{-1}(da,db)
=
\Omega^{-2}.
\]

Hence

\[
\boxed{
\Omega^2
=
\frac{
4L_+L_-
}{
\chi
}.
}
\]

In flat space,

\[
\chi_0=8L^2,
\]

which gives

\[
\Omega_0^2=\frac12.
\]

## 4. Affine-length cancellation

For a regular null generator in \(3+1\), write the physical thin-null coefficient as

\[
\boxed{
c_\pm^{\rm phys}
=
\frac{
\pi
}{
6
}
L_\pm^2
F_\pm,
}
\]

where

\[
F_\pm=1
\]

in flat space and contains the dimensionless focusing/shear correction in curved space.

Then

\[
\Omega^6
\left(
c_+^{\rm phys}c_-^{\rm phys}
\right)^{-3/2}
\]

equals

\[
\left(
\frac{
4L_+L_-
}{
\chi
}
\right)^3
\left[
\left(
\frac{\pi}{6}
\right)^2
L_+^2L_-^2
F_+F_-
\right]^{-3/2}.
\]

The affine-length factors cancel exactly:

\[
\boxed{
(L_+L_-)^3
(L_+^2L_-^2)^{-3/2}
=
1.
}
\]

Thus the recovery coefficient has the invariant schematic form

\[
\boxed{
K_4
\propto
V_D\,
A_E\,
\chi^{-3}
F_+^{-3/2}
F_-^{-3/2},
}
\]

with the known universal scalar prefactor fixed by the flat theorem.

There is no independent affine-length correction to compute.

## 5. Logarithmic decomposition

At order \(L^4\),

\[
\boxed{
\delta\ln K_4
=
\delta\ln V_D
+
\delta\ln A_E
-
3\delta\ln\chi
-
\frac32
\left(
\delta\ln F_+
+
\delta\ln F_-
\right).
}
\]

This is manifestly invariant under optical-coordinate rescaling.

## 6. Alexandrov edge area

Wang's \(3+1\) Ricci-flat ACD result gives

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

There is no \(B^2\) contribution at this order.

## 7. Parent Alexandrov volume

Wang's total ACD volume gives

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

The sign is **positive** in the logarithmic recovery decomposition because the net normalized-coefficient algebra leaves one power of \(V_D\).

## 8. Thin-null focusing

The plane-wave Jacobi lemma gives per generator

\[
\delta\ln F_{\rm thin}
=
\frac{
L^4
}{
504
}
\mathcal H_{AB}\mathcal H^{AB}.
\]

Wang's optical-tidal average in \(d=4\) implies

\[
\left\langle
\mathcal H_{AB}\mathcal H^{AB}
\right\rangle
=
\frac85
(E^2+B^2).
\]

Therefore one sheet has average

\[
\boxed{
\left\langle
\delta\ln F_\pm
\right\rangle
=
\frac{
1
}{
315
}
(E^2+B^2)L^4.
}
\]

The two sheets together contribute to \(\delta\ln K_4\)

\[
\boxed{
-\frac32
\left\langle
\delta\ln F_+
+
\delta\ln F_-
\right\rangle
=
-\frac1{105}
(E^2+B^2)L^4.
}
\]

## 9. Correct sum of the known terms

Add edge area, parent volume, and thin focusing.

### Electric part

\[
\frac2{135}
+
\frac{127}{4725}
-
\frac1{105}
=
\boxed{
\frac{
152
}{
4725
}
}.
\]

### Magnetic part

\[
\frac1{105}
-
\frac1{105}
=
\boxed{0}.
\]

Thus

\[
\boxed{
\delta\ln K_4
\big|_{\rm known}
=
\frac{
152
}{
4725
}
E^2L^4.
}
\]

The magnetic contribution cancels exactly among the already known pieces.

## 10. The only remaining geometric term

The full vacuum response is therefore

\[
\boxed{
\delta\ln K_4
=
\frac{
152
}{
4725
}
E^2L^4
-
3
\left\langle
\delta\ln\chi
\right\rangle
+
o(L^4).
}
\]

Write

\[
\left\langle
\delta\ln\chi
\right\rangle
=
L^4
\left[
X_EE^2
+
X_BB^2
\right]
+
o(L^4).
\]

Then

\[
\boxed{
\widehat C_E
=
\frac{
152
}{
4725
}
-
3X_E,
}
\]

\[
\boxed{
\widehat C_B
=
-3X_B.
}
\]

The full problem has therefore been reduced to the invariant cross-angle scalar \(\chi\).

## 11. Geometric interpretation of chi

The covectors

\[
dS_+,
\qquad
dS_-
\]

are the affinely scaled null normals to the two Alexandrov boundary sheets.

Thus

\[
\chi
=
-g^{-1}(dS_+,dS_-)
\]

measures their Lorentzian cross normalization at the codimension-two edge.

The remaining \(L^4\) response is therefore not an arbitrary coordinate normalization.

It is the curvature correction to the relative boost/cross angle of the two null sheets.

## 12. Bel-Robinson criterion

The full coefficient is proportional to

\[
E^2+B^2
\]

if and only if

\[
\frac{
152
}{
4725
}
-
3X_E
=
-3X_B.
\]

Equivalently,

\[
\boxed{
X_E-X_B
=
\frac{
152
}{
14175
}.
}
\]

No symmetry currently enforces this relation.

The Bel-Robinson question is therefore reduced to a concrete statement about the averaged world-function cross-normalization.

## 13. Correction to the previous repository version

The earlier version of this note combined:

- \(V_D^{-2}\) from the pair density;
- physical thin-null focusing coefficients;

without restoring the powers of \(V_D\) already contained in the normalized \(c_\pm\).

That produced the incorrect partial coefficients

\[
-\frac{229}{4725},
\qquad
-\frac1{35}.
\]

Those values are superseded.

The corrected invariant bookkeeping gives

\[
\boxed{
+\frac{152}{4725}E^2,
\qquad
0\cdot B^2,
}
\]

before the \(\chi\) term.

## 14. Next target

Compute

\[
\boxed{
\left\langle
\delta\ln\chi
\right\rangle
}
\]

from the Riemann-normal-coordinate world-function expansion for the two null sheets.

Because

\[
S_\pm
\]

are the squared geodesic intervals whose zero sets define the ACD boundaries, Wang's RNC expansion provides the correct starting point.

The calculation should be checked on:

1. a purely electric algebraic Weyl tensor;
2. a radiative/type-N Weyl configuration;
3. the flat limit.
