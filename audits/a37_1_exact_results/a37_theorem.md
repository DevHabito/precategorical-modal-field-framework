# A37.1 — Corrected Noise-Law Universality Audit

## Corrective numerical note

The original A37 evaluated the stationary Gaussian log-MGF through a long
floating-point series. The true Gaussian block error is identically zero,
but accumulated errors of order \(10^{-15}\) violated a strict monotonicity
check. A37.1 uses the exact closed form \(\log M_X(s)=s^2/2\). Scientific
thresholds and non-Gaussian calculations are unchanged.

## Stationary affine law

For

\[
X_{t+1}=aX_t+\xi_t,\qquad |a|<1,
\]

with iid innovations independent of the past, the stationary characteristic
function is

\[
\phi_X(t)=\prod_{k=0}^{\infty}\phi_\xi(a^k t).
\]

When the cumulants exist,

\[
\kappa_r(X)=\frac{\kappa_r(\xi)}{1-a^r}.
\]

Matching innovation means and variances therefore fixes the stationary mean
and variance, but not higher cumulants.

## Exponential-score obstruction

The stationary effective score is

\[
Q_\lambda
=
-\lambda^{-1}\log E[e^{-\lambda X}].
\]

It depends on all cumulants for which the expansion is valid. Heavy-tailed
laws such as Student-t have no nonzero moment-generating function, so
\(Q_\lambda\) is not finite even though their variance may exist.

## Conditional coarse-graining universality

For \(M\) independent stationary copies,

\[
Y_M=M^{-1/2}\sum_{i=1}^{M}X_i,
\]

the log-MGF is

\[
\log E[e^{sY_M}]
=
M\log M_X(s/\sqrt M).
\]

If exponential moments are controlled near zero, the effective score tends
to the Gaussian value as \(M\to\infty\). Weak CLT convergence alone does not
guarantee convergence of exponential moments.

## Dependence obstruction

A shared non-Gaussian common factor can survive variance-normalized
coarse-graining. Independence or an adequate mixing condition is therefore
required for Gaussian universality.

## Boundary

The audit establishes conditional universality classes. It does not identify
the physical RZS innovation law or demonstrate independence across relational
components.
