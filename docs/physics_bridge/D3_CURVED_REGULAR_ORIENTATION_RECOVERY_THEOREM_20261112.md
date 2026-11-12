# Theorem: conditional orientation-recovery law for regular curved 2+1 causal diamonds

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** assembled conditional analytic theorem under explicit regular-diamond hypotheses  
**Physical status:** first generic non-conformally-flat curved extension of the arrow-erasure recovery law in \(2+1\), conditional on regularity assumptions  
**Novelty status:** targeted literature review did not locate an equivalent finite stochastic UPO theorem for curved Lorentzian diamonds; absolute novelty and priority are not certified

## 1. Setting

Let

\[
D=I(p,q)
\]

be a compact causally convex Alexandrov interval in a smooth \(2+1\)-dimensional time-oriented Lorentzian spacetime.

Condition on cardinality \(n\) and sample

\[
X_1,\ldots,X_n
\]

iid from normalized physical volume

\[
d\mu
=
\frac{d\operatorname{Vol}_g}{V_D},
\qquad
V_D=\operatorname{Vol}_g(D).
\]

Let \(P_{g,n}\) be the induced chronological partial order.

Erase every arrow and retain only symmetric causal comparability.

Let

\[
G_{g,n}
\]

be the resulting comparability graph.

Let

\[
p_{3,g}^{\mathrm{UPO}}(n)
\]

be the probability that the original sampled partial order is reconstructible from \(G_{g,n}\) up to global reversal.

## 2. Regular-diamond hypotheses

Assume the following geometric conditions.

### H1. Temporal volume function

The finite-diamond volume-difference function

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

is \(C^2\) in the interior and has timelike differential everywhere.

Define

\[
\kappa(x)
=
\sqrt{
-g^{-1}(d\Phi_x,d\Phi_x)
}.
\]

### H2. Regular null edge

The future null boundary of \(p\) and past null boundary of \(q\) meet transversely along a compact smooth spacelike edge \(E\).

### H3. No relevant null caustics

The null generators from the tips to the edge contain no conjugate points or cut points in the relevant segments and admit uniform null-Fermi tubes.

### H4. Regular thin-null law

The endpoint interval volumes satisfy, uniformly in optical coordinates near the edge,

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

with positive bounded coefficients.

### H5. Regular joint pair cap

Nearby comparable pairs satisfy the tangential cap law

\[
|\xi|
=
\Theta(\sqrt{AB})
\]

in double-null joint coordinates.

### H6. Regular tips

The future-volume derivative at \(p\) and the time-reversed past-volume derivative at \(q\) are nonzero temporal covectors.

The null cones from the tips admit regular middle affine bands free of conjugate/cut points, with graphon degree bounded away from both zero and one.

These are precisely the hypotheses used in the curved tip theorem.

## 3. Main statement

Under H1--H6,

\[
\boxed{
p_{3,g}^{\mathrm{UPO}}(n)
\longrightarrow
1.
}
\]

More sharply,

\[
\boxed{
1-p_{3,g}^{\mathrm{UPO}}(n)
\sim
\frac{
K_{3,g}
}{
n
},
}
\]

where

\[
\boxed{
K_{3,g}
=
\frac{
2\pi
}{
V_D
}
\int_D
\kappa(x)^{-3}
\,d\mu(x).
}
\]

The integral is finite under the regular-joint hypotheses.

Comparable true twins are the unique leading obstruction.

## 4. Curved small-disagreement tail

The matched curved disagreement theorem gives

\[
\boxed{
F_{3,g}(\varepsilon)
=
\Pr(
X\sim Y,\,
\Delta_g(X,Y)\le\varepsilon
)
\sim
C_{3,g}\varepsilon^3,
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
\kappa(x)^{-3}
\,d\mu(x).
}
\]

The regular null-joint core contributes only

\[
O(\varepsilon^{10/3}),
\]

so the leading coefficient is bulk controlled.

## 5. True-twin first moment

Let \(T_n\) count comparable true-twin pairs.

Conditioned on a pair with disagreement \(\delta\), the pair is a sampled true twin exactly when the remaining \(n-2\) points avoid the splitter region.

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
C_{3,g}\delta^3,
\]

Laplace-Stieltjes transfer gives

\[
\boxed{
\mathbb E[T_n]
\sim
3C_{3,g}n^{-1}
=
K_{3,g}n^{-1}.
}
\]

## 6. True-twin occurrence probability

The curved comparable-ball theorem gives

\[
\sup_x
\mu
\{
z:z\sim x,\,
\Delta(x,z)\le t
\}
=
O(t^2).
\]

For two disjoint candidate twin pairs, the factorial second-moment contribution is

\[
O(n^{-2}).
\]

For overlapping candidate pairs:

- the first pair costs
  \[
  O(t^3);
  \]
- the third point lies in a comparable metric ball of mass
  \[
  O(t^2).
  \]

Hence the three-point tail is

\[
O(t^5),
\]

and the overlapping factorial contribution is also

\[
O(n^{-2}).
\]

Therefore

\[
\boxed{
\mathbb E[T_n(T_n-1)]
=
O(n^{-2})
=
o(n^{-1}).
}
\]

Thus

\[
\boxed{
\Pr(T_n>0)
\sim
K_{3,g}n^{-1}.
}
\]

## 7. Curved low-degree geometry

The regular curved edge theorem gives

\[
\boxed{
g_3(q)
=
\mu\{Q\le q\}
=
\Theta(q^{4/3}).
}
\]

It also gives internal low-degree sparsity:

\[
\boxed{
\sup_{x\in S_t}
\mu(A_x\cap S_t)
=
O(t^2).
}
\]

These are the exact exponents used by the flat component argument.

## 8. Unique edge-containing component

The component proof uses degree escalation.

For a low-degree sampled vertex, internal sparsity implies that only an \(O(t^2)\) fraction of the continuum mass remains inside the same low-degree layer.

A nonisolated low-degree vertex therefore has, with high probability, a neighbor whose continuum degree is substantially larger.

Iterating this escalation reaches a fixed positive-degree core.

A compact-cover argument inside the connected causal diamond then joins the core.

The same calculation as in flat \(2+1\), with the curved exponents above, gives

\[
\boxed{
\Pr(
G_{g,n}
\text{ has more than one edge-containing component}
)
\to0.
}
\]

Quantitatively, after true twins and residual local escalation failures are separated, the component ambiguity probability is

\[
O(n^{-2})
+
\text{superpolynomial}.
\]

## 9. Implication-edge escalation

The curved small-edge tail satisfies

\[
F_{3,g}(t)=\Theta(t^3),
\]

and the uniform comparable-ball estimate is

\[
O(t^2).
\]

For an edge of disagreement \(\delta\), the splitters that only lead to a forced edge of disagreement at most \(\delta^\alpha\), with

\[
\alpha\in(1/2,1),
\]

have total mass

\[
O(\delta^{2\alpha})
=
o(\delta).
\]

Therefore every implication class reaches a fixed positive-disagreement edge core with probability tending to one.

Separating the zero-splitter true-twin event and using a constant-factor escalation gives

\[
\boxed{
\Pr(
\text{non-twin residual escalation failure}
)
=
O(n^{-2}).
}
\]

## 10. Core edges force linear obstructions

A core edge has disagreement at least a fixed

\[
\delta_0>0.
\]

Its sampled splitter count is binomial with mean \(\Theta(n)\).

Uniform Chernoff concentration over all sampled edges gives a constant

\[
c_0>0
\]

such that every core edge has at least

\[
c_0n
\]

sampled splitters, outside an exponentially small event.

Hence:

- every non-stable module containing a core edge has linear size;
- every edge-containing component containing a core edge has linear size.

## 11. Balanced modules

The causal-comparability graphon of any smooth Lorentzian Alexandrov interval is prime.

This is curvature independent.

Therefore finite-colour graphon compactness excludes balanced modules asymptotically.

The cut-distance sampling argument gives, for every fixed \(\varepsilon>0\),

\[
\boxed{
\Pr(
\exists M:
\varepsilon n\le|M|\le(1-\varepsilon)n
)
\le
\exp\left(
-\frac{n}{2\log n}
\right)
}
\]

for sufficiently large \(n\).

A standard diagonal choice \(\varepsilon_n\downarrow0\) extends this to the slowly shrinking balanced range needed in the final assembly.

## 12. Curved tip geometry

The regular curved tip theorem gives

\[
\boxed{
\bar g_3(r)
=
\mu\{1-Q\le r\}
=
\Theta(r^3).
}
\]

It also gives a middle nonneighbor band of volume at least

\[
cR(x)
\]

whose points have graphon degree in a fixed interval

\[
[q_-,q_+]
\Subset(0,1).
\]

Therefore a vertex complete to an \(n-o(n)\) module must have a sampled-empty middle band.

Integrating the empty-band probability against the co-degree tail gives

\[
\boxed{
\Pr(
\text{near-whole module}
)
=
O(n^{-2})
+
e^{-\Theta(n)}.
}
\]

This is subleading to the \(n^{-1}\) true-twin scale.

## 13. Failure decomposition

Let \(\mathcal F_n\) be the orientation-recovery failure event.

Then, up to exponentially/superpolynomially small terms,

\[
\mathcal F_n
\]

is contained in the union of:

1. comparable true twins;
2. non-twin residual escalation failures;
3. multiple edge-containing components without true twins;
4. balanced internal non-stable modules;
5. near-whole internal modules.

Their scales are:

### True twins

\[
K_{3,g}n^{-1}
+
o(n^{-1}).
\]

### Residual local forcing

\[
O(n^{-2}).
\]

### Component ambiguity without twins

\[
O(n^{-2})
+
\text{superpolynomial}.
\]

### Balanced modules

superpolynomially small.

### Near-whole modules

\[
O(n^{-2}).
\]

Thus every non-twin failure class is

\[
o(n^{-1}).
\]

## 14. Completion

The lower bound follows from true-twin occurrence:

\[
1-p_{3,g}^{\mathrm{UPO}}(n)
\ge
\left(
K_{3,g}+o(1)
\right)n^{-1}.
\]

The failure decomposition gives the matching upper bound:

\[
1-p_{3,g}^{\mathrm{UPO}}(n)
\le
\left(
K_{3,g}+o(1)
\right)n^{-1}.
\]

Therefore

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

## 15. Flat check

For the unit flat \(2+1\) diamond,

\[
K_{3,\eta}
=
\frac{32\pi}{3}.
\]

Thus the theorem reduces to

\[
1-p_{3,\eta}^{\mathrm{UPO}}(n)
\sim
\frac{32\pi}{3n},
\]

exactly reproducing the flat result.

## 16. Conformal check

If

\[
g=\Omega^2\eta
\]

with smooth positive bounded \(\Omega\), all regularity hypotheses hold on a compact regular diamond away from conformal singularities.

The theorem is therefore compatible with the previously proved conformal-weight robustness theorem.

The coefficient \(K_{3,g}\) changes with the physical volume profile, while the \(n^{-1}\) exponent remains fixed.

## 17. Scope

This theorem is not unconditional over all curved \(2+1\) spacetimes.

It requires regularity of:

- the finite-diamond volume function;
- the null edge;
- the null generators;
- the tip volume derivatives.

The theorem can fail to apply in the presence of:

- caustics;
- conjugate points;
- nonsmooth diamond edges;
- degenerate volume-time gradients;
- causal boundaries or singular conformal factors.

These exclusions are explicit.

## 18. Scientific consequence

The result shows that the flat \(2+1\) orientation-recovery law is not merely a Minkowski accident.

Under a broad regular Lorentzian class, the same stochastic structure survives:

\[
\boxed{
\text{orientation recovery}
=
1
-
\frac{
\text{intrinsic geometric constant}
}{
n
}
+
o(n^{-1}).
}
\]

The leading constant is determined by the Lorentzian volume-time gradient:

\[
\boxed{
K_{3,g}
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
d\mu.
}
\]

This is the first genuinely curved extension in the current research program that does not rely on conformal equivalence to Minkowski space.
