# Loop chirality is not temporal order

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** physical counterbenchmark using the four-site magnetic-flux ring  
**Novelty status:** standard ring symmetry and Aharonov-Bohm/Peierls physics

## 1. Question

The cycle-space audits found a gauge-invariant loop degree of freedom.

Could a nonzero loop circulation itself be interpreted as temporal order?

The four-site magnetic ring gives a clean negative answer.

## 2. Uniform-flux ring

Take the four-site Hamiltonian

$$
H(\Phi)
=
-J
\sum_{j=0}^{3}
\left(
e^{i\Phi/4}|j\rangle\langle j+1|
+
e^{-i\Phi/4}|j+1\rangle\langle j|
\right).
$$

For generic nonzero \(\Phi\), the loop carries a nontrivial gauge-invariant holonomy.

The flux distinguishes the two loop orientations through

$$
\Phi\leftrightarrow-\Phi.
$$

## 3. Rotation symmetry remains exact

Let \(T\) translate the ring by one site,

$$
T|j\rangle=|j+1\rangle.
$$

Because every hopping edge carries the same phase in the uniform gauge,

$$
\boxed{
[T,H(\Phi)]=0.
}
$$

Thus all four sites remain equivalent under cyclic rotation.

The loop has chirality without a distinguished origin vertex.

## 4. Reflection reverses the flux

Let \(R\) reflect the ring,

$$
R|j\rangle=|-j\rangle.
$$

Then

$$
\boxed{
RH(\Phi)R^\dagger
=
H(-\Phi).
}
$$

For generic flux, reflection is therefore not a symmetry of one fixed-\(\Phi\) Hamiltonian unless it is accompanied by flux reversal.

This is the physical asymmetry carried by the holonomy.

## 5. Why there is still no temporal vertex order

A strict temporal order on the four sites would need to distinguish at least some vertex pair.

But cyclic rotation acts transitively on the sites.

Any canonical ordering derived only from the uniform-flux ring while respecting rotation symmetry cannot select one site as a first element.

Furthermore, orienting the sites cyclically as

$$
0\prec1\prec2\prec3\prec0
$$

would not be a strict partial order because it contains a cycle.

Therefore:

$$
\boxed{
\text{loop chirality}
\not\Rightarrow
\text{vertex temporal precedence}.
}
$$

## 6. What the flux actually supplies

The magnetic flux supplies an orientation-sensitive **loop property**.

It can affect:

- quantum phases;
- interference;
- energy levels;
- persistent currents;
- time-reversal/reflection properties.

It does not, by itself, provide:

- a first event;
- a partial order of sites;
- duration;
- a clock variable;
- causal precedence among the ring vertices.

This is the semantic separation the pregeometric programme needs.

## 7. Relation to C1

The graphA skeleton also contains one independent four-cycle.

Its one-dimensional cycle space can mathematically carry a chirality variable.

Bridge 3A shows that such a variable can have a completely non-temporal physical meaning.

Therefore the existence of a nonzero cycle class in graphA is insufficient evidence for emergent time.

## 8. Rotation versus reflection

This benchmark separates two types of symmetry breaking.

### Reflection/chirality

A signed loop field can distinguish clockwise from counterclockwise orientation.

### Translation/origin

The same field can leave all locations on the loop equivalent.

Breaking the first does not break the second.

A temporal ordering usually needs more structure than chirality alone.

## 9. Consequence for symmetry budgets

The previous distinguishing-color audit asked how many marks are needed to destroy all graph automorphisms.

The magnetic ring shows why that stronger requirement matters.

A single loop flux breaks reflection but leaves a nontrivial rotation group.

Thus an orientation-sensitive loop scalar may reduce the automorphism group without making the structure fully distinguishable.

The remaining symmetry still blocks a canonical vertex order.

## 10. Current pregeometric lesson

The direction-source problem has at least two independent layers:

1. **chirality:** distinguish a relation from its reversal;
2. **precedence:** identify an acyclic before/after structure among events.

A loop circulation can solve the first while failing the second.

Therefore future work must not treat “preferred sense around a loop” and “temporal order” as synonyms.

## 11. Current classification

**Gauge-invariant loop chirality:** PHYSICALLY REALIZABLE.

**Canonical temporal order from chirality alone:** REJECTED.

**Physical duration from chirality:** REJECTED.

**Use as a benchmark for asymmetric relational structure:** RETAINED.
