# A93 — Exact Continuum Full-Sequence One-Variation

## Status

Exact finite continuum-parameter certificate for the twenty-five algebraic contact cells selected by A92 under

\[
10\le M\le520,
\qquad
\frac{129}{1000}\le s\le\frac{133}{1000}.
\]

A93 promotes the twenty-five A92 **local** offset-three windows to **global compressed-maximizer** windows. The promotion is exact for the declared cells and uses rational outer-hull interval arithmetic. It is not an all-cell, all-support, lifted-KKT, or physical theorem.

## Question left by A92

A92 classified the decisive factor

\[
E_{M,b+2}(s)=V_{M,b+3}(s)-V_{M,b+2}(s),
\qquad
b=\lceil Mc(s)\rceil,
\]

on all 858 algebraic \(b\)-cells in the declared domain. It found fourteen cells where the decisive factor is positive throughout and eleven cells with one simple increasing root. It also checked the immediate neighbors \(E_{M,b+1}\) and \(E_{M,b+3}\).

That was sufficient for a strict local maximum, but not for a global one. A distant contact could in principle produce another sign reversal. A93 therefore certifies the full sequence

\[
E_{M,2}(s),E_{M,3}(s),\ldots,E_{M,\lfloor M/2\rfloor-2}(s)
\]

on every selected continuum cell.

## Exact interval method

For each non-decisive factor, A93 constructs the exact seven-term sparse rational polynomial inherited from A83–A84 and evaluates its monotone monomial interval enclosure on a rational **outer hull** containing the exact algebraic cell.

If

\[
P(s)=\sum_j a_j s^{n_j},
\qquad s\in[\ell,u]\subset(0,1),
\]

then each positive coefficient contributes

\[
a_j[\ell^{n_j},u^{n_j}],
\]

and each negative coefficient contributes

\[
a_j[u^{n_j},\ell^{n_j}].
\]

Every one of the 5,426 non-decisive factors excludes zero on the first enclosure. No interval subdivision, floating-point sign decision, interpolation, or root guessing is required.

The exact counts are

\[
\boxed{5,426\text{ non-decisive interval certificates}},
\]

with

\[
\boxed{1,873\text{ fixed positive factors}}
\]

and

\[
\boxed{3,553\text{ fixed negative factors}}.
\]

Including the twenty-five decisive factors already classified by A92 gives

\[
\boxed{5,451\text{ full-sequence factor classifications}}.
\]

All 108 independent sparse-polynomial versus A84 exact-evaluator regressions agree.

## Global one-variation theorem

Write

\[
E_{M,k}(s)=V_{M,k+1}(s)-V_{M,k}(s).
\]

### Fourteen full-positive cells

For

\[
M\in\{325,372,378,384,390,443,449,455,490,496,502,508,514,520\},
\]

A93 proves throughout the complete exact \(b\)-cell:

\[
E_{M,k}(s)>0\quad(k<b+3),
\]

and

\[
E_{M,k}(s)<0\quad(k\ge b+3).
\]

Therefore \(k=b+3\) is the unique global compressed maximizer throughout the cell.

### Eleven simple global transitions

For

\[
M\in\{360,366,425,431,437,454,460,466,472,478,484\},
\]

all non-decisive signs remain fixed throughout the complete cell, while the decisive factor \(E_{M,b+2}\) has the unique simple increasing root certified by A92. Consequently:

\[
s<r_{M,b}
\Longrightarrow
k^*=b+2,
\]

\[
s=r_{M,b}
\Longrightarrow
\operatorname*{argmax}_k V_{M,k}=\{b+2,b+3\},
\]

and

\[
s>r_{M,b}
\Longrightarrow
k^*=b+3.
\]

The root is therefore not merely a local orientation switch. It is an exact exchange of the **global compressed maximizer** between two adjacent contacts.

| \(M\) | \(b\) | left global maximum | root tie | right global maximum | root midpoint (presentation only) |
|---:|---:|---:|---:|---:|---:|
| 360 | 61 | 63 | 63, 64 | 64 | 0.129248669282242563092131 |
| 366 | 62 | 64 | 64, 65 | 65 | 0.129091452468879919329264 |
| 425 | 72 | 74 | 74, 75 | 75 | 0.129240907226494696744036 |
| 431 | 73 | 75 | 75, 76 | 76 | 0.129124448169573642714452 |
| 437 | 74 | 76 | 76, 77 | 77 | 0.129010339731351033977083 |
| 454 | 77 | 79 | 79, 80 | 80 | 0.129546704535396358424613 |
| 460 | 78 | 80 | 80, 81 | 81 | 0.129442491883118538475402 |
| 466 | 79 | 81 | 81, 82 | 82 | 0.129340702876228009063362 |
| 472 | 80 | 82 | 82, 83 | 83 | 0.129241200952938172549761 |
| 478 | 81 | 83 | 83, 84 | 84 | 0.129143852471873800616972 |
| 484 | 82 | 84 | 84, 85 | 85 | 0.129048525823565868611968 |

The decimal roots are not theorem inputs. Exact rational isolating brackets are stored in the A92 and A93 catalogues.

## What changed relative to A92

A92 proved a complete continuum atlas for one decisive factor and strict local maxima. A93 proves that no distant contact reverses the sequence on any of those twenty-five cells. Thus all twenty-five local windows are promoted to global compressed-maximizer windows.

This is a genuine strengthening:

\[
\text{local maximum}
\quad\longrightarrow\quad
\text{unique global maximum or exact adjacent global tie}.
\]

## Evidence discipline

A93 proves:

1. all 5,426 non-decisive adjacent factors have their required strict signs on rational outer hulls containing the exact cells;
2. all twenty-five complete factor sequences have one variation, with the decisive-root interpretation inherited exactly from A92;
3. fourteen exact cells have the unique global maximum \(b+3\);
4. eleven exact cells have a global transition \(b+2\to\{b+2,b+3\}\to b+3\);
5. all 108 independent evaluator regressions agree.

A93 does **not** prove:

1. continuum one-variation on the other 833 A92 cells;
2. continuum one-variation for arbitrary \(M\) or outside the declared interval;
3. that offsets four or larger are universally impossible;
4. primal feasibility or KKT optimality of every lifted full branch;
5. any physical, spacetime, matter, or pre-temporal interpretation.

## Next rigorous target

The remaining mathematical gap is no longer the twenty-five offset-three windows. It is the rest of the continuum atlas. A94 should classify the full adjacent-factor sequence on all 858 A92 cells, not only the twenty-five selected cells, and determine whether every cell has one variation or whether a genuine continuum counterexample exists.

That audit must allow either outcome. A negative cell in the decisive-factor atlas need not automatically have a simple global offset-two structure; the complete sequence must be checked rather than inferred.
