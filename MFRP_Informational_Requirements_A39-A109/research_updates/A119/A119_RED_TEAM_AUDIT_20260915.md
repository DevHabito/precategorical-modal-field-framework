# A119 — red-team audit

**Date:** 2026-09-15  
**Verdict:** **PASS WITH SCOPE**

The target claim is

\[
\Lambda_p=0\Longrightarrow\Xi_p>0
\]

under the frozen A115–A118 reduced-factor contract.

## Attacks performed

1. **Transcendental-root dependence.** Rejected as unnecessary. On a critical surface the A117 equation gives exactly
   \[
   q=e^{-\alpha}=\frac{a_pC}{A_p+\alpha D_{p,r}},
   \]
   so the A118 coefficient becomes rational in `s,alpha` for fixed parity and `r`.

2. **Hidden denominator sign.** The interval audit asserts positivity of `A_p+alpha D` on every certified box. Analytically A117 already gives `A_p>0`, `D>0`, and `alpha>0`.

3. **Missed deep contact cells.** The proof does not truncate `r` from numerical observation. Exact right-edge lower bounds prove there are no even critical cells for `r>=13` and no odd critical cells for `r>=20`.

4. **Wrong cell enclosure.** The true cell uses `L=-log s`. The audit uses the inherited exact A117 enclosure
   \[
   2<L<21/10
   \]
   and certifies a larger rational rectangle, so every true critical point is included.

5. **Point-sampling fallacy.** The 6400 computations are interval boxes, not samples. Every returned interval encloses the function over the full real box. The theorem uses the strictly positive lower endpoints.

6. **Dependency overestimation.** Natural interval evaluation can make bounds wider but cannot exclude a true value. Despite dependency overestimation, all 6400 lower endpoints remain positive; the smallest certified lower bound is still above `1.35`.

7. **Parity-copy attack.** Even and odd parities are certified separately. The odd factor `a_p=(1+s)/2` and half-cell shift are retained from A117/A118.

8. **Resonant endpoints.** The enlarged closed rectangles include the right endpoints and the resonance assignments from A117; no open-endpoint shortcut is used.

9. **Provenance.** The Git blob of the published audit script is byte-for-byte the same script executed to generate the promoted JSON result.

## Preserved limits

A119 does not produce a minimal finite `M` for sign realization. The statement remains asymptotic through A118. It does not generalize A114, and it makes no physical or ontological claim.

Within that scope, no surviving gap or counterexample was found.
