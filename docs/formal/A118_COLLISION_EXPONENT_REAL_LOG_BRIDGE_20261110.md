# Collision exponent and log remainder — formal integration gate

**Recorded:** 10 November 2026. **Scope:** reduced source A115/A118 collision scaling.
**Status:** exact algebra independently verified with SymPy; new Lean module submitted and awaiting individual kernel replay.

The collision exponent (L=(-1/(2x)+b)\log(1+2\alpha x)) is related *exactly* to its announced first two coefficients (A=\alpha^2+2b\alpha), (B=-4\alpha^3/3-2b\alpha^2) by

[
L+\alpha-Ax-Bx^2 =
(-1/(2x)+b)
[\log(1+z)-(z-z^2/2+z^3/3)]
+\frac83 b\alpha^3 x^3,\quad z=2\alpha x.
]

The lemma `exact_collision_exponent_decomposition` proves this identity with a genuine (x\ne0) precondition, not an informal expansion. Its algebraic difference was independently checked to be exactly zero with SymPy.

`collision_log_remainder_enclosure` instantiates the new real Mathlib-based logarithm remainder certificate on (0\le x\le10^{-3}), (0\le\alpha\le45). It proves the bounds on the variable (z) in Lean, rather than assuming the interval condition.

The module is a source-to-logarithm **bridge**, not the final (41\cdot10^6 x^3) log exponent inequality, not the exponential Taylor remainder, and not the complete (O(M^{-3})) result. These further inequalities and all uniform finite-power channel estimates still require Lean proofs.
