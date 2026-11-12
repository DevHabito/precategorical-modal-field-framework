# Adversarial audit: local all-dimensional curved orientation recovery

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** internal adversarial audit  
**Target:** ALLD_LOCAL_CURVED_ORIENTATION_RECOVERY_THEOREM_20261112.md

## 1. Audit question

The target theorem claims that at every strongly causal point of a smooth Lorentzian spacetime and for every fixed

\[
d\ge3,
\]

sufficiently small fixed Alexandrov diamonds satisfy

\[
1-p_{d,g,L}^{\mathrm{UPO}}(n)
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

The purpose of this audit is not to extend the theorem.

It is to search for a hidden dependence on:

- coordinate normalization;
- flat-space symmetry;
- an unjustified volume-function theorem;
- compact-containment assumptions;
- graphon closedness;
- an omitted competing failure class.

## 2. Finding A: optical-coordinate invariance — PASS

The curved \(d\ge4\) edge coefficient is written using optical functions \(a,b\).

Under

\[
a'=\lambda(s)a,
\qquad
b'=\mu(s)b,
\]

the double-null coefficient transforms as

\[
\Omega'^2
=
\frac{\Omega^2}{\lambda\mu}.
\]

The endpoint-volume coefficients transform as

\[
c_+'=c_+\lambda^{-d/2},
\qquad
c_-'=c_-\mu^{-d/2}.
\]

The pair-measure factor contributes

\[
(\lambda\mu)^{-(d+2)/2},
\]

while the scalar disagreement integral contributes

\[
(\lambda\mu)^{(d+2)/2}.
\]

They cancel exactly.

Therefore

\[
\boxed{
C_{d,g}^{\rm joint}
}
\]

is independent of optical normalization.

The symbolic regression is in

tools/verify_curved_joint_coefficient_normalization.py.

## 3. Finding B: flat d = 4 normalization — PASS

For the unit flat \(3+1\) diamond:

\[
V_D=\frac{2\pi}{3},
\]

\[
A_E=4\pi,
\]

\[
\Omega^2=\frac12,
\]

and

\[
c_+=c_-=\frac14.
\]

The curved formula reduces to

\[
\int_E\mathcal A_4\,dA_E
=
\frac94,
\]

and

\[
\mathcal S_4
=
\frac{2\pi}{3}.
\]

Hence

\[
C_4^{\rm joint}
=
2
\left(\frac94\right)
\left(\frac{2\pi}{3}\right)
=
3\pi.
\]

Then

\[
K_4
=
\frac12
C_4^{\rm joint}
\Gamma(4)
=
9\pi.
\]

This reproduces the independently derived flat theorem exactly.

No normalization defect was found.

## 4. Finding C: compact containment — corrected and strengthened

The first proof attempted to control the plane-wave curvature term with a generic causal-energy/Gronwall estimate.

That argument was not sufficient because the quadratic Penrose-plane-wave term

\[
\langle H(v)y,y\rangle
\]

has no fixed sign and cannot be made small merely by shrinking the null-Fermi tube.

The corrected theorem

THIN_NULL_COMPACT_CONTAINMENT_LEMMA_20261112.md

uses the transverse null index form

\[
Q_\gamma[y]
=
\int
\left(
|\dot y|^2
+
\langle H(v)y,y\rangle
\right)dv.
\]

Before the first conjugate point, the null Morse-index theorem and absence of a Dirichlet Jacobi kernel give a positive quadratic form.

For the compact generator family, the dedicated lemma

UNIFORM_NULL_INDEX_GAP_LEMMA_20261112.md

shows that the lowest Dirichlet Jacobi eigenvalue varies continuously and has a uniform positive minimum

\[
\lambda_*>0.
\]

After subtracting the Jacobi field interpolating the \(O(\sqrt a)\) transverse endpoint data, coercivity gives

\[
\|w\|_{H^1}^2
=
O(a),
\]

hence

\[
|y|=O(\sqrt a).
\]

The causal equation then gives

\[
|u|=O(a).
\]

Only the higher-order Fermi remainder is absorbed by shrinking the tube.

Thus Penrose-scaled compact containment is derived from **index-form coercivity**, not from a sign assumption on curvature.

### Negative control

The exact constant-profile plane-wave diagnostic

PLANE_WAVE_CAUSTIC_THRESHOLD_DIAGNOSTIC_20261112.md

shows that this mechanism fails exactly at conjugacy.

For

\[
ds^2
=
2\,du\,dv
+
dy^2
-
\omega^2y^2dv^2,
\]

the first Dirichlet eigenvalue is

\[
\lambda_1(L)
=
\left(\frac{\pi}{L}\right)^2-\omega^2.
\]

At

\[
L=\frac{\pi}{\omega},
\]

the Jacobi mode

\[
y=A\sin(\omega v)
\]

has zero index form for every amplitude \(A\).

The thin interval then loses the \(O(\sqrt a)\) transverse bound.

This is an exact control showing that the conjugate-free hypothesis is structural rather than technical.

## 5. Finding D: strongly causal local neighborhoods — corrected

The first local theorem stated that one could choose a single neighborhood that was simultaneously:

- causally convex in the ambient spacetime;
- convex normal.

That stronger statement was unnecessary and was not established by the cited local theorems.

The proof has been corrected to use nested neighborhoods

\[
o\in V\Subset C,
\]

where:

- \(V\) is causally convex in the ambient spacetime;
- \(C\) is strictly convex normal.

The diamond is chosen with

\[
\overline{D_L}\subset V.
\]

Causal curves are trapped by \(V\), while geodesic/world-function calculations use \(C\).

This is the precise local construction justified by strong causality plus standard convex-neighborhood theory.

## 6. Finding E: Chrusciel-Grant-Minguzzi scope — CORRECTION REQUIRED AND MADE

A previous draft described the constant-weight finite-diamond volume function as a direct corollary of Chrusciel--Grant--Minguzzi.

That was too strong.

Their theorem proves differentiability for a controlled class of positive smooth weights.

Their paper explicitly gives a bounded Minkowski-subspacetime example with

\[
\varphi=1
\]

for which the past-volume function is not differentiable across a pathological causal boundary.

Therefore:

\[
\boxed{
\text{finite volume + constant weight}
\not\Rightarrow
C^1
\text{ in arbitrary bounded subspacetimes}.
}
\]

The repository has been corrected.

For the strictly convex normal diamond, \(C^1\) regularity is now supported by the dedicated world-function shape-derivative proof

WORLD_FUNCTION_FINITE_DIAMOND_VOLUME_REGULARITY_20261112.md.

The literature is cited only for the established variation mechanism, not as a black-box theorem covering the present constant weight.

## 7. Finding F: finite-diamond world-function regularity — internally consistent

The dedicated proof writes the moving volume as a Heaviside/world-function integral and differentiates it into a null-hypersurface shape derivative.

The potential singular sets are:

1. the cone vertex;
2. the codimension-two intersection with the fixed opposite null boundary.

At the cone vertex:

- the world-function endpoint derivative is \(O(r)\);
- the auxiliary coarea denominator is \(O(r)\);
- the quotient is bounded;
- null-cone area is \(O(r^{d-2})\).

Thus the vertex is integrable for

\[
d\ge2.
\]

At the edge, strict convex-normal geometry gives transverse smooth null sheets, so the moving cutoff is regular.

For a future causal nonzero vector \(Z\), the endpoint derivative has strict sign on almost every null generator, proving timelikeness of the gradient.

No internal contradiction was found.

This remains a project proof requiring external review.

## 8. Finding G: tangent-space coefficient limit — strengthened

The original local theorem stated

\[
K_{d,g}(D_L)
\to
K_d^{\rm Mink}
\]

without a dedicated proof.

The new theorem

LOCAL_CURVED_COEFFICIENT_TANGENT_STABILITY_20261112.md

supplies the missing argument.

### d = 3

The edge singularity has the uniform integrable majorant

\[
\kappa_L^{-3}
\lesssim
(ab)^{-3/4}.
\]

Dominated convergence gives

\[
K_{3,g}(D_L)
\to
\frac{32\pi}{3}.
\]

### d >= 4

The edge integrand converges uniformly after identifying the smooth moving edge with the flat edge.

Therefore

\[
K_{d,g}(D_L)
\to
K_d^{\rm Mink}.
\]

## 9. Finding H: graphon primeness-to-gap transfer — PASS

The balanced-module proof does not merely assume that the class of graphons with a balanced homogeneous set is closed.

Instead it uses coloured graphon compactness.

If a sequence of balanced modules approached the prime causal graphon, the red/blue colourings have a convergent coloured subsequence.

Zero splitter density survives by the coloured counting lemma.

In the mixed-colour limit, either:

1. the support of the red density produces a nontrivial weakly homogeneous set; or
2. the red support has full measure, forcing a positive-measure set of graphon rows to be constant almost everywhere.

Both contradict causal-graphon primeness and

\[
0<Q(x)<1
\]

for almost every interior point.

Thus the positive cut-distance gap is justified.

No counterexample was found.

## 10. Finding I: second moment of true twins — PASS

For two disjoint candidate true-twin pairs, simultaneous survival requires both pair disagreements to be \(O(1/n)\).

Even if the two splitter regions overlap strongly, their union has measure at least the maximum of the two individual disagreements.

Therefore the joint Laplace scale is

\[
n^{-2\beta_d},
\]

and the \(O(n^4)\) pair count gives

\[
O(n^{4-2\beta_d}).
\]

For overlapping candidate pairs:

- the first pair costs \(O(t^{\beta_d})\);
- the third point lies in a comparable disagreement ball of mass \(O(t^2)\).

Hence

\[
O(n^{1-\beta_d}).
\]

Both are lower order than

\[
n^{2-\beta_d}.
\]

Thus

\[
\Pr(T_n>0)
\sim
\mathbb E[T_n].
\]

## 11. Finding J: residual forcing escalation — PASS

For a sampled edge of disagreement \(\delta\), a splitter is called bad when every directly forced edge stays at disagreement at most a fixed multiple of \(\delta\).

Such splitters lie in the union of two comparable disagreement balls.

Hence their mass is

\[
O(\delta^2).
\]

Conditioned on the edge, the probability of:

- at least one splitter;
- but no good splitter;

is

\[
O(
n\delta^2e^{-cn\delta}
).
\]

Integrating against

\[
F(\delta)=O(\delta^{\beta_d})
\]

and multiplying by \(O(n^2)\) candidate edges gives

\[
\boxed{
O(n^{1-\beta_d}).
}
\]

This is one full factor \(n^{-1}\) below the leading true-twin scale.

## 12. Finding K: arbitrary nonstable modules — PASS conditional on escalation

A nonstable graph module contains an internal edge.

Any splitter of an internal pair must itself lie inside the module, because outside vertices cannot split a module.

Therefore every direct forcing step from an internal edge remains inside the module.

Outside residual escalation failure, the edge reaches fixed positive disagreement.

That core edge has \(\Theta(n)\) sampled splitters with exponentially high probability.

Hence every nonstable module is either:

- linear in size;
- or part of the already counted residual rare event.

Balanced linear modules are superpolynomially rare.

Near-whole modules are controlled by the tip theorem.

Thus there is no omitted mesoscopic module class at the leading scale.

## 13. Finding L: local strongly-causal theorem — scope survives

After the neighborhood correction, the local geometric chain is:

\[
\boxed{
\text{strong causality at }o
}
\]

\[
\Downarrow
\]

nested

\[
V\Subset C
\]

with \(V\) causally convex and \(C\) strictly convex normal,

\[
\Downarrow
\]

small \(D_L\subset V\),

\[
\Downarrow
\]

regular null sheets, no local cuts/conjugate points, transverse edge, regular tips,

\[
\Downarrow
\]

thin-null + bulk + tip estimates,

\[
\Downarrow
\]

stochastic UPO assembly.

No use of global hyperbolicity of the ambient spacetime is required.

The theorem applies in particular at every point of a globally hyperbolic spacetime.

## 14. Remaining external-review risks

No internal contradiction was found, but the following deserve independent mathematical review.

### Highest priority

1. the world-function \(C^1\) finite-diamond volume proof;
2. the causal-energy proof of automatic thin-null compact containment;
3. the Penrose-scaled Alexandrov-domain convergence theorem.

### Next priority

4. uniformity of the all-dimensional double-null edge expansion over the compact edge;
5. the exact invariant edge coefficient for \(d>4\);
6. the local graphon primeness forcing proof in nontrivial Lorentzian topology.

### Lower risk

7. Laplace-Stieltjes transfers;
8. Chernoff bounds;
9. modular/forcing graph theory;
10. optical-normalization algebra.

## 15. Audit verdict

The adversarial audit found two genuine issues:

1. an unnecessarily strong neighborhood claim;
2. an overstatement of the scope of the Chrusciel--Grant--Minguzzi differentiability theorem.

Both have been corrected.

No mathematical counterexample to the local curved recovery law **inside the regular conjugate-free class** was found.

An exact plane-wave counterexample was found to any attempted extension of the compact-containment step through a conjugate point. This validates the present scope restriction rather than contradicting the theorem.

The current status should be stated as

\[
\boxed{
\text{internally coherent candidate theorem, externally unverified}.
}
\]

It should **not** yet be advertised as an established theorem of Lorentzian geometry.

The strongest next step is independent expert review of the three geometric lemmas listed above, rather than further expansion of the theorem's scope.
