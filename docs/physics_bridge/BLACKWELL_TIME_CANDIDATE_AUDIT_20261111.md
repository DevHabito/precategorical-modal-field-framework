# Audit of Blackwell informativeness as a timeless order candidate

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** candidate rejected as a universal origin of temporal order  
**Novelty status:** Blackwell comparison is classical; the rejection is a project governance conclusion, not a new information-theory theorem

## 1. Why Blackwell order was considered

The pregeometric anti-circularity gate requires any candidate temporal order to be defined without an external time parameter.

The Blackwell/degradation order is attractive because it already defines a direction using only statistical information.

For two channels with the same input alphabet,

$$
W_1\succeq_B W_2
$$

when there exists a stochastic post-processing channel \(G\) such that

$$
W_2=G\circ W_1.
$$

Operationally, \(W_1\) is at least as useful as \(W_2\) in every statistical decision problem.

No temporal parameter appears in the definition.

This makes Blackwell order a legitimate **timeless information order candidate**.

## 2. First obstruction: it is not generally a total order

Blackwell comparison is a preorder and becomes a partial order only after quotienting by Blackwell equivalence.

Many pairs of channels remain incomparable.

Therefore it cannot by itself provide a unique linear temporal ordering of arbitrary configurations.

A partial temporal/causal order does not have to be total, so incomparability alone does not kill every possible application.

It does kill any immediate identification with a universal one-dimensional clock.

## 3. Decisive obstruction: reversible evolution can be invisible to the order

Consider a two-state system.

Let

$$
I=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
$$

and

$$
F=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
$$

\(F\) is an invertible deterministic channel and

$$
F^2=I.
$$

Because output relabelings are reversible garblings,

$$
I\succeq_B F
$$

and

$$
F\succeq_B I.
$$

Thus

$$
\boxed{
I\sim_B F.
}
$$

Now consider the deterministic oscillation

$$
I,\;F,\;I,\;F,\ldots
$$

as successive maps from an initial binary state.

Distinct dynamical stages alternate indefinitely.

After quotienting by Blackwell equivalence, all of them occupy the same informational class.

Therefore Blackwell informativeness cannot distinguish temporal progression in a reversible deterministic system.

This is enough to reject

$$
\boxed{
\text{physical time}=\text{Blackwell information degradation}
}
$$

as a universal identification.

## 4. Semigroup monotonicity does not rescue emergence

For a Markov semigroup with an already supplied temporal parameter,

$$
K_{t+s}=K_sK_t.
$$

Then the later channel is a post-processing of the earlier channel:

$$
K_t\succeq_B K_{t+s}.
$$

This monotonicity is real and useful.

But it does not derive time.

The order \(t<t+s\) and the composition law were already assumed in the semigroup structure.

Blackwell degradation then reflects the pre-existing temporal dynamics.

Using this fact as evidence that time itself emerges would be circular.

## 5. Non-Markovian dynamics creates a second obstruction

When the observed system exchanges information with hidden degrees of freedom, distinguishability or predictive information can revive.

Thus the observed channel family need not follow a one-way degradation order at every temporal scale.

Bridge 2 and the broader non-Markovian literature already show that information can leave and later become predictively accessible again.

A monotone information-loss arrow is therefore not a universal description of physical temporal evolution.

## 6. Recent direct warning from channel-order literature

Recent 2026 work explicitly studies whether information decay can complete the Blackwell order.

It gives examples in which:

- Markov kernels remain Blackwell-incomparable at every finite horizon despite convergence toward the same no-information limit;
- natural crossing-time completions can fail transitivity.

This is a direct warning against deriving a universal temporal order by ranking channels according to “how far information has decayed.”

The project does not rely on those examples as a proof of its own claims, but they strengthen the negative audit.

## 7. What Blackwell order remains useful for

Rejecting Blackwell order as time does not make it useless.

It remains an excellent diagnostic for questions such as:

- whether one observation can simulate another;
- whether a later coarse observation contains strictly less decision-relevant information;
- whether a proposed compression is a genuine garbling;
- whether two retained descriptions are informationally equivalent.

It can therefore enter the repository as a **comparison tool**, not as a temporal primitive.

## 8. Relation to the working hypothesis

The working intuition connected temporal structure with relational persistence under external informational disturbance.

The Blackwell audit shows that simple information degradation is insufficient.

A system can undergo real reversible change while preserving Blackwell equivalence.

Therefore any future timeless order derived from the repository must distinguish:

$$
\boxed{
\text{change}
}
$$

from

$$
\boxed{
\text{irreversible information loss}.
}
$$

The two are not synonymous.

## 9. Consequence for the pregeometric programme

The first attempted non-temporal order candidate has failed as a universal temporal order.

This is useful.

The next candidate must be capable of representing reversible change or explain why reversible microscopic dynamics only produces temporal structure after an additional quotient/coarse-graining.

Potential benchmark areas include:

- causal order from intervention structure;
- relational clocks;
- histories/consistent histories;
- process-theoretic causal structure;
- partial orders derived from compatibility constraints.

Each must pass the same anti-circularity gate.

## 10. Current classification

**BLACKWELL ORDER AS UNIVERSAL TIME: REJECTED.**

**BLACKWELL ORDER AS A TIMELESS INFORMATION-COMPARISON TOOL: RETAINED.**

No physical claim is weakened by this rejection because no emergent-time result had previously been established.
