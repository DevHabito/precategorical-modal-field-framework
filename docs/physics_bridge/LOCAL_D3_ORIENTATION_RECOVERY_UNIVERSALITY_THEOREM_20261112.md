# Theorem: local orientation recovery in every smooth 2+1 Lorentzian spacetime

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** analytic local universality theorem
**Physical status:** removes the need to assume H1--H5 separately for sufficiently small timelike diamonds
**Novelty status:** Riemann normal-coordinate convergence is classical; the project-specific consequence is local asymptotic recovery after causal-arrow erasure

## 1. Statement

Let

\[
(M,g)
\]

be any smooth time-oriented \(2+1\)-dimensional Lorentzian spacetime.

Fix a point

\[
o\in M
\]

and a future-directed unit timelike vector

\[
T\in T_oM.
\]

For sufficiently small \(L>0\), define

\[
p_L
=
\exp_o(-LT),
\]

\[
q_L
=
\exp_o(LT),
\]

and the local Alexandrov interval

\[
D_L
=
I_g(p_L,q_L).
\]

Then there exists

\[
L_0>0
\]

such that, for every fixed

\[
0<L<L_0,
\]

the arrow-erased comparability graph of an iid size-\(n\) physical-volume sprinkling into \(D_L\) satisfies

\[
\boxed{
p_{3,g,L}^{\mathrm{UPO}}(n)
\longrightarrow
1
}
\]

as

\[
n\to\infty.
\]

More sharply,

\[
\boxed{
1-p_{3,g,L}^{\mathrm{UPO}}(n)
\sim
\frac{
\mathcal K_L
}{
n
},
}
\]

where

\[
\mathcal K_L
=
\mathcal K(D_L,g)
\]

is the intrinsic curved volume-time coefficient.

Finally,

\[
\boxed{
\mathcal K_L
\longrightarrow
\frac{32\pi}{3}
}
\]

as

\[
L\downarrow0.
\]

Therefore

\[
\boxed{
\lim_{L\downarrow0}
\lim_{n\to\infty}
n
\left(
1-p_{3,g,L}^{\mathrm{UPO}}(n)
\right)
=
\frac{32\pi}{3}.
}
\]

The order of limits is part of the statement.

## 2. Scaled Riemann normal coordinates

Choose Riemann normal coordinates centered at \(o\), with \(T\) aligned with the coordinate time direction.

For \(X\) in a fixed bounded coordinate neighborhood, define

\[
F_L(X)
=
\exp_o(LX).
\]

Define the rescaled metric

\[
\boxed{
\widehat g_L
=
L^{-2}
F_L^*g.
}
\]

The constant conformal factor \(L^{-2}\) does not change causal structure.

In normal coordinates,

\[
g_{\mu\nu}(LX)
=
\eta_{\mu\nu}
-
\frac13
R_{\mu\alpha\nu\beta}(o)
L^2
X^\alpha X^\beta
+
O(L^3)
\]

on fixed compact \(X\)-sets.

Because \(g\) is smooth,

\[
\boxed{
\widehat g_L
\to
\eta
}
\]

in \(C^4\) on every fixed bounded scaled neighborhood as

\[
L\downarrow0.
\]

## 3. Fixed scaled endpoints

In the chosen normal coordinates,

\[
p_L
\longleftrightarrow
-LT,
\qquad
q_L
\longleftrightarrow
LT.
\]

After the rescaling \(X=x/L\), the endpoints become the fixed points

\[
\widehat p=(-T),
\qquad
\widehat q=(T).
\]

Thus the physical shrinking-diamond problem is converted into a fixed-size causal-diamond problem whose metric converges to Minkowski.

## 4. Exact equivalence of the sprinkling problems

The map \(F_L\) is a diffeomorphism between the scaled diamond

\[
\widehat D_L
=
I_{\widehat g_L}
(\widehat p,\widehat q)
\]

and the physical diamond

\[
D_L.
\]

Because

\[
\widehat g_L
=
L^{-2}F_L^*g,
\]

the map preserves the causal relation.

The volume forms satisfy, in \(2+1\),

\[
d\operatorname{Vol}_{\widehat g_L}
=
L^{-3}
F_L^*
d\operatorname{Vol}_g.
\]

The total diamond volume obeys the same factor.

Therefore the normalized probability measures correspond exactly:

\[
\boxed{
(F_L^{-1})_*
\mu_{g,D_L}
=
\mu_{\widehat g_L,\widehat D_L}.
}
\]

Hence the sampled partial orders and arrow-erased comparability graphs are distributionally identical.

In particular,

\[
\boxed{
p_{3,g,L}^{\mathrm{UPO}}(n)
=
p_{3,\widehat g_L}^{\mathrm{UPO}}(n).
}
\]

## 5. Minkowski reference diamond

At

\[
L=0
\]

in the scaled limit, the reference geometry is the fixed Minkowski diamond

\[
D_0
=
I_\eta(\widehat p,\widehat q).
\]

That diamond satisfies the regular recovery hypotheses H1--H5 with strict margins:

- smooth transverse null joint;
- no cut/conjugate points;
- regular Penrose tubes;
- temporal finite-diamond volume gradient away from the joint;
- integrable inverse-gradient singularity;
- nondegenerate tip gradients;
- regular tip middle bands.

## 6. Apply openness

The recovery-openness theorem gives a \(C^4\) neighborhood of the Minkowski metric in which H1--H5 persist.

Since

\[
\widehat g_L
\to\eta
\]

in \(C^4\), there exists

\[
L_0>0
\]

such that

\[
\widehat g_L
\]

lies in this recovery neighborhood for every

\[
0<L<L_0.
\]

Therefore the regular curved \(2+1\) orientation-recovery rate theorem applies to every sufficiently small physical diamond.

Thus

\[
\boxed{
1-p_{3,g,L}^{\mathrm{UPO}}(n)
\sim
\frac{
\mathcal K_L
}{
n
}.
}
\]

## 7. Scale invariance of the coefficient

The intrinsic coefficient is

\[
\mathcal K(D,g)
=
\frac{
2\pi
}{
V_D
}
\int_D
\left[
-g^{-1}(d\Phi,d\Phi)
\right]^{-3/2}
\,d\mu.
\]

It is invariant under:

1. diffeomorphisms;
2. constant positive rescalings of the metric.

Therefore

\[
\boxed{
\mathcal K(D_L,g)
=
\mathcal K(
\widehat D_L,
\widehat g_L
).
}
\]

## 8. Flat local limit of the coefficient

The openness theorem also gives continuity of the coefficient under regular \(C^4\) metric perturbations.

Hence

\[
\mathcal K(
\widehat D_L,
\widehat g_L
)
\longrightarrow
\mathcal K(
D_0,
\eta
).
\]

The flat coefficient is

\[
\mathcal K(
D_0,
\eta
)
=
\frac{32\pi}{3}.
\]

Therefore

\[
\boxed{
\mathcal K_L
\to
\frac{32\pi}{3}.
}
\]

## 9. Iterated local-universality limit

For every fixed sufficiently small \(L\),

\[
\lim_{n\to\infty}
n
\left(
1-p_{3,g,L}^{\mathrm{UPO}}(n)
\right)
=
\mathcal K_L.
\]

Taking the small-diamond limit afterward gives

\[
\boxed{
\lim_{L\downarrow0}
\lim_{n\to\infty}
n
\left(
1-p_{3,g,L}^{\mathrm{UPO}}(n)
\right)
=
\frac{32\pi}{3}.
}
\]

This is a local universality statement.

## 10. What is universal and what is geometric

For every fixed sufficiently small curved diamond,

\[
1-p_{3,g,L}^{\mathrm{UPO}}(n)
\sim
\frac{
\mathcal K_L
}{
n
}.
\]

Thus the exponent

\[
1
\]

is already universal.

The coefficient

\[
\mathcal K_L
\]

depends on the finite curved diamond.

When the diamond shrinks to a point,

\[
\mathcal K_L
\to
32\pi/3.
\]

So curvature affects the finite-size coefficient, but the tangent-space limit is universal.

## 11. No conformal-flatness assumption

The proof uses only local smoothness of the Lorentzian metric.

In \(2+1\), the Cotton tensor may be nonzero at \(o\).

After rescaling,

\[
\widehat g_L-\eta
=
O(L^2),
\]

regardless of whether the original metric is conformally flat.

Therefore the theorem applies to sufficiently small diamonds in genuinely nonconformally-flat spacetimes.

## 12. Smoothness requirement

The proof uses \(C^4\) metric control because the openness theorem tracks:

- null geodesics;
- Jacobi fields;
- curvature;
- first Penrose-Fermi corrections;
- \(C^2\) volume-function data.

The spacetime is assumed smooth here, so this is automatic.

The minimal regularity required by the theorem has not been optimized.

## 13. What is not claimed

The theorem does not state that an arbitrary large causal diamond satisfies H1--H5.

Large diamonds can contain:

- caustics;
- cut-locus branching;
- nonsmooth joints;
- degenerate volume-time gradients.

It also does not interchange the limits

\[
L\downarrow0
\]

and

\[
n\to\infty.
\]

A joint double-scaling theorem would require estimates uniform in \(L\).

## 14. Scientific consequence

The curved \(2+1\) result is no longer only a theorem about a selected regular class.

Every smooth \(2+1\) Lorentzian spacetime contains a neighborhood basis of sufficiently small timelike Alexandrov intervals for which causal orientation is asymptotically recoverable from symmetric comparability alone, up to global reversal.

The leading local error approaches the universal Minkowski value

\[
\boxed{
32\pi/3.
}
\]
