# Audit: local all-dimensional orientation-recovery universality

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** adversarial local-scaling and causality audit
**Target:** LOCAL_ALLD_ORIENTATION_RECOVERY_UNIVERSALITY_THEOREM_20261112.md

## 1. Correct scope

The theorem must not be stated for an arbitrary point of an arbitrary time-oriented Lorentzian manifold.

The normal-coordinate argument is local, while the chronological relation is global.

At a point where strong causality fails, a causal curve may leave a small normal neighborhood and return, creating global comparabilities that are not represented by the local tangent-space geometry.

The theorem has therefore been corrected to require a relatively compact causally convex normal neighborhood.

This is guaranteed at every point of a strongly causal spacetime.

In particular, it holds in every globally hyperbolic spacetime.

## 2. Rescaled metric

Let

\[
F_L(X)=\exp_o(LX).
\]

The rescaled metric is

\[
\widehat g_L=L^{-2}F_L^*g.
\]

In Riemann normal coordinates,

\[
\widehat g_{L,\mu\nu}(X)
=
g_{\mu\nu}(LX).
\]

The normal-coordinate expansion gives

\[
g_{\mu\nu}(LX)
=
\eta_{\mu\nu}
-
\frac13
R_{\mu\alpha\nu\beta}(o)
L^2X^\alpha X^\beta
+
O(L^3).
\]

For a smooth metric, derivatives with respect to \(X\) bring compensating powers of \(L\).

Thus on each fixed compact scaled set,

\[
\boxed{
\|\widehat g_L-\eta\|_{C^4}\to0.
}
\]

The \(C^4\) topology required by the openness theorem is therefore available.

## 3. Endpoints are exactly fixed after scaling

Because the coordinates are defined through the exponential map at \(o\),

\[
p_L=\exp_o(-LT)
\]

has normal coordinate

\[
-LT,
\]

and

\[
q_L=\exp_o(LT)
\]

has normal coordinate

\[
LT.
\]

After \(X=x/L\), the endpoints are exactly

\[
-T,
\qquad
T.
\]

There is no endpoint \(O(L^2)\) correction.

## 4. Causal relation under rescaling

The pullback by \(F_L\) is a diffeomorphism.

Multiplying a Lorentzian metric by a positive constant does not change its causal cones.

Therefore

\[
x\ll_g y
\]

in the physical small diamond if and only if

\[
F_L^{-1}(x)
\ll_{\widehat g_L}
F_L^{-1}(y)
\]

in the scaled diamond.

The arrow-erased comparability graphs are exactly isomorphic under the map.

## 5. Normalized volume measure

In spacetime dimension \(d\),

\[
d\operatorname{Vol}_{\widehat g_L}
=
L^{-d}
F_L^*
d\operatorname{Vol}_g.
\]

The same factor multiplies the total diamond volume.

Hence normalized probability measures satisfy exactly

\[
(F_L^{-1})_*
\mu_{g,D_L}
=
\mu_{\widehat g_L,\widehat D_L}.
\]

Thus the iid sprinkling processes are distributionally identical after scaling.

No approximation is made in the probability measure.

## 6. Causal convexity closes the global/local gap

Let \(U\) be the chosen relatively compact causally convex normal neighborhood of \(o\).

For sufficiently small \(L\),

\[
p_L,q_L\in U
\]

and the local normal-coordinate diamond lies inside \(U\).

Because \(U\) is causally convex, every causal curve with endpoints in \(U\) remains in \(U\).

Therefore the global chronological interval

\[
I_M(p_L,q_L)
\]

coincides with the interval computed in the local metric neighborhood.

This justifies replacing the physical problem by the scaled local problem.

## 7. Apply openness only after fixing the scaled domain

The scaled metrics converge on a fixed neighborhood containing the closure of the reference Minkowski diamond.

The recovery-openness theorem supplies a metric neighborhood in which:

- the joint remains regular;
- Penrose tubes remain noncaustic;
- volume-null coordinates remain regular;
- tip and bulk temporal gradients remain nondegenerate;
- the error coefficient remains continuous.

Because

\[
\widehat g_L\to\eta,
\]

all sufficiently small \(L\) enter that neighborhood.

No assumption of globally small curvature is needed.

## 8. Metric-scale invariance of the coefficient

The physical and scaled metrics differ by a diffeomorphism and a constant positive metric factor.

The leading coefficients are invariant under both operations.

Therefore

\[
K(D_L,g)
=
K(
\widehat D_L,
\widehat g_L
).
\]

This equality is exact.

## 9. Continuity of the coefficient

The all-dimensional openness theorem gives continuity of the leading coefficient inside the regular class.

Hence

\[
K(
\widehat D_L,
\widehat g_L
)
\to
K(
D_{\mathrm{flat}},
\eta
).
\]

No pointwise convergence of an unbounded joint integrand is used without a common domination argument; that domination is part of the regular volume-null perturbation theorem.

## 10. Order of limits

The theorem states

\[
\lim_{L\downarrow0}
\lim_{n\to\infty}
n^{\rho_d}
\left(
1-p_{d,g,L}^{\mathrm{UPO}}(n)
\right)
=
K_d^{\mathrm{flat}}.
\]

This is an iterated limit.

The proof does not establish

\[
\lim_{L\downarrow0}
n(L)^{\rho_d}
\left(
1-p_{d,g,L}^{\mathrm{UPO}}(n(L))
\right)
\]

for arbitrary joint scalings \(n(L)\to\infty\).

In particular, it does not assume that the rare-event scale \(1/n\) remains larger than curvature corrections.

The fixed-\(L\) curved theorem is applied first.

This avoids the additive-curvature-error problem identified earlier in the project.

## 11. Dimension dependence

The local error exponent is

\[
\rho_d
=
\begin{cases}
1, & d=3,\\[4pt]
4/d, & d\ge4.
\end{cases}
\]

The tangent-space coefficients are:

\[
K_3^{\mathrm{flat}}
=
32\pi/3,
\]

and for \(d\ge4\),

\[
K_d^{\mathrm{flat}}
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
\left(
1+\frac2d
\right)
L_{d/2}
\Gamma\left(
1+\frac2d
\right)
\right]^2.
\]

The \(d=4\) value is

\[
9\pi.
\]

## 12. Curvature does not need to vanish

In normal coordinates,

\[
\widehat g_L-\eta
=
O(L^2).
\]

This is true whether or not:

- the \(2+1\) Cotton tensor vanishes;
- the \(d\ge4\) Weyl tensor vanishes.

Thus the local theorem genuinely includes nonconformal curvature.

The explicit nonzero-Cotton example in the repository is a concrete check of this point in \(2+1\).

## 13. Remaining external-review risk

The local scaling step itself is standard and survives the present audit.

The nonclassical risk remains concentrated in the regular-curved theorem it invokes:

- volume-null joint regularity;
- curved small-edge asymptotics;
- tip middle-band shape derivatives.

The local theorem does not introduce a new independent geometric assumption beyond causal convexity.

## 14. Audit verdict

After adding the causally convex/strong-causality hypothesis, no local/global causality mismatch remains.

The normalized sprinkling law, causal relation, and leading coefficient are exactly transported by the scaling map.

The local-universality theorem survives the present internal audit at the corrected scope.
