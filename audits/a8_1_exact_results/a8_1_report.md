# A8.1 — Condensation-Code Resolution

## Verdict

PASS_FORMAL_RESOLUTION_5234_REPRESENTATIVE_CODES_6942_FULL_LABELED_PREORDERS

## Exact result

- Full labeled condensation preorders: **6,942**
- Minimum-representative quotient-poset codes: **5,234**
- Fully unlabeled condensation preorders: **139**
- Difference caused by collapsed SCC memberships: **1,708**

## Formal diagnosis

The original A8 implementation stored SCC minima and the order between those minima, but not the full SCC membership partition. It therefore counted a valid intermediate quotient code rather than the complete labeled condensation preorder.

## Edge-flip check

- Changed pairs under representative code: 6,144,000
- Changed pairs under full code: 6,144,000
- Full-only discrepancies: 0
- Representative-only discrepancies: 0
- Exact fraction under both encodings: **75/256**

## Required manuscript correction

Replace the claim “5,234 distinct labeled condensation-poset codes” by two explicitly defined counts. The full labeled count is 6,942; 5,234 is retained only as the count of minimum-representative quotient-poset codes.

## Gates

- G1_exhaustive_full_code_count_is_6942: PASS
- G2_exhaustive_representative_code_count_is_5234: PASS
- G3_independent_full_combinatorial_formula_is_6942: PASS
- G4_independent_representative_formula_is_5234: PASS
- G5_labeled_poset_counts_reproduced: PASS
- G6_unlabeled_full_preorder_count_is_139: PASS
- G7_explicit_collision_proves_original_code_noninjective: PASS
- G8_code_fiber_accounting_exact: PASS
- G9_edge_flip_fraction_same_under_both_codes: PASS
- G10_no_full_labeled_claim_retained_for_5234: PASS