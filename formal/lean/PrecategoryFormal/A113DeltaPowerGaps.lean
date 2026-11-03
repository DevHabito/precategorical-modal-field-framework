import PrecategoryFormal.A113DeltaPreliminaries
import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
# A113 Delta: uniform normalized power-difference caps

This module turns individual high-power estimates into bounds for
the actual source-minus-beta differences used in the parity formulas.
It does not assert the final strict Delta interval.
-/

private theorem a113NodePow_le_one
    (node : ℝ) (n : ℕ) (hnode0 : 0 ≤ node) (hnode1 : node ≤ 1) :
    node ^ n ≤ 1 := by
  induction n with
  | zero => norm_num
  | succ n ih =>
      calc
        node ^ (n + 1) = node ^ n * node := pow_succ _ _
        _ ≤ node ^ n * 1 :=
          mul_le_mul_of_nonneg_left hnode1 (pow_nonneg hnode0 n)
        _ = node ^ n := by ring
        _ ≤ 1 := ih

/-- A power at M is no larger than the same node's half-index power. -/
theorem a113NodeFullPower_le_unit_div_million
    (size : ℕ) (node : ℝ)
    (hsize : 521 ≤ size)
    (hnode0 : 0 ≤ node)
    (hnodeUpper : node ≤ 1 / 6) :
    node ^ size ≤ a113Unit size / 1000000 := by
  have hsplit :
      size = a113HalfIndex size + (size - a113HalfIndex size) := by
    unfold a113HalfIndex
    omega
  have hnode1 : node ≤ 1 := by linarith
  calc
    node ^ size =
        node ^ (a113HalfIndex size + (size - a113HalfIndex size)) := by
          exact congrArg (fun exponent : ℕ => node ^ exponent) hsplit
    _ = node ^ a113HalfIndex size *
          node ^ (size - a113HalfIndex size) := by
        rw [pow_add]
    _ ≤ node ^ a113HalfIndex size * 1 :=
      mul_le_mul_of_nonneg_left
        (a113NodePow_le_one node _ hnode0 hnode1)
        (pow_nonneg hnode0 _)
    _ = node ^ a113HalfIndex size := by ring
    _ ≤ a113Unit size / 1000000 :=
      a113NodePower_le_unit_div_million
        size node hsize hnode0 hnodeUpper

/-- The next half-index power obeys the same tiny cap. -/
theorem a113NodeNextHalfPower_le_unit_div_million
    (size : ℕ) (node : ℝ)
    (hsize : 521 ≤ size)
    (hnode0 : 0 ≤ node)
    (hnodeUpper : node ≤ 1 / 6) :
    node ^ (a113HalfIndex size + 1) ≤
      a113Unit size / 1000000 := by
  have hnode1 : node ≤ 1 := by linarith
  calc
    node ^ (a113HalfIndex size + 1) =
        node ^ a113HalfIndex size * node := pow_succ _ _
    _ ≤ node ^ a113HalfIndex size * 1 :=
      mul_le_mul_of_nonneg_left hnode1 (pow_nonneg hnode0 _)
    _ = node ^ a113HalfIndex size := by ring
    _ ≤ a113Unit size / 1000000 :=
      a113NodePower_le_unit_div_million
        size node hsize hnode0 hnodeUpper

private theorem a113SourceBetaPowerRatio_bounds
    (size index : ℕ) (source : ℝ)
    (hbetaSource : (1 / 8 : ℝ) ≤ source)
    (hpower : source ^ index ≤ a113Unit size / 1000000) :
    0 ≤ (source ^ index - (1 / 8 : ℝ) ^ index) /
      a113Unit size ∧
    (source ^ index - (1 / 8 : ℝ) ^ index) /
      a113Unit size ≤ 1 / 1000000 := by
  have hu : 0 < a113Unit size := a113Unit_pos size
  have hmonotone : (1 / 8 : ℝ) ^ index ≤ source ^ index :=
    pow_le_pow_left₀ (by norm_num) hbetaSource index
  have hbetaNonnegative : 0 ≤ (1 / 8 : ℝ) ^ index := by
    positivity
  constructor
  · exact div_nonneg (sub_nonneg.mpr hmonotone) (le_of_lt hu)
  · apply (div_le_iff₀ hu).2
    nlinarith [hpower, hbetaNonnegative]

/-- Normalized difference of the source/beta half-index powers. -/
theorem a113DeltaHalfPowerRatio_bounds
    (size : ℕ) (source : ℝ)
    (hsize : 521 ≤ size)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    0 ≤ (source ^ a113HalfIndex size -
      (1 / 8 : ℝ) ^ a113HalfIndex size) / a113Unit size ∧
    (source ^ a113HalfIndex size -
      (1 / 8 : ℝ) ^ a113HalfIndex size) / a113Unit size ≤
        1 / 1000000 := by
  exact a113SourceBetaPowerRatio_bounds
    size (a113HalfIndex size) source
    (by linarith)
    (a113NodePower_le_unit_div_million
      size source hsize (by linarith) (by linarith))

/-- Normalized difference of the next source/beta half-index powers. -/
theorem a113DeltaNextPowerRatio_bounds
    (size : ℕ) (source : ℝ)
    (hsize : 521 ≤ size)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    0 ≤ (source ^ (a113HalfIndex size + 1) -
      (1 / 8 : ℝ) ^ (a113HalfIndex size + 1)) /
      a113Unit size ∧
    (source ^ (a113HalfIndex size + 1) -
      (1 / 8 : ℝ) ^ (a113HalfIndex size + 1)) /
      a113Unit size ≤ 1 / 1000000 := by
  exact a113SourceBetaPowerRatio_bounds
    size (a113HalfIndex size + 1) source
    (by linarith)
    (a113NodeNextHalfPower_le_unit_div_million
      size source hsize (by linarith) (by linarith))

/-- Normalized difference of the full source/beta M-th powers. -/
theorem a113DeltaFullPowerRatio_bounds
    (size : ℕ) (source : ℝ)
    (hsize : 521 ≤ size)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    0 ≤ (source ^ size - (1 / 8 : ℝ) ^ size) /
      a113Unit size ∧
    (source ^ size - (1 / 8 : ℝ) ^ size) /
      a113Unit size ≤ 1 / 1000000 := by
  exact a113SourceBetaPowerRatio_bounds
    size size source
    (by linarith)
    (a113NodeFullPower_le_unit_div_million
      size source hsize (by linarith) (by linarith))

end PrecategoryFormal
