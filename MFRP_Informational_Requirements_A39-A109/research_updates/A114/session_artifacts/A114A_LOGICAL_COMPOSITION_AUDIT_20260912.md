# A114-A — logical composition audit

## Verdict

**PASS.**

A114-A is logically promotable as a conditional analytic-tail theorem under the frozen contract:

\[
M\ge521,\quad 129/1000\le s\le133/1000,
\]

conditional on

\[
j=b+3
\]

being the strict compressed maximizer.

## Evidence checked

The audit requires all of the following to pass simultaneously:

1. the A113 compressed-objective dependency is `PASS`;
2. the A114-A theorem certificate is `PASS`;
3. all `141/141` theorem gates pass;
4. the theorem source contains no literal scientific `"gate": True` placeholders;
5. the standalone exact-rational cross-check passes;
6. the independent cross-check covers both tail parities;
7. the negative control is rejected;
8. the negative control fails structurally through `basic_p_92` and `rc_p_0`;
9. the dependency graph is acyclic.

Every item passed.

## Dependency DAG

The proof flow is:

\[
\text{A113 one-variation}
\to
\text{strict }b+3\text{ maximum}
\to
E_{b+2}>0
\to
Q>0.009.
\]

The quantitative `Q` bound plus the frozen tail bounds yields the endpoint primal signs. From there the proof splits:

- endpoint masses + adjacent compressed identities -> `p0` straddling;
- straddling + simplex exchange -> `r_P(0)>0`;
- endpoint system -> active dual positivity;
- endpoint system -> gamma slack positivity;
- endpoint system -> `r_Q(0),r_Q(2)>0`.

Then the extended-Chebyshev zero-count theorem closes the complete P and Q nonbasic reduced-cost families.

All branches meet only at the final strict-KKT conclusion. No conclusion is used as a premise of its own proof.

## Independent regression

The theorem proof does not use finite scans as premises.

A separate exact `Fraction` solver is used only as transcription/regression evidence. It reconstructs the original lifted LP and checks every unused atom at:

- historical A96: `M=125`;
- odd tail: `M=561`;
- even tail: `M=1282`.

All three pass their expected endpoint-released KKT systems. The two tail cases independently satisfy `E_(j-1)>0>E_j`.

The negative control

`M=521, s=129/1000, b=89, j=92=b+3`

is **not** a strict compressed maximum and is correctly rejected by the endpoint solver.

## Corrections incorporated before promotion

Promotion occurred only after correcting:

- the false claim that `j=b+3` alone suffices;
- the invalid whole-polynomial division of `r_P(M-1)` by `m`;
- the mixed-endpoint `RQ(2)` quadratic bound;
- the wrong use of `w_min` in a subtractive `RQ(2)` term;
- the wrong use of a lower `a` bound in the subtractive `p_j` term.

All corrected margins remain strictly positive.

## Claim boundary

A114-A proves one lifted architecture only:

\[
\boxed{
\text{strict }b+3\text{ compressed phase}
\Rightarrow
\text{endpoint-released strict global KKT lift}.
}
\]

It does not classify the `b+1` or `b+2` lifted phases and does not extend beyond the frozen source window.
