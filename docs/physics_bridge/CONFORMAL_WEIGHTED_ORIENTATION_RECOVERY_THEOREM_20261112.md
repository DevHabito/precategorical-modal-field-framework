# Theorem: orientation-recovery robustness under equivalent sprinkling measures and conformal curvature

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic robustness theorem  
**Physical status:** exact extension from uniform flat sprinklings to bounded positive density changes and conformally related Lorentzian metrics  
**Novelty status:** conformal invariance of causal structure is classical; the project-specific statement is robustness of finite stochastic UPO recovery and its error exponents under equivalent measures

## 1. Purpose

The flat Minkowski theorems use two ingredients:

1. the causal-comparability relation;
2. the probability measure used to sprinkle points.

A conformal metric change preserves the first exactly while changing the second.

This note isolates the measure dependence and proves that the qualitative recovery theorem and the leading **error exponent** are stable under every bounded positive reweighting of the sprinkling measure.

The result applies immediately to conformally Minkowskian curved metrics.

## 2. Weighted Minkowski model

Let

\[
D_d
\subset
\mathbb M^d
\]

be the unit flat Alexandrov interval with normalized Minkowski volume measure

\[
\mu.
\]

Let

\[
w:D_d\to(0,\infty)
\]

be measurable and normalized by

\[
\int_{D_d}w\,d\mu=1.
\]

Assume uniform bounds

\[
\boxed{
0<m\le w(x)\le M<\infty
\qquad
\text{for }\mu\text{-a.e. }x.
}
\]

Define the weighted probability measure

\[
d\mu_w(x)
=
w(x)\,d\mu(x).
\]

Sample

\[
X_1,\ldots,X_n
\]

iid from \(\mu_w\), retain the ordinary Minkowski causal-comparability relation, and erase orientation.

Let

\[
p_{d,w}^{\mathrm{UPO}}(n)
\]

be the probability that the resulting comparability graph reconstructs the sampled causal partial order up to global reversal.

## 3. Weighted degree, co-degree, and disagreement

For an event \(x\), write

\[
A_x
=
\{z:z\sim x\}.
\]

Define

\[
Q_w(x)
=
\mu_w(A_x),
\]

\[
R_w(x)
=
1-Q_w(x),
\]

and

\[
\Delta_w(x,y)
=
\mu_w(A_x\triangle A_y).
\]

The density bounds give the pointwise comparisons

\[
\boxed{
mQ(x)
\le
Q_w(x)
\le
MQ(x),
}
\]

\[
\boxed{
mR(x)
\le
R_w(x)
\le
MR(x),
}
\]

and

\[
\boxed{
m\Delta(x,y)
\le
\Delta_w(x,y)
\le
M\Delta(x,y).
}
\]

These inequalities are the basic robustness mechanism.

## 4. Small-disagreement edge tail

Define

\[
F_{d,w}(t)
=
\Pr_{\mu_w^{\otimes2}}
(
X\sim Y,\,
\Delta_w(X,Y)\le t
).
\]

Because

\[
\Delta_w\ge m\Delta,
\]

\[
\{\Delta_w\le t\}
\subseteq
\{\Delta\le t/m\}.
\]

Also

\[
w(x)w(y)\le M^2.
\]

Hence

\[
F_{d,w}(t)
\le
M^2
F_d(t/m).
\]

Conversely,

\[
\Delta\le t/M
\Longrightarrow
\Delta_w\le t,
\]

and

\[
w(x)w(y)\ge m^2,
\]

so

\[
F_{d,w}(t)
\ge
m^2
F_d(t/M).
\]

Therefore

\[
\boxed{
m^2F_d(t/M)
\le
F_{d,w}(t)
\le
M^2F_d(t/m).
}
\]

Since

\[
F_d(t)
=
\Theta(t^{\beta_d}),
\qquad
\beta_d
=
\min\left(
d,\,
2+\frac4d
\right),
\]

we obtain

\[
\boxed{
F_{d,w}(t)
=
\Theta(t^{\beta_d}).
}
\]

Thus the dimension threshold

\[
\beta_2=2,
\qquad
\beta_d>2
\quad(d\ge3)
\]

is invariant under every bounded positive density reweighting.

## 5. Uniform comparable-ball bound

Define

\[
B^w_t(x)
=
\{
z:
z\sim x,\,
\Delta_w(x,z)\le t
\}.
\]

Since

\[
\Delta_w(x,z)\ge m\Delta(x,z),
\]

\[
B^w_t(x)
\subseteq
B_{t/m}(x).
\]

Therefore

\[
\begin{aligned}
\mu_w(B^w_t(x))
&\le
M\mu(B_{t/m}(x))\\
&=
O(t^2),
\end{aligned}
\]

uniformly in \(x\).

Hence

\[
\boxed{
\sup_x
\mu_w(B^w_t(x))
=
O(t^2).
}
\]

The forcing-escalation mechanism survives unchanged at the exponent level.

## 6. Weighted low-degree tail

Let

\[
g_{d,w}(q)
=
\mu_w\{x:Q_w(x)\le q\}.
\]

Because

\[
Q_w(x)\ge mQ(x),
\]

\[
\{Q_w\le q\}
\subseteq
\{Q\le q/m\}.
\]

Therefore

\[
g_{d,w}(q)
\le
M
g_d(q/m)
=
O(q^{4/d}).
\]

Conversely,

\[
Q(x)\le q/M
\Longrightarrow
Q_w(x)\le q,
\]

so

\[
g_{d,w}(q)
\ge
m
g_d(q/M).
\]

Thus

\[
\boxed{
g_{d,w}(q)
=
\Theta(q^{4/d}).
}
\]

The null-joint low-degree exponent is measure-robust.

## 7. Weighted near-universal tail

Define

\[
\bar g_{d,w}(r)
=
\mu_w\{x:R_w(x)\le r\}.
\]

Using

\[
mR(x)\le R_w(x)\le MR(x)
\]

gives

\[
\boxed{
\bar g_{d,w}(r)
=
\Theta(r^d).
}
\]

Thus the timelike-tip co-degree exponent is also unchanged.

## 8. Weighted internal low-degree sparsity

Let

\[
S^w_t
=
\{x:Q_w(x)\le t\}.
\]

If

\[
x\in S^w_t,
\]

then

\[
Q(x)\le t/m.
\]

Likewise,

\[
S^w_t
\subseteq
S_{t/m}.
\]

Hence

\[
\begin{aligned}
\mu_w(
A_x\cap S^w_t
)
&\le
M
\mu(
A_x\cap S_{t/m}
)\\
&=
O(t^2).
\end{aligned}
\]

Therefore

\[
\boxed{
\sup_{x\in S^w_t}
\mu_w(
A_x\cap S^w_t
)
=
O(t^2).
}
\]

This preserves the iterative descent used to exclude near-whole modules.

## 9. Graphon primeness is measure-class invariant

The underlying adjacency kernel

\[
W(x,y)
=
\mathbf1_{\{x\sim y\}}
\]

is unchanged.

Because

\[
m\le w\le M,
\]

the measures

\[
\mu
\quad\text{and}\quad
\mu_w
\]

have exactly the same null sets.

A measurable set is weakly homogeneous under \(\mu_w\) if and only if it is weakly homogeneous under \(\mu\), modulo null sets.

Therefore the Minkowski causal graphon remains prime under the weighted probability space:

\[
\boxed{
W
\text{ has no nontrivial weakly homogeneous set under }\mu_w.
}
\]

The balanced-module exclusion therefore survives.

## 10. Weighted component and module theorems

The flat proofs use only:

- the degree tail;
- the co-degree tail;
- internal low-degree sparsity;
- small-edge tail;
- the uniform comparable-ball estimate;
- graphon primeness;
- standard concentration inequalities.

All of those inputs survive with the same exponents under \(\mu_w\).

Therefore, for every fixed integer

\[
d\ge3,
\]

\[
\boxed{
p_{d,w}^{\mathrm{UPO}}(n)
\to1.
}
\]

The dimension-two case remains critical.

## 11. Weighted reconstruction-error exponents

### d = 3

The weighted small-edge tail satisfies

\[
F_{3,w}(t)
=
\Theta(t^3).
\]

Therefore the comparable true-twin expectation and occurrence probability have scale

\[
\Theta(n^{-1}).
\]

All non-twin mechanisms remain lower order by the same weighted arguments.

Hence

\[
\boxed{
1-p_{3,w}^{\mathrm{UPO}}(n)
=
\Theta(n^{-1}).
}
\]

### d >= 4

For fixed

\[
d\ge4,
\]

\[
F_{d,w}(t)
=
\Theta(
t^{2+4/d}
).
\]

Thus

\[
\boxed{
1-p_{d,w}^{\mathrm{UPO}}(n)
=
\Theta(
n^{-4/d}
).
}
\]

The exact leading coefficient generally depends on the local behavior of \(w\) and is not determined by bounded-density comparison alone.

## 12. Conformal Lorentzian corollary

Let

\[
g
=
\Omega(x)^2\eta
\]

on the same causal diamond \(D_d\), where

\[
\Omega:D_d\to(0,\infty)
\]

is continuous.

On the compact closure of the diamond,

\[
0<\Omega_{\min}
\le
\Omega(x)
\le
\Omega_{\max}
<\infty.
\]

A positive conformal rescaling preserves timelike, causal, and null cones.

Therefore the chronological and causal relations are exactly the Minkowski relations.

The physical volume form transforms as

\[
d\mathrm{Vol}_g
=
\Omega(x)^d
d\mathrm{Vol}_\eta.
\]

After normalization, the sprinkling probability measure is

\[
d\mu_g
=
w_\Omega(x)d\mu_\eta,
\]

with

\[
w_\Omega(x)
=
\frac{
\Omega(x)^d
}{
\int_D\Omega^d\,d\mu_\eta
}.
\]

This density is bounded above and below by positive constants.

The weighted theorem therefore applies exactly.

Hence:

\[
\boxed{
p_{d,g}^{\mathrm{UPO}}(n)
\to1
\qquad
\forall\text{ fixed }d\ge3.
}
\]

Moreover,

\[
\boxed{
1-p_{3,g}^{\mathrm{UPO}}(n)
=
\Theta(n^{-1}),
}
\]

and for

\[
d\ge4,
\]

\[
\boxed{
1-p_{d,g}^{\mathrm{UPO}}(n)
=
\Theta(n^{-4/d}).
}
\]

## 13. Physical meaning

This is the first exact extension of the flat theorem to a genuinely curved metric class.

It includes every compact region whose metric is conformal to Minkowski with a regular positive conformal factor.

The result does not require the curvature to be perturbatively small.

What survives exactly is:

- the recovery limit \(1\) for every fixed \(d\ge3\);
- the dimension threshold;
- the leading error exponent.

What is not yet universal is the leading coefficient.

## 14. Relation to Lorentzian geometry

Conformal invariance of causal structure is classical.

A conformal metric change preserves the causal cones while changing proper time and the volume form.

Modern Lorentzian causality theory emphasizes that the causal cones determine the conformal metric, while the volume form supplies the remaining scale information.

The present theorem uses exactly that split:

\[
\boxed{
\text{causal kernel unchanged}
+
\text{volume measure reweighted}.
}
\]

The project-specific result is that the stochastic UPO reconstruction theorem is stable under this measure change.

## 15. Concrete curved spacetime classes

The conformal theorem is not limited to a formal density perturbation.

It applies to any causally convex Alexandrov interval that is contained in a conformal chart

\[
g=\Omega^2\eta
\]

with

\[
0<\Omega_{\min}\le\Omega\le\Omega_{\max}<\infty.
\]

Important examples include:

### de Sitter spacetime

de Sitter spacetime is conformally flat.

A compact Alexandrov interval contained away from conformal infinity admits a regular positive conformal factor.

Therefore the orientation-recovery theorem and the flat error exponents apply.

### anti-de Sitter local diamonds

Anti-de Sitter spacetime is also conformally flat.

For a compact causally convex diamond contained inside one regular conformal chart and away from the timelike conformal boundary, the same weighted theorem applies.

Global AdS boundary effects are not covered by this local statement.

### FLRW geometries

Friedmann--Lemaître--Robertson--Walker spacetimes are conformally flat.

For a causally convex compact diamond on which the scale factor is finite and positive, the physical volume measure is a smooth positive reweighting of the conformal Minkowski measure.

Hence

\[
p_d^{\mathrm{UPO}}(n)\to1
\]

for fixed \(d\ge3\), with the same recovery-error exponent as in flat spacetime.

The leading coefficient can depend on the scale-factor profile.

### Interpretation

These examples show that nonzero Ricci curvature alone does not destroy the recovery phenomenon.

The first genuinely new obstruction for generic curvature must come from the deformation of causal cones beyond a conformal rescaling, rather than merely from a changed physical volume density.

## 16. Limitation: generic curvature

A generic curved Lorentzian metric is not conformally equivalent to Minkowski on an open set.

Therefore the present theorem does not prove orientation recovery for arbitrary curved spacetimes.

For a generic small causal diamond, both the causal cones and the volume measure receive curvature corrections.

The next problem is to control those simultaneous perturbations.

## 17. Next target

The natural next extension is a small curved Alexandrov interval in a general Lorentzian manifold.

The key question is whether the flat small-disagreement geometry admits a curvature-uniform factorization strong enough to preserve

\[
\beta_d
\]

and the forcing escalation.

The classical small-causal-diamond volume expansion provides the correct starting point, but by itself is not yet sufficient for the rare-event regime.

That obstruction is documented separately.
