# Continuous Third-Parameter Audit and Singular Design Limits

**Programme:** Modal Field Research Programme  
**Provisional audit:** A44  
**Author line:** Felipe Gianini Romero  
**Status:** rigorous mathematical continuation of MFRP-TR-2026-01 and A39–A43; no physical design claim

## Technical abstract

A43 solved the direct nonlinear future-score design problem on the finite catalogue

\[
\{2,3,4,5,6\}\log2.
\]

The present audit releases the third parameter and studies

\[
D(\gamma)=\{2\log2,3\log2,\gamma\log2\},
\qquad \gamma>3.
\]

The microscopic contract remains

\[
\operatorname{supp}P\subseteq\{0,1,2,3,4,5\},
\qquad
\mathbb E[X]=\frac52,
\]

and the target remains the future score \(Q'_{2\log2}\) under the centered contraction
\(a=1/2\).

Write

\[
r=2^{-\gamma}\in(0,1/8).
\]

For exact observations, the direct maximum-ratio risk is obtained in closed form:

\[
\rho_0(\gamma)
=
\frac{532r+1063}{2(275r+527)}.
\]

This formula has exact primal and dual certificates for every \(\gamma>3\). Since

\[
\frac{d\rho_0}{dr}
=
-\frac{11961}{2(275r+527)^2}<0
\]

and \(dr/d\gamma<0\), the risk is strictly increasing in \(\gamma\). Therefore the continuous
problem has no minimizer among distinct finite parameters. Its infimum occurs in the singular
limit \(\gamma\downarrow3\):

\[
\inf_{\gamma>3}\rho_0(\gamma)=\frac{502}{499},
\]

\[
\inf_{\gamma>3}\mathcal R_0^Q(\gamma)
=
\frac12\log_2\frac{502}{499}
\approx0.004323774306755653.
\]

At the duplicated design \(\gamma=3\), however, the third observation adds no information and

\[
\rho_0(3)=\frac{3665}{3458},
\]

\[
\mathcal R_0^Q(3)
=
\frac12\log_2\frac{3665}{3458}
\approx0.04193766468944622.
\]

Hence the exact-data value function is discontinuous at the duplicated parameter. The limit
\(\gamma\downarrow3\) behaves like an additional derivative constraint, but this effect is
singular and ill-conditioned.

For the common absolute tolerance

\[
\varepsilon=10^{-4},
\]

compactify the design space by adjoining \(\gamma=\infty\). Since

\[
L_P(\gamma\log2)\longrightarrow p_0,
\]

the boundary observable is the mass at the support point \(x=0\).

The compactified boundary has exact minimax ratio

\[
\rho_{10^{-4}}(\infty)
=
\frac{26593405}{26235854},
\]

and direct future-score risk

\[
\mathcal R_{10^{-4}}^Q(\infty)
=
\frac12\log_2\frac{26593405}{26235854}
\approx0.009764379451330085.
\]

An exact extremal pair for the boundary problem is feasible for every finite
\(\gamma\ge3\). Consequently

\[
\rho_{10^{-4}}(\gamma)
\ge
\rho_{10^{-4}}(\infty)
\qquad\forall\gamma\ge3.
\]

Compactness and uniform convergence of the transform imply

\[
\lim_{\gamma\to\infty}\rho_{10^{-4}}(\gamma)
=
\rho_{10^{-4}}(\infty).
\]

Thus \(\gamma=\infty\) is a global minimizer of the compactified noisy design problem. No
claim of uniqueness among finite parameters is needed for this conclusion.

The catalogue winner \(\gamma=6\) from A43 is therefore not the continuous optimum. Replacing
it by the compactified boundary improves the direct minimax future risk by about \(1.02\%\).
In the exact problem, replacing the catalogue winner \(\gamma=4\) by the singular infimum
reduces the risk by about \(16.86\%\), but that improvement is not robust.

The two limiting operations do not commute:

\[
\lim_{\varepsilon\downarrow0}
\lim_{\gamma\downarrow3}
\rho_\varepsilon(\gamma)
=
\frac{3665}{3458},
\]

whereas

\[
\lim_{\gamma\downarrow3}
\lim_{\varepsilon\downarrow0}
\rho_\varepsilon(\gamma)
=
\frac{502}{499}.
\]

This is the principal scientific result of A44: exact-data continuous design can reward
arbitrarily close parameters by extracting derivative-like information that disappears under
any fixed positive observational tolerance.

No continuous physical measurement parameter, empirical noise law, support, or contraction
is inferred.

---

## 1. Contract and direct risk

Let

\[
S=\{0,1,2,3,4,5\}.
\]

For a probability vector \(p\), define

\[
L_p(\alpha\log2)
=
\sum_{x=0}^{5}p_x2^{-\alpha x}.
\]

The admissible class is

\[
\mathcal P_{5/2}
=
\left\{
p_x\ge0:
\sum_xp_x=1,
\quad
\sum_xxp_x=\frac52
\right\}.
\]

The observation design is

\[
D(\gamma)=\{2,3,\gamma\},
\qquad \gamma>3.
\]

For common absolute tolerance \(\varepsilon\), define the pairwise ratio problem

\[
\rho_\varepsilon(\gamma)
=
\max_{p,q\in\mathcal P_{5/2}}
\frac{L_p(\log2)}{L_q(\log2)}
\]

subject to

\[
\left|
L_p(k\log2)-L_q(k\log2)
\right|
\le2\varepsilon,
\qquad
k\in\{2,3,\gamma\}.
\]

By the A43 pairwise and Charnes–Cooper reduction,

\[
\mathcal R_\varepsilon^Q(\gamma)
=
\frac12\log_2\rho_\varepsilon(\gamma).
\]

---

## 2. Exact-data solution for every \(\gamma>3\)

Set

\[
r=2^{-\gamma}.
\]

For \(\gamma>3\),

\[
0<r<\frac18.
\]

### Theorem 2.1 — closed exact ratio

For every \(\gamma>3\),

\[
\boxed{
\rho_0(\gamma)
=
\frac{532r+1063}{2(275r+527)}.
}
\]

### Exact primal extremizers

One maximizing pair is

\[
p_\gamma=
\left(
0,
\frac{76r+217}{4(76r+121)},
0,
\frac{57(4r+3)}{4(76r+121)},
0,
\frac{24}{76r+121}
\right),
\]

\[
q_\gamma=
\left(
\frac{3r}{4(76r+121)},
\frac{17r+107}{2(76r+121)},
\frac{3(57r+14)}{4(76r+121)},
0,
\frac{3(8r+19)}{76r+121},
0
\right).
\]

All denominators are positive and all displayed numerators are nonnegative for

\[
0<r<\frac18.
\]

Direct substitution gives

\[
\sum_xp_{\gamma,x}
=
\sum_xq_{\gamma,x}
=1,
\]

\[
\sum_xxp_{\gamma,x}
=
\sum_xxq_{\gamma,x}
=\frac52,
\]

and

\[
L_{p_\gamma}(2\log2)
=
L_{q_\gamma}(2\log2),
\]

\[
L_{p_\gamma}(3\log2)
=
L_{q_\gamma}(3\log2),
\]

\[
L_{p_\gamma}(\gamma\log2)
=
L_{q_\gamma}(\gamma\log2).
\]

Their target-transform ratio is the boxed expression above.

### Exact dual certificate

The Charnes–Cooper dual has nonzero reduced costs proportional to

\[
-\frac{2r-1}{275r+527}.
\]

Since

\[
2r-1<0
\]

throughout the domain, all reduced costs are nonnegative. Equality holds on the primal support.
Thus the primal value equals the dual value for every \(\gamma>3\), proving global optimality.

---

## 3. Monotonicity and singular exact optimum

Differentiate with respect to \(r\):

\[
\frac{d\rho_0}{dr}
=
-\frac{11961}{2(275r+527)^2}<0.
\]

But

\[
\frac{dr}{d\gamma}
=
-(\log2)r<0.
\]

Therefore

\[
\frac{d\rho_0}{d\gamma}>0.
\]

The exact-data risk strictly worsens as the third parameter moves away from the existing
anchor at \(3\log2\).

Consequently,

\[
\inf_{\gamma>3}\rho_0(\gamma)
=
\lim_{r\uparrow1/8}
\frac{532r+1063}{2(275r+527)}
=
\frac{502}{499}.
\]

The limiting extremizers are

\[
p_{3^+}
=
\left(
0,
\frac{151}{348},
0,
\frac{133}{348},
0,
\frac{16}{87}
\right),
\]

\[
q_{3^+}
=
\left(
\frac1{1392},
\frac{97}{232},
\frac{169}{1392},
0,
\frac{40}{87},
0
\right).
\]

They match the observations at \(2\log2\) and \(3\log2\). The coalescing third equality
encodes a derivative-like condition in the limit.

### Duplicated parameter

At exactly

\[
\gamma=3,
\]

the third row is identical to the second row. The direct ratio is instead

\[
\boxed{
\rho_0(3)=\frac{3665}{3458}.
}
\]

One exact maximizing pair is

\[
p=
\left(
\frac3{208},
\frac{107}{1976},
\frac{2913}{3952},
0,
0,
\frac{48}{247}
\right),
\]

\[
q=
\left(
0,
\frac14,
0,
\frac34,
0,
0
\right).
\]

Hence

\[
\lim_{\gamma\downarrow3}\rho_0(\gamma)
=
\frac{502}{499}
\ne
\frac{3665}{3458}
=
\rho_0(3).
\]

The exact-data continuous design has an unattained infimum, not a finite optimal parameter.

---

## 4. Why close exact parameters imitate a derivative

Let

\[
\Delta(\alpha)
=
L_p(\alpha\log2)-L_q(\alpha\log2).
\]

For exact observations,

\[
\Delta(3)=0,
\qquad
\Delta(\gamma)=0.
\]

If \(\gamma\downarrow3\), then

\[
\frac{\Delta(\gamma)-\Delta(3)}{\gamma-3}=0.
\]

Because the transform is differentiable in \(\alpha\), every convergent sequence of feasible
pairs is driven toward

\[
\Delta(3)=0,
\qquad
\Delta'(3)=0.
\]

Thus two arbitrarily close exact parameters behave as a value-and-derivative measurement.
This additional derivative information is real mathematically, but it is singular: any fixed
positive tolerance prevents division by an arbitrarily small parameter separation without
unbounded noise amplification.

---

## 5. Compactified noisy design

Now fix

\[
\varepsilon=\frac1{10000}.
\]

As \(\gamma\to\infty\),

\[
2^{-\gamma x}\to
\begin{cases}
1,&x=0,\\
0,&x\ge1.
\end{cases}
\]

Therefore

\[
L_p(\gamma\log2)\to p_0.
\]

Adjoin a compactified boundary design

\[
D(\infty)=\{2,3,\infty\},
\]

where the third observed functional is \(p\mapsto p_0\).

### Theorem 5.1 — exact boundary optimum

The compactified problem has exact ratio

\[
\boxed{
\rho_{10^{-4}}(\infty)
=
\frac{26593405}{26235854}.
}
\]

An exact extremal pair is

\[
p_\infty=
\left(
\frac1{5000},
\frac{249961937}{533610000},
0,
\frac{166821821}{533610000},
0,
\frac{1458994}{6670125}
\right),
\]

\[
q_\infty=
\left(
0,
\frac{1741651}{3705625},
\frac{666969}{14822500},
0,
\frac{7188927}{14822500},
0
\right).
\]

They satisfy

\[
\mathbb E_{p_\infty}[X]
=
\mathbb E_{q_\infty}[X]
=
\frac52,
\]

\[
L_{p_\infty}(2\log2)-L_{q_\infty}(2\log2)
=
\frac1{5000},
\]

\[
L_{p_\infty}(3\log2)-L_{q_\infty}(3\log2)
=
-\frac1{5000},
\]

and

\[
p_{\infty,0}-q_{\infty,0}
=
\frac1{5000}.
\]

Since

\[
2\varepsilon=\frac1{5000},
\]

all three boundary constraints are saturated. An exact Charnes–Cooper dual certificate has
nonnegative inequality multipliers and nonnegative reduced costs, so the ratio is globally
optimal.

---

## 6. The boundary extremizer is feasible for every finite \(\gamma\)

Let

\[
r=2^{-\gamma},
\qquad
0\le r\le\frac18,
\]

and define

\[
\Delta_\infty(r)
=
L_{p_\infty}(\gamma\log2)
-
L_{q_\infty}(\gamma\log2).
\]

Exact simplification gives

\[
\Delta_\infty(r)
=
\frac{
(r-1)^2
\left(
116719520r^3
-25362332r^2
-622363r
+106722
\right)
}{533610000}.
\]

The upper-tolerance residual factors as

\[
\Delta_\infty(r)-\frac1{5000}
=
\frac{
r(4r-1)P_1(r)
}{533610000},
\]

where

\[
P_1(r)
=
29179880r^3
-57405373r^2
+27354112r
+835807.
\]

The lower-tolerance residual factors as

\[
\Delta_\infty(r)+\frac1{5000}
=
\frac{
(8r-1)P_2(r)
}{533610000},
\]

where

\[
P_2(r)
=
14589940r^4
-30526429r^3
+17036924r^2
-871745r
-213444.
\]

To certify the signs, put \(r=t/8\), \(t\in[0,1]\). The Bernstein coefficients of \(P_1(t/8)\)
are

\[
835807,\quad
\frac{5926685}{3},\quad
\frac{180245121}{64},\quad
3415104,
\]

all strictly positive.

The Bernstein coefficients of \(P_2(t/8)\) are

\[
-213444,\quad
-\frac{7701953}{32},\quad
-\frac{21461863}{96},\quad
-\frac{362443997}{2048},\quad
-\frac{114964605}{1024},
\]

all strictly negative.

Therefore, throughout \(0\le r\le1/8\),

\[
P_1(r)>0,
\qquad
P_2(r)<0.
\]

Since

\[
r\ge0,\qquad4r-1<0,\qquad8r-1\le0,
\]

it follows that

\[
-\frac1{5000}
\le
\Delta_\infty(r)
\le
\frac1{5000}.
\]

Thus the exact boundary extremal pair is feasible for every finite \(\gamma\ge3\). Its target
ratio does not depend on \(\gamma\), so

\[
\rho_{10^{-4}}(\gamma)
\ge
\frac{26593405}{26235854}
\quad\forall\gamma\ge3.
\]

---

## 7. Convergence to the boundary value

Let \(\gamma_n\to\infty\), and choose maximizing pairs \(p_n,q_n\). The admissible probability
simplex with fixed mean is compact, so a subsequence converges to \(p,q\).

Uniformly over all admissible distributions,

\[
\left|
L_p(\gamma\log2)-p_0
\right|
\le2^{-\gamma}.
\]

Therefore the finite-\(\gamma_n\) third constraints imply in the limit

\[
|p_0-q_0|\le2\varepsilon.
\]

The two anchored constraints also pass to the limit. The target denominator is bounded below
by \(2^{-5}>0\), so the target ratio is continuous.

Hence every subsequential limit of optimal ratios is no greater than the compactified boundary
optimum:

\[
\limsup_{\gamma\to\infty}
\rho_{10^{-4}}(\gamma)
\le
\rho_{10^{-4}}(\infty).
\]

Section 6 gives the reverse inequality for every finite \(\gamma\). Therefore

\[
\boxed{
\lim_{\gamma\to\infty}
\rho_{10^{-4}}(\gamma)
=
\rho_{10^{-4}}(\infty).
}
\]

The compactified boundary is consequently a global minimizer.

---

## 8. Positive noise removes the coalescing-parameter advantage

At the duplicated design \(\gamma=3\) and tolerance \(10^{-4}\), the exact direct ratio is

\[
\boxed{
\rho_{10^{-4}}(3)
=
\frac{337423987}{317703750}.
}
\]

The corresponding future risk is

\[
\frac12\log_2
\frac{337423987}{317703750}
\approx0.04344020875874143.
\]

For any fixed \(\varepsilon>0\), the finite-dimensional linear-programme value is continuous
as \(\gamma\downarrow3\). Informally, the two nearly identical noisy rows do not yield a
stable derivative constraint because their difference is smaller than the fixed error box.

A compactness argument gives the upper-limit inequality. For the lower-limit inequality, mix
an optimal duplicated-design pair with a strictly feasible neutral pair \(p=q\), creating
arbitrarily small slack while changing the ratio arbitrarily little. Uniform convergence of
the third transform row then preserves feasibility for \(\gamma\) sufficiently close to \(3\).

Thus, for fixed positive tolerance,

\[
\lim_{\gamma\downarrow3}
\rho_\varepsilon(\gamma)
=
\rho_\varepsilon(3).
\]

Letting \(\varepsilon\downarrow0\) afterward gives

\[
\lim_{\varepsilon\downarrow0}
\lim_{\gamma\downarrow3}
\rho_\varepsilon(\gamma)
=
\frac{3665}{3458}.
\]

In the reverse order, exact data are imposed first:

\[
\lim_{\gamma\downarrow3}
\lim_{\varepsilon\downarrow0}
\rho_\varepsilon(\gamma)
=
\frac{502}{499}.
\]

Therefore

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\lim_{\gamma\downarrow3}
\rho_\varepsilon(\gamma)
\ne
\lim_{\gamma\downarrow3}
\lim_{\varepsilon\downarrow0}
\rho_\varepsilon(\gamma).
}
\]

This noncommutation is the formal signature of the design singularity.

---

## 9. Comparison with A43 catalogue points

### Exact observations

A43 selected

\[
\gamma=4
\]

from the finite catalogue, with risk

\[
\frac12\log_2\frac{8770}{8707}
\approx0.00520055966453554.
\]

The continuous exact infimum is

\[
\frac12\log_2\frac{502}{499}
\approx0.004323774306755653.
\]

The formal reduction is approximately

\[
16.86\%.
\]

This gain is singular and is not robust to fixed positive noise.

### Tolerance \(10^{-4}\)

A43 selected

\[
\gamma=6,
\]

with risk

\[
\frac12\log_2
\frac{1828961429248}{1804118444725}
\approx0.00986529623594507.
\]

The compactified boundary gives

\[
\frac12\log_2\frac{26593405}{26235854}
\approx0.009764379451330085.
\]

The reduction is approximately

\[
1.02\%.
\]

Thus the catalogue already captured most of the robust benefit, while missing the exact
continuous boundary optimum.

---

## 10. Logical status

### Established

1. The exact direct-\(Q\) ratio is available in closed form for every \(\gamma>3\).
2. Exact risk is strictly increasing in \(\gamma\).
3. The exact continuous problem has an unattained infimum at \(\gamma\downarrow3\).
4. The duplicated exact design has a much larger risk, producing a genuine discontinuity.
5. At tolerance \(10^{-4}\), the compactified boundary \(\gamma=\infty\) has an exact
   primal-dual optimum.
6. Its extremal pair remains feasible for every finite \(\gamma\).
7. Finite-\(\gamma\) risks converge to the boundary risk.
8. The zero-noise and coalescing-parameter limits do not commute.
9. Catalogue points \(4\) and \(6\) are not the exact continuous optima under their respective
   contracts.

### Not established

1. No unique finite noisy minimizer is claimed.
2. No complete risk curve for every positive tolerance is derived.
3. No parameter-separation cost or measurement-time cost is included.
4. No empirical covariance model is supplied.
5. No continuous physical control parameter is identified.
6. No physical meaning is assigned to the boundary observable \(p_0\).

---

## 11. Consequence for future design work

The exact-data continuous optimization is mathematically ill-posed as an operational design
criterion: it rewards arbitrarily close parameters because exact differences encode
derivatives.

A non-ad-hoc operational design must therefore declare at least one of:

- a positive observational tolerance;
- a minimum parameter separation;
- a covariance model whose variance grows as parameters coalesce;
- a direct derivative measurement with its own error contract;
- a parameter-dependent measurement cost.

Without one of these contracts, a continuous exact-data optimum can be a singular artifact
rather than a robust information design.

The next rigorous target should therefore be a **joint separation-and-noise design**, for
example

\[
\gamma\ge3+\Delta_{\min},
\]

with an explicitly declared relation between \(\Delta_{\min}\), measurement precision, and
cost.
