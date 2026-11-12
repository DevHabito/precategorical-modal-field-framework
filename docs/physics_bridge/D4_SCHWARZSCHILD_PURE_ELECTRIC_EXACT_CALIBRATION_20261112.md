# Theorem candidate: exact Schwarzschild calibration of the d = 4 vacuum recovery coefficients

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact internal analytic derivation + independent numerical regression; externally unverified  
**Scope:** sufficiently small regular (3+1)-dimensional Ricci-flat Alexandrov diamonds  
**Purpose:** close the two-coefficient vacuum (L^4) response using a purely electric Schwarzschild calibration and the independent symmetric plane-wave calibration

## 1. Result

The previously established (3+1) vacuum invariant basis is

[
oxed{
rac{
K_{4,g}(D_L)
}{
9pi
}
=
1
+
L^4
left[
a_4E^2+b_4B^2
ight]_o
+
o(L^4).
}
]

The symmetric vacuum plane-wave calibration already gives

[
oxed{
a_4+b_4
=
rac{508}{4725}.
}
]

The present Schwarzschild calculation gives

[
oxed{
a_4
=
rac{683}{9450}.
}
]

Therefore

[
oxed{
b_4
=
rac{37}{1050}.
}
]

Hence the complete internally derived (3+1) vacuum response is

[
oxed{
rac{
K_{4,g}(D_L)
}{
9pi
}
=
1
+
L^4
left[
rac{683}{9450}E^2
+
rac{37}{1050}B^2
ight]_o
+
o(L^4).
}
]

This is an exact internal result, but it has not yet been independently reviewed outside the repository.

## 2. Why Schwarzschild isolates the electric coefficient

For Schwarzschild,

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

Relative to the static orthonormal observer, the magnetic Weyl tensor vanishes:

[
oxed{
B_{ij}=0.
}
]

The electric Weyl eigenvalues are proportional to

[
-2, 1, 1,
]

so

[
oxed{
E^2
=
rac{6M^2}{r^6}.
}
]

Thus a sufficiently small Schwarzschild diamond determines (a_4) directly.

## 3. Dimensionless weak-field variables

Choose the reference radius (r_0), and define

[
oxed{
m
=
rac{M}{r_0},
}
]

and

[
oxed{
	au
=
rac{T}{r_0},
}
]

where (T) is the static coordinate half-time of the symmetric tip pair.

The universal coefficient (a_4) is independent of (M) and (r_0).

Therefore it can be extracted from the weak-field coefficient of

[
m^2	au^4.
]

At the reference point,

[
E^2
=
rac{
6m^2
}{
r_0^4
}.
]

The true geodesic half-size obeys

[
L
=
sqrt{A_0},T
+
O(T^3),
]

with

[
A_0=1-2m.
]

Consequently,

[
E^2L^4
=
6m^2	au^4
+
O(m^3	au^4)
+
O(m^2	au^6).
]

Thus the coefficient of (m^2	au^4) in the recovery ratio is exactly (6a_4).

## 4. Why the weak-field extraction is legitimate

The invariant-basis theorem already excludes an independent scalar linear in

[

abla
abla C
]

at order (L^4) in a Ricci-flat neighborhood.

The centered parity theorem eliminates the odd curvature-jet sector.

Therefore the (m^2	au^4) term in a purely electric Schwarzschild family belongs to the quadratic Weyl sector

[
a_4E^2.
]

No additional vacuum scalar coefficient is available at this order in (3+1).

This step is essential: the weak-field calculation is a calibration of an already classified invariant basis, not an assumption that every fourth-order term must be Weyl squared.

## 5. Optical reduction

Factor the static lapse:

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

where

[
oxed{
h_{m opt}
=
A^{-2}dr^2
+
A^{-1}r^2dOmega^2.
}
]

The physical volume form is

[
dV_g
=
A^2
,dt,
dV_{m opt}.
]

Introduce the optical radial coordinate (R),

[
dR
=
rac{dr}{A},
]

and the warped-product radius

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

The optical sectional curvatures are

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

## 6. Optical geodesic system

Let

[
mu=cospsi
]

be the initial radial direction cosine and

[
ell
=
f(r_0)sinpsi
]

the conserved optical angular momentum.

Writing

[
v=rac{dR}{ds},
]

the exact optical geodesic equations reduce to

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

These equations are expanded formally in (m) and the dimensionless optical length.

## 7. Two exact Jacobi channels

The meridional transverse Jacobi field satisfies

[
oxed{
j_parallel''
+
K_{m rad}
j_parallel
=
0.
}
]

The orthogonal azimuthal field satisfies

[
oxed{
j_perp''
+
K_perp
j_perp
=
0,
}
]

where

[
oxed{
K_perp
=
v^2K_{m rad}
+
rac{ell^2}{f^2}
K_{m tan}.
}
]

For each channel, two fundamental solutions are used:

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

The backward Jacobi solution with

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

This identity follows from the unit Wronskian.

## 8. Thin-null coefficient

After setting

[
s=xT,
qquad
0<x<1,
]

the physical thin-null interval coefficient can be written as

[
c_psi(T)
=
rac{
pi T^2
}{6}
,
overline C(mu,m,	au),
]

with

[
oxed{
overline C
=
6
int_0^1
x(1-x)
A(xT)^2
sqrt{
mathcal R_J
}
,dx,
}
]

where

[
mathcal R_J
=
rac{
j_parallel(s)b_parallel(s)
j_perp(s)b_perp(s)
}{
j_parallel(T)j_perp(T)
T^2x^2(1-x)^2
}.
]

By construction,

[
overline C=1
]

in flat spacetime.

## 9. Normalized parent-volume factor

Define

[
overline V
]

by

[
V_D
=
rac{
2pi
}{3}
T^4
overline V.
]

The exact optical expression is

[
oxed{
overline V
=
rac12
int_{-1}^{1}
12
int_0^1
(1-x)
A(xT)^2
rac{
j_parallel(xT)
j_perp(xT)
}{
T^2
}
,dx,dmu.
}
]

Flat spacetime gives

[
overline V=1.
]

## 10. Normalized intrinsic edge factor

Let

[
I
=
int_{S^2}
A(T)^4
c_psi(T)^{-3}
j_parallel(T)
j_perp(T)
,dOmega.
]

Define

[
overline I
]

by

[
I
=
rac{
864
}{
pi^2T^4
}
overline I.
]

Then

[
oxed{
overline I
=
rac12
int_{-1}^{1}
A(T)^4
rac{
j_parallel(T)
j_perp(T)
}{
T^2
}
overline C^{-3}
,dmu.
}
]

The intrinsic edge theorem gives

[
oxed{
rac{
K_{m Schw}
}{
K_{m Mink}
}
=
overline V
,
overline I.
}
]

This factorization is exact for the static optical reduction before the small-(T) expansion.

## 11. Exact formal-series calculation

The repository script

[
	exttt{
tools/derive_d4_schwarzschild_pure_electric_exact.py
}
]

implements a truncated bivariate formal power-series ring.

It retains

[
m^i	au^j,
qquad
ile2,
qquad
jle6,
]

and uses exact SymPy rational arithmetic.

The script:

1. solves the optical geodesic equations coefficient by coefficient;
2. solves both Jacobi systems coefficient by coefficient;
3. constructs the backward Jacobi fields from the Wronskian;
4. forms the normalized thin-null coefficient;
5. integrates exactly over (xin[0,1]);
6. integrates exactly over (muin[-1,1]);
7. multiplies the normalized parent and edge factors.

No floating-point value is used to obtain the coefficient.

## 12. Exact parent-volume expansion

The angularly averaged parent factor is

[
oxed{
overline V
=
1
-
4m
+
4m^2
+
rac23
m^2	au^2
+
rac{17}{105}
m^2	au^4
+
O(
m^3,
m^2	au^6
).
}
]

The coefficients through the required order are exact rationals.

## 13. Exact edge expansion

The intrinsic edge factor is

[
oxed{
overline I
=
1
+
4m
+
12m^2
-
rac23
m^2	au^2
+
rac{428}{1575}
m^2	au^4
+
O(
m^3,
m^2	au^6
).
}
]

Again, all displayed coefficients are exact rationals.

## 14. Structural cancellations

Multiplying the two factors gives several nontrivial cancellations.

### Zeroth-size weak-field normalization

At (	au=0),

[
(1-4m+4m^2)
(1+4m+12m^2)
=
1
+
O(m^3).
]

Thus the lapse/measure normalization cancels from the recovery ratio.

### Apparent (m^2	au^2) term

The two factors contain

[
+rac23m^2	au^2
]

and

[
-rac23m^2	au^2.
]

They cancel exactly:

[
oxed{
[m^2	au^2]
left(
overline Voverline I
ight)
=
0.
}
]

This is consistent with the absence of a vacuum (L^2) response.

### First surviving vacuum term

At fourth order,

[
rac{17}{105}
+
rac{428}{1575}
=
rac{
255+428
}{
1575
}
=
oxed{
rac{683}{1575}.
}
]

Therefore

[
oxed{
rac{
K_{m Schw}
}{
K_{m Mink}
}
=
1
+
rac{
683
}{
1575
}
m^2	au^4
+
O(
m^3	au^4,
m^2	au^6
).
}
]

## 15. Extracting a4

At the same order,

[
E^2L^4
=
6m^2	au^4
+
O(
m^3	au^4,
m^2	au^6
).
]

Comparing with

[
rac{
K_{m Schw}
}{
K_{m Mink}
}
=
1
+
a_4E^2L^4
+
o(L^4)
]

gives

[
6a_4
=
rac{
683
}{
1575
}.
]

Hence

[
oxed{
a_4
=
rac{
683
}{
9450
}.
}
]

This coefficient is obtained analytically, not by rational reconstruction from floating-point data.

## 16. Independent numerical regression

Before the exact series derivation, the full unexpanded optical geodesic/Jacobi system was integrated numerically.

The independent numerical note is

[
	exttt{
D4_SCHWARZSCHILD_PURE_ELECTRIC_NUMERICAL_CALIBRATION_20261112.md
}.
]

Across several mass/radius choices, the (T	o0) extrapolations agreed with

[
rac{683}{9450}
=
0.072275132275132ldots
]

at approximately the (10^{-9}) to (10^{-8}) level in the tested grids.

That regression did not impose the rational value.

It therefore supplies an independent floating-point check of the exact formal-series calculation.

## 17. Magnetic coefficient from the independent plane wave

The symmetric plane-wave calculation gives

[
a_4+b_4
=
rac{
508
}{
4725
}
=
rac{
1016
}{
9450
}.
]

Subtracting the Schwarzschild coefficient,

[
egin{aligned}
b_4
&=
rac{
1016-683
}{
9450
}\
&=
rac{
333
}{
9450
}\
&=
oxed{
rac{
37
}{
1050
}.
}
end{aligned}
]

Thus both (3+1) vacuum coefficients are fixed.

## 18. Complete d = 4 vacuum response

The resulting first nonzero Ricci-flat correction is

[
oxed{
rac{
K_{4,g}(D_L)
}{
9pi
}
=
1
+
L^4
left[
rac{
683
}{
9450
}
E_{ij}E^{ij}
+
rac{
37
}{
1050
}
B_{ij}B^{ij}
ight]_o
+
o(L^4).
}
]

Equivalently,

[
K_{4,g}(D_L)
=
9pi
+
9pi L^4
left[
rac{
683
}{
9450
}
E^2
+
rac{
37
}{
1050
}
B^2
ight]_o
+
o(L^4).
]

## 19. Bel--Robinson question is resolved internally

The Bel--Robinson superenergy density in (3+1) is proportional to

[
E^2+B^2.
]

But

[
rac{
683
}{
9450
}

e
rac{
37
}{
1050
}.
]

Indeed,

[
rac{
683
}{
9450
}
-
rac{
37
}{
1050
}
=
rac{
350
}{
9450
}
=
oxed{
rac{
1
}{
27
}.
}
]

Therefore the recovery statistic is not proportional to the Bel--Robinson density at its first nonzero vacuum order:

[
oxed{
a_4-b_4
=
rac1{27}.
}
]

This is a particularly simple exact difference that was not imposed anywhere in the derivation.

## 20. Alternative invariant form

Using

[
W
=
E^2+B^2,
]

and

[
C_{mu
uhosigma}
C^{mu
uhosigma}
=
8(E^2-B^2),
]

write

[
a_4E^2+b_4B^2
=
alpha W
+
eta C^2.
]

Then

[
alpha
=
rac{
a_4+b_4
}{2}
=
oxed{
rac{
254
}{
4725
}
},
]

and

[
eta
=
rac{
a_4-b_4
}{16}
=
oxed{
rac{
1
}{
432
}
}.
]

Therefore

[
oxed{
a_4E^2+b_4B^2
=
rac{
254
}{
4725
}
(E^2+B^2)
+
rac{
1
}{
432
}
C_{mu
uhosigma}
C^{mu
uhosigma}.
}
]

This makes the deviation from pure Bel--Robinson proportionality explicit.

## 21. Literature boundary

The calculation uses established ingredients but applies them to a project-specific observable.

Relevant literature includes:

- **G. W. Gibbons and S. N. Solodukhin (2007)**, *The Geometry of Small Causal Diamonds*, arXiv:hep-th/0703098.
- **G. W. Gibbons, C. M. Warnick, and M. C. Werner (2008)**, *Light-bending in Schwarzschild-de-Sitter: projective geometry of the optical metric*, arXiv:0808.3074.
- **Stephen Casey (2012)**, *Optical 2-metrics of Schwarzschild-Tangherlini Spacetimes and the Bohlin-Arnold Duality*, arXiv:1208.0168.
- **Jinzhao Wang (2019)**, *Geometry of small causal diamonds*, arXiv:1904.01034.

The optical reduction, Schwarzschild Jacobi geometry, Weyl decomposition, and small-causal-diamond program are established subjects.

The coefficients

[
rac{683}{9450},
qquad
rac{37}{1050}
]

belong to the present arrow-erasure recovery observable.

A targeted search performed on 2026-11-12 found no obvious prior occurrence of these exact coefficients in this recovery context.

That search does not establish novelty by itself.

## 22. What has been proved internally

Conditional on the previously established repository results:

1. the (3+1) vacuum invariant basis is exactly (E^2,B^2);
2. the symmetric plane-wave calibration exactly fixes (a_4+b_4);
3. the intrinsic edge functional is the correct curved recovery coefficient;

the Schwarzschild weak-field series fixes

[
a_4=rac{683}{9450}
]

by exact rational algebra.

Together these imply

[
b_4=rac{37}{1050}.
]

No fit, empirical regression, or ad hoc parameter enters the exact coefficient extraction.

## 23. What is not yet claimed

The following stronger claims are not made:

- that the result has passed independent external peer review;
- that the coefficient pair has already appeared nowhere in the literature;
- that the (dge5) coefficients are known;
- that the same regular formula survives caustics or conjugate-point degeneration;
- that the entire repository proof chain has been formalized in Lean.

The result is internally exact but still requires independent derivation and external scrutiny.

## 24. Next target

The best next test is an independent calculation that does **not** use Schwarzschild optical coordinates.

A Riemann-normal-coordinate/world-function expansion of the intrinsic volume-gradient edge functional should reproduce

[
oxed{
a_4
=
rac{683}{9450},
qquad
b_4
=
rac{37}{1050}.
}
]

That would close the main coordinate-method dependence.

After that, the natural higher-dimensional frontier is to determine

[
a_d, b_d, c_d
qquad
(dge5)
]

for the invariant basis

[
E^2, H^2, D^2.
]
