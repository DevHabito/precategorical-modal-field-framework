# A80–A114 longitudinal scientific audit — 2026-09-13

## Final verdict

**PASS WITH EXPLICIT HISTORICAL REFUTATION AND SCOPE QUALIFICATIONS.**

The promoted mathematical chain from A80 through A114-B2-C2 is internally coherent under its declared contracts. A108 is **not** passed: its universal one-sided boundary conjecture is exactly refuted and remains marked `REFUTED_SUPERSEDED`. No promoted A110–A114 theorem dependency on that false rule was detected.

The initial review also found that `research_updates/A114/README.md` was stale and still described the pre-B2-B/C1/C2 frontier. That documentation finding has now been **resolved** in commit `f78f923aa91b5e0772548825d360c40b064d0705`.

This audit is not a fresh rerun of every expensive historical computation. It reviews committed theorem/result artifacts, stored verifier reports, declared contracts, exact certificates, logical-composition audits, preserved counterexamples, dependency statements and current promoted A114 files.

---

## What was audited

Four ledgers were kept separate:

1. **mathematical validity** — proved, refuted, pointwise, finite, continuum, or open;
2. **scope** — finite grid, finite continuum, rational witness, frozen architecture, analytic tail, or full LP;
3. **dependency** — circularity, reversed implications, and downstream reuse of false premises;
4. **provenance** — independent reconstructions, exact arithmetic, negative controls, manifests and replay limitations.

The review specifically attacked these known failure modes:

- compressed maximizer confused with a feasible/full-KKT basis;
- finite witness or census promoted to a continuum/all-M theorem;
- determinant/sign information proved under primal positivity reversed to prove primal positivity;
- a falsified historical conjecture silently retained downstream;
- degenerate zero boundaries silently absorbed into strict theorems;
- fitted/numerical thresholds used as analytic premises;
- human-facing documentation drifting from promoted mathematics.

---

## Audit ledger A80–A114

| Stage | Audit classification | Essential scope / finding |
|---|---|---|
| A80 | `CERTIFIED_FINITE_LOCAL_ATLAS` | Exact local compression atlas for selected contacts; not an all-M formula. |
| A81 | `CERTIFIED_FINITE_ALGEBRAIC_REDUCTION` | Exact two-variable reduction; primitive-normalization caveat retained. |
| A82 | `CERTIFIED_FINITE_LOCATOR_WITH_FEASIBILITY_EXCEPTIONS` | Eight compressed-maximizer primal-feasibility exceptions prove that compressed maximum != automatic KKT basis. |
| A83 | `CERTIFIED_LOCAL_CONTINUUM_FACTOR_ATLAS_WITH_NEGATIVE_RESULT` | Exact local factor atlas; global discrete concavity explicitly rejected. |
| A84 | `CERTIFIED_REDUCTION_PLUS_FINITE_STRESS` | Ten-term k-space reduction; coefficient-only variation proof route rejected as insufficient. |
| A85 | `CERTIFIED_DOMINANT_BALANCE_WITH_COUNTEREXAMPLE` | Parity dominant balance; exact `M=12` counterexample blocks universal small-support extrapolation. |
| A86 | `CERTIFIED_FINITE_THREE_CONTACT_LOCALIZER` | Valid only in declared finite range through `M<=300`. |
| A87 | `CERTIFIED_CLASSIFIER_WITH_REJECTED_GLOBAL_MONOTONICITY` | Classifier survives; global factor monotonicity is not promoted. |
| A88 | `CERTIFIED_FINITE_STRESS_AND_ASYMPTOTIC_LEADING_LIMITS` | Strong finite/asymptotic evidence, not itself an all-M theorem. |
| A89 | `CERTIFIED_ANALYTIC_LOCAL_SECANT_TAIL_THEOREM` | Analytic full-window statement for `M>=521`; threshold stated as sufficient, not minimal. |
| A90 | `CERTIFIED_FINITE_GRID_ONE_VARIATION` | Exact finite-grid one-variation; fifteen counterexamples preserve the limit of A86. |
| A91 | `CERTIFIED_FINITE_OFFSET3_CLASSIFIER` | Offset-three cells resolved; earlier locator not promoted as an exact rounding law. |
| A92 | `CERTIFIED_CONTINUUM_CELL_ATLAS` | 858 algebraic continuum cells; repairs limitations of the earlier rational-probe grid. |
| A93 | `CERTIFIED_SELECTED_CELL_GLOBAL_COMPRESSED` | Selected cells promoted to full compressed-maximizer statements. |
| A94 | `CERTIFIED_FINITE_SUPPORT_CONTINUUM_GLOBAL_COMPRESSED` | Full finite-support continuum one-variation, explicitly **compressed-objective / non-KKT**. |
| A95 | `CERTIFIED_RATIONAL_WITNESS_LIFT_OBSTRUCTION` | 83 lift obstructions found; missing active set not assumed; no continuum claim. |
| A96 | `CERTIFIED_POINTWISE_FULL_LP` | First obstruction resolved by exact unrestricted full-LP KKT. |
| A97 | `CERTIFIED_ENDPOINT_INTERVAL_PLUS_POINTWISE_RESOLUTION` | Endpoint-released interval theorem where proved; seven q0-entry residuals retained. |
| A98 | `CERTIFIED_POINTWISE_FULL_LP` | First q0/q1 residual resolved pointwise. |
| A99 | `CERTIFIED_Q0Q1_CONTINUUM_WITH_RESIDUALS` | Gamma-inactive q0/q1 components promoted only where certified; residuals preserved. |
| A100 | `CERTIFIED_POINTWISE_GAMMA_MINUS_FULL_LP` | First remaining residual resolved by gamma-minus-active q0/q1 basis. |
| A101 | `CERTIFIED_GAMMA_ACTIVE_INTERVALS_AND_POINTWISE_OBSTRUCTION_CLOSURE` | Gamma-active components plus pointwise closure of all 83 A95 obstruction witnesses. |
| A102 | `CERTIFIED_COMPLETE_RATIONAL_WITNESS_ATLAS` | All 1,063 rational witnesses closed; still pointwise, not continuum by itself. |
| A103 | `CERTIFIED_ENDPOINT_RELEASED_CONTINUUM_ATLAS` | Exact continuum promotion of endpoint-released source segments. |
| A104 | `CERTIFIED_Q0Q1_CONTINUUM_ATLAS` | Exact continuum promotion of seven exceptional q0/q1 segments. |
| A105 | `CERTIFIED_TWO_BAND_CONTINUUM_ATLAS` | Forty proper two-sided two-band components; no whole-segment overclaim. |
| A106 | `CERTIFIED_GAMMA_MINUS_CONTINUUM_ATLAS` | One complete + 17 one-sided gamma-minus components; lower adjacent mass is finite-atlas exit. |
| A107 | `CERTIFIED_LOCAL_GAMMA_PLUS_CONTINUUM_EXPLORATION` | Useful local/finite continuum evidence; emergent boundary pattern not universal theorem. |
| A108 | **`REFUTED_SUPERSEDED`** | Universal one-sided boundary rule is false; exact canonical-rank-105 right `basic_p_22` counterexample. |
| A109 | `SUPPORTED_PROSPECTIVE_FINITE_EVIDENCE` | Correct bilateral candidate survives stored resolved sequence through rank 414; not an all-922 theorem; H19 unexecuted. |
| A110 | `CERTIFIED_FINITE_STRUCTURAL_THEOREM` | Independently proves corrected bilateral adjacent-boundary theorem on frozen `14<=M<=520` gamma-plus envelope. |
| A111/A111B | `FINITE_RECONNAISSANCE_ONLY` | Preregistered tail stress, including selected large M; not analytic proof. |
| A112 | `CERTIFIED_ANALYTIC_TAIL_STRUCTURAL_THEOREM` | Analytic `M>=521` theorem inside frozen gamma-plus family/strict compressed phase; not global active-set selection. |
| A113 | `CERTIFIED_ANALYTIC_TAIL_GLOBAL_COMPRESSED_THEOREM` | Global compressed one-variation for tail; with A94 covers `M>=14`; still not lifted selection. |
| A114-A | `CERTIFIED_LIFTED_BPLUS3_BRANCH` | Strict `b+3` compressed max -> endpoint-released unique strict full-LP optimum. |
| A114-B1 | `CERTIFIED_LIFTED_BPLUS1_PIVOT_THEOREM` | `b+1` phase closed; determinant orientation repaired independently; `Phi=0` kept non-strict. |
| A114-B2-W1 | `CERTIFIED_POINTWISE_NEGATIVE_PIVOT_WITNESS` | Exact `M=521,s=129/1000` q0/q1 gamma-minus optimum; pointwise only. |
| A114-B2-A | `CERTIFIED_POSITIVE_PIVOT_BPLUS2_BRANCH` | Strict `b+2`, `Phi>0` -> gamma-plus contact `b+2`; census is regression only. |
| A114-B2-B | `CERTIFIED_NEGATIVE_PIVOT_PURE_GAMMA_MINUS_EXCLUSION` | `Phi<0` tail excludes pure central-Q gamma-minus architecture; exclusion, not full classification. |
| A114-B2-C1 | `CERTIFIED_ENDPOINT_RELEASED_CONDITIONAL_BRANCH` | `p0^C<0` and `r_E(q0)>0` -> endpoint-released `E`. |
| A114-B2-C2 | `CERTIFIED_COMPRESSED_CONDITIONAL_BRANCH` | `p0^C>0` -> compressed `C`; analytic certificate 49/49, logical audit 15/15. |
| A114-B2-QI/QA | `OPEN_ANALYTIC_FRONTIER` | `p0^C<0`, `r_E(q0)<0`; current derivations are intentionally unpromoted. |

The machine-readable companion file `A80_A114_LONGITUDINAL_AUDIT_20260913.json` carries the same ledger in structured form.

---

## Critical findings

### F1 — A108 is genuinely false

The one-sided universal rule proposed in A108 is exactly refuted at canonical rank 105 by a right `basic_p_22` boundary.

This is a **scientific falsification**, not something to normalize away. A108 remains in the history precisely because it failed.

### F2 — no downstream A108 contamination detected

Repository reference searches for `A108` and `one-sided boundary`, combined with the explicit dependency records of A110–A114, found no promoted A110–A114 theorem using the false unilateral A108 statement.

A110 does not “inherit A108 and hope”. It re-proves the corrected bilateral mechanism independently over all 1,870 finite A94-envelope `(M,j)` pairs.

### F3 — compressed objective and lifted LP remain separated

A82 first exposes why this distinction is necessary. A94 and A113 explicitly remain compressed-objective results. A95 onward performs actual lifted/full-KKT resolution.

No illicit inference

`compressed maximizer => lifted optimum`

was detected in the promoted chain.

### F4 — the major determinant circularity is repaired

The dangerous route was:

1. prove `D_G>0` assuming adjacent positivity;
2. use `D_G>0` to infer adjacent positivity.

A114-B1 repairs this by proving independently

`D_G = det(C) A(s) > 0`

from the generalized-Vandermonde determinant sign and A112-G branch regularity. B2-A then imports only that independent orientation.

No promoted circularity was detected after this repair.

### F5 — finite evidence is not silently converted into all-tail proof

The current analytic theorems explicitly separate finite controls/censuses from premises:

- A89 is the analytic replacement for prior finite secant stress;
- A110 is a finite continuum theorem, not an extrapolation from A109 ranks;
- A112/A113 use analytic certificates for the tail;
- A114 uses finite exact points as independent regression/falsification layers rather than all-M premises.

### F6 — A114 README drift was real and is now resolved

At the start of this audit, `research_updates/A114/README.md` still said the complete `Phi<=0` B2 region remained open. That was stale after B2-B/C1/C2.

The README was refreshed in commit

`f78f923aa91b5e0772548825d360c40b064d0705`

and now states the current C/E/QI-QA frontier correctly.

---

## Provenance / replay boundary

The stored A107–A109 packaging validation reports that the untouched A39–A106 baseline verifier returned:

- 68 audit results;
- 1,013 gates;
- zero failures;
- `PASS`.

The same packaging report says the historical A107–A109 rank-1..414 computation was **not freshly rerun** during packaging, and H19 was not executed.

This longitudinal audit likewise did not execute every expensive historical A80–A114 script from scratch. Therefore the rigorous wording is:

> the committed evidence, stored verifier outputs, exact certificates and promoted dependency chain were audited; this is not a claim of a fresh exhaustive recomputation of every historical CPU-intensive audit.

That distinction is intentional.

---

## Current mathematical frontier after audit

Under

`M>=521`, `129/1000<=s<=133/1000`, strict compressed `j=b+2`, `Phi<0`,

we now have

\[
\boxed{p_0^C>0\Longrightarrow C}
\]

by C2, and

\[
\boxed{p_0^C<0,\ r_E(q_0)>0\Longrightarrow E}
\]

by C1.

The only remaining open strict interior branch is

\[
\boxed{p_0^C<0,\ r_E(q_0)<0,}
\]

where `QI` and `QA` compete.

The current QI/QA pivot identities and reductions are **not** counted as proved in this audit. They require their own analytic certificate, independent exact controls and logical-composition audit before promotion.

Zero-discriminant sets (`p0^C=0`, `r_E(q0)=0`, and the relevant `b+2` `Phi=0` boundary) remain separate from the strict theorem ledger.

---

## Final statement

The correct conclusion is not “every historical guess was right”. It is stronger scientifically:

> **The A80–A114 programme contains explicit falsifications and corrections, but the currently promoted theorem chain survives them. A108 is refuted and superseded; A110 independently repairs the finite structural statement; A112/A113 establish the analytic-tail structural/compressed layers; A114 then performs full lifted selection branch by branch. No downstream dependence on the false A108 conjecture and no promoted circular dependency were detected.**

No physical interpretation is implied by this audit.