# Open-data target survey after Bridge 1B

**Date:** 2026-11-11  
**Purpose:** determine whether a public dataset can replace the author-data request without changing the scientific question

## Decision

No public dataset located in the targeted search is currently an equivalent substitute for the Salhani et al. experiment.

The requirement is unusually specific:

- experimentally resolved stochastic states;
- multiple states rather than a two-state calibration;
- time-resolved occupancy or trajectories;
- periodic external drive;
- enough protocol information to define the conditioned generator;
- a rate structure that supports a pre-analysis closure prediction.

Changing the physical system only to obtain easier data would change the question being tested.

## Public datasets considered

### Quantum-dot occupation arrays

A 2023/2024 Zenodo release from QuTech provides extensive data and scripts for single-electron occupation in quantum-dot arrays.

**Reason not substituted:** the dataset is valuable for charge-state measurement but is not the same driven multistate stochastic-thermodynamic transient problem.

### Optical-tweezer fluctuation-theorem data

A 2025 Zenodo release provides raw data and Python tutorials for fluctuation-theorem experiments with optical tweezers.

**Reason not substituted:** this is a continuous-coordinate stochastic system with a different generator and observable structure. It is a possible future bridge, not a drop-in validation of Bridge 1B.

### Hidden-degree-of-freedom experiments

A 2026 Zenodo release provides raw trajectories and MATLAB analysis for experiments on extracting work from hidden degrees of freedom.

**Reason not substituted:** highly relevant to the broader marginalization question, but its physical dynamics and protocol are different. It should be treated as an independent second bridge if selected.

### Periodically driven stochastic-system code

A 2026 Zenodo release accompanying work on impedance in periodically driven stochastic systems provides code and calculations.

**Reason not substituted:** useful theory/software comparison, but not an independent experimental dataset matching the multi-electron birth-death test.

## Next action

Keep the Salhani et al. data request as the direct empirical route for Bridge 1B.

In parallel, the hidden-degree-of-freedom dataset is the strongest candidate for a later Bridge 2 because it provides raw experimental trajectories and directly addresses information lost under partial observation.

No Bridge 2 claim is opened until its model, literature, and prospective observable are audited independently.
