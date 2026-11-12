> **Status update (2026-11-12):** the second independent vacuum calibration has now been completed. Both the exact Schwarzschild calculation and an independent LRS-Kasner/world-function calculation give \(a_4=683/9450\). Combined with the plane-wave result in this file, this gives \(b_4=37/1050\). See \`D4_KASNER_WORLD_FUNCTION_PURE_ELECTRIC_CALIBRATION_20261112.md\`.

# Theorem candidate: symmetric plane-wave calibration of the d = 4 vacuum response

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact analytic calibration + independent quadrature  
**Scope:** sufficiently small centered \(3+1\)-dimensional diamonds in a Ricci-flat symmetric plane wave, before the first conjugate phase  
**Novelty status:** symmetric plane-wave geodesics and Jacobi matrices are classical; the recovery-response calibration is project-specific

## 1. Vacuum response basis

The invariant-basis theorem gives, in \(3+1\) vacuum,

\[
\boxed{
\frac{
K_{4,g}(D_L)
}{
9\pi
}
=
1
+
L^4
\left[
a_4E^2
+
b_4B^2
\right]_o
+
o(L^4).
}
\]

A single type-N plane-wave calibration cannot determine \(a_4\) and \(b_4\) separately because

\[
E^2=B^2
\]

for a vacuum plane wave.

It can determine the exact combination

\[
a_4+b_4.
\]

## 2. Symmetric vacuum plane wave

Use Brinkmann coordinates with signature \((-+++)\):

\[
\boxed{
ds^2
=
-2\,du\,dv
+
(dx^1)^2
+
(dx^2)^2
+
H_{ij}x^ix^j\,du^2,
}
\]

with constant trace-free profile

\[
\boxed{
H
=
\begin{pmatrix}
-\omega^2&0\\
0&+\omega^2
\end{pmatrix}.
}
\]

The only independent curvature components are

\[
R_{uiuj}
=
-H_{ij}.
\]

Because

\[
\operatorname{tr}H=0,
\]

the metric is Ricci flat.

Take the central timelike geodesic

\[
x^1=x^2=0.
\]

## 3. Centered diamond

Introduce ordinary central-axis coordinates

\[
t
=
\frac{
u+v
}{
\sqrt2
},
\qquad
z
=
\frac{
v-u
}{
\sqrt2
}.
\]

On the central worldline

\[
z=0,
\]

\[
u=v=\frac t{\sqrt2},
\]

and

\[
ds^2=-dt^2.
\]

Choose endpoints at proper times

\[
t=\pm L.
\]

Their null-phase separation is therefore

\[
\boxed{
U
=
u_q-u_p
=
\sqrt2\,L.
}
\]

Define the dimensionless focusing parameter

\[
\boxed{
z=\omega U.
}
\]

The first conjugate phase occurs at

\[
z=\pi.
\]

The following analysis is restricted to

\[
|z|<\pi.
\]

## 4. Exact transverse Jacobi matrices

For a subsegment of phase length \(r\), the two transverse Jacobi solutions are:

### Focusing direction

\[
B_1(r)
=
\frac{
\sin(\omega r)
}{
\omega
}.
\]

### Defocusing direction

\[
B_2(r)
=
\frac{
\sinh(\omega r)
}{
\omega
}.
\]

For a parent segment of phase \(U\), at intermediate phase \(u\), the causal cross-section is governed by

\[
\boxed{
S_1(u)
=
\omega
\frac{
\sin(\omega U)
}{
\sin(\omega u)
\sin(\omega(U-u))
},
}
\]

and

\[
\boxed{
S_2(u)
=
\omega
\frac{
\sinh(\omega U)
}{
\sinh(\omega u)
\sinh(\omega(U-u))
}.
}
\]

These are the exact symmetric-plane-wave analogues of the flat

\[
\frac{U}{u(U-u)}
\]

focusing factors.

## 5. Exact parent interval volume

At fixed phase \(u\), the timelike causal cross-section is an ellipse.

Integrating first over the transverse ellipse and then over the conjugate null coordinate gives

\[
\boxed{
V(U,\delta)
=
\pi\delta^2 I(U),
}
\]

where

\[
\boxed{
I(U)
=
\int_0^U
\frac{
du
}{
\sqrt{
S_1(u)S_2(u)
}
}.
}
\]

Here \(\delta\) is the timelike inward displacement measured in the conjugate null coordinate.

In the flat limit,

\[
S_1=S_2=
\frac{
U
}{
u(U-u)
},
\]

so

\[
I(U)
=
\frac{
U^2
}{6},
\]

and

\[
V_{\rm flat}
=
\frac{
\pi
}{6}
U^2\delta^2.
\]

## 6. Exact thin-null coefficient

Because the symmetric plane wave admits the standard plane-wave homothety in the transverse/conjugate-null directions, the interval volume is exactly quadratic in \(\delta\).

Thus the thin-null coefficient for a phase segment of length \(r\) is

\[
\boxed{
c(r)
=
\pi I(r).
}
\]

No asymptotic approximation is needed for this statement.

## 7. Dimensionless functions

Set

\[
x=\frac uU,
\qquad
z=\omega U.
\]

Define

\[
\boxed{
a_z(x)
=
z
\frac{
\sin z
}{
\sin(zx)\sin(z(1-x))
},
}
\]

\[
\boxed{
b_z(x)
=
z
\frac{
\sinh z
}{
\sinh(zx)\sinh(z(1-x))
}.
}
\]

Then

\[
S_1
=
\frac1U
a_z(x),
\]

\[
S_2
=
\frac1U
b_z(x).
\]

Define

\[
\boxed{
F(z)
=
\int_0^1
\frac{
dx
}{
\sqrt{
a_z(x)b_z(x)
}
}.
}
\]

Therefore

\[
\boxed{
I(U)
=
U^2F(z).
}
\]

The flat value is

\[
\boxed{
F(0)=\frac16.
}
\]

## 8. Small-z thin-volume expansion

Expanding the exact functions gives

\[
\boxed{
F(z)
=
\frac16
\left[
1+
\frac{
z^4
}{252}
+
O(z^8)
\right].
}
\]

The \(z^2\) term cancels because the vacuum profile has zero trace:

\[
\operatorname{tr}H=0.
\]

This is the interval-volume manifestation of the absence of an \(O(L^2)\) Ricci correction in vacuum.

## 9. Exact volume-null joint coefficient

For the \(d=4\) recovery law, use volume-null coordinates built from the exact subinterval volumes.

At the edge, define the two null deficits

\[
\delta_-,
\qquad
\delta_+.
\]

The subinterval volumes are

\[
V(p,z)
=
c(u)\delta_-^2,
\]

\[
V(z,q)
=
c(U-u)\delta_+^2.
\]

The inverse-metric cross contraction of the two deficits is

\[
\boxed{
G
=
g^{-1}
(
d\delta_-,
d\delta_+
)
=
\frac12
x^T
S^2
x
}
\]

on the edge, where

\[
S
=
\operatorname{diag}
(
S_1,S_2
).
\]

Using Lorentzian coarea and integrating over the edge ellipse gives the exact invariant ratio

\[
\boxed{
\frac{
\mathcal J_4
}{
V_D^2
}
=
\frac1\pi
I(U)
\int_0^U
\frac{
S_1(u)+S_2(u)
}{
[S_1(u)S_2(u)]^2
[I(u)I(U-u)]^{3/2}
}
\,du.
}
\]

For flat spacetime this gives

\[
\boxed{
\frac{
\mathcal J_4
}{
V_D^2
}
=
\frac{
72
}{\pi},
}
\]

matching the independent curved-on-flat normalization audit.

Since all remaining factors in \(K_4\) are universal,

\[
\frac{
K_{\rm PW}
}{
K_{\rm Mink}
}
=
\frac{
(\mathcal J_4/V_D^2)_{\rm PW}
}{
72/\pi
}.
\]

## 10. Dimensionless exact K ratio

Substitution of the dimensionless functions gives

\[
\boxed{
\frac{
K_{\rm PW}(z)
}{
K_{\rm Mink}
}
=
\frac{
F(z)
}{72}
\int_0^1
\frac{
a_z(x)+b_z(x)
}{
[a_z(x)b_z(x)]^2
[x(1-x)]^3
[
F(zx)F(z(1-x))
]^{3/2}
}
\,dx.
}
\]

This is an exact one-dimensional nested-integral representation for the recovery coefficient in the symmetric vacuum plane wave, valid before the first conjugate phase.

## 11. Exact small-z expansion

The transverse factors have expansions

\[
a_z(x)
=
\frac1{x(1-x)}
+
O(z^2),
\]

\[
b_z(x)
=
\frac1{x(1-x)}
+
O(z^2),
\]

with opposite \(z^2\) corrections.

Using

\[
F(z)
=
\frac16
\left(
1+\frac{z^4}{252}
\right)
+
O(z^8),
\]

the entire exact integrand expands to

\[
\boxed{
\frac{
a_z+b_z
}{
(ab)^2[x(1-x)]^3
[F(zx)F(z(1-x))]^{3/2}
}
=
432
+
\frac{
6
}{
35}
\left(
26x^4
-
52x^3
-
202x^2
+
228x
-
15
\right)
z^4
+
O(z^8).
}
\]

The \(z^2\) term cancels identically.

Integrating,

\[
\int_0^1(\cdots)\,dx
=
432
+
\frac{
716
}{
175
}
z^4
+
O(z^8).
\]

Multiplying by \(F(z)/72\) yields

\[
\boxed{
\frac{
K_{\rm PW}(z)
}{
K_{\rm Mink}
}
=
1
+
\frac{
127
}{
9450
}
z^4
+
O(z^8).
}
\]

Thus the symmetric vacuum plane wave gives an exact rational response coefficient in the natural focusing variable \(z\).

## 12. Independent quadrature check

The unexpanded exact nested-integral formula was evaluated numerically.

The measured values of

\[
\frac{
K_{\rm PW}/K_{\rm Mink}-1
}{
z^4
}
\]

were:

| \(z\) | measured |
|---:|---:|
| 0.30 | 0.0134408304644 |
| 0.20 | 0.0134394846739 |
| 0.10 | 0.0134391741513 |
| 0.05 | 0.0134391549267 |

The exact prediction is

\[
\boxed{
\frac{
127
}{
9450
}
=
0.0134391534392\ldots
}
\]

and the quadrature converges monotonically toward it over the tested sequence.

## 13. Observer Weyl invariants

On the central axis,

\[
T
=
\partial_t
=
\frac{
\partial_u+\partial_v
}{
\sqrt2
}.
\]

The only nonzero curvature components are

\[
C_{uiuj}
=
-H_{ij}.
\]

Therefore the observer electric tensor in the transverse plane is

\[
\boxed{
E_{ij}
=
-\frac12H_{ij}.
}
\]

The longitudinal electric eigenvalue is zero.

Hence

\[
E^2
=
\frac14
\operatorname{tr}(H^2).
\]

For

\[
H
=
\operatorname{diag}
(-\omega^2,+\omega^2),
\]

\[
\boxed{
E^2
=
\frac{
\omega^4
}{2}.
}
\]

A vacuum plane wave is type N, so

\[
C_{\mu\nu\rho\sigma}
C^{\mu\nu\rho\sigma}
=
0.
\]

Using

\[
C^2
=
8(E^2-B^2),
\]

we get

\[
\boxed{
B^2=E^2=\frac{\omega^4}{2}.
}
\]

## 14. Convert z to physical half-size L

The phase separation is

\[
U=\sqrt2L.
\]

Therefore

\[
z^4
=
(\omega U)^4
=
4\omega^4L^4.
\]

Since

\[
E^2=B^2=\frac{\omega^4}{2},
\]

the vacuum ansatz gives

\[
L^4
\left(
a_4E^2+b_4B^2
\right)
=
\frac{
a_4+b_4
}{2}
\omega^4L^4.
\]

The plane-wave calculation gives

\[
\frac{
127
}{
9450
}
z^4
=
4
\frac{
127
}{
9450
}
\omega^4L^4.
\]

Thus

\[
\frac{
a_4+b_4
}{2}
=
4
\frac{
127
}{
9450
}.
\]

Hence

\[
\boxed{
a_4+b_4
=
\frac{
508
}{
4725
}
\approx
0.107513227513.
}
\]

This fixes one exact linear combination of the two \(3+1\) vacuum recovery coefficients.

## 15. What is still unknown

A type-N plane wave obeys

\[
E^2=B^2.
\]

Therefore it cannot separate

\[
a_4
\quad\text{from}\quad
b_4.
\]

A second independent vacuum calibration is required.

A purely electric vacuum geometry,

\[
B=0,
\]

would determine \(a_4\) directly.

A static type-D field such as a sufficiently small Schwarzschild vacuum diamond is a natural candidate, but no coefficient is asserted before that calculation is completed.

## 16. Caustic boundary

The exact representation is restricted to the conjugate-free regime.

The focusing factor

\[
\sin z
\]

vanishes at

\[
z=\pi.
\]

At that point the null Jacobi operator loses its spectral gap and the regular-edge compact-containment theorem fails.

Thus the same exact model simultaneously calibrates the regular vacuum response and exhibits the boundary of its validity.

## 17. Reproducibility

The repository script

\[
\texttt{tools/derive\_d4\_plane\_wave\_vacuum\_response.py}
\]

performs:

1. symbolic expansion to \(z^4\);
2. exact rational recovery of
   \[
   127/9450;
   \]
3. independent numerical quadrature of the unexpanded formula;
4. conversion to
   \[
   a_4+b_4=508/4725.
   \]

## 18. Current status

The exact combination

\[
\boxed{
a_4+b_4
=
508/4725
}
\]

is internally derived and independently numerically checked.

It remains externally unverified.

The next vacuum target is a second geometry with

\[
E^2/B^2
\ne1,
\]

preferably a purely electric vacuum field, to determine \(a_4\) and \(b_4\) separately.
