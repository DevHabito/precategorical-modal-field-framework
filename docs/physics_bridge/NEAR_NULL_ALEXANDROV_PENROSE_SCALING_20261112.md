# Penrose-limit reduction for nearly null Alexandrov-interval volumes

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact plane-wave scaling theorem + conditional generic-spacetime transfer  
**Physical status:** geometric mechanism behind long-and-skinny causal-interval volume scaling  
**Novelty status:** Penrose limits and null Fermi coordinates are classical; a targeted search did not locate their use to derive the nearly-null Alexandrov-volume scaling needed by the present arrow-erasure problem

## 1. Motivation

A small Alexandrov volume does not imply that the interval is geometrically local.

An interval can approach a null geodesic while stretching over a finite affine distance.

This is the long-and-skinny regime.

The standard small-diamond expansion in Riemann normal coordinates is not uniform in this limit.

The correct local model is instead the Penrose limit along the limiting null geodesic.

## 2. Penrose coordinates

Let

\[
\gamma
\]

be a regular null geodesic in a smooth \(d\)-dimensional Lorentzian spacetime.

Use null Fermi/Penrose-adapted coordinates

\[
(u,v,x^i),
\qquad
i=1,\ldots,d-2,
\]

with

\[
\gamma
=
\{v=0,\ x^i=0\}.
\]

The Penrose scaling is

\[
u=U,
\qquad
v=\Omega^2V,
\qquad
x^i=\Omega X^i.
\]

Let

\[
\Psi_\Omega(U,V,X)
=
(U,\Omega^2V,\Omega X).
\]

The rescaled metrics are

\[
g_\Omega
=
\Omega^{-2}
\Psi_\Omega^*g.
\]

Under the standard regularity assumptions of the Penrose limit,

\[
g_\Omega
\longrightarrow
g_{\mathrm{PW}}
\]

smoothly on compact subsets, where

\[
g_{\mathrm{PW}}
\]

is the plane-wave metric associated with \(\gamma\).

The plane-wave profile is determined by curvature components along the null geodesic and therefore encodes null geodesic deviation/focusing.

## 3. Exact scaling inside a plane wave

In Brinkmann coordinates, a plane wave has the form

\[
g_{\mathrm{PW}}
=
-2\,du\,dv
+
\delta_{ij}\,dx^i dx^j
+
H_{ij}(u)x^ix^j\,du^2
\]

up to signature convention.

Define

\[
\delta=\Omega^2.
\]

Under

\[
v=\delta V,
\qquad
x^i=\sqrt{\delta}\,X^i,
\]

we have exactly

\[
\boxed{
\Psi_{\sqrt{\delta}}^*
g_{\mathrm{PW}}
=
\delta
\,g_{\mathrm{PW}}.
}
\]

The right-hand side differs only by a positive constant conformal factor.

Therefore the causal relation is unchanged.

## 4. A family of nearly null endpoints

Fix

\[
u_0<u_1.
\]

Let

\[
p=(u_0,0,0),
\]

and define

\[
q_\delta
=
(u_1,\delta,0).
\]

Under the Penrose scaling,

\[
q_\delta
\longmapsto
q_1
=
(u_1,1,0).
\]

Because the pullback metric is a constant conformal rescaling, the causal interval maps exactly:

\[
\boxed{
\Psi_{\sqrt{\delta}}^{-1}
\left(
I_{g_{\mathrm{PW}}}(p,q_\delta)
\right)
=
I_{g_{\mathrm{PW}}}(p,q_1).
}
\]

## 5. Exact plane-wave volume law

The spacetime volume form of a \(d\)-dimensional metric rescales under

\[
g\mapsto\delta g
\]

by

\[
\delta^{d/2}.
\]

Hence

\[
\boxed{
\operatorname{Vol}_{g_{\mathrm{PW}}}
\left(
I(p,q_\delta)
\right)
=
\delta^{d/2}
\operatorname{Vol}_{g_{\mathrm{PW}}}
\left(
I(p,q_1)
\right).
}
\]

Define

\[
C_\gamma(u_0,u_1)
=
\operatorname{Vol}_{g_{\mathrm{PW}}}
\left(
I(
(u_0,0,0),
(u_1,1,0)
)
\right).
\]

Then

\[
\boxed{
V_{\mathrm{PW}}(p,q_\delta)
=
C_\gamma
\delta^{d/2}.
}
\]

This exponent is exact.

The coefficient depends on the Penrose-limit plane wave and therefore on focusing along the original null geodesic.

## 6. Relation to proper-time scaling

In flat spacetime,

\[
\tau(p,q_\delta)^2
\asymp
\delta.
\]

Thus

\[
\delta^{d/2}
\asymp
\tau^d,
\]

recovering the ordinary Minkowski interval-volume law.

The difference is conceptual:

in the long-and-skinny curved regime, the coefficient need not be the flat coefficient.

It can retain information accumulated along the full limiting null geodesic.

## 7. Generic-spacetime transfer

Return to the original metric \(g\).

Let

\[
q_\delta
=
\Psi_{\sqrt{\delta}}(u_1,1,0).
\]

The physical interval volume satisfies

\[
\begin{aligned}
V_g(p,q_\delta)
&=
\delta^{d/2}
V_{g_{\sqrt{\delta}}}
\left(
I_{g_{\sqrt{\delta}}}
(
p,q_1
)
\right).
\end{aligned}
\]

Assume the null tube is regular in the following sense:

1. \(g_{\sqrt{\delta}}\to g_{\mathrm{PW}}\) in \(C^2\) on a common compact tube;
2. the limiting null segment has no conjugate/cut point in the relevant range;
3. the rescaled Alexandrov intervals
   \[
   I_{g_{\sqrt{\delta}}}(p,q_1)
   \]
   remain inside that tube and converge in measure to
   \[
   I_{g_{\mathrm{PW}}}(p,q_1).
   \]

Then volume-form convergence and domain convergence give

\[
\boxed{
\delta^{-d/2}
V_g(p,q_\delta)
\longrightarrow
C_\gamma.
}
\]

Hence

\[
\boxed{
V_g(p,q_\delta)
\sim
C_\gamma
\delta^{d/2}.
}
\]

This is the generic near-null scaling needed by the curved arrow-erasure program.

## 8. Why the no-caustic condition matters

A conjugate point changes the Jacobi-field structure of the null congruence.

The Penrose-limit plane wave records that focusing.

At or beyond a caustic:

- the null boundary may cease to be smooth;
- the endpoint may have multiple null generators;
- the rescaled causal interval need not converge to one regular plane-wave interval;
- the coefficient can become singular or require summing multiple branches.

The regular theorem should therefore be stated before the first null cut/conjugate point.

## 9. Volume-null coordinates

The result immediately explains the volume-null coordinates used in the curved \(2+1\) joint theorem.

For general \(d\),

\[
V_g(p,x_\delta)
\sim
C_\gamma
\delta^{d/2}.
\]

Therefore

\[
\boxed{
V_g(p,x_\delta)^{2/d}
\sim
C_\gamma^{2/d}\delta.
}
\]

Thus

\[
a(x)
=
V_g(p,x)^{2/d}
\]

is asymptotically linear in a regular inward null coordinate.

If \(C_\gamma\) varies smoothly and remains positive along a compact family of joint generators, the volume-null coordinate is transverse to the null boundary.

For \(d=3\),

\[
\boxed{
V_g(p,x_\delta)
\sim
C_\gamma\delta^{3/2},
}
\]

so

\[
V_g(p,x_\delta)^{2/3}
\sim
C_\gamma^{2/3}\delta.
\]

This is exactly the regularity required by

CURVED_D3_REGULAR_JOINT_SUPPRESSION_THEOREM_20261112.md.

## 10. Connection with Jacobi fields and van Vleck

The Penrose-limit profile is determined by the tidal matrix

\[
R_{uiuj}
\]

along the null geodesic.

The same matrix governs the transverse Jacobi equation.

The van Vleck determinant measures focusing of the geodesic flow and is therefore the natural object controlling the coefficient

\[
C_\gamma.
\]

The exponent

\[
d/2
\]

is kinematic and fixed by Penrose scaling.

The coefficient is dynamical/geometric and records focusing.

This separation is useful:

\[
\boxed{
\text{universal exponent}
+
\text{generator-dependent focusing coefficient}.
}
\]

## 11. Relation to long-and-skinny causal intervals

Causal-set literature has explicitly noted that a small-volume Alexandrov interval can be long and skinny, approach a null direction, and fail to be approximately flat even when its volume is far below the curvature scale.

The Penrose-limit reduction explains the appropriate replacement for the naive flat approximation.

The correct zeroth-order geometry of a long-and-skinny interval is a plane wave, not necessarily Minkowski space.

## 12. Literature boundary

Penrose limits are classical.

Null Fermi coordinates and covariant expansions around null geodesics were developed in detail by Blau, Frank, and Weiss, *Classical and Quantum Gravity* 23 (2006), 3993--4010, DOI 10.1088/0264-9381/23/11/020.

Modern treatments emphasize that the Penrose plane-wave profile is the null-geodesic-deviation curvature matrix.

A targeted search did not locate an application deriving the asymptotic volume of nearly null Alexandrov intervals by scaling them to their Penrose-limit causal interval.

This remains limited negative evidence and is not a priority claim.

## 13. Remaining proof obligation

The exact plane-wave scaling is complete.

For a fully unconditional generic-spacetime theorem, the remaining task is to prove the measure convergence of rescaled Alexandrov domains under a clean geometric hypothesis such as:

- smooth null tube;
- no conjugate points;
- no competing null generator;
- compact transverse control.

That is now a sharply isolated Lorentzian-geometry problem.

If established, it supplies the near-null volume law needed to remove the main conditional hypothesis from the curved \(2+1\) joint theorem.
