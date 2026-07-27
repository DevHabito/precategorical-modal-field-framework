# Reproducibility A91

## Contract

- Python 3.13 or compatible modern Python 3
- SymPy is required because A91 imports the A84 coefficient helper module
- mpmath is required only for the explicitly non-exact parity-locator diagnostic
- all A91 theorem gates use `fractions.Fraction` arithmetic
- Matplotlib is used only for the deterministic figure

## Execute

```bash
python audits/a91_exact_four_term_offset_three_mechanism_audit.py
```

Required committed inputs:

- `audits/a84_k_space_exponential_polynomial_stress_audit.py`
- `results/a90_prethreshold_all_k_one_variation_results.json`
- `results/a90_prethreshold_contact_sequence_catalogue.json`

Outputs:

- `results/a91_four_term_offset_three_results.json`
- `results/a91_four_term_offset_three_catalogue.json`

The exact theorem layer verifies the four-core normalization identity, full/core sign equality, strict residual dominance, and the offset-three classification in exact rational arithmetic. The A85 parity-corrected screen is clearly separated and reported as a 120-digit numerical diagnostic.

## Figure

```bash
python tools/generate_a91_figure.py
```

Output:

- `figures/a91_offset_three_screen_and_exact_cases.png`
