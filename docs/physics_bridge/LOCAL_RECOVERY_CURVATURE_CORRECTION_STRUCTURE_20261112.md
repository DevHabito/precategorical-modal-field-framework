# Theorem: invariant structure of the first curvature correction to local orientation recovery

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** symmetry/covariance theorem under smooth dependence of the regular recovery coefficient
**Physical status:** constrains the first finite-curvature correction without fitting coefficients

## 1. Setting

Let

\[
(M,g)
\]

be a smooth strongly causal Lorentzian spacetime of fixed dimension

\[
d\ge3.
\]

Fix

\[
o\in M
\]

and a future-directed unit timelike vector

\[
T\in T_oM.
\]

Consider the centered timelike diamonds

\[
D_L
=
I(
\exp_o(-LT),
\exp_o(LT)
)
\]

for sufficiently small \(L\).

Let

\[
K_{d,L}
\]

be the leading arrow-erasure reconstruction-error coefficient:

\[
1-p_{d,g,L}^{\mathrm{UPO}}(n)
\sim
K_{d,L}
n^{-\rho_d},
\]

where

\[
\rho_d
=
\begin{cases}
1, & d=3,\\[4pt]
4/d, & d\ge4.
\end{cases}
\]

Assume the coefficient functional is smoothly differentiable with respect to the regular scaled metric family near Minkowski space.

This smooth dependence follows formally from the regular no-caustic formulas; an independent technical proof of the required Fréchet differentiability should still be reviewed before publication.

## 2. Scaled metric expansion

In Riemann normal coordinates at \(o\),

\[
\widehat g_L
=
L^{-2}F_L^*g
\]

has the expansion

\[
\widehat g_{L,\mu\nu}(X)
=
\eta_{\mu\nu}
-
\frac13
L^2
R_{\mu\alpha\nu\beta}(o)
X^\alpha X^\beta
-
\frac16
L^3
\nabla_\gamma
R_{\mu\alpha\nu\beta}(o)
X^\alpha X^\beta X^\gamma
+
O(L^4).
\]

Thus the first possible perturbation of the dimensionless recovery coefficient is linear in curvature and of order \(L^2\).

## 3. Stabilizer symmetry of the reference diamond

The reference Minkowski diamond has endpoints

\[
-T,
\qquad
T.
\]

Its spatial stabilizer is

\[
O(d-1),
\]

acting on the hyperplane orthogonal to \(T\).

The recovery coefficient is a scalar invariant of the diamond.

Therefore the linear functional of the curvature appearing at order \(L^2\) must be an \(O(d-1)\)-invariant scalar constructed from:

- the Riemann tensor at \(o\);
- the metric;
- the distinguished timelike vector \(T\).

## 4. Classification of linear curvature scalars

At linear order in curvature, every such scalar reduces to a linear combination of

\[
R
\]

and

\[
R_{TT}
=
R_{\mu\nu}T^\mu T^\nu.
\]

Indeed, contractions of the Riemann tensor with the spatial projector

\[
P^{\mu\nu}
=
g^{\mu\nu}
+
T^\mu T^\nu
\]

reduce to the Ricci and scalar curvature contractions.

No additional independent scalar exists at this order.

Hence there are dimension-dependent constants

\[
A_d,
\qquad
B_d
\]

such that

\[
\boxed{
K_{d,L}
=
K_d^{\mathrm{flat}}
+
L^2
\left[
A_dR(o)
+
B_dR_{\mu\nu}(o)T^\mu T^\nu
\right]
+
o(L^2).
}
\]

## 5. Why the Weyl tensor cannot enter linearly

For

\[
d\ge4,
\]

decompose the Riemann tensor into Weyl plus Ricci pieces.

The only natural contraction of the Weyl tensor with the preferred timelike vector at linear order is its electric part

\[
E_{\mu\nu}
=
C_{\mu\alpha\nu\beta}
T^\alpha T^\beta.
\]

This is spatial and trace-free:

\[
P^{\mu\nu}E_{\mu\nu}=0.
\]

The reference diamond has no preferred spatial direction.

An \(O(d-1)\)-invariant linear scalar would require tracing \(E_{\mu\nu}\) with the spatial metric, which vanishes.

Therefore

\[
\boxed{
\text{there is no linear Weyl contribution at order }L^2.
}
\]

Weyl curvature can affect the coefficient only through higher-order invariants or through nonlinear finite-diamond effects.

## 6. d = 3 interpretation

In \(2+1\),

\[
C_{\mu\nu\rho\sigma}=0
\]

identically.

The full Riemann tensor is determined by the Ricci tensor.

The same invariant classification therefore gives only

\[
R
\]

and

\[
R_{TT}
\]

at order \(L^2\).

Nonconformal information in three dimensions is carried by the Cotton tensor, which contains derivatives of curvature and cannot enter at order \(L^2\).

## 7. Centered-diamond time reversal

The unordered geometric diamond defined by endpoints

\[
-T,
\qquad
T
\]

is unchanged under

\[
T\mapsto -T.
\]

Therefore the coefficient satisfies

\[
K_{d,L}(T)
=
K_{d,L}(-T).
\]

Any term in the local covariant expansion that is odd under \(T\mapsto -T\) must vanish.

## 8. Absence of a cubic derivative term

The \(L^3\) metric perturbation is linear in

\[
\nabla Riem.
\]

Any \(O(d-1)\)-invariant scalar linear in one derivative of curvature necessarily uses an odd number of \(T\) factors, for example

\[
\nabla_T R,
\]

or

\[
\nabla_T R_{TT}.
\]

These change sign under

\[
T\mapsto -T.
\]

Spatial derivatives cannot produce an \(O(d-1)\)-invariant scalar without an additional preferred spatial vector.

Therefore the centered-diamond symmetry forces the complete linear derivative-curvature contribution to vanish.

Under a smooth local expansion,

\[
\boxed{
K_{d,L}
=
K_d^{\mathrm{flat}}
+
L^2
\left[
A_dR
+
B_dR_{TT}
\right]
+
O(L^4).
}
\]

## 9. First genuinely anisotropic curvature effects

For

\[
d\ge4,
\]

the first scalar terms involving Weyl curvature can occur quadratically, for example through invariants built from

\[
E_{\mu\nu}E^{\mu\nu},
\]

or through second derivatives combined with the reference symmetry.

These naturally occur at order

\[
L^4.
\]

In \(2+1\), Cotton-dependent scalar effects likewise require higher order than \(L^2\).

Thus the first finite-curvature correction is Ricci-controlled even in a nonconformally-flat spacetime.

## 10. Relation to small causal-diamond volume expansions

Small causal-diamond volume itself has the known structure

\[
V_D
=
V_{\mathrm{flat}}
\left[
1
+
L^2(
a_dR+b_dR_{TT}
)
+
\cdots
\right].
\]

The present theorem shows that the **orientation-recovery error coefficient** has the same invariant basis at first curvature order, although its numerical constants

\[
A_d,
\qquad
B_d
\]

are different observables and are not inferred from the volume coefficients.

## 11. What is not yet known

This theorem determines the allowed form of the first correction, not its coefficients.

The current open calculation is

\[
\boxed{
A_d,\ B_d\;?
}
\]

They must be derived from the recovery functional itself.

Two independent curved reference families would be sufficient to determine them in each dimension.

No fitted or guessed values are recorded here.

## 12. Research consequence

The local recovery law has a hierarchy:

\[
\boxed{
\text{flat universal term}
\to
\text{Ricci-controlled }L^2\text{ correction}
\to
\text{anisotropic/Weyl or Cotton effects at higher order}.
}
\]

This gives a concrete route from the probabilistic reconstruction theorem to local curvature information.
