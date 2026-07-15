# A24 — Operational Origin of q

## Result

A local, gauge-invariant and relabel-equivariant transition kernel makes q contrasts operationally measurable. It does not identify absolute q or its magnitude independently of the coupling calibration.

## Aggregate results

- maximum_global_gauge_error: 3.3306690738754696e-16
- maximum_relabel_error: 2.220446049250313e-16
- maximum_locality_error: 0.0
- minimum_local_contrast_tv: 0.04865553089335149
- mean_contrast_recovery_rmse: 0.016176653807657194
- maximum_contrast_recovery_rmse: 0.022235511305922117
- gauge_inequivalent_path_divergence_rate: 1.0
- median_first_path_divergence: 1.0
- maximum_beta_q_degeneracy_error: 2.220446049250313e-16

## Gates

- G1_order_derived_q_redundant: PASS
- G2_uncoupled_q_empirically_silent: PASS
- G3_global_q_gauge_invariant: PASS
- G4_relabeling_equivariant: PASS
- G5_declared_locality_holds: PASS
- G6_local_q_contrast_changes_observable_law: FAIL
- G7_gauge_equivalent_paths_identical: PASS
- G8_gauge_inequivalent_paths_diverge: PASS
- G9_q_contrasts_recoverable_when_beta_known: PASS
- G10_beta_q_scale_degeneracy_exact: PASS
- G11_local_kernel_has_additional_row_offset_gauge: PASS
- G12_actual_rzs_operational_origin_not_assumed: PASS

## Verdict

FAIL_Q_OPERATIONALIZATION_CRITERIA_AUDIT

## Boundary

The audit supplies criteria and a mathematical witness, not the missing physical bridge. The actual RZS q remains operationally ungrounded until its preparation, measurement, noise law, and coupling to observable events are specified independently of the desired emergent geometry.