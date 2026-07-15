# A34 — Effective Score and Dynamic Closure

## Main result

The log-partition effective score is exactly associative when carried with mass, but a single fixed-lambda scalar is not dynamically closed under the centered contraction.

## Aggregate results

- maximum_associativity_error: 7.105427357601002e-14
- maximum_shift_covariance_error: 8.881784197001252e-16
- maximum_affine_identity_error: 2.6645352591003757e-15
- maximum_same_moment_qeff_difference: 0.24258661624883915
- minimum_matched_mean_qeff_future_difference: 0.00705928847080739
- maximum_curve_closure_error: 5.551115123125783e-17
- median_scalar_loss_future_difference: 0.21753205000724668

## Gates

- G1_associative_mass_score_aggregation_exact: PASS
- G2_global_q_shift_covariance_exact: PASS
- G3_affine_rescaling_identity_exact: PASS
- G4_mean_and_variance_do_not_determine_effective_score: PASS
- G5_same_mean_and_qeff_can_have_different_future: PASS
- G6_whole_partition_curve_closes_centered_contraction: PASS
- G7_scalar_qeff_alone_not_dynamically_closed: PASS
- G8_cumulant_expansion_improves_with_added_terms_at_small_lambda: PASS
- G9_static_projectivity_not_promoted_to_dynamic_closure: PASS
- G10_no_physical_free_energy_or_thermodynamic_claim: PASS

## Verdict

PASS_STATIC_EFFECTIVE_SCORE_WITH_DYNAMIC_CLOSURE_OBSTRUCTION

## Boundary

A34 establishes a static sufficient message and a dynamic no-go. It does not identify Q_eff as physical free energy, prove thermodynamics, or establish a closed RZS macrodynamics.