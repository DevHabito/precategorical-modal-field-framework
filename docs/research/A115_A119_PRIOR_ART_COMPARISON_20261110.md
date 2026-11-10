# A115–A119: targeted prior-art comparison and priority limitations

**Review date:** 2026-11-10
**Research question:** Is the parity-dependent critical collision sign of the reduced two-active-band C2(k) exponential-moment comparison already implied by known moment-programming results?

## Exact publication candidate, not a claimed world-first theorem

The potential manuscript theorem is limited to the explicit C2(k) factor, target collision scaling tau=s+lambda/M, fixed parity and contact deficit, and positivity of the critical second-order coefficient Xi_p on the displayed parameter rectangle. The 35-box certificate is an **exact rational inclusion proof of the published substituted expression**, conditional on the A115–A118 derivation and A117 contact cell/tail lemmas. A Lean kernel proof of this complete chain has not been completed.

This is not a proof of the globally optimal F2 or F3 support, nor a physical pregeometry claim.

## Verified published neighbors

| Work | What the publisher abstract actually says | Originality consequence |
|---|---|---|
| A. E. Eckberg Jr. (1977), *Sharp Bounds on Laplace-Stieltjes Transforms, with Applications to Various Queueing Problems*, **Mathematics of Operations Research**, DOI [10.1287/moor.2.2.135](https://doi.org/10.1287/moor.2.2.135) | Derives sharp upper/lower Laplace-Stieltjes-transform bounds from partial distributional information such as moments | General transform extremal bounds predate this project |
| A. F. Karr (1983), *Extreme Points of Certain Sets of Probability Measures, with Applications*, **Mathematics of Operations Research**, DOI [10.1287/moor.8.1.74](https://doi.org/10.1287/moor.8.1.74) | Characterizes extreme points of measure sets with constraints; explicitly mentions prescribed Laplace-transform values | Extreme-measure reasoning and sparse-support context are not new |
| Anh Ninh and András Prékopa (2013), *The discrete moment problem with fractional moments*, **Operations Research Letters**, DOI [10.1016/j.orl.2013.09.001](https://doi.org/10.1016/j.orl.2013.09.001) | Studies fractional moments in discrete moment problems, with basic theory and an LP-based solution method | Discrete moment LPs with nonstandard moments are established prior art |
| J. Guo, H. Qiu, Z. Wang, Z. Wang, X. Zhang (2025), *Exact solving approach to moment problems with nonnegative Chebyshev ambiguity sets*, **Operations Research Letters**, DOI [10.1016/j.orl.2025.107349](https://doi.org/10.1016/j.orl.2025.107349) | Exact optimal-support and numerical work for certain bivariate Chebyshev moment ambiguity sets | Modern moment-support theorems require direct comparison, but the abstract does not establish equivalence with C2(k) |

The author order and publication years above follow the publisher search results inspected in this session. For the 2025 item, consult the canonical publisher record before using a full bibliographic citation.

## What these sources do and do not show

The general framework of probability measures constrained by moments or transform values, and extremal optimization over their support, is **not a new discovery**. Nor is a rational interval covering proof a new generic technique.

None of the consulted **abstracts** explicitly states A116–A119's exact model, tau=s+lambda/M collision scaling, half-integer parity cells, the particular second-order Xi_p or the 35-box inequality. **Absence from abstracts is not evidence of novelty**. Full theorem statements, assumptions, bibliography trails and specialist peer review remain open.

## Publication-specific tests

1. Translate C2(k) into the standard language of finite moment programming and characterize the admissible two-measure support without using project-internal labels.
2. Check whether extended Chebyshev/T-system theory supplies the same sign and contact structure as a corollary. If so, attribute it and focus on the model-specific quantitative certificate.
3. Compare collision scaling against *parametric* and *degenerate-basis* LP literature, not only moment-programming papers.
4. Do not extend C2(k) conclusions to F3 until a full primal/dual certificate is proved uniformly.
5. Expose the precise Lean statement and trusted axioms before the adjective “formally verified”.

**Editorial status:** mathematical novelty **NOT CERTIFIED**. The current strongest reproducibility contribution is a compact 35-box rational certificate for one explicitly declared reduced critical expression.
