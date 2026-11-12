# Higher-dimensional UPO obstruction audit — comparable twins and boundary localization

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** superseded finite-audit note  
**Current analytic result:** MINKOWSKI_D4_TWIN_ASYMPTOTIC_THEOREM_20261111.md

## 1. Purpose

This file records the finite higher-dimensional audit that identified adjacent true twins as the dominant local UPO obstruction in the tested \(2+1\) and \(3+1\) Minkowski sprinklings.

A true-twin pair \(x,y\) satisfies

\[
x\sim y
\]

and

\[
N(x)\setminus\{y\}
=
N(y)\setminus\{x\}.
\]

Then \(\{x,y\}\) is a size-two non-stable module and therefore obstructs unique partial orderability inside a connected comparability component.

## 2. Exact expectation bridge

For

\[
A_x=\{z:z\sim x\},
\]

define

\[
\Delta(x,y)
=
\mu(A_x\triangle A_y).
\]

If \(T_n\) counts adjacent true-twin pairs in an iid size-\(n\) sprinkling, then

\[
\boxed{
\mathbb E[T_n]
=
\binom n2
\mathbb E
\left[
\mathbf1_{\{X\sim Y\}}
(1-\Delta(X,Y))^{n-2}
\right].
}
\]

This identity is exact.

The finite audit originally motivated the hypothesis that the small-\(\Delta\) tail is controlled by the null-waist boundary.

That question has since been solved analytically in \(d=4\).

## 3. Current d=4 theorem

For \(3+1\) Minkowski spacetime,

\[
\boxed{
F_4(\varepsilon)
=
\Pr(
X\sim Y,\,
\Delta(X,Y)\le\varepsilon
)
\sim
3\pi\varepsilon^3.
}
\]

Consequently,

\[
\boxed{
\mathbb E[T_n]
\sim
\frac{9\pi}{n}.
}
\]

The codimension-two null joint is the unique leading small-\(\Delta\) sector.

Away from the joint,

\[
F_4^{\mathrm{outside\ joint}}(\varepsilon)
=
O(\varepsilon^4).
\]

The complete proof is in

MINKOWSKI_D4_TWIN_ASYMPTOTIC_THEOREM_20261111.md.

## 4. Why this note is retained

The original Monte Carlo audit remains useful as provenance:

- it showed that most finite non-UPO samples contain a minimal size-two module;
- the endpoint comparable-volume score \(Q_d\) of those twins moved toward low-\(Q_d\) regions as \(n\) increased;
- implication-class counts increasingly concentrated near the first non-UPO level;
- those observations led directly to the null-joint calculation.

The finite observations are not needed for the proof.

## 5. Current hierarchy

The next obstruction level is an induced-\(P_3\) module.

In \(d=4\),

\[
\mathbb E[M_{3,n}]
=
\Theta(n^{-2}).
\]

The global arbitrary-size module problem is now reduced by splitter closure; see

MINKOWSKI_SPLITTER_CLOSURE_REDUCTION_20261111.md.

## 6. Literature boundary

True twins, modules, modular decomposition, implication classes, and UPO theory are classical.

The project-specific contribution is the Lorentzian sprinkling measure together with the arrow-erasure reconstruction question and the resulting asymptotics.

No equivalent \(3\pi\varepsilon^3\) / \(9\pi n^{-1}\) result was located in the targeted review.

Absolute priority is not certified.
