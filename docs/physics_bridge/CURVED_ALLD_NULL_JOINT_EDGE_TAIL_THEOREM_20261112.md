# Theorem: regular curved null-joint small-disagreement law for fixed d >= 4

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** analytic joint asymptotic theorem under regular double-null/Penrose hypotheses
**Physical status:** curved generalization of the null-joint mechanism that controls arrow-erasure errors in spacetime dimension \(d\ge4\)
**Novelty status:** double-null geometry and Penrose limits are classical; the small-disagreement law and joint optical coefficient are project-specific candidates

## 1. Setting

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval in a smooth \(d\)-dimensional Lorentzian spacetime, with fixed integer

\[
d\ge4.
\]

Use normalized physical volume

\[
\mathcal V(a,b)
=
\frac{
\operatorname{Vol}_g(I(a,b))
}{
V_D
},
\qquad
V_D=\operatorname{Vol}_g(D).
\]

Let

\[
\Sigma
=
\partial I^+(p)
\cap
\partial I^-(q)
\]

be a compact smooth spacelike codimension-two joint.

Set

\[
m=\frac d2.
\]

## 2. Regular volume-null coordinates

Assume the regular Penrose/null-Fermi hypotheses needed to define

\[
a(x)
=
\mathcal V(p,x)^{1/m}
=
\mathcal V(p,x)^{2/d},
\]

and

\[
b(x)
=
\mathcal V(x,q)^{1/m}
=
\mathcal V(x,q)^{2/d}
\]

as regular transverse coordinates near the joint.

Let

\[
\sigma=(\sigma^1,\ldots,\sigma^{d-2})
\]

be local coordinates on \(\Sigma\).

At the joint, choose the orientation of \(a,b\) so the metric takes the double-null form

\[
\boxed{
g
=
2\chi(\sigma)\,da\,db
+
h_{AB}(\sigma)\,
d\sigma^A d\sigma^B
+
O(a+b),
}
\]

where

\[
\chi(\sigma)>0
\]

and \(h\) is the induced Riemannian joint metric.

For a future-comparable displacement we use

\[
da=A>0,
\qquad
db=-B<0.
\]

Then its leading squared interval is

\[
-2\chi AB
+
h_{AB}\zeta^A\zeta^B.
\]

## 3. Exact endpoint-volume increments

For an ordered pair

\[
x\prec y
\]

write

\[
a_x=\alpha,
\qquad
a_y=\alpha+A,
\]

\[
b_y=\beta,
\qquad
b_x=\beta+B,
\]

with

\[
A,B\ge0.
\]

By definition of \(a,b\),

\[
\mathcal V(p,x)
=
\alpha^m,
\]

\[
\mathcal V(p,y)
=
(\alpha+A)^m,
\]

\[
\mathcal V(y,q)
=
\beta^m,
\]

and

\[
\mathcal V(x,q)
=
(\beta+B)^m.
\]

The exact disagreement identity becomes

\[
\boxed{
\Delta_g(x,y)
=
g_m(\alpha,A)
+
g_m(\beta,B)
-
2\mathcal V(x,y),
}
\]

where

\[
g_m(u,v)
=
(u+v)^m-u^m.
\]

## 4. Small central interval

Assume the regular double-null chart gives

\[
\boxed{
\mathcal V(x,y)
\le
C_I(AB)^m
}
\]

for sufficiently close comparable pairs near the joint.

Since

\[
g_m(\alpha,A)\ge A^m,
\]

and

\[
g_m(\beta,B)\ge B^m,
\]

while

\[
A,B\le\eta
\]

in a sufficiently small joint chart,

\[
(AB)^m
\le
\eta^m
\min(A^m,B^m).
\]

Choose \(\eta\) so that

\[
2C_I\eta^m
\le
\frac12.
\]

Then

\[
\boxed{
\frac12
\left[
g_m(\alpha,A)
+
g_m(\beta,B)
\right]
\le
\Delta_g(x,y)
\le
g_m(\alpha,A)
+
g_m(\beta,B).
}
\]

Thus the small-disagreement geometry is governed by the same two one-side scalar increments as in flat spacetime.

## 5. Tangential causal cap

Let

\[
\zeta^A
=
\sigma_y^A-\sigma_x^A.
\]

At leading order, timelike comparability requires

\[
h_{AB}\zeta^A\zeta^B
<
2\chi AB.
\]

Therefore the coordinate volume of the tangential causal cap is

\[
\boxed{
\frac{
\omega_{d-2}
}{
\sqrt{\det h}
}
(2\chi AB)^{m-1},
}
\]

where

\[
\omega_{d-2}
=
\operatorname{Vol}
B^{d-2}_{\mathrm{Eucl}}(1).
\]

## 6. Normalized spacetime density at the joint

For the double-null metric block

\[
2\chi\,da\,db+h_{AB}d\sigma^Ad\sigma^B,
\]

the physical volume density is

\[
\chi
\sqrt{\det h}.
\]

Hence the normalized probability density is

\[
J_\Sigma(\sigma)
=
\frac{
\chi(\sigma)
\sqrt{\det h(\sigma)}
}{
V_D
}.
\]

For two nearby points, the product measure contributes

\[
J_\Sigma(\sigma)^2
\]

at leading order.

After integrating the tangential cap, the geometric coefficient for one time orientation becomes

\[
\frac{
\omega_{d-2}
2^{m-1}
}{
V_D^2
}
\chi(\sigma)^{m+1}
\,dA_\Sigma(\sigma),
\]

where

\[
dA_\Sigma
=
\sqrt{\det h}\,d^{d-2}\sigma.
\]

## 7. Joint optical functional

Define

\[
\boxed{
\mathcal J_d(D,g)
=
\int_\Sigma
\chi(\sigma)^{m+1}
\,dA_\Sigma(\sigma).
}
\]

This quantity is invariant under reparameterizations of the joint coordinates once \(a,b\) are fixed by normalized causal volume.

It contains the focusing information inherited from the two null families.

## 8. One-side scalar integral

Define

\[
J_m(s)
=
\int_0^\infty
\int_0^\infty
A^{m-1}
\mathbf1_{
\{g_m(\alpha,A)\le s\}
}
\,dA\,d\alpha.
\]

For

\[
m\ge2,
\]

the integral converges and is exactly homogeneous:

\[
\boxed{
J_m(s)
=
L_m
s^{a_m},
}
\]

where

\[
a_m
=
1+\frac1m
=
1+\frac2d,
\]

and

\[
\boxed{
L_m
=
\frac1{m+1}
\int_0^\infty
\left[
(1+t)^m-t^m
\right]^{-(m+1)/m}
dt.
}
\]

The associated Stieltjes density is

\[
dJ_m(g)
=
a_mL_m
g^{a_m-1}
\,dg.
\]

## 9. Scalar convolution

For two independent one-side increments,

\[
\begin{aligned}
&
\int_{g_1+g_2\le\varepsilon}
dJ_m(g_1)dJ_m(g_2)
\\
&\qquad=
(a_mL_m)^2
\frac{
\Gamma(a_m)^2
}{
\Gamma(2a_m+1)
}
\varepsilon^{2a_m}.
\end{aligned}
\]

Since

\[
2a_m
=
2+\frac4d,
\]

the curved joint exponent is

\[
\boxed{
\beta_d
=
2+\frac4d.
}
\]

## 10. Curved joint coefficient

Include both time orientations.

The small-disagreement probability contributed by the regular joint satisfies

\[
\boxed{
F_{d,g}^{\mathrm{joint}}(\varepsilon)
\sim
C_{d,g}^{\mathrm{joint}}
\varepsilon^{2+4/d},
}
\]

with

\[
\boxed{
C_{d,g}^{\mathrm{joint}}
=
\frac{
2^m
\omega_{d-2}
}{
V_D^2
}
\mathcal J_d(D,g)
(a_mL_m)^2
\frac{
\Gamma(a_m)^2
}{
\Gamma(2a_m+1)
}.
}
\]

This is the curved optical replacement of the flat null-joint coefficient.

## 11. Bulk comparison

Away from the joint, assume the finite-diamond volume function

\[
\Phi
=
\mathcal V(p,\cdot)
-
\mathcal V(\cdot,q)
\]

has nondegenerate timelike differential on regular compact bulk charts.

Then the local small-disagreement pair volume is

\[
O(\varepsilon^d).
\]

For every

\[
d\ge4,
\]

\[
2+\frac4d<d.
\]

Hence the bulk is strictly subleading.

Therefore, under the regularity hypotheses,

\[
\boxed{
F_{d,g}(\varepsilon)
\sim
C_{d,g}^{\mathrm{joint}}
\varepsilon^{2+4/d}.
}
\]

## 12. True-twin expectation

Let \(T_n\) count comparable true-twin pairs.

Laplace-Stieltjes transfer gives

\[
\boxed{
\mathbb E[T_n]
\sim
K_{d,g}^{\mathrm{twin}}
n^{-4/d},
}
\]

where

\[
K_{d,g}^{\mathrm{twin}}
=
\frac12
C_{d,g}^{\mathrm{joint}}
\Gamma\left(
3+\frac4d
\right).
\]

Since

\[
3+\frac4d
=
2a_m+1,
\]

the gamma denominator cancels and

\[
\boxed{
K_{d,g}^{\mathrm{twin}}
=
\frac{
2^{m-1}
\omega_{d-2}
}{
V_D^2
}
\mathcal J_d(D,g)
\left[
a_mL_m
\Gamma(a_m)
\right]^2.
}
\]

## 13. Flat all-dimensional regression

For the unit flat Minkowski diamond,

\[
V_D
=
\frac{
2S_{d-2}
}{
d(d-1)
}.
\]

In volume-null coordinates at the joint,

\[
\chi=2,
\]

and

\[
\operatorname{Area}(\Sigma)
=
S_{d-2}.
\]

Therefore

\[
\mathcal J_d
=
2^{m+1}
S_{d-2}.
\]

Substitution gives

\[
C_{d,\eta}^{\mathrm{joint}}
=
\frac{
2^{d-1}
d^2(d-1)^2
}{
d-2
}
\frac{
S_{d-3}
}{
S_{d-2}
}
(a_mL_m)^2
\frac{
\Gamma(a_m)^2
}{
\Gamma(2a_m+1)
},
\]

because

\[
\omega_{d-2}
=
\frac{
S_{d-3}
}{
d-2
}.
\]

This is exactly the previously derived flat all-dimensional coefficient.

For

\[
d=4,
\]

it reduces to

\[
\boxed{
C_{4,\eta}^{\mathrm{joint}}
=
3\pi,
}
\]

and

\[
\boxed{
K_{4,\eta}^{\mathrm{twin}}
=
9\pi.
}
\]

Thus the curved formula passes the full flat regression.

## 14. Geometric interpretation

The exponent

\[
2+\frac4d
\]

is universal over regular curved null joints.

Curvature enters the leading coefficient only through

\[
\boxed{
\mathcal J_d(D,g)
=
\int_\Sigma
\chi^{d/2+1}
\,dA_\Sigma.
}
\]

The function \(\chi\) measures the relative normalization of the two volume-null directions and therefore contains integrated null-focusing information.

The leading arrow-erasure defect is thus controlled by an optical functional of the codimension-two joint.

## 15. Scope

The theorem assumes:

- a smooth transverse joint;
- regular volume-null coordinates;
- no relevant cut/conjugate degeneration;
- a regular double-null causal cap;
- the small central-interval estimate;
- nondegenerate bulk volume-time gradient.

It does not cover caustic or nonsmooth joints.

Those regimes may change the exponent as well as the coefficient.
