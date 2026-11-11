# Physical architecture refinement — closure requires a declared reduction contract

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** methodological refinement of the physical bridge  
**Novelty status:** based on classical lumpability, projection, and coarse-graining theory; not a new physical postulate

## 1. Problem exposed by the physical bridges

The provisional architecture

$$
(R,q,\mu,K,\pi)
$$

was useful as an internal informational decomposition.

The physical bridges show that a statement such as

> “\(K\) determines the dynamics”

is incomplete unless the state on which \(K\) acts is declared.

Likewise, saying

> “\(\pi\) is the current state”

is incomplete if \(\pi\) is only an observed marginal of a larger physical state.

The solution is **not** to add a sixth fundamental variable.

The solution is to require every physical closure statement to declare its reduction contract.

## 2. Full state and observed state

Let

$$
S
$$

be the state space on which the physical dynamics is Markovian or otherwise explicitly defined.

Let

$$
O:S\to Y
$$

be the observation/coarse-graining map.

For a full distribution

$$
\Pi
$$

on \(S\), the observed distribution is the pushforward

$$
\nu=O_\#\Pi.
$$

The physical bridge should never silently identify

$$
\Pi
$$

with

$$
\nu.
$$

Bridge 2 gives an experimental reason for this distinction: two preparations can have the same \(\nu\) and different future observed evolution because their hidden-state conditional distributions differ.

## 3. External conditioning

Let

$$
\xi
$$

denote physical control/context information required to specify the transition law.

The transition law should be written conceptually as

$$
K^\xi
$$

or, under a time-dependent protocol,

$$
K_t^\xi.
$$

This notation does not make \(\xi\) a new fundamental primitive.

It records what information is required to identify the physical member of the transition-law family.

If \(\xi\) is omitted or marginalized, the observed process may cease to be Markovian.

## 4. Exact reduced closure

At a declared time step or observation interval \(\Delta\), exact reduced closure means that there exists a reduced evolution operator

$$
\widehat K_\Delta
$$

such that

$$
\boxed{
O_\#
K_\Delta^\xi
\Pi
=
\widehat K_\Delta
O_\#\Pi
}
$$

for every admissible preparation \(\Pi\) in the declared class.

The reduced future must depend only on the retained state.

This is an intertwining/factorization condition.

In finite-state Markov chains, the corresponding exact aggregation question belongs to classical lumpability theory.

## 5. Failure witness

A universal reduced operator cannot exist if there are two admissible full preparations

$$
\Pi_A,\Pi_B
$$

such that

$$
O_\#\Pi_A
=
O_\#\Pi_B
$$

but

$$
O_\#K_\Delta^\xi\Pi_A
\neq
O_\#K_\Delta^\xi\Pi_B.
$$

This is the distribution-level form of dynamic nonclosure.

Bridge 2 is a retrospective experimental example of this pattern.

## 6. Strong versus restricted closure

The phrase “exact closure” must specify the preparation class.

### Strong/universal closure

The reduced evolution works for every admissible full preparation.

### Restricted closure

The reduction works only for a special family of preparations, for example:

- equilibrium-conditioned states;
- an invariant manifold;
- one stationary family;
- one protocol-prepared ensemble;
- a family satisfying a prescribed hidden conditional law.

A restricted closure can be physically useful.

It must not be promoted into a universal statement.

This distinction parallels strong, weak, and preparation-dependent forms of lumpability.

## 7. Temporal resolution belongs to the closure statement

Bridge 1B shows that the same physical reduction can have different closure status at different temporal resolutions.

At arbitrary continuous time after phase marginalization:

$$
\text{scalar closure fails}.
$$

At integer drive periods:

$$
\text{an exact finite recurrence exists}.
$$

Therefore the closure claim must include its time map:

$$
\Delta t,\quad T,\quad nT,\quad\text{or continuous time}.
$$

Temporal resolution is not a new state variable.

It is part of the statement being tested.

## 8. Reduction contract

For audit purposes, every physical-bridge claim should declare the tuple

$$
\boxed{
\mathfrak C
=
(S,O,\Xi,\mathcal P,\mathcal T).
}
$$

This is **metadata for the theorem/test**, not a proposed physical ontology.

Its entries are:

- \(S\): full state space used by the physical dynamics;
- \(O\): observation/coarse-graining map;
- \(\Xi\): conditioning information regarded as known;
- \(\mathcal P\): admissible preparation class;
- \(\mathcal T\): temporal resolution/sampling rule.

A statement such as “the reduced state closes” has no acceptable physical meaning in this repository unless \(\mathfrak C\) is declared.

## 9. Bridge 1B contract

For the phase-conditioned electronic transform:

- \(S\): electron-number distribution together with the specified drive history;
- \(O\): selected exponential transform hierarchy;
- \(\Xi\): known phase/protocol;
- \(\mathcal P\): distributions for which the transforms exist;
- \(\mathcal T\): continuous time.

Under this contract, the commensurate transform hierarchy closes exactly.

After removing phase from \(\Xi\), that statement changes.

For phase-averaged continuous time, the reduced scalar is not closed.

For phase-averaged stroboscopic sampling at \(nT\), a finite recurrence reappears.

These are three different contracts, not contradictory results.

## 10. Bridge 2 contract

For the hidden-degree experiment:

- \(S\): observed particle plus hidden environmental degrees of freedom;
- \(O\): observed particle coordinate/distribution;
- \(\Xi\): experimental control protocol;
- \(\mathcal P\): measurement-conditioned ensembles constructed in the experiment;
- \(\mathcal T\): relaxation after the comparison time.

The history-aware and history-blind ensembles are prepared with the same observed marginal at \(t=0\) but different hidden conditional information.

Their later observed dynamics differ.

Therefore the reduction to the instantaneous observed marginal fails strong closure on that preparation class.

## 11. Consequence for \(K\)

The repository should stop treating a physical \(K\) as though it were always one context-free matrix or kernel.

Depending on the application, \(K\) can be:

- a fixed transition law;
- a time-dependent law;
- a family \(K^\xi\) conditioned on control;
- a full-state Markov law whose observable projection is non-Markovian;
- an effective reduced law valid only on a restricted preparation family.

These distinctions refine the meaning of \(K\); they do not require adding an arbitrary primitive.

## 12. Consequence for \(\pi\)

Likewise, distinguish:

$$
\Pi_{\rm full}
$$

from

$$
\pi_{\rm obs}=O_\#\Pi_{\rm full}.
$$

The observed occupancy/distribution is not guaranteed to be a sufficient dynamical state.

Bridge 2 provides direct experimental support for that warning.

## 13. Consequence for the provisional architecture

The current physical evidence does **not** support replacing

$$
(R,q,\mu,K,\pi)
$$

with a larger tuple.

It supports a stricter usage rule:

> the independence and sufficiency of each component are meaningful only relative to a declared state space, observation map, conditioning set, preparation class, and time resolution.

The physical programme should first attempt reduction under this contract.

Only after a genuine obstruction remains should the primitive architecture itself be enlarged.

## 14. Classical boundary

This refinement belongs to established ideas:

- Markov-chain lumpability;
- coarse-graining;
- intertwining/factorization;
- Mori-Zwanzig projection;
- hidden Markov models;
- predictive sufficient states;
- Koopman invariant subspaces.

No novelty claim is made for the contract formalism itself.

Its function is governance: prevent an under-specified closure claim from being mistaken for a new physical principle.
