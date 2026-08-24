# Signed q-Schur Decomposition and Arithmetic-Grid Dominance

**Programme:** Modal Field Research Programme  
**Provisional audit:** A70  
**Author line:** Felipe Gianini Romero  
**Status:** exact signed-minor decomposition and finite-family arithmetic-grid dominance theorem; no arbitrary-\(M\) induction theorem

## Technical abstract

A69 proved that, for each fixed active basis,

\[
\lambda_\alpha^+
=
\frac{\Delta_\alpha(\varepsilon)}
{\Delta(s,\varepsilon)},
\]

where the Cramer numerator \(\Delta_\alpha\) is independent of the continuous
first-anchor coordinate

\[
s=2^{-\alpha}
\]

and is at most affine in the tolerance.

The remaining target was to exploit the arithmetic microscopic grid

\[
x=0,1,\ldots,M.
\]

A70 expands every one of the 33 A67 Cramer numerators by a generalized
Laplace decomposition across:

1. the active \(P\)-columns;
2. the active \(Q\)-columns;
3. the Charnes–Cooper scale column.

Every nonzero term has the form

\[
\boxed{
T_\pi
=
\sigma_\pi\,
c_\pi(\varepsilon)\,
V_{P,\pi}\,
V_{Q,\pi},
}
\]

where:

- \(\sigma_\pi\in\{-1,+1\}\) is a row-partition orientation;
- \(c_\pi\) is one of the scale-column coefficients;
- \(V_{P,\pi}\) and \(V_{Q,\pi}\) are ordinary or first-confluent generalized
  \(q\)-Vandermonde minors.

For ordinary minors, let

\[
0<z_1<\cdots<z_r
\]

be the selected exponential nodes and

\[
0\le x_1<\cdots<x_r
\]

the selected arithmetic contact points. Then

\[
\det(z_j^{x_i})
=
V(z_1,\ldots,z_r)
s_\nu(z_1,\ldots,z_r),
\]

where

\[
V(z_1,\ldots,z_r)
=
\prod_{i<j}(z_j-z_i)>0
\]

and \(s_\nu\) is a Schur polynomial with nonnegative coefficients.

Thus every ordinary canonical minor has a positive Schur quotient.

The rows \(1\) and \(x\) correspond to a node at \(z=1\) and its first
confluent derivative. A70 audits the canonical orientation of every
norm–mean confluent minor and every derivative-only minor appearing in the
A67 family.

The exact counts are:

\[
\boxed{
84\text{ ordinary }q\text{-Schur minors},
}
\]

\[
\boxed{
270\text{ norm–mean confluent minors},
}
\]

and

\[
\boxed{
84\text{ derivative-only minors}.
}
\]

All 438 minor orientations agree with the canonical ordered-\(q\)
prediction. Including the complete term orientations gives 657 exact sign
checks.

However, the expected simple result does not occur:

\[
\boxed{
\text{none of the 33 Cramer expansions is termwise sign-coherent.}
}
\]

Every numerator contains both positive and negative terms.

Therefore Schur positivity does not prove the final sign by itself. The
arithmetic-grid result is a dominance theorem:

\[
\boxed{
\sum_{\operatorname{sgn}T_\pi=\operatorname{sgn}\Delta_\alpha}
|T_\pi|
>
\sum_{\operatorname{sgn}T_\pi=-\operatorname{sgn}\Delta_\alpha}
|T_\pi|.
}
\]

This inequality holds exactly in all 33 phases.

The smallest dominance ratio is

\[
\boxed{
\frac{
834925121797410
}{
824381054550353
}
=
1.0127902833148053\ldots
}
\]

and occurs at

\[
\boxed{
M=9,\qquad\text{phase }7.
}
\]

Thus the weakest certified surplus is only

\[
\boxed{
1.27902833148\%.
}
\]

The result is rigorous but also exposes the next difficulty: an arbitrary
support-size theorem cannot follow merely from positivity of the individual
Schur factors. It must establish a uniform inequality comparing two sums of
positive \(q\)-Schur/confluent terms.

---

## 1. Block-Laplace theorem

Let the Cramer numerator matrix have columns partitioned into:

\[
C_P,\qquad C_Q,\qquad C_t,
\]

with sizes

\[
p,\qquad q,\qquad1.
\]

For every partition of the active rows into:

\[
I,\qquad J,\qquad\{k\},
\]

with

\[
|I|=p,
\qquad
|J|=q,
\]

the generalized Laplace formula gives

\[
\Delta_\alpha
=
\sum_{I,J,k}
(-1)^{\pi(I,J,k)}
\det B[I,C_P]\,
\det B[J,C_Q]\,
B[k,C_t].
\]

Every term was reconstructed independently and the exact sum was compared
with the direct symbolic determinant.

Result:

\[
\boxed{
33/33\text{ exact decompositions}.
}
\]

The number of nonzero terms per phase is:

| Nonzero terms | Phases |
|---:|---:|
| 2 | 3 |
| 5 | 9 |
| 8 | 21 |

---

## 2. Ordinary q-Schur minors

For increasing integer contacts

\[
x_1<\cdots<x_r
\]

and increasing nodes

\[
z_1<\cdots<z_r,
\]

define the partition

\[
\nu_i
=
x_{r-i+1}-(r-i).
\]

Then:

\[
\det(z_j^{x_i})
=
V(z)s_\nu(z).
\]

In the declared family, the possible nodes are selected from:

\[
2^{-\gamma_M},
\qquad
2^{-3},
\qquad
2^{-1},
\qquad
1.
\]

Every exact quotient

\[
\frac{
\det(z_j^{x_i})
}{
V(z)
}
\]

was positive.

Result:

\[
\boxed{
84/84\text{ positive ordinary Schur quotients}.
}
\]

---

## 3. Confluent minors

The normalization and mean rows are:

\[
1
\]

and:

\[
x
=
\left.
\frac{\partial}{\partial z}
z^x
\right|_{z=1}.
\]

When both appear, the minor is a first-confluent generalized Vandermonde
minor at \(z=1\).

Some Laplace terms contain the derivative row without the normalization row.
Those are recorded separately as derivative-only minors.

The audit places the exponential rows in the canonical node order:

\[
2^{-\gamma_M}
<
2^{-3}
<
2^{-1}
<
1,
\]

with the normalization row before the derivative row at the confluent node.

After accounting for:

- row coefficients;
- active-band signs;
- the row permutation to canonical order;

all exact determinants possess the predicted orientation.

Result:

\[
\boxed{
354/354\text{ confluent or derivative minor orientations matched}.
}
\]

This is an exact result for the minors occurring in A67. It is not presented
as a theorem for arbitrary derivative-only contact configurations.

---

## 4. Why positivity alone fails

After converting each minor to its canonical positive magnitude, a complete
term becomes:

\[
T_\pi
=
\eta_\pi
|c_\pi|
|V_{P,\pi}|
|V_{Q,\pi}|,
\qquad
\eta_\pi\in\{-1,+1\}.
\]

If every \(\eta_\pi\) were equal, the sign theorem would be immediate.

Instead:

\[
\boxed{
\text{all 33 phases contain both signs.}
}
\]

The determinant orientation is produced by cancellation between positive
minor products.

This strengthens the obstruction found in A69. Even after imposing the
arithmetic grid and factoring every ordinary minor into positive Schur
pieces, the full coupled determinant remains a signed sum.

---

## 5. Exact dominance certificate

Let:

\[
\Sigma_{\rm aligned}
=
\sum_{\operatorname{sgn}T_\pi
=\operatorname{sgn}\Delta_\alpha}
|T_\pi|,
\]

and:

\[
\Sigma_{\rm opposing}
=
\sum_{\operatorname{sgn}T_\pi
=-\operatorname{sgn}\Delta_\alpha}
|T_\pi|.
\]

Define:

\[
D
=
\frac{
\Sigma_{\rm aligned}
}{
\Sigma_{\rm opposing}
}.
\]

Then:

\[
\operatorname{sgn}\Delta_\alpha
\]

is certified whenever:

\[
D>1.
\]

A70 computes both sums as exact rational numbers.

Result:

\[
\boxed{
D>1
\quad\text{in }33/33\text{ phases}.
}
\]

No floating-point comparison is used to decide this inequality.

---

## 6. Weakest phase

The smallest margin occurs for:

\[
M=9,
\qquad
\text{phase }7.
\]

The active supports are:

\[
P=\{0,2,3,9\},
\]

\[
Q=\{1,4,5\},
\]

with active bands:

\[
\alpha+,\qquad
\beta-,\qquad
\gamma-.
\]

The expansion has eight terms:

\[
4\text{ positive},
\qquad
4\text{ negative}.
\]

The final numerator orientation is negative.

The aligned magnitude is:

\[
\Sigma_{\rm aligned}
=
\frac{
36820197871265781
}{
1801439850948198400
},
\]

while the opposing magnitude is:

\[
\Sigma_{\rm opposing}
=
\frac{
363552045056705673
}{
18014398509481984000
}.
\]

Their ratio is:

\[
\boxed{
D
=
\frac{
834925121797410
}{
824381054550353
}.
}
\]

This is a genuine narrow dominance margin. Any future uniform theorem must
control cases at least this close to cancellation.

---

## 7. Complete phase table

| \(M\) | Phase | Terms | Positive | Negative | Final sign | Dominance ratio |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 1 | 8 | 5 | 3 | +1 | 1.240658221679 |
| 5 | 2 | 8 | 5 | 3 | +1 | 1.562780926625 |
| 5 | 3 | 8 | 5 | 3 | +1 | 2.126182104477 |
| 5 | 4 | 8 | 5 | 3 | +1 | 1.054028206269 |
| 5 | 5 | 2 | 1 | 1 | -1 | 1.466666666667 |
| 5 | 6 | 5 | 2 | 3 | -1 | 1.333256932742 |
| 5 | 7 | 5 | 2 | 3 | -1 | 1.465554819670 |
| 6 | 1 | 2 | 1 | 1 | +1 | 1.555555555556 |
| 6 | 2 | 8 | 5 | 3 | +1 | 1.201682750780 |
| 6 | 3 | 8 | 5 | 3 | +1 | 1.403846679550 |
| 6 | 4 | 8 | 5 | 3 | +1 | 1.196349918838 |
| 6 | 5 | 5 | 2 | 3 | +1 | 1.561161404520 |
| 6 | 6 | 5 | 2 | 3 | +1 | 1.904968045092 |
| 7 | 1 | 8 | 5 | 3 | -1 | 1.075565268441 |
| 7 | 2 | 2 | 1 | 1 | +1 | 1.333333333333 |
| 7 | 3 | 8 | 5 | 3 | +1 | 1.063984302016 |
| 7 | 4 | 8 | 5 | 3 | +1 | 1.069140264304 |
| 7 | 5 | 5 | 2 | 3 | +1 | 1.546785895088 |
| 7 | 6 | 5 | 2 | 3 | +1 | 1.735815014301 |
| 8 | 1 | 8 | 5 | 3 | -1 | 1.152589620173 |
| 8 | 2 | 8 | 5 | 3 | -1 | 1.333656283924 |
| 8 | 3 | 8 | 5 | 3 | +1 | 1.183701095320 |
| 8 | 4 | 8 | 5 | 3 | +1 | 1.037524613017 |
| 8 | 5 | 8 | 4 | 4 | -1 | 1.036173947794 |
| 8 | 6 | 5 | 2 | 3 | +1 | 1.856263096267 |
| 9 | 1 | 8 | 5 | 3 | -1 | 1.194674093564 |
| 9 | 2 | 8 | 5 | 3 | -1 | 1.061346711863 |
| 9 | 3 | 8 | 5 | 3 | -1 | 1.159190950307 |
| 9 | 4 | 8 | 5 | 3 | -1 | 1.332347956590 |
| 9 | 5 | 8 | 5 | 3 | +1 | 1.178892530597 |
| 9 | 6 | 5 | 2 | 3 | +1 | 1.545178925304 |
| 9 | 7 | 8 | 4 | 4 | -1 | 1.012790283315 |
| 9 | 8 | 5 | 2 | 3 | +1 | 1.850150265572 |

---

## 8. What A70 proves

### Exact general decomposition

Each fixed-basis numerator is a signed sum of products of \(P\)- and
\(Q\)-side generalized \(q\)-Vandermonde minors and one scale coefficient.

### Exact arithmetic-grid family result

For the 33 A67 phases:

1. every decomposition reproduces the exact numerator;
2. every ordinary Schur quotient is positive;
3. every confluent/derivative orientation is correct;
4. every complete term sign is predicted correctly;
5. every expansion is mixed-sign;
6. the terms aligned with the final orientation dominate exactly.

### Negative structural result

The desired sign cannot be obtained from:

\[
\text{“all Schur factors are positive”}
\]

alone.

The missing theorem is an inequality between sums of positive
Schur/confluent products.

---

## 9. Logical status

### Established

1. Thirty-three exact block-Laplace expansions.
2. Six hundred and fifty-seven exact orientation checks.
3. Eighty-four positive ordinary Schur quotients.
4. Three hundred and fifty-four certified confluent/derivative orientations.
5. Mixed-sign cancellation in every phase.
6. Exact dominance in every phase.
7. A quantified weakest dominance margin.

### Not established

1. A lower bound on \(D-1\) uniform in arbitrary \(M\).
2. An induction showing dominance for all central supports.
3. A closed formula for the signed Schur sums.
4. Arbitrary means or targets.
5. Arbitrary derivative-only contact patterns.
6. Jointly changing completion anchors.

---

## 10. Next rigorous target

The next step should focus on the signed sums rather than on the individual
minors.

A practical route is to search for a recurrence in support size:

\[
\Delta_{\alpha,M+1}
=
A_M\Delta_{\alpha,M}
+
R_M,
\]

or a condensation identity of Desnanot–Jacobi/Dodgson type relating nearby
contact minors.

The target would be:

1. pair or group opposing terms with aligned terms;
2. express each difference as a positive \(q\)-Schur combination;
3. derive a recurrence or injection between term families;
4. prove a lower dominance bound for the central arithmetic grid.

The very small \(M=9\), phase-7 margin shows that such a theorem must be
quantitative rather than purely orientational.
