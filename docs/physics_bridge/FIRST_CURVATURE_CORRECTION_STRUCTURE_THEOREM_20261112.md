# Theorem: structure of the first curvature correction to the local recovery coefficient

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** perturbative structural theorem; universal coefficients not yet evaluated  
**Physical status:** identifies the curvature tensors allowed in the first deviation from the Minkowski orientation-recovery constant  
**Literature boundary:** the small-diamond metric expansion is classical; the coefficient functional and its symmetry restriction are project-specific

## 1. Setting

Let

\[
(M^d,g)
\]

be a smooth time-oriented Lorentzian spacetime with fixed

\[
d\ge3.
\]

Fix a strongly causal point

\[
o
\]

and a future-directed unit timelike vector

\[
T.
\]

Define the centered small diamond

\[
D_L
=
I(
\exp_o(-LT),
\exp_o(LT)
).
\]

Let

\[
K_d(L)
=
K_{d,g}(D_L)
\]

be the leading orientation-recovery coefficient from the local curved theorem.

## 2. Claim

There exist dimension-dependent universal constants

\[
A_d,
\qquad
B_d
\]

such that

\[
\boxed{
K_d(L)
=
K_d^{\rm Mink}
+
L^2
\left[
A_d R
+
B_d R_{\mu\nu}T^\mu T^\nu
\right]_o
+
o(L^2).
}
\]

The theorem determines the tensorial form of the first correction.

It does not yet evaluate \(A_d\) or \(B_d\).

## 3. Rescaled normal-coordinate expansion

Use Riemann normal coordinates centered at \(o\) and rescale

\[
x=LX.
\]

After removing the overall constant conformal factor \(L^2\), the dimensionless metric satisfies

\[
\boxed{
\widehat g_{L,\mu\nu}(X)
=
\eta_{\mu\nu}
-
\frac{L^2}{3}
R_{\mu\alpha\nu\beta}(o)
X^\alpha X^\beta
+
O(L^3)
}
\]

in \(C^2\) on fixed compact sets.

Thus

\[
\widehat g_L-\eta
=
O(L^2).
\]

The first metric perturbation is linear in the Riemann tensor at the center.

## 4. Smooth dependence of the coefficient for d >= 4

For

\[
d\ge4,
\]

the recovery coefficient is a compact edge integral built from:

- the edge embedding;
- the induced edge metric;
- the double-null coefficient \(\Omega\);
- null geodesics and Jacobi fields;
- the thin-null Penrose coefficients \(c_\pm\).

All of these solve smooth ODE or implicit-function problems with coefficients depending smoothly on the metric.

On the regular small-diamond family, they therefore depend differentiably on the rescaled metric near \(\eta\).

The optical-gauge-invariant edge integrand is consequently differentiable as a functional of \(\widehat g\).

Hence

\[
\boxed{
K_d(L)
=
K_d^{\rm Mink}
+
L^2
\mathcal L_d[
R_{\mu\alpha\nu\beta}(o)
]
+
o(L^2)
}
\]

for a linear scalar functional \(\mathcal L_d\) of the algebraic curvature tensor.

## 5. Smooth dependence for d = 3

For \(d=3\),

\[
K_3(L)
=
\frac{
2\pi
}{
V_{\widehat g_L}(\widehat D_L)
}
\int_{\widehat D_L}
\kappa_L^{-3}
\,d\widehat\mu_L.
\]

The integrand is singular at the null edge, but the curved dominated-convergence theorem gives the uniform edge bound

\[
\kappa_L^{-3}
\le
C
(ab)^{-3/4}.
\]

The geometric data and their first parameter variations satisfy the same singular order.

Therefore differentiating the coefficient with respect to the metric parameter is permitted under an integrable majorant.

Thus the same expansion holds:

\[
\boxed{
K_3(L)
=
K_3^{\rm Mink}
+
L^2
\mathcal L_3[
R_{\mu\alpha\nu\beta}(o)
]
+
o(L^2).
}
\]

## 6. Isotropy of the flat reference diamond

The unit tangent-space diamond is invariant under the spatial rotation group fixing \(T\):

\[
O(d-1).
\]

The scalar recovery coefficient is also invariant under those rotations.

Therefore the linear functional

\[
\mathcal L_d[Riem]
\]

must be an \(O(d-1)\)-invariant scalar linear in the curvature tensor and depending on the distinguished timelike unit vector \(T\).

## 7. Classification of linear curvature scalars

At linear order in the Riemann tensor, every parity-even scalar constructed from:

- \(g_{\mu\nu}\);
- \(T^\mu\);
- \(R_{\mu\nu\rho\sigma}\);

reduces, using the Riemann symmetries, to a linear combination of

\[
R
\]

and

\[
R_{\mu\nu}T^\mu T^\nu.
\]

A contraction of the Weyl tensor with the metric vanishes.

With only one distinguished vector \(T\), no independent parity-even Weyl scalar exists at linear order.

Therefore

\[
\boxed{
\mathcal L_d[Riem]
=
A_d R
+
B_d R_{\mu\nu}T^\mu T^\nu.
}
\]

This proves the stated form.

## 8. Dimensional consistency

The coefficient

\[
K_d
\]

is dimensionless.

Curvature has dimension

\[
L^{-2}.
\]

Hence the first correction must appear as

\[
L^2R
\]

times a dimensionless number.

The expansion is therefore dimensionally consistent.

## 9. Relation to small causal-diamond geometry

Gibbons and Solodukhin showed that the first curvature correction to standard small causal-diamond geometric observables is of order

\[
L^2
\]

and involves the Ricci scalar and the timelike Ricci projection.

The present theorem does not import their numerical coefficients.

It shows independently, from the orientation-recovery functional and symmetry, that the **same tensorial basis** is forced at first order:

\[
\boxed{
R,
\qquad
R_{TT}.
}
\]

## 10. Vacuum consequence

If the spacetime is Ricci flat at \(o\),

\[
R_{\mu\nu}(o)=0,
\]

then

\[
R(o)=0
\]

and the entire quadratic-size correction vanishes:

\[
\boxed{
K_d(L)
=
K_d^{\rm Mink}
+
o(L^2).
}
\]

Thus Weyl curvature cannot modify the recovery constant linearly at order \(L^2\).

The first vacuum correction must occur at higher order.

## 11. Centered-diamond time-reversal symmetry

The diamond defined by endpoints

\[
\exp_o(\pm LT)
\]

is unchanged when

\[
T\mapsto -T
\]

and the tips are exchanged.

The arrow-erasure recovery coefficient is also unchanged.

Therefore any odd-in-\(T\) local scalar is forbidden.

In particular, possible \(L^3\) terms linear in first curvature derivatives, such as

\[
T^\mu\nabla_\mu R,
\]

change sign under tip exchange and cannot contribute to the centered scalar coefficient.

Under sufficient smoothness, this suggests the stronger expansion

\[
K_d(L)
=
K_d^{\rm Mink}
+
L^2(
A_dR+B_dR_{TT}
)
+
O(L^4),
\]

but the present theorem only claims

\[
o(L^2)
\]

after the displayed \(L^2\) term.

The absence and detailed structure of all cubic terms should receive a separate invariant perturbation audit before an \(O(L^4)\) remainder is asserted.

## 12. Quantitative status after the conformal-response calculation

The coefficients have now been evaluated explicitly for every fixed

\[
d\ge4.
\]

The dedicated theorem

EXPLICIT_FIRST_CURVATURE_RESPONSE_DGE4_20261112.md

gives

\[
\boxed{
A_d
=
-
K_d^{\rm Mink}
\frac{
d(d+6)
}{
4(d-1)(d+1)(d+2)
},
}
\]

and

\[
\boxed{
B_d
=
K_d^{\rm Mink}
\frac{
d^2+2d-4
}{
4(d-1)(d+1)
}.
}
\]

Thus the remaining first-order curvature-response problem is only the bulk-dominated case

\[
d=3.
\]

There one must perturb the intrinsic volume-time integral rather than the null-edge coefficient.

## 13. Explicit 3+1 consequence

For

\[
d=4,
\]

\[
K_4^{\rm Mink}=9\pi,
\]

and the explicit response coefficients are

\[
A_4=-\pi,
\qquad
B_4=3\pi.
\]

Therefore

\[
\boxed{
K_{4,g}(D_L)
=
9\pi
+
\pi L^2
\left(
3R_{TT}-R
\right)_o
+
o(L^2).
}
\]

In Ricci-flat spacetime the complete \(L^2\) correction vanishes.

## 14. Scientific consequence

The local recovery probability now has the perturbative structure

\[
\boxed{
1-p^{\rm UPO}(n)
\sim
\left[
K_d^{\rm Mink}
+
L^2(
A_dR+B_dR_{TT}
)
+\cdots
\right]
n^{2-\beta_d}.
}
\]

Thus the first curvature information visible to the arrow-erasure error rate is necessarily Ricci-type.

At this order, the statistic is insensitive to purely Weyl curvature.
