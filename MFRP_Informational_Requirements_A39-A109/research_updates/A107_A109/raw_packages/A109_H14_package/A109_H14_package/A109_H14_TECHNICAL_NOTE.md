# A109-H14 — Unchanged Two-Sided Adjacent-Boundary Holdout

## Frozen protocol
H14 was preregistered for canonical ranks 335..350 under the unchanged adjacent-boundary rule. Prediction: 11 full source-segment coverages and 5 proper strict subcomponents, all five with a left `basic_p_{j+1}` boundary; no right, two-sided, or non-adjacent boundary was predicted.

Preregistration SHA-256: `10900de0f0405a1f8db1f8af9c917fd042bdc6a9dad75507d3a7034622478320`.

## Full-atlas execution
Nine single-rank full-atlas shards completed under the 55-second wall-clock policy: [335, 336, 337, 338, 340, 345, 346, 347, 348]. Seven ranks timed out twice with no result: [339, 341, 342, 343, 344, 349, 350]. Therefore the full-atlas protocol alone is formally incomplete; the timeouts are not counted as passes.

## Separately frozen fallback
Only after the repeated timeouts, H14D was frozen for exactly those seven ranks. SHA-256: `722f2d04cc93e2ac634273ad3297f60f36c202bfc2723d385cfc8502a8fe489e`. It requires exact denominator/witness checks, exact monotonic target/root certification where partial, positivity of every non-target KKT numerator over the full source segment (or every KKT numerator for predicted full coverage), and independent exact direct-matrix regression at frozen rational probes.

All seven H14D ranks resolved with zero exact certificate failures and zero unresolved certificates. Across them, 3882 required KKT conditions were certified and 16660 direct rational comparisons were performed with zero mismatch.

## Exact result
Mathematically, H14 resolves all 16 ranks and exactly matches the frozen prediction:

- 16/16 class/boundary matches;
- 11 full source-segment coverages;
- 5 proper strict subcomponents;
- 5/5 partials bounded on the left by `basic_p_{j+1}`;
- 0 right boundaries;
- 0 two-sided records;
- 0 non-adjacent selected boundaries.

The five partial ranks are 339, 342, 343, 344, and 350.

### Root orientations
- rank 339: `basic_p_50` left root, decimal orientation `s* ~ 0.132461495521482` (certification uses exact rational bracket).
- rank 342: `basic_p_50` left root, decimal orientation `s* ~ 0.130705710311653` (certification uses exact rational bracket).
- rank 343: `basic_p_50` left root, decimal orientation `s* ~ 0.130021798878210` (certification uses exact rational bracket).
- rank 344: `basic_p_50` left root, decimal orientation `s* ~ 0.129115144712268` (certification uses exact rational bracket).
- rank 350: `basic_p_51` left root, decimal orientation `s* ~ 0.132302956615154` (certification uses exact rational bracket).

## Independent regression
The nine completed full-atlas ranks contributed 14937 exact direct comparisons. The seven fallback ranks contributed 16660. Total H14 direct comparisons: **31597**, with **0 mismatches**.

An independent artifact-level consistency pass checked hashes, all 16 prediction/outcome matches, all direct-mismatch counts, and aggregate class/boundary counts: **41/41 checks passed**.

## Cumulative status
Through canonical rank 350, ranks 106..350 comprise 245 mathematically resolved prospective records. The strict-clean prospective count is 244 because of the previously documented rank-295 protocol-ordering issue; H14 itself adds 16 clean records. Cumulative mathematical counts are 170 full, 75 partial, 70 left boundaries, 5 right boundaries, 0 two-sided, and 0 non-adjacent selected boundaries, with 349685 exact direct comparisons and 0 mismatches.

## Scope
H14 supports the unchanged adjacent-boundary rule on this finite holdout. It is not an all-922 theorem and makes no physical claim. A single future exact non-adjacent first obstruction, class mismatch, or unsupported boundary would refute the universal form.
