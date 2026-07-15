# A15 — Certified Counterexample Search

## Construction

Each adversary contains one or more induced copies of the six-element standard example S3 inside a Minkowski-order core.
The prefix/suffix placement is chosen only to match the ordering fraction of a paired independent Minkowski sprinkling.

## Results

### n = 96 (discovery)

- Minkowski holdout acceptance: 0.9500
- 1 S3 gadget(s): acceptance=0.7000, accepted=42/60, max p=0.8235, max density mismatch=0.066667
- 2 S3 gadget(s): acceptance=0.0667, accepted=4/60, max p=0.5385, max density mismatch=0.023684
- 3 S3 gadget(s): acceptance=0.0000, accepted=0/60, max p=0.0045, max density mismatch=0.001754

### n = 128 (discovery)

- Minkowski holdout acceptance: 0.9333
- 1 S3 gadget(s): acceptance=0.5833, accepted=35/60, max p=0.9864, max density mismatch=0.077633
- 2 S3 gadget(s): acceptance=0.0833, accepted=5/60, max p=0.7059, max density mismatch=0.000738
- 3 S3 gadget(s): acceptance=0.0000, accepted=0/60, max p=0.0045, max density mismatch=0.001107

### n = 192 (prospective_confirmation)

- Minkowski holdout acceptance: 0.9667
- 1 S3 gadget(s): acceptance=0.6833, accepted=41/60, max p=0.9502, max density mismatch=0.052792
- 2 S3 gadget(s): acceptance=0.2833, accepted=17/60, max p=0.7964, max density mismatch=0.000273
- 3 S3 gadget(s): acceptance=0.0333, accepted=2/60, max p=0.3710, max density mismatch=0.000382

## Gates

- G1_s3_dimension_self_tests: PASS
- G2_minkowski_model_and_holdout: PASS
- G3_all_candidates_transitive_and_certified: PASS
- G4_ordering_fraction_mismatch_le_0_02: FAIL
- G5_systematic_one_gadget_false_positives_discovery: PASS
- G6_systematic_one_gadget_false_positives_n192: PASS
- G7_at_least_one_prospective_counterexample: PASS
- G8_detection_non_decreasing_with_gadget_burden: PASS

## Verdict

SYSTEMATIC_CERTIFIED_COUNTEREXAMPLES_FOUND_A14_NOT_SUFFICIENT

## Boundary

The result addresses sufficiency of the A14 global signature for exact 1+1 embeddability. It does not erase the prior evidence that Q is a strong global manifoldlikeness diagnostic.