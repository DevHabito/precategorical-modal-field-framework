# Audit: conditional curved 2+1 orientation-recovery theorem

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** adversarial internal audit  
**Target:** D3_CURVED_REGULAR_ORIENTATION_RECOVERY_THEOREM_20261112.md

## 1. Purpose

The curved \(2+1\) theorem is substantially less mature than the flat theorem.

This audit separates:

1. exact identities;
2. consequences that are rigorous under explicitly stated hypotheses;
3. geometric hypotheses that remain nontrivial to verify in a general Lorentzian diamond;
4. proof steps that should be expanded before publication.

The theorem is **conditional**.

It should not be described as a theorem for arbitrary smooth \(2+1\) spacetimes.

## 2. Exact pieces

The following parts are exact and curvature independent.

### Exact disagreement identity

For

\[
x\prec y,
\]

\[
\Delta_g(x,y)
=
\frac{
V(p,y)-V(p,x)
+
V(x,q)-V(y,q)
-
2V(x,y)
}{
V(p,q)
}.
\]

### Degree-disagreement inequality

For every causal-comparability graphon,

\[
|Q(x)-Q(y)|
\le
\Delta(x,y).
\]

### True-twin conditional probability

Conditioned on a pair with disagreement \(\delta\),

\[
\Pr(
\text{sampled true twin}
\mid x,y
)
=
(1-\delta)^{n-2}.
\]

### Graphon primeness mechanism

Under the Lorentzian Alexandrov-interval assumptions of the dedicated primeness theorem, continuum forcing connectivity is curvature independent.

These pieces do not rely on asymptotic expansions.

## 3. Strong geometric hypotheses

The main theorem assumes several facts that are not automatic in every smooth diamond.

### Volume-time differentiability

The theorem assumes

\[
\Phi\in C^2
\]

with timelike differential everywhere.

Current volume-time literature establishes \(C^1\) temporal regularity for important classes, but not this exact finite-diamond \(C^2\) statement in full generality.

Thus H1 is a genuine hypothesis.

### Regular null generators

The theorem excludes:

- conjugate points;
- cut points;
- caustics;
- nonsmooth edge formation.

This is a major restriction.

### Uniform Penrose-Fermi tube

The thin-null theorem assumes that the null-Fermi/Penrose scaling is uniform along every relevant compact generator family.

Pointwise null-Fermi coordinates are not by themselves enough.

Uniformity over the edge is required for the stochastic tail bounds.

### Regular tip first variation

The tip theorem assumes a nondegenerate temporal first variation of the future/past interval volume at the tips.

Again, this is plausible in a regular convex setting but should be verified from an independent Lorentzian volume-variation theorem.

## 4. Audit of the thin-null exponent

The proposed scaling is

\[
u=aU,
\qquad
y^A=\sqrt a\,Y^A,
\qquad
v=V.
\]

The coordinate Jacobian is exactly

\[
a^{d/2}.
\]

The Penrose-Fermi expansion gives smooth convergence of the rescaled metrics on compact subsets to the plane-wave limit.

The repository now contains a dedicated scaled-domain theorem:

PENROSE_SCALED_ALEXANDROV_DOMAIN_CONVERGENCE_20261112.md.

It proves, under the same regular-tube and compact-containment hypotheses, that:

1. points strictly inside the limiting plane-wave interval eventually remain inside the rescaled intervals;
2. points outside the limiting causal diamond eventually remain outside, by cone sandwiching and the Lorentzian limit-curve theorem;
3. the only undecided set is the regular null boundary, which has measure zero;
4. the rescaled volume densities converge uniformly.

Dominated convergence therefore gives

\[
\operatorname{Vol}(I(p,x_a))
=
\mathcal C_\gamma a^{d/2}[1+o(1)].
\]

Thus the scaled-domain convergence gap is closed **within the regular null-tube hypotheses**.

The theorem still does not cover caustic or noncompact scaled-domain regimes.

## 5. Audit of the curved joint-core exponent

Assuming the thin-null endpoint laws and regular double-null cap geometry,

\[
\varepsilon^{10/3}
\]

for the nonlinear \(2+1\) joint core follows by direct power counting:

- four optical variables scale as
  \[
  \lambda^4;
  \]
- tangential cap width scales as
  \[
  \lambda;
  \]
- disagreement scales as
  \[
  \lambda^{3/2}.
  \]

Therefore

\[
\lambda=\varepsilon^{2/3}
\]

and

\[
\lambda^5
=
\varepsilon^{10/3}.
\]

This step is robust **if** the endpoint and cap normal forms are uniform.

No additional hidden curvature power appears in the counting.

## 6. Audit of the matched bulk coefficient

The coefficient

\[
C_{3,g}
=
\frac{
2\pi
}{
3V_D
}
\int_D
\kappa^{-3}\,d\mu
\]

is now supported by an explicit global integrable majorant.

The repository theorem

D3_CURVED_DOMINATED_CONVERGENCE_THEOREM_20261112.md

proves near the edge that

\[
P_\varepsilon(x)
\le
C\varepsilon^3
(ab)^{-3/4}
\asymp
C\varepsilon^3\kappa(x)^{-3}
\]

uniformly across:

- the nonlinear core;
- one-sided transition regions;
- the fully linear joint region.

Since

\[
\kappa^{-3}
\asymp
(ab)^{-3/4}
\]

is integrable, dominated convergence applies directly to the normalized conditional pair volumes.

This removes the earlier need for an informal two-stage matching argument.

The measure-theoretic matching gap is therefore closed under the regular-joint assumptions.

## 7. Audit of low-degree geometry

Under

\[
Q(x)
\asymp
a^{3/2}+b^{3/2},
\]

the tail

\[
g_3(q)=\Theta(q^{4/3})
\]

is immediate.

Under the regular causal-cap law

\[
|\xi|
\lesssim
\sqrt{AB},
\]

the internal-sparsity estimate

\[
\mu(A_x\cap S_t)=O(t^2)
\]

is also a direct volume estimate.

These steps are lower risk than the thin-null and matching theorems.

## 8. Audit of the uniform comparable-ball theorem

The transition estimate uses

\[
L_t(a)^{3/2}
\lesssim
\min\left(
t,
t^{3/2}a^{-3/4}
\right).
\]

This follows from the \(3/2\) endpoint-volume law.

The product bound is algebraically correct and yields \(O(t^2)\).

The remaining issue is again uniformity of constants across the compact edge.

If the thin-null coefficients stay bounded above and below, the comparable-ball proof survives.

## 9. Audit of the tip theorem

The co-degree tail

\[
\bar g_3(r)=\Theta(r^3)
\]

follows from the nonzero temporal first variation

\[
R(\exp_p h)
=
\Lambda_p(h)+O(|h|^2).
\]

The middle-band swept-volume estimate is now derived explicitly in

D3_CURVED_TIP_SYNGE_SHAPE_DERIVATIVE_20261112.md.

On a regular null-cone band, Synge's world function satisfies

\[
\sigma(p,z)=0,
\]

and the shifted cone is

\[
\sigma(\exp_p h,z)=0.
\]

The endpoint first variation gives

\[
D_x\sigma(p,z)[h]
=
-\lambda g_p(h,k_z).
\]

A parameter-dependent implicit-function theorem converts this into a transverse boundary displacement linear in

\[
-g_p(h,k_z).
\]

Compactness of the normalized causal-direction section yields a uniform positive-measure set of null directions on which this displacement is bounded below by a constant times \(\Lambda_p(h)\).

Integrating the resulting tubular thickness proves

\[
\mu(B_x^{\mathrm{mid}})
\ge
cR(x).
\]

Thus the swept-volume gap is closed on every regular affine null band free of cut/conjugate points.

## 10. Audit of stochastic assembly

Once the following are accepted:

\[
F(t)\sim Ct^3,
\]

\[
\sup_x\mu(B_t(x))=O(t^2),
\]

\[
g(q)=\Theta(q^{4/3}),
\]

\[
\mu(A_x\cap S_t)=O(t^2),
\]

\[
\bar g(r)=\Theta(r^3),
\]

and the tip middle-band estimate,

the probabilistic assembly is the same as in the audited flat \(d=3\) proof.

The exponents imply:

- true twins:
  \[
  \Theta(n^{-1});
  \]
- residual escalation:
  \[
  O(n^{-2});
  \]
- larger fixed modules:
  \[
  O(n^{-2});
  \]
- near-whole modules:
  \[
  O(n^{-2});
  \]
- balanced modules:
  superpolynomial.

No new probabilistic obstruction appears solely because the metric is curved.

## 11. Curved component-rate statement

The repository now contains the dedicated proof

D3_CURVED_COMPONENT_STRUCTURE_THEOREM_20261112.md.

It establishes directly from the curved estimates that:

\[
\Pr(
\text{more than one edge-containing component}
)
\to0,
\]

and, after true twins are removed,

\[
\Pr(
\text{component ambiguity}
)
=
O(n^{-2})
+
\exp\!\left(-\frac{n}{2\log n}\right)
+
e^{-\Theta(n)}.
\]

No appeal to the phrase "the flat calculation is the same" remains.

The documentation/proof-expansion gap is closed.

## 12. Literature consistency

The curved program is consistent with known warnings in causal-set literature:

a small-volume Alexandrov interval can be long and skinny and need not be approximately Minkowskian.

The present approach does not assume Minkowski local geometry along the entire interval.

It uses the Penrose plane-wave limit instead.

This is an important conceptual correction.

## 13. Current confidence levels

### High confidence

- exact disagreement identity;
- graphon primeness under the stated Lorentzian assumptions;
- power counting of the joint core once the normal forms hold;
- low-degree and comparable-ball algebra once the endpoint law holds;
- probabilistic UPO assembly once the geometric estimates hold.

### High confidence conditional on the stated regularity hypotheses

- universal thin-null exponent \(a^{d/2}\) in a compact regular null-Fermi tube;
- matched \(2+1\) coefficient formula;
- uniform tip middle-band first variation;
- curved component-rate assembly.

### Still external-review priorities

- whether the regularity hypotheses H1--H6 follow from a simpler standard geometric condition;
- behavior when conjugate points, cut points, or caustics occur;
- whether the finite-diamond volume function is automatically regular enough in useful broad classes;
- independent verification of the Penrose-scaled domain theorem and the Synge swept-volume argument.

## 14. Audit verdict

No contradiction was found in the conditional curved theorem.

The three concrete proof obligations identified in the first audit have now been supplied by independent repository theorems:

1. Penrose-scaled Alexandrov-domain convergence;
2. an explicit integrable dominated-convergence majorant;
3. the Synge-world-function swept-volume proof of the tip middle band.

The dedicated curved component proof has also been added.

The correct current label is therefore:

\[
\boxed{
\text{internally complete conditional theorem under explicit regular-diamond hypotheses.}
}
\]

This is **not** an unconditional theorem for arbitrary curved \(2+1\) spacetimes.

The remaining scientific frontier is no longer an internal proof gap.  It is to weaken or verify the hypotheses, especially in the presence of caustics, cut loci, and degenerate volume-time geometry, and to obtain independent external mathematical review.
