# A18 — Exact Order–Measure Identifiability Limit

## Exact construction

For every finite sample and every strictly increasing coordinate-wise transform T_u,T_v, the relation u_i<u_j and v_i<v_j is unchanged bit-for-bit.

## Transform summaries

### n=128, beta_edge_concentrated
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.214200
- Median transformed marginal KS: 0.170289
- Median Wasserstein shift: 0.067889

### n=128, beta_skew_opposed
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.226704
- Median transformed marginal KS: 0.415821
- Median Wasserstein shift: 0.217561

### n=128, power_anisotropic
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.239923
- Median transformed marginal KS: 0.496800
- Median Wasserstein shift: 0.233579

### n=256, beta_edge_concentrated
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.264188
- Median transformed marginal KS: 0.145060
- Median Wasserstein shift: 0.068953

### n=256, beta_skew_opposed
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.289286
- Median transformed marginal KS: 0.415859
- Median Wasserstein shift: 0.214916

### n=256, power_anisotropic
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.313577
- Median transformed marginal KS: 0.492340
- Median Wasserstein shift: 0.233531

### n=512, beta_edge_concentrated
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.264420
- Median transformed marginal KS: 0.130897
- Median Wasserstein shift: 0.068033

### n=512, beta_skew_opposed
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.328957
- Median transformed marginal KS: 0.406349
- Median Wasserstein shift: 0.217345

### n=512, power_anisotropic
- Relation identity rate: 1.0000
- Rank identity rate: 1.0000
- Median coordinate JS divergence: 0.347434
- Median transformed marginal KS: 0.481931
- Median Wasserstein shift: 0.233098

## Gates

- G1_all_monotone_transform_relations_bitwise_identical: PASS
- G2_all_coordinate_ranks_identical: PASS
- G3_all_relation_hashes_identical: PASS
- G4_interval_abundance_and_interval_sizes_identical: PASS
- G5_coordinate_distributions_strongly_changed: FAIL
- G6_pushforward_densities_normalized: FAIL
- G7_nonseparable_copula_control_changes_order_statistics: PASS
- G8_same_cardinality_in_every_pair: PASS
- G9_impossibility_follows_from_identical_input: PASS

## Verdict

FAIL_ORDER_MEASURE_IDENTIFIABILITY_AUDIT

## Logical consequence

No deterministic method using only a single finite relation matrix and its element count can uniquely recover a preferred coordinate sampling density across this monotone-transform equivalence class. Additional physical structure, calibration, repeated sampling, or a distinguished volume assignment is required.

## Boundary

The ambiguity concerns the choice of sampling measure or conformal-volume representative. It does not say that causal structure contains no geometric information, nor does it contradict continuum statements in which causal structure is supplemented by an independently specified local volume element.