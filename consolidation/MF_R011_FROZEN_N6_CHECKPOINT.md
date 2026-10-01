# MF-R011 — frozen n=6 exact cross-check target

**Frozen:** 2026-10-01  
**Purpose:** pre-register an exact next checkpoint before writing an independent n=6 checker.  
**Status:** derived target, not yet an independent computational verification.

This note deliberately freezes the expected integers and fractions first. If a
later independently written checker disagrees, the target in this file must not
be edited to fit the checker. The disagreement must be investigated.

## 1. General counting consequence

Let `a_j` denote the number of loopless labeled digraphs on `j` vertices in
which every vertex is reachable from one distinguished root.

The exact recurrence is

\[
a_1=1,
\]

and, for \(n\ge 2\),

\[
a_n
=2^{n(n-1)}
-\sum_{j=1}^{n-1}
\binom{n-1}{j-1}a_j\,2^{(n-j)(n-1)}.
\]

These are the classical counts of initially connected rooted digraphs. The
values used here agree with published tables, including Jonah Ostroff,
*Counting Connected Digraphs with Gradings*, PhD dissertation, Brandeis
University, 2013, Table 1. No novelty claim is attached to this sequence.

Fix distinct labels `s,t`. Let `B_n` be the number of loopless labeled digraphs
on `n` vertices in which `t` is not reachable from `s`.

If the reachable set of `s` has size `j`, it contains `s`, excludes `t`, and
chooses its remaining `j-1` labels from the other `n-2` labels. Its internal
graph must be one of the `a_j` rooted-reachable graphs. Every edge from that
reachable set to its complement is forbidden; all edges from the complement
back into the reachable set and all edges internal to the complement are free.
There are

\[
(n-j)j+(n-j)(n-j-1)=(n-j)(n-1)
\]

such free edges.

Therefore

\[
\boxed{
B_n
=\sum_{j=1}^{n-1}
\binom{n-2}{j-1}a_j\,2^{(n-j)(n-1)}
}.
\]

Since the structural toggle pairing gives

\[
P_n=2\Pr(s\not\leadsto t),
\]

we have the exact consequence

\[
\boxed{
P_n=\frac{2B_n}{2^{n(n-1)}}
}.
\]

This is a counting consequence of the structural reduction; it is not claimed
as a new random-digraph recurrence.

## 2. Inputs for n=6

The required rooted-reachable counts are

\[
a_1=1,
\qquad a_2=2,
\qquad a_3=32,
\qquad a_4=2432,
\qquad a_5=745472.
\]

For `n=6`,

\[
B_6
=\sum_{j=1}^{5}
\binom{4}{j-1}a_j\,2^{(6-j)5}.
\]

Keep every term as an integer:

\[
\begin{aligned}
j=1:&\quad \binom40(1)2^{25}=33554432,\\
j=2:&\quad \binom41(2)2^{20}=8388608,\\
j=3:&\quad \binom42(32)2^{15}=6291456,\\
j=4:&\quad \binom43(2432)2^{10}=9961472,\\
j=5:&\quad \binom44(745472)2^5=23855104.
\end{aligned}
\]

Thus

\[
\boxed{
B_6
=33554432+8388608+6291456+9961472+23855104
=82051072
}.
\]

The full six-vertex graph ensemble has

\[
2^{30}=1073741824
\]

graphs, so

\[
\Pr(s\not\leadsto t)
=\frac{82051072}{1073741824}
=\frac{313}{4096}.
\]

Therefore the frozen sensitivity target is

\[
\boxed{
P_6=\frac{313}{2048}
}.
\]

No decimal approximation is part of the checkpoint.

## 3. Full graph-edge integer target

There are

\[
6\cdot5=30
\]

directed non-loop edge coordinates, hence

\[
30\cdot2^{30}
=32212254720
\]

ordered `(graph, edge)` pairs.

The predicted exact number of sensitive pairs is

\[
32212254720\cdot\frac{313}{2048}
=4923064320.
\]

So an independent n=6 implementation must reproduce exactly

\[
\boxed{4923064320\text{ sensitive pairs out of }32212254720},
\]

or equivalently

\[
\boxed{P_6=313/2048}.
\]

## 4. Independence requirement for the next checker

A future checker does not count as an independent verification if it simply
imports `B_6=82051072`, `313/4096`, `313/2048`, or the recurrence output from
this note.

Preferred acceptable routes are:

1. a separately written exact fixed-pair reachability computation following a
   different state decomposition;
2. an independent implementation of a published exact method for
   \(\gamma_{n,p}\), evaluated at `n=6`, `p=1/2`;
3. a proof-assistant derivation from separately formalized finite-set counting
   definitions.

A brute-force scan over all `2^30` graphs is not required and should not be
attempted merely to look more exhaustive if a mathematically exact independent
method is available.

## 5. Failure rule

If the independent result differs from any frozen integer above:

- do not average, round, or replace either value;
- do not weaken the discrepancy into a numerical tolerance issue;
- identify the first differing definition or counting step;
- preserve both outputs and the failed route in provenance;
- do not promote the n=6 value until the discrepancy is resolved.

## 6. Nonclaims

This checkpoint does not establish novelty, asymptotics, monotonicity of
`P_n`, physical meaning, or any connection to nature. It is one exact,
pre-registered mathematical cross-check target under the declared uniform
loopless labeled-digraph ensemble.
