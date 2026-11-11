# Canonical-mark obstruction on the C1 witness skeletons

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact finite orbit obstruction  
**Conclusion:** no deterministic isomorphism-invariant vertex mark derived solely from the unmarked C1 skeleton can generate the symmetry-breaking pattern needed for the audited orientation doublet

## 1. Why this audit matters

The pre-time-orientation audit found a useful finite pattern:

the graphA square \(C_4\), when equipped with an alternating binary mark,

$$
(0,1,0,1),
$$

admits exactly one acyclic orientation class modulo global reversal.

That does **not** imply that the unmarked graphA skeleton derives such a mark.

This audit tests that missing step.

## 2. Canonical vertex marks must respect automorphisms

Let \(G\) be an unmarked graph and let

$$
m:V(G)\to X
$$

be a deterministic mark constructed canonically from \(G\).

Isomorphism invariance requires

$$
m(\sigma v)=m(v)
$$

for every

$$
\sigma\in\operatorname{Aut}(G).
$$

Therefore \(m\) is constant on every automorphism orbit.

This is elementary group-action logic.

## 3. graphA skeleton

The graphA skeleton is a four-cycle on

$$
\{0,2,3,4\}
$$

plus isolated vertex \(1\).

Its automorphism group has eight elements.

The orbit decomposition is

$$
\boxed{
\{0,2,3,4\},
\qquad
\{1\}.
}
$$

All four cycle vertices belong to one orbit.

Therefore every canonical scalar vertex mark derived solely from the skeleton must satisfy

$$
\boxed{
m(0)=m(2)=m(3)=m(4).
}
$$

It cannot produce an alternating pattern around the cycle.

## 4. Exact binary enumeration

There are

$$
2^5=32
$$

binary vertex colorings of the five vertices.

Only four are invariant under the full automorphism group of the unmarked graphA skeleton:

$$
(0,0,0,0,0),
$$

$$
(0,1,0,0,0),
$$

$$
(1,0,1,1,1),
$$

and

$$
(1,1,1,1,1),
$$

where the coordinate order is \(0,1,2,3,4\).

None alternates around the four-cycle.

Therefore none yields the orientation doublet identified in the previous audit.

## 5. graphB skeleton

The graphB skeleton is:

- a triangle on \(\{0,2,3\}\);
- an isolated edge on \(\{1,4\}\).

Its automorphism group has twelve elements.

The vertex orbits are

$$
\boxed{
\{0,2,3\},
\qquad
\{1,4\}.
}
$$

A canonical scalar vertex mark derived solely from the skeleton must be constant on each of these two orbits.

The exact binary invariant colorings are again only four.

They can distinguish the two connected-component types.

They cannot orient the triangle internally or distinguish the two endpoints of the isolated edge.

## 6. Degree and other simple structural marks

This orbit obstruction includes ordinary canonical vertex diagnostics such as:

- degree;
- component size;
- triangle membership;
- local motif counts;
- any deterministic message-passing feature that remains automorphism invariant.

For graphA, every cycle vertex has the same degree and the same unmarked structural environment.

For graphB, the three triangle vertices remain equivalent and the two edge endpoints remain equivalent.

Thus adding more deterministic structural post-processing does not create the missing polarity.

## 7. Relation to the symmetry-orientation theorem

This is the mark-level version of the previous no-go.

If a primitive automorphism maps \(u\) to \(v\), then every invariant scalar mark must assign

$$
m(u)=m(v).
$$

Consequently an invariant mark cannot later be invoked as if it had independently broken that same symmetry.

Doing so would merely hide a non-invariant choice in the mark construction.

## 8. Consequence for q

A q-field can break the graphA cycle symmetry only if q contains information not determined by the unmarked graphA skeleton.

This is exactly consistent with A21-A23:

$$
q=F(R,\text{model-independent invariant data})
$$

cannot distinguish states inside an automorphism orbit if \(F\) is equivariant.

A physically useful q therefore needs an independently justified source.

## 9. Consequence for the orientation doublet

The alternating mark demonstrates **sufficiency**:

> if such a mark exists, an orientation doublet can be defined.

It does not establish **origin**:

> why should such a mark exist on graphA?

Therefore the orientation-doublet result must remain classified as a conditional finite construction.

## 10. Physical interpretation

This is scientifically useful because it prevents a subtle form of ad hoc reasoning.

One cannot:

1. inspect the orientation one wants;
2. choose a coloring that makes it possible;
3. call the coloring emergent from the same symmetric graph.

The mark needs independent physical semantics.

## 11. Current verdict

**Can graphA's unmarked skeleton derive the alternating binary mark canonically?**  
NO.

**Can a deterministic isomorphism-invariant scalar mark split one automorphism orbit?**  
NO.

**Can an independent physical mark split the orbit?**  
YES, in principle.

**Does the repository currently possess such a physical mark for graphA?**  
NO established mapping.

## 12. Revised pre-time-orientation problem

The finite criterion is now correctly factored:

$$
\boxed{
\text{unmarked structure}
+
\text{independently justified mark}
\longrightarrow
\text{orientation doublet}.
}
$$

The missing physical bridge is the origin and semantics of the mark, not the combinatorics of the doublet.
