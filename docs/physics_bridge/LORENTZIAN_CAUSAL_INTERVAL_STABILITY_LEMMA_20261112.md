# Lemma: causal-interval volume stability under uniform Lorentzian metric convergence

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic stability lemma  
**Purpose:** remove the domain-convergence hypothesis from the near-null Penrose scaling theorem

## 1. Statement

Let \(K\) be a compact subset of a smooth manifold.

Let

\[
g_n\to g
\]

uniformly on a neighborhood of \(K\), with compatible time orientations.

Fix

\[
p,q\in \operatorname{int}K
\]

such that

\[
p\ll_g q.
\]

Assume:

1. the \(g\)-causal diamond
   \[
   J_g(p,q)
   =
   J_g^+(p)\cap J_g^-(q)
   \]
   is compact and contained in \(\operatorname{int}K\);
2. \(g\) is causally simple on a neighborhood of that diamond;
3. the boundary
   \[
   \partial J_g(p,q)
   \]
   has spacetime volume zero.

Then

\[
\boxed{
\mathbf1_{I_{g_n}(p,q)}
\longrightarrow
\mathbf1_{I_g(p,q)}
}
\]

in measure on \(K\).

If, in addition, the metric volume densities satisfy

\[
d\operatorname{Vol}_{g_n}
\to
d\operatorname{Vol}_g
\]

uniformly on \(K\), then

\[
\boxed{
\operatorname{Vol}_{g_n}
\left(
I_{g_n}(p,q)
\right)
\longrightarrow
\operatorname{Vol}_{g}
\left(
I_{g}(p,q)
\right).
}
\]

## 2. Cone ordering

For Lorentzian metrics \(h_1,h_2\), write

\[
h_1\prec h_2
\]

when every nonzero \(h_1\)-causal vector is \(h_2\)-timelike.

Thus \(h_2\) has strictly wider cones.

Because \(g_n\to g\) uniformly on the compact set \(K\), for every sufficiently small cone-opening parameter \(\epsilon>0\) one can choose smooth metrics

\[
g^-_\epsilon,
\qquad
g^+_\epsilon
\]

such that

\[
g^-_\epsilon
\prec
g
\prec
g^+_\epsilon,
\]

and, for all sufficiently large \(n\),

\[
\boxed{
g^-_\epsilon
\prec
g_n
\prec
g^+_\epsilon.
}
\]

The metrics can be chosen to converge uniformly to \(g\) as

\[
\epsilon\downarrow0.
\]

This is the standard cone-narrowing/cone-widening stability mechanism.

## 3. Interval sandwich

Cone inclusion gives chronological inclusion:

\[
I_{g^-_\epsilon}^+(p)
\subset
I_{g_n}^+(p)
\subset
I_{g^+_\epsilon}^+(p),
\]

and similarly for chronological pasts.

Therefore

\[
\boxed{
I_{g^-_\epsilon}(p,q)
\subset
I_{g_n}(p,q)
\subset
I_{g^+_\epsilon}(p,q).
}
\]

For sufficiently small \(\epsilon\), all three intervals remain inside \(K\), by compactness of the limiting diamond and causal simplicity.

## 4. Interior points persist under narrowing

Let

\[
x\in I_g(p,q).
\]

There exist future-directed timelike curves

\[
p\to x,
\qquad
x\to q.
\]

Their tangent vectors lie strictly inside the \(g\)-cones.

By compactness of each curve segment, there is a uniform timelike margin.

Therefore, for sufficiently small \(\epsilon\),

\[
p\ll_{g^-_\epsilon}x
\ll_{g^-_\epsilon}q.
\]

Hence

\[
\boxed{
x\in I_{g^-_\epsilon}(p,q)
}
\]

for all sufficiently small \(\epsilon\).

## 5. Exterior points remain outside under small widening

Let

\[
x\notin J_g(p,q).
\]

Because \(J_g(p,q)\) is closed by causal simplicity, \(x\) lies in an open set disjoint from the limiting causal diamond.

If arbitrarily small cone widenings made \(x\) belong to

\[
J_{g^+_\epsilon}(p,q),
\]

one could choose \(\epsilon_k\downarrow0\) and causal curves for \(g^+_{\epsilon_k}\) passing through \(x\).

The standard limit-curve compactness argument on \(K\) would produce a \(g\)-causal curve from \(p\) to \(q\) through \(x\), contradicting

\[
x\notin J_g(p,q).
\]

Therefore

\[
\boxed{
x\notin J_{g^+_\epsilon}(p,q)
}
\]

for all sufficiently small \(\epsilon\).

## 6. Pointwise convergence away from the null boundary

For every

\[
x\notin
\partial J_g(p,q),
\]

the preceding two sections imply

\[
\mathbf1_{
I_{g^-_\epsilon}(p,q)
}
(x)
\to
\mathbf1_{
I_g(p,q)
}
(x),
\]

and

\[
\mathbf1_{
I_{g^+_\epsilon}(p,q)
}
(x)
\to
\mathbf1_{
I_g(p,q)
}
(x).
\]

Since the \(g_n\)-interval indicator is sandwiched between them, it follows that

\[
\mathbf1_{I_{g_n}(p,q)}(x)
\to
\mathbf1_{I_g(p,q)}(x)
\]

at every point away from the boundary.

By hypothesis,

\[
\operatorname{Vol}_g(
\partial J_g(p,q)
)
=
0.
\]

Hence convergence holds almost everywhere.

Because the indicators are uniformly bounded by one and \(K\) has finite volume,

\[
\boxed{
\mathbf1_{I_{g_n}(p,q)}
\to
\mathbf1_{I_g(p,q)}
}
\]

in \(L^1\), and therefore in measure.

## 7. Volume-form convergence

Write

\[
d\operatorname{Vol}_{g_n}
=
\rho_n\,d\lambda,
\qquad
d\operatorname{Vol}_{g}
=
\rho\,d\lambda
\]

relative to a fixed smooth reference density on \(K\).

Uniform metric convergence with nondegenerate Lorentzian signature gives

\[
\rho_n\to\rho
\]

uniformly.

Then

\[
\begin{aligned}
&
\left|
\operatorname{Vol}_{g_n}
(I_{g_n})
-
\operatorname{Vol}_{g}
(I_g)
\right|
\\
&\le
\int_K
\left|
\mathbf1_{I_{g_n}}\rho_n
-
\mathbf1_{I_g}\rho
\right|
d\lambda
\to0.
\end{aligned}
\]

Thus the interval volumes converge.

## 8. Application to Penrose scaling

In a regular null Fermi tube, the Penrose-rescaled metrics satisfy

\[
g_\Omega
=
\Omega^{-2}\Psi_\Omega^*g
\longrightarrow
g_{\mathrm{PW}}
\]

smoothly on compact subsets.

Take fixed rescaled endpoints

\[
p,
\qquad
q_1.
\]

If the plane-wave interval

\[
J_{g_{\mathrm{PW}}}(p,q_1)
\]

is compact inside the tube and lies before the first relevant caustic, its null boundary is a smooth hypersurface up to a measure-zero joint.

The lemma therefore gives

\[
\boxed{
\operatorname{Vol}_{g_\Omega}
(I_{g_\Omega}(p,q_1))
\to
\operatorname{Vol}_{g_{\mathrm{PW}}}
(I_{g_{\mathrm{PW}}}(p,q_1)).
}
\]

This removes the explicit domain-convergence assumption from the near-null Alexandrov Penrose-scaling theorem.

## 9. Literature boundary

Cone widening and stable causality under the \(C^0\) fine topology are classical Lorentzian-causality tools; work by Minguzzi and collaborators develops these stability ideas in detail.

The limit-curve argument is also standard.

The present lemma packages those facts specifically for convergence of finite Alexandrov-interval volumes under a convergent family of Lorentzian metrics.

No novelty is claimed for the underlying causal-stability machinery.
