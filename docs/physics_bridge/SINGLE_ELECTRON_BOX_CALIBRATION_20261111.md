# Bridge 1A — retrospective calibration on a single-electron box

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** literature-grounded retrospective calibration  
**Evidence status:** published experiment + exact algebraic mapping; not prospective evidence for the framework

## 1. Purpose

This note calibrates the repository's provisional informational roles against the metallic single-electron box studied by O.-P. Saira, Y. Yoon, T. Tanttu, M. Möttönen, D. V. Averin, and J. P. Pekola in *Physical Review Letters* **109**, 180601 (2012).

The experiment is useful because the required physical quantities are not invented by this repository:

- charge states are experimentally resolved;
- electrostatic energy is fixed by the circuit model;
- the gate protocol is externally controlled;
- electron-transfer events are detected;
- heat is reconstructed from event times;
- charging energy and temperature are independently constrained;
- Jarzynski and Crooks relations are tested experimentally.

The present exercise asks whether \(R,q,\mu,K,\pi\) can be assigned without circularity.

It does **not** treat the published fluctuation-relation result as a new prediction.

## 2. Physical system

The relevant degree of freedom is the integer charge-transfer number \(n\). In the strong Coulomb-blockade regime the protocol restricts the relevant dynamics to

$$
n\in\{0,1\}.
$$

The electrostatic energy is

$$
U(n,n_g)
=
E_{\rm c}\left(n^2-2nn_g\right),
$$

where \(E_{\rm c}\) is the charging-energy scale and \(n_g(t)\) is the externally controlled gate charge.

The published protocol is

$$
n_g(t)
=
\frac12-\frac12\cos(2\pi f t).
$$

For the two retained states,

$$
U_0(t)=0,\qquad
U_1(t)=E_{\rm c}[1-2n_g(t)].
$$

Thus

$$
\frac{U_1-U_0}{E_{\rm c}}
=
1-2n_g(t)
=
\cos(2\pi f t).
$$

This energy difference is fixed before any transition-rate inference.

## 3. Mapping

### Relation \(R\)

The two directed relations \(0R1\) and \(1R0\) mean that a single-electron transfer is admissible.

Once the full kinetic model is retained, this relation is also the support of \(K_t\), so it is not independent information.

### Quantitative mark \(q_t\)

Use the dimensionless calibrated energy

$$
q_t(n)=\frac{U(n,n_g(t))}{E_{\rm c}}.
$$

Then

$$
q_t(0)=0,\qquad
q_t(1)=1-2n_g(t).
$$

The time index matters. In a driven bridge, the existing quantitative mark is protocol-dependent because the physical energy landscape changes with time.

### Additive mass \(\mu\)

No independent \(\mu\) is assigned.

The two measured charge states are coarse states containing many microscopic electronic degrees of freedom. Their microscopic density-of-states structure enters the tunneling theory, but the two-state trajectory record does not provide an independent state-level multiplicity that can be identified with the repository's \(\mu\) without an extra assumption.

Forcing \(\mu=(1,1)\) would be bookkeeping rather than an experimental identification.

### Transition law \(K_t\)

\(K_t\) is the pair of time-dependent forward/backward tunneling rates. Individual transitions are detected, and the microscopic rate theory is constrained independently by device parameters.

### Occupancy \(\pi_t\)

$$
\pi_t=(P[n=0,t],P[n=1,t]).
$$

It can be estimated from repeated charge trajectories.

## 4. Exact event identity

For a transfer with \(\Delta n=\pm1\), the published heat expression is

$$
Q_{\rm event}
=
2E_{\rm c}\,\Delta n
\left(n_g-\frac12\right).
$$

The exact system-energy change is

$$
\Delta U
=
U(n+\Delta n,n_g)-U(n,n_g).
$$

For both directions,

$$
\boxed{Q_{\rm event}=-\Delta U.}
$$

The trajectory heat is the sum over events.

This gives a non-circular calibration route:

$$
\text{gate protocol}
\longrightarrow q_t
\longrightarrow
\text{event energy change},
$$

while the detector independently supplies the transition times and directions.

## 5. Published fluctuation-relation result

The experiment reports the Jarzynski form

$$
\left\langle e^{-Q/k_{\rm B}T}\right\rangle=1
$$

for the relevant protocol.

The reported experimental averages are approximately

$$
1.033\pm0.003,\qquad
1.032\pm0.003,\qquad
1.044\pm0.004
$$

for 1, 2, and 4 Hz. The paper also discusses detector-bandwidth bias and uncertainty in the independently measured energy scale.

These values are literature-reported results. They are not prospective evidence for this repository.

## 6. Why Bridge 1A cannot test C2

The repository's mathematical claim C2 concerns non-closure on an unrestricted finite-distribution class under a specific centered-contraction update of the quantitative marks.

This experiment does not realize those hypotheses.

### Two-state obstruction

Any distribution on \(\{0,1\}\) has the form

$$
\pi=(1-p,p).
$$

Its mean is

$$
\bar n=p.
$$

The mean therefore determines the complete distribution. A four-point non-closure witness cannot be embedded in this two-state simplex.

### Dynamical mismatch

The experimental probabilities evolve under a time-dependent master equation. C2 instead studies the mark update

$$
q_i'
=
\bar q+a(q_i-\bar q).
$$

These are different operations. No physical equivalence between them has been derived.

Therefore

$$
\boxed{\text{Bridge 1A calibrates meaning; it does not test C2.}}
$$

Calling it evidence for C2 would be a category error.

## 7. What is learned

1. \(R\), \(q_t\), \(K_t\), and \(\pi_t\) can all receive operational meanings in one established experiment.
2. \(q_t\) is calibrated independently of the observed transition trajectory.
3. Event heat is exactly tied to the change of the calibrated state energy.
4. \(R\) is redundant once the support of \(K_t\) is retained.
5. The experiment does not justify a separate physical \(\mu\).
6. The experiment is unsuitable for testing C2.

## 8. Boundary

This note does not establish that the repository derives Jarzynski's equality, that \(q\) is fundamentally energy, that \(\mu\) is physical, that C2 has experimental support, or that any pregeometric interpretation follows.

The main value of Bridge 1A is methodological: it demonstrates a non-circular mapping and records an experiment that should **not** be used to claim more than it can test.
