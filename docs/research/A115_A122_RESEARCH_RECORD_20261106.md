# A115–A122 research record

*6 November 2026 — working branch: `formal/a115-a122-critical-audit-20261106`*

I am keeping the definitions, proofs, failed attempts and references in separate files so that the mathematical claims can be checked without reconstructing the history of the discussion. The original A-series notes are not being rewritten to hide uncertainties or preserve an early conjecture. This is a research log, not a finished manuscript.

## Start here

1. **[Notation and terminology](A115_A122_NOTATION_AND_TERMS_20261106.md)** — support, measure weights, target deformation, parity, two different uses of `q` and `r`, collision and rounding regimes. Read this before interpreting an A119 or A122 formula.
2. **[Literature and attribution](A115_A122_LITERATURE_AND_ATTRIBUTION_20261106.md)** — journal sources with verified metadata and DOIs; what is standard mathematics; which comparisons are still open. Originality is **not certified**.
3. **[Evidence and failure ledger](A115_A122_EVIDENCE_AND_FAILURE_LEDGER_20261106.md)** — exact executable tests, Lean build and kernel replay, source-reported results, compiler failures, genuine counterexamples, rejected out-of-domain data, and outstanding proof obligations.
4. **[A115 Q-block feasibility](../formal/A115_CENTRAL_FEASIBILITY_INTERVAL_20261106.md)** — exact three-weight nonnegativity intervals, Lean proof and the distinction from full LP feasibility.
5. **[A115 cofactor/ten-channel bridge](../formal/A115_TEN_CHANNEL_IDENTITY_GATE_20261106.md)** — universal polynomial identity and exact finite-basis bridge, with the CI history.
6. **[Primal constraints to moment-adjusted basis](../formal/A115_PRIMAL_TO_BASIS_BRIDGE_20261106.md)** — finite P support, exact mass/mean elimination, transform ratio, and the determinant's orientation. The full KKT cofactor derivation remains open.
7. **[A115 compressed adjacent objective and sign orientation](../formal/A115_COMPRESSED_ADJACENT_OBJECTIVE_IDENTITY_20261107.md)** — derive the actual adjacent objective difference from the two active band equalities, reconcile A81/A83 signs, and distinguish the reduced factor from its rational prefactor.
8. **[A119/A122 independent arithmetic recheck](../novelty/A119_A122_INDEPENDENT_CERTIFICATE_RECHECK_20261106.md)** — independent interval-covering computations and rational logarithm brackets.

## What can be claimed today

The project has Lean 4 proofs of the exact algebraic statements now present in these files:

- central parity-dependent normalization and target equations;
- a finite denominator identity;
- necessary and sufficient nonnegativity conditions for the central three-site Q weights;
- the finite-basis representation and adjacent difference;
- the universal identity between the A115 cofactor factor and its ten-channel expansion.

The relevant fully successful runs are:
- [17/17 Lean jobs, Q-block equivalences](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42306617445)
- [19/19 Lean jobs, ten-channel identity and basis bridge](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42307816396)

For exact arithmetic, the project has standalone Python scripts in `audits/` and a dedicated [GitHub Actions workflow](../../.github/workflows/a115-a122-exact-audits.yml), which executes the checked-in code in a clean Python 3.13 runner.

The A119 positivity calculation has been reproduced as **6,400 exact rational interval comparisons** for the published reduced expression. The A122 continuous double-critical sign change has been reproduced using rational logarithm enclosures. Those are meaningful checks **of the formulas they evaluate**; they do not certify that all inherited asymptotic deductions are correct.

There are also genuine negative results worth preserving:

- A115's blanket positivity extension to all target deformations is **false**. Two admissible `M=521` counterexamples were independently reproduced and hash-checked.
- A third negative numerical value was **not** a valid in-domain counterexample and was rejected after checking the factor index.
- Several Lean proof attempts failed for explicit parsing, noncomputability, or tactic-normalization reasons before the corrected formal statements passed. All are identified in the ledger.

## What I will not claim yet

- That A115's factor has been formally derived from the **full** original primal/dual problem and its KKT conditions.
- That the full two-measure optimization is feasible whenever the three-site central block is nonnegative.
- That A116–A122 are entirely formalized in Lean.
- That A119's analytic tail exclusion or its derivation from A118 has been independently reconstructed at theorem level.
- That A122's arithmetic near-resonance is realized by a particular infinite integer subsequence.
- That this work is the first of its kind, or that a literature search proves novelty.
- Any physical or ontological interpretation of these finite optimization statements.

## Next mathematical gates

The next paper-ready result is not another sequence label. It is a self-contained derivation of the exact sign factor from the full finite LP, followed by independent verification of the A118 asymptotic formula. Only then does it make sense to promote the A119 positivity certificate from an independently reproduced computation to an end-to-end checked theorem.

The source remains in English and the evidence stays tied to the revision that generated it. The default `main` branch is not changed by this research record.
