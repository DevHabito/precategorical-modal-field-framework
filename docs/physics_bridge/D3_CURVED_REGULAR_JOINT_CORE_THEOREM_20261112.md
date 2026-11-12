# Theorem: regular curved 2+1 null-joint core is subleading

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic local theorem under regular transverse-joint hypotheses  
**Physical status:** curved replacement for the flat \(2+1\) joint-core exponent \(10/3\)  
**Novelty status:** double-null coordinates and null hypersurface geometry are classical; the project-specific result is the small-disagreement joint-core exponent for arrow-erased causal comparability

## 1. Setting

Let

\[
D=I(p,q)
\]

be a smooth causally convex Alexandrov interval in a \(2+1\)-dimensional Lorentzian spacetime.

Assume that the future null boundary of \(p\) and the past null boundary of \(q\) meet along a compact smooth spacelike edge

\[
E.
\]

Assume:

1. the two null hypersurfaces meet transversely;
2. their null generators are free of conjugate points up to \(E\);
3. a regular double-null coordinate system exists in a neighborhood of \(E\);
4. the thin-null endpoint-volume theorem applies uniformly along the compact edge.

Choose local coordinates

\[
(a,b,s),
\]

where

\[
a\ge0,
\qquad
b\ge0,
\]

are inward optical depths from the two null boundary sheets, and \(s\) parametrizes the edge.

## 2. Endpoint-volume laws

Uniformly along compact pieces of \(E\),

\[
\boxed{
\mathcal V(p,x)
=
c_+(s)
a^{3/2}
[1+o(1)],
}
\]

and

\[
\boxed{
\mathcal V(x,q)
=
c_-(s)
b^{3/2}
[1+o(1)],
}
\]

with

\[
0<c_*\le c_\pm(s)\le c^*<\infty.
\]

The coefficients contain the Penrose-limit geometry along the corresponding null generators.

## 3. Pair coordinates

For an ordered pair

\[
x\prec y
\]

near the joint, write

\[
a_x=\alpha,
\qquad
b_y=\beta,
\]

and

\[
A=a_y-a_x\ge0,
\qquad
B=b_x-b_y\ge0.
\]

Let

\[
\xi=s_y-s_x
\]

be the relative edge displacement.

## 4. Local causal-cap scaling

Because the two optical covectors are transverse null covectors, the metric in the \((a,b,s)\) chart has, at the edge, a nondegenerate double-null form.

After smooth coordinate normalization,

\[
g
=
-2\Omega^2\,da\,db
+
h\,ds^2
+
O(a+b)
\]

at the scaling level relevant here, with

\[
\Omega>0,
\qquad
h>0.
\]

For two sufficiently close points, the squared interval has leading form

\[
g(\delta x,\delta x)
=
-2\Omega^2AB
+
h\xi^2
+
o(AB+\xi^2).
\]

Strict timelike comparability therefore implies two-sided bounds

\[
\boxed{
c_1AB
\le
\xi_{\max}^2
\le
c_2AB
}
\]

for suitable positive constants on a sufficiently small compact joint chart.

Equivalently, the available tangential width is

\[
\boxed{
|\xi|
=
\Theta(\sqrt{AB}).
}
\]

This is the curved \(2+1\) analogue of the flat angular-cap factor.

## 5. Leading endpoint disagreement

The exact curved disagreement identity is

\[
\Delta_g(x,y)
=
\Phi(y)-\Phi(x)
-
2\mathcal V(x,y).
\]

Using the thin-null endpoint laws,

\[
\begin{aligned}
\Phi(y)-\Phi(x)
&=
c_+(s_x)
\left[
(\alpha+A)^{3/2}
-
\alpha^{3/2}
\right]\\
&\quad+
c_-(s_x)
\left[
(\beta+B)^{3/2}
-
\beta^{3/2}
\right]
+
\text{higher-order coefficient variations}.
\end{aligned}
\]

The nearby interval \(I(x,y)\) has ordinary local \(2+1\) volume

\[
\mathcal V(x,y)
=
O(
(AB-\Theta(\xi^2))^{3/2}
).
\]

Under the joint scaling below, this term is higher order.

Thus the leading core disagreement is equivalent, up to positive constants, to

\[
\boxed{
g_{3/2}(\alpha,A)
+
g_{3/2}(\beta,B),
}
\]

where

\[
g_{3/2}(u,v)
=
(u+v)^{3/2}-u^{3/2}.
\]

## 6. Homogeneous joint-core scaling

In the genuinely nonlinear core, all four optical-depth variables scale together:

\[
\alpha,\beta,A,B
=
O(\lambda).
\]

Then

\[
\Delta_g
=
O(\lambda^{3/2}).
\]

Therefore

\[
\lambda
\asymp
\varepsilon^{2/3}.
\]

The pair measure contains:

- \(d\alpha\,d\beta\,dA\,dB\), contributing \(\lambda^4\);
- the relative edge displacement \(d\xi\), whose causal width is \(O(\lambda)\);
- the common edge coordinate \(ds\), which contributes only a finite macroscopic factor.

Hence the core pair volume is

\[
O(\lambda^5).
\]

Substituting

\[
\lambda=\varepsilon^{2/3}
\]

gives

\[
\boxed{
F_{3,g}^{\mathrm{joint\ core}}(\varepsilon)
=
O(
\varepsilon^{10/3}
).
}
\]

## 7. Lower scaling on nondegenerate subcharts

Choose a compact edge segment and scaled variables bounded away from all degenerate faces.

The thin-null coefficients, double-null metric coefficients, and volume density are then bounded above and below by positive constants.

The limiting scaled core has positive finite measure.

Therefore the homogeneous core also satisfies a matching lower scaling on such a restricted sector:

\[
\boxed{
F_{3,g}^{\mathrm{joint\ core}}(\varepsilon)
=
\Theta(
\varepsilon^{10/3}
)
}
\]

for the isolated core sector.

This does not mean the entire joint neighborhood is \(\Theta(\varepsilon^{10/3})\); the transition to larger optical depths matches onto the bulk \(\varepsilon^3\) contribution.

## 8. Bulk dominance

Because

\[
\frac{10}{3}>3,
\]

the genuinely nonlinear joint core is smaller than the bulk scale

\[
\varepsilon^3.
\]

Thus a regular curved \(2+1\) joint does not create a new exponent below the volume-time bulk exponent.

The only remaining issue for the exact curved leading coefficient is a matched-asymptotic justification that the joint-to-bulk transition is already captured by the integrable volume-time coefficient

\[
\kappa(x)^{-3}.
\]

## 9. Integrability of the bulk coefficient near the edge

From

\[
\Phi
\sim
c_+(s)a^{3/2}
-
c_-(s)b^{3/2},
\]

one obtains

\[
d\Phi
\sim
\frac32
c_+(s)a^{1/2}\,da
-
\frac32
c_-(s)b^{1/2}\,db
+
\text{lower tangential terms}.
\]

Since

\[
g^{-1}(da,db)
\]

is nonzero at the transverse null edge while

\[
g^{-1}(da,da)
=
g^{-1}(db,db)
=
0
\]

on the edge,

\[
\kappa^2
=
-g^{-1}(d\Phi,d\Phi)
\asymp
\sqrt{ab}.
\]

Therefore

\[
\boxed{
\kappa^{-3}
\asymp
(ab)^{-3/4}.
}
\]

The local volume measure is smooth in

\[
da\,db\,ds.
\]

Hence

\[
\int_0^\eta
\int_0^\eta
(ab)^{-3/4}
\,da\,db
<
\infty.
\]

Thus the volume-time bulk coefficient is integrable through the regular joint.

## 10. Conditional curved 2+1 conclusion

Under the hypotheses of this theorem and the volume-time bulk theorem, the geometry is now consistent with

\[
\boxed{
F_{3,g}(\varepsilon)
\sim
C_{3,g}^{\mathrm{bulk}}
\varepsilon^3,
}
\]

where

\[
C_{3,g}^{\mathrm{bulk}}
=
\frac{
2\pi
}{
3V_D
}
\int_D
\kappa(x)^{-3}\,d\mu(x).
\]

The only missing proof step is the uniform matched-asymptotic passage between compact bulk charts and the joint transition.

No competing smaller exponent remains under the regular-joint assumptions.

## 11. Failure modes

The result can fail to apply if:

- a null generator reaches a conjugate point before the edge;
- the two null sheets fail to meet transversely;
- the edge is nonsmooth;
- the Penrose-limit coefficient degenerates;
- the volume-time gradient becomes null or vanishes in a nonintegrable way.

These are now explicit geometric failure mechanisms rather than unspecified "curvature corrections."

## 12. Literature relation

Local double-null foliations are standard in Lorentzian geometry and general relativity.

Optical functions satisfy the eikonal equation and their level sets give the two null hypersurface families.

Null Fermi/Penrose expansions control the thin-null endpoint-volume law used here.

The project-specific result is the combination of those tools to establish the \(10/3\) arrow-erasure joint-core exponent in a regular curved \(2+1\) causal diamond.
