# A32 — Infinite Refinement, Projective Limits, and Terminality

## Projective-limit proposition
For a finitely branching rooted tree, assign positive child fractions summing
to one at every node. Cylinder mass is the product of fractions along its
finite path. Level masses sum to one and parent mass equals the sum of child
masses. These consistent cylinder probabilities determine a unique Borel
probability measure on the infinite path space by the standard extension
theorem for consistent finite-dimensional distributions.

Terminal leaves are not required.

## Atomicity is not terminality
For a path with branch fractions
\[
p_n=1-\frac1{n^2},\qquad n\ge2,
\]
the depth-\(N\) cylinder mass is
\[
\prod_{n=2}^{N} \left(1-\frac1{n^2}\right)=\frac{N+1}{2N}\to\frac12.
\]
Thus an infinite nonterminal path can be an atom of mass \(1/2\).

Conversely, if every child fraction is at most \(r<1\), every depth-\(d\)
cylinder has mass at most \(r^d\to0\); the measure is non-atomic.

## Non-uniqueness
Projective consistency does not select the split fractions. The same infinite
binary tree supports uniform, biased, atomic, and non-atomic measures.

## Mark convergence witness
Let a scalar refinement mark satisfy
\[
Q_{d+1}=Q_d+\epsilon_d,\qquad E[\epsilon_d\mid\mathcal F_d]=0.
\]
For independent symmetric increments with variance \(\sigma_d^2\),
\[
E[(Q_m-Q_n)^2]=\sum_{d=n}^{m-1}\sigma_d^2.
\]
If \(\sum_d\sigma_d^2<\infty\), the marks are Cauchy in \(L^2\) and possess an
\(L^2\) limit. Constant-size increments fail this criterion.

## Boundary
This establishes mathematical measures and convergent marks on infinite
refinement systems. It does not show that the RZS has an infinite refinement
tree, identify its sigma-algebra, or derive physical split fractions.
