# A109-H2 — Unchanged Two-Sided Adjacent-Boundary Holdout (Ranks 122..172)

## Frozen status

The A109 two-sided rule was not modified. The deterministic contiguous holdout ranks 122..172 was preregistered before full-atlas execution.

Preregistration SHA-256: `879c061ccaf5bcec45182b08b85858b1119c26404026e0f80fb1ac04f58c8aea`.

Frozen predictions: 38 `full_segment_coverage` and 13 `proper_strict_subcomponent`; no record in this interval was predicted to have a right-only or two-sided boundary.

## Execution transparency

The first frozen shard 122..129 completed normally. The 8-record execution unit 130..137 exceeded runtime twice and produced no result file. Before inspecting any mathematical outcome from that range, execution was repartitioned deterministically while preserving every rank, prediction, criterion, and aggregate adjudication. Later, 142..145 also timed out as a four-record execution unit and was split into 142..143 and 144..145 before either result was obtained. These are execution-only changes, not scientific selection changes.

Execution manifest SHA-256: `ed9a68a9c04814ae565377863b5ed87563797ee6becce5ac2966cdc3ea03fcdd`.

Supplement SHA-256: `1abeaee97a896052fb9244153c75ead5be50ad97d1eb7f0a0bea0fbbb880832b`.

## Exact result

Verdict: **PASS_A109_H2_UNCHANGED_TWO_SIDED_RULE**.

- class matches: **51/51**
- exact selected-boundary-set matches: **51/51**
- full source-segment coverage: **38**
- proper strict subcomponents: **13**
- non-adjacent selected boundaries: **0**
- two-sided selected boundary sets: **0**
- direct exact matrix comparisons: **51,894**
- direct mismatches: **0**
- core-certificate failures: **0**
- hull-certificate failures: **0**
- root failures: **0**
- direct positivity failures: **0**
- direct outside-sign failures: **0**

All 13 partial records had exactly the frozen left boundary `basic_p_(j+1)`. Their canonical ranks are: 122, 129, 130, 136, 137, 138, 144, 145, 151, 158, 159, 167, 168.

## Combined prospective A109 status

With the prior frozen ranks 106..121 and the separately preregistered right-branch rank 173, the two-sided A109 rule has now been prospectively confronted with the contiguous canonical range 106..173: **68/68 exact class/boundary matches**. Across those prospective tests there are 50 full records and 18 partial records: 17 left-boundary partials and 1 right-boundary partial (rank 173). There are **0 non-adjacent selected boundaries** and **0 two-sided boundary records** in that prospective range. Exact direct-matrix comparisons total **66,922**, with **0 mismatches**.

## What this does and does not establish

The result strengthens the two-sided adjacent-variable hypothesis substantially and directly searches 51 additional records for a third, non-adjacent boundary mechanism without finding one. It does **not** prove the rule for all 922 gamma-plus records. It also does not confirm the two-simultaneous-sides branch, because no rank through 173 has prospectively exercised such a case. A later exact counterexample remains sufficient to refute the universal form.

## Next falsification target

Keep the A109 rule unchanged. Using target-only adjacent quantities only, search after rank 173 for the first predicted two-sided record. If one exists, freeze it before full-atlas execution. Independently, continue deterministic contiguous full-atlas coverage to search for a non-adjacent KKT boundary.
