# MF-R047 — Affine Covariance of the Effective Score

**Novelty audit:** C2  
**Search date:** 2026-07-15  
**Final classification:** `CLASSICAL_ALGEBRAIC_IDENTITY`

## Exact claim

For positive normalized masses \(\mu_i\),

\[
Q_\lambda(q,\mu)
=
-\frac1\lambda
\log\sum_i\mu_i e^{-\lambda q_i}.
\]

For \(a>0\) and \(c\in\mathbb R\),

\[
Q_\lambda(aq+c,\mu)
=
c+aQ_{a\lambda}(q,\mu).
\]

## Derivation

\[
\begin{aligned}
Q_\lambda(aq+c)
&=
-\frac1\lambda
\log\sum_i\mu_i e^{-\lambda(aq_i+c)}\\
&=
-\frac1\lambda
\log\left(
e^{-\lambda c}
\sum_i\mu_i e^{-a\lambda q_i}
\right)\\
&=
c-\frac1\lambda
\log\sum_i\mu_i e^{-a\lambda q_i}\\
&=
c+aQ_{a\lambda}(q).
\end{aligned}
\]

## Prior literature comparison

This object is the exponential certainty equivalent, up to sign conventions,
and is directly related to the entropic risk measure. Cash/translation
invariance is standard in convex-risk-measure theory, and exponential utility
generates the entropic functional. The scaling relation follows immediately
when the scale change is absorbed into the risk-aversion or transform
parameter.

The exact notation used in A34 is project-specific, but the algebra is not a
new result.

## Project contribution that remains

The useful point is interpretive:

- changing the scale of \(q\) changes the effective parameter from
  \(\lambda\) to \(a\lambda\);
- therefore \(\lambda\) cannot be treated independently of the score
  convention;
- the full \(Q(\lambda)\) curve transforms naturally under affine changes.

## Safe manuscript wording

> The exponential effective score obeys the standard affine covariance of an
> exponential certainty equivalent,
> \(Q_\lambda(aq+c)=c+aQ_{a\lambda}(q)\). We use this classical algebraic
> identity to track the coupling between score scale and the parameter
> \(\lambda\).

## Wording to avoid

- “We discovered a new transformation law for log-partition functions.”
- “The identity is evidence of renormalization-group dynamics.”
- “\(Q_\lambda\) is thereby established as physical free energy.”

## Editorial decision

Treat as a **background identity with attribution**, not as a novelty claim.
Its role is to support the dynamic result and the parameter-status discussion.
