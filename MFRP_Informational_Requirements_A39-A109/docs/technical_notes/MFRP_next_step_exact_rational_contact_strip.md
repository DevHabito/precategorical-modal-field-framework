# Exact Rational Contact Strip and Finite Exclusion Thresholds

**Programme:** Modal Field Research Programme  
**Audit:** A86  
**Author line:** Felipe Gianini Romero  
**Status:** exact finite localization theorem under the A84 three-probe contract

## Technical abstract

A85 derived the asymptotic contact slope

\[
c(s)=\frac{\log 2}{-2\log s},
\]

but its finite offset diagnostic used high-precision logarithms and was therefore not a formal interval certificate. A86 removes that limitation for the finite A84 domain. For a rational comparison point \(p/q\), the transcendental comparison is equivalent to an integer comparison:

\[
c(s)>\frac pq
\quad\Longleftrightarrow\quad
2^q s^{2p}>1,
\]

\[
c(s)<\frac pq
\quad\Longleftrightarrow\quad
2^q s^{2p}<1.
\]

Using this identity, A86 constructs exact rational enclosures for all three probe slopes, computes \(\lceil M c(s)\rceil\) without floating-point logarithms, and compares it with the exact A84 transition contact for every

\[
10\le M\le300.
\]

The result is the finite three-contact localization law

\[
\boxed{
\lceil M c(s)\rceil
\le k^\star(M,s)
\le \lceil M c(s)\rceil+2
}
\]

for all 873 support/probe cells. Equivalently,

\[
\boxed{
\frac{9}{10}
<k^\star(M,s)-M c(s)<3
}.
\]

The upper bound sharpens to \(14/5\) at \(s=131/1000\) and to \(27/10\) at \(s=133/1000\). Combined with A84's exact one-sign-variation theorem, all admissible contacts below the asymptotic slope are certified positive and all contacts at least three indices above it are certified negative. The full finite contact scan is therefore compressed to at most three candidate contacts per support/probe cell.

This is not an all-\(M\) rounding theorem. The proof is exact but finite and inherits the three fixed rational probes and support range of A84.

---

## 1. Exact comparison lemma

Let

\[
0<s<1,
\qquad
c(s)=\frac{\log 2}{-2\log s},
\]

and let \(p/q\ge0\) be rational. Since \(-2q\log s>0\),

\[
c(s)>\frac pq
\iff
q\log2>-2p\log s.
\]

Exponentiation gives

\[
c(s)>\frac pq
\iff
2^q s^{2p}>1.
\]

The reverse strict inequality is identical. For rational \(s=a/b\), this becomes the exact integer comparison

\[
2^q a^{2p}
\mathrel{\gtrless}
b^{2p}.
\]

No numerical logarithm enters any gate in A86.

---

## 2. Exact slope enclosures

With denominator \(100000\), the certified brackets are:

\[
\frac{16923}{100000}
<c\!\left(\frac{129}{1000}\right)
<\frac{16924}{100000},
\]

\[
\frac{17051}{100000}
<c\!\left(\frac{131}{1000}\right)
<\frac{17052}{100000},
\]

\[
\frac{17179}{100000}
<c\!\left(\frac{133}{1000}\right)
<\frac{17180}{100000}.
\]

Each endpoint is checked by the integer comparison lemma. The common bracket width is exactly

\[
10^{-5}.
\]

---

## 3. Exact finite contact strip

A84 supplies, for each support and probe, an exact strict sign sequence

\[
+,+,\ldots,+,-,\ldots,-
\]

and a unique transition contact \(k^\star\). A86 compares \(k^\star/M\) directly with \(c(s)\) by integer arithmetic.

Across all 873 cells:

\[
k^\star-Mc(s)>\frac9{10}.
\]

The certified upper bounds are:

\[
k^\star-Mc(s)<3,
\qquad s=\frac{129}{1000},
\]

\[
k^\star-Mc(s)<\frac{14}{5},
\qquad s=\frac{131}{1000},
\]

\[
k^\star-Mc(s)<\frac{27}{10},
\qquad s=\frac{133}{1000}.
\]

The uniform consequence is

\[
0<k^\star-Mc(s)<3.
\]

Because \(Mc(s)\) is nonintegral for the declared rational probes, this is equivalent to

\[
k^\star\in
\left\{
\lceil Mc(s)\rceil,
\lceil Mc(s)\rceil+1,
\lceil Mc(s)\rceil+2
\right\}.
\]

The exact offset counts are:

| Probe | offset 0 | offset 1 | offset 2 |
|---|---:|---:|---:|
| \(129/1000\) | 1 | 65 | 225 |
| \(131/1000\) | 1 | 105 | 185 |
| \(133/1000\) | 1 | 133 | 157 |

For every probe, offset zero occurs only at \(M=12\).

---

## 4. Sign exclusion consequence

Let \(E_{M,k}(s)\) be the adjacent compressed-objective factor from A83–A85. A84 proves

\[
E_{M,k}(s)>0\quad(k<k^\star),
\]

and

\[
E_{M,k}(s)<0\quad(k\ge k^\star).
\]

The A86 strip then gives:

\[
\boxed{
\frac{k}{M}\le c(s)
\Longrightarrow
E_{M,k}(s)>0
}
\]

and

\[
\boxed{
\frac{k}{M}\ge c(s)+\frac3M
\Longrightarrow
E_{M,k}(s)<0
}.
\]

Thus the exact transition is confined to a strip of at most three contact indices. This does not prove the A84 one-sign-variation theorem independently; it converts that theorem into an explicit localization and exclusion rule.

---

## 5. Finite exact tail thresholds

A86 also asks when

\[
0<\frac{k^\star}{M}-c(s)<\delta
\]

holds on a complete finite tail ending at \(M=300\). The smallest verified tail starts are:

| Probe | \(\delta=1/20\) | \(\delta=1/50\) | \(\delta=1/100\) |
|---|---:|---:|---:|
| \(129/1000\) | 46 | 133 | 291 |
| \(131/1000\) | 46 | 132 | 272 |
| \(133/1000\) | 46 | 126 | 265 |

For example, at the central probe,

\[
132\le M\le300
\quad\Longrightarrow\quad
0<\frac{k^\star}{M}-c(s)<\frac1{50}.
\]

These are exact finite thresholds. They are not claims about every \(M>300\).

---

## 6. Computational reduction

The A84 finite scan contains 64,821 adjacent contact/probe evaluations. Intersecting the three-contact localizer with the admissible contact range leaves 2,619 candidate contact/probe cells, a reduction factor of approximately

\[
24.75.
\]

The reduction is a consequence of the certified finite strip, not a heuristic truncation.

---

## 7. What A86 proves

1. An exact integer criterion for comparing the asymptotic slope with any nonnegative rational number.
2. Exact width-\(10^{-5}\) slope brackets at all three A84 probes.
3. Exact computation of \(\lceil Mc(s)\rceil\) for every \(10\le M\le300\).
4. A three-contact localization theorem in all 873 support/probe cells.
5. The stronger uniform lower offset \(k^\star-Mc(s)>9/10\).
6. Probe-specific upper contact-unit bounds.
7. Exact finite \(\delta\)-tail thresholds through \(M=300\).
8. A finite reduction from the full contact scan to at most three candidates per cell.

---

## 8. What A86 does not prove

A86 does not prove:

1. the three-contact strip for \(M>300\);
2. a universal formula selecting offset 0, 1, or 2;
3. all-\(M\) unimodality;
4. exact periodicity of contact blocks;
5. a physical meaning for \(M\), \(k\), the probes, or the active contacts.

The next rigorous target is to explain the offset choice inside the three-contact strip. A natural A87 question is whether parity and the sign of a single exactly normalized residual can decide among

\[
\lceil Mc\rceil,
\quad
\lceil Mc\rceil+1,
\quad
\lceil Mc\rceil+2,
\]

without restoring a full contact scan. That hypothesis must be tested against all 873 exact cells and must remain allowed to fail.
