# Interval-Stable Gamma Bifurcation and the \(M=14\) Extension

**Programme:** Modal Field Research Programme  
**Provisional audit:** A74  
**Author line:** Felipe Gianini Romero  
**Status:** exact interval-stable support-size bifurcation for one declared contact family plus an independent exact \(M=14\) theorem; not an arbitrary-\(M\) theorem

## Technical abstract

A73 established at one exact rational probe that the late-stage signature

\[
S_M:
\quad
P=\{0,3,4,M\},
\qquad
Q=\{1,6,7\},
\]

changes its valid completion-band orientation between \(M=12\) and \(M=13\).

A74 upgrades that pointwise statement in two ways.

First, it derives an exact symbolic Cramer representation for the active
\(\gamma+\) multiplier:

\[
\boxed{
\lambda_{\gamma+}
=
\frac{
N(M,R,T,s,\varepsilon)
}{
D(M,R,T,s,\varepsilon)
},
}
\]

where

\[
R=2^{-M},
\qquad
T=s^M,
\qquad
s=2^{-\alpha}.
\]

The exact numerator and denominator polynomials are stored in the machine
result file. Their specializations reproduce the independently constructed
\(M=12\) and \(M=13\) dual branches identically.

Second, the sign change is certified on the common rational interval

\[
\boxed{
s\in
\left[
\frac{13}{100},
\frac{33}{250}
\right].
}
\]

In first-anchor coordinates, this is

\[
2.9213901653036336\ldots
\le
\alpha
\le
2.9434164716336325\ldots.
\]

Throughout this complete interval:

\[
\boxed{
\lambda_{\gamma+}^{(12)}(s)>0,
}
\]

while:

\[
\boxed{
\lambda_{\gamma+}^{(13)}(s)<0.
}
\]

There are no numerator roots and no denominator roots in the interval.

For \(M=13\), the replacement multiplier also satisfies:

\[
\boxed{
\lambda_{\gamma-}^{(13)}(s)>0.
}
\]

At the exact rational midpoint

\[
s=\frac{131}{1000},
\]

the values are:

\[
\lambda_{\gamma+}^{(12)}
=
2224838033493638813649227536663176772129390592/493559476219425782432514557768829807322564979,
\]

\[
\lambda_{\gamma+}^{(13)}
=
-167035361588963268849827510698750339667993217204224/34557838998663223821110466679591513568569382865437,
\]

and:

\[
\lambda_{\gamma-}^{(13)}
=
167035361588963268849827510698750339667993217204224/33487715040224407622009316509322013978847140842013.
\]

The exact sign conclusion does not rely on this midpoint. It follows from
root isolation and denominator control over the full interval.

The \(M=13\) result is stronger still. On the complete exact phase-7 interval:

\[
\boxed{
\lambda_{\gamma+}^{(13)}<0,
\qquad
\lambda_{\gamma-}^{(13)}>0.
}
\]

Thus the band-sign selection is stable across an entire algebraic phase, not
only around the A73 probe.

A74 then attacks \(M=14\) without importing the \(M=13\) phase grammar. A
separate numerical discovery scan finds seven stable signatures. Those
signatures are then independently certified by exact algebraic phase
analysis.

The exact \(M=14\) integer catalogue contains 84 designs. The unique winner
remains:

\[
\boxed{\{2,3,4\}.}
\]

The continuous completion

\[
D_\alpha=\{\alpha,3,4\},
\qquad
2\le\alpha<3,
\]

has seven exact phases and six simple finite transitions. The minimax risk is
strictly increasing over the full interval, so:

\[
\boxed{\alpha^\star=2}
\]

remains the unique global first-anchor optimum.

---

## 1. Symbolic Cramer reconstruction

The active basis uses the basic variables corresponding to:

\[
p_0,\ p_3,\ p_4,\ p_M,\ q_1,\ q_6,\ q_7,\ t.
\]

The active rows are:

1. \(P\)-normalization;
2. \(Q\)-normalization;
3. \(P\)-mean;
4. \(Q\)-mean;
5. target denominator;
6. \(\alpha+\);
7. \(\beta-\);
8. \(\gamma+\).

Replacing the \(\gamma+\) row by the basic objective row gives the Cramer
numerator \(N\). The original active-basis determinant gives \(D\).

The symbolic formula contains:

- 1124 characters in the factored numerator;
- 1455 characters in the factored denominator.

It is intentionally retained in the JSON result rather than expanded in the
main note, because a copied multiline polynomial is less auditable than the
machine-readable symbolic expression.

The specializations

\[
(M,R,T,\varepsilon)
=
\left(
12,2^{-12},s^{12},\frac1{120000}
\right)
\]

and:

\[
(M,R,T,\varepsilon)
=
\left(
13,2^{-13},s^{13},\frac1{160000}
\right)
\]

agree exactly with the independently reconstructed dual multipliers.

---

## 2. Exact support-size sign bifurcation

The common interval lies strictly inside:

- the exact \(M=12\) phase with \(\gamma+\);
- the exact \(M=13\) phase selected with \(\gamma-\).

The inherited \(M=13\) \(\gamma+\) basis is evaluated on the same contact
support and the same interval.

For all three multiplier expressions, the audit verifies:

1. zero numerator roots in the interval;
2. zero denominator roots in the interval;
3. a nonzero exact rational sample with the declared sign.

Therefore the sign statements hold throughout the interval.

The support-size transition is consequently not an artifact of selecting
different \(\alpha\) values:

\[
\boxed{
\text{at the same continuous first-anchor interval, the dual orientation
changes between }M=12\text{ and }M=13.
}
\]

---

## 3. Full \(M=13\) interval stability

The exact phase-7 interval is bounded by two algebraic transition roots.

Across the entire interval:

\[
\lambda_{\gamma+}^{(13)}(s)<0.
\]

The old signature is therefore dual-infeasible everywhere in that phase.

The selected sign-flipped basis satisfies:

\[
\lambda_{\gamma-}^{(13)}(s)>0
\]

throughout the same interval, and the full phase certificate also proves:

- positive basic variables;
- nonnegative active multipliers;
- nonnegative reduced costs;
- nonnegative inactive slacks;
- positive first-anchor derivative.

This is an interval-stable active-set selection theorem.

---

## 4. Independent \(M=14\) discovery

The numerical discovery scan used 1,000 values of

\[
\alpha\in[2,2.999]
\]

and did not import any \(M=13\) contact list.

It found seven stable phases beginning approximately at:

\[
2.000,\quad
2.616,\quad
2.686,\quad
2.751,\quad
2.938,\quad
2.942,\quad
2.985.
\]

The exact algebraic audit independently recovered the same seven signatures.

The \(M=14\) first phase is:

\[
P=\{1,5,14\},
\qquad
Q=\{0,2,7,8\}.
\]

This differs from the \(M=13\) first phase:

\[
P=\{1,4,13\},
\qquad
Q=\{0,2,6,7\}.
\]

Also:

\[
\boxed{
\text{\(M=13\) has eight phases, whereas \(M=14\) has seven.}
}
\]

Thus the new support does not simply inherit the previous phase grammar.

---

## 5. Exact \(M=14\) phase atlas

| Phase | Active \(P\)-support | Active \(Q\)-support | Active bands |
|---:|---:|---:|---|
| 1 | [1, 5, 14] | [0, 2, 7, 8] | alpha+, beta-, gamma+ |
| 2 | [0, 1, 5, 14] | [2, 7, 8] | alpha+, beta-, gamma+ |
| 3 | [0, 5, 14] | [1, 2, 7, 8] | alpha+, beta-, gamma+ |
| 4 | [0, 4, 5, 14] | [1, 7, 8] | alpha+, beta-, gamma+ |
| 5 | [0, 4, 14] | [1, 7, 8] | alpha+, beta- |
| 6 | [0, 3, 4, 14] | [1, 7, 8] | alpha+, beta-, gamma- |
| 7 | [0, 3, 14] | [1, 7, 8] | alpha+, gamma- |

The exact transitions are:

| Transition | \(\alpha\) | \(s\) |
|---:|---:|---:|
| 1→2 | 2.615847730157685 | 0.163136585870644 |
| 2→3 | 2.685043391904400 | 0.155496779719033 |
| 3→4 | 2.750782829822397 | 0.148570250861960 |
| 4→5 | 2.937089494876706 | 0.130571370357120 |
| 5→6 | 2.941643524261327 | 0.130159856956477 |
| 6→7 | 2.984934717292722 | 0.126312146372401 |

Every transition is a simple algebraic root. All adjacent value branches join
continuously and have finite denominators at the junction.

---

## 6. Exact \(M=14\) catalogue

All 84 designs from

\[
\binom{\{2,\ldots,10\}}3
\]

were solved over exact rational arithmetic.

| Rank | Design | Ratio | Future risk |
|---:|---:|---:|---:|
| 1 | (2, 3, 4) | 1.939453926997 | 0.477825252054 |
| 2 | (2, 3, 5) | 2.004470935403 | 0.501610749364 |
| 3 | (2, 3, 6) | 2.037074198944 | 0.513249265189 |

The winner ratio is:

\[
\boxed{
\rho_{14}(2,3,4)
=
3784218097438011943968095573/1951177104422225715007265924.
}
\]

The runner-up is:

\[
\{2,3,5\}.
\]

The exact positive gap is:

\[
\boxed{
20070555349772232030948077034662589286302377619598755616/308696998553470727299714117417560416131894824762462243773.
}
\]

The top three designs have independently matching exact primal and dual
values.

---

## 7. Global \(M=14\) theorem

For the declared contract:

\[
\operatorname{supp}P\subseteq\{0,\ldots,14\},
\qquad
\mathbb E[X]=7,
\]

\[
\mu=1,
\qquad
\varepsilon=\frac1{240000},
\]

and:

\[
D_\alpha=\{\alpha,3,4\},
\]

the exact ratio is continuous and strictly increasing on:

\[
[2,3).
\]

Therefore:

\[
\boxed{
\arg\min_{2\le\alpha<3}
\rho_{14}(\alpha)
=
\{2\}.
}
\]

The boundary risk is:

\[
Q_{14}(2)
=
0.47782525205358922124201482550708069246660781964958.
\]

The coalescence limit is:

\[
Q_{14}(3^-)
=
1.1718060558950103085195664937838298326625372165651.
\]

---

## 8. What A74 proves

1. An exact symbolic Cramer formula for the declared \(\gamma+\) multiplier.
2. Exact agreement of that formula with the \(M=12\) and \(M=13\) dual
   branches.
3. A support-size sign bifurcation on one common continuous interval.
4. Full-phase instability of \(\gamma+\) at \(M=13\).
5. Full-phase positivity of the selected \(\gamma-\) multiplier at \(M=13\).
6. An independent phase discovery for \(M=14\).
7. Seven exact \(M=14\) phases and six exact transitions.
8. A unique exact catalogue winner \(\{2,3,4\}\) at \(M=14\).
9. A global continuous first-boundary theorem at \(M=14\).

The global exact family now covers:

\[
\boxed{
M=5,6,7,8,9,10,11,12,13,14.
}
\]

This remains a finite collection of exact theorems.

---

## 9. What A74 does not prove

A74 does not establish:

1. a universal gamma-sign threshold for arbitrary \(M\);
2. a closed-form proof that the sign remains negative for all \(M\ge13\);
3. a universal phase grammar;
4. a theorem for means other than \(M/2\);
5. joint continuous reoptimization of all anchors;
6. a support-size-uniform lower bound on the multiplier magnitude.

---

## 10. Next rigorous target

The next target should not merely add \(M=15\).

The exact symbolic formula should be used to study the support-size variable
itself.

A controlled target is:

1. substitute the central-mean normalized errors separately for even and odd
   \(M\);
2. reduce \(N(M,2^{-M},s^M,s,\varepsilon_M)\) to parity-specific forms;
3. test whether the gamma-sign transition repeats or stabilizes for
   \(M=14,15,16\);
4. isolate any support-size threshold on a fixed rational \(s\)-interval;
5. search for a monotone or eventually dominant term structure in \(M\).

A successful result would replace the pairwise \(12\to13\) bifurcation with
an eventual support-size orientation theorem. A failure would identify the
next exact counterexample.
