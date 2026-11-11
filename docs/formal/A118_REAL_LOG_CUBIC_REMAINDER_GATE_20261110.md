# Kernel-targeted cubic log remainder from an existing Mathlib theorem

**Recorded:** 10 November 2026. **Working branch:** `research/a115-a119-uniform-remainder-20261110`.

The new module `A118LogTaylorRemainder.lean` submits the real-analytic inequality

[
|\log(1+z)-(z-z^2/2+z^3/3)|\le z^4/(1-z)
]

for **every real** 0<=z<=9/100. It instantiates Mathlib's `Real.abs_log_sub_add_sum_range_le` at x=-z and n=3. The finite three-term polynomial is reduced with real ring arithmetic; the exact denominator 1-z remains positive on the declared domain. No floating-point or externally asserted transcendental interval is used.

Mathlib documentation: https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Log/Deriv.html

The new inequality is weaker than the tighter `z^4/4` alternating-series remainder used in the earlier hand-written analysis. **Until the tighter result is also kernel checked, no final Lean proof may cite it as a proved lemma.** If the weaker inequality is used for the final uniform M^-3 result, all intermediate constants must be recomputed with exact rational arithmetic and a new final bound explicitly verified.

**Status:** this is a submitted Lean statement, not a PASS until the full build and its individual leanchecker job succeed. The source-to-A118 first-jet and complete source-to-O(M^-3) claims are separate obligations.


## First CI result and corrective edit

[Lean run 42927105590](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42927105590) initially FAILED because a rewrite had already closed the denominator-identity subgoal, leaving a redundant `norm_num` tactic and a `No goals to be solved` error at line 42. The statement, the appeal to `Real.abs_log_sub_add_sum_range_le`, and all mathematical hypotheses were unchanged. The redundant tactic was removed; a corrected build and individual kernel replay are required before claiming certification.
