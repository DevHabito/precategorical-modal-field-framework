# Bridge 1A — retrospective calibration on a single-electron box

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** literature-grounded retrospective calibration  
**Evidence status:** published experimental system + exact algebraic mapping; not prospective evidence for the framework

## 1. Purpose

This note calibrates the repository's provisional informational roles against the metallic single-electron box studied experimentally by O.-P. Saira, Y. Yoon, T. Tanttu, M. Möttönen, D. V. Averin, and J. P. Pekola in *Physical Review Letters* **109**, 180601 (2012).

The experiment is useful because the physical quantities needed for the mapping are not invented by the repository:

- the charge states are experimentally resolved;
- the electrostatic energy is fixed by the circuit model;
- the gate protocol is externally controlled;
- electron-transfer events are detected;
- heat is reconstructed from event times;
- the charging energy and temperature are independently constrained;
- the published work tests Jarzynski and Crooks fluctuation relations.

The present exercise asks whether the abstract roles (R,q,mu,K,pi) can be assigned without circularity.

It does **not** treat the published fluctuation-relation result as a new prediction of this repository.

## 2. Physical system

The relevant degree of freedom is the integer number (n) of transferred electrons. In the strong Coulomb-blockade regime, the protocol restricts the experimentally relevant dynamics to the neighboring charge states

[
nin{0,1}.
]

The (n)-dependent electrostatic energy is

[
U(n,n_g)
=
E_{m c}left(n^2-2nn_gight),
]

where (E_{m c}) is the charging-energy scale and (n_g(t)) is the externally controlled gate charge.

The published driving protocol is

[
n_g(t)
=
rac12-rac12cos(2pi f t).
]

For the two retained states,

[
U_0(t)=0,
qquad
U_1(t)=E_{m c}[1-2n_g(t)].
]

Hence the dimensionless energy difference is

[
rac{U_1-U_0}{E_{m c}}
=
1-2n_g(t)
=
cos(2pi f t).
]

This quantity is fixed by the circuit model and external gate protocol before any transition-rate inference is performed.

## 3. Mapping of the repository variables

### 3.1 Relation (R)

For this calibration,

[
0,R,1,
qquad
1,R,0
]

means that a single-electron transfer between the two retained charge states is physically admissible.

Because the allowed transitions are observed directly and also belong to the support of the transition law, (R) is not independent of (K) once the full kinetic model is supplied.

### 3.2 Quantitative mark (q)

Use the dimensionless calibrated energy

[
q_t(n)=rac{U(n,n_g(t))}{E_{m c}}.
]

Then

[
q_t(0)=0,
qquad
q_t(1)=1-2n_g(t).
]

The subscript (t) is important. A driven physical bridge requires the repository's mark to be treated as a time-indexed mark when the external protocol changes the energy landscape.

No new primitive is introduced by this notation; the physical control protocol changes the value of the existing quantitative mark.

### 3.3 Additive mass (mu)

No independent (mu) is assigned at this stage.

The two experimentally resolved charge states are coarse states containing many microscopic electronic degrees of freedom. Their microscopic densities of states enter the orthodox tunneling theory, but the published two-state trajectory record does not provide an independent state-level multiplicity that can be identified with the repository's (mu) without additional assumptions.

Forcing

[
mu=(1,1)
]

would therefore be bookkeeping, not an experimentally justified physical identification.

The correct status for this pilot is:

[
oxed{mu 	ext{uninstantiated}.}
]

### 3.4 Transition law (K_t)

(K_t) is represented by the time-dependent forward and backward tunneling rates between (n=0) and (n=1).

The experiment detects individual tunneling events, and the microscopic tunneling theory is independently constrained by device parameters. The published paper reports that distributions can be reproduced without fitting parameters in the regime used for the fluctuation-relation test.

### 3.5 Occupancy (pi_t)

(pi_t) is the two-component probability vector

[
pi_t=(P[n=0,t],P[n=1,t]).
]

It can be estimated from repeated charge trajectories.

Unlike equilibrium occupancy in a fixed reversible three-state toy model, (pi_t) is not a static object in the driven experiment.

## 4. Exact event-level identity

For an electron-transfer event with (Delta n=pm1), the published heat formula is

[
Q_{m event}
=
2E_{m c},Delta n
left(n_g-rac12ight).
]

The exact energy change of the two-state system is

[
Delta U
=
U(n+Delta n,n_g)-U(n,n_g).
]

For both allowed directions,

[
oxed{Q_{m event}=-Delta U.}
]

For (0	o1),

[
Delta U=E_{m c}(1-2n_g),
]

so

[
Q_{m event}
=
E_{m c}(2n_g-1)
=
-Delta U.
]

For (1	o0),

[
Delta U=E_{m c}(2n_g-1),
]

and

[
Q_{m event}
=
E_{m c}(1-2n_g)
=
-Delta U.
]

The trajectory heat is the sum of these event contributions.

This gives a clean calibration path:

[
	ext{external gate protocol}
longrightarrow q_t
longrightarrow
	ext{event energy changes},
]

while the detector independently supplies transition times and directions.

## 5. Why this mapping is not circular

The physical mark (q_t) is obtained from the electrostatic circuit model and the externally controlled gate charge. It is not defined by fitting the observed heat distribution.

The transition events are read out independently by a capacitively coupled detector.

The charging-energy scale (E_{m c}) and the temperature are independently constrained in the published experiment.

Therefore the event-level heat reconstruction does not require defining (q_t) from the target heat statistic itself.

This is the kind of operational separation required for a serious physical bridge.

## 6. Published fluctuation-relation result

The experiment reports

[
leftlangle e^{-Q/k_{m B}T}ightangle
=
1
]

as the relevant Jarzynski form for protocols in which the (0	o1) transition occurs with essentially unit probability.

The published experimental averages are approximately

[
1.033pm0.003,
qquad
1.032pm0.003,
qquad
1.044pm0.004
]

for drive frequencies (1), (2), and (4) Hz, respectively. The paper also reports a finite detector-bandwidth bias and uncertainty in the independently determined charging-energy scale.

These numbers are recorded here as **literature-reported experimental results**.

They are not a prospective test of this repository because the target relation and its outcome were already known before the bridge mapping was written.

## 7. An exact suitability obstruction: this system cannot test C2

The repository's C2 result proves a non-closure statement for an unrestricted finite-distribution class under a specific centered-contraction update of the quantitative marks.

The present experiment does not realize that theorem's hypotheses.

There are two independent reasons.

### 7.1 Two-state distributions have only one independent occupancy coordinate

For support ({0,1}),

[
pi=(1-p,p).
]

The mean charge is

[
ar n=p.
]

Therefore the mean alone determines the entire probability distribution.

Any static functional of that distribution is consequently a function of the mean once the support is fixed.

A four-point or higher-dimensional non-closure witness cannot be embedded into this two-state probability simplex.

### 7.2 The physical evolution acts on occupancy, not by the C2 mark contraction

In the experiment, the charge-state probabilities evolve under time-dependent tunneling kinetics.

C2 instead studies the declared update

[
q_i'
=
ar q+a(q_i-ar q)
]

on quantitative marks.

These are different dynamical operations.

No physical identification between them has been derived.

### Conclusion

[
oxed{	ext{Bridge 1A is a calibration of meaning, not a test of C2.}}
]

Trying to advertise the two-state experiment as evidence for C2 would be a category error.

## 8. What Bridge 1A establishes

The retrospective calibration supports the following limited statements.

1. A relational support (R), a calibrated quantitative mark (q_t), a transition law (K_t), and a time-dependent occupancy (pi_t) can all be given operational meanings in one established electronic experiment.
2. (q_t) can be calibrated independently of the transition trajectory.
3. Event heat is exactly linked to the change of the calibrated state energy.
4. (R) is redundant if the support of (K_t) is already retained.
5. The experiment does not justify a separate physical (mu).
6. The experiment does not test the repository's C2 non-closure theorem.

## 9. What would count as a stronger bridge

A stronger system should have:

- at least three, preferably many, resolved states;
- measured time-dependent occupancy distributions;
- independently determined transition rates;
- nontrivial nonequilibrium driving;
- a physical operation that can be compared honestly with one of the repository's declared update classes.

A multi-electron dot is attractive because it supplies many resolved charge states and experimentally measured time-dependent distributions. However, the update class must still be checked before any repository theorem is applied.

## 10. Scientific boundary

This note does not establish:

- that the repository derives the Jarzynski equality;
- that (q) is fundamentally energy;
- that the physical system contains a fundamental (mu);
- that C2 has experimental support;
- any new result in stochastic thermodynamics;
- spacetime, gravity, quantum gravity, or pregeometry.

Its purpose is narrower: it shows what a non-circular mapping looks like and records one physical system that is **unsuitable** for testing a stronger repository theorem.
