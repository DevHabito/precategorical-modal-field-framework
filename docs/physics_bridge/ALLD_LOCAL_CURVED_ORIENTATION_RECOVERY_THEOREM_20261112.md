# Theorem: local curved orientation recovery at strongly causal points in every fixed d >= 3

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** local analytic theorem  
**Physical status:** local curved-spacetime orientation-recovery law around every strongly causal point  
**Novelty status:** the local Lorentzian-geometric ingredients are classical; the stochastic arrow-erasure conclusion is project-specific

## 1. Statement

Let

\[
(M^d,g)
\]

be a smooth time-oriented Lorentzian spacetime with fixed integer

\[
d\ge3.
\]

Let

\[
o\in M
\]

be a strongly causal point and let

\[
T\in T_oM
\]

be a future-directed unit timelike vector.

For sufficiently small

\[
L>0,
\]

define

\[
p_L=\exp_o(-LT),
\qquad
q_L=\exp_o(LT),
\]

and

\[
D_L=I(p_L,q_L).
\]

Then there exists

\[
L_0>0
\]

such that for every fixed

\[
0<L<L_0,
\]

the arrow-erased comparability graph of \(n\) iid physical-volume samples from \(D_L\) satisfies

\[
\boxed{
p_{d,g,L}^{\mathrm{UPO}}(n)
\to1
}
\]

as

\[
n\to\infty.
\]

More sharply,

\[
\boxed{
1-p_{d,g,L}^{\mathrm{UPO}}(n)
\sim
K_{d,g}(D_L)
n^{2-\beta_d},
}
\]

where

\[
\boxed{
\beta_d
=
\begin{cases}
3,&d=3,\\[4pt]
2+\dfrac4d,&d\ge4.
\end{cases}
}
\]

Thus

\[
\boxed{
1-p_{3,g,L}^{\mathrm{UPO}}(n)
\sim
\frac{
K_{3,g}(D_L)
}{
n
},
}
\]

and for every fixed

\[
d\ge4,
\]

\[
\boxed{
1-p_{d,g,L}^{\mathrm{UPO}}(n)
\sim
K_{d,g}(D_L)
n^{-4/d}.
}
\]

## 2. Order of limits

The order is:

1. choose a fixed sufficiently small physical diamond \(D_L\);
2. let \(n\to\infty\).

No simultaneous limit

\[
L=L_n\to0
\]

is required.

The tangent-space limit

\[
L\to0
\]

is a separate statement about the coefficient.

## 3. Local causally convex convex-normal neighborhood

Strong causality at \(o\) provides arbitrarily small causally convex neighborhoods.

Smooth Lorentzian geometry provides arbitrarily small convex normal neighborhoods.

Choose a relatively compact neighborhood

\[
U\ni o
\]

that is both:

- causally convex in the ambient spacetime;
- convex normal.

For sufficiently small \(L\),

\[
\overline{D_L}\subset U.
\]

Therefore every causal relation between points of \(D_L\) is represented entirely inside the regular local geometry of \(U\).

## 4. No cuts or conjugate points

Because \(U\) is convex normal:

- every two points in \(U\) are joined by a unique geodesic in \(U\);
- the exponential maps are nonsingular on the relevant star domains;
- the null generators forming the boundary of \(D_L\) encounter no cut or conjugate point before leaving the local domain.

Thus all null generator families required by the regular curved theorem are geodesically regular.

## 5. Smooth transverse codimension-two edge

The two null boundary sheets are locally

\[
\sigma(p_L,x)=0
\]

and

\[
\sigma(x,q_L)=0,
\]

where \(\sigma\) is Synge's world function.

At an intersection point, their differentials are the null covectors tangent to the unique null generators from \(p_L\) and toward \(q_L\).

If these covectors were linearly dependent, the two generators would form one null geodesic from \(p_L\) to \(q_L\).

But

\[
p_L\ll q_L.
\]

Therefore the two null sheets meet transversely.

Their intersection is a smooth compact spacelike codimension-two edge

\[
E_L.
\]

## 6. Uniform null-Fermi tubes

The generator families from the tips to the compact edge are compact.

They are free of cuts and conjugate points.

Null-Fermi tubes therefore exist around every generator.

Compactness gives:

- a finite tube subcover;
- uniform bounds on metric coefficients;
- uniform Jacobi-field bounds;
- uniform Penrose-Fermi expansions.

Thus the regular thin-null geometry is automatic.

## 7. Penrose-scaled compact containment

Inside the uniform null-Fermi tubes, the metric cones are uniformly sandwiched between nearby model cone structures.

For a thin-null endpoint of optical depth \(a\):

- longitudinal inward displacement is \(O(a)\);
- transverse causal width is \(O(\sqrt a)\);
- affine position along the generator stays in a fixed compact interval.

Therefore after

\[
u=aU,
\qquad
y^A=\sqrt a\,Y^A,
\qquad
v=V,
\]

the rescaled Alexandrov intervals remain in one fixed compact coordinate set.

The limiting endpoints are timelike related in the Penrose plane-wave metric.

Hence the Penrose-scaled domain-convergence theorem applies automatically.

## 8. Thin-null endpoint laws

Therefore, uniformly along the edge,

\[
\boxed{
V(p_L,x)
=
c_+(s)a^{d/2}
[1+o(1)],
}
\]

and

\[
\boxed{
V(x,q_L)
=
c_-(s)b^{d/2}
[1+o(1)],
}
\]

with positive bounded coefficients.

## 9. Double-null cap law

Transversality supplies a regular double-null neighborhood

\[
(a,b,s^A)
\]

of the edge.

The metric has leading form

\[
g
=
-2\Omega^2 da\,db
+
h_{AB}ds^Ads^B
+
O(a+b).
\]

For nearby comparable pairs,

\[
h_{AB}\xi^A\xi^B
\lesssim
AB.
\]

Hence the tangential cap has volume

\[
\Theta(
(AB)^{(d-2)/2}
).
\]

Thus the regular curved joint theorem applies.

## 10. Finite-diamond volume-time regularity

Define

\[
\tau_-(x)
=
V(p_L,x),
\]

\[
\tau_+(x)
=
V(x,q_L).
\]

The convex-diamond volume-time theorem gives

\[
\tau_\pm\in C^1(D_L),
\]

with:

\[
\nabla\tau_-
\]

past-directed timelike and

\[
\nabla\tau_+
\]

future-directed timelike.

Therefore

\[
\boxed{
\Phi_L(x)
=
\frac{
\tau_-(x)-\tau_+(x)
}{
V(D_L)
}
}
\]

is \(C^1\) temporal.

No independent bulk nondegeneracy assumption remains.

## 11. Regular tips

At \(p_L\), the first variation of

\[
x\mapsto V(x,q_L)
\]

is a nonzero temporal covector by the same null-boundary volume variation formula.

The time-reversed result holds at \(q_L\).

Choose compact affine bands on the two tip null cones separated from:

- the tips;
- the joint edge.

No cuts or conjugate points occur in \(U\).

The degree function is continuous and lies strictly between zero and one on those bands.

Therefore the all-dimensional Synge middle-band theorem applies.

Thus the tip hypotheses are automatic.

## 12. Small-disagreement law

The local regular geometry now supplies the all-dimensional curved small-edge law

\[
\boxed{
F_{d,g,L}(\varepsilon)
\sim
C_{d,g}(D_L)
\varepsilon^{\beta_d}.
}
\]

### d = 3

\[
C_{3,g}(D_L)
=
\frac{
2\pi
}{
3V(D_L)
}
\int_{D_L}
\left[
-g^{-1}(d\Phi_L,d\Phi_L)
\right]^{-3/2}
d\mu_L.
\]

### d >= 4

\[
C_{d,g}(D_L)
=
2
\int_{E_L}
\mathcal A_d(s)
\mathcal S_d(s)
\,dA_{E_L}(s),
\]

with the local edge factors defined by the regular curved joint theorem.

## 13. Low-degree and tip exponents

The same local geometry gives

\[
\boxed{
g_{d,g,L}(q)
=
\Theta(q^{4/d}),
}
\]

\[
\boxed{
\sup_{x\in S_t}
\mu(A_x\cap S_t)
=
O(t^2),
}
\]

\[
\boxed{
\sup_x
\mu(B_t(x))
=
O(t^2),
}
\]

and

\[
\boxed{
\bar g_{d,g,L}(r)
=
\Theta(r^d).
}
\]

The middle-band estimate gives

\[
\mu(B_x^{\rm mid})
\ge
cR(x).
\]

## 14. Graphon primeness

The causal-comparability graphon of a Lorentzian Alexandrov interval is prime independently of flatness.

Thus balanced modules are superpolynomially rare in the finite iid sample.

## 15. True twins

Let \(T_n\) be the comparable true-twin count.

The exact first-moment identity and the small-edge tail give

\[
\boxed{
\mathbb E[T_n]
\sim
K_{d,g}(D_L)
n^{2-\beta_d},
}
\]

where

\[
\boxed{
K_{d,g}(D_L)
=
\frac12
C_{d,g}(D_L)
\Gamma(\beta_d+1).
}
\]

The uniform \(O(t^2)\) comparable-ball theorem gives a factorial second moment lower order than the mean.

Hence

\[
\boxed{
\Pr(T_n>0)
\sim
K_{d,g}(D_L)
n^{2-\beta_d}.
}
\]

## 16. All other failure modes are subleading

The local theorem chain gives:

### Non-twin escalation failure

\[
O(
n^{1-\beta_d}
).
\]

### Multiple edge-containing components without twins

\[
O(
n^{1-\beta_d}
)
+
\text{superpolynomial}.
\]

### Balanced modules

superpolynomially small.

### Near-whole modules

\[
O(n^{1-d}).
\]

Every one is

\[
o(
n^{2-\beta_d}
).
\]

Therefore true twins are the unique leading orientation-recovery obstruction.

## 17. Main conclusion

\[
\boxed{
1-p_{d,g,L}^{\mathrm{UPO}}(n)
\sim
K_{d,g}(D_L)
n^{2-\beta_d}.
}
\]

This is a local curved-spacetime theorem at every strongly causal point.

## 18. Tangent-space coefficient limit

Rescale the small diamond \(D_L\) to fixed unit size.

As

\[
L\to0,
\]

the rescaled metric converges smoothly to the Minkowski tangent metric.

All local geometric coefficients in the formulas above converge to their flat values.

Therefore

\[
\boxed{
K_{d,g}(D_L)
\longrightarrow
K_d^{\rm Mink}
}
\]

as

\[
L\downarrow0.
\]

In particular,

\[
d=3:
\qquad
K_{3,g}(D_L)
\to
\frac{32\pi}{3},
\]

and

\[
d=4:
\qquad
K_{4,g}(D_L)
\to
9\pi.
\]

For \(d>4\), the limit is the previously derived flat constant \(K_d^{\rm twin}\).

## 19. Scope

The theorem is local at strongly causal points.

It includes every point of a globally hyperbolic spacetime.

It does not apply at points where strong causality fails.

It also does not imply that a large causal diamond crossing caustics or cut loci obeys the same law.

## 20. Scientific consequence

For every fixed

\[
d\ge3,
\]

asymptotic recoverability of causal orientation from symmetric comparability is a **local Lorentzian property**, not a peculiarity of Minkowski space:

\[
\boxed{
\text{small regular curved diamond}
\Longrightarrow
1-p^{\rm UPO}
\sim
K(D)n^{2-\beta_d}.
}
\]

The exponent is universal.

The coefficient carries local and finite-diamond geometry.
