# A29 — Contextual Normalization and Refinement

## Main result

Naive unit-mass alternatives are clone-sensitive. A positive additive base mass restores exact refinement consistency for both raw and context-normalized exponential kernels.

## Refinement results

### unweighted_raw
- Consistency rate: 0.000000
- Median macro TV: 0.171351
- Maximum macro error: 0.420204

### unweighted_z
- Consistency rate: 0.000000
- Median macro TV: 0.130071
- Maximum macro error: 0.434967

### weighted_raw
- Consistency rate: 1.000000
- Median macro TV: 0.000000
- Maximum macro error: 3.33067e-16

### weighted_z
- Consistency rate: 1.000000
- Median macro TV: 0.000000
- Maximum macro error: 4.44089e-16

## Gates

- G1_additive_base_measure_refinement_theorem_proved: PASS
- G2_naive_raw_cloning_inconsistent: PASS
- G3_naive_zscore_cloning_inconsistent: PASS
- G4_weighted_raw_exactly_refinement_consistent: PASS
- G5_weighted_zscore_exactly_refinement_consistent: PASS
- G6_near_zero_mass_alternative_becomes_irrelevant: FAIL
- G7_unweighted_zscore_extreme_limit_matches_theory: PASS
- G8_extreme_unweighted_zscore_collapses_old_odds: PASS
- G9_iid_context_has_large_degree_limit: PASS
- G10_refinement_consistency_requires_measure_like_data_within_factorized_class: PASS
- G11_no_physical_volume_measure_claimed: PASS

## Verdict

FAIL_CONTEXTUAL_REFINEMENT_AUDIT

## Boundary

The base mass is mathematical bookkeeping required for exact refinement consistency within the audited factorized class. It is not identified with spacetime volume, probability mass, matter density, or counting measure without an independent operational argument.