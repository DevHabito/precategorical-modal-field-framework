# A103 — Exact Continuum Atlas for the 76 Endpoint-Released Lift Segments

## Question

A97 found 76 rational witnesses for which the finite LP has the strict active architecture

\[
P=\{j-1,j,M\},\qquad Q=\{1,h,h+1\},\qquad h=\lfloor M/2\rfloor,
\]

with \(\alpha+\) and \(\beta-\) active and both \(\gamma\) inequalities inactive. A102 later placed those witnesses inside the complete 1,063-witness lift atlas. The remaining question was whether each A97 basis is valid only at its witness or on a continuous part of the corresponding A95 rational phase segment.

A103 answers that question for all 76 segments without assuming that the answer is positive on the whole segment.

## Exact symbolic reduction

Only the \(\alpha\)-row depends on the probe \(s\). Starting from the dyadic reference value \(s=1/8\), the audit applies an exact Sherman–Morrison row update to the seven-dimensional basis matrix. Every basic variable, active multiplier, reduced cost, inactive-band slack, and the basis denominator is therefore represented by a sparse rational polynomial numerator over one sparse common denominator.

The atlas contains

\[
54\,944
\]

KKT conditions and 76 additional common denominators, for

\[
55\,020
\]

exact sparse polynomial sign obligations.

No floating-point tolerance decides any gate.

## Segment classification

The 76 source objects are the exact rational inner phase segments committed by A95. The result is

\[
\boxed{25\text{ complete-segment certificates}}
\]

and

\[
\boxed{51\text{ proper witness-containing strict components}}.
\]

There are no unresolved segments and no internal counterexample inside any certified component.

The classification is exactly aligned with the compressed phase type:

| Compressed phase | Source segments | Lifted continuum result |
|---|---:|---|
| unique \(b+3\) | 14 | complete source-segment coverage |
| \(b+2\to b+3\), right side | 11 | complete source-segment coverage |
| \(b+1\to b+2\), right side | 46 | proper strict subcomponent |
| unique \(b+2\) | 5 | proper strict subcomponent |

Thus all 25 offset-three-related segments in this 76-segment family remain valid throughout their complete declared rational source segments. The other 51 witnesses are genuine local phases, but their bases encounter an additional full-LP KKT boundary before the end of the compressed phase segment.

## Boundary mechanisms

A103 isolates 55 selected algebraic boundaries. Every selected root has opposite exact endpoint signs and a derivative of fixed nonzero sign on its isolating bracket.

The boundary census is:

- 4 lower boundaries where the inactive \(\gamma-\) slack reaches zero;
- 49 upper boundaries where the lower adjacent basic mass \(p_{j-1}\) reaches zero;
- 2 upper boundaries where the nonbasic reduced cost of \(q_0\) reaches zero.

The two \(q_0\)-entry boundaries occur in the unique-\(b+2\) segments at \(M=437\) and \(M=478\). In those cases the reduced-cost boundary is encountered before the adjacent \(P\)-mass boundary.

## Complete exact certification

For every record, all oriented KKT numerators and the common denominator are strictly positive on a closed rational core containing the A95 witness. For every partial segment, all nonselected conditions are additionally certified on the complete hull spanning the tiny algebraic boundary brackets. The selected boundary condition is controlled by its opposite endpoint signs and fixed derivative sign.

The exact sign census closes with:

\[
55\,020/55\,020
\]

core polynomial certificates and zero failures. Every proper component also has an exact rational point outside it where the selected boundary condition is negative. Because four records have both a lower and an upper boundary, the 51 partial segments produce 55 exact outside counterexamples.

## What changed scientifically

The pointwise closure in A102 does not automatically promote to complete segment coverage. A103 separates two statements that had previously been easy to conflate:

1. the endpoint-released architecture is a valid continuous phase around every one of its 76 witnesses;
2. only 25 of those phases cover the entire compressed rational source segment.

This is a useful negative result. The compressed maximizer can remain unchanged while the lifted LP changes active architecture. In most partial cases the first new event is the disappearance of \(p_{j-1}\); in four cases \(\gamma-\) becomes active at the lower side, and in two cases \(q_0\) wants to enter at the upper side.

## Scope boundary

A103 proves an exact theorem only for the 76 A95 rational inner phase segments assigned to the endpoint-released family. It does not prove:

- continuous lifting for the other 987 A102 witnesses;
- coverage of the excluded algebraic root brackets or the complete A92 cells beyond the A95 rational inner segments;
- a universal support law for arbitrary \(M\), means, targets, or noise contracts;
- any physical, spacetime, matter, or ontological interpretation.

## Next rigorous target

The next nonredundant target is A104: perform the same continuous promotion for the three \(q_0/q_1\), \(\gamma\)-inactive witnesses resolved by A98–A99 and the four \(q_0/q_1\), \(\gamma-\)-active witnesses resolved by A100–A101. The audit must determine whether the seven exceptional architectures cover their complete A95 rational source segments, occupy proper subcomponents, or undergo further active-set changes.
