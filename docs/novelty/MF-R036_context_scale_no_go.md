# MF-R036 — Context–Scale Incompatibility

**Novelty audit:** C2  
**Search date:** 2026-07-15  
**Final classification:** `ELEMENTARY_COROLLARY_OF_STANDARD_MEASUREMENT_INVARIANCE`

## Exact claim

Let \(D_S(x,y)\) be the difference between scalar scores assigned to two
alternatives \(x,y\) in a finite context \(S\). Assume:

1. **Extension stability:** adding arbitrary alternatives to the context does
   not change \(D_S(x,y)\);
2. **positive-affine invariance:**
   \[
   D(ax+b,ay+b)=D(x,y),\qquad a>0;
   \]
3. **continuity and normalization:** \(D\) is continuous and \(D(x,x)=0\).

Then \(D\equiv0\).

## Proof status

The proof is correct and short.

Extension stability removes dependence on the surrounding context. Translation
invariance gives

\[
D(x,y)=h(x-y).
\]

Scale invariance gives

\[
h(ad)=h(d),\qquad a>0.
\]

Thus \(h\) is constant on \((0,\infty)\) and separately constant on
\((-\infty,0)\). Continuity at zero and \(h(0)=0\) force both constants to be
zero.

## Prior literature comparison

Representational measurement theory treats an interval scale as unique up to

\[
x\mapsto ax+b,\qquad a>0,
\]

and studies which functions or statements remain meaningful under that
transformation group. Marichal and Mesiar review this invariance-based
programme and the associated functional equations.

No source was located that combines the project's exact phrase “extension
stability” with this two-point score-difference formulation. However, after
extension stability removes context, the remaining no-go is an elementary
consequence of standard interval-scale invariance. It should not be presented
as a deep new functional-equation theorem.

## Important clarification

The theorem assumes **numerical invariance of the score difference itself**:

\[
D(ax+b,ay+b)=D(x,y).
\]

This is stronger than the ordinary interval-scale fact that numerical
differences transform covariantly:

\[
(ax+b)-(ay+b)=a(x-y).
\]

Ratios of nonzero differences can be meaningful on interval scales, while an
absolute numerical difference independent of the unit cannot remain both
cardinal and nontrivial without an external scale convention.

## Project contribution that remains

The useful contribution is the explicit trilemma inside the Modal Field
architecture:

- raw differences are extension-stable but scale-covariant;
- context normalization can be scale-invariant but is context-dependent;
- ordinal signs/ranks can be invariant but are not cardinal.

That organization is valuable, even though the proof itself is elementary.

## Safe manuscript wording

> We formalize an elementary incompatibility between context extension,
> numerical invariance under all positive-affine recalibrations, and continuous
> nontrivial cardinal score differences. The argument is a direct
> measurement-invariance corollary rather than a new general theorem.

## Wording to avoid

- “We prove a fundamentally new measurement-theory impossibility theorem.”
- “Interval-scale differences are meaningless.”
- “No invariant quantitative comparison can exist under any enriched model.”

## Editorial decision

Demote from “central new theorem” to a **foundational lemma**. Keep the
trilemma and its consequence for selecting \(q\)-based scores.
