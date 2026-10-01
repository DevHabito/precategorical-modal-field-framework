# C1.3 — exact edge-toggle sensitivity of finite reachability

**Consolidation 1.0 canonical note**  
**Source claim:** MF-R011  
**Current status:** exact mathematical result; Lean end-to-end promotion gate still open  
**Novelty status:** priority of the specific finite value is not certified

This note is the short self-contained mathematical unit for C1.3. Historical
audits remain provenance, but the theorem below should be readable without the
A-number chronology.

## Definition

Let `D_n` be the set of all loopless directed graphs on the labeled vertex set
`[n]`. There are

\[
2^{n(n-1)}
\]

such graphs.

For a graph `G`, let `C(G)` denote its full reflexive-transitive reachability
relation. For a directed non-loop edge coordinate `e`, let `G triangle e` be the
graph obtained by toggling exactly that edge.

Define

\[
P_n
=
\frac{1}{n(n-1)2^{n(n-1)}}
\sum_{G\in D_n}\sum_e
\mathbf 1\!\left[C(G)\ne C(G\triangle e)\right].
\]

Thus `P_n` is the exact uniform probability that one directed-edge toggle
changes at least one reachability fact.

---

## Box 1 — Hypotheses

The theorem uses only the following assumptions.

1. Vertices are labeled.
2. Self-loops are excluded from the edge coordinates.
3. Every one of the `n(n-1)` directed non-loop edges is independently present
   or absent with probability `1/2`; equivalently, graphs are uniform over
   `D_n`.
4. The observable is the **full reflexive-transitive reachability relation**,
   not only the SCC partition and not the lossy minimum-representative code.
5. A toggle complements exactly one directed non-loop edge.

No physical interpretation, RZS assumption, continuum limit, asymptotic
assumption, or empirical model enters the claim.

---

## Structural theorem

Fix distinct labels `s,t` and the directed edge `e=(s,t)`. Consider a graph `H`
with `e` absent.

### Lemma — insertion criterion

\[
C(H+e)=C(H)
\quad\Longleftrightarrow\quad
s\leadsto_H t.
\]

### Proof

If `s` already reaches `t`, any path in `H+e` that uses the newly inserted
edge can replace that occurrence of `s -> t` by the pre-existing path from `s`
to `t`. Therefore insertion creates no new reachable pair.

Conversely, if `s` does not reach `t` in `H`, insertion makes `t` reachable
from `s` immediately. Hence the full reachability relation changes. `square`

The logical content of this lemma is isolated in Lean as a theorem for an
arbitrary binary relation on an arbitrary type. The Lean statement does not use
finiteness, graph masks, probabilities, or `n=5`.

### Toggle pairing

Pair every graph with `e` absent with the graph obtained by inserting `e`.
Every sensitive undirected pair in this pairing contributes two ordered toggle
states: insertion from the edge-absent side and deletion from the edge-present
side.

Moreover,

\[
s\not\leadsto_G t
\]

already implies that the direct edge `s -> t` is absent. Therefore, for a fixed
edge coordinate,

\[
\Pr(C(G)\ne C(G\triangle e))
=2\Pr(s\not\leadsto t).
\]

By permutation symmetry of the labeled uniform ensemble, every directed
non-loop edge coordinate has the same probability. Hence

\[
\boxed{P_n=2\Pr(s\not\leadsto t)}.
\]

If the classical fixed-pair random-digraph reachability probability is denoted
by

\[
\gamma_{n,1/2}=\Pr(s\leadsto t),
\]

then

\[
\boxed{P_n=2\bigl(1-\gamma_{n,1/2}\bigr)}.
\]

This identity explains the statistic structurally. It is not treated as a new
general random-digraph theory; fixed-pair reachability has prior literature.

---

## Exact n=5 computation

Let `a_j` be the number of loopless labeled digraphs on `j` vertices in which
all vertices are reachable from one distinguished root. Then

\[
a_1=1
\]

and

\[
a_k
=2^{k(k-1)}
-\sum_{j=1}^{k-1}
\binom{k-1}{j-1}a_j2^{(k-j)(k-1)}.
\]

The required exact values are

\[
a_1=1,\qquad a_2=2,\qquad a_3=32,\qquad a_4=2432.
\]

For five vertices, fix distinct `s,t`. If exactly `j` vertices are reachable
from `s` while `t` is not, choose the other `j-1` reachable labels from the
remaining three. The exact number of graphs with `s` not reaching `t` is

\[
\begin{aligned}
B_5
&=\sum_{j=1}^{4}
\binom{3}{j-1}a_j2^{(5-j)4}\\
&=65536+24576+24576+38912\\
&=153600.
\end{aligned}
\]

Since

\[
2^{20}=1048576,
\]

we obtain

\[
\Pr(s\not\leadsto t)
=\frac{153600}{1048576}
=\frac{75}{512}.
\]

Therefore

\[
\boxed{P_5=\frac{75}{256}}.
\]

The complete ordered graph-edge ensemble contains

\[
20\cdot2^{20}=20971520
\]

pairs. The exact sensitive-pair count is

\[
20971520\cdot\frac{75}{256}=6144000.
\]

Thus the unreduced integer statement is

\[
\boxed{6144000\text{ sensitive pairs out of }20971520}.
\]

No decimal approximation is used in the claim.

---

## Box 2 — Conclusion

Under exactly the finite uniform ensemble above,

\[
\boxed{
P_5
=\frac{6144000}{20971520}
=\frac{75}{256}
}.
\]

More generally, for any fixed distinct labels `s,t`,

\[
\boxed{
P_n=2\Pr(s\not\leadsto t)
=2\bigl(1-\gamma_{n,1/2}\bigr)
}.
\]

The second displayed identity is a structural reduction of the declared
statistic to ordinary fixed-pair reachability in the same random-digraph
ensemble.

---

## Independent n=6 checkpoint

A result should not be trusted merely because the same decomposition was coded
twice. For that reason the next value was frozen before an independent checker
was written.

The reachable-set derivation predicts

\[
B_6=82051072,
\]

\[
\Pr(s\not\leadsto t)=\frac{313}{4096},
\]

and

\[
\boxed{P_6=\frac{313}{2048}}.
\]

Equivalently,

\[
\boxed{4923064320\text{ sensitive pairs out of }32212254720}.
\]

A separately written checker then treated non-reachability as a union of
**directed-cut events** and used exact inclusion-exclusion over those cuts. It
does not use the `a_j` recurrence or import the frozen target values. It
reproduced exactly

\[
B_6=82051072
\]

and

\[
P_6=313/2048,
\]

as well as every historical value for `n=2,3,4,5`.

The pre-registration is preserved in
`MF_R011_FROZEN_N6_CHECKPOINT.md`; the independent calculation is recorded in
`MF_R011_CUT_IE_CHECK.md` and its executable checker in
`tools/mf_r011_cut_inclusion_exclusion.py`.

---

## Box 3 — Verification status

### Human-readable mathematics

**PASS for the displayed finite identities.**

The insertion criterion, toggle pairing, exact reachable-set count, and n=5
arithmetic are explicit in this note. The n=6 result was frozen and reproduced
by a different exact decomposition.

### Historical exhaustive computation

The repository preserves the original exact small-`n` enumeration. For `n=5`
it records

- `1048576` graphs;
- `20` directed non-loop edge coordinates;
- `20971520` ordered graph-edge pairs;
- `6144000` sensitive pairs;
- reduced fraction `75/256`.

This is provenance; it is not being silently treated as a fresh independent run
in the present consolidation session.

### Independent Lean path

The active formalization branch contains:

1. an independent bit-mask graph ensemble;
2. exact Lean `native_decide` counts through `n=5`;
3. a relation-based five-step Floyd-Warshall reference closure;
4. a symbolic proof that the reference closure is exactly
   `Relation.ReflTransGen` reachability;
5. an exhaustive all-`2^20`-graph audit connecting the optimized reachability
   code to that semantic reference;
6. a bijection between the 20 mask coordinates and the 20 actual directed
   non-loop edges;
7. a proof that toggling a coordinate flips exactly its edge and preserves all
   others;
8. an indicator bridge intended to prove that every enumerator summand is
   exactly the mathematical event that full reachability changes;
9. a generic edge-addition reachability theorem with no finite-graph or
   probability assumptions.

**Promotion status: NOT YET COMPLETE.**

The most recent clean formal gate must include both a full pinned-toolchain
`lake build` and successful module-sharded bundled `leanchecker` replay for all
declared modules. A theorem being present in source, or an earlier dependency
module building successfully, is not enough to mark C1.3 as end-to-end
kernel-passed.

The generic edge-addition theorem formalizes the insertion criterion. It does
not, by itself, kernel-check the finite probability pairing or label-symmetry
argument. Those boundaries must remain explicit.

### Independent cut computation

**PASS as an exact computational cross-check through n=6.**

This checker uses integer bit masks and exact rational reduction only. It does
not replace the Lean semantic gate.

---

## Literature position

The general fixed-pair reachability problem is prior art. Uno and Ibaraki
(1998), *Reachability Problems of Random Digraphs*, study the independent-edge
random-digraph model, define the fixed-pair reachability probability, and give
an exact computation method.

Reachability-based edge influence also has direct prior work, including Qin,
Sheng, Parkinson, and Falkner (DASFAA 2017), *Edge Influence Computation in
Dynamic Graphs*.

Therefore C1.3 must **not** be presented as the discovery of random-digraph
reachability, exact reachability computation, or edge influence as a general
concept.

No inspected source so far settles priority of the particular reduced value
`75/256`. Failure to locate that fraction is not a proof of novelty. The safe
status is: **priority of the specific value is not certified**.

---

## Box 4 — Nonclaims

C1.3 does **not** establish any of the following:

- that `75/256` is a universal constant;
- that the specific fraction is globally novel;
- that the specific fraction was definitely known before;
- a new general theory of random-digraph reachability;
- a new general theory of edge influence;
- an asymptotic theorem for `P_n`;
- monotonicity of `P_n`;
- a statement about an arbitrary non-uniform graph distribution;
- a statement about undirected graphs;
- physical relevance of the finite ensemble;
- a bridge from this graph statistic to RZS, the modal field, spacetime,
  quantum gravity, or nature.

Any such statement requires separate hypotheses and separate evidence.

---

## Promotion rule for this note

Only the text inside **Box 3 — Verification status** should change when the
formal gate changes. The exact integers and fractions must not be edited to
match a failing checker. If an independent route disagrees, both results are to
be preserved until the discrepancy is resolved.
