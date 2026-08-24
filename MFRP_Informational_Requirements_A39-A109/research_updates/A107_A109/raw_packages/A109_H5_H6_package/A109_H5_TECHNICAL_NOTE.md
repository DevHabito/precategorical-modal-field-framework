# A109-H5 — Unchanged Two-Sided Adjacent-Boundary Holdout

## Frozen question

For canonical `legacy_three_band_gamma_plus` ranks 190..205, does the unchanged A109 target-only rule correctly predict the exact full-atlas class and selected boundary set, while no non-adjacent KKT condition becomes the selected obstruction?

The preregistration was frozen before full-atlas execution with SHA-256:

`d510a645173bf6806f83fea4cbc44550446406732790b7a07be598d46f4f858e`

The prediction source was the previously frozen target-only scan SHA-256:

`86e00691027e8f51d2882a053cd47e697da31bc059179701217fe19c33bc0c6f`

No full-atlas outcome for ranks 190..205 was inspected before preregistration.

## Frozen prediction

The 16 ranks were predicted as:

- 12 `full_segment_coverage`;
- 4 `proper_strict_subcomponent`;
- 4 left boundaries;
- 0 right boundaries;
- 0 two-sided boundaries.

The four predicted partial records were ranks 192, 193, 200, and 201. The predicted boundaries were `basic_p_35` for ranks 192/193 and `basic_p_36` for ranks 200/201.

## Exact result

**Formal verdict:** `PASS_A109_H5_TWO_SIDED_HOLDOUT`.

All 16/16 ranks matched both the preregistered class and the exact selected boundary set.

Observed counts:

- 12 full;
- 4 partial;
- 4 left boundaries;
- 0 right boundaries;
- 0 two-sided boundaries;
- 0 non-adjacent selected boundaries.

The partial roots were uniquely isolated with exact rational brackets. Decimal midpoints, only for readability, are approximately:

- rank 192: `s* ~ 0.13018208464189276`, left `basic_p_35`;
- rank 193: `s* ~ 0.12906199490825085`, left `basic_p_35`;
- rank 200: `s* ~ 0.13087729346760500`, left `basic_p_36`;
- rank 201: `s* ~ 0.13002418918688202`, left `basic_p_36`.

Each partial record also has an exact rational outside point on the left where the selected condition has negative sign.

## Independent exact regression and certificates

Across H5:

- 20,080 direct rational matrix comparisons;
- 0 direct mismatches;
- 0 direct interior-positivity failures;
- 0 outside-sign failures;
- 0 root failures;
- 6,196 core conditions certified, 0 failures;
- 6,192 nonselected-hull conditions certified, 0 failures.

Three representative/precarious shards were independently rerun (190..191, 192..193, and 200..201). After removing runtime seconds only, each rerun was structurally identical to its first completed result. Normalized SHA-256 values are recorded in `A109_H5_AGGREGATE_RESULT.json`.

## Execution transparency

An outer orchestration timeout occurred before shard 196..197 produced a result file. The identical preregistered shard was rerun with no change to ranks, predictions, criteria, support, or tolerances and then completed normally. During reproducibility checking, one attempted rerun of 192..193 also timed out without producing a result; the identical rerun later completed and matched structurally.

These are execution events, not mathematical failures or favorable case substitutions.

## Updated finite prospective status

Using the already established exact results through rank 189, H5 ranks 190..205, and the separately preregistered rank-206 right-boundary test, the mathematically resolved prospective interval is now ranks 106..206 inclusive: 101 records.

Within that interval:

- 73 full;
- 28 partial;
- 26 left-boundary partials;
- 2 right-boundary partials;
- 0 two-sided selected-boundary cases;
- 107,486 direct rational matrix comparisons;
- 0 direct mismatches.

Methodological warning: rank 183 remains resolved by a separately preregistered exact sufficient-certificate diagnostic after full-atlas timeout. Therefore the mathematical interval 106..206 is continuous, but the original uniform full-atlas protocol still has a formal execution gap at rank 183.

## Scope

H5 supports the unchanged two-adjacent-variable rule on ranks 190..205 and finds no third selected-boundary mechanism in this block. It does **not** establish an all-922 theorem, and it makes no physical claim.
