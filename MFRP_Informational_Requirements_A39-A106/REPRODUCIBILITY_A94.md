# Reproducibility — A94

Run from the repository root:

```bash
python audits/a94_exact_all_cell_continuum_one_variation_audit.py
python tools/generate_a94_figure.py
```

A94 reads the committed A92 exact algebraic-cell catalogue and the A84 exact evaluator. It regenerates all non-decisive seven-term adjacent factors with `fractions.Fraction` arithmetic.

The first certificate is a rational monotone-monomial outer-hull enclosure. Factors not resolved by that enclosure are handled by adaptive rational interval subdivision. Opposite endpoint signs are certified by a signed derivative; twelve residual cases use a positive second derivative, exact endpoint signs, and a locally signed derivative on the isolated root bracket.

All worker outputs are sorted before JSON serialization. No floating-point value decides a gate. Decimal root midpoints and plotted coordinates are presentation-only.

The theorem covers the 858 A92 cells in the declared finite contract. It does not certify lifted KKT feasibility or any physical interpretation.
