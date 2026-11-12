# Numerical calibration candidate: the purely electric d = 4 vacuum response in Schwarzschild

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** reproducible numerical calibration candidate; not an analytic theorem  
**Scope:** small regular Schwarzschild Alexandrov intervals outside the horizon  
**Purpose:** obtain an independent purely electric calibration for the two-coefficient (3+1) vacuum recovery law

## 1. Question

The current (3+1) Ricci-flat expansion is

[
oxed{
rac{K_{4,g}(D_L)}{9pi}
=
1
+
L^4
left[
a_4 E^2
+
b_4 B^2
ight]_o
+
o(L^4).
}
]

The symmetric plane-wave calculation already fixes the exact combination

[
oxed{
a_4+b_4
=
rac{508}{4725}.
}
]

A second vacuum geometry with a different electric/magnetic ratio is therefore enough to separate the two coefficients.

Schwarzschild is useful because the Weyl tensor is purely electric for the static orthonormal observer:

[
B_{ij}=0,
]

and

[
oxed{
E^2
=
rac{6M^2}{r^6}.
}
]

The small-diamond limit of a Schwarzschild calibration therefore isolates (a_4).

## 2. Static conformal split

Write the Schwarzschild metric as

[
ds^2
=
-A(r),dt^2
+
A(r)^{-1}dr^2
+
r^2dOmega^2,
]

with

[
A(r)
=
1-rac{2M}{r}.
]

Factor out the lapse:

[
oxed{
g
=
A
left[
-dt^2
+
h_{m opt}
ight],
}
]

where the optical metric is

[
oxed{
h_{m opt}
=
A^{-2}dr^2
+
A^{-1}r^2dOmega^2.
}
]

This is the standard optical-geometry reduction of a static spacetime: null curves project to geodesics of (h_{m opt}).

The physical four-volume form is

[
dV_g
=
A^2,dt,dV_{m opt}.
]

For tips at the same static spatial point and coordinate times

[
t=pm T,
]

the causal diamond in the conformally related ultrastatic metric is

[
|t|+ho_{m opt}(x,x_0)<T.
]

Thus the whole coefficient calculation can be reduced to optical geodesics and their Jacobi fields.

## 3. Optical warped-product geometry

Introduce the optical radial coordinate (R) by

[
dR
=
rac{dr}{A},
]

and define

[
f(r)
=
rac{r}{sqrt A}.
]

Then

[
h_{m opt}
=
dR^2
+
f(R)^2dOmega^2.
]

The two independent sectional curvatures are

[
oxed{
K_{m rad}
=
rac{
M(3M-2r)
}{
r^4
},
}
]

and

[
oxed{
K_{m tan}
=
rac{
M(4r-9M)
}{
r^4
}.
}
]

For an optical geodesic launched at angle (psi), let

[
mu=cospsi,
]

and let

[
ell
=
f(r_0)sinpsi
]

be the conserved angular momentum.

Writing

[
v=rac{dR}{ds},
]

the radial system is

[
oxed{
rac{dr}{ds}
=
A v,
}
]

[
oxed{
rac{dv}{ds}
=
ell^2
rac{
A(1-3M/r)
}{
r^3
}.
}
]

## 4. Two Jacobi channels

There are two transverse Jacobi modes.

The meridional mode obeys

[
j_parallel''
+
K_{m rad}j_parallel
=
0.
]

The azimuthal mode obeys

[
j_perp''
+
K_perp j_perp
=
0,
]

where

[
oxed{
K_perp
=
v^2K_{m rad}
+
rac{ell^2}{f^2}K_{m tan}.
}
]

For each channel we integrate two fundamental solutions:

[
j(0)=0,
qquad
j'(0)=1,
]

and

[
k(0)=1,
qquad
k'(0)=0.
]

The backward solution satisfying

[
b(T)=0,
qquad
b'(T)=-1
]

is

[
oxed{
b(s)
=
j(T)k(s)-k(T)j(s).
}
]

The Wronskian then gives the transverse Hessian sum

[
oxed{
mathcal M_i(s)
=
rac{
j_i(T)
}{
j_i(s)b_i(s)
}.
}
]

## 5. Thin-null physical volume coefficient

For a small inward null deficit (alpha), write

[
V_{m thin}
=
c_psi(T)alpha^2
+
o(alpha^2).
]

The optical/Jacobi reduction gives

[
oxed{
c_psi(T)
=
pi
int_0^T
A(s)^2
sqrt{
rac{
j_parallel(s)b_parallel(s)
j_perp(s)b_perp(s)
}{
j_parallel(T)j_perp(T)
}
}
,ds.
}
]

In flat space,

[
j_i=s,
qquad
b_i=T-s,
qquad
A=1,
]

so

[
c_0(T)
=
rac{pi T^2}{6},
]

as required.

## 6. Parent volume

The geodesic-polar optical volume element is

[
dV_{m opt}
=
j_parallel(s)
j_perp(s)
,ds,dOmega.
]

Therefore

[
oxed{
V_D
=
2
int_{S^2}
int_0^T
(T-s)
A(s)^2
j_parallel(s)
j_perp(s)
,ds,dOmega.
}
]

The factor (2(T-s)) is the ultrastatic coordinate-time width of the diamond at optical radius (s).

## 7. Intrinsic edge factor

For the static time-symmetric pair, the two physical thin coefficients agree at each edge direction.

Using the volume-null coordinates of the intrinsic curved-edge theorem, the (d=4) joint functional reduces to a factor proportional to

[
V_D
int_{S^2}
A(T)^4
c_psi(T)^{-3}
j_parallel(T)
j_perp(T)
,dOmega.
]

Define

[
oxed{
I(T)
=
int_{S^2}
A(T)^4
c_psi(T)^{-3}
j_parallel(T)
j_perp(T)
,dOmega.
}
]

In flat spacetime,

[
V_0
=
rac{2pi}{3}T^4,
]

and

[
I_0
=
rac{864}{pi^2T^4}.
]

Hence

[
V_0I_0
=
rac{576}{pi}.
]

The normalized Schwarzschild recovery ratio used in the computation is therefore

[
oxed{
rac{K_{m Schw}}{K_{m Mink}}
=
rac{
V_DI
}{
576/pi
}.
}
]

This formula has the correct flat limit exactly.

## 8. Centering issue

The two static-coordinate tips are not connected by a segment of the static worldline that is itself geodesic.

That does not make the Alexandrov interval non-geodesic: in a sufficiently small convex normal neighborhood the two tip events have a unique timelike geodesic and therefore a well-defined geodesic midpoint.

Time-reflection symmetry places that midpoint on the (t=0) slice and makes the midpoint four-velocity static.

As (T	o0),

[
r_{m mid}
=
r_0
+
O(T^2),
]

and the geodesic half proper time satisfies

[
L
=
sqrt{A(r_0)},T
+
O(T^3).
]

Consequently replacing (r_{m mid}) by (r_0), and (L) by (sqrt{A_0}T), changes

[
E^2L^4
]

only beyond the (T^4) coefficient being extracted.

This is sufficient for the numerical small-(T) calibration, but an explicit midpoint-expansion lemma should still be written before promoting the result to an analytic theorem.

## 9. Numerical protocol

The repository script

[
	exttt{tools/calibrate_d4_schwarzschild_pure_electric_response.py}
]

uses:

- SciPy DOP853 for the optical geodesic and Jacobi equations;
- relative tolerance (2	imes10^{-12});
- absolute tolerance (2	imes10^{-14});
- Gauss--Legendre quadrature in both optical radius and launch direction;
- an even extrapolation in (T), fitted as a cubic polynomial in (T^2).

The default half-time sequence is

[
T
=
0.45,,
0.55,,
0.65,,
0.75,,
0.85,,
0.95,,
1.05.
]

For each run the measured quantity is

[
oxed{
Q(T)
=
rac{
K_{m Schw}/K_{m Mink}-1
}{
E^2
left(
sqrt{A_0}T
ight)^4
}.
}
]

The target is the intercept

[
lim_{T	o0}Q(T).
]

## 10. Main run

For

[
M=1,
qquad
r_0=8,
]

with (48) angular nodes and (80) radial nodes, the measured sequence was

| (T) | (Q(T)) |
|---:|---:|
| 0.45 | 0.0724009032868 |
| 0.55 | 0.0724630405222 |
| 0.65 | 0.0725376254449 |
| 0.75 | 0.0726246717154 |
| 0.85 | 0.0727241925129 |
| 0.95 | 0.0728362033899 |
| 1.05 | 0.0729607214840 |

The cubic-in-(T^2) intercept is

[
oxed{
0.0722751272222.
}
]

## 11. Rational recognition

The stable numerical limit is extremely close to

[
oxed{
rac{683}{9450}
=
0.072275132275132ldots
}
]

For the principal run the difference is approximately

[
-5.05	imes10^{-9}.
]

The rational value was recognized after the numerical extrapolation; it was not imposed in the fit.

Using a denominator cap of (10^4), the independently extrapolated values below all rationalize to the same fraction (683/9450).

This is evidence for a candidate exact coefficient, not an analytic proof of rationality.

## 12. Mass/radius cross-checks

Using the same (48	imes80) quadrature and the same half-time sequence:

| (M) | (r_0) | extrapolated (a_4) | difference from (683/9450) |
|---:|---:|---:|---:|
| 0.5 | 8.0 | 0.0722751290635 | (-3.21	imes10^{-9}) |
| 1.0 | 8.0 | 0.0722751272222 | (-5.05	imes10^{-9}) |
| 1.5 | 8.0 | 0.0722751311354 | (-1.14	imes10^{-9}) |
| 1.0 | 6.0 | 0.0722751330216 | (+7.46	imes10^{-10}) |
| 0.8 | 7.0 | 0.0722751313467 | (-9.28	imes10^{-10}) |

The agreement across distinct values of (M/r_0) is important because the coefficient is supposed to be local and universal.

## 13. Resolution check

For

[
M=1,
qquad
r_0=8,
]

the (T	o0) intercept remains near the same value as the angular/radial quadrature is changed:

| angular nodes | radial nodes | intercept |
|---:|---:|---:|
| 24 | 40 | 0.0722751634 |
| 32 | 60 | 0.0722751824 |
| 48 | 80 | 0.0722751272 |
| 64 | 100 | 0.0722751350 |

The convergence is not monotone, so the finite-resolution difference should not be interpreted as a rigorous error bound.

It does show that the rational candidate is not tied to one quadrature grid.

## 14. Candidate coefficient

The present computation supports

[
oxed{
a_4
stackrel{m num}{=}
rac{683}{9450}.
}
]

The notation

[
stackrel{m num}{=}
]

is deliberate: the equality is currently a numerical conjecture.

It must not yet be cited as a proved exact coefficient.

## 15. Conditional magnetic coefficient

If the Schwarzschild candidate is certified analytically, then the exact plane-wave relation

[
a_4+b_4
=
rac{508}{4725}
=
rac{1016}{9450}
]

would imply

[
oxed{
b_4
=
rac{333}{9450}
=
rac{37}{1050}.
}
]

Thus the full (3+1) vacuum response would become

[
oxed{
rac{K_{4,g}}{9pi}
=
1
+
L^4
left[
rac{683}{9450}E^2
+
rac{37}{1050}B^2
ight]
+
o(L^4).
}
]

This formula is still conditional on the analytic certification of the Schwarzschild coefficient.

## 16. Bel--Robinson consequence

The two candidate coefficients are unequal:

[
rac{683}{9450}

e
rac{37}{1050}.
]

Therefore, if the calibration is confirmed, the arrow-erasure recovery response is **not** proportional to

[
E^2+B^2
]

at first nonzero vacuum order.

That would distinguish this observable from a direct Bel--Robinson superenergy density.

The conclusion should remain conditional until the analytic Schwarzschild coefficient is proved.

## 17. Literature boundary

Relevant established work includes:

1. **G. W. Gibbons and S. N. Solodukhin (2007)**, *The Geometry of Small Causal Diamonds*, arXiv:hep-th/0703098.  
   This establishes the general small-Alexandrov-diamond curvature-expansion program at Ricci order.

2. **Jinzhao Wang (2019)**, *Geometry of small causal diamonds*, arXiv:1904.01034.  
   This gives higher-order vacuum causal-diamond geometry in terms of electric, magnetic, and spatial Weyl invariants and emphasizes that simple Bel--Robinson proportionality depends on the observable.

3. **G. W. Gibbons, C. M. Warnick, and M. C. Werner (2008)**, *Light-bending in Schwarzschild-de-Sitter: projective geometry of the optical metric*, arXiv:0808.3074.  
   This is part of the standard optical-geometry literature behind the static conformal reduction.

4. **Stephen Casey (2012)**, *Optical 2-metrics of Schwarzschild-Tangherlini Spacetimes and the Bohlin-Arnold Duality*, arXiv:1208.0168.  
   This treats projected Schwarzschild null geodesics as geodesics of the optical metric.

These works do not determine the project-specific arrow-erasure coefficient (a_4).

A targeted literature search on 2026-11-12 found no obvious occurrence of the exact fractions

[
683/9450
]

or

[
37/1050
]

in this causal-diamond/recovery context.

That negative search is **not** a proof of novelty.

## 18. Failed analytic route

An exploratory attempt to obtain the same coefficient directly from a bivariate symbolic Picard expansion of the optical geodesic/Jacobi system became algebraically unwieldy before a clean exact coefficient was obtained.

No symbolic result from that attempt is used as evidence.

The numerical ODE/quadrature calculation is independent of that failed symbolic route.

## 19. Next analytic target

The immediate task is no longer to search for another numerical geometry.

It is to prove or falsify

[
oxed{
a_4
=
rac{683}{9450}.
}
]

The cleanest route is a controlled small-(T) expansion of:

1. the Schwarzschild optical geodesics;
2. the two Jacobi determinants;
3. the thin-null coefficient (c_psi);
4. the parent volume (V_D);
5. the intrinsic edge integral (I);

followed by the exact angular integral over (mu=cospsi).

A second independent implementation should also evaluate the same coefficient using the Riemann-normal-coordinate/world-function formulation rather than optical coordinates.

Only after those two checks agree should the numerical candidate be promoted to a theorem.
