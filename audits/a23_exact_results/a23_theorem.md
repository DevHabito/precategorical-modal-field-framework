# A23 — q-Field Primitive, Gauge, and Rate Audit

## Proposition 1: information criterion

If `q` is a measurable function of the order, its relational history, and
model-independent randomness, then the A21 equivariance theorem applies. It
cannot distinguish latent representatives that produce the same order.

A q-field can add information only if its conditional marked law is not
determined by that order and differs between the representatives.

## Proposition 2: global additive gauge

For every edge,

`ell_ij = exp(q_ij)`.

Under `q_ij -> q_ij + c`,

`ell_ij -> exp(c) ell_ij`.

Every directed path cost is multiplied by `exp(c)`. Minimization over paths
therefore commutes with the multiplication, so

`d_dir -> exp(c) d_dir`

and

`D_eff -> exp(c) D_eff`.

Any normalization homogeneous of degree one removes this factor. Centered q,
q differences, and normalized D_hat are gauge-invariant; absolute D_eff is
not.

## Proposition 3: centered dynamics is gauge-equivariant

For

`q_{t+1} = q_t - 1/2 center(eta center(q_t) + noise_t)`,

replace `q_t` by `q_t+c`. Centering removes `c`, so the update term is
unchanged and

`q'_{t+1} = q_{t+1}+c`.

The constant mode is neither damped nor selected. The dynamics evolves only
the quotient by the global shift.

## Proposition 4: rate-time degeneracy

The noiseless centered mode contracts per step by

`a = 1 - eta/2`.

If represented as a continuous exponential relaxation,

`a = exp(-lambda Delta_tau)`.

Only `lambda Delta_tau = -log(a)` is identified. Without an independently
calibrated `Delta_tau`, no physical rate `lambda` follows from eta alone.

## Boundary

These statements show that q may carry genuine relative information while
still failing to supply absolute scale. They do not establish whether the
actual RZS q has an independent operational measurement or physical unit.
