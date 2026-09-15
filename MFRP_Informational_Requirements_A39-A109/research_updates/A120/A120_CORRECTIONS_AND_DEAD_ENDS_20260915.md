# A120 — corrections and dead ends

**Date:** 2026-09-15

## 1. The first A120 conjecture was false

The initial natural target was an eventual fixed-interior analogue of the A113 remote signs,

\[
E_{b_\tau}>0,
\qquad
E_{b_\tau+3}<0.
\]

This is false.

Exact counterexamples were found before theorem promotion:

- `M=1200, s=131/1000, tau=1/5`: `E_b<0`;
- `M=536, s=129/1000, tau=9/10`: `E_{b+3}>0`.

The final theorem explains these failures rather than patching the parameter window.

## 2. High-precision raw evaluation can still lie

Exploratory arbitrary-precision evaluation of the unnormalized ten-term expression produced at least one wrong sign at very large `M` because exponentially tiny terms cancel strongly.

Those exploratory signs were discarded. Promoted finite signs use exact `fractions.Fraction` arithmetic.

## 3. The missing variable was the ceiling phase

Using only

\[
\frac{b_M}{M}\to c
\]

loses the order-one factor

\[
s^{b_M-Mc}=s^{\rho_M}.
\]

The correct asymptotic keeps

\[
\rho_M=\lceil Mc\rceil-Mc.
\]

This is the source of persistent remote-sign variation.

## 4. A fixed interior pair need not have an eventual remote sign

For irrational `c`, the parity-restricted rounding phases are dense. If the phase function crosses zero inside `(0,1)`, both factor signs occur infinitely often.

Thus searching for a larger universal `M0` is the wrong repair.

## 5. A120 does not weaken A113

A113 remains a finite all-tail theorem for the frozen target `tau=1/2`. A120 only shows that its remote-sign package is not structurally stable under arbitrary target deformation.

## 6. Boundary scaling remains separate

A120 treats fixed `s<tau`. It does not classify the collision regime `tau-s=O(1/M)`, where A117–A119 already showed that different asymptotics are required for the central nesting factor.
