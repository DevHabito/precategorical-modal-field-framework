# Lemma: odd curvature-jet orders vanish for centered arrow-erasure recovery coefficients

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** symmetry lemma  
**Purpose:** exclude an \(L^3\) correction and isolate the first possible vacuum/Weyl response

## 1. Setting

Let

\[
D_L
=
I(
\exp_o(-LT),
\exp_o(LT)
)
\]

be a centered sufficiently small regular causal diamond.

Let

\[
K_{d,g}(D_L)
\]

be the leading orientation-recovery error coefficient.

The arrow-erased experiment is invariant under exchanging the two tips:

\[
p_L
\leftrightarrow
q_L.
\]

A global reversal of the recovered partial order is already identified as the same reconstruction outcome.

## 2. Central inversion of the tangent diamond

In Riemann normal coordinates at \(o\), consider

\[
\iota:
x^\mu
\mapsto
-x^\mu.
\]

The flat tangent diamond is preserved as a set, while its two tips are exchanged.

The pullback metric is

\[
(\iota^*g)_{\mu\nu}(x)
=
g_{\mu\nu}(-x).
\]

Because \(K\) is diffeomorphism invariant and tip exchange does not change the arrow-erasure experiment,

\[
\boxed{
K[g(x);T]
=
K[g(-x);-T].
}
\]

Since the physical centered diamond determined by \(T\) and \(-T\) is the same unordered pair of tips,

\[
\boxed{
K[g(x);T]
=
K[g(-x);T].
}
\]

## 3. Metric-jet parity

The Riemann-normal-coordinate expansion has the schematic form

\[
g_{\mu\nu}(L\bar x)
=
\eta_{\mu\nu}
+
L^2 g^{(2)}_{\mu\nu}(\bar x)
+
L^3 g^{(3)}_{\mu\nu}(\bar x)
+
L^4 g^{(4)}_{\mu\nu}(\bar x)
+\cdots.
\]

Here:

\[
g^{(2)}
\sim
R\,\bar x^2,
\]

\[
g^{(3)}
\sim
\nabla R\,\bar x^3,
\]

and generally the odd-order coefficients contain odd curvature jets.

Under

\[
\bar x\mapsto-\bar x,
\]

\[
g^{(2j)}
\mapsto
g^{(2j)},
\]

while

\[
g^{(2j+1)}
\mapsto
-g^{(2j+1)}.
\]

The equality of the coefficient functional under central inversion therefore implies that its local Taylor expansion is even in the odd metric jets.

## 4. Exclusion of L^3

The only possible \(O(L^3)\) contribution is linear in the cubic metric jet,

\[
g^{(3)}
\sim
\nabla R_{\mu\nu\rho\sigma}.
\]

Central inversion changes its sign.

But \(K\) is unchanged.

Therefore

\[
\boxed{
K^{(3)}=0.
}
\]

Equivalently,

\[
\boxed{
K_{d,g}(D_L)
=
K_d^{\rm Mink}
+
L^2K_d^{(2)}
+
O(L^4).
}
\]

No \(L^3\) term is allowed.

## 5. Invariant interpretation

The same conclusion follows from the residual symmetry group.

A scalar linear in

\[
\nabla_\lambda
R_{\mu\nu\rho\sigma}
\]

must contract the derivative index with the only distinguished vector \(T\), directly or after Bianchi reductions.

The remaining curvature tensor requires an even number of \(T\)-insertions.

Thus every such scalar contains an odd total number of \(T\)'s and changes sign under

\[
T\mapsto-T.
\]

The centered arrow-erasure coefficient is even under this reversal.

Hence every linear first-derivative curvature scalar is excluded.

## 6. Vacuum consequence

Suppose the spacetime is Ricci flat in a neighborhood of \(o\):

\[
R_{\mu\nu}=0.
\]

Then

\[
R=0,
\qquad
R_{TT}=0.
\]

The \(O(L^2)\) response therefore vanishes.

The symmetry lemma also eliminates \(O(L^3)\).

Hence

\[
\boxed{
K_{d,g}(D_L)
=
K_d^{\rm Mink}
+
O(L^4)
}
\]

in vacuum.

This is stronger than the earlier statement

\[
K=K^{\rm Mink}+o(L^2).
\]

## 7. First possible Weyl response

In vacuum,

\[
R_{\mu\nu\rho\sigma}
=
C_{\mu\nu\rho\sigma}.
\]

At order \(L^4\), the metric expansion and the second variation of \(K\) can generate quantities quadratic in the Weyl tensor.

Relative to \(T\), decompose the Weyl tensor into the spatial tensors

\[
E_{ij}
=
C_{0i0j},
\]

\[
H_{ijk}
=
C_{0ijk},
\]

\[
D_{ijkl}
=
C_{ijkl}.
\]

Rotationally invariant parity-even quadratic scalars include

\[
E^2,
\qquad
H^2,
\qquad
D^2.
\]

Therefore the first vacuum response has the structural candidate form

\[
\boxed{
\frac{
K_{d,g}(D_L)
}{
K_d^{\rm Mink}
}
=
1
+
L^4
\left[
a_dE^2
+
b_dH^2
+
c_dD^2
\right]_o
+
o(L^4),
}
\]

subject to algebraic reductions among these invariants in the chosen dimension.

No values of

\[
a_d,b_d,c_d
\]

are claimed here.

## 8. Linear second-derivative Weyl terms

The fourth Riemann-normal-coordinate jet also contains terms schematically linear in

\[
\nabla\nabla C.
\]

In a vacuum neighborhood, candidate scalar contractions are heavily constrained:

- traces of \(C\) vanish identically;
- divergences of \(C\) vanish by the vacuum Bianchi equations;
- contractions of differentiated trace identities remain zero;
- commuting derivatives introduces curvature times curvature.

Thus on shell, scalar contributions from the linear \(\nabla^2C\) sector either vanish or reduce to quadratic Weyl terms plus total derivative structures that are excluded by the local scalar symmetry.

A full tensor-basis reduction should still be written before treating the three-coefficient quadratic ansatz as publication-ready in arbitrary dimension.

## 9. Literature consistency

Jinzhao Wang's 2019 analysis of small causal diamonds finds that the leading vacuum corrections to causal-diamond geometric observables occur at higher order than the Ricci response and are expressed through quadratic electric/magnetic/spatial Weyl invariants.

This is consistent with the symmetry result above.

It does not determine the project-specific recovery coefficients.

## 10. Scientific consequence

The curvature hierarchy of the centered recovery coefficient is now:

\[
\boxed{
K
=
K_{\rm Mink}
+
L^2(\text{Ricci})
+
L^4(\text{first possible vacuum/Weyl response})
+\cdots.
}
\]

Thus ordinary matter/Ricci curvature perturbs the leading recovery constant two powers of \(L\) earlier than purely vacuum tidal curvature.

The exact \(L^4\) Weyl response is the next curvature-level target.
