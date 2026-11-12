# Audit: leading error law in a regular curved 2+1 Lorentzian diamond

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** adversarial normalization, dependency, and failure-class audit
**Target:** CURVED_D3_ORIENTATION_RECOVERY_RATE_THEOREM_20261112.md

## 1. Audit purpose

The target theorem states

\[
1-p_{3,g}^{\mathrm{UPO}}(n)
\sim
\frac{\mathcal K(D,g)}{n},
\]

with

\[
\mathcal K(D,g)
=
\frac{2\pi}{V_D}
\int_D
\left[
-g^{-1}(d\Phi,d\Phi)
\right]^{-3/2}
\,d\mu.
\]

This audit checks:

1. normalization of the coefficient;
2. invariance under a constant metric rescaling;
3. the true-twin Laplace-Stieltjes factor;
4. the factorial second moment;
5. the scope of the tip middle-band argument;
6. exhaustion of all non-twin UPO failure modes;
7. whether any geometric hypothesis used by a dependency was missing from the final theorem statement.

## 2. Normalization of the local bulk coefficient

The normalized sprinkling measure is

\[
d\mu
=
\frac{
d\operatorname{Vol}_g
}{
V_D
}.
\]

For a fixed root point \(x\), the physical volume of future-timelike displacements satisfying

\[
d\Phi_x(h)\le\varepsilon
\]

is

\[
\frac{\pi}{3}
\frac{
\varepsilon^3
}{
\kappa(x)^3
},
\]

where

\[
\kappa(x)
=
\sqrt{
-g^{-1}(d\Phi,d\Phi)
}.
\]

Dividing by \(V_D\) gives the conditional probability for the second iid point.

Including both time orientations gives

\[
\frac{
2\pi
}{
3V_D
}
\kappa(x)^{-3}
\varepsilon^3.
\]

Integrating the root point against normalized \(d\mu(x)\) therefore gives

\[
C_g
=
\frac{
2\pi
}{
3V_D
}
\int_D
\kappa^{-3}
\,d\mu.
\]

No additional factor of \(V_D\) is missing.

## 3. Constant metric-rescaling check

Let

\[
\tilde g=c^2g,
\qquad
c>0.
\]

Then:

- causal structure is unchanged;
- normalized Alexandrov volumes \(\mathcal V\) are unchanged;
- \(\Phi\) is unchanged as a scalar function;
- the inverse metric scales as
  \[
  \tilde g^{-1}=c^{-2}g^{-1};
  \]
- therefore
  \[
  \tilde\kappa=c^{-1}\kappa;
  \]
- the total diamond volume scales as
  \[
  \tilde V_D=c^3V_D;
  \]
- normalized probability measure \(d\mu\) is unchanged.

Hence

\[
\frac{2\pi}{\tilde V_D}
\int
\tilde\kappa^{-3}
\,d\mu
=
\frac{
2\pi
}{
c^3V_D
}
\int
c^3\kappa^{-3}
\,d\mu
=
\mathcal K(D,g).
\]

Thus the proposed error coefficient is invariant under a global change of length units.

This is a necessary consistency check and it passes exactly.

## 4. Flat regression

For the unit flat \(2+1\) diamond,

\[
V_D=\frac{2\pi}{3},
\]

and the independently evaluated intrinsic integral is

\[
\int_D
\kappa^{-3}
\,d\mu
=
\frac{32\pi}{9}.
\]

Therefore

\[
\mathcal K(D,\eta)
=
\frac{2\pi}{2\pi/3}
\frac{32\pi}{9}
=
\frac{32\pi}{3}.
\]

The curved formula reproduces the independently derived flat law

\[
1-p_3^{\mathrm{UPO}}(n)
\sim
\frac{32\pi}{3n}.
\]

## 5. Laplace-Stieltjes transfer

If

\[
F_{3,g}(t)
\sim
C_gt^3,
\]

then

\[
dF_{3,g}(t)
\]

has the asymptotic Stieltjes mass corresponding to exponent \(3\).

The true-twin expectation is

\[
\binom n2
\int
(1-t)^{n-2}
\,dF_{3,g}(t).
\]

The standard Laplace-Stieltjes transfer gives

\[
\int
(1-t)^{n-2}
\,dF_{3,g}(t)
\sim
C_g\Gamma(4)n^{-3}.
\]

Since

\[
\binom n2\sim\frac{n^2}{2}
\]

and

\[
\Gamma(4)=6,
\]

\[
\boxed{
\mathbb E[T_n]
\sim
3C_gn^{-1}.
}
\]

The factor \(3\) is correct.

## 6. Disjoint true-twin pairs

For two disjoint candidate pairs, simultaneous survival requires the outside sample to avoid the union of their splitter regions.

The union volume is at least the larger disagreement:

\[
\mu(\mathcal D_1\cup\mathcal D_2)
\ge
\max(\delta_1,\delta_2).
\]

Before imposing cross-pair constraints, the two continuum pairs are independent.

Thus

\[
\Pr(
\delta_1\le t,\delta_2\le t
)
=
F_{3,g}(t)^2
=
O(t^6).
\]

This gives a factorial-moment contribution

\[
O(
n^4n^{-6}
)
=
O(n^{-2}).
\]

Dropping cross-pair compatibility only enlarges the event, so the bound is valid.

## 7. Overlapping true-twin pairs

If two adjacent true-twin pairs share one vertex, all three involved vertices lie in one true-twin equivalence class.

For three-way splitter volume at most \(t\):

- the first comparable pair has disagreement at most \(t\), probability \(O(t^3)\);
- the third point must lie in a comparable-disagreement ball of radius \(t\), mass \(O(t^2)\).

Therefore

\[
H_{\mathrm{overlap}}(t)
=
O(t^5),
\]

and the factorial-moment contribution is

\[
O(n^3n^{-5})
=
O(n^{-2}).
\]

Hence

\[
\Pr(T_n>0)
\sim
\mathbb E[T_n].
\]

No independence assumption is made in the overlapping case.

## 8. Tip middle-band first variation

The key geometric input is the variation of Synge's world function with respect to its base point.

For a geodesic with affine parameter interval \(\Delta\lambda\),

\[
\sigma_{\alpha'}
=
-\Delta\lambda\,
g_{\alpha'\beta'}t^{\beta'}.
\]

For a null generator parameterized by \(\lambda\) from the tip, this gives

\[
d_p\sigma(v)
=
-\lambda g(v,k_\theta).
\]

This is the standard first-variation formula.

The middle-band theorem uses the same angular weight

\[
-g(v,k_\theta)\ge0
\]

in the full null-cone variation and in the fixed affine middle band.

The pointwise inequality

\[
H_{\mathrm{mid}}(\theta)
\ge
c_*H_{\mathrm{tot}}(\theta)
\]

therefore survives multiplication by that nonnegative angular weight and integration.

This closes the potentially dangerous limit in which the tip is approached almost tangentially to one null generator.

## 9. Scope of the middle-band argument

The near-whole theorem is applied only after multiple edge-containing components have been excluded.

This ordering is necessary.

A sampled middle-band point \(z\) is a nonneighbor of the complete external module vertex.

On the unique edge-containing-component event, such a point is either:

1. in the same nontrivial component and hence subject to the module external-type condition; or
2. isolated.

Because its continuum degree is uniformly in

\[
[q_-,q_+]\subset(0,1),
\]

the isolated alternative is exponentially unlikely.

Therefore the middle-band obstruction is valid at the exact scope in which the final proof uses it.

## 10. Complete external vertices outside the tip regime

The middle-band theorem is stated for small continuum co-degree

\[
R(x)<r_0.
\]

A near-whole module has complement \(o(n)\), so a complete external vertex has sampled co-degree \(o(n)\).

If instead

\[
R(x)\ge r_0,
\]

its conditional expected sampled co-degree is at least \(r_0(n-1)\).

Chernoff gives probability

\[
e^{-\Theta(n)}
\]

for such a vertex to have \(o(n)\) observed co-degree.

Thus the reduction to the tip regime loses only an exponentially small probability.

## 11. Failure-class exhaustion

Condition on

\[
T_n=0.
\]

If orientation recovery fails, then one of the following occurs.

### A. Residual forcing failure

Probability

\[
O(n^{-2}).
\]

### B. More than one edge-containing component

Outside residual forcing, every component reaches a core edge and is linear.

Two such components produce a balanced module.

Probability

\[
O(n^{-2})
+
\exp[-n/(2\log n)]
+
e^{-\Theta(n)}.
\]

### C. Unique edge-containing component but internal non-UPO

The connected comparability-graph criterion produces a proper non-stable module.

Its internal edge forcing class reaches the core, so the module has linear size.

It is therefore either:

- balanced relative to a deterministic diagonal threshold;
- near-whole.

The balanced case is superpolynomially small.

The near-whole case is

\[
O(n^{-2})+e^{-\Theta(n)}
\]

by tip clearance.

### D. No edge-containing component

Choose two fixed positive-volume open sets \(U,V\subset D\) with

\[
U\ll V.
\]

If both contain a sampled point, the graph has an edge.

The probability that either is empty is exponentially small.

Thus the empty graph is negligible.

No additional UPO failure class remains.

## 12. Classical module criterion

The proof uses the classical fact:

for a connected comparability graph,

\[
G\text{ is UPO}
\iff
\text{every proper nontrivial module is stable}.
\]

A non-stable module contains an internal edge.

Therefore every connected non-UPO witness enters the edge-forcing/core argument.

Stable modules do not create independent transitive-orientation ambiguity.

## 13. Explicit correction made during this audit

The target theorem initially stated H3 only as:

- \(C^2\) volume-time function;
- timelike \(d\Phi\);
- integrable \(\kappa^{-3}\).

The curved small-edge theorem additionally uses a uniform Taylor remainder and dominated compact-exhaustion argument.

H3 has now been corrected to include that bulk-regularity hypothesis explicitly.

This correction narrows the stated theorem to exactly the hypotheses used by its dependencies.

It does not change the mathematical proof.

## 14. Remaining nonclassical review risks

At its stated conditional scope, no missing factor or unclassified failure event was found.

The principal geometric points still deserving independent expert review are:

1. uniform Penrose-Fermi control used to justify the volume-null chart;
2. the curved joint cap estimate;
3. the bulk dominated-convergence step for the exact coefficient;
4. the null-cone shape derivative underlying the tip middle band.

These are precisely the geometric assumptions/lemmas isolated in H1--H5.

## 15. Audit verdict

The error law

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
[-g^{-1}(d\Phi,d\Phi)]^{-3/2}
\,d\mu
\right)
\frac1n
}
\]

survives the present internal audit **for regular curved \(2+1\) diamonds satisfying the corrected H1--H5 package**.

No claim is made that every smooth \(2+1\) diamond satisfies those hypotheses.
