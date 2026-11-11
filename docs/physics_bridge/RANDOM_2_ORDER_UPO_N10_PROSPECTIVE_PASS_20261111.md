# N=10 prospective direct regression — PASS

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact prospective finite regression

The prediction was committed before direct enumeration:

\[
C_{10}=692297,
\qquad
R_{10}=843873.
\]

An independent C++ classifier then enumerated all

\[
10!=3628800
\]

relative permutations.

The direct classifier did not use the substitution counting formula. It used:

1. the increasing-pair comparability graph;
2. connected-component classification;
3. the induced relative permutation on the unique nontrivial component;
4. the proper-common-interval criterion.

The observed results were

\[
\boxed{
C_{10}=692297
}
\]

and

\[
\boxed{
R_{10}=843873.
}
\]

Thus both preregistered counts passed exactly.

The complete partition was:

\[
843873
+
2636060
+
148866
+
1
=
3628800,
\]

corresponding respectively to:

- recoverable;
- internal module ambiguity;
- multiple nontrivial components;
- empty antichain.

The exact recovery fraction is

\[
\boxed{
\frac{843873}{3628800}
=
\frac{281291}{1209600}
\approx0.23254877645502645.
}
\]

This is a prospective finite validation of the counting theorem.

It is not a novelty certificate and does not turn orientation recovery into a physical theory of time.
