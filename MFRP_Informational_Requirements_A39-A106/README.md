# Informational Requirements for Pre-Categorical Relational Models

**Computational audit repository, A39–A106**  
**Author:** Felipe Gianini Romero  
**Programme:** Modal Field Research Programme (MFRP)  
**Repository language:** English

This repository contains the complete computational audit sequence developed from the technical report **“Informational Requirements for Pre-Categorical Relational Models: Identifiability, Measure, Dynamic Closure, and Coarse-Graining”** (MFRP-TR-2026-01, v1.1, July 2026).

The central mathematical object is the Laplace-type transform

\[
L_P(\lambda)=\int e^{-\lambda x}\,dP(x),
\qquad
Q_P(\lambda)=-\frac{1}{\lambda}\log L_P(\lambda),
\]

under finite or controlled observation contracts. The audit sequence studies identifiability, sharp prediction intervals, finite-budget minimax design, continuous anchor optimization, covariance uncertainty, bootstrap calibration, finite-support generalization, exact active-basis phase theorems, dual envelopes, Cramer orientation, signed \(q\)-Schur decompositions, and active-set bifurcation.

## Repository status

- **68 main audits:** A39 through A106.
- **All stored audit verdicts:** `PASS` under their declared contracts.
- **English technical notes:** audit-by-audit notes plus the base non-closure note.
- **English figures:** 110 publication figures, including the A78 selection map, A79 exact compression intervals, the A80 local window atlas, and the A82 contact locator.
- **Exact and numerical outputs:** JSON records with gates, values, boundaries, and verdicts.
- **Original report:** included under `paper/`.

A passing audit means that the code satisfied the gates encoded for its declared mathematical and computational contract. It does **not** convert a finite-domain result into a universal physical theorem. Each technical note states its own scope and boundary conditions.

## Directory layout

```text
.
├── audits/                 # Audit programs and exact helper modules
├── results/                # Full JSON results and compact summaries
├── docs/technical_notes/   # English audit notes
├── figures/                # English-language regenerated figures
├── paper/                  # Original English technical report PDF
├── templates/              # Input/configuration templates for A60–A62
├── tools/                  # Figure generation, verification, and runners
├── tests/                  # Repository integrity tests
├── provenance/             # File mapping and provenance metadata
├── AUDIT_INDEX.md          # One-row index for A39–A106
├── RUNBOOK.md              # Reproduction commands and practical notes
├── REPRODUCIBILITY.md      # Scope, exactness, numerical layers, limitations
└── MANIFEST.sha256         # SHA-256 inventory
```

## Quick verification

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python tools/verify_results.py
python -m unittest discover -s tests -v
```

## Regenerate all English figures

```bash
python tools/generate_english_figures.py
python tools/generate_a79_figure.py
python tools/generate_a80_figure.py
python tools/generate_a82_figure.py
python tools/generate_a83_figure.py
python tools/generate_a84_figure.py
python tools/generate_a85_figure.py
python tools/generate_a86_figure.py
python tools/generate_a87_figure.py
python tools/generate_a88_figure.py
python tools/generate_a89_figure.py
python tools/generate_a90_figure.py
python tools/generate_a91_figure.py
python tools/generate_a92_figure.py
python tools/generate_a93_figure.py
python tools/generate_a94_figure.py
python tools/generate_a95_figure.py
python tools/generate_a96_figure.py
python tools/generate_a97_figure.py
python tools/generate_a98_figure.py
python tools/generate_a99_figure.py
python tools/generate_a100_figure.py
python tools/generate_a101_figure.py
python tools/generate_a102_figure.py
python tools/generate_a103_figure.py
python tools/generate_a104_figure.py
python tools/generate_a105_figure.py
python tools/generate_a106_figure.py
```

The legacy generator reconstructs A47–A71 figures. Dedicated A79, A80, A82, A83, A84, A85, A86, A87, A88, A89, A90, A91, A92, A93, A94, A95, A96, A97, A98, A99, A100, A101, A102, A103, A104, A105, and A106 generators reconstruct the exact compression-interval, local-window-atlas, and contact-locator figures from committed result JSON. The A78 selection map remains committed from its exact result package.

## Re-running audits

The historical audit programs use a flat working-directory convention because later audits read earlier result files by filename. The structured repository therefore includes a runtime materializer:

```bash
python tools/materialize_runtime.py
python tools/run_all_audits.py --from-audit 39 --to-audit 106
```

Several audits are computationally expensive, especially A62, A67, A70, and A71. See `RUNBOOK.md` before starting a full replay. A97 uses a separate two-phase exact replay; run it with `RUNBOOK_A97.md`. A98 uses a discovery-plus-exact-certificate replay; run it with `RUNBOOK_A98.md`. A99 is a direct exact symbolic/rational replay; run it with `RUNBOOK_A99.md`. A100 uses a discovery-plus-exact-certificate replay; run it with `RUNBOOK_A100.md`. A101 is a direct exact symbolic/rational replay; run it with `RUNBOOK_A101.md`. A102 consolidates the complete rational-witness lift atlas; run it with `RUNBOOK_A102.md`. A103 promotes all 76 endpoint-released witnesses to exact witness-containing continuum components; run it with `RUNBOOK_A103.md`. A104 promotes the seven exceptional q0/q1 witnesses to exact two-sided continuum components; run it with `RUNBOOK_A104.md`. A105 promotes the forty legacy two-band witnesses to exact two-sided continuum components; run it with `RUNBOOK_A105.md`. A106 promotes the eighteen legacy gamma-minus witnesses to exact witness-containing continuum components; run it with `RUNBOOK_A106.md`.

## Main result sequence

The sequence progresses from exact finite-grid non-identifiability to increasingly strong design and structural results:

1. **A39–A43:** sharp intervals, monotone refinement, robust interval data, finite-budget and direct-\(Q\) minimax design.
2. **A44–A54:** continuous anchor optimization, noise phase diagrams, target exclusion, continuum witnesses, and a global anchor optimum under the declared contract.
3. **A55–A62:** finite implementability, cost regularization, channel calibration, covariance uncertainty, and model-conditional bootstrap validation.
4. **A63–A65:** general finite-support non-identifiability, scale-normalized noise, and continuous first-anchor stress with exact local sensitivity.
5. **A66–A68:** exact global phase theorems, a five-support family theorem, and an exact dual value-of-information theorem for the first channel.
6. **A69–A71:** Cramer reduction, the obstruction to order-only total positivity, signed \(q\)-Schur dominance, and active-set protection after an orientation bifurcation at \(M=10\).
7. **A72–A77:** local pivot diamonds, complete one-pivot neighborhoods, interval-stable gamma bifurcations, parity-reduced support-size theorems, candidate-versus-actual active-set separation, and an exact contact-family reset.
8. **A78:** exact rational-probe selection across `M=10,...,80`, including three forced gamma-inactive compression resets.
9. **A79:** exact maximal compression intervals at `M=40,57,74`, with contact-entry Cramer-polynomial identities.
10. **A80:** exact local compression-window atlas on `129/1000 <= s <= 133/1000`, with 20 strict-KKT windows, 142 six-term boundary polynomials, and 1,888 interval KKT certificates.
11. **A81:** exact two-variable reduction, closed six-coefficient boundary formulas, positive gap/determinant certificates for all 1,438 admissible contacts, and endpoint-only recovery of the A80 root atlas.
12. **A82:** exact adjacent-contact objective locator at the A78 probe, strict unimodality for all 71 supports, eight recorded primal-feasibility exceptions, and two certified local gamma-orientation switches.
13. **A83:** exact seven-term adjacent-difference factorization, complete local sign atlas for all 1,367 adjacent pairs, and exact rejection of global discrete concavity.
14. **A84:** exact ten-term k-space reduction, finite one-variation stress through `M=300` at three rational probes, and an explicit obstruction to a coefficient-only variation-diminishing proof.
15. **A85:** parity-resolved four-channel dominant balance at the exact transition brackets, an explicit `M=12` counterexample to universal small-support dominance, and the asymptotic contact slope `k/M -> log(2)/(-2 log s)`.
16. **A86:** exact rational slope comparisons, a finite three-contact localizer through `M=300`, and exact finite exclusion thresholds.
17. **A87:** exact secant-residual classification of the three A86 offsets, an exact eight-term fallback, and explicit rejection of global factor monotonicity.
18. **A88:** exact nine-term secant reduction, 8,019 positive local-secant certificates through `M=900` on nine rational probes, four-term-core dominance, and positive parity-phase leading limits.
19. **A89:** explicit continuum positivity threshold `M>=521` for the classifier local secant on the full interval `129/1000<=s<=133/1000`, with an exact rational lower-margin certificate.
20. **A90:** exact all-contact one-variation on nine rational probes for `M=10,...,520`, an integer-scaled evaluator for 594,423 factor signs, and fifteen exact counterexamples to extending the A86 three-contact strip beyond its declared range.
21. **A91:** exact four-channel classification of all fifteen A90 offset-three cells, strict residual dominance in 4,563 eligible cells, and a preserved obstruction to treating the A85 parity-corrected locator as an exact rounding rule.
22. **A92:** exact continuum decisive-factor atlas over 858 algebraic contact cells, 25 strict local offset-three windows, and ten windows missed by the prior nine-probe grid.
23. **A93:** exact full-sequence one-variation on all 25 A92 selected cells, promoting the local windows to global compressed-maximizer windows and certifying eleven exact adjacent global-maximizer exchanges.
24. **A94:** exact full-sequence one-variation on all 858 A92 algebraic cells, with 653 fixed unique maximizers and 205 simple adjacent global exchanges.
25. **A95:** exact rational-witness lifting of the A94 phases, with 980 unique strict natural lifts, 83 lift obstructions, and an exhaustive restricted-family counterexample at `M=125`, `s=33/250`.
26. **A96:** exact unrestricted resolution of the first A95 obstruction, with `P={23,24,125}`, `Q={1,62,63}`, active `alpha+` and `beta-`, inactive gamma, and 259 strict KKT conditions.
27. **A97:** exact algebraic strict-KKT interval for the A96 endpoint-released basis, 76/83 exact resolutions of the A95 obstruction witnesses, and seven preserved q0-entry residual obstructions.
28. **A98:** exact unrestricted resolution of the first A97 residual, with `P={70,396}`, `Q={0,1,198,199}`, active `alpha+` and `beta-`, inactive gamma, and 801 strict KKT conditions.
29. **A99:** exact strict-KKT interval persistence of the A98 q0/q1 basis at `M=396`, plus exact strict resolutions at `M=455,496` and four preserved residual obstructions.
30. **A100:** exact unrestricted resolution of the first A99 residual, with `P={77,78,443}`, `Q={0,1,221,222}`, active `alpha+`, `beta-`, `gamma-`, and 895 strict KKT conditions.
31. **A101:** exact interval persistence of the A100 gamma-active basis at `M=443`, strict resolutions at `M=449,484,490`, and pointwise exact closure of all 83 A95 lift-obstruction witnesses.
32. **A102:** complete exact merge of all 1,063 A95 rational phase witnesses, 676,847 source KKT conditions, and an independent 183-branch replay layer with zero mismatch.
33. **A103:** exact continuum classification of all 76 endpoint-released source segments, with 25 complete-segment certificates, 51 proper strict subcomponents, 55 algebraic KKT boundaries, and exact outside counterexamples.
34. **A104:** exact continuum classification of all seven exceptional q0/q1 source segments, with seven proper two-sided strict subcomponents, 14 algebraic KKT boundaries, exact competing-root ordering, and exact outside counterexamples.
35. **A105:** exact continuum classification of all 40 legacy two-band source segments, with zero complete-segment certificates, 40 proper two-sided strict subcomponents, 80 algebraic KKT boundaries, and 80 exact outside counterexamples.
36. **A106:** exact continuum classification of all 18 legacy gamma-minus source segments, with one complete source-segment certificate, 17 proper one-sided strict subcomponents, 17 algebraic KKT boundaries, and 2,410 exact direct-matrix/rank-one regressions.

See `AUDIT_INDEX.md` for direct links and stored gate counts.

## Scientific boundaries

This repository does not claim:

- a physical spacetime metric or physical calibration of \(\lambda\);
- a universal theorem for all support sizes, means, targets, noise models, or anchor budgets;
- that bootstrap inflation factors are distribution-free constants;
- that finite catalogue or finite-family results automatically extend to continuous or arbitrary domains.

The strongest global continuous theorems are explicitly tied to declared finite-support contracts and fixed anchor completions. The notes preserve negative results and counterexamples, including the failure of order-only total positivity and fixed-signature induction.

## Citation

Use the metadata in `CITATION.cff`. Until a DOI or archival release is assigned, cite the repository version and commit hash.

## License

This package follows the parent repository split licensing model. Software is
licensed under Apache-2.0, and scientific content, documentation, figures,
tables, JSON result files, reports, and other research outputs are licensed
under CC BY 4.0. See `LICENSE_NOTICE.md` and the parent repository `LICENSE.md`.


## A72–A106 update

- **A72:** Exact local pivot diamond at M=10–12; orientation selects between two terminal pivot routes.
- **A73:** Complete declared one-pivot neighborhood at a rational probe and exact M=13 global extension.
- **A74:** Interval-stable gamma-sign bifurcation from M=12 to M=13 and independent exact M=14 extension.
- **A75:** Parity-reduced all-M candidate-orientation theorem on a fixed interval; exact M=15–16 extensions.
- **A76:** Candidate orientation separated from actual active-set selection; no active re-entry at M=22.
- **A77:** Fixed-family double bifurcation and exact active contact reset from {5,6} to {6,7}.
- **A78:** Exhaustive rational-probe contact selection for `M=10,...,80`, with forced two-band compression at `M=40,57,74`.
- **A79:** Exact algebraic compression intervals and exact contact-entry polynomial identities at `M=40,57,74`.
- **A80:** Exact local compression-window atlas for the A78-selected contacts; 20 strict-KKT windows, of which only `M=40,57,74` contain `s0`.
- **A81:** Reduced two-variable boundary system; all six coefficients derived explicitly, 142/142 A80 polynomials reconstructed, and no reversed selected root pairs on the local interval.
- **A82:** Exact adjacent-contact locator; 1,367 nonzero probe comparisons, strict compressed-objective unimodality for all 71 supports, eight primal-feasibility exceptions, and two certified local orientation switches.
- **A83:** Seven-term factorization of all adjacent differences; complete local root/sign atlas and rejection of discrete concavity as the unimodality mechanism.
- **A84:** Ten-term confluent exponential-polynomial reduction in `k`; exact one-variation stress through `M=300` at three rational probes and rejection of the raw coefficient-variation route as a sufficient proof.
- **A85:** Parity-resolved dominant-balance reduction; exact four-term sign control at all A84 transition brackets from `M=13` through `M=300`, one explicit `M=12` counterexample, an exact eight-term fallback, and asymptotic contact localization.
- **A86:** Exact integer comparison of the asymptotic slope, exact width-`1e-5` slope brackets, and a three-contact localization theorem in all 873 A84 support/probe cells.
- **A87:** Exact normalized secant residual for choosing offsets `0,1,2`; full and eight-term classifiers pass all 873 cells, while the four-term `M=12` counterexample is preserved.
- **A88:** Exact nine-term local-secant reduction; 8,019/8,019 positive secants through `M=900` on nine probes, strict four-term-core dominance, and positive even/odd leading-limit margins.
- **A89:** Exact rational majorants convert the A88 asymptotic mechanism into a continuum theorem: the local secant is positive for every declared real probe and every integer `M>=521`.
- **A90:** Exact denominator-cleared all-contact audit below the A89 threshold; 4,599 strict one-variation sequences, a finite four-contact strip, and fifteen preserved offset-three counterexamples.
- **A91:** Exact four-term offset-three discriminant; 4,563/4,563 sign matches with strict six-term-residual dominance, exact recovery of all fifteen offset-three cells, and fifty-four preserved false positives of the parity-corrected continuous screen.
- **A92:** Exact continuum decisive-factor atlas; 858/858 algebraic `b`-cells classified, eleven simple roots isolated, twenty-five strict local offset-three windows certified, and ten between-probe windows added without promoting a global continuum theorem.
- **A93:** Full adjacent-factor continuum certification on the twenty-five A92 cells; fourteen unique global offset-three cells and eleven exact `b+2 -> tie -> b+3` global transitions.
- **A94:** Full adjacent-factor continuum certification on all 858 A92 cells; 653 fixed unique compressed maxima, 205 simple adjacent global exchanges, and one preserved decreasing transition at `M=28`.
- **A95:** Exact rational-witness KKT lift audit; 980 unique natural lifts, 83 obstructions, and no strict pass among 19,421 old-family candidates in the declared obstruction prefix through `M=325`.
- **A96:** Exact unrestricted full-LP resolution at the first obstruction; the unique strict basis releases the forced P endpoint and selects `P={23,24,125}`, `Q={1,62,63}` with gamma inactive.
- **A97:** Exact interval persistence of the A96 basis and an exact 83-witness obstruction atlas; 76 endpoint-released strict passes, seven q0-entry residuals, and zero repairs by direct q1-to-q0 substitution.


- **A98:** Exact unrestricted full-LP resolution at `M=396`, with `P={70,396}` and `Q={0,1,198,199}`.
- **A99:** Exact interval persistence of the A98 basis, two additional strict residual resolutions, and four preserved non-universal-support obstructions.
- **A100:** Exact unrestricted resolution at `M=443`; the lower adjacent P contact returns and gamma-minus becomes active while the q0/q1 central-Q topology persists.
- **A101:** Exact interval persistence of the gamma-active M443 basis, three final strict residual resolutions, and exact pointwise closure of the 83-witness A95 obstruction list.
- **A102:** Complete exact rational-witness lift atlas over all 1,063 A95 phase segments; 980+76+3+4 resolution partition, 676,847 KKT conditions, and 183 independent exact replays.
- **A103:** Exact continuum atlas for all 76 endpoint-released source segments; 25 complete-segment certificates, 51 proper strict subcomponents, 55 locally unique simple algebraic KKT boundaries, and 55 exact negative outside counterexamples.
- **A104:** Exact continuum atlas for all seven exceptional q0/q1 source segments; seven proper two-sided strict subcomponents, 25 candidate roots, 14 selected simple boundaries, 11 exact root-ordering inequalities, and 14 exact negative outside counterexamples.
- **A105:** Exact continuum atlas for all forty legacy two-band source segments; forty proper two-sided strict subcomponents, 181 candidate roots, 80 selected simple boundaries, 101 exact root-ordering inequalities, and 80 exact negative outside counterexamples.
- **A106:** Exact continuum atlas for all eighteen legacy gamma-minus source segments; one complete source-segment certificate, seventeen proper one-sided strict subcomponents, 22 candidate roots, 17 selected simple boundaries, five exact root-ordering inequalities, and seventeen exact negative outside counterexamples.

The current package contains 68 main audits and 110 English figures.
