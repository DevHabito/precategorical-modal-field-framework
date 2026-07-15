# A36.1 — Corrective CLT Audit

## Main result

The original KS gate remains recorded as failed. The corrected characteristic-function diagnostic passes without lowering that threshold.

## Results

### laplace
- Error n=1: 0.203632185723
- Error n=128: 0.00210912096588
- Error n=2048: 0.000132141851575
- Reduction factor: 1541.012

### rademacher
- Error n=1: 1.00746482401
- Error n=128: 0.00141416413351
- Error n=2048: 8.81261206802e-05
- Reduction factor: 11432.080

### uniform
- Error n=1: 0.260529806921
- Error n=128: 0.000848246531204
- Error n=2048: 5.28746892267e-05
- Reduction factor: 4927.307

## Gates

- G1_original_ks_threshold_not_lowered: PASS
- G2_lattice_finite_size_issue_explicitly_identified: PASS
- G3_characteristic_function_is_valid_clt_convergence_diagnostic: PASS
- G4_rademacher_compact_cf_converges: PASS
- G5_laplace_compact_cf_converges: PASS
- G6_uniform_compact_cf_converges: PASS
- G7_compact_cf_errors_monotonically_decrease: PASS
- G8_clt_remains_conditional_on_iid_finite_variance_assumptions: PASS
- G9_original_a36_failure_preserved_in_record: PASS
- G10_no_gaussian_rzs_noise_claimed: PASS

## Verdict

PASS_CORRECTED_CLT_DIAGNOSTIC_GAUSSIAN_SELECTION_REMAINS_CONDITIONAL

## Boundary

The corrected result supports the conditional CLT statement only. It does not turn centered RZS noise into Gaussian noise.