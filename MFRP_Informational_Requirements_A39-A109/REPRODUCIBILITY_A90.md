# Reproducibility A90

## Contract

- Python 3.13 or compatible Python 3.x
- SymPy is required because A90 imports the A84 coefficient helper module
- all A90 sign gates themselves use `fractions.Fraction` and Python integers
- Matplotlib only for the deterministic figure

## Execute

```bash
python audits/a90_prethreshold_all_k_one_variation_audit.py
```

Outputs:

- `results/a90_prethreshold_all_k_one_variation_results.json`
- `results/a90_prethreshold_contact_sequence_catalogue.json`

All sign gates are exact. The audit clears rational denominators and evaluates integer exponential sums. No floating-point number decides a factor sign.

## Figure

```bash
python tools/generate_a90_figure.py
```

Output:

- `figures/a90_exact_prethreshold_contact_offsets.png`
