# Exact cancellation checkpoint: the A115 adjacent cofactor

**Recorded:** 2026-11-10. **Branch:** `research/a115-a119-uniform-remainder-20261110`.
**Status:** symbolic identity independently rechecked; new Lean module submitted for kernel verification, not yet PASS.

## Scope

This is the A115 **reduced C2(k)** cofactor, not an unrestricted optimal F2/F3 solution.
Start from the precise active-band cofactor

\[
E_k=(A_\tau B_\beta-H_\beta B_\tau)\Delta B_s+
(-A_\tau\Delta B_\beta+H_\beta\Delta B_\tau)B_s+
(-B_\beta\Delta B_\tau+B_\tau\Delta B_\beta)H_s.
\]

Keep the untruncated powers beta^k=uK, s^k=uW, tau^k=uT and let x=1/M and q=k/M. To isolate one clean *polynomial* obligation, take A_a=1/2 and the finite-length power terms a^M=0 in B_a and Delta B_a, but keep H_beta=1/2+uU and H_s=1/2+uV. This is **an auxiliary algebraic specialization only**: the actual finite-M model has nonzero a^M and those terms must be restored later.

Under these definitions, the exact relation is

\[
2(\tau E_k-E_{k+1}) =
u^2\mathcal C+u^2K\mathcal R_K+u^3\mathcal R_u.
\]

All three coefficients are explicitly defined in [A115CofactorReducedCore.lean](../../formal/lean/PrecategoryFormal/A115CofactorReducedCore.lean). In particular the u^0 and u^1 coefficients cancel without imposing a sign assumption, and beta-channel and cubic-u terms remain visible.

## Independent arithmetic test

I constructed the cofactor twice, at k and k+1, with the correct shifts q->q+x, K->beta K, W->sW, T->tau T. A SymPy polynomial expansion of the difference between the two sides returned **exact zero** (no tolerances). The test included all 11 symbolic variables x,q,u,beta,s,tau,K,W,T,U,V.

This does **not** prove any asymptotic remainder bound. To obtain the desired uniform O(M^-3) statement from the original finite-M expression, independent obligations remain:

1. Reinsert the finite terms beta^M, s^M and tau^M, preserve their exact coefficients, and bound them after normalization.
2. Derive U and V from the original central Q equations; prove the central denominator is positive with a uniform lower bound.
3. Bound u, K and their coefficients by one geometric envelope, uniformly over the declared parameter box, integer deficit range and parity.
4. Analyze the real x->0 extension of the ratio (1+2alpha x)^(-1/(2x)+sigma) with one uniform third-order Taylor bound.
5. Compare the first two Taylor coefficients with the **independently derived** Lambda and Xi; do not infer coefficient correctness from A119 positivity.
6. Combine the bounds into one C and M0 valid throughout the frozen box.

The previously submitted [A119CriticalSubstitutionIdentity.lean](../../formal/lean/PrecategoryFormal/A119CriticalSubstitutionIdentity.lean) had a failed CI build [42910102041](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42910102041) because the two explicit `ring` tactics ran after `simp` had already discharged each goal. This commit removes only those redundant tactics, without changing the theorem statement or assumptions. The failed CI run remains part of the record.

New Lean acceptance requires a completed build **and** the corresponding individual `leanchecker` module job at the exact committing SHA. The original source-to-uniform-remainder and full A119 physical/global claims remain open.
