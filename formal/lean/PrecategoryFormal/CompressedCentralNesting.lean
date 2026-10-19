import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
C3: elementary order-theoretic implications of the frozen A113
central nesting hypothesis.

These lemmas do not prove the A113 uniform positivity bound itself.
They isolate exactly what follows from E_(b+1) - 2 * E_(b+2) > 0,
so the false stronger second-secant inequality is never imported.
-/

/-- Nonnegative right increment forces a strictly positive left increment. -/
theorem centralLeftPositiveOfRightNonnegative
    (left right : ℝ)
    (nesting : 0 < left - 2 * right)
    (rightNonnegative : 0 ≤ right) :
    0 < left := by
  linarith

/-- A nonpositive left increment forces a strictly negative right increment. -/
theorem centralRightNegativeOfLeftNonpositive
    (left right : ℝ)
    (nesting : 0 < left - 2 * right)
    (leftNonpositive : left ≤ 0) :
    right < 0 := by
  linarith

/-- The two central increments cannot change from negative to positive. -/
theorem centralNestingForbidsNegativeToPositive
    (left right : ℝ)
    (nesting : 0 < left - 2 * right) :
    ¬(left < 0 ∧ 0 < right) := by
  intro reversal
  linarith [reversal.1, reversal.2]

/--
No strict local minimum can occur at the middle of three consecutive
compressed objective values when the A113 nesting margin is positive.
-/
theorem centralObjectiveHasNoStrictValley
    (first middle last : ℝ)
    (nesting : 0 < (middle - first) - 2 * (last - middle)) :
    ¬(middle < first ∧ middle < last) := by
  intro valley
  linarith [valley.1, valley.2]

/--
A113 nesting does not imply positivity of the stronger second secant.
This explicit rational arithmetic witness keeps the rejected statement
visible without modifying the A113 analytic certificate.
-/
theorem positiveNestingAllowsNegativeSecondSecant :
    ∃ left right : ℝ,
      0 < left - 2 * right ∧ left - right < 0 := by
  refine ⟨-3, -2, ?_⟩
  norm_num

end PrecategoryFormal
