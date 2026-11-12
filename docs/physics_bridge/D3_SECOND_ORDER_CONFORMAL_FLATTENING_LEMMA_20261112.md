# Lemma: second-order conformal flattening in 2+1 Lorentzian geometry

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** local differential-geometric lemma  
**Physical status:** identifies why generic \(2+1\) curvature may perturb the arrow-erasure problem more weakly than naive Riemann-normal-coordinate power counting suggests  
**Novelty status:** the vanishing of the Weyl tensor in three dimensions, the Schouten representation of curvature, and conformal normalization are classical. The project-specific role is in the splitter-volume/recovery program.

## 1. Statement

Let

\[
(M^3,g)
\]

be a smooth three-dimensional Lorentzian manifold and let

\[
o\in M.
\]

Then there exists a smooth positive conformal factor

\[
\Omega
\]

defined near \(o\), with

\[
\Omega(o)=1,
\]

such that for

\[
\tilde g=\Omega^2 g
\]

one has

\[
\operatorname{Riem}[\tilde g](o)=0.
\]

Consequently, in \(\tilde g\)-Riemann normal coordinates centered at \(o\),

\[
\boxed{
\tilde g_{\mu\nu}(x)
=
\eta_{\mu\nu}
+
O(|x|^3).
}
\]

Since positive conformal rescalings preserve causal cones exactly, the causal structure of \(g\) is represented locally by a metric whose first deviation from Minkowski cone geometry begins at cubic coordinate order.

## 2. Three-dimensional curvature decomposition

In dimension three the Weyl tensor vanishes identically.

The Riemann tensor is therefore determined completely by the Schouten tensor

\[
P_{ab}
=
R_{ab}
-
\frac14 Rg_{ab}.
\]

Explicitly,

\[
\boxed{
R_{abcd}
=
g_{ac}P_{bd}
-
g_{ad}P_{bc}
-
g_{bc}P_{ad}
+
g_{bd}P_{ac}.
}
\]

Thus

\[
P_{ab}(o)=0
\]

implies

\[
R_{abcd}(o)=0.
\]

## 3. Conformal transformation of the Schouten tensor

Write

\[
\tilde g=e^{2\omega}g.
\]

The Schouten tensor transforms as

\[
\tilde P_{ab}
=
P_{ab}
-
\nabla_a\nabla_b\omega
+
\nabla_a\omega\nabla_b\omega
-
\frac12
(\nabla\omega)^2g_{ab}.
\]

Choose \(\omega\) so that at \(o\),

\[
\omega(o)=0,
\qquad
\nabla_a\omega(o)=0,
\]

and

\[
\boxed{
\nabla_a\nabla_b\omega(o)
=
P_{ab}(o).
}
\]

A smooth local function with prescribed value, gradient, and Hessian at one point always exists.

Then

\[
\tilde P_{ab}(o)=0.
\]

Because the Weyl tensor vanishes identically in dimension three,

\[
\boxed{
\operatorname{Riem}[\tilde g](o)=0.
}
\]

## 4. Normal-coordinate consequence

For any smooth pseudo-Riemannian metric, Riemann normal coordinates at \(o\) satisfy

\[
g_{\mu\nu}(x)
=
\eta_{\mu\nu}
-
\frac13
R_{\mu\alpha\nu\beta}(o)
x^\alpha x^\beta
+
O(|x|^3).
\]

Applying this to \(\tilde g\) and using

\[
\tilde R_{\mu\alpha\nu\beta}(o)=0
\]

gives

\[
\boxed{
\tilde g_{\mu\nu}(x)
=
\eta_{\mu\nu}
+
O(|x|^3).
}
\]

The ordinary quadratic Riemann-normal-coordinate distortion has been removed by a conformal gauge choice.

## 5. Where the first conformal obstruction appears

In three dimensions, local conformal flatness is equivalent to vanishing of the Cotton tensor

\[
C_{abc}
=
\nabla_cP_{ab}
-
\nabla_bP_{ac}.
\]

Thus the first invariant obstruction to extending the pointwise flattening to an actual conformally flat neighborhood depends on first derivatives of the Schouten tensor, equivalently derivatives of curvature.

This is consistent with the cubic remainder in the conformally normalized coordinates.

The statement should not be overstated:

\[
\tilde g
=
\eta+O(|x|^3)
\]

at one center does **not** imply that a generic three-dimensional metric is locally conformally flat.

That requires

\[
C_{abc}=0
\]

through a neighborhood.

## 6. Relevance to the splitter problem

The causal relation is unchanged by

\[
g\mapsto\tilde g=\Omega^2g.
\]

Therefore the non-conformal change in the local causal cones can be studied using \(\tilde g\).

For a diamond of linear scale \(L\) centered at \(o\), the metric perturbation controlling the cones is now schematically

\[
O(\nabla R\,L^3)
\]

rather than the naive

\[
O(RL^2)
\]

Riemann-normal-coordinate term.

The physical volume form of the original metric still differs by the conformal weight

\[
\Omega^{-3},
\]

but bounded positive conformal weights are already covered exactly by the weighted-measure recovery theorem.

Thus, in \(2+1\), the genuinely new causal-cone perturbation begins one order later than the volume reweighting.

## 7. Connection to the Cotton tensor

The Cotton tensor is the three-dimensional analogue of the Weyl tensor as the local conformal-curvature obstruction.

Because

\[
C_{abc}
\sim
\nabla P,
\]

the natural dimensionless non-conformal small-diamond parameter is expected to involve

\[
|C|L^3
\]

rather than only

\[
|R|L^2.
\]

This is a geometric guide, not yet a proved splitter-volume estimate.

A rigorous orientation-recovery theorem still requires control of

\[
\mu_g(A_x\triangle A_y)
\]

uniformly in the rare-event region.

## 8. Literature boundary

Classical facts used here include:

- the Weyl tensor vanishes identically in dimension three;
- the Riemann tensor is determined by the Schouten tensor;
- the Cotton tensor is the obstruction to local conformal flatness in three dimensions;
- Riemann normal-coordinate expansion.

These are standard conformal-geometry results and are not claimed as new.

The project-specific observation is that this conformal normalization removes the \(O(RL^2)\) **causal-cone** perturbation from the \(2+1\) arrow-erasure problem, leaving bounded conformal measure reweighting plus a cubic-order non-conformal remainder.

## 9. Next target

The next required estimate is a quantitative causal-boundary stability lemma of the form

\[
\Delta_g(x,y)
=
\Delta_{\mathrm{conf-flat}}(x,y)
+
\text{controlled remainder}
\]

where the remainder vanishes proportionally to the splitter volume as

\[
\Delta\to0.
\]

In \(2+1\), the cubic conformal normalization suggests that such a relative estimate may depend on a bound for the Cotton tensor and its derivatives rather than only on the Ricci tensor.
