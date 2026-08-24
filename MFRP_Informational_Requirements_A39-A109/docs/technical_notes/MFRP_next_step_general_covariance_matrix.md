# General Covariance Matrix Robust Calibration Theorem

**Programme:** Modal Field Research Programme  
**Provisional audit:** A60  
**Author line:** Felipe Gianini Romero  
**Status:** exact general-covariance theorem inside the A58 certified region; no empirical covariance claim

## Technical abstract

A59 solved the correlated calibration problem for one equicorrelation family.
The present audit removes that symmetry restriction.

Let

\[
u=(u_2,u_\beta,u_\infty)^\top
\]

be the three calibration-error factors for the compactified optimal design

\[
D^\star=\{2,\beta^\star,\infty\}\log2,
\]

with

\[
\beta^\star
=
2.728401216547027876\ldots.
\]

Fix the centre

\[
\bar u=
\begin{pmatrix}
1.05\\
1.05\\
1.05
\end{pmatrix}
\]

and let

\[
\Sigma\succ0
\]

be an arbitrary \(3\times3\) covariance matrix. The uncertainty set is

\[
\mathcal E_\Sigma
=
\left\{
u:
(u-\bar u)^\top
\Sigma^{-1}
(u-\bar u)
\le1
\right\}.
\]

If

\[
\boxed{
\Sigma_{ii}\le0.05^2
\qquad(i=1,2,3),
}
\]

then

\[
\mathcal E_\Sigma\subseteq[1,1.1]^3.
\]

Therefore the exact A58 primal–dual branch remains valid throughout the
ellipsoid.

On that branch,

\[
\rho(u)
=
\frac{n_0+n^\top u}
{d_0+d^\top u},
\]

with positive denominator over the full certified box.

Define

\[
a=N(\bar u)=n_0+n^\top\bar u,
\]

\[
b=D(\bar u)=d_0+d^\top\bar u,
\]

and

\[
v(y)=n-yd.
\]

Then the exact robust ratio is the unique admissible root of

\[
\boxed{
(a-yb)^2
=
v(y)^\top\Sigma v(y),
}
\]

subject to

\[
a-yb\le0.
\]

Expanding gives one quadratic equation,

\[
A_\Sigma y^2+B_\Sigma y+C_\Sigma=0,
\]

where

\[
A_\Sigma
=
b^2-d^\top\Sigma d,
\]

\[
B_\Sigma
=
-2ab+2n^\top\Sigma d,
\]

\[
C_\Sigma
=
a^2-n^\top\Sigma n.
\]

The exact adversarial calibration vector is

\[
\boxed{
u_\Sigma^\star
=
\bar u+
\frac{
\Sigma(n-y_\Sigma^\star d)
}{
\sqrt{
(n-y_\Sigma^\star d)^\top
\Sigma
(n-y_\Sigma^\star d)
}
}.
}
\]

It lies on the ellipsoid boundary and reproduces the robust ratio exactly.

The theorem also establishes monotonicity in the Loewner order:

\[
\boxed{
\Sigma_1\preceq\Sigma_2
\quad\Longrightarrow\quad
\rho_{\Sigma_1}^\star
\le
\rho_{\Sigma_2}^\star.
}
\]

If

\[
(n-y_{\Sigma_1}^\star d)^\top
(\Sigma_2-\Sigma_1)
(n-y_{\Sigma_1}^\star d)>0,
\]

the inequality is strict.

Thus any positive-semidefinite enlargement of the calibration covariance
cannot improve the robust result.

Representative exact-audit matrices give:

| Scenario | Robust future risk | Worst factors \((u_2,u_\beta,u_\infty)\) |
|---|---:|---|
| Unequal independent scales | 0.00988898768357363 | (1.089555, 1.074333, 1.051283) |
| Unequal positive correlations | 0.00991524824786416 | (1.094924, 1.083078, 1.056072) |
| Mixed correlations | 0.00987436091686483 | (1.086353, 1.069169, 1.051055) |
| Loewner-small covariance | 0.00984508170687792 | (1.073341, 1.065581, 1.051183) |
| Loewner-large covariance | 0.00987091252355004 | (1.080701, 1.071627, 1.057729) |

The last two matrices satisfy

\[
\Sigma_{\rm large}
=
\Sigma_{\rm small}
+
ww^\top,
\]

so

\[
\Sigma_{\rm small}\preceq\Sigma_{\rm large}.
\]

The exact risks obey the predicted strict ordering.

A reusable covariance input template is supplied with the audit. It accepts
a centre and a symmetric covariance matrix, checks positive definiteness and
box containment, and evaluates the exact robust root and worst direction.

---

## 1. General covariance contract

The ellipsoid is

\[
\mathcal E_\Sigma
=
\left\{
\bar u+\Sigma^{1/2}z:
\|z\|_2\le1
\right\}.
\]

The maximum deviation of coordinate \(i\) is

\[
\max_{u\in\mathcal E_\Sigma}
|u_i-\bar u_i|
=
\sqrt{\Sigma_{ii}}.
\]

Therefore the diagonal condition

\[
\Sigma_{ii}\le\frac1{400}
\]

is sufficient and necessary for coordinatewise containment around the centre
\(1.05\):

\[
1\le u_i\le1.1.
\]

No restriction to equal marginal variances or equal pairwise correlations is
required.

---

## 2. Exact robust reduction

For any candidate ratio \(y\),

\[
\rho(u)\le y
\]

is equivalent to

\[
N(u)-yD(u)\le0.
\]

The maximum of the affine functional over the ellipsoid is

\[
a-yb+
\sqrt{
v(y)^\top\Sigma v(y)
}.
\]

Hence the robust ratio is the unique zero of

\[
F_\Sigma(y)
=
a-yb+
\sqrt{
v(y)^\top\Sigma v(y)
}.
\]

Since

\[
D(u)>0
\]

throughout the ellipsoid,

\[
F_\Sigma(y)
=
\max_{u\in\mathcal E_\Sigma}
[N(u)-yD(u)]
\]

is strictly decreasing in \(y\). This establishes uniqueness before the
equation is squared.

---

## 3. Quadratic coefficients

Squaring the admissible branch gives

\[
(a-yb)^2
=
(n-yd)^\top\Sigma(n-yd).
\]

Collecting powers of \(y\):

\[
\begin{aligned}
0={}&
\left(
b^2-d^\top\Sigma d
\right)y^2\\
&+
\left(
-2ab+2n^\top\Sigma d
\right)y\\
&+
\left(
a^2-n^\top\Sigma n
\right).
\end{aligned}
\]

Only the root satisfying

\[
a-yb\le0
\]

and the unsquared support equation is retained.

This provides an exact algebraic solution for any supplied covariance matrix.

---

## 4. Exact worst direction

At the robust root, the support-maximizing direction is

\[
u^\star-\bar u
=
\frac{
\Sigma v(y^\star)
}{
\sqrt{
v(y^\star)^\top
\Sigma v(y^\star)
}
}.
\]

It satisfies

\[
(u^\star-\bar u)^\top
\Sigma^{-1}
(u^\star-\bar u)
=
1.
\]

Substitution into the linear-fractional ratio gives exactly

\[
\rho(u^\star)=y^\star.
\]

Therefore the theorem supplies both:

- the worst robust value;
- the concrete joint calibration pattern that realizes it.

---

## 5. Loewner monotonicity

Suppose

\[
\Sigma_1\preceq\Sigma_2.
\]

Then for every vector \(v\),

\[
v^\top\Sigma_1v
\le
v^\top\Sigma_2v.
\]

Therefore

\[
F_{\Sigma_1}(y)
\le
F_{\Sigma_2}(y)
\]

for every \(y\).

Both functions are strictly decreasing. Their unique zeros consequently obey

\[
y_{\Sigma_1}^\star
\le
y_{\Sigma_2}^\star.
\]

This is a matrix-level robust-information ordering: enlarging uncertainty in
any positive-semidefinite direction cannot lower the worst-case ratio.

---

## 6. Unequal marginal scales

The diagonal example uses standard deviations

\[
(0.05,0.04,0.02).
\]

Thus

\[
\Sigma_{\rm diag}
=
\operatorname{diag}
\left(
\frac1{400},
\frac1{625},
\frac1{2500}
\right).
\]

The worst direction allocates most of the uncertainty budget to the first
channel, then the interior channel, and very little to the extreme channel.

This agrees with the A58 sensitivity hierarchy, but now includes unequal
marginal scales exactly rather than through a local gradient only.

---

## 7. Pair-specific correlations

The positive-correlation example is

\[
\Sigma_{+}
=
\begin{pmatrix}
1/400&1/1000&1/5000\\
1/1000&1/625&1/5000\\
1/5000&1/5000&1/2500
\end{pmatrix}.
\]

The mixed-correlation example is

\[
\Sigma_{\rm mix}
=
\begin{pmatrix}
1/400&-1/2000&-1/10000\\
-1/2000&1/625&1/12500\\
-1/10000&1/12500&1/2500
\end{pmatrix}.
\]

Both are positive definite and share the same marginal scales.

The positively correlated matrix has the larger robust risk because it aligns
the two sensitive lower channels more strongly in a common adverse direction.

This comparison is example-specific. The general ordering theorem is the
Loewner theorem, not a claim that every matrix with more positive entries is
larger in Loewner order.

---

## 8. Covariance contribution diagnostic

At the ellipsoid centre, let

\[
g=\nabla Q(\bar u).
\]

The local robust variance is

\[
g^\top\Sigma g
=
\sum_i g_i^2\Sigma_{ii}
+
2\sum_{i<j}g_ig_j\Sigma_{ij}.
\]

The audit reports separately:

- three marginal contributions;
- three pairwise covariance contributions;
- the total local robust variance.

This identifies which variance or covariance entry is driving the robust
uncertainty.

Negative pairwise contributions can reduce the local total, while positive
common-mode contributions amplify it.

---

## 9. Reusable experimental interface

The supplied template uses the structure:

```json
{
  "centre": [1.05, 1.05, 1.05],
  "covariance": [
    [0.0025, 0.0010, 0.0002],
    [0.0010, 0.0016, 0.0002],
    [0.0002, 0.0002, 0.0004]
  ]
}
```

Before evaluation, the audit checks:

1. symmetry;
2. positive definiteness;
3. diagonal containment in the A58 box;
4. positivity of the ratio denominator;
5. admissibility of the selected quadratic root;
6. ellipsoid-boundary reproduction;
7. containment of the worst vector.

This is the first point in the sequence where a covariance matrix estimated
from repeated calibration data can be inserted directly into the robust
mathematical machinery.

---

## 10. Logical status

### Established

1. The exact robust solution holds for every positive-definite covariance
   matrix whose ellipsoid stays inside the A58 box.
2. Marginal scales and pairwise correlations may all differ.
3. The robust ratio is the admissible root of one quadratic.
4. The exact worst calibration vector is supplied.
5. Robust risk is monotone in the Loewner order.
6. Unequal-scale and pair-specific-correlation examples pass all KKT and
   containment checks.
7. A covariance-contribution diagnostic is supplied.
8. A machine-readable covariance input template is supplied.

### Not established

1. No covariance matrix has yet been estimated from real calibration data.
2. The ellipsoid centre remains fixed at \(u=(1.05,1.05,1.05)\).
3. Ellipsoids extending outside \([1,1.1]^3\) are not covered.
4. The anchor \(\beta^\star\) is not reoptimized for each covariance matrix.
5. Covariance-estimation uncertainty is not included.
6. Heavy-tailed or non-elliptical errors are not modelled.

---

## 11. Next rigorous target

The general covariance theorem is now closed.

The next bridge to data is covariance estimation uncertainty. Instead of
treating \(\Sigma\) as known exactly, the model should accept a confidence set

\[
\Sigma\in\mathcal S
\]

and solve

\[
\max_{\Sigma\in\mathcal S}
\rho_\Sigma^\star.
\]

A first controlled version can use spectral uncertainty,

\[
\Sigma
=
\widehat\Sigma+\Delta,
\qquad
0\preceq\Delta\preceq\tau I,
\]

which is directly compatible with the Loewner monotonicity theorem.
