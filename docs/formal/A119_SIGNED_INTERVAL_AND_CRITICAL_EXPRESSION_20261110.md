# A119 — signed interval arithmetic and exact critical-expression anchors

*10 November 2026. Working branch: research/a115-a119-uniform-remainder-20261110.*

## Problem and scope

The preceding [35-box certificate](../research/A119_COMPACT_35_BOX_CERTIFICATE_20261110.md) evaluates a project-specific rational function of (s, alpha, parity, r) using Python Fraction interval arithmetic. Its 35 positive lower bounds do not constitute a Lean-verified mathematical certificate until the interpreter/evaluation algorithm is itself connected to a formally proved inclusion property.

This checkpoint develops two separate Lean components: sound interval operations and a literal rational definition of the A119 critical-substitution expression. It **does not claim** to have made the connection between them yet. These results concern the reduced C2(k) comparison factor, not the unrestricted F2/F3 optimum and not a physical pregeometry claim.

## Added formal modules

1. [A119IntervalArithmetic.lean](../../formal/lean/PrecategoryFormal/A119IntervalArithmetic.lean) proves:
   - a signed multiplier maps a closed rational interval between the two endpoint products;
   - any product x*y of two closed rational intervals lies between the minimum and maximum of **all four** endpoint products;
   - for 0<c<=y<=d and for c<=y<=d<0, the reciprocal is contained in [1/d,1/c];
   - composition with four-corner multiplication bounds x/y whenever the divisor interval does not cross or touch zero.

   The last hypothesis is mathematical, not optional. Evaluating an interval division across zero with finite endpoints would be unsound.

2. [A119CriticalExpression.lean](../../formal/lean/PrecategoryFormal/A119CriticalExpression.lean) defines the A118/A119 critical substituted rational function \`criticalXiHat\` with explicit parity and contact deficit. It checks two exact rational anchors, independently computed beforehand with Python Fraction:
   - even, s=129/1000, alpha=8, r=4:
     51866142966881744/24790160053359375, strictly positive;
   - odd, s=129/1000, alpha=9, r=4:
     2429919448126013663457/1560406595032373046875, strictly positive.

   These are rational **formula-validation anchors**. They do not necessarily satisfy the actual critical equation Lambda=0 and cannot establish positivity on a rectangle or for all parameters.

The original A119 35-box Python checker, A119 6400-box checker, and frozen branch contracts are unchanged.

## Recorded Lean failure and correction

Initial GitHub Actions runs [42870562164](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42870562164) and [42870571151](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42870571151) failed in the new interval module at its last \`division_enclosure\` proof line. The mathematical goals were equivalent, but the simplifier left a term \`x * (1 * y⁻¹)\` while the goal expected \`x * y⁻¹\`. The kernel correctly rejected the mismatch.

The fix was surgical: add \`one_mul\` to the explicit simplification list. The corrected source commit is \`5e82e49f272be7def63944dade38c23977c3beae\`. No statement or mathematical hypothesis was weakened. These failures remain part of the audit record rather than being erased.

## Exact acceptance boundaries

A **successful build** is evidence that Lean elaborated the statements and constructed proofs. Only after the dedicated individual \`leanchecker\` module jobs finish successfully should these additions be labeled kernel-replayed. Check [the corrected CI run 42871107534](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42871107534) and its job records for final status.

These new lemmas are *building blocks*, not the full A119 proof. Remaining obligations:

1. Implement a rational-interval evaluator for \`criticalXiHat\` using precisely the already proved signed addition/subtraction, four-corner multiplication, reciprocal and division rules.
2. Prove by compositional induction that its output contains \`criticalXiHat(s,alpha,parity,r)\` whenever s and alpha lie in its input boxes, and that all division denominators are separated from zero on the relevant boxes.
3. Run **all 35** exact rational lower-bound calculations in Lean, with explicit endpoint coverage and strict lower positivity. Record any performance/normalization issues; never replace a failed rational enclosure with floating-point tolerance.
4. Formally identify the rational function with the A118 coefficient under the A117 critical substitution. Do not merely give two definitions the same name.
5. Join this with the A117 high-deficit exclusion and the A115–A118 source-to-coefficient derivation. Even success on all previous gates does not establish full F3 optimality.

## Originality and attribution

Signed four-corner multiplication, inversion of sign-separated intervals, and interval arithmetic are classical. Formalizing them for this certificate is a reproducibility step, **not** an original mathematical discovery. The possible research contribution is the model-specific reduced collision and parity classification; its priority remains unverified. No source in the literature bibliography was established as an exact duplicate in this checkpoint, but this does not certify novelty.

*Build and replay status must be updated with direct CI evidence before any final PASS statement.*
