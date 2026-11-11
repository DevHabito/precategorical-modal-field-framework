# Symmetry-breaking is operation-relative

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact finite group-action audit + classical symmetry-breaking context  
**Novelty status:** automorphism stabilizers and distinguishing colorings are classical; project-specific role is to align symmetry-breaking requirements with the operation being requested

## 1. Why one symmetry budget is not enough

The previous audit used the classical distinguishing number.

A distinguishing coloring removes **every** nontrivial automorphism.

That is stronger than many operations actually require.

For pregeometric work, at least three distinct targets should be separated:

1. orient one selected ordered pair;
2. distinguish the chirality of a cycle;
3. eliminate every structural automorphism.

The minimum additional information can differ across these tasks.

## 2. Marked automorphism group

Let \(G\) be an unmarked graph and let

$$
\ell:V(G)\to\{1,\ldots,k\}
$$

be a vertex mark.

Define the mark-preserving subgroup

$$
\operatorname{Aut}(G,\ell)
=
\{
g\in\operatorname{Aut}(G):
\ell(gv)=\ell(v)\ \forall v
\}.
$$

The added mark changes what can be selected canonically by shrinking the symmetry group.

## 3. Pair-orientability criterion

Fix distinct vertices \(a,b\).

The ordered pair

$$
(a,b)
$$

is intrinsically orientable relative to the marked structure if its reverse

$$
(b,a)
$$

does not lie in the same orbit under

$$
\operatorname{Aut}(G,\ell).
$$

Equivalently, there is no mark-preserving automorphism \(g\) such that

$$
g(a)=b,
\qquad
g(b)=a.
$$

This is exactly the finite version of the symmetry-orientation gate.

It is weaker than full distinguishability.

## 4. Cycle-chirality criterion

For a cycle, a mark selects chirality if no mark-preserving automorphism reverses the orientation of the cycle.

Rotations are allowed.

Thus a structure can have a preferred clockwise/counterclockwise sense while still lacking a distinguished origin vertex.

The magnetic-ring bridge demonstrated the physical importance of this distinction.

## 5. Full distinguishing criterion

A marking is fully distinguishing when

$$
\operatorname{Aut}(G,\ell)
=
\{\mathrm{id}\}.
$$

This removes both reflections and nontrivial rotations.

It is the strongest of the three targets considered here.

## 6. Exhaustive cycle audit

For cycles

$$
C_n,\qquad n=3,\ldots,8,
$$

the repository enumerates every coloring for alphabets \(k=1,2,3\).

For each coloring it computes:

- whether the target edge \((0,1)\) can be reversed by a mark-preserving automorphism;
- whether any reflection survives;
- whether any nonidentity automorphism survives.

The exact counts are:

| \(n\) | \(k\) | pair-orienting | chirality-selecting | fully distinguishing |
|---:|---:|---:|---:|---:|
|3|1|0|0|0|
|3|2|4|0|0|
|3|3|18|6|6|
|4|1|0|0|0|
|4|2|12|0|0|
|4|3|72|24|24|
|5|1|0|0|0|
|5|2|24|0|0|
|5|3|216|120|120|
|6|1|0|0|0|
|6|2|56|12|12|
|6|3|702|450|444|
|7|1|0|0|0|
|7|2|112|28|28|
|7|3|2106|1638|1638|
|8|1|0|0|0|
|8|2|240|96|96|
|8|3|6480|5352|5328|

## 7. The C4 lesson

The graphA skeleton is \(C_4\).

With two marks:

- there are \(2^4=16\) colorings;
- 12 orient the selected edge \((0,1)\);
- zero choose a global cycle chirality;
- zero fully distinguish the cycle.

Therefore:

$$
\boxed{
\text{binary information can orient a local pair without orienting the whole cycle}.
}
$$

This corrects a possible overreading of the earlier distinguishing-number result.

## 8. Why the pair can be oriented with two colors

If the endpoints of the selected edge carry different marks, no mark-preserving automorphism can exchange them.

That is already enough to make

$$
(a,b)
$$

and

$$
(b,a)
$$

different marked orbits.

But the rest of the graph can retain reflections or rotations.

Thus local orientation does not imply a global arrow.

## 9. Hierarchy of symmetry-breaking demands

For cycle structures the audits now exhibit the hierarchy

$$
\boxed{
\text{local pair orientation}
\;\;\text{can require less information than}\;\;
\text{global chirality}
\;\;\text{can require no more than}\;\;
\text{full distinction}.
}
$$

For \(C_4\):

$$
\boxed{
2\text{ symbols suffice locally,}
\qquad
3\text{ are required for chirality/full distinction}.
}
$$

The exact relation between the latter two depends on cycle size and marking.

For \(C_6\) with three colors, for example, the audit finds 450 chirality-selecting colorings but 444 fully distinguishing colorings.

So chirality and full identity are genuinely distinct operations.

## 10. Relation to A22

A22 said that a binary alphabet is the smallest nontrivial alphabet capable of adding information beyond an invariant relation.

The present audit refines that statement.

Binary information may be sufficient for some **specific symmetry-breaking tasks**, such as orienting one pair.

It need not be sufficient for:

- selecting a global cycle chirality;
- identifying every vertex;
- destroying every automorphism.

There is no contradiction.

The required informational budget is operation-relative.

## 11. Relation to the broader architecture

This is structurally similar to the repository's general obstruction-driven philosophy.

A representation should not carry more information than the declared operation requires.

For temporal/pregeometric work, asking for complete graph rigidity may be unnecessary if the physical operation only needs one local influence direction.

Conversely, proving one local edge is orientable does not justify a global temporal order.

## 12. Physical boundary

A mark that mathematically orients an edge is not automatically physical.

It must still have:

- an operational origin;
- an accepted gauge transformation law;
- a measurement/coupling map;
- a non-temporal semantics;
- and a reason its orientation should correspond to causal or temporal precedence.

The group-theoretic audit says only what the marked structure permits.

## 13. Current conclusion

The correct question is not:

> How many bits are needed to create time?

It is:

$$
\boxed{
\text{What symmetry must be broken for the specific physical operation under study, and what is the minimal physically justified information that breaks exactly that symmetry?}
}
$$

This is a much narrower and testable target.
