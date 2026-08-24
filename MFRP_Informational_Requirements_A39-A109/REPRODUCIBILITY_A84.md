# Reproducibility A84

A84 uses Python exact `Fraction` arithmetic for all finite sign decisions and SymPy only for one generic symbolic expansion identity.

Scope:

- `10 <= M <= 300`;
- `2 <= k < floor(M/2)-1`;
- exact probes `129/1000`, `131/1000`, and `133/1000`;
- `beta=1/8`, `target=1/2`, and the inherited parity-normalized error contract.

The audit evaluates 21,607 adjacent pairs at three probes, for 64,821 exact signs. No floating-point value decides a gate.

Endpoint sign disagreement is recorded only as an existence witness for at least one interior root. A84 does not perform a complete root count beyond the A83 range.
