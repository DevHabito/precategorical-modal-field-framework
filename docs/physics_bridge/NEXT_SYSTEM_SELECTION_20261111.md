# Selection of the first published physical target

**Date:** 2026-11-11  
**Status:** target selection; no empirical test has been promoted.

The exact three-state pilot is only a calibration of the bridge logic. The next stage needs a published physical system.

## Selection criteria

A useful target should have as many of the following as possible:

1. state labels with an operational experimental meaning;
2. transition events or transition rates;
3. time-resolved state occupancy;
4. at least three effective states, preferably with a nontrivial cycle;
5. a controlled thermal or reservoir interpretation;
6. a published preparation/driving protocol;
7. enough information to define a coarse-graining without fitting it after seeing the result;
8. data or parameters that can be independently recovered.

## Candidate A — metallic single-electron box

O.-P. Saira et al., “Test of the Jarzynski and Crooks Fluctuation Relations in an Electronic System,” *Physical Review Letters* **109**, 180601 (2012).  
DOI: https://doi.org/10.1103/PhysRevLett.109.180601

### Strengths

- direct experimental stochastic thermodynamics;
- a classical two-state system;
- individual electron transfers are monitored;
- a microscopic theory reproduces the measured distributions without fitting parameters;
- useful for testing the rate/energy/occupancy calibration with little ambiguity.

### Limitation

Two states do not contain a nontrivial cycle. This system cannot by itself test the cycle-affinity obstruction found in the exact pilot.

### Role

**Calibration target.** Use it to test whether the bridge can recover accepted thermodynamic quantities without post-hoc freedom.

## Candidate B — multielectron nonequilibrium quantum dot

Katsuhiko Nishiguchi et al., “Heat-dissipation decomposition and free-energy generation in a nonequilibrium dot with multiple electron states,” *Physical Review Research* **8**, 023209 (2026).  
DOI: https://doi.org/10.1103/947j-vvk2

### Strengths

- experimental nonequilibrium system;
- multiple electron states;
- single-electron counting statistics;
- time-domain probability distributions;
- explicit free-energy and heat-dissipation analysis;
- much closer to the occupancy and coarse-graining questions of the repository.

### Current limitation

Before using this paper as evidence, the bridge must verify that the transition rates, state definitions, driving protocol, and enough raw or tabulated data are available to reproduce the required quantities independently.

### Role

**Preferred multi-state candidate, pending reproducibility gate.**

## Candidate C — molecular-motor Markov networks

Stochastic thermodynamic models of kinesin and rotary motors provide nontrivial cycles, chemical affinities, currents, and external mechanical forcing.

Representative references include:

- André C. Barato and Udo Seifert, thermodynamic uncertainty work on biomolecular processes;
- David Andrieux and Pierre Gaspard, “Fluctuation theorems and the nonequilibrium thermodynamics of molecular motors,” *Physical Review E* **74**, 011906 (2006);
- later Markov-network analyses of kinesin energy conversion.

### Strengths

- genuine nonequilibrium cycles;
- direct relevance of affinities and current observables;
- strong test of whether one scalar (q) is insufficient.

### Limitation

Biochemical models introduce more parameterization and model-selection choices than the electronic targets.

### Role

**Second-stage stress test after an electronic calibration.**

## Decision

The programme will use a two-step progression.

### Bridge 1A — calibration

Start with the single-electron box.

Goal:

> check whether the mapping from accepted physical quantities into the repository variables can recover a known stochastic-thermodynamic relation without fitting the target quantity.

A failure here would stop the bridge before any more ambitious interpretation.

### Bridge 1B — multi-state test

If Bridge 1A passes, move to the 2026 multielectron quantum-dot experiment, provided the reproducibility gate closes.

Goal:

> test occupancy dependence, nonequilibrium currents, and whether the scalar-potential picture survives or must be replaced by cycle/edge information.

## Pre-registration rule

Before any quantitative comparison, the corresponding bridge note must freeze:

- the physical state map;
- the definition of (R);
- the candidate meaning of (q);
- whether (mu) is used and how it is measured;
- the generator or transition law (K);
- how (pi) is estimated;
- every fitted/calibrated parameter;
- the held-out observable;
- the failure criterion.

If these are changed after inspecting the held-out result, the comparison is exploratory and cannot be promoted as prospective evidence.
