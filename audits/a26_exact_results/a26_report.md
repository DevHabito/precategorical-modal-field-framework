# A26 — Kernel Selection Principles Audit

## Main result

IIA, detailed balance, and aggregation were nonselective. Difference-only odds plus continuity selected the exponential family. Maximum entropy selected the same family conditional on a fixed expected-score constraint. Lambda remained free.

## Functional results

### exp_0_5
- Median shift residual: 5.55112e-17
- Median composition residual: 5.55112e-17

### exp_1
- Median shift residual: 0
- Median composition residual: 5.55112e-17

### exp_2
- Median shift residual: 0
- Median composition residual: 0

### asinh
- Median shift residual: 0.0799252
- Median composition residual: 0.0452603

### logistic
- Median shift residual: 0.0985363
- Median composition residual: 0.0539225

## Gates

- G1_all_pointwise_kernels_satisfy_iia: PASS
- G2_rank_context_control_violates_iia: PASS
- G3_detailed_balance_is_nonselective: PASS
- G4_weight_aggregation_is_nonselective: PASS
- G5_exponential_family_satisfies_difference_and_composition: PASS
- G6_nonexponential_controls_fail_exponential_axioms: PASS
- G7_maximum_entropy_recovers_exponential_solution: PASS
- G8_maximum_entropy_solution_dominates_feasible_perturbations: PASS
- G9_lambda_remains_observationally_nonunique: PASS
- G10_different_constraints_generate_different_lambda: PASS
- G11_exponential_form_not_physical_strength_claimed: PASS
- G12_no_unique_rzs_kernel_claimed: PASS

## Verdict

PASS_EXPONENTIAL_FAMILY_SELECTION_WITH_FREE_STRENGTH

## Boundary

A26 does not establish that transitions in nature obey the difference-only odds axiom, that standardized q is the correct constraint variable, or that any tested lambda is physical. The result narrows the admissible family without deriving a complete RZS law.