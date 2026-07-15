# A37.1 — Corrected Noise-Law Universality

## Main result

Noise-law details survive at the stationary component and operational-kernel levels. Conditional universality appears under independent coarse-graining with exponential-moment control.

## Stationary effective-score spread

### lambda=0.5
- Minimum defined Q: -0.253032889029
- Maximum defined Q: -0.248052842725
- Spread: 0.0049800463043

### lambda=1.0
- Minimum defined Q: -0.525971423532
- Maximum defined Q: -0.485139516558
- Spread: 0.0408319069737

### lambda=2.0
- Minimum defined Q: -1.30624197726
- Maximum defined Q: -0.898810791087
- Spread: 0.407431186173

## Gates

- G1_stationary_characteristic_function_and_cumulant_formula_stated: PASS
- G2_equal_stationary_mean_variance_do_not_fix_higher_cumulants: PASS
- G3_light_tailed_stationary_effective_scores_depend_on_noise_law: PASS
- G4_student_t_finite_variance_does_not_make_q_lambda_finite: PASS
- G5_independent_light_tailed_block_scores_converge_to_gaussian: PASS
- G6_student_t_block_q_remains_undefined_under_finite_block_averaging: PASS
- G7_common_nongaussian_factor_blocks_gaussian_universality: PASS
- G8_standardized_operational_kernel_retains_noise_law_sensitivity: PASS
- G9_variance_matching_and_centering_are_not_exact_universality_principles: PASS
- G10_universality_requires_independence_or_mixing_and_exponential_moment_control: PASS
- G11_no_physical_rzs_noise_law_claimed: PASS

## Verdict

PASS_CORRECTED_PARTIAL_NOISE_UNIVERSALITY_WITH_MOMENT_AND_DEPENDENCE_LIMITS

## Boundary

A37 identifies universality classes in an affine stationary model. It does not prove that RZS relational components are independent copies, that their innovations have exponential moments, or that the audited block sum is the physical coarse-graining operation.