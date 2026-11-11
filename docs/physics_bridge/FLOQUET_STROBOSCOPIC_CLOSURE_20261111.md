# Exact Floquet and stroboscopic closure under randomized phase

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact analytic consequence of the phase-conditioned transform hierarchy  
**Novelty status:** Floquet/monodromy theory is classical; model-specific recurrence priority not certified

## 1. Motivation

Random-phase averaging destroys the continuous-time scalar closure of the conditioned transform \(G_c\).

That does not mean every reduced description is lost after marginalization.

The drive is periodic. At integer multiples of the drive period, the phase-conditioned transform hierarchy has a monodromy matrix. Its diagonal Floquet multipliers are independent of the phase shift.

This produces exact stroboscopic recurrences that survive phase averaging.

## 2. Conditioned commensurate hierarchy

Let

$$
q=e^{-c}\in(0,1),
$$

and define

$$
H_j(t,\phi)=G_{jc,\phi}(t),
\qquad
H_0=1.
$$

For a fixed phase,

$$
\dot H_j
=
-(1-q^j)\Gamma_\phi^+(t)H_j
+
D(q^{-j}-1)H_{j-1},
$$

with

$$
\Gamma_\phi^+(t)
=
\Gamma_0e^{-A\sin(\omega t+\phi)}.
$$

For \(j=0,\ldots,m\), the augmented vector

$$
X_m=(H_0,H_1,\ldots,H_m)^\top
$$

satisfies a linear lower-triangular periodic system.

## 3. Exact Floquet multipliers

Let

$$
T=\frac{2\pi}{\omega}.
$$

The diagonal equation at level \(j\ge1\) has coefficient

$$
-(1-q^j)\Gamma_\phi^+(t).
$$

Therefore the \(j\)-th diagonal element of the one-period fundamental matrix is

$$
\mu_j
=
\exp\left[
-(1-q^j)
\int_0^T
\Gamma_\phi^+(t)\,dt
\right].
$$

The full-period integral is independent of the phase shift:

$$
\int_0^T
\Gamma_0e^{-A\sin(\omega t+\phi)}\,dt
=
\Gamma_0T I_0(A).
$$

Hence

$$
\boxed{
\mu_0=1,
\qquad
\mu_j
=
\exp[-(1-q^j)\Gamma_0T I_0(A)].
}
$$

Every phase-conditioned monodromy matrix is lower triangular and has the same diagonal multipliers.

The off-diagonal entries can depend on phase.

## 4. Exact scalar stroboscopic closure for \(G_c\)

For \(m=1\), each fixed phase has a one-period affine map

$$
H_{1,n+1}^{(\phi)}
=
\mu_1H_{1,n}^{(\phi)}
+
C_\phi,
$$

where

$$
H_{1,n}^{(\phi)}
=
G_{c,\phi}(nT),
$$

and \(C_\phi\) is the phase-dependent particular contribution accumulated over one period.

Because the same phase is retained along a trajectory and the coefficient is periodic, \(C_\phi\) is the same on every cycle.

Average over the phase ensemble:

$$
\boxed{
\bar H_{1,n+1}
=
\mu_1\bar H_{1,n}
+
\bar C.
}
$$

No assumption of independence between \(H_{1,n}^{(\phi)}\) and \(\phi\) is needed because \(\mu_1\) is phase-independent.

Thus random-phase marginalization, which destroys continuous-time scalar closure, preserves an exact scalar affine map at stroboscopic times.

## 5. Intercept-free three-point test

The unknown averaged intercept can be removed.

From

$$
\bar H_{n+1}=\mu_1\bar H_n+\bar C,
$$

it follows that

$$
\boxed{
\bar H_{n+2}
-
(1+\mu_1)\bar H_{n+1}
+
\mu_1\bar H_n
=
0.
}
$$

Equivalently,

$$
\boxed{
\bar H_{n+2}-\bar H_{n+1}
=
\mu_1
(\bar H_{n+1}-\bar H_n).
}
$$

The multiplier is fixed before data analysis:

$$
\boxed{
\mu_1
=
\exp[-(1-e^{-c})\Gamma_0T I_0(A)].
}
$$

This gives an exact phase-averaged test that does not require phase metadata, provided the distributions are evaluated at integer multiples of the drive period.

## 6. Higher hierarchy and Cayley-Hamilton recurrence

For the augmented hierarchy through \(H_m\), let \(M_\phi\) be the one-period monodromy matrix.

It is lower triangular with eigenvalues

$$
\mu_0,\mu_1,\ldots,\mu_m,
$$

independent of \(\phi\).

Therefore every \(M_\phi\) has the same characteristic polynomial

$$
P_m(z)
=
\prod_{j=0}^{m}(z-\mu_j).
$$

By Cayley-Hamilton,

$$
P_m(M_\phi)=0.
$$

Let \(E\) denote the one-period forward shift in the cycle index \(n\).

For every phase-conditioned trajectory,

$$
P_m(E)X_{m,n}^{(\phi)}=0.
$$

Averaging over phase preserves this linear identity:

$$
\boxed{
P_m(E)\bar X_{m,n}=0.
}
$$

In particular,

$$
\boxed{
\prod_{j=0}^{m}(E-\mu_j)
\,
\overline{G_{mc}}(nT)
=
0.
}
$$

This is an exact finite stroboscopic recurrence for the phase-averaged commensurate transform.

## 7. Explicit \(m=2\) recurrence

For

$$
\lambda=2c,
$$

the roots are

$$
1,\mu_1,\mu_2.
$$

Thus

$$
\boxed{
\bar H_{2,n+3}
-
(1+\mu_1+\mu_2)\bar H_{2,n+2}
+
(\mu_1+\mu_2+\mu_1\mu_2)\bar H_{2,n+1}
-
\mu_1\mu_2\bar H_{2,n}
=
0.
}
$$

Again, no phase-resolved observation is needed to test this recurrence at stroboscopic times.

## 8. Relationship to the continuous-time obstruction

There is no contradiction.

At arbitrary time,

$$
\dot{\bar G}_c
$$

contains the hidden covariance

$$
\operatorname{Cov}_\phi
(\Gamma_\phi^+,G_{c,\phi}).
$$

At a full drive period, the conditional linear maps all share the same homogeneous multiplier.

The stroboscopic map therefore compresses one complete cycle in a way that removes the continuously varying hidden correlation from the recurrence coefficients.

The logical structure is

$$
\boxed{
\text{continuous-time marginal closure fails}
\quad\text{but}\quad
\text{period-sampled closure can be exact}.
}
$$

This is a useful warning against treating “closure” as independent of temporal resolution.

## 9. Generality

The derivation does not depend specifically on a sinusoid until the Bessel expression is used.

For any positive periodic rate \(B_\phi(t)\) obtained by phase-shifting one period-\(T\) waveform,

$$
\mu_j
=
\exp\left[
-(1-q^j)
\int_0^T B(t)\,dt
\right]
$$

is phase-independent.

The sinusoidal electronic drive gives the explicit integral

$$
\int_0^T B(t)\,dt
=
\Gamma_0T I_0(A).
$$

## 10. Literature boundary

Floquet theory, monodromy matrices, and periodically driven Markov processes are classical topics.

The project does not claim novelty for:

- Floquet multipliers;
- monodromy matrices;
- Cayley-Hamilton recurrences;
- periodic Markov dynamics;
- Bessel averaging of a sinusoidal exponential rate.

The model-specific contribution recorded here is the explicit application to the exact commensurate transform hierarchy and the observation that stroboscopic sampling restores a finite phase-averaged recurrence after continuous-time phase marginalization destroys closure.

Absolute priority for that formulation is not certified.

## 11. Empirical use

This result materially improves the data plan.

If only phase-averaged distributions are available, exact tests remain possible at

$$
t=nT.
$$

For \(G_c\), three consecutive stroboscopic transform values are sufficient for the intercept-free recurrence.

For \(G_{2c}\), four consecutive values test the third-order recurrence.

The multipliers are fixed by independently calibrated physical parameters.

No fitted closure coefficient is required.
