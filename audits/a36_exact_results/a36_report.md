# A36 — Gaussian Noise Selection

## Main result

Gaussian noise is selected only by strong additional axiom packages. The current centered-noise contract does not select it.

## CLT controls

### laplace
- Initial excess: 2.974752
- Final excess: 0.033299
- Initial KS: 0.062693
- Final KS: 0.004020

### rademacher
- Initial excess: -1.999994
- Final excess: -0.005721
- Initial KS: 0.341945
- Final KS: 0.036891

### uniform
- Initial excess: -1.206353
- Final excess: 0.001772
- Initial KS: 0.059134
- Final KS: 0.004935

## Gates

- G1_fixed_variance_maximum_entropy_selects_gaussian: PASS
- G2_entropy_selection_depends_on_constraints: PASS
- G3_exact_finite_variance_sqrt_sum_stability_selects_gaussian: PASS
- G4_cauchy_exact_nongaussian_stable_without_finite_variance: PASS
- G5_iid_finite_variance_block_sums_gaussianize: FAIL
- G6_perfect_dependence_blocks_clt: PASS
- G7_rotational_invariance_alone_nonselective: PASS
- G8_independence_alone_nonselective: PASS
- G9_rotational_invariance_plus_independence_selection_theorem_stated: PASS
- G10_infinite_divisibility_nonselective: PASS
- G11_projective_rotational_scale_mixture_nonselective: PASS
- G12_current_rzs_centering_and_amplitude_do_not_imply_gaussianity: PASS
- G13_no_physical_noise_law_claimed: PASS

## Verdict

FAIL_GAUSSIAN_NOISE_SELECTION_AUDIT

## Boundary

A36 identifies sufficient principles and counterexamples. It does not establish that RZS innovations satisfy independence, exact stability, Maxwell symmetry, or a physical entropy constraint.