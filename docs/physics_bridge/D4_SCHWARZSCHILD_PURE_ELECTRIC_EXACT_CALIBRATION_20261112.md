> **Status update (2026-11-12):** the requested independent non-Schwarzschild verification has now been completed using the LRS Kasner vacuum, exact null-cone integrals, Synge world-function endpoint gradients, and the local intrinsic edge density. It reproduces \(a_4=683/9450\) exactly. See \`D4_KASNER_WORLD_FUNCTION_PURE_ELECTRIC_CALIBRATION_20261112.md\`.

# Theorem candidate: exact Schwarzschild calibration of the d = 4 vacuum recovery coefficients

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact internal analytic derivation + independent numerical regression; externally unverified  
**Scope:** sufficiently small regular \(3+1\)-dimensional Ricci-flat Alexandrov diamonds

## 1. Result

The established \(3+1\) vacuum invariant basis is

\[
\boxed{
\frac{K_{4,g}(D_L)}{9\pi}
=
1+
L^4\left[a_4E^2+b_4B^2\right]_o
+
o(L^4).
}
\]

The symmetric vacuum plane-wave calibration gives

\[
\boxed{
a_4+b_4=\frac{508}{4725}.
}
\]

The Schwarzschild calculation gives

\[
\boxed{
a_4=\frac{683}{9450}.
}
\]

Therefore

\[
\boxed{
b_4=\frac{37}{1050}.
}
\]

Hence

\[
\boxed{
\frac{K_{4,g}(D_L)}{9\pi}
=
1+
L^4
\left[
\frac{683}{9450}E^2+
\frac{37}{1050}B^2
\right]_o
+
o(L^4).
}
\]

This is an exact internal result, not yet an externally reviewed theorem.

## 2. Why Schwarzschild isolates the electric coefficient

For Schwarzschild,

\[
ds^2=-A(r)\,dt^2+A(r)^{-1}dr^2+r^2d\Omega^2,
\qquad
A(r)=1-\frac{2M}{r}.
\]

Relative to the static orthonormal observer,

\[
B_{ij}=0,
\qquad
E^2=\frac{6M^2}{r^6}.
\]

A sufficiently small Schwarzschild diamond therefore isolates \(a_4\).

## 3. Weak-field variables

Set

\[
m=\frac{M}{r_0},
\qquad
\tau=\frac{T}{r_0}.
\]

The geodesic half-size obeys

\[
L=\sqrt{A_0}\,T+O(T^3),
\]

and therefore

\[
E^2L^4
=
6m^2\tau^4
+
O(m^3\tau^4,m^2\tau^6).
\]

Thus the coefficient of \(m^2\tau^4\) in the recovery ratio is \(6a_4\).

## 4. Exact formal-series calculation

The checker at

tools/derive_d4_schwarzschild_pure_electric_exact.py

uses exact SymPy rational arithmetic and retains

\[
m^i\tau^j,
\qquad
i\le2,
\qquad
j\le6.
\]

It constructs the optical geodesic series, the two Jacobi channels, the backward Jacobi fields, the thin-null coefficient, the parent volume, the intrinsic edge factor, and the exact angular integrals.

No floating-point fit enters the coefficient derivation.

## 5. Parent and edge factors

With

\[
V_D=\frac{2\pi}{3}T^4\overline V,
\]

the exact series is

\[
\boxed{
\overline V
=
1-4m+4m^2
+\frac23m^2\tau^2
+\frac{17}{105}m^2\tau^4
+O(m^3,m^2\tau^6).
}
\]

The normalized intrinsic edge factor is

\[
\boxed{
\overline I
=
1+4m+12m^2
-\frac23m^2\tau^2
+\frac{428}{1575}m^2\tau^4
+O(m^3,m^2\tau^6).
}
\]

The recovery ratio is

\[
\frac{K_{\rm Schw}}{K_{\rm Mink}}
=
\overline V\,\overline I.
\]

## 6. Structural cancellations

The apparent vacuum term at order \(m^2\tau^2\) cancels exactly:

\[
+\frac23m^2\tau^2-\frac23m^2\tau^2=0.
\]

The first surviving vacuum term is

\[
\frac{17}{105}
+
\frac{428}{1575}
=
\frac{683}{1575}.
\]

Therefore

\[
\boxed{
\frac{K_{\rm Schw}}{K_{\rm Mink}}
=
1+
\frac{683}{1575}m^2\tau^4
+
O(m^3\tau^4,m^2\tau^6).
}
\]

Comparing with \(E^2L^4=6m^2\tau^4+\cdots\),

\[
\boxed{
a_4=\frac{683}{9450}.
}
\]

## 7. Independent numerical regression

The separate numerical checker at

tools/calibrate_d4_schwarzschild_pure_electric_response.py

integrates the unexpanded optical geodesic/Jacobi system.

Across several \(M,r_0\) choices and quadrature resolutions, the \(T\to0\) extrapolation converges to

\[
\frac{683}{9450}
=
0.072275132275132\ldots
\]

at approximately the \(10^{-9}\) to \(10^{-8}\) level in the best tested grids.

The numerical experiment preceded the exact series derivation.

## 8. Magnetic coefficient

The independent plane-wave relation gives

\[
a_4+b_4=\frac{508}{4725}.
\]

Thus

\[
\boxed{
b_4=\frac{37}{1050}.
}
\]

A useful exact difference is

\[
\boxed{
a_4-b_4=\frac1{27}.
}
\]

Therefore the response is not proportional to \(E^2+B^2\).

## 9. Alternative invariant form

Since

\[
C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}
=
8(E^2-B^2),
\]

the response may be written

\[
\boxed{
a_4E^2+b_4B^2
=
\frac{254}{4725}(E^2+B^2)
+
\frac1{432}
C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}.
}
\]

## 10. Scientific status

The result is internally exact conditional on the previously established invariant-basis and intrinsic-edge theorems.

It is not yet claimed to have independent external verification, and no negative literature search is treated as proof of novelty.

The next verification target is a world-function/Riemann-normal-coordinate derivation of the intrinsic volume-gradient edge functional that reproduces the same two coefficients without using the Schwarzschild optical reduction.
