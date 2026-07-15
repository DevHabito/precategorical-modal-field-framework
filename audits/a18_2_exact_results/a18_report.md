# A18.2 — Numerically Robust Exact Order–Measure Identifiability Limit

## Exact construction

For every finite sample and every strictly increasing coordinate-wise transform T_u,T_v, the relation u_i<u_j and v_i<v_j is unchanged bit-for-bit.

## Transform summaries

### n=128, beta_skew_opposed
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.223707
- Median transformed marginal KS: 0.429324
- Median Wasserstein shift: 0.215640

### n=128, power_anisotropic
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.243473
- Median transformed marginal KS: 0.503681
- Median Wasserstein shift: 0.232702

### n=128, power_isotropic_extreme
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.296057
- Median transformed marginal KS: 0.693906
- Median Wasserstein shift: 0.385334

### n=256, beta_skew_opposed
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.290696
- Median transformed marginal KS: 0.421352
- Median Wasserstein shift: 0.216610

### n=256, power_anisotropic
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.311598
- Median transformed marginal KS: 0.492042
- Median Wasserstein shift: 0.234346

### n=256, power_isotropic_extreme
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.402871
- Median transformed marginal KS: 0.678793
- Median Wasserstein shift: 0.388771

### n=512, beta_skew_opposed
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.325224
- Median transformed marginal KS: 0.408578
- Median Wasserstein shift: 0.215908

### n=512, power_anisotropic
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.351467
- Median transformed marginal KS: 0.477056
- Median Wasserstein shift: 0.234205

### n=512, power_isotropic_extreme
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.486349
- Median transformed marginal KS: 0.666176
- Median Wasserstein shift: 0.389564

## Gates

- G1_all_monotone_transform_relations_bitwise_identical: PASS
- G2_all_coordinate_ranks_identical: PASS
- G3_all_relation_hashes_identical: PASS
- G4_interval_abundance_and_interval_sizes_identical: PASS
- G5_coordinate_distributions_strongly_changed: PASS
- G6_pushforward_densities_normalized: PASS
- G7_nonseparable_copula_control_changes_order_statistics: PASS
- G8_same_cardinality_in_every_pair: PASS
- G9_impossibility_follows_from_identical_input: PASS

## Verdict

PASS_EXACT_ORDER_MEASURE_IDENTIFIABILITY_LIMIT_ROBUST

## Logical consequence

No deterministic method using only a single finite relation matrix and its element count can uniquely recover a preferred coordinate sampling density across this monotone-transform equivalence class. Additional physical structure, calibration, repeated sampling, or a distinguished volume assignment is required.

## Boundary

The ambiguity concerns the choice of sampling measure or conformal-volume representative. It does not say that causal structure contains no geometric information, nor does it contradict continuum statements in which causal structure is supplemented by an independently specified local volume element.