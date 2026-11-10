# A119: complete 35-box rational Lean certificate — audited checkpoint

**Recorded:** 10 November 2026  
**Working branch:** \`research/a115-a119-uniform-remainder-20261110\`  
**Last verified source commit:** \`e5031677683c7d51625c9359b63ac4a96bcfca5d\`  
**Verification:** [GitHub Actions run 42887340405](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42887340405), status completed, conclusion **SUCCESS**, **39/39 jobs successful** (one project build and 38 individual module \`leanchecker\` jobs).

## Exactly what is proved

The repository now contains Lean 4 proofs of **35/35 exact rational inclusion evaluations** of A119's explicit parity-dependent critical function \(\widehat{\Xi}_{p,r}(s,\alpha)\), with source

\[
s\in[129/1000,133/1000]
\]

and a rational enlarged alpha interval

\[
\alpha\in
\left[2(r+\sigma_p),\frac{21}{10}(r+1+\sigma_p)\right],
\qquad
\sigma_{\mathrm{even}}=0,\quad\sigma_{\mathrm{odd}}=1/2.
\]

The 35 rectangles are the disjoint-interior, closed-endpoint subdivisions detailed below; *all* interval arithmetic is exact rational arithmetic. The Lean checks use \`decide +kernel\`, not \`native_decide\`, floating-point thresholds, an assumed Python result, or an assumed numerical lower endpoint.

| Parity and contact deficit | Number of kernel-checked boxes | Checked modules |
|---|---:|---|
| even and odd r=4, three alpha intervals each | 6 | \`A119BoxReplay\`, \`A119R4Remaining\` |
| even and odd r=5, two each | 4 | \`A119R5Boxes\` |
| even and odd r=6, two each | 4 | \`A119R6Boxes\` |
| even and odd r=7, two each | 4 | \`A119R7Boxes\` |
| even and odd r=8,9,10,11,12, one each | 10 | \`A119R8R12Boxes\` |
| odd r=13,14,15,16,17,18,19, one each | 7 | \`A119OddR13R19\` |
| **Total** | **35** | |

The rational source-to-interval interpretation is independently justified within the checked Lean source:

- \`A119IntervalArithmetic\` verifies signed four-corner multiplication and sign-separated division;
- \`A119IntervalEvaluator\` proves that every successful expression-tree interval evaluation encloses **all rational** point values in the input boxes;
- \`A119CertifiedExpression\` proves that the checked expression tree is **equal to the explicit rational function** \`criticalXiHat\` and that a strictly positive checked interval lower bound implies positivity at all rational points in its box;
- \`A119CompactCertificate\` checks the 14+21=35 count and the two/three-piece interval coverage lemmas;
- \`A119R4Coverage\`, \`A119R5Boxes\`, and \`A119R7Boxes\` contain additional quantified full-alpha results for their respective r values.

These proofs establish strict positivity of the *explicit rational function* at every **rational** parameter point covered by the complete finite manifest. This is more substantial than evaluating a few isolated numeric parameters or proving merely that pre-reported rational constants are positive.

## Verification and independent evidence

The exact final GitHub Actions run associated with the high-contact extension is **42887340405** at source commit \`e5031677683c7d51625c9359b63ac4a96bcfca5d\`. Its full jobs response (requested with \`per_page=100\`, since a default 30-job page is incomplete) reported **39/39 successful**.

The independently performed Python standard-library \`Fraction\` certificate for the same expression passed **35/35** exact closed rectangles at [run 42855045033](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42855045033). The smaller Lean proofs do **not** assume or import its output as a proposition; the two systems offer separate arithmetic evidence.

Earlier failed or incomplete Lean attempts remain visible in the GitHub history and are documented in [A119_COMPOSITIONAL_INTERVAL_EVALUATOR_20261110.md](A119_COMPOSITIONAL_INTERVAL_EVALUATOR_20261110.md). For example, ordinary \`decide\` could not normalize a full rational box, whereas the same formula was later accepted using \`decide +kernel\`. We did not change a mathematical hypothesis to turn that failure into a PASS.

## What has NOT been proved

**1. Real-variable Lean theorem.** The current source-to-interval soundness and final pointwise positivity theorems quantify over \(\mathbb Q\), not \(\mathbb R\). There is a mathematical reason that exact rational endpoint interval bounds work over **all real points** as well, without weakening strict positivity. The hand-auditable proof and its conditions are in [A119_ANALYTIC_REAL_INTERVAL_BRIDGE_20261110.md](A119_ANALYTIC_REAL_INTERVAL_BRIDGE_20261110.md). It remains **not kernel-checked over reals**.

**2. Explicit all-r finite-manifest theorem.** Individual box evaluations are all checked and basic split-coverage lemmas are checked, with full-cell coverage theorems for some deficits. A single theorem in Lean quantifying over all legal parity/deficit pairs and showing the manifest covers each entire enlarged critical cell remains to be compiled and kernel-replayed.

**3. Coefficient identification.** The AST-to-\`criticalXiHat\` equality does not prove that \`criticalXiHat\` is the coefficient \(\Xi_p\) arising from the A115–A118 LP/cofactor expansion on \(\Lambda_p=0\). The exact source-to-critical-coefficient bridge must be formally re-proved.

**4. Uniform asymptotic remainder.** The analytic \(O(M^{-3})\) remainder reported in the research note remains a separate mathematical statement; its full hypotheses and bounds have not been kernel-proved.

**5. Boundary/large-deficit exclusion.** A117 contact-cell classification and A119 high-contact exclusion were separately supported by exact rational and analytic checks, but the complete mathematical argument has not been assembled in the Lean kernel.

**6. Global LP or physics.** The rational sign theorem is about the reduced C2(k) family. It says nothing by itself about the unrestricted F2/F3 global primal/dual optima, physical pregeometry, molecular biology, a universal law, or a new fundamental principle.

**7. Historical novelty.** No full-text theorem-level prior-art review or external peer review has certified priority. Rational interval inclusion is an established method; a possible original contribution is the particular collision/parity sign statement *if* it is not already implied by existing moment and parametric LP theory.

## Recommended next scientific milestone

**Close the semantic gap to the reals and the finite manifest before expanding to any A123 claims.** Encode the same expression tree over \(\mathbb R\), with exact rational interval endpoints, prove sign-separated division and four-corner product inclusion for real inputs, and transport the already verified 35 Boolean computations to a **uniform strictly positive real-domain bound**. Then prove the complete finite manifest and return to the A115–A118 critical coefficient derivation.

The branch is isolated from \`main\`. This checkpoint is ready for an independent mathematical reader, but it is **not a complete A119 paper proof or a novelty certificate**.
