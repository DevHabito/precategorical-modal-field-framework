> **Status update (2026-11-12):** this first-order RNC audit led to the independent LRS-Kasner/world-function closure. The full local edge density, rather than separately averaged area and logarithmic factors, reproduces \(a_4=683/9450\). See \`D4_KASNER_WORLD_FUNCTION_PURE_ELECTRIC_CALIBRATION_20261112.md\`. The standalone second-order average of \(q=\log(\chi/\chi_0)\) should not be treated as an invariant coefficient without fixing the edge-direction identification; the invariant object is the complete local edge integrand.

# RNC/world-function audit of the d = 4 vacuum null-edge anisotropy

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic first-order lemma + exact plane-wave second-order calibration  
**Scope:** centered sufficiently small regular \(3+1\)-dimensional Ricci-flat Alexandrov diamonds  
**Purpose:** begin an independent world-function verification of the vacuum recovery coefficients and repair an earlier factorization error

## 1. Why this calculation is needed

The intrinsic recovery functional is

\[
\mathcal J_4
=
\int_\Sigma
\left[
g^{-1}
\left(
d\mathcal V_-^{1/2},
d\mathcal V_+^{1/2}
\right)
\right]^{-3}
dA_\Sigma.
\]

A previous bookkeeping note attempted to separate the order-\(L^4\) correction into:

- parent volume;
- total edge area;
- thin-null focusing;
- an averaged logarithmic cross-normalization.

That separation is incomplete in vacuum.

The reason is that the local edge measure and the local cross-normalization both contain anisotropic terms linear in the Weyl tensor. Their separate spherical averages vanish, but their products do not.

Those products contribute at order

\[
C^2L^4.
\]

Therefore an integrated edge functional cannot be replaced, at this order, by the product of a total edge area and exponentials of separately averaged logarithms.

## 2. First-curvature world-function expansion

Use Riemann normal coordinates centered at the diamond midpoint \(o\), with signature \((-+++)\).

To first order in curvature,

\[
g_{\mu\nu}(z)
=
\eta_{\mu\nu}
-
\frac13
C_{\mu\alpha\nu\beta}
z^\alpha z^\beta
+
O(L^3\nabla C,L^4C^2).
\]

Let

\[
\Delta^\mu=x^\mu-y^\mu,
\qquad
\bar z^\mu=\frac{x^\mu+y^\mu}{2}.
\]

At first order in the metric perturbation, the flat straight segment is sufficient in the world-function action because the flat geodesic is stationary.

Thus

\[
\boxed{
2\sigma(y,x)
=
\eta_{\mu\nu}\Delta^\mu\Delta^\nu
-
\frac13
C_{\mu\alpha\nu\beta}
\Delta^\mu\Delta^\nu
\bar z^\alpha\bar z^\beta
+
O(L^5\nabla C,L^6C^2).
}
\]

The possible term proportional to

\[
C_{\mu\alpha\nu\beta}
\Delta^\mu\Delta^\nu
\Delta^\alpha\Delta^\beta
\]

vanishes by the Riemann antisymmetries.

This is the only world-function input needed for the first-order edge calculation.

## 3. Centered tips and flat edge

Choose

\[
p=(-L,\mathbf 0),
\qquad
q=(+L,\mathbf 0).
\]

Let

\[
n^in_i=1,
\]

and define

\[
E_{nn}
=
E_{ij}n^in^j,
\qquad
E_{ij}=C_{0i0j}.
\]

The flat edge point in direction \(n\) is

\[
x_0=(0,Ln^i).
\]

For both null sheets, the first curvature correction to \(2\sigma\) at \(x_0\) is

\[
-\frac13L^4E_{nn}.
\]

The equality of the two corrections implies that the edge remains on

\[
t=0
\]

at first order.

Solving either null condition gives

\[
\boxed{
\frac{\delta r}{L}
=
\frac16L^2E_{nn}.
}
\]

Thus the edge is distorted anisotropically even though

\[
\langle E_{nn}\rangle_{S^2}=0.
\]

## 4. World-function cross-normalization

Define

\[
S_-=2\sigma(p,x),
\qquad
S_+=2\sigma(x,q),
\]

and use the positive magnitude of the null-sheet cross contraction

\[
\chi
=
\left|
g^{-1}(dS_-,dS_+)
\right|.
\]

In flat spacetime,

\[
\chi_0=8L^2.
\]

Differentiating the first-order world functions, evaluating the inverse RNC metric at the perturbed edge, and retaining the terms linear in Weyl gives

\[
\boxed{
\frac{\chi}{\chi_0}
=
1
-
\frac13L^2E_{nn}
+
O(L^3\nabla C,L^4C^2).
}
\]

Therefore, writing

\[
q
=
\ln\frac{\chi}{\chi_0},
\]

the linear anisotropy is

\[
\boxed{
q_1(n)
=
-\frac13L^2E_{nn}.
}
\]

No linear magnetic scalar is available in this parity-even local quantity.

The symbolic checker

tools/verify_d4_rnc_first_order_edge_anisotropy.py

reproduces the coefficient using an explicit trace-free purely electric Weyl tensor.

## 5. First-order edge-area anisotropy

The radial shift contributes

\[
2\frac{\delta r}{L}
=
\frac13L^2E_{nn}
\]

to the area density.

The RNC spatial metric contributes

\[
-\frac16L^2E_{nn}.
\]

Hence

\[
\boxed{
\frac{\delta dA^{(1)}}{dA_0}
=
a_1(n)
=
\frac16L^2E_{nn}.
}
\]

Equivalently,

\[
\boxed{
a_1=-\frac12q_1.
}
\]

Both first-order terms integrate to zero over the sphere, but this does not make them irrelevant at second order.

## 6. Missing quadratic covariance term

Consider only the local area and cross-normalization factors,

\[
\frac{dA}{dA_0}
=
1+a_1+a_2+\cdots,
\]

\[
\frac{\chi}{\chi_0}
=
e^{q_1+q_2+\cdots}.
\]

Then

\[
\frac{
dA\,\chi^{-3}
}{
dA_0\,\chi_0^{-3}
}
=
1
+
(a_1-3q_1)
+
\left[
a_2
-3q_2
+\frac92q_1^2
-3a_1q_1
\right]
+\cdots.
\]

Since

\[
a_1=-\frac12q_1,
\]

the quadratic contribution generated solely by the first-order anisotropies is

\[
\boxed{
\frac92q_1^2-3a_1q_1
=
6q_1^2.
}
\]

Using

\[
q_1
=
-\frac13L^2E_{nn},
\]

and the standard STF angular identity

\[
\left\langle
(E_{nn})^2
\right\rangle_{S^2}
=
\frac{2}{15}E^2,
\]

gives

\[
\boxed{
\left\langle
\frac92q_1^2-3a_1q_1
\right\rangle
=
\frac{4}{45}E^2L^4.
}
\]

This term was absent from the earlier factorized logarithmic bookkeeping.

It is not optional and it is numerically large enough to affect any attempted \(L^4\) coefficient extraction.

## 7. Consequence for the earlier decomposition

The note

D4_VACUUM_L4_KNOWN_RECOVERY_TERMS_20261112.md

must not be used as a complete \(L^4\) decomposition.

Its reduction of the edge integral to a total edge area multiplied by separately averaged logarithmic corrections misses products of zero-mean first-order anisotropies.

The individual geometric inputs in that note may still be useful, but their assembly into the full coefficient is superseded.

The intrinsic integral must be expanded locally before angular integration.

## 8. Exact plane-wave world-function test

The symmetric Ricci-flat plane wave provides an exact world-function check.

Let

\[
z=\omega U,
\qquad
x=\frac{u}{U},
\]

and define

\[
a_z(x)
=
z
\frac{\sin z}{
\sin(zx)\sin(z(1-x))
},
\]

\[
b_z(x)
=
z
\frac{\sinh z}{
\sinh(zx)\sinh(z(1-x))
}.
\]

The two exact null sheets give the edge condition

\[
S_1x_1^2+S_2x_2^2=2U.
\]

Parameterize the transverse ellipse by an angle \(\phi\).

Direct contraction of the two world-function gradients gives

\[
\boxed{
\frac{\chi}{\chi_0}
=
x(1-x)
\left[
a_z(x)\cos^2\phi
+
b_z(x)\sin^2\phi
\right],
}
\]

with

\[
\chi_0=4U^2=8L^2.
\]

This formula is exact before the first conjugate phase.

## 9. Plane-wave expansion

Write

\[
q
=
\ln\frac{\chi}{\chi_0}.
\]

The exact expansion begins

\[
\boxed{
q
=
-\frac{z^2}{3}
x(1-x)\cos(2\phi)
+
z^4 q_2(x,\phi)
+
O(z^6).
}
\]

The \(z^2\) term agrees exactly with the general RNC result because, for the plane wave,

\[
E_{nn}L^2
=
z^2x(1-x)\cos(2\phi).
\]

The exact \(z^4\) coefficient may be written

\[
\boxed{
q_2(x,\phi)
=
\frac{
y^2\left[6-5\cos^2(2\phi)\right]-2y
}{
90
},
\qquad
y=x(1-x).
}
\]

Using the flat-edge measure,

\[
x\in[0,1],
\qquad
\phi\in[0,2\pi),
\]

gives

\[
\boxed{
\left\langle q_2\right\rangle_{\rm PW}
=
-\frac{13}{5400}z^4.
}
\]

The checker

tools/verify_d4_plane_wave_world_function_cross_normalization.py

performs this expansion and angular integration with exact SymPy rational arithmetic.

## 10. Invariant interpretation of the plane-wave result

For the symmetric plane wave,

\[
E^2=B^2=\frac{\omega^4}{2},
\]

and

\[
z^4=4\omega^4L^4.
\]

Therefore the genuine second-order logarithmic cross-normalization satisfies the type-N constraint

\[
\boxed{
Q_E+Q_B
=
-\frac{13}{1350},
}
\]

if the generic second-order expansion is written as

\[
\left\langle q_2\right\rangle
=
L^4
\left[
Q_EE^2+Q_BB^2
\right].
\]

This constraint comes directly from the world function and does not use the Schwarzschild recovery calibration.

## 11. Current frontier

The independent verification problem is now narrower.

We do not need to recompute the whole recovery coefficient at once.

The remaining world-function target is to determine the purely electric value

\[
Q_E
\]

directly in a second geometry or from the general RNC world-function expansion.

Once \(Q_E\) is known, the exact plane-wave relation

\[
Q_E+Q_B=-\frac{13}{1350}
\]

determines \(Q_B\).

The full intrinsic edge integral can then be rebuilt locally, including the mandatory covariance term

\[
\frac{4}{45}E^2L^4,
\]

and compared against the independently obtained recovery coefficients

\[
a_4=\frac{683}{9450},
\qquad
b_4=\frac{37}{1050}.
\]

That comparison will be a substantially stronger coordinate-method audit than the superseded factorized-log approach.

## 12. Literature boundary

The ingredients used here are standard:

- Synge world function and its endpoint derivatives;
- Riemann normal coordinates;
- perturbative small-causal-diamond geometry;
- Jacobi propagators in plane waves.

The project-specific contribution is the application of those objects to the local integrand of the arrow-erasure recovery functional and the identification of the missing anisotropy covariance.

Relevant background includes Poisson, Pound and Vega on world functions and bitensors, and Wang's RNC analysis of small causal diamonds.

No claim is made that the general bitensor identities themselves are new.
