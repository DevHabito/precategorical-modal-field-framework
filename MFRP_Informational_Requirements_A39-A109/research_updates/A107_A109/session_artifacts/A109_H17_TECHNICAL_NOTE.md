# A109-H17 — Unchanged Two-Sided Adjacent-Boundary Holdout

## Status

**Mathematical verdict:** `RESOLVED_SUPPORT_A109_H17_MIXED_EXACT_PROTOCOL`

**Original full-atlas protocol:** 13/16 completed; ranks 392, 395, and 398 each produced no result in two identical preregistered 55-second attempts. Their full-atlas status remains incomplete.

**Fallback protocol:** only after both repeated timeouts for each rank, `A109_H17D_PREREGISTRATION.json` was frozen. Exact sufficient certificates then resolved those three ranks without changing predictions, source intervals, supports, or tolerances.

## Frozen question

For canonical gamma-plus ranks 383..398, does the unchanged adjacent-boundary rule continue to predict the exact strict-KKT class and selected boundary set? Any exact class/boundary mismatch or any selected non-adjacent KKT obstruction refutes the rule on this holdout.

Frozen batch prediction: 11 full, 5 partial; 5 left boundaries, 0 right boundaries, 0 two-sided.

## Exact result

- class matches: **16/16**
- boundary-set matches: **16/16**
- full source-segment coverage: **11**
- proper strict subcomponents: **5**
- left adjacent boundaries: **5**
- right adjacent boundaries: **0**
- two-sided boundaries: **0**
- non-adjacent selected boundaries: **0**
- direct exact comparisons: **32,127**
- direct mismatches: **0**
- full-atlas core failures: **0**
- full-atlas hull failures: **0**
- full-atlas root failures: **0**
- H17D non-target conditions certified: **1826**
- H17D exact certificate failures: **0**
- H17D unresolved certificates: **0**

## Partial records

- rank 385: left `basic_p_54` — full atlas
- rank 386: left `basic_p_54` — full atlas
- rank 392: left `basic_p_55` — H17D after two full-atlas timeouts
- rank 395: left `basic_p_55` — H17D after two full-atlas timeouts
- rank 398: left `basic_p_55` — H17D after two full-atlas timeouts

Ranks 392, 395, and 398 were not counted as completed full-atlas executions. Their mathematical resolution comes from the separately frozen H17D sufficient-certificate protocol.

## H17D exact certificate details

- rank 392: target `basic_p_55`, side `left`, exact signs `{'L': -1, 'witness': 1, 'R': 1}`, certified monotonic derivative, one rationally bracketed root; midpoint approximately `0.132702138996646` for orientation only.
- rank 395: target `basic_p_55`, side `left`, exact signs `{'L': -1, 'witness': 1, 'R': 1}`, certified monotonic derivative, one rationally bracketed root; midpoint approximately `0.131730809711306` for orientation only.
- rank 398: target `basic_p_55`, side `left`, exact signs `{'L': -1, 'witness': 1, 'R': 1}`, certified monotonic derivative, one rationally bracketed root; midpoint approximately `0.130150387628702` for orientation only.

All non-target KKT numerators in the fallback ranks were certified strictly positive on the complete frozen source segment. Four independent rational direct probes per fallback rank matched the symbolic reconstruction exactly, and the outside probe failed only at the frozen target condition.

## Independent consistency check

`A109_H17_INDEPENDENT_CONSISTENCY_CHECK.json` re-reads the raw artifacts and frozen predictions: **71/71 checks passed, 0 failures**.

The repository baseline was rerun with `tools/verify_results.py`: 68 audit results, 1013 gates, 110 figures, zero failures, status `PASS`.

## Cumulative prospective accounting through rank 398

- mathematically resolved consecutive ranks 106..398: **293**
- strict-clean prospective count: **292**
- full: **204**
- partial: **89**
- left adjacent: **83**
- right adjacent: **6**
- two-sided: **0**
- non-adjacent: **0**
- exact direct comparisons: **442,853**
- direct mismatches: **0**

The one-count gap between mathematical and strict-clean totals remains solely the previously documented rank-295 protocol-order issue. H17 adds 16 clean prospective resolutions.

## Scope and limit

H17 does **not** establish an all-922 theorem. It is another finite prospective holdout in which the unchanged adjacent-boundary classifier survives exact attempts at refutation. A single future exact non-adjacent boundary or class/boundary mismatch remains sufficient to refute the universal form.

## Next frozen holdout

`A109_H18_PREREGISTRATION.json` freezes ranks 399..414 before any full-atlas outcome is inspected. Prediction: 11 full, 5 partial, all 5 partials left-adjacent; no right or two-sided case is predicted. SHA-256: `ea471ffc0a5e62c2ec0c15adea3d759b424802e7d35bcd92f13fb90e67cd6ef3`.
