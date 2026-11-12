# Theorem: all-dimensional small-disagreement tail for Minkowski causal-comparability edges

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem for every fixed integer spacetime dimension \(d\ge2\)  
**Physical status:** local Lorentzian geometry of arrow-erased causal comparability  
**Novelty status:** no equivalent all-dimensional UPO-oriented disagreement-tail theorem was located in the targeted review; absolute priority is not certified

## 1. Statement

Let

\[
D_d
\subset
\mathbb M^d
\]

be the unit flat Alexandrov interval with normalized volume measure.

For a comparable pair \(x\sim y\), define

\[
\Delta_d(x,y)
=
\mu(A_x\triangle A_y),
\]

where

\[
A_x=\{z:z\sim x\}.
\]

Let

\[
F_d(\varepsilon)
=
\Pr(
X\sim Y,\,
\Delta_d(X,Y)\le\varepsilon
).
\]

Then, for every fixed integer

\[
d\ge2,
\]

\[
\boxed{
F_d(\varepsilon)
=
\Theta(
\varepsilon^{\beta_d}
)
}
\]

with

\[
\boxed{
\beta_d
=
\min\!\left(
d,\,
2+\frac4d
\right).
}
\]

Thus

\[
\beta_2=2,
\]

\[
\beta_3=3,
\]

\[
\beta_4=3,
\]

and for

\[
d\ge4,
\]

\[
\beta_d
=
2+\frac4d.
\]

In particular,

\[
\boxed{
\beta_d>2
\quad
\text{for every finite integer }d\ge3.
}
\]

## 2. Exact disagreement formula

For

\[
x\prec y,
\]

the exact normalized disagreement is

\[
\boxed{
\Delta_d(x,y)
=
\frac{
\tau(p,y)^d-\tau(p,x)^d
+
\tau(x,q)^d-\tau(y,q)^d
-
2\tau(x,y)^d
}{
2^d
}.
}
\]

This identity was derived earlier from the decomposition of the common comparability region into Alexandrov subintervals.

## 3. Joint-adapted coordinates

Use

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

and

\[
A=a_y-a_x\ge0,
\qquad
B=b_x-b_y\ge0.
\]

Set

\[
m=\frac d2.
\]

Near the codimension-two null joint,

\[
\alpha,\beta,A,B\ll1.
\]

The leading endpoint-volume contribution is

\[
\boxed{
H_m
=
2^{-m}
\left[
(\alpha+A)^m-\alpha^m
+
(\beta+B)^m-\beta^m
\right].
}
\]

The interval term

\[
\tau(x,y)^d
\]

is higher order under the full joint blow-up.

## 4. Joint pair measure

The causal condition is

\[
\tau(x,y)^2
=
AB
-
2r_xr_y(1-\cos\theta)
>
0.
\]

The relative angular sphere has dimension

\[
d-2.
\]

In a sufficiently small joint chart,

\[
r_x,r_y\asymp1,
\]

and the causal angular cap has measure

\[
\Theta(
(AB)^{(d-2)/2}
).
\]

Since

\[
m-1
=
\frac{d-2}{2},
\]

the ordered-pair measure is bounded above and below, up to dimension-dependent constants, by

\[
\boxed{
(AB)^{m-1}
\,d\alpha\,d\beta\,dA\,dB.
}
\]

## 5. Lower control of the disagreement in the joint chart

For a sufficiently small fixed chart, the factors

\[
2-a,
\qquad
2-b
\]

in the exact endpoint proper-time expressions differ from \(2\) only by a controlled relative error.

Also,

\[
\tau(x,y)^d
\le
(AB)^m.
\]

Because

\[
(\alpha+A)^m-\alpha^m
\ge
A^m
\]

and similarly on the other side, the interval term can be absorbed by choosing the chart sufficiently small.

Hence

\[
\boxed{
\Delta_d
\ge
c_d
\left[
g_m(\alpha,A)
+
g_m(\beta,B)
\right],
}
\]

where

\[
g_m(u,v)
=
(u+v)^m-u^m.
\]

The corresponding upper bound also holds on a smaller chart.

Therefore the small-\(\Delta_d\) joint geometry is equivalent, up to constants, to the two independent one-side increments \(g_m\).

## 6. One-side integral

Define

\[
J_m(s)
=
\int_0^\eta
\int_0^\infty
A^{m-1}
\mathbf1_{
\{g_m(\alpha,A)\le s\}
}
\,dA\,d\alpha.
\]

For \(m>1\), rescale

\[
\alpha=s^{1/m}t,
\qquad
A=s^{1/m}u.
\]

Then

\[
J_m(s)
=
s^{1+1/m}
\int_0^{\eta s^{-1/m}}
\int_0^\infty
u^{m-1}
\mathbf1_{
\{(t+u)^m-t^m\le1\}
}
\,du\,dt.
\]

For large \(t\),

\[
u_{\max}(t)
\asymp
t^{1-m},
\]

so the inner integral behaves as

\[
t^{-m(m-1)}.
\]

Thus the large-\(t\) behavior is decided by

\[
m(m-1).
\]

### Convergent case

If

\[
m(m-1)>1,
\]

the scaled integral converges, and

\[
\boxed{
J_m(s)
=
\Theta(
s^{1+1/m}
).
}
\]

### Matching-to-bulk case

If

\[
m(m-1)<1,
\]

the scaled integral diverges polynomially at its upper cutoff

\[
t\asymp s^{-1/m}.
\]

The divergence exactly changes the total power to

\[
\boxed{
J_m(s)
=
\Theta(s^m).
}
\]

### Integer dimensions

The critical value

\[
m=\frac{1+\sqrt5}{2}
\]

does not correspond to an integer spacetime dimension.

For the integer cases:

- \(d=2\), \(m=1\), directly
  \[
  J_1(s)=\Theta(s);
  \]
- \(d=3\), \(m=3/2\),
  \[
  J_{3/2}(s)=\Theta(s^{3/2});
  \]
- \(d\ge4\),
  \[
  J_{d/2}(s)
  =
  \Theta(
  s^{1+2/d}
  ).
  \]

## 7. Joint contribution

The two null sides factor at the scaling level.

Therefore

\[
F_d^{\mathrm{joint}}(\varepsilon)
=
O(
J_m(C\varepsilon)^2
).
\]

This gives the joint exponent

\[
\beta_{\mathrm{joint}}
=
\begin{cases}
d, & d=2,3,\\[4pt]
2+\dfrac4d, & d\ge4.
\end{cases}
\]

For \(d\ge4\), restricting the scaled variables to a compact positive-measure subset of the limiting joint domain gives the matching lower bound

\[
F_d^{\mathrm{joint}}(\varepsilon)
=
\Omega(
\varepsilon^{2+4/d}
).
\]

## 8. Away from the joint

At the diagonal \(A=B=0\), the first increment coefficients are

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

and

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

For every

\[
d>2,
\]

both coefficients are strictly positive except at the null joint

\[
(\alpha,\beta)=(0,0).
\]

The \(d=2\) case is elementary and has the same bulk power.

Therefore, on every compact chart separated from the joint,

\[
\Delta_d
\ge
c(A+B)
\]

for sufficiently small comparable displacements.

The causal angular factor is

\[
(AB)^{m-1}.
\]

Thus

\[
\int_0^{C\varepsilon}
\int_0^{C\varepsilon}
(AB)^{m-1}
\,dA\,dB
=
O(\varepsilon^{2m})
=
O(\varepsilon^d).
\]

A compactness argument excludes nonlocal small-\(\Delta\) pairs on such charts.

Hence

\[
\boxed{
F_d^{\mathrm{outside\ joint}}(\varepsilon)
=
O(\varepsilon^d).
}
\]

## 9. Bulk lower bound

Choose a compact positive-volume interior set

\[
K\Subset D^\circ.
\]

For every \(x\in K\), take future timelike displacements in a fixed compact cone of coordinate scale \(O(\varepsilon)\).

Then

\[
\Delta_d(x,y)
=
O(\varepsilon),
\]

and the \(d\)-dimensional displacement volume is

\[
\Theta(\varepsilon^d).
\]

Therefore

\[
\boxed{
F_d(\varepsilon)
=
\Omega(\varepsilon^d).
}
\]

For \(d=2,3\), this lower bound gives the leading exponent.

For \(d\ge4\), the joint lower bound is larger and dominates.

Combining all sectors yields

\[
\boxed{
\beta_d
=
\min\left(
d,\,
2+\frac4d
\right).
}
\]

## 10. Uniform comparable metric-ball theorem

Define

\[
B_t(x)
=
\{z:z\sim x,\ \Delta_d(x,z)\le t\}.
\]

For every fixed integer

\[
d\ge2,
\]

\[
\boxed{
\sup_{x\in D}
\mu(B_t(x))
=
O(t^2).
}
\]

### Low-degree case

The graphon degree satisfies

\[
|Q_d(x)-Q_d(z)|
\le
\Delta_d(x,z).
\]

If

\[
Q_d(x)\le Ct
\]

and

\[
\Delta_d(x,z)\le t,
\]

then both points lie in a low-degree layer

\[
S_{C't}.
\]

The dimension-independent internal-sparsity lemma gives

\[
\mu(A_x\cap S_{C't})
=
O(t^2).
\]

### Joint-transition case

Suppose

\[
Q_d(x)>Ct
\]

while \(x\) remains in a small joint chart.

Let its two null-depth coordinates be \(a,b\).

For a future comparable point, let \(A,B\) be the causal increments.

The disagreement constraint implies one-side bounds of the form

\[
g_m(a,A)\le Ct,
\]

\[
b^m-(b-B)^m\le Ct.
\]

Define the corresponding maximal allowed increments

\[
L_t(a),
\qquad
L_t(b).
\]

For any \(u\ge0\),

\[
L_t(u)^m
\le
C
\begin{cases}
t, & u^m\le Ct,\\[4pt]
t^m u^{-m(m-1)}, & u^m>Ct.
\end{cases}
\]

The conditional comparable volume is bounded by

\[
C
L_t(a)^m
L_t(b)^m.
\]

Since

\[
Q_d(x)\asymp a^m+b^m>Ct,
\]

at least one of \(a^m,b^m\) exceeds a constant multiple of \(t\).

If only one does, the product is

\[
O(
t^{m+1}t^{-(m-1)}
)
=
O(t^2).
\]

If both do, it is

\[
O(
t^{2m}t^{-2(m-1)}
)
=
O(t^2).
\]

Thus the transition chart also satisfies the uniform bound.

All compact charts away from the joint give the stronger local order

\[
O(t^d)
\le
O(t^2).
\]

## 11. Implication-class consequence

Fix

\[
\alpha\in(1/2,1).
\]

For an edge with

\[
\delta=\Delta_d(e),
\]

the mass of splitters leading to a forced edge of disagreement at most

\[
\delta^\alpha
\]

is at most

\[
C\delta^{2\alpha}
=
o(\delta).
\]

Therefore, for sufficiently small fixed \(\delta_0\), every edge with

\[
0<\delta<\delta_0
\]

has a good-splitter region of volume at least

\[
\delta/2.
\]

The expected number \(Z_n\) of sampled low-disagreement edges having no sampled good splitter satisfies

\[
\mathbb E[Z_n]
\le
Cn^2
\int_0^{\delta_0}
e^{-cn\delta}
\,dF_d(\delta).
\]

Using

\[
F_d(\delta)
=
O(\delta^{\beta_d}),
\]

\[
\boxed{
\mathbb E[Z_n]
=
O(
n^{2-\beta_d}
).
}
\]

Hence:

### \(d=2\)

\[
\mathbb E[Z_n]=O(1),
\]

so microscopic forcing defects need not disappear.

### Every fixed \(d\ge3\)

\[
\beta_d>2,
\]

and therefore

\[
\boxed{
\mathbb E[Z_n]\to0.
}
\]

Thus, for every fixed integer spacetime dimension

\[
d\ge3,
\]

with probability tending to one every implication class reaches a fixed positive-disagreement edge core.

## 12. Dimensional transition

The arrow-erasure forcing problem has an exact threshold at spacetime dimension two:

\[
\boxed{
d=2:
\beta_2=2,
}
\]

whereas

\[
\boxed{
d\ge3:
\beta_d>2.
}
\]

This is the local geometric reason the random-\(2\)-order case can retain a nontrivial asymptotic ambiguity while all higher fixed dimensions can potentially become fully orientation-recoverable.

The remaining ingredients for an all-\(d\ge3\) theorem are global module bounds, treated separately.
