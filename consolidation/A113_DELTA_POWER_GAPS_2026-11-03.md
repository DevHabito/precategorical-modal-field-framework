# A113 Delta: uniform power-difference sublemmas

**Research author:** Felipe Gianini Romero  
**Date:** 2026-11-03  
**Initial status:** proposed Lean source awaiting an exact-head CI result.

The first delta-preliminaries module proves that, under `M>=521`, `0<=r<=1/6`, and `h=floor(M/2)`, the half-index power obeys `r^h<=U/10^6`. I now need more than a pointwise small-power bound: the central Delta calculation uses **differences** `s^n-beta^n` divided by `U`, and they must retain their sign.

The new `A113DeltaPowerGaps.lean` candidate uses `beta=1/8<s`, monotonicity of nonnegative powers, and the algebraic identity `M=h+(M-h)`. Because `s<=1/6<1`, powers at `M` and at `h+1` are bounded above by the same half-index cap. This gives, at each of `n=h,h+1,M`,

    0 <= (s^n-beta^n)/U <= 1/1000000.

These are **universally quantified statements** over every integer `M>=521` and every real source in `[129/1000,133/1000]` if Lean accepts the proofs. No finite-source grid is substituted for the quantifiers. The statements do **not** establish the final Delta inequalities or any physics claim.

I am testing the proofs with the pinned Lean 4.33.1 library, transitive axiom inspection and the full now-32-module checker matrix. Until those steps pass, this is a reproducible proof candidate rather than a certified theorem. Failure diagnostics will be preserved rather than worked around with extra hypotheses.

With these estimates, the scalar budget already audited in `A113_DELTA_ERROR_BUDGET_2026-11-03.md` has strict exact rational margins for both parities. Remaining work: prove the normalized even/odd source identities from the actual H definitions, derive the coefficient sign bounds, and combine these estimates in Lean into the final interval without assuming Delta.
