# A38.1 — Corrected Gauge-Compatible Coarse-Graining Audit

## Corrective gate note

The original A38 used a 70% empirical failure-rate threshold to reject closure
of weighted medians. That threshold measured prevalence, not the universal
closure property. A single exact counterexample is logically decisive.
A38.1 preserves the original result and replaces only that misaligned gate
with an explicit counterexample; all other gates and tolerances are unchanged.

## Translation-covariant decomposable means

Within the class of continuous strictly monotone weighted quasi-arithmetic
means

\[
M_f(q;\mu)
=
f^{-1}
\left(
\frac{\sum_i\mu_i f(q_i)}
{\sum_i\mu_i}
\right),
\]

decomposability is automatic when a block passes its mass and its mean.
Requiring translation covariance

\[
M_f(q+c;\mu)=M_f(q;\mu)+c
\]

restricts the generator, up to equivalent affine changes, to two families:

1. \(f(q)=q\), giving the weighted arithmetic mean;
2. \(f(q)=e^{kq}\), giving the exponential or log-sum-exp means.

Thus gauge covariance and hierarchical decomposability do not select a unique
coarse variable. They select arithmetic and exponential families inside the
audited regular mean class.

## Observable-relative sufficiency

The arithmetic mean exactly preserves the first weighted moment.

For the exponential microscopic weight

\[
w_i=\mu_i e^{-\lambda q_i},
\]

the exact block message is

\[
W_B=\sum_{i\in B}\mu_i e^{-\lambda q_i}.
\]

Equivalently, a block may pass

\[
\mu_B=\sum_{i\in B}\mu_i,
\qquad
Q_B=-\lambda^{-1}\log(W_B/\mu_B).
\]

Then

\[
W_B=\mu_Be^{-\lambda Q_B}
\]

and nested aggregation is exact. Replacing \(Q_B\) by the arithmetic mean,
median, or minimum generally does not preserve the exponential observable.

## Dynamic graph obstruction

A microscopic row-stochastic kernel \(K_{ij}\) does not determine a unique
macro transition from a source region \(A\) unless a conditional source
occupancy \(\rho(i\mid A)\) is supplied:

\[
K^{\mathrm{macro}}_{AB}
=
\sum_{i\in A}\rho(i\mid A)
\sum_{j\in B}K_{ij}.
\]

Different occupancies on the same microscopic graph can give different macro
kernels.

If a global occupancy \(\pi_i\) is supplied, the joint flow

\[
F_{ij}=\pi_iK_{ij}
\]

aggregates exactly:

\[
F_{AB}=\sum_{i\in A,j\in B}F_{ij},
\qquad
K^{\mathrm{macro}}_{AB}
=
F_{AB}/\pi_A.
\]

## Boundary

The audit selects sufficient messages relative to declared observables. It
does not prove that the exponential kernel is physical, derive lambda, or
supply the source occupancy required for dynamic graph coarse-graining.
