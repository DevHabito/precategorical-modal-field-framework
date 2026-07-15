# A28 — q-Score Selection Audit

## Main result

Scale-free cardinal normalization and extension-stable local odds cannot coexist nontrivially under positive-affine q invariance. Every natural score sacrifices scale calibration, context stability, cardinality, or locality.

## Score summaries

### raw
- Extension violation rate: 0.0000
- Median extension log-odds change: 0.000000
- Remote locality violation rate: 0.0000
- Median monotone-warp TV: 0.049737

### min_shift
- Extension violation rate: 0.0000
- Median extension log-odds change: 0.000000
- Remote locality violation rate: 0.0000
- Median monotone-warp TV: 0.049737

### row_zscore
- Extension violation rate: 1.0000
- Median extension log-odds change: 0.232828
- Remote locality violation rate: 0.0000
- Median monotone-warp TV: 0.033817

### row_mad
- Extension violation rate: 0.9552
- Median extension log-odds change: 0.398857
- Remote locality violation rate: 0.0000
- Median monotone-warp TV: 0.041499

### row_rank
- Extension violation rate: 0.9613
- Median extension log-odds change: 0.085714
- Remote locality violation rate: 0.0000
- Median monotone-warp TV: 0.000000

### global_zscore
- Extension violation rate: 1.0000
- Median extension log-odds change: 0.046925
- Remote locality violation rate: 1.0000
- Median monotone-warp TV: 0.044587

## Gates

- G1_context_scale_incompatibility_theorem_proved: PASS
- G2_all_scores_relabel_equivariant: PASS
- G3_raw_and_min_shift_extension_stable: PASS
- G4_dimensionless_scores_positive_affine_invariant: PASS
- G5_dimensionless_scores_context_dependent: PASS
- G6_global_normalization_nonlocal: PASS
- G7_rank_is_ordinal_not_cardinal: PASS
- G8_raw_score_lambda_scale_degeneracy_exact: PASS
- G9_no_natural_candidate_satisfies_all_desiderata: PASS
- G10_no_physical_score_selected: PASS

## Verdict

PASS_SCORE_CONTEXT_SCALE_INCOMPATIBILITY_NO_GO

## Boundary

A28 does not show that context dependence is always physically unacceptable, nor that a calibrated raw-q score is impossible. It proves that the desired properties cannot all be obtained for free from the current relational and gauge structure.