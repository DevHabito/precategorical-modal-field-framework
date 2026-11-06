# A115 finite central reconstruction and Lean 4 validation status

**Date:** 2026-11-06  
**Scope:** only the target-deformed three-site Q block and associated finite algebra; NOT the entire A115–A122 theorem chain.  
**Branch:** `formal/a115-a122-critical-audit-20261106`.

## 1. Confirmed Lean checks

GitHub Actions run [42302765344](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42302765344) completed **successfully**, including the four initial auxiliary lemmas in `TargetDeformationAudit.lean`, the full project build, and the pre-existing 15-module Leanchecker matrix. The new module was compiled but was not among those 15 individual kernel-replay targets.

GitHub Actions run [42304186498](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42304186498) completed **successfully** after adding:
- even/odd central mean equations in cross-multiplied form;
- even/odd central target equations in cross-multiplied form;
- an algebraic exponential basis difference.

The subsequent changes additionally introduce:
- the finite geometric-sum identity for the central denominator;
- a version of the exponential basis difference with `M : Nat` and `r ^ M`, maintaining the original discrete exponent type;
- a dedicated Leanchecker matrix entry for `PrecategoryFormal.TargetDeformationAudit`.

The last set was submitted as GitHub Actions run [42304567864](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42304567864). **The Lean build stage completed SUCCESSFULLY** for this commit. Individual Leanchecker replay of the new module was still queued at the latest observation; do not claim its completion until the corresponding job reports success.

## 2. New independent exact finite reconstruction

The checked-in file `audits/a115_independent_central_reconstruction_20261106.py` was executed in the available Python environment.

For each integer `M=4,...,104`, target `tau in {1/7,1/3,1/2,4/5,9/10}`, and `t in {0,2/7,1}`, it reconstructs `q_1,q_h,q_(h+1)` by the A115 even/odd formula, then checks *all three* normalization/mean/target equations using exact `fractions.Fraction` equality. This gives **1,515** exact controls (101 support sizes, 5 targets, 3 values of t).

For the 505 pairs `(M,tau)`, it checks exactly:

```
D_tau = tau - h*tau^h + (h-1)*tau^(h+1)
      = tau*(1-tau)^2 * sum((j+1)*tau^j, j=0,...,h-2)
      > 0.
```

For each `(M,tau)` and source `r in {1/8,129/1000,131/1000,133/1000}`, it independently obtains the slope in `t` from the direct three-coordinate system (`t=0` and `t=1`) and compares it exactly with A115's stated `D_r` expression: **2,020** exact comparisons.

**Observed execution output:**
```
PASS: 1515 exact central-system controls; 505 exact denominator identities; 2020 exact D_r slope checks
```

The `t=0` case is used only as an algebraic interpolation probe; it is not presumed to yield a feasible physical or probabilistic solution. No claim that all three weights are nonnegative for these choices is made.

These finite checks independently support the formulas. They are **not a proof for arbitrary M/tau/t**.

## 3. Main mathematical observation

For `h>=2` and `0<tau<1`, every factor in the finite sum representation of `D_tau` is positive, so `D_tau>0` follows without derivatives. The equality is an elementary finite geometric-sum identity, not a novel theorem, and it removes a denominator-singularity concern for the central algebra.

## 4. Important open gates

- Prove the full A115 cofactor/ten-term factor identity **from** the original LP constraints, not just the isolated Q block.
- Check that the solution `q` is nonnegative under precisely the feasibility assumptions used later; a solution of the equalities need not be LP-feasible.
- Finish Lean 4 kernel replay on the new module after the extended CI passes.
- Rebuild the A118 second-order coefficient independently before claiming Lean verification of A119.
- Keep novelty status **NOT CERTIFIED** until comparison with prior art and independent mathematical review.

**Conservative conclusion:** substantial exact and Lean-compiled evidence for the A115 central algebra, not full A115–A122 formal certification.
