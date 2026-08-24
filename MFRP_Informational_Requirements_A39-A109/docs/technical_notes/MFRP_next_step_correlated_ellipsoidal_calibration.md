# Correlated Ellipsoidal Calibration Uncertainty

**Programme:** Modal Field Research Programme  
**Provisional audit:** A59  
**Author line:** Felipe Gianini Romero  
**Status:** exact nonlinear ellipsoidal robust theorem inside the A58 certified box; no empirical covariance claim

## Technical abstract

A58 allowed the three channel-error factors to vary independently in the box

\[
1\le u_2,u_\beta,u_\infty\le1.1
\]

for the compactified design

\[
D^\star=\{2,\beta^\star,\infty\}\log2.
\]

The present audit replaces that independent box by a correlated ellipsoid.

Let

\[
\bar u=
\begin{pmatrix}
1.05\\
1.05\\
1.05
\end{pmatrix},
\qquad
h=0.05,
\]

and define the equicorrelation matrix

\[
R_\varrho
=
\begin{pmatrix}
1&\varrho&\varrho\\
\varrho&1&\varrho\\
\varrho&\varrho&1
\end{pmatrix},
\qquad
-\frac12<\varrho<1.
\]

The correlated calibration set is

\[
\mathcal E_\varrho
=
\left\{
u:
(u-\bar u)^\top
R_\varrho^{-1}
(u-\bar u)
\le h^2
\right\}.
\]

Because each diagonal entry of \(R_\varrho\) is one, every point in this
ellipsoid satisfies

\[
|u_i-1.05|\le0.05.
\]

Therefore

\[
\mathcal E_\varrho
\subseteq
[1,1.1]^3,
\]

so the exact A58 primal–dual branch remains valid throughout every ellipsoid.

On this branch, the minimax ratio is exactly linear-fractional:

\[
\rho(u)
=
\frac{n_0+n^\top u}
{d_0+d^\top u},
\]

with strictly positive denominator and

\[
\frac{\partial\rho}{\partial u_i}>0
\]

throughout the certified box.

For a candidate ratio \(y\), define

\[
v(y)=n-yd,
\]

\[
F_\varrho(y)
=
N(\bar u)
-yD(\bar u)
+h
\sqrt{
v(y)^\top
R_\varrho
v(y)
}.
\]

The exact robust ratio over the ellipsoid is the unique root

\[
\boxed{
F_\varrho(y_\varrho^\star)=0.
}
\]

Equivalently, \(y_\varrho^\star\) is the admissible root of the quadratic
equation

\[
\boxed{
\left[
N(\bar u)-yD(\bar u)
\right]^2
=
h^2
(n-yd)^\top
R_\varrho
(n-yd),
}
\]

with the branch condition

\[
N(\bar u)-yD(\bar u)\le0.
\]

The exact worst-case error vector is

\[
\boxed{
u_\varrho^\star
=
\bar u+
h
\frac{
R_\varrho v(y_\varrho^\star)
}{
\sqrt{
v(y_\varrho^\star)^\top
R_\varrho
v(y_\varrho^\star)
}
}.
}
\]

This is a complete nonlinear solution, not a first-order approximation.

The robust ratio and risk increase strictly with the common correlation
parameter \(\varrho\). Positive common-mode correlation allows the three
harmful error directions to move together; anticorrelation forces tradeoffs
between them.

Representative exact algebraic evaluations are:

| Correlation \(\varrho\) | Robust future risk | Excess over ellipsoid centre | Worst error factors \((u_2,u_\beta,u_\infty)\) |
|---:|---:|---:|---|
| \(-0.4\) | 0.00985985570569086 | \(8.34985\times10^{-5}\) | (1.078516, 1.075621, 1.018957) |
| \(0\) | 0.00990125074489123 | \(1.24894\times10^{-4}\) | (1.085669, 1.084284, 1.057230) |
| \(0.5\) | 0.00993875897944824 | \(1.62402\times10^{-4}\) | (1.093387, 1.092853, 1.082452) |
| \(0.9\) | 0.00996341527592995 | \(1.87058\times10^{-4}\) | (1.098746, 1.098654, 1.096848) |

The centre risk is

\[
Q(\bar u)
=
0.00977635717857709\ldots.
\]

For comparison, the independent-box worst corner from A58 is

\[
Q(1.1,1.1,1.1)
=
0.00996908574327555\ldots.
\]

Even the highly correlated ellipsoid with \(\varrho=0.9\) remains below the
box worst case, because the box permits simultaneous full deterioration in
all coordinates while the ellipsoid imposes a joint radius.

The exact nonlinear excess is extremely close to the local ellipsoidal
support prediction

\[
h\sqrt{
\nabla Q(\bar u)^\top
R_\varrho
\nabla Q(\bar u)
}.
\]

Across the four representative correlations, the relative discrepancy is
below \(0.1\%\). This validates the A58 gradient as an excellent local summary,
while A59 supplies the exact nonlinear answer.

---

## 1. Correlated uncertainty contract

The three factors are

\[
u=
(u_2,u_\beta,u_\infty)^\top.
\]

The ellipsoid is centered at a nominal 5% deterioration:

\[
\bar u=(1.05,1.05,1.05)^\top.
\]

Its marginal radius is 5%, so every coordinate remains in the A58-certified
interval \([1,1.1]\).

The equicorrelation parameter satisfies

\[
-\frac12<\varrho<1,
\]

which is exactly the positive-definiteness domain of \(R_\varrho\).

The cases have direct interpretations:

- \(\varrho=0\): uncorrelated ellipsoidal calibration uncertainty;
- \(\varrho>0\): common-mode deterioration;
- \(\varrho<0\): tradeoff or anti-correlated calibration error.

---

## 2. Exact linear-fractional reduction

The A58 ratio can be written as

\[
\rho(u)
=
\frac{N(u)}{D(u)}
=
\frac{n_0+n^\top u}
{d_0+d^\top u}.
\]

The denominator is positive on the complete box.

For any \(y\),

\[
\rho(u)\le y
\]

is equivalent to

\[
N(u)-yD(u)\le0.
\]

The maximum of this affine expression over the ellipsoid is the support
function

\[
N(\bar u)-yD(\bar u)
+
h
\sqrt{
(n-yd)^\top
R_\varrho
(n-yd)
}.
\]

Therefore the smallest valid upper ratio is the unique zero of
\(F_\varrho(y)\).

This converts the nonlinear robust problem into one algebraic quadratic.

---

## 3. Worst-case direction

At the robust root, the maximizing ellipsoid direction is

\[
z^\star
=
\frac{
R_\varrho(n-y^\star d)
}{
\sqrt{
(n-y^\star d)^\top
R_\varrho
(n-y^\star d)
}
}.
\]

It satisfies exactly

\[
(z^\star)^\top
R_\varrho^{-1}
z^\star=1.
\]

Thus

\[
u^\star=\bar u+hz^\star
\]

lies on the ellipsoid boundary.

Substituting \(u^\star\) into the A58 ratio reproduces
\(y_\varrho^\star\).

---

## 4. Correlation monotonicity theorem

For every ratio attained in the certified box,

\[
n_i-y d_i>0.
\]

This follows from

\[
\partial_{u_i}\rho
=
\frac{n_i-y d_i}{D(u)}
>0.
\]

Hence every component of \(v(y)\) is positive.

For equicorrelation,

\[
v^\top R_\varrho v
=
\sum_i v_i^2
+
2\varrho
\sum_{i<j}v_iv_j.
\]

Because all pair products are positive, the ellipsoidal support term strictly
increases with \(\varrho\).

Also,

\[
F_\varrho(y)
=
\max_{u\in\mathcal E_\varrho}
[N(u)-yD(u)]
\]

is strictly decreasing in \(y\), because \(D(u)>0\).

Therefore:

### Theorem 4.1

\[
\boxed{
\varrho_1<\varrho_2
\quad\Longrightarrow\quad
y_{\varrho_1}^\star
<
y_{\varrho_2}^\star.
}
\]

The same strict ordering holds for the future-score risk.

---

## 5. Local correlation geometry

At the ellipsoid centre, let

\[
g=\nabla Q(\bar u).
\]

The first-order worst-case excess is

\[
\Delta Q_{\mathrm{lin}}(\varrho)
=
h\sqrt{
g^\top R_\varrho g
}.
\]

Since all components of \(g\) are positive,

\[
g^\top R_\varrho g
=
\sum_i g_i^2
+
2\varrho
\sum_{i<j}g_ig_j
\]

is strictly increasing in correlation.

This is the local counterpart of the exact nonlinear monotonicity theorem.

---

## 6. Exact nonlinear versus first-order prediction

The first-order formula slightly overestimates the exact nonlinear excess in
the representative cases:

| \(\varrho\) | Exact excess | Linear prediction | Relative discrepancy |
|---:|---:|---:|---:|
| \(-0.4\) | \(8.34985\times10^{-5}\) | \(8.35270\times10^{-5}\) | 0.0341% |
| \(0\) | \(1.24894\times10^{-4}\) | \(1.24969\times10^{-4}\) | 0.0601% |
| \(0.5\) | \(1.62402\times10^{-4}\) | \(1.62535\times10^{-4}\) | 0.0821% |
| \(0.9\) | \(1.87058\times10^{-4}\) | \(1.87238\times10^{-4}\) | 0.0962% |

The A58 gradient is therefore highly accurate for calibration planning at
this uncertainty scale, while the algebraic root should be used when an exact
nonlinear robust value is required.

---

## 7. Interpretation

Correlation changes the shape of the set of jointly plausible calibration
errors.

With positive correlation, the sensitive lower channels can deteriorate
together. The worst direction approaches the common-mode corner.

With negative correlation, making one sensitive channel worse forces another
channel to improve or deteriorate less. The resulting worst-case risk is
smaller even though each channel has the same marginal uncertainty.

Therefore marginal error bars alone are insufficient. Two instruments with
the same per-channel precision can have different robust risks because their
errors co-move differently.

---

## 8. Logical status

### Established

1. Every correlation ellipsoid lies inside the exact A58 box.
2. The full nonlinear robust maximum reduces to a quadratic algebraic root.
3. The exact worst-case direction is supplied.
4. Robust risk increases strictly with equicorrelation.
5. Common-mode correlation is more adversarial than independent error.
6. Anticorrelation reduces the robust worst case.
7. The A58 gradient accurately approximates the exact robust excess at the
   certified scale.
8. The independent-box worst case remains an upper bound for every contained
   ellipsoid.

### Not established

1. The equicorrelation family does not represent every covariance matrix.
2. The ellipsoid is centered at \(u=(1.05,1.05,1.05)\), not at the A54
   baseline corner.
3. Larger marginal radii are not certified.
4. The anchor \(\beta^\star\) is not reoptimized under covariance.
5. No empirical covariance matrix is supplied.
6. Correlation between raw measurement residuals and calibration-factor
   uncertainty is not identified.

---

## 9. Next rigorous target

The equicorrelation theorem is now closed.

The next extension should accept a general positive-definite covariance matrix

\[
\Sigma
\]

with unequal marginal scales. The same support-function reduction remains
valid:

\[
F_\Sigma(y)
=
N(\bar u)-yD(\bar u)
+
\sqrt{
(n-yd)^\top
\Sigma
(n-yd)
}.
\]

That will permit direct insertion of a covariance matrix estimated from
repeated experimental calibration runs.
