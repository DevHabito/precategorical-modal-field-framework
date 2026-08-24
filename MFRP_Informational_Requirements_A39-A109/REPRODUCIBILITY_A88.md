# Reproducibility A88

## Contract

- Python 3.13 or compatible Python 3.x
- standard library `fractions.Fraction`
- SymPy for one symbolic identity gate
- Matplotlib only for the deterministic figure

## Execute

```bash
python audits/a88_nine_term_secant_positivity_audit.py
```

Outputs:

- `results/a88_nine_term_secant_positivity_results.json`
- `results/a88_nine_term_secant_positivity_catalogue.json`

The theorem gates use exact integer/Fraction arithmetic. Decimal strings in the result file are display fields only.

## Figure

```bash
python tools/generate_a88_figure.py
```

Output:

- `figures/a88_exact_local_secant_core_dominance.png`
