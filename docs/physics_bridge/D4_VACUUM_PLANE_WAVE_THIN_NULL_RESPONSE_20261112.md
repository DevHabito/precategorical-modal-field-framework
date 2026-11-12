# Lemma: Ricci-flat plane-wave response of the 3+1 thin-null volume coefficient

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic plane-wave lemma + numerical regression  
**Physical status:** isolates one explicit Weyl-squared contribution to the first vacuum correction of the arrow-erasure recovery coefficient  
**Novelty status:** plane-wave Jacobi equations are classical; the use of the resulting thin-null volume response in the present recovery problem is project-specific

## 1. Setting

Consider a four-dimensional Brinkmann plane wave with constant transverse tidal matrix

\[
H
=
\begin{pmatrix}
h&0\\
0&-h
\end{pmatrix}.
\]

The trace vanishes:

\[
\operatorname{tr}H=0,
\]

so the plane wave is Ricci flat.

Let the reference null geodesic have affine length

\[
L.
\]

Consider a timelike endpoint approaching the null-related endpoint with inward conjugate-null coordinate \(a>0\).

The nearly-null Alexandrov volume has the form

\[
V_{\rm thin}
=
c_{\rm thin}(H,L)
a^2
+
o(a^2).
\]

## 2. Jacobi channels

The two transverse Jacobi channels satisfy

\[
S_+''=hS_+,
\]

\[
S_-''=-hS_-,
\]

with

\[
S_\pm(0)=0,
\qquad
S_\pm'(0)=1.
\]

Thus

\[
\boxed{
S_+(u)
=
\frac{
\sinh(\sqrt h\,u)
}{
\sqrt h
},
}
\]

and

\[
\boxed{
S_-(u)
=
\frac{
\sin(\sqrt h\,u)
}{
\sqrt h
}
}
\]

for \(h>0\), with analytic continuation for the opposite sign.

Define the Riccati/Jacobi slopes

\[
P_\pm(u)
=
\frac{
S_\pm'(u)
}{
S_\pm(u)
}.
\]

Explicitly,

\[
P_+(u)
=
\sqrt h\,
\coth(\sqrt h\,u),
\]

\[
P_-(u)
=
\sqrt h\,
\cot(\sqrt h\,u).
\]

## 3. Thin Alexandrov cross-section

At affine position

\[
u\in(0,L),
\]

the future null cone from the initial endpoint and the past null cone from the final endpoint combine into the transverse quadratic form

\[
M_\pm(u)
=
P_\pm(u)
+
P_\pm(L-u).
\]

For transverse coordinates \(x_+,x_-\), the available null-conjugate thickness is

\[
a
-
\frac12
\left[
M_+(u)x_+^2
+
M_-(u)x_-^2
\right].
\]

The transverse section is the ellipse

\[
M_+(u)x_+^2
+
M_-(u)x_-^2
<
2a.
\]

Integrating the conjugate-null thickness over this ellipse gives

\[
\boxed{
dV_{\rm thin}(u)
=
\frac{
\pi a^2
}{
\sqrt{
M_+(u)M_-(u)
}
}
\,du.
}
\]

Therefore

\[
\boxed{
c_{\rm thin}(H,L)
=
\pi
\int_0^L
\frac{
du
}{
\sqrt{
M_+(u)M_-(u)
}
}.
}
\]

This is exact for the constant-profile plane wave.

## 4. Flat check

At

\[
h=0,
\]

\[
P_\pm(u)=\frac1u.
\]

Hence

\[
M_0(u)
=
\frac1u
+
\frac1{L-u}
=
\frac{
L
}{
u(L-u)
}.
\]

Therefore

\[
\begin{aligned}
c_{\rm flat}
&=
\pi
\int_0^L
\frac{
u(L-u)
}{
L
}
\,du\\
&=
\boxed{
\frac{
\pi L^2
}{
6
}.
}
\end{aligned}
\]

This agrees with the flat \(3+1\) Alexandrov-volume formula for a nearly null interval.

## 5. Small-curvature expansion

The Jacobi slopes have expansions

\[
P_+(u)
=
\frac1u
+
\frac{
hu
}{
3
}
-
\frac{
h^2u^3
}{
45
}
+
O(h^3u^5),
\]

and

\[
P_-(u)
=
\frac1u
-
\frac{
hu
}{
3
}
-
\frac{
h^2u^3
}{
45
}
+
O(h^3u^5).
\]

Write

\[
M_\pm
=
m_0
\pm
hm_1
+
h^2m_2
+
O(h^3L^5),
\]

with

\[
m_0
=
\frac{
L
}{
u(L-u)
},
\]

\[
m_1
=
\frac L3,
\]

\[
m_2
=
-
\frac{
u^3+(L-u)^3
}{
45
}.
\]

Multiplying,

\[
M_+M_-
=
m_0^2
+
h^2
\left(
2m_0m_2-m_1^2
\right)
+
O(h^4L^6).
\]

The linear \(h\) term cancels exactly.

That cancellation is the optical manifestation of

\[
\operatorname{tr}H=0.
\]

## 6. Volume response

Expanding the inverse square root,

\[
\frac1{\sqrt{M_+M_-}}
=
\frac1{m_0}
\left[
1
-
h^2
\left(
\frac{m_2}{m_0}
-
\frac{
m_1^2
}{
2m_0^2
}
\right)
+
O(h^4L^8)
\right].
\]

Set

\[
x=\frac uL.
\]

The relative correction reduces to

\[
6
\int_0^1
x(1-x)
\left[
\frac{
x(1-x)
\left(
x^3+(1-x)^3
\right)
}{
45
}
+
\frac{
x^2(1-x)^2
}{
18
}
\right]
dx.
\]

The integral evaluates exactly to

\[
\boxed{
\frac1{252}.
}
\]

Therefore

\[
\boxed{
\frac{
c_{\rm thin}(H,L)
}{
c_{\rm flat}(L)
}
=
1
+
\frac{
h^2L^4
}{
252
}
+
O(h^4L^8).
}
\]

Since

\[
\operatorname{tr}(H^2)
=
2h^2,
\]

this is equivalently

\[
\boxed{
\frac{
c_{\rm thin}(H,L)
}{
c_{\rm flat}(L)
}
=
1
+
\frac{
L^4
}{
504
}
\operatorname{tr}(H^2)
+
O(L^8\|H\|^4).
}
\]

## 7. Geometric meaning

For a vacuum null generator,

\[
H_{AB}
=
-
C_{AkBk}
\]

up to the sign convention for the Brinkmann profile.

Therefore the first correction to the thin-null endpoint-volume coefficient is quadratic in the optical Weyl tidal matrix.

The absence of a linear correction follows from

\[
R_{kk}
=
\operatorname{tr}H
=
0.
\]

Thus the plane-wave calculation makes explicit the mechanism anticipated by the vacuum \(L^4\) invariant classification:

\[
\boxed{
\text{Ricci-flat focusing}
\Longrightarrow
\text{shear/Weyl-squared response}.
}
\]

## 8. Role in the full recovery coefficient

For \(d=4\), the edge recovery integrand contains

\[
c_+^{-3/2}
c_-^{-3/2}
\]

in addition to:

- parent diamond volume;
- edge area;
- double-null cap normalization.

The present lemma supplies the \(O(L^4)\) contribution of each thin-null coefficient.

It does **not** by itself determine the full constants

\[
C_E,
\qquad
C_B
\]

in

\[
K_4
=
9\pi
+
L^4
(
C_EE^2+C_BB^2
)
+
o(L^4).
\]

The remaining contributions from the parent diamond, edge geometry, and double-null normalization must be included before those constants are claimed.

## 9. Regression

The repository script

tools/verify_d4_plane_wave_thin_null_response.py

evaluates the exact constant-profile Jacobi integral and compares it to

\[
1+\frac{h^2L^4}{252}.
\]

For decreasing \(h\), the scaled quantity

\[
\frac{
c(h)/c(0)-1
}{
h^2L^4
}
\]

converges to

\[
\frac1{252}.
\]

The numerical calculation is a regression only; the coefficient \(1/252\) is derived analytically above.

## 10. Next step

The remaining \(L^4\) vacuum problem is to combine:

1. the thin-null Weyl response derived here;
2. the vacuum expansion of the Alexandrov parent volume;
3. the vacuum expansion of the codimension-two edge;
4. the double-null cross-normalization response.

Only the resulting gauge-invariant combination determines whether

\[
C_E=C_B
\]

and therefore whether the recovery statistic is proportional to Bel-Robinson superenergy.
