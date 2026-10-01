# MF-R011 — independent exact counting derivation

This note records a second route to the five-vertex value used in Consolidation 1.0. It is deliberately separate from the historical Python enumeration and from the Lean bit-mask scan.

The point of the note is not to manufacture novelty. It is to check the same finite claim by a different argument and to expose the structural reason the edge-toggle statistic is tied to ordinary fixed-pair reachability in a random digraph.

## 1. Ensemble

Work with loopless labeled digraphs on `n` vertices. Every directed non-loop edge is present or absent independently with probability `1/2`. There are

\[
2^{n(n-1)}
\]

graphs.

Fix two distinct vertices `s` and `t`.

For one directed edge `e=(s,t)`, pair every graph in which `e` is absent with the graph obtained by inserting `e`. Toggling `e` changes the full reachability relation exactly when, in the graph with `e` absent, `t` is not already reachable from `s`. The reverse deletion is the same unordered graph-pair viewed from the other side.

Thus, for a fixed directed edge,

\[
\Pr(\text{toggle changes reachability})
=2\Pr(e\notin G\text{ and }s\not\to t).
\]

Since `e` is necessarily absent whenever `s` does not reach `t`,

\[
\Pr(\text{toggle changes reachability})
=2\Pr(s\not\to t).
\]

By label symmetry this is also the normalized average over all directed non-loop edge coordinates. Therefore

\[
P_n=2\Pr(s\not\to t).
\]

This identity is structural, not a five-vertex fit.

## 2. Root-reachable digraph counts

Let `a_k` be the number of loopless labeled digraphs on `k` vertices in which every vertex is reachable from one distinguished root.

Clearly

\[
a_1=1.
\]

For `k>=2`, classify a graph by the exact size `j` of the root's reachable set. Choose the other `j-1` reachable labels, choose an internally root-reachable digraph on those `j` labels, forbid every edge from the reachable set to its complement, and leave every remaining edge arbitrary.

This gives the recurrence

\[
a_k
=2^{k(k-1)}
-\sum_{j=1}^{k-1}
\binom{k-1}{j-1}a_j\,2^{(k-j)(k-1)}.
\]

The first values are

\[
a_1=1,
\qquad a_2=2,
\qquad a_3=32,
\qquad a_4=2432,
\qquad a_5=745472.
\]

No decimal approximation is used here.

## 3. Exact non-reachability count for `n=5`

Now fix distinct `s,t` among five labels. If the reachable set of `s` has size `j` and does not contain `t`, choose its other `j-1` labels from the remaining three vertices. Therefore the number of five-vertex graphs with `s` not reaching `t` is

\[
\sum_{j=1}^{4}
\binom{3}{j-1}a_j\,2^{(5-j)4}.
\]

Substituting the exact values above,

\[
\begin{aligned}
&\binom30(1)2^{16}
+\binom31(2)2^{12}
+\binom32(32)2^8
+\binom33(2432)2^4\\
&=65536+24576+24576+38912\\
&=153600.
\end{aligned}
\]

Since there are

\[
2^{20}=1048576
\]

five-vertex loopless labeled digraphs,

\[
\Pr(s\not\to t)
=\frac{153600}{1048576}
=\frac{75}{512}.
\]

Hence

\[
P_5
=2\cdot\frac{75}{512}
=\frac{75}{256}.
\]

Equivalently, in the full ordered graph-edge ensemble,

\[
20\cdot2^{20}=20971520
\]

pairs are tested and

\[
20971520\cdot\frac{75}{256}=6144000
\]

of them are sensitive.

So the independent derivation reproduces exactly

\[
\boxed{P_5=\frac{75}{256}},
\qquad
\boxed{6144000\text{ sensitive pairs out of }20971520}.
\]

## 4. Independence and scope

This derivation does not use the historical Python enumerator and does not rely on the Lean `native_decide` result. Conversely, it does not replace the Lean semantic bridge: the proof-assistant branch is still needed to check that the executable bit-mask statistic is exactly the declared mathematical reachability event.

The recurrence above is also not being claimed as new. During consolidation we recovered prior random-digraph reachability literature, including Uno and Ibaraki (1998), which studies exact fixed-pair reachability probabilities. The correct role of this note is independent verification and structural clarification.

## 5. Nonclaims

This note does **not** establish:

- novelty or priority of the fixed-pair reachability problem;
- novelty of edge pivotality or edge influence;
- an asymptotic law for `P_n`;
- physical significance;
- any statement about nature from the finite graph ensemble.

Its claim is narrower: under the declared uniform loopless labeled-digraph ensemble, the five-vertex value follows exactly by the displayed counting argument and agrees with the independent executable computations.
