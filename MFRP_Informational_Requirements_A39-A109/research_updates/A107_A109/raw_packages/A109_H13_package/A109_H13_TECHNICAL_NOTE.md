# A109-H13 — Prospective Adjacent-Boundary Holdout

## Frozen protocol
Ranks 319..334 were preregistered before any full-atlas outcomes were inspected. The unchanged two-adjacent-variable rule predicted 8 full and 8 partial cases, all 8 partials with a left boundary and none with a right or two-sided boundary.

Preregistration SHA-256: `24f6ab5bf007089a1c7b04260010406835bd1b9f6bc23ef3ffe0e5af4bedf11a`

## Result
Mixed exact mathematical verdict: **RESOLVED_SUPPORT_A109_H13_MIXED_EXACT_PROTOCOL**.

- class matches: 16/16
- boundary-set matches: 16/16
- observed full: 8
- observed partial: 8
- left boundaries: 8
- right boundaries: 0
- two-sided boundaries: 0
- non-adjacent selected boundaries: 0
- direct exact comparisons: 30092
- direct mismatches: 0

The eight partial ranks are 319, 320, 321, 327, 330, 331, 332, and 333. Their selected boundary is respectively `basic_p_48`, `basic_p_48`, `basic_p_48`, `basic_p_49`, `basic_p_49`, `basic_p_49`, `basic_p_49`, and `basic_p_49`, always on the left.

## Execution distinction
The original full-atlas protocol completed for 13/16 ranks. Ranks 319, 327, and 330 each produced two identical 55-second timeouts with no result file. Only after the two timeouts was an exact sufficient-certificate route preregistered. Those certificates proved the frozen target crossing and positivity of every non-target KKT condition, followed by independent direct rational regression. Thus all 16 ranks are mathematically resolved, but the original full-atlas protocol remains formally incomplete for those three ranks.

Across the three certificate-resolved ranks, 1602 non-target KKT conditions were certified, with zero exact failures and zero unresolved conditions.

## Independent consistency review
A separate artifact-level review ran 75 checks; 75 passed and 0 failed. Status: **PASS**.

## Scope
H13 is a finite prospective holdout result for ranks 319..334. It is not an all-922 theorem and not a physical claim. A later exact non-adjacent boundary would still refute the universal form of the current conjecture.