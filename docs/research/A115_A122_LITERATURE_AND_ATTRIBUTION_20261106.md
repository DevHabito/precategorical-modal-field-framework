# Literature and attribution record: A115–A122

*Reviewed 6 November 2026. This is a targeted bibliography, not a systematic priority search.*

I have kept this separate from the project theorem record. The purpose is to say what can already be found in the literature, what these sources actually address, and which parts of our present derivation still lack an exact published counterpart **in the sources consulted**. No absence-of-match claim should be read as proof of originality.

The journal metadata and DOIs in the first six entries were checked against publisher pages during this review. For articles behind paywalls, the reviewed evidence is the publisher metadata and abstract, not a line-by-line reading of the full text. That difference matters.

## Verified prior work

### 1. Linear-fractional optimization and homogenization

**A. Charnes and W. W. Cooper (1962).** “Programming with Linear Fractional Functionals.” *Naval Research Logistics Quarterly* **9**(3–4), 181–186. DOI: https://doi.org/10.1002/nav.3800090303  
**Checked at:** [Wiley publication page](https://onlinelibrary.wiley.com/doi/10.1002/nav.3800090303).  
**Connection:** converting a ratio objective to a homogenized linear optimization formulation is classical. The source alone does not identify the precise A115 active factor or the A117–A122 parameter layers.

### 2. Parametric basis changes

**Tomas Gal and Josef Nedoma (1972).** “Multiparametric Linear Programming.” *Management Science* **18**(7), 406–422. DOI: https://doi.org/10.1287/mnsc.18.7.406  
**Checked at:** [INFORMS publication page](https://pubsonline.informs.org/doi/10.1287/mnsc.18.7.406).  
**Connection:** basis stability regions, transitions, and algorithms for parametric linear programs are existing methods. Their abstract describes affine dependence in RHS/objective coefficients. That is not identical to our exponential-parameter family and does not by itself settle its exact phase boundaries.

### 3. Discrete moment optimization

**András Prékopa (1990).** “The Discrete Moment Problem and Linear Programming.” *Discrete Applied Mathematics* **27**(3), 235–254. DOI: https://doi.org/10.1016/0166-218X(90)90068-N  
**Checked at:** [Elsevier publication page](https://www.sciencedirect.com/science/article/pii/0166218X9090068N).  
**Connection:** moment-constrained problems with finite support and their LP/dual basis formulations are established mathematics. A115's finite support and use of moment constraints are not a new class of optimization on their own.

### 4. Extreme measures and Laplace transforms — particularly close prior art

**Alan F. Karr (1983).** “Extreme Points of Certain Sets of Probability Measures, with Applications.” *Mathematics of Operations Research* **8**(1), 74–85. DOI: https://doi.org/10.1287/moor.8.1.74  
**Checked at:** [INFORMS publication page](https://pubsonline.informs.org/doi/abs/10.1287/moor.8.1.74).  
**Connection:** the publisher abstract expressly includes measures with prescribed moments and prescribed Laplace-transform values. Consequently, sparsity/extreme support under a finite number of transform constraints cannot safely be claimed as a project discovery.

### 5. Eventual parametric behavior — a related but nonidentical setting

**Robert G. Jeroslow (1973).** “Asymptotic Linear Programming.” *Operations Research* **21**(5), 1128–1141. DOI: https://doi.org/10.1287/opre.21.5.1128  
**Checked at:** [INFORMS publication page](https://pubsonline.informs.org/doi/10.1287/opre.21.5.1128).  
**Connection:** eventual LP behavior and parameter sensitivity are established topics. The abstract explicitly concerns coefficients rational in one parameter; it would be wrong to treat that as a ready-made theorem for our exponential target deformation.

## Earlier project literature review (not reproduced as new independent verification)

The repository already contains a broader bibliography in [A110–A114 Literature Positioning and Novelty Map](../novelty/A110_A114_LITERATURE_POSITIONING_AND_NOVELTY_MAP_20260914.md). That document discusses Krein–Nudelman, Karlin–Studden, total positivity, Chebyshev/ECT systems, and related moment-space and active-set work. Those remain essential starting points, but I have **not** rechecked every book and journal reference on that list in this session. Readers should use the original cited editions and verify exact theorem statements before making reductions to them.

The other targeted research note is [A119–A122 Independent Certificate Recheck](../novelty/A119_A122_INDEPENDENT_CERTIFICATE_RECHECK_20261106.md); its literature section also discusses standard interval validation. The present note neither duplicates nor supersedes those sources.

## Attribution rules for the manuscript

| Ingredient | Classification | Reason |
|---|---|---|
| Finite measures with fixed ordinary moments | Classical | Prékopa, Karr, broader moment literature |
| Ratio objective and LP homogenization | Classical | Charnes–Cooper |
| Parametric basis regions and changes | Classical | Gal–Nedoma |
| Sparse extremal measures under Laplace constraints | Close classical prior art | Karr |
| Elementary central three-weight solution and denominator factorization | Project calculation using standard algebra | Lean formalization does not confer historical novelty |
| Universal cofactor-to-ten-channel polynomial expansion | Project-specific algebraic identity; mathematical novelty not claimed | Its verification is a polynomial calculation |
| Exact A116–A122 collision/rounding phase classification with frozen constants | **Specific project claim requiring a closer prior-art search** | No exact equivalence established from the consulted abstracts |
| A119 6,400-box rational positivity certificate | Project computational certificate | Reproduced for the published rational formula, not yet kernel-verified as the complete theorem |
| Lean 4 code and a reproducible audit trail | Project implementation and reproducibility contribution | Software verification is not proof of a world-first theorem |

## Open literature questions

1. Does a known theorem on totally positive exponential kernels or Chebyshev systems directly imply the A115–A119 sign conclusions after the right substitution? If so, cite it and narrow the novelty claim.
2. Are periodic or irrational rotation effects in ceiling-based asymptotic contact selection already documented in a technically equivalent parametric optimization setting? Compare the actual hypotheses, not just keywords.
3. Does existing theory for several coupled measures or generalized moment problems yield the same support and dual certificate without the project-specific determinant calculation?
4. Can the A122 near-resonant formula be reduced to a standard lattice correction after a change of variables? A negative search is insufficient; full-text comparisons are needed.

**Current assessment:** `NOVELTY_NOT_CERTIFIED`. A mathematically defensible paper would separate its concrete theorems from the classical tools used to establish them. The existence of the present bibliography is not a claim of exhaustive scholarship.
