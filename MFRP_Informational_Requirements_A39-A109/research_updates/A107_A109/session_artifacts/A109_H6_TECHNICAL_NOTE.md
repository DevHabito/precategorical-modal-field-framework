# A109-H6 — Unchanged Two-Adjacent-Variable Rule, Ranks 207..222

## Preregistration

H6 was frozen before full-atlas execution with SHA-256:

`6a325f6eedd0772ec7ad2cbe66c8d5a98b37276336431fff68b265d975b3862a`

The unchanged A109 rule predicted 10 full records and 6 proper strict subcomponents, all six with a left boundary. It predicted no right or two-sided boundary in this block.

## Original full-atlas execution status

The full atlas completed for 12/16 ranks: 207, 208, 211..216, and 219..222. All 12 matched the frozen class and selected boundary set, with zero direct symbolic-vs-matrix mismatches and zero core/hull failures.

The preregistered shards 209..210 and 217..218 timed out repeatedly before producing result files. Therefore the **original H6 full-atlas protocol is formally inconclusive**, not PASS.

A transient orchestration timeout also occurred for 215..216, but the identical preregistered shard later completed normally without any protocol change.

## Separately preregistered exact sufficient-certificate diagnostic

After the repeated timeouts, a separate protocol was frozen before diagnostic execution:

`A109_H6D_PREREGISTRATION.json`

SHA-256:

`ac533ef4fc567a7da804a38ed27ec9e67266edce359bbc227934799fb3b7ff79`

This diagnostic does not run the full root atlas. It uses the exact rank-one KKT polynomials, certifies the common denominator, target monotonicity/sign pattern for partial predictions, strict positivity of every required non-target KKT numerator on the complete source segment, and exact direct rational matrix regression.

All four timed ranks were mathematically resolved in support of the frozen predictions:

- rank 209: left `basic_p_37`;
- rank 210: left `basic_p_37`;
- rank 217: full segment coverage;
- rank 218: left `basic_p_38`.

Across these four diagnostics:

- 1,615 KKT conditions certified by the sufficient-certificate protocol;
- 0 exact failures;
- 0 unresolved certificates;
- 6,881 direct rational matrix comparisons;
- 0 direct mismatches.

## Mixed exact mathematical result for H6

Combining the 12 completed full-atlas ranks with the four separately preregistered exact sufficient certificates gives a mathematical resolution of all 16 ranks:

- 16/16 support the unchanged rule;
- 10 full;
- 6 partial;
- 6/6 partial boundaries are left adjacent (`basic_p_{j+1}`);
- 0 right boundaries in this block;
- 0 two-sided cases;
- 22,782 direct rational matrix comparisons;
- 0 direct mismatches.

The partial ranks are 209, 210, 211, 218, 220, and 221.

This mixed result must not be mislabeled as a full-atlas PASS: the method differs for four ranks because of execution timeouts.

## Updated prospective interval

Together with the previously resolved ranks, the mathematically resolved prospective interval now extends continuously from rank 106 through rank 222: 117 records.

Within ranks 106..222:

- 83 full;
- 34 partial;
- 32 left-boundary partials;
- 2 right-boundary partials;
- 0 two-sided selected-boundary cases;
- 130,268 direct rational matrix comparisons;
- 0 direct mismatches.

Methodological caveat: rank 183 and ranks 209, 210, 217, 218 are resolved by separately preregistered sufficient-certificate diagnostics rather than completed full-atlas executions.

## Scientific interpretation

No exact counterexample to the two-adjacent-variable rule was found in H6. No non-adjacent selected boundary appeared in the full-atlas-completed H6 ranks, and the sufficient certificates prove all required non-target conditions remain positive in the four timeout ranks.

This still does not establish an all-922 theorem. A single future exact non-adjacent boundary or classification mismatch would refute the universal form.
