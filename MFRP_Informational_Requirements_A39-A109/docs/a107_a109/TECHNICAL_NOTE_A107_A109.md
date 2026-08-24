# A107-A109 technical research note

## Scope

This note covers the transition from A106 into the legacy three-band gamma-plus continuum program. It is intentionally conservative about claims: exact counterexamples are treated as refutations, timeouts are treated as execution failures rather than mathematical failures, and mixed exact protocols are kept distinct from completed full-atlas runs.

## A107: opening the gamma-plus continuum family

The canonical gamma-plus records are ordered by `(maximum, compressed_maximizer_contact, witness)`. A107-MIN starts from the first record and uses the A103/A105 exact continuum machinery with the gamma-plus architecture

`P = {0, j, j+1, M}`, `Q = {1, h, h+1}`, active `alpha+`, `beta-`, `gamma+`.

A107-B1/B2/B3 and the structural endpoint holdouts extended this analysis. The early empirical pattern was that partial components were cut on the left by `basic_p_{j+1}`. A simple modular predictor was prospectively refuted in B3 and was not reused.

## A108: exact refutation of the one-sided boundary claim

The one-sided A108 rule claimed, in effect, that only `basic_p_{j+1}` could become the first boundary. Canonical rank 105 refutes that claim exactly. The record has `M=119`, `j=22`, source segment `(129/1000, 133/1000)`, and the exact atlas status `proper_strict_subcomponent`. The selected boundary is **right `basic_p_22`**. Its root is isolated by an exact rational bracket with derivative negative across the bracket. The core certificate passes 248/248 conditions; the independent direct regression performs 988 exact comparisons with zero mismatch and no positivity/outside-sign failures.

That counterexample is not an implementation nuisance. It changes the structural hypothesis.

## A109: two-sided adjacent-boundary candidate

The replacement candidate uses both adjacent variables. Development on ranks 1-105 was explicitly post-hoc. The rule was then frozen and tested on future records.

At the current stored cutoff, ranks 106-414 are mathematically resolved. The cumulative status artifact records:

- 309 mathematically resolved prospective records;
- 308 strict-clean prospective records;
- 215 full source-segment coverages;
- 94 proper strict subcomponents;
- 88 left adjacent boundaries;
- 6 right adjacent boundaries;
- 0 observed two-sided cases;
- 0 observed non-adjacent selected KKT boundaries;
- 475,782 exact direct symbolic-versus-matrix comparisons;
- 0 direct mismatches.

The strict-clean direct-comparison count is 473,770. The one-record difference between mathematical and strict-clean accounting is the documented rank-295 protocol-ordering issue. The mathematical certificate for rank 295 remains valid, but it is not counted as a strict-clean prospective confirmation.

## Full atlas versus exact fallback certificates

As `M` increased, some full-atlas runs exceeded the frozen 55-second wall-clock window. The rule used in later holdouts was: run the frozen single-rank shard; if it times out with no result, repeat the identical shard once; only after two timeouts may a separately preregistered sufficient-certificate protocol be used.

A fallback certificate does not retroactively turn a timeout into a completed full-atlas run. It is a distinct mathematical resolution route. The fallback route requires exact positivity of the common denominator, exact target sign/monotonicity behavior, exact positivity of all non-target KKT numerators over the complete source interval, exact root isolation when a boundary exists, and independent direct rational matrix probes.

## Current epistemic status

The evidence supports a finite conjecture:

> Within the tested legacy three-band gamma-plus records, the first KKT obstruction is controlled by the two basic variables adjacent to the compressed contact: `basic_p_{j+1}` on the left and `basic_p_j` on the right.

This wording is intentionally weaker than a theorem. The current artifacts do not prove that a non-adjacent condition can never win on an untested record, and they do not prove the claim for all 922 gamma-plus records.

## Next frozen test

H19 covers ranks 415-430 and remains unexecuted in this package. It predicts 11 full and 5 partial records. Four partials are predicted to terminate on the left. Rank 428 is frozen as a right-boundary case at `basic_p_56`. Any exact class/boundary mismatch or any non-adjacent selected obstruction is a refutation on that record; an execution/certification failure without an exact contradiction is inconclusive.
