# Explicit nonconformally-flat 2+1 example inside the orientation-recovery class

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** explicit analytic example using the recovery-openness theorem
**Physical status:** concrete genuinely nonconformal curved spacetime family with asymptotic arrow-erasure recovery

## 1. Metric family

Consider, on a bounded coordinate neighborhood of the origin,

\[
\boxed{
g_\varepsilon
=
-dt^2
+
dx^2
+
f_\varepsilon(x)^2dy^2,
}
\]

where

\[
\boxed{
f_\varepsilon(x)
=
1+\varepsilon x^3.
}
\]

Choose the coordinate neighborhood

\[
|x|\le R
\]

and restrict

\[
|\varepsilon|R^3<\frac12.
\]

Then

\[
f_\varepsilon(x)>\frac12,
\]

so the metric is smooth and Lorentzian.

As

\[
\varepsilon\to0,
\]

\[
g_\varepsilon
\to
\eta
\]

in \(C^4\) on every fixed bounded coordinate neighborhood.

## 2. Ultrastatic product structure

Write

\[
g_\varepsilon
=
-dt^2
+
h_\varepsilon,
\]

with

\[
h_\varepsilon
=
dx^2
+
f_\varepsilon(x)^2dy^2.
\]

The spatial metric is a two-dimensional warped product.

Its Gaussian curvature is

\[
\boxed{
K_\varepsilon(x)
=
-\frac{
f_\varepsilon''(x)
}{
f_\varepsilon(x)
}.
}
\]

For the chosen \(f_\varepsilon\),

\[
f_\varepsilon''(x)
=
6\varepsilon x,
\]

so

\[
\boxed{
K_\varepsilon(x)
=
-\frac{
6\varepsilon x
}{
1+\varepsilon x^3
}.
}
\]

In particular,

\[
K_\varepsilon(0)=0,
\]

but

\[
\boxed{
K_\varepsilon'(0)
=
-6\varepsilon.
}
\]

Thus the spatial curvature is not locally constant when

\[
\varepsilon\ne0.
\]

## 3. Three-dimensional Ricci tensor

For an ultrastatic product

\[
-\mathbb R_t^2\times(\Sigma,h),
\]

the time direction is flat and the only nonzero Ricci components are spatial.

In two spatial dimensions,

\[
\operatorname{Ric}^{(h)}_{ij}
=
K h_{ij}.
\]

Therefore the \(2+1\) Ricci tensor satisfies

\[
\operatorname{Ric}_{00}=0,
\]

and

\[
\operatorname{Ric}_{ij}
=
K_\varepsilon h_{ij}.
\]

The three-dimensional scalar curvature is

\[
R=2K_\varepsilon.
\]

## 4. Schouten tensor

In three dimensions use

\[
P_{ab}
=
R_{ab}
-
\frac14
R g_{ab}.
\]

For the time-time component,

\[
\begin{aligned}
P_{00}
&=
0
-
\frac14
(2K_\varepsilon)(-1)\\
&=
\boxed{
\frac12K_\varepsilon.
}
\end{aligned}
\]

The mixed time-space components vanish.

## 5. Cotton tensor

Use the three-index Cotton tensor

\[
C_{abc}
=
\nabla_cP_{ab}
-
\nabla_bP_{ac}.
\]

The ultrastatic product has no mixed time-space connection coefficients.

Therefore

\[
C_{00x}
=
\nabla_xP_{00}
-
\nabla_0P_{0x}
=
\frac12
K_\varepsilon'(x).
\]

At the origin,

\[
\boxed{
C_{00x}(0)
=
-3\varepsilon.
}
\]

Hence, for every

\[
\varepsilon\ne0,
\]

\[
\boxed{
C_{abc}\not\equiv0.
}
\]

In three spacetime dimensions, vanishing Cotton tensor is equivalent to local conformal flatness.

Therefore

\[
\boxed{
g_\varepsilon
\text{ is not locally conformally flat for }
\varepsilon\ne0.
}
\]

## 6. A fixed timelike diamond

Choose reference endpoints

\[
p=(-T,0,0),
\qquad
q=(T,0,0),
\]

with \(T>0\) small enough that the Minkowski diamond

\[
D_0=I_\eta(p,q)
\]

has closure inside the chosen coordinate neighborhood.

The unit/reference Minkowski diamond satisfies the regular recovery hypotheses with strict margins.

Because

\[
g_\varepsilon\to\eta
\]

in \(C^4\), the recovery-openness theorem gives an

\[
\varepsilon_0>0
\]

such that for every

\[
|\varepsilon|<\varepsilon_0,
\]

the perturbed diamond

\[
D_\varepsilon
=
I_{g_\varepsilon}(p,q)
\]

satisfies H1--H5.

## 7. Orientation-recovery theorem

For every fixed

\[
0<|\varepsilon|<\varepsilon_0,
\]

let

\[
p_{3,\varepsilon}^{\mathrm{UPO}}(n)
\]

be the arrow-erasure recovery probability for an iid sprinkling from normalized physical volume in

\[
D_\varepsilon.
\]

Then

\[
\boxed{
p_{3,\varepsilon}^{\mathrm{UPO}}(n)
\to1.
}
\]

More sharply,

\[
\boxed{
1-p_{3,\varepsilon}^{\mathrm{UPO}}(n)
\sim
\frac{
\mathcal K_\varepsilon
}{
n
},
}
\]

where

\[
\boxed{
\mathcal K_\varepsilon
=
\frac{
2\pi
}{
V_{D_\varepsilon}
}
\int_{D_\varepsilon}
\left[
-g_\varepsilon^{-1}
(
d\Phi_\varepsilon,
d\Phi_\varepsilon
)
\right]^{-3/2}
\,d\mu_\varepsilon.
}
\]

This is a genuinely nonconformal curved example.

It is not covered merely by the conformal-weight theorem.

## 8. Flat limit

Continuity of the leading coefficient under regular metric perturbations gives

\[
\boxed{
\mathcal K_\varepsilon
\to
\frac{32\pi}{3}
}
\]

as

\[
\varepsilon\to0.
\]

Thus the nonconformal curved family continuously approaches the flat recovery law.

## 9. Reflection symmetry in the perturbation parameter

Under the coordinate reflection

\[
x\mapsto-x,
\]

\[
f_\varepsilon(-x)
=
1-\varepsilon x^3
=
f_{-\varepsilon}(x).
\]

Hence the reflection is an isometry between

\[
g_\varepsilon
\]

and

\[
g_{-\varepsilon}.
\]

The endpoints \(p,q\) are fixed by this reflection.

Therefore the corresponding diamonds and sprinkling problems are isometric.

Thus

\[
\boxed{
\mathcal K_\varepsilon
=
\mathcal K_{-\varepsilon}.
}
\]

The leading reconstruction-error coefficient is an even function of the deformation parameter.

If differentiability of \(\mathcal K_\varepsilon\) in the metric parameter is invoked, this immediately gives

\[
\mathcal K_\varepsilon'
\big|_{\varepsilon=0}
=
0.
\]

No explicit second-order coefficient is derived here.

## 10. Why this example matters

The conformal robustness theorem already covered curved metrics whose causal cones remain exactly Minkowskian.

The present metric has nonzero Cotton tensor and therefore deforms the conformal causal geometry itself.

Yet for sufficiently small deformation, the orientation-recovery theorem and its \(1/n\) error law survive.

This proves that the recovery phenomenon is not restricted to conformal reweightings of flat causal structure.

## 11. Reproducible curvature check

The algebraic check uses only

\[
K=-f''/f,
\]

and

\[
C_{00x}=\frac12K'.
\]

For

\[
f=1+\varepsilon x^3,
\]

\[
K'(0)=-6\varepsilon,
\]

hence

\[
C_{00x}(0)=-3\varepsilon.
\]

An independent symbolic session reproduced these identities exactly.
