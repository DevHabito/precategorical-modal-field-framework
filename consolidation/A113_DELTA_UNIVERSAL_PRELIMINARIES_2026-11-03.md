# A113 Delta proof: stronger preliminaries

**Research author:** Felipe Gianini Romero  
**Date:** 2026-11-03  
**Status:** new Lean module submitted for pinned build, axiom audit, and 31-module replay; **not pre-certified**.

## Reconstructed gap and existing limitation

The exact A113 finite-channel formulas give

`H_source(s) - H_beta(1/8) = (s^M-(1/8)^M)/2 - (D(s)-D(1/8)) - 4 epsilon_M`.

The existing bounds `d>=3/4` and `s^h<=U/128` are too weak to establish the narrow universal normalized gap interval

`43/10000 < (H_source-H_beta)/U < 7/500`.

The lower margin of the simple odd-parity leading expression is only `1/10000` at `s=129/1000`. I therefore do not combine loose absolute-value estimates and claim a uniform sign.

## Exact new sublemmas

The review module `formal/lean/PrecategoryFormal/A113DeltaPreliminaries.lean` proposes, solely from the frozen definitions:

1. For every integer M>=521, `d_M >= 999/1000`, where `d_M=1-(h+1)2^(-h)`, `h=floor(M/2)`. This is proved using monotone dyadic correction starting at exponent 15. The declared base check is exact integer/rational arithmetic, not float.
2. For every natural exponent n>=14 and real `0<=r<=1/6`, `r^n <= (1/2)^n / 1000000`. The base case is the exact inequality `3^14 >= 1000000` and the remainder is induction.
3. Consequently `r^h <= U_M/1000000` for the entire source/beta node domain.
4. The historical source/beta channel gap is exactly decomposed into a full-power difference, a parity-dependent defect difference, and a **negative** four-epsilon correction. No parity sign convention is changed.

These estimates are sufficient ingredients for strictly controlling the residual terms without approximating them away. The actual desired Delta inequality is **not** a theorem in the new module. The proof still needs a full-power estimate, one-sided residual envelopes, and separate even/odd strict comparison arithmetic.

## Current acceptance gates

The CI workflow now checks the **31 existing and proposed modules**, runs `AssuranceA113DeltaPreliminaries.lean`, prints transitive axioms, and invokes `leanchecker`. The code uses no `sorry`, `admit`, or `native_decide` in the proposed declarations.

The module is new. Until the new exact-head workflow has completed, I call these results *proposed lemmas*, not kernel-verified results. Any failure must be retained and fixed without changing the mathematical contract.

## Existing context and open literature limits

The older A113 small-left and central algebraic bridge results were verified separately on 2026-11-03; their exact run IDs and axioms are documented in `consolidation/A113_SMALL_LEFT_LEAN_VERIFICATION_2026-11-03.md` and `consolidation/A113_CENTRAL_PAIR_LEAN_VERIFICATION_2026-11-03.md`.

The historic A113 certificate has passed exact computational checks, but a theorem-level all-tail bridge and general physical interpretation remain open. The bibliography cited in `consolidation/C3_A110_A114_ADVERSARIAL_CHECKPOINT_2026-10-19.md` (including S. Karlin and W. J. Studden, 1966) describes existing Tchebycheff and moment-space methods; this checkpoint makes no originality claim.
