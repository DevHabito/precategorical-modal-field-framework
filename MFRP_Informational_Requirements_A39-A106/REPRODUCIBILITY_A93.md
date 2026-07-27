# Reproducibility — A93

Run from the repository root:

```bash
python audits/a93_exact_continuum_global_one_variation_audit.py
python tools/generate_a93_figure.py
```

A93 reads the committed A92 exact cell/root catalogue and the A84 exact evaluator. It recomputes every non-decisive seven-term adjacent factor with `fractions.Fraction` arithmetic and certifies its sign on a rational outer hull containing the exact algebraic cell.

The audit uses up to eight worker processes. Results are sorted before serialization, so the JSON output is deterministic. Set the operating-system CPU affinity externally if fewer workers are desired.

No floating-point value decides a gate. Decimal margins and root midpoints are presentation-only. The theorem is restricted to the twenty-five A92 selected cells, `10<=M<=520`, and `129/1000<=s<=133/1000`.
