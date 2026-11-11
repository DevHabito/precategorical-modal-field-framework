# Page-Wootters benchmark — reversible relational time without external noise

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** classical benchmark for the pregeometric programme  
**Novelty status:** Page-Wootters relational time is established; no project originality claim

## 1. Why this benchmark is required

The working research motivation previously suggested that temporal structure might arise when a relation is exposed to unresolved external influence or informational noise.

That idea must be tested against established relational-time models.

The Page-Wootters mechanism is a particularly important counterpoint because it recovers subsystem dynamics relative to an internal clock while the global state satisfies a stationary constraint.

External noise is not required for the ideal construction.

Therefore a strong claim of the form

> external unresolved influence is necessary for time to exist

is not compatible with this benchmark.

## 2. Ideal Page-Wootters assumptions

In the standard ideal construction:

1. the total Hilbert space factorizes,

$$
\mathcal H_U
=
\mathcal H_C\otimes\mathcal H_S;
$$

2. the clock and system have Hamiltonians \(H_C,H_S\);

3. in the ideal noninteracting case,

$$
H_U
=
H_C\otimes I
+
I\otimes H_S;
$$

4. the global state satisfies an energy constraint, usually

$$
H_U|\Psi\rangle=0;
$$

5. the clock has states that can serve as readings relative to its Hamiltonian.

Conditioning the global stationary state on a clock reading produces ordinary system evolution relative to that reading.

The construction is relational, but it does not start from an arbitrary unlabeled relation.

It already assumes a clock subsystem and Hamiltonian structure.

## 3. Finite diagnostic model

For a finite benchmark, let clock and system each have dimension \(d\).

Choose system energy levels

$$
E_k=k,
\qquad
k=0,\ldots,d-1.
$$

Define

$$
H_S
=
\sum_{k=0}^{d-1}
E_k|k\rangle\langle k|
$$

and

$$
H_C
=
-\sum_{k=0}^{d-1}
E_k|k\rangle\langle k|.
$$

Use the entangled global state

$$
\boxed{
|\Psi\rangle
=
\frac1{\sqrt d}
\sum_{k=0}^{d-1}
|k\rangle_C|k\rangle_S.
}
$$

Then term by term,

$$
(H_C+H_S)|\Psi\rangle=0.
$$

The global state is stationary under the constraint.

## 4. Internal clock readings

Define finite clock pointer states

$$
|t_n\rangle_C
=
\frac1{\sqrt d}
\sum_{k=0}^{d-1}
e^{iE_kt_n}
|k\rangle_C,
$$

with

$$
t_n=\frac{2\pi n}{d},
\qquad
n=0,\ldots,d-1.
$$

Conditioning the global state on \(t_n\) gives

$$
{}_C\langle t_n|\Psi\rangle
\propto
\sum_k
e^{-iE_kt_n}|k\rangle_S.
$$

After normalization,

$$
\boxed{
|\psi(t_n)\rangle_S
=
e^{-iH_St_n}|\psi(0)\rangle_S,
}
$$

where

$$
|\psi(0)\rangle
=
\frac1{\sqrt d}
\sum_k|k\rangle.
$$

Thus reversible system evolution is recovered relative to the internal clock.

## 5. Diagnostic computation

The repository includes a dependency-light numerical audit for

$$
d\in\{2,3,4,5,8\}.
$$

For every tested dimension:

- the global Hamiltonian-constraint residual is exactly zero in floating-point arithmetic for the diagonal construction;
- the normalized conditional state agrees with the target unitary state to approximately \(10^{-16}\) in Euclidean norm.

This is a regression of a classical construction, not evidence for a project theory.

## 6. Why this is a counterexample to the strong noise-origin claim

The model contains:

- reversible conditional dynamics;
- distinguishable clock readings;
- relational change;

without requiring:

- environmental noise;
- entropy production;
- information loss to an external system;
- a coarse-grained irreversible arrow.

Therefore

$$
\boxed{
\text{external informational noise is not necessary for relational temporal description}.
}
$$

This does not settle whether such relational time is fundamental in nature.

It only prevents the project from claiming noise as a universal necessary condition.

## 7. What external noise can still do

The previous physical bridges remain relevant.

Unresolved external or hidden information can:

- destroy closure of a reduced state;
- generate memory;
- change required predictive-state dimension;
- produce an effective arrow;
- degrade a physical clock;
- make temporal coarse-graining scale-dependent.

These are questions about **quality and sufficiency of temporal description**, not the universal existence of relational time.

## 8. Revised working hypothesis

The strong formulation should be rejected:

> Time exists because relations are exposed to unresolved external noise.

A safer surviving research direction is:

> Persistent unresolved external influence can change the amount of relational information required to describe evolution relative to an internal or already-defined ordering structure.

An even narrower experimentally grounded version is:

> Marginalizing persistent external information can make an instantaneous reduced state dynamically insufficient, and the required memory can depend on the temporal resolution of observation.

The electronic and hidden-environment bridges support this narrower statement.

## 9. What Page-Wootters does not solve for this project

The benchmark does not give the project a pregeometric solution for free.

It assumes:

- a Hilbert-space factorization;
- Hamiltonians;
- a clock subsystem;
- a constraint structure;
- an appropriate clock observable or clock states.

Therefore it does not answer the project's harder question:

> Why should a suitable clock/order structure exist in the first place?

It handles reversible relational evolution once an internal clock structure is available.

## 10. Finite-clock limitations

Ideal Page-Wootters clocks are often formulated with idealized clock observables.

Finite clocks have:

- finite resolution;
- periodicity/recurrence;
- bounded distinguishability;
- possible clock-system interaction errors.

Modern work studies quasi-ideal clocks and interaction-induced corrections.

This reinforces the separation between:

$$
\text{relational time exists}
$$

and

$$
\text{a real clock represents it accurately}.
$$

## 11. Relation to SCC macro-order

The SCC construction and Page-Wootters benchmark solve different problems.

### SCC condensation

Produces an acyclic macro-order by collapsing reversible/cyclic sectors.

### Page-Wootters

Represents reversible evolution *inside* a relational clock description without requiring a monotone scalar arrow.

This suggests an important project distinction:

$$
\boxed{
\text{arrow/order between sectors}
\neq
\text{reversible relational evolution within sectors}.
}
$$

A future pregeometric framework may need to account for both rather than forcing them into one scalar time variable.

## 12. Current classification

**PAGE-WOOTTERS AS EXISTING BENCHMARK: RETAINED.**

**EXTERNAL NOISE AS NECESSARY ORIGIN OF ALL TIME: REJECTED.**

**EXTERNAL PERSISTENCE AS A SOURCE OF MEMORY/ARROW IN REDUCED DESCRIPTIONS: RETAINED AND PHYSICALLY SUPPORTED.**

## 13. Next question

The strongest open question left by this benchmark is:

> Can the repository derive a clock-like relational structure from a genuinely non-temporal primitive model, rather than assuming either a causal partial order or a clock Hamiltonian?

No answer has yet been established.
