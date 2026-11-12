# Theorem: bulk-controlled small-edge tail and implication escalation in 2+1 Minkowski sprinklings

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem  
**Physical status:** transitive-orientation forcing after arrow erasure in \(2+1\)-dimensional Minkowski spacetime  
**Novelty status:** no equivalent Minkowski-sprinkling UPO/edge-disagreement theorem was located in the targeted review; absolute priority is not certified

## 1. Setting

Let

\[
D\subset\mathbb M^3
\]

be the unit flat Alexandrov interval with normalized volume measure.

For a comparable pair \(x\sim y\), define

\[
\Delta(x,y)
=
\mu(A_x\triangle A_y).
\]

Let

\[
F_3(\varepsilon)
=
\Pr(
X\sim Y,\,
\Delta(X,Y)\le\varepsilon
).
\]

Then

\[
\boxed{
F_3(\varepsilon)
=
\Theta(\varepsilon^3).
}
\]

Unlike \(d=4\), the leading exponent is bulk-controlled rather than null-joint-controlled.

## 2. General pair coordinates

Use null-waist coordinates

\[
a=1-r+t,
\qquad
b=1-r-t.
\]

For an ordered comparable pair \(x\prec y\), write

\[
a_x=\alpha,
\qquad
b_y=\beta,
\]

\[
A=a_y-a_x\ge0,
\qquad
B=b_x-b_y\ge0.
\]

Let

\[
m=\frac d2=\frac32.
\]

Near the null joint, the endpoint-volume part of the disagreement has leading form

\[
H_{3}
=
2^{-3/2}
\left[
(\alpha+A)^{3/2}-\alpha^{3/2}
+
(\beta+B)^{3/2}-\beta^{3/2}
\right].
\]

The interval term involving \(\tau(x,y)^3\) is higher order in the full joint blow-up.

The causal angular cap in \(2+1\) has one relative angular dimension and contributes

\[
(AB)^{1/2}.
\]

## 3. One-side small-increment integral

Define

\[
J(s)
=
\int_0^\eta
\int_0^\infty
A^{1/2}
\mathbf1_{\{
(\alpha+A)^{3/2}-\alpha^{3/2}\le s
\}}
\,dA\,d\alpha.
\]

Split the \(\alpha\)-integral at

\[
\alpha=s^{2/3}.
\]

### 3.1 Very near the joint

If

\[
0\le\alpha\le s^{2/3},
\]

then the constraint implies

\[
A=O(s^{2/3}).
\]

Hence this region contributes at most

\[
O(s^{2/3})
\int_0^{Cs^{2/3}}
A^{1/2}\,dA
=
O(s^{5/3}).
\]

### 3.2 Matching into the bulk

If

\[
\alpha\ge s^{2/3},
\]

the mean-value theorem gives

\[
(\alpha+A)^{3/2}-\alpha^{3/2}
\ge
c\alpha^{1/2}A
\]

through the relevant small-increment range.

Thus

\[
A
\le
Cs\alpha^{-1/2}.
\]

Therefore

\[
\begin{aligned}
J_{\mathrm{outer}}(s)
&\le
C
\int_{s^{2/3}}^\eta
\left(
s\alpha^{-1/2}
\right)^{3/2}
\,d\alpha\\
&=
Cs^{3/2}
\int_{s^{2/3}}^\eta
\alpha^{-3/4}\,d\alpha\\
&=
O(s^{3/2}).
\end{aligned}
\]

Hence

\[
\boxed{
J(s)=O(s^{3/2}).
}
\]

## 4. Joint-neighborhood upper bound

The two null sides are independent at leading order in the pair measure.

Therefore the joint-neighborhood contribution satisfies

\[
F_3^{\mathrm{joint}}(\varepsilon)
=
O(
J(C\varepsilon)^2
)
=
O(\varepsilon^3).
\]

The fully homogeneous joint scaling alone would give the higher exponent

\[
2+\frac43
=
\frac{10}{3},
\]

but its large scaled-depth tail matches continuously onto the ordinary bulk and restores the exponent \(3\).

This is why \(d=3\) is bulk-controlled.

## 5. Away from the null joint

At the diagonal \(A=B=0\), the first derivatives of the disagreement are

\[
c_A(\alpha,\beta)
=
2^{-d}m
\left[
(2-\beta)
\{\alpha(2-\beta)\}^{m-1}
+
\beta
\{\beta(2-\alpha)\}^{m-1}
\right],
\]

and symmetrically

\[
c_B(\alpha,\beta)
=
2^{-d}m
\left[
\alpha
\{\alpha(2-\beta)\}^{m-1}
+
(2-\alpha)
\{\beta(2-\alpha)\}^{m-1}
\right].
\]

For

\[
m=\frac32,
\]

both are strictly positive away from

\[
(\alpha,\beta)=(0,0).
\]

On every compact chart separated from the joint,

\[
\Delta
\ge
c(A+B)
\]

for sufficiently small comparable displacement.

The causal angular factor is

\[
(AB)^{1/2}.
\]

Therefore the comparable-pair volume satisfying

\[
\Delta\le\varepsilon
\]

is

\[
O(\varepsilon^3)
\]

on each such chart.

A finite chart cover gives

\[
F_3(\varepsilon)=O(\varepsilon^3).
\]

## 6. Lower bound

Choose a compact positive-volume interior region

\[
K\Subset D^\circ
\]

away from all boundaries.

For every \(x\in K\), choose future timelike displacements in a fixed compact cone whose coordinate size is \(O(\varepsilon)\).

The disagreement is Lipschitz in this chart:

\[
\Delta(x,y)\le C\varepsilon.
\]

The \(3\)-dimensional displacement volume is

\[
\Theta(\varepsilon^3).
\]

Integrating over \(x\in K\) gives

\[
F_3(\varepsilon)
=
\Omega(\varepsilon^3).
\]

Combining upper and lower bounds,

\[
\boxed{
F_3(\varepsilon)
=
\Theta(\varepsilon^3).
}
\]

No leading constant is required for the orientation-recovery argument.

## 7. Uniform comparable metric-ball bound

Define

\[
B_t(x)
=
\{z:z\sim x,\ \Delta(x,z)\le t\}.
\]

Then

\[
\boxed{
\sup_{x\in D}
\mu(B_t(x))
=
O(t^2).
}
\]

### Low-degree chart

The degree function satisfies

\[
|Q_3(x)-Q_3(z)|
\le
\Delta(x,z).
\]

If

\[
Q_3(x)\le4t
\]

and

\[
\Delta(x,z)\le t,
\]

then

\[
Q_3(z)\le5t.
\]

The dimension-independent low-degree internal-sparsity estimate gives

\[
\mu(A_x\cap S_{5t})
=
O(t^2).
\]

### Two-sided joint transition

If both null-depth coordinates have the same small scale and

\[
Q_3(x)=q>4t,
\]

the linear coefficients have order

\[
q^{1/3}.
\]

Thus

\[
A,B
=
O(tq^{-1/3}).
\]

Integrating the angular-weighted measure

\[
(AB)^{1/2}\,dA\,dB
\]

gives

\[
O(t^3/q)
\le
O(t^2).
\]

### One-sided null-face transition

Suppose one null-depth coordinate vanishes to leading order while the other gives

\[
Q_3(x)\asymp q.
\]

The exact disagreement retains both:

- a nonlinear term \(A^{3/2}\);
- a linear opposite-cone term \(qA\).

The other causal increment satisfies

\[
B=O(tq^{-1/3}).
\]

If

\[
t\le q\le t^{1/3},
\]

then

\[
A=O(t^{2/3}),
\]

and the angular-weighted volume is

\[
O(t^{5/2}q^{-1/2})
\le
O(t^2).
\]

If

\[
q\ge t^{1/3},
\]

then

\[
A=O(t/q),
\]

and the volume is

\[
O(t^3q^{-2})
\le
O(t^{7/3}).
\]

All remaining compact charts are better.

Hence the uniform \(O(t^2)\) bound follows.

## 8. Edge escalation

Fix

\[
\alpha\in(1/2,1).
\]

Let \(e=\{x,y\}\) be a comparable edge with

\[
\delta=\Delta(e).
\]

A splitter is bad if the directly forced new edge has disagreement at most

\[
\delta^\alpha.
\]

The metric-ball theorem gives

\[
\mu(\text{bad splitters})
\le
C\delta^{2\alpha}
=
o(\delta).
\]

Thus, for sufficiently small fixed \(\delta_0\), every edge with

\[
0<\delta<\delta_0
\]

has a good-splitter region of volume at least

\[
\delta/2.
\]

The probability that a sampled edge has no sampled good splitter is at most

\[
e^{-cn\delta}.
\]

Using

\[
F_3(\delta)=O(\delta^3),
\]

the expected number \(Z_n\) of low-disagreement sampled edges that fail to escalate satisfies

\[
\begin{aligned}
\mathbb E[Z_n]
&\le
\binom n2
\int_0^{\delta_0}
e^{-cn\delta}
\,dF_3(\delta)\\
&=
O(n^{-1}).
\end{aligned}
\]

Therefore

\[
\boxed{
\Pr(Z_n>0)\to0.
}
\]

With probability tending to one, every implication class reaches a fixed positive-disagreement edge core

\[
\mathcal E_{\mathrm{core}}
=
\{e:\Delta(e)\ge\delta_0\}.
\]

## 9. Dimensional contrast

The small-edge exponents now read

\[
d=2:
\qquad
\beta_2=2,
\]

\[
d=3:
\qquad
\beta_3=3,
\]

\[
d=4:
\qquad
\beta_4=3.
\]

The \(d=2\) value sits exactly at the \(O(n^2)\)-edge union-bound threshold and is consistent with a nontrivial limiting UPO probability.

For \(d=3,4\),

\[
\beta_d>2,
\]

so microscopic implication-class defects disappear.

The geometric mechanisms differ:

\[
d=3:
\text{ bulk-controlled},
\]

\[
d=4:
\text{ null-joint-controlled}.
\]

## 10. Current consequence

The component problem in \(d=3\) is already closed by the general non-isolated giant theorem, and in fact the stronger Hladký–Viswanathan graphon connectivity theorem applies because

\[
g_3(q)=o(q).
\]

The causal graphon is prime in every fixed dimension.

Thus, after the present edge-escalation theorem, the remaining \(2+1\) task is only the analogue of the near-whole-module exclusion.

That step depends on the \(d=3\) low-degree tail

\[
g_3(q)=\Theta(q^{4/3}),
\]

the timelike-tip co-degree tail

\[
\bar g_3(r)=\Theta(r^3),
\]

and the same internal-sparsity estimate

\[
\mu(A_x\cap S_t)=O(t^2).
\]

Those exponents are favorable, so the final \(2+1\) recovery theorem is the next target.
