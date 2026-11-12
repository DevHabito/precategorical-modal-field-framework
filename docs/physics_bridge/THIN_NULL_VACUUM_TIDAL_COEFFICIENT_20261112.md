# Proposition: universal vacuum tidal correction to the thin-null volume coefficient

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic Jacobi-determinant proposition  
**Scope:** regular conjugate-free null segments; quadratic locally constant tidal response  
**Purpose:** isolate the universal focusing contribution entering the curved volume-null edge functional

## 1. Setting

Let

\[
\gamma:[0,U]\to(M^d,g)
\]

be a regular null geodesic segment.

The transverse screen dimension is

\[
r=d-2.
\]

Work in a parallel screen frame.

Let the transverse Jacobi matrix \(B(t)\) satisfy

\[
\boxed{
B''(t)=H(t)B(t),
}
\]

with

\[
B(0)=0,
\qquad
B'(0)=I_r.
\]

For the local vacuum tidal calculation, freeze the leading tidal matrix along the segment:

\[
H(t)=H+O(U\nabla H).
\]

In vacuum,

\[
\operatorname{Tr}H=0.
\]

We calculate the universal quadratic contribution in \(H\).

## 2. Constant tidal Jacobi expansion

For constant \(H\),

\[
\boxed{
B(t)
=
t
\left[
I
+
\frac{t^2}{6}H
+
\frac{t^4}{120}H^2
+
O(t^6H^3)
\right].
}
\]

Set

\[
X(t)
=
\frac{t^2}{6}H
+
\frac{t^4}{120}H^2
+\cdots.
\]

Then

\[
\log\det(I+X)
=
\operatorname{Tr}X
-
\frac12\operatorname{Tr}X^2
+\cdots.
\]

Because

\[
\operatorname{Tr}H=0,
\]

the \(t^2\) term vanishes.

At order \(t^4\),

\[
\frac1{120}
-
\frac1{72}
=
-\frac1{180}.
\]

Hence

\[
\boxed{
\det B(t)
=
t^{d-2}
\left[
1
-
\frac{
\operatorname{Tr}(H^2)
}{180}
t^4
+
O(t^6H^3)
\right].
}
\]

Therefore

\[
\boxed{
\sqrt{\det B(t)}
=
t^{d/2-1}
\left[
1
-
\frac{
\operatorname{Tr}(H^2)
}{360}
t^4
+
O(t^6H^3)
\right].
}
\]

## 3. Thin-null coefficient from Jacobi determinants

For a symmetric plane-wave model, and more generally for the locally frozen quadratic tidal problem, the thin-null interval coefficient has the Jacobi-determinant form

\[
\boxed{
c_H(U)
\propto
\frac1{
\sqrt{\det B(U)}
}
\int_0^U
\sqrt{
\det B(u)
\det B(U-u)
}
\,du.
}
\]

All prefactors independent of \(H\) cancel in the ratio

\[
c_H/c_0.
\]

Let

\[
m=\frac d2.
\]

In flat spacetime,

\[
\sqrt{\det B(t)}
=
t^{m-1}.
\]

Thus the flat longitudinal kernel is

\[
u^{m-1}(U-u)^{m-1}.
\]

## 4. Quadratic tidal expansion

Substituting the determinant expansion,

\[
\begin{aligned}
\frac{
c_H(U)
}{
c_0(U)
}
={}&
1
+
\frac{
\operatorname{Tr}(H^2)
}{360}
\Big[
U^4\\
&\qquad
-
\langle
u^4+(U-u)^4
\rangle_{m,m}
\Big]
+
\cdots,
\end{aligned}
\]

where the average uses the normalized Beta kernel

\[
u^{m-1}(U-u)^{m-1}.
\]

Set

\[
x=\frac uU.
\]

Then

\[
x\sim\operatorname{Beta}(m,m).
\]

Its fourth moment is

\[
\boxed{
\mathbb E[x^4]
=
\frac{
(m)_4
}{
(2m)_4
},
}
\]

where

\[
(a)_4
=
a(a+1)(a+2)(a+3)
\]

is the rising factorial.

By symmetry,

\[
\mathbb E[
x^4+(1-x)^4
]
=
2
\frac{
(m)_4
}{
(2m)_4
}.
\]

Hence

\[
\boxed{
\frac{
c_H(U)
}{
c_0(U)
}
=
1
+
\lambda_d
U^4
\operatorname{Tr}(H^2)
+
\cdots,
}
\]

with

\[
\boxed{
\lambda_d
=
\frac1{360}
\left[
1
-
2
\frac{
(d/2)_4
}{
(d)_4
}
\right].
}
\]

## 5. d = 4

For

\[
d=4,
\qquad
m=2,
\]

\[
\frac{
(m)_4
}{
(2m)_4
}
=
\frac17.
\]

Therefore

\[
\boxed{
\lambda_4
=
\frac1{504}.
}
\]

For the symmetric vacuum plane wave

\[
H
=
\operatorname{diag}
(-\omega^2,+\omega^2),
\]

\[
\operatorname{Tr}(H^2)
=
2\omega^4.
\]

Thus

\[
\frac{
c_H(U)
}{
c_0(U)
}
=
1
+
\frac{
\omega^4U^4
}{252}
+
\cdots.
\]

Writing

\[
z=\omega U,
\]

\[
\boxed{
\frac{
c_H
}{
c_0
}
=
1+
\frac{
z^4
}{252}
+
O(z^8),
}
\]

which exactly reproduces the independent symmetric-plane-wave calculation.

## 6. Interpretation

The absence of an \(O(U^2)\) term is the Jacobi-determinant form of the vacuum trace condition

\[
\operatorname{Tr}H=0.
\]

The first focusing correction depends on the squared tidal matrix:

\[
\operatorname{Tr}(H^2).
\]

This is a null-direction-dependent contraction of the Weyl tensor.

Thus the leading vacuum modification of the thin-null coefficient is controlled by **shear/focusing energy**, not by a linear Weyl scalar.

## 7. Conjugate-point limitation

The determinant representation is regular only while

\[
\det B(t)\ne0
\]

on the relevant open segment.

At a conjugate point,

\[
\det B=0,
\]

and the thin-null coefficient can diverge.

The exact symmetric-plane-wave caustic diagnostic demonstrates this breakdown.

Therefore the expansion is uniform only on compact generator families with a positive null-index spectral gap.

## 8. Derivative corrections

If the tidal matrix varies along the null generator,

\[
H(t)
=
H_0
+
tH_1
+
\frac12t^2H_2
+\cdots,
\]

additional curvature-derivative terms appear in the Jacobi expansion.

For a centered full diamond, odd-jet contributions cancel after the two-sided/edge integration by the central-inversion symmetry theorem.

In a Ricci-flat neighborhood, the remaining scalar \(L^4\) content reduces to the quadratic Weyl basis described in

\[
\texttt{VACUUM\_L4\_WEYL\_INVARIANT\_BASIS\_20261112.md}.
\]

The present proposition isolates only the universal locally constant tidal piece and does not claim to replace the full edge calculation.

## 9. Role in the second vacuum calibration

For a general small vacuum \(3+1\) diamond, the intrinsic edge functional depends on:

1. parent volume;
2. edge area;
3. crossing of the two volume-null gradients;
4. incoming and outgoing thin-null coefficients.

The formula above fixes the universal quadratic-Weyl contribution from item 4.

The remaining unknown second-calibration information is concentrated in the edge/cross-gradient geometry rather than in the thin-null focusing normalization itself.
