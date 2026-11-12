# Audit: coordinate invariance and flat reduction of the curved null-edge coefficient

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** algebraic coefficient audit  
**Target:** ALLD_CURVED_REGULAR_JOINT_EDGE_TAIL_THEOREM_20261112.md

## 1. Purpose

The curved \(d\ge4\) theorem writes the leading small-disagreement coefficient as

\[
C_{d,g}^{\rm joint}
=
2
\int_E
\mathcal A_d(s)
\mathcal S_d(s)
\,dA_E(s).
\]

Because the individual optical coordinates \(a,b\) are not canonical, the first question is whether this formula depends on arbitrary rescaling of the defining functions.

The second question is whether it really reduces to the previously derived Minkowski constant.

Both checks pass.

## 2. Optical gauge freedom

Near the null edge, replace

\[
a
\mapsto
a'
=
\lambda(s)a,
\]

\[
b
\mapsto
b'
=
\mu(s)b,
\]

with smooth positive functions

\[
\lambda,\mu>0.
\]

At the edge, higher-order terms in \(a,b\) do not affect the leading coefficient.

The double-null metric is

\[
g
=
-2\Omega^2 da\,db
+
h_{AB}ds^Ads^B
+
O(a+b).
\]

Therefore

\[
da\,db
=
\frac{
da'\,db'
}{
\lambda\mu
}
+
\text{higher-order edge terms},
\]

so

\[
\boxed{
\Omega'^2
=
\frac{
\Omega^2
}{
\lambda\mu
}.
}
\]

## 3. Endpoint coefficients

Write

\[
\mathcal V(p,x)
=
c_+(s)a^m[1+o(1)],
\]

\[
\mathcal V(x,q)
=
c_-(s)b^m[1+o(1)],
\]

with

\[
m=\frac d2.
\]

Under the optical rescaling,

\[
a
=
\frac{a'}{\lambda},
\]

so

\[
\boxed{
c_+'
=
c_+
\lambda^{-m}.
}
\]

Similarly,

\[
\boxed{
c_-'
=
c_-
\mu^{-m}.
}
\]

## 4. Pair-density transformation

The local pair-density factor is

\[
\mathcal A_d
=
\frac{
\omega_{d-2}
2^{m-1}
\Omega^{d+2}
}{
V_D^2
}.
\]

Since

\[
\Omega'
=
\Omega
(\lambda\mu)^{-1/2},
\]

we obtain

\[
\boxed{
\mathcal A_d'
=
\mathcal A_d
(\lambda\mu)^{-(d+2)/2}.
}
\]

Because

\[
\frac{d+2}{2}
=
m+1,
\]

this is

\[
\mathcal A_d'
=
\mathcal A_d
(\lambda\mu)^{-(m+1)}.
\]

## 5. Scalar-integral transformation

Define

\[
a_m
=
1+\frac1m.
\]

The scalar factor contains

\[
c_+^{-a_m}
c_-^{-a_m}.
\]

Therefore

\[
\begin{aligned}
(c_+')^{-a_m}
(c_-')^{-a_m}
&=
c_+^{-a_m}
c_-^{-a_m}
\lambda^{ma_m}
\mu^{ma_m}.
\end{aligned}
\]

But

\[
ma_m
=
m+1.
\]

Hence

\[
\boxed{
\mathcal S_d'
=
\mathcal S_d
(\lambda\mu)^{m+1}.
}
\]

## 6. Exact cancellation

Multiplying,

\[
\mathcal A_d'
\mathcal S_d'
=
\mathcal A_d
\mathcal S_d.
\]

Thus

\[
\boxed{
\mathcal A_d\mathcal S_d
}
\]

is invariant under arbitrary positive optical rescalings.

A reparametrization of the edge coordinates changes the coordinate expression of \(h_{AB}\), but

\[
dA_E
\]

is the intrinsic edge-area form.

Therefore

\[
\boxed{
C_{d,g}^{\rm joint}
}
\]

is coordinate invariant at the displayed order.

## 7. Flat Minkowski data

For the unit Minkowski diamond

\[
p=(-1,\mathbf0),
\qquad
q=(1,\mathbf0),
\]

use

\[
a=1-r+t,
\qquad
b=1-r-t.
\]

At the null joint,

\[
-dt^2+dr^2
=
da\,db.
\]

In the curved-theorem convention

\[
-2\Omega^2 da\,db,
\]

the absolute cross coefficient is

\[
\boxed{
\Omega^2=\frac12.
}
\]

The normalized endpoint volume has the flat expansion

\[
\frac{
V(p,x)
}{
V_D
}
\sim
2^{-d/2}a^{d/2}.
\]

Hence

\[
\boxed{
c_+=c_-=2^{-d/2}.
}
\]

The parent diamond volume is

\[
\boxed{
V_D
=
\frac{
2S_{d-2}
}{
d(d-1)
}.
}
\]

The edge is the unit

\[
S^{d-2}
\]

with area

\[
S_{d-2}.
\]

## 8. Curved formula evaluated on the flat diamond

Substituting the flat data into the curved coefficient gives

\[
K_{d,\eta}^{\rm curved\ formula}
=
2^{d-2}
\frac{
d^2(d-1)^2
}{
d-2
}
\frac{
S_{d-3}
}{
S_{d-2}
}
\left[
a_mL_m\Gamma(a_m)
\right]^2.
\]

This is exactly the previously derived flat constant

\[
\boxed{
K_d^{\rm twin}.
}
\]

No extra geometric normalization survives.

## 9. d = 4 check

For

\[
d=4,
\]

\[
m=2,
\qquad
a_m=\frac32,
\qquad
L_2=\frac13.
\]

The formula reduces to

\[
\boxed{
K_{4,\eta}
=
9\pi.
}
\]

Thus the curved coefficient reproduces the independently derived flat \(3+1\) theorem exactly.

## 10. Numerical regression

The repository script

tools/verify_curved_edge_coefficient_invariance.py

checks:

1. optical-gauge cancellation for several arbitrary positive rescalings;
2. equality between the curved-on-flat coefficient and the old flat formula for
   \[
   d=4,\ldots,10;
   \]
3. the exact \(d=4\) value
   \[
   9\pi.
   \]

Representative exact-ratio output is numerically

\[
\frac{
K_{d,\eta}^{\rm curved\ formula}
}{
K_d^{\rm twin}
}
=
1
\]

to integration precision in every tested dimension.

## 11. Audit verdict

The coefficient formula survives the coordinate-normalization attack.

The optical factors are individually gauge dependent, but their product is not.

The curved edge coefficient is therefore not an artifact of the chosen double-null defining functions.

The remaining all-dimensional audit targets are global sector exhaustion and the small-diamond automatic-regularity argument, not coefficient normalization.
