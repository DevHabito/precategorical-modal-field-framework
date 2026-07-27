# A100 — Exact Unrestricted Full-LP Resolution at the First A99 Residual

## Status

Exact rational theorem at one declared finite contract, following a discovery-only 180-digit revised-simplex solve.

## Contract

The audit fixes

\[
M=443,\qquad \mathbb E[X]=\frac{443}{2},\qquad s=\frac{13}{100},
\]

with target, beta, and gamma bases

\[
t=\frac12,\qquad \beta=\frac18,\qquad \gamma=\frac1{16},
\]

and normalized tolerance

\[
\varepsilon=\frac{1}{2500\,2^{221}}.
\]

This is the first of the four exact residual obstructions preserved by A99. The failed A99 architecture was

\[
P=\{78,443\},\qquad Q=\{0,1,221,222\},
\]

with alpha-plus and beta-minus active and gamma inactive. Its exact failures were negative `q1` mass and negative gamma-minus slack.

## Unrestricted discovery

No support cardinality, support location, adjacency, or band-activity pattern was imposed. A two-phase revised-simplex solve at 180 decimal digits selected the candidate

\[
P=\{77,78,443\},
\qquad
Q=\{0,1,221,222\},
\]

with

\[
\alpha+,
\qquad
\beta-,
\qquad
\gamma-
\]

active.

The high-precision computation is discovery only. It is not used as the proof.

## Exact reconstruction

The candidate gives an exact eight-by-eight Charnes–Cooper basis. A100 reconstructs it with rational arithmetic and checks:

- eight strictly positive basic variables;
- three strictly positive active-band multipliers;
- all 881 reduced costs of unused P/Q atoms;
- the three opposite-band slacks;
- all exact primal equations;
- exact equality of primal and dual objective values.

The resulting strict KKT certificate has

\[
8+3+881+3=895
\]

strict conditions.

Every condition is positive. Therefore the selected basis is the unique global optimum of the declared finite LP.

## Selected probability laws

After undoing Charnes–Cooper scaling, the P law is supported on 77, 78, and 443. Numerically,

\[
P(77)\approx0.00614897604356513,
\]

\[
P(78)\approx0.600683492515220,
\]

\[
P(443)\approx0.393167531441215.
\]

The Q law is supported on 0, 1, 221, and 222. The endpoint masses are exactly positive but extremely small, while the central pair carries essentially one half each:

\[
Q(0)\approx2.13849\times10^{-70},
\]

\[
Q(1)\approx3.76644\times10^{-70},
\]

\[
Q(221)\approx Q(222)\approx\frac12.
\]

These tiny endpoint masses must not be rounded to zero in an exact active-set claim.

## Structural result

A100 identifies two simultaneous corrections to the failed A99 architecture:

1. the lower adjacent P contact returns, changing
   \[
   \{78,443\}\longrightarrow\{77,78,443\};
   \]
2. gamma-minus changes from a violated inactive inequality to an active constraint.

The q0/q1 plus central-Q topology survives:

\[
Q=\{0,1,h,h+1\},\qquad h=221.
\]

Thus the obstruction is not repaired by replacing q1, deleting q0, or moving the central pair. It is repaired by jointly changing P support and band activity.

## What A100 proves

At the exact declared rational contract, A100 proves:

- the unrestricted finite LP has a unique global optimum;
- its active set is exactly
  \[
  P=\{77,78,443\},\quad Q=\{0,1,221,222\};
  \]
- alpha-plus, beta-minus, and gamma-minus are active;
- all unused atom directions and opposite-band directions are strictly excluded.

## What A100 does not prove

A100 does not establish:

- persistence of this basis on an interval of `s`;
- reuse of this architecture at the residuals `M=449,484,490`;
- a universal support-transition rule;
- a physical meaning for the atoms, channels, or active bands;
- spacetime, matter, calibrated duration, or a pre-temporal ontology.

The result remains a contract-relative theorem in finite parametric linear programming.

## Next rigorous target

A101 should construct all 895 KKT conditions symbolically in `s`, isolate the maximal strict component containing `13/100`, and test the new architecture at the remaining A99 residuals. The test must permit the architecture to fail and must not assume gamma-minus remains active outside the certified component.
