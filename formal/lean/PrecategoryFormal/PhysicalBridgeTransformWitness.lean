import Mathlib

namespace PrecategoryFormal.PhysicalBridge

/--
Exact rational four-state witness used by the multi-electron transform bridge.

The two distributions have the same normalization, the same mean state,
and the same transform at z = 1/2, but different transforms at y = 3/4.

This theorem is purely algebraic. It does not formalize the experimental
master equation, stochastic thermodynamics, or any empirical claim.
-/
theorem four_state_transform_nonclosure_witness :
    ((9 : ℚ) / 40 + 7 / 20 + 1 / 8 + 3 / 10 = 1) ∧
    ((11 : ℚ) / 40 + 3 / 20 + 3 / 8 + 1 / 5 = 1) ∧
    ((7 : ℚ) / 20 + 2 * (1 / 8) + 3 * (3 / 10) = 3 / 2) ∧
    ((3 : ℚ) / 20 + 2 * (3 / 8) + 3 * (1 / 5) = 3 / 2) ∧
    ((9 : ℚ) / 40
        + (7 / 20) * ((1 : ℚ) / 2)
        + (1 / 8) * (((1 : ℚ) / 2) ^ 2)
        + (3 / 10) * (((1 : ℚ) / 2) ^ 3)
      = 15 / 32) ∧
    ((11 : ℚ) / 40
        + (3 / 20) * ((1 : ℚ) / 2)
        + (3 / 8) * (((1 : ℚ) / 2) ^ 2)
        + (1 / 5) * (((1 : ℚ) / 2) ^ 3)
      = 15 / 32) ∧
    ((9 : ℚ) / 40
        + (7 / 20) * ((3 : ℚ) / 4)
        + (1 / 8) * (((3 : ℚ) / 4) ^ 2)
        + (3 / 10) * (((3 : ℚ) / 4) ^ 3)
      = 219 / 320) ∧
    ((11 : ℚ) / 40
        + (3 / 20) * ((3 : ℚ) / 4)
        + (3 / 8) * (((3 : ℚ) / 4) ^ 2)
        + (1 / 5) * (((3 : ℚ) / 4) ^ 3)
      = 437 / 640) ∧
    ((219 : ℚ) / 320 ≠ 437 / 640) := by
  norm_num

/--
The exact shifted-transform separation in the rational witness is 1/640.
-/
theorem four_state_shifted_transform_gap :
    (219 : ℚ) / 320 - 437 / 640 = 1 / 640 := by
  norm_num

end PrecategoryFormal.PhysicalBridge
