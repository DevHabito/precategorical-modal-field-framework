# Theorem: regular curved 2+1 low-degree geometry and uniform comparable-ball bound

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem under the regular-diamond hypotheses of the curved joint program  
**Physical status:** curvature-robust local estimates needed for implication-edge escalation and component control  
**Novelty status:** optical/double-null coordinates are classical; the project-specific estimates concern causal-comparability degree layers and graphon-neighborhood disagreement

## 1. Setting

Let

\[
D=I(p,q)
\]

be a compact causally convex \(2+1\)-dimensional Lorentzian Alexandrov interval satisfying the regular-joint hypotheses:

1. smooth transverse null edge \(E\);
2. no conjugate points on the relevant null generators;
3. uniform null-Fermi thin-null endpoint law;
4. regular double-null coordinates \((a,b,s)\) near \(E\);
5. smooth positive physical volume density.

Let

\[
Q(x)=\mu(A_x)
\]

be the causal-comparability graphon degree and

\[
\Delta(x,y)=\mu(A_x\triangle A_y).
\]

## 2. Curved low-degree normal form

The thin-null theorem gives uniformly along the compact edge

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

Because

\[
A_x
=
I(p,x)
\dot\cup
I(x,q)
\]

up to null boundaries,

\[
Q(x)
=
\mathcal V(p,x)
+
\mathcal V(x,q).
\]

Hence

\[
\boxed{
Q(x)
\asymp
a^{3/2}+b^{3/2}
}
\]

uniformly in a sufficiently small edge neighborhood.

Away from the edge, \(Q\) is bounded below by a positive constant.

## 3. Low-degree tail

Define

\[
g_3(q)
=
\mu\{x:Q(x)\le q\}.
\]

For sufficiently small \(q\), the low-degree set lies entirely in the edge charts.

The condition

\[
Q(x)\le q
\]

is equivalent, up to fixed constants, to

\[
a^{3/2}+b^{3/2}
\le Cq.
\]

Rescale

\[
a=q^{2/3}\bar a,
\qquad
b=q^{2/3}\bar b.
\]

The \((a,b)\)-Jacobian is

\[
q^{4/3}.
\]

The edge coordinate \(s\) ranges over finite total length and the physical volume density is smooth and bounded above and below.

Therefore

\[
\boxed{
g_3(q)
=
\Theta(q^{4/3}).
}
\]

The flat exponent survives generic regular curvature.

## 4. Low-degree internal sparsity

Let

\[
S_t
=
\{x:Q(x)\le t\}.
\]

Take

\[
x\in S_t.
\]

Then

\[
a_x,b_x
=
O(t^{2/3}).
\]

If

\[
z\in A_x\cap S_t,
\]

then likewise

\[
a_z,b_z
=
O(t^{2/3}).
\]

Write the optical-depth differences as

\[
A=|a_z-a_x|,
\qquad
B=|b_z-b_x|.
\]

The regular curved causal-cap theorem gives

\[
|s_z-s_x|
\le
C\sqrt{AB}.
\]

Since

\[
A,B
=
O(t^{2/3}),
\]

the allowed tangential width is

\[
O(t^{2/3}).
\]

Thus the available \(z\)-volume is bounded by

\[
O(t^{2/3})
\cdot
O(t^{2/3})
\cdot
O(t^{2/3}).
\]

Hence

\[
\boxed{
\sup_{x\in S_t}
\mu(A_x\cap S_t)
=
O(t^2).
}
\]

This reproduces the flat internal-sparsity exponent without flat symmetry.

## 5. Degree difference is controlled by disagreement

For every graphon kernel,

\[
Q(x)
=
\int W(x,z)\,d\mu(z).
\]

Therefore

\[
\begin{aligned}
|Q(x)-Q(y)|
&\le
\int
|W(x,z)-W(y,z)|
\,d\mu(z)\\
&=
\Delta(x,y).
\end{aligned}
\]

Thus

\[
\boxed{
|Q(x)-Q(y)|
\le
\Delta(x,y).
}
\]

This is curvature independent.

## 6. Comparable metric balls

Define

\[
B_t(x)
=
\{z:z\sim x,\ \Delta(x,z)\le t\}.
\]

We prove

\[
\boxed{
\sup_{x\in D}
\mu(B_t(x))
=
O(t^2).
}
\]

There are three regimes.

## 7. Low-degree root

If

\[
Q(x)\le4t
\]

and

\[
z\in B_t(x),
\]

then

\[
Q(z)
\le
Q(x)+\Delta(x,z)
\le
5t.
\]

Therefore

\[
B_t(x)
\subseteq
A_x\cap S_{5t}.
\]

Internal sparsity gives

\[
\mu(B_t(x))
=
O(t^2).
\]

## 8. Joint-transition root

Now suppose

\[
Q(x)>4t
\]

but \(x\) lies in a small joint chart.

Write its optical depths as

\[
a,b.
\]

For a nearby comparable point, let \(A,B\) be the causal increments.

The endpoint-volume normal form implies that the one-side increment constraint is, up to fixed positive constants,

\[
(a+A)^{3/2}-a^{3/2}
\lesssim t,
\]

and similarly for \(b,B\).

Let \(L_t(a)\) be the maximal allowed \(A\).

Then

\[
\boxed{
L_t(a)^{3/2}
\le
C
\min\left(
t,
t^{3/2}a^{-3/4}
\right).
}
\]

To see this:

- if \(a^{3/2}\lesssim t\), then \(A^{3/2}\lesssim t\);
- if \(a^{3/2}\gg t\), the mean-value theorem gives
  \[
  A\lesssim t\,a^{-1/2}.
  \]

The curved causal-cap width is

\[
O(\sqrt{AB}).
\]

Therefore the conditional comparable volume is bounded by

\[
C
L_t(a)^{3/2}
L_t(b)^{3/2}.
\]

Set

\[
q_a=a^{3/2},
\qquad
q_b=b^{3/2}.
\]

Since

\[
Q(x)\asymp q_a+q_b>4t,
\]

at least one of \(q_a,q_b\) is at least a fixed multiple of \(t\).

### One side below the t-scale

If

\[
q_a\lesssim t,
\qquad
q_b\gtrsim t,
\]

then

\[
L_t(a)^{3/2}
\lesssim t,
\]

and

\[
L_t(b)^{3/2}
\lesssim
t^{3/2}q_b^{-1/2}
\lesssim t.
\]

Hence the product is

\[
O(t^2).
\]

### Both sides above the t-scale

If

\[
q_a,q_b\gtrsim t,
\]

then

\[
L_t(a)^{3/2}
L_t(b)^{3/2}
\lesssim
t^3(q_aq_b)^{-1/2}.
\]

Since both factors are at least order \(t\),

\[
(q_aq_b)^{-1/2}
\lesssim
t^{-1}.
\]

Thus again

\[
O(t^2).
\]

Therefore the entire joint-transition regime obeys the uniform bound.

## 9. Compact bulk charts

Away from the edge, the volume-time differential is uniformly timelike on compact subsets.

Hence

\[
\Delta(x,\exp_x h)
\asymp
|h|
\]

for sufficiently small comparable displacements.

The local spacetime volume satisfying

\[
\Delta\le t
\]

is therefore

\[
O(t^3).
\]

Since

\[
t^3\le t^2
\]

for small \(t\), compact bulk charts are strictly better than required.

A finite cover completes the proof.

## 10. Uniform theorem

Combining the three regimes,

\[
\boxed{
\sup_{x\in D}
\mu
\{z:z\sim x,\ \Delta(x,z)\le t\}
=
O(t^2).
}
\]

This is the same exponent as in the flat \(2+1\) diamond.

## 11. Implication-edge consequence

The matched curved small-disagreement theorem gives

\[
F_{3,g}(t)
=
\Theta(t^3).
\]

Fix

\[
\alpha\in(1/2,1).
\]

For an edge of disagreement \(\delta\), splitters leading only to a forced edge with disagreement at most

\[
\delta^\alpha
\]

lie in a union of two comparable metric balls.

Their mass is

\[
O(\delta^{2\alpha})
=
o(\delta).
\]

Therefore the flat implication-edge escalation argument transfers:

\[
\boxed{
\Pr(
\text{a low-disagreement sampled edge fails to reach the core}
)
=
O(n^{-1})
}
\]

at the crude all-edge level, and the non-twin residual refinement gives

\[
\boxed{
O(n^{-2})
}
\]

after zero-splitter true twins are separated.

Thus local forcing defects other than true twins remain subleading to the \(n^{-1}\) twin scale.

## 12. Consequence for the curved program

Under the regular-diamond hypotheses, the following flat exponents have now been transported to curved \(2+1\):

\[
\boxed{
g_3(q)=\Theta(q^{4/3}),
}
\]

\[
\boxed{
\sup_{x\in S_t}
\mu(A_x\cap S_t)=O(t^2),
}
\]

\[
\boxed{
\sup_x\mu(B_t(x))=O(t^2),
}
\]

and

\[
\boxed{
F_{3,g}(t)\sim C_{3,g}t^3.
}
\]

Together with curvature-independent graphon primeness, these close most of the local geometric input required for full curved orientation recovery.

## 13. Remaining local input

The principal unresolved estimate is now the timelike-tip co-degree geometry needed for quantitative near-whole-module suppression.

Specifically, one needs a curved analogue of

\[
\bar g_3(r)
=
\Theta(r^3)
\]

and a tip middle-band lemma ensuring that a fixed fraction of the nonneighbor region of a near-universal vertex has graphon degree bounded away from \(0\) and \(1\).

Those are local shape-derivative questions near the tips \(p\) and \(q\), not null-joint questions.
