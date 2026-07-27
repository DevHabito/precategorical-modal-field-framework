# A101 — Exact gamma-active interval theorem and final residual closure

## Status

**Exact symbolic interval theorem at one support, plus exact rational KKT closure of the final three declared residual witnesses.**

A100 resolved the first of the four A99 residuals at

\[
M=443,\qquad s=\frac{13}{100},\qquad j=78
\]

with

\[
P=\{77,78,443\},
\]

\[
Q=\{0,1,221,222\},
\]

and active bands \(\alpha+\), \(\beta-\), and \(\gamma-\).

A101 asks two falsifiable questions:

1. Does this basis persist on a nonzero interval in \(s\), or was A100 an isolated rational point?
2. Does the same architecture resolve the final three witnesses \(M=449,484,490\), or does another active-set change occur?

No contract parameter is altered after seeing the result.

## Exact rank-one symbolic construction

The eight basic variables are

\[
p_{77},\ p_{78},\ p_{443},\ q_0,\ q_1,\ q_{221},\ q_{222},\ t.
\]

Only the active \(\alpha+\) row depends on the probe \(s\). Therefore the basis matrix is an exact rank-one row update of its value at \(s_0=13/100\). The Sherman–Morrison identity gives every basic and dual variable over one common sparse denominator

\[
d(s).
\]

The denominator has seven nonzero terms. Each of the complete KKT conditions can be written as

\[
\frac{N_i(s)}{d(s)}.
\]

The full system contains

\[
\boxed{895\text{ KKT conditions}}:
\]

- 8 basic variables;
- 3 active-band multipliers;
- 881 reduced costs for every unused \(P\)- and \(Q\)-atom;
- 3 opposite-band slacks.

The common denominator is strictly positive on the complete certified boundary hull.

## Exact strict component at \(M=443\)

Inside

\[
\frac{129}{1000}\le s\le\frac{133}{1000},
\]

the maximal connected strict-KKT component containing \(13/100\) is bounded by two simple algebraic roots.

### Lower boundary

The lower boundary is where the active \(\gamma-\) multiplier reaches zero:

\[
y_{\gamma-}=0.
\]

Its isolating interval is

\[
\frac{129950386680648955573451}{10^{24}}
<r_-<
\frac{129950386680648955573452}{10^{24}}.
\]

Numerically,

\[
r_-\approx0.1299503866806489555734515.
\]

The numerator changes from negative to positive, and its derivative is strictly positive on the entire boundary hull. Thus the root is unique and simple.

### Upper boundary

The upper boundary is where the basic mass \(p_{77}\) reaches zero:

\[
p_{77}=0.
\]

Its isolating interval is

\[
\frac{130103853082902466513379}{10^{24}}
<r_+<
\frac{130103853082902466513380}{10^{24}}.
\]

Numerically,

\[
r_+\approx0.1301038530829024665133795.
\]

The numerator changes from positive to negative, and its derivative is strictly negative on the entire boundary hull. This root is also unique and simple.

Therefore the certified strict component is

\[
\boxed{r_-<s<r_+}.
\]

Its midpoint width is approximately

\[
1.53466402253510939928\times10^{-4}.
\]

Every other

\[
\boxed{893\text{ condition numerators}}
\]

is strictly positive on the full boundary hull under exact integer interval arithmetic. There are no unresolved interval signs.

Immediately below \(r_-\), the active \(\gamma-\) multiplier is negative. Immediately above \(r_+\), the basic mass \(p_{77}\) is negative. Hence the connected strict component containing \(13/100\) cannot be extended through either root.

## Final three residual witnesses

The same architecture

\[
P=\{j-1,j,M\},\qquad Q=\{0,1,h,h+1\},
\]

with \(\alpha+\), \(\beta-\), and \(\gamma-\) active was tested at the three witnesses left after A100.

| \(M\) | \(j\) | \(P\) support | \(Q\) support | KKT conditions | Result |
|---:|---:|---|---|---:|---|
| 449 | 79 | \(\{78,79,449\}\) | \(\{0,1,224,225\}\) | 907 | **strict global pass** |
| 484 | 85 | \(\{84,85,484\}\) | \(\{0,1,242,243\}\) | 977 | **strict global pass** |
| 490 | 86 | \(\{85,86,490\}\) | \(\{0,1,245,246\}\) | 989 | **strict global pass** |

Across the three points,

\[
\boxed{2873/2873\text{ KKT conditions are strictly positive}}.
\]

All primal equations close exactly and every primal objective is literally equal to its dual objective.

The smallest conditions are the reduced costs of the atoms immediately below \(M\):

\[
r_{p_{448}}\approx3.80324\times10^{-27},
\]

\[
r_{p_{483}}\approx5.51093\times10^{-29},
\]

\[
r_{p_{489}}\approx2.72138\times10^{-29}.
\]

They are very small but exactly positive; no tolerance decision is used.

## Closure of the A95 rational-witness obstruction list

A95 found 83 rational phases without a strict lift in the original natural families. The later exact results now account for all of them:

| Architecture | Resolved witnesses |
|---|---:|
| endpoint-released \(P=\{j-1,j,M\}, Q=\{1,h,h+1\}\), \(\gamma\) inactive | 76 |
| \(q_0/q_1\) co-entry, \(P=\{j,M\}\), \(\gamma\) inactive | 3 |
| \(q_0/q_1\) co-entry, lower adjacent \(P\)-pair restored, \(\gamma-\) active | 4 |
| **Total** | **83** |

Thus every one of the 83 selected rational obstruction witnesses now has a strict exact full-LP KKT certificate.

This is a closure of the **pointwise rational-witness atlas**, not a continuum theorem over every phase cell.

## Structural conclusion

The residual sequence did not require a new free parameter. It required two genuine active-set changes:

1. entry of \(q_0\) alongside \(q_1\);
2. for the final four witnesses, restoration of the lower adjacent \(P\)-contact and activation of \(\gamma-\).

The same gamma-active architecture then resolves all four members of its residual class and persists on a certified open interval at \(M=443\).

## What A101 does not prove

A101 does not establish:

1. interval persistence at \(M=449,484,490\);
2. continuous lifted-KKT certification over all 858 A92 cells;
3. that the three observed architectures exhaust every contract outside the tested range;
4. an all-\(M\) support theorem;
5. any physical, spatial, temporal, material, or ontological interpretation.

## Next rigorous target

The pointwise obstruction hunt is now closed. The next scientifically useful step should be consolidation rather than another isolated active-set search.

A102 should construct a **complete exact rational-witness lift atlas** over all 1,063 A95 phase witnesses, merging:

- the 980 original natural lifts;
- the 76 endpoint-released lifts;
- the 3 q0/q1 gamma-inactive lifts;
- the 4 gamma-active lifts.

The merged audit should verify one strict certified optimum per witness, no unresolved witness, no duplicated phase key, exact provenance to the source audit, and a minimal architecture classification. It must preserve the distinction between pointwise closure and continuum phase certification.
