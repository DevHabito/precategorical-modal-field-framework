# A17 — Multiscale Subinterval Self-Similarity Audit

## Design

- Anchored Minkowski reference intervals at [24, 32, 48, 64, 96] elements.
- Minkowski-only local and parent covariance estimation.
- Discovery at n=192 and prospective confirmation at n=256.
- Exact-2D challenges: opposing order regimes, two compact clusters, and four corner clusters.

## Family results

### bimodal_clusters at n=192
- Acceptance: 0.9583
- Rejection: 0.0417
- Median p-value: 0.5270
- Maximum density mismatch: 0.004854

### four_corner_clusters at n=192
- Acceptance: 0.9583
- Rejection: 0.0417
- Median p-value: 0.5270
- Maximum density mismatch: 0.025142

### minkowski_holdout at n=192
- Acceptance: 1.0000
- Rejection: 0.0000
- Median p-value: 0.4730
- Maximum density mismatch: 0.000000

### opposing_diagonal_bands at n=192
- Acceptance: 0.0000
- Rejection: 1.0000
- Median p-value: 0.0270
- Maximum density mismatch: 0.013743

### bimodal_clusters at n=256
- Acceptance: 0.9583
- Rejection: 0.0417
- Median p-value: 0.5270
- Maximum density mismatch: 0.004994

### four_corner_clusters at n=256
- Acceptance: 1.0000
- Rejection: 0.0000
- Median p-value: 0.6486
- Maximum density mismatch: 0.015319

### minkowski_holdout at n=256
- Acceptance: 1.0000
- Rejection: 0.0000
- Median p-value: 0.7027
- Maximum density mismatch: 0.000000

### opposing_diagonal_bands at n=256
- Acceptance: 0.0000
- Rejection: 1.0000
- Median p-value: 0.0270
- Maximum density mismatch: 0.018566

## Gates

- G1_local_reference_covariances_stable: PASS
- G2_parent_covariances_stable: PASS
- G3_minkowski_acceptance_ge_0_90: PASS
- G4_opposing_regime_rejection_ge_0_90: PASS
- G5_bimodal_cluster_rejection_ge_0_80: FAIL
- G6_four_corner_rejection_ge_0_80: FAIL
- G7_density_matching_le_0_02: FAIL
- G8_all_challenges_are_exact_2d_orders: PASS
- G9_no_challenge_used_for_calibration: PASS

## Verdict

FAIL_MULTISCALE_SELF_SIMILARITY

## Boundary

The test addresses self-similarity relative to a uniform anchored 2D Minkowski interval ensemble. It neither proves nor disproves exact causal embeddability, because every challenge family in this audit is explicitly constructed as a 2D product order.