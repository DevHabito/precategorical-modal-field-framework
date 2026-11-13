# Exact higher-dimensional LRS-Kasner checks of the corrected vacuum ACD volume

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact rational directional-jet calculations in \(d=5\) and \(d=6\); externally unverified  
**Scope:** centered LRS-Kasner Alexandrov intervals in spacetime dimensions five and six  
**Purpose:** provide a second exact Ricci-flat family, independent of Cahen--Wallach, that probes the corrected all-\(d\) vacuum Alexandrov-volume coefficients

## 1. Corrected all-d target

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
o(L^4),
\]

with the coefficients obtained by direct re-integration of Wang's published intermediate equations,

\[
A_d
=
\frac{
d(7d^2+44d+58)
}{
180(d+1)(d+3)(d+4)
},
\]

\[
B_d
=
\frac{
d(d+6)
}{
60(d+1)(d+3)(d+4)
},
\]

\[
C_d
=
-\frac{
d
}{
120(d+1)(d+3)(d+4)
}.
\]

The symmetric Cahen--Wallach family checks one exact combination of these coefficients for arbitrary \(d\).

The purpose of the present calculation is to probe a different invariant direction with

\[
H^2=0
\]

and dimension-dependent

\[
\frac{D^2}{E^2}.
\]

## 2. LRS-Kasner family

Let

\[
n=d-1
\]

and choose

\[
p_\parallel
=
-\frac{n-2}{n},
\qquad
p_\perp
=
\frac2n,
\]

with \(p_\perp\) repeated \(n-1\) times.

The metric is

\[
ds^2
=
-dt^2
+
t^{2p_\parallel}dx^2
+
t^{2p_\perp}d\mathbf y^2.
\]

The Kasner constraints hold:

\[
p_\parallel+(n-1)p_\perp=1,
\]

\[
p_\parallel^2+(n-1)p_\perp^2=1.
\]

Thus the metric is Ricci flat.

Choose centered tips

\[
p=(1-L,\mathbf0),
\qquad
q=(1+L,\mathbf0).
\]

The central comoving line is geodesic, so \(L\) is the exact proper-time half-size.

At the midpoint,

\[
H^2=0,
\]

\[
E^2
=
\frac{
4(n-2)^2(n-1)
}{
n^3
},
\]

\[
D^2
=
\frac{
16(n-1)(n-2)
}{
n^3
}.
\]

Hence

\[
\frac{D^2}{E^2}
=
\frac4{n-2},
\]

which changes with dimension.

## 3. Exact directional-jet method

Spatial translation symmetry gives first integrals for null geodesics.

For an axial direction cosine \(\mu\), set

\[
w=\mu^2.
\]

The calculation is performed direction by direction using exact rational \(w\).

For each rational direction it:

1. expands the conserved-momentum parameter through \(L^4\);
2. solves the null-ray direction equation coefficient by coefficient;
3. constructs past and future cone radii;
4. solves their crossing location;
5. integrates the physical volume density
   \[
   \sqrt{\det g_{\rm spatial}}=t;
   \]
6. extracts the directional \(L^2\) and \(L^4\) coefficients.

Five rational directions reconstruct the directional polynomials.

Three additional rational directions are held out from the interpolation and used as exact zero-residual tests.

No floating-point value enters the calculation.

## 4. Exact d = 5 result

For

\[
d=5,
\qquad
n=4,
\]

the Kasner exponents are

\[
p_\parallel=-\frac12,
\qquad
p_\perp=\frac12.
\]

The exact directional expansion is

\[
I(w,L)
=
\frac25
+
c_2(w)L^2
+
c_4(w)L^4
+
O(L^6),
\]

where

\[
\boxed{
c_2(w)
=
\frac{
4(16w^2-20w+3)
}{
105
},
}
\]

and

\[
\boxed{
c_4(w)
=
\frac{
26560w^4
-70336w^3
+61059w^2
-19080w
+1377
}{
22680
}.
}
\]

The held-out directions

\[
w=\frac9{16},
\qquad
\frac34,
\qquad
\frac23
\]

all reproduce both polynomials with exact zero residual.

For the normalized \(S^3\) measure,

\[
\langle w^k\rangle
=
\frac{(1/2)_k}{(2)_k}.
\]

Therefore

\[
\boxed{
\langle c_2\rangle=0,
}
\]

and

\[
\boxed{
\langle c_4\rangle=\frac5{576}.
}
\]

The physical normalization is

\[
\frac{n+1}{2}
=
\frac52.
\]

Hence

\[
\boxed{
\frac{
V_{\rm Kasner}^{(5)}
}{
V_{\rm flat}^{(5)}
}
=
1+
\frac{
25
}{
1152
}
L^4
+
O(L^6).
}
\]

At the midpoint,

\[
E^2=\frac34,
\qquad
D^2=\frac32.
\]

The corrected all-\(d\) formula gives

\[
\boxed{
A_5E^2+C_5D^2
=
\frac{25}{1152}.
}
\]

The exact geometry and corrected RNC formula therefore agree identically.

Checker:

tools/derive_d5_lrs_kasner_parent_volume_exact.py

## 5. Exact d = 6 result

For

\[
d=6,
\qquad
n=5,
\]

the exponents are

\[
p_\parallel=-\frac35,
\qquad
p_\perp=\frac25.
\]

The directional series is

\[
I(w,L)
=
\frac13
+
c_2(w)L^2
+
c_4(w)L^4
+
O(L^6),
\]

with

\[
\boxed{
c_2(w)
=
\frac{
175w^2-215w+28
}{
280
},
}
\]

and

\[
\boxed{
c_4(w)
=
\frac{
12271875w^4
-31773000w^3
+26430775w^2
-7600010w
+505456
}{
9450000
}.
}
\]

The same three held-out directions again give exact zero residual.

For \(S^4\),

\[
\langle w^k\rangle
=
\frac{(1/2)_k}{(5/2)_k}.
\]

Thus

\[
\boxed{
\langle c_2\rangle=0,
}
\]

\[
\boxed{
\langle c_4\rangle
=
\frac{
2288
}{
196875
}.
}
\]

The physical normalization factor is

\[
\frac{n+1}{2}=3.
\]

Therefore

\[
\boxed{
\frac{
V_{\rm Kasner}^{(6)}
}{
V_{\rm flat}^{(6)}
}
=
1+
\frac{
2288
}{
65625
}
L^4
+
O(L^6).
}
\]

At the midpoint,

\[
E^2=\frac{144}{125},
\qquad
D^2=\frac{192}{125}.
\]

The corrected all-\(d\) formula predicts

\[
\boxed{
A_6E^2+C_6D^2
=
\frac{
2288
}{
65625
}.
}
\]

Again the equality is exact.

Checker:

tools/derive_d6_lrs_kasner_parent_volume_exact.py

## 6. Why these checks are stronger than the earlier numerical regressions

The previous all-\(d\) Kasner audit used direct numerical integration and \(L\to0\) extrapolation.

The present calculations instead use:

- exact rational direction values;
- exact truncated formal series;
- exact symbolic integration;
- exact sphere moments;
- held-out directions not used in interpolation;
- exact comparison with the all-\(d\) coefficient formula.

Therefore the evidence classification for \(d=5,6\) can be upgraded from numerical regression to exact internal analytic/computational verification.

## 7. Combined invariant coverage

The two exact geometry families probe distinct Weyl directions.

### Cahen--Wallach

For the symmetric plane wave,

\[
E^2=\frac14T_2,
\qquad
H^2=\frac12T_2,
\qquad
D^2=T_2.
\]

This probes

\[
\frac{A_d}{4}
+
\frac{B_d}{2}
+
C_d.
\]

### LRS Kasner

For the higher-dimensional Kasner family,

\[
H^2=0,
\]

and

\[
\frac{D^2}{E^2}
=
\frac4{d-3}.
\]

This probes

\[
A_dE^2+C_dD^2
\]

along a distinct direction whose invariant ratio changes with \(d\).

Thus the agreement in \(d=5,6\) is not a repetition of the type-N test.

## 8. Current evidence boundary

These results substantially strengthen the corrected all-\(d\) formula implied by the published intermediate equations.

They do **not** yet prove the full formula for every \(d\), because:

1. the LRS-Kasner family has \(H^2=0\);
2. one exact family does not span the full three-invariant space in \(d\ge5\);
3. the omitted terms in the abridged published null-boundary formula have not been reconstructed generically for arbitrary \(d\);
4. no independent external review has yet been obtained.

The strongest current statement is:

\[
\boxed{
\text{the corrected all-d formula passes exact independent geometry tests}
}
\]

for:

- the Cahen--Wallach invariant direction in arbitrary dimension;
- the LRS-Kasner invariant direction exactly in \(d=4,5,6\).

## 9. Next target

The remaining invariant direction is the magnetic/hook sector.

A decisive next geometry would have

\[
H^2\ne0
\]

and a ratio of

\[
E^2,\ H^2,\ D^2
\]

not proportional to the Cahen--Wallach relation.

An exact homogeneous Ricci-flat geometry with tractable null geodesics would be ideal.

If such a family is not available, the alternative is a direct algebraic construction of generic Weyl tensors and a complete unabridged RNC null-boundary expansion through \(C^2\), followed by exact angular integration.
