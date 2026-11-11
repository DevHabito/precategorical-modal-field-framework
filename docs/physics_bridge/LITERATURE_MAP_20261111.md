# Literature map for the Markov thermal bridge

**Date checked:** 2026-11-11  
**Scope:** stochastic thermodynamics, local detailed balance, cycle consistency, birth-death generating functions, and coarse-graining.

This note records literature used to prevent the physical bridge from relabeling established results as project discoveries.

## 1. Mesoscopic and macroscopic stochastic thermodynamics

Gianmaria Falasco and Massimiliano Esposito, **“Macroscopic stochastic thermodynamics,”** *Reviews of Modern Physics* **97**, 015002 (2025).  
DOI: https://doi.org/10.1103/RevModPhys.97.015002

The review starts from Markov jump processes and develops conditions under which deterministic macroscopic dynamics and thermodynamics emerge.

**Use here:** background and terminology boundary.  
**Not claimed:** a new theory of Markov thermodynamics.

## 2. Local detailed balance across scales

Gianmaria Falasco and Massimiliano Esposito, **“Local detailed balance across scales: From diffusions to jump processes and beyond,”** *Physical Review E* **103**, 042114 (2021).  
DOI: https://doi.org/10.1103/PhysRevE.103.042114

This work relates log rate ratios to free-energy changes and nonconservative work and studies local detailed balance across scales.

**Use here:** the rate-ratio interpretation of a potential-like \(q\) is classical physical structure.  
**Constraint:** outside conservative sectors, rate ratios need not come from one state potential.

## 3. Master-equation stochastic thermodynamics

Massimiliano Esposito and Christian Van den Broeck, **“Three faces of the second law. I. Master equation formulation,”** *Physical Review E* **82**, 011143 (2010).  
DOI: https://doi.org/10.1103/PhysRevE.82.011143

**Use here:** background for driven master equations, broken detailed balance, and entropy production.

## 4. Cycle structure and affinities

Matteo Polettini, Gregory Bulnes-Cuetara, and Massimiliano Esposito, **“Conservation laws and symmetries in stochastic thermodynamics,”** *Physical Review E* **94**, 052117 (2016).  
DOI: https://doi.org/10.1103/PhysRevE.94.052117

**Use here:** nonzero cycle affinity is physical nonequilibrium information, not a defect to be patched by an arbitrary scalar.

## 5. Cycle balance and Markov chains

Stefan Müller and Badal Joshi, **“Detailed Balance = Complex Balance + Cycle Balance: A Graph-Theoretic Proof for Reaction Networks and Markov Chains,”** *Bulletin of Mathematical Biology* **82**, 116 (2020).  
DOI: https://doi.org/10.1007/s11538-020-00792-1

**Use here:** the cycle-product calculation in the finite pilot is classical.

## 6. Partial observation and effective thermodynamics

Matteo Polettini and Massimiliano Esposito, **“Effective Thermodynamics for a Marginal Observer,”** *Physical Review Letters* **119**, 240601 (2017).  
DOI: https://doi.org/10.1103/PhysRevLett.119.240601

**Use here:** warning that retained observables and hidden degrees of freedom change the effective thermodynamic description.

## 7. Single-electron-box calibration experiment

O.-P. Saira, Y. Yoon, T. Tanttu, M. Möttönen, D. V. Averin, and J. P. Pekola, **“Test of the Jarzynski and Crooks Fluctuation Relations in an Electronic System,”** *Physical Review Letters* **109**, 180601 (2012).  
DOI: https://doi.org/10.1103/PhysRevLett.109.180601

The experiment measures individual electron transfers in a metallic single-electron box, reconstructs dissipated heat, and tests fluctuation relations. The paper reports independently determined device parameters and microscopic predictions without fitting the target heat distributions.

**Use here:** retrospective calibration of \(R,q_t,K_t,\pi_t\).  
**Boundary:** the system has only two relevant charge states and cannot test the repository's four-point C2 non-closure witness.

## 8. Multi-electron nonequilibrium dot

Chloe Salhani, Kensaku Chida, Takase Shimizu, Toshiaki Hayashi, and Katsuhiko Nishiguchi, **“Heat-dissipation decomposition and free-energy generation in a nonequilibrium dot with multiple electron states,”** *Physical Review Research* **8**, 023209 (2026).  
DOI: https://doi.org/10.1103/947j-vvk2  
arXiv:2501.16721v3

The experiment uses single-electron counting to reconstruct time-dependent probability distributions over many electron-number states. The published model is a birth-death master equation with

$$
\Gamma^+(t)=\Gamma_0e^{-\beta eV(t)}
$$

and

$$
\Gamma_N^-=\Gamma_0e^{\beta\,2E_{\rm C}(N-1/2)}.
$$

The paper reports \(E_{\rm C}=9.8\) meV, \(\Gamma_0=0.1\) Hz, a 1 Hz drive in the main experiment, time-resolved \(\rho_N(t)\), and experimental reconstruction of heat terms.

**Use here:** source model for Bridge 1B.  
**Data boundary:** the published data are not publicly available; the article states that supporting data are available from the authors. Therefore no empirical out-of-sample closure test is currently claimed.

## 9. Generating functions for birth-death processes are classical

Forrest W. Crawford, Lam Si Tung Ho, and Marc A. Suchard, **“Computational methods for birth-death processes,”** *Wiley Interdisciplinary Reviews: Computational Statistics* **10**(2), e1423 (2018).  
DOI: https://doi.org/10.1002/wics.1423

The review emphasizes the long history of birth-death theory and generating-function methods, including work going back to Kendall and Karlin–McGregor.

Standard birth-death literature derives evolution equations for probability generating functions by transforming the master equation.

**Use here:** the act of applying an exponential/probability-generating transform to a birth-death master equation is classical.  
**Not claimed:** novelty for transform evolution, moment hierarchies, or generating-function closure problems.

## 10. Moment-closure background

Birth-death and population-process literature has long noted that when rate functions are nonlinear, low-order moment equations generally couple to higher moments, motivating moment-closure approximations.

**Use here:** general non-closure of compressed moment descriptions is established background.

## 11. Current novelty boundary for Bridge 1B

The exact identity

$$
\dot G_\lambda
=
\Gamma^+(t)(e^{-\lambda}-1)G_\lambda
+
\Gamma_0e^{-\beta E_{\rm C}}(e^\lambda-1)G_{\lambda-2\beta E_{\rm C}}
$$

is a direct specialization of the published rate law under an exponential transform.

The four-state witness showing that equal normalization, equal mean, and equal \(G_\lambda\) need not determine the shifted transform is a project derivation used to expose the closure issue cleanly.

At present the safe classification is:

> **project-specific bridge derivation; generating-function and closure mechanism classical; novelty not certified.**

No claim of new stochastic thermodynamics is justified by this result alone.

## 12. Recent pathwise-observable framework

A recent 2026 pathwise-observable framework in *Physical Review X* develops stochastic calculus directly for Markov-jump trajectories and emphasizes inference under partial accessibility of dissipative degrees of freedom.

**Use here:** any future trajectory-level observable introduced by the project must be compared against current pathwise stochastic-thermodynamics theory before novelty is considered.

## 13. Overall boundary

The literature already contains mature theory for:

- Markov jump thermodynamics;
- detailed and local detailed balance;
- cycle affinities;
- birth-death processes;
- generating functions;
- moment closure;
- coarse-graining;
- partial observation;
- pathwise thermodynamic observables.

The project-specific question remains narrower:

> When the repository's provisional informational roles are mapped into established physical models, which roles remain independently necessary, and which closure failures survive under the physical dynamics actually used by those models?

That is currently a framework stress test, not a new fundamental theory.
