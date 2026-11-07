# A115–A122 research record

*6 November 2026 — working branch: `formal/a115-a122-critical-audit-20261106`*

I am keeping the definitions, proofs, failed attempts and references in separate files so that the mathematical claims can be checked without reconstructing the history of the discussion. The original A-series notes are not being rewritten to hide uncertainties or preserve an early conjecture. This is a research log, not a finished manuscript.

**Adversarial audit (7 November 2026):** [A115–A122 Scientific Audit](A115_A122_ADVERSARIAL_SCIENTIFIC_AUDIT_20261107.md). Read this before citing a global optimization or originality claim: it documents the A113 value/factor discrepancy, strengthened test assertions, and the distinct full-LP feasibility witness.

## Start here

1. **[Notation and terminology](A115_A122_NOTATION_AND_TERMS_20261106.md)** — support, measure weights, target deformation, parity, two different uses of `q` and `r`, collision and rounding regimes. Read this before interpreting an A119 or A122 formula.
2. **[Literature and attribution](A115_A122_LITERATURE_AND_ATTRIBUTION_20261106.md)** — journal sources with verified metadata and DOIs; what is standard mathematics; which comparisons are still open. Originality is **not certified**.
3. **[Evidence and failure ledger](A115_A122_EVIDENCE_AND_FAILURE_LEDGER_20261106.md)** — exact executable tests, Lean build and kernel replay, source-reported results, compiler failures, genuine counterexamples, rejected out-of-domain data, and outstanding proof obligations.
4. **[A115 Q-block feasibility](../formal/A115_CENTRAL_FEASIBILITY_INTERVAL_20261106.md)** — exact three-weight nonnegativity intervals, Lean proof and the distinction from full LP feasibility.
5. **[A115 cofactor/ten-channel bridge](../formal/A115_TEN_CHANNEL_IDENTITY_GATE_20261106.md)** — universal polynomial identity and exact finite-basis bridge, with the CI history.
6. **[Primal constraints to moment-adjusted basis](../formal/A115_PRIMAL_TO_BASIS_BRIDGE_20261106.md)** — finite P support, exact mass/mean elimination, transform ratio, and the determinant's orientation. The full KKT cofactor derivation remains open.
7. **[A115 compressed adjacent objective and sign orientation](../formal/A115_COMPRESSED_ADJACENT_OBJECTIVE_IDENTITY_20261107.md)** — derive the actual adjacent objective difference from the two active band equalities, reconcile A81/A83 signs, and distinguish the reduced factor from its rational prefactor.
8. **[Uniform source-numerator sign lemma](../formal/A115_UNIFORM_SOURCE_NUMERATOR_SIGN_20261107.md)** — exact target-term cancellation; a uniform calculus proof of `Z<0` for `0<beta<s<1/4`; separately kernel-checked conditional algebra and independent exact-rational tests.
9. **[A119/A122 independent arithmetic recheck](../novelty/A119_A122_INDEPENDENT_CERTIFICATE_RECHECK_20261106.md)** — independent interval-covering computations and rational logarithm brackets.

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

## 7 November — a stronger source-sign result, with a visible formalization boundary

The new [A115 uniform source-numerator sign note](../formal/A115_UNIFORM_SOURCE_NUMERATOR_SIGN_20261107.md) proves a parameter-uniform sign statement for the compressed common Cramer numerator: `Z<0` when `M>=4`, `0<beta<s<1/4`, `0<tau<1`, and `delta>=0`. The proof reduces the source numerator to an exact cancellation, then uses a strictly increasing `L_h` and strictly decreasing `R_(M,h)`. It is a self-contained calculus argument, not an extrapolation from the existing finite A83 atlas.

The following have been verified by Lean 4 and independent kernel replay: the exact three-site P nonnegativity criterion; automatic determinant orientation from strictly positive interior masses plus `Z<0`; the common-source cancellation; the negative-sign implication given the L/R ordering; the all-natural-index power inequality underpinning `L_h'`; and the parity identities. The corresponding complete successful workflow runs are [42358308334](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42358308334), [42358976869](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42358976869), and [42359321885](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42359321885). The independently published Python checker passed [42358910281](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42358910281).

The **entire derivative-to-strict-monotonicity connection has not yet passed Lean**. Three failed elaboration attempts, including an additive-group instance mismatch, have been archived at [A115 failed Lean monotonicity experiment](../formal/experiments/A115_FAILED_SOURCE_MONOTONICITY_LEAN_20261107.md). The failed file was removed from the compiled project; the source is preserved in the archive, not silently discarded.

The current result narrows the global proof obligations but does not remove the need to check every remaining band and the full dual/KKT conditions of the original LP. Mathematical priority over earlier publications is not claimed.
