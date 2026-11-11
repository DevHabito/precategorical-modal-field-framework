# Pre-time-orientability: deriving an orientation doublet without choosing a polarity

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact finite group-action criterion inspired by Lorentzian time orientability  
**Novelty status:** Lorentzian time orientability is classical; the finite "orientation doublet" criterion is a project-specific organizational device, not yet a theorem of physical emergence

## 1. Why the polarity target may have been too strong

The previous frontier asked for a physical reason to choose one invariant acyclic orientation

$$
O
$$

rather than its global reverse

$$
O^{\mathrm{op}}.
$$

Lorentzian geometry suggests that this may ask too much from the underlying unoriented structure.

A connected time-orientable Lorentzian manifold has two time orientations.

Choosing one component of the timelike cone bundle continuously gives a time orientation; reversing the choice gives the other.

The Lorentzian metric can therefore support **time orientability** before one labels one orientation future and the other past.

This motivates a finite analogue.

## 2. Orientation doublet

Let \((G,\ell)\) be a finite marked undirected structure.

Let

$$
H=\operatorname{Aut}(G,\ell).
$$

Let \(\mathcal O_H\) be the set of acyclic orientations of \(G\) that are invariant under every automorphism in \(H\).

Global reversal acts on this set:

$$
O\mapsto O^{\mathrm{op}}.
$$

Define the marked structure to have a **unique orientation doublet** when

$$
\boxed{
\mathcal O_H=
\{O,O^{\mathrm{op}}\}
}
$$

for one acyclic orientation \(O\).

The unordered pair

$$
\boxed{
[O]_{\pm}:=\{O,O^{\mathrm{op}}\}
}
$$

is then determined by the marked structure even though neither member is selected as the positive polarity.

## 3. Why the doublet is a stronger object than orientability

Plain orientability asks only whether

$$
\mathcal O_H\neq\varnothing.
$$

A unique orientation doublet asks for substantially more:

- an invariant acyclic orientation exists;
- every other invariant acyclic orientation is its global reverse;
- no further orientation ambiguity remains.

Thus the structure determines the **axis of temporal orientation** without choosing a sign.

## 4. Why the doublet is weaker than polarity

The doublet does not distinguish

$$
O
$$

from

$$
O^{\mathrm{op}}.
$$

Therefore it does not define:

- absolute future versus past;
- a preferred T direction;
- a thermodynamic arrow;
- an initial boundary;
- duration.

It provides only a globally consistent two-sided orientation structure.

## 5. Lorentzian benchmark

For a connected time-orientable Lorentzian manifold \((M,g)\), a continuous timelike vector field \(T\) determines one time orientation.

The field \(-T\) determines the opposite one.

The two belong to distinct equivalence classes of global timelike vector fields, and a connected time-orientable manifold has exactly two time orientations.

This gives the conceptual pattern

$$
\boxed{
\text{time-orientable structure}
\quad\Rightarrow\quad
\{\text{orientation},\text{reverse orientation}\}.
}
$$

The finite doublet criterion is only an analogy to this pattern.

It is not a discretization of Lorentzian geometry.

## 6. Exact cycle enumeration

The repository exhaustively enumerates all vertex colorings of

$$
C_n,\qquad n=3,\ldots,8
$$

for alphabets

$$
k=1,2,3.
$$

For each coloring it computes every acyclic edge orientation, retains those invariant under the mark-preserving automorphism group, and asks whether exactly two survive and are global reverses.

The exact counts are:

| \(n\) | \(k=1\) | \(k=2\) | \(k=3\) |
|---:|---:|---:|---:|
|3|0|0|0|
|4|0|2|6|
|5|0|0|0|
|6|0|2|6|
|7|0|0|0|
|8|0|2|6|

For the graphA skeleton \(C_4\), exactly

$$
\boxed{
2/16
}
$$

binary colorings produce a unique orientation doublet.

They are the two complementary alternating colorings

$$
(0,1,0,1)
$$

and

$$
(1,0,1,0).
$$

## 7. The C4 doublet

For the alternating coloring

$$
\ell=(0,1,0,1),
$$

the only invariant acyclic orientation pair is

$$
1\to0,\quad
1\to2,\quad
3\to2,\quad
3\to0
$$

and its global reverse.

Equivalently, one orientation sends every color-1 vertex toward adjacent color-0 vertices.

The reverse sends every color-0 vertex toward adjacent color-1 vertices.

The marked square therefore determines a bipartite orientation **axis** while leaving its polarity unresolved.

## 8. Important interpretation

The binary mark has not created one preferred future.

It has done something more precise:

$$
\boxed{
\text{it reduced a large orientation space to a single reversal pair}.
}
$$

This is structurally analogous to obtaining two consistent time-cone choices before selecting one as future.

## 9. Complementary coloring does not create a new doublet

The complementary marking

$$
(1,0,1,0)
$$

produces the same unordered orientation pair.

Thus the doublet itself does not depend on which binary symbol is called 0 or 1.

This is important.

The orientation axis is more invariant than the label polarity.

## 10. Why odd cycles fail in the tested range

For

$$
C_3,\ C_5,\ C_7,
$$

none of the tested 1-, 2-, or 3-symbol colorings yields a unique acyclic orientation doublet.

This is a finite combinatorial result for the audited coloring class.

It should not be generalized beyond that scope without proof.

The result nevertheless shows that pre-orientability is structure dependent.

## 11. Even cycles

For

$$
C_4,\ C_6,\ C_8,
$$

the audit finds two binary colorings with a unique reversal pair.

These are the alternating two-colorings associated with the bipartition of the even cycle.

With three symbols, six colorings produce a unique doublet for each audited even cycle.

Again, this is exact finite enumeration, not a new general theorem about all marked graphs.

## 12. Relation to stochastic sector selection

The sector-selection audit showed that a symmetric theory can realize either \(+\) or \(-\) while assigning equal probability to both.

The orientation doublet supplies a natural structural target for such a mechanism.

First derive

$$
\{O,O^{\mathrm{op}}\}.
$$

Then a stochastic or boundary process may select one member.

This gives the hierarchy

$$
\boxed{
\text{pre-time-orientability}
\to
\text{orientation doublet}
\to
\text{sector/polarity selection}.
}
$$

The ensemble may remain invariant under exchange of the two members.

## 13. Relation to the symmetry no-go

The orientation doublet does not violate the automorphism no-go.

The no-go forbids a canonical **single asymmetric orientation** when a reversal symmetry remains.

The unordered pair

$$
\{O,O^{\mathrm{op}}\}
$$

is itself reversal invariant.

Therefore a symmetric primitive can potentially determine the pair without determining one sign.

This is a key logical escape from the false dilemma:

> either derive a unique future or derive nothing.

A symmetric structure may determine a two-fold orientation class.

## 14. Relation to physical T violation

If the effective physical laws later contain T-violating structure, the two members of the doublet need not remain physically equivalent.

Law-level polarity can then select or distinguish one orientation.

But that is a **later** physical input.

The structural doublet can be discussed independently.

## 15. Relation to boundary-state arrows

A special boundary condition can likewise select one member of the doublet as the realized macroscopic arrow.

Again, this does not mean the boundary condition created the orientability structure.

It selects within an already available two-fold class.

## 16. Revised target for the pregeometric programme

The first pregeometric target should therefore be weakened from

> derive a unique future direction

to

> derive a globally consistent reversal pair of candidate orientations from non-temporal structure.

Formally:

$$
\boxed{
\text{primitive structure}
\longrightarrow
[O]_\pm=\{O,O^{\mathrm{op}}\}.
}
$$

Only after this succeeds should the project ask whether physics selects one member.

## 17. Necessary tests

A candidate pre-time-orientation class should satisfy:

1. label/isomorphism invariance;
2. gauge invariance;
3. exact reversal pairing;
4. global consistency;
5. acyclicity or another declared orderability condition;
6. uniqueness modulo global reversal;
7. stability under irrelevant representation refinement;
8. a non-temporal construction rule.

The finite cycle audit checks only the first six in a narrow combinatorial setting.

## 18. What remains missing

Even a successful orientation doublet does not provide:

- metric duration;
- local clock rates;
- causal speed limits;
- Lorentzian signature;
- spacetime dimension;
- physical light cones;
- empirical calibration.

It is an **ordinal orientation precursor** only.

## 19. Current verdict

**Can a symmetric structure canonically determine one polarity?**  
Not when the reversal symmetry remains.

**Can it canonically determine an unordered pair of opposite orientations?**  
YES, in the audited marked-cycle examples.

**Does this resemble Lorentzian time orientability?**  
Structurally, yes.

**Is it already Lorentzian spacetime or physical time?**  
NO.

**Does it provide a better next pregeometric target than absolute polarity?**  
YES.

## 20. New frontier

The next question becomes:

$$
\boxed{
\text{Can the repository's non-temporal relational structures
derive a unique orientation class modulo global reversal?}
}
$$

If yes, the polarity problem can be postponed to sector/boundary/law selection.

If no, even time-orientability has not emerged.
