# Reproducibility A89

## Contract

- Python 3.13 or compatible Python 3.x
- standard library only for the audit (`fractions.Fraction`, integer arithmetic, JSON)
- Matplotlib only for the deterministic figure

## Execute

```bash
python audits/a89_uniform_secant_threshold_audit.py
```

Outputs:

- `results/a89_uniform_secant_threshold_results.json`
- `results/a89_uniform_secant_threshold_catalogue.json`

All theorem gates are exact. Decimal fields are presentation-only renderings of stored rational numbers.

## Figure

```bash
python tools/generate_a89_figure.py
```

Output:

- `figures/a89_uniform_secant_threshold_budget.png`
