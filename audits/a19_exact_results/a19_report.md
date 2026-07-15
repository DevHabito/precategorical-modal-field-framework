# A19 — Ensemble-Level Copula Identifiability Theorem

## Exact result

The finite-order law depends on continuous marginals only through their copula. Models with the same copula and different marginals therefore induce identical laws for any finite or infinite iid sequence of observed orders.

## Numerical audit

- Canonical order size: 6; categories: 720.
- Independent ensemble size per copula/marginal: 100000.
- Coupled relation identity rate: 1.0000.
- Minimum same-copula homogeneity p-value: 0.21919.
- Maximum same-copula total variation: 0.048850.
- Minimum different-copula total variation: 0.485500.

## Gates

- G1_coupled_relations_and_hashes_identical: PASS
- G2_independence_permutation_uniformity: PASS
- G3_same_copula_homogeneity_tests: PASS
- G4_same_copula_total_variation_small: PASS
- G5_same_copula_ordering_fraction_stable: PASS
- G6_gaussian_ordering_fraction_matches_theory: PASS
- G7_different_copula_total_variation_large: PASS
- G8_different_copula_controls_rejected: PASS
- G9_infinite_ensemble_nonidentifiability_proved: PASS
- G10_no_claim_of_copula_injectivity: PASS

## Verdict

PASS_ENSEMBLE_COPULA_IDENTIFIABILITY_LIMIT

## Boundary

The theorem establishes marginal non-identifiability. It does not establish that the full copula is uniquely recoverable from order ensembles; distinct copulas may still share some or all finite-order probabilities.