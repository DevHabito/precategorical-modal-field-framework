# A35 — Gaussian Closure and Innovation-Law Audit

## Affine Gaussian invariance

Let

\[
X_{t+1}=b+aX_t+\xi_t,
\]

where \(X_t\) is Gaussian and \(\xi_t\) is independent Gaussian noise. Then
\(X_{t+1}\) is Gaussian with

\[
m_{t+1}=b+am_t,
\qquad
v_{t+1}=a^2v_t+v_\xi.
\]

For a Gaussian law,

\[
Q_\lambda
=
-\lambda^{-1}\log E[e^{-\lambda X}]
=
m-\frac{\lambda}{2}v.
\]

Thus mean and variance form an exact finite-dimensional closure only inside
the Gaussian family.

## Cumulant recurrence

For independent affine innovations,

\[
\kappa_r(X_{t+1})
=
a^r\kappa_r(X_t)+\kappa_r(\xi_t)
\]

for \(r\ge2\), with the usual affine rule for the mean. Gaussian innovations
have no cumulants above order two, so initial higher cumulants decay as
\(a^{rt}\) when \(|a|<1\).

Non-Gaussian innovations continuously regenerate higher cumulants. Their
stationary values are

\[
\kappa_r^*
=
\frac{\kappa_r(\xi)}{1-a^r}.
\]

Therefore a Gaussian stationary closure is not valid unless the innovation
law is Gaussian or satisfies equivalent higher-cumulant restrictions.

## Centering is not Gaussianization

The map \(\epsilon\mapsto\epsilon-\bar\epsilon\) is linear. It preserves
Gaussianity when the input is Gaussian, but it does not generally transform
non-Gaussian input into Gaussian noise.

## Finite empirical caveat

Even when the population law is exactly Gaussian, the finite empirical
quantity

\[
-\lambda^{-1}\log\left(n^{-1}\sum_i e^{-\lambda q_i}\right)
\]

is a random estimator, not exactly \(m-\lambda v/2\). Its uncertainty depends
strongly on both sample size and \(\lambda\).

## Boundary

The current RZS contract specifies centered noise but does not, in the
materials audited here, derive a Gaussian innovation law. Gaussian closure is
therefore conditional, not established as an RZS law.
