# A25 — Non-Circular q Couplings and Law Underdetermination

## Result

Scale-free local q-shape couplings exist and satisfy the required symmetries without an external q unit. The same requirements admit multiple observationally distinct kernels, so no unique physical law is derived.

## Kernel summaries

### raw_softmax
- Maximum row-affine error: 0.550599
- Median global-scale TV: 0.231401
- Minimum shape sensitivity TV: 0.089020

### standardized_asinh
- Maximum row-affine error: 9.4369e-16
- Median global-scale TV: 0.000000
- Minimum shape sensitivity TV: 0.114581

### standardized_exponential
- Maximum row-affine error: 9.4369e-16
- Median global-scale TV: 0.000000
- Minimum shape sensitivity TV: 0.131631

### standardized_rank
- Maximum row-affine error: 0
- Median global-scale TV: 0.000000
- Minimum shape sensitivity TV: 0.048091

## Gates

- G1_scale_free_family_theorem_proved: PASS
- G2_scale_free_kernels_row_affine_invariant: PASS
- G3_all_kernels_relabel_equivariant: PASS
- G4_all_kernels_declared_local: PASS
- G5_scale_free_kernels_sensitive_to_q_shape: PASS
- G6_raw_softmax_exposes_hidden_q_normalization: PASS
- G7_scale_free_kernels_ignore_global_q_rescaling: PASS
- G8_admissible_kernel_family_is_observationally_nonunique: PASS
- G9_centered_q_dynamics_reparameterization_exact: PASS
- G10_noise_scale_is_normalization_not_physical_unit: PASS
- G11_no_unique_or_physical_coupling_claimed: PASS

## Verdict

PASS_NONCIRCULAR_Q_COUPLING_WITH_LAW_UNDERDETERMINATION

## Boundary

A25 establishes structural admissibility and exact underdetermination. It does not derive a matter coupling, transition law, physical q unit, absolute length, energy, temperature, or time scale.