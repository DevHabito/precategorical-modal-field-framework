# A90 — Exact Pre-Threshold All-k One-Variation Audit

## Status

Exact finite theorem at nine declared rational probes. The result uses integer arithmetic after an exact denominator-clearing transformation. It is not a continuum theorem in the probe parameter and not an all-support theorem.

## Motivation

A89 proves the local secant inequality

\[
S_{M,b}(s)=E_{M,b}(s)-E_{M,b+1}(s)>0,
\qquad b=\lceil M c(s)\rceil,
\]

for every real

\[
129/1000\le s\le133/1000
\]

and every integer \(M\ge521\). That theorem controls one local comparison needed by the offset classifier. It does not determine the complete sign sequence

\[
k\longmapsto E_{M,k}(s)
\]

for every admissible contact.

A90 studies the complementary finite range

\[
10\le M\le520
\]

at nine rational probes

\[
s_j=\frac{258+j}{2000},\qquad j=0,\ldots,8.
\]

The first goal is to test the complete all-\(k\) one-variation law below the A89 analytic threshold. The second is to test whether the three-contact strip proved by A86 on \(M\le300\) survives beyond its declared domain.

## Exact integer evaluator

A84 writes the adjacent factor as a ten-term confluent exponential polynomial in \(k\):

\[
E_{M,k}(s)=\sum_i c_i r_i^k
+k\sum_j d_j q_j^k,
\]

where all coefficients and nodes are rational under the declared probe contract.

Let

\[
L=\operatorname{lcm}\{\operatorname{den}(c_i),\operatorname{den}(d_j)\},
\]

and

\[
D=\operatorname{lcm}\{\operatorname{den}(r_i),\operatorname{den}(q_j)\}.
\]

Then

\[
L D^k E_{M,k}(s)
\]

is an integer sum with integer bases \(D r_i\) and \(D q_j\). Since \(L D^k>0\), the integer sum has exactly the sign of the original rational factor. No floating-point sign decision is used.

The transformation was checked independently in 45 regression cells against direct rational evaluation of the A84 formula.

## Finite all-contact result

A90 evaluates every admissible adjacent factor for

\[
10\le M\le520
\]

at all nine probes. The catalogue contains

\[
511\times9=4599
\]

complete contact sequences and

\[
594423
\]

exact adjacent-factor evaluations.

Every sequence is strictly of the form

\[
+,+,\ldots,+,-,\ldots,-.
\]

There are no zero factors, and every sequence has exactly one positive-to-negative transition. Therefore every declared \((M,s_j)\) cell has one strict compressed-objective maximizing contact.

This is a complete all-contact result on the finite probe grid. It is stronger than checking only the transition neighborhood, but it remains pointwise in \(s\).

## Contact-strip result and counterexample

Define

\[
b=\lceil M c(s)\rceil,
\qquad
c(s)=\frac{\log2}{-2\log s}.
\]

Across the 4599 cells, the maximizing-contact offset is distributed as

\[
\begin{array}{c|rrrr}
k^*-b&0&1&2&3\\
\hline
\text{count}&9&1207&3368&15.
\end{array}
\]

Thus the exact finite strip is

\[
\boxed{
k^*\in\{b,b+1,b+2,b+3\}
}
\]

on the A90 grid.

The A86 three-contact strip

\[
k^*\in\{b,b+1,b+2\}
\]

is reproduced exactly throughout its declared \(M\le300\) scope at the three original probes. Its naive extension beyond that scope is false.

The first counterexample occurs at

\[
M=325,
\qquad
s=129/1000,
\qquad
b=55,
\qquad
k^*=58=b+3.
\]

There are exactly fifteen offset-three cells in the A90 domain. Fourteen occur at \(s=129/1000\), and one occurs at \(s=259/2000\). The full list is stored in the result JSON.

This does not contradict A86: it falsifies only an extrapolation outside A86's stated finite range.

## Relation to A89

A89 and A90 cover complementary questions:

- A89: one local secant, continuum in \(s\), all \(M\ge521\);
- A90: the complete all-contact sequence, nine rational probes, \(10\le M\le520\).

They do **not** combine into a continuum all-\(M\) proof of global unimodality. A90 is probe-discrete, while A89 controls only one local secant.

## What A90 proves

1. An exact denominator-clearing integer evaluator for the A84 ten-term factor.
2. Strict one-variation of all 4599 complete contact sequences on the declared finite grid.
3. Exactly 594423 nonzero adjacent-factor signs.
4. A finite exact four-contact strip through \(M=520\) at nine probes.
5. Exact reproduction of the A86 three-contact theorem inside its original domain.
6. Fifteen exact counterexamples to extending that strip unchanged through \(M=520\).

## What A90 does not prove

A90 does not prove:

- one variation for every real \(s\) between the nine probes;
- global all-contact one variation for \(M\ge521\);
- an all-\(M\) four-contact strip;
- that offset three is the largest possible offset outside the audited range;
- full KKT feasibility for every compressed-objective maximizer under arbitrary contracts;
- any physical, spacetime, pre-temporal, or ontological interpretation.

## Next rigorous target

A91 should study the offset-three mechanism directly. A useful falsifiable question is whether a parity-resolved correction to the A85 asymptotic locator can predict the transition between offsets two and three, or whether the offset depends on a genuinely nonlocal residual. Any proposed classifier must reproduce the fifteen A90 counterexamples and remain explicitly separate from the KKT feasibility problem.
