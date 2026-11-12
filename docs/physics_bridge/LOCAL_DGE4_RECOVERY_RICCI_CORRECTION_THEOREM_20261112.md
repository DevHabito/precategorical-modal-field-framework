# Theorem: first Ricci correction to the local orientation-recovery error for fixed d >= 4

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic curvature-correction theorem, derived from two independent symmetric reference families  
**Physical status:** first explicit finite-curvature correction to the local arrow-erasure recovery law  
**Novelty status:** small causal-diamond volume and joint-area expansions are established; the near-null coefficient and the resulting recovery correction are project-specific candidates

## 1. Setting

Fix an integer spacetime dimension

\[
d\ge4.
\]

Let \(o\) be the center of a sufficiently small timelike Alexandrov interval with endpoints

\[
p_L=\exp_o(-LT),
\qquad
q_L=\exp_o(LT),
\]

where

\[
g(T,T)=-1.
\]

The total proper-time duration is

\[
\tau=2L.
\]

Let

\[
K_{d,L}
\]

be the leading orientation-recovery error coefficient:

\[
1-p_{d,g,L}^{\mathrm{UPO}}(n)
\sim
K_{d,L}
n^{-4/d}.
\]

Then

\[
\boxed{
K_{d,L}
=
K_d^{\mathrm{flat}}
\left[
1
+
L^2
\left(
a_d R(o)
+
b_d R_{\mu\nu}(o)T^\mu T^\nu
\right)
+
O(L^4)
\right],
}
\]

where

\[
\boxed{
a_d
=
-\frac{
d(d+6)
}{
4(d-1)(d+1)(d+2)
},
}
\]

and

\[
\boxed{
b_d
=
\frac{
d^2+2d-4
}{
4(d-1)(d+1)
}.
}
\]

No linear Weyl term occurs at this order.

## 2. Recovery coefficient in a regular curved joint

Set

\[
m=\frac d2.
\]

For a regular curved diamond, the leading \(d\ge4\) recovery coefficient has the form

\[
K_{d,g}
=
C_d^{\mathrm{scalar}}
\,
\frac{
\mathcal J_d(D,g)
}{
V_D^2
},
\]

where the dimension-only factor is

\[
C_d^{\mathrm{scalar}}
=
2^{m-1}
\omega_{d-2}
\left[
\left(
1+\frac2d
\right)
L_m
\Gamma\left(
1+\frac2d
\right)
\right]^2,
\]

and the optical joint functional is

\[
\mathcal J_d(D,g)
=
\int_\Sigma
\chi^{m+1}
\,dA_\Sigma.
\]

Therefore the first curvature correction is completely determined by the expansions of:

1. total causal-diamond volume \(V_D\);
2. joint area;
3. the volume-null cross coefficient \(\chi\).

The first two are known in the small-causal-diamond literature.

The third is derived below from the nearly-null interval volume.

## 3. Established small-diamond volume expansion

Gibbons and Solodukhin give, in arbitrary spacetime dimension,

\[
V_D
=
V_{\mathrm{flat}}
\left[
1
-
\frac{
d
}{
24(d+1)(d+2)
}
R\tau^2
+
\frac{
d
}{
24(d+1)
}
R_{TT}\tau^2
+
O(\tau^4)
\right].
\]

With

\[
\tau=2L,
\]

this becomes

\[
\boxed{
\frac{V_D}{V_{\mathrm{flat}}}
=
1
+
L^2
\left[
-\frac{
d
}{
6(d+1)(d+2)
}
R
+
\frac{
d
}{
6(d+1)
}
R_{TT}
\right]
+
O(L^4).
}
\]

## 4. Established joint-area expansion

The same work gives

\[
A_\Sigma
=
A_{\mathrm{flat}}
\left[
1
-
\frac{
1
}{
24(d-1)
}
R\tau^2
+
\frac{
d-4
}{
12(d-1)
}
R_{TT}\tau^2
+
O(\tau^4)
\right].
\]

Therefore

\[
\boxed{
\frac{A_\Sigma}{A_{\mathrm{flat}}}
=
1
+
L^2
\left[
-\frac{
1
}{
6(d-1)
}
R
+
\frac{
d-4
}{
3(d-1)
}
R_{TT}
\right]
+
O(L^4).
}
\]

The recovery coefficient still requires the expansion of \(\chi\).

## 5. First reference family: Einstein static universe

Consider

\[
ds^2
=
-dt^2
+
d\chi^2
+
\sin^2\chi\,d\Omega_{d-2}^2.
\]

For this family,

\[
R=(d-1)(d-2),
\qquad
R_{TT}=0.
\]

The centered diamond has endpoints

\[
t=\pm L,
\qquad
\chi=0,
\]

and joint

\[
t=0,
\qquad
\chi=L.
\]

## 6. Near-null interval coefficient in the Einstein static universe

Introduce ordinary radial null slacks

\[
u=t+L-\chi,
\qquad
v=L-t-\chi.
\]

Near the joint,

\[
u,v\to0.
\]

Take a point \(x_u\) on \(v=0\) with small \(u>0\).

The interval \(I(p,x_u)\) is a thin tube around the limiting null geodesic from \(p\) to the joint.

Let \(\lambda\in(0,L)\) be arclength along the spatial radial geodesic.

For a small transverse displacement \(y\), the excess broken-geodesic length has second variation

\[
d(p,z)+d(z,x_0)-L
=
\frac12
c_L(\lambda)
|y|^2
+
O(|y|^3),
\]

where

\[
c_L(\lambda)
=
\cot\lambda
+
\cot(L-\lambda)
=
\frac{
\sin L
}{
\sin\lambda\sin(L-\lambda)
}.
\]

After integrating the allowed time thickness and the \(d-2\) transverse directions, one obtains

\[
\boxed{
\operatorname{Vol}
I(p,x_u)
=
C_{\mathrm E}(L)
u^m
+
o(u^m),
}
\]

with

\[
\boxed{
C_{\mathrm E}(L)
=
\frac{
2^m\omega_{d-2}
}{
d
}
\int_0^L
\left[
\frac{
\sin\lambda\sin(L-\lambda)
}{
\sin L
}
\right]^{m-1}
d\lambda.
}
\]

This is the nearly-null coefficient required by the volume-null coordinate.

## 7. Small-L expansion of the nearly-null coefficient

Use

\[
\sin x
=
x-\frac{x^3}{6}+O(x^5).
\]

Then

\[
\frac{
\sin\lambda\sin(L-\lambda)
}{
\sin L
}
=
\frac{
\lambda(L-\lambda)
}{
L
}
\left[
1
+
\frac13
\lambda(L-\lambda)
+
O(L^4)
\right].
\]

The flat beta-function weight is

\[
[\lambda(L-\lambda)/L]^{m-1}.
\]

Its normalized moment is

\[
\frac{
\int_0^L
[\lambda(L-\lambda)/L]^{m-1}
\lambda(L-\lambda)\,d\lambda
}{
\int_0^L
[\lambda(L-\lambda)/L]^{m-1}
\,d\lambda
}
=
L^2
\frac{
m
}{
2(2m+1)
}.
\]

Therefore

\[
\boxed{
\frac{
C_{\mathrm E}(L)
}{
C_{\mathrm{flat}}(L)
}
=
1
+
\frac{
d(d-2)
}{
24(d+1)
}
L^2
+
O(L^4).
}
\]

## 8. Volume-null cross coefficient

If

\[
\operatorname{Vol}I(p,x_u)
=
C(L)u^m+o(u^m),
\]

then the normalized volume-null coordinate is

\[
a
=
\left(
\frac{
\operatorname{Vol}I(p,x)
}{
V_D
}
\right)^{1/m}
=
\left(
\frac{C(L)}{V_D}
\right)^{1/m}
u
+
o(u).
\]

By symmetry the same coefficient holds for \(b\).

Since the radial metric in ordinary null coordinates is

\[
du\,dv,
\]

the joint metric in volume-null coordinates is

\[
2\chi\,da\,db,
\]

with

\[
\boxed{
\chi
=
\frac12
\left(
\frac{
V_D
}{
C(L)
}
\right)^{2/m}.
}
\]

Thus

\[
\boxed{
\delta\log\chi
=
\frac{2}{m}
\left(
\delta\log V_D
-
\delta\log C
\right).
}
\]

## 9. Einstein-static recovery correction

For the Einstein static universe, the known total-volume and area expansions are

\[
\frac{V_{\mathrm E}}{V_{\mathrm{flat}}}
=
1
-
\frac{
d(d-1)(d-2)
}{
6(d+1)(d+2)
}
L^2
+
O(L^4),
\]

and

\[
\frac{
A_{\mathrm E}
}{
A_{\mathrm{flat}}
}
=
1
-
\frac{
d-2
}{
6
}
L^2
+
O(L^4).
\]

Using the near-null coefficient above gives

\[
\frac{
\chi_{\mathrm E}
}{
\chi_{\mathrm{flat}}
}
=
1
-
\frac{
(d-2)(5d-2)
}{
6(d+1)(d+2)
}
L^2
+
O(L^4).
\]

Since

\[
\mathcal J_d
=
\chi^{m+1}A_\Sigma
\]

in this isotropic model,

\[
\frac{
K_{d,\mathrm E}(L)
}{
K_d^{\mathrm{flat}}
}
=
1
-
\frac{
d(d-2)(d+6)
}{
4(d+1)(d+2)
}
L^2
+
O(L^4).
\]

Because

\[
R=(d-1)(d-2),
\qquad
R_{TT}=0,
\]

we obtain

\[
\boxed{
a_d
=
-\frac{
d(d+6)
}{
4(d-1)(d+1)(d+2)
}.
}
\]

## 10. Second reference family: de Sitter spacetime

Use global de Sitter coordinates

\[
ds^2
=
-dt^2
+
\cosh^2 t
\left(
d\chi^2
+
\sin^2\chi\,d\Omega_{d-2}^2
\right).
\]

The centered endpoints are

\[
t=\pm L.
\]

Introduce conformal time \(\eta\) with

\[
ds^2
=
\sec^2\eta
\left[
-d\eta^2
+
d\chi^2
+
\sin^2\chi\,d\Omega_{d-2}^2
\right].
\]

Let

\[
\ell
=
N/2
\]

be the half conformal duration.

The exact relation is

\[
\cos\ell
=
\operatorname{sech}L,
\]

hence

\[
\boxed{
\ell
=
L-\frac{L^3}{6}
+
O(L^5).
}
\]

## 11. de Sitter near-null coefficient

The causal geometry in conformal coordinates is that of the Einstein cylinder, while the physical volume density carries the factor

\[
\sec^d\eta.
\]

The near-null coefficient is therefore

\[
\boxed{
C_{\mathrm{dS}}(L)
=
\frac{
2^m\omega_{d-2}
}{
d
}
\int_0^\ell
\sec^d(\lambda-\ell)
\left[
\frac{
\sin\lambda\sin(\ell-\lambda)
}{
\sin\ell
}
\right]^{m-1}
d\lambda.
}
\]

Expanding the spatial focusing factor and the conformal weight gives, relative to a flat interval of conformal half-duration \(\ell\),

\[
\frac{
C_{\mathrm{dS}}
}{
C_{\mathrm{flat}}(\ell)
}
=
1
+
\frac d6
\ell^2
+
O(\ell^4).
\]

Since

\[
C_{\mathrm{flat}}(\ell)
\propto
\ell^m,
\]

and

\[
\ell/L
=
1-\frac{L^2}{6}+O(L^4),
\]

we obtain

\[
\boxed{
\frac{
C_{\mathrm{dS}}(L)
}{
C_{\mathrm{flat}}(L)
}
=
1
+
\frac d{12}
L^2
+
O(L^4).
}
\]

## 12. de Sitter recovery correction

The known de Sitter expansions are

\[
\frac{
V_{\mathrm{dS}}
}{
V_{\mathrm{flat}}
}
=
1
-
\frac{
d(d-1)
}{
3(d+2)
}
L^2
+
O(L^4),
\]

and

\[
\frac{
A_{\mathrm{dS}}
}{
A_{\mathrm{flat}}
}
=
1
-
\frac{
d-2
}{
3
}
L^2
+
O(L^4).
\]

Using the near-null coefficient gives

\[
\frac{
\chi_{\mathrm{dS}}
}{
\chi_{\mathrm{flat}}
}
=
1
-
\frac{
5d-2
}{
3(d+2)
}
L^2
+
O(L^4).
\]

Hence

\[
\boxed{
\frac{
K_{d,\mathrm{dS}}(L)
}{
K_d^{\mathrm{flat}}
}
=
1
-
\frac{
d^2+4d-4
}{
2(d+2)
}
L^2
+
O(L^4).
}
\]

For unit-radius de Sitter spacetime,

\[
R=d(d-1),
\]

and

\[
R_{TT}=-(d-1).
\]

Thus

\[
(d-1)
\left(
d a_d-b_d
\right)
=
-\frac{
d^2+4d-4
}{
2(d+2)
}.
\]

Substituting the previously determined \(a_d\) yields

\[
\boxed{
b_d
=
\frac{
d^2+2d-4
}{
4(d-1)(d+1)
}.
}
\]

## 13. Final first-curvature law

Therefore, for every fixed integer

\[
d\ge4,
\]

\[
\boxed{
K_{d,L}
=
K_d^{\mathrm{flat}}
\left[
1
+
L^2
\left(
-\frac{
d(d+6)
}{
4(d-1)(d+1)(d+2)
}
R
+
\frac{
d^2+2d-4
}{
4(d-1)(d+1)
}
R_{TT}
\right)
+
O(L^4)
\right].
}
\]

This determines the previously unknown coefficients \(A_d,B_d\).

## 14. 3+1 specialization

For

\[
d=4,
\]

\[
a_4=-\frac19,
\]

and

\[
b_4=\frac13.
\]

Since

\[
K_4^{\mathrm{flat}}=9\pi,
\]

\[
\boxed{
K_{4,L}
=
9\pi
\left[
1
-
\frac19
R L^2
+
\frac13
R_{TT}L^2
+
O(L^4)
\right].
}
\]

Equivalently,

\[
\boxed{
K_{4,L}
=
9\pi
+
\pi
\left(
-R+3R_{TT}
\right)
L^2
+
O(L^4).
}
\]

Thus the local \(3+1\) reconstruction law is

\[
\boxed{
1-p_{4,g,L}^{\mathrm{UPO}}(n)
\sim
\frac{
9\pi
+
\pi(-R+3R_{TT})L^2
+
O(L^4)
}{
n
}.
}
\]

The \(n\to\infty\) limit is taken at fixed sufficiently small \(L\).

## 15. Constant-curvature check

For de Sitter with sectional curvature \(+1\),

\[
R=d(d-1),
\qquad
R_{TT}=-(d-1).
\]

The formula gives

\[
\frac{
K_{d,L}
}{
K_d^{\mathrm{flat}}
}
=
1
-
\frac{
d^2+4d-4
}{
2(d+2)
}
L^2
+
O(L^4),
\]

matching the direct de Sitter calculation.

For the Einstein static universe,

\[
R=(d-1)(d-2),
\qquad
R_{TT}=0,
\]

it gives

\[
1
-
\frac{
d(d-2)(d+6)
}{
4(d+1)(d+2)
}
L^2
+
O(L^4),
\]

again matching the direct calculation.

## 16. Literature boundary

The total-volume and joint-area expansions used above are from:

G. W. Gibbons and S. N. Solodukhin, **The Geometry of Small Causal Diamonds**, *Physics Letters B* 649 (2007), 317--324.

Their arbitrary-dimensional formulas determine the Ricci structure of those observables.

The nearly-null interval coefficient \(C(L)\), its use to reconstruct the volume-null cross coefficient \(\chi\), and the resulting \(a_d,b_d\) for the arrow-erasure recovery functional are not imported from that work.

A targeted search did not locate these recovery coefficients in existing literature.

No absolute priority claim is made.

## 17. Remaining case d = 3

The derivation above uses the \(d\ge4\) null-joint leading coefficient.

In \(2+1\), the recovery error is bulk dominated.

Therefore the coefficients multiplying

\[
R
\]

and

\[
R_{TT}
\]

at order \(L^2\) in

\[
K_{3,L}
\]

must be calculated from the volume-time integral instead.

They are not obtained by substituting \(d=3\) into the formulas above.
