# Data request specification for the multi-electron closure test

**Date:** 2026-11-11  
**Target:** Salhani et al., *Physical Review Research* **8**, 023209 (2026)  
**Purpose:** execute the corrected pre-registered test without figure digitization or post-hoc parameter fitting

## 1. Key correction

The experiment randomizes the ac phase between repetitions.

Phase-averaged probabilities alone are **not sufficient** for the primary exact scalar-closure test, because averaging introduces the joint quantity

$$
\mathbb E_\phi[\Gamma_\phi^+G_{c,\phi}].
$$

The primary request is therefore for phase-resolved information.

## 2. Minimum data for the exact primary test

At least one of the following is needed.

### Preferred

Individual electron-count trajectories with:

- measurement times;
- excess-electron number \(N(t)\);
- applied phase \(\phi\) for that repetition;
- drive start time and synchronization information.

### Acceptable alternative

Phase-conditioned distributions

$$
\rho_N(t\mid\phi)
$$

on documented phase bins, with:

- time points;
- state labels \(N\);
- phase-bin definitions;
- counts contributing to each bin;
- state-window and missing-tail information.

Without phase information, the exact conditioned test cannot be executed.

## 3. Data still useful if only phase-averaged values are available

A machine-readable table of

$$
\bar\rho_N(t)
$$

remains useful for:

- testing the paper's constant-rate coarse-grained approximation;
- calculating \(\bar G_c(t)\);
- stationary discrete-normal checks;
- the \(\Delta_c\) transient diagnostic;
- comparison with numerical master-equation results.

Such an analysis will be labeled **phase-averaged approximate-model test**, not exact closure validation.

## 4. Requested physical metadata

If available:

- \(E_{\rm C}\) and uncertainty;
- temperature and uncertainty;
- \(\Gamma_0\) and uncertainty;
- \(S_{\rm AC}\);
- \(\omega_{\rm AC}\);
- phase convention;
- actual phase values used for each repetition;
- detector sampling rate and bandwidth;
- missed-transition corrections;
- number of repetitions;
- processed arrays behind the transient probability figures;
- numerical master-equation output used for the solid curves.

## 5. Frozen exact test

For each phase-conditioned ensemble,

$$
G_{c,\phi}(t)
=
\sum_N
\rho_N(t\mid\phi)e^{-cN},
\qquad
c=\frac{2E_{\rm C}}{k_{\rm B}T}.
$$

The exact predicted equation is

$$
\dot G_{c,\phi}
=
-(1-e^{-c})
\Gamma_0e^{-A\sin(\omega t+\phi)}
G_{c,\phi}
+
D(e^c-1).
$$

No target-dependent parameter will be fitted.

## 6. Frozen phase-averaged comparison

For phase-averaged data, the paper's approximation uses

$$
\bar\Gamma
=
\Gamma_0I_0(A).
$$

The corresponding scalar equation is an **approximation**.

The exact phase-averaged equation contains the covariance

$$
\operatorname{Cov}_\phi
(\Gamma_\phi^+,G_{c,\phi}).
$$

Agreement with the constant-rate model therefore assesses approximation quality, not exact closure.

## 7. Reproducibility rules

If data are received:

- preserve source files unchanged;
- record cryptographic checksums;
- do not redistribute data unless permission allows it;
- document units and phase conventions;
- freeze analysis code before the held-out comparison;
- record every deviation from the pre-registration.

No plotted pixel values will be presented as original raw data.
