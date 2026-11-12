# Hypothesis reduction for the regular curved 2+1 orientation-recovery theorem

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** theorem refactoring / assumption reduction  
**Purpose:** distinguish primitive geometric assumptions from estimates that are now derived inside the repository

## 1. Motivation

The first version of the curved \(2+1\) theorem listed six hypotheses, including several asymptotic estimates that were not yet independently proved.

Subsequent work has derived those estimates from more primitive Lorentzian-geometric conditions.

The theorem can therefore be reformulated with a smaller assumption set.

## 2. Primitive assumptions

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval in a smooth \(2+1\)-dimensional time-oriented Lorentzian spacetime.

The reduced theorem uses three primitive assumptions.

### R1. C1 temporal finite-diamond volume function

Define

\[
\Phi(x)
=
\frac{
\operatorname{Vol}(I(p,x))
-
\operatorname{Vol}(I(x,q))
}{
V_D
}.
\]

Assume

\[
\boxed{
\Phi\in C^1(D^\circ)
}
\]

and

\[
\boxed{
d\Phi
\text{ is timelike everywhere in }D^\circ.
}
\]

No \(C^2\) assumption is required.

For every compact

\[
K\Subset D^\circ,
\]

\(C^1\) regularity gives the uniform first-order expansion

\[
\Phi(\exp_x h)-\Phi(x)
=
d\Phi_x(h)
+
o_K(|h|).
\]

That is sufficient for the local bulk cone-volume asymptotic.

### R2. Regular transverse null edge

Assume the two null boundary sheets

\[
\partial I^+(p),
\qquad
\partial I^-(q)
\]

meet transversely along a compact smooth spacelike edge \(E\).

Assume the relevant null-generator families from the tips to \(E\):

- contain no conjugate points;
- contain no cut points;
- admit a uniform compact null-Fermi tube;
- admit a regular double-null neighborhood of \(E\).

### R3. Regular timelike tips

Assume the one-sided volume functions

\[
x\mapsto
\frac{\operatorname{Vol}(I(x,q))}{V_D}
\]

near \(p\), and its time-reversed analogue near \(q\), have nonzero temporal first derivatives at the tips.

Assume also that each tip null cone contains a compact middle affine band:

- free of cut/conjugate points;
- contained in a common geodesically regular two-point domain;
- separated from the opposite tip and the joint edge.

## 3. Previously assumed statements that are now derived

Under R2, the repository now derives the thin-null endpoint law.

The compact-containment step is supplied by null index-form coercivity: a compact conjugate-free generator family has a uniform positive Dirichlet Jacobi spectral gap, forcing

[
u=O(a),
qquad
y=O(sqrt a).
]

Combined with Penrose-scaled domain convergence, this gives the endpoint law:

\[
\boxed{
\mathcal V(p,x)
=
c_+(s)a^{3/2}[1+o(1)],
}
\]

\[
\boxed{
\mathcal V(x,q)
=
c_-(s)b^{3/2}[1+o(1)].
}
\]

The proof uses:

- null Fermi coordinates;
- Penrose metric convergence;
- causal-domain convergence;
- dominated convergence for the rescaled volume.

Therefore the old H4 is no longer primitive.

## 4. Joint cap is derived from R2

A regular double-null neighborhood has local metric form

\[
g
=
-2\Omega^2 da\,db
+
h\,ds^2
+
O(a+b).
\]

For nearby comparable points with optical increments \(A,B\) and edge separation \(\xi\),

\[
g(\delta x,\delta x)
=
-2\Omega^2 AB
+
h\xi^2
+
o(AB+\xi^2).
\]

Thus

\[
\boxed{
|\xi|
=
\Theta(\sqrt{AB}).
}
\]

The old H5 is therefore a consequence of the regular transverse double-null geometry in R2.

## 5. Tip middle band is derived from R4

On the regular middle null band, Synge's world function is smooth and satisfies

\[
\sigma(p,z)=0.
\]

For

\[
x=\exp_p h,
\]

the shifted cone is

\[
\sigma(x,z)=0.
\]

The endpoint first variation gives

\[
D_x\sigma(p,z)[h]
=
-\lambda g_p(h,k_z).
\]

The parameter-dependent implicit-function theorem turns this into a transverse swept thickness.

Compactness of normalized future causal directions gives a uniformly positive-measure angular sector with thickness

\[
\ge c\Lambda_p(h).
\]

Hence

\[
\boxed{
\mu(B_x^{\rm mid})
\ge
cR(x).
}
\]

The old middle-band assumption is therefore derived rather than postulated.

## 6. C2 is unnecessary

The original theorem assumed

\[
\Phi\in C^2.
\]

This was used only to write

\[
\Phi(\exp_x h)-\Phi(x)
=
d\Phi_x(h)+O(|h|^2).
\]

For the leading cone-volume asymptotic, the stronger quadratic remainder is unnecessary.

A uniform

\[
o(|h|)
\]

remainder on compact subsets is enough.

That follows from

\[
\Phi\in C^1.
\]

Near the null edge, the proof does not depend on this generic Taylor remainder: it uses the dedicated thin-null endpoint normal forms and their explicit integrable domination.

Therefore the theorem can be weakened to \(C^1\) temporal regularity.

## 7. Relation to volume-time literature

This reduction aligns the theorem more closely with established Lorentzian causality results.

Chruściel, Grant, and Minguzzi prove differentiability for classes of Geroch volume functions and construct \(C^1\) temporal volume functions on globally hyperbolic spacetimes.

García-Heveling proves in 2026 that the unweighted cosmological volume function is \(C^1\) temporal in several geometrically natural settings.

These results do not automatically imply R1 for the exact finite-diamond function \(\Phi\).

They do show that \(C^1\) temporal volume regularity is a natural Lorentzian hypothesis rather than an ad hoc smoothness requirement.

## 8. Reduced theorem dependency chain

Under R1--R3, the repository derives:

### Thin-null endpoint geometry

\[
V_{\rm thin}
\sim
c a^{3/2}.
\]

### Curved degree tail

\[
g_3(q)
=
\Theta(q^{4/3}).
\]

### Joint core

\[
F^{\rm core}_{3,g}(\varepsilon)
=
O(\varepsilon^{10/3}).
\]

### Integrable bulk domination

\[
P_\varepsilon(x)
\le
C\varepsilon^3\kappa(x)^{-3}.
\]

### Small-disagreement law

\[
F_{3,g}(\varepsilon)
\sim
C_{3,g}\varepsilon^3.
\]

### Comparable-ball and internal sparsity

\[
\sup_x\mu(B_t(x))
=
O(t^2),
\]

\[
\sup_{x\in S_t}
\mu(A_x\cap S_t)
=
O(t^2).
\]

### Tip geometry

\[
\bar g_3(r)
=
\Theta(r^3),
\]

and

\[
\mu(B_x^{\rm mid})
\ge
cR(x).
\]

### Graphon primeness

Curvature independent.

### Stochastic assembly

\[
\boxed{
1-p_{3,g}^{\mathrm{UPO}}(n)
\sim
\frac{
K_{3,g}
}{
n
}.
}
\]

## 9. What remains genuinely conditional

The theorem still does not apply automatically to every smooth \(2+1\) causal diamond.

The genuinely nontrivial primitive questions are now:

1. when does the exact finite-diamond function \(\Phi\) satisfy R1?
2. when do all relevant null generators satisfy the regularity in R2?
3. what happens when caustics or cut points violate R2/R3?

These are substantially fewer and more recognizable geometric questions than the original six-hypothesis formulation.

## 10. Recommended theorem statement

A future article should state the curved result using R1--R3 rather than treating the derived asymptotic estimates as assumptions.

This makes the logical content clearer:

\[
\boxed{
\text{regular Lorentzian geometry}
\Longrightarrow
\text{splitter asymptotics}
\Longrightarrow
\text{orientation-recovery law}.
}
\]
