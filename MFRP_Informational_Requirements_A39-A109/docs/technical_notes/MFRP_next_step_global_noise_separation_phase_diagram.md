# Complete Global Noise–Separation Phase Diagram

**Programme:** Modal Field Research Programme  
**Provisional audit:** A47  
**Author line:** Felipe Gianini Romero  
**Status:** rigorous global continuation of MFRP-TR-2026-01 and A39–A46; no physical design claim

## Technical abstract

A46 identified the local and asymptotic bifurcation skeleton of the two-parameter design
problem but deliberately stopped short of a global theorem. The present audit closes that gap.

The declared contract is unchanged:

\[
\operatorname{supp}P\subseteq\{0,1,2,3,4,5\},
\qquad
\mathbb E[X]=\frac52,
\]

with exact mean, anchors \(2\log2\) and \(3\log2\), a third observation
\(\gamma\log2\), common absolute tolerance

\[
0<\varepsilon\le10^{-4},
\]

and direct minimax future-score risk under the centered contraction \(a=1/2\).

Set

\[
r=2^{-\gamma}\in[0,1/8].
\]

The whole rectangle

\[
\mathcal D=
\left\{
(r,\varepsilon):
0\le r\le\frac18,\;
0<\varepsilon\le10^{-4}
\right\}
\]

is partitioned by five explicitly rational boundary functions

\[
B_0(r)>B_1(r)>B_2(r)>B_3(r)>B_4(r)\ge0
\qquad
(0\le r<1/8).
\]

Exactly six Charnes–Cooper primal–dual certificates cover the six layers:

\[
\begin{array}{c|c}
\text{layer}&\text{condition}\\
\hline
\mathcal A_0&\varepsilon\ge B_0(r),\\
\mathcal A_1&B_1(r)\le\varepsilon\le B_0(r),\\
\mathcal A_2&B_2(r)\le\varepsilon\le B_1(r),\\
\mathcal A_3&B_3(r)\le\varepsilon\le B_2(r),\\
\mathcal A_4&B_4(r)\le\varepsilon\le B_3(r),\\
\mathcal A_5&0<\varepsilon\le B_4(r).
\end{array}
\]

In each layer, a symbolic rational primal solution and a symbolic rational dual solution are
feasible and have identical objective values. Consequently the direct minimax ratio is a
globally exact piecewise-rational function

\[
\rho_\varepsilon(r)=R_i(r,\varepsilon)
\quad\text{on }\mathcal A_i.
\]

Adjacent formulas coincide on every boundary \(B_i\), so the value function is continuous
for every positive error level.

This global atlas promotes the local design branches of A46 to global minimizers. Let

\[
r_a
\]

be the unique root in \((0,1/8)\) of

\[
J(r)=
123904r^5-359168r^4+338000r^3-96856r^2-8379r+441,
\]

and define

\[
\varepsilon_a=B_4(r_a)
=
0.000036878499088019888\ldots.
\]

Also define

\[
\varepsilon_b=
\frac{189}{2367604}
=
0.00007982753872691548\ldots.
\]

Then the global optimum over \(\gamma\in[3,\infty]\) is:

\[
0<\varepsilon<\varepsilon_a:
\quad
r^\star=r_5(\varepsilon),
\]

where \(r_5\) is the unique solution of

\[
E_5(r)=\varepsilon
\quad\text{in }(r_a,1/8);
\]

\[
\varepsilon_a\le\varepsilon<\varepsilon_b:
\quad
r^\star=r_4(\varepsilon),
\]

where \(r_4\) is the unique solution of

\[
E_4(r)=\varepsilon
\quad\text{in }[0,r_a];
\]

and

\[
\varepsilon\ge\varepsilon_b:
\quad
r^\star=0,
\qquad
\gamma^\star=\infty.
\]

Thus the finite stationary branches found in A46 are not merely local artifacts: within the
declared contract they are the unique global minimizers until the compactified boundary takes
over.

As \(\varepsilon\downarrow0\),

\[
\gamma^\star(\varepsilon)
=
3+
\frac{64\sqrt{174}}{7\log2}\sqrt{\varepsilon}
+
\frac{913408}{147\log2}\varepsilon
+
O(\varepsilon^{3/2}),
\]

recovering the singular exact-data boundary layer without promoting the duplicated
parameter \(\gamma=3\) into an optimum.

The theorem is finite-support and contract-relative. It does not infer a physical support,
noise law, measurement cost, contraction, or interpretation of the compactified observable.

---

## 1. Direct minimax formulation

For \(p=(p_0,\ldots,p_5)\), define

\[
L_p(\alpha\log2)=
\sum_{x=0}^{5}p_x2^{-\alpha x}.
\]

Let

\[
\mathcal P_{5/2}
=
\left\{
p_x\ge0:
\sum_xp_x=1,\quad
\sum_xxp_x=\frac52
\right\}.
\]

For \(r=2^{-\gamma}\), the third observed functional is

\[
L_p(\gamma\log2)=\sum_xp_xr^x.
\]

The pairwise maximum-ratio problem is

\[
\rho_\varepsilon(r)=
\max_{p,q\in\mathcal P_{5/2}}
\frac{L_p(\log2)}{L_q(\log2)}
\]

subject to

\[
|L_p(2\log2)-L_q(2\log2)|\le2\varepsilon,
\]

\[
|L_p(3\log2)-L_q(3\log2)|\le2\varepsilon,
\]

\[
\left|
\sum_x(p_x-q_x)r^x
\right|
\le2\varepsilon.
\]

The direct future-score width is

\[
\mathcal R_\varepsilon^Q(r)
=
\frac12\log_2\rho_\varepsilon(r).
\]

The Charnes–Cooper substitution converts every fixed \((r,\varepsilon)\) problem into a
finite linear programme with rational coefficients whenever \(r\) and \(\varepsilon\) are
rational.

---

## 2. Five exact phase boundaries

Define

\[
B_0(r)=
-\frac{
1323(r-1)^2(8r-1)(8r+19)
}{
32\left(
174080r^4+43520r^3+10880r^2-800228r+535439
\right)
},
\]

\[
B_1(r)=
\frac{
441(r-1)^2(8r-1)(8r+19)
}{
8\left(
123904r^4+30976r^3-1463248r^2+2266412r-904389
\right)
},
\]

\[
B_2(r)=
\frac{
8379(r-1)^2(4r+3)(8r-1)
}{
8\left(
1090048r^4-5611456r^3-1402864r^2+14576068r-8123919
\right)
},
\]

\[
B_3(r)=
-\frac{
441(r-1)^2(2r-1)(8r-1)
}{
40\left(
74752r^4+18688r^3-346384r^2+333188r-76863
\right)
},
\]

and

\[
B_4(r)=
-\frac{
1323r(r-1)^2(8r-1)
}{
8\left(
1090048r^4-442304r^3-2290672r^2+1571780r+53361
\right)
}.
\]

Exact real-root isolation gives

\[
B_i(r)>0
\quad
(0\le r<1/8,\;i=0,\ldots,3),
\]

\[
B_4(r)\ge0,
\]

and

\[
\boxed{
B_0(r)>B_1(r)>B_2(r)>B_3(r)>B_4(r)
}
\]

for every \(0\le r<1/8\).

All five functions vanish at \(r=1/8\). At \(r=0\),

\[
B_0(0)=\frac{1323}{901792},
\]

\[
B_1(0)=\frac{2793}{2411704},
\]

\[
B_2(0)=\frac{8379}{21663784},
\]

\[
B_3(0)=\frac{147}{1024840},
\]

and

\[
B_4(0)=0.
\]

The first four values exceed \(10^{-4}\).

Moreover,

\[
B_i'(r)<0
\quad
(i=0,1,2,3)
\]

throughout \([0,1/8]\). Therefore every horizontal error level
\(0<\varepsilon\le10^{-4}\) intersects each \(B_0,\ldots,B_3\) exactly once.

The derivative of \(B_4\) is

\[
B_4'(r)=
-\frac{
160083(r-1)J(r)
}{
8\left(
1090048r^4-442304r^3-2290672r^2+1571780r+53361
\right)^2
}.
\]

The polynomial \(J\) has exactly one root \(r_a\) in \((0,1/8)\). Hence \(B_4\) rises from
zero, reaches the unique maximum

\[
\varepsilon_a=B_4(r_a),
\]

and returns to zero at \(r=1/8\).

---

## 3. Six globally certified bases

The support patterns are:

\[
\begin{array}{c|c|c|c}
\text{certificate}&\operatorname{supp}p&\operatorname{supp}q&
\text{third constraint}\\
\hline
\mathcal A_0&\{0,1,2,5\}&\{1,3\}&\text{inactive},\\
\mathcal A_1&\{0,1,2,5\}&\{1,2,3\}&\text{active},\\
\mathcal A_2&\{0,2,5\}&\{1,2,3,4\}&\text{active},\\
\mathcal A_3&\{0,2,3,5\}&\{1,2,4\}&\text{active},\\
\mathcal A_4&\{0,1,3,5\}&\{1,2,4\}&\text{active},\\
\mathcal A_5&\{1,3,5\}&\{0,1,2,4\}&\text{active}.
\end{array}
\]

For \(\mathcal A_1,\ldots,\mathcal A_5\), the three active observation differences have signs

\[
(+,-,+):
\]

\[
L_p(2\log2)-L_q(2\log2)=2\varepsilon,
\]

\[
L_p(3\log2)-L_q(3\log2)=-2\varepsilon,
\]

\[
L_p(\gamma\log2)-L_q(\gamma\log2)=2\varepsilon.
\]

### Affine-strip certification lemma

Every primal weight, inequality multiplier, and reduced cost in these certificates is a
rational function

\[
X(r,\varepsilon)=
\frac{a(r)\varepsilon+b(r)}
{c(r)\varepsilon+d(r)}.
\]

For a strip

\[
L(r)\le\varepsilon\le U(r),
\]

if the denominator has one strict sign at both endpoints and the numerator has the compatible
weak sign at both endpoints, then \(X\ge0\) throughout the strip. This follows because, for
fixed \(r\), both numerator and denominator are affine in \(\varepsilon\).

The audit applies this lemma to all 80 nontrivial feasibility expressions in
\(\mathcal A_1,\ldots,\mathcal A_5\). Every endpoint sign is then reduced to a univariate
polynomial sign problem on \(0\le r\le1/8\), certified by exact real-root isolation.

For \(\mathcal A_0\), all microscopic and dual quantities are nonnegative on
\(0<\varepsilon\le10^{-4}\). Its omitted third constraint is feasible exactly in the upper
layer

\[
\varepsilon\ge B_0(r).
\]

---

## 4. Exact global phase atlas

Let

\[
R_i(r,\varepsilon)
\]

be the primal–dual objective of certificate \(\mathcal A_i\). Then

\[
\boxed{
\rho_\varepsilon(r)=
\begin{cases}
R_0(\varepsilon),
&\varepsilon\ge B_0(r),\\[1mm]
R_1(r,\varepsilon),
&B_1(r)\le\varepsilon\le B_0(r),\\[1mm]
R_2(r,\varepsilon),
&B_2(r)\le\varepsilon\le B_1(r),\\[1mm]
R_3(r,\varepsilon),
&B_3(r)\le\varepsilon\le B_2(r),\\[1mm]
R_4(r,\varepsilon),
&B_4(r)\le\varepsilon\le B_3(r),\\[1mm]
R_5(r,\varepsilon),
&0<\varepsilon\le B_4(r).
\end{cases}
}
\]

The first ratio is

\[
R_0(\varepsilon)=
\frac{11233792\varepsilon+538755}{508326}.
\]

The remaining formulas are:

\[
R_1=
\frac{
495616\varepsilon r^4+123904\varepsilon r^3
+4243648\varepsilon r^2-10400080\varepsilon r
+5205868\varepsilon
-28224r^4-7056r^3+107163r^2-80262r+8379
}{
1392640\varepsilon r^4+348160\varepsilon r^3
+87040\varepsilon r^2-6401824\varepsilon r
+4283512\varepsilon
-28224r^4-7056r^3+107163r^2-80262r+8379
},
\]

\[
R_2=
-\frac{
2\left(
-14372864\varepsilon r^3+28018176\varepsilon r^2
-13099648\varepsilon r-409248\varepsilon
+3528r^4+571095r^3-1225098r^2+722799r-72324
\right)
}{
1191936\varepsilon r^4+47369728\varepsilon r^3
-105836928\varepsilon r^2+64704416\varepsilon r
-7359768\varepsilon
-28224r^4-1086624r^3+2401245r^2-1429722r+143325
},
\]

\[
R_3=
\frac{
17440768\varepsilon r^4+19735552\varepsilon r^3
-58288896\varepsilon r^2-9466048\varepsilon r
+28384208\varepsilon
-811440r^4-36162r^3+2726703r^2-2099160r+220059
}{
4\left(
9441280\varepsilon r^4+2360320\varepsilon r^3
-28829760\varepsilon r^2+13319120\varepsilon r
+3329780\varepsilon
-208152r^4+4851r^3+669438r^2-520821r+54684
\right)
},
\]

\[
R_4=
\frac{
21800960\varepsilon r^4+45749504\varepsilon r^3
-41974976\varepsilon r^2-131391536\varepsilon r
+98982900\varepsilon
-1862784r^4+208152r^3+5640831r^2-4454982r+468783
}{
2\left(
30330880\varepsilon r^4+7582720\varepsilon r^3
-62340160\varepsilon r^2-15585040\varepsilon r
+37156860\varepsilon
-963144r^4+187425r^3+2746989r^2-2203677r+232407
\right)
},
\]

and

\[
R_5=
-\frac{
-5570560\varepsilon r^3-1392640\varepsilon r^2
+18543616\varepsilon r-10865408\varepsilon
+208544r^4-26460r^3-624799r^2+494802r-52087
}{
2\left(
2125824\varepsilon r^4+1166848\varepsilon r^3
-3959936\varepsilon r^2-3690400\varepsilon r
+4062488\varepsilon
-107800r^4+22491r^3+304241r^2-244755r+25823
\right)
}.
\]

On every boundary,

\[
R_i(r,B_i(r))=
R_{i+1}(r,B_i(r)).
\]

Thus the global value is continuous for every \(\varepsilon>0\), even though the optimal
support pattern changes.

---

## 5. Global optimization over the third parameter

The first three nonconstant branches satisfy

\[
\frac{\partial R_i}{\partial r}>0
\qquad
(i=1,2,3)
\]

throughout their certified layers. Since \(r=2^{-\gamma}\) decreases with \(\gamma\), the
risk decreases as the design moves away from the duplicated anchor through
\(\mathcal A_1,\mathcal A_2,\mathcal A_3\).

For the last two branches, write

\[
\frac{\partial R_j}{\partial r}
=
-\text{(positive factor)}\,F_j(r,\varepsilon),
\qquad j=4,5,
\]

where

\[
F_j(r,\varepsilon)=C_j(r)\left[\varepsilon-E_j(r)\right],
\]

and

\[
C_j(r)<0.
\]

The stationary curves are

\[
E_5(r)=
\frac{
1323(r-1)^3(8r-1)^2
}{
16\left(
348160r^5+522240r^4-2258368r^3
+394480r^2+1826712r-1035937
\right)
},
\]

\[
E_4(r)=
\frac{
1323(r-1)^3(8r-1)^2
}{
4\left(
1516544r^5+1729792r^4-8695472r^3
+1481064r^2+7298469r-4143307
\right)
}.
\]

Both are strictly decreasing in \(r\). Their relation to the phase boundary \(B_4\) is
controlled by the same polynomial \(J\):

\[
B_4(r)-E_j(r)
\]

has the sign of \(J(r)\) up to a fixed nonzero factor. Therefore:

- for \(r>r_a\),
  \[
  B_4(r)>E_4(r),E_5(r);
  \]
- for \(r<r_a\),
  \[
  B_4(r)<E_4(r),E_5(r).
  \]

### Global regime I: \(0<\varepsilon<\varepsilon_a\)

The layer \(\mathcal A_5\) is a nonempty band bounded by the two roots of

\[
B_4(r)=\varepsilon.
\]

Inside it, the equation

\[
E_5(r)=\varepsilon
\]

has exactly one solution

\[
r_5(\varepsilon)\in(r_a,1/8).
\]

The global risk decreases before this point and increases after it, including through the
lower-\(r\) \(\mathcal A_4\) layer. Hence

\[
\boxed{
r^\star=r_5(\varepsilon)
}
\]

is the unique global minimizer.

### Global regime II: \(\varepsilon_a\le\varepsilon<\varepsilon_b\)

The \(\mathcal A_5\) layer has collapsed. The equation

\[
E_4(r)=\varepsilon
\]

has exactly one solution

\[
r_4(\varepsilon)\in[0,r_a].
\]

The global value decreases down to this point and increases afterward. Hence

\[
\boxed{
r^\star=r_4(\varepsilon)
}
\]

is the unique global minimizer.

### Global regime III: \(\varepsilon\ge\varepsilon_b\)

Since

\[
E_4(0)=\varepsilon_b
\]

and \(E_4\) is decreasing in \(r\),

\[
\varepsilon\ge E_4(r)
\quad
\forall r\in[0,r_a].
\]

The global risk therefore decreases all the way to the compactified boundary:

\[
\boxed{
r^\star=0,\qquad
\gamma^\star=\infty.
}
\]

At the benchmark

\[
\varepsilon=10^{-4},
\]

this reproduces the complete A45 theorem.

---

## 6. Small-noise global optimum

Because the A46 stationary branch is now globally certified, its asymptotic expansion becomes
the expansion of the global optimum:

\[
r^\star(\varepsilon)
=
\frac18
-
\frac{8\sqrt{174}}7\sqrt{\varepsilon}
+
\frac{19456}{147}\varepsilon
+
O(\varepsilon^{3/2}),
\]

\[
\boxed{
\gamma^\star(\varepsilon)
=
3+
\frac{64\sqrt{174}}{7\log2}\sqrt{\varepsilon}
+
\frac{913408}{147\log2}\varepsilon
+
O(\varepsilon^{3/2})
}.
\]

The global minimax ratio is

\[
\rho^\star(\varepsilon)
=
\frac{502}{499}
+
\frac{226816\sqrt{174}}{5229021}
\sqrt{\varepsilon}
+
\frac{7391973997568}{383564377413}
\varepsilon
+
O(\varepsilon^{3/2}).
\]

Therefore the singular exact-data infimum is approached through a robust boundary layer, not
by selecting the duplicated parameter itself.

---

## 7. Logical status

### Established

1. Five ordered rational curves partition the full declared
   \((r,\varepsilon)\) rectangle.
2. Six symbolic primal–dual certificates cover all six layers.
3. The direct minimax ratio is globally piecewise rational.
4. Adjacent objective formulas agree exactly on their shared boundaries.
5. The A46 regular and boundary-active stationary branches are unique global minimizers in
   their respective error regimes.
6. The compactified boundary is globally optimal exactly from
   \(\varepsilon_b\) upward.
7. The small-noise square-root law describes the global optimum.
8. A45 is recovered as the \(\varepsilon=10^{-4}\) horizontal slice.

### Not established

1. No physical support or empirical error model is inferred.
2. No parameter-dependent measurement cost is included.
3. The anchor pair \(\{2,3\}\) is still fixed rather than jointly optimized.
4. No theorem here extends automatically to continuous microscopic support.
5. No physical meaning is assigned to \(r=0\) or to the limiting functional \(p\mapsto p_0\).

---

## 8. Next rigorous target

The two-parameter third-observation problem is now closed under the finite-support contract.
The next non-ad-hoc extension is to release the anchors themselves.

A natural four-variable design problem is

\[
\{\alpha\log2,\beta\log2,\gamma\log2\},
\]

with a declared ordering and separation contract, and risk

\[
\inf_{\alpha,\beta,\gamma}
\sup_{P,Q}
\left|
Q'_{\lambda}(P)-Q'_{\lambda}(Q)
\right|.
\]

That extension should not be attempted before choosing whether the anchor parameters have
equal measurement cost and equal error. Without that contract, “jointly optimal anchors” is
not a well-defined question.
