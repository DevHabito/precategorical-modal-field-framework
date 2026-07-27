# A87 Reproducibility

A87 uses exact Python `Fraction` arithmetic for every factor, local secant drop, normalized residual, threshold comparison, class assignment, and monotonicity census.

Run:

```bash
python audits/a87_exact_secant_offset_classifier_audit.py
```

The script reads:

- `results/a84_k_space_exponential_polynomial_stress_results.json`;
- `results/a85_parity_dominant_balance_contact_localization_results.json`;
- `results/a86_exact_rational_contact_strip_catalogue.json`.

It writes two deterministic JSON files. Decimal strings are generated only for readable presentation and are never used in a gate.

The theorem is finite to `10<=M<=300` and the three rational probes. The positive local secant is not a global monotonicity claim; the audit explicitly records 40,483 global monotonicity failures.
