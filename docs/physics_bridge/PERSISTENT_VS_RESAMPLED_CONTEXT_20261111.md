# Persistent versus resampled external context

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** classical stochastic-process distinction used as a bridge diagnostic  
**Novelty status:** quenched/annealed and hidden-mixture effects are classical

## 1. Why persistence matters

The physical bridge should not treat every kind of external randomness as the same operation.

There is a structural difference between:

1. an external context sampled once and then retained along a trajectory;
2. an external context resampled independently at each step.

The first creates persistent hidden heterogeneity. The second is a rapidly refreshed environment.

This distinction is classical and closely related to quenched versus annealed descriptions.

## 2. Minimal scalar example

Let

$$
x_{n+1}=M_nx_n,
$$

with common deterministic initial value \(x_0\).

### Persistent hidden context

Sample one random multiplier \(M\) once and keep it for the complete trajectory:

$$
M_n=M.
$$

Then

$$
x_n=M^nx_0
$$

and

$$
\boxed{
\mathbb E[x_n]
=
x_0\mathbb E[M^n].
}
$$

### Independently resampled context

Now let

$$
M_0,M_1,\ldots
$$

be independent identically distributed copies of \(M\).

Then

$$
x_n=
\left(\prod_{k=0}^{n-1}M_k\right)x_0,
$$

so independence gives

$$
\boxed{
\mathbb E[x_n]
=
x_0(\mathbb E[M])^n.
}
$$

The two descriptions agree at the first step.

At the second step,

$$
\mathbb E[x_2]_{\rm persistent}
-
\mathbb E[x_2]_{\rm resampled}
=
x_0
\left[
\mathbb E[M^2]
-
(\mathbb E[M])^2
\right].
$$

Therefore

$$
\boxed{
\mathbb E[x_2]_{\rm persistent}
-
\mathbb E[x_2]_{\rm resampled}
=
x_0\operatorname{Var}(M).
}
$$

If the external multiplier has nonzero variance, persistence becomes visible at second order in the trajectory length.

## 3. General correlated context sequence

For a stationary multiplier process,

$$
x_n=x_0\prod_{k=0}^{n-1}M_k,
$$

and therefore

$$
\boxed{
\mathbb E[x_n]
=
x_0
\mathbb E
\left[
\prod_{k=0}^{n-1}M_k
\right].
}
$$

A one-number annealed replacement

$$
\mathbb E[x_n]
\stackrel{?}{=}
x_0(\mathbb E[M])^n
$$

requires factorization of these joint moments.

Temporal correlations of the external context obstruct that factorization.

The reduced dynamics therefore depends on the persistence structure of the external process, not merely on its one-time marginal distribution.

## 4. Relation to the randomized-phase quantum-dot bridge

In the Salhani protocol, a phase is randomized between repetitions but then determines a complete periodic drive history inside a repetition.

Relative to a single trajectory, the phase is a persistent context.

This is why averaging the phase at the beginning is not equivalent to replacing the instantaneous rate by its phase average at every instant.

The difference appears already at the second derivative of the averaged transform.

The exact stroboscopic recurrence is possible because the full-period maps share a common finite algebraic structure despite that persistent hidden context.

## 5. Markovization

If the hidden context has its own state dynamics, the joint pair

$$
(\text{observed state},\text{context state})
$$

can often be Markov even when the observed marginal process is not.

This is classical hidden-state or random-environment modeling.

For the repository, the methodological consequence is:

> Before adding a new reduced variable, first ask whether the apparent nonclosure comes from having omitted a real conditioning variable whose inclusion restores Markovianity.

The omitted context is not automatically a new fundamental primitive. It may simply be part of the physical specification of \(K\).

## 6. Connection to the broader research motivation

The worked example supports a limited statement:

> The same one-time distribution of external perturbations can produce different reduced dynamics depending on how long the external context persists along a trajectory.

This provides a mathematically controlled way to study “external persistence” without equating it with physical time.

The project still has no result showing that time itself emerges from informational noise or from failure of relational persistence.

## 7. Literature boundary

Quenched versus annealed randomness is classical in statistical physics and random dynamical systems.

Mixtures of Markov processes and hidden Markov mixtures are also known to generate non-Markovian marginal dynamics and path dependence.

Recent literature continues to study when quenched and annealed statistical laws agree or differ.

Therefore the project claims no novelty for the persistence distinction itself.

Its role is to sharpen the physical-bridge protocol:

- external amplitude distribution;
- external temporal persistence;
- observable choice;
- marginalization rule;
- sampling resolution

must be treated as separate ingredients.
