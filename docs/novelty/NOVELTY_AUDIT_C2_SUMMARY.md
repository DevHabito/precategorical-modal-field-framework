# Novelty Audit C2 — Context–Scale Compatibility and Effective-Score Closure

**Project:** Pre-Categorical Modal Field Framework  
**Author:** Felipe Gianini Romero  
**Search date:** 2026-07-15  
**Scope:** MF-R036, MF-R047, MF-R048, MF-R049

## Executive verdict

| Claim | Final classification | Manuscript treatment |
|---|---|---|
| MF-R036 | Elementary corollary of standard measurement invariance | Keep as foundational lemma, not a headline new theorem |
| MF-R047 | Classical algebraic identity of exponential certainty equivalents | Attribute as background |
| MF-R048 | Project-specific direct corollary of MF-R047 | Keep prominently as exact transport proposition |
| MF-R049 | Project-specific exact non-closure corollary with constructive witness | Promote as the strongest self-contained A34 result |

## Main correction to novelty language

Three mathematically correct claims require weaker novelty wording:

1. **MF-R036** is a short invariance argument once context dependence has been
   removed.
2. **MF-R047** is standard log-Laplace / entropic certainty-equivalent algebra.
3. **MF-R048** follows immediately by substituting the centered affine map into
   MF-R047.

Their value is in how they organize the framework, not in priority over the
underlying mathematics.

## Strongest retained result

MF-R049 now has an exact four-point witness. Two distributions have identical

\[
\bar q=\frac32
\]

and identical

\[
Q_{\log2},
\]

but different

\[
Q_{\frac12\log2}.
\]

Under contraction \(a=\tfrac12\), their next \(Q_{\log2}\) values therefore
differ. No optimization, random seed, or tolerance is needed for the logical
counterexample.

## Literature relationship

- Measurement theory supplies the positive-affine transformation group for
  interval scales and the meaningfulness framework.
- Entropic risk-measure and exponential-utility literature supplies the
  classical object underlying \(Q_\lambda\).
- Moment-closure literature explains why low-dimensional summaries generally
  require additional closure assumptions.
- Laplace-transform uniqueness literature shows why a full transform curve is
  qualitatively different from a single evaluation.

## Consequence for the foundational paper

The paper should present a hierarchy:

1. standard measurement-invariance background;
2. standard affine covariance of the exponential certainty equivalent;
3. the framework-specific centered-contraction transport identity;
4. the exact scalar non-closure counterexample;
5. conditional finite-dimensional closure only when an invariant family is
   independently justified.

## Matrix updates

Apply `RESULT_CLASSIFICATION_PATCH_C2.csv` to MF-R036, MF-R047, MF-R048, and
MF-R049. The mathematical formulas remain unchanged; only novelty,
attribution, and editorial status are refined.

## Limits

A negative literature search cannot certify priority. The package authorizes
cautious phrases such as “no exact match was located in the searched
literature,” but not “first ever.”
