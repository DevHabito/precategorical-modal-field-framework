# Bridge 1B — corrected pre-registration for transform closure

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** corrected and frozen before access to author-supplied raw data  
**Empirical status:** not tested  
**Correction:** the original protocol treated phase-averaged data as if the phase-conditioned scalar equation survived averaging exactly. It does not. This version replaces that claim.

## 1. Physical distinction that controls the test

The experiment randomizes the ac phase \(\phi\) between repetitions.

For a fixed phase,

$$
\Gamma_\phi^+(t)
=
\Gamma_0
e^{-A\sin(\omega t+\phi)},
\qquad
A=\beta eS_{\rm AC},
$$

and the transform

$$
G_{c,\phi}(t)
=
\sum_N
\rho_N(t\mid\phi)e^{-cN}
$$

obeys the exact scalar equation

$$
\boxed{
\dot G_{c,\phi}
=
-(1-e^{-c})
\Gamma_\phi^+(t)G_{c,\phi}
+
D(e^c-1).
}
$$

The published phase-averaged transform

$$
\bar G_c
=
\mathbb E_\phi[G_{c,\phi}]
$$

instead obeys

$$
\boxed{
\dot{\bar G}_c
=
-(1-e^{-c})\bar\Gamma\,\bar G_c
+
D(e^c-1)
-
(1-e^{-c})
\operatorname{Cov}_\phi
(\Gamma_\phi^+,G_{c,\phi}).
}
$$

Therefore exact conditioned closure and phase-averaged closure are different empirical questions.

## 2. Primary test — exact phase-conditioned closure

This is now the primary test.

Required data:

- raw trajectories with the applied phase \(\phi\) recorded; or
- phase-conditioned probability distributions \(\rho_N(t\mid\phi)\).

For each phase bin or exact phase value, compute

$$
G_{c,\phi}(t)
=
\sum_N\rho_N(t\mid\phi)e^{-cN}.
$$

Use the independently calibrated

$$
c=2\beta E_{\rm C}
$$

and the known drive to propagate

$$
\dot G_{c,\phi}
=
-a_\phi(t)G_{c,\phi}+b,
$$

with

$$
a_\phi(t)
=
(1-e^{-c})\Gamma_\phi^+(t),
\qquad
b=D(e^c-1).
$$

The exact integral solution is

$$
G_{c,\phi}(t)
=
e^{-A_\phi(t;t_0)}G_{c,\phi}(t_0)
+
b
\int_{t_0}^{t}
e^{-A_\phi(t;s)}\,ds,
$$

where

$$
A_\phi(t;s)
=
\int_s^t a_\phi(u)\,du.
$$

No closure parameter will be fitted.

## 3. Secondary test — phase-averaged coarse model

If only phase-averaged distributions are available, compute

$$
\bar G_c(t)
=
\sum_N\bar\rho_N(t)e^{-cN}.
$$

The paper's coarse-grained approximation uses

$$
\bar\Gamma
=
\Gamma_0I_0(A).
$$

The corresponding approximate scalar model is

$$
\dot G_c^{\rm av}
=
-(1-e^{-c})\bar\Gamma G_c^{\rm av}
+
D(e^c-1).
$$

A comparison between \(\bar G_c\) and \(G_c^{\rm av}\) tests the quality of the published period-averaged approximation.

It is **not** an exact closure test.

## 4. Pre-registered phase-averaging obstruction

For a common phase-independent initial distribution,

$$
G_{c,\phi}(0)=G_0,
$$

the exact and averaged-rate models have the same first derivative.

Their second derivatives differ by

$$
\boxed{
(1-e^{-c})^2
G_0
\Gamma_0^2
\left[
I_0(2A)-I_0(A)^2
\right].
}
$$

This quantity is positive for nonzero drive amplitude.

If sufficiently high-time-resolution phase-averaged data are available, this sign is a predeclared early-time diagnostic.

No claim is made that the experiment has enough temporal resolution to resolve it.

## 5. Secondary commensurate transform

For phase-conditioned data,

$$
G_{2c,\phi}
$$

obeys the exact triangular pair

$$
\dot G_{2c,\phi}
=
\Gamma_\phi^+(t)(e^{-2c}-1)G_{2c,\phi}
+
D(e^{2c}-1)G_{c,\phi}.
$$

This remains the secondary exact closure test.

After phase averaging, additional rate-transform correlations again enter.

## 6. Noncommensurate control

The predeclared control remains

$$
\lambda=\frac32c.
$$

At fixed phase,

$$
\dot G_{3c/2,\phi}
=
\Gamma_\phi^+(t)(e^{-3c/2}-1)G_{3c/2,\phi}
+
D(e^{3c/2}-1)G_{c/2,\phi}.
$$

No autonomous scalar fit for \(G_{3c/2}\) will be introduced after seeing the data.

## 7. Parameter provenance

The following must come from the paper, supplementary information, author metadata, or independent calibration:

- \(E_{\rm C}\);
- temperature \(T\);
- \(\Gamma_0\);
- drive amplitude \(S_{\rm AC}\);
- drive frequency;
- phase convention;
- actual applied phase per trajectory if the primary exact test is attempted;
- detector bandwidth and time resolution;
- state-window information.

## 8. Held-out strategy

### Exact conditioned analysis

Use one initial interval only to determine the measured initial transform.

Propagate the exact phase-conditioned equation with published/calibrated parameters and compare against later phase-conditioned distributions.

### Phase-averaged analysis

Treat the constant-rate equation as the paper's approximation.

Do not label agreement as verification of exact scalar closure.

## 9. Failure interpretation

A failure of the exact phase-conditioned equation would first trigger checks of:

1. phase metadata and synchronization;
2. state-window truncation;
3. detector bandwidth;
4. calibration of \(E_{\rm C}\), \(T\), and \(\Gamma_0\);
5. validity of the published master-equation rates.

A failure of the phase-averaged constant-rate model is much weaker: it can arise simply because the discarded covariance is not negligible.

## 10. Frozen nonclaims

I do not claim that:

- phase-averaged \(G_c\) is exactly scalar-autonomous;
- the paper's replacement \(\Gamma^+(t)\to\Gamma_0I_0(A)\) is exact;
- a successful coarse-model comparison is a new physical law;
- C2 is experimentally verified;
- the closure has a spacetime or pregeometric interpretation.

## 11. Data status

The exact primary test is blocked until phase-resolved raw trajectories or phase-conditioned distributions are obtained.

The published phase-averaged distributions remain useful for testing the coarse-grained approximation and stationary identities, but not for promoting exact conditioned closure.


## 12. Exact phase-averaged stroboscopic test

Although continuous-time phase averaging destroys scalar closure, exact closure is recovered at integer multiples of the drive period.

Let

$$
T=\frac{2\pi}{\omega},
\qquad
q=e^{-c},
$$

and define

$$
\mu_1
=
\exp[-(1-q)\Gamma_0T I_0(A)].
$$

For each fixed phase, the one-period map has the form

$$
G_{c,\phi}((n+1)T)
=
\mu_1G_{c,\phi}(nT)
+
C_\phi.
$$

The homogeneous multiplier is phase-independent.

Averaging over the randomized phase therefore gives the exact recurrence

$$
\bar G_{c,n+1}
=
\mu_1\bar G_{c,n}
+
\bar C.
$$

Eliminating the unknown intercept,

$$
\boxed{
\bar G_{c,n+2}
-
(1+\mu_1)\bar G_{c,n+1}
+
\mu_1\bar G_{c,n}
=
0.
}
$$

This is now the primary exact test available from phase-averaged distributions sampled at integer multiples of \(T\).

The multiplier \(\mu_1\) is fixed from the independently calibrated physical parameters. It will not be fitted from the transform sequence.

## 13. Exact \(2c\) stroboscopic recurrence

Define

$$
\mu_2
=
\exp[-(1-q^2)\Gamma_0T I_0(A)].
$$

Then the phase-averaged \(G_{2c}\) sequence at \(nT\) must satisfy

$$
\boxed{
\bar G_{2c,n+3}
-
(1+\mu_1+\mu_2)\bar G_{2c,n+2}
+
(\mu_1+\mu_2+\mu_1\mu_2)\bar G_{2c,n+1}
-
\mu_1\mu_2\bar G_{2c,n}
=
0.
}
$$

This follows from the common characteristic polynomial of the lower-triangular one-period monodromy matrices.

## 14. Evidence hierarchy after the phase correction

The empirical tests now have three levels.

1. **Exact phase-conditioned continuous-time test:** requires phase-resolved data.
2. **Exact phase-averaged stroboscopic test:** requires only phase-averaged distributions at integer periods.
3. **Approximate phase-averaged continuous-time test:** evaluates the paper's averaged-rate approximation.

These evidence classes must be reported separately.
