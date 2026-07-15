# A13 — Analytic Interval-Abundance Signature

## Design

- No trained classifier.
- Prospective sizes: [96, 128, 160].
- Exact fixed-cardinality 2D interval-abundance expectation.
- Squared Hellinger discrepancy with empirical same-n Minkowski calibration.
- Matched transitive-percolation, three-layer, and low-m adversarial nulls.
- Cover-deletion perturbations at 10%, 20%, and 30%.

## Results by size

### n = 96

- Minkowski acceptance: 0.9875
- Transitive-percolation rejection: 0.8875
- Three-layer rejection: 1.0000
- Adversarial rejection: 0.8333
- Maximum ordering-fraction mismatch: 0.004825
- Adversarial low-m error reduction: 0.1500
- Perturbation rejection rates: {'0.0': 0.050000000000000044, '0.1': 0.30000000000000004, '0.2': 0.8666666666666667, '0.3': 1.0}

### n = 128

- Minkowski acceptance: 0.9625
- Transitive-percolation rejection: 0.9875
- Three-layer rejection: 1.0000
- Adversarial rejection: 1.0000
- Maximum ordering-fraction mismatch: 0.004183
- Adversarial low-m error reduction: 0.1833
- Perturbation rejection rates: {'0.0': 0.01666666666666672, '0.1': 0.33333333333333337, '0.2': 0.9166666666666666, '0.3': 1.0}

### n = 160

- Minkowski acceptance: 0.9625
- Transitive-percolation rejection: 1.0000
- Three-layer rejection: 1.0000
- Adversarial rejection: 1.0000
- Maximum ordering-fraction mismatch: 0.004717
- Adversarial low-m error reduction: 0.1339
- Perturbation rejection rates: {'0.0': 0.08333333333333337, '0.1': 0.44999999999999996, '0.2': 0.95, '0.3': 1.0}

## Gates

- G1_exact_formula_normalization: PASS
- G2_monte_carlo_formula_validation: PASS
- G3_minkowski_holdout_acceptance_ge_0_90: PASS
- G4_transitive_percolation_rejection_ge_0_90: FAIL
- G5_three_layer_rejection_ge_0_90: PASS
- G6_adversarial_rejection_ge_0_80: PASS
- G7_adversarial_low_m_matching_and_density_control: FAIL
- G8_perturbation_response: PASS
- G9_no_trained_classifier: PASS

## Verdict

FAIL_ANALYTIC_INTERVAL_SIGNATURE

## Boundary

This is a necessary-signature test against specified finite null families, not a proof of sufficient manifoldlikeness or a derivation of physical spacetime.