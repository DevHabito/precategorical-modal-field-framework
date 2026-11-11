# Physical Bridge V1 — canonical synthesis

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** canonical physics-facing summary  
**Empirical status:** no project-specific physical prediction has yet been validated against held-out experimental data  
**Novelty status:** conservative; classical structure has been removed wherever identified

## 1. The question being tested

The repository began with a provisional informational architecture

$$
(R,q,\mu,K,\pi).
$$

The physical bridge does not assume that these five roles are fundamental.

The working question is:

> When the repository's informational roles are mapped into established physical systems, which roles remain independently necessary, which become derivable, and which closure properties survive changes of observable, coarse-graining, hidden controls, and temporal resolution?

The bridge is designed to make the framework smaller when physics permits it.

## 2. Rule against ad hoc physics

No new physical variable or equation is added merely because a reduced description fails.

A new structure is considered only when forced by at least one of:

- an exact obstruction;
- an operational measurement requirement;
- a symmetry or conservation law;
- an established physical limit;
- prospective data that cannot be described by the current model.

A successful fit is not sufficient evidence. The bridge also records failure criteria and classical alternatives.

## 3. First calibration: reversible Markov dynamics

The exact three-state pilot showed that the provisional tuple need not survive as five independent physical primitives.

In the reversible sector:

- the support relation \(R\) is recoverable from \(K\);
- a potential-like \(q\) can be reconstructed from rate ratios up to a constant;
- equilibrium occupancy can be determined by \(K\);
- current/transient occupancy remains additional state information when preparation is not encoded;
- energy-like \(q\) and degeneracy-like \(\mu\) need not be separately identifiable from equilibrium weights.

Breaking one cycle condition showed that a single state scalar cannot encode arbitrary nonequilibrium driving.

These are diagnostics inside classical stochastic thermodynamics, not new physical laws.

## 4. Bridge 1A: single-electron-box calibration

The 2012 metallic single-electron-box experiment provides an operationally clean mapping:

- \(R\): admissible electron-transfer transitions;
- \(q_t\): electrostatic state energy fixed independently by the circuit and gate protocol;
- \(K_t\): tunneling dynamics;
- \(\pi_t\): charge-state occupancy;
- \(\mu\): left uninstantiated because the experiment does not independently measure a state-level multiplicity corresponding to that repository role.

The event-level identity

$$
Q_{\rm event}=-\Delta U
$$

gives a non-circular calibration of the quantitative mark.

The same experiment is unsuitable for testing mathematical claim C2 because it has only two relevant states and its physical evolution is not the centered mark contraction used in C2.

This negative suitability result is retained.

## 5. Bridge 1B: multi-electron birth-death model

The 2026 multi-electron dot supplies a stronger test because the state variable \(N\) takes many integer values and the published model is a driven birth-death master equation.

For a specified drive history,

$$
\dot\rho_N
=
\Gamma^+(t)\rho_{N-1}
-
[\Gamma^+(t)+\Gamma_N^-]\rho_N
+
\Gamma_{N+1}^-\rho_{N+1},
$$

with

$$
\Gamma_N^-
=
D e^{cN},
\qquad
c=2\beta E_{\rm C},
\qquad
D=\Gamma_0e^{-c/2}.
$$

For

$$
G_\lambda
=
\sum_N\rho_Ne^{-\lambda N},
$$

the exact transform equation is

$$
\boxed{
\dot G_\lambda
=
\Gamma^+(t)(e^{-\lambda}-1)G_\lambda
+
D(e^\lambda-1)G_{\lambda-c}.
}
$$

This identity is the central analytic bridge.

## 6. Dynamic closure depends on the observable

The ordinary mean satisfies

$$
\boxed{
\frac{d}{dt}\langle N\rangle
=
\Gamma^+(t)-DG_{-c}.
}
$$

It is therefore not autonomous over unrestricted distributions.

An exact three-state counterexample gives two distributions with the same mean but different instantaneous mean derivatives.

By contrast, at

$$
\lambda=c,
$$

normalization gives \(G_0=1\), so

$$
\boxed{
\dot G_c
=
-\Gamma^+(t)(1-e^{-c})G_c
+
D(e^c-1).
}
$$

For a specified drive history, \(G_c\) is an exact scalar reduced coordinate even though the mean is not.

This is the cleanest physical example currently found for the repository's principle that dynamic sufficiency is observable-relative.

## 7. Finite commensurate hierarchy

For

$$
\lambda=mc,
\qquad
m\in\mathbb N,
$$

the transform ladder closes:

$$
G_{mc}
\to
G_{(m-1)c}
\to
\cdots
\to
G_c
\to
G_0=1.
$$

Within finite spans of pure exponential observables, the commensurability condition is necessary and sufficient for this natural finite closure.

The minimal nonconstant transform dimension is \(m\).

This statement is exact, but its constant-rate spectral content is classical, as explained below.

## 8. Classical identification: Stieltjes-Wigert

For constant birth rate \(B\), define

$$
q=e^{-c},
\qquad
y=\frac{B}{D}q^N.
$$

Then

$$
\boxed{
\frac{\mathcal L}{B}g(y)
=
g(qy)-g(y)
+
\frac1y[g(y/q)-g(y)].
}
$$

This is the classical Stieltjes-Wigert q-difference operator shifted by the identity.

Consequently:

- the finite polynomial flag is classical;
- the constant-rate eigenvalues are classical;
- the degree-one transform mode is a Stieltjes-Wigert eigenmode;
- the discrete-normal/q-lattice stationary structure is classical.

The constant-rate closure ladder must not be advertised as a new spectral discovery.

## 9. Randomized phase changes the closure problem

The experiment randomizes the drive phase \(\phi\) between repetitions.

At fixed phase,

$$
\dot G_{c,\phi}
=
-(1-q)\Gamma_\phi^+(t)G_{c,\phi}+b.
$$

After phase averaging,

$$
\boxed{
\dot{\bar G}_c
=
-(1-q)\bar\Gamma\,\bar G_c+b
-
(1-q)
\operatorname{Cov}_\phi
(\Gamma_\phi^+,G_{c,\phi}).
}
$$

Therefore exact conditioned scalar closure does not survive generic continuous-time marginalization.

For a common initial distribution, the averaged-rate approximation agrees at first derivative but differs at second derivative by

$$
\boxed{
(1-q)^2G_0
\operatorname{Var}_\phi(\Gamma_\phi^+).
}
$$

For the sinusoidal exponential rate,

$$
\operatorname{Var}_\phi(\Gamma_\phi^+)
=
\Gamma_0^2
[I_0(2A)-I_0(A)^2].
$$

This is an exact coarse-graining obstruction.

## 10. The hidden phase produces an infinite Fourier hierarchy

Restoring the phase coordinate \(\theta=\omega t+\phi\), the conditioned scalar obeys

$$
\partial_tU+\omega\partial_\theta U
=
-(1-q)\Gamma_0e^{-A\sin\theta}U+b.
$$

The drive has infinitely many modified-Bessel Fourier harmonics for nonzero \(A\).

The Fourier coefficients of \(U\) therefore satisfy an infinite convolution hierarchy.

Starting from a phase-independent state, infinitely many phase modes are generated immediately.

Thus the exact continuous-time marginal description is not repaired by adding one arbitrary correction scalar.

This is a concrete instance of the classical coarse-graining principle that eliminating degrees of freedom can generate memory or unresolved correlations.

## 11. Stroboscopic sampling restores finite exact closure

The drive is periodic with period

$$
T=\frac{2\pi}{\omega}.
$$

For the commensurate hierarchy, the one-period monodromy is lower triangular.

Its diagonal Floquet multipliers are

$$
\boxed{
\mu_0=1,
\qquad
\mu_j
=
\exp[-(1-q^j)\Gamma_0TI_0(A)].
}
$$

They are independent of the randomized phase.

For \(G_c\), each phase-conditioned one-period map is affine with the same slope \(\mu_1\).

Therefore the phase average satisfies the exact stroboscopic recurrence

$$
\bar G_{c,n+1}
=
\mu_1\bar G_{c,n}
+
\bar C.
$$

Eliminating the unknown intercept gives the exact three-point test

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

For \(G_{mc}\), Cayley-Hamilton gives

$$
\boxed{
\prod_{j=0}^{m}(E-\mu_j)
\overline{G_{mc}}(nT)=0.
}
$$

The important structural lesson is:

$$
\boxed{
\text{continuous-time marginal closure can fail while period-sampled closure is exact}.
}
$$

Closure is therefore relative not only to the observable and dynamics but also to the temporal resolution of the description.

## 12. What is classical

The bridge now explicitly attributes the following to established literature:

- Markov jump stochastic thermodynamics;
- detailed and local detailed balance;
- cycle affinities;
- birth-death generating functions;
- moment-closure problems;
- discrete-normal distributions;
- reversible birth-death/Stein operators;
- Stieltjes-Wigert q-difference spectral structure;
- q-adapted birth-death processes;
- Floquet and monodromy theory;
- random-phase averaging in periodically forced stochastic systems;
- Mori-Zwanzig and the general emergence of memory under coarse-graining.

These structures are context, not project discoveries.

## 13. What remains project-specific

The strongest project-specific material currently retained is narrower:

1. the explicit transform-shift derivation for the published multi-electron rate law;
2. the exact finite witnesses used to expose nonclosure of selected summaries;
3. the explicit conditioned-versus-marginal closure comparison for the experimental random-phase protocol;
4. the second-order phase-averaging obstruction;
5. the exact stroboscopic recurrence for the phase-averaged commensurate transform hierarchy;
6. the use of these results as a falsifiable stress test of the repository's informational architecture.

Absolute novelty and priority are not certified.

## 14. Formal verification

Two finite algebraic cores now have end-to-end Lean/kernel verification:

- the four-state equal-mean/equal-transform but shifted-transform-separated witness;
- the three-state equal-mean but different-mean-derivative witness.

GitHub Actions run 733 completed successfully with the pinned build, proof-placeholder rejection, and independent leanchecker replay for both physical-bridge modules.

Lean verification does not certify the physical model or the literature claim.

## 15. Empirical status

No project-specific bridge prediction has yet been promoted as empirically supported.

The raw supporting data for the 2026 experiment are not publicly distributed through the article.

The corrected pre-registration defines three evidence classes:

1. exact phase-conditioned continuous-time test;
2. exact phase-averaged stroboscopic test;
3. approximate phase-averaged continuous-time test.

The second class is especially useful because it can be tested from phase-averaged distributions at integer drive periods without reconstructing the hidden phase.

## 16. What the bridge says about \((R,q,\mu,K,\pi)\)

The physical work argues against reading the tuple as five universal primitives.

Current evidence suggests:

- \(R\) can be redundant when the support of \(K\) is known;
- \(q\) may be independently calibrated in one model and derivable from \(K\) in another regime;
- \(\mu\) has not yet received a non-arbitrary operational realization in the electronic bridge;
- \(K\) must be understood together with the externally imposed protocol when the rates are driven;
- current \(\pi\) can remain necessary even when equilibrium occupancy is derivable.

The randomized-phase example adds an important qualification.

The external protocol should **not** be declared a sixth primitive merely because marginalization loses closure.

The correct question is first whether the protocol belongs to the conditioning information required to specify \(K\).

Only an independent obstruction could justify enlarging the architecture.

## 17. Relation to the broader hypothesis about external influence

The bridge gives one rigorous statement relevant to the broader research motivation:

> A reduced state that is dynamically sufficient when external control is known can become insufficient when that external information is marginalized.

It also shows that the required information can depend on temporal resolution: exact continuous-time marginal closure fails, while exact stroboscopic closure can reappear.

This does **not** establish that physical time emerges from informational noise, relational failure, or external perturbation.

It does provide a concrete physical model in which external conditioning, information loss, memory, and sampling scale can be studied without inventing a new fundamental equation.

## 18. Next research question

The next general question is not “what new variable should be added?”

It is:

> Given a physical generator conditioned on an external protocol, under what conditions does marginalizing that protocol preserve a finite closed observable description, produce finite memory, or require an infinite hierarchy?

This question must be positioned against Mori-Zwanzig projection theory, Koopman invariant-subspace theory, hidden Markov dynamics, and Floquet theory before any originality claim is considered.

The multi-electron dot is now a worked control case for that broader investigation.


## 19. Numerical stress regression

A dependency-free numerical stress test was run over 16 diagnostic parameter combinations:

- \(q\in\{0.35,0.65\}\);
- \(A\in\{0.4,1.3\}\);
- \(\Gamma_0\in\{0.2,0.8\}\);
- \(\omega\in\{0.7,1.9\}\).

Each case used 24 phase sectors, 800 RK4 steps per drive period, and five periods.

The largest absolute residual of the exact three-point stroboscopic recurrence was

$$
2.913578232843772\times10^{-12}.
$$

In the same grid, the exact phase ensemble and the constant averaged-rate continuous-time approximation differed in every case at the diagnostic within-period checkpoints.

The maximum within-period differences ranged from approximately

$$
2.35\times10^{-4}
$$

to

$$
4.31\times10^{-1}.
$$

This is a numerical regression of the derived equations. It is not experimental evidence and the grid is not fitted to the device parameters.
