# A38 — RZS Coarse-Graining Audit

## Main result

Coarse-graining is observable-relative. The exponential score is exact for the exponential kernel, while dynamic graph aggregation additionally requires source occupancy or flow.

## Scalar associativity

### exponential_mean
- Pass rate: 1.000000
- Median error: 1.11022302463e-16

### minimum
- Pass rate: 1.000000
- Median error: 0

### weighted_arithmetic
- Pass rate: 1.000000
- Median error: 3.46944695195e-17

### weighted_median
- Pass rate: 0.391600
- Median error: 0.0782990066999

## Gates

- G1_translation_covariant_quasi_arithmetic_classification_stated: PASS
- G2_weighted_arithmetic_associative_refinement_consistent_and_gauge_covariant: PASS
- G3_exponential_mean_associative_refinement_consistent_and_gauge_covariant: PASS
- G4_weighted_median_not_closed_by_mass_and_median_message: FAIL
- G5_minimum_is_associative_but_mass_insensitive_extremal_control: PASS
- G6_unweighted_mean_is_clone_sensitive_under_mass_preserving_refinement: PASS
- G7_rms_fails_additive_gauge_covariance: PASS
- G8_exponential_mean_exactly_preserves_exponential_kernel: PASS
- G9_arithmetic_mean_does_not_preserve_exponential_kernel: PASS
- G10_nested_graph_partition_sum_aggregation_exact: PASS
- G11_macro_transition_depends_on_source_occupancy: PASS
- G12_supplied_occupancy_flow_aggregation_exact: PASS
- G13_coarse_graining_declared_observable_relative_not_unique: PASS
- G14_no_physical_lambda_or_source_occupancy_claimed: PASS

## Verdict

FAIL_RZS_COARSE_GRAINING_AUDIT

## Boundary

A38 determines consistency requirements relative to declared observables. It does not establish the physical exponential kernel, a physical lambda, a unique regional partition, or the occupancy measure required by dynamic coarse-graining.