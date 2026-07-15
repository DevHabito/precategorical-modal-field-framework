# A21 — Equivariance Theorem for Endogenous Relational Dynamics

## Setting

Let `O_t` denote the complete observed relational history through time `t`.
Allow an arbitrary endogenous internal state `S_t`, provided `S_t` is
measurable with respect to the observed history and previous
model-independent random variables.

Let

`(O_{t+1},S_{t+1}) = Phi_t(O_0,...,O_t,S_t,Xi_t)`,

where `Xi_t` is fresh randomness with the same law in both latent models.

## Theorem

Suppose a latent transformation leaves the initial observed state and
endogenous state identical. Couple the two models with the same sequence
`Xi_0,Xi_1,...`. Then their complete observed trajectories and endogenous
states are identical almost surely.

## Proof

At time zero, the observed and endogenous states agree by assumption.
Assume they agree through time `t`. The two copies feed identical arguments
and the same `Xi_t` into the same measurable update map `Phi_t`. Their next
observed and endogenous states are therefore identical. Induction gives
identity for all finite times.

Consequently the two trajectory laws are equal. No statistic of the complete
order-valued path can distinguish the latent representatives.

## Scope

The result covers Markov and non-Markov dynamics, reinforcement, adaptive
rules, random attachment, and any other kernel whose state and transition
probabilities are functions only of the relational history and
model-independent randomness.

## Necessary route to symmetry breaking

A transition can break the degeneracy only if it depends on an additional
variable whose value or conditional law is not measurable from the
relational history and is not invariant under the latent transformation.

This is a necessary logical condition, not a proposed physical mechanism.
