# Bridge 2 — hidden degrees of freedom as an experimental closure witness

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Physical source:** Muruga, Ginot, Loos, Bechinger, Nature Physics (2026)  
**Status:** retrospective empirical calibration  
**Novelty status:** the experiment, non-Markovian memory, predictive-state ideas, and hidden-state augmentation are classical/published; no project priority claim

## 1. Why this experiment is useful

The first physical bridge used an electronic birth-death model to study observable-dependent closure and protocol marginalization.

A second system should test the same general concern without relying on that special generator.

The 2026 Nature Physics experiment on hidden degrees of freedom is unusually suitable because the authors explicitly distinguish:

- an observed coordinate \(X\);
- hidden environmental degrees of freedom \(Y\);
- the full state \(Z=(X,Y)\);
- a history-blind control ensemble;
- a two-measurement ensemble retaining information about the past.

The paper states that the enlarged state \(Z=(X,Y)\) is Markovian while the observable coordinate alone can show non-Markovian memory.

The experiment therefore provides an independent physical control case for the repository's closure questions.

## 2. The decisive construction

Let

$$
\rho_{|ij\rangle}(x,t)
$$

be the observable particle-position distribution conditioned on two measurement outcomes \(i\) and \(j\).

The authors construct a history-blind control distribution

$$
\tilde\rho_{|ij\rangle}(x,t)
$$

by subsampling trajectories from a single-measurement ensemble.

Crucially, the construction enforces

$$
\boxed{
\tilde\rho_{|ij\rangle}(x,0)
=
\rho_{|ij\rangle}(x,0).
}
$$

Thus the two ensembles have the same complete observed position distribution at the comparison time.

They differ only in information retained about the earlier history and its correlations with the hidden environmental state.

The paper reports that their later relaxation differs.

This is stronger than a same-mean counterexample: the entire observed marginal distribution is initially matched.

## 3. Distribution-level nonclosure proposition

Suppose there existed a universal autonomous evolution map on the observable marginal alone,

$$
\mathcal T_t:
\rho_X(0)\mapsto\rho_X(t),
$$

valid for all admissible preparations in the experiment.

Then

$$
\rho_X^{(A)}(0)=\rho_X^{(B)}(0)
$$

would imply

$$
\rho_X^{(A)}(t)
=
\rho_X^{(B)}(t)
$$

for every later time.

The history-blind control construction is designed precisely to test this implication.

The reported divergence of the relaxation curves therefore rules out a universal autonomous description based only on the instantaneous observed distribution for that preparation class.

This is a retrospective empirical witness of observable-level nonclosure.

It is the experiment's result, not a project discovery.

## 4. Why the previous measurement matters

The second measurement outcome \(j\) specifies the current visible measurement class.

The earlier outcome \(i\) carries predictive information because the hidden bath has not fully relaxed.

Therefore two preparations that are indistinguishable at the level of the reconstructed current position distribution can still correspond to different conditional hidden-state distributions.

Schematically,

$$
\rho_X^{(A)}(0)
=
\rho_X^{(B)}(0)
$$

but

$$
\rho_{Y|X}^{(A)}(0)
\neq
\rho_{Y|X}^{(B)}(0).
$$

The future observed dynamics can therefore differ.

The past measurement is useful as a proxy for hidden-state information, not because “history” is a new fundamental variable.

## 5. Mapping to the repository architecture

This experiment does not justify a direct one-to-one realization of every component of

$$
(R,q,\mu,K,\pi).
$$

A conservative mapping is:

### \(\pi\)

The observed distribution of particle position is an operational state distribution.

The experiment directly shows that the observed marginal distribution alone is not a universally sufficient dynamical state.

### \(K\)

The full dynamics can be regarded as Markovian on the enlarged state \(Z=(X,Y)\).

After eliminating \(Y\), an autonomous Markov kernel on \(X\) alone is not generally sufficient.

Thus the physically relevant transition structure depends on what is retained in the state description.

### \(q\)

The experiment has a calibrated harmonic potential

$$
V(x)=\frac12\kappa(x-\lambda)^2,
$$

and therefore physically meaningful energy observables.

No claim is made that the repository's abstract \(q\) is fundamentally this energy coordinate.

### \(R\) and \(\mu\)

No independent operational identification is needed for this bridge.

They remain uninstantiated rather than being assigned arbitrary meanings.

## 6. Same visible state, different future

This experiment supplies a physical version of a pattern that the repository has repeatedly studied mathematically:

$$
\boxed{
\text{same retained state}
\not\Rightarrow
\text{same future}
}
$$

when information relevant to the dynamics has been discarded.

The important strengthening here is that “same retained state” means the same **empirical position distribution**, not merely the same mean or one compressed score.

This makes the experiment a particularly strong retrospective calibration for dynamic nonclosure.

## 7. Memory decay provides a physical scale

The paper compares short measurement delay, such as

$$
\delta t=1\ {\rm s},
$$

with a much longer delay,

$$
\delta t=200\ {\rm s},
$$

that greatly exceeds the hidden-environment relaxation time.

At the long delay, the relaxation curves for fixed current outcome collapse as the hidden degrees of freedom equilibrate.

Thus the predictive relevance of the earlier measurement decays with the hidden environmental memory.

This gives a physical example in which the amount of history needed for prediction depends on the persistence timescale of omitted degrees of freedom.

It does **not** imply that physical time emerges from that persistence.

## 8. Information-level witness

The authors quantify the visible-state information using the KL divergence

$$
\mathcal I_{|ij\rangle}(t)
=
D_{\rm KL}
[
\rho_{|ij\rangle}(x,t)
\Vert
\rho_{\rm eq}(x)
].
$$

The history-blind control gives

$$
\tilde{\mathcal I}_{|ij\rangle}(t).
$$

By construction,

$$
\boxed{
\tilde{\mathcal I}_{|ij\rangle}(0)
=
\mathcal I_{|ij\rangle}(0),
}
$$

but the paper reports different subsequent relaxation, with the history-aware ensemble retaining excess information.

This is a scalar consequence of the stronger distribution-level witness.

## 9. What this says about adding state variables

A poor response to the observed nonclosure would be to invent an arbitrary memory scalar.

The established alternatives are:

1. retain the hidden physical degrees of freedom \(Y\) if they are modeled;
2. use an exact memory-kernel description after projection;
3. retain a sufficient statistic of observable history;
4. use a controlled approximation whose information loss is measured.

Which option is minimal is a separate question.

## 10. Causal-state boundary

The question

> What is the smallest function of the observed past that preserves the predictive distribution of the future?

is already classical.

Computational mechanics defines causal states as equivalence classes of past histories with identical conditional future distributions.

They are minimal sufficient statistics for prediction under the theory's assumptions.

Predictive-state representations provide a related controlled-systems language.

Therefore the repository must not introduce a renamed “minimal relational memory state” as though this problem were new.

A serious next step would instead compare any proposed repository state to the causal-state/predictive-state benchmark.

## 11. Empirical status

This bridge is retrospective because the Nature Physics experiment was published before this analysis.

The article itself already demonstrates hidden-memory effects and constructs the matched history-blind controls.

Therefore the bridge can support:

- compatibility with an independently observed physical nonclosure phenomenon;
- validation of the repository's methodological insistence on distinguishing current visible state from hidden/history information.

It cannot support:

- a project prediction made before the data;
- novelty for hidden-state memory;
- novelty for information backflow;
- novelty for causal states;
- a fundamental physical interpretation of the full repository architecture.

## 12. Data availability and reproducibility

The article provides processed source-data spreadsheets for its main figures and an open Zenodo dataset with analysis code.

The full raw experimental data are available from the corresponding authors upon reasonable request.

In the present session, the binary Springer XLSX files could not be loaded into the analysis runtime.

Therefore no numerical reproduction is claimed here.

The next reproducibility step is clearly separated from the conceptual result:

> load the official Fig. 2 and Fig. 3 source data, reconstruct the history-aware and history-blind relaxation differences, and verify the zero-time matching before calculating any project-specific metric.

Until that succeeds, the quantitative reproduction status remains **PENDING**.

## 13. Bridge comparison

### Bridge 1B — hidden external protocol

A drive phase is physically known at the conditioned level but discarded by ensemble averaging.

Closure changes with conditioning and temporal sampling.

### Bridge 2 — hidden environmental state

The hidden variables belong to the physical environment itself.

Observable histories contain predictive information about them.

These are different mechanisms.

Both produce the same methodological lesson:

$$
\boxed{
\text{a reduced description is sufficient only relative to what information is retained}.
}
$$

## 14. Strongest allowed conclusion

The two bridges jointly support the following modest physical statement:

> Established stochastic systems provide explicit cases in which the same retained observable description can fail to determine future evolution because dynamically relevant context or hidden-state information has been omitted.

This statement is well within existing stochastic-process theory.

Its value to the repository is that the abstract concern about informational sufficiency now has two concrete physical realizations with different mechanisms.
