# A79 Reproducibility and Claim Boundary

A79 reconstructs every certificate from the declared central-mean LP contract. It does not consume pre-fitted boundary values.

## Exact layers

1. The compressed branches are built symbolically in `s`.
2. Boundary polynomials are normalized to primitive integer form.
3. Each boundary root is isolated by an exact rational interval and certified simple.
4. Every KKT numerator and denominator is checked for roots on the enclosing rational hull.
5. Entering-atom Cramer numerators are independently constructed from determinant replacement and compared exactly.
6. Adjacent branches are evaluated at exact rational witnesses using the full KKT system.

## Non-proof layers

Decimal root and alpha values are presentation only. They are not used for gates.

## Claim boundary

The theorem is exact only for `M=40,57,74` under the frozen support, mean, target, channel, and error contracts. It does not establish an all-support recurrence, periodicity, a complete global phase atlas, or a physical interpretation.
