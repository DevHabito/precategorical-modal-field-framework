# From the finite primal constraints to the A115 moment-adjusted basis

**Research note, 6 November 2026**  
**Scope:** one precise bridge from the original finite optimization problem to its reduced algebra. This is not a completed KKT derivation of `E_{M,k}`.

## Why this step matters

The previous Lean audit checked the ten-channel identity after the cofactor factor `E` had already been defined. That leaves an important question unanswered: why is the particular moment-adjusted function `B_{M,k}(r)` present in the first place?

Here I go back to the actual scaled weights. Let the finite support be `X_M = {0,...,M}`. The original problem has nonnegative scaled weights `p_x,q_x` with a common mass `t` and prescribed mean `M/2`. The Q transform is fixed to 1 at the target node `tau`, and the scaled P transform at the same node is the objective. The [existing A110–A114 literature-positioning note](../novelty/A110_A114_LITERATURE_POSITIONING_AND_NOVELTY_MAP_20260914.md) gives this normalization.

No claim of originality is attached to the ratio-to-LP reformulation; Charnes and Cooper's 1962 linear-fractional transformation is relevant prior art.

## 1. Recovering the transform ratio

Put `p_x=t*mu_x` and `q_x=t*nu_x`. For every finite support and every real target `tau`,

```
sum_x p_x*tau^x = t * sum_x mu_x*tau^x
sum_x q_x*tau^x = t * sum_x nu_x*tau^x.
```

With the original target normalization `sum_x q_x*tau^x=1`, the Q transform cannot vanish. Hence

```
t = 1 / G_nu(tau)
sum_x p_x*tau^x = G_mu(tau) / G_nu(tau).
```

This is an **algebraic equivalence**, not an optimality certificate. The Lean theorem does not need to assume `t>0` or probability normalization to prove the equality; interpreting `mu,nu` as probability laws does require nonnegative weights, unit mass, and `t>0`. Those are logically separate assumptions.

## 2. Deriving B from a genuine three-point P support

Now consider a P measure with possible nonzero scaled masses only at `0,k,M`, with `0<k<M`. Let `z=p_k`. The mass and mean constraints are:

```
p_0 + z + p_M = t
k*z + M*p_M = M*t/2.
```

Solving them gives

```
p_M = t/2 - (k/M)*z
p_0 = t/2 - ((M-k)/M)*z.
```

Therefore its transform is

```
p_0 + z*r^k + p_M*r^M
 = t*(1+r^M)/2 + z*B_(M,k)(r),
```

where

```
B_(M,k)(r) = r^k - (M-k)/M - (k/M)*r^M.
```

This is the direct mathematical origin of the moment-adjusted basis. Its adjacent difference is the already Lean-checked identity

```
B_(M,k+1)(r)-B_(M,k)(r)
  = (r-1)*r^k + (1-r^M)/M.
```

There is no appeal to a numerical fit, interpolation guess, or cofactor ansatz in this derivation.

## 3. Formal proof boundary

New module:
[`formal/lean/PrecategoryFormal/TargetPrimalBridge.lean`](../../formal/lean/PrecategoryFormal/TargetPrimalBridge.lean).

It defines a finite transform over `Fin(M+1)` and states:

- `transform_scale`: exact scaling under `p_x=t*mu_x`;
- `target_ratio_from_scaled_primal`: target normalization forces a nonzero Q denominator and gives the transform ratio;
- `endpoint_mass_identity`: the proposed three-site weights sum to `t`;
- `endpoint_mean_identity`: their first moment is `M*t/2`;
- `three_site_transform_basis`: the finite P transform decomposes into baseline + `z*B`.

The module is imported by `PrecategoryFormal.lean` and included as a dedicated `leanchecker` target. The first submission is commit `44ae36385e15af4fec3a534a7bb1fb9abd0359aa`, tracked by [Lean CI run 42320051698](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42320051698). Its build and kernel status must be read before claiming formal success.

## 4. Independent rational controls

The script [`audits/a115_independent_three_site_primal_bridge_20261106.py`](../../audits/a115_independent_three_site_primal_bridge_20261106.py) checks the normalization, mean, transform decomposition, and nonnegative-mass interval on a finite deterministic rational grid. A separate set checks that scaling the P and Q masses gives the same transform ratio as the unscaled measures. The script uses `fractions.Fraction` for every comparison.

Its inclusion in [the exact audit workflow](../../.github/workflows/a115-a122-exact-audits.yml) means that a clean GitHub runner checks the code from the published repository. The run status and counts must be taken from its actual log, not assumed.

## 5. What remains open

The three-site construction is for the P support and must not be confused with the Q block `{1,h,h+1}`, whose separate nonnegativity conditions have already been certified.

The source has not yet been shown in Lean to imply the specific determinant/cofactor combination

```
E_(M,k) = X*DeltaB_s + Y*B_s + W*H_s.
```

To close that gap, the next formal file must include the active transform-band equalities, the second measure, the precise orientation of the reduced objective, and the determinant/dual sign relation. It must then establish why `E` has that expression rather than merely defining `E` that way.

This is a concrete prerequisite for any end-to-end certification of A116–A122. The new results here are elementary algebraic components; mathematical priority is **not claimed**.

## 6. Necessity and determinant orientation — new proof obligations

The first formal file built successfully on [run 42320048684](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42320048684), at the revision before the converse was appended. A separate commit `754880ef3ef0034716e78f0fe8a93604324a10f2` adds `endpoints_forced_by_primal_equations` and `three_site_transform_from_primal_equations`: unlike the previous constructed endpoint weights, these theorems begin with **arbitrary** real endpoint masses satisfying the two primal equations and aim to show that the A115 moment-adjusted basis is forced. Track the build and replay on [run 42320382810](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42320382810). **Do not call these new converse lemmas kernel-certified until that revision passes.**

A second algebraic observation fixes the determinant orientation of the previously certified cofactor:

```text
E = det [ [B_beta,      B_tau,      B_s],
          [H_beta,      A,          H_s],
          [DeltaB_beta, DeltaB_tau, DeltaB_s] ].
```

This expansion is consistent with the previously proved `X DeltaB_s + Y B_s + W H_s`; the row order matters because a swap reverses the determinant sign. The native `Matrix.det` statement was appended to `TargetFactorTenChannel.lean` at commit `1a6d5a4151b13bb4f23ddab6b3c23696f5d813e9`, with [Lean run 42320523915](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42320523915) as the corresponding independent build/kernel gate.

Even when these calculations are checked, neither shows the sign of the determinant or proves that its sign selects a globally optimal LP architecture. That conclusion requires the *actual* active constraint matrix, the dual objective direction, and nonnegative primal/dual multipliers. This distinction is preserved deliberately.

## 7. First primal bridge fully kernel-replayed

GitHub Actions [run 42320051698](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42320051698), at source commit `44ae36385e15af4fec3a534a7bb1fb9abd0359aa`, has now reported **20/20 jobs SUCCESS**, including the dedicated `leanchecker (PrecategoryFormal.TargetPrimalBridge)` job. This verifies the first version: scaling the finite transform, the target ratio under a normalization, the constructed endpoint masses, and the identity producing `B_{M,k}`.

The later **necessity** lemma and native `Matrix.det` lemma were committed after that run; their CI status is separate and must not be inferred from the earlier 20/20 PASS.
