# A110–A114 literature positioning and novelty map

**Date:** 2026-09-14  
**Scope:** A110–A114, with A113/A114 as the main focus  
**Purpose:** give reviewers and researchers a clear account of what is classical, what was extracted from the project, what appears project-specific, and what is **not** yet a certified novelty claim.

## Read this first

This note is deliberately conservative.

The current A110–A114 programme uses several powerful mathematical ideas that are not new: linear-fractional homogenization, parametric linear programming, generalized moment problems, Chebyshev/extended-Chebyshev systems, total positivity, variation-diminishing arguments, sparse extremal measures, principal representations of moment spaces, simplex pivots, and KKT sensitivity. We should not claim any of those ingredients as original.

The potentially interesting contribution is narrower: the project obtains an explicit, exact active-set classification for a particular **coupled exponential-moment extremal problem**, including a tail one-variation theorem and a short staircase of lifted KKT architectures controlled by explicit discriminants.

A targeted literature search did **not** locate the same classification theorem in the sources listed below. That is evidence for further novelty review, not proof of priority. In the vocabulary already used by this repository, the strongest appropriate status at this stage is:

> **APPARENTLY_UNREPORTED / NOVELTY_NOT_CERTIFIED**

No negative literature search authorizes wording such as “first ever”, “previously unknown”, or “new mathematical theory” without specialist review.

---

# 1. The mathematical object hidden by the internal architecture labels

The internal labels `C`, `E`, `QI`, `QA`, `b+2`, `Phi`, and `Gamma` are useful for the proof programme, but they make the underlying optimization problem look more idiosyncratic than it is.

Let the original nonnegative LP variables be `p_x` and `q_x`, with scale `t>0`, on the finite support

\[
X_M=\{0,1,\ldots,M\}.
\]

The normalization and first-moment constraints have the form

\[
\sum_x p_x=t,\qquad \sum_xq_x=t,
\]

and

\[
\sum_x xp_x=\frac M2t,\qquad
\sum_xxq_x=\frac M2t.
\]

Define probability measures

\[
\mu_x=\frac{p_x}{t},\qquad
\nu_x=\frac{q_x}{t}.
\]

Then

\[
\sum_x\mu_x=\sum_x\nu_x=1,
\qquad
E_\mu[X]=E_\nu[X]=\frac M2.
\]

For `0<r<1`, define the probability-generating/Laplace-type transform

\[
G_\mu(r)=\sum_{x=0}^M\mu_xr^x,
\qquad
G_\nu(r)=\sum_{x=0}^M\nu_xr^x.
\]

Because

\[
r^x=e^{-(-\log r)x},
\]

this is equivalently a discrete Laplace transform sampled at `-log r`.

The target normalization in the present programme is

\[
\sum_x\tau^xq_x=1,
\]

so

\[
tG_\nu(\tau)=1,
\qquad
\boxed{t=\frac1{G_\nu(\tau)}}.
\]

The LP objective is

\[
\sum_x\tau^xp_x
=tG_\mu(\tau),
\]

hence, before homogenization, the optimization target is exactly

\[
\boxed{
\frac{G_\mu(\tau)}{G_\nu(\tau)}
}.
\]

The bilateral transform bands become

\[
\boxed{
|G_\mu(r)-G_\nu(r)|\le 2\varepsilon
}
\]

at the selected transform nodes (`s`, `beta`, `gamma` in the current frozen family).

A natural external description of the object is therefore:

> **Coupled exponential-moment extremal problem:** optimize a ratio of transforms of two probability measures with a shared ordinary moment and bilateral constraints on their transform differences at other nodes.

This reformulation is useful for communication and comparison with the literature. It is **not itself a novelty claim**.

---

# 2. What is clearly classical

## 2.1 Ratio-to-LP homogenization is classical

The passage from a ratio objective to a homogeneous linear program has an obvious conceptual relative in linear-fractional programming. Charnes and Cooper developed the classical transformation for programming with linear fractional functionals in 1962.

Our measure normalization is adapted to the present constraints, but we should not present the basic idea “turn a ratio into a linear program with a scale variable” as original.

**Classification:** `CLASSICAL`.

Reference: A. Charnes and W. W. Cooper, “Programming with Linear Fractional Functionals,” *Naval Research Logistics Quarterly* **9** (1962), 181–186. DOI: https://doi.org/10.1002/nav.3800090303

## 2.2 Parametric LP regions and basis changes are classical

The idea that parameter space is partitioned into regions where a basis remains optimal, with transitions associated with basis changes, is standard in parametric and multiparametric linear programming. Gal and Nedoma explicitly formulated regions associated with optimal bases and algorithms that move through the resulting graph.

Our source parameter enters through exponential coefficients such as `s^x`, so the boundary geometry is not simply the standard affine/polyhedral multiparametric-LP setting. But the general language of “critical regions”, “basis stability”, and “neighboring pivots” is inherited from classical parametric optimization.

**Classification:** `CLASSICAL` at the general level; the exact exponential boundaries in this project are problem-specific.

Reference: T. Gal and J. Nedoma, “Multiparametric Linear Programming,” *Management Science* **18** (1972), 406–422. DOI: https://doi.org/10.1287/mnsc.18.7.406

A related continuation viewpoint also appears in one-parameter semi-infinite programming, where KKT curves are followed and the active set is changed when needed.

Reference: T. Rupp, “Kuhn-Tucker curves for one-parametric semi-infinite programming,” *Optimization* **20** (1989), 61–77. DOI: https://doi.org/10.1080/02331938908843414

## 2.3 Moment problems formulated as linear optimization are classical

Optimization over probability measures subject to prescribed moments is a classical subject. Krein–Nudelman and Karlin–Studden are central references for moment-space geometry and extremal problems.

For finite support, Prékopa explicitly formulated discrete moment problems as linear programs and derived sharp bounds and dual-basis structure. This is particularly close in spirit to the present finite-support LPs.

**Classification:** `CLASSICAL`.

References:

- M. G. Krein and A. A. Nudelman, *The Markov Moment Problem and Extremal Problems*, AMS, 1977.
- A. Prékopa, “The discrete moment problem and linear programming,” *Discrete Applied Mathematics* **27** (1990), 235–254. DOI: https://doi.org/10.1016/0166-218X(90)90068-N

## 2.4 Extreme probability measures under prescribed Laplace-transform information are not new

This is an especially important near-neighbor.

Karr studied extreme points of sets of probability measures with prescribed integrals of finitely many functions and explicitly listed applications to measures with prescribed moments **or values of Laplace transforms**.

Therefore, a statement such as

> “extremizers under finitely many transform constraints have sparse support”

would not be a safe novelty claim for this project.

**Classification:** `CLASSICAL / CLOSE PRIOR ART`.

Reference: A. F. Karr, “Extreme Points of Certain Sets of Probability Measures, with Applications,” *Mathematics of Operations Research* **8** (1983), 74–85. DOI: https://doi.org/10.1287/moor.8.1.74

## 2.5 Generalized moment problems can involve multiple measures

The generalized moment problem is linear optimization over positive measures subject to linear integral constraints. Modern formulations routinely allow finitely many measures and coupled linear constraints. Thus “we optimize over two positive measures” is not, by itself, a novelty claim.

A recent example states the GMP directly as optimization over finitely many Borel measures with linear integral constraints.

**Classification:** `CLASSICAL FRAMEWORK / MODERN STANDARD FORM`.

Example reference: C. Cardoen, S. Marx, A. Nouy, N. Seguin et al., “A moment approach for entropy solutions of parameter-dependent hyperbolic conservation laws,” *Numerische Mathematik* **156** (2024), 1289–1324. DOI: https://doi.org/10.1007/s00211-024-01428-5

## 2.6 Chebyshev systems, ECT systems, and moment-space sparsity are classical

Karlin and Studden developed the geometry of Tchebycheff systems, moment spaces, canonical/principal representations, and their extremal properties. Krein–Nudelman developed closely related moment/extremal geometry.

In modern statistical language, Dette and Schorning use the fact that boundary points of moment spaces generated by Chebyshev systems have unique representations, and principal representations control extremal design problems.

The present programme uses the same broad geometry when a small support can certify an extremal point.

**Classification:** `CLASSICAL`.

References:

- S. Karlin and W. J. Studden, *Tchebycheff Systems: With Applications in Analysis and Statistics*, Interscience, 1966.
- H. Dette and K. Schorning, “Complete classes of designs for nonlinear regression models and principal representations of moment spaces,” *Annals of Statistics* **41** (2013), 1260–1267. DOI: https://doi.org/10.1214/13-AOS1108 ; arXiv: https://arxiv.org/abs/1306.4872

## 2.7 Total positivity and variation-diminishing arguments are classical

The kernel

\[
K(x,\lambda)=e^{\lambda x}
\]

is a fundamental totally positive kernel. Since

\[
r^x=e^{x\log r},
\]

matrices built from ordered exponential bases are generalized Vandermonde/total-positive objects.

This is the deep reason that linear combinations such as

\[
1,\ x,\ \gamma^x,\ \beta^x,\ s^x,\ \tau^x
\]

have strongly controlled zero and sign-variation behavior when they form the relevant Chebyshev/ECT system.

Accordingly, the basic fact that an ECT-space function has a limited zero budget, or that total positivity supports variation-diminishing behavior, is not original to this project.

**Classification:** `CLASSICAL`.

References:

- S. Karlin, *Total Positivity*, Vol. I, Stanford University Press, 1968.
- A. Pinkus, *Totally Positive Matrices*, Cambridge University Press, 2010. DOI: https://doi.org/10.1017/CBO9780511691713

## 2.8 The connection between total positivity and cyclic-polytope combinatorics is classical

Sturmfels proved an explicit equivalence between totally positive matrices and cyclic polytopes. More generally, coordinate functions of convex/generalized moment curves are tightly connected with Chebyshev systems and oriented sign patterns.

This is relevant because several determinant-orientation facts in A110–A114 may admit a future reformulation in oriented-matroid or cyclic-polytope language.

That possible reformulation would be useful, but the total-positivity/cyclic-polytope connection itself is not ours.

**Classification:** `CLASSICAL`.

Reference: B. Sturmfels, “Totally positive matrices and cyclic polytopes,” *Linear Algebra and its Applications* **107** (1988), 275–281. DOI: https://doi.org/10.1016/0024-3795(88)90250-9

## 2.9 Stochastic orders based on Laplace-transform ratios are classical

Shaked and Wong studied stochastic comparisons defined by ratios of Laplace transforms. Their question is not the same as ours: they study order/monotonicity properties of transform ratios across the transform parameter, whereas this project extremizes a ratio at one node subject to moment and transform-band constraints at other nodes.

Still, their work is important prior context. We should not claim that “ratios of Laplace transforms of two distributions” are a new object.

**Classification:** `CLASSICAL NEIGHBORING LITERATURE`.

Reference: M. Shaked and T. Wong, “Stochastic orders based on ratios of Laplace transforms,” *Journal of Applied Probability* **34** (1997), 404–419. Stable publisher page: https://www.cambridge.org/core/journals/journal-of-applied-probability/article/stochastic-orders-based-on-ratios-of-laplace-transforms/550438678A2CA99A9F2F0204AEF3A426

---

# 3. What the project actually adds mathematically

The following statements are **project theorems**, meaning they were derived and certified in this repository. “Project theorem” does not automatically mean “world-first theorem”. Literature novelty is assessed separately.

## 3.1 A113: global compressed one-variation in the analytic tail

Under the frozen reduced/compressed contract, A113 proves that the adjacent objective factors satisfy

\[
E_{M,k}>0\quad(k\le b),
\]

\[
E_{M,k}<0\quad(k\ge b+3),
\]

and the central nesting inequality

\[
\boxed{E_{M,b+1}-2E_{M,b+2}>0}.
\]

Consequently the full adjacent-factor sequence has exactly one positive-to-negative variation and the compressed maximizer is confined to

\[
\boxed{\{b+1,b+2,b+3\}}.
\]

A113 is not merely “Chebyshev systems have few zeros”. Its proof uses the exact ten-term factor, parity-sensitive tail estimates, and the special cancellation caused by `2 tau = 1` in the central combination.

### Literature position

We found classical variation-diminishing and total-positivity theory, but we did **not** locate a theorem in the reviewed sources that directly gives the A113 factor inequalities or the exact three-contact localization for this family.

However, this remains an important open novelty check:

> Can A113 be re-expressed as a direct corollary of a classical variation-diminishing transform or a known sign-regular kernel theorem?

If yes, the conceptual novelty of A113 would decrease, although the explicit specialization and quantitative tail bounds could remain useful.

**Current novelty status:** `APPARENTLY_UNREPORTED / NOVELTY_NOT_CERTIFIED`.

## 3.2 A110 + A112: adjacent-boundary structure for the gamma-plus family

A110 proves the corrected bilateral adjacent-boundary mechanism on the frozen finite envelope. A112 proves the analytic-tail structural theorem in the frozen gamma-plus family. In the tail, complete strict KKT reduces to the positivity of the two adjacent P masses, and the only internal KKT boundaries are the corresponding adjacent mass-zero surfaces.

The proof combines exact Cramer identities, determinant orientation, active-dual signs, Chebyshev/ECT zero counts, and monotonicity of the adjacent masses.

### Literature position

The individual ingredients are classical. Parametric active-set changes are classical; moment-space sparse representations are classical; ECT zero budgets are classical.

What was not found in the reviewed literature is this exact theorem for the present exponential-moment family, with the stated support pattern and uniform finite-plus-tail coverage.

**Current novelty status:** `PROJECT_SPECIFIC_NO_MATCH_FOUND / NOVELTY_NOT_CERTIFIED`.

## 3.3 A114: exact lifted active-set classification in the strict tail interior

The strongest project-specific result currently is the strict active-set classification.

For the strict `b+2`, `Phi<0` tail, the promoted chain is

\[
\boxed{
\begin{array}{rcl}
p_0^C>0 &\Longrightarrow& C,\\
p_0^C<0,\ r_E(q_0)>0 &\Longrightarrow& E,\\
p_0^C<0,\ r_E(q_0)<0,\ \Gamma>0 &\Longrightarrow& QI,\\
p_0^C<0,\ r_E(q_0)<0,\ \Gamma<0 &\Longrightarrow& QA,
\end{array}}
\]

where

\[
\Gamma=S_{\gamma-}^{QI}.
\]

The transitions can be read as a staircase

\[
\boxed{
C\xrightarrow{p_0^C=0}
E\xrightarrow{r_E(q_0)=0}
QI\xrightarrow{S_{\gamma-}^{QI}=0}
QA.
}
\]

The project does not merely enumerate those bases. It proves determinant orientations, bordered pivot identities, primal/dual positivity, inactive slacks, and all nonbasic reduced costs over the declared analytic-tail contract. The last closure, A114-B2-C3, is backed by a 97/97 rational analytic certificate, a 79/79 independent `Fraction` crosscheck, and a 27/27 logical-composition audit.

### Literature position

The general idea “optimal bases change across KKT boundaries” is classical. The individual objects “basic mass”, “reduced cost”, and “slack” as pivot discriminants are classical simplex/KKT quantities.

What we did **not** locate is an existing theorem that, for a pair of probability measures with common mean and bilateral exponential-transform constraints, produces this exact support sequence and proves that these three discriminants exhaust the strict interior.

The closest literatures each cover only part of the picture:

- parametric LP: basis regions and neighboring pivots;
- moment theory: sparse/extremal measures;
- Tchebycheff systems: uniqueness/principal representations and zero control;
- total positivity: determinant signs and variation diminution;
- Laplace-transform stochastic orders: comparisons of transform ratios;
- GMP: optimization over one or several measures.

The current theorem sits at their intersection.

**Current novelty status:** `APPARENTLY_UNREPORTED / NOVELTY_NOT_CERTIFIED`.

---

# 4. A novelty map for reviewers

| Item | What the project uses/proves | Literature assessment | Safe status |
|---|---|---|---|
| Ratio objective homogenized by a scale variable | `G_mu(tau)/G_nu(tau)` converted to LP form | Charnes–Cooper and linear-fractional programming are classical | `CLASSICAL` |
| Parameter regions with fixed optimal basis | Active-set/basis changes with source parameter | Classical parametric LP | `CLASSICAL` |
| Optimization over probability measures with moment constraints | `mu`, `nu` with shared mean | Classical moment/GMP framework | `CLASSICAL` |
| Sparse extremal measures under transform information | finite atomic supports | Karr and moment-space theory already cover sparse/extreme measures under integral/Laplace constraints | `CLASSICAL / CLOSE PRIOR ART` |
| Chebyshev/ECT zero budget | closes whole reduced-cost families from finitely many sentinels | Classical Karlin–Studden / total positivity | `CLASSICAL` |
| Generalized Vandermonde determinant signs | orientation of exponential interpolation matrices | Classical total positivity | `CLASSICAL` |
| Principal/canonical representations | sparse representations of moment-space points | Classical | `CLASSICAL` |
| Total positivity ↔ cyclic-polytope combinatorics | possible oriented-matroid interpretation | Sturmfels and related literature | `CLASSICAL` |
| Laplace-transform ratio comparisons | ratio of transforms of two measures | Shaked–Wong and stochastic-order literature | `CLASSICAL NEIGHBOR` |
| A113 one-variation theorem with exact `{b+1,b+2,b+3}` localization | uniform tail theorem for the project’s exact factor | no exact match located in targeted review | `APPARENTLY_UNREPORTED / NOVELTY_NOT_CERTIFIED` |
| A110/A112 exact adjacent-boundary theorem for frozen gamma-plus family | full KKT iff adjacent masses positive; no hidden interior components | no exact match located | `PROJECT_SPECIFIC_NO_MATCH_FOUND` |
| A114 `C→E→QI→QA` strict active-set staircase | complete strict interior classification by three explicit discriminants | no exact match located | `APPARENTLY_UNREPORTED / NOVELTY_NOT_CERTIFIED` |
| Exact all-tail determinant/sign bounds used to certify the staircase | quantitative specialization for fixed nodes/window | project-specific calculations; general sign tools classical | `PROJECT_SPECIFIC_NO_MATCH_FOUND` |
| Fraction-only independent reconstruction + logical audits | proof-engineering/provenance discipline | methodology, not a mathematical novelty claim | `REPRODUCIBILITY CONTRIBUTION`, not theorem novelty |

---

# 5. The extracted general structure — useful, but not yet proved as a general theorem

The completed special-case analysis suggests a broader statement. We should treat it as a research target, not as a theorem.

## Working name

**Coupled Exponential-Moment Active-Set Staircase**

## Candidate abstract setting

Let `mu` and `nu` be positive probability measures on an ordered finite support. Impose shared low-order moments and bilateral constraints

\[
|G_\mu(r_i)-G_\nu(r_i)|\le \delta_i
\]

at ordered transform nodes

\[
0<r_1<r_2<\cdots<r_m<1,
\]

and optimize a transform ratio

\[
\frac{G_\mu(\tau)}{G_\nu(\tau)}.
\]

Assume the relevant function family forms an extended complete Chebyshev system and that determinant orientations remain fixed in the parameter region under study.

The project suggests that, under additional separation/nondegeneracy hypotheses, the optimal supports may evolve through a short sequence of adjacent pivots, each transition being detected by a single KKT discriminant: a basic mass, a reduced cost, or an inactive-band slack.

For the frozen project family, the staircase is exactly

\[
C\to E\to QI\to QA.
\]

## Status

**NOT PROVED in this generality.**

This is an abstraction extracted from the special-case theorem, not a promoted result.

A serious generalization would replace the numerical ordering

\[
\gamma=1/16,\quad \beta=1/8,\quad s\approx0.13,\quad \tau=1/2
\]

by symbolic inequalities such as

\[
0<\gamma<\beta<s<\tau<1
\]

and prove the active-set topology on an open parameter region.

If that succeeds, it would be substantially more interesting than adding further case-specific constants.

---

# 6. Where a genuinely reusable contribution may lie

The strongest potential contribution is not any one classical tool. It is the reduction of a large KKT system to a small topological/sign problem.

In the current proofs, thousands of possible nonbasic inequalities are not checked one by one in the analytic theorem. Instead:

1. exact Cramer/bordered identities identify a small number of pivot discriminants;
2. total positivity fixes determinant orientation;
3. tail separation gives uniform quantitative margins;
4. ECT zero budgets turn a few positive sentinels into positivity of an entire reduced-cost family;
5. the resulting strict regions fit into a short active-set staircase.

That composition may be useful in other structured moment programs even if every ingredient is classical.

Possible application domains are mathematical rather than currently physical:

- robust probability and extremal-distribution bounds;
- reliability and actuarial problems involving Laplace transforms;
- queueing models where transform inequalities are natural;
- optimal experimental design and moment-space methods;
- finite-support generalized moment problems;
- structured parametric LPs with exponential kernels;
- algorithms that exploit sign-regular/ECT structure to avoid exhaustive KKT scans.

These are plausible transfer directions, not claims that the current theorem has already solved problems in those fields.

---

# 7. What would reduce or eliminate the novelty claim?

A responsible novelty note should state how it could be falsified.

The apparent novelty of A113/A114 would be substantially weakened if any of the following is found:

1. **A direct classical theorem implies A113.**  
   If the complete A113 adjacent-factor sequence can be represented as a totally-positive transform of a sequence with one sign change, and classical variation-diminishing theory immediately yields the exact localization and central behavior, then A113 becomes primarily a specialization/quantitative corollary.

2. **Moment-space theory already gives the full support staircase.**  
   If a theorem of Karlin–Studden/Krein–Nudelman type applied to two coupled measures and bilateral transform bands already forces the support sequence `C/E/QI/QA`, then A114 is a rediscovery in specialized coordinates.

3. **Oriented-matroid/cyclic-polytope theory forces the pivot graph.**  
   If the allowed bases and transitions follow directly from the chirotope of a generalized moment curve, the combinatorial part of A114 may be classical, leaving only quantitative feasibility thresholds as project-specific.

4. **Parametric semi-infinite/moment programming contains an equivalent active-set theorem.**  
   A theorem giving the same finite sequence of supports for this class of transform constraints would supersede the apparent novelty.

We have not located such a theorem in the present search. That statement should be read literally: **not located**, not **does not exist**.

---

# 8. What can safely be said today

## Safe wording

> The A110–A114 programme combines classical tools from parametric linear programming, moment-space theory, Tchebycheff/ECT systems, total positivity, and simplex/KKT analysis. Within a frozen exponential-moment family, it derives exact finite- and analytic-tail structure, including a one-variation theorem for the compressed objective and a complete strict-interior active-set classification. A targeted literature review found close classical precedents for each major tool and for sparse extremal measures under moment/Laplace constraints, but did not locate the same combined classification theorem. Novelty therefore remains plausible but not certified.

## Wording to avoid

Do **not** write:

- “We invented a new kind of linear programming.”
- “Sparse extremal measures are new.”
- “Using Laplace-transform ratios is new.”
- “The generalized Vandermonde/ECT argument is new.”
- “This is the first theorem of its kind.”
- “No previous work exists.”
- “This establishes a new physical law.”

The current results are mathematical results for a declared optimization family. They do not establish that nature uses this family.

---

# 9. Literature-search method and limitations

This positioning note was prepared from a targeted literature review on 2026-09-14. Searches included combinations of:

- multiparametric / parametric linear programming, critical regions, basis changes;
- linear fractional programming and Charnes–Cooper transformation;
- discrete and generalized moment problems;
- extreme probability measures with prescribed moments or Laplace transforms;
- multiple-measure generalized moment problems;
- Tchebycheff/Chebyshev/ECT systems and principal representations;
- total positivity, exponential kernels, generalized Vandermonde matrices, variation diminution;
- cyclic polytopes, oriented matroids, and total positivity;
- Laplace-transform ratio stochastic orders;
- parametric optimization of measures and active-set continuation.

The review prioritized foundational monographs, primary papers, publisher pages, DOI records, and modern papers that explicitly connect the classical theories to current terminology.

This is **not** a systematic review of every paper in approximation theory, semi-infinite programming, moment problems, stochastic orders, or optimal design. Citation chains in Karlin–Studden, Krein–Nudelman, Karr, Prékopa, Pinkus, and the semi-infinite programming literature should be followed by a domain specialist before any priority claim is made in a manuscript.

---

# 10. Core references

1. **Charnes, A.; Cooper, W. W.** (1962). “Programming with Linear Fractional Functionals.” *Naval Research Logistics Quarterly* 9, 181–186. https://doi.org/10.1002/nav.3800090303

2. **Gal, T.; Nedoma, J.** (1972). “Multiparametric Linear Programming.” *Management Science* 18, 406–422. https://doi.org/10.1287/mnsc.18.7.406

3. **Karlin, S.; Studden, W. J.** (1966). *Tchebycheff Systems: With Applications in Analysis and Statistics*. Interscience.

4. **Karlin, S.** (1968). *Total Positivity, Vol. I*. Stanford University Press.

5. **Krein, M. G.; Nudelman, A. A.** (1977). *The Markov Moment Problem and Extremal Problems*. American Mathematical Society, Translations of Mathematical Monographs 50.

6. **Karr, A. F.** (1983). “Extreme Points of Certain Sets of Probability Measures, with Applications.” *Mathematics of Operations Research* 8, 74–85. https://doi.org/10.1287/moor.8.1.74

7. **Sturmfels, B.** (1988). “Totally Positive Matrices and Cyclic Polytopes.” *Linear Algebra and its Applications* 107, 275–281. https://doi.org/10.1016/0024-3795(88)90250-9

8. **Rupp, T.** (1989). “Kuhn-Tucker curves for one-parametric semi-infinite programming.” *Optimization* 20, 61–77. https://doi.org/10.1080/02331938908843414

9. **Prékopa, A.** (1990). “The discrete moment problem and linear programming.” *Discrete Applied Mathematics* 27, 235–254. https://doi.org/10.1016/0166-218X(90)90068-N

10. **Shaked, M.; Wong, T.** (1997). “Stochastic orders based on ratios of Laplace transforms.” *Journal of Applied Probability* 34, 404–419. Publisher page: https://www.cambridge.org/core/journals/journal-of-applied-probability/article/stochastic-orders-based-on-ratios-of-laplace-transforms/550438678A2CA99A9F2F0204AEF3A426

11. **Pinkus, A.** (2010). *Totally Positive Matrices*. Cambridge Tracts in Mathematics 181. https://doi.org/10.1017/CBO9780511691713

12. **Dette, H.; Schorning, K.** (2013). “Complete classes of designs for nonlinear regression models and principal representations of moment spaces.” *Annals of Statistics* 41, 1260–1267. https://doi.org/10.1214/13-AOS1108 ; https://arxiv.org/abs/1306.4872

13. **Cardoen, C.; Marx, S.; Nouy, A.; Seguin, N.; et al.** (2024). “A moment approach for entropy solutions of parameter-dependent hyperbolic conservation laws.” *Numerische Mathematik* 156, 1289–1324. https://doi.org/10.1007/s00211-024-01428-5

---

# 11. Project files most relevant to this positioning

- `MFRP_Informational_Requirements_A39-A109/research_updates/A110_A112/session_artifacts/A112_ANALYTIC_TAIL_STRUCTURAL_THEOREM_20260911.md`
- `MFRP_Informational_Requirements_A39-A109/research_updates/A113/session_artifacts/A113_ANALYTIC_TAIL_GLOBAL_COMPRESSED_ONE_VARIATION_THEOREM_20260911.md`
- `MFRP_Informational_Requirements_A39-A109/research_updates/A114/A114B2C1_ENDPOINT_RELEASED_NEGATIVE_PIVOT_BRANCH_THEOREM_20260913.md`
- `MFRP_Informational_Requirements_A39-A109/research_updates/A114/A114B2C2_COMPRESSED_NEGATIVE_PIVOT_BRANCH_THEOREM_20260913.md`
- `MFRP_Informational_Requirements_A39-A109/research_updates/A114/A114B2C3_QI_QA_RESIDUAL_BRANCH_THEOREM_20260914.md`
- `MFRP_Informational_Requirements_A39-A109/research_updates/A114/A80_A114_LONGITUDINAL_AUDIT_20260913.md`

The distinction to keep in mind is simple:

> **The tools are mostly classical. The exact theorem package and the active-set classification are project results. Whether those project results are genuinely new to the literature remains a specialist-review question, and this repository intentionally says so.**
