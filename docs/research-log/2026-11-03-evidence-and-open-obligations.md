# Research log — 3 November 2026

**Author:** Felipe Gianini Romero  
**Repository:** DevHabito/precategorical-modal-field-framework  
**Base inspected:** audit/2026-10-19-trust-and-integrity, \`8beff0808bf29c9d11467cd76a8b50a1c74a4174\`  
**Method:** source inspection, independent symbolic algebra, exact rational computation, and explicit separation of past CI evidence from new tests.

## What I found in the archive

The canonical project README expressly does not claim a confirmed fundamental physical theory. The mathematical core is organized under \`consolidation/\`, while historical A-number updates retain their original provenance. I am keeping that boundary: formal mathematics, computational evidence, historical speculation and physical interpretation cannot be used interchangeably.

At the date of this log, \`main\` pointed to \`89e2668c3aef3fbff5a7f399f86de7d27e467da1\`. The later audit work was in open draft PR #20, with head \`8beff0808bf29c9d11467cd76a8b50a1c74a4174\`. I inspected the latter because its sources include newer Lean files and more explicit assurance caveats. I did not infer from its draft status that its mathematical claims were either true or false.

## Results I independently rechecked

### C2 / F3 — fixed-score non-closure

Using only exact rational arithmetic and a separately authored SymPy calculation, I checked the two strictly positive four-point distributions

    p+ = (15,22,7,20)/64
    p- = (17,10,25,12)/64.

Their masses are both 1, means both 3/2, initial moments at t=1/4 both 85/256, and rescaled moments at t=1/2 equal 121/256 and 119/256, respectively. Their signed difference is exactly

    D(t) = (t-1)^2 (t-1/4) / 8.

The linear constraint matrix for cubic differences preserving mass, mean and the first exponential moment has rank three, hence a one-dimensional nullspace. A deliberate perturbation of the data broke the initial-moment equality as expected. The original finite-state example therefore passes this independent algebraic and rational audit.

I did not rerun Lean for this result. The existing formal sources are \`DynamicNonclosure.lean\` and \`DynamicNonclosureTransport.lean\`. Prior GitHub Actions and axiom traces, documented under \`consolidation/LEAN_AXIOM_DEPENDENCIES_2026-10-19.md\`, report successful proof and no native-evaluation axioms for the five selected F3 declarations. Those are historical CI results, not results of my current machine.

The mathematical conclusion concerns the insufficiency of a selected coarse state under a specified update. It does not rule out all finite closures or establish any physical law.

### C3 / A113 — frozen small-left sector

I checked the exact A83/A84 cofactor identity using independent formal algebra, with one deliberately altered sign as a negative control. I then reran the 60-case rational test and extended the test grid to all 28 integer contacts k=2,...,29 at four M values and three source nodes: 336 cases in total. Each exact test passed the stated coefficient, remainder and positivity assertions.

I also checked the rational margin and the inequality

    18 + 267/521 = 9645/521 < 20.

I derived a written remainder assembly from the already stated Lean coefficient inequalities. The full argument and source paths are in \`consolidation/A113_SMALL_LEFT_CLOSURE_CHECKPOINT_2026-11-03.md\`.

What I **did not** do was compile, kernel-check or run \`leanchecker\` against the newly drafted joining proof. It is a candidate only. I have not independently re-proved all upstream A83/A84 inequalities or the remaining global A113 sectors.

## Distinguishing past CI from current execution

- GitHub Actions run 39491064741, attempt 2, was inspected and reported 29/29 successful jobs for code SHA \`9f38572c9114dc9b6412a6faa0d1928107e11f5a\`.
- The audited branch's later HEAD is \`8beff0808bf29c9d11467cd76a8b50a1c74a4174\`. Its five new workflow records inspected at this checkpoint had conclusion \`action_required\`, not \`success\`. I will not call that HEAD green.
- The Lean trust boundary matters: selected C1 finite counts use \`native_decide\`, while the cited selected F3 trace has no native-computation axiom. A checker pass alone does not erase the former dependency.
- The documented historical ZIP audit examined 22 tracked archives and reported 19 valid and 3 invalid packages. I confirmed the linked GitHub Actions integrity workflow concluded \`failure\`, but did **not** independently retrieve and recheck all 22 archive byte streams in this session.
- The documented recovery of one intact A113 Python member is partial; it does not repair the complete archive or prove the missing analytic bridges.

## What remains unresolved

1. Compile and kernel-replay the isolated A113 closure candidate; check actual axioms and imports.
2. Validate upstream coefficient/defect bounds independently against the historical definitions, including parity-sensitive signs and boundary controls.
3. Review the remaining A112/A113 middle/remote/central and lifted KKT proof dependencies separately.
4. Resolve the historical ZIP reproducibility failures without destroying original checksums or overwriting evidence.
5. Refresh/check root integrity indexes from the exact final tree before any merge.
6. Complete theorem-level originality review, not merely literature metadata review.
7. Supply operational definitions, units, measurement models and falsifiable empirical predictions before making any astrophysical or physical claim.

## Documentation and reproducibility

This log is not a substitute for the source proofs. The exact scripts and captured outputs are preserved in \`tools/research_2026_11_03/\`. Source and bibliography checkpoints are linked in the A113 note and \`docs/novelty/VERIFIED_CONTEXT_2026-11-03.md\`. The uncompiled Lean candidate lives in \`consolidation/candidates/\`.

I did not change the mathematics in the historical archives, hide a failing check, report a CI pass without a run, or declare the physical hypothesis confirmed. This is a research checkpoint, not a release claim.

## Later verification on 3 November: exact Delta interval

I closed the previously open parity-sensitive normalized H-channel interval in pinned Lean 4.33.1, including source-to-scalar and both parity identities. [Run 41727101617](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41727101617) passed the full 35-module checker matrix and reported only `propext`, `Classical.choice`, `Quot.sound` for the two new final statements. I retained the earlier power-gap rewrite failure rather than hiding it. See `../../consolidation/A113_DELTA_UNIFORM_LEAN_VERIFICATION_2026-11-03.md` for the exact proof domain, tests, dates, source files and remaining obligations. This closes one mathematical gap, not all A113 sectors and not any physical claim.
