# A122 — corrections and dead ends

**Date:** 2026-09-15

## 1. `Psi=0` does not automatically make `Omega/M` decisive

The first tempting continuation of A121 was

\[
\Psi=0\quad\Rightarrow\quad \text{look only at }\Omega/M.
\]

That is incomplete for an actual sequence because the rounding phase itself moves with `M`.

If

\[
\rho_M-\rho_*=O(1/M),
\]

then the linearization of `Psi` contributes at exactly the same order as `Omega/M`.

The corrected object is the scaled drift

\[
\eta=M(x_M-\xi_p).
\]

## 2. There is no polynomial tower of independent intrinsic coefficients

For fixed interior parameters, the normalized factor has

\[
\Phi(x_M)+\Omega(x_M)/M
\]

plus a remainder smaller than every power of `1/M`.

So an attempted intrinsic `M^-2` coefficient at fixed phase would be artificial. `M^-2` terms arise from a more refined movement of the phase itself.

## 3. `Omega(xi)` is not sign-definite

Exact interval calculations show opposite signs at two nearby rational targets for `s=129/1000`, even parity. Hence an interior intrinsic double-critical target exists.

This kills any proposed universal rule such as `Omega(xi)>0`.

## 4. Double-critical does not imply actual exact resonance

The equation

\[
\Omega_p(\xi_p)=0
\]

is a statement about the asymptotic phase front. It does not force the arithmetic sequence `rho_M` to hit `xi_p-j` exactly, or even faster than `1/M`.

That realization problem is separate.

## 5. Finite signs remain exact

All promoted finite factor signs in the A122 audit use `Fraction`. The displayed values of `eta`, `eta_*`, `Theta`, and the approximate double-critical root are diagnostics only.
