# Proposition: intrinsic volume-gradient form of the curved null-edge recovery functional

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact geometric reformulation  
**Scope:** regular curved Alexandrov diamonds in fixed \(d\ge4\)  
**Purpose:** remove all residual optical-coordinate dependence from the leading recovery coefficient

## 1. Setting

Let

\[
D=I(p,q)
\]

be a regular Lorentzian Alexandrov interval in dimension

\[
d\ge4.
\]

Let

\[
V_D
=
\operatorname{Vol}(D),
\]

and define normalized subinterval volumes

\[
\mathcal V_-(x)
=
\frac{
\operatorname{Vol}(I(p,x))
}{
V_D
},
\]

\[
\mathcal V_+(x)
=
\frac{
\operatorname{Vol}(I(x,q))
}{
V_D
}.
\]

Let the future null boundary of \(p\) and past null boundary of \(q\) meet transversely along the smooth compact codimension-two edge

\[
\Sigma.
\]

Set

\[
m=\frac d2.
\]

## 2. Canonical volume-null defining functions

Define

\[
\boxed{
a
=
\mathcal V_-^{\,1/m}
=
\mathcal V_-^{\,2/d},
}
\]

and

\[
\boxed{
b
=
\mathcal V_+^{\,1/m}
=
\mathcal V_+^{\,2/d}.
}
\]

The regular thin-null theorem gives

\[
\mathcal V_-
=
c_-(s)\alpha^m[1+o(1)]
\]

for any smooth inward defining function \(\alpha\) of the first null sheet, with

\[
c_-(s)>0.
\]

Hence

\[
a
=
c_-(s)^{1/m}\alpha
+
o(\alpha).
\]

Therefore \(a\) extends to a smooth first-order defining function of the null sheet.

Similarly,

\[
b
=
c_+(s)^{1/m}\beta
+
o(\beta).
\]

Thus

\[
da,
\qquad
db
\]

are nonzero null covectors on \(\Sigma\).

## 3. Volume-null double-null form

Because the two null sheets meet transversely,

\[
da
\quad\text{and}\quad
db
\]

are linearly independent on \(\Sigma\).

In the canonical coordinates

\[
(a,b,s^A),
\]

the metric has edge form

\[
\boxed{
g
=
2\chi(s)\,da\,db
+
h_{AB}(s)\,ds^Ads^B
+
O(a+b).
}
\]

The \(a,b\) block is

\[
\begin{pmatrix}
0&\chi\\
\chi&0
\end{pmatrix}.
\]

Its inverse is

\[
\begin{pmatrix}
0&\chi^{-1}\\
\chi^{-1}&0
\end{pmatrix}.
\]

Therefore

\[
\boxed{
g^{-1}(da,db)
=
\chi^{-1}.
}
\]

Equivalently,

\[
\boxed{
\chi
=
\left[
g^{-1}(da,db)
\right]^{-1}.
}
\]

This identity is exact on the edge.

## 4. Intrinsic joint functional

The regular \(d\ge4\) recovery theorem uses

\[
\mathcal J_d(D,g)
=
\int_\Sigma
\chi^{m+1}
\,dA_\Sigma.
\]

Substituting the gradient identity gives the intrinsic form

\[
\boxed{
\mathcal J_d(D,g)
=
\int_\Sigma
\left[
g^{-1}
\left(
d\mathcal V_-^{\,2/d},
d\mathcal V_+^{\,2/d}
\right)
\right]^{-(d/2+1)}
dA_\Sigma.
}
\]

No arbitrary optical normalization appears.

## 5. Leading recovery coefficient

Hence for fixed

\[
d\ge4,
\]

\[
\boxed{
K_{d,g}
=
\frac{
2^{d/2-1}\omega_{d-2}
}{
V_D^2
}
\mathcal J_d(D,g)
\left[
\left(
1+\frac2d
\right)
L_{d/2}
\Gamma\left(
1+\frac2d
\right)
\right]^2.
}
\]

Therefore the leading arrow-erasure error coefficient is an intrinsic functional of exactly three continuum objects:

1. the parent diamond volume \(V_D\);
2. the codimension-two edge measure \(dA_\Sigma\);
3. the cross norm of the two canonical causal-volume gradients.

## 6. Relation to arbitrary optical coordinates

Suppose instead

\[
\mathcal V_-
=
c_-\alpha^m[1+o(1)],
\]

\[
\mathcal V_+
=
c_+\beta^m[1+o(1)].
\]

Then

\[
da
=
c_-^{1/m}d\alpha,
\]

\[
db
=
c_+^{1/m}d\beta
\]

on the edge.

Thus

\[
g^{-1}(da,db)
=
(c_-c_+)^{1/m}
g^{-1}(d\alpha,d\beta).
\]

This reproduces exactly the cancellation between:

- the thin-null endpoint coefficients;
- the double-null cross coefficient;

found in the earlier optical-normalization audit.

The canonical volume-null formulation packages that cancellation into one scalar.

## 7. Jacobi-determinant interpretation

The thin-null coefficients

\[
c_\pm(s)
\]

are determined by the Penrose-limit/Jacobi geometry of the two null generator segments joining the tips to the edge point \(s\).

Thus

\[
g^{-1}
\left(
d\mathcal V_-^{2/d},
d\mathcal V_+^{2/d}
\right)
\]

combines:

- the normalization supplied by the incoming null Jacobi determinant;
- the normalization supplied by the outgoing null Jacobi determinant;
- the local crossing angle of the two null normals.

This identifies the leading recovery coefficient as a weighted edge integral of two-sided optical focusing data.

## 8. Vacuum expansion target

For a centered small vacuum diamond,

\[
R_{\mu\nu}=0.
\]

A published \(L^4\) Weyl expansion for the parent Alexandrov volume exists in the small-causal-diamond literature. However, the repository's later \(3+1\) audit found that the printed final coefficient in Wang (2019), Eq. (79), is inconsistent with that paper's own intermediate Eqs. (74) and (76), as well as with exact Kasner and symmetric-plane-wave calculations.

The internally supported \(3+1\) parent-volume law is now

\[
\frac{V(D_L)}{V_{\rm Mink}(L)}
=
1
+
L^4
\left[
\frac{17}{630}E^2
+
\frac1{210}B^2
\right]
+
o(L^4).
\]

See

\[
\texttt{D4\_CORRECTED\_VACUUM\_ALEXANDROV\_VOLUME\_THEOREM\_CANDIDATE\_20261112.md}.
\]

Accordingly, the remaining project-specific vacuum calculation can be localized to

\[
\boxed{
\mathcal J_d
=
\int_\Sigma
\left[
g^{-1}
\left(
d\mathcal V_-^{2/d},
d\mathcal V_+^{2/d}
\right)
\right]^{-(d/2+1)}
dA_\Sigma.
}
\]

At order \(L^4\), its scalar content is already known from the vacuum invariant-basis theorem:

\[
E^2,\quad H^2,\quad D^2
\]

for \(d\ge5\), and

\[
E^2,\quad B^2
\]

for \(d=4\).

Thus the vacuum coefficient problem is now an explicit perturbation problem for one intrinsic edge functional rather than a coordinate-dependent null-joint calculation.

## 9. d = 4 plane-wave check

For the symmetric vacuum plane wave calibration, direct evaluation of this same volume-null functional gives

\[
\frac{
K_{\rm PW}
}{
K_{\rm Mink}
}
=
1+
\frac{127}{9450}z^4
+
O(z^8),
\]

and hence

\[
a_4+b_4
=
\frac{508}{4725}.
\]

This confirms that the intrinsic formulation retains the exact plane-wave calibration.

## 10. Scientific use

The proposition provides the clean geometric object to compare against other small-diamond observables.

In particular, it can now be expanded alongside:

- parent Alexandrov volume;
- edge area;
- null expansion/shear;
- van Vleck/Jacobi determinants.

This is the appropriate starting point for a second vacuum calibration and for any attempt to derive the full \(L^4\) Weyl response analytically.
