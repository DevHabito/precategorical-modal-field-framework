# Audit of observational dependence as a timeless temporal-order candidate

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** observational dependence rejected as a sufficient universal source of temporal direction  
**Novelty status:** Markov equivalence and causal-discovery limits are classical

## 1. Candidate

After rejecting simple information degradation as a universal time order, a second natural possibility is:

> derive direction from statistical dependence structure without assuming time.

This is attractive because conditional independences can be defined on an unordered collection of random variables.

If the dependency pattern uniquely selected a directed acyclic graph, one might hope to interpret that direction as a primitive order.

The classical causal-discovery literature shows that this hope is too strong.

## 2. Minimal Markov-equivalence obstruction

Consider three variables \(A,B,C\).

The DAGs

$$
A\to B\to C,
$$

$$
A\leftarrow B\to C,
$$

and

$$
A\leftarrow B\leftarrow C
$$

have:

- the same undirected skeleton \(A-B-C\);
- no v-structure/collider.

Therefore they are Markov equivalent.

Under the standard Markov and faithfulness assumptions they imply the same conditional-independence pattern:

$$
\boxed{
A\perp C\mid B.
}
$$

Observational conditional independences alone cannot choose among these three orientations.

## 3. Consequence

The same timeless observational distribution can be compatible with different directed causal structures.

Therefore

$$
\boxed{
\text{observational dependence structure}
\not\Rightarrow
\text{unique directed order}.
}
$$

A temporal interpretation cannot be recovered uniquely from conditional independence alone.

## 4. Why collider information is not enough

A collider such as

$$
A\to B\leftarrow C
$$

has a distinct conditional-independence signature and can orient some edges under suitable assumptions.

But a general graph can still contain unoriented edges within its Markov equivalence class.

Causal-discovery algorithms therefore return objects such as CPDAGs or PAGs when direction is not identifiable.

This is the correct representation of uncertainty.

The repository must not convert an unoriented edge into a temporal arrow merely because one is desired.

## 5. Additional assumptions can orient edges

Causal direction can sometimes be recovered by adding structure such as:

- interventions;
- temporal ordering already known from measurements;
- non-Gaussian additive-noise assumptions;
- functional restrictions;
- causal sufficiency;
- faithfulness;
- domain knowledge.

These are legitimate scientific assumptions when independently justified.

They are not free consequences of the observational distribution.

For a pregeometric programme, each extra assumption must be checked for hidden temporal content.

## 6. Interventions do not automatically solve the origin-of-time problem

Interventions can break Markov equivalence and identify causal direction.

However, intervention semantics distinguish manipulated variables from downstream responses.

That supplies an operational causal asymmetry.

Using interventions may therefore help reconstruct a causal graph in a laboratory, but it does not automatically explain the origin of temporal order in a closed timeless universe.

The intervention framework is a benchmark, not yet a pregeometric solution.

## 7. Relation to the anti-circularity gate

A future timeless derivation may use an intrinsic asymmetry in the primitive structure.

It may not:

- infer an edge direction from data when the Markov equivalence class leaves it unresolved;
- use measurement timestamps to orient edges and then claim time was derived;
- use intervention order as a hidden temporal label without declaring it;
- select one DAG from an equivalence class because it matches the desired interpretation.

## 8. What observational causal structure remains useful for

Conditional independence remains valuable for:

- detecting screening relations;
- identifying equivalence classes of admissible causal structures;
- ruling out candidate orderings;
- exposing hidden confounding;
- defining what additional experiments are required.

So the result is not “causal discovery is useless.”

It is narrower:

$$
\boxed{
\text{observational CI alone is insufficient as a universal generator of temporal direction}.
}
$$

## 9. Current pregeometric candidate status

### Candidate 1 — Blackwell degradation

Rejected as universal time because reversible dynamical change can remain Blackwell-equivalent and the order is incomplete.

### Candidate 2 — observational conditional-dependence orientation

Rejected as sufficient because Markov-equivalent DAGs can have different directions while generating the same observational independence structure.

The next candidate must introduce a genuine asymmetry without smuggling in an external temporal label.

## 10. Scientific boundary

This audit proves no no-go theorem against all informational approaches to time.

It rules out two particularly simple identifications.

A richer timeless structure may still support an intrinsic order.

But any such proposal must contain enough information to resolve the equivalences identified above.
