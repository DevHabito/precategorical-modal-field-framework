# A16 — Local–Global Manifoldlikeness Criterion

## Design

- Global A14 covariance-aware interval-abundance test.
- Exact induced-S3 certificate channel for the unanchored A15 family.
- Exact dimension<=2 recognition on every order interval with 6-10 elements.
- Prospective n=256 challenge with a minimal seven-element dimension-3 obstruction whose every six-element deletion is dimension<=2.
- Exact 2D bimodal control to test global/local complementarity.

## Model validation

### n = 128
- Global Minkowski acceptance: 1.0000
- Local Minkowski pass: 1.0000
- Combined scanned holdout acceptance: 1.0000

### n = 256
- Global Minkowski acceptance: 1.0000
- Local Minkowski pass: 1.0000
- Combined scanned holdout acceptance: 1.0000

## Family results

### minkowski_holdout at n=128
- Global acceptance: 1.0000
- Local pass: 1.0000
- Combined acceptance: 1.0000
- Maximum density mismatch: 0.000000
- Local channels: {'none': 4}

### unanchored_s3 at n=128
- Global acceptance: 0.6667
- Local pass: 0.0000
- Combined acceptance: 0.0000
- Maximum density mismatch: 0.000369
- Local channels: {'induced_s3': 12}

### anchored_minimal7_obstruction at n=256
- Global acceptance: 1.0000
- Local pass: 0.0000
- Combined acceptance: 0.0000
- Maximum density mismatch: 0.004565
- Local channels: {'small_interval_dimension': 10}

### bimodal_exact_2d_order at n=256
- Global acceptance: 1.0000
- Local pass: 1.0000
- Combined acceptance: 1.0000
- Maximum density mismatch: 0.004933
- Local channels: {'none': 6}

### minkowski_holdout at n=256
- Global acceptance: 1.0000
- Local pass: 1.0000
- Combined acceptance: 1.0000
- Maximum density mismatch: 0.000000
- Local channels: {'none': 4}

### unanchored_s3 at n=256
- Global acceptance: 1.0000
- Local pass: 0.0000
- Combined acceptance: 0.0000
- Maximum density mismatch: 0.004350
- Local channels: {'induced_s3': 12}

## Gates

- G1_exact_recognition_self_tests: PASS
- G2_minkowski_global_and_local_acceptance: PASS
- G3_all_structures_transitive: PASS
- G4_all_adversaries_density_matched: PASS
- G5_unanchored_s3_detection_discovery: PASS
- G6_unanchored_s3_detection_n256: PASS
- G7_unseen_minimal7_interval_detection: PASS
- G8_bimodal_2d_local_accept_global_reject: FAIL
- G9_global_q_has_sparse_defect_false_positives: PASS
- G10_no_adversary_used_for_calibration: PASS

## Verdict

FAIL_LOCAL_GLOBAL_COMPLEMENTARITY

## Boundary

The combined criterion is validated only against the tested families and finite sizes. Local exact tests cover S3 certificates and small order intervals, not every possible sparse global obstruction.