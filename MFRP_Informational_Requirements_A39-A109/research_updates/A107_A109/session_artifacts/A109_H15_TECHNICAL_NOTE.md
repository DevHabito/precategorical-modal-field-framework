# A109-H15 — Unchanged Two-Sided Adjacent Boundary Holdout

## Frozen protocol

H15 was frozen before any full-atlas outcome for canonical ranks 351..366. The frozen prediction was 11 full source-segment coverages and 5 proper strict subcomponents, all five with a left adjacent boundary, with no right-boundary or two-sided case predicted. The same two-target rule and exact adjudication criteria from H14 were retained unchanged.

Preregistration SHA-256:

`7c12da017762a0cef7733172991be68f3d621488dedf579be038abd3631d630b`

## Execution

All 16 preregistered single-rank full-atlas shards ultimately completed under the frozen protocol. Ranks 352, 360, and 361 produced no result on their first 55-second-window attempt; each was repeated once identically, as allowed prospectively, and completed. No alternate sufficient-certificate protocol was used.

## Exact result

**Verdict:** `PASS_A109_H15_FULL_ATLAS_HOLDOUT`

- class matches: 16/16
- exact boundary-set matches: 16/16
- full source-segment coverage: 11
- proper strict subcomponents: 5
- left adjacent boundaries: 5
- right adjacent boundaries: 0
- two-sided boundaries: 0
- non-adjacent selected boundaries: 0
- direct rational comparisons: 30313
- direct mismatches: 0
- core-certificate failures: 0
- hull-certificate failures: 0
- root failures: 0

The partial ranks are 353, 354, 355, 363, and 364. Their selected boundaries are exactly `basic_p_51` for ranks 353..355 and `basic_p_52` for ranks 363..364, all on the left.

## Exact root certificates

- rank 353: `basic_p_51` left, exact bracket `157867916749749680072485333/1208925819614629174706176000 < s* < 78933958374874840036242667/604462909807314587353088000`, decimal orientation `~ 0.130585280079528`.
- rank 354: `basic_p_51` left, exact bracket `157058899601211756777110647/1208925819614629174706176000 < s* < 19632362450151469597138831/151115727451828646838272000`, decimal orientation `~ 0.129916076779035`.
- rank 355: `basic_p_51` left, exact bracket `38996568956996828038702219/302231454903657293676544000 < s* < 155986275827987312154808877/1208925819614629174706176000`, decimal orientation `~ 0.129028823189260`.
- rank 363: `basic_p_52` left, exact bracket `39432084243007077172379427/302231454903657293676544000 < s* < 157728336972028308689517709/1208925819614629174706176000`, decimal orientation `~ 0.130469822393493`.
- rank 364: `basic_p_52` left, exact bracket `156936354056197304976319481/1208925819614629174706176000 < s* < 78468177028098652488159741/604462909807314587353088000`, decimal orientation `~ 0.129814709480044`.

Each selected root is certified as unique and simple in its exact rational bracket, and each partial record has an exact rational outside point where the selected condition is negative.

## Independent regression

The exact symbolic reconstruction was checked against independent direct rational matrix evaluation at the audit checkpoints. Across H15 there were 30313 comparisons and zero discrepancies.

An independent artifact consistency pass checked preregistration hashes, ranks, frozen classes, frozen boundary sets, empty failure lists, direct mismatches, core failures, hull failures, and root failures: 144/144 checks passed.

The baseline repository verifier also remained `PASS`: 68 audit results, 1013 gates, 110 figures, zero failures.

## Cumulative status

Through canonical rank 366, the prospective two-adjacent-variable programme has mathematically resolved 261 consecutive ranks 106..366. Of those, 260 count as strict-clean prospective tests because of the previously documented rank-295 protocol-order exception. The mathematical distribution is 181 full and 80 partial, with 75 left adjacent boundaries, 5 right adjacent boundaries, zero two-sided cases, and zero observed non-adjacent selected KKT boundaries. Total exact direct comparisons are 379,998 with zero mismatches.

This remains a finite prospective record, not an all-922 theorem and not a physical claim.

## Next frozen holdout

A109-H16 has been frozen for ranks 367..382 before any full-atlas outcome was inspected. It predicts 12 full and 4 partial cases: three left boundaries and one right boundary (rank 378, `basic_p_52`), with no two-sided case. This is useful because it prospectively exercises the rarer right-boundary branch again without changing the rule.
