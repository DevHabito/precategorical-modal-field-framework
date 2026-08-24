# A109-H11 — Exact Adjacent-Boundary Holdout Review

## Frozen question
H11 preregistered canonical ranks 287..302 as 16 single-rank shards under the unchanged two-sided adjacent-boundary rule. The frozen batch prediction was 11 full-segment cases and 5 proper strict subcomponents, all five with a left `basic_p_{j+1}` boundary, with no right or two-sided case predicted.

## Full-atlas execution
The full atlas completed for 15/16 ranks. Every completed rank matched its frozen class and boundary prediction, with zero direct rational mismatches and zero core/hull failures. Rank 295 exceeded the 55-second execution window. A second identical full-atlas retry later also timed out and produced no result file.

Formal parent-protocol status: `INCOMPLETE_EXECUTION_R295`.

## Rank 295 exact certificate
The frozen prediction for rank 295 was a proper strict subcomponent with left boundary `basic_p_46`. An exact sufficient-certificate audit found:

- target signs: L = -1, witness = +1, R = +1;
- target derivative strictly positive on the full source segment;
- a unique left root bracket, approximately `s* = 0.13235395345023` for readability only;
- 502 required non-target KKT conditions certified strictly positive on the complete source segment;
- 2,012 direct symbolic-vs-matrix rational comparisons, zero mismatches;
- zero exact failures and zero unresolved certificates.

Mathematically, rank 295 therefore supports the frozen prediction.

## Protocol-order deviation
The H11 parent execution policy stated that *repeated* timeout ranks could be handled by a separately preregistered exact sufficient-certificate protocol. H11D was frozen and executed after the first rank-295 timeout, before the second identical full-atlas retry was run. The second retry subsequently also timed out (exit 124).

This does not create a mathematical contradiction, and the H11D certificate remains valid as exact evidence. However, it is a preregistration-order deviation. For that reason rank 295 is **not counted as clean prospective confirmatory evidence** in the strict accounting below.

## Strict accounting
- Clean completed full-atlas ranks: 15/15 exact class and boundary matches.
- Rank 295: mathematically resolved in support, but excluded from clean preregistration-compliant confirmation.
- All 16 mathematical outcomes: 11 full, 5 partial; all five partial boundaries are left adjacent; no right, two-sided, or non-adjacent boundary occurred.
- Direct comparisons across all mathematical resolutions: 26,697; mismatches: 0.
- Direct comparisons from clean full-atlas ranks only: 24,685; mismatches: 0.

## Cumulative status after H11
Before H11, ranks 106..286 comprised 181 prospectively resolved records with 234,171 exact direct comparisons and zero mismatches. Adding only the 15 clean H11 full-atlas records gives 196 clean prospectively confirmed records and 258,856 direct comparisons with zero mismatches. Including rank 295 as mathematical-but-not-clean evidence gives 197 mathematically resolved records through rank 302 and 260,868 direct comparisons with zero mismatches.

The two-sided adjacent-boundary rule is therefore still unrefuted in the tested catalogue, but H11 does **not** justify an all-922 theorem.

## Next frozen holdout
A109-H12 is frozen for canonical ranks 303..318 before any atlas outcome is inspected. It predicts 12 full cases and 4 partial cases: two left-adjacent boundaries and, importantly, two right-adjacent boundaries (ranks 303 and 313). This gives the next holdout stronger leverage against the current rule than H11, because the rarer right branch is prospectively exercised twice.
