# Evidence triangulation for the vacuum ACD volume correction

**Date:** 2026-11-13  
**Author:** Felipe Gianini Romero  
**Status:** research evidence map  
**Purpose:** separate algebraic re-integration, independent geometry checks, formal arithmetic, and numerical evidence for the proposed correction to Wang (2019), Eq. (79)

## 1. Competing laws

Write

\[
\frac{V(D_L)}{V_{\rm flat}(L)}
=
1+
L^4
\left[
A_dE^2+B_dH^2+C_dD^2
\right]
+
o(L^4).
\]

Direct integration of the publicly printed intermediate equations gives

\[
A_d^{\rm corr}
=
\frac{
d(7d^2+44d+58)
}{
180(d+1)(d+3)(d+4)
},
\]

\[
B_d^{\rm corr}
=
\frac{
d(d+6)
}{
60(d+1)(d+3)(d+4)
},
\]

\[
C_d^{\rm corr}
=
-\frac{
d
}{
120(d+1)(d+3)(d+4)
}.
\]

The printed Eq. (79) instead implies

\[
A_d^{\rm print}
=
\frac{
d(7d^3+58d^2+146d+108)
}{
180(d+1)(d+2)(d+3)(d+4)
},
\]

\[
B_d^{\rm print}
=
\frac{
d(d+6)
}{
30(d+1)(d+3)(d+4)
},
\]

\[
C_d^{\rm print}
=
C_d^{\rm corr}.
\]

Thus the disagreement is confined to the electric and hook sectors.

## 2. Layer A: direct re-integration of the printed equations

The repository contains independent symbolic and Fraction-only implementations of the angular and radial integrations of the printed Eqs. (74), (76)--(78).

They agree on

\[
(A_d,B_d,C_d)
=
(A_d^{\rm corr},B_d^{\rm corr},C_d^{\rm corr}).
\]

The Fraction-only implementation uses no computer-algebra system.

This establishes a public-text consistency statement:

\[
\boxed{
\text{the printed intermediate equations do not integrate to the printed Eq. (79).}
}
\]

It does not by itself establish the historical source of the discrepancy because Eq. (74) is explicitly described as abridged.

## 3. Layer B: exact symmetric Cahen--Wallach geometry

For a symmetric trace-free plane wave with transverse profile \(P\),

\[
E^2=\frac14\operatorname{Tr}(P^2),
\]

\[
H^2=\frac12\operatorname{Tr}(P^2),
\]

\[
D^2=\operatorname{Tr}(P^2).
\]

The exact Jacobi-determinant volume calculation gives

\[
\boxed{
\frac{\delta V}{V_{\rm flat}L^4\operatorname{Tr}(P^2)}
=
\frac{
d(7d+22)
}{
720(d+1)(d+3)
}.
}
\]

The corrected coefficients satisfy this identity exactly for arbitrary \(d\).

The printed coefficients differ by

\[
\boxed{
\frac{
d(3d^2+24d+32)
}{
360(d+1)(d+2)(d+3)(d+4)
}.
}
\]

Therefore the plane-wave test is an exact independent discriminator in every dimension in which the invariant decomposition applies.

## 4. Layer C: exact comoving LRS-Kasner geometries

For the LRS-Kasner family,

\[
H^2=0,
\]

\[
E^2
=
\frac{
4(d-3)^2(d-2)
}{
(d-1)^3
},
\]

\[
D^2
=
\frac{
16(d-3)(d-2)
}{
(d-1)^3
}.
\]

Independent directional-jet calculations give exact parent volumes in:

### d = 4

\[
\boxed{
c_4^{\rm Kasner}
=
\frac{68}{8505}.
}
\]

The corrected law reproduces it exactly.

The printed law differs by

\[
\boxed{
\frac4{127575}.
}
\]

### d = 5

\[
\boxed{
c_5^{\rm Kasner}
=
\frac{25}{1152}.
}
\]

The printed law differs by

\[
\boxed{
\frac1{18144}.
}
\]

### d = 6

\[
\boxed{
c_6^{\rm Kasner}
=
\frac{2288}{65625}.
}
\]

The printed law differs by

\[
\boxed{
\frac4{65625}.
}
\]

The general corrected-minus-printed Kasner gap is

\[
\boxed{
\frac{
8d(d-3)^2(d-2)
}{
45(d-1)^3(d+1)(d+2)(d+3)(d+4)
}.
}
\]

It is positive for every physical integer

\[
d\ge4.
\]

## 5. Layer D: boosted non-type-N Kasner geometry

The comoving Kasner family has

\[
H^2=0.
\]

A transverse boost in \(d=5\) gives

\[
E^2(v)
=
\frac{
v^4+2v^2+3
}{
4(1-v^2)^2
},
\]

\[
H^2(v)
=
\frac{
3v^2
}{
(1-v^2)^2
},
\]

\[
D^2(v)
=
\frac{
7v^4+2v^2+3
}{
2(1-v^2)^2
}.
\]

This produces an invariant direction different from the type-N plane-wave relation.

Direct physical causal-volume integration at

\[
v=0.3,\quad0.5,\quad0.7
\]

agrees with the corrected function within approximately

\[
1.4\times10^{-5}
\]

after \(L\to0\) extrapolation.

The same numerical volumes are separated from the printed Eq. (79) by approximately

\[
6.1\times10^{-4},
\quad
2.7\times10^{-3},
\quad
1.17\times10^{-2},
\]

respectively.

Thus the nonzero-\(H^2\) evidence is not confined to the type-N plane-wave direction.

## 6. Layer E: coefficient-level boosted perturbation

For

\[
d=5,
\qquad
v=\frac12,
\]

the corrected law predicts

\[
\boxed{
c_4=\frac7{144}.
}
\]

A second boosted calculation propagates exact local Taylor jets through the moving lens geometry and integrates the perturbative coefficient directly.

It gives:

\[
c_2\approx0
\]

and

\[
c_4
\approx
\frac7{144}
\]

without evaluating a finite-\(L\) parent volume.

The high-resolution coefficient quadrature differs from \(7/144\) by approximately

\[
2.1\times10^{-7}.
\]

This calculation has different numerical systematics from the finite-\(L\) extrapolation.

## 7. Layer F: exact boosted substructures

The following ingredients of the boosted calculation are already exact:

- timelike-tip jets;
- null-cone first-integral jets;
- flat lens switching surface;
- \(C^1\) matching of the three-ball lens;
- moving time-switch jets \(T_1(L),T_2(L)\);
- the entire fully-contained regime-III integral through \(L^4\).

Thus only the closed analytic integration of the partial-lens regimes I and II remains between the coefficient-level computation and a completely closed boosted proof.

## 8. Layer G: formal arithmetic

Lean 4 certifies the rational reductions used in the all-dimensional coefficient law, including:

- the corrected all-\(d\) coefficient reductions;
- the \(d=4\) physical specialization;
- the boosted \(d=5\) invariant combination;
- the printed boosted comparison;
- the common-numerator electric identities.

Lean does not certify the differential geometry or numerical quadrature.

Its role is deliberately narrower:

\[
\boxed{
\text{formal verification of the final algebra once geometric inputs are fixed.}
}
\]

## 9. Electric discrepancy fingerprint

The corrected electric numerator factorizes as

\[
\boxed{
(d+2)(7d^2+44d+58).
}
\]

The printed numerator is

\[
\boxed{
(d+2)(7d^2+44d+58)-8.
}
\]

All nonconstant coefficients therefore agree with the expansion of the corrected factorized form.

Only the constant term differs.

Moreover, no dimension-independent multiplicative change in any strict subset of the five printed electric contributions produces the required \(-8d\) common-numerator shift.

This localizes the electric mismatch to the final multi-term combination more strongly than to any single displayed integration term.

## 10. Hook discrepancy fingerprint

The hook coefficient has a different signature:

\[
\boxed{
B_d^{\rm print}
=
2B_d^{\rm corr}.
}
\]

The contraction identities printed earlier in the same paper are consistent with the smaller coefficient.

Thus the electric and hook discrepancies should not be assumed to have the same historical cause.

## 11. Current scientific statement

The current evidence supports:

> The publicly printed intermediate equations in Wang (2019) yield a vacuum Alexandrov-volume coefficient law different from the printed Eq. (79). The re-integrated law is independently selected by exact Cahen--Wallach geometry and exact comoving LRS-Kasner geometries in \(d=4,5,6\), and is additionally supported in the nonzero-\(H^2\) sector by direct boosted-Kasner physical volumes and coefficient-level perturbative integration.

The repository should still avoid:

> Wang (2019) is definitively wrong.

The unresolved historical issue is the unavailable/full supplemental calculation behind the explicitly abridged Eq. (74).

The mathematical issue, however, is now narrower: two explicit coefficient laws make different predictions, and the independent geometries tested so far select the re-integrated one.
