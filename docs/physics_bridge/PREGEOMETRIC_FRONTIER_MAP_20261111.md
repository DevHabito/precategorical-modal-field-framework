# Pregeometric frontier map after Physical Bridge V1

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Purpose:** identify what is settled, what is classical, what has failed, and what remains worth researching

## 1. Questions that should not be reopened as project novelties

The following have mature existing theory.

| Question | Established framework |
|---|---|
| Does hidden-variable elimination generate memory/non-Markovianity? | Mori-Zwanzig, hidden-state processes |
| When does a Markov projection remain Markov? | Lumpability/intertwining |
| What is the minimal statistic of past observations for future prediction? | Causal states/computational mechanics, predictive-state representations |
| Can observables form finite invariant dynamical subspaces? | Koopman/operator invariant-subspace theory |
| Can periodically driven systems be analyzed by one-period maps? | Floquet/monodromy theory |
| Can quantum dynamics be formulated without predefined global causal order? | Process matrices and related operational frameworks |
| Can relational evolution be recovered from an internal clock? | Page-Wootters and relational-clock theory |
| Can a partial order encode pregeometric causal structure? | Causal-set theory |
| Can q-adapted birth-death operators have exact polynomial spectra? | Stieltjes-Wigert/q-orthogonal-polynomial theory |

These subjects remain useful benchmarks and tools.

They are not open project claims.

## 2. Candidate routes already rejected in strong form

### Time as information degradation

Rejected.

Blackwell-equivalent reversible transformations can represent distinct dynamical change.

### Time direction from passive observational dependence

Rejected.

Markov-equivalent DAGs can encode different directions with the same observational conditional independences.

### External noise as a necessary origin of all time

Rejected.

Page-Wootters gives a counterbenchmark with reversible relational evolution and no external noise requirement.

### SCC condensation as universal physical time

Rejected.

It collapses all internal recurrent dynamics and contains no duration.

## 3. Candidate routes retained only conditionally

### SCC condensation

Retained as a canonical macro-order of one-way accessibility after a directed relation is already justified.

### Operational signalling

Retained as a causal-orientation reconstruction tool in an intervention-capable, orderable sector.

### Entropy/information monotones

Retained as possible arrows or clocks in restricted regimes, not as universal origins of time.

### Page-Wootters

Retained as a benchmark for reversible relational evolution once clock/Hamiltonian structure is available.

## 4. Exact mathematical gates now established

The programme now requires:

1. label invariance;
2. anti-circularity;
3. orderability before order;
4. automorphism/symmetry audit;
5. cycle/acyclicity audit for strict scalar ranks;
6. separation of order from duration;
7. declared reduction contract \((S,O,\Xi,\mathcal P,\mathcal T)\);
8. explicit preparation-specific versus universal closure status;
9. classical-prior-art audit before novelty language.

Several finite algebraic cores are Lean/kernel checked.

## 5. The foundational gap that remains

The repository currently starts much of its relational mathematics with a directed \(R\).

For pregeometry, this leaves the key question unresolved:

$$
\boxed{
\text{What non-temporal physical structure justifies the orientation of }R?
}
$$

If the arrow of \(R\) already means “earlier influences later,” temporal direction has been assumed.

If the arrow has another operational meaning, the project must define that meaning and derive the temporal interpretation separately.

## 6. Small Question F1 — intrinsic orientability

Let \(\mathfrak P\) be a finite unlabeled primitive structure and let \(a,b\) be two elements.

Question:

> Are the ordered pairs \((a,b)\) and \((b,a)\) in the same orbit under \(\operatorname{Aut}(\mathfrak P)\)?

If yes, the symmetry gate forbids any canonical isomorphism-equivariant strict orientation of that pair.

If no, the primitive structure contains enough asymmetry to distinguish the two orientations in principle.

This does **not** yet make either orientation temporal.

It identifies where intrinsic directional information exists.

### Why F1 is useful

- finite;
- exact;
- label invariant;
- computationally testable;
- compatible with Lean formalization;
- does not assume time;
- exposes whether a proposed arrow comes from structure or convention.

### Literature status

The group-action mathematics is classical.

The project-specific value would be using it as a systematic pregeometric gate across the repository's finite relational models.

No novelty claim is attached to the orbit criterion itself.

## 7. Small Question F2 — physical semantics of an intrinsically oriented pair

If F1 finds an intrinsically distinguishable orientation, ask:

> What operational quantity distinguishes the two ordered-pair orbits?

Candidates must be defined without “before” or “after.”

Examples to test, not assume:

- one-way convertibility;
- intervention/signalling asymmetry;
- recoverability asymmetry;
- compatibility constraints;
- resource monotones.

This is where physics enters.

A purely combinatorial asymmetry is not automatically a causal asymmetry.

## 8. Small Question F3 — definite-order recovery

Given an operational structure with asymmetric influence information, determine whether it admits a definite partial order.

This is an orderability problem.

The project should compare the result against:

- causal models;
- process matrices;
- causal separability;
- cyclic causal models.

If the system is not orderable, retain that result rather than forcing a DAG.

## 9. Small Question F4 — reversible sector

If the macroscopic order quotients a strongly connected/reversible sector, ask:

> What internal relational clock, if any, describes change inside that sector?

This is where Page-Wootters and relational-clock theory become the benchmark.

The project should not ask a monotone macro-order to represent reversible internal dynamics.

## 10. Small Question F5 — duration

Only after an order/clock structure exists, ask:

> What quantity behaves as physical duration and is stable under irrelevant refinement?

Required checks include:

- dimensional scale;
- clock correspondence;
- refinement law;
- continuum/experimental calibration.

Graph depth alone fails this gate.

## 11. First recommended computational task

The next low-risk calculation is F1.

For selected finite relational models already in the repository:

1. remove any purely conventional labels;
2. compute the automorphism group;
3. compute orbits of ordered pairs;
4. identify pairs whose reverse lies in the same orbit;
5. classify which proposed directions are structurally orientable;
6. repeat after removing primitive arrow orientation to test whether the direction was assumed;
7. document all failures.

This does not produce a theory of time.

It tells the project exactly where a non-temporal arrow could or could not be encoded by the current structures.

## 12. Promotion rule

No pregeometric result should be promoted beyond **MATHEMATICAL STRUCTURE** until it completes:

$$
\text{intrinsic asymmetry}
\to
\text{operational semantics}
\to
\text{orderability}
\to
\text{relational evolution}
\to
\text{duration/recovery}
\to
\text{empirical/model discrimination}.
$$

Skipping a stage turns the bridge into interpretation rather than derivation.

## 13. Current research frontier

The best next question is no longer

> What equation should I invent?

It is:

$$
\boxed{
\text{Does the existing primitive relational structure contain any label-free asymmetric information at all?}
}
$$

If the answer is no, a temporal arrow cannot emerge from that structure without additional data.

If the answer is yes, the next question is whether that asymmetry has a physical operational meaning rather than being merely combinatorial.

This is the smallest rigorous step currently available.


## 14. Direction V1 update

The F1/F2 programme has now advanced beyond simple intrinsic orientability.

The canonical direction synthesis is:

PREGEOMETRIC_DIRECTION_V1_SYNTHESIS_20261111.md.

The frontier is now:

$$
\text{symmetry breaking}
\to
\text{orientability}
\to
\boxed{\text{polarity}}
\to
\text{physical order}
\to
\text{duration}.
$$

The first open stage is polarity: a non-temporal physical reason to choose one of two reversed, symmetry-compatible orientations.

This replaces the earlier broad F2 wording.
