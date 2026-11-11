# Bridge 1B — pre-registration for the scalar and finite transform closures

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** frozen analytic protocol before access to author-supplied raw data  
**Empirical status:** not tested

## 1. Purpose

The published multi-electron master equation implies an exact transform shift

$$
\dot G_\lambda
=
\Gamma^+(t)(e^{-\lambda}-1)G_\lambda
+
D(e^\lambda-1)G_{\lambda-c},
$$

where

$$
c=2\beta E_{\rm C},
\qquad
D=\Gamma_0e^{-\beta E_{\rm C}}.
$$

The purpose of this pre-registration is to freeze a data test before access to the underlying time-resolved distributions.

The test asks whether the transform coordinates derived from the measured \(\rho_N(t)\) obey the exact reduced equations implied by the published master equation.

Passing this test would validate the reduction against the experiment within that physical model. It would **not** establish a new law of nature.

## 2. Primary observable: the physically selected scalar closure

Set

$$
\lambda=c.
$$

Because \(G_0=1\),

$$
\boxed{
\dot G_c
=
-\Gamma^+(t)(1-e^{-c})G_c
+
D(e^c-1).
}
$$

Define

$$
a(t)=\Gamma^+(t)(1-e^{-c}),
\qquad
b=D(e^c-1).
$$

Then

$$
\dot G_c=-a(t)G_c+b.
$$

No empirical closure parameter appears in this equation.

The transform parameter \(c\) is fixed by the physical charging-energy scale and temperature,

$$
c=2\beta E_{\rm C}.
$$

It is not selected by looking at the transform data.

## 3. Integral prediction

For an initial time \(t_0\), define

$$
A(t;s)=\int_s^t a(u)\,du.
$$

The exact solution is

$$
\boxed{
G_c(t)
=
e^{-A(t;t_0)}G_c(t_0)
+
b\int_{t_0}^{t}e^{-A(t;s)}\,ds.
}
$$

This form will be used for the empirical comparison.

The integral formulation is preferred to a finite-difference estimate of \(\dot G_c\), because numerical differentiation would amplify measurement noise and introduce a discretionary smoothing scale.

## 4. Constant-rate stationary prediction

If the effective birth rate is constant,

$$
\Gamma^+(t)=\Gamma^+,
$$

then the scalar equation has stationary value

$$
\boxed{
G_c^{\rm ss}
=
\frac{\Gamma_0e^{\beta E_{\rm C}}}{\Gamma^+}.
}
$$

This follows algebraically from

$$
\frac{e^c-1}{1-e^{-c}}=e^c.
$$

If the published phase-averaged model is used, its independently specified effective birth rate must be inserted here. No stationary transform value will be fitted from the measured \(\rho_N\).

## 5. Secondary finite closure

Set

$$
\lambda=2c.
$$

Then

$$
\dot G_{2c}
=
\Gamma^+(t)(e^{-2c}-1)G_{2c}
+
D(e^{2c}-1)G_c.
$$

Together with the scalar equation for \(G_c\), this gives an exact two-dimensional triangular system.

The empirical comparison will propagate the pair

$$
(G_c,G_{2c})
$$

from the initial measured values using only the published physical parameters.

## 6. Noncommensurate control

Fix, before data access,

$$
\boxed{\lambda=\frac32c.}
$$

Then

$$
\dot G_{3c/2}
=
\Gamma^+(t)(e^{-3c/2}-1)G_{3c/2}
+
D(e^{3c/2}-1)G_{c/2}.
$$

The derivative depends on an additional transform \(G_{c/2}\).

This control has a specific purpose: it checks that the apparent closure at \(c\) is not being manufactured by a generic one-score fitting procedure.

I will not fit an autonomous scalar differential equation for \(G_{3c/2}\) after inspecting the data.

## 7. Data reduction

At every available time point,

$$
G_\lambda(t)
=
\sum_N \rho_N(t)e^{-\lambda N}.
$$

The state range used in the sum will be exactly the state range supplied by the experimental data.

If the published measurement window omits non-negligible tail probability, the transform will be marked as truncated and the missing-mass uncertainty must be propagated. No renormalization of a truncated state window will be performed silently.

## 8. Parameter provenance

The following quantities must come from the publication, supplementary material, author-supplied metadata, or independently documented calibration:

- \(E_{\rm C}\);
- temperature \(T\), hence \(\beta=1/(k_{\rm B}T)\);
- \(\Gamma_0\);
- drive waveform \(V(t)\) or the published effective birth rate;
- time origin and phase convention;
- measured \(\rho_N(t_0)\).

No parameter may be chosen to minimize the closure residual unless the resulting analysis is explicitly relabeled exploratory.

## 9. Held-out protocol

When sufficiently resolved time-series data are obtained:

1. choose an initial time interval used only to establish \(G_c(t_0)\) and \(G_{2c}(t_0)\);
2. propagate the scalar and two-dimensional systems with the published rates;
3. compare the propagated transforms with transform values calculated directly from later measured distributions;
4. keep the later time points held out from parameter calibration.

If repeated traces are available, uncertainty will be estimated by resampling complete trajectories rather than treating state probabilities at different times as independent observations.

## 10. Primary failure criterion

The exact theory predicts the integral residual

$$
\mathcal R_c(t)
=
G_c(t)
-
e^{-A(t;t_0)}G_c(t_0)
-
b\int_{t_0}^{t}e^{-A(t;s)}\,ds
$$

to vanish.

The empirical bridge fails its scalar-closure test if the residual is statistically inconsistent with zero after propagating:

- occupancy uncertainty;
- uncertainty in \(E_{\rm C}\);
- temperature uncertainty;
- transition-rate calibration uncertainty;
- state-window truncation;
- time/phase uncertainty.

A numerical tolerance will not be invented before these experimental uncertainties are known.

## 11. Interpretation of possible outcomes

### Pass

A pass would show that one physically selected exponential transform is an experimentally adequate exact reduced coordinate **within the published Markov model and experimental uncertainty**.

It would not show that \(Q_\lambda\) is fundamental.

### Fail

A failure would not automatically establish new physics.

The first checks would be:

1. state truncation;
2. parameter mismatch;
3. detector bandwidth and finite-time resolution;
4. drive-phase averaging;
5. breakdown of the published rate model;
6. only then, inadequacy of the proposed bridge mapping.

### Difference between \(c\) and \(3c/2\)

If \(G_c\) follows the scalar equation while \(G_{3c/2}\) requires the measured \(G_{c/2}\), the data would exhibit the parameter-selective closure predicted analytically.

That would be evidence for the **closure structure of the published model**, not evidence for a new fundamental law.

## 12. Frozen nonclaims

Before data access I explicitly do not claim:

- that the experiment has already passed this test;
- that the scalar closure is novel in birth-death theory;
- that \(G_c\) is uniquely optimal among all reduced observables;
- that C2 is experimentally verified;
- that the closure has a spacetime or pregeometric meaning;
- that a failure would falsify stochastic thermodynamics.

## 13. Data status

The 2026 article is open access, but its supporting raw data are not presently public through the article. The publication states that supporting data can be requested from the authors.

Therefore the protocol remains frozen at the analytic stage until suitable data are obtained.


## 14. Pre-registered relaxation-mode check

For the phase-averaged constant-rate model, the scalar closure predicts

$$
G_c(t)-G_c^{\rm ss}
=
[G_c(t_0)-G_c^{\rm ss}]
e^{-a_c(t-t_0)},
$$

with

$$
\boxed{
a_c=\Gamma^+(1-e^{-c}).
}
$$

This supplies a direct secondary test.

After \(G_c(t)\) is computed from the measured distributions, the residual mode

$$
H_c(t)=G_c(t)-G_c^{\rm ss}
$$

will be compared with the predetermined exponential decay.

The decay rate \(a_c\) will be calculated from the published/calibrated physical parameters. It will not be fitted from the held-out \(G_c(t)\) curve.

If the full time-dependent rate rather than the constant phase-averaged approximation is used, this exponential test will be replaced by the already frozen integral solution rather than forcing a constant-rate fit.
