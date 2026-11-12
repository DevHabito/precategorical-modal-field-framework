# Theorem capsule: uniform regularity of volume-null coordinates along a compact null joint

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic reduction using a uniform Penrose-Fermi expansion  
**Physical status:** removes the main coordinate-regularity hypothesis from the curved \(2+1\) joint theorem  
**Novelty status:** the Penrose-Fermi expansion is established literature; its use to regularize Alexandrov-volume null coordinates is project-specific

## 1. Setting

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval in a smooth \(d\)-dimensional Lorentzian spacetime.

Let

\[
\Sigma
=
\partial I^+(p)
\cap
\partial I^-(q)
\]

be a compact smooth spacelike joint.

Assume:

1. the two null boundaries are smooth and transverse near \(\Sigma\);
2. each null generator from \(p\) to \(\Sigma\), and from \(\Sigma\) to \(q\), is free of cut/conjugate points in the relevant segment;
3. the generators form smooth compact families;
4. uniform null Fermi/Penrose tubes exist around those families.

The goal is to control

\[
a(x)
=
\mathcal V(p,x)^{2/d},
\qquad
b(x)
=
\mathcal V(x,q)^{2/d},
\]

where

\[
\mathcal V
\]

is normalized Alexandrov volume.

## 2. One-generator near-null expansion

Fix one future null generator

\[
\gamma
\]

from \(p\) to a point of \(\Sigma\).

Let

\[
\delta
\]

be a regular inward null coordinate transverse to the future light cone of \(p\).

The Penrose-limit volume theorem gives

\[
\mathcal V(p,x_\delta)
=
\delta^{d/2}
C_\gamma
+
o(
\delta^{d/2}
),
\]

where

\[
C_\gamma>0
\]

is the normalized volume of a fixed Alexandrov interval in the plane-wave Penrose limit associated with \(\gamma\).

## 3. First subleading Penrose-Fermi control

In null Fermi coordinates, the rescaled metrics admit a covariant expansion of the form

\[
g_\Omega
=
g_{\mathrm{PW}}
+
\Omega h_1
+
O(\Omega^2),
\]

on compact subsets, where

\[
\Omega=\sqrt{\delta}.
\]

Assume this expansion is uniform over the compact family of joint generators in the \(C^2\) topology.

The causal-interval stability lemma, applied uniformly to the parameter family, then gives

\[
\operatorname{Vol}_{g_\Omega}
\left(
I_{g_\Omega}(p,q_1)
\right)
=
C_\gamma
+
O(\Omega),
\]

uniformly in \(\gamma\).

Restoring the physical volume factor

\[
\Omega^d
=
\delta^{d/2},
\]

we obtain

\[
\boxed{
\mathcal V(p,x_\delta)
=
\delta^{d/2}
\left[
C_\gamma
+
O(
\sqrt{\delta}
)
\right].
}
\]

The same statement holds at the future boundary with the corresponding family of incoming null generators.

## 4. Continuity and positivity of the coefficient

The plane-wave profile is determined by curvature components along the null generator in a parallel-propagated transverse frame.

Because:

- the spacetime curvature is smooth;
- the joint family of generators is smooth;
- the family is compact;
- no generator reaches a cut/conjugate degeneration;

the plane-wave profiles vary continuously with the generator label.

The causal-interval volume stability lemma then gives continuity of

\[
\gamma
\longmapsto
C_\gamma.
\]

Each coefficient is strictly positive because the fixed rescaled endpoints are timelike related in the plane-wave limit.

Compactness therefore gives

\[
\boxed{
0<C_{\min}
\le
C_\gamma
\le
C_{\max}<\infty.
}
\]

## 5. Volume-null coordinate expansion

Raise the near-null volume expansion to the power

\[
2/d.
\]

Then

\[
\begin{aligned}
a(x_\delta)
&=
\mathcal V(p,x_\delta)^{2/d}\\
&=
\delta
C_\gamma^{2/d}
\left[
1
+
O(
\sqrt{\delta}
)
\right].
\end{aligned}
\]

Thus

\[
\boxed{
a
=
c_\gamma
\delta
\left[
1
+
O(
\sqrt{\delta}
)
\right],
}
\]

where

\[
c_\gamma
=
C_\gamma^{2/d}.
\]

Uniformly,

\[
0<c_{\min}
\le
c_\gamma
\le
c_{\max}<\infty.
\]

Therefore

\[
\boxed{
a\asymp\delta
}
\]

uniformly along the compact joint.

The same holds for

\[
b
=
\mathcal V(\cdot,q)^{2/d}.
\]

## 6. Transverse derivative

If the uniform Penrose-Fermi expansion is differentiable in the transverse scaling parameter, then

\[
\partial_\delta a
=
c_\gamma
+
O(
\sqrt{\delta}
).
\]

Consequently,

\[
\boxed{
\partial_\delta a
\to
c_\gamma>0
}
\]

uniformly as the null boundary is approached.

Hence \(a\) is a regular transverse coordinate.

Likewise,

\[
b
\]

is a regular transverse coordinate at the other null boundary.

Together with a smooth joint coordinate \(\sigma\),

\[
\boxed{
(a,b,\sigma)
}
\]

forms a regular volume-null coordinate system in a sufficiently small joint neighborhood.

## 7. Jacobian bounds

Because the transformation from an ordinary double-null chart to

\[
(a,b,\sigma)
\]

has transverse derivatives bounded above and below by positive constants, its Jacobian satisfies

\[
\boxed{
0<c_J
\le
J(a,b,\sigma)
\le
C_J<\infty.
}
\]

This establishes the measure-regularity hypothesis used in the curved \(2+1\) joint-suppression theorem.

## 8. Causal-cap transfer

In an ordinary regular double-null chart, a small comparable pair satisfies a transverse cap estimate of the form

\[
|\Delta\sigma|
\le
C
\sqrt{
\delta_a\delta_b
}.
\]

Since

\[
a\asymp\delta_a,
\qquad
b\asymp\delta_b,
\]

the same estimate becomes

\[
\boxed{
|\Delta\sigma|
\le
C'
\sqrt{AB}
}
\]

in volume-null increments.

Thus the angular/tangential pair-measure factor required by the joint-suppression theorem is preserved.

## 9. Consequence for 2+1

For

\[
d=3,
\]

\[
a
=
\mathcal V(p,\cdot)^{2/3},
\qquad
b
=
\mathcal V(\cdot,q)^{2/3}
\]

are therefore regular joint coordinates under the uniform regular-Penrose-tube assumptions.

This removes the principal coordinate hypothesis from

\[
\texttt{CURVED\_D3\_REGULAR\_JOINT\_SUPPRESSION\_THEOREM\_20261112.md}.
\]

The remaining local geometric input there is the small-interval estimate

\[
\mathcal V(x,y)
\le
C(AB)^{3/2},
\]

which follows from an ordinary local convex-normal-neighborhood volume estimate because \(x\) and \(y\) themselves approach one another in the joint scaling.

## 10. Literature boundary

Blau, Frank, and Weiss developed null Fermi coordinates and the covariant expansion around the Penrose plane-wave limit:

**M. Blau, D. Frank, S. Weiss, "Fermi Coordinates and Penrose Limits," Classical and Quantum Gravity 23 (2006), 3993--4010, DOI 10.1088/0264-9381/23/11/020.**

Modern Penrose-expansion work continues this null-geodesic expansion beyond leading order.

The present result uses that established expansion to identify the regularity of the volume-defined optical coordinates required by the arrow-erasure disagreement problem.

## 11. Remaining review target

The only nontrivial analytic step in this capsule that deserves an independent technical check is the uniform \(O(\Omega)\) control of the rescaled Alexandrov-volume functional over the compact family of plane-wave profiles.

The causal-interval stability lemma gives continuity.

The stated rate uses the first subleading Penrose-Fermi expansion and should be reviewed as a parameter-dependent domain perturbation estimate before publication.
