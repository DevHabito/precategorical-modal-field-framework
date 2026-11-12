# Theorem: suppression of a regular curved null-joint contribution in 2+1

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** conditional analytic theorem under explicit regular-joint hypotheses  
**Physical status:** curved-spacetime boundary control for the \(2+1\) small-disagreement statistic  
**Novelty status:** double-null coordinates and null focusing are established Lorentzian geometry; the volume-null coordinate reduction and its use in the arrow-erasure disagreement tail are project-specific

## 1. Purpose

In \(2+1\) flat Minkowski spacetime,

\[
F_3(\varepsilon)
\sim
C_{\mathrm{bulk}}\varepsilon^3,
\]

while the genuinely joint-scaled core is higher order.

To transfer the bulk coefficient to a curved Alexandrov interval, one must show that the neighborhood of the intersection of the future and past null boundaries does not contribute an additional order-\(\varepsilon^3\) coefficient.

This note proves that statement under a regular double-null edge package.

## 2. Geometric setting

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval in a smooth \(2+1\)-dimensional Lorentzian spacetime.

Let

\[
\Sigma
=
\partial I^+(p)
\cap
\partial I^-(q)
\]

be the codimension-two joint.

Assume:

1. \(\Sigma\) is a compact smooth spacelike one-manifold;
2. the two null boundaries are smooth near \(\Sigma\);
3. they intersect transversely;
4. the relevant null generators contain no conjugate or cut points in the chosen joint neighborhood.

These assumptions are the standard regularity conditions under which a local double-null description is available.

## 3. Normalized causal volumes

Use normalized spacetime volume

\[
\mathcal V(a,b)
=
\frac{
\operatorname{Vol}_g(I(a,b))
}{
\operatorname{Vol}_g(D)
}.
\]

Near the joint define the **volume-null coordinates**

\[
\boxed{
a(x)
=
\mathcal V(p,x)^{2/3},
}
\]

and

\[
\boxed{
b(x)
=
\mathcal V(x,q)^{2/3}.
}
\]

Assume that, together with a coordinate

\[
\sigma
\]

along \(\Sigma\), these give a \(C^1\) coordinate system

\[
(a,b,\sigma)
\]

on a joint neighborhood

\[
U_\eta
=
\{0\le a,b<\eta\},
\]

with volume density bounded above and below:

\[
0<c_J
\le
J(a,b,\sigma)
\le
C_J<\infty.
\]

This is the first regular-joint hypothesis to be verified from null focusing geometry in a fully unconditional curved theorem.

## 4. Ordered comparable pair coordinates

For

\[
x\prec y
\]

inside the joint chart write

\[
a_x=\alpha,
\qquad
a_y=\alpha+A,
\]

and

\[
b_y=\beta,
\qquad
b_x=\beta+B,
\]

with

\[
A,B\ge0.
\]

Let

\[
\sigma_x=\sigma,
\qquad
\sigma_y=\sigma+\zeta.
\]

Assume the double-null metric is uniformly regular in the chart so that causal comparability implies the cap bound

\[
\boxed{
|\zeta|
\le
C_{\mathrm{cap}}
\sqrt{AB}.
}
\]

This is the \(2+1\) analogue of the flat angular-cap factor.

It follows from smooth double-null geometry if the two null directions remain uniformly transverse and the induced metric along \(\Sigma\) is nondegenerate.

## 5. Exact endpoint-volume increments

By definition of the volume-null coordinates,

\[
\mathcal V(p,x)
=
\alpha^{3/2},
\]

\[
\mathcal V(p,y)
=
(\alpha+A)^{3/2},
\]

\[
\mathcal V(y,q)
=
\beta^{3/2},
\]

and

\[
\mathcal V(x,q)
=
(\beta+B)^{3/2}.
\]

Therefore the exact curved disagreement identity becomes

\[
\boxed{
\Delta_g(x,y)
=
g(\alpha,A)
+
g(\beta,B)
-
2\mathcal V(x,y),
}
\]

where

\[
g(u,v)
=
(u+v)^{3/2}
-
u^{3/2}.
\]

This is why volume-null coordinates are useful: all tangential variation of the endpoint-volume coefficients has been absorbed into the coordinates themselves.

## 6. Small interval bound

Assume the regular double-null chart also satisfies

\[
\boxed{
\mathcal V(x,y)
\le
C_I(AB)^{3/2}
}
\]

for sufficiently close comparable pairs in the joint neighborhood.

This is the natural \(2+1\) local Alexandrov-volume estimate because the squared proper-time scale of a small comparable displacement is bounded by a constant multiple of \(AB\).

Since

\[
A,B<\eta
\]

inside a sufficiently small joint chart,

\[
(AB)^{3/2}
\le
\eta^{3/2}
\min(
A^{3/2},
B^{3/2}
).
\]

Also

\[
g(\alpha,A)
\ge
A^{3/2},
\]

and

\[
g(\beta,B)
\ge
B^{3/2}.
\]

Choose \(\eta\) sufficiently small that

\[
2C_I\eta^{3/2}
\le
\frac12.
\]

Then

\[
2\mathcal V(x,y)
\le
\frac12
\left[
g(\alpha,A)
+
g(\beta,B)
\right].
\]

Hence

\[
\boxed{
\Delta_g(x,y)
\ge
\frac12
\left[
g(\alpha,A)
+
g(\beta,B)
\right].
}
\]

The reverse upper bound is immediate from positivity of the interval term:

\[
\Delta_g(x,y)
\le
g(\alpha,A)
+
g(\beta,B).
\]

Thus the curved joint disagreement is equivalent, up to constants, to the same two one-side increments that govern the flat problem.

## 7. Pair-measure bound

The spacetime volume density is uniformly bounded.

For each fixed

\[
\alpha,\beta,A,B,\sigma,
\]

the admissible tangential displacement \(\zeta\) has length at most

\[
C\sqrt{AB}.
\]

Therefore the ordered comparable-pair measure in the joint chart is bounded by

\[
\boxed{
C
(AB)^{1/2}
\,d\alpha\,d\beta\,dA\,dB\,d\sigma.
}
\]

After integrating over the compact joint coordinate \(\sigma\), the relevant scalar measure factor is

\[
A^{1/2}B^{1/2}
\,d\alpha\,dA\,d\beta\,dB.
\]

## 8. Truncated one-side integral

Define

\[
J_\eta(s)
=
\int_0^\eta
\int_0^\infty
A^{1/2}
\mathbf1_{
\{g(\alpha,A)\le s\}
}
\,dA\,d\alpha.
\]

Split at

\[
\alpha=s^{2/3}.
\]

### Inner joint core

For

\[
0\le\alpha\le s^{2/3},
\]

the constraint gives

\[
A=O(s^{2/3}).
\]

Thus

\[
J_\eta^{\mathrm{inner}}(s)
=
O(s^{5/3}).
\]

### Matching region

For

\[
\alpha\ge s^{2/3},
\]

the mean-value theorem gives

\[
g(\alpha,A)
\ge
c\alpha^{1/2}A
\]

through the relevant range.

Hence

\[
A
\le
Cs\alpha^{-1/2}.
\]

Therefore

\[
\begin{aligned}
J_\eta^{\mathrm{match}}(s)
&\le
C
s^{3/2}
\int_{s^{2/3}}^\eta
\alpha^{-3/4}
\,d\alpha\\
&\le
C
s^{3/2}
\eta^{1/4}.
\end{aligned}
\]

Combining the two sectors,

\[
\boxed{
J_\eta(s)
\le
C
\left(
s^{3/2}\eta^{1/4}
+
s^{5/3}
\right).
}
\]

## 9. Joint-pair tail

Let

\[
F_3^{\mathrm{joint}}(
\varepsilon;\eta
)
\]

be the probability contribution from comparable pairs lying in the joint chart

\[
U_\eta.
\]

The disagreement lower bound implies

\[
g(\alpha,A)
+
g(\beta,B)
\le
C\varepsilon.
\]

Dropping the sum constraint to two separate constraints only enlarges the integration domain.

Hence

\[
F_3^{\mathrm{joint}}(
\varepsilon;\eta
)
\le
C
J_\eta(C\varepsilon)^2.
\]

Using the preceding estimate,

\[
\boxed{
F_3^{\mathrm{joint}}(
\varepsilon;\eta
)
\le
C
\left[
\eta^{1/2}\varepsilon^3
+
\eta^{1/4}\varepsilon^{19/6}
+
\varepsilon^{10/3}
\right].
}
\]

Therefore, for every fixed sufficiently small \(\eta\),

\[
\limsup_{\varepsilon\downarrow0}
\frac{
F_3^{\mathrm{joint}}(
\varepsilon;\eta
)
}{
\varepsilon^3
}
\le
C\eta^{1/2}.
\]

Letting

\[
\eta\downarrow0
\]

gives

\[
\boxed{
\lim_{\eta\downarrow0}
\limsup_{\varepsilon\downarrow0}
\frac{
F_3^{\mathrm{joint}}(
\varepsilon;\eta
)
}{
\varepsilon^3
}
=
0.
}
\]

Thus a regular curved null joint contributes no independent leading \(\varepsilon^3\) coefficient.

## 10. Combination with the bulk volume-time theorem

Away from the joint, assume the finite-diamond volume function

\[
\Phi(x)
=
\mathcal V(p,x)
-
\mathcal V(x,q)
\]

is \(C^2\) and has timelike differential

\[
d\Phi.
\]

Define

\[
\kappa(x)
=
\sqrt{
-g^{-1}(d\Phi,d\Phi)
}.
\]

The bulk theorem gives

\[
F_3^{\mathrm{bulk}}(\varepsilon)
\sim
C_3^{\mathrm{bulk}}
\varepsilon^3,
\]

with

\[
\boxed{
C_3^{\mathrm{bulk}}
=
\frac{
2\pi
}{
3V_D
}
\int_D
\kappa(x)^{-3}
\,d\mu(x),
}
\]

provided the integral is finite and the compact-exhaustion Taylor estimate is dominated.

The regular-joint theorem above shows that the null-joint neighborhood does not add a separate leading coefficient.

Therefore, under the combined hypotheses,

\[
\boxed{
F_3(\varepsilon)
\sim
C_3^{\mathrm{bulk}}
\varepsilon^3.
}
\]

## 11. What is proved and what remains conditional

The analytic integration from Sections 5--9 is proved from the stated regular-joint assumptions.

What remains to obtain an unconditional generic-curved theorem is to derive those assumptions from standard geometric hypotheses such as:

- smooth transverse null boundaries;
- absence of null conjugate points;
- controlled null expansion;
- bounded van Vleck/Jacobi determinant.

In particular, one must prove that the volume-null coordinates

\[
a=\mathcal V(p,\cdot)^{2/3},
\qquad
b=\mathcal V(\cdot,q)^{2/3}
\]

are regular coordinates near the joint and that the causal cap satisfies

\[
|\zeta|
\le
C\sqrt{AB}.
\]

These are now precise Lorentzian-geometry targets.

## 12. Literature connection

Double-null coordinate systems adapted to two transversely intersecting null hypersurfaces are standard in the characteristic initial-value formulation of general relativity.

The van Vleck determinant and Jacobi fields control the focusing of geodesic congruences and are natural tools for proving regularity of the volume-null coordinates.

The present theorem does not claim those geometric technologies as new.

The project-specific contribution is the observation that, once expressed in volume-null coordinates, the curved arrow-erasure disagreement reduces to the same one-side \(3/2\)-power integral that controls the flat \(2+1\) joint.

## 13. Current frontier

The generic curved \(2+1\) problem has now been reduced to a clean geometric lemma:

> Under smooth transverse null-boundary intersection with no conjugate points, prove that the volume-null coordinate map is regular and that the local causal cap has width \(O(\sqrt{AB})\).

If this lemma follows from standard Jacobi-field estimates, then the leading curved \(2+1\) small-disagreement coefficient is entirely the bulk volume-time integral.
