# Audit: regular curved 2+1 orientation-recovery theorem

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** adversarial dependency and scope audit  
**Target:** CURVED_D3_ORIENTATION_RECOVERY_THEOREM_20261112.md

## 1. Audit question

The repository now proves

\[
p_{3,g}^{\mathrm{UPO}}(n)\to1
\]

for a regular class of curved \(2+1\) Alexandrov intervals.

This audit asks:

1. whether any recovery conclusion is hidden inside the geometric assumptions;
2. whether the graphon-connectivity theorem is being applied to the correct random-graph model;
3. whether the curved local estimates actually cover all points;
4. whether the final theorem is being over-described as a theorem for arbitrary curved spacetimes.

## 2. Geometric assumptions only

The hypotheses H1--H4 are:

- smooth transverse null joint;
- no relevant cut/conjugate degeneration;
- uniform Penrose/null-Fermi tubes;
- temporal finite-diamond volume gradient;
- integrability of its inverse norm;
- temporal nondegenerate tip gradients.

None of these hypotheses refers to:

- graph modules;
- UPO;
- implication classes;
- random graph connectivity;
- true twins.

Thus the theorem is not tautological.

## 3. Sampling model check

The causal graphon is

\[
W_g(x,y)
=
\mathbf1_{\{x\sim y\}}.
\]

The graphon sample \(G(n,W_g)\) is formed by:

1. sampling iid latent points \(X_i\);
2. including edge \(ij\) independently with probability
   \[
   W_g(X_i,X_j).
   \]

Because \(W_g\in\{0,1\}\), the second stage is deterministic.

Therefore \(G(n,W_g)\) is exactly the sampled causal-comparability graph.

The Hladký--Viswanathan connectivity theorem applies without a model mismatch.

## 4. Connected graphon hypothesis

The general Lorentzian causal-graphon theorem proves that \(W_g\) is prime.

If a graphon were disconnected, there would exist a measurable set

\[
S,
\qquad
0<\mu(S)<1,
\]

such that

\[
W_g=0
\]

almost everywhere across

\[
S\times S^c.
\]

Such an \(S\) is weakly homogeneous.

Primeness therefore implies graphon connectedness.

## 5. Low-degree connectivity criterion

The curved low-degree theorem gives

\[
g_3(q)
\sim
C_\Sigma q^{4/3}.
\]

Hence

\[
\frac{g_3(q)}q
=
C_\Sigma q^{1/3}
(1+o(1))
\to0.
\]

Hladký and Viswanathan prove that connectedness of \(W\) plus

\[
g_W(q)=o(q)
\]

is equivalent to asymptotic connectedness of \(G(n,W)\).

Thus the finite connectivity step is externally supported by a general graphon theorem.

## 6. Small-edge tail coverage

The curved small-edge proof divides the domain into:

1. a regular joint neighborhood;
2. compact bulk exhaustions away from the joint.

The joint contribution is controlled by the volume-null \(3/2\)-power integrals.

The bulk contribution is controlled by the timelike gradient of

\[
\Phi.
\]

The theorem explicitly assumes that no additional boundary degeneration lies outside these charts.

This is automatic for the declared regular diamond if:

- the only simultaneous low-degree locus is the smooth joint;
- the remaining null boundary is regular and has one endpoint-volume term bounded away from zero.

An external reviewer should verify this chart exhaustion.

## 7. Comparable-ball uniformity

The \(O(t^2)\) theorem has three regimes:

1. low degree:
   controlled by internal sparsity;
2. joint transition:
   controlled by volume-null increment bounds;
3. bulk:
   controlled by a positive lower bound for the temporal-gradient norm on compact sets.

The transition between the three regimes is explicit.

No pointwise-in-\(x\) estimate is silently upgraded to a uniform estimate without a compactness argument.

## 8. Near-whole proof dependencies

The curved near-whole proof uses only:

\[
g_3(q)=O(q^{4/3}),
\]

\[
\bar g_3(r)=O(r^3),
\]

and

\[
\sup_{x\in S_t}
\mu(A_x\cap S_t)=O(t^2).
\]

These are all established earlier from geometric assumptions.

It does not use the final orientation-recovery theorem.

## 9. Circularity check

The dependency chain is:

\[
\text{Lorentzian regularity}
\]

\[
\downarrow
\]

\[
\text{Penrose scaling / volume-null coordinates / volume-time gradient}
\]

\[
\downarrow
\]

\[
\text{degree tails, edge tail, comparable balls, graphon primeness}
\]

\[
\downarrow
\]

\[
\text{general probability + comparability-graph theory}
\]

\[
\downarrow
\]

\[
p_{3,g}^{\mathrm{UPO}}(n)\to1.
\]

No reverse dependency was found.

## 10. What is not yet unconditional

The theorem should **not** currently be advertised as:

> every smooth curved \(2+1\) Alexandrov interval is asymptotically orientation recoverable.

The repository has not proved that H1--H4 follow automatically from arbitrary smooth causal diamonds.

Potential obstructions include:

- null conjugate points;
- cut-locus branching;
- nonsmooth joint structure;
- degeneration of the volume-time gradient;
- nonintegrability of \(\kappa^{-3}\);
- degenerate tip gradients.

The correct scope is:

\[
\boxed{
\text{regular curved }2+1\text{ Lorentzian diamonds satisfying H1--H4}.
}
\]

## 11. Relation to conformally flat examples

Conformally Minkowskian diamonds with smooth positive bounded conformal factor satisfy a stronger theorem already proved by the weighted-measure argument.

They are therefore examples inside the broader recovery program, but they do not test the genuinely nonconformal part of H1--H4.

The next useful example should have nonzero Cotton tensor.

## 12. Rate status

The theorem proves

\[
p_{3,g}^{\mathrm{UPO}}(n)\to1.
\]

The true-twin lower scale is

\[
\Pr(T_n>0)
\sim
3C_g\,n^{-1}.
\]

However, the current near-whole bound is only \(o(1)\), not \(o(n^{-1})\).

Therefore the repository must not yet claim

\[
1-p_{3,g}^{\mathrm{UPO}}(n)
\sim
3C_g/n
\]

for the full regular curved class.

A curved tip-clearance theorem remains necessary for the matching upper bound.

## 13. Literature boundary

The graphon connectivity step is grounded in:

Jan Hladký and Gopal Viswanathan, **Connectivity of Inhomogeneous Random Graphs II**, *Random Structures & Algorithms* 69 (2026), e70098, DOI 10.1002/rsa.70098.

The Penrose/null-Fermi expansion is established literature.

The generic Lorentzian causal-graphon primeness and its use in UPO recovery are project-specific applications.

No external peer verification of the assembled curved theorem has occurred.

## 14. Audit verdict

No circularity or random-model mismatch was found.

The theorem survives the internal audit **at its stated conditional scope**.

The main scientific task is now to replace H1--H4 by more standard sufficient conditions, or to verify them in explicit nonconformally-flat spacetimes.
