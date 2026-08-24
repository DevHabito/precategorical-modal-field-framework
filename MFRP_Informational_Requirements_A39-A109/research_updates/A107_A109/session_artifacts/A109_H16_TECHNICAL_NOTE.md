# A109-H16 — Unchanged Two-Sided Adjacent-Boundary Holdout

## Status

**Mathematical verdict:** `RESOLVED_SUPPORT_A109_H16_MIXED_EXACT_PROTOCOL`

**Original full-atlas protocol:** 14/16 completed; ranks 378 and 382 each produced no result in two identical preregistered 55-second attempts. Their full-atlas status remains incomplete.

**Fallback protocol:** after both repeated timeouts, `A109_H16D_PREREGISTRATION.json` was frozen. Exact sufficient certificates then resolved ranks 378 and 382 without changing predictions, supports, intervals, or tolerances.

## Frozen question

For canonical gamma-plus ranks 367..382, does the unchanged adjacent-boundary rule continue to predict the exact strict-KKT class and selected boundary set? A non-adjacent selected KKT obstruction or any class/boundary mismatch would refute the rule on this holdout.

Frozen batch prediction: 12 full, 4 partial; 3 left boundaries, 1 right boundary, 0 two-sided.

## Exact result

- class matches: **16/16**
- boundary-set matches: **16/16**
- full source-segment coverage: **12**
- proper strict subcomponents: **4**
- left adjacent boundaries: **3**
- right adjacent boundaries: **1**
- two-sided boundaries: **0**
- non-adjacent selected boundaries: **0**
- direct exact comparisons: **30,728**
- direct mismatches: **0**
- full-atlas core failures: **0**
- full-atlas hull failures: **0**
- full-atlas root failures: **0**
- H16D non-target conditions certified: **1,190**
- H16D exact certificate failures: **0**
- H16D unresolved certificates: **0**

## Partial records

- rank 373: left `basic_p_53`
- rank 374: left `basic_p_53`
- rank 378: right `basic_p_52`
- rank 382: left `basic_p_54`

Ranks 373 and 374 were resolved by the full atlas. Ranks 378 and 382 were resolved by H16D after repeated full-atlas timeouts.

## Prospectively important right-boundary case: rank 378

Frozen source key: `M=293|b=51|phase=b_plus_1_to_b_plus_2|side=left|s=33/250|j=52`.

The exact target signs are `{'L': 1, 'witness': 1, 'R': -1}` and the derivative certificate proves strict decrease of the right-boundary target. A unique root is rationally bracketed; its midpoint is approximately `0.132856610136208` for orientation only. Direct matrix checks agree exactly at all four frozen probes, and the outside-right probe has exactly `basic_p_52` nonpositive.

Thus the preregistered prediction `right basic_p_52` is mathematically supported. The full-atlas execution itself remains incomplete because both preregistered attempts timed out without result.

## Rank 382

Frozen source key: `M=294|b=51|phase=b_plus_1_to_b_plus_2|side=right|s=33/250|j=53`.

The target `basic_p_54` has signs `{'L': -1, 'witness': 1, 'R': 1}` with certified strict increase and one rationally bracketed left root. Its midpoint is approximately `0.131865286215500` for orientation only. The outside-left direct probe has exactly `basic_p_54` nonpositive; all direct symbolic-vs-matrix comparisons agree exactly.

## Independent consistency check

`A109_H16_INDEPENDENT_CONSISTENCY_CHECK.json` re-reads the raw full-atlas and H16D artifacts. Result: **109/109 checks passed, 0 failures**.

The repository baseline was independently rerun with `tools/verify_results.py`: 68 audit results, 1013 gates, 110 figures, zero failures, status `PASS`.

## Cumulative prospective accounting through rank 382

- mathematically resolved consecutive ranks 106..382: **277**
- strict-clean prospective count: **276**
- full: **193**
- partial: **84**
- left adjacent: **78**
- right adjacent: **6**
- two-sided: **0**
- non-adjacent: **0**
- exact direct comparisons: **410,726**
- direct mismatches: **0**

The one-count gap between mathematical and strict-clean totals remains solely the previously documented rank-295 protocol-order issue; H16 adds 16 clean prospective resolutions.

## Scope and limit

H16 does **not** establish an all-922 theorem. It supplies another finite prospective holdout in which the unchanged adjacent-boundary rule survives exact attempts at refutation. A future exact non-adjacent boundary or class/boundary mismatch would still refute the universal form.

## Next frozen holdout

`A109_H17_PREREGISTRATION.json` freezes ranks 383..398 before any full-atlas outcomes are inspected. Prediction: 11 full, 5 partial, all 5 partials left-adjacent; no right or two-sided case is predicted. Its SHA-256 is `6ce9427d24839288d758f6993f1796d05459cb5d221d8c033da7afcaf51e0e82`.
