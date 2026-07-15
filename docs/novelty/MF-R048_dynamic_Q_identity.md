# MF-R048 — Centered-Contraction Transport Identity

**Novelty audit:** C2  
**Search date:** 2026-07-15  
**Final classification:** `PROJECT_SPECIFIC_DIRECT_COROLLARY_OF_CLASSICAL_AFFINE_IDENTITY`

## Exact claim

For the centered affine contraction

\[
q_i'
=
\bar q+a(q_i-\bar q)
=
(1-a)\bar q+aq_i,
\]

the effective score satisfies

\[
Q_\lambda(q')
=
(1-a)\bar q+aQ_{a\lambda}(q).
\]

## Derivation

Set

\[
c=(1-a)\bar q.
\]

Then \(q'=aq+c\). Applying affine covariance gives

\[
Q_\lambda(q')
=
c+aQ_{a\lambda}(q)
=
(1-a)\bar q+aQ_{a\lambda}(q).
\]

## Novelty comparison

No source was located that states this exact identity for the project's
centered \(q\)-contraction. However, the equation is a one-line substitution
into the classical affine covariance of the exponential certainty equivalent.

Its mathematical status is therefore:

- exact;
- elegant;
- useful inside the framework;
- not an independent new theorem.

## What is project-specific

The project-specific contribution is the interpretation of the equation as a
transport law on the parameterized curve

\[
\lambda\mapsto Q_\lambda.
\]

A step of the contraction at fixed observational \(\lambda\) requires the
previous state at \(a\lambda\). This immediately exposes why one fixed-lambda
summary is not autonomous in general.

## Safe manuscript wording

> For the proposed centered contraction, classical affine covariance yields
> the exact transport identity
> \(Q_\lambda'=(1-a)\bar q+aQ_{a\lambda}\).
> The identity is model-specific as a dynamical statement, but algebraically it
> is a direct corollary of the exponential certainty-equivalent transform.

## Wording to avoid

- “We introduce a previously unknown log-partition identity.”
- “This equation is a derived law of nature.”
- “The equation establishes a physical renormalization flow in \(\lambda\).”

## Editorial decision

Retain prominently as a **central exact proposition**, while describing its
novelty correctly: the algebra is classical; the use as a closure diagnostic
inside the Modal Field framework is project-specific.
