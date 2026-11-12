# Exact disagreement geometry for comparable-twin obstructions

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** superseded transition note  
**Current theorem:** see MINKOWSKI_D4_TWIN_ASYMPTOTIC_THEOREM_20261111.md

## 1. Exact continuum quantity

For an event \(x\) in a flat Alexandrov interval \(D=I(p,q)\), define

\[
A_x=\{z\in D:\ z\sim x\}.
\]

For a comparable pair \(x\prec y\), define

\[
\Delta(x,y)=\mu(A_x\triangle A_y).
\]

The exact normalized disagreement volume is

\[
\boxed{
\Delta(x,y)
=
\frac{
\tau(p,y)^d-\tau(p,x)^d+
\tau(x,q)^d-\tau(y,q)^d-
2\tau(x,y)^d
}{2^d}.
}
\]

This follows from

\[
A_x\cap A_y
=
I(p,x)
\;\dot\cup\;
I(x,y)
\;\dot\cup\;
I(y,q)
\]

up to measure-zero boundaries, together with Alexandrov-volume scaling

\[
\mu(I(a,b))
=
\frac{\tau(a,b)^d}{2^d}.
\]

## 2. Exact twin expectation identity

Let \(T_n\) be the number of comparable true-twin pairs in an iid size-\(n\) sprinkling.

Conditioned on \(X=x\) and \(Y=y\), all remaining \(n-2\) points must avoid

\[
A_x\triangle A_y.
\]

Therefore

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

This identity remains one of the main bridges between graph modules and Lorentzian geometry.

## 3. What changed after this exploratory note

This note originally recorded a finite-window numerical suggestion that the \(d=4\) small-\(\Delta\) tail had an exponent near three.

That question has since been resolved analytically.

The current result is

\[
\boxed{
F_4(\varepsilon)
=
\Pr(
X\sim Y,\,
\Delta(X,Y)\le\varepsilon
)
\sim
3\pi\varepsilon^3,
}
\]

and consequently

\[
\boxed{
\mathbb E[T_n]
\sim
\frac{9\pi}{n}.
}
\]

The leading contribution comes uniquely from the codimension-two null joint.

Away from the joint, the exact disagreement has a nonzero linear response and contributes only

\[
O(\varepsilon^4).
\]

A previous intermediate idea that a single null face might define a separate leading exponent was incorrect and has been removed from the current theorem.

## 4. Reproducible checks

The exact polynomial and coefficient algebra are checked by

tools/verify_d4_twin_asymptotic_symbolic.py

and the slow finite-\(n\) approach to the \(9\pi\) coefficient is tested by

tools/minkowski_null_joint_twin_asymptotic.py.

## 5. Literature boundary

Symmetric differences of causal or Alexandrov neighborhoods are not themselves new.

Bombelli's 1987 dissertation used symmetric differences to quantify disagreement between causal structures, and modern Lorentzian metric-space work uses related future/past symmetric differences.

The project-specific contribution is the use of \(\Delta(x,y)\) as the exact probability-controlling variable for true-twin modules in an arrow-erased Minkowski causal-set comparability graph.

For the complete proof and current novelty statement, use

MINKOWSKI_D4_TWIN_ASYMPTOTIC_THEOREM_20261111.md.
