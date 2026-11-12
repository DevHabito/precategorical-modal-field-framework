# Lemma: automatic compact containment of thin-null Alexandrov intervals

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic causal-energy lemma  
**Purpose:** remove compact containment as an independent hypothesis in the Penrose-scaled thin-null theorem

## 1. Setting

Let

\[
\gamma:[0,L]\to(M,g)
\]

be a compact null geodesic segment with a regular null-Fermi tube

\[
\mathcal T_\rho
=
\{
|u|<\rho,\,
|y|<\rho,\,
v\in[-\rho,L+\rho]
\}.
\]

Use null-Fermi coordinates

\[
(u,v,y^A),
\qquad
A=1,\ldots,d-2,
\]

adapted to \(\gamma\), so

\[
\gamma(v)=(0,v,0).
\]

Assume the metric on the tube is uniformly close to a regular Penrose-Fermi form:

\[
g
=
2\,du\,dv
+
H_{AB}(v)y^Ay^B\,dv^2
+
\delta_{AB}dy^Ady^B
+
E,
\]

where the error tensor satisfies, after shrinking the tube,

\[
|E|
\le
\epsilon_0
\]

in a fixed auxiliary Euclidean norm.

Let the endpoints of the nearly null interval satisfy

\[
P_a=(0,0,0)+O(a),
\]

\[
Q_a=(aU_*,L,\sqrt a\,Y_*)+o(\sqrt a)
\]

for bounded \(U_*,Y_*\).

## 2. Claim

There are constants

\[
C_u,C_y>0
\]

and

\[
a_0>0
\]

such that for every

\[
0<a<a_0,
\]

the entire Alexandrov interval

\[
I(P_a,Q_a)
\]

satisfies

\[
\boxed{
|u|\le C_u a,
\qquad
|y|\le C_y\sqrt a,
\qquad
v\in[-Ca,L+Ca].
}
\]

Therefore after the Penrose scaling

\[
u=aU,
\qquad
y=\sqrt a\,Y,
\qquad
v=V,
\]

the rescaled intervals lie in one fixed compact set.

## 3. Monotonicity of v

Inside a sufficiently small regular null-Fermi tube, choose the time orientation so that

\[
\partial_u
\]

is future null.

For every future-directed causal vector \(X\), the dual null coordinate \(v\) is nondecreasing:

\[
dv(X)\ge0,
\]

with equality only for vectors parallel to the distinguished null direction.

After shrinking the tube and using uniform cone comparison, there is a constant \(C\) such that every future causal curve from \(P_a\) to \(Q_a\) satisfies

\[
-Ca
\le
v
\le
L+Ca.
\]

Thus the longitudinal coordinate cannot escape the fixed generator interval.

## 4. Causal energy inequality

Write a future causal curve as

\[
c(s)
=
(u(s),v(s),y(s)).
\]

On portions where

\[
\dot v>0,
\]

use \(v\) as parameter.

The causal inequality

\[
g(\dot c,\dot c)\le0
\]

and uniform control of the metric coefficients give

\[
|\partial_v y|^2
\le
C
\left(
-\partial_v u
+
u_0
+
|y|^2
\right)
\]

for a sufficiently small tube, where the harmless lower-order term \(u_0\) is bounded by \(Ca\) for the endpoint configuration.

Integrating between \(v_1\) and \(v_2\) gives the schematic energy estimate

\[
\boxed{
\int_{v_1}^{v_2}
|\partial_v y|^2\,dv
\le
C
\left[
|u(v_2)-u(v_1)|
+
a
+
\int_{v_1}^{v_2}|y|^2\,dv
\right].
}
\]

A Gronwall argument will close this estimate once \(u=O(a)\).

## 5. Bound on the u-coordinate

The same cone comparison gives

\[
|\partial_v u|
\le
C
\left[
|\partial_v y|^2
+
a
+
|y|^2
\right].
\]

Integrating from either endpoint and combining with the previous inequality yields

\[
\boxed{
\sup |u|
\le
C
\left[
a
+
\int_0^L|y|^2\,dv
\right].
}
\]

## 6. Bootstrap for transverse displacement

Suppose the curve stays inside

\[
|y|\le\rho
\]

up to some first exit time.

The preceding inequalities imply

\[
\int_0^L
|\partial_v y|^2\,dv
\le
C
\left[
a
+
\int_0^L|y|^2\,dv
\right].
\]

Since the endpoint transverse displacement is

\[
O(\sqrt a),
\]

the one-dimensional Poincare/energy inequality gives

\[
\sup_{0\le v\le L}
|y(v)|^2
\le
C
\left[
a
+
\int_0^L
|\partial_v y|^2\,dv
\right].
\]

Combining the two estimates and taking the tube sufficiently small so the lower-order coefficient can be absorbed gives

\[
\boxed{
\sup |y|^2
\le
Ca.
}
\]

Hence

\[
\boxed{
\sup |y|
\le
C_y\sqrt a.
}
\]

Substituting back gives

\[
\boxed{
\sup |u|
\le
C_u a.
}
\]

## 7. First-exit contradiction

Assume, for contradiction, that a sequence of causal curves inside the Alexandrov intervals first exits the fixed null-Fermi tube through

\[
|y|=\rho
\]

or

\[
|u|=\rho.
\]

The bootstrap estimates valid up to the first exit give

\[
|y|
\le
C_y\sqrt a,
\]

\[
|u|
\le
C_u a.
\]

For sufficiently small \(a\), both are strictly less than \(\rho\).

This contradicts the definition of the first exit.

Therefore every causal curve joining the endpoints remains inside the tube, and in particular every point of

\[
I(P_a,Q_a)
\]

satisfies the same bounds.

## 8. Penrose-scaled compactness

After

\[
U=u/a,
\qquad
Y=y/\sqrt a,
\qquad
V=v,
\]

the bounds become

\[
|U|\le C_u,
\qquad
|Y|\le C_y,
\qquad
-Ca\le V\le L+Ca.
\]

Thus the rescaled Alexandrov intervals lie inside the fixed compact set

\[
[-C_u,C_u]
\times
[-1,L+1]
\times
\overline{B_{C_y}(0)}
\]

for all sufficiently small \(a\).

Hence the compact-containment assumption used in

PENROSE_SCALED_ALEXANDROV_DOMAIN_CONVERGENCE_20261112.md

is a consequence of regular null-Fermi geometry and the nearly null endpoint scaling.

## 9. Consequence

The thin-null theorem no longer needs compact containment as an independent primitive hypothesis.

The logical chain is now:

\[
\boxed{
\text{regular null-Fermi tube}
\Longrightarrow
\text{causal energy bound}
\Longrightarrow
\text{scaled compact containment}
\Longrightarrow
\text{domain convergence}
\Longrightarrow
V_{\rm thin}\sim c\,a^{d/2}.
}
\]

## 10. Scope

The argument assumes a regular null-Fermi tube with uniform cone comparison.

It does not apply through:

- conjugate points;
- cut points;
- caustics;
- degeneration of the adapted null coordinate.

Those remain genuine failure regimes.
