# A120 — red-team audit

**Date:** 2026-09-15  
**Verdict:** **PASS WITH REFUTATION OF THE NAIVE STABILIZATION CLAIM**

The audit attacks the fixed-interior remote-sign theorem and its corollaries rather than attempting to preserve an A113-like picture.

## Attacks performed

1. **Frozen regression attack.** The exact audit rechecks 21 `tau=1/2` A113 sentinels and reproduces `E_b>0` and `E_{b+3}<0`.

2. **Naive stabilization attack.** Exact rational counterexamples show that neither remote sign extends universally to arbitrary fixed interior targets.

3. **Hidden-rounding attack.** The derivation keeps `rho_M=b_M-Mc` exactly. Replacing `b_M` by `Mc+o(M)` would erase the leading factor `s^{rho_M}` and give a false single-limit statement.

4. **Parity attack.** The normalization retains both `sigma_p` in `tau^{sigma_p}` and the central-Q factor `a_p(tau)`, so odd parity is not copied from even parity.

5. **Discarded-channel attack.** Each omitted ten-term channel is bounded after normalization: beta-product, beta-affine and source-affine terms vanish geometrically, while the constant channel vanishes because `b_M/M<1/2` asymptotically.

6. **Finite-counterexample overreach attack.** Infinite alternation is not inferred from the two finite counterexamples. It uses the analytic phase theorem, exact nonzero endpoint margins, irrationality of `c`, and density of parity-restricted fractional parts.

7. **Irrationality attack.** For both promoted alternating examples, irrationality follows from unique prime factorization: a rational `c` would force `tau^n=s^{2m}`, impossible because the source contains a prime absent from the target.

8. **Floating-sign attack.** Exploratory high-precision unnormalized evaluations produced a wrong large-`M` sign and were discarded. Promoted finite signs and phase endpoint bounds use exact `Fraction` arithmetic.

## Result

No contradiction was found in the rounding-phase asymptotic or its density corollaries.

The conjecture

\[
E_{b_M}>0,\qquad E_{b_M+3}<0
\]

for all sufficiently large `M` at every fixed interior `(s,tau)` is **refuted**, not repaired.

A120 makes no target-deformed A114, novelty, physical, or ontological claim.
