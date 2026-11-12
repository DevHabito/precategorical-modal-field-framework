# Null-joint scaling of comparable-twin obstructions in 3+1 Minkowski sprinklings

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** superseded local-analysis note  
**Current theorem:** MINKOWSKI_D4_TWIN_ASYMPTOTIC_THEOREM_20261111.md

## 1. Purpose of this note

This file records the local null-joint blow-up that led to the complete \(d=4\) comparable-twin theorem.

The final result is now

\[
\boxed{
F_4(\varepsilon)
\sim
3\pi\varepsilon^3
}
\]

and

\[
\boxed{
\mathbb E[T_n]
\sim
\frac{9\pi}{n}.
}
\]

The full proof, including the complementary-sector estimate, is in the current theorem file listed above.

## 2. Joint coordinates

For a point with time \(t\) and spatial radius \(r\), define

\[
\delta=1-r,
\qquad
a=\delta+t,
\qquad
b=\delta-t.
\]

The codimension-two null joint is

\[
a=b=0.
\]

For an ordered comparable pair \(x\prec y\), write

\[
a_x=\alpha,
\qquad
b_y=\beta,
\]

\[
A=a_y-a_x,
\qquad
B=b_x-b_y.
\]

Near the joint, the exact disagreement has the leading form

\[
\boxed{
\Delta
=
\frac{
2\alpha A+A^2+
2\beta B+B^2
}{4}
+
\text{higher-order terms}.
}
\]

Thus

\[
\Delta=O(\varepsilon)
\]

requires the joint scaling

\[
\alpha,\beta,A,B
=
O(\sqrt{\varepsilon}).
\]

## 3. Why the exponent is three

In \(d=4\), the ordered causal-pair measure contains

\[
AB\,
d\alpha\,d\beta\,dA\,dB.
\]

Under the joint scaling,

\[
d\alpha\,d\beta\,dA\,dB
\sim
\varepsilon^2,
\]

and

\[
AB\sim\varepsilon.
\]

Therefore the joint contribution is

\[
\varepsilon^3.
\]

This exponent is geometric, not fitted.

## 4. Exact local integral

Define

\[
g(\alpha,A)=2\alpha A+A^2.
\]

The one-side measure induces

\[
w(g)=\frac{\sqrt g}{2}.
\]

The step integral is

\[
J_{\mathrm{step}}
=
\frac14
\int_{g_1+g_2\le4}
g_1^{1/2}g_2^{1/2}\,
dg_1\,dg_2
=
\boxed{\frac{2\pi}{3}}.
\]

Together with the ordered-pair coefficient \(9/4\) and both time orientations, this gives

\[
\boxed{
3\pi
}
\]

for the complete \(d=4\) small-disagreement tail coefficient.

The corresponding Laplace integral is

\[
J_{\mathrm{Lap}}=4\pi,
\]

which gives

\[
\boxed{
9\pi
}
\]

for the coefficient of \(n^{-1}\) in the expected true-twin count.

## 5. Correction to the intermediate boundary picture

An earlier intermediate version of this note treated a single null face as though it might have its own lower asymptotic exponent.

That was incorrect.

The exact disagreement polynomial shows that away from the joint, the opposite causal-cone contribution restores a nonzero linear term.

Consequently,

\[
F_4^{\mathrm{outside\ joint}}(\varepsilon)
=
O(\varepsilon^4),
\]

and the codimension-two joint is the unique leading \(\varepsilon^3\) sector.

## 6. Dimension threshold

The local joint exponent in spacetime dimension \(d\) is

\[
\beta_{\mathrm{joint}}(d)
=
2+\frac4d.
\]

The generic bulk exponent is

\[
\beta_{\mathrm{bulk}}(d)=d.
\]

The first integer dimension in which the joint wins is

\[
\boxed{d=4}.
\]

Thus \(3+1\) spacetime is the first integer-dimensional case where the null joint changes the leading small-disagreement asymptotic.

## 7. Current use

This note should now be read as the derivational bridge to the theorem, not as the authoritative final statement.

For the complete proof, symbolic regression, and current research consequence, use:

- docs/physics_bridge/MINKOWSKI_D4_TWIN_ASYMPTOTIC_THEOREM_20261111.md
- tools/verify_d4_twin_asymptotic_symbolic.py
- tools/minkowski_null_joint_twin_asymptotic.py
