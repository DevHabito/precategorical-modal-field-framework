# Candidate correction to the arbitrary-dimensional vacuum ACD volume formula

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact re-integration of published intermediate equations; external verification required  
**Reference:** Jinzhao Wang, *Geometry of small causal diamonds*, Phys. Rev. D 100, 064020 (2019), arXiv:1904.01034v2  
**Scope:** Ricci-flat Alexandrov causal diamonds in arbitrary spacetime dimension \(d\ge4\)

## 1. Result

Direct integration of the published null-cone boundary in Eq. (74) together with the published RNC volume density in Eq. (76) gives

\[
\boxed{
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
\left(
7d^3+58d^2+146d+116
\right)E^2
+
3(d+2)(d+6)H^2
-
\frac32(d+2)D^2
}{
90(d-1)(d+1)(d+2)(d+3)(d+4)
}
+
O(L^{d+5}).
}
\]

The printed Eq. (79) instead contains

\[
7d^3+58d^2+146d+108
\]

in the electric numerator and

\[
6(d+2)(d+6)
\]

in the \(H^2\) numerator.

The \(D^2\) coefficient is unchanged.

Thus the direct re-integration of the printed intermediate equations requires only

\[
\boxed{
108\to116
}
\]

and

\[
\boxed{
6(d+2)(d+6)
\to
3(d+2)(d+6).
}
\]

## 2. Relative-volume form

With

\[
V_0
=
\frac{
2\Omega_{d-2}L^d
}{
d(d-1)
},
\]

the result is equivalently

\[
\boxed{
\frac{\delta V}{V_0}
=
L^4
\left[
v_E(d)E^2
+
v_H(d)H^2
+
v_D(d)D^2
\right]
+
O(L^5),
}
\]

where

\[
\boxed{
v_E(d)
=
\frac{
d(7d^2+44d+58)
}{
180(d+1)(d+3)(d+4)
},
}
\]

\[
\boxed{
v_H(d)
=
\frac{
d(d+6)
}{
60(d+1)(d+3)(d+4)
},
}
\]

and

\[
\boxed{
v_D(d)
=
-\frac{
d
}{
120(d+1)(d+3)(d+4)
}.
}
\]

## 3. Cone contribution from Eq. (74)

Let

\[
s=d-1.
\]

For the upper cone,

\[
r_+
=
(L-t)
\left[
1+a_1+a_2
\right].
\]

The first-order term is

\[
a_1
=
\frac16L^2E_{nn}.
\]

Using the standard angular moments on \(S^{d-2}\),

\[
\left\langle
E_{nn}^2
\right\rangle
=
\frac{
2E^2
}{
s(s+2)
},
\]

\[
\left\langle
(E^2)_{nn}
\right\rangle
=
\frac{
E^2
}{s},
\]

and Wang's identity

\[
\left\langle
n^in^jn^ln^k
H_i{}^m{}_jH_{lmk}
\right\rangle
=
\frac{
3H^2
}{
2s(s+2)
},
\]

the expansion of

\[
r_+^{\,s}
\]

gives the normalized cone contributions

\[
\boxed{
v_E^{\rm cone}
=
\frac{
7d+2
}{
180(d+2)
},
}
\]

\[
\boxed{
v_H^{\rm cone}
=
\frac{
d
}{
60(d+1)(d+2)
},
}
\]

\[
\boxed{
v_D^{\rm cone}
=
0.
}
\]

The term quadratic in the first-order radius perturbation is retained.

## 4. Angular average of Eq. (76)

Write

\[
\sqrt{|g|}
=
1-\frac{Q}{180}+\cdots.
\]

Using the Weyl identities in Eqs. (11a)--(11f), the angular average of the tensorial contraction in Eq. (76) reduces to

\[
\boxed{
\left\langle
Q
\right\rangle
=
E^2t^4
+
\frac{
3H^2
}{
d-1
}
r^2t^2
+
\frac{
3E^2-3H^2+\frac32D^2
}{
(d-1)(d+1)
}
r^4.
}
\]

This form was also checked independently using explicit algebraic Weyl tensors in several integer dimensions.

## 5. Volume-density contribution

Since the density correction is already quadratic in curvature, it is integrated over the flat upper cone and doubled.

The exact radial/time integrals give

\[
\boxed{
v_E^{\sqrt g}
=
-\frac{
d^2+2d+8
}{
60(d+1)(d+2)(d+3)(d+4)
},
}
\]

\[
\boxed{
v_H^{\sqrt g}
=
\frac{
d^2
}{
60(d+1)(d+2)(d+3)(d+4)
},
}
\]

and

\[
\boxed{
v_D^{\sqrt g}
=
-\frac{
d
}{
120(d+1)(d+3)(d+4)
}.
}
\]

Adding cone and density terms gives the coefficients in Section 2.

## 6. Independent algebraic sector checks

Three algebraic Weyl families were used as cross-checks.

### Pure-electric family

For \(s=d-1\), take a trace-free symmetric \(E_{ij}\), \(H=0\), and

\[
D_{ijkl}
=
\frac1{s-2}
\left(
\delta_{ik}E_{jl}
-
\delta_{il}E_{jk}
-
\delta_{jk}E_{il}
+
\delta_{jl}E_{ik}
\right).
\]

This obeys the Weyl trace conditions and

\[
D^2
=
\frac4{d-3}E^2.
\]

For this family, the direct integration differs from printed Eq. (79) by

\[
\boxed{
\frac{
2d
}{
45(d+1)(d+2)(d+3)(d+4)
}
E^2L^4.
}
\]

In the absolute numerator normalization of Eq. (79), this is exactly an additional

\[
\boxed{
8E^2.
}
\]

### Pure-\(H\) family

Choose an algebraic Weyl tensor with

\[
E=0,
\qquad
D=0,
\qquad
H\ne0.
\]

The direct result is exactly one half of the printed \(H^2\) coefficient for every tested \(d\ge4\).

The symbolic calculation gives

\[
\boxed{
v_H^{\rm direct}
=
\frac12
v_H^{\rm printed}.
}
\]

### Pure spatial-Weyl family

For \(d\ge5\), choose

\[
E=0,
\qquad
H=0,
\qquad
D\ne0
\]

with \(D\) a trace-free algebraic Weyl tensor on the spatial subspace.

The direct integration agrees exactly with the printed \(D^2\) coefficient.

Thus the \(D^2\) term requires no change.

## 7. Four-dimensional reduction

In \(d=4\),

\[
H^2=2B^2,
\qquad
D^2=4E^2.
\]

Therefore

\[
\begin{aligned}
v_E^{(4)}
&=
v_E(4)
+
4v_D(4)
\\
&=
\boxed{
\frac{17}{630}
},
\end{aligned}
\]

and

\[
\begin{aligned}
v_B^{(4)}
&=
2v_H(4)
\\
&=
\boxed{
\frac1{210}
}.
\end{aligned}
\]

Hence

\[
\boxed{
\frac{V^{(4)}}{V_0}
=
1+
L^4
\left[
\frac{17}{630}E^2
+
\frac1{210}B^2
\right]
+
O(L^5).
}
\]

This is the same pair obtained independently from LRS Kasner and the symmetric plane wave.

## 8. Evidence hierarchy

The current evidence is now:

1. the published Eq. (74) integrated directly;
2. the published tensorial Eq. (76) integrated directly;
3. Wang's own angular identities in Eqs. (7)--(11);
4. explicit algebraic Weyl-sector checks;
5. exact LRS Kasner causal-cone integration;
6. exact symmetric Cahen--Wallach plane-wave integration.

All six are consistent with the candidate formula above.

The printed Eq. (79) is the outlier.

## 9. Epistemic status

The repository can now state that there is an exact algebraic inconsistency between the publicly printed intermediate equations and the publicly printed final Eq. (79).

It should still avoid claiming a formal published erratum because:

- the supplemental derivation is not publicly available through the accessible source;
- the calculation has not yet been independently reviewed by another researcher;
- the original author has not confirmed the discrepancy.

The appropriate wording is:

> Direct re-integration of the published intermediate equations yields a different coefficient formula from Eq. (79), and the re-integrated formula is independently supported by two exact Ricci-flat geometries.

## 10. Reproducibility

The symbolic checker is

tools/derive_wang_acd_volume_from_intermediate_equations_all_d.py

and keeps \(d\) symbolic.

The independent \(d=4\) checker is

tools/audit_wang_d4_eq74_eq76_to_eq79_full.py.

## 11. Next scientific step

The most useful next step is no longer another internal derivation.

The result should now be stress-tested against:

1. the unavailable Section C supplemental calculation, if it can be obtained;
2. an independent implementation in a second computer-algebra system;
3. external review by the original author or another specialist in small causal-diamond geometry.

Only after one of those checks should the candidate formula be presented as a correction to the literature rather than as a repository-level consistency result.


## 12. Software-independent regression

A second implementation was added at

\`tools/regress_wang_acd_volume_fraction_only.py\`.

It intentionally does not import SymPy or any other computer-algebra system.

It uses only:

- Python \`fractions.Fraction\`;
- integer factorials;
- the elementary beta-integral identity
  \[
  \int_0^1dt\,t^a
  \int_0^{1-t}dr\,r^{s-1+b}
  =
  \frac{
  a!(s+b-1)!
  }{
  (s+b+a+1)!
  };
  \]
- the angular contractions already stated in the paper.

The implementation checks every integer dimension

\[
4\le d\le20
\]

and reproduces independently

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

The \(d=4\) reduction again gives

\[
v_E^{(4)}=\frac{17}{630},
\qquad
v_B^{(4)}=\frac1{210}.
\]

This check reduces dependence on symbolic simplification in the main SymPy derivation.

## 13. Algebraic signature of the magnetic discrepancy

The paper explicitly states

\[
H^{kl}{}_iH_{lkj}\delta^{ij}
=
\frac12H^2,
\]

and

\[
H^{kl}{}_iH^{min}\delta^{(4)}_{klmn}
=
\frac32H^2.
\]

The \(H^2\) coefficient printed in Eq. (79) is exactly twice the coefficient obtained by applying these identities to Eqs. (74), (77), and (78).

Therefore the magnetic discrepancy has the same algebraic signature that would result if the factors \(1/2\) in those contractions were lost during the final simplification.

This is a diagnostic observation, not a claim about the unpublished intermediate algebra.

For the electric sector, the discrepancy is different: the re-integrated numerator is

\[
7d^3+58d^2+146d+116,
\]

whereas Eq. (79) prints

\[
7d^3+58d^2+146d+108.
\]

Only the constant term differs, by exactly

\[
8.
\]

No unique line-level source for that \(8\) has yet been established.

## 14. Supplemental-material access status

The APS article page identifies supplemental material but currently marks it as subscription-required.

The public ETH Research Collection entry found during this audit contains bibliographic metadata rather than the supplemental derivation.

No open copy of the Section C calculation was located in the targeted public search performed on 2026-11-12.

This is an access limitation, not evidence that no public copy exists elsewhere.
