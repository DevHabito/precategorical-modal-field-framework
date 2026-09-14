# A114 — lifted active-set selection after compressed one-variation

A113 tells us **where the compressed maximum can live**. A114 asks the next question:

> Once the compressed maximizer is known, which lifted LP architecture actually satisfies the full KKT system?

This separation is essential. A compressed maximum and a valid lifted basis are not the same statement; A82 already records compressed-maximizer primal-feasibility exceptions.

## Frozen analytic-tail contract

The current A114 tail results use

`M>=521`, `129/1000<=s<=133/1000`,

with the frozen beta, gamma, target and normalized-tolerance conventions inherited from A112/A113. Write

`b=ceil(M*c(s))`, `c(s)=log(2)/(-2 log(s))`, `h=floor(M/2)`.

## Current status — 2026-09-14

The current classification is now:

- strict compressed `b+3` -> endpoint-released lift (A114-A);
- strict compressed `b+1` -> gamma-plus pivot theorem, including its internal `Phi=0` degeneracy (A114-B1);
- strict compressed `b+2`, `Phi>0` -> gamma-plus at contact `b+2` (A114-B2-A);
- strict compressed `b+2`, `Phi=0` -> unique primal optimum with degenerate `C/G+` coalescence (A114-B2-E);
- strict compressed `b+2`, `Phi<0`, `p0^C>0` -> compressed two-band basis `C` (A114-B2-C2);
- strict compressed `b+2`, `Phi<0`, `p0^C<0`, `r_E(q0)>0` -> endpoint-released basis `E` (A114-B2-C1);
- strict compressed `b+2`, `Phi<0`, `p0^C<0`, `r_E(q0)<0`, `Gamma>0` -> q0/q1 gamma-inactive basis `QI` (A114-B2-C3);
- the same residual premises with `Gamma<0` -> q0/q1 gamma-minus-active basis `QA` (A114-B2-C3);
- `p0^C=0` -> unique primal optimum with degenerate `C/E/QI` coalescence (A114-B2-D);
- `p0^C<0`, `r_E(q0)=0` -> exact one-dimensional optimal face, ending at `QI` for `Gamma>=0` and at `QA` for `Gamma<0` (A114-B2-D);
- `p0^C<0`, `r_E(q0)<0`, `Gamma=0` -> unique primal optimum with degenerate `QI/QA` coalescence (A114-B2-D).

Here

`Phi=F_(b+2)^up`,

`Gamma=S_(gamma-)^QI`.

A114-B2-B separately proves that the pure central-Q gamma-minus family cannot be strictly primal feasible on the `Phi<0` analytic tail.

Therefore the **entire strict compressed `b+2` phase is classified under the frozen tail contract, including its outer `Phi=0` pivot and all internal equality sets**. This does not close the separate surfaces where the compressed maximizer itself is non-strict.

## Literature and novelty positioning

For reviewer-facing context, read [`../../../docs/novelty/A110_A114_LITERATURE_POSITIONING_AND_NOVELTY_MAP_20260914.md`](../../../docs/novelty/A110_A114_LITERATURE_POSITIONING_AND_NOVELTY_MAP_20260914.md).

That note rewrites the current LP family as a **coupled exponential-moment extremal problem** and distinguishes:

- classical tools and close prior art (linear-fractional programming, parametric LP, discrete/generalized moment problems, extremal measures with prescribed Laplace information, Tchebycheff/ECT systems, total positivity, principal representations, cyclic-polytope connections, and Laplace-transform ratio orders);
- project theorems such as A113 and the A114 active-set classification;
- the broader `Coupled Exponential-Moment Active-Set Staircase` as an extracted research conjecture, **not** a promoted general theorem.

The literature note deliberately uses `APPARENTLY_UNREPORTED` / `PROJECT_SPECIFIC_NO_MATCH_FOUND` together with `NOVELTY_NOT_CERTIFIED`; it does not make a priority claim from a negative search result.

## A114-A — strict compressed `b+3`

**PROVED.** If `j=b+3` is the strict compressed maximizer, the unique strict lifted optimum is

`P={j-1,j,M}`, `Q={1,h,h+1}`,

with `alpha+`, `beta-` active and gamma inactive.

The theorem requires strict compressed maximality. The stronger arithmetic statement `j=b+3 => endpoint-released` without that premise is false and has an exact negative control.

Primary files:

- `session_artifacts/A114A_ANALYTIC_TAIL_ENDPOINT_RELEASED_LIFT_THEOREM_20260912.md`
- `session_artifacts/A114A_LOGICAL_COMPOSITION_AUDIT_20260912.md`
- `A114A_CORRECTIONS_AND_DEAD_ENDS_20260912.md`

## A114-B1 — strict compressed `b+1`

**PROVED / CLOSED.** Define `Phi=F_(b+2)^up`.

- `Phi<0`: unique strict gamma-plus lift at contact `b+1`;
- `Phi>0`: unique strict gamma-plus lift at contact `b+2`;
- `Phi=0`: the two neighboring bases meet at the same non-strict degenerate global optimum; strict complementarity/uniqueness are not claimed there.

The determinant orientation is proved independently of adjacent primal positivity:

`D_G = det(C) A(s) > 0`,

using the A110 generalized-Vandermonde determinant sign and A112-G branch regularity. This repairs the circular route that would result from reversing the original A112-B implication.

Primary files:

- `session_artifacts/A114B1_ANALYTIC_TAIL_BPLUS1_GAMMA_PIVOT_THEOREM_20260912.md`
- `session_artifacts/A114B1_LOGICAL_COMPOSITION_AUDIT_20260912.md`
- `A114B1_CORRECTIONS_AND_DEAD_ENDS_20260912.md`
- `session_artifacts/A114B1_GAMMA_PIVOT_ORIENTATION_CERTIFICATE_20260912.json`
- `session_artifacts/A114B1_INDEPENDENT_EXACT_CROSSCHECK_20260912.json`

## A114-B2-W1 — first negative-pivot tail witness

**PROVED POINTWISE ONLY.** At

`M=521, s=129/1000, h=260, b=89, j=91=b+2`,

the unique strict global lifted optimum is

`P={90,91,521}`, `Q={0,1,260,261}`,

with `alpha+`, `beta-`, `gamma-` active.

The theorem is backed by complete exact KKT and an independent `Fraction` reconstruction. The first exploratory simplex run used the wrong odd-parity epsilon scale and is explicitly invalid provenance; the theorem does not depend on it.

## A114-B2-A — strict `b+2`, positive pivot

**PROVED / CLOSED for `Phi>0`.** The unique strict global lifted optimum is gamma-plus at contact `b+2`:

`P={0,b+2,b+3,M}`, `Q={1,h,h+1}`.

The proof uses the independent A114-B1 determinant orientation, exact A112-A adjacent-mass identities and the A112 full-KKT composition. The A102 finite census is consistency evidence only, not an all-tail premise.

Primary files:

- `session_artifacts/A114B2A_POSITIVE_PIVOT_GAMMA_PLUS_THEOREM_20260912.md`
- `session_artifacts/A114B2A_LOGICAL_AUDIT_20260912.md`
- `A114B2A_CORRECTIONS_AND_SCOPE_20260912.md`

## A114-B2-B — negative-pivot pure gamma-minus exclusion

**PROVED LEMMA for `Phi<0`.** The pure central-Q gamma-minus architecture

`P={0,j-1,j,M}`, `Q={1,h,h+1}`

cannot be strictly primal feasible on the analytic tail.

The proof first establishes

`Phi<0 => 3j-h>=13`,

then uses exact even/odd Cramer reductions to prove that positivity of the relevant interior P mass forces the endpoint P mass negative.

Primary files:

- `session_artifacts/A114B2B_GAMMA_MINUS_TAIL_EXCLUSION_THEOREM_20260913.md`
- `session_artifacts/A114B2B_GAMMA_MINUS_TAIL_EXCLUSION_ANALYTIC_CERTIFICATE_20260913.json`
- `A114B2B_CORRECTIONS_AND_SCOPE_20260913.md`

## A114-B2-C1 — endpoint-released negative-pivot branch

**PROVED conditional branch theorem.** Under strict `b+2` and `Phi<0`,

`p0^C<0 and r_E(q0)>0 => E`,

where `E: P={j-1,j,M}, Q={1,h,h+1}` with `alpha+`, `beta-` active and gamma inactive.

The proof contains a B2-specific source box, exact Cramer exchange identity, protected endpoint gates, ECT closure and independent exact controls. Finite controls are regression only.

Primary files:

- `A114B2C1_ENDPOINT_RELEASED_NEGATIVE_PIVOT_BRANCH_THEOREM_20260913.md`
- `A114B2C1_ENDPOINT_PROTECTED_GATES_SUMMARY_20260913.json`
- `A114B2C1_GITHUB_LOGICAL_AUDIT_20260913.json`
- `A114B2C_SOURCE_BOX_CERTIFICATE_20260913.json`

## A114-B2-C2 — compressed negative-pivot branch

**PROVED conditional branch theorem.** Under strict `b+2` and `Phi<0`,

`p0^C>0 => C`,

where `C: P={0,j,M}, Q={1,h,h+1}` with `alpha+`, `beta-` active and gamma inactive.

The analytic certificate passes **49/49** exact rational gates and the logical audit passes **15/15** checks. Finite controls are regression only.

Primary files:

- `A114B2C2_COMPRESSED_NEGATIVE_PIVOT_BRANCH_THEOREM_20260913.md`
- `A114B2C2_COMPRESSED_BRANCH_ANALYTIC_CERTIFICATE_20260913.json`
- `A114B2C2_GITHUB_LOGICAL_AUDIT_20260913.json`
- `a114b2c2_compressed_branch_analytic_certificate.py`
- `a114b2c2_github_logical_audit.py`

## A114-B2-C3 — QI/QA residual branch

**PROVED conditional branch theorem.** Under strict `b+2`, `Phi<0`,

`p0^C<0 and r_E(q0)<0`,

define

`Gamma=S_(gamma-)^QI`,

where `QI: P={j,M}, Q={0,1,h,h+1}` with `alpha+`, `beta-` active and gamma inactive.

Then

- `Gamma>0 => QI`;
- `Gamma<0 => QA`, where `QA: P={j-1,j,M}, Q={0,1,h,h+1}` with `alpha+`, `beta-`, `gamma-` active.

The analytic certificate passes **97/97** exact rational gates. The independent `Fraction` crosscheck passes **79/79** gates and explicitly falsifies the tempting but invalid proof shortcut that QI remains primal-feasible on the QA side. The logical-composition audit passes **27/27** checks. The older independent 12-point package supplies complete atom-by-atom exact KKT scans for the three QI and three QA controls; those controls remain regression/falsification evidence only.

Primary files:

- `A114B2C3_QI_QA_RESIDUAL_BRANCH_THEOREM_20260914.md`
- `A114B2C3_QI_QA_ANALYTIC_CERTIFICATE_20260914.json`
- `A114B2C3_FRACTION_CROSSCHECK_20260914.json`
- `A114B2C3_LOGICAL_AUDIT_20260914.json`
- `A114B2C3_CORRECTIONS_AND_SCOPE_20260914.md`
- `a114b2c3_qi_qa_analytic_certificate.py`
- `a114b2c3_fraction_crosscheck.py`
- `a114b2c3_logical_audit.py`

## A114-B2-D — internal zero-discriminant boundaries

**PROVED conditional boundary theorem; independently red-teamed.** Under strict compressed `b+2` and `Phi<0`:

1. `p0^C=0` gives a unique primal optimum. `C`, `E`, and `QI` are degenerate basis representations of the same primal point after their zero pivot coordinates are deleted.
2. `p0^C<0` and `r_E(q0)=0` gives a genuine one-dimensional primal optimal face. The entire face is `conv{E,QI}` when `Gamma>=0`, with `QI=QA` at `Gamma=0`, and `conv{E,QA}` when `Gamma<0`.
3. `p0^C<0`, `r_E(q0)<0`, and `Gamma=0` gives a unique primal optimum with `QI` and `QA` collapsing to the same primal point.

The D1 boundary certificate uses exact rational arithmetic and passes **13/13** gates. The independent exact boundary regression scans complete P/Q reduced costs on ten adversarial controls and passes **30/30** gates. The hardened logical-composition audit passes **28/28** checks. The independent red-team audit reports **PASS WITH SCOPE** and explicitly tests continuity shortcuts, circularity, hidden optimal directions, rounding sensitivity, ad-hoc phase ordering, and higher-codimension overlap.

Primary files:

- `A114B2D_INTERNAL_ZERO_BOUNDARY_THEOREM_20260914.md`
- `A114B2D_BOUNDARY_HARDENING_NOTE_20260914.md`
- `A114B2D_BOUNDARY_ANALYTIC_CERTIFICATE_20260914.json`
- `A114B2D_EXACT_BOUNDARY_REGRESSION_20260914.json`
- `A114B2D_LOGICAL_AUDIT_20260914.json`
- `A114B2D_RED_TEAM_AUDIT_20260914.md`
- `A114B2D_FRONTIER_UPDATE_20260914.md`
- `a114b2d_boundary_analytic_certificate.py`
- `a114b2d_exact_boundary_regression.py`
- `a114b2d_logical_audit.py`

## A114-B2-E — outer `Phi=0` boundary

**PROVED conditional boundary theorem; independently red-teamed.** Under strict compressed `b+2` and `Phi=0`:

- the C point has all primal masses positive and every nonbasic P/Q reduced cost strict;
- `S_(gamma-)^C>0` and `S_(gamma+)^C=0`;
- the primal optimum is unique;
- the adjacent gamma-plus basis has `p_(j+1)=0`, `p_j>0`, and collapses to the same primal point as C.

The equality-surface analytic certificate passes **22/22** exact rational gates. It re-establishes the B2 source box at `Phi=0` and proves the uniform separation

`p0^C > 0.0029407...`,

so the `Phi=0` and `p0^C=0` surfaces cannot collide inside the frozen tail contract. The independent near-boundary Fraction reconstruction passes **24/24** gates, the section-scoped logical audit passes **32/32**, and a 13-cell exact-rational red-team scan from `M=521` through `M=1000` passes **79/79** gates. The independent red-team audit reports **PASS WITH SCOPE**.

Primary files:

- `A114B2E_PHI_ZERO_BOUNDARY_THEOREM_20260914.md`
- `A114B2E_PHI_ZERO_ANALYTIC_CERTIFICATE_20260914.json`
- `A114B2E_PHI_ZERO_FRACTION_CROSSCHECK_20260914.json`
- `A114B2E_PHI_ZERO_LOGICAL_AUDIT_20260914.json`
- `A114B2E_PHI_ZERO_REDTEAM_SCAN_20260914.json`
- `A114B2E_PHI_ZERO_RED_TEAM_AUDIT_20260914.md`
- `A114B2E_FRONTIER_UPDATE_20260914.md`
- `a114b2e_phi_zero_analytic_certificate.py`
- `a114b2e_phi_zero_fraction_crosscheck.py`
- `a114b2e_phi_zero_logical_audit.py`
- `a114b2e_phi_zero_redteam_scan.py`

## Longitudinal A80–A114 audit

The programme from A80 through A114-B2-C2 was reviewed longitudinally on 2026-09-13 for scope drift, circularity, witness-to-continuum promotion, compressed/lifted conflation, provenance and downstream reuse of refuted claims.

The audit records A108 as **REFUTED / SUPERSEDED**, finds no downstream A110–A114 dependency on its false one-sided rule, and identifies A110 as the independent finite-domain proof of the corrected bilateral adjacent-boundary mechanism.

Read:

- `A80_A114_LONGITUDINAL_AUDIT_20260913.md`
- `A80_A114_LONGITUDINAL_AUDIT_20260913.json`

That dated audit predates C3/D/E. C3, D and E have their own independent certificates, exact crosschecks/regressions, hardening/red-team notes and logical audits listed above; the older audit is retained as a historical snapshot rather than rewritten retroactively.

## Current frontier

Inside every **strict compressed `b+2` phase** under the frozen tail contract, the lifted LP is now classified including equality sets:

- `Phi>0` -> unique strict gamma-plus `G+`;
- `Phi=0` -> unique primal optimum, degenerate `C/G+` coalescence;
- `Phi<0`, `p0^C>0` -> unique strict `C`;
- `Phi<0`, `p0^C=0` -> unique primal optimum, degenerate `C/E/QI` coalescence;
- `Phi<0`, `p0^C<0`, `r_E(q0)>0` -> unique strict `E`;
- `Phi<0`, `p0^C<0`, `r_E(q0)=0` -> exact one-dimensional optimal face;
- `Phi<0`, `p0^C<0`, `r_E(q0)<0`, `Gamma>0` -> unique strict `QI`;
- the same residual branch with `Gamma=0` -> unique primal optimum, degenerate `QI/QA` coalescence;
- the same residual branch with `Gamma<0` -> unique strict `QA`.

The remaining natural A114 boundary problem is no longer an internal `b+2` pivot. It is the set where the **compressed maximizer itself is non-strict**. In A113 notation the principal tie surfaces are

- `E_(b+1)=0`, the `b+1` / `b+2` compressed tie;
- `E_(b+2)=0`, the `b+2` / `b+3` compressed tie.

These surfaces are not classified by the strict-phase A114 theorems and must be studied separately; no limit-from-neighboring-phase rule is assumed.

## Claim boundary

A114 does **not** currently prove:

- the lifted architecture on the compressed tie surfaces `E_(b+1)=0` or `E_(b+2)=0`;
- a universal monotone ordering of all discriminant zeros as `s` varies;
- anything outside the frozen source window `[129/1000,133/1000]` unless explicitly covered by another theorem;
- any physical interpretation.

## Field-note discipline

Failed stronger claims, implementation mistakes, historical waypoints and negative controls remain preserved intentionally. The authoritative current status is this README plus the dated theorem, certificate, logical-audit, hardening, red-team and correction files listed above.
