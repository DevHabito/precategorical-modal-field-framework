# Reproducibility A92

## Contract

- Python 3.13 or compatible modern Python 3
- SymPy is required only because A92 independently imports the committed A84 evaluator for exact regression checks
- all A92 theorem decisions use `fractions.Fraction` arithmetic and exact integer comparisons
- no floating-point value decides a gate
- Matplotlib is required only for the deterministic figure

## Execute

```bash
python audits/a92_exact_continuum_offset_three_window_audit.py
```

Required committed input:

- `audits/a84_k_space_exponential_polynomial_stress_audit.py`

Outputs:

- `results/a92_continuum_offset_three_window_results.json`
- `results/a92_continuum_offset_three_window_catalogue.json`

The audit reconstructs each decisive adjacent factor as a sparse rational polynomial, brackets every algebraic `b`-cell boundary by exact integer comparison, and certifies signs with adaptive rational interval arithmetic. The eleven internal roots are isolated by exact bisection after a positive-derivative certificate.

## Figure

```bash
python tools/generate_a92_figure.py
```

Output:

- `figures/a92_continuum_offset_three_windows.png`
