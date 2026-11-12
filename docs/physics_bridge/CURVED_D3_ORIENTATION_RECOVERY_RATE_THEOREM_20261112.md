# Theorem: leading causal-orientation recovery error in a regular curved 2+1 Lorentzian diamond

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** assembled analytic asymptotic theorem under the regular curved \(2+1\) hypotheses
**Physical status:** first-order reconstruction-error law for a genuinely curved causal diamond
**Novelty status:** targeted literature review did not locate an equivalent finite-sprinkling arrow-erasure error law in curved Lorentzian geometry; absolute priority is not certified

## 1. Model

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval in a smooth time-oriented \(2+1\)-dimensional Lorentzian spacetime.

Sample

\[
X_1,\ldots,X_n
\]

iid from normalized physical spacetime volume on \(D\).

Form the induced causal partial order, erase every causal arrow, and retain only symmetric timelike comparability.

Let

\[
p_{3,g}^{\mathrm{UPO}}(n)
\]

be the probability that the sampled causal order is recoverable from the resulting comparability graph up to one global reversal.

## 2. Geometric hypotheses

Assume the regular curved recovery package:

### H1. Regular joint

The null boundaries of \(I^+(p)\) and \(I^-(q)\) meet transversely in a compact smooth spacelike joint, before the relevant cut/conjugate loci.

### H2. Uniform regular Penrose tubes

The compact families of null generators reaching the joint admit uniform Penrose/null-Fermi control, so the volume-null coordinates

\[
a=\mathcal V(p,\cdot)^{2/3},
\qquad
b=\mathcal V(\cdot,q)^{2/3}
\]

are regular and satisfy the curved causal-cap estimate.

### H3. Temporal volume-time gradient and bulk regularity

The finite-diamond volume function

\[
\Phi(x)
=
\mathcal V(p,x)
-
\mathcal V(x,q)
\]

is \(C^2\) away from the joint, with timelike differential.

On every compact exhaustion separated from the joint, the first-order expansion

\[
\Delta_g(x,\exp_x h)
=
d\Phi_x(h)
+
O(|h|^2)
\]

has a uniform remainder bound, and the corresponding local cone-volume asymptotic is dominated by an integrable majorant as the exhaustion approaches the joint and the regular boundary charts.

Define

\[
\kappa(x)
=
\sqrt{
-g^{-1}(d\Phi,d\Phi)
}.
\]

Assume

\[
\kappa^{-3}\in L^1(D,\mu).
\]

Equivalently, H3 includes the compact-exhaustion/dominated-convergence hypothesis used in the curved small-edge theorem; it is not inferred from pointwise timelikeness alone.

### H4. Regular tips

The co-degree function has nonzero timelike first derivative at the two timelike tips.

### H5. Regular noncaustic tip cones

The null cone segments from each timelike tip to the joint have unique smooth generators and no cut/conjugate degeneration, so the curved tip middle-band theorem applies.

No probabilistic or UPO conclusion is contained in H1--H5.

## 3. Curved small-edge coefficient

The curved bulk volume-time theorem and regular-joint suppression give

\[
\boxed{
F_{3,g}(\varepsilon)
:=
\Pr(
X\sim Y,\,
\Delta_g(X,Y)\le\varepsilon
)
\sim
C_g\varepsilon^3,
}
\]

where

\[
\boxed{
C_g
=
\frac{
2\pi
}{
3V_D
}
\int_D
\kappa(x)^{-3}
\,d\mu(x).
}
\]

Here

\[
V_D
=
\operatorname{Vol}_g(D).
\]

The coefficient is finite and positive by hypothesis.

## 4. True-twin first moment

Let \(T_n\) be the number of adjacent true-twin pairs.

Conditioned on a comparable pair with disagreement \(\delta\), the pair is a sampled true-twin pair exactly when all remaining \(n-2\) points avoid the splitter region.

Thus

\[
\mathbb E[T_n]
=
\binom n2
\int_0^1
(1-\delta)^{n-2}
\,dF_{3,g}(\delta).
\]

Using

\[
F_{3,g}(\delta)
\sim
C_g\delta^3,
\]

Laplace-Stieltjes transfer gives

\[
\begin{aligned}
\mathbb E[T_n]
&\sim
\frac12
C_g
\Gamma(4)
n^{-1}\\
&=
\boxed{
\frac{3C_g}{n}.
}
\end{aligned}
\]

Equivalently,

\[
\boxed{
\mathbb E[T_n]
\sim
\frac{
2\pi
}{
V_D
}
\left(
\int_D
\kappa(x)^{-3}
\,d\mu(x)
\right)
\frac1n.
}
\]

## 5. True-twin second moment

It remains to show that the true-twin count is not clustered strongly enough to change the occurrence probability.

### 5.1 Disjoint twin pairs

For two disjoint candidate pairs with disagreements \(\delta_1,\delta_2\), simultaneous true-twin survival requires the remaining sample to avoid the union of the two splitter regions.

This gives an upper bound

\[
e^{-cn\max(\delta_1,\delta_2)}.
\]

Because the two continuum pairs are independent before cross-pair constraints,

\[
\Pr(
\max(\delta_1,\delta_2)\le t
)
\le
F_{3,g}(t)^2
=
O(t^6).
\]

Therefore the disjoint contribution to the factorial second moment is

\[
O(
n^4 n^{-6}
)
=
\boxed{
O(n^{-2}).
}
\]

### 5.2 Overlapping twin pairs

Suppose the two candidate pairs share one vertex.

If their three-way splitter volume is at most \(t\), then:

1. the first comparable pair has disagreement at most \(t\), costing
   \[
   O(t^3);
   \]
2. the third point must lie in a comparable-disagreement ball of radius \(t\).

The curved uniform comparable-ball theorem gives ball mass

\[
O(t^2).
\]

Thus the three-point tail is

\[
O(t^5),
\]

and the overlapping factorial-moment contribution is

\[
O(
n^3n^{-5}
)
=
\boxed{
O(n^{-2}).
}
\]

Hence

\[
\boxed{
\mathbb E[
T_n(T_n-1)
]
=
O(n^{-2})
=
o(n^{-1}).
}
\]

## 6. True-twin occurrence

For a nonnegative integer-valued variable,

\[
\mathbb E[T_n]
-
\mathbb E\binom{T_n}{2}
\le
\Pr(T_n>0)
\le
\mathbb E[T_n].
\]

Therefore

\[
\boxed{
\Pr(T_n>0)
\sim
\frac{3C_g}{n}.
}
\]

An adjacent true-twin pair is a non-stable size-two module unless the graph is in the exponentially rare degenerate case in which the unique edge-containing component is only that \(K_2\).

Hence

\[
\boxed{
1-p_{3,g}^{\mathrm{UPO}}(n)
\ge
\frac{3C_g+o(1)}{n}.
}
\]

## 7. Non-twin residual escalation is second order

The curved edge tail

\[
F_{3,g}(t)=O(t^3)
\]

and the curved comparable-ball estimate

\[
\sup_x\mu(B_t(x))=O(t^2)
\]

give the constant-factor residual escalation bound

\[
\boxed{
\Pr(R_n>0)
=
O(n^{-2}),
}
\]

where \(R_n\) counts low-disagreement edges that have sampled splitters but no sampled splitter forcing a factor-two increase in disagreement.

Outside

\[
\{T_n>0\}\cup\{R_n>0\},
\]

every sampled edge reaches a fixed positive-disagreement core by repeated forcing.

## 8. Core edges force linear modules and components

Let the core threshold be

\[
\Delta_g(e)\ge\delta_0>0.
\]

The sampled splitter count of a core edge is binomial with mean at least

\[
\delta_0(n-2).
\]

Uniform Chernoff concentration over all sampled edges gives a constant \(c_0>0\) such that, except with probability \(e^{-\Theta(n)}\),

\[
\boxed{
\text{every core edge has at least }c_0n\text{ sampled splitters}.
}
\]

Consequences:

1. every module containing a core edge has at least \(c_0n\) vertices;
2. every connected component containing a core edge has at least \(c_0n\) vertices.

Therefore, outside true twins and residual escalation, every UPO obstruction is macroscopic on at least one side.

## 9. Multiple components without twins are second order

The curved non-twin component-rate theorem gives

\[
\boxed{
\Pr(
\text{at least two edge-containing components},
\;
T_n=0
)
=
O(n^{-2})
+
\exp\!\left(
-\frac{n}{2\log n}
\right)
+
e^{-\Theta(n)}.
}
\]

Thus component ambiguity is \(o(n^{-1})\).

## 10. Balanced internal modules are superpolynomially rare

The Lorentzian causal graphon is prime.

For every fixed \(\varepsilon>0\), the class of graphons possessing a homogeneous set of measure in

\[
[\varepsilon,1-\varepsilon]
\]

has positive cut-distance separation from the causal graphon.

The Second Sampling Lemma therefore gives

\[
\boxed{
\Pr(
\exists\ \varepsilon\text{-balanced module}
)
\le
\exp\!\left(
-\frac{n}{2\log n}
\right)
}
\]

for sufficiently large \(n\).

A standard diagonal construction gives a deterministic sequence

\[
\varepsilon_n\downarrow0
\]

so slowly that modules with both sides at least

\[
\varepsilon_n n
\]

still obey the same superpolynomial upper bound.

## 11. Near-whole modules are second order

Work after excluding multiple edge-containing components.

A near-whole proper module requires a sampled outside vertex complete to the module.

The curved tip middle-band theorem gives, for every near-universal tip candidate \(x\), a nonneighbor region

\[
B_x^{\mathrm{mid}}
\]

with

\[
\mu(B_x^{\mathrm{mid}})
\ge
c_0R(x),
\]

where every point in that region has continuum degree in a fixed interval

\[
[q_-,q_+]
\subset(0,1).
\]

Such an intermediate-degree sampled point cannot have either module-compatible external type relative to an \(n-o(n)\) module, except with probability \(e^{-\Theta(n)}\).

Therefore a near-whole module requires a tip-clear candidate.

The curved co-degree tail is

\[
\bar g_3(r)=O(r^3).
\]

Hence the expected number of tip-clear candidates is

\[
n
\int
e^{-cnr}
\,d\bar g_3(r)
=
O(n^{-2}).
\]

Thus

\[
\boxed{
\Pr(
\text{near-whole proper non-stable module}
)
=
O(n^{-2})
+
e^{-\Theta(n)}.
}
\]

## 12. Exhaustion of non-twin failure modes

Let \(\mathcal F_n\) be the event that orientation recovery fails.

On

\[
T_n=0,
\]

a failure can occur only through:

1. residual local escalation failure;
2. multiple edge-containing components;
3. a balanced internal non-stable module;
4. a near-whole internal non-stable module;
5. an exponentially rare core-splitter concentration failure;
6. an exponentially rare empty/degenerate graph event.

The preceding sections give

\[
\boxed{
\Pr(
\mathcal F_n,\,
T_n=0
)
=
O(n^{-2})
+
\exp\!\left(
-\frac{n}{2\log n}
\right)
+
e^{-\Theta(n)}.
}
\]

Therefore

\[
\boxed{
\Pr(
\mathcal F_n,\,
T_n=0
)
=
o(n^{-1}).
}
\]

## 13. Main error law

Combining the true-twin lower bound and the non-twin upper bound,

\[
\boxed{
1-p_{3,g}^{\mathrm{UPO}}(n)
\sim
\frac{3C_g}{n}.
}
\]

Substituting the geometric coefficient,

\[
\boxed{
1-p_{3,g}^{\mathrm{UPO}}(n)
\sim
\frac{
2\pi
}{
V_D
}
\left(
\int_D
\left[
-g^{-1}(d\Phi,d\Phi)
\right]^{-3/2}
\,d\mu
\right)
\frac1n.
}
\]

Equivalently,

\[
\boxed{
p_{3,g}^{\mathrm{UPO}}(n)
=
1
-
\frac{
2\pi
}{
V_D
}
\left(
\int_D
\left[
-g^{-1}(d\Phi,d\Phi)
\right]^{-3/2}
\,d\mu
\right)
\frac1n
+
o(n^{-1}).
}
\]

## 14. Flat check

For the unit flat \(2+1\) Minkowski diamond,

\[
V_D
=
\frac{2\pi}{3},
\]

and

\[
\int_D
\kappa^{-3}
\,d\mu
=
\frac{32\pi}{9}.
\]

Therefore

\[
\frac{
2\pi
}{
V_D
}
\int_D
\kappa^{-3}
\,d\mu
=
\frac{32\pi}{3}.
\]

The curved formula reduces exactly to

\[
\boxed{
p_3^{\mathrm{UPO}}(n)
=
1-\frac{32\pi}{3n}+o(n^{-1}).
}
\]

## 15. Interpretation

The leading orientation-recovery error in a regular curved \(2+1\) diamond is governed by a geometric functional of the finite-diamond volume-time function:

\[
\boxed{
\mathcal K(D,g)
=
\frac{
2\pi
}{
V_D
}
\int_D
\left[
-g^{-1}(d\Phi,d\Phi)
\right]^{-3/2}
\,d\mu.
}
\]

Then

\[
\boxed{
1-p_{3,g}^{\mathrm{UPO}}(n)
\sim
\frac{\mathcal K(D,g)}{n}.
}
\]

The exponent \(1\) is universal over the stated regular class.

The coefficient contains the curved geometry.

## 16. What this theorem does not claim

The theorem is not a statement for every smooth \(2+1\) spacetime.

It requires H1--H5.

It does not cover:

- caustic null boundaries;
- cut-locus branching;
- nonsmooth joints;
- degenerate volume-time gradients;
- divergent \(\kappa^{-3}\);
- degenerate tip gradients.

It also does not select one of the two global time orientations.

## 17. Current scientific frontier

The first-order regular-curved \(2+1\) recovery problem is closed under H1--H5.

The next useful questions are:

1. verify H1--H5 in explicit nonconformally-flat metrics with nonzero Cotton tensor;
2. prove openness of H1--H5 under small generic metric perturbations of a regular diamond;
3. determine whether the geometric coefficient \(\mathcal K(D,g)\) has an invariant expansion in curvature;
4. extend the curved null-joint analysis to \(3+1\), where the joint is leading rather than subleading.
