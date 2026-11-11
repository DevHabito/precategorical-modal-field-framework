# Information-theoretic closure diagnostic — preparation-specific versus universal closure

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** classical information-theoretic reformulation of the physical reduction contract  
**Novelty status:** conditional mutual information, Markov screening, causal states, and lumpability are established; no originality claim

## 1. Purpose

The physical bridge now distinguishes:

- a full physical state;
- an observed/reduced state;
- hidden or discarded information;
- a future observable;
- a preparation class;
- a time horizon.

The next question is how to diagnose, without inventing a new score, whether the retained state is sufficient for prediction.

Conditional mutual information already supplies the correct language.

## 2. Variables

Let

$$
X_t
$$

be the retained observable state at time \(t\).

Let

$$
H_t
$$

denote information that is available in the full description but omitted from the reduced state. Depending on the physical model, \(H_t\) can represent:

- a hidden environmental state;
- an external protocol phase;
- a portion of observed history;
- another full-state coordinate.

Let

$$
X_{t+\Delta}
$$

be the future observed state at horizon \(\Delta>0\).

For a specified preparation law \(P\), define the already-standard conditional mutual information

$$
\boxed{
I_P(H_t;X_{t+\Delta}\mid X_t).
}
$$

No new information measure is introduced.

## 3. Preparation-specific screening theorem

For a fixed joint law \(P\),

$$
\boxed{
I_P(H_t;X_{t+\Delta}\mid X_t)=0
}
$$

if and only if

$$
\boxed{
X_{t+\Delta}
\perp
H_t
\mid
X_t.
}
$$

Equivalently, for \(P\)-almost every retained state,

$$
P(X_{t+\Delta}\mid X_t,H_t)
=
P(X_{t+\Delta}\mid X_t).
$$

Thus the retained current state screens the omitted information from the chosen future observable at horizon \(\Delta\).

This is a **preparation-specific** statement.

It does not imply strong lumpability for every possible initial distribution.

## 4. Positive CMI as a closure witness

If

$$
I_P(H_t;X_{t+\Delta}\mid X_t)>0,
$$

then the omitted information contains predictive information about the future beyond the retained current state.

Therefore no predictor that uses only \(X_t\) can reproduce the full conditional future law for that preparation.

This is a distribution-level closure witness.

The statement is informational and predictive. It does not by itself identify a thermodynamic resource or a fundamental state variable.

## 5. Full Markov state

Suppose the complete physical state is

$$
Z_t=(X_t,H_t)
$$

and the full process is Markov.

Then all predictive dependence of the future on earlier history is mediated through \(Z_t\).

In this case,

$$
I(H_t;X_{t+\Delta}\mid X_t)
$$

measures precisely the predictive information carried by the omitted current full-state component, relative to the retained state, for the declared preparation and horizon.

This is the natural information-theoretic counterpart of the reduction contract.

## 6. Universal closure and strong lumpability

Now consider a Markov transition law on the full state and an observation map retaining \(X\).

At a fixed horizon \(\Delta\), assume the admissible preparation class is rich enough to assign positive probability to arbitrary relevant hidden states within each retained state.

Then the following are equivalent.

### A. Universal predictive screening

For every admissible preparation \(P\),

$$
I_P(H_t;X_{t+\Delta}\mid X_t)=0.
$$

### B. Hidden-state-independent reduced transition law

For every retained state \(x\) and every pair of admissible hidden states \(h,h'\),

$$
\boxed{
P(X_{t+\Delta}\in\cdot\mid X_t=x,H_t=h)
=
P(X_{t+\Delta}\in\cdot\mid X_t=x,H_t=h').
}
$$

### C. Exact reduced kernel

There exists a reduced transition kernel

$$
\widehat K_\Delta(x,\cdot)
$$

such that the future observed law depends only on the retained state for every admissible preparation.

For finite Markov chains and partition observations, this is the familiar strong-lumpability condition at the declared step/horizon.

## 7. Why the equivalence holds

If B holds, then the hidden state does not change the future observed distribution once \(X_t\) is fixed, so A follows immediately.

Conversely, suppose B fails.

Then for some retained state \(x\), two hidden states \(h_1,h_2\) induce different future observed distributions.

Choose a preparation supported on

$$
(X_t,H_t)=(x,h_1)
$$

and

$$
(x,h_2)
$$

with positive weights.

Since the two conditional future laws differ, \(X_{t+\Delta}\) is not conditionally independent of \(H_t\) given \(X_t=x\).

Therefore

$$
I(H_t;X_{t+\Delta}\mid X_t)>0.
$$

Thus universal vanishing of the CMI is equivalent to the hidden-state independence required for exact reduction.

## 8. Weak/restricted closure

A particular preparation can satisfy

$$
I_P(H_t;X_{t+\Delta}\mid X_t)=0
$$

even when the full transition law is not strongly lumpable.

For example, one preparation may occupy only a special hidden conditional distribution for which the hidden dependence cancels.

Therefore:

$$
\boxed{
\text{CMI}=0\text{ for one }P
\not\Rightarrow
\text{universal closure}.
}
$$

This is the information-theoretic counterpart of weak or preparation-dependent lumpability.

Every empirical zero or near-zero CMI result must therefore state the preparation class.

## 9. History-based version

If the omitted variable is the observed past rather than a directly modeled hidden state, write

$$
\overleftarrow X_t
$$

for the relevant past history.

Then

$$
I(
\overleftarrow X_t;
X_{t+\Delta}
\mid X_t
)
$$

asks whether the present observed state is sufficient for predicting the chosen future horizon.

For a first-order Markov observed process, suitable past-future conditional mutual informations vanish.

For processes with memory, they need not vanish.

This is established predictive-information and non-Markovianity territory.

## 10. Causal-state boundary

Computational mechanics solves a more general problem:

> compress the entire past into a minimal sufficient statistic that preserves the conditional distribution of the future.

The resulting causal states are predictive equivalence classes of pasts.

Therefore, if the repository later proposes an augmented history-based state

$$
S_t^\star=f(\overleftarrow X_t),
$$

the correct benchmark is not whether it “improves prediction.”

The benchmark is:

1. does it satisfy predictive sufficiency?
2. how does its statistical complexity compare with the causal-state construction?
3. does it contain redundant history?
4. does it remain valid across the declared preparation class?

No renamed causal-state construction should be presented as new.

## 11. Horizon dependence

The diagnostic depends on \(\Delta\):

$$
I(H_t;X_{t+\Delta}\mid X_t).
$$

There is no general permission to assume this function decreases monotonically with \(\Delta\).

Memory effects can be oscillatory, delayed, or exhibit information revivals.

Therefore the repository will not define a universal “memory time” by an arbitrary first threshold crossing.

A timescale may be reported only when the physical model or data support a declared monotonicity/decay structure.

## 12. Temporal resolution versus predictive horizon

The horizon \(\Delta\) and the observation/sampling rule are distinct.

Bridge 1B showed that continuous-time phase-averaged closure can fail while an exact recurrence exists at integer drive periods.

Thus a complete information-theoretic closure statement must specify both:

- the prediction horizon;
- the temporal sampling map.

The reduction contract already includes this information through \(\mathcal T\).

## 13. Bridge 2 interpretation

In the hidden-degree experiment, the history-blind and history-aware ensembles have the same observed position distribution at the comparison time but different later evolution.

At a conceptual level this implies that the retained instantaneous observed state does not screen all history/hidden information from the future for the short-delay preparation class.

The article quantifies related information backflow using KL-based observables.

A direct CMI estimate should be attempted only from suitable joint trajectory data.

It must not be reconstructed from insufficient marginal curves.

## 14. What not to claim

This note does not introduce:

- a new information measure;
- a new definition of Markovianity;
- a new memory metric;
- a new causal-state construction;
- a new lumpability criterion.

Its role is to align the repository's physical bridge with established information theory and prevent an ad hoc closure score.

## 15. Literature boundary

Relevant established areas include:

- conditional mutual information and Markov screening;
- information-theoretic non-Markovianity;
- causal states and predictive information;
- strong, weak, and higher-order lumpability;
- predictive-state representations.

The project-specific question remains operational:

> For each proposed physical reduction contract, which established diagnostic most directly tests whether omitted information still predicts the future?
