# A21 — Equivariance of Endogenous Relational Dynamics

## Exact theorem

If the update state is measurable from the relational history and model-independent randomness, identical initial relations coupled with the same random tape produce identical complete trajectories by induction.

## Endogenous kernels

### history_reinforced — beta_skew
- Prefix identity: 1.0000
- Final identity: 1.0000
- Action identity: 1.0000

### principal_ideal — beta_skew
- Prefix identity: 1.0000
- Final identity: 1.0000
- Action identity: 1.0000

### random_downset — beta_skew
- Prefix identity: 1.0000
- Final identity: 1.0000
- Action identity: 1.0000

### two_ideal_union — beta_skew
- Prefix identity: 1.0000
- Final identity: 1.0000
- Action identity: 1.0000

### history_reinforced — power_anisotropic
- Prefix identity: 1.0000
- Final identity: 1.0000
- Action identity: 1.0000

### principal_ideal — power_anisotropic
- Prefix identity: 1.0000
- Final identity: 1.0000
- Action identity: 1.0000

### random_downset — power_anisotropic
- Prefix identity: 1.0000
- Final identity: 1.0000
- Action identity: 1.0000

### two_ideal_union — power_anisotropic
- Prefix identity: 1.0000
- Final identity: 1.0000
- Action identity: 1.0000

## Exogenous positive control

### beta_skew
- Trajectory divergence rate: 1.0000
- Final relation difference rate: 1.0000
- Median first divergence step: 2.00

### power_anisotropic
- Trajectory divergence rate: 1.0000
- Final relation difference rate: 1.0000
- Median first divergence step: 1.00

## Gates

- G1_initial_relations_identical: PASS
- G2_all_endogenous_prefixes_identical: PASS
- G3_all_endogenous_final_relations_identical: PASS
- G4_endogenous_path_and_action_hashes_identical: PASS
- G5_history_dependent_kernel_identical: PASS
- G6_all_generated_relations_transitive: PASS
- G7_exogenous_marks_change: PASS
- G8_exogenous_kernel_breaks_trajectory_identity: PASS
- G9_exogenous_divergence_occurs_early: PASS
- G10_equivariance_and_symmetry_breaking_theorems_proved: PASS
- G11_no_physical_dynamics_claimed: PASS

## Verdict

PASS_ENDOGENOUS_RELATIONAL_EQUIVARIANCE

## Boundary

The theorem identifies a no-go class and a necessary route around it. It does not establish that a physically justified non-invariant primitive exists in the pre-categorical theory.