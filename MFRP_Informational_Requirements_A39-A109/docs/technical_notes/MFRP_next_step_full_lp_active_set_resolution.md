# A96 — Exact unrestricted full-LP active-set resolution at the first A95 obstruction

## Question

A95 established an exact obstruction at

\[
M=125,\qquad s=\frac{33}{250},\qquad \mathbb E[X]=\frac{125}{2}.
\]

At that point, none of the 370 previously declared F2/F3 support candidates satisfies the complete strict KKT system. The unresolved question was not whether the LP had an optimum—the finite problem is bounded—but which active support the unrestricted LP actually selects.

A96 removes the old support template. A 180-digit, two-phase revised-simplex calculation was used only to discover a candidate basis. The candidate was then reconstructed independently with exact rational arithmetic and checked against every atom column of the complete finite LP.

## Exact active set

The unique strict optimum is

\[
P:\ \{23,24,125\},
\qquad
Q:\ \{1,62,63\}.
\]

The active observation bands are

\[
\alpha+,
\qquad
\beta-,
\]

while both gamma inequalities are strictly inactive. The opposite alpha and beta inequalities are also strictly inactive.

This is an endpoint-released two-band basis:

\[
P=\{j-1,j,M\},\qquad j=24,
\]

rather than either old form

\[
\{0,j,M\}
\quad\text{or}\quad
\{0,j,j+1,M\}.
\]

The structural correction is therefore specific: the old architecture failed because it forced the endpoint zero into the P support.

## Exact KKT certificate

The exact basis contains seven positive Charnes–Cooper variables:

- three P atoms;
- three Q atoms;
- the scale variable \(t\).

The unrestricted certificate checks:

- 7 strictly positive basic variables;
- 2 strictly positive active-band multipliers;
- 246 strictly positive nonbasic atom reduced costs;
- 4 strictly positive inactive-band slacks.

Thus the certificate contains

\[
7+2+246+4=\boxed{259}
\]

strict inequalities, in addition to exact primal feasibility and exact primal–dual objective equality.

The smallest reduced cost occurs at the unused P atom \(x=124\):

\[
r_{p,124}
=4.9897064981022456077\ldots\times10^{-10}>0.
\]

The smallest inactive slack is the gamma-minus slack:

\[
1.1623369816648020038\ldots\times10^{-4}>0.
\]

Therefore the basis is not merely feasible. It is the unique global basic optimum of the unrestricted declared LP.

## Probability laws

After dividing by \(t\), the probability masses are approximately

\[
P(23)=0.00293229242464617858,
\]

\[
P(24)=0.615850556165208810,
\]

\[
P(125)=0.381217151410145012,
\]

and

\[
Q(1)=2.47081017680963154\times10^{-21},
\]

\[
Q(62)=0.499999999999999999847,
\]

\[
Q(63)=0.500000000000000000151.
\]

The tiny but exactly positive Q atom at 1 is essential to the strict basis. It must not be rounded to zero in a proof.

The exact transform ratio is

\[
\rho
=226143135079.406524967073474077638\ldots.
\]

The large ratio is contract-relative: the Q law lies extremely close to the mean-constrained minimum of the target transform. No physical interpretation is attached to this scale.

## What A96 proves

A96 proves, at the declared rational point:

1. the complete unrestricted finite LP has a unique strict global basic optimum;
2. its P support is \(\{23,24,125\}\);
3. its Q support is \(\{1,62,63\}\);
4. alpha-plus and beta-minus are active;
5. gamma is inactive on both sides;
6. the first A95 obstruction is an obstruction to the old support architecture, not to the LP itself.

## What A96 does not prove

A96 does not establish:

- persistence of this basis on an interval in \(s\);
- the same endpoint release at the other 82 A95 obstruction witnesses;
- an all-M active-set theorem;
- a physical meaning for the support points, bands, or transform ratio;
- spacetime, matter, energy, or a pre-temporal ontology.

## Next exact target

A97 should treat the newly discovered family

\[
P=\{j-1,j,M\},
\qquad
Q=\{1,h,h+1\},
\qquad
\gamma\text{ inactive},
\]

as a candidate structural class. The first task is to isolate the maximal rational interval around \(s=33/250\) on which all 259 KKT conditions remain strict. The second is to test the same endpoint-released family against the remaining A95 obstruction witnesses without assuming that it must succeed.
