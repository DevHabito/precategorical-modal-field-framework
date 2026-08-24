# A80 Reproducibility Contract

A80 uses exact rational and symbolic arithmetic through SymPy.

- Boundary polynomials are primitive integer Cramer numerators.
- Root existence and uniqueness on the local interval follow from exact endpoint signs and an exact positive derivative enclosure.
- Roots are enclosed by 80 exact rational bisection steps.
- All non-boundary KKT rational functions are certified positive using exact Horner interval enclosures for numerator and denominator.
- Every interval is independently checked at an exact rational midpoint through the A78 KKT evaluator.
- Floating-point values are used only for display in tables and figures.

The result is finite and contract-relative: `10 <= M <= 80`, A78-selected contacts, and `129/1000 <= s <= 133/1000`.
