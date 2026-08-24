# A109 Continuation — H7, H8, H9 Exact Prospective Audit

## Baseline
Immediately before aggregation, `python tools/verify_results.py` returned 68 audit results, 1013 gates, 110 figures, zero failures, status `PASS`.

## Frozen rule
The A109 predictor was not changed:

- `basic_p_(j+1)` is the candidate left boundary when its exact lower-endpoint numerator sign is negative.
- `basic_p_j` is the candidate right boundary when its exact upper-endpoint numerator sign is negative.
- both target endpoint signs positive predicts full source-segment coverage.
- a class/boundary mismatch or any selected non-adjacent KKT obstruction refutes the finite holdout claim.

No modular rule was reintroduced.

## H7 — canonical ranks 223..238
Preregistration SHA-256: `7271e73abc02f7e0c37d2a8f4ff5c3d71f8a0fa86dbf5cba8c3515efc9fa440a`.

The preregistered full-atlas shard 227..228 timed out twice without a result file, so the original H7 full-atlas protocol is formally incomplete. A separate preregistered exact sufficient-certificate protocol (H7D, SHA-256 `7d7269e4680ba2b0227dba9afef266bfb1dca9cb60209dc68b8b50d91ded719f`) resolved those two ranks without calling the full root atlas.

Mixed exact mathematical result:

- 16/16 class and boundary predictions supported;
- 13 full, 3 partial;
- all 3 partial boundaries are left adjacent;
- rank 228 is certified as left `basic_p_39`;
- 22,557 independent direct rational comparisons;
- 0 direct mismatches;
- no non-adjacent selected boundary;
- no two-sided boundary.

## H8 — canonical ranks 239..254
Preregistration SHA-256: `3acf7079c7c150bc44e3cfb19fe6d4419394a561eebc850144a62de4906250de`.

The preregistered full-atlas shard 239..240 timed out twice. H8D (SHA-256 `65f281a7fec2ab904af0afe3028a301b1ccf37a456b0374251569d5bfa9feb9d`) was frozen before diagnostic execution and resolved both ranks by exact sufficient certificates.

Mixed exact mathematical result:

- 16/16 class and boundary predictions supported;
- 12 full, 4 partial;
- all 4 partial boundaries are left adjacent;
- ranks 239 and 240 are certified as left `basic_p_40`;
- 23,238 independent direct rational comparisons;
- 0 direct mismatches;
- no non-adjacent selected boundary;
- no two-sided boundary.

## H9 — canonical ranks 255..270
Preregistration SHA-256: `61e4d93d144a942afa0cebde8ba375d80261688d63eea4ba6b366bcb032022f2`.

Six preregistered full-atlas pair shards timed out twice without result files: 255..258 and 261..268. The full-atlas protocol is therefore formally incomplete on those shards. H9D (SHA-256 `d143f195ed509fdc16ba320e4c3a191447c0f6f88e28049d5081930257a379c4`) was frozen before diagnostic execution and mathematically resolved the 12 affected ranks by exact sufficient certificates. Ranks 259..260 and 269..270 completed the original full-atlas protocol.

Mixed exact mathematical result:

- 16/16 class and boundary predictions supported;
- 9 full, 7 partial;
- 6 left-adjacent partial boundaries;
- 1 right-adjacent partial boundary;
- 30,405 independent direct rational comparisons;
- 0 direct mismatches;
- 5,597 KKT conditions certified in the H9D timeout diagnostics;
- 0 exact diagnostic failures and 0 unresolved diagnostic conditions;
- no non-adjacent selected boundary;
- no two-sided boundary.

### Prospectively important right-boundary case: rank 262
Rank 262 was frozen before execution as a right-boundary case. Its parameters are M=229, j=41, with predicted boundary `basic_p_41`.

The exact sufficient certificate found target signs

`L: +1, witness: +1, R: -1`,

with strictly decreasing right target under the frozen rule, and isolated the unique sign-change bracket

`71359035877/536870912000 < s* < 35679517939/268435456000`

(width `1/536870912000`). The independent outside-right direct probe has `basic_p_41` nonpositive, while all strict probes remain positive. Thus rank 262 supplies a third prospectively supported right-adjacent boundary in the continuing A109 programme, after the earlier rank-173 and rank-206 cases.

## Cumulative prospective status through rank 270
Using the previously audited mixed-exact status through rank 222 plus H7, H8 and H9:

- canonical prospective ranks resolved: **106..270 = 165 records**;
- class/boundary matches: **165/165**;
- full source-segment coverage: **117**;
- proper strict subcomponents: **48**;
- left-adjacent boundaries: **45**;
- right-adjacent boundaries: **3**;
- two-sided boundaries observed: **0**;
- selected non-adjacent boundaries observed: **0**;
- independent direct rational comparisons: **206,468**;
- direct symbolic-vs-matrix mismatches: **0**.

## What is established and what is not
The finite prospective evidence for the two-adjacent-variable rule has strengthened substantially. In the mathematically resolved prospective sequence 106..270, no counterexample has been found, including a prospectively predicted right-boundary case at rank 262.

This is **not** an all-922 theorem. Several ranks were resolved by separately preregistered exact sufficient certificates after full-atlas execution timeouts, so one must not describe the entire sequence as a uniform full-atlas computation. A future exact non-adjacent boundary or class mismatch would still refute a universal form of the rule.

## Next frozen holdout
A109-H10 is frozen for ranks 271..286 before any full-atlas outcome was inspected. Preregistration SHA-256: `8d4444e53f594b29dbab84060d623525cf2922c5060e6aa9d9102e2b2ca2c555`.

Frozen target-only prediction:

- 11 full;
- 5 partial;
- 5 left boundaries;
- 0 right boundaries;
- 0 two-sided boundaries.

The correct next action is to execute H10 unchanged and continue looking for a class mismatch or a selected non-adjacent KKT obstruction.
