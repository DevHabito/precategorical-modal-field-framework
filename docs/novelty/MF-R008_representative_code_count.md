# MF-R008 — Minimum-Representative Quotient-Poset Codes

**Novelty audit:** C1  
**Search date:** 2026-07-15  
**Final classification:** `PROJECT_SPECIFIC_ELEMENTARY_PROPOSITION_NO_MATCH_FOUND`

## Exact claim

For each strongly connected component \(B\), retain only its minimum labeled
vertex \(m(B)\), and retain the quotient partial order on the set of these
representatives. Discard the assignment of all nonminimum vertices to SCCs.

Let \(p(k)\) be the number of labeled \(k\)-element posets. The number of such
codes on \(\{0,\ldots,n-1\}\) is

\[
N_{\mathrm{rep}}(n)
=
\sum_{k=1}^{n}\binom{n-1}{k-1}p(k).
\]

For \(n=5\),

\[
N_{\mathrm{rep}}(5)=5234.
\]

## Formal verification status

The declared counting claim is now formalized end to end in Lean 4 under the
project's pinned Lean/mathlib environment. The formal chain:

- proves the cardinality \(\binom{n-1}{k-1}\) of representative sets containing the distinguished label `0`;
- independently enumerates the small labeled-poset counts through a three-state antisymmetric encoding and Lean `native_decide`;
- proves the executable transitivity checker equivalent to mathematical transitivity;
- constructs a bijection between accepted encodings and Boolean partial-order matrices;
- derives the fiber sum from an explicit canonical code type rather than taking the formula as a definition;
- proves that the canonical `Fin k` presentation is equivalent to the literal code `(S,P)` in which `P` is a partial order on the actual representative set `S`;
- proves `Nat.card (LiteralRepresentativeCode 4) = 5234`.

The full Lean library build passes with no `sorry`/`admit`, and every project
module passes a bundled `leanchecker` kernel replay in the module-sharded CI.
The `native_decide` values are exact finite formal computations; this does not
turn the classical poset-count sequence into a new analytic theorem.

This formal verification changes the verification status of the claim, not its
novelty classification. The literature assessment below remains separate.

## Why the formula holds

The representative set must contain vertex \(0\). Conversely, every
\(k\)-element subset containing \(0\) is feasible as a set of SCC minima.
There are

\[
\binom{n-1}{k-1}
\]

such subsets. Once a representative set is chosen, any partial order on its
\(k\) labeled representatives is a valid quotient-poset code.

The formula is therefore immediate from the definition of the project-specific
encoding.

## Literature search

Searches covered:

- finite-preorder and finite-topology enumeration;
- restricted finite topologies;
- set partitions with prescribed block minima;
- restricted growth functions, which canonically encode set partitions;
- exact searches for the formula and the initial sequence
  \(1,4,26,286,5234,153574,\ldots\);
- terminology involving SCC minima and representative quotient codes.

The literature inspected contains standard encodings of set partitions by
restricted growth functions and classical counts of preorders, but no source
was located that defines this exact lossy SCC-minimum code or states the same
count.

A negative search result is not proof of global novelty. The correct status is
therefore “no matching prior formulation found in the searched literature,”
not “first theorem of its kind.”

## Mathematical comparison

This claim differs from the classical preorder count because it does not retain
the equivalence-class partition. A code is only a pair

\[
(S,P),
\]

where \(S\subseteq\{0,\ldots,n-1\}\), \(0\in S\), and \(P\) is a partial order
on \(S\). The discarded SCC membership is exactly why \(5234<6942\).

The ordinary generating function satisfies

\[
\sum_{n\geq1}N_{\mathrm{rep}}(n)x^n
=
\sum_{k\geq1}p(k)
\left(\frac{x}{1-x}\right)^k,
\]

as a direct consequence of the shifted binomial transform.

## Novelty assessment

- **Definition:** project-specific.
- **Proof difficulty:** elementary once the encoding is stated.
- **Technical value:** useful as a corrective proposition and as a precise
  analysis of information loss.
- **Standalone theorem value:** limited without a broader theory of encoding
  fibers, asymptotics, or optimal representatives.

## Safe manuscript wording

> We define a minimum-representative quotient-poset encoding and derive its
> exact count
> \(N_{\mathrm{rep}}(n)=\sum_k\binom{n-1}{k-1}p(k)\).
> We found no matching formulation in the sources searched, but the counting
> argument is elementary and the principal significance is corrective: it
> identifies exactly what the earlier value \(5234\) counted.

## Wording to avoid

- “This is definitively the first formula of this type.”
- “The \(5234\) count is a deep new enumeration theorem.”
- “The code retains the full labeled condensation structure.”

## Editorial decision

Retain as a named project proposition inside the combinatorics paper, but do
not make it the sole headline theorem. Its strongest role is in the formal
resolution of the coding ambiguity and in a subsequent study of code fibers.
