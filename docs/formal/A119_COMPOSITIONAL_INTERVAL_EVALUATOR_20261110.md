# A119 — fail-closed interval expression interpreter and proof bridge

**Date:** 2026-11-10  
**Branch:** research/a115-a119-uniform-remainder-20261110  
**Scope:** the reduced C2(k) A119 substituted rational expression, not full F2/F3 optimality.  
**Evidence:** source audit and GitHub Actions builds; individual verification for this checkpoint must be read from the exact runs below.

## A new proof boundary

The earlier Lean modules verified finite box counts, interval-covering arithmetic, signed four-corner multiplication and reciprocal/division inequalities. But a Python script computing the rational function is not a Lean theorem about that function. Two missing links were:

1. a verified *compositional* interpreter for expressions built from rational constants, source (s), parameter (alpha), addition, subtraction, multiplication, division and natural powers;
2. a proof that the interpreter's source expression is the same (widehat\Xi_{p,r}(s,alpha)) used by the A119 paper.

Both are now addressed in source, separately from the finite box calculations.

## Exact code

- [A119IntervalEvaluator.lean](../../formal/lean/PrecategoryFormal/A119IntervalEvaluator.lean): implements a closed rational interval type, four-corner multiplication, a fail-closed denominator check and recursive evaluation of an expression AST. The theorem `intervalValue_sound` proves by structural induction that when evaluation succeeds, **every rational value inside the input intervals lies in the output interval**. It depends on already kernel-checked local interval lemmas; it is not a restatement of an evaluator output.
- [A119CertifiedExpression.lean](../../formal/lean/PrecategoryFormal/A119CertifiedExpression.lean): constructs A119's critical-substitution rational expression using that AST and states `xiExpr_matches_critical`, a literal equality against the independently defined `criticalXiHat`. The theorem `certified_box_sound` then derives true pointwise positivity from a kernel-verified Boolean certificate for a box, including exact source and alpha endpoint assumptions.

The evaluator returns `none` when a divisor interval touches or straddles zero. A failed enclosure cannot be silently converted to a successful positive result.

## Adversarial failures preserved

- [Run 42873117131](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42873117131): `pow_sound` base case was missing a definitional simplification. No mathematical bound was relaxed. Corrected by unfolding `powI` and `singleton`.
- [Run 42873668922](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42873668922): the Xi expression bridge exposed a local name resembling a constructor, a mathematically equivalent but syntactically regrouped rational formula, and a Boolean condition already simplified into a proposition. The source was adjusted; hypotheses were unchanged.
- [Run 42874079660](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42874079660): the strict Lean style checker rejected an unnecessary `<;>` tactic combinator in the Xi formula proof. The explicit additional `ring` step remains as a separate tactic, not as an assumption.

A subsequent corrected run is [42874445972](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42874445972), source commit `f5c39156c97678ae957b3fa6870526dff9fc8c0f`. **Its conclusion and the two individual module jobs must be checked before describing this checkpoint as Leanchecker PASS.**

## Remaining obligations (ordered)

1. Check Lean kernel replay for `A119IntervalEvaluator` and `A119CertifiedExpression` at a pinned source revision.
2. Implement the **specific 35-box manifest** within Lean, with the correct even (4..12) and odd (4..19) deficit cases and rational subdivisions.
3. Execute and prove `passes odd r t0 t1 = true` for each of the 35 cases in the Lean kernel, not via an opaque native computation or by asserting precomputed lower endpoints.
4. Establish a uniform semantic theorem from the verified manifest and closed-interval cover for each entire critical rectangle. Keep every denominator strict-positivity obligation explicit.
5. Prove the source identity connecting the rational `criticalXiHat` expression to the A115–A118 asymptotic coefficient under the A117 critical equation. The expression match inside Lean is necessary but **not sufficient** for that external derivation.
6. Re-check the analytic high-deficit cutoff and remaining asymptotic error hypotheses before calling A119 a fully proved research theorem.

## Scientific verdict

If the current CI passes, the work delivers a reusable sound interpreter and a verified formula mapping. That is a real formalization advance, but **no full 35-box kernel certificate, unrestricted optimizer theorem, physical prediction or novelty certification** follows without the remaining gates.

All method descriptions and conclusions here are limited to the inspected source and linked CI; failed attempts have not been erased.


## Verified source-to-interval bridge (2026-11-10)

The [Lean CI run 42874445972](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42874445972), at exact commit \`f5c39156c97678ae957b3fa6870526dff9fc8c0f\`, successfully built the project, and the two relevant **individual** kernel checks finished SUCCESS:

- \`leanchecker (PrecategoryFormal.A119IntervalEvaluator)\`: structurally inductive interval evaluator soundness, including fail-closed division.
- \`leanchecker (PrecategoryFormal.A119CertifiedExpression)\`: exact equality of the AST expression to \`criticalXiHat\` and the general box-certification implication.

Other matrix jobs may still be finishing at the time of this addendum; the overall 30-job conclusion must be checked separately. The source-to-expression identity is mathematically distinct from A115-to-A118's derivation of the expression.

A first direct **whole-box** kernel computation was submitted in [A119BoxReplay.lean](../../formal/lean/PrecategoryFormal/A119BoxReplay.lean): even parity, deficit r=4, alpha upper-half interval. This relies on a kernel-evaluated \`passes = true\` rather than an asserted lower endpoint. The attempt's CI must be read independently; **this document does not yet claim the first box passed**.


## Full workflow confirmation and first full-box failure

The complete [Lean workflow 42874445972](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42874445972) has now finished **30/30 SUCCESS** (one project build and 29 individual Leanchecker module jobs), at commit \`f5c39156c97678ae957b3fa6870526dff9fc8c0f\`. The generic compositional evaluator and exact AST-to-Xi-hat formula identity are thus kernel-replayed.

The separate [first-box attempt 42875122400](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42875122400) **FAILED**. The \`decide\` tactic failed to reduce the large rational proposition \`passes false 4 (1/2) 1 = true\` to an \`isTrue\` or \`isFalse\` constructor. It did **not** produce a counterexample or prove the bound false. Its failure is preserved as a reproducibility/automation obstacle.

An alternative \`decide +kernel\` proof is being tested in [run 42875647665](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42875647665). This uses the Lean kernel reducer, rather than \`decide +native\` or \`native_decide\` (which rely on a compiler-related trust assumption). Do not call the first complete box kernel-certified unless that run and the individual module replay actually succeed.


## Latest verified whole-box checkpoint (supersedes the earlier pending status)

Two rational Xi-hat rectangles have now passed the full source-to-box inference with kernel-reduced computations. See [A119_FIRST_KERNEL_CHECKED_RECTANGLE_20261110.md](A119_FIRST_KERNEL_CHECKED_RECTANGLE_20261110.md).

- Even r=4 alpha in [37/4,21/2]: [CI 42875647665](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42875647665), **30/30 success**.
- Odd r=4 alpha in [411/40,231/20]: [CI 42876905479](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42876905479), **30/30 success**.

Both use rational s in [129/1000,133/1000] and kernel \`decide +kernel\` proof terms. Current count: **2/35 Lean-certified rational rectangles**, alongside the independent 35/35 exact Python tests. The distinction between rational and real domains and between the Xi-hat rational formula and the A115–A118 derivation remains mandatory.
