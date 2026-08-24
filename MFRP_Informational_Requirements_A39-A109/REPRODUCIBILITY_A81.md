# A81 Reproducibility Contract

A81 is exact and self-contained relative to the committed A78/A80 results.

- All coefficients are SymPy rational numbers.
- The reduced boundary formulas are assembled coefficient-by-coefficient; no floating-point fitting is used.
- The 142 A80 boundary polynomials are compared as exact primitive integer polynomials.
- Positivity of `T(s)` and `Delta(s)` is certified by dependency-safe monomial interval enclosure on the positive rational interval `[129/1000,133/1000]`.
- Selected-contact derivative positivity is certified by the same exact interval method.
- Endpoint root classes use exact rational signs.
- Decimal approximations are not used by any gate.

The analytic formulas hold under the declared support and band equations. The positivity theorem remains finite: `10 <= M <= 80`, `2 <= k < floor(M/2)`, and the stated local interval in `s`.
