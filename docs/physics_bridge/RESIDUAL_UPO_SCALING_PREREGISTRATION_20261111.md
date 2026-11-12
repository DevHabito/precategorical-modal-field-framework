# Residual UPO scaling after adjacent twins — preregistration

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** frozen structural scaling hypothesis before the held-out runs below  
**Scope:** fixed-cardinality \(3+1\) Minkowski sprinklings

## 1. Residual event

Let

\[
T_n
\]

be the number of adjacent twin pairs.

Let

\[
k_\Gamma
\]

be the number of inverse implication-class pairs of the comparability graph, so a nonempty graph is UPO exactly when

\[
k_\Gamma=1.
\]

Define

\[
\boxed{
q_4^{\mathrm{res}}(n)
=
P(
k_\Gamma>1,\,
T_n=0
).
}
\]

The adjacent-twin theorem already proves

\[
P(T_n>0)
=
O(n^{-1}).
\]

This note freezes a prediction for what remains after that leading obstruction is removed.

## 2. Stable-twin quotient observation

A stable module is an independent set whose members have identical adjacency to every outside vertex.

Equivalently, its members are **false twins**: they have identical open neighborhoods.

Collapse every maximal false-twin class to one quotient vertex.

Finite exploratory audits show that most internal non-UPO failures remaining after raw adjacent twins are removed become adjacent twins in this quotient.

The smallest original configuration represented by such a quotient pair is a three-vertex \(P_3\)-type module:

- two false-twin endpoints;
- one center adjacent to both;
- the whole triple externally indistinguishable.

This is the first modular obstruction not already counted by \(T_n\).

## 3. Geometric scaling hypothesis

In the critical \(3+1\) null-waist regime:

- locating the first point in the relevant waist layer costs probability \(O(n^{-1})\);
- each additional point that must remain in the same causal/angular microconfiguration contributes an additional \(O(n^{-2})\) phase-space factor;
- choosing an \(m\)-tuple contributes \(O(n^m)\).

Therefore a minimal externally indistinguishable block of size \(m\) is predicted to have expected count on the scale

\[
n^m
n^{-[1+2(m-1)]}
=
n^{1-m}.
\]

The already proved case

\[
m=2
\]

gives

\[
n^{-1},
\]

consistent with

\[
E[T_n]\sim\frac{9\pi}{n}.
\]

The next predicted level is

\[
m=3:
\qquad
O(n^{-2}).
\]

This motivates the frozen residual hypothesis

\[
\boxed{
q_4^{\mathrm{res}}(n)
=
O(n^{-2}).
}
\]

No limiting constant is preregistered.

## 4. Held-out protocol

The following sizes are reserved for the prospective finite check:

\[
\boxed{
n=144,\qquad n=176.
}
\]

They were not used in deriving the exponent.

Target sample counts:

\[
8000
\]

trials at \(n=144\), and

\[
6000
\]

trials at \(n=176\).

Frozen seeds:

\[
202611114144,
\qquad
202611114176.
\]

Primary diagnostic:

\[
\boxed{
n^2\,
\widehat q_4^{\mathrm{res}}(n).
}
\]

Under the frozen hypothesis, this quantity should remain order one rather than grow polynomially with \(n\).

Secondary classification:

1. raw adjacent twin;
2. residual multiple nontrivial components;
3. adjacent twin after false-twin quotient;
4. deeper residual not explained by either of the previous two mechanisms.

## 5. Claim discipline

The held-out test can only provide finite consistency evidence.

It cannot prove

\[
q_4^{\mathrm{res}}(n)=O(n^{-2}).
\]

A proof would require geometric bounds for externally indistinguishable blocks of size at least three and for disconnected nontrivial components.

No exponent will be altered after inspecting the frozen runs without opening a new hypothesis.
