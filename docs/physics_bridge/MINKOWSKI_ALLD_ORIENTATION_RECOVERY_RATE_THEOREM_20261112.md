# Theorem: asymptotic error law for arrow-erased Minkowski orientation recovery in every fixed d >= 3

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** assembled quantitative asymptotic theorem for every fixed integer \(d\ge3\)  
**Physical status:** leading reconstruction-error law for the declared flat Minkowski arrow-erasure experiment  
**Novelty status:** targeted literature review did not locate an equivalent Minkowski UPO error law; absolute novelty and priority are not certified

## 1. Main statement

Fix an integer spacetime dimension

\[
d\ge3.
\]

Let

\[
p_d^{\mathrm{UPO}}(n)
\]

be the probability that the arrow-erased comparability graph of an iid size-\(n\) sprinkling into a fixed flat Alexandrov interval reconstructs the causal partial order up to global reversal.

Then

\[
\boxed{
1-p_d^{\mathrm{UPO}}(n)
\sim
\begin{cases}
\dfrac{32\pi}{3}\,n^{-1}, & d=3,\\[8pt]
K_d^{\mathrm{twin}}\,n^{-4/d}, & d\ge4.
\end{cases}
}
\]

For

\[
d\ge4,
\]

the constant is

\[
\boxed{
K_d^{\mathrm{twin}}
=
2^{d-2}
\frac{
d^2(d-1)^2
}{
d-2
}
\frac{
S_{d-3}
}{
S_{d-2}
}
\left[
a_mL_m\Gamma(a_m)
\right]^2,
}
\]

with

\[
m=\frac d2,
\qquad
a_m=1+\frac2d,
\]

and

\[
L_m
=
\frac1{m+1}
\int_0^\infty
\left[
(1+t)^m-t^m
\right]^{-(m+1)/m}
dt.
\]

In every fixed dimension

\[
d\ge3,
\]

comparable true twins are the unique leading orientation-recovery obstruction.

The geometry producing the coefficient changes at \(d=4\):

- \(d=3\): bulk-dominated small-disagreement pairs;
- \(d\ge4\): null-joint-dominated small-disagreement pairs.

## 2. The 2+1 law

For

\[
d=3,
\]

the small-disagreement tail is bulk dominated and has the exact coefficient

\[
\boxed{
F_3(\varepsilon)
\sim
\frac{32\pi}{9}
\varepsilon^3.
}
\]

Laplace-Stieltjes transfer gives

\[
\boxed{
\mathbb E[T_n]
\sim
\frac{32\pi}{3n}.
}
\]

The factorial second moment is \(O(n^{-2})\), so

\[
\Pr(T_n>0)
\sim
\frac{32\pi}{3n}.
\]

All verified non-twin failure mechanisms are \(O(n^{-2})\) or smaller. Therefore

\[
\boxed{
1-p_3^{\mathrm{UPO}}(n)
\sim
\frac{32\pi}{3n}.
}
\]

The dedicated proof is recorded in MINKOWSKI_D3_ORIENTATION_RECOVERY_RATE_THEOREM_20261112.md.

## 3. The 3+1 law

For

\[
d=4,
\]

\[
L_2=\frac13,
\]

and the constant reduces exactly to

\[
K_4^{\mathrm{twin}}
=
9\pi.
\]

Therefore

\[
\boxed{
1-p_4^{\mathrm{UPO}}(n)
\sim
\frac{9\pi}{n}.
}
\]

Equivalently,

\[
\boxed{
p_4^{\mathrm{UPO}}(n)
=
1-\frac{9\pi}{n}
+
o(n^{-1}).
}
\]

This is the sharp first-order reconstruction-error law for the fixed flat \(3+1\) ensemble.

## 4. Lower bound from true-twin occurrence

Let \(T_n\) be the number of comparable true-twin pairs.

The true-twin occurrence theorem proves

\[
\boxed{
\Pr(T_n>0)
\sim
K_d^{\mathrm{twin}}
n^{-4/d}.
}
\]

Except for an exponentially rare degenerate graph in which the only nontrivial component is a single \(K_2\), an adjacent true-twin pair is an orientation-recovery obstruction.

Hence

\[
\boxed{
1-p_d^{\mathrm{UPO}}(n)
\ge
\left(
K_d^{\mathrm{twin}}+o(1)
\right)
n^{-4/d}.
}
\]

It remains to show that every failure not containing a comparable true twin is lower order.

## 5. Quantitative diagonal for macroscopic modules

For every fixed

\[
\varepsilon>0,
\]

the balanced-module theorem gives a positive cut-distance gap

\[
\rho_{d,\varepsilon}>0
\]

between the Minkowski causal graphon and graphons possessing a homogeneous set of measure in

\[
[\varepsilon,1-\varepsilon].
\]

The Second Sampling Lemma gives

\[
\Pr\!\left(
\delta_\square(
G(n,W_d),W_d
)
>
\frac{22}{\sqrt{\log n}}
\right)
\le
\exp\!\left(
-\frac{n}{2\log n}
\right).
\]

Choose a decreasing sequence

\[
\varepsilon_k\downarrow0,
\]

for example

\[
\varepsilon_k=\frac1k.
\]

For each \(k\), choose \(N_k\) sufficiently large that

\[
\frac{22}{\sqrt{\log n}}
<
\rho_{d,\varepsilon_k}
\]

for all

\[
n\ge N_k.
\]

Increase the \(N_k\) so that

\[
N_1<N_2<\cdots.
\]

Define the deterministic diagonal sequence

\[
\varepsilon_n
=
\varepsilon_k
\]

for

\[
N_k\le n<N_{k+1}.
\]

Then

\[
\varepsilon_n\downarrow0
\]

and

\[
\boxed{
\Pr\!\left(
\exists\text{ module }M:
\varepsilon_n n
\le
|M|
\le
(1-\varepsilon_n)n
\right)
\le
\exp\!\left(
-\frac{n}{2\log n}
\right)
}
\]

for all sufficiently large \(n\).

This supplies a quantitative bridge between the fixed-\(\varepsilon\) graphon theorem and the sublinear-complement theorem.

## 6. Residual microscopic forcing failures

Let \(R_n\) count low-disagreement sampled edges that:

- are not true twins;
- have no sampled splitter forcing a new edge with more than twice the disagreement.

The non-twin escalation theorem gives

\[
\boxed{
\Pr(R_n>0)
=
O(
n^{-1-4/d}
)
}
\]

for every fixed

\[
d\ge4.
\]

Outside the events

\[
\{T_n>0\}
\]

and

\[
\{R_n>0\},
\]

every sampled edge reaches the fixed positive-disagreement core by repeated forcing.

## 7. Core edges make every residual obstruction linear

Let

\[
e
\]

be a core edge with

\[
\Delta_d(e)\ge\delta_0.
\]

Its number of sampled splitters is binomial with mean at least

\[
\delta_0(n-2).
\]

Uniform Chernoff concentration over all sampled edges gives, except with probability

\[
e^{-\Theta(n)},
\]

a constant

\[
c_d>0
\]

such that every core edge has at least

\[
c_dn
\]

sampled splitters.

Every graph module containing the edge must contain all of these splitters.

Every connected component containing the edge must also contain all of them.

Therefore, outside the residual microscopic event:

\[
\boxed{
\text{every non-stable module and every edge-containing component has size at least }c_dn.
}
\]

## 8. Multiple components without true twins

If the graph has two edge-containing components and no true twin/residual escalation failure, both components have size at least

\[
c_dn.
\]

Each connected component is a graph module.

Thus one of the components is a balanced module.

The quantitative balanced-module theorem gives

\[
\boxed{
\Pr(
\text{multiple edge-containing components},
\;
T_n=0
)
=
O(n^{-1-4/d})
+
\exp\!\left(
-\frac{n}{2\log n}
\right).
}
\]

This is

\[
o(n^{-4/d}).
\]

## 9. Internal non-stable modules without true twins

Now suppose there is a unique edge-containing component \(C_n\), but it is not UPO.

By the classical connected-UPO criterion, there is a proper non-stable module

\[
M\subsetneq C_n.
\]

Choose an internal edge.

Outside the residual escalation event, its implication class reaches the core while remaining inside \(M\).

Hence

\[
|M|\ge c_dn.
\]

There are two possibilities.

### 9.1 Complement at least epsilon_n n

If

\[
|C_n\setminus M|
\ge
\varepsilon_n n,
\]

then for sufficiently large \(n\),

\[
|M|\ge c_dn\ge\varepsilon_n n.
\]

Thus \(M\) lies in the diagonal balanced range.

Its probability is at most

\[
\exp\!\left(
-\frac{n}{2\log n}
\right).
\]

### 9.2 Complement at most epsilon_n n

If

\[
|C_n\setminus M|
<
\varepsilon_n n,
\]

the complement is sublinear.

The tip-clearance near-whole theorem gives

\[
\boxed{
\Pr(
\text{near-whole module}
)
=
O(n^{1-d})
+
e^{-\Theta(n)}.
}
\]

For every

\[
d\ge4,
\]

\[
n^{1-d}
=
o(n^{-4/d}).
\]

Thus every internal non-twin modular obstruction is lower order.

## 10. Upper bound

Let \(\mathcal F_n\) be the orientation-recovery failure event.

Split according to whether a comparable true twin exists.

Using the preceding estimates,

\[
\begin{aligned}
\Pr(\mathcal F_n)
&\le
\Pr(T_n>0)\\
&\quad+
O(n^{-1-4/d})\\
&\quad+
O(n^{1-d})\\
&\quad+
\exp\!\left(
-\frac{n}{2\log n}
\right)
+
e^{-\Theta(n)}.
\end{aligned}
\]

Every term after \(\Pr(T_n>0)\) is

\[
o(n^{-4/d}).
\]

Therefore

\[
\boxed{
1-p_d^{\mathrm{UPO}}(n)
\le
\left(
K_d^{\mathrm{twin}}+o(1)
\right)
n^{-4/d}.
}
\]

Together with the lower bound,

\[
\boxed{
1-p_d^{\mathrm{UPO}}(n)
\sim
K_d^{\mathrm{twin}}
n^{-4/d}.
}
\]

## 11. Quantitative hierarchy

For fixed \(d\ge4\):

### Leading obstruction

Comparable true twins:

\[
\boxed{
K_d^{\mathrm{twin}}n^{-4/d}.
}
\]

### Residual local forcing failures

\[
O(n^{-1-4/d}).
\]

### Every fixed-size non-twin minimal module

At least

\[
O(n^{-1-4/d}).
\]

### Multiple nontrivial components without a true twin

\[
O(n^{-1-4/d})
+
\text{superpolynomial}.
\]

### Balanced linear modules

\[
\exp\!\left(
-\frac{n}{2\log n}
\right).
\]

### Near-whole modules

\[
O(n^{1-d}).
\]

Thus the asymptotic hierarchy has a unique first level.

## 12. Geometric interpretation of the leading error

For \(d\ge4\), the leading true-twin event is localized near the codimension-two null joint of the Alexandrov interval.

Its continuum small-disagreement tail is

\[
F_d(\varepsilon)
\sim
C_d^{\mathrm{edge}}
\varepsilon^{2+4/d}.
\]

There are

\[
\Theta(n^2)
\]

candidate pairs.

The sampled-twin condition probes the scale

\[
\Delta
\asymp
n^{-1}.
\]

Hence

\[
n^2
n^{-(2+4/d)}
=
n^{-4/d}.
\]

The entire reconstruction-error exponent therefore comes from the null-joint pair geometry.

For \(d=4\), the exact coefficient is

\[
9\pi.
\]

## 13. What the theorem does not say

The theorem quantifies failure of orientation recovery under a declared information-loss experiment.

It does not:

- select one of the two global time orientations;
- reconstruct proper time;
- reconstruct metric scale;
- prove the causal-set hypothesis physically;
- extend automatically to curved spacetimes;
- remove dependence on the finite Alexandrov-window geometry.

The result is a sharp probabilistic statement inside the stated model.

## 14. Literature boundary

The proof combines classical comparability/UPO theory, graphon sampling, weakly homogeneous sets, and standard concentration inequalities with project-specific Lorentzian estimates.

The Second Sampling Lemma used in the balanced-module rate is standard graphon theory, appearing as Lemma 10.16 in Lovász's *Large Networks and Graph Limits* and based on work of Borgs, Chayes, Lovász, Sós, and Vesztergombi.

A targeted search did not locate a prior theorem giving the asymptotic orientation-recovery error

\[
K_d n^{-4/d}
\]

for arrow-erased Minkowski sprinklings.

This remains limited negative evidence.

Absolute novelty and priority are not certified.

## 15. Next frontier

The flat fixed-window asymptotic recovery probability is now known to first order for every fixed

\[
d\ge3.
\]

The next quantitative questions are:

1. derive the second-order correction for \(d=3\) and \(d=4\);
2. determine whether the first residual non-twin term has a computable constant;
3. replace the Alexandrov interval with other windows;
4. perturb the bulk and null-joint calculations under weak curvature;
5. determine which parts of the leading coefficient are boundary-universal and which depend on the chosen finite window.

The leading flat-space error law itself is closed under the current assumptions.
