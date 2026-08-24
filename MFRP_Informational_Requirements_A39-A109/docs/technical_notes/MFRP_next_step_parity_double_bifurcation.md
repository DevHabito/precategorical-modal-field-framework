# Parity-Reduced Support-Size Orientation and the Exact \(M=15,16\) Extensions

**Programme:** Modal Field Research Programme  
**Provisional audit:** A75  
**Author line:** Felipe Gianini Romero  
**Status:** exact all-\(M\) orientation theorem on one declared continuous interval, plus exact global theorems for \(M=15,16\); not a universal active-set theorem

## Technical abstract

A74 proved that the late-stage \(\gamma+\) multiplier changes sign between
\(M=12\) and \(M=13\) on the common exact interval

\[
I=
\left[
\frac{13}{100},
\frac{33}{250}
\right]
\]

in the coordinate

\[
s=2^{-\alpha}.
\]

A75 studies the support-size variable itself.

For the central-mean signature

\[
P=\{0,3,4,M\},
\qquad
Q=\{1,h,h+1\},
\qquad
h=\left\lfloor\frac M2\right\rfloor,
\]

with active bands

\[
\alpha+,\qquad\beta-,\qquad\gamma+,
\]

the normalized error has exact parity forms.

For even supports:

\[
M=2h,
\qquad
U=2^{-h},
\qquad
V=s^h,
\qquad
\varepsilon=\frac{U}{1875}.
\]

For odd supports:

\[
M=2h+1,
\qquad
U=2^{-h},
\qquad
V=s^h,
\qquad
\varepsilon=\frac{U}{2500}.
\]

The active \(\gamma+\) multiplier has the exact parity-specific Cramer forms

\[
\lambda_{\gamma+}^{\rm even}
=
\frac{
N_{\rm even}(h,U,V,s)
}{
D_{\rm even}(h,U,V,s)
},
\]

and

\[
\lambda_{\gamma+}^{\rm odd}
=
\frac{
N_{\rm odd}(h,U,V,s)
}{
D_{\rm odd}(h,U,V,s)
}.
\]

The complete exact polynomials are stored in:

- `a75_parity_formula_cache.json`;
- `a75_parity_orientation_results.json`.

Their \(M=12\) and \(M=13\) specializations agree identically with the
independent A74 symbolic Cramer construction.

The exact support-size theorem on \(I\) is:

\[
\boxed{
\lambda_{\gamma+}(M,s)>0
\quad
\text{for }M=10,11,12,
}
\]

\[
\boxed{
\lambda_{\gamma+}(M,s)<0
\quad
\text{for }13\le M\le21,
}
\]

and

\[
\boxed{
\lambda_{\gamma+}(M,s)>0
\quad
\text{for every integer }M\ge22.
}
\]

Thus the negative orientation discovered at \(M=13\) is not permanent.

There are two exact support-size bifurcations:

\[
\boxed{
12\longrightarrow13
}
\]

and

\[
\boxed{
21\longrightarrow22.
}
\]

The mechanisms differ.

At the first bifurcation, the Cramer numerator changes sign.

At the second bifurcation, the numerator remains negative, but the
active-basis determinant changes from positive to negative. The ratio
therefore becomes positive again.

A75 also independently discovers and certifies the complete continuous
first-anchor problems for \(M=15\) and \(M=16\).

Each support has:

\[
\boxed{
6\text{ exact algebraic phases}
}
\]

and

\[
\boxed{
5\text{ simple finite transitions}.
}
\]

For both supports:

\[
\frac{d\rho_M}{d\alpha}>0
\quad
\text{on }[2,3),
\]

so

\[
\boxed{
\alpha^\star=2
}
\]

is the unique global first-anchor optimum.

All 84 integer designs were also ranked exactly for each support, and the
unique winner remains:

\[
\boxed{\{2,3,4\}.}
\]

---

## 1. Parity-specific leading orientation

Setting the exponentially small variables

\[
U=V=0
\]

gives the leading even-support determinants:

\[
N_{\rm even}^{(0)}
=
\frac{
3h(2s-1)(8s-1)(84s^2+10s+1)
}{
65536
},
\]

\[
D_{\rm even}^{(0)}
=
-\frac{
h(8s-1)(16s-1)(448s^2+24s+1)
}{
67108864
}.
\]

For odd supports:

\[
N_{\rm odd}^{(0)}
=
\frac{
3(2h+1)(2s-1)(8s-1)(84s^2+10s+1)
}{
131072
},
\]

\[
D_{\rm odd}^{(0)}
=
-\frac{
(2h+1)(8s-1)(16s-1)(448s^2+24s+1)
}{
134217728
}.
\]

On \(I\):

\[
2s-1<0,
\]

while:

\[
8s-1>0,
\qquad
16s-1>0.
\]

Both quadratic factors are positive. Hence all four leading determinants are
strictly negative.

Therefore the eventual multiplier orientation is positive, provided the
exponentially small remainder cannot overturn either determinant.

---

## 2. Exact finite Bernstein certificates

For every integer

\[
10\le M\le35,
\]

the specialized numerator and denominator are ordinary rational polynomials
in \(s\).

Each polynomial was transformed exactly to the Bernstein basis on \(I\).
Every Bernstein coefficient had one strict sign.

No root isolation or floating-point sampling is needed for these finite
certificates.

| \(M\) | Parity | Numerator | Denominator | Multiplier | Degree |
|---:|---:|---:|---:|---:|---:|
| 10 | even | +1 | +1 | +1 | 10 |
| 11 | odd | +1 | +1 | +1 | 11 |
| 12 | even | +1 | +1 | +1 | 12 |
| 13 | odd | -1 | +1 | -1 | 13 |
| 14 | even | -1 | +1 | -1 | 14 |
| 15 | odd | -1 | +1 | -1 | 15 |
| 16 | even | -1 | +1 | -1 | 16 |
| 17 | odd | -1 | +1 | -1 | 17 |
| 18 | even | -1 | +1 | -1 | 18 |
| 19 | odd | -1 | +1 | -1 | 19 |
| 20 | even | -1 | +1 | -1 | 20 |
| 21 | odd | -1 | +1 | -1 | 21 |
| 22 | even | -1 | -1 | +1 | 22 |
| 23 | odd | -1 | -1 | +1 | 23 |
| 24 | even | -1 | -1 | +1 | 24 |
| 25 | odd | -1 | -1 | +1 | 25 |
| 26 | even | -1 | -1 | +1 | 26 |
| 27 | odd | -1 | -1 | +1 | 27 |
| 28 | even | -1 | -1 | +1 | 28 |
| 29 | odd | -1 | -1 | +1 | 29 |
| 30 | even | -1 | -1 | +1 | 30 |
| 31 | odd | -1 | -1 | +1 | 31 |
| 32 | even | -1 | -1 | +1 | 32 |
| 33 | odd | -1 | -1 | +1 | 33 |
| 34 | even | -1 | -1 | +1 | 34 |
| 35 | odd | -1 | -1 | +1 | 35 |

The sign pattern is:

| Support range | Numerator | Denominator | Multiplier |
|---:|---:|---:|---:|
| \(10\le M\le12\) | \(+\) | \(+\) | \(+\) |
| \(13\le M\le21\) | \(-\) | \(+\) | \(-\) |
| \(22\le M\le35\) | \(-\) | \(-\) | \(+\) |

This proves both bifurcations through \(M=35\).

---

## 3. Exact asymptotic bound

Write:

\[
N=N^{(0)}+R_N,
\qquad
D=D^{(0)}+R_D.
\]

Every monomial in a remainder contains at least one positive power of \(U\)
or \(V\).

A generic remainder monomial is bounded by:

\[
|c|h^p
\left(
2^{-u}
\left(\frac{33}{250}\right)^v
\right)^h
\left(\frac{33}{250}\right)^r.
\]

The maximum polynomial power in \(h\) is \(p=2\).

For \(h\ge18\), the one-step ratio is at most:

\[
\frac12
\left(
\frac{19}{18}
\right)^2
=
\boxed{
\frac{361}{648}
<1.
}
\]

Thus every termwise upper bound decreases with \(h\), and it is sufficient to
evaluate the total remainder bounds at \(h=18\).

| Parity | Determinant | Remainder terms | Remainder/leading | Maximum step ratio |
|---:|---:|---:|---:|---:|
| even | numerator | 88 | 0.030075705502 | 361/648 |
| even | denominator | 124 | 0.499682205793 | 361/648 |
| odd | numerator | 92 | 0.021972818527 | 361/648 |
| odd | denominator | 128 | 0.356626327734 | 361/648 |

All four ratios are strictly below one.

Consequently:

\[
N_{\rm even}<0,
\qquad
D_{\rm even}<0
\quad
(h\ge18),
\]

and:

\[
N_{\rm odd}<0,
\qquad
D_{\rm odd}<0
\quad
(h\ge18).
\]

This covers:

\[
M\ge36
\quad\text{for even supports}
\]

and:

\[
M\ge37
\quad\text{for odd supports}.
\]

Combining this asymptotic proof with the exact finite certificates for
\(22\le M\le35\) proves:

\[
\boxed{
\lambda_{\gamma+}>0
\quad
\text{for every integer }M\ge22
}
\]

on \(I\).

---

## 4. Interpretation of the double bifurcation

The Cramer multiplier is:

\[
\lambda_{\gamma+}
=
\frac ND.
\]

The first bifurcation is:

\[
M=12:
\quad
N>0,\ D>0,
\]

\[
M=13:
\quad
N<0,\ D>0.
\]

Therefore the multiplier becomes negative because the numerator changes
orientation.

The second bifurcation is:

\[
M=21:
\quad
N<0,\ D>0,
\]

\[
M=22:
\quad
N<0,\ D<0.
\]

The multiplier becomes positive again because the active-basis determinant
changes orientation.

This distinction matters. The return of a positive multiplier does not mean
that the same dual-envelope coefficient has reversed its Cramer numerator.
It means that the orientation of the basic coordinate system has changed.

---

## 5. Independent \(M=15,16\) discovery

A separate numerical discovery scan used 1,200 values of:

\[
\alpha\in[2,2.999]
\]

for each support.

It did not import the \(M=14\) phase list.

Both supports produced six stable signatures. The numerical signatures agree
exactly with the independently certified algebraic phase signatures.

---

## 6. Exact \(M=15,16\) phase atlas

| \(M\) | Phase | Active \(P\)-support | Active \(Q\)-support | Active bands |
|---:|---:|---:|---:|---|
| 15 | 1 | [1, 5, 15] | [0, 2, 7, 8] | alpha+, beta-, gamma+ |
| 15 | 2 | [0, 1, 5, 15] | [2, 7, 8] | alpha+, beta-, gamma+ |
| 15 | 3 | [0, 5, 15] | [1, 2, 7, 8] | alpha+, beta-, gamma+ |
| 15 | 4 | [0, 4, 5, 15] | [1, 7, 8] | alpha+, beta-, gamma+ |
| 15 | 5 | [0, 4, 15] | [1, 7, 8] | alpha+, beta- |
| 15 | 6 | [0, 4, 15] | [1, 7, 8] | alpha+, gamma- |
| 16 | 1 | [1, 5, 16] | [0, 2, 8, 9] | alpha+, beta-, gamma+ |
| 16 | 2 | [0, 1, 5, 16] | [2, 8, 9] | alpha+, beta-, gamma+ |
| 16 | 3 | [0, 5, 16] | [1, 2, 8, 9] | alpha+, beta-, gamma+ |
| 16 | 4 | [0, 4, 5, 16] | [1, 8, 9] | alpha+, beta-, gamma+ |
| 16 | 5 | [0, 4, 16] | [1, 8, 9] | alpha+, beta- |
| 16 | 6 | [0, 4, 16] | [1, 8, 9] | alpha+, gamma- |

The exact transitions are:

| \(M\) | Transition | \(\alpha\) |
|---:|---:|---:|
| 15 | 1→2 | 2.690149562520366 |
| 15 | 2→3 | 2.743809471560168 |
| 15 | 3→4 | 2.797082833515613 |
| 15 | 4→5 | 2.951065494237261 |
| 15 | 5→6 | 2.953927379207709 |
| 16 | 1→2 | 2.777320902352483 |
| 16 | 2→3 | 2.813660693978793 |
| 16 | 3→4 | 2.852382622339198 |
| 16 | 4→5 | 2.966259189149633 |
| 16 | 5→6 | 2.967680221680576 |

Every transition is a simple algebraic root, and every adjacent ratio branch
has a finite denominator there.

---

## 7. Exact catalogues

All

\[
84+84=168
\]

integer designs were solved exactly.

| \(M\) | Rank | Design | Ratio | Future risk |
|---:|---:|---:|---:|---:|
| 15 | 1 | (2, 3, 4) | 2.178684776262 | 0.561728737368 |
| 15 | 2 | (2, 3, 5) | 2.275461182874 | 0.593079487780 |
| 15 | 3 | (2, 3, 6) | 2.323561085746 | 0.608168786690 |
| 16 | 1 | (2, 3, 4) | 2.449906308442 | 0.646363288710 |
| 16 | 2 | (2, 3, 5) | 2.600514493848 | 0.689398539376 |
| 16 | 3 | (2, 3, 6) | 2.675675046445 | 0.709951457588 |

For \(M=15\), the unique winner is:

\[
\{2,3,4\}
\]

with future risk:

\[
Q_{15}(2)
=
0.56172873736830370656202807981241442676796484723723.
\]

For \(M=16\), the unique winner is:

\[
\{2,3,4\}
\]

with:

\[
Q_{16}(2)
=
0.64636328870957157684628541353309982775750608761980.
\]

The top three designs at each support have exactly matching primal and dual
values.

---

## 8. Global continuous theorems

For both \(M=15\) and \(M=16\):

\[
D_\alpha=\{\alpha,3,4\},
\qquad
2\le\alpha<3.
\]

The exact minimax ratio is continuous and strictly increasing.

Therefore:

\[
\boxed{
\arg\min_{2\le\alpha<3}
\rho_M(\alpha)
=
\{2\}.
}
\]

The boundary and coalescence risks are:

| \(M\) | \(Q_M(2)\) | \(Q_M(3^-)\) |
|---:|---:|---:|
| 15 | 0.56172873736830370656202807981241442676796484723723 | 1.3119201838558254020097574193852155446415542991235 |
| 16 | 0.64636328870957157684628541353309982775750608761980 | 1.5288619847524960465624386936729386300426111928421 |

The exact global family now covers:

\[
\boxed{
M=5,6,\ldots,16.
}
\]

This remains a finite collection of global phase theorems.

---

## 9. What A75 proves

1. Exact parity-specific Cramer formulas under central-mean normalized noise.
2. Exact finite Bernstein certificates for \(M=10,\ldots,35\).
3. Exact asymptotic determinant bounds for both parities.
4. A complete support-size orientation theorem on \(I\) for every \(M\ge10\).
5. A negative \(\gamma+\) window restricted exactly to \(13\le M\le21\).
6. Positive orientation re-entry for every \(M\ge22\).
7. Exact global first-anchor theorems for \(M=15,16\).
8. Unique exact catalogue winners \(\{2,3,4\}\) for both supports.

---

## 10. What A75 does not prove

The all-\(M\) theorem concerns one declared candidate signature on one fixed
continuous interval.

It does not prove:

1. that the candidate signature is optimal for every \(M\);
2. that \(\gamma+\) is active in the true optimizer for every \(M\ge22\);
3. the same sign pattern outside \(I\);
4. a universal active-set grammar;
5. joint continuous optimization of all anchors.

The distinction between candidate orientation and optimal active-set
selection remains essential.

---

## 11. Next rigorous target

The next question is now sharper.

The candidate \(\gamma+\) multiplier becomes positive again at \(M=22\), but
that does not imply that the optimizer returns to the old \(\gamma+\)
signature.

The next audit should compare, at \(M=21,22,23\):

1. the \(\gamma+\) candidate;
2. the \(\gamma-\) candidate;
3. every declared one-pivot neighbor;
4. the actual globally optimal phase signatures.

The goal is to determine whether the second orientation bifurcation produces
an active-set re-entry or only a locally admissible but globally unused
basis.
