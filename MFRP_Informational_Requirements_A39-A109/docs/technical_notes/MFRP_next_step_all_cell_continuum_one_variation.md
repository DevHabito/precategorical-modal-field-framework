# A94 — Exact Continuum One-Variation on All 858 A92 Cells

## Status

Exact finite continuum-parameter certificate for every algebraic contact cell constructed by A92 under

\[
10\le M\le520,
\qquad
\frac{129}{1000}\le s\le\frac{133}{1000}.
\]

The A92 admissibility condition for the decisive factor leaves 858 nonempty cells, with effective support range \(14\le M\le520\). A94 classifies the **complete adjacent-factor sequence** on every one of those cells. The result concerns the compressed objective only; it is not a lifted-KKT, arbitrary-support, or physical theorem.

## Question left by A93

A93 proved full-sequence one-variation on the twenty-five cells where A92 had found a positive portion of

\[
E_{M,b+2}(s)=V_{M,b+3}(s)-V_{M,b+2}(s),
\qquad
b=\lceil Mc(s)\rceil.
\]

The remaining 833 cells had a strictly negative decisive factor, but that alone did not determine the global maximizer. A distant factor could have introduced another sign reversal, or the lower central factor \(E_{M,b+1}\) could have changed sign inside a cell. A94 therefore classifies

\[
E_{M,2}(s),E_{M,3}(s),\ldots,E_{M,\lfloor M/2\rfloor-2}(s)
\]

on all 858 cells, while allowing a continuum counterexample to appear.

## Exact certification method

The complete audit contains

\[
\boxed{125,814\text{ factor--cell classifications}},
\]

of which

\[
\boxed{124,956}
\]

are non-decisive factors and 858 are the decisive A92 factors.

For each non-decisive seven-term sparse rational polynomial, A94 first applies the monotone-monomial enclosure on a rational outer hull containing the exact algebraic cell. This closes immediately for

\[
\boxed{119,984\text{ factors}}.
\]

The remaining

\[
\boxed{4,972}
\]

are resolved exactly as follows:

- 4,674 fixed positive factors by adaptive rational interval subdivision;
- 104 fixed negative factors by the same method;
- 181 simple increasing roots and one simple decreasing root by a globally signed first derivative;
- twelve further simple increasing roots by a strict-convexity certificate \(P''>0\), exact opposite endpoint signs, and a locally positive derivative on the rational root bracket.

Every root bracket has width at most \(10^{-24}\) and lies strictly inside the corresponding exact algebraic \(b\)-cell. Decimal root midpoints are presentation-only.

## Remote-sign law

A94 finds that all non-decisive roots occur at exactly

\[
k=b+1.
\]

Together with the A92 decisive factor at \(k=b+2\), this yields the finite remote-sign law

\[
E_{M,k}(s)>0\quad(k<b+1),
\]

and

\[
E_{M,k}(s)<0\quad(k>b+2)
\]

throughout every exact A92 cell.

Thus only the two central factors

\[
E_{M,b+1},\qquad E_{M,b+2}
\]

can determine the global compressed-maximizer phase in the declared atlas. No distant reversal occurs.

## Complete phase classification

All 858 cells have one variation. The exact phase counts are:

| Phase | Cell count |
|---|---:|
| unique global maximum \(b+1\) | 195 |
| unique global maximum \(b+2\) | 444 |
| increasing exchange \(b+1\to\{b+1,b+2\}\to b+2\) | 193 |
| decreasing exchange \(b+2\to\{b+1,b+2\}\to b+1\) | 1 |
| unique global maximum \(b+3\) | 14 |
| increasing exchange \(b+2\to\{b+2,b+3\}\to b+3\) | 11 |

Therefore:

\[
\boxed{653\text{ cells have a fixed unique global maximizer}},
\]

and

\[
\boxed{205\text{ cells contain one simple adjacent global exchange}}.
\]

There are 204 increasing transitions and one decreasing transition. The unique decreasing case is

\[
\boxed{M=28,\quad b=5},
\]

where the global maximizer moves

\[
b+2\longrightarrow\{b+1,b+2\}\longrightarrow b+1
\]

as \(s\) increases.

This reverse transition is preserved rather than rewritten as an increasing law.

## Relation to A92 and A93

A92 supplied the complete exact atlas for the upper central factor \(E_{M,b+2}\). A93 promoted twenty-five selected cells from local to global. A94 now closes the remaining finite continuum gap:

\[
\boxed{858/858\text{ exact cells have full-sequence one-variation}}.
\]

The result is stronger than a probe-grid stress test because it covers each complete algebraic cell in the declared continuum interval. It is also narrower than a universal theorem because both \(M\) and \(s\) remain bounded by the explicit contract.

## Independent regressions

Forty-eight exact comparisons reconstruct representative central factors through both:

1. the A94/A92 sparse seven-term polynomial generator; and
2. the independent A84 exact \(k\)-space evaluator.

All 48 values agree literally.

## Evidence discipline

A94 proves:

1. all 125,814 factor--cell pairs are classified exactly;
2. every one of the 858 A92 cells has one variation;
3. all fixed and transition global compressed-maximizer phases have the counts stated above;
4. only the two central factors can change the maximizer in the declared atlas;
5. all 205 transition roots are simple and adjacent;
6. the single reverse transition at \(M=28\) is genuine within the declared contract.

A94 does **not** prove:

1. one-variation for \(M>520\);
2. one-variation outside \(129/1000\le s\le133/1000\);
3. a universal bound on contact offsets in another contract;
4. primal feasibility or KKT optimality of every lifted branch;
5. any physical, spacetime, matter, or pre-temporal interpretation.

## Next rigorous target

The remaining obstruction is no longer continuum one-variation inside the finite A92 atlas. It is the separation between the compressed-objective maximizer and the lifted full LP/KKT branch.

A95 should test the 858 continuum phase cells against exact primal feasibility and active-dual conditions of the corresponding lifted families. It must preserve the eight probe-level feasibility exceptions already found by A82 and allow new continuum feasibility boundaries to appear. A compressed maximum must not be promoted to a valid full branch without that additional certificate.
