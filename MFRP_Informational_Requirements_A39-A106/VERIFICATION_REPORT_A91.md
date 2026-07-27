# Verification Report — A39–A91

**Status:** PASS  
**Main audits:** 53  
**Registered gates:** 697/697  
**English figures:** 95  
**Integrity tests:** 31/31

## A91

- Audit: `A91_EXACT_FOUR_TERM_OFFSET_THREE_MECHANISM`
- Verdict: `PASS_EXACT_FOUR_TERM_OFFSET_THREE_CLASSIFIER_AND_PARITY_SCREENING_OBSTRUCTION`
- Gates: 15/15
- Source grid: `10<=M<=520`, nine rational probes
- A90 source cells: 4,599
- Eligible `b+2` versus `b+3` comparisons: 4,563
- Small-support boundary exclusions: 36
- Exact four-core/full-factor sign matches: 4,563/4,563
- Strict core-over-residual dominance: 4,563/4,563
- Exact offset-three cases: 15
- Exact non-offset-three cases: 4,548
- Minimum core-to-residual ratio: `74.9243129638466299807...`
- A85 parity-screen diagnostic: 69 screened cells, 15 true positives, 54 false positives, 0 false negatives

## Verification layers

1. A91 re-runs from the committed A84 factor formulas and A90 exact contact catalogue.
2. Every exact theorem gate uses `fractions.Fraction` arithmetic.
3. The normalized four-core identity is checked cell by cell.
4. The four-core sign, full-factor sign, and A90 offset-three class agree in every eligible cell.
5. The six-term residual is strictly dominated in every eligible cell.
6. The parity-locator screen is labeled as a 120-digit numerical diagnostic rather than an exact theorem.
7. Repository integrity tests, source compilation, JSON parsing, figures, and SHA-256 manifests are replayed after freezing the package.

## Claim boundary

A91 is finite and probe-discrete. It does not prove the classifier on the continuous probe interval, for `M>520`, or for offsets beyond the A90 four-contact strip. It also does not merge compressed-objective contact selection with the full KKT feasibility problem.
