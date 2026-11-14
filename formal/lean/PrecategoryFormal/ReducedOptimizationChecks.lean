import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

namespace PrecategoryFormal.ReducedOptimization

/-- A119: eliminate the exponential variable on the critical surface
once the two denominator terms and the phase are known to be positive. -/
theorem a119CriticalSubstitution (q a c A α D : ℝ)
    (hA : 0 < A) (hα : 0 < α) (hD : 0 < D)
    (hcritical : -a * c + q * (A + α * D) = 0) :
    q = a * c / (A + α * D) := by
  have hden : 0 < A + α * D := add_pos hA (mul_pos hα hD)
  apply (eq_div_iff hden.ne').2
  linarith

private def a119Cmax : ℚ := 1 - (1 / 8) / (133 / 1000) - 4 / 1875
private def a119Bmax : ℚ := (1 / 8) / (129 / 1000) + 2 / 1875

/-- Exact rational lower bound at the first excluded even cell, and the
decay ratio bound used to extend the cutoff. -/
theorem a119EvenCutoffArithmetic :
    0 < -a119Cmax + 14 * 2 * (129 / 1000 : ℚ) ^ 3 -
      14 * (21 / 10) * a119Bmax * (133 / 1000) ^ 14 ∧
    (15 / 14 : ℚ) * (133 / 1000) < 1 := by
  norm_num [a119Cmax, a119Bmax]

/-- The corresponding exact arithmetic checks for the first excluded odd cell. -/
theorem a119OddCutoffArithmetic :
    0 < -(567 / 1000 : ℚ) * a119Cmax +
      (43 / 2) * 2 * (129 / 1000) ^ 3 * (359 / 1000) -
      (567 / 1000) * (43 / 2) * (21 / 10) * a119Bmax *
        (133 / 1000) ^ 21 * (365 / 1000) ∧
    (45 / 43 : ℚ) * (133 / 1000) < 1 := by
  norm_num [a119Cmax, a119Bmax]

/-- A122: the resonant drift coefficient decreases strictly in the drift
parameter when the positive amplitude multiplies a negative logarithm. -/
theorem a122ResonantDriftStrictAnti (Q logSource Ω : ℝ)
    (hQ : 0 < Q) (hlog : logSource < 0) :
    StrictAnti (fun η : ℝ => Q * logSource * η + Ω) := by
  intro x y hxy
  exact add_lt_add_left (mul_lt_mul_of_neg_left hxy (mul_neg_of_pos_of_neg hQ hlog)) Ω

end PrecategoryFormal.ReducedOptimization
