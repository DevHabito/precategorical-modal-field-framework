# A114 — lifted active-set selection after compressed one-variation

A113 tells us **where the compressed maximum can live**. A114 asks the next question:

> Once the compressed maximizer is known, which lifted LP architecture actually satisfies the full KKT system?

This separation is essential. A compressed maximum and a valid lifted basis are not the same statement; A82 already records compressed-maximizer primal-feasibility exceptions.

## Frozen analytic-tail contract

The current A114 tail results use

`M>=521`, `129/1000<=s<=133/1000`,

with the frozen beta, gamma, target and normalized-tolerance conventions inherited from A112/A113. Write

`b=ceil(M*c(s))`, `c(s)=log(2)/(-2 log(s))`, `h=floor(M/2)`.

## Current status — 2026-09-13

The promoted strict interior classification is now:

- strict compressed `b+3` -> endpoint-released lift (A114-A);
- strict compressed `b+1` -> gamma-plus pivot theorem (A114-B1);
- strict compressed `b+2`, `Phi>0` -> gamma-plus at contact `b+2` (A114-B2-A);
- strict compressed `b+2`, `Phi<0`, `p0^C>0` -> compressed two-band basis `C` (A114-B2-C2);
- strict compressed `b+2`, `Phi<0`, `p0^C<0`, `r_E(q0)>0` -> endpoint-released basis `E` (A114-B2-C1).

Here

`Phi=F_(b+2)^up`.

A114-B2-B separately proves that the pure central-Q gamma-minus family cannot be strictly primal feasible on the `Phi<0` analytic tail.

Therefore the only currently open **strict interior** branch of the negative-pivot `b+2` tail is

`p0^C<0 and r_E(q0)<0`,

where q0/q1 gamma-inactive (`QI`) and q0/q1 gamma-minus-active (`QA`) compete.

The sets `p0^C=0`, `r_E(q0)=0`, and the `b+2` `Phi=0` transition remain separate degenerate/open boundaries unless explicitly covered by a theorem.

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

**PROVED conditional branch theorem.** Let

`C: P={0,j,M}, Q={1,h,h+1}`

and

`E: P={j-1,j,M}, Q={1,h,h+1}`,

both with `alpha+`, `beta-` active and gamma inactive. Under strict `b+2` and `Phi<0`,

`p0^C<0 and r_E(q0)>0 => E`.

The proof contains a B2-specific source box, an exact Cramer exchange identity, protected endpoint gates, ECT closure and independent exact controls. Finite controls are regression only.

Primary files:

- `A114B2C1_ENDPOINT_RELEASED_NEGATIVE_PIVOT_BRANCH_THEOREM_20260913.md`
- `A114B2C1_ENDPOINT_PROTECTED_GATES_SUMMARY_20260913.json`
- `A114B2C1_GITHUB_LOGICAL_AUDIT_20260913.json`
- `A114B2C_SOURCE_BOX_CERTIFICATE_20260913.json`

## A114-B2-C2 — compressed negative-pivot branch

**PROVED conditional branch theorem.** Under strict `b+2` and `Phi<0`,

`p0^C>0 => C`,

where

`C: P={0,j,M}, Q={1,h,h+1}`

with `alpha+`, `beta-` active and gamma inactive.

The analytic certificate passes **49/49** exact rational gates. The logical audit passes **15/15** checks. In particular, the inactive gamma-plus slack is protected through an exact bordered-basis pivot identity rather than an empirical architecture census.

Primary files:

- `A114B2C2_COMPRESSED_NEGATIVE_PIVOT_BRANCH_THEOREM_20260913.md`
- `A114B2C2_COMPRESSED_BRANCH_ANALYTIC_CERTIFICATE_20260913.json`
- `A114B2C2_GITHUB_LOGICAL_AUDIT_20260913.json`
- `a114b2c2_compressed_branch_analytic_certificate.py`
- `a114b2c2_github_logical_audit.py`

## Longitudinal A80–A114 audit

The programme from A80 through the present state has been reviewed longitudinally for scope drift, circularity, witness-to-continuum promotion, compressed/lifted conflation, provenance and downstream reuse of refuted claims.

The audit records A108 as **REFUTED / SUPERSEDED**, finds no downstream A110–A114 dependency on its false one-sided rule, and identifies A110 as the independent finite-domain proof of the corrected bilateral adjacent-boundary mechanism.

Read:

- `A80_A114_LONGITUDINAL_AUDIT_20260913.md`
- `A80_A114_LONGITUDINAL_AUDIT_20260913.json`

The audit also records that it did not freshly rerun every expensive historical A80–A114 computation; it reviews committed theorem/result records, stored verification reports, exact certificates, dependency declarations and current promoted artifacts.

## Current frontier

Inside strict compressed `b+2` with `Phi<0`:

- `p0^C>0` -> `C` by C2;
- `p0^C<0` and `r_E(q0)>0` -> `E` by C1;
- `p0^C<0` and `r_E(q0)<0` -> **QI versus QA remains open**.

Current QI/QA pivot identities and reductions under investigation are not promoted here as theorems until an analytic certificate, independent exact controls and a logical-composition audit are committed.

## Claim boundary

A114 does **not** currently prove:

- the QI/QA split on the remaining strict negative-pivot branch;
- a generic strict classification on `p0^C=0` or `r_E(q0)=0`;
- the complete `b+2` architecture classification on `Phi=0`;
- any extension outside the declared source window;
- any physical interpretation.

## Field-note discipline

Failed stronger claims, implementation mistakes, historical waypoints and negative controls remain preserved intentionally. The authoritative current status is this README plus the dated theorem, certificate, logical-audit and longitudinal-audit files listed above.