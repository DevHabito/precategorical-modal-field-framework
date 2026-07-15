# A33 — Projective Branch Fractions

## Main result

Regrouping invariance selects ratios of additive subtree weights. It does not select terminal weights, mu, q, or lambda.

### base_mass
- Median tree TV: 0.000000
- Median target TV: 0.000000

### descendant_count
- Median tree TV: 0.000000
- Median target TV: 0.000000

### mass_times_exp_mean_q
- Median tree TV: 0.247081
- Median target TV: 0.137109

### mean_q_softmax
- Median tree TV: 0.729150
- Median target TV: 0.450846

### partition_sum
- Median tree TV: 0.000000
- Median target TV: 0.000000

### uniform_child
- Median tree TV: 0.618056
- Median target TV: 0.335648

## Gates

- G1_projective_ratio_theorem_proved: PASS
- G2_uniform_child_rule_fails_regrouping: PASS
- G3_descendant_count_rule_exact_for_uniform_leaves: PASS
- G4_base_mass_rule_exact_for_supplied_mu: PASS
- G5_naive_mean_q_softmax_fails_regrouping: PASS
- G6_mass_times_exp_mean_q_fails_regrouping: PASS
- G7_partition_sum_q_rule_exact_and_projective: PASS
- G8_q_weighted_rules_global_shift_invariant: PASS
- G9_partition_sum_message_associative: PASS
- G10_maxent_leaf_solution_factorizes_exactly: PASS
- G11_projectivity_does_not_select_terminal_weights: PASS
- G12_no_mu_lambda_or_physical_split_law_claimed: PASS

## Verdict

PASS_PROJECTIVE_RATIO_LAW_WITH_TERMINAL_WEIGHT_UNDERDETERMINATION

## Boundary

A33 establishes conditional consistency requirements and rejects grouping-dependent shortcuts. It does not derive physical branching probabilities.