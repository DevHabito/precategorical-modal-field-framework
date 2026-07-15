# MF-R049 — Failure of Scalar Dynamic Closure

**Novelty audit:** C2  
**Search date:** 2026-07-15  
**Final classification:** `PROJECT_SPECIFIC_EXACT_NONCLOSURE_COROLLARY_WITH_CONSTRUCTIVE_WITNESS`

## Exact claim

A macrostate consisting only of the mean and a single fixed-\(\lambda\) score,

\[
(\bar q,Q_\lambda),
\]

does not generally determine the next \(Q_\lambda\) under the centered
contraction

\[
q_i'=\bar q+a(q_i-\bar q).
\]

The transport identity requires \(Q_{a\lambda}\), which is not determined by
one value \(Q_\lambda\) on the unrestricted class of finite distributions.

## Exact four-point witness

Let

\[
\lambda=\log2,\qquad a=\frac12,
\]

with support

\[
q\in\{0,1,2,3\}.
\]

Define two probability vectors

\[
p^+
=
\left(
\frac9{40},
\frac7{20},
\frac18,
\frac3{10}
\right),
\]

and

\[
p^-
=
\left(
\frac{11}{40},
\frac3{20},
\frac38,
\frac15
\right).
\]

Both have mean

\[
\bar q=\frac32.
\]

At \(\lambda=\log2\),

\[
\sum_i p_i^+e^{-\lambda q_i}
=
\sum_i p_i^-e^{-\lambda q_i}
=
\frac{15}{32}.
\]

Therefore

\[
Q_\lambda(p^+)=Q_\lambda(p^-).
\]

At the required rescaled parameter \(a\lambda=\tfrac12\log2\),

\[
M^+_{a\lambda}
=
\frac{23}{80}+\frac{\sqrt2}{4},
\]

whereas

\[
M^-_{a\lambda}
=
\frac{37}{80}+\frac{\sqrt2}{8}.
\]

Their difference is

\[
M^+_{a\lambda}-M^-_{a\lambda}
=
\frac{5\sqrt2-7}{40}>0.
\]

Thus

\[
Q_{a\lambda}(p^+)\neq Q_{a\lambda}(p^-),
\]

and consequently

\[
Q_\lambda'(p^+)\neq Q_\lambda'(p^-).
\]

This is an exact counterexample, not a fitted or Monte Carlo witness.

## Prior literature comparison

Moment-closure literature treats the generic problem that low-order summaries
do not determine unresolved higher-order quantities and that closure usually
requires an approximation or an invariant family. Separately, uniqueness
results for Laplace transforms show that a complete transform—or a
sufficiently rich set of values—can determine a distribution.

Those bodies of work strongly anticipate the obstruction. No source was
located that states this exact mean-plus-one-entropic-score counterexample
under the centered contraction.

The correct status is therefore not “new general moment-closure theorem,” but:

> a project-specific exact corollary of transform non-identifiability, supported
> by a clean constructive witness.

## Whole-curve closure

For this deterministic contraction, carrying the mean and the entire curve

\[
\lambda\mapsto Q_\lambda
\]

is sufficient, because every future fixed-\(\lambda\) value is obtained from
the previous value at \(a\lambda\).

This does not imply that the curve is the minimal state for every restricted
family. Gaussian or other invariant finite-dimensional families may close
with fewer parameters.

## Safe manuscript wording

> A single entropic score is not an autonomous macrostate on the unrestricted
> finite-distribution class. We give an exact four-point counterexample with
> identical mean and identical \(Q_{\log2}\), but different
> \(Q_{\frac12\log2}\), and hence different next scores under the centered
> contraction.

## Wording to avoid

- “No finite-dimensional closure can ever exist.”
- “The whole curve is always the unique minimal macrostate.”
- “This is a new theorem resolving the general moment-closure problem.”
- “The counterexample establishes physical macrodynamics.”

## Editorial decision

This is the strongest mathematically self-contained result in the A34 group.
Promote it as an exact proposition/counterexample in the foundational paper,
while linking it explicitly to classical moment-closure and transform
identifiability literature.
