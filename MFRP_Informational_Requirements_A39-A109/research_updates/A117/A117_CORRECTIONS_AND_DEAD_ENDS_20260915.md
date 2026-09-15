# A117 — corrections and dead ends

**Date:** 2026-09-15

This file preserves rejected routes and numerical failures encountered while classifying the A116 collision layer.

## 1. False shortcut: copy the even phase formula into odd parity

Rejected.

For `M=2h+1`, the scale-normalized central block contributes

\[
a_{\rm odd}(s)=\frac{1+s}{2},
\]

and the contact cells are shifted by one half unit. The odd formula had to be rederived from the exact A115 Q block.

## 2. First-order contact localization is insufficient on resonances

Using only

\[
M c_{\tau_M}(s)=\frac M2-x+o(1)
\]

leaves integer/half-integer `x` ambiguous.

The next term is

\[
+\frac{\alpha^2}{(-\log s)M},
\]

which is strictly positive and fixes the eventual ceiling convention.

## 3. Deep floating-point cancellation produced false signs

Exploratory arbitrary-precision calculations with too few digits caused individual coefficients to round to zero when `M` was large, and at least one odd-parity normalized factor was assigned the wrong sign.

Those outputs were discarded.

All promoted finite phase signs use exact `Fraction` arithmetic. Limit signs in the audit use rational Taylor enclosures.

## 4. Finite-M sign need not match the limiting phase quickly

Several controls near a critical curve have the opposite finite sign at `M` around one thousand and only settle later.

Therefore A117 does not infer a finite realization threshold from the asymptotic phase function.

The theorem says only:

\[
\Lambda_p\ne0
\Longrightarrow
\operatorname{sgn}J_M=\operatorname{sgn}\Lambda_p
\]

for sufficiently large `M` of the fixed parity.

## 5. Critical surfaces are not classified by continuity

At

\[
\Lambda_p=0,
\]

the leading `1/M` boundary term vanishes. A117 deliberately makes no finite-sign claim there.

A next-order expansion is required.

## 6. Lambert W is representation, not proof

The `W_{-1}` expression for the phase root is useful but not needed for existence or uniqueness. The proof uses the exact derivative sign and positive left-edge margin.

This prevents branch-selection conventions from becoming hidden theorem premises.

## 7. No physical interpretation

The emergence of cells, phases and a collision layer is a property of the reduced exponential-moment optimization problem. No spacetime, field, RZS or ontological claim follows from A117.
