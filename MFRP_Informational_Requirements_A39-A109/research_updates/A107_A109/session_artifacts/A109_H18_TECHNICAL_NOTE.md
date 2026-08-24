# A109-H18 Technical Note — unchanged two-sided adjacent-boundary holdout

## Frozen scope

H18 covered canonical gamma-plus ranks 399–414 under the unchanged adjacent-boundary rule. The parent preregistration was frozen before any H18 full-atlas outcome and had SHA-256:

`ea471ffc0a5e62c2ec0c15adea3d759b424802e7d35bcd92f13fb90e67cd6ef3`

It predicted 11 full-segment cases and 5 proper strict subcomponents, all five with a single **left** adjacent boundary. No right, two-sided, or NO_CLASSIFICATION case was predicted.

The rule remained:

- `basic_p_{j+1}` can supply a left boundary when its lower-end sign is negative and it is strictly increasing;
- `basic_p_j` can supply a right boundary when its right-end sign is negative and it is strictly decreasing;
- if both relevant endpoint signs are positive, predict full source-segment coverage;
- any exact class/boundary mismatch or non-adjacent selected KKT obstruction refutes the frozen classifier on that record.

## Full-atlas execution

Single-rank shards used the frozen 55-second wall-clock window.

Full atlas completed for 14/16 ranks:

399, 400, 401, 402, 403, 404, 406, 407, 408, 409, 411, 412, 413, 414.

Ranks **405** and **410** each timed out twice under identical execution, with no full-atlas result file. They therefore remain formally incomplete under the H18 full-atlas protocol.

The 14 completed full-atlas records all matched their frozen class and exact boundary prediction. They produced 27,961 direct rational matrix comparisons with 0 mismatches, 0 core-certificate failures, 0 hull-certificate failures, and 0 root failures.

## H18D exact sufficient certificates after repeated timeout

Only after both repeated timeouts, H18D was frozen for ranks 405 and 410. Its preregistration SHA-256 is:

`2ebcd6612c005291a11913ef705555bd306e860b06a8eda1dc39e4b2164835a1`

For each timeout rank H18D required:

1. exact positivity of the common denominator over the complete frozen source interval;
2. strict positivity of all KKT conditions at the frozen witness;
3. the frozen target `basic_p_56` to have the declared left-boundary sign pattern and strictly increasing derivative;
4. exact rational isolation of a unique target root;
5. every non-target KKT numerator to be certified strictly positive over the full source interval;
6. four independently evaluated rational matrix probes to agree exactly with the symbolic numerator reconstruction and to show target failure only at the frozen outside probe.

### Rank 405

Frozen prediction: proper strict subcomponent with left `basic_p_56`.

Observed exact target signs: `[-,+,+]` at lower endpoint, witness, and right endpoint. The derivative was certified positive. A unique root was rationally bracketed; midpoint approximation is

`0.132553616083281`.

618 non-target KKT conditions were certified strictly positive. Four direct probes produced 2,476 exact comparisons with 0 mismatches, 0 interior positivity failures, and 0 outside-sign failures.

### Rank 410

Frozen prediction: proper strict subcomponent with left `basic_p_56`.

Observed exact target signs: `[-,+,+]`; derivative certified positive. The unique root bracket has midpoint approximation

`0.130944956751315`.

622 non-target KKT conditions were certified strictly positive. Four direct probes produced 2,492 exact comparisons with 0 mismatches, 0 interior positivity failures, and 0 outside-sign failures.

H18D therefore mathematically resolves both timeout records, but does **not** retroactively convert their full-atlas timeouts into completed full-atlas executions.

## Aggregate H18 result

Mathematical verdict:

`RESOLVED_SUPPORT_A109_H18_MIXED_EXACT_PROTOCOL`

Across all 16 frozen records:

- class + exact boundary matches: **16/16**;
- full-segment coverage: **11**;
- proper strict subcomponents: **5**;
- left adjacent boundaries: **5**;
- right adjacent boundaries: **0**;
- two-sided cases: **0**;
- non-adjacent selected KKT boundaries: **0**;
- direct rational comparisons: **32,929**;
- direct mismatches: **0**.

The five partial records are 399, 405, 410, 411, and 412. Their approximate unique left-boundary roots are, respectively:

- 399: `0.129534204748828`, `basic_p_55`;
- 405: `0.132553616083281`, `basic_p_56`;
- 410: `0.130944956751315`, `basic_p_56`;
- 411: `0.130052033405979`, `basic_p_56`;
- 412: `0.129447821177614`, `basic_p_56`.

All certification itself used exact rational arithmetic; decimals above are orientation only.

## Cumulative prospective status after H18

The mathematically resolved prospective sequence is now ranks **106–414**, i.e. 309 consecutive records. The strict-clean prospective count is 308 because the previously documented rank-295 protocol-ordering issue remains the sole accounting gap.

Current counts:

- mathematically resolved: **309**;
- strict-clean prospective: **308**;
- full: **215**;
- partial: **94**;
- left adjacent boundaries: **88**;
- right adjacent boundaries: **6**;
- two-sided: **0**;
- non-adjacent selected boundary: **0**;
- exact direct comparisons on the mathematically resolved sequence: **475,782**;
- exact direct mismatches: **0**.

This is strong finite prospective evidence for the adjacent-boundary classifier. It is **not** an all-922 theorem.

## Next frozen holdout: H19

Before any full-atlas outcome for ranks 415–430, an exact target-only snapshot was frozen with SHA-256:

`25825c8638b869429e02f90cbac174da7b4d0590389efcb3b8a1490a7dfc6236`

H19 preregistration SHA-256:

`abe35d929e8a35b9db9fbad96ad375152e854d65e25df33ce70781d411709d5d`

H19 predicts:

- 11 full-segment records;
- 5 partial records;
- 4 left boundaries;
- **1 right boundary**;
- 0 two-sided;
- 0 NO_CLASSIFICATION.

The right-branch case is prospectively frozen at **rank 428**, with predicted right `basic_p_56`.

H19 has not been full-atlas executed in this note.
