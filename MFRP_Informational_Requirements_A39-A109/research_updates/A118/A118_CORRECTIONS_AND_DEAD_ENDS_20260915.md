# A118 — corrections and dead ends

**Date:** 2026-09-15

## 1. Do not infer `1/M^2` from a few finite values

The second-order scaling was not accepted from numerical convergence. It was derived symbolically from the surviving A117 collision channels and checked by an exact SymPy coefficient identity.

## 2. Odd parity has a genuine second-order correction

For odd `M`,

\[
\frac{1+\tau_M}{2}
=\frac{1+s}{2}+\frac{\alpha s}{M}.
\]

The `alpha s/M` term contributes to `B_1` and `S_1`. Dropping it gives a wrong `Xi_odd`.

## 3. Root scans are not a global proof

The regular grid and random-source stress found no nonpositive `Xi_p`, but those are finite samples of a continuous critical set.

They are evidence, not theorem premises.

## 4. The apparent worst sampled point is only locally certified

The exact interval certificate at `s=129/1000`, odd parity, `r=4` proves positivity only for that rigorously isolated critical point. It does not prove that this point is the global minimum of `Xi_p`.

## 5. Higher degeneracy remains possible

A118 has not ruled out

\[
\Lambda_p=0,
\qquad
\Xi_p=0
\]

somewhere else on the continuous source window.

A future global sign proof must either exclude this directly or produce a counterexample.
