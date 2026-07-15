# A19 — Ensemble-Level Copula Identifiability Theorem

## Assumptions

Let `(X_i,Y_i)`, `i=1,...,n`, be iid. Assume both marginal CDFs are
continuous and strictly increasing on their supports. Define the labeled
strict order

`i <_P j` iff `X_i < X_j` and `Y_i < Y_j`.

## Theorem

The probability law of `P` depends on the joint distribution of `(X,Y)` only
through its copula.

## Proof

Let `U_i=F_X(X_i)` and `V_i=F_Y(Y_i)`. Strict monotonicity gives, almost
surely,

`X_i<X_j` iff `U_i<U_j`, and `Y_i<Y_j` iff `V_i<V_j`.

Therefore the full labeled relation matrix constructed from `(X_i,Y_i)` is
identical, under this coupling, to the relation matrix constructed from
`(U_i,V_i)`. By Sklar's representation, `(U_i,V_i)` has uniform marginals
and the same copula as `(X_i,Y_i)`. Hence the induced order law is a
functional only of the copula.

## Infinite-ensemble corollary

Take two models with the same copula but different continuous strictly
increasing marginals. Their law for one observed finite order is identical.
The product law for any finite number of independent observed orders is
therefore identical. The law for an infinite iid sequence is also identical
on all cylinder events.

Consequently, no estimator or statistical test whose data consist only of
those orders and their cardinalities can consistently identify which
marginal model generated the sequence.

## Independence corollary

For the independence copula, sort the sample by the first coordinate.
The ranks of the second coordinates are independent of that sorting and form
a uniform random permutation. Thus every permutation in `S_n` has probability
exactly `1/n!`.

## Limitation

The theorem proves that the order law depends at most on the copula. It does
not prove that distinct copulas always induce distinct laws of finite orders.
