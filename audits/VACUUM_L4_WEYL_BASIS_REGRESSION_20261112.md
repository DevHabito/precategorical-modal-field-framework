# Audit: random algebraic-Weyl regression for the vacuum L4 invariant basis

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** executed computational regression  
**Target:** VACUUM_L4_WEYL_INVARIANT_BASIS_20261112.md

## 1. Purpose

The analytic theorem predicts that the parity-even quadratic invariant space seen by a centered observer-dependent scalar has:

\[
\operatorname{rank}=2
\]

in spacetime dimension

\[
d=4,
\]

and

\[
\operatorname{rank}=3
\]

for

\[
d\ge5.
\]

This audit tests the algebra on random Weyl tensors without imposing any special spacetime metric or Petrov/Weyl type.

## 2. Tensor generation

Random algebraic Riemann tensors were generated as sums of Kulkarni--Nomizu products of random symmetric bilinear forms.

They were projected to the Weyl tensor using the Lorentz-signature Ricci/scalar trace subtraction.

For each sample, the regression checked:

- algebraic Bianchi identity;
- full Lorentzian trace-freeness;
- the spatial trace identity
  \[
  \delta^{kl}D_{kilj}=E_{ij}.
  \]

## 3. Redundant invariant list

For every random Weyl tensor the following eight contractions were recorded:

\[
E^2,
\]

\[
H^2,
\]

\[
D^2,
\]

\[
E^{ij}D^k{}_{ikj},
\]

\[
(D^k{}_{ikj})(D_l{}^{ilj}),
\]

\[
D_{ijkl}D^{ikjl},
\]

\[
H_{ijk}H^{jik},
\]

\[
H_{ijk}H^{kij}.
\]

The numerical matrix of these contractions was then subjected to singular-value rank analysis.

## 4. Executed regression

Parameters:

\[
30
\]

random Weyl tensors per dimension, with fixed reproducible random seed

\[
20261112.
\]

### d = 4

Observed rank:

\[
\boxed{2}.
\]

Leading singular values:

\[
1.18548237\times10^3,
\]

\[
4.35528057\times10^2,
\]

followed by

\[
1.02\times10^{-13},
\qquad
5.15\times10^{-14}.
\]

Maximum algebraic residuals were below

\[
3.6\times10^{-15}.
\]

### d = 5

Observed rank:

\[
\boxed{3}.
\]

Leading singular values:

\[
4.93292356\times10^3,
\]

\[
7.09798429\times10^2,
\]

\[
4.46889846\times10^2,
\]

followed by

\[
5.60\times10^{-13}.
\]

Maximum algebraic residuals were below

\[
2.9\times10^{-15}.
\]

### d = 6

Observed rank:

\[
\boxed{3}.
\]

Leading singular values:

\[
1.47343045\times10^4,
\]

\[
1.15074348\times10^3,
\]

\[
7.06440538\times10^2,
\]

followed by

\[
3.37\times10^{-12}.
\]

Maximum algebraic residuals were below

\[
5.4\times10^{-15}.
\]

### d = 7

Observed rank:

\[
\boxed{3}.
\]

Leading singular values:

\[
3.47403355\times10^4,
\]

\[
2.05197956\times10^3,
\]

\[
9.26666132\times10^2,
\]

followed by

\[
8.93\times10^{-12}.
\]

Maximum algebraic residuals were below

\[
7.2\times10^{-15}.
\]

## 5. Contraction identities

Every executed sample reproduced, to floating-point precision,

\[
\boxed{
E^{ij}D^k{}_{ikj}=E^2,
}
\]

\[
\boxed{
D_{ijkl}D^{ikjl}=\frac12D^2,
}
\]

\[
\boxed{
H_{ijk}H^{jik}=\frac12H^2,
}
\]

and

\[
\boxed{
H_{ijk}H^{kij}=-\frac12H^2.
}
\]

For

\[
d=4,
\]

the regression also reproduced

\[
\boxed{
D^2=4E^2.
}
\]

## 6. Interpretation

The regression provides no evidence for an additional independent parity-even quadratic Weyl scalar beyond:

### d = 4

\[
E^2,
\qquad
B^2
\]

or equivalently

\[
E^2,
\qquad
H^2.
\]

### d >= 5

\[
E^2,
\qquad
H^2,
\qquad
D^2.
\]

This is consistent with the analytic spatial irreducible decomposition.

## 7. Reproducibility

The reusable repository script is

\[
\texttt{tools/verify\_vacuum\_weyl\_quadratic\_basis.py}.
\]

The present audit records an equivalent in-session NumPy execution of the same algebraic construction and contraction tests.

The regression is not used as a proof of the invariant-basis theorem.
