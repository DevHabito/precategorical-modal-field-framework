# A114-B2-C — residual-chain exact finite evidence

## Status

**EXACT FINITE EVIDENCE / NOT AN ALL-TAIL THEOREM.**

This note records the current rigorous evidence for the residual architecture chain inside the frozen A114 tail contract

\[
M\ge521,\qquad 129/1000\le s\le133/1000,
\]

under the premise that the compressed objective has strict maximizer

\[
j=b+2,
\]

and

\[
\Phi=F_j^{up}<0.
\]

A114-B2-B has already excluded the pure central-Q gamma-minus architecture on this region. The remaining observed strict architectures are denoted

- `C`: compressed two-band, \(P=\{0,j,M\}, Q=\{1,h,h+1\}\), gamma inactive;
- `E`: endpoint-released, \(P=\{j-1,j,M\}, Q=\{1,h,h+1\}\), gamma inactive;
- `QI`: q0/q1 co-entry, \(P=\{j,M\}, Q=\{0,1,h,h+1\}\), gamma inactive;
- `QA`: q0/q1 co-entry with gamma-minus active, \(P=\{j-1,j,M\}, Q=\{0,1,h,h+1\}\).

## Candidate sign tree

The exact finite evidence is consistent with the hierarchy

\[
\boxed{
\begin{array}{rcl}
p_0^C>0 &\Rightarrow& C,\\
p_0^C<0,\ r_E(q_0)>0 &\Rightarrow& E,\\
p_0^C<0,\ r_E(q_0)<0,\ S_{\gamma-}^{QI}>0 &\Rightarrow& QI,\\
p_0^C<0,\ r_E(q_0)<0,\ S_{\gamma-}^{QI}<0 &\Rightarrow& QA.
\end{array}}
\]

This implication tree is **not** promoted here as an all-M theorem.

## Exact pivot census

`a114b2c_exact_pivot_census.py` uses `fractions.Fraction` only for all sign decisions. It reconstructs the declared LP bases and verifies the premise exactly at 20 adversarial support sizes spanning \(521\) through \(1000\), across nine rational probes in the source window.

There are 28 exact records satisfying strict `b+2` and \(\Phi<0\). Their predicted residual classes are

\[
C=5,\qquad E=17,\qquad QI=2,\qquad QA=4.
\]

Across all 28 records, six independent sign relations have zero failures:

\[
\operatorname{sgn}p_{j-1}^{E}=-\operatorname{sgn}p_0^C,
\]

\[
\operatorname{sgn}\lambda_{\gamma-}^{QA}=-\operatorname{sgn}r_E(q_0),
\]

\[
\operatorname{sgn}p_{j-1}^{QA}=-\operatorname{sgn}S_{\gamma-}^{QI},
\]

and, whenever \(p_0^C<0\),

\[
p_{j-1}^{E}>0,\qquad q_0^{QI}>0,
\]

while both gamma slacks of the endpoint-released basis are positive.

These are exact finite identities/sign observations, not a proof that the proportionality factors have the required sign for every tail point.

## Twelve complete exact KKT controls

`a114b2c_12_point_full_kkt_certificate.py` independently scans every unused atom and every inactive band slack at twelve points selected *after* exact premise reconstruction. There are three controls for each residual architecture:

| Class | Exact controls |
|---|---|
| `C` | \((538,53/400)\), \((973,13/100)\), \((989,33/250)\) |
| `E` | \((522,263/2000)\), \((800,261/2000)\), \((1000,261/2000)\) |
| `QI` | \((555,13/100)\), \((908,13/100)\), \((967,13/100)\) |
| `QA` | \((521,129/1000)\), \((970,129/1000)\), \((1000,129/1000)\) |

Every control satisfies, exactly:

1. `j=b+2` is the strict compressed winner among the three A113 tail candidates;
2. \(\Phi<0\), with the sign read through the gamma-plus Cramer mass using the already-proved \(D_G>0\) orientation;
3. the sign tree selects the declared class;
4. all \(2M+9\) strict full-LP KKT conditions are positive;
5. all basis equations hold exactly;
6. primal and dual objectives agree exactly.

The largest controls have

\[
2(1000)+9=2009
\]

strict KKT conditions, all positive.

## Correction to an earlier exploratory statement

An earlier exploratory summary claimed a different set of twelve large-support representatives all passed. Independent exact replay rejected that statement: several inherited points had \(\Phi>0\) and therefore lay outside the declared negative-pivot region, while one negative-pivot point belonged to `C` rather than the previously assigned `QI` class.

Those inherited labels are discarded. The twelve controls listed above were re-selected from exact premise checks and then independently passed the complete KKT scan.

## Structural interpretation

The three repeated sign reversals are what one expects from neighboring simplex bases and bordered linear systems. In particular:

- `C` and `E` exchange \(p_0\) with \(p_{j-1}\);
- `E` and `QA` are connected by the q0/gamma-minus bordered direction;
- `QI` and `QA` are connected by the lower-adjacent-P/gamma-minus bordered direction.

This suggests that the residual classification may reduce to signs of a small sequence of Schur complements. That reduction is the next analytic target.

## Claim boundary

This package does **not** prove:

- the sign tree for every real \(s\) and every \(M\ge521\);
- positivity of every proportionality/Schur factor all-tail;
- that no other KKT condition cuts a candidate edge first outside the tested exact controls;
- classification of \(\Phi=0\);
- any physical interpretation.

A114-B2 remains open beyond B2-A and B2-B.
