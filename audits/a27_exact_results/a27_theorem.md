# A27 — Status of the Exponential Strength lambda

## Raw-score reparameterization

For `P_j(lambda,s) proportional to exp(-lambda s_j)` and `a>0`,

`P(lambda,s)=P(lambda/a, a s+b)`.

Thus lambda cannot be separated from an uncalibrated raw score scale.

## Standardized-score uniqueness

Let `z=(s-mean s)/sd(s)`. Positive affine transformations of `s` leave `z`
unchanged. Suppose `z` is nonconstant and `P_lambda=P_mu`. For two entries
with `z_j!=z_k`,

`exp[-lambda(z_j-z_k)] = exp[-mu(z_j-z_k)]`.

Therefore `lambda=mu`. Lambda is identifiable within the standardized-score
model and is not removable by the accepted affine q gauge.

## Stationary centered dynamics

For centered state `x_t`,

`x_{t+1}=a x_t - 1/2 P epsilon_t`,
`a=1-eta/2`,

where `P` is the centering projector. With iid noise variance `sigma^2`, the
stationary per-component variance is

`Var(x_i)= [sigma^2/4 * (1-1/d)] / (1-a^2)`.

Changing sigma rescales q but leaves row-standardized scores and their
transition probabilities unchanged. Stationary q variance therefore does not
fix lambda for the standardized kernel.

## Coarse-graining closure

For additive path scores `S_p`, each group has total weight

`W_B(lambda)=sum_{p in B}exp(-lambda S_p)`.

Defining

`F_B(lambda)=-(1/lambda)log W_B(lambda)`

gives `W_B=exp(-lambda F_B)` exactly. Closure holds for every lambda. The
effective score itself is lambda-dependent, so closure does not select a
unique strength.

## Empirical identifiability

Given observed standardized scores and multinomial transition counts, the
log-likelihood is strictly concave in lambda whenever some score row is
nonconstant. Lambda is then statistically identifiable and estimable.

## Constraint map

For `p_lambda(j) proportional to exp(-lambda z_j)`,

`d E_lambda[z]/d lambda = -Var_lambda(z) < 0`

for nonconstant z. A numerical expected-score constraint determines a unique
lambda, but the constraint must be supplied independently.
