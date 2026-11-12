# Localization audit of the d = 4 vacuum ACD volume discrepancy

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic elimination of several candidate failure mechanisms  
**Scope:** Wang (2019), Sec. VI, especially Eqs. (74)--(79)  
**Purpose:** localize the source of the two-geometry disagreement without prematurely declaring a literature error

## 1. Established discrepancy

Two exact Ricci-flat calibrations disagree with the \(d=4\) specialization of Wang Eq. (79):

1. LRS Kasner, purely electric;
2. symmetric Cahen--Wallach plane wave, type N.

The direct exact checks imply the candidate coefficient pair

\[
v_E=\frac{17}{630},
\qquad
v_B=\frac1{210},
\]

whereas Eq. (79) gives

\[
v_E^{\rm W}=\frac{127}{4725},
\qquad
v_B^{\rm W}=\frac1{105}.
\]

The present note asks where the mismatch can enter.

## 2. Published derivation structure

Section VI writes the ACD volume as upper plus lower null-cone contributions.

The null-cone radius is then replaced by an explicitly **abridged** expansion in Eq. (74), where terms declared irrelevant under angular integration are omitted before the final integral.

Next, because the angular average of the temporal edge displacement vanishes, the two halves are replaced by twice the upper half in Eq. (75).

The final volume formula is Eq. (79).

These reductions are legitimate only if no discarded local anisotropy can feed a surviving quadratic term at the target order.

## 3. Generic first-order world-function calculation

Let the RNC origin be the midpoint \(O\), and place the past tip at

\[
p=(-L,\mathbf 0).
\]

For a field point

\[
x=(t,rn^i),
\qquad
n^in_i=1,
\]

the first-curvature expansion of Synge's world function gives

\[
2\sigma(p,x)
=
r^2-(L+t)^2
-
\frac13
L^2r^2E_{nn}
+
O(C^2,\nabla C),
\]

where

\[
E_{nn}=E_{ij}n^in^j.
\]

A full generic \(3+1\) Weyl decomposition was used in the symbolic audit, including both electric and magnetic STF tensors.

All terms linear in the magnetic Weyl tensor cancel identically.

Therefore

\[
\boxed{
r_-(t,n)
=
(L+t)
\left[
1+\frac16L^2E_{nn}
\right]
+
O(C^2,\nabla C).
}
\]

By time reversal,

\[
\boxed{
r_+(t,n)
=
(L-t)
\left[
1+\frac16L^2E_{nn}
\right]
+
O(C^2,\nabla C).
}
\]

This agrees with the first-curvature part of Wang Eq. (74).

## 4. Consequence: no hidden linear magnetic term

A natural suspicion was that the abridged Eq. (74) might have dropped a linear magnetic term with zero angular mean, whose square would later generate a missing \(B^2\) contribution.

The generic world-function audit excludes that mechanism.

There is no such linear magnetic term in the radial null-cone boundary.

Therefore the disagreement in the magnetic coefficient must originate in a genuinely second-order contribution.

The checker is

tools/audit_wang_d4_first_order_rnc_cone_boundary.py

and performs the cancellation symbolically.

## 5. Temporal edge displacement is not the \(C^2\) source

For a centered vacuum ACD, Wang Eq. (39) shows that the temporal edge displacement starts beyond the linear curvature order.

For locally constant curvature, the first surviving displacement is already quadratic in curvature.

Suppose

\[
t_E(n)=O(C^2L^5).
\]

The exact volume splitting is schematically

\[
\int_{-L}^{t_E}F_-(t,n)\,dt
+
\int_{t_E}^{L}F_+(t,n)\,dt.
\]

Moving the splitting surface from \(t_E\) to \(0\) changes the result by

\[
t_E
\left[
F_-(0,n)-F_+(0,n)
\right]
+\cdots.
\]

At flat order,

\[
F_-^{(0)}(0,n)=F_+^{(0)}(0,n).
\]

Hence the bracket begins at least at \(O(C)\).

The resulting correction is therefore at least

\[
O(C^3),
\]

not \(O(C^2)\).

Thus the replacement of the angle-dependent splitting surface by \(t=0\) cannot explain the constant-curvature plane-wave disagreement at the quadratic Weyl order.

## 6. The RNC volume-density sector

The vacuum RNC volume density used in Eq. (76) has the standard quartic structure

\[
\sqrt{|g|}
=
1
-
\frac1{180}
C^{\gamma\alpha}{}_{\mu\nu}
C_{\gamma\rho\alpha\sigma}
x^\mu x^\nu x^\rho x^\sigma
+
\cdots.
\]

At this stage no independent evidence has been found that this universal determinant coefficient is the source of the mismatch.

The exact Kasner agreement with Wang's separate edge-area calculation also argues against a wholesale RNC convention mismatch.

The determinant term should nevertheless be rederived independently in the final generic audit.

## 7. Remaining candidate location

After eliminating:

1. the first-order cone radius;
2. a hidden linear magnetic term;
3. the temporal splitting displacement as a \(C^2\) effect;
4. a simple half-size convention mismatch;

the principal unresolved sector is

\[
\boxed{
\text{the genuine }C^2\text{ part of }r^\pm(t,n)
\text{ in Eq. (74), or its reduction in the radial integral.}
}
\]

This includes the coefficients multiplying:

- \(E_{nn}^2\);
- \(E_i{}^kE_{kj}n^in^j\);
- magnetic quadratic contractions;
- mixed spatial-Weyl contractions;
- terms that may have been removed in forming the abridged expression but can contribute after nonlinear expansion of the radial boundary.

## 8. Why "zero angular mean" is not sufficient at second order

Even if a local first- or intermediate-order angular structure \(f(n)\) obeys

\[
\langle f\rangle=0,
\]

one cannot discard it before applying a nonlinear operation such as

\[
r^3,\quad
r^{d-1},\quad
\sqrt{g(r,n)},\quad
\text{or a perturbed upper limit}.
\]

For example,

\[
\left\langle
(1+\epsilon f)^3
\right\rangle
=
1
+
3\epsilon^2
\langle f^2\rangle
+\cdots
\]

even when

\[
\langle f\rangle=0.
\]

The recovery-functional audit already encountered exactly this type of failure when separately averaged edge-area and cross-normalization anisotropies were factorized.

The same methodological warning applies to the ACD volume derivation.

This observation does not prove that Wang's abridgement committed that error; it identifies the precise consistency condition the full supplemental calculation must satisfy.

## 9. Strongest next calculation

The next calculation should not start from Eq. (74).

Instead it should start from the unabridged RNC world-function/geodesic interval expansion and:

1. solve the null condition for \(r^\pm(t,n)\) through \(O(C^2)\);
2. retain every angular tensor structure;
3. substitute the full local radius into the radial volume integral;
4. expand the nonlinear powers before angular averaging;
5. only then apply the STF angular identities.

This will produce independent universal coefficients \(v_E,v_B\).

The exact-geometry target is

\[
\boxed{
v_E=\frac{17}{630},
\qquad
v_B=\frac1{210}.
}
\]

The published target is

\[
\boxed{
v_E^{\rm W}=\frac{127}{4725},
\qquad
v_B^{\rm W}=\frac1{105}.
}
\]

No choice between these pairs is imposed in the derivation.

## 10. Scientific status

The discrepancy is now localized but not yet traced to a single algebraic line in the published derivation.

The repository should therefore continue to use the wording:

\[
\boxed{
\text{unresolved two-geometry tension with Wang Eq. (79)}
}
\]

rather than

\[
\text{published error}.
\]

A general unabridged \(C^2\) RNC null-cone derivation is the remaining decisive test.
