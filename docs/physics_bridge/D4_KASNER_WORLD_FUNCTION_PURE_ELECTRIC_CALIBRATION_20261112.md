# Independent d = 4 pure-electric calibration from LRS Kasner and Synge world functions

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact internal derivation; independent of the Schwarzschild optical calculation; externally unverified  
**Scope:** sufficiently small centered Alexandrov intervals in the LRS Kasner vacuum  
**Purpose:** test the \(3+1\) vacuum recovery coefficient by a second geometry and a second computational route

## 1. Geometry

Use the nontrivial locally rotationally symmetric Kasner vacuum

\[
\boxed{
ds^2
=
-dt^2
+
t^{-2/3}dx^2
+
t^{4/3}(dy^2+dz^2).
}
\]

The Kasner exponents are

\[
-\frac13,\qquad \frac23,\qquad \frac23.
\]

The comoving line

\[
x=y=z=0
\]

is a timelike geodesic.

Choose centered tips

\[
p=(1-L,0,0,0),
\qquad
q=(1+L,0,0,0).
\]

Therefore \(L\) is exactly the geodesic half proper-time separation.

At the midpoint \(t=1\), relative to the comoving observer,

\[
B_{ij}=0,
\]

and the electric Weyl eigenvalues are

\[
-\frac49,\qquad \frac29,\qquad \frac29.
\]

Hence

\[
\boxed{
E^2=\frac8{27}.
}
\]

This geometry is therefore a clean purely electric calibration independent of Schwarzschild.

## 2. Exact null geodesics

Spatial translations are Killing symmetries.

Normalize the conserved spatial momenta so that

\[
P_x^2+P_\perp^2=1,
\]

and define

\[
c=P_x^2.
\]

Along a null geodesic,

\[
\boxed{
\frac{dt}{d\lambda}
=
\mathcal E(t,c)
=
\sqrt{
c\,t^{2/3}
+
(1-c)t^{-4/3}
}.
}
\]

The coordinate displacements obey

\[
\boxed{
\frac{dx}{dt}
=
\frac{
\sqrt c\,t^{2/3}
}{
\mathcal E(t,c)
},
}
\]

\[
\boxed{
\frac{d\rho_\perp}{dt}
=
\frac{
\sqrt{1-c}\,t^{-4/3}
}{
\mathcal E(t,c)
}.
}
\]

These one-dimensional integrals determine the null cones exactly.

The repository checker

tools/derive_d4_kasner_world_function_pure_electric_calibration.py

expands these integrals directly in \(L\) with exact rational arithmetic.

## 3. Direction parameter and edge

Let

\[
\mu
\]

be the axial direction cosine of a coordinate ray at the midpoint and set

\[
w=\mu^2.
\]

Solving the past- and future-cone direction equations and then equating their ray radii gives the edge time

\[
t_E=1+L\,Y_E,
\]

with

\[
\boxed{
Y_E
=
\left(
\frac w2-\frac13
\right)L
+
\frac{
216w^3-477w^2+324w-56
}{
648
}
L^3
+
O(L^5).
}
\]

Equivalently,

\[
t_E
=
1+
\left(
\frac w2-\frac13
\right)L^2
+
O(L^4).
\]

Unlike a locally static calibration, the edge is not located on one constant-\(t\) slice.

The directional dependence is retained throughout the calculation rather than averaged prematurely.

## 4. Exact parent volume

On a constant-\(t\) Kasner slice,

\[
\sqrt{\det g_{\rm spatial}}=t.
\]

The coordinate-space causal section is star shaped.

For each direction the radial boundary is the smaller of the past-tip future cone and the future-tip past cone, with the switch occurring at \(Y_E(\mu)\).

Integrating the exact null-cone series gives

\[
\boxed{
\frac{
V_{\rm Kasner}
}{
V_{\rm Mink}
}
=
1+
\frac{
68
}{
8505
}
L^4
+
O(L^6).
}
\]

Because

\[
E^2=\frac8{27},
\]

this is

\[
\boxed{
\frac{
\delta V
}{
V_{\rm Mink}
}
=
\frac{
17
}{
630
}
E^2L^4
+
O(L^6).
}
\]

The \(L^2\) and \(L^3\) coefficients vanish exactly.

A separate direct numerical integration of the unexpanded Kasner cones converges to

\[
\frac{68}{8505}
=
0.00799529688418\ldots
\]

when extrapolated to \(L\to0\).

## 5. Edge area

Using the exact edge embedding

\[
X^\mu(\mu,\phi)
=
\left(
t_E(\mu),
\rho_E(\mu)\mu,
\rho_E(\mu)\sqrt{1-\mu^2}\cos\phi,
\rho_E(\mu)\sqrt{1-\mu^2}\sin\phi
\right),
\]

the induced area density relative to the flat sphere is

\[
\begin{aligned}
\frac{dA}{dA_0}
={}&
1
+
\frac{
45\mu^4-48\mu^2+7
}{
27
}
L^2
\\
&+
\frac{
5103\mu^8
-12663\mu^6
+10467\mu^4
-3117\mu^2
+194
}{
1458
}
L^4
+
O(L^6).
\end{aligned}
\]

The \(L^2\) term integrates to zero.

The averaged fourth-order term is

\[
\boxed{
\frac{
\delta A
}{
A_0
}
=
\frac{
2
}{
135
}
E^2L^4
+
O(L^6).
}
\]

This agrees with the \(d=4\) purely electric ACD edge-area coefficient in Wang's 2019 RNC calculation.

## 6. Raw Synge cross-normalization

Let

\[
S_-=2\sigma(p,x),
\qquad
S_+=2\sigma(x,q),
\]

and define

\[
\chi
=
\left|
g^{-1}(dS_-,dS_+)
\right|.
\]

For a null geodesic whose conserved spatial momentum norm is one,

\[
d(2\sigma)
=
2\lambda\,p_\mu dx^\mu
\]

at the endpoint, where

\[
\lambda
=
\int
\frac{dt}{
\mathcal E(t,c)
}
\]

is its affine length in that normalization.

Using the exact past and future null generators at the edge gives

\[
q(\mu)
=
\ln\frac{\chi}{8L^2}.
\]

Its expansion is

\[
\boxed{
q(\mu)
=
\frac{
2(3\mu^2-1)
}{
27
}
L^2
+
\frac{
540\mu^6
-1467\mu^4
+1164\mu^2
-137
}{
3645
}
L^4
+
O(L^6).
}
\]

The first term is exactly the general RNC result

\[
q_1=-\frac13L^2E_{nn}.
\]

## 7. Why the full local edge density must be used

The area density and \(\chi\) both have zero-mean \(O(L^2)\) anisotropies.

Therefore it is incorrect at \(O(L^4)\) to multiply a total area by a separately averaged logarithmic cross-normalization.

The invariant object is the local product.

For the Kasner edge,

\[
\boxed{
\left\langle
\frac{dA}{dA_0}
\left(
\frac{\chi}{\chi_0}
\right)^{-3}
\right\rangle
=
1+
\frac{
296
}{
18225
}
L^4
+
O(L^6).
}
\]

Since

\[
E^2=\frac8{27},
\]

the corresponding purely electric coefficient is

\[
\boxed{
\frac{
37
}{
675
}
E^2L^4.
}
\]

This automatically includes all covariance terms generated by the local \(O(L^2)\) anisotropies.

## 8. Thin-null focusing

For

\[
E
=
\operatorname{diag}
\left(
-\frac49,
\frac29,
\frac29
\right),
\qquad
B=0,
\]

the squared screen tidal matrix along a null direction with axial cosine \(\mu\) is

\[
\boxed{
\mathcal H_{AB}\mathcal H^{AB}
=
\frac89(1-\mu^2)^2.
}
\]

Its spherical average is

\[
\boxed{
\left\langle
\mathcal H^2
\right\rangle
=
\frac{
64
}{
135
}
=
\frac85E^2.
}
\]

The universal \(d=4\) thin-null Jacobi result gives, for each sheet,

\[
F
=
1+
\frac{
L^4
}{
504
}
\mathcal H^2
+\cdots.
\]

The recovery integrand contains

\[
F_-^{-3/2}F_+^{-3/2}.
\]

Thus the two-sheet averaged contribution is

\[
\boxed{
-\frac1{105}E^2L^4.
}
\]

## 9. Independent closure of the purely electric coefficient

The three independently calculated pieces are

\[
\text{parent volume}
=
\frac{17}{630}E^2L^4,
\]

\[
\text{local edge and cross-normalization}
=
\frac{37}{675}E^2L^4,
\]

\[
\text{thin-null focusing}
=
-\frac1{105}E^2L^4.
\]

Therefore

\[
\begin{aligned}
a_4
&=
\frac{17}{630}
+
\frac{37}{675}
-
\frac1{105}
\\
&=
\boxed{
\frac{683}{9450}
}.
\end{aligned}
\]

This is exactly the coefficient previously obtained by the independent Schwarzschild optical calculation.

The Kasner derivation does not use:

- Schwarzschild coordinates;
- Schwarzschild optical geometry;
- the Schwarzschild weak-field expansion;
- rational reconstruction from the Schwarzschild numerical data.

It therefore supplies a genuine method-and-geometry redundancy check.

## 10. Consequence for the magnetic coefficient

The independent symmetric-plane-wave calibration gives

\[
a_4+b_4
=
\frac{508}{4725}.
\]

Combining it with the Kasner result gives again

\[
\boxed{
b_4=\frac{37}{1050}.
}
\]

Thus the internally supported \(3+1\) vacuum response remains

\[
\boxed{
\frac{
K_{4,g}(D_L)
}{
9\pi
}
=
1+
L^4
\left[
\frac{683}{9450}E^2
+
\frac{37}{1050}B^2
\right]_o
+
o(L^4).
}
\]

## 11. Literature consistency and one unresolved discrepancy

Jinzhao Wang's 2019 paper computes the ACD geometry in Riemann normal coordinates and gives, in Eq. (79), a vacuum total-volume formula.

Specializing that published formula to \(d=4\), using

\[
D^2=4E^2,
\qquad
H^2=2B^2,
\]

gives

\[
\left.
\frac{\delta V}{V_0}
\right|_{\rm Wang}
=
L^4
\left[
\frac{127}{4725}E^2
+
\frac1{105}B^2
\right].
\]

For a purely electric field this predicts

\[
\frac{127}{4725}E^2L^4.
\]

The direct Kasner cone calculation instead gives

\[
\frac{17}{630}E^2L^4.
\]

Their difference is

\[
\boxed{
\frac1{9450}E^2L^4.
}
\]

This is not explained by a factor-of-two size convention: Wang explicitly places the ACD vertices at RNC coordinates

\[
(\pm l,0,\ldots,0).
\]

At the same time, the Kasner edge-area calculation reproduces Wang's ACD edge-area coefficient exactly.

Therefore the discrepancy appears localized to the total-volume result or to a subtle assumption in comparing the two calculations.

The repository does **not** currently label the published formula incorrect.

The discrepancy requires an additional independent check.

## 12. Reproducibility

The exact checker is

tools/derive_d4_kasner_world_function_pure_electric_calibration.py

and uses exact SymPy rational arithmetic.

The calculation performed during development also independently verified:

\[
\frac{V}{V_0}
=
1+
\frac{68}{8505}L^4+\cdots,
\]

\[
\left\langle
\frac{dA}{dA_0}
(\chi/\chi_0)^{-3}
\right\rangle
=
1+
\frac{296}{18225}L^4+\cdots,
\]

and

\[
a_4=\frac{683}{9450}.
\]

## 13. Next target

There are now two separate questions.

### Recovery problem

The purely electric coefficient has passed two independent analytic calibrations:

1. Schwarzschild optical geometry;
2. LRS Kasner world-function/null-cone geometry.

The next recovery-level task is an independent magnetic/radiative check of \(b_4\), beyond using the plane-wave sum with the electric calibration.

### Small-diamond geometry problem

The total-volume discrepancy with Wang Eq. (79) should be stress-tested on a second exact Ricci-flat geometry.

The symmetric Cahen--Wallach plane wave is the natural candidate because its causal cross-sections are analytically integrable and its curvature is covariantly constant.

Only after that comparison should any correction to the published ACD volume coefficient be proposed.
