# A109 — Post-A108 Refutation and Two-Sided Adjacent-Boundary Audit

## Baseline
Before this continuation, `python tools/verify_results.py` returned 68 audit results, 1013 gates, 110 figures, zero failures, status `PASS`.

## 1. A108 one-sided sufficiency claim was refuted
The already-frozen A108 continuation was resumed at canonical ranks 98..105 without changing the predictor. The shard verdict was `REFUTED_A108_P5`.

The exact counterexample is canonical rank 105:
- `M = 119`, `j = 22`, witness `131/1000`
- source interval `(129/1000, 133/1000)`
- old frozen endpoint-only rule predicted `full_segment_coverage` because `basic_p_23` stayed positive
- the full exact atlas returned `proper_strict_subcomponent`
- selected boundary: **right `basic_p_22`**
- at the source right endpoint `basic_p_22` is negative while it is positive at the witness
- the selected root is unique and simple with negative derivative across its exact isolating bracket
- independent direct rational matrix regression for the record: 988 comparisons, 0 mismatches, 0 positivity failures, 0 outside-sign failures

Therefore the strong statement “only `basic_p_(j+1)` can be the first boundary” is false. No rescue of that statement is permitted.

## 2. Post-hoc development diagnostic (ranks 1..105)
After accepting the refutation, a new candidate was formulated using the two adjacent basic variables:
- upper adjacent `basic_p_(j+1)`, increasing with the probe, candidate left boundary;
- lower adjacent `basic_p_j`, decreasing with the probe, candidate right boundary.

On the already-observed development set ranks 1..105, this two-sided rule matches 105/105 classes and 105/105 selected boundary sets. There are 75 full and 30 partial records; 29 partial boundaries are left `basic_p_(j+1)` and one is the new right `basic_p_j` counterexample at rank 105. Both monotonicity certificates hold on all 105 development records.

This is **development evidence only**, not prospective confirmation.

## 3. A109 prospective holdout: ranks 106..121
The two-sided rule was frozen before full-atlas execution. Preregistration SHA-256:

`67b286eb336f2cc5ea5831fe4531368d3e36147befa7aefd0a61d7e3feb55829`

Frozen prediction counts: 12 full and 4 partial. The two shards 106..113 and 114..121 both returned `PASS_A109_TWO_SIDED_HOLDOUT`.

Combined result:
- 16/16 exact class matches
- 16/16 exact boundary-set matches
- 12 full, 4 partial
- 13,624 exact direct-matrix comparisons
- 0 direct mismatches
- 0 core-certificate failures
- 0 nonselected-hull failures

All four partials in this holdout were left-boundary cases. Thus this holdout did **not by itself** prospectively exercise the newly introduced right-boundary branch.

Both shards were independently rerun. After removing runtime-only `seconds`, each rerun was structurally identical to its first run.

## 4. Dedicated prospective test of the right-boundary branch
To avoid claiming support for a branch that had not appeared in ranks 106..121, a separate target-only selection was frozen:

“Starting after rank 121, choose the first canonical record for which the already-frozen two-sided target-only rule predicts a single right `basic_p_j` boundary, without inspecting any other KKT condition or the full atlas.”

The first such record was frozen as rank 173:
- `M = 171`, `j = 31`
- predicted class: `proper_strict_subcomponent`
- predicted selected boundary: right `basic_p_31`

Preregistration SHA-256:

`857d75f1890bbba742f709269b924561c072f7f9e3c573465568159b1a646918`

Full exact execution returned:
- `PASS_A109_R1_RIGHT_BRANCH`
- observed class exactly `proper_strict_subcomponent`
- observed selected boundary exactly right `basic_p_31`
- 1,404 independent exact direct-matrix comparisons
- 0 mismatches
- 0 positivity failures
- 0 outside-sign failures

The right root is approximately `0.13291244861665016` for readability; certification uses an exact rational bracket.

The result was rerun independently and is structurally identical after removing runtime-only timing.

## 5. Current truth status
1. The A108 **one-sided** universal sufficiency hypothesis is **refuted** by rank 105.
2. A **two-sided adjacent-variable mechanism** is now the stronger candidate: `p_(j+1)` can terminate the strict component on the left and `p_j` can terminate it on the right.
3. The two-sided rule is a perfect post-hoc classifier on ranks 1..105, receives prospective support on 16/16 ordinary holdout records (106..121), and its newly added right branch receives a separate prospective success at rank 173.
4. This is **not** yet an all-922 theorem. A later record may still expose a third KKT boundary mechanism or failure of the two-sided classification.

## 6. Next falsification target
Do not resume the refuted one-sided A108 claim. The next rigorous programme should keep the A109 two-sided rule frozen and search deterministically for:
- the first prospective record predicted to have two simultaneous sides, if such a record exists; or
- a record where a non-adjacent KKT condition becomes a selected boundary; or
- enough unchanged-rule holdouts to justify attempting a symbolic theorem for a precisely stated subclass.

The priority remains falsification, not accumulation of favorable cases.
