# Target-Exclusion Distance Law

**Programme:** Modal Field Research Programme  
**Provisional audit:** A51  
**Author line:** Felipe Gianini Romero  
**Status:** rigorous continuation of MFRP-TR-2026-01 and A39–A50; no physical design claim

## Technical abstract

A48 established that permitting direct observation of the target parameter
\(\log2\) changes the problem from prediction to measurement. A50 then proved
that, under the fixed exclusion domain \(2\le\alpha\le3\), the best first
anchor is the lower boundary \(\alpha=2\).

The present audit promotes the exclusion distance itself to an explicit
parameter:

\[
\Delta>0,
\qquad
1+\Delta\le\alpha\le3.
\]

Two controlled design contracts are retained.

For exact data,

\[
D_0(\alpha)=\{\alpha,3,4\}\log2.
\]

For common absolute tolerance

\[
\varepsilon=10^{-4},
\]

\[
D_\varepsilon(\alpha)
=
\{\alpha,3,\infty\}\log2.
\]

The finite-support and mean contracts remain

\[
\operatorname{supp}P\subseteq\{0,1,2,3,4,5\},
\qquad
\mathbb E[X]=\frac52.
\]

Set

\[
s=2^{-\alpha}.
\]

The exact-data minimax ratio for every distinct
\(\alpha\in(1,3)\) is

\[
\rho_0(\alpha)
=
\frac{5(392s+779)}
{2(1043s+1916)}.
\]

It is strictly increasing in \(\alpha\). Therefore, for every

\[
0<\Delta<2,
\]

the unique minimizer is

\[
\boxed{
\alpha_0^\star(\Delta)=1+\Delta.
}
\]

Equivalently,

\[
\boxed{
\rho_0^\star(\Delta)
=
\frac{
5\left(392\,2^{-(1+\Delta)}+779\right)
}{
2\left(1043\,2^{-(1+\Delta)}+1916\right)
}.
}
\]

As \(\Delta\downarrow0\),

\[
\rho_0^\star(\Delta)
=
1+
\frac{21\log2}{1625}\Delta
+
O(\Delta^2),
\]

and the future-score risk satisfies

\[
\boxed{
\mathcal R_0^{Q,\star}(\Delta)
=
\frac{21}{3250}\Delta
+
O(\Delta^2).
}
\]

Thus exact predictive uncertainty vanishes linearly as the permitted anchor
approaches the target.

At \(\Delta=2\), the admissible interval collapses to the duplicated design
\(\alpha=3\). The actual exact ratio is

\[
\frac{3871}{3484},
\]

rather than the distinct-anchor limit

\[
\frac{1840}{1819}.
\]

This is the exact coalescence singularity already identified in A44 and A50.

For the positive-noise contract, the whole interval

\[
1\le\alpha\le3
\]

is covered by fourteen exact primal–dual phases separated by thirteen
algebraic transition points. Every phase has strictly increasing risk in
\(\alpha\), and adjacent ratios agree exactly on their transition boundaries.
Consequently, for every

\[
0<\Delta\le2,
\]

\[
\boxed{
\alpha_{10^{-4}}^\star(\Delta)=1+\Delta.
}
\]

Near the direct-measurement boundary,

\[
\rho_{10^{-4}}^\star(\Delta)
=
\frac{1877}{1875}
+
\frac{2\log2}{9375}\Delta
+
O(\Delta^2),
\]

so

\[
\boxed{
\mathcal R_{10^{-4}}^{Q,\star}(\Delta)
=
\frac12\log_2\frac{1877}{1875}
+
\frac{\Delta}{9385}
+
O(\Delta^2).
}
\]

The constant term is precisely the direct-target uncertainty proved in A48.
Hence the target-excluding predictive programme connects continuously to
direct noisy measurement as \(\Delta\downarrow0\).

The main conclusion is a boundary law, not a physical constant:

\[
\boxed{
\text{for a declared target-exclusion distance }\Delta,
\text{ the optimal first anchor is the closest permitted point.}
}
\]

---

## 1. Information contract

The target is

\[
L_P(\log2).
\]

The first observed exponent is constrained by

\[
\alpha\ge1+\Delta.
\]

The upper endpoint \(3\) is retained to avoid changing the other controlled
anchors in A50.

The direct future-score width is

\[
\mathcal R^Q
=
\frac12\log_2\rho,
\]

where \(\rho\) is the worst compatible transform ratio.

The exclusion distance is part of the question. It separates:

- direct target measurement, \(\Delta=0\);
- prediction from an omitted target, \(\Delta>0\).

---

## 2. Exact-data exclusion law

For distinct \(\alpha\in(1,3)\),

\[
\rho_0(\alpha)
=
\frac{5(392s+779)}
{2(1043s+1916)},
\qquad
s=2^{-\alpha}.
\]

Differentiating,

\[
\frac{d\rho_0}{ds}
=
-\frac{307125}
{2(1043s+1916)^2}<0.
\]

Since

\[
\frac{ds}{d\alpha}
=
-(\log2)s<0,
\]

\[
\frac{d\rho_0}{d\alpha}>0.
\]

Therefore the global optimum over

\[
1+\Delta\le\alpha<3
\]

is always its lower endpoint.

### Small-\(\Delta\) expansion

At \(\alpha=1\),

\[
s=\frac12,
\qquad
\rho_0=1.
\]

The derivative is

\[
\left.
\frac{d\rho_0}{d\alpha}
\right|_{\alpha=1}
=
\frac{21\log2}{1625}.
\]

Therefore,

\[
\rho_0^\star(\Delta)
=
1+
\frac{21\log2}{1625}\Delta
+
O(\Delta^2).
\]

Because the future transport contributes a factor \(1/2\),

\[
\mathcal R_0^{Q,\star}(\Delta)
=
\frac{21}{3250}\Delta
+
O(\Delta^2).
\]

### Collapsed exclusion domain

For

\[
\Delta=2,
\]

only \(\alpha=3\) remains admissible. The exact duplicate ratio is

\[
\rho_0^\star(2)
=
\frac{3871}{3484}.
\]

But

\[
\lim_{\Delta\uparrow2}
\rho_0^\star(\Delta)
=
\frac{1840}{1819}.
\]

The discontinuity is caused by loss of derivative-like information when two
exactly distinct rows become the same row.

---

## 3. Positive-noise phase atlas

Fix

\[
\varepsilon=\frac1{10000}.
\]

The full interval \(1\le\alpha\le3\) is partitioned into fourteen exact
primal–dual phases.

The first seven phases lie in a narrow boundary layer near the directly
observed target:

| Phase | Approximate \(\alpha\)-interval |
|---|---:|
| \(M_0\) | \(1\)–\(1.0009048371\) |
| \(M_1\) | \(1.0009048371\)–\(1.0012823029\) |
| \(M_2\) | \(1.0012823029\)–\(1.0016422733\) |
| \(M_3\) | \(1.0016422733\)–\(1.0025074512\) |
| \(M_4\) | \(1.0025074512\)–\(1.0105049894\) |
| \(M_5\) | \(1.0105049894\)–\(1.0110832511\) |
| \(M_6\) | \(1.0110832511\)–\(1.1051683802\) |

The remaining phases continue the A50 atlas:

| Phase | Approximate \(\alpha\)-interval |
|---|---:|
| \(N_1\) | \(1.1051683802\)–\(2.2794407565\) |
| \(N_2\) | \(2.2794407565\)–\(2.6506501816\) |
| \(N_3\) | \(2.6506501816\)–\(2.8771796415\) |
| \(N_4\) | \(2.8771796415\)–\(2.9092795006\) |
| \(N_{4a}\) | \(2.9092795006\)–\(2.9114612584\) |
| \(N_{5a}\) | \(2.9114612584\)–\(2.9135569097\) |
| \(N_{5b}\) | \(2.9135569097\)–\(3\) |

Each phase supplies:

- a rational Charnes–Cooper primal solution;
- a rational dual solution;
- nonnegative microscopic weights;
- nonnegative inequality multipliers;
- nonnegative reduced costs;
- exact equality of primal and dual objectives;
- feasibility of every inactive observation constraint.

For every phase ratio \(R_j(s)\),

\[
R_j'(s)<0.
\]

Since \(s\) decreases with \(\alpha\),

\[
\frac{dR_j}{d\alpha}>0.
\]

Adjacent phases satisfy

\[
R_j(s_j)=R_{j+1}(s_j),
\]

so the global positive-noise ratio is continuous and strictly increasing on
\([1,3]\).

---

## 4. Noisy exclusion-distance law

For every

\[
0<\Delta\le2,
\]

the admissible interval is

\[
1+\Delta\le\alpha\le3.
\]

Global monotonicity immediately yields

\[
\boxed{
\alpha_{10^{-4}}^\star(\Delta)
=
1+\Delta.
}
\]

Thus the exact optimizer can be obtained by evaluating the appropriate phase
ratio at

\[
s_\Delta=2^{-(1+\Delta)}.
\]

### Small-\(\Delta\) boundary layer

The first phase has ratio

\[
R_{M_0}(s)
=
\frac{
6000s^5-18000s^3+12000s^2+1
}{
6000s^2(s-1)^2(s+2)
}.
\]

At

\[
s=\frac12,
\]

\[
R_{M_0}\left(\frac12\right)
=
\frac{1877}{1875}.
\]

This reproduces the universal direct-target ratio from A48.

The derivative with respect to \(\alpha\) is

\[
\left.
\frac{dR_{M_0}}{d\alpha}
\right|_{\alpha=1}
=
\frac{2\log2}{9375}.
\]

Therefore,

\[
\rho_{10^{-4}}^\star(\Delta)
=
\frac{1877}{1875}
+
\frac{2\log2}{9375}\Delta
+
O(\Delta^2).
\]

For the future score,

\[
\boxed{
\mathcal R_{10^{-4}}^{Q,\star}(\Delta)
=
0.000769027280134359\ldots
+
\frac{\Delta}{9385}
+
O(\Delta^2).
}
\]

The predictive uncertainty approaches the direct-measurement floor
continuously.

---

## 5. Interpretation for non-specialists

The exclusion distance \(\Delta\) says how close the instrument is allowed to
look at the quantity it is supposed to predict.

If \(\Delta\) is large, the observations must stay far from the target and the
prediction is harder.

If \(\Delta\) is small, the first observation may move closer to the target,
and the worst-case uncertainty falls.

The minimax rule is simple:

\[
\boxed{
\text{place the first observation exactly at the nearest permitted location.}
}
\]

As \(\Delta\to0\), this becomes almost a direct measurement. The mathematics
does not choose a universal ideal distance; the distance must be declared by
the information or experimental contract.

---

## 6. Logical status

### Established

1. The exact-data ratio is strictly increasing for every distinct
   \(\alpha\in(1,3)\).
2. For every \(0<\Delta<2\), the exact optimum is
   \(\alpha=1+\Delta\).
3. Exact risk approaches zero linearly as \(\Delta\downarrow0\).
4. The exact collapsed domain at \(\Delta=2\) is discontinuous.
5. Fourteen exact noisy certificates cover \([1,3]\).
6. Thirteen algebraic transitions are isolated and ordered.
7. The noisy value is continuous and strictly increasing in \(\alpha\).
8. For every \(0<\Delta\le2\), the noisy optimum is
   \(\alpha=1+\Delta\).
9. The noisy \(\Delta\downarrow0\) limit reproduces the A48 direct-target
   theorem.
10. The A50 phase atlas is exactly reproduced on \([2,3]\).

### Not established

1. The second and third anchors are not jointly reoptimized as functions of
   \(\Delta\).
2. No measurement cost is attached to reducing \(\Delta\).
3. No empirical noise law determines a preferred exclusion distance.
4. No continuous-support extension is supplied.
5. No physical status is assigned to the exponent coordinates.

---

## 7. Next rigorous target

The first-anchor problem is now closed under the controlled contracts.

The next non-ad-hoc extension is to let the second anchor respond to the
exclusion distance, for example

\[
D(\Delta,\beta)
=
\{(1+\Delta)\log2,\beta\log2,\gamma\log2\},
\]

while retaining an ordering and a minimum separation between observed
parameters. This would test whether the second anchor \(3\log2\) also follows a
boundary law or has a genuine interior optimum.
