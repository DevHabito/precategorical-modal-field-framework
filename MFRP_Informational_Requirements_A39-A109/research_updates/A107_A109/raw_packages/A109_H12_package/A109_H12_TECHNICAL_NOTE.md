# A109-H12 — Two-Sided Adjacent-Boundary Holdout

## Frozen protocol
Ranks 303..318 were frozen before atlas execution. The target-only predictor declared 12 full source-segment cases and 4 proper strict subcomponents: left boundaries at ranks 308 and 309, and right boundaries at ranks 303 and 313. No two-sided case was predicted. Single-rank shards were used. The execution policy, frozen before the run, required an identical second 55-second full-atlas attempt after any first timeout; only after two timeouts could a separately preregistered exact sufficient-certificate method be used.

## Full-atlas result
The full atlas completed on the first attempt for 15/16 ranks. All 15 matched their frozen class and exact boundary prediction, with zero direct symbolic-vs-matrix mismatches, zero core-certificate failures and zero hull-certificate failures.

Rank 303 is especially informative: it prospectively predicted a right boundary `basic_p_45`, and the full atlas returned exactly a proper strict subcomponent with right `basic_p_45`.

Rank 313 timed out twice under identical 55-second full-atlas executions and produced no full-atlas result file. Therefore the parent full-atlas status is formally `INCOMPLETE_EXECUTION_R313`.

## H12D exact sufficient certificate for rank 313
Only after the two timeouts, a separate protocol was frozen. The rank-313 prediction remained unchanged: proper strict subcomponent with right `basic_p_46`.

The exact certificate found:

- target signs L=+1, witness=+1, R=-1;
- strict decrease of the target numerator over the source segment (implemented as positivity of the negated derivative certificate);
- one unique right crossing, with rational bracket centered approximately at `s* = 0.132800121220216` for readability only;
- 524 non-target KKT conditions certified strictly positive on the complete source segment;
- 2,100 exact direct symbolic-vs-matrix comparisons with zero mismatches;
- zero exact failures and zero unresolved certificates.

Therefore rank 313 is mathematically resolved in support under a preregistration-compliant mixed exact protocol. This does not retroactively complete the full-atlas execution.

## H12 verdict
`RESOLVED_SUPPORT_A109_H12_MIXED_EXACT_PROTOCOL`

Across the 16 ranks:

- class matches: 16/16;
- boundary-set matches: 16/16;
- 12 full, 4 partial;
- 2 left adjacent boundaries;
- 2 right adjacent boundaries;
- 0 two-sided boundaries;
- 0 non-adjacent selected boundaries;
- 27,128 exact direct comparisons;
- 0 direct mismatches.

## Cumulative strict accounting
The previous H11 review identified a procedural preregistration-order deviation for rank 295: its alternative certificate was run after one timeout, although the parent policy required repeated timeouts. Rank 295 remains mathematically supported but is excluded from the clean confirmatory count.

Thus, through rank 318:

- 213 records (ranks 106..318) are mathematically resolved and all agree with the unchanged adjacent-boundary rule;
- 212 qualify for the strict clean prospective count under the recorded execution policies;
- mathematical distribution: 151 full and 62 partial;
- among the 62 partial: 57 left `p_{j+1}=0` and 5 right `p_j=0`;
- 0 two-sided and 0 non-adjacent selected boundaries observed;
- 287,996 exact direct comparisons across all mathematical resolutions, zero mismatches;
- 285,984 direct comparisons in the strict clean prospective accounting, zero mismatches.

These are finite catalogue results, not an all-922 theorem.

## Next frozen holdout
A109-H13 is frozen for ranks 319..334. It predicts 8 full and 8 partial cases, all eight partials on the left. It has not been executed.
