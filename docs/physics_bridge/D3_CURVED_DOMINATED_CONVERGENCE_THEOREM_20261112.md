# Theorem: dominated-convergence closure of the curved 2+1 bulk coefficient

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic domination theorem under the regular curved-diamond hypotheses  
**Physical status:** closes the measure-theoretic matching gap in the curved \(2+1\) small-disagreement law

## 1. Goal

For a regular curved \(2+1\) Alexandrov interval, define

\[
P_\varepsilon(x)
=
\mu\{
y:
y\sim x,\,
\Delta(x,y)\le\varepsilon
\}.
\]

For almost every interior \(x\), the local volume-time calculation gives

\[
\frac{P_\varepsilon(x)}{\varepsilon^3}
\longrightarrow
\frac{
2\pi
}{
3V_D
}
\kappa(x)^{-3},
\]

after both time orientations are included in the global pair integral.

To interchange the limit and the \(x\)-integration, it is enough to prove an integrable bound

\[
\boxed{
P_\varepsilon(x)
\le
C\varepsilon^3\kappa(x)^{-3}
}
\]

near the null edge, together with the obvious compact-bulk bound.

This note proves that domination.

## 2. Regular joint coordinates

Near the smooth transverse null edge use optical coordinates

\[
(a,b,s).
\]

The endpoint-volume laws are

\[
\mathcal V(p,x)
=
c_+(s)a^{3/2}
+
O(a^2),
\]

\[
\mathcal V(x,q)
=
c_-(s)b^{3/2}
+
O(b^2),
\]

with positive bounded coefficients.

The volume-time norm satisfies

\[
\boxed{
\kappa(x)^{-3}
\asymp
(ab)^{-3/4}.
}
\]

## 3. One-side increment bound

Let \(A\ge0\) be the optical increment on the \(a\)-side.

The disagreement constraint implies

\[
(a+A)^{3/2}-a^{3/2}
\le
C\varepsilon.
\]

Let \(L_\varepsilon(a)\) be the largest allowed \(A\).

Then uniformly,

\[
\boxed{
L_\varepsilon(a)^{3/2}
\le
C
\min\left(
\varepsilon,\,
\varepsilon^{3/2}a^{-3/4}
\right).
}
\]

Indeed:

### Core side

If

\[
a\le C\varepsilon^{2/3},
\]

then monotonicity gives

\[
A^{3/2}
\le
C\varepsilon,
\]

so

\[
L_\varepsilon(a)^{3/2}
\le
C\varepsilon.
\]

### Linear side

If

\[
a>C\varepsilon^{2/3},
\]

the mean-value theorem gives

\[
(a+A)^{3/2}-a^{3/2}
\ge
c a^{1/2}A,
\]

hence

\[
A
\le
C\varepsilon a^{-1/2}.
\]

Raising to the \(3/2\) power gives

\[
L_\varepsilon(a)^{3/2}
\le
C
\varepsilon^{3/2}
a^{-3/4}.
\]

The same bound holds on the \(b\)-side.

## 4. Curved causal-cap volume

For a nearby comparable pair, let \(A,B\) be the two optical increments.

The regular double-null cap law gives tangential width

\[
|\xi|
\le
C\sqrt{AB}.
\]

The physical volume density is smooth and bounded in the compact edge charts.

Therefore the conditional \(y\)-volume is bounded by

\[
\boxed{
P_\varepsilon(x)
\le
C
L_\varepsilon(a)^{3/2}
L_\varepsilon(b)^{3/2}.
}
\]

The exponent \(3/2\) on each side comes from one optical increment times the square-root tangential cap.

## 5. Global edge majorant

We now show

\[
L_\varepsilon(a)^{3/2}
L_\varepsilon(b)^{3/2}
\le
C
\varepsilon^3
(ab)^{-3/4}
\]

in every regime.

### Both sides linear

If

\[
a,b
\ge
C\varepsilon^{2/3},
\]

then directly

\[
L_\varepsilon(a)^{3/2}
L_\varepsilon(b)^{3/2}
\le
C
\varepsilon^3
(ab)^{-3/4}.
\]

### One side in the core

Suppose

\[
a\le C\varepsilon^{2/3},
\qquad
b\ge C\varepsilon^{2/3}.
\]

Then

\[
L_\varepsilon(a)^{3/2}
L_\varepsilon(b)^{3/2}
\le
C
\varepsilon^{5/2}
b^{-3/4}.
\]

But

\[
a\le C\varepsilon^{2/3}
\]

implies

\[
a^{-3/4}
\ge
c\varepsilon^{-1/2}.
\]

Therefore

\[
\varepsilon^{5/2}b^{-3/4}
\le
C
\varepsilon^3
a^{-3/4}
b^{-3/4}.
\]

The opposite case is identical.

### Both sides in the core

If

\[
a,b
\le
C\varepsilon^{2/3},
\]

then

\[
L_\varepsilon(a)^{3/2}
L_\varepsilon(b)^{3/2}
\le
C\varepsilon^2.
\]

Also

\[
(ab)^{-3/4}
\ge
c\varepsilon^{-1}.
\]

Hence

\[
\varepsilon^2
\le
C
\varepsilon^3
(ab)^{-3/4}.
\]

Thus in every edge regime,

\[
\boxed{
P_\varepsilon(x)
\le
C
\varepsilon^3
(ab)^{-3/4}.
}
\]

Using

\[
(ab)^{-3/4}
\asymp
\kappa(x)^{-3},
\]

we obtain

\[
\boxed{
P_\varepsilon(x)
\le
C
\varepsilon^3
\kappa(x)^{-3}.
}
\]

## 6. Integrability

Near the edge,

\[
\kappa(x)^{-3}
\asymp
(ab)^{-3/4}.
\]

Therefore

\[
\int_0^\eta
\int_0^\eta
(ab)^{-3/4}
\,da\,db
=
16\eta^{1/2}
<
\infty.
\]

The edge coordinate ranges over finite length and the volume density is bounded.

Thus

\[
\boxed{
\kappa^{-3}\in L^1(D,\mu).
}
\]

## 7. Compact bulk domination

Away from the edge, \(\kappa\) is bounded below on every compact chart.

The local temporal-gradient estimate gives

\[
P_\varepsilon(x)
\le
C_K\varepsilon^3.
\]

Since

\[
\kappa^{-3}
\]

is bounded above and below there, the same global domination can be enlarged to cover the entire diamond:

\[
\boxed{
\frac{
P_\varepsilon(x)
}{
\varepsilon^3
}
\le
C
\left[
1+\kappa(x)^{-3}
\right].
}
\]

The right-hand side is integrable.

## 8. Pointwise limit

For every interior point with

\[
\kappa(x)>0,
\]

Riemann normal coordinates and the volume-time first variation give

\[
\Delta(x,\exp_x h)
=
d\Phi_x(h)
+
O(|h|^2).
\]

Hence

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\frac{
P_\varepsilon(x)
}{
\varepsilon^3
}
=
\frac{
2\pi
}{
3V_D
}
\kappa(x)^{-3},
}
\]

with the convention appropriate to the two time orientations in the pair integral.

The null edge itself has measure zero.

## 9. Dominated convergence

The pointwise limit and the integrable majorant imply

\[
\begin{aligned}
\lim_{\varepsilon\downarrow0}
\frac{
F_{3,g}(\varepsilon)
}{
\varepsilon^3
}
&=
\int_D
\lim_{\varepsilon\downarrow0}
\frac{
P_\varepsilon(x)
}{
\varepsilon^3
}
\,d\mu(x)\\
&=
\boxed{
\frac{
2\pi
}{
3V_D
}
\int_D
\kappa(x)^{-3}\,d\mu(x).
}
\end{aligned}
\]

Thus

\[
\boxed{
F_{3,g}(\varepsilon)
\sim
C_{3,g}\varepsilon^3
}
\]

with the intrinsic coefficient already identified.

No separate \(\eta\)-matching limit is needed.

## 10. Consequence for the audit

The earlier curved audit listed a missing publication-level dominated-convergence theorem for the bulk/joint matching.

The present estimate supplies that theorem under the same regular-joint assumptions.

The second of the three major geometric proof obligations is therefore closed.

The remaining principal obligation is the tip middle-band swept-volume estimate.
