# A35 — Gaussian Closure Audit

## Main result

Gaussian closure is exact only conditional on a Gaussian law and Gaussian affine innovations. Centering alone is not enough.

## Matched-moment nulls

### lambda=0.5
- Initial difference: 0.00472993209957
- Step 1 difference: 0.00225788809448
- Step 10 difference: 2.3655434859e-06
- Step 30 difference: 4.91162666094e-13

### lambda=1.0
- Initial difference: 0.0293818139337
- Step 1 difference: 0.0150717579738
- Step 10 difference: 1.88041055125e-05
- Step 30 difference: 3.92885723954e-12

### lambda=2.0
- Initial difference: 0.115989924879
- Step 1 difference: 0.0695860738266
- Step 10 difference: 0.000146690994212
- Step 30 difference: 3.14300807602e-11

## Gates

- G1_affine_gaussian_family_exactly_closed: PASS
- G2_gaussian_q_exactly_mean_variance_functional: PASS
- G3_same_mean_variance_nongaussian_nulls_differ_at_finite_time: PASS
- G4_gaussian_innovations_asymptotically_erase_higher_moments: PASS
- G5_higher_cumulants_decay_under_gaussian_innovations: PASS
- G6_nongaussian_innovations_generate_nongaussian_stationary_law: PASS
- G7_nongaussian_stationary_q_differs_from_gaussian_closure: PASS
- G8_centering_does_not_gaussianize_rademacher_noise: PASS
- G9_finite_empirical_gaussian_q_converges_with_sample_size: PASS
- G10_finite_sample_error_increases_with_lambda: PASS
- G11_population_closure_distinguished_from_empirical_estimator: PASS
- G12_gaussian_rzs_noise_not_claimed_or_derived: PASS

## Verdict

PASS_GAUSSIAN_CLOSURE_CONDITIONAL_ON_INNOVATION_LAW

## Boundary

A35 establishes conditional probabilistic theorems and controls. It does not show that actual RZS q values are iid, Gaussian, exchangeable, or governed by Gaussian innovations.