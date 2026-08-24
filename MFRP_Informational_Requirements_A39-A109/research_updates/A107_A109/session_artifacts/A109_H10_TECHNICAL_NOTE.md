# A109-H10 — Unchanged Two-Adjacent Boundary Holdout

## Frozen question

Ranks 271..286 were frozen before full-atlas inspection under the unchanged adjacent-boundary rule:

- left candidate: `basic_p_{j+1}` when the upper-adjacent numerator is negative at the left source endpoint and positive at the witness;
- right candidate: `basic_p_j` under the corresponding right-endpoint sign reversal;
- both positive at the relevant endpoints -> full source-segment coverage;
- any exact class/boundary mismatch or non-adjacent selected obstruction -> refutation.

Parent preregistration SHA-256:

`8d4444e53f594b29dbab84060d623525cf2922c5060e6aa9d9102e2b2ca2c555`

The frozen batch prediction was 11 full, 5 partial, all five left, zero right, zero two-sided.

## Execution status

The original rank-pair full-atlas protocol completed for 10 ranks: 271, 272, 275, 276, 279, 280, 281, 282, 285, 286. It repeatedly timed out without result files for the frozen pair shards 273-274, 277-278, and 283-284.

Therefore the **formal full-atlas H10 protocol is incomplete**. No timeout is counted as a mathematical pass.

Before any alternative diagnostic outcome was inspected, a separate exact sufficient-certificate protocol was frozen for the six timeout ranks. Diagnostic preregistration SHA-256:

`e545aec22d76b989732da4505988d1be316ad3115116365aecf2ae61cbbcb836`

The alternate protocol certified the denominator, the frozen target's required monotonicity/sign crossing when partial, strict positivity of every non-target KKT condition on the entire source segment, and independent exact-rational direct matrix regression. It does not retroactively turn the timed-out full-atlas jobs into completed atlas runs.

## Exact result

**Mixed exact mathematical verdict:** `RESOLVED_SUPPORT_A109_H10_MIXED_EXACT_PROTOCOL`.

All 16 frozen H10 predictions are mathematically resolved without contradiction:

- 11 full source-segment coverages;
- 5 proper strict subcomponents;
- 5/5 partials have a left adjacent boundary;
- 0 right boundaries in this batch;
- 0 two-sided cases;
- 0 non-adjacent boundary counterexamples.

| rank | M | j | exact method | resolved class | boundary |
|---:|---:|---:|---|---|---|
| 271 | 235 | 42 | full atlas | `full_segment_coverage` | — |
| 272 | 235 | 42 | full atlas | `full_segment_coverage` | — |
| 273 | 235 | 43 | exact sufficient certificate | `proper_strict_subcomponent` | left `basic_p_44` |
| 274 | 236 | 42 | exact sufficient certificate | `full_segment_coverage` | — |
| 275 | 236 | 42 | full atlas | `full_segment_coverage` | — |
| 276 | 237 | 43 | full atlas | `proper_strict_subcomponent` | left `basic_p_44` |
| 277 | 238 | 43 | exact sufficient certificate | `proper_strict_subcomponent` | left `basic_p_44` |
| 278 | 239 | 43 | exact sufficient certificate | `proper_strict_subcomponent` | left `basic_p_44` |
| 279 | 239 | 43 | full atlas | `full_segment_coverage` | — |
| 280 | 240 | 43 | full atlas | `full_segment_coverage` | — |
| 281 | 240 | 43 | full atlas | `full_segment_coverage` | — |
| 282 | 241 | 43 | full atlas | `full_segment_coverage` | — |
| 283 | 241 | 43 | exact sufficient certificate | `full_segment_coverage` | — |
| 284 | 241 | 44 | exact sufficient certificate | `proper_strict_subcomponent` | left `basic_p_45` |
| 285 | 242 | 43 | full atlas | `full_segment_coverage` | — |
| 286 | 242 | 43 | full atlas | `full_segment_coverage` | — |

## Independent exact regression

Full-atlas completed ranks:

- direct comparisons: 15,075;
- direct mismatches: 0;
- core-certificate failures: 0;
- hull-certificate failures: 0.

Separate timeout-rank certificates:

- certified required KKT conditions: 2,910;
- exact condition failures: 0;
- unresolved conditions: 0;
- direct comparisons: 12,628;
- direct mismatches: 0.

Combined H10 exact direct regression:

**27,703 comparisons, 0 mismatches.**

A separate artifact-level consistency checker recomputed the frozen-rank coverage, prediction identity, exact results, and direct comparison totals from the raw outputs: 140 checks, 0 failures, status `PASS`.

Aggregate result SHA-256:

`ef066e6476613df221269687b2058e0aa50295e4ea2201eaa4fd740d04756311`

## Cumulative prospective status

After H10, the mixed-exact prospectively resolved contiguous sequence is ranks 106..286:

- 181 records;
- 181/181 frozen rule matches;
- 128 full;
- 53 partial;
- 50 left-adjacent partials;
- 3 right-adjacent partials;
- 0 two-sided cases found;
- 0 non-adjacent selected/certified boundary counterexamples;
- 234,171 exact direct comparisons;
- 0 direct mismatches.

This is **not** uniform full-atlas completion, because some timeout ranks were resolved by separately preregistered sufficient certificates. It is also **not** a theorem for all 922 gamma-plus records.

## Interpretation

H10 did not produce a counterexample to the current two-adjacent-boundary rule. This strengthens finite prospective evidence but does not establish universality. A later rank can still refute the universal form by exhibiting a wrong class, a wrong boundary side, a non-adjacent first obstruction, failure of the target monotonicity/applicability assumptions, or another exact contradiction.

## Next frozen holdout

A109-H11 is frozen for canonical ranks 287..302, using the same target-only scan and unchanged scientific rule. Because pair-shard execution has become increasingly expensive at larger M, the execution granularity is preregistered as single-rank shards before any atlas outcome is inspected. This is computational only; selection and adjudication are unchanged.

Frozen H11 prediction: 11 full, 5 partial, all five left, zero right, zero two-sided.

H11 preregistration SHA-256:

`2e7623534df3b2b520eb46ea0a57bf284d928156f6af60c09864f6b6c62358a4`

H11 has **not been executed** in this note.
