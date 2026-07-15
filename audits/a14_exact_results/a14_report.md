# A14 — Covariance-Aware Analytic Interval Signature

## Design

- No trained discriminative classifier.
- Exact A13 analytic mean profile.
- Minkowski-only Ledoit–Wolf covariance.
- Independent Minkowski calibration and holdout samples.
- Fresh matched ordinary and adversarial nulls.

## Results by size

### n = 96

- Binned dimension: 36
- Minkowski acceptance: 0.9250
- Transitive-percolation rejection: 1.0000
- Three-layer rejection: 1.0000
- Adversarial rejection: 1.0000
- Adversarial low-six error reduction: 0.2318
- Maximum ordering-fraction mismatch: 0.004825
- Perturbation rejection rates: {'0.0': 0.020000000000000018, '0.1': 0.18000000000000005, '0.2': 0.88, '0.3': 1.0}

### n = 128

- Binned dimension: 54
- Minkowski acceptance: 0.9375
- Transitive-percolation rejection: 1.0000
- Three-layer rejection: 1.0000
- Adversarial rejection: 1.0000
- Adversarial low-six error reduction: 0.1605
- Maximum ordering-fraction mismatch: 0.004552
- Perturbation rejection rates: {'0.0': 0.020000000000000018, '0.1': 0.26, '0.2': 0.98, '0.3': 1.0}

### n = 160

- Binned dimension: 72
- Minkowski acceptance: 0.9375
- Transitive-percolation rejection: 1.0000
- Three-layer rejection: 1.0000
- Adversarial rejection: 1.0000
- Adversarial low-six error reduction: 0.1974
- Maximum ordering-fraction mismatch: 0.004717
- Perturbation rejection rates: {'0.0': 0.07999999999999996, '0.1': 0.43999999999999995, '0.2': 1.0, '0.3': 1.0}

## Gates

- G1_covariance_positive_and_conditioned: PASS
- G2_minkowski_holdout_acceptance_ge_0_90: PASS
- G3_transitive_percolation_rejection_ge_0_90: PASS
- G4_three_layer_rejection_ge_0_90: PASS
- G5_adversarial_rejection_ge_0_80: PASS
- G6_adversarial_low_six_matching_and_density: PASS
- G7_perturbation_response: PASS
- G8_no_null_used_for_weights_or_thresholds: PASS
- G9_no_trained_discriminative_classifier: PASS

## Verdict

PASS_COVARIANCE_AWARE_INTERVAL_SIGNATURE

## Boundary

The result is a model-checking statement against specified finite nulls. It is not a proof that the accepted structures possess a physical Lorentzian continuum.