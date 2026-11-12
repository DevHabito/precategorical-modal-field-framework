# Audit: local curved all-dimensional orientation-recovery theorem

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** adversarial internal audit after curvature generalization  
**Target:** ALLD_LOCAL_CURVED_ORIENTATION_RECOVERY_THEOREM_20261112.md

## 1. Audit question

The target theorem states that for every strongly causal point of a smooth Lorentzian spacetime and every fixed dimension

\[
d\ge3,
\]

a sufficiently small fixed centered causal diamond satisfies

\[
1-p_{d,g,L}^{\rm UPO}(n)
\sim
K_{d,g}(D_L)
n^{2-\beta_d},
\]

with

\[
\beta_3=3,
\qquad
\beta_d=2+\frac4d
\quad(d\ge4).
\]

This audit asks whether the curvature extension introduced a hidden sector, coordinate artifact, or unsupported regularity claim.

## 2. Finding: strong causality is the correct local causality hypothesis

Strong causality is equivalent to the existence of arbitrarily small causally convex neighborhoods.

Choose such a neighborhood with compact closure inside a convex-normal neighborhood.

For sufficiently small centered endpoints \(p_L,q_L\), every causal curve from \(p_L\) to \(q_L\) remains in the causally convex set.

Therefore

\[
\overline{D_L}
\]

lies inside the convex-normal region.

This justifies:

- unique local causal geodesics;
- absence of relevant local cut points;
- absence of conjugate points before the boundary;
- use of Synge's world function on the required two-point domains.

No global-hyperbolicity assumption on the full spacetime is needed.

## 3. Finding: unweighted volume-time regularity is nontrivial

The general literature on Geroch/cosmological volume functions does **not** imply that the physical unweighted volume function is always \(C^1\) temporal merely because the volume is finite.

This was a real overgeneralization risk.

The local convex-diamond theorem survives because the repository now contains a dedicated truncation proof:

CONVEX_DIAMOND_VOLUME_TIME_REGULARITY_AUDIT_20261112.md.

The proof:

1. approximates the physical weight \(1\) by compactly supported smooth weights;
2. applies the established light-cone/Jacobi derivative formula;
3. uses the finite convex generator geometry to obtain a uniform integrable majorant;
4. passes both the functions and their derivatives to the physical-weight limit;
5. proves strict temporal sign from the positive-measure family of nonaligned null directions.

Thus the local result is not being imported incorrectly from the general literature.

## 4. Finding: Penrose compact containment is automatic locally

The Penrose-scaled domain theorem originally assumed that the rescaled thin intervals remain in a fixed compact coordinate set.

That assumption is now derived in

LOCAL_PENROSE_COMPACT_CONTAINMENT_THEOREM_20261112.md.

Cone comparison in the null-Fermi tube gives

\[
u=O(a),
\]

\[
|y|=O(\sqrt a),
\]

\[
v=O(1).
\]

Therefore after

\[
u=aU,
\qquad
y=\sqrt a\,Y,
\qquad
v=V,
\]

the rescaled intervals remain uniformly bounded.

This closes a genuine local-geometry gap.

## 5. Finding: scaled Alexandrov domains converge

Given compact containment, smooth Penrose-Fermi metric convergence implies:

- interior points of the limiting plane-wave interval eventually remain inside;
- points outside the limiting causal diamond eventually remain outside by cone sandwiching and the limit-curve theorem;
- only the null boundary remains undecided;
- that boundary has measure zero in the regular tube.

Therefore interval indicators converge almost everywhere.

Dominated convergence yields

\[
V(p,x_a)
=
\mathcal C_\gamma
a^{d/2}
[1+o(1)].
\]

The thin-null exponent is therefore supported by a domain-convergence proof, not power counting alone.

## 6. Finding: the curved edge coefficient is coordinate invariant

The coefficient uses noncanonical optical functions.

Under

\[
a\mapsto\lambda a,
\qquad
b\mapsto\mu b,
\]

the pair-density factor changes by

\[
(\lambda\mu)^{-(d+2)/2},
\]

while the scalar disagreement integral changes by

\[
(\lambda\mu)^{(d+2)/2}.
\]

They cancel exactly.

The intrinsic edge-area form handles reparametrization of \(E\).

Thus

\[
\boxed{
K_{d,g}
}
\]

is not an optical-coordinate artifact.

The independent regression script

tools/verify_curved_edge_coefficient_invariance.py

also checks the flat reduction numerically for

\[
d=4,\ldots,10.
\]

## 7. Finding: exact flat reduction

Substituting the unit Minkowski data into the curved edge formula gives algebraically

\[
K_{d,\eta}
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
[
a_mL_m\Gamma(a_m)
]^2.
\]

This is exactly the independently derived flat true-twin constant.

For \(d=4\),

\[
\boxed{
K_{4,\eta}=9\pi.
}
\]

Thus the curved formula has the correct flat normalization.

## 8. Finding: there is a second nonlocal zero of disagreement

On the compactified diamond,

\[
A_p=A_q=D
\]

up to null sets.

Therefore

\[
\boxed{
\Delta(p,q)=0.
}
\]

This nonlocal degeneration had not been highlighted in the first curved assembly.

It does not threaten the leading asymptotic.

For

\[
x=\exp_p h,
\qquad
y=\exp_q(-k),
\]

tip volume first variation gives

\[
\Delta(x,y)
=
\Lambda_p(h)
+
\Lambda_q(k)
+
o(|h|+|k|).
\]

Therefore the pair measure with

\[
\Delta\le\varepsilon
\]

is

\[
\boxed{
O(\varepsilon^{2d}).
}
\]

This is subleading to:

\[
\varepsilon^3
\quad(d=3),
\]

and

\[
\varepsilon^{2+4/d}
\quad(d\ge4).
\]

## 9. Finding: small-disagreement sectors are exhausted

The repository theorem

LOCAL_CURVED_SMALL_DISAGREEMENT_SECTOR_EXHAUSTION_20261112.md

classifies all possible \(\Delta\to0\) ordered comparable-pair limits in a sufficiently small convex diamond.

They are:

1. local diagonal bulk/regular-face sectors;
2. local diagonal null-joint sector;
3. opposite-tip sector.

Away from neighborhoods of those zero sets, compactness and continuity give a positive disagreement gap.

Thus no hidden fourth boundary sector remains.

## 10. Finding: the d = 3 bulk/joint matching is measure-theoretically controlled

Near the regular joint,

\[
\kappa^{-3}
\asymp
(ab)^{-3/4}.
\]

The explicit conditional-pair bound is

\[
P_\varepsilon(x)
\le
C
\varepsilon^3
(ab)^{-3/4}.
\]

The right-hand side is integrable.

Therefore dominated convergence gives the bulk coefficient directly.

The earlier informal two-stage matching argument is no longer necessary.

## 11. Finding: the tip middle-band has an explicit shape derivative

The shifted null cone is represented by

\[
\sigma(\exp_p h,z)=0.
\]

Synge's endpoint derivative gives

\[
D_x\sigma(p,z)[h]
=
-\lambda g(h,k_z).
\]

The implicit-function theorem converts this into a transverse boundary displacement.

A compact angular argument gives a uniformly positive-measure family of directions with displacement at least

\[
c\Lambda_p(h).
\]

Therefore

\[
\mu(B_x^{\rm mid})
\ge
cR(x).
\]

The near-whole-module rate is supported by an explicit first-variation calculation.

## 12. Finding: graphon primeness is curvature independent

The continuum forcing graph of timelike edges in an Alexandrov interval is connected through finite robust \(P_3\) forcing chains.

A positive-measure weakly homogeneous set would have to absorb all robust splitter neighborhoods along such paths.

That contradicts a density point of its complement.

Therefore the causal-comparability graphon is prime.

No flat-space symmetry enters this argument.

## 13. Finding: balanced-module separation remains valid

The coloured-graphon compactness proof survives curvature because it uses only:

- graphon primeness;
- absence of positive-measure constant causal rows;
- standard coloured counting convergence.

Finite balanced modules yield strongly homogeneous sets in empirical step graphons.

Therefore the positive cut-distance gap and Second Sampling Lemma continue to exclude balanced modules superpolynomially.

No new curved graphon obstruction was found.

## 14. Finding: true-twin second moments remain subleading

The proof uses only:

\[
F_{d,g}(t)
=
O(t^{\beta_d}),
\]

and

\[
\sup_x\mu(B_t(x))
=
O(t^2).
\]

For disjoint candidate pairs,

\[
O(n^{4-2\beta_d}).
\]

For overlapping candidate pairs,

\[
O(n^{1-\beta_d}).
\]

Both are

\[
o(n^{2-\beta_d}).
\]

Hence

\[
\Pr(T_n>0)
\sim
\mathbb E[T_n].
\]

No independence beyond the iid continuum-pair sampling used in the disjoint upper bound is assumed.

## 15. Finding: non-twin forcing remains one order lower

For an edge with disagreement \(\delta\), all splitters that fail to create a constant-factor larger disagreement edge lie in two comparable metric balls.

Their mass is

\[
O(\delta^2).
\]

The residual sampled-edge rate is therefore

\[
O(n^{1-\beta_d}),
\]

one full factor of \(n^{-1}\) below the true-twin rate

\[
n^{2-\beta_d}.
\]

This remains dimension independent at the mechanism level.

## 16. Finding: component ambiguity does not re-enter

Outside true twins and residual forcing failures:

- every edge reaches a positive-disagreement core edge;
- every core edge has \(\Theta(n)\) sampled splitters;
- every edge-containing component is therefore linear;
- two such components produce a balanced module.

Thus multiple nontrivial components are subleading.

The curved component proof is now written independently rather than inherited by phrase from the flat case.

## 17. Tangent-space coefficient limit

After rescaling the small diamond to unit size,

\[
\widehat g_L\to\eta
\]

smoothly.

For \(d\ge4\), the edge coefficient converges by compact dominated convergence.

For \(d=3\), the uniform edge majorant

\[
(ab)^{-3/4}
\]

permits dominated convergence through the singular edge.

Therefore

\[
\boxed{
K_{d,g}(D_L)
\to
K_d^{\rm Mink}.
}
\]

## 18. First curvature correction

The coefficient functional is differentiable around the flat regular diamond under the local smooth family.

Riemann normal coordinates give

\[
\widehat g_L-\eta
=
O(L^2).
\]

Flat spatial isotropy then forces the first curvature correction to have the form

\[
\boxed{
K_{d,g}(D_L)
=
K_d^{\rm Mink}
+
L^2
[
A_dR+B_dR_{TT}
]_o
+
o(L^2).
}
\]

The constants \(A_d,B_d\) have not been computed.

This structural theorem should receive independent review because it differentiates a nontrivial geometric functional.

## 19. Poisson ensemble consequence

Conditioning a Poisson sprinkling on cardinality reproduces the iid fixed-\(n\) model.

If

\[
N\sim{\rm Poisson}(\rho V_D),
\]

then

\[
\boxed{
\Pr_{\rm Pois}(\text{failure})
\sim
K_{d,g}(D)
(\rho V_D)^{2-\beta_d}.
}
\]

For \(d\ge4\),

\[
2-\beta_d=-\frac4d.
\]

Writing

\[
\ell_\rho=\rho^{-1/d},
\]

the leading density dependence is

\[
\boxed{
(\ell_\rho/L)^4
}
\]

for geometrically similar diamonds.

This transfer is elementary and does not add a new geometric assumption.

## 20. Remaining external-review priorities

No internal contradiction was found.

The strongest remaining reasons not to call the curved theorem established are external verification rather than an identified missing case.

Priority checks are:

1. **Unweighted finite-diamond volume-time proof.**  
   Verify the compact-support truncation and uniform Jacobi majorant carefully.

2. **Penrose compact-containment/domain convergence.**  
   Check the cone-comparison argument and the passage to plane-wave Alexandrov domains independently.

3. **Differentiability of the coefficient functional.**  
   This matters especially for the claimed \(L^2\) curvature-correction structure.

4. **Global graphon gap proof.**  
   The coloured compactness argument should be checked by a graph-limit specialist.

5. **All-dimensional sector exhaustion.**  
   In particular, verify the classification of zero-disagreement ordered boundary pairs.

## 21. Audit verdict

The adversarial review found corrections of scope and one previously unstated subleading sector, but no leading counterexample.

The current status is:

\[
\boxed{
\text{internally coherent local curved theorem, externally unverified.}
}
\]

The flat theorem remains more mature.

The curved theorem is now strong enough that the next serious step should be independent mathematical review and computation of the universal curvature-response constants

\[
A_d,\ B_d,
\]

rather than adding more layers to the proof architecture.
