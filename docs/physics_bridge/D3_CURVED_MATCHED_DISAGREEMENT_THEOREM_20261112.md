# Theorem: matched small-disagreement asymptotic in regular curved 2+1 causal diamonds

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** conditional analytic theorem under explicit regular-diamond hypotheses  
**Physical status:** curved \(2+1\) small-disagreement law for arrow-erased causal comparability  
**Novelty status:** the geometric tools are classical; the matched splitter-volume asymptotic is project-specific

## 1. Setting

Let

\[
D=I(p,q)
\]

be a compact causally convex Alexandrov interval in a smooth \(2+1\)-dimensional Lorentzian spacetime.

Use normalized physical volume

\[
d\mu
=
\frac{d\operatorname{Vol}_g}{V_D},
\qquad
V_D=\operatorname{Vol}_g(D).
\]

For \(x\in D\), define

\[
A_x=\{z\in D:z\sim x\},
\]

and for comparable \(x,y\),

\[
\Delta_g(x,y)
=
\mu(A_x\triangle A_y).
\]

Let

\[
F_{3,g}(\varepsilon)
=
\Pr(
X\sim Y,\,
\Delta_g(X,Y)\le\varepsilon
).
\]

## 2. Regular-diamond hypotheses

Assume the following.

### H1. Smooth temporal volume function

The function

\[
\Phi(x)
=
\frac{
\operatorname{Vol}(I(p,x))
-
\operatorname{Vol}(I(x,q))
}{
V_D
}
\]

is \(C^2\) in the interior and has timelike differential

\[
d\Phi_x
\]

for every interior point.

Define

\[
\kappa(x)
=
\sqrt{
-g^{-1}(d\Phi_x,d\Phi_x)
}.
\]

### H2. Regular transverse edge

The two null boundary sheets

\[
\partial I^+(p),
\qquad
\partial I^-(q)
\]

meet along a compact smooth spacelike edge \(E\), transversely.

### H3. No relevant null caustics

The null generators from \(p\) and \(q\) reaching \(E\) have no conjugate points on the relevant segments, and admit uniform null-Fermi tubes.

### H4. Uniform thin-null endpoint law

In optical-depth coordinates \((a,b,s)\) near \(E\),

\[
\mathcal V(p,x)
=
c_+(s)a^{3/2}
+
O(a^2),
\]

\[
\mathcal V(x,q)
=
c_-(s)b^{3/2}
+
O(b^2),
\]

uniformly along the compact edge, with

\[
0<c_*\le c_\pm(s)\le c^*<\infty.
\]

This is supplied by the Penrose-Fermi thin-null theorem under the regular-tube assumptions.

### H5. Regular pair-cap geometry

For nearby comparable pairs in the same joint chart, if

\[
A=a_y-a_x\ge0,
\qquad
B=b_x-b_y\ge0,
\]

then the allowed relative edge displacement \(\xi=s_y-s_x\) satisfies

\[
|\xi|
=
\Theta(\sqrt{AB})
\]

uniformly.

## 3. Interior bulk asymptotic

On every compact set

\[
K\Subset D^\circ
\]

separated from the null edge, the exact identity

\[
\Delta_g(x,\exp_x h)
=
d\Phi_x(h)
+
O(|h|^2)
\]

is uniform.

Since \(d\Phi_x\) is timelike, the local future-cone volume is

\[
\frac{\pi}{3}
\frac{\varepsilon^3}{\kappa(x)^3}.
\]

Including both time orientations gives

\[
\boxed{
F_{3,g}^{K}(\varepsilon)
=
\frac{2\pi}{3V_D}
\left(
\int_K
\kappa(x)^{-3}\,d\mu(x)
\right)
\varepsilon^3
+
o_K(\varepsilon^3).
}
\]

## 4. Behavior of kappa near the edge

From the thin-null endpoint law,

\[
\Phi
=
c_+(s)a^{3/2}
-
c_-(s)b^{3/2}
+
O(a^2+b^2).
\]

Thus

\[
d\Phi
=
\frac32
c_+(s)a^{1/2}da
-
\frac32
c_-(s)b^{1/2}db
+
O(a+b)\,ds
+
O(a+b).
\]

The double-null metric has

\[
-g^{-1}(da,db)
\asymp1
\]

while the self-contractions of the optical covectors vanish at the edge.

Therefore

\[
\boxed{
\kappa^2
\asymp
\sqrt{ab}
}
\]

and hence

\[
\boxed{
\kappa^{-3}
\asymp
(ab)^{-3/4}.
}
\]

This is locally integrable:

\[
\int_0^\eta
\int_0^\eta
(ab)^{-3/4}
\,da\,db
=
16\eta^{1/2}.
\]

Thus the proposed bulk coefficient

\[
\int_D
\kappa^{-3}\,d\mu
\]

is finite at a regular edge.

## 5. Joint one-side matching integral

Fix an edge coordinate \(s\) and consider one optical side.

Up to smooth positive coefficients, the endpoint increment has the form

\[
(\alpha+A)^{3/2}
-
\alpha^{3/2}.
\]

The pair-cap measure contributes

\[
A^{1/2}\,dA\,d\alpha
\]

on that side.

For a small fixed edge cutoff \(\eta\), define

\[
J(\varepsilon,\eta)
=
\int_0^\eta
\int_0^\infty
A^{1/2}
\mathbf1_{
\{
(\alpha+A)^{3/2}
-
\alpha^{3/2}
\le C\varepsilon
\}
}
\,dA\,d\alpha.
\]

Split at

\[
\alpha
=
\varepsilon^{2/3}.
\]

### Nonlinear core

For

\[
0\le\alpha\le\varepsilon^{2/3},
\]

\[
A=O(\varepsilon^{2/3}),
\]

so

\[
J_{\mathrm{core}}
=
O(\varepsilon^{5/3}).
\]

### Matching region

For

\[
\varepsilon^{2/3}
\le\alpha\le\eta,
\]

the mean-value theorem gives

\[
A
=
O(
\varepsilon\alpha^{-1/2}
).
\]

Therefore

\[
\begin{aligned}
J_{\mathrm{match}}
&=
C(s)\varepsilon^{3/2}
\int_{\varepsilon^{2/3}}^\eta
\alpha^{-3/4}\,d\alpha
+
o(\varepsilon^{3/2})\\
&=
4C(s)
\eta^{1/4}
\varepsilon^{3/2}
+
O(\varepsilon^{5/3}).
\end{aligned}
\]

The coefficient \(C(s)\) is exactly the local coefficient obtained from the linearized volume-time gradient.

Thus the joint transition does not create a new independent \(\varepsilon^3\) coefficient.

It is the boundary portion of the bulk integral.

## 6. Two-sided joint contribution

The two optical sides combine through the pair-cap factor.

The product of the matching pieces is

\[
O(
\eta^{1/2}\varepsilon^3
),
\]

matching the edge contribution

\[
\int_{a,b<\eta}
\kappa^{-3}\,d\mu
=
O(\eta^{1/2}).
\]

Terms involving at least one nonlinear-core side gain an additional positive power of \(\varepsilon\).

The fully nonlinear core satisfies

\[
\boxed{
O(\varepsilon^{10/3}).
}
\]

Therefore, after subtracting the bulk coefficient associated with

\[
\kappa^{-3},
\]

the residual joint contribution is

\[
o(\varepsilon^3)
\]

as

\[
\varepsilon\to0
\]

followed by

\[
\eta\to0.
\]

## 7. Global matched asymptotic

Exhaust the interior by compact sets

\[
K_\eta
=
D\setminus J_\eta,
\]

where \(J_\eta\) is an optical-depth neighborhood of the null edge.

For fixed \(\eta\),

\[
F_{3,g}^{K_\eta}(\varepsilon)
=
C(K_\eta)\varepsilon^3
+
o_\eta(\varepsilon^3).
\]

The joint matching estimate gives

\[
F_{3,g}^{J_\eta}(\varepsilon)
=
\left(
C(D)-C(K_\eta)
\right)
\varepsilon^3
+
O(\eta^\rho\varepsilon^3)
+
O(\varepsilon^{10/3})
\]

for some \(\rho>0\).

Letting first

\[
\varepsilon\downarrow0
\]

and then

\[
\eta\downarrow0
\]

yields

\[
\boxed{
F_{3,g}(\varepsilon)
\sim
C_{3,g}
\varepsilon^3,
}
\]

with

\[
\boxed{
C_{3,g}
=
\frac{
2\pi
}{
3V_D
}
\int_D
\kappa(x)^{-3}\,d\mu(x).
}
\]

## 8. Flat-space check

For the unit flat \(2+1\) diamond,

\[
V_D
=
\frac{2\pi}{3},
\]

and the integral evaluates to

\[
\frac{32\pi}{9}.
\]

Thus

\[
C_{3,\eta}
=
\frac{32\pi}{9},
\]

recovering the exact Minkowski result.

## 9. True-twin first moment in the curved regular diamond

Let \(T_n\) count comparable true-twin pairs.

The exact identity remains

\[
\mathbb E[T_n]
=
\binom n2
\int
(1-\delta)^{n-2}
\,dF_{3,g}(\delta).
\]

Using

\[
F_{3,g}(\delta)
\sim
C_{3,g}\delta^3,
\]

Laplace-Stieltjes transfer gives

\[
\boxed{
\mathbb E[T_n]
\sim
3C_{3,g}\,n^{-1}.
}
\]

Therefore the natural curved leading twin constant is

\[
\boxed{
K_{3,g}^{\mathrm{twin}}
=
3C_{3,g}
=
\frac{
2\pi
}{
V_D
}
\int_D
\kappa(x)^{-3}\,d\mu(x).
}
\]

## 10. What this theorem proves

Under H1--H5, the small-disagreement law and the comparable-true-twin first moment are fully determined.

The leading exponent is unchanged:

\[
\boxed{
F_{3,g}(\varepsilon)
\sim
C_{3,g}\varepsilon^3,
}
\]

\[
\boxed{
\mathbb E[T_n]
\sim
K_{3,g}^{\mathrm{twin}}n^{-1}.
}
\]

The coefficient is an intrinsic Lorentzian functional of the finite-diamond volume-time gradient.

## 11. What is still needed for full curved UPO recovery

To promote the true-twin first moment to

\[
1-p_{3,g}^{\mathrm{UPO}}(n)
\sim
K_{3,g}^{\mathrm{twin}}n^{-1},
\]

the stochastic graph arguments must also be extended quantitatively to the curved diamond.

The remaining ingredients are:

1. a curved uniform comparable-ball estimate
   \[
   \sup_x\mu(B_t(x))=O(t^2);
   \]
2. low-degree internal sparsity near the regular edge;
3. graphon primeness for the curved causal kernel;
4. tip-clearance control near \(p\) and \(q\);
5. component and module assembly.

Several of these are primarily causal-topological rather than curvature-specific.

The present theorem closes the main rare-event geometric calculation in regular curved \(2+1\).
