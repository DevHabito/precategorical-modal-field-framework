# A113 Delta: conditional exact scalar interval proofs

**Research author:** Felipe Gianini Romero  
**Date:** 2026-11-03  
**Initial status:** new real-arithmetic Lean candidates, not yet compiled.

The exact rational budgets in `A113_DELTA_ERROR_BUDGET_2026-11-03.md` have strictly positive margins for both parities. I translated them into two reusable mathematical implications in `formal/lean/PrecategoryFormal/A113DeltaScalarBudgets.lean`. Their premises expose **all** quantities needed to close the inequality:

- real source `129/1000<=s<=133/1000`;
- real denominator `999/1000<=d<=1`;
- nonnegative normalized full-power term `p<=1/(2*10^6)`;
- nonnegative normalized half and next-half differences `q,r<=1/10^6`;
- nonnegative coefficients `x,y<=1/3` for the parity defects.

The even expression is `2(s-1/8)/d -4/1875 +p -(1+2x)q+2yr`.

The odd expression is `(3/2)(s-1/8)/d-4/2500+p-(1/2+(3/2)x)q-(1/2-(3/2)y)r`.

Each conclusion is exactly the strict interval `(43/10000,7/500)`. The algebraic proofs use positive-denominator comparisons, elementary product bounds and exact rational normalization; there are no fitted constants.

**Assurance boundary:** even a fully checked conditional scalar lemma does not prove the full A113 Delta interval. It remains necessary to set `p,q,r,x,y,d` to the **actual** A113 parity-dependent functions and prove, without assuming the desired Delta conclusion, that every premise holds for all `M>=521` and every real source in the declared interval. The previously proposed `A113DeltaPowerGaps.lean` handles three power-difference premises, but the exact parity identity and final composition are still open. The original central `J>0` also remains open.

The new source is reviewed by the pinned Lean 4.33.1 build, explicit axiom output and the now-33-module `leanchecker` matrix. Any error is recorded rather than bypassed with an additional hypothesis.
