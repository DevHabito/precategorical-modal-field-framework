# Selection and status of the first published physical targets

**Date:** 2026-11-11  
**Status:** Bridge 1A completed as retrospective calibration; Bridge 1B analytic stage active; no empirical support promoted.

## Selection criteria

A useful target should provide:

1. operational state labels;
2. transition events or rates;
3. time-resolved occupancy;
4. at least three effective states for a nontrivial closure test;
5. a controlled thermal or reservoir model;
6. a published preparation or driving protocol;
7. enough information to define the mapping before target comparison;
8. recoverable data or parameters.

## Bridge 1A — metallic single-electron box

O.-P. Saira et al., *Physical Review Letters* **109**, 180601 (2012).

### Result

Bridge 1A is complete as a **retrospective calibration**.

The mapping assigns:

- \(R\): admissible \(0\leftrightarrow1\) electron transfers;
- \(q_t\): independently calibrated electrostatic state energy divided by \(E_{\rm c}\);
- \(K_t\): time-dependent tunneling kinetics;
- \(\pi_t\): charge-state occupancy estimated from repeated trajectories;
- \(\mu\): left uninstantiated because no independent state-level multiplicity is measured by the two-state record.

An exact audit verifies the event identity

$$
Q_{\rm event}=-\Delta U
$$

for both transfer directions.

### Suitability boundary

This experiment cannot test mathematical claim C2:

- it has only two relevant states, so the mean occupancy determines the entire distribution;
- its physical evolution acts on occupancy through a master equation rather than through the centered mark contraction assumed in C2.

## Bridge 1B — multi-electron nonequilibrium dot

C. Salhani et al., *Physical Review Research* **8**, 023209 (2026), arXiv:2501.16721v3.

### Reproducibility gate

The following are now independently recoverable from the open paper/preprint:

- state variable \(N\): excess electron number;
- charging energy \(E_{\rm C}=9.8\) meV;
- baseline rate \(\Gamma_0=0.1\) Hz;
- time-dependent birth rate;
- state-dependent death rate;
- full birth-death master equation;
- phase-averaged time-dependent occupancy \(\rho_N(t)\);
- main drive frequency of 1 Hz;
- experimental reconstruction of heat terms;
- repeated-measurement count for the principal transient figure.

The raw supporting data are **not publicly available**. The published data-availability statement says they can be obtained from the authors.

### Analytic bridge result

Applying an exponential transform to the published master equation yields an exact shift relation:

$$
G_\lambda
\longrightarrow
G_{\lambda-2\beta E_{\rm C}}.
$$

A constructive four-state witness shows that one transform value plus the mean does not generically determine the shifted transform.

This is recorded as an analytic physical-bridge theorem, not as an experimental validation and not as a novelty claim.

### Next empirical gate

A direct experimental closure test requires raw or sufficiently tabulated \(\rho_N(t)\) data.

No attempt will be made to digitize plotted points and then call the result a prospective test. Figure digitization, if ever used, must be labeled exploratory.

## Molecular-motor networks

Molecular motors remain a later candidate because they offer genuine nonequilibrium cycles and chemical affinities. They are deferred until the electronic bridge is methodologically stable.

## Promotion rule

Before any physical comparison is promoted, freeze:

- state map;
- definition of \(R\);
- physical meaning of \(q\);
- status of \(\mu\);
- transition law \(K\);
- occupancy estimator \(\pi\);
- fitted parameters;
- held-out observable;
- failure criterion.

Any mapping changed after inspecting the held-out result remains exploratory.
