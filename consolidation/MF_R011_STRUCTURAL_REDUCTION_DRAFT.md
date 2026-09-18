# MF-R011 structural reduction — draft, not yet promoted

**Status:** consolidation working note.  
**Promotion status:** NOT CANONICAL; formal and independent verification still required.  
**Novelty status:** NOT CERTIFIED. The auxiliary initially-connected digraph counts are classical, and exact reachability in random digraphs has prior literature.

## 1. Ensemble

Let \(\mathcal D_n\) be the set of loopless labeled digraphs on \([n]\), with

\[
m=n(n-1), \qquad |\mathcal D_n|=2^m.
\]

For a graph \(G\), let \(C(G)\) denote its full reflexive reachability preorder.
For a directed non-loop edge \(e=(a,b)\), let \(G\triangle e\) toggle that edge.

The MF-R011 statistic is

\[
P_n
=
\frac{1}{m2^m}
\sum_{G\in\mathcal D_n}\sum_e
\mathbf 1[C(G)\neq C(G\triangle e)].
\]

## 2. Fixed-edge toggle criterion

Fix \(e=(a,b)\).  If \(H\) does not contain \(e\), then

\[
C(H+e)\neq C(H)
\quad\Longleftrightarrow\quad
a\not\leadsto_H b.
\]

### Proof

If \(a\not\leadsto_H b\), adding \(a\to b\) creates at least the new reachable
pair \((a,b)\), so the preorder changes.

Conversely, assume \(a\leadsto_H b\). Any path in \(H+e\) that does not use
the new edge is already a path in \(H\). If a path uses the new edge \(a\to b\),
replace that occurrence by an existing path from \(a\) to \(b\) in \(H\).
The resulting walk lies entirely in \(H\). Hence the full reachability relation
does not change.

This is the mathematical content formalized abstractly in
`EdgeToggleSemantics.lean`.

## 3. Hypercube pairing

For fixed \(e\), pair every graph without \(e\) with the graph obtained by
adding \(e\). Both orientations of the toggle have the same
changed/unchanged status.

Let

\[
A_n
=
\#\{G\in\mathcal D_n : a\not\leadsto_G b\}.
\]

The condition \(a\not\leadsto_G b\) already forces \(a\to b\notin E(G)\).
Therefore the number of changed ordered graph-toggle pairs for one fixed edge is

\[
2A_n.
\]

By relabeling symmetry, \(A_n\) is independent of the selected ordered pair
\((a,b)\). Summing over the \(m=n(n-1)\) directed non-loop edges gives

\[
\#\{(G,e):C(G)\neq C(G\triangle e)\}=2mA_n,
\]

and hence the structural identity

\[
\boxed{P_n=\frac{2A_n}{2^{n(n-1)}}}
\]

or, probabilistically for any fixed distinct labels \(a,b\),

\[
\boxed{P_n=2\,\Pr_G[a\not\leadsto_G b]}.
\]

Thus MF-R011 is reducible to the classical two-vertex reachability probability
in the uniform random loopless digraph.

## 4. Reachable-set decomposition

Let \(I_k\) denote the number of loopless labeled digraphs on \(k\) vertices
in which every vertex is reachable from one fixed distinguished root.
These are classically called **initially connected digraphs**.

Fix distinct \(a,b\), and let \(S\) be the set of vertices reachable from
\(a\). Under \(a\not\leadsto b\),

\[
a\in S,\qquad b\notin S.
\]

If \(|S|=k\), then:

1. choose the other \(k-1\) vertices of \(S\) from the \(n-2\) labels other
   than \(a,b\): \(\binom{n-2}{k-1}\) choices;
2. the induced graph on \(S\) must be initially connected from \(a\):
   \(I_k\) choices;
3. every directed edge from \(S\) to its complement must be absent;
4. edges from the complement into \(S\), and edges internal to the complement,
   are arbitrary.

The number of arbitrary edges in item 4 is

\[
k(n-k)+(n-k)(n-k-1)=(n-k)(n-1).
\]

Therefore

\[
\boxed{
A_n
=
\sum_{k=1}^{n-1}
\binom{n-2}{k-1}
I_k\,
2^{(n-k)(n-1)}
}
\]

and hence

\[
\boxed{
P_n
=
\sum_{k=1}^{n-1}
\binom{n-2}{k-1}
I_k\,
2^{1-k(n-1)}
}.
\]

This is a structural reduction, not an independent novelty claim about the
classical sequence \(I_k\).

## 5. Classical recurrence for the auxiliary counts

Partition all \(n\)-vertex digraphs by the full set reachable from the fixed
root. The same decomposition gives

\[
2^{n(n-1)}
=
\sum_{k=1}^{n}
\binom{n-1}{k-1}
I_k\,
2^{(n-k)(n-1)}.
\]

Thus, with \(I_1=1\),

\[
\boxed{
I_n
=
2^{n(n-1)}
-
\sum_{k=1}^{n-1}
\binom{n-1}{k-1}
I_k\,
2^{(n-k)(n-1)}
}.
\]

The first values are

\[
I_1,\ldots,I_7
=
1,2,32,2432,745472,875036672,3913822502912.
\]

These match the classical initially-connected-digraph enumeration reported in
the literature; they must not be presented as project-original values.

## 6. Recovery of MF-R011 and further arithmetic consequences

The structural formulas give

| \(n\) | \(A_n\) | \(P_n\) |
|---:|---:|---:|
| 2 | 2 | \(1\) |
| 3 | 24 | \(3/4\) |
| 4 | 1024 | \(1/2\) |
| 5 | 153600 | \(75/256\) |
| 6 | 82051072 | \(313/2048\) |
| 7 | 162470559744 | \(2421/32768\) |

The \(n=2,3,4,5\) row reproduces the existing independent exact enumeration.
The \(n\ge6\) rows are **draft consequences of the structural reduction** and
must not be promoted until the reduction receives an independent implementation
or formal proof.

For \(n=5\),

\[
P_5
=
\frac{2\cdot153600}{2^{20}}
=
\frac{153600}{2^{19}}
=
\frac{75}{256}.
\]

Equivalently, the historical ordered graph-edge changed-pair count is

\[
20\cdot2\cdot153600=6\,144\,000.
\]

## 7. Prior-literature boundary

Two prior-work facts materially narrow novelty language:

1. **Initially connected digraphs are classical.** Liskovets studied their
   enumeration in the late 1960s/1970s, and later work tabulates the same
   sequence above.
2. **Exact reachability probabilities in random digraphs are prior art.**
   Uno and Ibaraki (1998), *Reachability Problems of Random Digraphs*, explicitly
   study and compute the exact probability that one fixed vertex is reachable
   from another in the independent-edge random digraph.

Accordingly, the safe present claim is:

> MF-R011's uniform edge-toggle sensitivity reduces to twice the
> fixed-pair non-reachability probability. Combining that reduction with a
> reachable-set decomposition reproduces the exact values
> \(P_2=1\), \(P_3=3/4\), \(P_4=1/2\), and \(P_5=75/256\).

Do **not** currently claim that the general formula, the reduction, or any
resulting sequence is novel. A claim-specific literature comparison with the
exact formulas in prior random-digraph reachability work is still required.

## 8. Formalization obligations before promotion

The current Lean branch must still close, end to end:

1. semantic correctness of the finite separator checker;
2. equivalence between the optimized cut checker and semantic
   non-reachability, or an independent semantic count;
3. fixed-edge pairing under toggle;
4. label symmetry or direct full-ensemble counting;
5. exact five-vertex changed-pair count and reduction to \(75/256\);
6. clean `lake build` and bundled `leanchecker` replay.

Only after those gates pass should C1.3 be promoted from
**EXACT FINITE RESULT** to a formal-kernel status.
