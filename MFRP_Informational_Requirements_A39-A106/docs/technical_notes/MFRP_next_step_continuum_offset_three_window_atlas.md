# A92 — Exact Continuum Offset-Three Window Atlas

## Status

Exact finite continuum-parameter certificate for

\[
10\le M\le520,
\qquad
\frac{129}{1000}\le s\le\frac{133}{1000}.
\]

All theorem gates use exact rational arithmetic, exact integer comparisons, and adaptive rational interval bounds. Decimal values below are presentation-only midpoints of certified rational brackets.

The theorem is a complete atlas for the **decisive adjacent factor** and a certificate of strict **local** compressed maxima. It is not promoted to a continuum global-maximizer theorem because global one-variation over all contacts has only been proved on the finite A90 probe grid.

## Motivation

A90 and A91 found fifteen cells on nine rational probes where

\[
k^*=\lceil Mc(s)\rceil+3,
\qquad
c(s)=\frac{\log2}{-2\log s}.
\]

A pointwise grid cannot determine whether these cells are isolated samples from open windows, whether additional windows lie between probes, or whether hidden roots occur in cells having equal endpoint signs. A92 removes that ambiguity over the declared finite domain.

## Exact cell decomposition

Write

\[
b(s)=\lceil Mc(s)\rceil.
\]

The boundary between consecutive values of \(b\) is

\[
\sigma_{M,b}=2^{-M/(2b)},
\]

characterized exactly by

\[
2^M\sigma_{M,b}^{2b}=1.
\]

No logarithm is needed to classify a rational point. For \(s=a/d\), the comparison is the integer comparison

\[
2^M a^{2b}\mathrel{\lessgtr}d^{2b}.
\]

Each algebraic boundary is enclosed in a rational bracket of width \(10^{-18}\). The exact \(b\)-cell lies inside the corresponding outer rational hull, so a sign certificate on the hull is also valid on the exact algebraic cell.

## Sparse decisive factor

For every nonempty \(b\)-cell, A92 constructs the complete adjacent factor

\[
E_{M,b+2}(s)=V_{M,b+3}(s)-V_{M,b+2}(s)
\]

as a sparse rational polynomial in \(s\). The independent generator was compared exactly against the committed A84 evaluator in 42 regression cases, with no mismatch.

Across the complete atlas of

\[
\boxed{858\text{ nonempty }b\text{-cells}},
\]

the classification is

\[
\boxed{833\text{ strictly negative cells}},
\]

\[
\boxed{14\text{ strictly positive cells}},
\]

and

\[
\boxed{11\text{ cells with one simple increasing root}}.
\]

There are no undecided cells. In every root cell, the derivative is certified positive over the complete outer hull, so the sign transition is uniquely

\[
-\longrightarrow+.
\]

Each root is isolated in a rational bracket of width at most \(10^{-24}\).

## Twenty-five local offset-three windows

The complete support set is

\[
\boxed{325, 360, 366, 372, 378, 384, 390, 425, 431, 437, 443, 449, 454, 455, 460, 466, 472, 478, 484, 490, 496, 502, 508, 514, 520}.
\]

The strict local pattern is certified throughout every positive portion:

\[
E_{M,b+1}(s)>0,
\qquad
E_{M,b+2}(s)>0,
\qquad
E_{M,b+3}(s)<0.
\]

Hence

\[
V_{M,b+2}<V_{M,b+3}>V_{M,b+4},
\]

so contact \(b+3\) is a strict local compressed maximizer on each window.

| \(M\) | \(b\) | local maximum | lower endpoint | algebraic-cell upper endpoint | window type |
|---:|---:|---:|---:|---:|---|
| 325 | 55 | 58 | 0.129000000000000000000000 | 0.129001034966776203500000 | full-positive |
| 360 | 61 | 64 | 0.129248669282242563092131 | 0.129334612698326732500000 | root-to-boundary |
| 366 | 62 | 65 | 0.129091452468879919329264 | 0.129263520724808224500000 | root-to-boundary |
| 372 | 63 | 66 | 0.129000000000000000000000 | 0.129194722875878466500000 | full-positive |
| 378 | 64 | 67 | 0.129000000000000000000000 | 0.129128109877653552500000 | full-positive |
| 384 | 65 | 68 | 0.129000000000000000000000 | 0.129063579287150369500000 | full-positive |
| 390 | 66 | 69 | 0.129000000000000000000000 | 0.129001034966776203500000 | full-positive |
| 425 | 72 | 75 | 0.129240907226494696744036 | 0.129283593664214653500000 | root-to-boundary |
| 431 | 73 | 76 | 0.129124448169573642714452 | 0.129223933926531396500000 | root-to-boundary |
| 437 | 74 | 77 | 0.129010339731351033977083 | 0.129165913039068644500000 | root-to-boundary |
| 443 | 75 | 78 | 0.129000000000000000000000 | 0.129109464393673369500000 | full-positive |
| 449 | 76 | 79 | 0.129000000000000000000000 | 0.129054524943216899500000 | full-positive |
| 454 | 77 | 80 | 0.129546704535396358424613 | 0.129582971565724137500000 | root-to-boundary |
| 455 | 77 | 80 | 0.129000000000000000000000 | 0.129001034966776203500000 | full-positive |
| 460 | 78 | 81 | 0.129442491883118538475402 | 0.129523165143833857500000 | root-to-boundary |
| 466 | 79 | 82 | 0.129340702876228009063362 | 0.129464899371782896500000 | root-to-boundary |
| 472 | 80 | 83 | 0.129241200952938172549761 | 0.129408115480172188500000 | root-to-boundary |
| 478 | 81 | 84 | 0.129143852471873800616972 | 0.129352757650877830500000 | root-to-boundary |
| 484 | 82 | 85 | 0.129048525823565868611968 | 0.129298772834105824500000 | root-to-boundary |
| 490 | 83 | 86 | 0.129000000000000000000000 | 0.129246110578887623500000 | full-positive |
| 496 | 84 | 87 | 0.129000000000000000000000 | 0.129194722875878466500000 | full-positive |
| 502 | 85 | 88 | 0.129000000000000000000000 | 0.129144564011429260500000 | full-positive |
| 508 | 86 | 89 | 0.129000000000000000000000 | 0.129095590431999997500000 | full-positive |
| 514 | 87 | 90 | 0.129000000000000000000000 | 0.129047760618069745500000 | full-positive |
| 520 | 88 | 91 | 0.129000000000000000000000 | 0.129001034966776203500000 | full-positive |

For the fourteen `full-positive` rows, the window starts at the declared lower endpoint \(s=129/1000\). For the eleven `root-to-boundary` rows, the lower endpoint is the unique simple root and is excluded. The algebraic upper boundary belongs to the \(b\)-cell because \(Mc(s)=b\) there and \(\lceil Mc(s)\rceil=b\).

## Ten windows missed by the nine-probe grid

The continuum audit adds the exact supports

\[
\boxed{360, 366, 425, 431, 437, 454, 466, 472, 478, 484}.
\]

These are not corrections to A90 or A91. Those audits classified their declared finite probes correctly. A92 shows that a nine-point grid was insufficient to enumerate all open windows between the probes.

The distinction matters:

> Pointwise exactness does not imply continuum completeness.

## Evidence discipline

A92 proves:

1. the complete sign classification of the decisive factor \(E_{M,b+2}\) on all 858 exact \(b\)-cells in the declared domain;
2. uniqueness and simplicity of the eleven internal roots;
3. the existence of twenty-five strict local compressed-maximizer windows;
4. ten additional windows not sampled by the A90–A91 probe grid.

A92 does **not** prove:

1. global one-variation over all contacts for every real \(s\) in the interval;
2. that the local maximum is the global compressed maximum throughout every window;
3. validity for \(M>520\) or outside the declared \(s\)-interval;
4. a universal bound excluding offsets four or larger;
5. any physical, spacetime, matter, or pre-temporal interpretation.

## Next rigorous target

The next legitimate audit is to certify the full adjacent-factor sign sequence on these twenty-five continuum windows, rather than only the decisive and immediate neighboring factors. That would test whether the local windows can be promoted to global offset-three windows without assuming continuum unimodality.
