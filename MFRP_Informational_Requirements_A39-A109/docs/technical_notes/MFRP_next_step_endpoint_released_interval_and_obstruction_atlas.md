# A97 — Endpoint-Released Interval and Obstruction Atlas

**Programme:** Modal Field Research Programme  
**Audit:** A97  
**Status:** exact interval theorem at one support plus an exact rational-witness KKT atlas  
**Evidence class:** symbolic rational-function construction, exact rational interval arithmetic, and complete finite-LP KKT checks

## 1. Question

A95 found 83 rational phase-segment witnesses at which none of the previously declared natural lift families passed the complete KKT system. A96 solved the first case,

\[
M=125,\qquad s=\frac{33}{250},
\]

with the unrestricted basis

\[
P=\{23,24,125\},\qquad Q=\{1,62,63\},
\]

and active bands \(\alpha+\) and \(\beta-\), while \(\gamma\) remained inactive.

A97 asks two narrower questions:

1. Is this A96 basis valid only at one rational point, or on an exact open interval in \(s\)?
2. Does the same endpoint-released architecture
   \[
   P=\{j-1,j,M\},\qquad Q=\{1,h,h+1\},\qquad h=\lfloor M/2\rfloor,
   \]
   resolve the other A95 rational obstructions?

## 2. Exact M=125 interval

The symbolic branch contains 259 strict KKT conditions:

- 7 basic variables;
- 2 active-band multipliers;
- 246 nonbasic atom reduced costs;
- 4 inactive-band slacks.

Inside the declared search interval

\[
\frac{129}{1000}\le s\le\frac{133}{1000},
\]

the connected strict-KKT component containing \(33/250\) is bounded by two algebraic roots.

### Lower boundary

The lower boundary is the unique simple zero of the reduced cost of the nonbasic atom \(p_0\). Its exact isolating bracket is

\[
\frac{131966486281809654082390}{10^{24}}
<r_-<
\frac{131966486281809654082393}{10^{24}}.
\]

Presentation midpoint:

\[
r_-\approx0.1319664862818096540823915.
\]

The numerator changes sign from positive to negative, its derivative is strictly negative throughout the bracket, and its denominator is strictly negative. Hence the reduced cost changes from negative to positive as \(s\) crosses \(r_-\).

### Upper boundary

The upper boundary is the unique simple zero of the basic mass \(p_{23}\). Its exact isolating bracket is

\[
\frac{132121156974041079026925}{10^{24}}
<r_+<
\frac{132121156974041079026928}{10^{24}}.
\]

Presentation midpoint:

\[
r_+\approx0.1321211569740410790269265.
\]

The numerator changes from negative to positive, its derivative is strictly positive throughout the bracket, and its denominator is strictly negative. Therefore \(p_{23}\) changes from positive to negative at \(r_+\).

### Complete sign census

Every numerator and denominator other than the two boundary numerators was evaluated by exact rational interval Horner arithmetic on the entire rational hull from the lower isolating bracket to the upper isolating bracket.

\[
516/516
\]

nonboundary polynomial parts retained their required signs. The two boundary numerators were handled separately using their exact endpoint signs and derivative enclosures. Thus the maximal connected strict-KKT component containing the A96 probe, within the declared search interval, is

\[
\boxed{r_-<s<r_+}.
\]

The term “maximal” here is relative to this fixed active basis and the declared local search interval.

## 3. Atlas over the 83 A95 obstructions

At each of the 83 exact rational witnesses, A97 tested

\[
P=\{j-1,j,M\},\qquad Q=\{1,h,h+1\},
\]

with \(\alpha+\) and \(\beta-\) active and \(\gamma\) inactive. Every test included all atoms of the unrestricted finite LP.

The result is:

\[
\boxed{76\text{ strict global KKT passes}},
\]

\[
\boxed{7\text{ residual obstructions}}.
\]

The residual cases are exactly:

| \(M\) | \(s\) | \(j\) | first failure |
|---:|---:|---:|---|
| 396 | \(13/100\) | 70 | negative reduced cost of \(q_0\) |
| 443 | \(13/100\) | 78 | negative reduced cost of \(q_0\) |
| 449 | \(13/100\) | 79 | negative reduced cost of \(q_0\) |
| 455 | \(13/100\) | 80 | negative reduced cost of \(q_0\) |
| 484 | \(13/100\) | 85 | negative reduced cost of \(q_0\) |
| 490 | \(13/100\) | 86 | negative reduced cost of \(q_0\) |
| 496 | \(13/100\) | 87 | negative reduced cost of \(q_0\) |

Thus the endpoint release explains most, but not all, of the A95 failures.

## 4. Direct q0 replacement does not solve the residual cases

The negative reduced cost of \(q_0\) suggests that the active set must change. A97 tested the simplest possible repair:

\[
Q=\{0,h,h+1\}
\]

with the same \(P=\{j-1,j,M\}\) and the same two active bands.

It passes in

\[
\boxed{0/7}
\]

cases. The failures split into:

- three primal failures, at \(M=396,455,496\);
- four inactive \(\gamma-\) slack failures, at \(M=443,449,484,490\).

Therefore a negative \(q_0\) reduced cost is a reliable signal that the q1-based basis is no longer optimal, but it does not imply that a one-column substitution \(q_1\mapsto q_0\) is the correct new basis.

## 5. What A97 proves

1. The A96 basis persists on a nonzero exact algebraic interval in \(s\).
2. Its lower boundary is a \(p_0\) reduced-cost entry event.
3. Its upper boundary is a \(p_{23}\) basic-mass exit event.
4. The endpoint-released architecture resolves 76 of the 83 exact A95 obstruction witnesses.
5. Seven lower-s cases require a different active-set architecture involving the \(q_0\) direction.
6. A direct replacement of \(q_1\) by \(q_0\) is insufficient in all seven cases.

## 6. What A97 does not prove

A97 does not establish:

- interval persistence at the other 82 witnesses;
- the true unrestricted optimum at any of the seven residual cases;
- an all-\(M\) support theorem;
- a universal rule for q-support changes;
- any physical interpretation of \(P,Q,q,\lambda\), contacts, or active bands;
- spacetime, matter, energy, or a pre-temporal ontology.

## 7. Next rigorous target

The first unresolved case is

\[
M=396,\qquad s=\frac{13}{100},\qquad j=70.
\]

A98 should solve the unrestricted full LP at this point without imposing either \(Q=\{1,h,h+1\}\) or \(Q=\{0,h,h+1\}\). The discovery stage may be numerical, but the final claim must be reconstructed as a complete exact rational primal-dual KKT certificate.
