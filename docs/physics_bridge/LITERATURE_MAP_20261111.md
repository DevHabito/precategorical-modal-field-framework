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


## 14. q-linear and exponentially structured birth-death rates

Andreas Ruffing and Moritz Simon, **“Linear and q-Linear Birth-and-Death Processes with Killing: Spectral Analysis of Mixed Rate Structures via Regular Perturbation Theory”** (2008), study birth-death systems containing q-linear rate structures and connect them with classical orthogonal-polynomial/spectral machinery.

This is relevant because q-deformed rate structures can grow exponentially with state number.

**Use here:** additional warning that exponentially structured birth-death rates and their special-function consequences have prior mathematical literature.

The targeted search performed for the present bridge did not locate the exact statement that the Salhani et al. rate law produces the finite ladder

$$
G_c,\;G_{2c},\ldots,G_{mc}
$$

at \(\lambda=mc\).

That negative search is **not** a priority proof. The safe status remains:

> exact specialization of a classical generating-function mechanism; novelty not certified.


## 15. Spectral-span context

Herman Callaert and Julian Keilson, **“On exponential ergodicity and spectral structure for birth-death processes I,”** *Stochastic Processes and their Applications* **1** (1973), 187–216, and the companion Part II study finite and infinite spectral span and exponential ergodicity for birth-death processes.

**Use here:** finite/infinite invariant or spectral structure in birth-death systems has deep classical precedent.

**Important distinction:** their spectral-span results are not identified with the project's finite dictionary theorem for the explicit observables \(N\mapsto e^{-\alpha N}\). The objects and questions differ.

The targeted search did not locate the exact predecessor-shift classification for the Salhani et al. generator. Priority remains uncertified.

## 16. Observable-selection boundary

The exact comparison between

$$
\dot{\langle N\rangle}
=
\Gamma^+-DG_{-c}
$$

and the scalar closure of \(G_c\) should be read against classical moment-closure and generating-function theory.

The general lesson that nonlinear propensities produce moment hierarchies is established. The present bridge uses the published exponential rate law to identify a transform coordinate that is closed exactly while the ordinary mean is not autonomous on unrestricted distributions.

Safe status:

**EXACT MODEL-SPECIFIC OBSERVABLE COMPARISON; CLASSICAL CLOSURE CONTEXT; NOVELTY NOT CERTIFIED.**


## 17. Discrete-normal identification

Adrienne W. Kemp, **“Characterizations of a discrete normal distribution,”** *Journal of Statistical Planning and Inference* **63** (1997), 223–229.  
DOI: https://doi.org/10.1016/S0378-3758(97)00020-7

Discrete-normal literature writes an integer-supported Gaussian family equivalently in a form proportional to

$$
\theta^Nq^{N(N-1)/2}.
$$

The stationary distribution used in the multi-electron bridge is exactly of this form after reparametrization.

**Use here:** the stationary law and its exponential-family/tilting structure are classical.  
**Not claimed:** a new discrete Gaussian or a new stationary distribution.

## 18. Stein-generator context

Christophe Ley, Gesine Reinert, and Yvik Swan, **“Stein's method for comparison of univariate distributions,”** *Probability Surveys* **14** (2017), 1–52.  
DOI: https://doi.org/10.1214/16-PS278

The generator approach to Stein's method and discrete birth-death Stein operators use rates satisfying detailed balance with a target law.

**Use here:** a reversible birth-death generator adapted to a discrete target distribution is established structure.  
**Boundary:** the bridge's model-specific transform closure is not being identified with a new Stein construction.

## 19. Exactly solvable q-birth-death neighbor

Ryu Sasaki, **“Exactly solvable birth and death processes,”** *Journal of Mathematical Physics* **50**, 103509 (2009).  
DOI: https://doi.org/10.1063/1.3215983

A particularly close structural neighbor is the alternative q-Charlier process, with constant birth rate and exponentially growing death rate

$$
B(x)=a,\qquad D(x)=q^{-x}-1,
$$

and natural coordinate

$$
\eta(x)=1-q^x.
$$

The Salhani-model death rate is proportional to \(q^{-N}\), not \(q^{-N}-1\), so the generators are not identical.

**Use here:** strong prior that constant-birth/exponential-death structures and q-adapted observables belong to established exactly solvable birth-death theory.

## 20. Bilateral birth-death context

Birth-death chains on the full integer lattice \(\mathbb Z\) have a separate spectral literature, including continuous-time and q-calculus examples.

This matters because the excess-electron variable in the analytic dot model is naturally centered and is not conceptually restricted to a population count on \(\mathbb N_0\).

**Use here:** do not import boundary-at-zero conclusions from ordinary population birth-death chains without checking the state-space contract.


## 21. Exact Stieltjes-Wigert operator identification

Jacob S. Christiansen and Erik Koelink, **“Self-adjoint difference operators and classical solutions to the Stieltjes-Wigert moment problem,”** *Journal of Approximation Theory* **140** (2006), 1-26.  
DOI: https://doi.org/10.1016/j.jat.2005.11.010

The Stieltjes-Wigert polynomials are eigenfunctions of a second-order q-difference operator. In a standard normalization,

$$
L_{\rm SW}
=
T_q-x^{-1}(I-T_{q^{-1}}).
$$

After the bridge change of variable

$$
y=(B/D)q^N,
$$

the constant-rate electronic generator satisfies

$$
\frac{\mathcal L}{B}
=
L_{\rm SW}-I.
$$

Therefore the previously derived finite polynomial flag and constant-rate eigenmodes are classical Stieltjes-Wigert spectral structure in a physical coordinate.

**Novelty consequence:** do not claim the constant-rate closure ladder, eigenvalues, or degree-one transform mode as new spectral mathematics.

Jacob Stordal Christiansen, **“The moment problem associated with the Stieltjes-Wigert polynomials,”** *Journal of Mathematical Analysis and Applications* **277** (2003), 218-245.  
DOI: https://doi.org/10.1016/S0022-247X(02)00534-6

**Use here:** classical indeterminate moment-problem and discrete-measure context for the same polynomial family.


## 22. Modified-Bessel Fourier expansion

NIST Digital Library of Mathematical Functions, §10.35, records the Jacobi-Anger expansions for modified Bessel functions, including

$$
e^{z\cos\theta}
=
I_0(z)+2\sum_{n\ge1}I_n(z)\cos(n\theta).
$$

For positive real \(z\), \(I_n(z)>0\).

**Use here:** the sinusoidal exponential entry rate has infinitely many nonzero Fourier harmonics for nonzero drive amplitude. This is classical special-function structure.

## 23. Floquet context for periodically driven Markov processes

Floquet and monodromy methods for periodically forced Markov systems are established. They are used, for example, in transition statistics and in large-deviation/current-fluctuation theory for periodically driven stochastic systems.

**Use here:** the phase-independent one-period multipliers and Cayley-Hamilton recurrence are applications of classical Floquet theory to the bridge hierarchy.

**Not claimed:** a new Floquet theorem or a new theory of periodically driven Markov chains.


## 24. Random-phase Floquet precedent

P. Jung and P. Hänggi, **“Stochastic Nonlinear Dynamics Modulated by External Periodic Forces,”** *Europhysics Letters* **8** (1989), 505.

The work develops stochastic dynamics with periodic forcing and uses generalized Floquet theory after averaging over a random phase.

**Use here:** random-phase averaging combined with Floquet structure has direct classical precedent.

**Novelty boundary:** the bridge must not claim that random-phase averaging or Floquet analysis of stochastic dynamics is new.

## 25. Mori-Zwanzig coarse-graining boundary

The Mori-Zwanzig projection formalism provides a broad classical explanation for why eliminating unresolved degrees of freedom can generate memory and non-Markovian reduced dynamics.

Representative modern references include work on memory effects in coarse-grained molecular models and recent structural studies of Markovian embeddings of exact projected dynamics.

**Use here:** the hidden-phase covariance/Fourier hierarchy is a concrete finite physical example of a general coarse-graining phenomenon.

**Novelty boundary:** the principle “discarded variables generate memory or extra information requirements” is not a project discovery.


## 26. Quenched versus annealed external context

Jonathan Dewitt and Dmitry Dolgopyat, **“On equivalence of quenched and annealed statistical properties for conservative IID random dynamical systems,”** *Probability Theory and Related Fields* (2026).  
DOI: https://doi.org/10.1007/s00440-026-01531-8

The work distinguishes quenched statements, conditioned on almost every realization of the random dynamics, from annealed statements averaged over realizations, and provides conditions relating the two.

**Use here:** the distinction between conditioned/persistent external randomness and ensemble-averaged dynamics is classical.

## 27. Mixtures of Markov dynamics and induced non-Markovianity

Literature on mixtures of Markov processes and hidden Markov mixtures explicitly notes that the observed mixture need not itself be Markov and can acquire path dependence through hidden component weights.

Recent multi-state mixture work in 2026 likewise describes generalized non-Markovianity caused by unobserved heterogeneity.

**Use here:** persistent hidden context creating non-Markovian marginal dynamics is established background.

**Novelty boundary:** no claim is made for the general idea that a hidden persistent environment destroys Markovianity.


## 28. Experimental hidden-degree memory

Lokesh Muruga, Felix Ginot, Sarah A. M. Loos, and Clemens Bechinger, **“The extraction of work from hidden degrees of freedom,”** *Nature Physics* (2026).  
DOI: https://doi.org/10.1038/s41567-026-03442-w

The experiment uses an observed optically trapped Brownian particle coupled to hidden environmental degrees of freedom. A delayed double-measurement protocol retrieves information stored in environmental memory.

A particularly important control construction matches the complete observed position distribution at the comparison time while removing history information. Subsequent relaxation differs, isolating the effect of hidden-state memory.

**Use here:** independent retrospective physical witness that an identical instantaneous observed marginal need not determine the future when hidden degrees of freedom retain predictive information.

**Novelty boundary:** this phenomenon and its thermodynamic exploitation are the authors' published result, not a project discovery.

## 29. Causal states and minimal predictive statistics

Computational mechanics defines forward causal states as equivalence classes of observed pasts that induce the same conditional future distribution.

Under the framework's assumptions, causal states are minimal sufficient statistics for prediction.

Related predictive-state representations give an analogous language for controlled systems.

**Use here:** the problem of finding a minimal history-based predictive state is established theory.

**Novelty boundary:** do not introduce a renamed minimal-memory state without comparison against causal-state and predictive-state literature.


## 30. Lumpability and exact reduction

Bernhard C. Geiger, **“Information-theoretic reduction of Markov chains,”** *Computer Science Review* **59**, 100802 (2026).  
DOI: https://doi.org/10.1016/j.cosrev.2025.100802

The review separates coarse graining from model reduction and discusses lumpability as the case in which a projection yields a reduced Markov model.

**Use here:** exact reduced Markov closure under a projection is classical and should be described in lumpability language where applicable.

Udo Seifert, **“Coarse-Graining,”** in *Stochastic Thermodynamics* (Cambridge University Press, 2025), pp. 324–337.  
DOI: https://doi.org/10.1017/9781009024358.018

**Use here:** physical coarse-graining loses information and generally changes what thermodynamic quantities can be inferred.

## 31. Current stochastic coarse-graining theory

Hong Duong, Carsten Hartmann, and Michela Ottobre, **“Coarse Graining of Stochastic Differential Equations: Averaging and Projection Method,”** *SIAM Journal on Mathematical Analysis* **58** (2026), 5880–5917.  
DOI: https://doi.org/10.1137/25M1770114

The paper compares averaging and projection-based coarse graining, gives sufficient conditions for agreement, and supplies counterexamples showing that even perfect scale separation does not make the two procedures automatically identical.

**Use here:** averaging and projection must not be treated as interchangeable operations without proof.


## 32. Conditional mutual information and Markov screening

Conditional mutual information vanishes exactly under conditional independence and is therefore a standard information-theoretic diagnostic of Markov screening.

Zhiqiang Huang and Xiao-Kan Guo, **“Quantifying non-Markovianity via conditional mutual information,”** *Physical Review A* **104**, 032212 (2021).  
DOI: https://doi.org/10.1103/PhysRevA.104.032212

**Use here:** CMI-based non-Markovianity is established; the bridge must not introduce a renamed information-memory score.

A broad tutorial on quantum stochastic processes likewise emphasizes vanishing CMI as the signature of finite Markov order when the appropriate memory block is conditioned upon.

## 33. Predictive information and causal-state sufficiency

Ryan G. James, John R. Mahoney, and James P. Crutchfield, **“Information trimming: Sufficient statistics, mutual information, and predictability from effective channel states,”** *Physical Review E* **95**, 060102(R) (2017).  
DOI: https://doi.org/10.1103/PhysRevE.95.060102

The work relates minimal sufficient statistics to predictive information and causal states.

**Use here:** minimal sufficient compression of past information for predicting the future is established theory.

## 34. Strong versus preparation-dependent lumpability

Strong lumpability requires the coarse-grained process to be Markov for every initial distribution, while weak/restricted forms can hold only for selected starting laws.

Higher-order lumpability similarly asks whether the projected process is finite-order Markov.

**Use here:** a zero closure diagnostic for one preparation must not be promoted into universal closure.


## 35. Pregeometric and relational-time boundary

### Causal sets

Modern causal-set work continues to treat locally finite causal order as the fundamental discrete structure, with order and number carrying the information needed to approximate Lorentzian geometry under appropriate conditions.

Tomasz Placek and Leszek Wroński, **“On the Growing Universe of Causal Set Theory—An Order-Type Approach,”** *Foundations of Physics* **54**, 42 (2024).  
DOI: https://doi.org/10.1007/s10701-024-00767-5

**Use here:** a project that simply postulates a partial order does not derive temporal order from informational closure; it enters established causal-set territory.

### Page-Wootters and relational clocks

The Page-Wootters mechanism recovers relational subsystem dynamics by conditioning a globally constrained state on a clock subsystem. Work in quantum cosmology continues to apply this framework in 2026.

**Use here:** internal-clock dynamics has a mature benchmark and should not be renamed as a project-specific emergence mechanism.

### Thermal time and circularity

Eugene Y. S. Chua, **“The Time in Thermal Time,”** *Journal for General Philosophy of Science* **57** (2026), 235–258.  
DOI: https://doi.org/10.1007/s10838-024-09691-8

The paper develops a circularity objection to the thermal-time programme: temporally or dynamically loaded ingredients may already be required to motivate the purported emergence of time.

**Use here:** any project claim of emergent time must pass an explicit anti-circularity audit.

## 36. Required novelty boundary for a pregeometric bridge

The project must distinguish:

- deriving an order from timeless structure;
- using a pre-existing causal order;
- deriving relational evolution from a clock subsystem;
- extracting an effective timescale from already temporal dynamics.

Only the first would address the project's strongest pregeometric ambition.

The current physical bridges address the fourth category and, in part, predictive sufficiency under hidden variables. They do not yet address the first.


## 37. Blackwell order as a non-temporal information order

Channel comparison literature defines the Blackwell/degradation order by post-processing:

$$
W_1\succeq_BW_2
\iff
W_2=G\circ W_1
$$

for some stochastic channel \(G\).

Blackwell's theorem gives an operational decision-theoretic interpretation.

Modern reviews emphasize that the relation is a preorder, becomes a partial order after quotienting equivalent channels, and leaves many channel pairs incomparable.

**Use here:** Blackwell order is a legitimate example of an order defined without external time.

**Negative result for this project:** reversible output relabelings are Blackwell-equivalent, so the order cannot represent universal temporal progression.

## 38. Information decay does not automatically complete Blackwell order

Eyal Sulganik, **“Information Decay Need Not Yield a Transitive Completion of the Blackwell Order,”** preprint (2026).  
DOI: https://doi.org/10.2139/ssrn.7220598

The preprint gives examples where positive doubly stochastic Markov kernels remain Blackwell-incomparable at finite horizons and where natural decay-based completion rules fail transitivity.

**Use here:** additional adversarial evidence against identifying information degradation with a universal time order.

**Evidence boundary:** this is a recent preprint and is used as a warning, not as a foundational source for a project theorem.


## 39. Markov equivalence and observational orientation limits

Causal-discovery theory establishes that two DAGs are Markov equivalent exactly when they have the same skeleton and the same v-structures.

As a result, observational conditional independences generally identify only a Markov equivalence class rather than one unique directed causal graph.

Recent causal-discovery reviews continue to emphasize this limitation and the need for interventions or additional structural assumptions to orient unresolved edges.

**Use here:** statistical dependence patterns do not supply a unique timeless directed order in general.

**Novelty boundary:** the project claims no new causal-discovery theorem.

## 40. Interventional identifiability boundary

Interventional data can refine or break observational Markov equivalence classes.

This makes interventions an important benchmark for any proposed intrinsic directionality.

However, a pregeometric time proposal must still explain whether intervention semantics can be defined without presupposing temporal or agent-level causal structure.


## 41. Strongly connected condensation as an acyclic quotient

For any directed graph, mutual reachability partitions the vertices into strongly connected components.

Contracting each SCC produces the condensation graph, which is always a DAG.

This is a classical graph-theoretic result.

**Use here:** SCC condensation supplies a canonical acyclic quotient without introducing external time labels.

**Boundary:** the quotient is non-injective and erases all internal strongly connected dynamics. It is therefore not a universal reconstruction of physical time.

## 42. Relation to causal-set order

Causal-set theory takes a locally finite partial order as fundamental.

An SCC condensation followed by reachability also yields a partial order in finite cases, but no causal interpretation follows from graph theory alone.

**Use here:** structural similarity to a causet is insufficient. A physical meaning for the primitive directed relation is still required.


## 43. Proper-time reconstruction in causal sets

Causal-set literature uses longest chains between timelike-related elements as a discrete timelike-distance candidate.

In Poisson sprinklings into Minkowski spacetime, longest-chain length approaches continuum proper time up to a density- and dimension-dependent scale in the appropriate limit.

**Use here:** chain length becomes physically meaningful only together with a continuum correspondence, element density, and causal interpretation.

**Boundary:** arbitrary graph depth in the project is not proper time.

## 44. Entropy, arrow, and time are distinct questions

Recent 2026 literature continues to distinguish entropy growth, irreversibility, temporal orientation, and physical time.

Some proposals use entropy as an internal clock, while other work emphasizes that microscopic reversible dynamics can continue when such a clock stalls or that the thermodynamic arrow depends on coarse graining or boundary conditions.

**Use here:** a monotone can be a useful clock on a restricted regime without establishing the ontological origin of time.


## 45. Page-Wootters reversible relational-time benchmark

Don N. Page and William K. Wootters, **“Evolution without evolution: Dynamics described by stationary observables,”** *Physical Review D* **27**, 2885 (1983).  
DOI: https://doi.org/10.1103/PhysRevD.27.2885

The mechanism describes system evolution relationally with respect to internal clock readings while the closed global system can remain in a stationary constrained state.

A modern analysis of the assumptions makes explicit the Hilbert-space factorization, clock/system Hamiltonians, global energy constraint, and clock observable structure.

**Use here:** reversible relational temporal description does not require external noise or entropy production.

**Project consequence:** external unresolved influence cannot be claimed as a necessary origin of all time.

## 46. Finite and nonideal clocks

Modern Page-Wootters literature studies finite or quasi-ideal clocks, clock-system interactions, finite resolution, and corrections to ideal Schrödinger evolution.

**Use here:** the existence of relational time and the accuracy of a physical clock are separate questions.

**Boundary:** the repository's finite numerical benchmark is only a regression of this established mechanism.


## 47. Process matrices and indefinite causal order

Ognyan Oreshkov, Fabio Costa, and Časlav Brukner, **“Quantum correlations with no causal order,”** *Nature Communications* **3**, 1092 (2012).  
DOI: https://doi.org/10.1038/ncomms2076

The process-matrix framework describes local quantum operations without imposing one predefined global causal order and contains correlations incompatible with definite causal order.

**Use here:** definite causal order must not be assumed to be a logically necessary primitive of every pregeometric model.

## 48. Operational quantum theory without predefined time

Ognyan Oreshkov and Nicolas J. Cerf, **“Operational quantum theory without predefined time,”** *New Journal of Physics* **18**, 073037 (2016).  
DOI: https://doi.org/10.1088/1367-2630/18/7/073037

The work develops an operational formulation intended not to assume a predefined time or causal structure.

**Use here:** direct benchmark for the repository's anti-circularity ambition.

## 49. Time-delocalized realizations and causal inequalities

Julian Wechs, Cyril Branciard, and Ognyan Oreshkov, **“Existence of processes violating causal inequalities on time-delocalised subsystems,”** *Nature Communications* **14**, 1471 (2023).  
DOI: https://doi.org/10.1038/s41467-023-36893-3

The work studies realizations of broad classes of processes on time-delocalized subsystems, including examples relevant to violations of causal inequalities.

**Use here:** causal nonseparability/indefinite order cannot be reduced casually to an ordinary graph cycle.

## 50. Cyclic quantum causal models

Jonathan Barrett, Robin Lorenz, and Ognyan Oreshkov, **“Cyclic quantum causal models,”** *Nature Communications* **12**, 885 (2021).  
DOI: https://doi.org/10.1038/s41467-020-20456-x

The work extends quantum causal-model reasoning to cyclic causal structures.

**Use here:** cyclicity and causal indefiniteness are both established but distinct generalizations; the repository must not conflate them.


## 51. Symmetry obstruction to a unique arrow

Time-reversal and symmetry literature repeatedly distinguishes symmetric laws/structures from asymmetric solutions, boundary conditions, or sectors.

A general structural lesson, aligned with Curie's principle, is that an asymmetric observable effect requires either asymmetric input structure or a symmetry-breaking selection.

**Use here:** if an automorphism of a timeless primitive structure exchanges two candidate orientations, an isomorphism-equivariant deterministic rule cannot canonically choose one strict direction between them.

**Novelty boundary:** this is elementary symmetry reasoning, not a new theorem about the arrow of time.

Cristian López and Olimpia Lombardi, **“A Review of the Concept of Time Reversal and the Direction of Time,”** *Entropy* **26**, 563 (2024).  
DOI: https://doi.org/10.3390/e26070563

**Use here:** benchmark for keeping time-reversal symmetry, temporal direction, motion reversal, and arrow-of-time claims distinct.


## 52. Operational signalling and causal precedence

Ognyan Oreshkov and Christina Giarmatzi, **“Causal and causally separable processes,”** *New Journal of Physics* **18**, 093020 (2016).  
DOI: https://doi.org/10.1088/1367-2630/18/9/093020

Operationally, causal order is tied to signalling constraints: if \(A\) is in the causal past of \(B\), signalling can be possible from \(A\) to \(B\) but not from \(B\) to \(A\).

**Use here:** signalling supplies a physically meaningful orientation diagnostic without requiring passive observational correlations alone.

## 53. Interventions in quantum causal modelling

Fabio Costa and Sally Shrapnel, **“Quantum causal modelling,”** *New Journal of Physics* **18**, 063032 (2016).  
DOI: https://doi.org/10.1088/1367-2630/18/6/063032

The framework emphasizes autonomous mechanisms and interventions and identifies causal influence with the possibility of changing statistics at one event through intervention at another.

**Use here:** the direction obtained by signalling relies on declared intervention structure; it is not extracted from passive symmetric data for free.


## 54. Distinguishing labels and cycle symmetry breaking

Michael O. Albertson and Karen L. Collins, **“Symmetry Breaking in Graphs,”** *Electronic Journal of Combinatorics* **3** (1996), R18.  
DOI: https://doi.org/10.37236/1242

A labeling is distinguishing when no nontrivial graph automorphism preserves all labels. For cycle graphs,

$$
D(C_n)=3\quad(n=3,4,5),
$$

and

$$
D(C_n)=2\quad(n\ge6).
$$

**Use here:** A22's binary-alphabet lower bound does not imply binary marks are sufficient to break the automorphism group of every primitive structure.

## 55. Graph Hodge decomposition and cyclic edge information

Xiaoye Jiang, Lek-Heng Lim, Yuan Yao, and Yinyu Ye, **“Statistical ranking and combinatorial Hodge theory,”** *Mathematical Programming* **127** (2011), 203-244.  
DOI: https://doi.org/10.1007/s10107-010-0419-x

The work decomposes edge flows into gradient and cyclic components using combinatorial Hodge theory.

**Use here:** nonzero loop circulation is classical non-gradient edge information. A scalar vertex potential cannot represent it.

## 56. Gauge-invariant currents and cycle affinities

Artur Wachtel, Jürgen Vollmer, and Bernhard Altaner, **“Fluctuating currents in stochastic thermodynamics. I. Gauge invariance of asymptotic statistics,”** *Physical Review E* **92**, 042132 (2015).  
DOI: https://doi.org/10.1103/PhysRevE.92.042132

Cycle-current observables in Markov jump networks have a natural gauge structure and connect to the Schnakenberg cycle decomposition.

**Use here:** gauge-invariant closed-loop information in a transition network is established stochastic-thermodynamic structure.

**Boundary:** a thermodynamic cycle affinity presupposes a dynamical transition model and is not a derivation of time.


## 57. Boundary conditions and the thermodynamic arrow

Sheldon Goldstein, Roderich Tumulka, and Nino Zanghì, **“Is the hypothesis about a low entropy initial state of the Universe necessary for explaining the arrow of time?”** *Physical Review D* **94**, 023520 (2016).  
DOI: https://doi.org/10.1103/PhysRevD.94.023520

The paper discusses the familiar statistical-mechanical fact that a generic low-entropy macrostate can exhibit entropy increase away from that state in both temporal directions and analyzes cosmological models that may avoid a conventional Past Hypothesis.

**Use here:** a special boundary state is a classical route to selecting a thermodynamic arrow, but its necessity is model-dependent.

Pablo Arrighi, Gilles Dowek, and Amélia Durbec, **“Time arrow without past hypothesis: a toy model explanation,”** *New Journal of Physics* **26**, 113019 (2024).  
DOI: https://doi.org/10.1088/1367-2630/ad93f5

The authors give reversible expanding toy models in which entropic-arrow behavior can arise without the conventional low-entropy Past Hypothesis.

**Use here:** do not elevate boundary-state asymmetry into a universal necessary explanation of every arrow.

## 58. Entanglement Past Hypothesis

Jim Al-Khalili and Eddy Keming Chen, **“The Decoherent Arrow of Time and the Entanglement Past Hypothesis,”** *Foundations of Physics* **54**, 49 (2024).  
DOI: https://doi.org/10.1007/s10701-024-00785-3

The paper studies a low-entanglement boundary condition as a possible grounding for the decoherent arrow when unitary dynamics itself permits recoherence.

**Use here:** different effective arrows can be traced to different asymmetric boundary-state information; this remains distinct from deriving temporal order itself.


## 59. Direct microscopic T violation

J. P. Lees et al. (BABAR Collaboration), **“Observation of Time-Reversal Violation in the B0 Meson System,”** *Physical Review Letters* **109**, 211801 (2012).  
DOI: https://doi.org/10.1103/PhysRevLett.109.211801

BABAR directly compared T-conjugated neutral-B transitions and reported statistically significant T-violating parameters.

**Use here:** established empirical example of law-level temporal polarity.

**Boundary:** the T transformation and transition evolution are already defined inside temporal quantum theory; this is not a derivation of time.

## 60. Law asymmetry versus thermodynamic asymmetry

The contemporary foundations literature continues to separate microscopic time-reversal properties of laws from the grounding of thermodynamic asymmetry.

Bryan W. Roberts, **“Does Thermodynamics Have a Reversibility Problem?”** *Mind* (2026), fzag008.  
DOI: https://doi.org/10.1093/mind/fzag008

**Use here:** law-level polarity and macroscopic thermodynamic-arrow explanations should not be conflated.


## 61. Resource convertibility as a non-temporal preorder

Tobias Fritz, **“Resource convertibility and ordered commutative monoids,”** *Mathematical Structures in Computer Science* **27** (2017), 850–938.  
DOI: https://doi.org/10.1017/S0960129515000444

Resource convertibility asks whether one resource can be transformed into another under an allowed class of operations. Together with resource composition, the structure is naturally described by ordered commutative monoids.

**Use here:** explicit directed semantics for R that need not mean temporal precedence.

**Boundary:** the allowed-operation class supplies the polarity, and resource convertibility does not generically imply causal time.

## 62. Current resource-theory boundary

Masahito Hayashi and Hayata Yamasaki, **“The generalized quantum Stein’s lemma and the second law of quantum resource theories,”** *Nature Physics* **21** (2025), 1988–1993.

Modern quantum resource theory continues to treat state/channel convertibility and resource monotones as operational ordering structures.

**Use here:** resource ordering is active contemporary physics, but it remains a convertibility structure rather than a general temporal ontology.


## 63. Constructor-theoretic possible/impossible transformations

David Deutsch, **“Constructor Theory,”** *Synthese* **190** (2013), 4331–4359.  
DOI: https://doi.org/10.1007/s11229-013-0279-z

Constructor theory proposes expressing fundamental laws through possible and impossible physical transformations rather than primarily through trajectories generated from initial conditions.

David Deutsch and Chiara Marletto, **“Constructor theory of information,”** *Proceedings of the Royal Society A* **471**, 20140540 (2015).  
DOI: https://doi.org/10.1098/rspa.2014.0540

**Use here:** established benchmark showing that physical transformation arrows can be formulated without using them as explicit clock coordinates.

**Boundary:** a task already contains input/output polarity; the possible/impossible structure does not automatically derive that polarity from untyped symmetric data.

## 64. Constructor-theoretic thermodynamics

Chiara Marletto, **“Constructor Theory of Thermodynamics,”** preprint/programme (2016).

The work formulates thermodynamic constraints in terms of possible/impossible tasks and emphasizes exact, scale-independent statements of irreversibility.

**Use here:** irreversibility and transformation direction can be represented without identifying the task arrow with metric time.

**Boundary:** constructor-theoretic task polarity remains distinct from the origin of temporal order.


## 65. Lorentzian time orientability as a two-choice global structure

Ettore Minguzzi, **“Lorentzian causality theory,”** *Living Reviews in Relativity* **22**, 3 (2019).  
DOI: https://doi.org/10.1007/s41114-019-0019-x

A Lorentzian manifold is time orientable when one can choose continuously one component of the timelike cone at every point; equivalently, a global continuous timelike vector field exists.

Klaas Landsman, **“Foundations of General Relativity: From Einstein to Black Holes”** (online book/lecture text, 2022), causal-structure chapter.

For a connected time-orientable Lorentzian manifold, global timelike vector fields fall into two orientation classes represented by \(T\) and \(-T\). These define the two possible time orientations.

**Use here:** the physically mature target is not necessarily a canonically named future from metric structure alone; time orientability first supplies a globally consistent two-fold orientation structure.

**Boundary:** the project's finite orientation-doublet criterion is only structurally analogous. It does not derive a Lorentzian metric, cone bundle, or spacetime.

## 66. Spontaneous symmetry breaking and sector selection

David Wallace, **“Spontaneous Symmetry Breaking in Finite Quantum Systems: a decoherent-histories approach”** (2018).

The paper emphasizes approximately dynamically isolated symmetry-related sectors in realistic finite systems and their relation to the infinite-volume SSB limit.

James D. Fraser, **“Spontaneous Symmetry Breaking in Finite Systems,”** *Philosophy of Science* **83**, 585–605 (2016).  
DOI: https://doi.org/10.1086/687263

Standard strict SSB is associated with thermodynamic-limit structure, while large finite systems can reproduce much of the phenomenology.

**Use here:** distinguish realization-level sector selection from a canonical ensemble-level polarity, and avoid calling the finite three-state witness a new SSB result.


## 67. Comparability graphs and uniquely partially orderable graphs

Martin Aigner and Geert Prins, **“Uniquely Partially Orderable Graphs,”** *Journal of the London Mathematical Society* s2-3(2), 260–266 (1971).  
DOI: https://doi.org/10.1112/jlms/s2-3.2.260

A comparability graph is transitively orientable. A UPO graph is one whose compatible strict partial order is unique except for reversal/duality.

Rolf H. Möhring, **“Almost all comparability graphs are UPO,”** *Discrete Mathematics* **50**, 63–70 (1984).  
DOI: https://doi.org/10.1016/0012-365X(84)90035-9

Martin C. Golumbic, **Algorithmic Graph Theory and Perfect Graphs**, 2nd ed., Elsevier, 2004, Chapter 5.

**Use here:** transitive orientation, comparability, implication classes, and uniqueness up to duality are classical. Any project claim about a unique partial order up to reversal must be positioned against UPO theory.

## 68. Automorphism action on transitive orientations

Pavel Klavík and Peter Zeman, **“Automorphism Groups of Comparability Graphs,”** arXiv:1506.05064 (2015).

The paper explicitly treats the induced action of \(\operatorname{Aut}(G)\) on the set of transitive orientations and relates orientation structure to modular decomposition.

**Use here:** the project criterion “a duality class fixed by every graph automorphism” is built from established group-action structure. No originality claim is attached to the action itself.

**Project-specific distinction:** the diamond \(K_4-e\) has six transitive orientations and is therefore not UPO, but one of its three reversal pairs is invariant as a set under the full automorphism group. The novelty of using this fixed duality class as a pregeometric governance criterion is not certified.
