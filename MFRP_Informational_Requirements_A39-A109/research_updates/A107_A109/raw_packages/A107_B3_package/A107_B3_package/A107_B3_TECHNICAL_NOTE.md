# A107-B3 — Prospective Exact Gamma-Plus Batch Audit

## Status

**Primary verdict:** `PASS_BATCH_LOCAL_STABILITY`

**Upper-adjacent boundary hypothesis:** `SUPPORT_BATCH`

**Previously preregistered finite M mod 5 rule:** `REFUTED_B3_FINITE_RULE`

This audit was run only after freezing `A107_B3_PREREGISTRATION.json`. Its SHA-256 is:

`1eb7952fc98af4a865ef9943ff960ee27c53e74fc7bb7742e13dcae5677917d9`

The repository baseline was independently checked before the B3 execution with `tools/verify_results.py`: 68 audit results, 1013 gates, 110 figures, zero failures, status `PASS`.

## Frozen question

For canonical `legacy_three_band_gamma_plus` ranks 18..25, selected in the established deterministic order `(maximum, compressed_maximizer_contact, witness)`, does each source witness lie in a nonzero open strict-KKT component under the frozen A102 architecture? For every proper strict subcomponent, is the selected internal boundary still `basic_p_{j+1}`? The previously preregistered residue rule was carried forward unchanged and tested only on its declared scope.

No replacement, rank change, batch resizing, support/active-band change, tolerance change, boundary-rule edit, residue-rule edit, or residue-3 prediction was permitted after inspection.

## Exact B3 results

| canonical rank | M | j | M mod 5 | phase | observed class | selected boundary | residue prediction |
|---:|---:|---:|---:|---|---|---|---|
| 18 | 35 | 8 | 0 | unique_b_plus_1 | full_segment_coverage | — | **mismatch** (predicted partial) |
| 19 | 36 | 8 | 1 | unique_b_plus_1 | proper_strict_subcomponent | `basic_p_9` (left) | **mismatch** (predicted full) |
| 20 | 37 | 8 | 2 | unique_b_plus_1 | full_segment_coverage | — | match |
| 21 | 38 | 8 | 3 | unique_b_plus_1 | full_segment_coverage | — | out of preregistered scope |
| 22 | 39 | 8 | 4 | unique_b_plus_1 | full_segment_coverage | — | **mismatch** (predicted partial) |
| 23 | 41 | 9 | 1 | unique_b_plus_1 | full_segment_coverage | — | match |
| 24 | 42 | 9 | 2 | unique_b_plus_1 | full_segment_coverage | — | match |
| 25 | 43 | 9 | 3 | unique_b_plus_1 | full_segment_coverage | — | out of preregistered scope |

The batch therefore contains 7 full source-segment coverages and 1 proper strict subcomponent.

## Primary local-stability test

All 8 records satisfy the exact frozen local-stability criteria. The batch reconstructs 694 KKT conditions and performs 2163 direct exact checkpoint comparisons between the rank-one symbolic reconstruction and independent direct-matrix evaluation.

- per-record success: 8/8
- direct exact comparisons: 2163
- direct mismatches: 0
- witness failures: 0
- unresolved records: 0
- core-certificate failures: 0
- nonselected-hull failures: 0
- root-ordering failures: 0
- root-certification failures: 0
- direct interior positivity failures: 0
- direct outside-sign failures: 0

Hence the primary B3 verdict is `PASS_BATCH_LOCAL_STABILITY`.

## Exact partial record

The only B3 partial record is canonical rank 19:

- source key: `M=36|b=7|phase=unique_b_plus_1|side=full|s=131/1000|j=8`
- witness: `131/1000`
- source segment: `(129/1000, 133/1000)`
- frozen support architecture: upper adjacent atom is `j+1 = 9`
- selected boundary: `basic_p_9`
- boundary side: left

The unique simple root is isolated in the exact rational bracket

`1950177729719599999337431/15111572745182864683827200`

< s_* <

`156014218377567999946994481/1208925819614629174706176000`

with bracket width

`1/1208925819614629174706176000`.

Numerically only for orientation, `s_* ≈ 0.12905193672453852`, while the witness is `0.131`.

The exact outside counterexample on the left is

`19497853069240947717755699/151115727451828646838272000`,

where the selected condition `basic_p_9` has negative sign. Thus the loss of strict feasibility outside the certified component is independently witnessed.

## Upper-adjacent-atom boundary hypothesis

B3 contains one proper strict subcomponent. Its selected boundary is exactly

`basic_p_9 = basic_p_{j+1}`.

Therefore the preregistered boundary mechanism receives `SUPPORT_BATCH` in B3. This does not prove a universal theorem: B3 contributes one additional partial case only.

Across A107-MIN + B1 + B2 + B3, the cumulative exact finite record is now:

- 25/25 canonical gamma-plus witnesses locally stable under their frozen A102 architectures;
- 17 full source-segment coverages;
- 8 proper strict subcomponents;
- 8/8 observed selected internal boundaries equal `basic_p_{j+1}` and occur on the left;
- 1647 reconstructed KKT conditions;
- 5379 direct exact checkpoint comparisons;
- 0 direct mismatches.

These are finite audited facts, not an all-922 theorem.

## Prospective residue rule: refuted

The preregistered finite rule carried from B2 predicted, only in phase `unique_b_plus_1` and only for residues in `{0,1,2,4}`:

- residues 0 or 4 -> `proper_strict_subcomponent`;
- residues 1 or 2 -> `full_segment_coverage`.

B3 has six in-scope records. Three match and three mismatch. The exact mismatches are:

1. M=35, residue 0: predicted partial, observed full;
2. M=36, residue 1: predicted full, observed partial;
3. M=39, residue 4: predicted partial, observed full.

A single mismatch would have refuted the finite B3 rule. There are three. Therefore the correct verdict is unambiguously `REFUTED_B3_FINITE_RULE`.

The residue-3 observations at M=38 and M=43 are reported but are not counted for or against the rule because residue 3 was explicitly outside the preregistered scope.

No replacement modular rule is introduced here. Any new classifier would be post-hoc and must be preregistered separately before prospective testing.

## Deterministic rerun

The complete B3 audit was executed twice independently with separate output paths. The resulting JSON files are byte-for-byte identical.

SHA-256 of both runs:

`b23157ac018285527d35869a1907ee1b7841a8481d06f635272a4938361d30a2`

This confirms deterministic reproducibility of the implemented B3 audit in the current runtime.

## Scope

B3 establishes only the exact local-continuum classification of canonical gamma-plus ranks 18..25 under the existing A95/A102 source segments and frozen A102 architecture. It does not establish an all-M theorem, an all-922 theorem, a residue-3 rule, a rule for other phases, or a physical claim.
