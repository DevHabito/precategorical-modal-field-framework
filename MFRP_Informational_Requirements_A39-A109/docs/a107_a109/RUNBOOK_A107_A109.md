# A107-A109 runbook

## Current state

The current mathematically resolved prospective sequence ends at canonical rank 414. H19 (415-430) is frozen but unexecuted.

## Scientific rule under test

For a classifiable gamma-plus record, use only the frozen denominator and adjacent-target certificates to predict:

- left boundary if `N_{j+1}(L) < 0` while `N_j(R) > 0`;
- right boundary if `N_{j+1}(L) > 0` while `N_j(R) < 0`;
- two-sided partial component if both relevant endpoint signs are negative;
- full source-segment coverage if both are positive.

A class or boundary mismatch, or a selected non-adjacent KKT obstruction, refutes the rule on that record.

## H19 execution order

1. Confirm the H19 preregistration SHA-256 is `abe35d929e8a35b9db9fbad96ad375152e854d65e25df33ce70781d411709d5d`.
2. Execute only preregistered single-rank shards 415 through 430.
3. Give each full-atlas attempt a 55-second wall-clock limit.
4. If a rank times out without a result, repeat the identical command once.
5. After two timeouts, record the full-atlas status as incomplete for that rank. Do not change the prediction and do not invent a replacement rank.
6. If a fallback is needed, freeze a separate exact sufficient-certificate preregistration before running it.
7. Preserve full-atlas and fallback accounting separately.
8. Run independent direct rational matrix regression on every mathematically resolved rank.

## H19 frozen predictions

The batch contains 11 full records and 5 partial records. Four partial records are frozen as left boundaries. Rank 428 is frozen as a right boundary at `basic_p_56`. There are no frozen two-sided or `NO_CLASSIFICATION` cases.

## Stop conditions

Stop and report rather than repair if any of the following occurs:

- the preregistration hash does not match;
- a requested shard is not in the frozen shard list;
- the canonical source record no longer matches its frozen key;
- class or boundary differs from prediction;
- a non-adjacent KKT condition is selected as the first obstruction;
- direct symbolic/matrix regression disagrees;
- certification cannot resolve a required positivity or root claim.

An unresolved computation is `INCONCLUSIVE`, not a mathematical failure and not support.
