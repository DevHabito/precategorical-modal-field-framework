# Symmetry-breaking information budget on cycle skeletons

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** classical distinguishing-number benchmark + exact finite repository regression  
**Novelty status:** distinguishing numbers are classical; project-specific role is to refine the A22 admissibility statement for pregeometric orientation

## 1. Why this audit was needed

A22 established an information-theoretic minimum:

> a one-symbol mark is constant, so a binary alphabet is the smallest alphabet that can carry nontrivial additional marked information.

That statement is correct.

It does **not** imply that two symbols are sufficient to destroy every structural symmetry of a particular relational object.

The pregeometric direction problem requires a stronger question:

> How rich must an added mark be before the relevant reversal automorphisms are actually removed?

This belongs to classical graph symmetry breaking.

## 2. Distinguishing labeling

For a graph \(G\), a vertex labeling

$$
\ell:V(G)\to\{1,\ldots,k\}
$$

is distinguishing if the only graph automorphism preserving every label is the identity.

The distinguishing number

$$
D(G)
$$

is the smallest \(k\) for which such a labeling exists.

This definition is due to the classical graph-symmetry literature.

## 3. Cycle benchmark

For cycle graphs,

$$
\boxed{
D(C_n)=
\begin{cases}
3,&n=3,4,5,\\
2,&n\ge 6.
\end{cases}
}
$$

Therefore a binary mark is not sufficient to remove all automorphisms of

$$
C_3,\;C_4,\;C_5.
$$

The graphA undirected skeleton is

$$
C_4.
$$

Hence

$$
\boxed{
D(C_4)=3.
}
$$

## 4. Exact exhaustive regression

A repository audit enumerates every vertex coloring for cycle sizes

$$
n=3,\ldots,10
$$

and alphabets

$$
k=1,\ldots,4.
$$

For each coloring it enumerates the full dihedral automorphism group and checks whether the stabilizer is trivial.

The exact counts of distinguishing colorings are:

| \(n\) | \(k=1\) | \(k=2\) | \(k=3\) | \(k=4\) | minimal \(k\) |
|---:|---:|---:|---:|---:|---:|
| 3 | 0 | 0 | 6 | 24 | 3 |
| 4 | 0 | 0 | 24 | 120 | 3 |
| 5 | 0 | 0 | 120 | 720 | 3 |
| 6 | 0 | 12 | 444 | 3192 | 2 |
| 7 | 0 | 28 | 1638 | 14616 | 2 |
| 8 | 0 | 96 | 5328 | 60480 | 2 |
| 9 | 0 | 252 | 17550 | 253008 | 2 |
| 10 | 0 | 600 | 54240 | 1022640 | 2 |

The calculation reproduces the classical distinguishing-number result.

It is not a new graph theorem.

## 5. Consequence for graphA

The graphA skeleton has 16 binary vertex labelings.

None is distinguishing.

Thus no binary vertex mark on the undirected square eliminates every nontrivial dihedral symmetry.

A ternary mark can.

There are exactly 24 distinguishing ternary colorings of the labeled \(C_4\).

Therefore the A22 statement

$$
\text{binary is the smallest nontrivial alphabet}
$$

must not be promoted into

$$
\text{binary always supplies enough symmetry breaking}.
$$

The second statement is false.

## 6. Relevance to orientation

To choose one chirality of an undirected cycle canonically, reflection symmetries must at least be broken.

A fully distinguishing coloring is stronger: it removes rotations as well.

For the short cycles \(C_3,C_4,C_5\), binary vertex markings fail even the classical full-symmetry benchmark.

Thus the amount of additional information required depends on the automorphism group of the primitive structure.

There is no structure-independent claim that “one bit creates direction.”

## 7. Connection to q

A real-valued independently calibrated field \(q\) can generically destroy graph automorphisms if its values are sufficiently asymmetric.

But that statement is mathematically cheap.

It says only that enough extra labels can identify vertices.

For pregeometry, the actual questions remain:

1. where do the \(q\)-values come from?
2. which transformations of \(q\) are gauge?
3. which \(q\)-contrasts are observable?
4. does the physically observable marked structure actually break the reversal automorphism?
5. is the resulting asymmetry causal/temporal or merely cardinal?

The current A24 row-gauge audit already shows that raw reciprocal edge \(q\)-differences fail question 3.

## 8. Symmetry-breaking budget is structure dependent

The correct general principle is:

$$
\boxed{
\text{minimum added mark complexity depends on }\operatorname{Aut}(G).
}
$$

A22 supplied a lower bound on alphabet cardinality for any nontrivial information.

Distinguishing-number theory supplies a stronger graph-specific benchmark for complete automorphism breaking.

These are different questions.

## 9. Physical boundary

A distinguishing labeling does not become physical merely because it destroys symmetries.

An arbitrary unique identifier on every vertex would trivially make most finite structures asymmetric.

That would be the opposite of emergence: the answer would be stored directly in the labels.

Therefore a physically admissible mark must also satisfy:

- label invariance/equivariance;
- operational measurability;
- an independently justified preparation or origin;
- gauge consistency;
- non-circular semantics.

## 10. Current conclusion

The finite C1 examples now show three layers:

1. **unmarked skeleton:** reversal symmetry prevents intrinsic orientation;
2. **sufficiently rich added marks:** symmetry can be broken mathematically;
3. **physical direction:** still requires an independently justified meaning for those marks.

The project should measure symmetry-breaking requirements before introducing a marked primitive, but should never mistake the existence of a distinguishing coloring for a physical derivation of time.
