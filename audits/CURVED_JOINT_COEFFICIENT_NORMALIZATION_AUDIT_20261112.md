# Audit: coordinate invariance and flat normalization of the curved null-joint coefficient

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** symbolic/algebraic audit  
**Target:** ALLD_CURVED_REGULAR_JOINT_EDGE_TAIL_THEOREM_20261112.md

## 1. Purpose

The curved \(d\ge4\) coefficient is written in optical coordinates.

That creates two obvious risks:

1. dependence on an arbitrary normalization of the optical functions;
2. a hidden normalization error in the local pair measure.

This audit checks both.

## 2. Optical rescaling

Let

\[
a'=\lambda(s)a,
\qquad
b'=\mu(s)b,
\]

with

\[
\lambda,\mu>0
\]

smooth along the edge.

At leading order on the edge,

\[
da=\lambda^{-1}da',
\qquad
db=\mu^{-1}db'.
\]

If

\[
g
=
-2\Omega^2 da\,db
+
h_{AB}ds^Ads^B,
\]

then

\[
\boxed{
\Omega'^2
=
\frac{\Omega^2}{\lambda\mu}.
}
\]

## 3. Thin-null coefficients

Let

\[
m=\frac d2.
\]

If

\[
\mathcal V(p,x)
=
c_+a^m[1+o(1)],
\]

then

\[
a=\frac{a'}{\lambda}
\]

gives

\[
\boxed{
c_+'
=
c_+\lambda^{-m}.
}
\]

Similarly,

\[
\boxed{
c_-'
=
c_-\mu^{-m}.
}
\]

## 4. Pair-measure prefactor

The curved edge pair prefactor is

\[
\mathcal A_d
\propto
\Omega^{d+2}.
\]

Therefore

\[
\boxed{
\mathcal A_d'
=
\mathcal A_d
(\lambda\mu)^{-(d+2)/2}.
}
\]

## 5. Scalar disagreement factor

Define

\[
a_m
=
1+\frac2d.
\]

The scalar factor contains

\[
c_+^{-a_m}c_-^{-a_m}.
\]

Thus

\[
\begin{aligned}
c_+'^{-a_m}c_-'^{-a_m}
&=
c_+^{-a_m}c_-^{-a_m}
\lambda^{ma_m}
\mu^{ma_m}.
\end{aligned}
\]

But

\[
ma_m
=
\frac d2
\left(
1+\frac2d
\right)
=
\frac{d+2}{2}.
\]

Hence

\[
\boxed{
\mathcal S_d'
=
\mathcal S_d
(\lambda\mu)^{(d+2)/2}.
}
\]

## 6. Cancellation

Multiplying,

\[
\mathcal A_d'\mathcal S_d'
=
\mathcal A_d\mathcal S_d.
\]

Therefore the edge density

\[
2\mathcal A_d\mathcal S_d\,dA_E
\]

is invariant.

Thus

\[
\boxed{
C_{d,g}^{\rm joint}
}
\]

does not depend on the normalization of the optical functions.

The cancellation is exact.

## 7. Flat d = 4 test

Use the unit Minkowski Alexandrov interval

\[
D=I((-1,\mathbf0),(1,\mathbf0)).
\]

Its physical four-volume is

\[
V_D
=
\frac{2\pi}{3}.
\]

The joint edge is a unit \(S^2\), with area

\[
A_E
=
4\pi.
\]

In the standard null-waist coordinates,

\[
|\Omega|^2=\frac12.
\]

Also,

\[
c_+=c_-=\frac14.
\]

For

\[
d=4,
\qquad
m=2,
\qquad
a_m=\frac32,
\]

the one-side constant is

\[
L_2=\frac13.
\]

## 8. Pair-measure factor

The local prefactor density is

\[
\mathcal A_4
=
\frac{
\pi
\,2
\,\Omega^6
}{
V_D^2
}.
\]

Since

\[
\Omega^6
=
\frac18,
\]

we obtain

\[
\mathcal A_4
=
\frac{9}{16\pi}.
\]

Integrating over the edge,

\[
\boxed{
\int_E
\mathcal A_4\,dA_E
=
\frac94.
}
\]

This exactly reproduces the flat \(d=4\) ordered-pair prefactor previously derived directly.

## 9. Scalar factor

The scalar factor is

\[
\mathcal S_4
=
(a_mL_2)^2
c_+^{-3/2}
c_-^{-3/2}
\frac{
\Gamma(3/2)^2
}{
\Gamma(4)
}.
\]

Substituting

\[
a_mL_2
=
\frac12,
\]

\[
c_\pm^{-3/2}
=
8,
\]

\[
\Gamma(3/2)^2
=
\frac\pi4,
\]

and

\[
\Gamma(4)=6,
\]

gives

\[
\boxed{
\mathcal S_4
=
\frac{2\pi}{3}.
}
\]

## 10. Edge-tail coefficient

There are two time orientations.

Therefore

\[
\begin{aligned}
C_4^{\rm joint}
&=
2
\left(
\frac94
\right)
\left(
\frac{2\pi}{3}
\right)\\
&=
\boxed{
3\pi.
}
\end{aligned}
\]

## 11. True-twin coefficient

The Laplace-Stieltjes transfer gives

\[
K_4
=
\frac12
C_4^{\rm joint}
\Gamma(4).
\]

Hence

\[
\begin{aligned}
K_4
&=
\frac12
(3\pi)
(6)\\
&=
\boxed{
9\pi.
}
\end{aligned}
\]

Thus the curved coefficient formula reduces exactly to the independently derived flat theorem.

## 12. Computational regression

The repository script

tools/verify_curved_joint_coefficient_normalization.py

checks symbolically:

1. the optical-rescaling exponent cancellation;
2. \(C_4=3\pi\);
3. \(K_4=9\pi\).

The symbolic regression is supplementary.

The cancellations above are the analytic audit.

## 13. Verdict

No coordinate-normalization defect was found.

The curved edge coefficient is invariant under independent regular rescalings of the two optical functions and reproduces the exact flat \(3+1\) constant.
