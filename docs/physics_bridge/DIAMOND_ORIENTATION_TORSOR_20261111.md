# Diamond graph orientation torsor — first intrinsic doublet with nontrivial order depth

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact finite structural result + elementary proof  
**Novelty status:** comparability graphs, transitive orientations, automorphism actions, and UPO theory are classical. The project-specific Aut-stable-duality filter has no certified novelty claim.

## 1. Question

The bipartite C4 construction produced an intrinsic orientation doublet but no directed path of length two.

The next finite question was:

> Can an unmarked non-temporal finite graph canonically determine one acyclic orientation class modulo global reversal while also supporting a directed chain of at least two edges?

The answer is yes.

The smallest example found in exhaustive search is the four-vertex diamond graph

$$
K_4-e.
$$

## 2. Diamond graph

Let the vertices be

$$
a,b,x,y.
$$

Take edges

$$
\{a,b\},
\{a,x\},
\{a,y\},
\{b,x\},
\{b,y\},
$$

with the single missing edge

$$
\{x,y\}.
$$

Thus:

$$
\deg(a)=\deg(b)=3,
$$

and

$$
\deg(x)=\deg(y)=2.
$$

The degree classes are intrinsic.

## 3. Automorphism structure

The graph admits:

- a swap

$$
s:x\leftrightarrow y
$$

fixing \(a,b\);

- a swap

$$
r:a\leftrightarrow b
$$

fixing \(x,y\);

- their composition.

These generate the four-element automorphism group.

The two degree-3 vertices form one orbit.

The two degree-2 vertices form another.

## 4. Candidate orientation

Choose temporarily one degree-3 vertex as \(a\) and the other as \(b\).

Define

$$
O:
\qquad
a\to b,
\quad
a\to x,
\quad
a\to y,
\quad
x\to b,
\quad
y\to b.
$$

This orientation is acyclic.

It contains the two length-two chains

$$
a\to x\to b,
$$

and

$$
a\to y\to b.
$$

Therefore its directed depth is at least 2.

## 5. Low-degree swap preserves O

The automorphism

$$
s:x\leftrightarrow y
$$

fixes the edge

$$
\{a,b\}
$$

pointwise.

If \(s\) globally reversed \(O\), it would have to reverse the direction of the fixed edge \(a\to b\), which is impossible because the endpoints are unchanged.

Therefore

$$
s(O)=O.
$$

Consequently the two low-degree branches must carry the same orientation pattern.

## 6. High-degree swap reverses O

The automorphism

$$
r:a\leftrightarrow b
$$

swaps the endpoints of the edge

$$
\{a,b\}.
$$

It cannot preserve an orientation of that edge.

For the unordered orientation class

$$
[O]_\pm
=
\{O,O^{\mathrm{op}}\}
$$

to be invariant, \(r\) must send

$$
O\mapsto O^{\mathrm{op}}.
$$

This links the orientations on the four side edges.

## 7. Acyclicity forces the depth-two pattern

Assume without loss of global reversal that

$$
a\to b.
$$

Consider the edge \(a-x\).

### Case 1

Suppose

$$
a\to x.
$$

Because \(r\) maps \(O\) to \(O^{\mathrm{op}}\), the corresponding edge at \(b\) must be

$$
x\to b.
$$

Thus

$$
a\to x\to b.
$$

The same holds for \(y\).

### Case 2

Suppose instead

$$
x\to a.
$$

The reversal constraint forces

$$
b\to x.
$$

Then

$$
x\to a\to b\to x
$$

is a directed cycle.

Acyclicity rejects this case.

Therefore the only acyclic possibility with \(a\to b\) is

$$
a\to x,\quad
a\to y,\quad
x\to b,\quad
y\to b.
$$

Global reversal supplies the only other member.

Hence:

$$
\boxed{
\mathcal O_{\rm canonical}(K_4-e)
=
\{O,O^{\mathrm{op}}\}.
}
$$

## 8. Intrinsic nature of the doublet

The construction did not use:

- vertex numerical labels;
- an external binary mark;
- a timestamp;
- a chosen topological ordering.

It used only:

- degree-orbit structure;
- graph automorphisms;
- acyclicity.

Choosing which degree-3 pole is called \(a\) merely chooses one member of the reversal pair.

Therefore the **pair** is intrinsic.

## 9. Exhaustive search definition

For each connected labeled simple graph \(G\), the audit enumerates every acyclic orientation \(O\).

An orientation class

$$
[O]_\pm
=
\{O,O^{\mathrm{op}}\}
$$

is called automorphism-canonical in the audit when every

$$
g\in\operatorname{Aut}(G)
$$

satisfies

$$
g(O)\in\{O,O^{\mathrm{op}}\}.
$$

The graph passes orientation-class uniqueness when exactly one such reversal class exists.

This is a finite project criterion.

It is not standard terminology.

## 10. Exhaustive results through n=5

Every connected labeled simple graph was audited for

$$
n=2,3,4,5.
$$

Results:

| n | connected labeled graphs | unique canonical reversal class | class with directed depth >= 2 |
|---:|---:|---:|---:|
|2|1|1|0|
|3|4|0|0|
|4|38|13|6|
|5|728|30|25|

For \(n=4\), all six labeled deep cases are copies of

$$
K_4-e,
$$

corresponding to the six possible choices of the missing edge.

Therefore the diamond graph is the first unlabeled witness in this search.

## 11. Why P4 does not pass uniqueness

A four-vertex path has a natural end-to-end orientation and its reverse.

However, it also admits a second automorphism-compatible reversal class in which the two ends flow toward or away from the center.

Thus the graph does not uniquely select the linear orientation class.

This illustrates why “looks like a timeline” is not enough.

The automorphism audit must be performed.

## 12. Improvement over C4

The C4 bipartite doublet gave:

$$
\text{orientation axis}
+
\text{depth }1.
$$

The diamond gives:

$$
\boxed{
\text{intrinsic orientation axis}
+
\text{depth }2.
}
$$

This is the first finite witness in the current programme with nontrivial compositional order depth.

## 13. Still not physical time

The diamond can have many non-temporal interpretations:

- a source/product dependency network;
- a two-route workflow;
- a dominance hierarchy;
- a reliability network;
- a static poset incidence pattern.

Nothing in the abstract graph says “time.”

Therefore the physical-semantic problem remains.

## 14. No duration

The two-edge chain

$$
a\prec x\prec b
$$

provides ordinal depth.

It does not imply equal temporal intervals or any metric duration.

Even if one assigned chain length 2, refinement could change that number.

Duration remains a later calibration problem.

## 15. New structural lesson

The graphA C4 showed that one can derive an orientation torsor from bipartiteness.

The diamond shows that one can also derive **nontrivial ordinal depth** without a preferred polarity.

Therefore there is no purely combinatorial obstruction to the first two stages:

$$
\boxed{
\text{orientation class}
\to
\text{nontrivial order depth}.
}
$$

The obstruction has moved again.

## 16. Revised frontier

The next question is no longer whether such finite structures exist.

They do.

The next question is:

$$
\boxed{
\text{what physical, non-temporal criterion distinguishes an intrinsic
orientation-depth structure that should be interpreted causally
from one that is merely a static dependency order?}
}
$$

That is now the bridge to physics.


## 17. Comparability/UPO correction

A dedicated literature audit places the diamond result inside classical comparability-graph theory.

The displayed depth-two orientation is transitive, so the diamond is a comparability graph.

However, the diamond has

$$
\boxed{
6
}
$$

transitive orientations, forming three reversal pairs.

Therefore

$$
\boxed{
K_4-e\text{ is not UPO}.
}
$$

UPO would require exactly two transitive orientations, one the reverse of the other.

What is special under the project's filter is narrower:

- \(\operatorname{Aut}(K_4-e)\) acts on all six transitive orientations;
- among the three reversal pairs, exactly one pair is preserved as a set by every automorphism;
- that pair has directed depth two.

Thus the canonical project statement is now:

> the diamond is the smallest witness found in the audited range with one Aut-stable transitive-orientation duality class of nontrivial depth.

This should not be described as discovery of unique partial orderability.

Aigner–Prins UPO theory, Möhring's later work, Golumbic's comparability-graph treatment, and the established automorphism action on transitive orientations are prior art.
