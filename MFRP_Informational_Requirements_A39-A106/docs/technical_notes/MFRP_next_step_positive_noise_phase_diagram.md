# Complete Positive-Noise Phase Diagram for the Continuous Third Parameter

**Programme:** Modal Field Research Programme  
**Provisional audit:** A45  
**Author line:** Felipe Gianini Romero  
**Status:** rigorous mathematical continuation of MFRP-TR-2026-01 and A39–A44; no physical design claim

## Technical abstract

A44 proved two endpoint results for the continuous design

\[
D(\gamma)=\{2\log2,3\log2,\gamma\log2\},
\qquad \gamma\ge3.
\]

With exact observations, the direct minimax future-score risk has a singular unattained
infimum as \(\gamma\downarrow3\). With common absolute tolerance
\(\varepsilon=10^{-4}\), the compactified boundary \(\gamma=\infty\) is globally optimal.

The present audit closes the interval between those endpoints. Under the same declared
contract,

\[
\operatorname{supp}P\subseteq\{0,1,2,3,4,5\},
\qquad
\mathbb E[X]=\frac52,
\]

the complete direct-ratio value function is derived and certified for every
\(\gamma\in[3,\infty]\).

Set

\[
r=2^{-\gamma}\in[0,1/8].
\]

There are four algebraic transition points

\[
0<r_3<r_2<r_1<r_0<\frac18
\]

and five optimal regimes. Their corresponding parameter values are

\[
\gamma_0\approx3.102814919037135,
\]

\[
\gamma_1\approx3.115695163716007,
\]

\[
\gamma_2\approx3.382335432437322,
\]

\[
\gamma_3\approx4.670493013621934.
\]

For \(3\le\gamma\le\gamma_0\), the third observation is redundant at the minimax optimum and
the risk is constant:

\[
\rho(\gamma)=\frac{337423987}{317703750}.
\]

For \(\gamma>\gamma_0\), four rational functions of \(r\) describe the successive optimal
bases. Each function is strictly increasing in \(r\), hence strictly decreasing in
\(\gamma\). Adjacent formulas agree at every algebraic transition, and the final regime
converges to

\[
\rho(\infty)=\frac{26593405}{26235854}.
\]

Consequently, for the positive-noise benchmark,

\[
\rho(\gamma)
\]

is nonincreasing on \([3,\infty]\), constant only on the initial redundancy plateau and
strictly decreasing afterward. The compactified minimizer \(\gamma=\infty\) is therefore
unique.

This produces a hard-cap design rule without inventing a scalar measurement cost. If the
third parameter is constrained by

\[
3\le\gamma\le\Gamma_{\max},
\]

then:

- when \(\Gamma_{\max}\le\gamma_0\), every admissible \(\gamma\) ties;
- when \(\Gamma_{\max}>\gamma_0\), the unique minimax choice is
  \[
  \gamma^\star=\Gamma_{\max}.
  \]

Combined with the exact-data result of A44, this gives an endpoint reversal. Under exact data
and a minimum separation \(\gamma\ge3+\Delta_{\min}\), the best parameter is the smallest
allowed value. Under the audited positive-noise contract and a finite upper cap, the best
parameter is the largest allowed value.

The result is contract-relative. It does not infer an empirical noise law, a physical
measurement cost, a physical support, or a physical interpretation of \(\gamma=\infty\).

---

## 1. Declared problem

Let

\[
S=\{0,1,2,3,4,5\}.
\]

For a probability vector \(p=(p_0,\ldots,p_5)\), define

\[
L_p(\alpha\log2)
=
\sum_{x=0}^{5}p_x2^{-\alpha x}.
\]

The admissible microscopic class is

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

Fix

\[
\varepsilon=\frac1{10000}.
\]

For

\[
D(\gamma)=\{2,3,\gamma\},
\]

define

\[
\rho(\gamma)
=
\max_{p,q\in\mathcal P_{5/2}}
\frac{L_p(\log2)}{L_q(\log2)}
\]

subject to

\[
\left|
L_p(k\log2)-L_q(k\log2)
\right|
\le
\frac1{5000},
\qquad
k\in\{2,3,\gamma\}.
\]

The direct future-score minimax risk is

\[
\mathcal R^Q(\gamma)
=
\frac12\log_2\rho(\gamma).
\]

The mean contribution cancels because both microscopic distributions have the same exact
mean.

---

## 2. Algebraic transition points

Let

\[
r=2^{-\gamma}.
\]

Define the four transition polynomials

\[
A_0(r)
=
53268160r^4
+13317040r^3
-200908865r^2
+148890794r
-14639747,
\]

\[
A_1(r)
=
35156096r^4
+8789024r^3
-132490502r^2
+98061088r
-9569361,
\]

\[
A_2(r)
=
334069952r^4
-455233544r^3
-113808386r^2
+257741432r
-23297331,
\]

and

\[
A_3(r)
=
1838752r^4
-4611812r^3
+3732866r^2
-989812r
+33387.
\]

Each polynomial has exactly one root in

\[
(0,1/8).
\]

Call those roots \(r_0,r_1,r_2,r_3\), respectively. Exact Sturm isolation gives

\[
r_0\in
\left(
\frac{11640178}{10^8},
\frac{11640179}{10^8}
\right),
\]

\[
r_1\in
\left(
\frac{11536718}{10^8},
\frac{11536719}{10^8}
\right),
\]

\[
r_2\in
\left(
\frac{9589933}{10^8},
\frac{9589934}{10^8}
\right),
\]

\[
r_3\in
\left(
\frac{3926824}{10^8},
\frac{3926825}{10^8}
\right).
\]

Therefore

\[
0<r_3<r_2<r_1<r_0<\frac18.
\]

Define

\[
\gamma_j=-\log_2r_j.
\]

Numerically,

\[
\gamma_0
=
3.1028149190371346925\ldots,
\]

\[
\gamma_1
=
3.1156951637160071020\ldots,
\]

\[
\gamma_2
=
3.3823354324373222336\ldots,
\]

\[
\gamma_3
=
4.6704930136219336098\ldots.
\]

---

## 3. Complete piecewise ratio

### Regime 0 — redundant third observation

For

\[
r_0\le r\le\frac18
\qquad
\left(
3\le\gamma\le\gamma_0
\right),
\]

the optimal pair is already optimal using only the anchors \(2\log2\) and \(3\log2\).
The third inequality is inactive. The exact value is

\[
\boxed{
R_0(r)
=
\frac{337423987}{317703750}.
}
\]

The third-transform difference of this pair is

\[
\Delta_0(r)
=
\frac{
(r-1)^2
\left(
213072640r^3
+426145280r^2
-177734580r
+14857601
\right)
}{1089270000}.
\]

On the full plateau,

\[
-\frac1{5000}
\le
\Delta_0(r)
\le
\frac1{5000}.
\]

At \(r=1/8\), the lower side is saturated. At \(r=r_0\), the upper side is saturated and the
third observation becomes active.

### Regime 1

For

\[
r_1\le r\le r_0
\qquad
\left(
\gamma_0\le\gamma\le\gamma_1
\right),
\]

\[
\boxed{
R_1(r)
=
\frac{
70436096r^4
+17609024r^3
-268968412r^2
+203255020r
-22248967
}{
38\left(
1847680r^4
+461920r^3
-7050770r^2
+5322512r
-579431
\right)
}.
}
\]

An optimal pair has support pattern

\[
\operatorname{supp}p=\{0,1,2,5\},
\qquad
\operatorname{supp}q=\{1,2,3\}.
\]

All three observational inequalities are active with signs

\[
(+,-,+).
\]

### Regime 2

For

\[
r_2\le r\le r_1
\qquad
\left(
\gamma_1\le\gamma\le\gamma_2
\right),
\]

\[
\boxed{
R_2(r)
=
\frac{
4\left(
2205000r^4
+356036071r^3
-763935114r^2
+450930647r
-45228078
\right)
}{
35131008r^4
+1352358784r^3
-2988326634r^2
+1779064448r
-178236279
}.
}
\]

The support pattern is

\[
\operatorname{supp}p=\{0,2,5\},
\qquad
\operatorname{supp}q=\{1,2,3,4\}.
\]

### Regime 3

For

\[
r_3\le r\le r_2
\qquad
\left(
\gamma_2\le\gamma\le\gamma_3
\right),
\]

\[
\boxed{
R_3(r)
=
\frac{
506059952r^4
+21367778r^3
-1700546319r^2
+1312566628r
-139310888
}{
5\left(
103603936r^4
-2543516r^3
-333277512r^2
+259744544r
-27508489
\right)
}.
}
\]

The support pattern is

\[
\operatorname{supp}p=\{0,2,3,5\},
\qquad
\operatorname{supp}q=\{1,2,4\}.
\]

### Regime 4

For

\[
0\le r\le r_3
\qquad
\left(
\gamma_3\le\gamma\le\infty
\right),
\]

\[
\boxed{
R_4(r)
=
\frac{
4651509760r^4
-531817376r^3
-14091583756r^2
+11170302884r
-1196703225
}{
10\left(
480055456r^4
-94091636r^3
-1370377492r^2
+1102617752r
-118061343
\right)
}.
}
\]

The support pattern is

\[
\operatorname{supp}p=\{0,1,3,5\},
\qquad
\operatorname{supp}q=\{1,2,4\}.
\]

At the compactified boundary,

\[
R_4(0)
=
\frac{26593405}{26235854}.
\]

---

## 4. Transition mechanisms

The active-set changes are not arbitrary numerical labels.

### At \(r=r_0\)

The third constraint of the duplicated-anchor optimum becomes active. The factor

\[
A_0(r)
\]

is simultaneously the upper-tolerance residual of the plateau pair and the entering
\(q_2\) weight of Regime 1.

### At \(r=r_1\)

The factor

\[
A_1(r)
\]

is the vanishing \(p_1\) weight in Regime 1 and the entering \(q_4\) weight in Regime 2.

### At \(r=r_2\)

The factor

\[
A_2(r)
\]

is the vanishing \(q_3\) weight in Regime 2 and the entering \(p_3\) weight in Regime 3.

### At \(r=r_3\)

The factor

\[
A_3(r)
\]

is a reduced-cost degeneracy. Regimes 3 and 4 meet on an optimal face; the optimal objective
is continuous even though the displayed extremal pair need not be unique at the transition.

For every adjacent pair,

\[
R_j(r_j)=R_{j+1}(r_j).
\]

The equalities are certified algebraically because the numerator of each adjacent difference
is divisible by the corresponding transition polynomial.

---

## 5. Exact optimality certificates on all regimes

For Regimes 1–4, the Charnes–Cooper linear programme supplies symbolic rational functions
for:

- all nonzero primal weights;
- the scaling variable;
- all three inequality multipliers;
- every reduced cost;
- the primal and dual objectives.

On each algebraic interval, exact real-root isolation verifies:

\[
p_x(r)\ge0,
\qquad
q_x(r)\ge0,
\]

\[
u_j(r)\ge0,
\]

and

\[
\text{reduced cost}_k(r)\ge0.
\]

The primal constraints hold symbolically:

\[
\sum_xp_x=\sum_xq_x=1,
\]

\[
\sum_xxp_x=\sum_xxq_x=\frac52,
\]

and

\[
L_p(2\log2)-L_q(2\log2)=\frac1{5000},
\]

\[
L_p(3\log2)-L_q(3\log2)=-\frac1{5000},
\]

\[
L_p(\gamma\log2)-L_q(\gamma\log2)=\frac1{5000}.
\]

The primal and dual objectives agree identically. Hence every displayed rational function is
the global minimax ratio on its full regime, not merely a fitted branch.

---

## 6. Global monotonicity

The derivatives of the four active branches factor as follows.

For Regime 1,

\[
R_1'(r)
=
\frac{
1946478(r-1)
\left(
174080r^4
-307584r^3
-87232r^2
+359442r
-166489
\right)
}{
19D_1(r)^2
},
\]

where \(D_1\) is the denominator polynomial of \(R_1\).

For Regime 2,

\[
R_2'(r)
=
\frac{
-1083846732(r-1)
\left(
35156096r^5
-114300832r^4
+131468770r^3
-60313982r^2
+7753233r
+337557
\right)
}{
D_2(r)^2
}.
\]

For Regime 3,

\[
R_3'(r)
=
\frac{
-20115858(r-1)
\left(
34807936r^5
-114823072r^4
+134423458r^3
-62697070r^2
+7745785r
+780662
\right)
}{
D_3(r)^2
}.
\]

For Regime 4,

\[
R_4'(r)
=
\frac{
-433867842(r-1)
\left(
210163456r^5
-689689792r^4
+805802972r^3
-381843564r^2
+55544031r
+835807
\right)
}{
5D_4(r)^2
}.
\]

Exact root isolation shows

\[
R_j'(r)>0
\]

throughout the interior of every active regime.

Since

\[
\frac{dr}{d\gamma}=-(\log2)r<0
\]

for finite \(\gamma\),

\[
\frac{dR_j}{d\gamma}<0.
\]

Therefore

\[
\boxed{
\rho(\gamma)
\text{ is constant on }[3,\gamma_0]
\text{ and strictly decreasing on }(\gamma_0,\infty).
}
\]

The logarithm is strictly increasing, so the same statement holds for the direct future-score
risk

\[
\mathcal R^Q(\gamma)=\frac12\log_2\rho(\gamma).
\]

---

## 7. Numerical risk map

| \(\gamma\) or transition | Direct future risk |
|---:|---:|
| \(3\) | \(0.0434402087587414\) |
| \(\gamma_0\approx3.1028149190\) | \(0.0434402087587414\) |
| \(\gamma_1\approx3.1156951637\) | \(0.0408909496394752\) |
| \(\gamma_2\approx3.3823354324\) | \(0.0182772033735726\) |
| \(4\) | \(0.0117038075340311\) |
| \(\gamma_3\approx4.6704930136\) | \(0.0102512972458510\) |
| \(6\) | \(0.0098652962359451\) |
| \(10\) | \(0.0097681452113757\) |
| \(\infty\) | \(0.0097643794513301\) |

Most of the robust gain occurs before \(\gamma=6\); the remaining improvement from
\(\gamma=6\) to the compactified boundary is about \(1.02\%\), as already bounded in A44.

---

## 8. Hard-cap design theorem

### Theorem 8.1 — positive-noise cap rule

Fix an operational upper limit

\[
3\le\gamma\le\Gamma_{\max}.
\]

Under the full A45 contract:

1. If
   \[
   3\le\Gamma_{\max}\le\gamma_0,
   \]
   every admissible \(\gamma\) has the same minimax risk.

2. If
   \[
   \Gamma_{\max}>\gamma_0,
   \]
   the unique minimax choice is
   \[
   \boxed{\gamma^\star=\Gamma_{\max}.}
   \]

### Proof

The complete phase diagram proves constancy on the initial plateau and strict decrease
afterward. \(\square\)

This theorem avoids combining risk and parameter magnitude through an arbitrary scalar
weight. It reports the exact best risk achievable for every hard operational cap.

---

## 9. Endpoint reversal relative to exact data

A44 proved that with exact observations,

\[
\rho_0(\gamma)
=
\frac{532r+1063}{2(275r+527)}
\]

is strictly increasing in \(\gamma\) for every \(\gamma>3\).

Therefore, under an exact-data minimum-separation contract

\[
3+\Delta_{\min}\le\gamma\le\Gamma_{\max},
\]

the optimum is

\[
\boxed{
\gamma^\star_{\mathrm{exact}}
=
3+\Delta_{\min}.
}
\]

Under the A45 positive-noise contract and a cap exceeding \(\gamma_0\),

\[
\boxed{
\gamma^\star_{\mathrm{noisy}}
=
\Gamma_{\max}.
}
\]

Thus the preferred endpoint reverses:

\[
\boxed{
\text{exact idealization: smallest permitted separation;}
}
\]

\[
\boxed{
\text{audited positive noise: largest permitted parameter.}
}
\]

This reversal is the operational manifestation of the noncommuting limits established in
A44.

---

## 10. Logical status

### Established

1. The complete \(\varepsilon=10^{-4}\) direct-risk curve is piecewise rational in
   \(r=2^{-\gamma}\).
2. Four algebraic transition points and five optimal regimes are exactly identified.
3. Every branch has a symbolic primal-dual certificate over its full algebraic interval.
4. Adjacent branches agree at their transition points.
5. The third observation is redundant on a nonzero initial interval.
6. The risk is strictly decreasing after the redundancy plateau.
7. The compactified minimizer \(\gamma=\infty\) is unique.
8. A finite upper cap produces an exact endpoint design rule.
9. Exact and positive-noise contracts select opposite permitted endpoints.

### Not established

1. No analogous complete phase diagram has been derived for arbitrary \(\varepsilon>0\).
2. No empirical variance or covariance law is supplied.
3. No measurement cost depending on \(\gamma\) is inferred.
4. No physical meaning is assigned to the support, the anchors, or the limiting observable
   \(p_0\).
5. The anchor pair \(\{2,3\}\) has not itself been continuously optimized.
6. No result here promotes this formal design into a physical experiment.

---

## 11. Next rigorous target

The remaining limitation is that the error level is fixed at one benchmark.

The next non-ad-hoc problem is a two-parameter phase diagram:

\[
(\varepsilon,\gamma)
\longmapsto
\rho_\varepsilon(\gamma).
\]

The aims would be:

- derive the redundancy boundary
  \[
  \gamma_0(\varepsilon);
  \]
- locate active-set bifurcation curves;
- determine whether the upper-endpoint rule holds for every positive \(\varepsilon\) or only
  beyond a threshold;
- recover the singular exact-data limit as
  \[
  \varepsilon\downarrow0.
  \]

That problem would convert the isolated noncommutation result into a complete
noise–separation phase diagram.
