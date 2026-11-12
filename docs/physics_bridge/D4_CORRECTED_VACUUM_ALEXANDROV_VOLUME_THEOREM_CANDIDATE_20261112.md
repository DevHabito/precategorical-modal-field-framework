> **CURRENT AUDIT STATUS — 2026-11-12:** the coefficient pair is derived exactly from the printed RNC intermediate equations and passes the exact symmetric-plane-wave combination. The physical LRS-Kasner volume independently converges numerically to the same purely electric coefficient; the earlier factor-two alarm was a bookkeeping issue in a symbolic Kasner series implementation, not in the physical volume. The symbolic Kasner series checker remains diagnostic, so Kasner is counted here as an independent **numerical geometry check**, not as an exact analytic calibration.

# Theorem candidate: corrected d = 4 vacuum Alexandrov four-volume coefficients

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact internal derivation from published intermediate RNC equations + exact plane-wave consistency check + independent numerical Kasner check; externally unverified  
**Scope:** sufficiently small centered \(3+1\)-dimensional Alexandrov intervals in a Ricci-flat neighborhood  
**Purpose:** state the internally supported \(L^4\) vacuum four-volume law independently of the orientation-recovery observable

## 1. Statement

Let

\[
D_L
=
I(
\exp_o(-LT),
\exp_o(+LT)
)
\]

be a centered sufficiently small Alexandrov interval in a smooth \(3+1\)-dimensional Ricci-flat neighborhood.

Relative to the unit timelike vector \(T\), write the Weyl tensor in electric/magnetic form

\[
E_{ij}=C_{0i0j},
\qquad
B_{ij}
=
\frac12
\epsilon_{jkl}
C_{0i}{}^{kl}.
\]

Then the internally derived vacuum four-volume expansion is

\[
\boxed{
\frac{
V(D_L)
}{
V_{\rm Mink}(L)
}
=
1
+
L^4
\left[
\frac{17}{630}E^2
+
\frac1{210}B^2
\right]_o
+
o(L^4).
}
\]

Here

\[
V_{\rm Mink}(L)
=
\frac{2\pi}{3}L^4.
\]

This result is exact within the repository derivations but has not yet passed independent external review.

## 2. Invariant basis

For a centered parity-even scalar in \(3+1\) vacuum, the \(L^4\) quadratic Weyl basis is

\[
E^2,
\qquad
B^2.
\]

No independent scalar linear in \(\nabla\nabla C\) survives after the vacuum Bianchi identities, trace identities, centered parity, and derivative commutators are reduced.

Therefore two independent vacuum calibrations are sufficient to determine the universal coefficient pair.

## 3. Independent numerical calibration A: LRS Kasner

Use the LRS Kasner vacuum

\[
ds^2
=
-dt^2
+
t^{-2/3}dx^2
+
t^{4/3}(dy^2+dz^2)
\]

with centered tips

\[
t=1\pm L.
\]

The central comoving worldline is geodesic.

At the midpoint,

\[
B^2=0,
\qquad
E^2=\frac8{27}.
\]

A direct numerical integration of the unexpanded physical null cones, with the flat normalization built into \(V/V_{\rm Mink}\), extrapolates to

\[
\frac{
V_{\rm Kasner}/V_{\rm Mink}-1
}{
L^4
}
\longrightarrow
\frac{68}{8505}
=
0.00799529688418\ldots.
\]

Since \(E^2=8/27\), this supports

\[
\boxed{
v_E=\frac{17}{630}.
}
\]

The independent physical-volume checker is

tools/check_d4_kasner_parent_volume_numerically.py.

The older formal-series Kasner script remains under normalization audit and is not used here as an exact proof.

## 4. Exact calibration B: symmetric plane wave

Use the Ricci-flat symmetric plane wave

\[
ds^2
=
-2\,du\,dv
+
dx_1^2+dx_2^2
+
H_{ij}x^ix^jdu^2,
\]

with

\[
H
=
\operatorname{diag}
(-\omega^2,+\omega^2).
\]

For a centered diamond,

\[
U=\sqrt2L,
\qquad
z=\omega U.
\]

The exact causal-volume function gives

\[
\frac{
V_{\rm PW}
}{
V_{\rm Mink}
}
=
1+\frac{z^4}{252}+O(z^8).
\]

Since

\[
E^2=B^2=\frac{\omega^4}{2},
\qquad
z^4=4\omega^4L^4,
\]

the plane wave fixes

\[
\frac{
v_E+v_B
}{2}
=
\frac1{63}.
\]

Thus

\[
v_E+v_B
=
\frac2{63}.
\]

Substituting \(v_E=17/630\),

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

## 5. Direct RNC integration of Wang's intermediate equations

The same pair follows without using either coefficient fit above.

Wang (2019), *Geometry of small causal diamonds*, gives:

- Eq. (74): the vacuum ACD null-cone boundary;
- Eq. (75): the doubled upper-cone volume integral;
- Eq. (76): the Ricci-flat RNC volume density.

The repository checker

tools/audit_wang2019_d4_acd_volume_eq79.py

integrates those printed intermediate equations directly.

### Pure electric representative

Take

\[
E=\operatorname{diag}(2,-1,-1),
\qquad
B=0,
\]

so

\[
E^2=6.
\]

The moving-boundary contribution is

\[
\boxed{
v_E^{\rm boundary}
=
\frac1{36}.
}
\]

The RNC determinant contribution is

\[
\boxed{
v_E^{\det g}
=
-\frac1{1260}.
}
\]

Hence

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

### Pure magnetic representative

Take

\[
E=0,
\qquad
B=\operatorname{diag}(2,-1,-1),
\]

so

\[
B^2=6.
\]

The moving-boundary contribution is

\[
\boxed{
v_B^{\rm boundary}
=
\frac1{225}.
}
\]

The RNC determinant contribution is

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

Thus the corrected coefficient pair follows directly from the published formulas preceding Eq. (79).

## 6. Internal inconsistency with the printed Eq. (79)

The \(d=4\) specialization of Wang Eq. (79) gives instead

\[
\left.
\frac{\delta V}{V_0}
\right|_{\rm Eq.\,79}
=
L^4
\left[
\frac{127}{4725}E^2
+
\frac1{105}B^2
\right].
\]

The differences are

\[
\boxed{
\frac{17}{630}
-
\frac{127}{4725}
=
\frac1{9450},
}
\]

and

\[
\boxed{
\frac1{210}
-
\frac1{105}
=
-\frac1{210}.
}
\]

Therefore Eq. (79) is not consistent with the direct \(d=4\) integration of Eqs. (74) and (76), under the conventions printed in the paper.

## 7. Exact plane-wave audit of the intermediate formulas

The symmetric plane wave permits a stronger local test.

Its exponential map around the midpoint gives exact RNC coordinates with transverse Jacobian factors

\[
F_1(U)
=
\frac{\sin(\omega U)}{\omega U},
\]

\[
F_2(U)
=
\frac{\sinh(\omega U)}{\omega U}.
\]

Hence

\[
\sqrt{|g_{\rm RNC}|}
=
F_1F_2
=
1
-
\frac{\omega^4U^4}{90}
+
O(\omega^8U^8).
\]

Using

\[
U=\frac{t-z}{\sqrt2},
\]

\[
\boxed{
\sqrt{|g_{\rm RNC}|}
=
1
-
\frac{\omega^4}{360}
(t-z)^4
+
\cdots,
}
\]

which agrees exactly with Eq. (76).

The exact plane-wave null boundary transformed to RNC reproduces all angularly relevant terms in Eq. (74).

The difference from the printed abridged expression is odd in the longitudinal direction cosine and integrates to zero.

Thus the intermediate formulas themselves pass the exact plane-wave check.

## 8. Alternative invariant form

Using

\[
C_{\mu\nu\rho\sigma}
C^{\mu\nu\rho\sigma}
=
8(E^2-B^2)
\]

and

\[
W=E^2+B^2,
\]

write

\[
v_EE^2+v_BB^2
=
\alpha W+\beta C^2.
\]

Then

\[
\alpha
=
\frac12
\left(
\frac{17}{630}
+
\frac1{210}
\right)
=
\boxed{
\frac1{63}
},
\]

and

\[
\beta
=
\frac1{16}
\left(
\frac{17}{630}
-
\frac1{210}
\right)
=
\boxed{
\frac1{720}
}.
\]

Therefore

\[
\boxed{
\frac{
V(D_L)
}{
V_{\rm Mink}(L)
}
=
1
+
L^4
\left[
\frac1{63}(E^2+B^2)
+
\frac1{720}
C_{\mu\nu\rho\sigma}
C^{\mu\nu\rho\sigma}
\right]_o
+
o(L^4).
}
\]

This is equivalent to the electric/magnetic form.

## 9. Scientific status

The coefficient pair is supported internally by three distinct routes:

1. direct exact integration of the published RNC intermediate formulas;
2. exact symmetric-plane-wave causal-volume integration of the type-N combination;
3. independent numerical LRS-Kasner causal-volume integration of the purely electric sector.

Only the first two items are analytic/exact at present; the Kasner item is a high-precision numerical geometry check.

The current public APS page lists the 2019 article and its supplemental material, but the supplemental material is subscription-restricted.

A targeted literature search performed on 2026-11-12 did not reveal a published erratum correcting Eq. (79).

Absence of an erratum in that search is not proof that none exists.

The repository therefore uses the wording:

\[
\boxed{
\text{internally exact corrected coefficient candidate, externally unverified.}
}
\]

It does not claim an erratum on behalf of the original author.

## 10. Next verification target

The most useful next external-quality step is to reconstruct the general \(d=4\) angular integration from Eqs. (74) and (76) in a short human-readable derivation, independent of the SymPy checker.

That proof should expose the four rational pieces

\[
\frac1{36},
\qquad
-\frac1{1260},
\qquad
\frac1{225},
\qquad
\frac1{3150},
\]

directly from standard \(S^2\) moments.

Once written, the discrepancy can be communicated as a concise reproducible note rather than as a large computational audit.
