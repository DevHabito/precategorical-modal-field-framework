# A115 — corrections and dead ends

**Date:** 2026-09-14

This file preserves failed or invalid intermediate routes rather than deleting
them.

## 1. False universal threshold

A tempting extension of A113 was

\[
M\ge521,\quad\beta<s<\tau<1
\Longrightarrow
J_{\tau,b_\tau+1}>0.
\]

This is false.

Valid in-domain exact counterexamples include

\[
(M,s,\tau)=
\left(521,\frac{131}{1000},\frac{141}{1000}\right)
\]

and

\[
(M,s,\tau)=
\left(521,\frac{133}{1000},\frac{143}{1000}\right).
\]

Both use valid A84 adjacent contacts and survive an independent direct
\(3\times3\) rational reconstruction.

Therefore the frozen A113 threshold `521` cannot be carried unchanged into
the target-deformed problem.

## 2. Rejected exploratory counterexample outside the factor domain

The point

\[
(M,s,\tau)=
\left(521,\frac{129}{1000},\frac{667}{5000}\right)
\]

was initially tempting because the algebraic \(J\)-value is negative.

However,

\[
h=260,\qquad b_\tau=257,\qquad b_\tau+2=259.
\]

The A84 adjacent-factor domain is

\[
2\le k\le h-2=258.
\]

Thus \(E_{b_\tau+2}\) is outside the declared adjacent-factor domain.

The point is not a valid counterexample and is explicitly rejected.

This correction is important: an algebraically evaluable expression is not
automatically an admissible object of the theorem being tested.

## 3. Coarse-grid success is not a theorem

The predeclared coarse grid gives

\[
192/192
\]

positive \(J\)-controls.

That result does not support universal positivity because the near-wall grid
contains exact negative controls.

Finite successes remain evidence only.

## 4. No fitted tau threshold

The coarse strong package happens to pass every declared control for
\(\tau\ge3/10\), while lower target values have failures.

No threshold at \(3/10\) is claimed.

That number is a feature of the finite grid and must not be promoted into a
hypothesis without an independent derivation.

## 5. Eventual positivity remains open

The structure of the exact cancellation suggests studying whether

\[
J_{\tau,b_\tau+1}>0
\]

is eventually true for each fixed interior pair or uniformly on compact
subsets of

\[
\beta<s<\tau<1.
\]

No proof is recorded in A115.

A future proof must control all residual channels uniformly and must not use
finite stress results as a premise.
