# A22 — Minimal Primitive Admissibility Audit

## Exact classification

Order-derived, independent, rank-based, and covariantly recalibrated marks remained invariant. A fixed calibrated binary threshold broke the equivalence.

## Theoretical probabilities

- uniform: 0.500000000000
- power_anisotropic: 0.159103584746
- beta_skew: 0.109375000000

## Binary separation

### n=32: uniform vs power_anisotropic
- Single-bit total variation: 0.340896
- Clean exact balanced accuracy: 0.983485
- Noisy exact balanced accuracy: 0.919948

### n=32: uniform vs beta_skew
- Single-bit total variation: 0.390625
- Clean exact balanced accuracy: 0.995252
- Noisy exact balanced accuracy: 0.951617

### n=64: uniform vs power_anisotropic
- Single-bit total variation: 0.340896
- Clean exact balanced accuracy: 0.998773
- Noisy exact balanced accuracy: 0.976975

### n=64: uniform vs beta_skew
- Single-bit total variation: 0.390625
- Clean exact balanced accuracy: 0.999882
- Noisy exact balanced accuracy: 0.990286

### n=128: uniform vs power_anisotropic
- Single-bit total variation: 0.340896
- Clean exact balanced accuracy: 0.999991
- Noisy exact balanced accuracy: 0.997652

### n=128: uniform vs beta_skew
- Single-bit total variation: 0.390625
- Clean exact balanced accuracy: 1.000000
- Noisy exact balanced accuracy: 0.999525

### n=256: uniform vs power_anisotropic
- Single-bit total variation: 0.340896
- Clean exact balanced accuracy: 1.000000
- Noisy exact balanced accuracy: 0.999969

### n=256: uniform vs beta_skew
- Single-bit total variation: 0.390625
- Clean exact balanced accuracy: 1.000000
- Noisy exact balanced accuracy: 0.999998

## Gates

- G1_relations_identical_under_monotone_models: PASS
- G2_order_derived_marks_exactly_redundant: PASS
- G3_independent_bits_add_no_model_information: PASS
- G4_rank_marks_exactly_invariant: PASS
- G5_covariantly_moving_threshold_invariant: PASS
- G6_fixed_threshold_really_breaks_identity: PASS
- G7_fixed_threshold_probabilities_match_theory: PASS
- G8_single_binary_mark_has_large_model_tv: PASS
- G9_clean_exact_binary_count_separation: PASS
- G10_known_noise_binary_separation: PASS
- G11_simulation_matches_exact_binomial_results: PASS
- G12_binary_alphabet_minimality_proved: PASS
- G13_no_physical_primitive_claimed: PASS

## Verdict

PASS_MINIMAL_PRIMITIVE_ADMISSIBILITY_AUDIT

## Boundary

The fixed threshold X>1/2 is intentionally only a witness. It assumes a shared numerical coordinate scale and therefore cannot be promoted to a physical primitive without an independent operational definition inside the theory.