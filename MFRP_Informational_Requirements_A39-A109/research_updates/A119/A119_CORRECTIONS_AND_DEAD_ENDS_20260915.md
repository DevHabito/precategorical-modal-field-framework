# A119 — corrections and dead ends

**Date:** 2026-09-15

## 1. Dense positive root scans are not a proof

A118 found 5270 positive critical-root controls. A119 does not promote that finite evidence into a theorem.

## 2. Monotonicity of sampled Xi was not used

Exploration suggested the smallest critical `Xi_p` occurs near `s=0.129`, odd parity, `r=4`, and that sampled branches increase with `s`. This was not accepted as a global monotonicity theorem.

The final proof avoids that route completely.

## 3. The key simplification is the critical equation

Trying to prove positivity directly from the raw A118 `Xi_p` expression leaves exponentials and the implicit critical root entangled.

On `Lambda_p=0`, substituting

\[
q=\frac{a_pC}{A_p+\alpha D_{p,r}}
\]

removes the transcendental root from the sign problem and turns it into rational interval arithmetic.

## 4. The finite deficit cutoff must be proved, not observed

Numerical root scans suggested critical cells stop near `r=11` even and `r=17` odd. Those empirical cutoffs were not used.

A119 instead proves the coarser but rigorous uniform exclusions

\[
r\ge13\quad\text{even},
\qquad
r\ge20\quad\text{odd}.
\]

## 5. Coarse one-box interval evaluation fails in early cells

A single interval over the entire source window and entire enlarged cell is too wide and produces negative lower bounds for the first few deficits because of dependency overestimation.

A fixed preregistered `16 x 16` rational subdivision per cell is sufficient. No adaptive box deletion or post-hoc domain narrowing is used.

## 6. No finite-M claim

A119 closes the sign of the asymptotic second-order coefficient. It does not erase the slow-convergence warning from A117/A118 and does not claim a practical finite threshold.
