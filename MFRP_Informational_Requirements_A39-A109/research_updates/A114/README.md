# A114 — lifted active-set selection after compressed one-variation

A113 tells us **where the compressed maximum can live**. A114 asks the next question:

> Once the compressed maximizer is known, which lifted LP architecture actually satisfies the full KKT system?

This is deliberately separated from A113. A compressed maximum and a valid lifted basis are not the same statement.

## Frozen analytic-tail contract

The current A114 tail results use

`M>=521`, `129/1000<=s<=133/1000`,

with the frozen beta, gamma, target and normalized-tolerance conventions inherited from A112/A113.

Write

`b=ceil(M*c(s))`, `c(s)=log(2)/(-2 log(s))`.

## A114-A — strict compressed `b+3` phase

**PROVED.**

If the strict compressed maximizer is `j=b+3`, then the unique strict lifted optimum is the endpoint-released architecture

`P={j-1,j,M}`,

`Q={1,h,h+1}`,

with `alpha+` and `beta-` active and gamma inactive.

Read in this order:

1. `session_artifacts/A114A_ANALYTIC_TAIL_ENDPOINT_RELEASED_LIFT_THEOREM_20260912.md`
2. `session_artifacts/A114A_LOGICAL_COMPOSITION_AUDIT_20260912.md`
3. `A114A_CORRECTIONS_AND_DEAD_ENDS_20260912.md`
4. `archives/A114A_FULL_REPRODUCIBILITY_PACKAGE_20260912.zip`

The stronger arithmetic statement `j=b+3 => endpoint-released` is false without strict compressed maximality. The exact negative control `M=521, s=129/1000` is retained in A114-A.

## A114-B1 — strict compressed `b+1` phase

**PROVED / CLOSED under the same frozen tail contract.**

Define

`Phi(M,s)=F_(b+2)^up(s)`.

If the strict compressed maximizer is `b+1`, then:

- `Phi<0`: the unique strict global lift is gamma-plus at contact `b+1`,
  `P={0,b+1,b+2,M}`, `Q={1,h,h+1}`;
- `Phi>0`: the unique strict global lift is gamma-plus at contact `b+2`,
  `P={0,b+2,b+3,M}`, `Q={1,h,h+1}`;
- `Phi=0`: the two neighboring bases meet at the same non-strict degenerate global optimum. Strict complementarity and uniqueness are not claimed on this pivot set.

The determinant orientation needed to use the Cramer signs is proved independently of primal positivity:

`D_G = det(C) A(s) > 0`,

using the A110 generalized-Vandermonde sign `det(C)<0` and the A112-G branch-regularity sign `A(s)<0`.

A114-B1 also preserves the exact counterexample to the false same-contact rule:

`M=561, s=13277/100000, b=97` has strict compressed maximizer `98=b+1`, but the strict lifted gamma-plus contact is `99=b+2`.

Read in this order:

1. `session_artifacts/A114B1_ANALYTIC_TAIL_BPLUS1_GAMMA_PIVOT_THEOREM_20260912.md`
2. `session_artifacts/A114B1_LOGICAL_COMPOSITION_AUDIT_20260912.md`
3. `A114B1_CORRECTIONS_AND_DEAD_ENDS_20260912.md`
4. `session_artifacts/a114b1_gamma_pivot_orientation_certificate.py`
5. `session_artifacts/A114B1_GAMMA_PIVOT_ORIENTATION_CERTIFICATE_20260912.json`
6. `session_artifacts/a114b1_independent_exact_crosscheck.py`
7. `session_artifacts/A114B1_INDEPENDENT_EXACT_CROSSCHECK_20260912.json`

`MANIFEST_A114B1_20260912.sha256` hashes the promoted A114-B1 text and executable artifacts.

## A114-B2-W1 — first exact strict-`b+2` tail witness

**PROVED POINTWISE; A114-B2 REMAINS OPEN.**

At the exact first-tail point

`M=521, s=129/1000`, `h=260`, `b=89`,

the compressed objective has strict maximizer

`j=91=b+2`.

The unique strict global lifted optimum is not gamma-plus. It is

`P={90,91,521}`,

`Q={0,1,260,261}`,

with `alpha+`, `beta-`, `gamma-` active.

The exact certificate checks all

`1051 = 2M+9`

strict KKT conditions. A standalone `fractions.Fraction` implementation independently reproduces the full pass.

The two natural adjacent gamma-plus lifts fail for different reasons:

- contact `b+1`: `active_dual_gamma_+1<0`;
- contact `b+2`: `basic_p_92<0`.

This proves that non-gamma-plus architecture does not disappear merely because the analytic tail begins at `M>=521`.

A discovery correction is recorded explicitly: the first exploratory M=521 simplex run used the wrong even-parity epsilon scale `1875` and is invalid. The corrected discovery rerun uses the required odd-parity scale `2500`, recovers the same candidate, and is retained only as provenance. The theorem itself depends only on the exact certificates.

Read in this order:

1. `session_artifacts/A114B2_W1_M521_Q0Q1_GAMMA_MINUS_POINTWISE_THEOREM_20260912.md`
2. `session_artifacts/A114B2_W1_LOGICAL_AUDIT_20260912.md`
3. `A114B2_W1_CORRECTIONS_AND_SCOPE_20260912.md`
4. `session_artifacts/a114b2_w1_m521_exact_kkt_certificate.py`
5. `session_artifacts/A114B2_W1_M521_EXACT_KKT_CERTIFICATE_20260912.json`
6. `session_artifacts/a114b2_w1_m521_fraction_crosscheck.py`
7. `session_artifacts/A114B2_W1_M521_FRACTION_CROSSCHECK_20260912.json`
8. `session_artifacts/a114b2_w1_corrected_discovery.py`
9. `session_artifacts/A114B2_W1_CORRECTED_DISCOVERY_20260912.json`

`MANIFEST_A114B2_W1_20260912.sha256` hashes the promoted B2-W1 notes and executable artifacts.

## Current frontier — A114-B2

The strict compressed `b+2` phase remains **OPEN** as an all-tail classification problem.

B2-W1 proves one exact q0/q1 gamma-minus tail point, but it does not justify the all-`M` rule

`Phi<0 => q0/q1 gamma-minus`.

The finite atlas contains multiple architectures in the `b+2` region. The next rigorous target is to derive an analytic partition of the strict `b+2` phase without assuming gamma-plus, two-band, q0/q1, gamma-minus or endpoint-released in advance.

## Claim boundary

A114 currently proves:

- the strict `b+3` phase (A114-A);
- the strict `b+1` phase (A114-B1);
- the exact B2-W1 point `M=521, s=129/1000`.

It does **not** yet prove:

- the lifted architecture classification of the complete strict compressed `b+2` phase;
- that `F_(b+2)^up` is a universal classifier outside B1;
- that `Phi<0` selects q0/q1 gamma-minus for every tail point;
- any extension outside the declared source window;
- any physical interpretation.

## Field-note discipline

This folder keeps failed stronger claims and implementation mistakes on purpose. A future reader should be able to tell:

- what was observed;
- what was guessed;
- what was refuted;
- what was corrected;
- what is actually proved;
- what remains open.
