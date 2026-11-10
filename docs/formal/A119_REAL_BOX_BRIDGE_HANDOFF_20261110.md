# A119: from 35 rational certificates to a real-parameter statement

**Research checkpoint:** 10 November 2026  
**Working branch:** \`research/a115-a119-uniform-remainder-20261110\`  
**Scope:** the **explicit** reduced C2(k) rational critical function \(\widehat\Xi\), not unrestricted F2/F3 optimality.  
**Evidence status:** exact rational interval program kernel verified; real interval semantics and exact formula correspondence kernel checked; an explicit 35-corollary real module has compiled but its individual checker must be inspected before calling that module completed.

## Verified mathematical steps

1. **All 35 exact rational box evaluations.** The [Lean CI run 42887340405](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42887340405), commit \`e5031677683c7d51625c9359b63ac4a96bcfca5d\`, passed **39/39** jobs. The certificate is fail-closed on division intervals crossing zero and uses \`decide +kernel\`, not \`native_decide\`. See [A119_35BOX_KERNEL_VERIFIED_CHECKPOINT_20261110.md](A119_35BOX_KERNEL_VERIFIED_CHECKPOINT_20261110.md).
2. **The same interval arithmetic is sound for real inputs.** [A119RealIntervalCore.lean](../../formal/lean/PrecategoryFormal/A119RealIntervalCore.lean) proves signed four-corner multiplication, rational-endpoint addition/subtraction and denominator-separated division against **real** point values. [Lean CI 42889935585](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42889935585) finished **40/40 SUCCESS**, including the relevant core module's individual \`leanchecker\`.
3. **Structural expression-tree real semantics.** [A119RealIntervalEvaluator.lean](../../formal/lean/PrecategoryFormal/A119RealIntervalEvaluator.lean) proves by structural induction that any successful *rational-endpoint* interval evaluation contains the expression value for **every real input** inside its input boxes. Its individual \`leanchecker\` in [run 42891589181](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42891589181) succeeded.
4. **Critical formula identity and positivity.** [A119RealCritical.lean](../../formal/lean/PrecategoryFormal/A119RealCritical.lean) proves an exact identity between the real interpretation of the already verified expression tree and a separate real-valued \`criticalXiHatReal\`. The theorem \`certified_box_sound_real\` derives strict positivity at **every real point** in a box whenever its pre-existing rational Boolean interval check passed. This module's individual \`leanchecker\` in run **42891589181** succeeded.

These results establish a sound **formal implication** from any one of the 35 pre-verified exact rational box calculations to its corresponding real-parameter inequality. They do not require continuity/density inference and do not import a floating-point or precomputed positive bound as an axiom. All strict lower endpoints are rational; coercion to \(\mathbb R\) preserves their signs.

## Explicit real corollary replay

The new [A119Real35Boxes.lean](../../formal/lean/PrecategoryFormal/A119Real35Boxes.lean) lists **35** named theorems, one per checked rectangle. Each directly applies \`certified_box_sound_real\` and the specific earlier **kernel-replayed** rational box Boolean theorem. Its source SHA \`dbed0f60592307dc0eb75fd21bb72d8b77b3f401\` has a successful Lean project build in [workflow 42891947892](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42891947892).

**At the time this checkpoint was written, the individual \`leanchecker (PrecategoryFormal.A119Real35Boxes)\` job in that run had not yet finished.** Do not report \`A119Real35Boxes\` as independently kernel-replayed until the exact job reports SUCCESS. The general theorem that justifies it has already passed its own checker.

## Exact failure ledger

- Initial real expression-tree module failed because real division is noncomputable and the exponent-zero simplification did not unfold the specific singleton definition. Corrected by \`noncomputable def\` and an explicit unfolding; mathematical bounds unchanged.
- The first real critical module initially failed because a previously verified r=4 Boolean lemma was not imported. Corrected by an explicit import. No mathematical hypothesis was weakened.
- All these failures remain visible in GitHub Actions source history; none constitutes a counterexample to the real inequality.

## Remaining scientific gates

1. Confirm the 35 named real corollaries by the **individual** Leanchecker job at the exact source SHA.
2. Prove a **single finite-manifest coverage theorem** in Lean quantifying over the 25 eligible parity/deficit cases and all real alpha coordinates. Individual closed-box theorems and the existing arithmetic split lemmas are in place; the final source-level case union must be checked.
3. Prove the identification of the rational critical function with the **A118 second-order asymptotic coefficient** under the A117 critical equation; the current AST-to-rational-function identity is not that result.
4. Kernel-formalize the A115–A118 source/cofactor algebra and the uniform \(O(M^{-3})\) remainder, including its boundary assumptions and high-deficit exclusions.
5. Evaluate full-text neighboring mathematical theorems for historical priority. **No novelty conclusion has been established.**

The latest results are **substantial formal evidence for a restricted critical sign lemma**. They do not justify claiming a full A119 independent-paper theorem, a universal LP support theorem, or a physical pregeometry law.
