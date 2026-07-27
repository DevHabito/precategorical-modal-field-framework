# A99 — Exact q0/q1 interval theorem and remaining-residual atlas

## Status

**Exact symbolic interval theorem at one support, plus an exact rational-witness KKT atlas over six declared residuals.**

A98 resolved the first residual obstruction left by A97 at

\[
M=396,\qquad s=\frac{13}{100},\qquad j=70
\]

with the unrestricted active set

\[
P=\{70,396\},
\]

\[
Q=\{0,1,198,199\},
\]

active bands \(\alpha+\) and \(\beta-\), and both gamma orientations inactive.

A99 tests whether this correction is more than a one-point solution. It does so in two separate stages:

1. a symbolic strict-KKT interval certificate in the variable \(s\) at \(M=396\);
2. an exact rational test of the same support architecture at the six remaining A97 residual witnesses.

No support is altered after a failure in order to force a pass.

## Symbolic construction

The seven-variable Charnes–Cooper basis is written with variable order

\[
p_{70},\ p_{396},\ q_0,\ q_1,\ q_{198},\ q_{199},\ t.
\]

All basic variables and dual variables are represented over one common determinant polynomial \(D(s)\). Every KKT condition is therefore written as

\[
\frac{N_i(s)}{D(s)}.
\]

The determinant has six nonzero terms and remains strictly negative on the complete certified boundary hull. Consequently, the sign of each KKT condition is the opposite of the sign of its numerator on that hull.

The complete symbolic system contains

\[
\boxed{801\text{ KKT conditions}}.
\]

These consist of:

- 7 basic variables;
- 2 active-band multipliers;
- 788 reduced costs for every unused P/Q atom;
- 4 inactive-band slacks.

## Exact strict component at \(M=396\)

Inside

\[
\frac{129}{1000}\le s\le\frac{133}{1000},
\]

the maximal connected strict-KKT component containing \(13/100\) is bounded by two simple algebraic roots.

### Lower boundary

The lower boundary is the zero of the inactive gamma-minus slack numerator:

\[
\operatorname{num}(\mathrm{slack}_{\gamma-})=0.
\]

Its exact isolating interval is

\[
\frac{129987460460605135017979}{10^{24}}
<r_-<
\frac{129987460460605135017980}{10^{24}}.
\]

Numerically,

\[
r_-\approx0.1299874604606051350179795.
\]

The numerator changes from positive to negative, and its derivative is strictly negative on the complete isolating interval.

### Upper boundary

The upper boundary is the zero of the basic \(q_0\) numerator:

\[
\operatorname{num}(q_0)=0.
\]

Its exact isolating interval is

\[
\frac{130017128515377642396099}{10^{24}}
<r_+<
\frac{130017128515377642396100}{10^{24}}.
\]

Numerically,

\[
r_+\approx0.1300171285153776423960995.
\]

The numerator changes from negative to positive, and its derivative is strictly positive on the isolating interval.

Therefore the certified component is

\[
\boxed{r_-<s<r_+}.
\]

Its width is approximately

\[
2.96680547725\times10^{-5}.
\]

Because the common denominator is negative, both boundary numerators are negative throughout the closed core between the root brackets, so the associated KKT conditions are positive there. Immediately outside the respective boundaries, the gamma-minus slack or the \(q_0\) mass becomes negative. Thus the component cannot be extended through either root.

All other

\[
\boxed{799\text{ condition numerators}}
\]

are sign-stable on the full boundary hull under exact rational interval evaluation. No nonboundary sign failure occurs.

## Remaining six A97 residual witnesses

The same architecture

\[
P=\{j,M\},\qquad Q=\{0,1,h,h+1\}
\]

was tested at the six A97 residuals not solved by A98, always at \(s=13/100\).

| \(M\) | \(j\) | Result | Exact obstruction when failing |
|---:|---:|---|---|
| 443 | 78 | fail | \(q_1<0\), gamma-minus slack \(<0\) |
| 449 | 79 | fail | \(q_1<0\), gamma-minus slack \(<0\) |
| 455 | 80 | **strict global KKT pass** | — |
| 484 | 85 | fail | \(q_1<0\), \(q_{243}<0\), gamma-minus slack \(<0\) |
| 490 | 86 | fail | \(q_1<0\), \(q_{246}<0\), gamma-minus slack \(<0\) |
| 496 | 87 | **strict global KKT pass** | — |

Thus the A98 support correction resolves exactly

\[
\boxed{2/6}
\]

of the remaining rational witnesses.

At \(M=455\) and \(M=496\), every basic variable, active multiplier, unused-atom reduced cost, and inactive slack is strictly positive, and the primal and dual objectives are exactly equal.

At the other four supports, the failure is not a numerical ambiguity. It is exact primal/slack infeasibility. In particular, the q0/q1 co-entry architecture is reusable but not universal.

## Structural conclusion

A99 establishes two distinct facts:

1. the A98 basis persists on a genuine algebraic interval and was not a single isolated rational coincidence;
2. the same support topology succeeds at two later residuals but fails at four others through a new pattern of disappearing Q masses and gamma-minus infeasibility.

The first unresolved point is now

\[
\boxed{M=443,\qquad s=\frac{13}{100},\qquad j=78}.
\]

The architecture already has \(q_0\) and \(q_1\), yet \(q_1\) becomes negative. A new unrestricted active-set discovery is therefore required; merely repeating the A98 support pattern would be ad hoc.

## What A99 does not prove

A99 does not establish:

1. interval persistence at \(M=455\) or \(M=496\);
2. a solution of the four residual obstructions;
3. a universal q0/q1 co-entry law;
4. an all-support theorem;
5. any physical, spatial, temporal, material, or ontological interpretation.

## Next rigorous target

A100 should solve the unrestricted finite LP at

\[
M=443,\qquad s=\frac{13}{100}
\]

without preassigning:

- the number of P or Q atoms;
- inclusion or exclusion of \(q_0\) or \(q_1\);
- the central Q pair;
- adjacency of the P contacts;
- gamma activity.

Any numerically discovered basis must again be rebuilt as an exact rational primal-dual certificate before promotion.
