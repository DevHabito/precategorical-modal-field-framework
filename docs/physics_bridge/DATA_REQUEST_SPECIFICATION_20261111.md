# Data request specification for the multi-electron closure test

**Date:** 2026-11-11  
**Target article:** Salhani, Chida, Shimizu, Hayashi, Nishiguchi, *Physical Review Research* **8**, 023209 (2026)  
**Corresponding author listed by APS:** Katsuhiko Nishiguchi  
**Purpose:** execute the pre-registered transform-closure test without figure digitization or post-hoc parameter fitting

## 1. Why the data are needed

The published article states that the supporting data are not publicly available and are available from the authors upon reasonable request.

The bridge protocol was frozen before access to those data.

The primary test concerns the transform

$$
G_c(t)=\sum_N\rho_N(t)e^{-cN},
\qquad
c=2E_{\rm C}/(k_{\rm B}T).
$$

The published master equation predicts an exact scalar reduced dynamics for \(G_c\). A second test uses \(G_{2c}\), and a predeclared control uses \(G_{3c/2}\).

## 2. Minimum requested dataset

The smallest dataset sufficient for the primary test is:

1. time points \(t_j\) used for the transient probability distributions;
2. integer excess-electron state labels \(N\);
3. phase-averaged or experimentally reconstructed probabilities \(\rho_N(t_j)\);
4. the state window actually retained in the experimental analysis;
5. normalization or missing-tail information if the recorded state window is truncated.

A machine-readable table such as CSV, TSV, JSON, or plain text is sufficient.

## 3. Strongly preferred additional information

If available:

- individual electron-count trajectories used to construct \(\rho_N(t)\);
- number of repetitions contributing to each time point;
- uncertainty estimates or bootstrap samples;
- detector time resolution and bandwidth;
- corrections made for missed transitions;
- exact temperature used for \(\beta\);
- device charging energy \(E_{\rm C}\) and uncertainty;
- \(\Gamma_0\) and uncertainty;
- drive amplitude \(S_{\rm AC}\);
- drive frequency and phase convention;
- the effective time-averaged \(\Gamma^+\) used in the simplified transient model;
- any code or processed arrays behind Figs. 2, 3, 5, and 6.

## 4. What will be tested

No model parameter will be inferred from the target transform trajectory unless that parameter is explicitly designated as a calibration quantity in the pre-registration.

### Primary test

Compute

$$
G_c(t_j)
=
\sum_N\rho_N(t_j)e^{-cN}
$$

directly from the supplied distributions.

Compare with the frozen integral solution of

$$
\dot G_c
=
-\Gamma^+(t)(1-e^{-c})G_c
+
\Gamma_0e^{-c/2}(e^c-1).
$$

### Constant-rate secondary test

Under the paper's phase-averaged approximation,

$$
G_c(t)-G_c^{\rm ss}
$$

must decay with predetermined rate

$$
\Gamma^+(1-e^{-c}).
$$

### Two-coordinate test

Compute \(G_{2c}\) and test the frozen triangular pair \((G_c,G_{2c})\).

### Noncommensurate control

Compute

$$
G_{3c/2}
$$

and

$$
G_{c/2}.
$$

The published generator predicts explicit dependence of the former's derivative on the latter. No autonomous one-score fit will be introduced after data inspection.

## 5. What will not be done

- no silent renormalization of a truncated state window;
- no selection of \(\lambda\) after inspecting residuals;
- no fitted closure coefficient replacing \(c=2\beta E_{\rm C}\);
- no claim that a successful comparison validates a fundamental pregeometric theory;
- no claim of novelty for stochastic-thermodynamic structures already present in the literature.

## 6. Reproducibility output

If the data are provided with permission to analyze them, the repository will record:

- a read-only checksum of the received source files;
- an untouched source-data directory if redistribution is permitted, otherwise metadata only;
- a deterministic analysis script;
- parameter provenance;
- uncertainty propagation;
- the pre-registered pass/fail result;
- every deviation from the frozen protocol.

If redistribution is not permitted, no raw data will be committed publicly.

## 7. Requested format is flexible

The analysis does not require a particular software ecosystem. Spreadsheet exports, text tables, or raw trajectory files are all acceptable provided the meaning of columns and units is documented.

The key requirement is access to numerical probabilities or trajectories rather than values reconstructed from plotted pixels.
