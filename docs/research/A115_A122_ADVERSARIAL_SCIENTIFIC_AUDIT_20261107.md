# A115–A122: adversarial scientific audit

**Review date:** 7 November 2026  
**Scope:** the actively developed formal branch, the A64/A81/A83/A113/A115 source contracts, and the computational/formal claims reused from A118–A122. This is a **targeted audit**, not a certification of every historical file in the repository.  
**Verdict:** `PASS_WITH_MATERIAL_LIMITATIONS_AND_CORRECTIONS`; **not ready to claim global LP optimality or mathematical priority**.

## Why I carried out this review

I wanted to know whether the recent sequence of Lean proofs and rational tests actually supports the interpretation being given to A115–A122. Passing tests is not enough if the wrong thing is tested, if an output is merely printed when it should be asserted, or if a reduced active-set calculation is mistaken for the full optimization problem.

I inspected the source implementations, archived attempts, formal statements and real GitHub Actions job records. I also checked a selection of historical citations at the publishers' pages and independently constructed a full-band feasibility sanity witness.

## 1. What I could verify

| Evidence | Observation | Defensible conclusion |
|---|---|---|
| [Lean run 42360306701](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42360306701), source SHA `de666c070d41a4955a3457e3cfe832ea9a48fe15` | **25 of 25 jobs SUCCESS** | The imported Lean modules and their individually checked statements passed under the pinned toolchain |
| [Lean run 42360295371](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42360295371) | **25/25 SUCCESS** | Earlier equivalent Lean checkpoint also passed |
| The actual current `.lean` files | Eight relevant content hashes — including the entrypoint, formal core modules and workflow — **match** those at the successful source commit | The checked Lean sources were not silently replaced after the cited success |
| [Python run 42371029548](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42371029548) | All workflow steps SUCCESS, including A115, A119 and A122 scripts | The published finite arithmetic tests executed successfully, but their assertions must be inspected to know what was proved |
| [Python run 42376765403](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42376765403) | SUCCESS after adding a separate centered-support witness | The full-band feasibility sanity test has a reproducible initial checkpoint |
| [A115 gamma audit](../formal/A115_INHERITED_GAMMA_BAND_COMPATIBILITY_20261107.md) | 213 adjacent pairs; 159 pairs with nonnegative sparse weights; 0 pairs with both gamma bands satisfied; 2 gamma-feasible *individual occurrences* out of 426 | A finite incompatibility of the *chosen compressed active set* with an inherited gamma band; not full-LP infeasibility |

The `Lean 4.33.1` / Mathlib `v4.33.1` toolchain is pinned. The workflow rejects source occurrences of `sorry` or `admit`, compiles the project, and runs the Leanchecker kernel replay module by module. I also inspected the current relevant formal module sources for `axiom`, `unsafe`, `sorry`, `admit`, and `native_decide` tokens: none appeared in the selected modules. This check is not a proof of every external dependency, but the versioned build/replay evidence is real.

**Important:** the Lean statements are primarily exact algebraic identities, equivalences under stated nonzero denominators, and implications with explicit sign premises. A successful kernel replay is not evidence that every premise has been derived for the intended full LP.

## 2. A literal mathematical statement that needs correction in A113

[A113's theorem note](../../MFRP_Informational_Requirements_A39-A109/research_updates/A113/session_artifacts/A113_ANALYTIC_TAIL_GLOBAL_COMPRESSED_ONE_VARIATION_THEOREM_20260911.md) writes

```text
E_(M,k) = V_(M,k+1) - V_(M,k).
```

But the earlier [A83 factorization](../../MFRP_Informational_Requirements_A39-A109/docs/technical_notes/MFRP_next_step_seven_term_adjacent_sign_atlas.md) calls `E` a *factor* of the cross numerator, and the newly kernel-checked [active-band derivation](../formal/A115_COMPRESSED_ADJACENT_OBJECTIVE_IDENTITY_20261107.md) gives, for the **literal scaled target objective**,

```text
(V_(k+1)-V_k) * Delta_k * Delta_(k+1) = -Z * E_(M,k).
```

These expressions are not equal numerically unless the omitted rational factor happens to be 1. I checked this independently with exact `Fraction` arithmetic at both:

- `M=24, k=4, s=129/1000, tau=1/2`;
- **inside A113's published frozen range**: `M=521, k=90, s=131/1000, tau=1/2`.

In both cases `E != V_(k+1)-V_k`, `E!=0`, and the full cross-multiplied identity holds exactly. The second case has `2<=k<=floor(M/2)-2` and satisfies the frozen `M>=521` and source-window conditions. The earlier source may have intended `V` to mean a specially normalized sequence, but no such normalization is stated in the displayed A113 definition.

**Required correction:** either define that normalized `V` exactly and prove it, or replace the literal equality with the cross-product factorization and explicitly state the positive-prefactor assumptions. This is a correction of a statement/notation, not a refutation of A113's one-sign-variation result by itself.

The exact in-range nonidentity is now a regression condition in [`a115_independent_compressed_adjacent_identity_20261107.py`](../../audits/a115_independent_compressed_adjacent_identity_20261107.py).

## 3. A genuine weakness in the test harness: printing instead of asserting

The former independent A119 checker [`a119_independent_fraction_certificate_20261106.py`](../../audits/a119_independent_fraction_certificate_20261106.py) **asserted** the lower bounds of the 6,400 rational interval boxes, but merely **printed** the two tail-cutoff signs. A script could have reported `False` for a tail cutoff and still exited with status zero. Therefore, its former CI `SUCCESS` did not by itself certify that its tail-cutoff assertions passed — they were not assertions.

The former independent A122 checker [`a122_independent_rational_log_brackets_20261106.py`](../../audits/a122_independent_rational_log_brackets_20261106.py) similarly printed a Boolean `certified sign` without failing when the expected negative or positive sign was missing. It also lacked explicit positivity checks for every logarithm argument.

**Corrective changes already committed:**
- A119 now asserts both exact rational cutoff lower bounds are strictly positive, checks both claimed decay-ratio bounds are inside `(0,1)`, checks interval-domain validity and positive critical denominators, and asserts the expected even/odd box counts.
- A122 now asserts `x>0` before evaluating logarithm bounds, verifies interval and phase domains, and requires the *specific* strict sign at each of the two rational targets.
- The gamma-band script now asserts the count **2** rather than just printing it.

These are improvements to **test acceptance conditions**. They do not independently establish the source-to-A118 formula, A119's entire analytic tail proof, or A122's discrete resonance realization. The strengthened CI run's conclusion must be read before claiming that the corrections have passed.

## 4. The third-node gamma contract must stay conditional

[A81's reduced system](../../MFRP_Informational_Requirements_A39-A109/audits/a81_reduced_boundary_system_audit.py) includes the third node `gamma=1/16`. The [A115 target-deformation script](../../MFRP_Informational_Requirements_A39-A109/research_updates/A115/a115_target_deformation_exact_audit.py) analyzes the two-band compressed factor and does not independently impose the inherited gamma constraint.

On the finite grid, requiring the inherited band `|P_gamma-Q_gamma|<=2*epsilon*t` left **0 of 213** pairs with both contacts gamma-feasible. Only **2 of 426 individual occurrences** passed that gamma band; these are not 426 distinct parameter/contact tuples. This is exact finite evidence and is explicitly conditional on importing A81's gamma contract unchanged.

It would be an error to write either of these stronger statements:
- “The original full LP is infeasible”; or
- “A115 formally assumes the gamma band.”

The precise optimization problem must be fixed before using a compressed sign change to make a global claim. Later work should write one full primal with *every* mass, moment, normalization, band, nonnegativity and objective requirement, and then derive its dual with the correct orientation.

## 5. Independent feasibility sanity witness: the full LP is not ruled out

If the full finite program allows coincident probability measures, choose `P=Q` supported at the center of `{0,...,M}`. For `0<tau<1`:

- **Even M=2h:** put the common scaled mass `t=tau^(-h)` at `h`.
- **Odd M=2h+1:** put the common scaled mass `v=1/[tau^h*(1+tau)]` at each of `h,h+1`, giving `t=2v`.

In either parity, `t>0`, both sums of masses equal t, both first moments are `M*t/2`, and `Q_tau=1`. Because the two measures coincide, **every transform difference is zero at every observation node**, including beta, s and gamma. Their target-transform ratio (the scaled P objective) is exactly 1.

This is an elementary **all-M algebraic feasibility construction** for the nonnegative symmetric-band version of the full contract, provided no extra constraint forbids coincident distributions. It is not a proof of optimality, and it does not satisfy the *selected active equalities* at their nonzero endpoints.

The independent [centered witness script](../../audits/a115_unrestricted_centered_witness_20261107.py) checked the mass, mean, target and all displayed bands for 40 exact combinations of M and tau. [CI run 42376765403](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42376765403) reported success and the exact 40-control line.

This is a useful falsification check: elimination of one chosen three-site *architecture* does not eliminate every feasible measure.

## 6. What remains valid and what remains open

| Research claim | Current epistemic status |
|---|---|
| Three-site P and central Q normalization identities | **Lean-checked**, under the precise assumptions in the files |
| Central-Q weight nonnegativity equivalences | **Lean-checked** for the three-site block, not the full LP |
| A115 cofactor/ten-channel identity and finite-basis derivation | **Lean-checked algebra** |
| Adjacent objective identity from the two active bands | **Lean-checked conditional identity**; the rational prefactor cannot be omitted |
| Strict sign of the common Cramer numerator `Z<0` | A self-contained **handwritten uniform argument** from monotonicity of L and R; Lean checks its algebraic cancellation, conditional sign step and all-index power inequality, **not** the final derivative/strict-monotonicity link |
| Positive interior masses imply determinant orientation | **Lean-checked conditional theorem** |
| Global full-LP primal feasibility of the selected compressed basis | **Not established**; gamma stress shows failures among sampled candidates |
| Global dual reduced costs, KKT and uniqueness of the deformed LP optimum | **Not established** |
| A118 second-order coefficient `Xi` derived independently from the original finite LP | **Not established by the independent A119 checker** |
| A119 positive interval certificate for the published substituted formula | The exact rational covering is reproducible; strengthened assertions are an added audit gate; **not end-to-end Lean-certified** |
| A122 sign brackets and continuous root | Two rational sign brackets can be certified; the passage to a discrete resonant subsequence is **not certified** |
| New mathematical law or first-priority result | **Not certified**; separate close literature comparison and external peer review are needed |

## 7. Failed formalization was disclosed, not secretly converted to PASS

The abandoned strict monotonicity attempt was preserved verbatim in [`A115_FAILED_SOURCE_MONOTONICITY_LEAN_20261107.md`](../formal/experiments/A115_FAILED_SOURCE_MONOTONICITY_LEAN_20261107.md). Actual build runs [42359621482](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42359621482), [42359869530](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42359869530), and [42360042902](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42360042902) failed.

Run [42360292504](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42360292504) had 25 successful jobs and **one failed individual monotonicity job**. Its log states `Could not find any oleans for: PrecategoryFormal.CompressedSourceMonotonicity`. The experimental source was not part of the successful imported build. It was subsequently removed from the active matrix; [run 42360306701](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42360306701) then passed 25/25. This must not be described as repairing the missing strict-monotonicity proof.

The separate gamma audit had an initially **wrong stronger assertion** (`single_gamma==0`): [run 42370993450](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42370993450) failed, and the corrected finite-pair / individual distinction passed [42371029548](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42371029548).

The history should remain in place. A compilation mistake is not an empirical counterexample; a mistaken test assertion *is* an audit defect; and an infeasible candidate is not an infeasible full LP.

## 8. Prior work and priority

I checked journal metadata against the publishers' pages:
- **A. Charnes and W. W. Cooper (1962)**, “Programming with Linear Fractional Functionals,” *Naval Research Logistics Quarterly* 9(3–4), 181–186. DOI: https://doi.org/10.1002/nav.3800090303
- **Tomas Gal and Josef Nedoma (1972)**, “Multiparametric Linear Programming,” *Management Science* 18(7), 406–422. DOI: https://doi.org/10.1287/mnsc.18.7.406
- **András Prékopa (1990)**, “The Discrete Moment Problem and Linear Programming,” *Discrete Applied Mathematics* 27(3), 235–254. DOI: https://doi.org/10.1016/0166-218X(90)90068-N
- **Alan F. Karr (1983)**, “Extreme Points of Certain Sets of Probability Measures, with Applications,” *Mathematics of Operations Research* 8(1), 74–85. DOI: https://doi.org/10.1287/moor.8.1.74

The available publisher abstracts cover linear-fractional transformations, parametric LP, discrete moment problems, and extreme measures under Laplace constraints. These ideas are **prior art**; neither the current scripts nor Lean proofs establish novelty over them. I did not perform a systematic full-text prior-art review.

## 9. Required repair order

1. **Fix A113's literal E/value-difference definition**, distinguishing the exact objective difference from its sign-controlling cross-numerator factor, without rewriting the archival source to erase its original language.
2. **Freeze the complete LP contract** for the proposed A115–A122 theorem: whether gamma is present, source/target bands, their scale, positivity, support and the exact objective.
3. **Build independent primal feasibility and dual/KKT checks** of selected candidates; a compressed optimum is not a full optimum.
4. **Close the A118→A119 formula derivation independently**, then strengthen the analytic tail and A122 arithmetic resonance gates; do not promote printed finite tests to global theorems.
5. **Finish the full L/R monotonicity proof in Lean** or preserve it clearly as a verified-on-paper mathematical proof with an incomplete formalization.
6. **Obtain an external mathematical referee**, especially on possible reductions to classical Chebyshev/variation-diminishing moment theory, before claiming originality.

**Bottom line:** the algebraic foundation is substantial and reproducible, and the current project keeps many of its limitations visible. There were still meaningful audit defects: test checks that did not enforce their own printed claims, an A113 equality missing its rational prefactor when interpreted as the literal objective, and a risk of treating reduced-basis failures as full-model infeasibility. These are corrected or explicitly blocked here. No global A115–A122 or novelty claim is authorized by this audit.

## 10. Audit corrections tested: final GitHub evidence

The strengthened [exact-arithmetic CI run 42377130346](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42377130346) completed **SUCCESS** on source commit `f03fe1dd899ae34c42f7ff700cbfb63997e8fc13`. Its logs include all the new mandatory assertions:

- the A113 literal factor/value *nonidentity* at **both** exact controls, including `M=521,k=90,s=131/1000,tau=1/2`;
- the 213 adjacent active-band comparisons and exact finite gamma count (`0/213` pairs, `2/426` individual occurrences);
- the 40 equal-measure full-band witnesses, each with objective exactly 1;
- A119 **strictly positive** rational even/odd tail cutoffs, with exact decay ratio bounds `57/400` and `1197/8600` (both below 1), as well as the 6,400 positive interval cells;
- A122 the **specific** negative and positive signs at the two rational target points, with checked logarithm domains and interval ordering.

The job no longer treats either tail sign or A122 sign as a nonfatal `print` expression. The new sources and workflow on the research branch were compared by blob SHA with the successful CI commit: **six of six files matched**. Later report-only commits cannot retroactively validate other source changes.

This changes the strength of the *finite executable* evidence, not the scope of the mathematical theorem: critical-surface derivations, global LP feasibility of the compressed optimizer, and the all-parameter A119/A122 results are still independent proof obligations.

**Final disposition:** `REPRODUCIBLE_PARTIAL_MATHEMATICS_WITH_RECORDED_CORRECTIONS`. The full research program remains **not certified as a global optimization theorem**.
