# Pregeometric Direction V2 — orientation class before polarity

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** canonical synthesis replacing the V1 polarity-first target  
**Physical status:** no derivation of physical time or Lorentzian spacetime  
**Core correction:** derive orientation modulo global reversal before asking for a preferred polarity

## 1. Why V2 is needed

Direction V1 isolated the chain

$$
\text{symmetry breaking}
\to
\text{orientability}
\to
\text{polarity}
\to
\text{physical order}
\to
\text{duration}.
$$

Further analysis shows that demanding a preferred polarity immediately after orientability is unnecessarily strong.

Lorentzian geometry supplies the correct comparison.

A connected time-orientable Lorentzian manifold admits exactly two global time orientations.

The metric/cone structure can therefore support **time orientability** without canonically naming one member “future.”

Therefore the first pregeometric target should be an orientation class modulo global reversal.

## 2. New canonical chain

The direction programme is now organized as

$$
\boxed{
\text{primitive non-temporal structure}
\to
\text{orderability}
\to
\text{orientation class }[O]_\pm
\to
\text{polarity/sector selection}
\to
\text{physical causal order}
\to
\text{duration}.
}
$$

Here

$$
[O]_\pm
=
\{O,O^{\mathrm{op}}\}.
$$

The unordered pair is the primary orientation object.

## 3. The orientation torsor

If the admissible orientation set is exactly

$$
\mathcal T=
\{O,O^{\mathrm{op}}\},
$$

and global reversal swaps the two members, then \(\mathcal T\) carries a free transitive action of

$$
\mathbb Z_2.
$$

It is therefore naturally a two-element orientation torsor.

This language avoids choosing a preferred basepoint.

A polarity choice is the later selection of one element of the torsor.

## 4. Lorentzian analogy

At each point of a Lorentzian manifold, the timelike vectors have two connected components.

Time orientability is the global consistency condition permitting one component to be selected continuously over the manifold.

For connected time-orientable Lorentzian manifolds there are two global time orientations, represented by a timelike field \(T\) and its reverse \(-T\).

The project's finite structure

$$
\{O,O^{\mathrm{op}}\}
$$

is analogous only at the level of a global two-fold orientation choice.

No claim is made that:

- graph edges are tangent vectors;
- acyclic orientations are light cones;
- graph automorphisms are Lorentz transformations;
- the finite doublet approximates a Lorentzian metric.

## 5. Exact C4 result

For the graphA undirected cycle skeleton \(C_4\), the exhaustive coloring/orientation audit found:

- 16 binary vertex colorings;
- 10 admit at least one automorphism-invariant acyclic orientation;
- exactly 2 admit a **unique orientation class modulo global reversal**.

Those two colorings are

$$
(0,1,0,1)
$$

and

$$
(1,0,1,0).
$$

Both determine the same unordered orientation pair.

Thus the binary symbol names themselves are irrelevant to the doublet.

## 6. Exact even-cycle pattern in the audited range

For \(C_n\), \(n=3,\ldots,8\), with binary marks:

- \(C_4\): 2 unique doublet colorings;
- \(C_6\): 2;
- \(C_8\): 2;
- \(C_3,C_5,C_7\): 0.

The successful binary colorings on the audited even cycles are the two complementary alternating bipartitions.

This is an exact finite observation.

It is not yet promoted to a general theorem for all even cycles in the repository.

## 7. Why this is not yet emergence from graphA

The orientation doublet requires a mark.

For graphA's unmarked skeleton, the four cycle vertices form one automorphism orbit:

$$
\{0,2,3,4\}.
$$

Any deterministic isomorphism-invariant scalar mark derived solely from the skeleton must be constant on this orbit.

Therefore it cannot generate the alternating mark.

The exact invariant-mark audit found only four fully automorphism-invariant binary colorings on all five graphA vertices, and none alternates on the cycle.

Hence:

$$
\boxed{
\text{graphA skeleton alone}
\not\Rightarrow
\text{the audited orientation doublet}.
}
$$

An independently justified mark is still required.

## 8. Lean orbit obstruction

The generic kernel now formalizes:

if a symmetry map sends

$$
a\mapsto b
$$

and a mark is invariant under that map, then

$$
\boxed{
m(a)=m(b).
}
$$

This is the formal reason a canonical invariant scalar cannot split one automorphism orbit.

The module is PhysicalBridgeInvariantMarkOrbit.lean.

Its CI status must be read from the current workflow result before promotion.

## 9. Lean reversal kernel

The orientation-doublet module formalizes that global reversal:

- is an involution;
- preserves irreflexivity;
- preserves asymmetry;
- preserves transitivity.

Therefore reversing a strict-order candidate gives another strict-order candidate.

The module is PhysicalBridgeOrientationDoublet.lean.

This formalizes the logical kernel behind the two-fold orientation class.

## 10. Symmetric sector selection

The minimal exact stochastic model has states

$$
0,+,-
$$

and transition kernel

$$
K=
\begin{pmatrix}
0&1/2&1/2\\
0&1&0\\
0&0&1
\end{pmatrix}.
$$

Starting from the symmetric neutral state gives

$$
\pi_n=
\left(
0,\frac12,\frac12
\right)
$$

for every \(n\ge1\).

The reversal-odd ensemble order parameter

$$
M=\pi_+-\pi_-
$$

remains exactly zero.

Yet each realized trajectory enters either \(+\) or \(-\) and remains there.

Therefore:

$$
\boxed{
\text{realization polarity can emerge without ensemble sign preference}.
}
$$

This is classified as symmetric stochastic sector selection, not a new theorem about thermodynamic SSB.

## 11. Why sector selection fits the orientation torsor

Suppose the pregeometric structure first determines

$$
[O]_\pm
=
\{O,O^{\mathrm{op}}\}.
$$

A symmetric sector-selection law could then select one member in a realized universe while assigning equal measure to both over the ensemble.

This would satisfy the symmetry no-go because the theory would not canonically prefer one member.

It would produce:

- a structural orientation axis;
- a realized polarity;
- no absolute ensemble sign.

This is logically coherent.

It is not yet a physical theory.

## 12. Canonical versus realized polarity

The project must now keep two questions separate.

### Canonical polarity

Does the law/primitive structure prefer

$$
O
$$

over

$$
O^{\mathrm{op}}?
$$

This requires asymmetric information somewhere.

### Realized polarity

Can one physical realization occupy one member of the reversal pair while the full law remains symmetric?

Yes mathematically, through sector selection.

The observed universe being one realization makes the second question physically relevant.

But stability and interpretation remain open.

## 13. Existing physical polarity sources

Established physics shows several places where later sign selection can live:

- law-level T violation;
- asymmetric boundary/preparation conditions;
- intervention versus response typing;
- external fields/holonomies;
- asymmetric sectors/solutions.

These should be treated as **post-orientability polarity mechanisms**, unless a deeper theory derives them.

## 14. Non-temporal semantics for R

Resource convertibility and constructor-theoretic tasks show that a directed relation can have physically legitimate non-temporal semantics.

Examples:

$$
x\succeq y
$$

meaning resource \(x\) can be converted to \(y\) by allowed operations;

or

$$
x\to y
$$

as a possible constructor-theoretic task.

These pass the semantic anti-circularity gate.

But their source/target polarity is part of the operational task structure.

They do not solve the origin of the orientation torsor from an untyped symmetric substrate.

## 15. Current architecture boundary remains

The provisional tuple

$$
(R,q,\mu,K,\pi)
$$

does not currently derive time from a timeless substrate.

- directed \(R\) needs non-temporal semantics;
- q can add marks/asymmetry but its physical origin remains open;
- \(\mu\) provides multiplicity;
- dynamical \(K\) already uses transition semantics;
- \(\pi\) can select an effective arrow but not succession itself.

V2 does not change this boundary.

It changes the next target.

## 16. New primary mathematical target

The immediate finite target is:

> Given a non-temporal marked relational structure, determine whether the admissible order structures form exactly one reversal pair.

Formally seek conditions for

$$
\boxed{
\mathcal O(\mathfrak P)
/
(O\sim O^{\mathrm{op}})
}
$$

to contain exactly one element.

This is an **orientation-class uniqueness** problem.

## 17. New primary physical target

The physical question is:

> What independently measurable non-temporal information supplies the marks or operational structure required to make the orientation class unique modulo reversal?

This is stricter than inventing a coloring.

The mark must be:

- operationally defined;
- label invariant;
- gauge consistent;
- not reconstructed from the orientation it is supposed to explain;
- physically justified before the temporal interpretation.

## 18. Secondary physical target: polarity selection

Only after the orientation torsor exists should the project ask:

> What selects one member in a realized physical sector?

Candidate classes include:

- stochastic sector selection;
- boundary conditions;
- T-asymmetric dynamics;
- operational source/target types;
- environment-induced stable sectors.

Each carries separate empirical and theoretical obligations.

## 19. Stability requirement

A realized orientation is physically useful only if it is sufficiently stable for records, causal inference, and internal observers.

A sector that flips rapidly between

$$
O
$$

and

$$
O^{\mathrm{op}}
$$

does not provide a persistent macroscopic arrow.

Thus a future candidate must quantify:

- switching rate;
- barrier or decoherence scale;
- finite-size restoration time;
- robustness to perturbations;
- scaling toward a macroscopic regime.

This is where SSB/decoherence literature becomes relevant.

## 20. Local versus global orientability

Lorentzian geometry also warns that local cone choices need not glue into one global time orientation.

The finite programme therefore needs a future analogue of a gluing obstruction:

- local orientation candidates may exist;
- pairwise consistency may hold;
- global orientation may still fail.

The current marked-cycle audits test globally on small graphs and therefore do not yet expose a separate local-to-global obstruction theory.

This is a new mathematical direction worth studying.

## 21. Duration remains separate

Even a perfect orientation torsor plus stable polarity supplies only ordinal direction.

Duration still requires additional quantitative structure:

- a relational clock;
- a metric/proper-time reconstruction;
- scaling under refinement;
- calibration against physical observables.

No result in V2 changes that separation.

## 22. Promotion ladder

A pregeometric time claim should now pass:

1. non-temporal primitive semantics;
2. label/isomorphism invariance;
3. gauge audit;
4. local orderability;
5. global orientation-class existence;
6. uniqueness modulo reversal;
7. independently justified marks/structure;
8. realized polarity selection if physically required;
9. stability/internal observability;
10. causal-structure recovery;
11. duration calibration;
12. empirical or rigorous physical discrimination.

## 23. Current strongest conclusion

The latest work supports a more precise statement than V1:

$$
\boxed{
\text{a symmetric theory need not derive an absolute future to derive an orientation structure}.
}
$$

A two-fold orientation class is compatible with reversal symmetry.

One realized sector can later select one member without making the symmetric ensemble prefer a sign.

## 24. Current frontier

The immediate open problem is now:

$$
\boxed{
\text{find a physically justified non-temporal mark/structure
that makes the orientation class unique modulo reversal}.
}
$$

For the existing C1 graphA witness, no such mark has yet been identified.

That negative result is retained.
