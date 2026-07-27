# Reproducibility — A95

A95 reads the committed A94 phase-cell catalogue and reuses the exact A78 full-KKT evaluators.

For each fixed A94 phase it chooses one low-denominator rational strictly inside the exact open cell. For each transition it chooses one witness on each open side of the isolated root. The witness-selection rule is deterministic.

At every witness, A95 tests:

- `P={0,j,M}`, gamma inactive;
- `P={0,j-1,j,M}`, gamma minus;
- `P={0,j,j+1,M}`, gamma plus;

against the complete finite LP KKT system. No floating-point quantity decides a status.

The exhaustive prefix certificate checks every F2/F3 contact candidate at each obstruction witness through the first A90 offset-three support `M=325`.

Run:

```bash
python audits/a95_rational_witness_lift_obstruction_audit.py --workers 16
```

The script sorts all worker outputs before JSON serialization. Exact decimal renderings, if shown in figures, are presentation-only.

The result is pointwise at rational witnesses. It is not a continuum lifted-KKT theorem and does not identify a physical interpretation.
