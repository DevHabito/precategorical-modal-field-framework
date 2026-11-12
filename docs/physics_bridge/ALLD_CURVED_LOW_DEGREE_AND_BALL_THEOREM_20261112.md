# Theorem: regular curved all-dimensional low-degree geometry and comparable-ball bound

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem under the regular curved null-edge hypotheses  
**Physical status:** transports the degree-tail and local-forcing exponents from flat Minkowski space to regular curved causal diamonds

## 1. Setting

Let

\[
D=I(p,q)
\]

be a regular curved Alexandrov interval in fixed integer spacetime dimension

\[
d\ge3.
\]

Assume a compact smooth transverse null edge \(E\), regular double-null coordinates, and the thin-null endpoint-volume law

\[
\mathcal V(p,x)
=
c_+(s)a^{d/2}[1+o(1)],
\]

\[
\mathcal V(x,q)
=
c_-(s)b^{d/2}[1+o(1)],
\]

uniformly along the edge, with positive bounded coefficients.

Set

\[
m=\frac d2.
\]

Let

\[
Q(x)=\mu(A_x)
\]

be the causal-comparability graphon degree.

## 2. Degree normal form

Near the edge,

\[
A_x
=
I(p,x)\dot\cup I(x,q)
\]

up to null boundaries.

Therefore

\[
\boxed{
Q(x)
=
c_+(s)a^m
+
c_-(s)b^m
+
o(a^m+b^m).
}
\]

In particular,

\[
\boxed{
Q(x)
\asymp
a^m+b^m.
}
\]

Away from the edge, \(Q\) is bounded below by a positive constant.

## 3. Low-degree tail

Define

\[
g_{d,g}(q)
=
\mu\{x:Q(x)\le q\}.
\]

For small \(q\), the relevant set lies in the edge charts.

Rescale

\[
a=q^{1/m}\bar a,
\qquad
b=q^{1/m}\bar b.
\]

Since

\[
\frac1m=\frac2d,
\]

the optical Jacobian contributes

\[
q^{2/m}
=
q^{4/d}.
\]

The edge coordinates range over finite measure and the physical density is smooth.

Hence

\[
\boxed{
g_{d,g}(q)
=
\Theta(q^{4/d}).
}
\]

More precisely, there is a positive finite coefficient obtained by integrating the local weighted \(L^m\)-quarter-ball volume along \(E\).

## 4. Low-degree layer scale

Let

\[
S_t=\{x:Q(x)\le t\}.
\]

For

\[
x\in S_t,
\]

the optical depths satisfy

\[
a_x,b_x
=
O(t^{1/m})
=
O(t^{2/d}).
\]

The same holds for every

\[
z\in S_t.
\]

Thus the available two optical coordinates for \(z\) have total scale

\[
O(t^{2/m})
=
O(t^{4/d}).
\]

## 5. Tangential causal cap

For two nearby points with optical differences \(A,B\), the regular double-null metric gives

\[
h_{AB}\xi^A\xi^B
\lesssim
AB.
\]

Inside \(S_t\),

\[
A,B
=
O(t^{1/m}).
\]

Therefore

\[
AB
=
O(t^{2/m}).
\]

The radius of the allowed tangential ellipsoid is

\[
O(t^{1/m}).
\]

Its dimension is

\[
d-2.
\]

Hence its volume is

\[
O(
t^{(d-2)/m}
)
=
O(
t^{2(d-2)/d}
).
\]

## 6. Internal low-degree sparsity

Multiplying the optical and tangential factors,

\[
t^{4/d}
t^{2(d-2)/d}
=
t^2.
\]

Therefore

\[
\boxed{
\sup_{x\in S_t}
\mu(
A_x\cap S_t
)
=
O(t^2).
}
\]

The exponent is independent of \(d\).

## 7. Degree-disagreement inequality

For every graphon,

\[
Q(x)
=
\int W(x,z)\,d\mu(z).
\]

Thus

\[
\boxed{
|Q(x)-Q(y)|
\le
\Delta(x,y).
}
\]

No curvature assumption is involved.

## 8. Comparable metric balls

Define

\[
B_t(x)
=
\{
z:
z\sim x,\,
\Delta(x,z)\le t
\}.
\]

We prove

\[
\boxed{
\sup_x
\mu(B_t(x))
=
O(t^2).
}
\]

## 9. Low-degree root

If

\[
Q(x)\le Ct,
\]

then for

\[
z\in B_t(x),
\]

\[
Q(z)
\le
Q(x)+t
\le
C't.
\]

Therefore

\[
B_t(x)
\subseteq
A_x\cap S_{C't}.
\]

Internal sparsity gives

\[
\mu(B_t(x))
=
O(t^2).
\]

## 10. Joint-transition root

Now let \(x\) lie in a joint chart with optical depths \(a,b\).

For a nearby comparable \(z\), let \(A,B\) be the positive causal increments.

The endpoint-volume increment on one side obeys

\[
(a+A)^m-a^m
\lesssim
t.
\]

Let \(L_t(a)\) be the maximal allowed \(A\).

Then

\[
\boxed{
L_t(a)^m
\le
C
\min\left(
t,\,
t^m(a^m)^{-(m-1)}
\right).
}
\]

Indeed:

### Core side

If

\[
a^m\lesssim t,
\]

then

\[
A^m\lesssim t.
\]

### Linear side

If

\[
a^m\gg t,
\]

the mean-value theorem gives

\[
A
\lesssim
t a^{1-m},
\]

hence

\[
A^m
\lesssim
t^m
(a^m)^{-(m-1)}.
\]

The same holds for \(b,B\).

## 11. Conditional comparable volume

The pair cap measure contains

\[
(AB)^{m-1}.
\]

Integrating

\[
A\in[0,L_t(a)],
\qquad
B\in[0,L_t(b)]
\]

gives

\[
\boxed{
\mu(B_t(x))
\le
C
L_t(a)^m
L_t(b)^m.
}
\]

Let

\[
q_a=a^m,
\qquad
q_b=b^m.
\]

If \(x\) is not in the low-degree case, then

\[
q_a+q_b
\gtrsim
t.
\]

### One side small

If

\[
q_a\lesssim t,
\qquad
q_b\gtrsim t,
\]

then

\[
L_t(a)^m
\lesssim t,
\]

and

\[
L_t(b)^m
\lesssim
t^m q_b^{-(m-1)}
\lesssim
t.
\]

Thus the product is

\[
O(t^2).
\]

### Both sides large

If

\[
q_a,q_b\gtrsim t,
\]

then

\[
L_t(a)^m
L_t(b)^m
\lesssim
t^{2m}
(q_aq_b)^{-(m-1)}
\lesssim
t^{2m}
t^{-2(m-1)}
=
t^2.
\]

Therefore the entire joint-transition regime satisfies

\[
O(t^2).
\]

## 12. Bulk charts

Away from the null edge, assume the finite-diamond volume function has nondegenerate temporal first variation.

Then

\[
\Delta(x,\exp_x h)
\asymp
|h|
\]

for sufficiently small timelike \(h\).

The local \(d\)-dimensional cone volume is

\[
O(t^d).
\]

For

\[
d\ge2,
\]

\[
t^d
\le
t^2
\]

at small \(t\).

Thus bulk charts are no worse than the joint bound.

## 13. Uniform theorem

Combining all regimes,

\[
\boxed{
\sup_{x\in D}
\mu
\{
z:z\sim x,\,
\Delta(x,z)\le t
\}
=
O(t^2).
}
\]

The exponent is dimension independent.

## 14. Consequence for forcing escalation

If the small-edge tail is

\[
F(t)=O(t^{\beta}),
\]

with

\[
\beta>2,
\]

then the bad-splitter mass for an edge of disagreement \(\delta\) is

\[
O(\delta^{2\alpha})
\]

for any

\[
\alpha>1/2.
\]

Therefore the implication-edge escalation proof depends only on the inequality

\[
\beta>2.
\]

For regular curved diamonds:

\[
d=3:
\quad
\beta=3,
\]

and

\[
d\ge4:
\quad
\beta=2+\frac4d>2.
\]

Thus the local forcing mechanism survives curvature in every fixed dimension \(d\ge3\).

## 15. Structural interpretation

Two universal exponents combine:

\[
\text{optical-depth area}
=
t^{4/d},
\]

and

\[
\text{codimension-two tangential cap}
=
t^{2(d-2)/d}.
\]

Their sum is always

\[
2.
\]

Hence

\[
\boxed{
\text{internal low-degree sparsity exponent}
=
2
}
\]

is a codimension-two Lorentzian scaling law rather than a flat-space coincidence.
