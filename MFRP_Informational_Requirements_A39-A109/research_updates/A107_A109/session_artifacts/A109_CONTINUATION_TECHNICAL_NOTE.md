# A109 Continuation — H3, H4 diagnostic, exhaustive target-only scan, and R2

## Scientific status

The A109 two-adjacent-variable rule was kept unchanged:

- `basic_p_{j+1}` is the candidate left boundary;
- `basic_p_j` is the candidate right boundary;
- both negative endpoint target signs would predict a two-sided strict component;
- both positive endpoint target signs predict full source-segment coverage.

No non-adjacent KKT condition or full-atlas outcome is used to generate predictions.

## Repository baseline

Immediately before the continuation, `python tools/verify_results.py` returned:

- audit results: 68
- gates: 1013
- figures: 110
- failures: 0
- status: PASS

## A109-H3: deterministic ranks 174..181

Preregistration SHA-256:

`2d9247f90804bff38cddd3c744c8a83a98dc609c2d603c34bb2fa87792fd2e1a`

The eight ranks were frozen before full-atlas execution. The scientific prediction was not changed after outcomes.

Result:

- exact class/boundary matches: 8/8
- full source-segment coverage: 6
- proper strict subcomponents: 2
- both partial cases had exactly the predicted left boundary `basic_p_33`
- direct exact matrix comparisons: 9,310
- direct mismatches: 0
- core certificate failures: 0
- hull certificate failures: 0

A frozen two-record execution unit timed out without a result file. It was repartitioned only for execution into single-record units after an execution manifest was frozen. No rank, prediction, criterion, support, or tolerance changed.

Formal H3 verdict: `PASS_A109_H3_TWO_SIDED_HOLDOUT`.

## Exact target-only scan after rank 173

A faster exact implementation was written to compute only the two A109 target numerators and common denominator. Before the catalogue scan, it was algebraically regression-checked against the original `rank_one_gamma_plus_conditions` implementation on ranks 174..181.

Scan SHA-256:

`86e00691027e8f51d2882a053cd47e697da31bc059179701217fe19c33bc0c6f`

Ranks scanned: 174..922 (749 records).

Target-only predictor output:

- classifiable: 749/749
- predicted full: 488
- predicted partial: 261
- predicted left-only boundary: 237
- predicted right-only boundary: 24
- predicted two-sided boundary: 0

This is **not** a full-atlas classification of ranks 174..922. It is an exhaustive exact statement about what the frozen A109 target-only predictor says on those records.

Therefore the two-sided branch cannot be prospectively exercised by selecting a target-only-predicted two-sided record from the remaining A102 gamma-plus catalogue: there is no such record in ranks 174..922.

## A109-R2: second prospective right-boundary challenge

Using only the frozen target-only scan, the first post-173 rank predicted to have a single right boundary was selected before full-atlas inspection:

- canonical rank: 206
- `M = 194`
- `j = 35`
- predicted class: `proper_strict_subcomponent`
- predicted boundary: right `basic_p_35`

Preregistration SHA-256:

`75e400b94e7a27cc15b5813085928b5da7c2f7bed62780eeb60ac8c97f3327f6`

Full-atlas result:

- class: `proper_strict_subcomponent`
- selected boundary: exactly right `basic_p_35`
- core failures: 0
- hull failures: 0
- direct exact matrix comparisons: 1,588
- direct mismatches: 0
- direct positivity failures: 0
- outside-sign failures: 0

Verdict: `PASS_A109_R2_RIGHT_BRANCH`.

The R2 audit was rerun independently. After removing runtime duration only, the two JSON results are structurally identical with normalized SHA-256:

`43ed32093970ef9e86ed572d832357cf72a2b0e6bf863dcba66f6dbe208be79c`

## A109-H4: ranks 182..189 and the rank-183 execution obstruction

H4 was frozen before full-atlas outcomes.

Preregistration SHA-256:

`804612fe7a9455b626721804b382f7a7e5dfb6e2fc29187ab3455e762bd77a3b`

Frozen predictions:

- 5 full
- 3 partial, all predicted left `basic_p_34`

Full-atlas execution completed for ranks 182 and 184..189:

- completed ranks: 7
- matches: 7/7
- completed direct exact comparisons: 8,497
- direct mismatches: 0
- observed partials at 184 and 185: exactly left `basic_p_34`

Rank 183 was different computationally. The preregistered full-atlas execution timed out twice and produced no result file. Therefore, by the frozen H4 protocol, H4 is formally:

`INCONCLUSIVE_EXECUTION_R183`

It must **not** be relabelled a formal full-atlas PASS.

### Independent exact diagnostic for rank 183

After the atlas timeouts and before running a different mathematical route, an independent sufficient-certificate diagnostic was preregistered.

Diagnostic preregistration SHA-256:

`fe222cf6aac119e2bc745a5f1e57cc16fe7c27ed7e8511d9dbce39d879a6e25c`

Frozen parent prediction:

- rank 183
- `M = 177`, `j = 33`
- partial
- left boundary `basic_p_34`

The diagnostic did not enumerate the full root atlas. It instead required:

1. positive common denominator on the entire source interval;
2. strictly increasing `basic_p_34` numerator;
3. negative target sign at the lower endpoint and positive sign at the witness;
4. every other KKT numerator strictly positive on the entire source interval;
5. an exact rational sign-changing bracket for the unique target root;
6. independent direct-matrix checks inside and outside the certified component.

Result:

- non-target KKT conditions certified: 362
- non-target failures: 0
- non-target unresolved: 0
- exact target root bracket obtained by rational monotone bisection
- direct exact comparisons: 1,089
- direct mismatches: 0
- verdict: `RESOLVED_SUPPORT_R183_LEFT_BOUNDARY`

This independently settles the mathematical class/boundary in support of the already-frozen prediction, but it does **not** retroactively convert the original H4 full-atlas protocol into a completed PASS.

## Current prospective accounting

Using a uniform completed full-atlas protocol, the contiguous range 106..182 is now:

- 77 prospectively tested records
- 77/77 class/boundary matches
- 77,321 direct exact comparisons
- 0 direct mismatches

If the separately preregistered exact sufficient-certificate resolution of rank 183 is allowed as a mixed exact method, then ranks 106..189 are mathematically resolved:

- 84 records
- 84/84 rule matches
- 61 full
- 23 partial
- 22 left-boundary partials
- 1 right-boundary partial
- 85,818 direct exact comparisons
- 0 direct mismatches

Rank 206 adds a second independent prospective right-boundary success, but ranks 190..205 have not yet been full-atlas covered, so rank 206 is not part of a contiguous full-atlas interval.

## What is established and what remains open

Supported:

- the unchanged A109 two-adjacent-variable rule has not yet been contradicted by any prospectively resolved record in this continuation;
- the right-boundary mechanism has now passed a second separately preregistered future challenge at rank 206;
- no non-adjacent selected boundary was found in the completed H3/H4 records;
- exact target-only scanning shows that no two-sided target prediction exists anywhere after rank 173 in this finite catalogue.

Not established:

- no all-922 full-atlas theorem exists yet;
- target-only prediction is not equivalent to full KKT certification until non-target inequalities are proved or audited;
- a non-adjacent KKT boundary may still occur in an unexecuted record;
- the original H4 full-atlas protocol remains formally incomplete at rank 183 even though the rank itself has been mathematically resolved by an independent exact certificate.

## Next falsification target

The appropriate next step is not to invent a new classifier. Keep A109 unchanged and continue deterministic full-KKT coverage after rank 189, with special attention to the gap 190..205 leading up to the already-preregistered right-boundary rank 206. The purpose is to search for the first non-adjacent KKT boundary or any exact mismatch. A single exact counterexample is sufficient to refute the universal form.
