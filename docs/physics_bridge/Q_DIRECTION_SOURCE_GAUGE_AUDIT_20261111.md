# q as a pregeometric direction source — gauge audit

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** current q operationalization rejected as a sufficient primitive direction source  
**Scope:** A21-A24 / current foundational q contract

## 1. Question

The symmetry-orientation gate shows that a directed primitive relation requires genuine asymmetric information.

The existing foundational programme already introduced an additional quantitative field \(q\) precisely because relation/order data alone do not identify all latent structure.

This raises a natural question:

> Can the current \(q\) supply the non-temporal asymmetry needed to orient primitive relations?

The answer is only partially positive.

A genuinely independent calibrated \(q\) can break an order-only symmetry class.

The current operational contract does **not** make reciprocal edge orientation gauge-identifiable.

## 2. What A21-A23 already establish

A21 proves a general equivariance obstruction:

> If the complete endogenous state, update law, and model-independent randomness respect the same latent symmetry, the observed trajectories remain symmetry-related.

Therefore purely endogenous equivariant evolution does not select one representative inside the targeted equivalence class.

A22 then gives the necessary route around the obstruction:

> an added primitive can break the degeneracy only if its conditional marked law is not invariant across the latent representatives.

A23 applies this logic to \(q\):

- if \(q\) is determined by \(R\), it is redundant;
- if \(q\) is independent model-blind noise, it does not identify the representative;
- if \(q\) is a genuinely additional calibrated field, it can carry information absent from \(R\);
- the physical origin and calibration of the actual RZS \(q\) remain unresolved.

This is fully consistent with the new symmetry-orientation gate.

## 3. The A24 operational kernel

A24 uses the local witness

$$
K_\beta(i,j)
=
\frac{A_{ij}e^{-\beta q_{ij}}}
{\sum_kA_{ik}e^{-\beta q_{ik}}}.
$$

Within one source row,

$$
\log
\frac{K_\beta(i,j)}
{K_\beta(i,k)}
=
-\beta(q_{ij}-q_{ik}).
$$

Thus, when \(\beta\) is calibrated, the observable transition frequencies identify local \(q\)-contrasts.

This is a valid operational witness.

## 4. Row gauge

The same kernel is invariant under an independent offset for every source:

$$
\boxed{
q_{ij}\mapsto q_{ij}+c_i.
}
$$

Indeed,

$$
K_\beta(i,j;q+c_i)
=
K_\beta(i,j;q).
$$

Therefore only within-row contrasts are identified by this kernel.

## 5. Reciprocal-edge orientation fails the gauge test

Suppose both directions between \(i\) and \(j\) are admissible.

A tempting direction score is

$$
D_{ij}=q_{ij}-q_{ji}.
$$

One could try to define

$$
i\prec j
\quad\Longleftrightarrow\quad
D_{ij}<0
$$

or the opposite convention.

But under the A24 row gauge,

$$
q_{ij}\mapsto q_{ij}+c_i,
\qquad
q_{ji}\mapsto q_{ji}+c_j,
$$

so

$$
\boxed{
D_{ij}
\mapsto
D_{ij}+c_i-c_j.
}
$$

Because \(c_i\) and \(c_j\) are independently arbitrary, the transformed reciprocal difference can be assigned any real value.

For any target \(r\), choose

$$
c_i-c_j=r-D_{ij}.
$$

Then

$$
D_{ij}'=r.
$$

In particular the sign can be reversed while the entire transition matrix \(K_\beta\) remains unchanged.

Therefore

$$
\boxed{
\operatorname{sign}(q_{ij}-q_{ji})
\text{ is not operationally identifiable under the current A24 kernel}.
}
$$

## 6. Consequence

The current edge \(q\)-field can rank alternatives **from the same source**.

It cannot canonically compare the raw \(q\) values attached to opposite directions coming from different source rows.

Thus:

$$
\boxed{
\text{local preference information}
\neq
\text{gauge-invariant reciprocal orientation}.
}
$$

This distinction is important for pregeometry.

## 7. Vertex-potential alternative

Suppose instead that a scalar mark

$$
\varphi:V\to\mathbb R
$$

were independently supplied on vertices.

One could orient an undirected edge by

$$
u\to v
\quad\Longleftrightarrow\quad
\varphi(u)<\varphi(v).
$$

This rule is:

- label-equivariant;
- invariant under global additive shifts;
- invariant under positive rescaling;
- asymmetric when endpoint values differ.

However, it has an exact limitation.

Along every oriented edge,

$$
\varphi
$$

strictly increases.

Therefore no directed cycle can occur.

A scalar vertex potential can generate only an acyclic orientation.

So it cannot reconstruct the cyclic orientation present in graphA.

This is the standard distinction between gradient/potential structure and circulation.

## 8. Edge fields and circulation

To orient a genuinely cyclic structure without inserting an explicit directed graph, a scalar potential is insufficient.

A more general antisymmetric edge field

$$
F_{ij}=-F_{ji}
$$

can contain a non-gradient/circulatory component.

If

$$
F_{ij}=\varphi_j-\varphi_i,
$$

then every closed-cycle sum vanishes:

$$
\sum_{\rm cycle}F_{ij}=0.
$$

A nonzero cycle circulation therefore certifies that the edge field is not globally generated by one scalar potential.

This is classical discrete Hodge/flow structure.

It may be a useful mathematical language for future direction-source candidates.

It is **not** yet a physical explanation of why such a field exists.

## 9. Current q versus an antisymmetric 1-form

The current A24 \(q_{ij}\) is a source-normalized transition score.

It is not automatically an antisymmetric physical edge 1-form.

Constructing

$$
q_{ij}-q_{ji}
$$

does not solve this because that expression is row-gauge dependent.

Therefore the project must not silently reinterpret the current \(q\) as a gauge-invariant circulation field.

A future field intended to carry intrinsic directional information would need its own:

- transformation law;
- gauge group;
- observable coupling;
- operational calibration;
- locality contract;
- physical origin.

## 10. Cycle affinity is an important benchmark

For a Markov jump process with forward/backward rates, stochastic thermodynamics defines cycle affinities from log rate ratios.

Cycle affinity is gauge-invariant and measures nonequilibrium driving around cycles.

This is established theory.

It shows that physically meaningful gauge-invariant cyclic asymmetry is possible.

But it does not solve the present pregeometric problem:

- the rates already belong to a dynamical transition law;
- transition trajectories already use temporal dynamics;
- thermodynamic affinity therefore cannot be used as evidence that time itself emerged.

It is a benchmark for what a physically operational cyclic asymmetry looks like **after dynamics is defined**.

## 11. F2 verdict

### Can additional \(q\)-information break an \(R\)-only symmetry?

**YES, conditionally.**

This was already established by A21-A23 when \(q\) is genuinely independent and non-invariant.

### Does the current A24 operational \(q\) provide a gauge-invariant reciprocal edge direction?

**NO.**

The sign of \(q_{ij}-q_{ji}\) is row-gauge dependent.

### Can a single scalar potential generate arbitrary directed relations?

**NO.**

Its strict-gradient orientation is acyclic.

### Is a non-gradient edge field mathematically capable of carrying cyclic direction?

**YES.**

This is classical edge-flow/Hodge structure.

### Has the project derived a physical non-temporal circulation field?

**NO.**

That remains open.

## 12. Revised frontier

The direction-source problem is now sharper.

The missing object cannot merely be:

- a deterministic function of \(R\);
- model-independent noise;
- a label convention;
- the raw reciprocal difference of the current A24 edge scores;
- one global scalar potential if cyclic orientation must be represented.

The next admissible candidate must be a label-invariant, gauge-invariant, operationally meaningful asymmetric quantity whose origin is specified independently of the temporal interpretation it is later asked to support.
