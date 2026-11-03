# A113 closure candidate — first failed Lean build and minimal correction

**Research author:** Felipe Gianini Romero  
**Date:** 2026-11-03  
**Experiment branch:** `research/2026-11-03-a113-evidence-ledger`  
**Original code revision:** `10467c77cb54f17e6d797e056c2e307aba55dbd0`

## Observed result — failure, not a certified theorem

The pinned Lean 4.33.1 GitHub Actions run [41714981951](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41714981951) **failed**. The initial checkout, forbidden-placeholder check, and Lean setup succeeded; `lake build` failed in `PrecategoryFormal.A113SmallLeftClosure`. Both the subsequent `#print axioms` step and the module-specific `leanchecker` step were skipped, so they must not be reported as passing.

The job log records the concrete source diagnostic:

```text
error: PrecategoryFormal/A113SmallLeftClosure.lean:198:10: No goals to be solved
```

Inspection of the exact source shows two consecutive tactics for the first equality in the final calculation:

```lean
rw [a113ActualFactor_sub_ideal_eq_namedErrors]
rfl
```

The `rw` tactic closed the goal already, leaving no goal for `rfl`. The minimally justified code correction **removes the redundant `rfl` line and changes nothing else**. It does not change definitions, theorems, hypotheses, constants, target inequalities, or upstream formal modules. This correction addresses the observed tactic-level failure, not mathematical validity or the status of other repository claims.

## Required evidence after correction

1. A new pinned `lake build` must complete at the **new exact revision**.
2. `AssuranceA113SmallLeftClosure.lean` must print the transitive axioms for both new declarations; assess native-computation dependence and `sorryAx` separately.
3. The module-specific `lake env leanchecker PrecategoryFormal.A113SmallLeftClosure` must succeed.
4. The full established Lean module matrix remains a separate regression gate.
5. Independently review the A83/A84 source-definition bridge and preserve the known historical ZIP integrity failures.
6. Refresh the branch's root integrity indexes from the final clean checkout before review/merge; the current branch has modified tracked files.

Even if the corrected build succeeds, neither a global A113 optimization result nor a physical law follows. The first run remains a historical **FAIL** and must never be relabeled as a success.
