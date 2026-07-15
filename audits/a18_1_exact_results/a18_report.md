# A18.1 — Corrective Exact Order–Measure Identifiability Limit

## Exact construction

For every finite sample and every strictly increasing coordinate-wise transform T_u,T_v, the relation u_i<u_j and v_i<v_j is unchanged bit-for-bit.

## Transform summaries

### n=128, beta_extreme_edges
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.254825
- Median transformed marginal KS: 0.300593
- Median Wasserstein shift: 0.148368

### n=128, beta_skew_opposed
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.223845
- Median transformed marginal KS: 0.426977
- Median Wasserstein shift: 0.216633

### n=128, power_anisotropic
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.243917
- Median transformed marginal KS: 0.493026
- Median Wasserstein shift: 0.233737

### n=256, beta_extreme_edges
- Relation identity rate: 0.9667
- Rank identity rate: 0.9667
- Median coordinate JS divergence: 0.335915
- Median transformed marginal KS: 0.285455
- Median Wasserstein shift: 0.149759

### n=256, beta_skew_opposed
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.295076
- Median transformed marginal KS: 0.410795
- Median Wasserstein shift: 0.217444

### n=256, power_anisotropic
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.318743
- Median transformed marginal KS: 0.494619
- Median Wasserstein shift: 0.233945

### n=512, beta_extreme_edges
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.390739
- Median transformed marginal KS: 0.270494
- Median Wasserstein shift: 0.148892

### n=512, beta_skew_opposed
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.326368
- Median transformed marginal KS: 0.406256
- Median Wasserstein shift: 0.214542

### n=512, power_anisotropic
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.350716
- Median transformed marginal KS: 0.482976
- Median Wasserstein shift: 0.232418

## Gates

- G1_all_monotone_transform_relations_bitwise_identical: FAIL
- G2_all_coordinate_ranks_identical: FAIL
- G3_all_relation_hashes_identical: FAIL
- G4_interval_abundance_and_interval_sizes_identical: PASS
- G5_coordinate_distributions_strongly_changed: PASS
- G6_pushforward_densities_normalized: PASS
- G7_nonseparable_copula_control_changes_order_statistics: PASS
- G8_same_cardinality_in_every_pair: PASS
- G9_impossibility_follows_from_identical_input: PASS

## Verdict

FAIL_ORDER_MEASURE_IDENTIFIABILITY_AUDIT

## Logical consequence

No deterministic method using only a single finite relation matrix and its element count can uniquely recover a preferred coordinate sampling density across this monotone-transform equivalence class. Additional physical structure, calibration, repeated sampling, or a distinguished volume assignment is required.

## Boundary

The ambiguity concerns the choice of sampling measure or conformal-volume representative. It does not say that causal structure contains no geometric information, nor does it contradict continuum statements in which causal structure is supplemented by an independently specified local volume element.