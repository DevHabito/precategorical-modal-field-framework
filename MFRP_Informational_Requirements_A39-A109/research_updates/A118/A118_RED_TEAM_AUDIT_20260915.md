# A118 — red-team audit

**Date:** 2026-09-15  
**Verdict:** **PASS WITH OPEN GLOBAL SIGN**

The audit attacks the A118 second-order critical-layer expansion rather than trying to confirm a desired sign.

## Attacks performed

1. **Wrong scaling attack.** Tested whether a critical A117 point still carries a nonzero `1/M` term. The symbolic gate gives exact cancellation when `Lambda_p=0`; the next polynomial term is `Xi_p/M^2`.

2. **Parity-copy attack.** The odd finite factor `(1+tau_M)/2` contributes at order `1/M`. The odd `B_1,S_1` terms were rederived rather than copied from even parity.

3. **Missing contact-offset attack.** The source exponent correction uses `k=h-r+1`, giving `eta_k=alpha^2+2 alpha(sigma+r-1)`. Omitting `r-1` changes `Xi_p`.

4. **Hidden constant-channel attack.** A117 already supplies the stronger grouped constant estimate; after dividing by `tau^h tau^k`, it is exponentially small compared with `M^-2` for fixed collision coordinates. It does not enter `Xi_p`.

5. **Finite-root overreach attack.** Thousands of positive critical-root controls are explicitly classified as finite evidence only. They are not promoted into a global sign theorem.

6. **Local exact certificate.** At the apparent worst regular-grid control `(s,p,r)=(129/1000,odd,4)`, the critical alpha is bracketed by rational Taylor bounds and `Xi_p` is interval-certified above `2`.

7. **Slow convergence attack.** A117 already exhibits extremely slow finite-M realization near critical curves. A118 therefore makes no finite realization-threshold claim.

## Result

No contradiction was found in the second-order expansion or the displayed `Xi_p` formula.

The global statement

\[
\Xi_p>0\quad\text{on every critical surface}
\]

is **not promoted**. It remains the next falsification target.

No physical or ontological interpretation is made.
