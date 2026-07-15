# A25 — Non-Circular q Couplings and Underdetermination

## Scale-free local family

For every source vertex `i`, standardize the outgoing q-values:

`z_ij = (q_ij - mean_i q) / sd_i q`.

For any strictly positive measurable function `f`, define

`K_f(i->j) = A_ij f(z_ij) / sum_k A_ik f(z_ik)`.

This family is local, relabel-equivariant, and invariant under every row-wise
positive affine transformation

`q_ij -> a_i q_ij + b_i`, with `a_i>0`.

Therefore it uses q-shape information without importing an absolute q unit.

## Underdetermination

The requirements above do not determine `f`. Distinct positive functions
generally give distinct transition probabilities on the same `(A,q)`.
There are infinitely many such functions, so symmetry and locality alone
cannot derive a unique physical coupling.

## Raw softmax

`K(i->j) proportional to exp(-q_ij)` is invariant under row shifts but not
under q rescaling. Its coefficient implicitly fixes a q unit, equivalently an
inverse scale beta.

## Centered dynamics

The update

`q_{t+1}=q_t-1/2 center(eta center(q_t)+noise_t)`

is equivariant under

`q->a q+c`, `noise->a noise`.

Thus q amplitude is fixed only relative to the chosen noise amplitude. A
numerical noise variance is a normalization postulate, not yet a physical
unit or observable calibration.

## Boundary

Scale-free couplings show that non-circular operational sensitivity to
relative q-shape is mathematically possible. They do not select a unique law
and cannot recover absolute q magnitude or physical length.
