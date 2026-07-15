# A26 — Kernel Selection Principles

## IIA theorem

For any strictly positive pointwise weight `f`,

`P(j|S)=f(z_j)/sum_{k in S}f(z_k)`.

Therefore

`P(j|S)/P(k|S)=f(z_j)/f(z_k)`,

which is independent of all alternatives other than `j,k`. IIA admits every
positive pointwise `f` and does not select the exponential.

## Detailed-balance theorem

On an undirected graph with symmetric score `s_ij=s_ji`, set
`w_ij=f(s_ij)=w_ji` and `P_ij=w_ij/sum_k w_ik`. Then

`pi_i = sum_k w_ik / sum_{a,b} w_ab`

satisfies `pi_i P_ij = pi_j P_ji`. Every positive `f` is reversible.

## Aggregation theorem

For a block `B`, its direct probability is

`sum_{j in B}f(z_j)/sum_k f(z_k)`.

Representing the block by its total weight `W_B=sum_{j in B}f(z_j)` reproduces
that probability exactly for every positive `f`.

## Exponential-family uniqueness theorem

Assume the odds ratio depends only on score difference:

`f(x)/f(y)=g(x-y)`,

with positive continuous `f`. Setting `y=0` and comparing three scores gives

`g(a+b)=g(a)g(b)`.

The continuous positive solutions are `g(t)=exp(-lambda t)`, so

`f(z)=C exp(-lambda z)`.

This selects the exponential family. It does not fix `lambda`.

## Maximum-entropy theorem

Maximize `H(p)=-sum_j p_j log p_j` subject to

`sum_j p_j=1`,
`sum_j p_j z_j=m`.

The Lagrange stationary condition gives

`p_j proportional to exp(-lambda z_j)`.

Strict concavity makes this the unique maximizer for an interior feasible
constraint. The multiplier `lambda` is determined by the specified value
`m`. Without a law fixing `m`, maximum entropy does not choose a unique
kernel strength.

## Boundary

The exponential family has rigorous axiomatic support. A unique physical
transition law still requires an independently justified score, constraint,
and value of `lambda`.
