# Theorem: universal thin-null Alexandrov-volume exponent from Penrose-Fermi scaling

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic local asymptotic theorem under a regular null-tube hypothesis  
**Physical status:** curved-spacetime replacement for the flat null-face law \(V\sim a^{d/2}\)  
**Novelty status:** null Fermi coordinates and Penrose limits are established; the project-specific use is the asymptotic volume of nearly null Alexandrov intervals required by arrow-erasure reconstruction

## 1. Problem

Let

\[
(M^d,g)
\]

be a smooth Lorentzian spacetime.

Fix a future-directed null geodesic segment

\[
\gamma:[0,L]\to M
\]

from

\[
p=\gamma(0)
\]

to

\[
r=\gamma(L).
\]

Assume the segment lies in a regular null tube:

1. there are no conjugate points to \(p\) along \(\gamma|_{(0,L]}\);
2. the null exponential map is nonsingular on a tubular neighborhood of the segment;
3. null Fermi coordinates exist uniformly on the compact segment.

Let \(x_a\) be a smooth one-parameter family of timelike points approaching \(r\) from the interior side of the future null cone of \(p\), with transverse optical depth \(a>0\) and

\[
a\downarrow0.
\]

Then the Alexandrov interval

\[
I(p,x_a)
\]

is long and thin: its volume tends to zero although its endpoints need not become close in ordinary coordinates.

The theorem below determines the universal power of that volume.

## 2. Null Fermi coordinates

Choose null Fermi coordinates

\[
(v,u,y^A),
\qquad
A=1,\ldots,d-2,
\]

adapted to \(\gamma\), so that

\[
\gamma(v)
=
(v,0,0)
\]

and the metric admits the Penrose-Fermi expansion around the null geodesic.

The leading scaled metric is the Penrose plane-wave metric

\[
g_{\mathrm{PW}}
=
2\,dU\,dV
+
\delta_{AB}\,dY^A dY^B
+
H_{AB}(V)Y^A Y^B\,dV^2,
\]

where the profile \(H_{AB}\) is determined by curvature components along \(\gamma\).

The exact numerical sign conventions are irrelevant for the volume exponent.

## 3. Anisotropic near-null scaling

The correct blow-up of a nearly null interval is

\[
\boxed{
u=aU,
\qquad
y^A=\sqrt a\,Y^A,
\qquad
v=V.
}
\]

Under this scaling,

\[
du
=
a\,dU,
\]

and

\[
d^{d-2}y
=
a^{(d-2)/2}
d^{d-2}Y.
\]

Therefore the coordinate Jacobian is

\[
\boxed{
du\,dv\,d^{d-2}y
=
a^{d/2}
dU\,dV\,d^{d-2}Y.
}
\]

This already identifies the candidate universal exponent \(d/2\).

## 4. Penrose-Fermi metric scaling

The Penrose-Fermi expansion implies that after the anisotropic coordinate blow-up and removal of the common overall factor \(a\), the metric converges on compact scaled sets to the Penrose plane-wave metric:

\[
\boxed{
a^{-1}
g
\longrightarrow
g_{\mathrm{PW}}
}
\]

in the scaled coordinate representation, with higher-order corrections vanishing as \(a\to0\).

Equivalently, the local causal inequalities defining the long-thin Alexandrov interval converge to those of a finite causal domain in the plane-wave limit.

The limiting domain depends on:

- the null geodesic segment;
- the Penrose profile \(H_{AB}(V)\);
- the way \(x_a\) approaches the null cone.

It does not collapse under the regular-tube hypotheses.

## 5. Volume-form scaling

The physical volume form has the local form

\[
d\operatorname{Vol}_g
=
J(v,u,y)\,
du\,dv\,d^{d-2}y,
\]

where \(J\) is smooth and positive in the regular tube.

After the blow-up,

\[
J(V,aU,\sqrt a\,Y)
\to
J(V,0,0)
\]

uniformly on compact scaled sets.

Therefore

\[
d\operatorname{Vol}_g
=
a^{d/2}
\left[
J(V,0,0)+o(1)
\right]
dU\,dV\,d^{d-2}Y.
\]

## 6. Limiting scaled interval

Let

\[
\widehat I_a
\]

be the image of \(I(p,x_a)\) under the anisotropic blow-up.

Under the regular null-tube and nonconjugacy assumptions,

\[
\widehat I_a
\]

converges, in the local measure sense required for volume asymptotics, to a finite nondegenerate domain

\[
I_{\mathrm{PW}}
\]

in the Penrose plane-wave geometry.

Define

\[
\mathcal C_\gamma
=
\int_{I_{\mathrm{PW}}}
J(V,0,0)\,
dU\,dV\,d^{d-2}Y.
\]

The regularity assumptions imply

\[
0<
\mathcal C_\gamma
<
\infty.
\]

## 7. Universal thin-null exponent

Combining the coordinate Jacobian, volume-form convergence, and limiting domain gives

\[
\boxed{
\operatorname{Vol}_g(I(p,x_a))
=
\mathcal C_\gamma\,
a^{d/2}
\left[
1+o(1)
\right].
}
\]

Thus

\[
\boxed{
\operatorname{Vol}_g(I(p,x_a))
\asymp
a^{d/2}.
}
\]

The exponent is universal.

The coefficient is not universal: it records the Penrose-limit geometry along the null generator.

## 8. Flat-space check

In Minkowski spacetime,

\[
H_{AB}=0,
\]

so the limiting plane wave is flat.

The coefficient reduces to the ordinary flat null-face coefficient.

The theorem therefore reproduces

\[
V_{\mathrm{flat}}
\propto
a^{d/2}.
\]

For \(d=3\),

\[
V
\propto
a^{3/2}.
\]

For \(d=4\),

\[
V
\propto
a^2.
\]

## 9. Why small volume does not imply local flatness

A nearly null Alexandrov interval can have arbitrarily small volume while extending along a finite null-geodesic segment.

Therefore the ordinary small-diamond expansion based on two coalescing timelike endpoints is not the correct approximation.

The correct tangent object is the Penrose plane-wave limit of the null geodesic.

This resolves the "long and skinny interval" obstruction at the exponent level:

\[
\boxed{
\text{small thin-null volume}
\not\Rightarrow
\text{Minkowski coefficient},
}
\]

but

\[
\boxed{
\text{regular null tube}
\Rightarrow
\text{universal }a^{d/2}\text{ exponent}.
}
\]

## 10. Role of conjugate points

The nonconjugacy assumption is structural.

At a conjugate point, the transverse null exponential map degenerates.

Then:

- the limiting scaled domain can develop caustic degeneracies;
- the coefficient \(\mathcal C_\gamma\) can fail to remain regular;
- the naive \(a^{d/2}\) law may require modification.

Thus caustics are not a technical nuisance.

They are a genuine candidate mechanism by which curved-spacetime arrow-erasure statistics could differ from the regular Minkowski-type universality class.

## 11. Consequence for curved null-face degree tails

In a regular curved Alexandrov diamond, let \(a\) and \(b\) measure inward optical depth from the two null boundary sheets meeting at a smooth edge.

The theorem gives, along each regular null family,

\[
V(p,x)
=
c_+(s)\,
a^{d/2}
[1+o(1)],
\]

and

\[
V(x,q)
=
c_-(s)\,
b^{d/2}
[1+o(1)],
\]

where \(s\) parametrizes the codimension-two edge and

\[
c_\pm(s)>0
\]

are smooth local coefficients determined by the corresponding Penrose limits.

Therefore the causal-comparability degree has the curved local form

\[
\boxed{
Q_g(x)
\sim
c_+(s)a^{d/2}
+
c_-(s)b^{d/2}.
}
\]

The flat exponent survives.

Only the coefficients change.

## 12. Immediate d = 3 consequence

In \(2+1\),

\[
Q_g
\sim
c_+(s)a^{3/2}
+
c_-(s)b^{3/2}.
\]

Hence the low-degree edge layer still has volume exponent

\[
\boxed{
g_3(q)
\asymp
q^{4/3}
}
\]

under a smooth transverse joint with regular null generators.

This is precisely the exponent required by the flat component and near-whole arguments.

## 13. Literature connection

Blau, Frank, and Weiss developed null Fermi coordinates and a covariant Penrose-Fermi expansion of the metric around an arbitrary null geodesic.

The leading scaled geometry is the Penrose plane-wave limit, while higher corrections are controlled by curvature and its derivatives.

The present theorem uses that established expansion for a different observable:

\[
\operatorname{Vol}(I(p,x_a))
\]

as a timelike endpoint approaches a null-related endpoint along a fixed null generator.

The exponent \(d/2\) is the project-specific consequence relevant to causal-neighborhood disagreement.

## 14. What remains to prove for the full curved recovery theorem

This theorem settles one major issue:

\[
\boxed{
\text{null-face endpoint volumes retain their flat powers.}
}
\]

It does not yet by itself establish the full curved small-disagreement pair tail.

The next required ingredients are:

1. a curved pair-cap scaling law near a smooth transverse null joint;
2. matched asymptotics between the bulk volume-time gradient and the joint transition;
3. quantitative control uniform along the entire compact edge;
4. treatment or exclusion of caustics and conjugate points.

For \(2+1\), these ingredients now look tractable because the endpoint-volume exponent is fixed at \(3/2\).
