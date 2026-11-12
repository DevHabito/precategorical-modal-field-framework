# Numerical Schwarzschild calibration of the d = 4 purely electric vacuum response

> **Superseded as a coefficient proof:** this file is retained as an independent floating-point regression. The value \(a_4=683/9450\) was subsequently obtained by exact rational formal-series algebra in D4_SCHWARZSCHILD_PURE_ELECTRIC_EXACT_CALIBRATION_20261112.md.

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** independent numerical regression  
**Scope:** small regular Schwarzschild Alexandrov intervals outside the horizon

## 1. Target

For a centered \(3+1\) vacuum diamond,

\[
\frac{K_{4,g}(D_L)}{9\pi}
=
1+
L^4[a_4E^2+b_4B^2]
+
o(L^4).
\]

Schwarzschild is purely electric for the static observer:

\[
B_{ij}=0,
\qquad
E^2=\frac{6M^2}{r^6}.
\]

Therefore the small-diamond limit isolates \(a_4\).

## 2. Numerical method

The script

tools/calibrate_d4_schwarzschild_pure_electric_response.py

uses the Schwarzschild optical metric, integrates the optical geodesic and both transverse Jacobi systems with SciPy DOP853, and evaluates the parent-volume and intrinsic-edge integrals using Gauss--Legendre quadrature.

The measured quantity is

\[
Q(T)
=
\frac{
K_{\rm Schw}/K_{\rm Mink}-1
}{
E^2(\sqrt{A_0}T)^4
},
\qquad
A_0=1-\frac{2M}{r_0}.
\]

The \(T\to0\) intercept estimates \(a_4\).

## 3. Main regression

For

\[
M=1,
\qquad
r_0=8,
\]

with \(48\) angular nodes and \(80\) radial nodes:

| \(T\) | \(Q(T)\) |
|---:|---:|
| 0.45 | 0.0724009032868 |
| 0.55 | 0.0724630405222 |
| 0.65 | 0.0725376254449 |
| 0.75 | 0.0726246717154 |
| 0.85 | 0.0727241925129 |
| 0.95 | 0.0728362033899 |
| 1.05 | 0.0729607214840 |

A cubic extrapolation in \(T^2\) gives

\[
0.0722751272222.
\]

The exact value later obtained analytically is

\[
\frac{683}{9450}
=
0.072275132275132\ldots
\]

with a difference of about

\[
-5.05\times10^{-9}
\]

for this run.

## 4. Mass/radius checks

Using the same quadrature and half-time sequence:

| \(M\) | \(r_0\) | extrapolated coefficient |
|---:|---:|---:|
| 0.5 | 8.0 | 0.0722751290635 |
| 1.0 | 8.0 | 0.0722751272222 |
| 1.5 | 8.0 | 0.0722751311354 |
| 1.0 | 6.0 | 0.0722751330216 |
| 0.8 | 7.0 | 0.0722751313467 |

The result is stable across distinct \(M/r_0\) values.

## 5. Resolution check

For \(M=1,r_0=8\):

| angular nodes | radial nodes | intercept |
|---:|---:|---:|
| 24 | 40 | 0.0722751634 |
| 32 | 60 | 0.0722751824 |
| 48 | 80 | 0.0722751272 |
| 64 | 100 | 0.0722751350 |

The convergence is not monotone, so these differences are not treated as rigorous error bars.

## 6. Role of this file

This regression is useful because it was performed before the exact symbolic derivation and did not impose the rational coefficient.

It is therefore an independent floating-point check of

\[
\boxed{
a_4=\frac{683}{9450}.
}
\]

It is not the proof of that equality.

The remaining independent scientific target is a direct world-function/RNC derivation rather than another optical-coordinate regression.
