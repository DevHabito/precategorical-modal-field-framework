# Bridge 3A — gauge-invariant loop structure from a magnetic-flux ring

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** classical physics calibration of a gauge-invariant loop degree of freedom  
**Evidence status:** established Aharonov-Bohm/Peierls physics + finite numerical regression  
**Novelty status:** no novelty claim; this bridge calibrates the *type* of mathematical object found in the q-cycle audit

## 1. Why this bridge is useful

The q-cycle audit found a structural pattern:

- local edge quantities can be gauge-dependent;
- a closed-loop sum can remain gauge-invariant;
- the gauge-invariant loop class can contain physical information not reducible to one scalar potential.

Before assigning any pregeometric interpretation to that pattern, it is useful to compare it with a physical system where the same mathematical structure is already understood.

A charged quantum particle on a ring threaded by magnetic flux provides exactly such a benchmark.

This bridge does **not** identify the repository's q with the electromagnetic vector potential.

## 2. Four-site ring

Consider a tight-binding ring with four sites,

$$
j=0,1,2,3,
$$

and nearest-neighbor hopping magnitude \(J>0\).

Write the Hamiltonian as

$$
H
=
-J
\sum_{j=0}^{3}
\left(
e^{i\theta_j}
|j\rangle\langle j+1|
+
e^{-i\theta_j}
|j+1\rangle\langle j|
\right),
$$

where indices are modulo four.

The local phases \(\theta_j\) are Peierls phases.

## 3. Local gauge transformation

Apply a local basis phase

$$
|j\rangle
\mapsto
e^{i\chi_j}|j\rangle.
$$

Then the edge phases transform as

$$
\boxed{
\theta_j'
=
\theta_j+\chi_j-\chi_{j+1}.
}
$$

The Hamiltonians are related by a unitary similarity transformation

$$
H'
=
UHU^\dagger.
$$

Therefore all spectral predictions are unchanged.

The individual \(\theta_j\) are representation dependent.

## 4. Loop holonomy

Define the loop phase

$$
\boxed{
\Phi_{\rm loop}
=
\sum_{j=0}^{3}\theta_j
\quad(\mathrm{mod}\ 2\pi).
}
$$

Under the local gauge transformation,

$$
\sum_j(\chi_j-\chi_{j+1})=0.
$$

Hence

$$
\boxed{
\Phi_{\rm loop}'=\Phi_{\rm loop}
\quad(\mathrm{mod}\ 2\pi).
}
$$

This is the lattice holonomy associated with the enclosed magnetic flux.

The Aharonov-Bohm effect supplies the physical interpretation: a closed-loop phase can be observable even when the local gauge potential used to represent it is not.

## 5. Uniform gauge

Choose

$$
\theta_j=\frac{\Phi_{\rm loop}}4.
$$

The Bloch wave numbers are

$$
k_m=\frac{2\pi m}{4},
\qquad
m=0,1,2,3.
$$

The energies are

$$
\boxed{
E_m(\Phi_{\rm loop})
=
-2J
\cos
\left(
\frac{2\pi m+\Phi_{\rm loop}}4
\right).
}
$$

Thus changing the gauge while preserving \(\Phi_{\rm loop}\) leaves the spectrum unchanged, whereas changing the loop flux can change the physical spectrum.

## 6. Numerical regression

A four-site numerical benchmark used

$$
J=1
$$

and loop phases

$$
0,\quad
\frac{\pi}{3},\quad
\frac{\pi}{2},\quad
\pi.
$$

The local gauge vector was

$$
\chi=(0.3,-0.7,1.1,-0.2).
$$

For every tested flux:

- the direct and gauge-transformed Hamiltonians were related by unitary conjugation to numerical error below \(5\times10^{-16}\);
- the loop-phase sum was preserved to floating-point precision;
- the eigenvalue sets agreed below \(9\times10^{-16}\).

Representative spectra were:

### Zero flux

$$
\{-2,0,0,2\}.
$$

### \(\Phi_{\rm loop}=\pi/3\)

Approximately

$$
\{-1.93185,-0.51764,0.51764,1.93185\}.
$$

### \(\Phi_{\rm loop}=\pi/2\)

Approximately

$$
\{-1.84776,-0.76537,0.76537,1.84776\}.
$$

### \(\Phi_{\rm loop}=\pi\)

Approximately

$$
\{-\sqrt2,-\sqrt2,\sqrt2,\sqrt2\}.
$$

This is a regression of standard tight-binding gauge physics.

It is not evidence for the pregeometric framework.

## 7. Structural analogy with the q-cycle audit

The q-cycle audit had

$$
F_{ij}
=
q_{ij}-q_{ji},
$$

with gauge transformation

$$
F_{ij}'
=
F_{ij}+c_i-c_j.
$$

The magnetic ring has

$$
\theta_{ij}'
=
\theta_{ij}+\chi_i-\chi_j.
$$

In both cases:

- local edge representatives change by a vertex-gradient term;
- closed-loop sums eliminate the gradient;
- the gauge-invariant information lives in a loop class.

This is a mathematical analogy.

The variables, units, observable laws, and physical meanings are different.

## 8. Important lesson for F2

This benchmark answers one question positively:

> Can a gauge-invariant loop class have a genuine physical operational meaning that is not a temporal coordinate?

**Yes.**

Magnetic flux/holonomy is an explicit physical example.

Therefore the fact that the C1/q audits leave a one-dimensional cycle class does not imply that this class is time.

It could represent some other physical gauge degree of freedom.

This is an important negative constraint on interpretation.

## 9. Reversal and chirality

Reversing the orientation of the loop changes

$$
\Phi_{\rm loop}\mapsto-\Phi_{\rm loop}.
$$

The magnetic flux therefore supplies orientation-sensitive loop information.

For a spinless system, time reversal also changes the sign of the magnetic flux.

This connects loop orientation to time-reversal symmetry breaking in the physical model.

But the magnetic flux is an external physical field/holonomy.

It does not originate the temporal parameter in the Schrödinger equation.

Thus:

$$
\boxed{
\text{physical orientation-breaking loop field}
\neq
\text{origin of time}.
}
$$

## 10. Why this is useful for the repository

The bridge supplies a concrete physical calibration of the hierarchy:

### Local representation

Gauge-dependent edge values.

### Loop class

Gauge-invariant physical content.

### Dynamics

Specified separately by the Hamiltonian.

### Time

Still an independent parameter/relational issue.

This is almost exactly the separation the pregeometric programme now needs to enforce.

## 11. Comparison with stochastic cycle affinity

The magnetic-flux ring and stochastic cycle affinity are different physical theories, but they share one mathematical lesson:

$$
\boxed{
\text{closed-loop information can survive local gauge freedom}.
}
$$

In stochastic thermodynamics the loop quantity measures nonequilibrium driving.

In the quantum ring it represents magnetic holonomy/flux.

The same mathematical slot can therefore host different physical meanings.

That fact is itself a warning against assigning temporal semantics from mathematics alone.

## 12. Current consequence

The project now has a real physical example showing that the sort of one-dimensional cycle class identified in graphA/graphB can be operationally meaningful without being time.

Therefore the next pregeometric question becomes stricter:

> What additional empirical or structural condition would distinguish a genuinely temporal/causal circulation from other gauge-invariant loop variables such as magnetic holonomy?

No answer is currently established.
