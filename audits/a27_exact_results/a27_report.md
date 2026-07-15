# A27 — Lambda Status Audit

## Main result

Lambda is removable against an uncalibrated raw score, but becomes an identifiable model parameter after local score standardization. Neither the current q dynamics nor exact coarse-graining closure selects its value.

## Estimation results

### lambda=0.5
- Mean estimate: 0.499636
- Bias: -0.000364
- RMSE: 0.004009

### lambda=1.0
- Mean estimate: 0.999617
- Bias: -0.000383
- RMSE: 0.004440

### lambda=2.0
- Mean estimate: 2.000985
- Bias: 0.000985
- RMSE: 0.008612

## Gates

- G1_raw_score_lambda_scale_degeneracy_exact: PASS
- G2_standardized_score_affine_invariant: PASS
- G3_distinct_lambda_not_gauge_after_standardization: PASS
- G4_stationary_variance_matches_linear_theory: PASS
- G5_noise_amplitude_cannot_fix_standardized_kernel: PASS
- G6_coarse_graining_closure_holds_for_every_lambda: PASS
- G7_coarse_graining_does_not_select_lambda: PASS
- G8_lambda_statistically_estimable_given_z_and_kernel: PASS
- G9_expected_score_map_strictly_monotone: PASS
- G10_lambda_is_model_parameter_not_current_gauge: PASS
- G11_no_physical_lambda_value_claimed: PASS

## Verdict

PASS_LAMBDA_IDENTIFIABLE_BUT_NOT_DERIVED

## Boundary

A27 does not prove that standardized q is the correct physical score or that lambda is fundamental. Estimability from an assumed kernel is not a derivation of that kernel or of its physical units.