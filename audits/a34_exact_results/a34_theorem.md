# A34 — Effective Score and Dynamic Closure

## Definition
For positive masses \(\mu_i\) with \(\sum_i\mu_i=1\),
\[
Q_\lambda(q,\mu)=-\frac1\lambda\log\sum_i\mu_i e^{-\lambda q_i}.
\]

## Associative aggregation
For a partition into groups \(G\), let \(\mu_G=\sum_{i\in G}\mu_i\) and
\(Q_G=Q_\lambda(q_G,\mu_G^{-1}\mu|_G)\). Then
\[
Q_\lambda(q,\mu)
=-\frac1\lambda\log\sum_G\mu_G e^{-\lambda Q_G}.
\]
Thus exact aggregation requires carrying both group mass and group effective
score.

## Gauge and affine covariance
\[
Q_\lambda(q+c)=Q_\lambda(q)+c,
\]
and for \(a>0\),
\[
Q_\lambda(aq+c)=c+aQ_{a\lambda}(q).
\]

## Cumulant expansion
Writing weighted cumulants \(\kappa_n\),
\[
Q_\lambda=\kappa_1-\frac\lambda2\kappa_2
+\frac{\lambda^2}{6}\kappa_3
-\frac{\lambda^3}{24}\kappa_4+\cdots.
\]
Mean and variance are insufficient at finite lambda because higher cumulants
contribute.

## Dynamic closure obstruction
For centered affine contraction
\[
q_i'=\bar q+a(q_i-\bar q),
\]
\[
Q_\lambda'= (1-a)\bar q+aQ_{a\lambda}.
\]
Therefore a scalar \(Q_\lambda\) at one fixed lambda is not generally closed.
Two microdistributions can have the same mean and the same \(Q_\lambda\), but
different \(Q_{a\lambda}\), and hence different next macro scores.

Exact deterministic closure is available if one carries the mean and the
whole log-partition curve in lambda. This is an infinite-dimensional macro
state unless an independently justified finite-dimensional distribution
family is invariant under the dynamics.

## Boundary
Static associativity does not establish autonomous macrodynamics. No physical
interpretation of Q, thermodynamic free energy, or exact RZS closure is claimed.
