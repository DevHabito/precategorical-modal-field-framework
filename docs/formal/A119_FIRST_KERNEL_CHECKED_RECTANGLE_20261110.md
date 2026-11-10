# A119: first kernel-checked whole-rectangle certificate

**Date:** 2026-11-10
**Branch:** `research/a115-a119-uniform-remainder-20261110`
**Scope:** exact rational A119 critical-substitution expression on C2(k), **not** global F2/F3 optimality.

## Result verified in the Lean kernel

The theorem `even_r4_upper_half_passes` in [A119BoxReplay.lean](../../formal/lean/PrecategoryFormal/A119BoxReplay.lean) proves the **actual Boolean interval computation**, not merely positivity of a constant taken from Python.

- Parity: even.
- Deficit: r=4.
- Rational source coordinate: `129/1000 <= s <= 133/1000`.
- Rational collision coordinate: `37/4 <= alpha <= 21/2`, i.e. the upper half of the enlarged r=4 alpha interval.
- Conclusion: `criticalXiHat s alpha false 4 > 0` for every **rational** point in that closed rectangle.

The proof passes by `decide +kernel`. The independently proved `intervalValue_sound` theorem covers all rational points in the input rectangle; the separate `xiExpr_matches_critical` identifies the expression tree with the project's explicit Xi-hat rational formula. The whole-box proof does **not** postulate the expected interval lower bound as a premise.

**Clean verification:** [Lean run 42875647665](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42875647665), source commit `d5fc8ca09f7c9a1f0e67d871399f743953db9982`, finished **30/30 SUCCESS**, including the individual `leanchecker (PrecategoryFormal.A119BoxReplay)` job `130039811326`.

This is the first of the 35 boxes whose complete interval evaluation has been replayed in Lean. The Python Fraction checker still separately certifies **35/35**; it must not be described as 35/35 Lean.

## Attempt history and trust boundary

- [Run 42875122400](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42875122400) **failed**: plain `decide` did not reduce the large rational instance to `isTrue` or `isFalse`. That is a reduction failure, not evidence that the proposition is false.
- `decide +kernel` solved the same proposition, with no changed math assumptions, no native evaluation axiom, no `sorry`, and no `admit`.
- The official Lean 4 tactic reference documents `decide +kernel` as kernel reduction, whereas `decide +native` uses the native compiler and adds compiler trust: https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference

A second odd-parity r=4 upper-half theorem was then submitted in the same file, but **must not be labeled passed until its corresponding CI build and individual module replay succeed**.

## What remains unproved

1. Kernel-evaluate the **other 34 rectangles** (or 33 if the odd case succeeds) with reproducible rational calculations; preserve exact failures and avoid trust-expanding tactics.
2. Formalize the full finite 35-box manifest and prove its union covers each enlarged critical rectangle in the sense used by A117.
3. Distinguish `ℚ` from `ℝ`. The current fully checked theorem quantifies **rational** points. A real-valued conclusion requires a justified rational-to-real transport, using the known continuous rational function on domains where every denominator stays nonzero and a uniform strict positivity margin. Density alone plus strict positivity on rationals would prove at most nonnegativity at a real accumulation point if a uniform margin were missing.
4. Independently formalize `Xi_hat = Xi_p` under the A117 critical equation, and the A115–A118 asymptotic remainder. The kernel-checked AST-to-`criticalXiHat` identity is a different and strictly narrower claim.
5. Validate A119's high-deficit exclusion and the external prior-art comparison before calling the whole theorem novel or publication-ready.

**Editorial verdict:** meaningful machine-checked progress on the reduced critical expression, not yet a fully machine-checked mathematical A119 theorem and not a physical interpretation.
