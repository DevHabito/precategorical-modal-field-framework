# A8.1 — Formal Resolution of 5,234 versus 6,942

## Definitions

Let \(G=(V,E)\) be a finite loopless digraph on the labeled set
\(V=\{0,\ldots,n-1\}\). Define its reflexive reachability preorder by

\[
i\preceq_G j
\quad\Longleftrightarrow\quad
\text{there is a directed path from }i\text{ to }j,
\]

including the path of length zero. Define

\[
i\sim_G j
\quad\Longleftrightarrow\quad
i\preceq_G j\ \text{and}\ j\preceq_G i.
\]

The equivalence classes of \(\sim_G\) are the strongly connected components.
The quotient \(V/{\sim_G}\), ordered by reachability, is the condensation
partial order.

### Full labeled condensation code

The matrix

\[
C_{\mathrm{full}}(G)
=
\bigl[\mathbf 1(i\preceq_G j)\bigr]_{i,j\in V}
\]

is injective on the complete labeled condensation structure. Its symmetric
part recovers the SCC partition and its quotient recovers the partial order.

### Minimum-representative code

For each SCC \(B\), let \(m(B)=\min B\), and let

\[
A(G)=\{m(B):B\in V/{\sim_G}\}.
\]

The original A8 code stores only \(A(G)\) and the strict quotient order
restricted to \(A(G)\). It does not store the assignment of nonminimum
vertices to SCCs. Therefore it is not a full labeled condensation code.

## Exact counting theorem

Let \(p(k)\) be the number of partial orders on \(k\) labeled elements and
\(S(n,k)\) the Stirling number of the second kind.

A full labeled condensation structure is obtained by:

1. partitioning \(V\) into \(k\) SCC blocks;
2. choosing a partial order on those \(k\) distinct blocks.

Hence

\[
N_{\mathrm{full}}(n)
=
\sum_{k=1}^{n} S(n,k)\,p(k).
\]

For the minimum-representative code, the active minimum set must contain
vertex \(0\), and every subset containing \(0\) is feasible. There are
\(\binom{n-1}{k-1}\) such sets of size \(k\). Hence

\[
N_{\mathrm{rep}}(n)
=
\sum_{k=1}^{n}
\binom{n-1}{k-1}\,p(k).
\]

For \(n=5\),

\[
p(1),\ldots,p(5)
=
1,3,19,219,4231,
\]

so

\[
N_{\mathrm{full}}(5)
=
1+45+475+2190+4231
=
6942,
\]

whereas

\[
N_{\mathrm{rep}}(5)
=
1+12+114+876+4231
=
5234.
\]

Thus both numbers are correct, but they count different objects.

## Corrected terminology

- \(6942\): distinct full labeled condensation preorders.
- \(5234\): distinct minimum-representative quotient-poset codes.

The phrase “distinct labeled condensation-poset codes” must not be used for
the second number without the minimum-representative qualification.

## Edge-flip result

Although the original code is globally noninjective, exhaustive enumeration
shows that for a single edge flip on \(n=5\), it changes if and only if the
full labeled reachability preorder changes. Therefore the previously reported
edge-flip fraction remains exactly

\[
\frac{75}{256}=0.29296875.
\]

This preservation is an enumerative fact at \(n=5\), not a general theorem
established here.
