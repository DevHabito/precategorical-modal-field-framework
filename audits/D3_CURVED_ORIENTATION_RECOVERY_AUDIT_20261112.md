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

The Penrose-Fermi expansion makes this the correct candidate exponent.

However, the step

\[
\widehat I_a
\longrightarrow
I_{\mathrm{PW}}
\]

with a positive finite limiting volume still requires a precise domain-convergence argument.

The absence of conjugate points strongly supports nondegeneracy but the repository does not yet contain a full measure-convergence proof.

Therefore the statement

\[
V(p,x_a)
=
\mathcal C_\gamma a^{d/2}[1+o(1)]
\]

should currently be regarded as:

\[
\boxed{
\text{proved modulo uniform scaled-domain convergence in the null-Fermi chart.}
}
\]

This is the most important geometric proof gap in the curved program.

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

The formal coefficient

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

is well motivated.

Near a regular edge,

\[
\kappa^{-3}
\asymp
(ab)^{-3/4},
\]

which is integrable.

The one-side matching integral reproduces the same edge singularity.

What remains to be written more formally is a dominated-convergence theorem controlling:

1. the Taylor remainder of
   \[
   \Delta=d\Phi(h)+O(|h|^2)
   \]
   as \(x\) approaches the edge;
2. the coefficient variation in the optical charts;
3. the passage
   \[
   \varepsilon\to0
   \]
   followed by
   \[
   \eta\to0.
   \]

The repository currently contains the asymptotic matching calculation but not a measure-theoretic theorem with explicit dominating function.

This is a second publication-level proof gap.

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

follows from a nonzero timelike first derivative

\[
R(\exp_p h)
=
\Lambda_p(h)+O(|h|^2).
\]

This is structurally sound under T1.

The middle-band statement is more delicate.

The argument uses:

- first variation of the shifted null cone;
- a positive-measure set of null directions with
  \[
  -g(h,k)\ge c|h|;
  \]
- a regular affine band with intermediate graphon degree.

The compactness argument is plausible, but the repository does not yet derive the null-boundary swept-volume formula from a standard shape-derivative theorem.

Thus the bound

\[
\mu(B_x^{\mathrm{mid}})
\ge
cR(x)
\]

should be treated as conditional on the explicit first-variation hypothesis.

This is the third publication-level geometric gap.

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

The assembled theorem currently states a quantitative curved component ambiguity bound inherited from the flat proof.

The ingredients are sufficient, but the repository should still contain a dedicated curved component proof rather than only the phrase "the same calculation applies."

This is a documentation/proof-expansion gap, not an identified mathematical contradiction.

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

### Medium confidence

- universal thin-null exponent \(a^{d/2}\) under regular null-Fermi tubes;
- matched \(2+1\) coefficient formula.

### Requires dedicated proof before publication

- scaled-domain convergence to the Penrose-limit interval;
- uniform null-boundary shape derivative for the tip middle band;
- explicit curved component-rate proof.

## 14. Audit verdict

No contradiction was found in the conditional curved theorem.

However, it should not yet be promoted to the same status as the flat theorem.

The correct current label is:

\[
\boxed{
\text{conditional curved theorem with three geometric proof obligations remaining.}
}
\]

Those obligations are precise and local.

This is substantial progress: the generic-curvature problem is no longer vague, but it is not yet fully closed.
