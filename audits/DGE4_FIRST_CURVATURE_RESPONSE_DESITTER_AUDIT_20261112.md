# Audit: de Sitter check of the d >= 4 first curvature response

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** independent numerical asymptotic regression  
**Target:** DGE4_FIRST_CURVATURE_RESPONSE_COEFFICIENTS_20261112.md

## 1. Purpose

The analytic derivation of

\[
\alpha_d,
\qquad
\gamma_d
\]

uses a Taylor expansion of a general spatially-flat FLRW conformal factor.

This audit avoids that Taylor derivation.

Instead it starts from the **exact** conformal density of de Sitter spacetime on a centered proper-time diamond and evaluates the weighted null-joint coefficient directly by one-dimensional quadrature.

## 2. Exact de Sitter density

In flat slicing,

\[
ds^2
=
-d\tau^2
+
e^{2H\tau}d\mathbf x^2.
\]

In conformal time,

\[
A(\eta)
=
-\frac1{H\eta}.
\]

A centered proper-time diamond has endpoints

\[
\tau=\pm L.
\]

After mapping the conformal-coordinate interval to the unit Minkowski diamond, the exact raw sprinkling density is

\[
\boxed{
w_x(t)
=
[
\cosh x
-
t\sinh x
]^{-d},
}
\]

where

\[
x=HL.
\]

No small-\(x\) metric expansion is used to obtain this expression.

## 3. Exact weighted coefficient formula

For \(d\ge4\),

\[
\frac{
K_d[w]
}{
K_d[1]
}
=
w(0)^2
\langle w\rangle_-^{-a_m}
\langle w\rangle_+^{-a_m}
\langle w\rangle_D^{2a_m-2},
\]

with

\[
a_m
=
1+\frac2d.
\]

The three averages are computed numerically from the exact \(w_x(t)\).

## 4. Curvature prediction

de Sitter satisfies

\[
R=d(d-1)H^2,
\]

and, for unit timelike \(T\),

\[
R_{TT}
=
-(d-1)H^2.
\]

Therefore the candidate curvature formula predicts

\[
\frac{
K_{\rm dS}
}{
K_{\rm Mink}
}
=
1+c_dx^2+O(x^4),
\]

where

\[
\boxed{
c_d
=
d(d-1)\alpha_d
-
(d-1)\gamma_d.
}
\]

The \(O(x^3)\) term is absent by the centered de Sitter symmetry.

## 5. Independent quadrature results

An independent numerical quadrature was executed during the derivation.

### d = 4

Prediction:

\[
c_4
=
-\frac73
=
-2.333333333333\ldots
\]

Measured values:

| \(x\) | \((K/K_0-1)/x^2\) |
|---:|---:|
| 0.10 | -2.3030735173 |
| 0.05 | -2.3257130409 |
| 0.02 | -2.3321115880 |
| 0.01 | -2.3330278076 |

### d = 5

Prediction:

\[
c_5
=
-\frac{41}{14}
=
-2.928571428571\ldots
\]

Measured:

| \(x\) | \((K/K_0-1)/x^2\) |
|---:|---:|
| 0.10 | -2.8818158985 |
| 0.05 | -2.9167788036 |
| 0.02 | -2.9266798274 |
| 0.01 | -2.9280980112 |

### d = 6

Prediction:

\[
c_6
=
-\frac72
=
-3.5.
\]

Measured:

| \(x\) | \((K/K_0-1)/x^2\) |
|---:|---:|
| 0.10 | -3.4342016069 |
| 0.05 | -3.4833802648 |
| 0.02 | -3.4973331382 |
| 0.01 | -3.4993330087 |

### d = 8

Prediction:

\[
c_8
=
-\frac{23}{5}
=
-4.6.
\]

Measured:

| \(x\) | \((K/K_0-1)/x^2\) |
|---:|---:|
| 0.10 | -4.4887550475 |
| 0.05 | -4.5718234712 |
| 0.02 | -4.5954751701 |
| 0.01 | -4.5988681982 |

## 6. Interpretation

The exact de Sitter weighted calculation approaches the analytic \(L^2\) response in every tested dimension.

This is not an independent proof of universality beyond conformally flat metrics.

It is a strong regression against:

- sign errors;
- proper-time/conformal-time centering errors;
- missing normalization factors;
- mistakes in the Beta-kernel moments;
- mistakes in the conversion from \((h,k)\) to \((R,R_{TT})\).

No discrepancy was found.

## 7. Reproducibility

The repository script

\[
\texttt{tools/verify\_dge4\_curvature\_response\_desitter.py}
\]

implements the exact density calculation with Gauss--Legendre quadrature.

The analytic coefficient derivation is in

\[
\texttt{tools/derive\_dge4\_first\_curvature\_response.py}.
\]

## 8. Verdict

The \(d\ge4\) first-curvature-response coefficients survive an independent exact de Sitter check.

The remaining uncertainty is the structural extension from the conformally flat calibration family to the full regular metric class, not the coefficient algebra inside the calibration.
