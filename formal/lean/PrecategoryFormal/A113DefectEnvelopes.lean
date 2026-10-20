import PrecategoryFormal.A113FiniteChannels
import Mathlib

set_option autoImplicit false
set_option warningAsError true
set_option exponentiation.threshold 512

namespace PrecategoryFormal

/-!
# A113: geometric high-power envelopes

This module establishes the uniform high-power estimates required for
the parity-dependent finite-M defect bounds. It does not assert that
the defect bound or the full A113 sign theorem is already proved.
-/

/--
A real node between zero and 1/6 has a uniformly tiny fifth-and-higher
power relative to the matching dyadic unit. This is proved by induction
for every natural exponent, with exact rational constants.
-/
theorem a113GeometricPowerBound (index : ℕ) (node : ℝ)
    (hindex : 5 ≤ index)
    (hnodeNonnegative : 0 ≤ node)
    (hnodeUpper : node ≤ 1 / 6) :
    node ^ index ≤ (1 / 2 : ℝ) ^ index / 128 := by
  induction index, hindex using Nat.le_induction with
  | base =>
      calc
        node ^ 5 ≤ (1 / 6 : ℝ) ^ 5 :=
          pow_le_pow_left₀ hnodeNonnegative hnodeUpper 5
        _ ≤ (1 / 2 : ℝ) ^ 5 / 128 := by norm_num
  | succ index hindex ih =>
      calc
        node ^ (index + 1) = node ^ index * node := pow_succ _ _
        _ ≤ node ^ index * (1 / 2 : ℝ) :=
          mul_le_mul_of_nonneg_left
            (by linarith) (pow_nonneg hnodeNonnegative index)
        _ ≤ ((1 / 2 : ℝ) ^ index / 128) * (1 / 2 : ℝ) :=
          mul_le_mul_of_nonneg_right ih (by norm_num)
        _ = (1 / 2 : ℝ) ^ (index + 1) / 128 := by
          rw [pow_succ]
          ring

/--
Uniform bound at the historical half-index. The bound is deliberately
stronger than the threshold required by the A84 defect estimates.
-/
theorem a113NodePower_le_unit_div_128 (size : ℕ) (node : ℝ)
    (hsize : 521 ≤ size)
    (hnodeNonnegative : 0 ≤ node)
    (hnodeUpper : node ≤ 1 / 6) :
    node ^ a113HalfIndex size ≤ a113Unit size / 128 := by
  unfold a113Unit
  apply a113GeometricPowerBound
  · unfold a113HalfIndex
    omega
  · exact hnodeNonnegative
  · exact hnodeUpper

/-- The next power has another explicit factor of at most 1/6. -/
theorem a113NodeNextPower_le_unit_div_768 (size : ℕ) (node : ℝ)
    (hsize : 521 ≤ size)
    (hnodeNonnegative : 0 ≤ node)
    (hnodeUpper : node ≤ 1 / 6) :
    node ^ (a113HalfIndex size + 1) ≤ a113Unit size / 768 := by
  have hpower := a113NodePower_le_unit_div_128
    size node hsize hnodeNonnegative hnodeUpper
  calc
    node ^ (a113HalfIndex size + 1) =
        node ^ a113HalfIndex size * node := pow_succ _ _
    _ ≤ node ^ a113HalfIndex size * (1 / 6 : ℝ) :=
      mul_le_mul_of_nonneg_left hnodeUpper
        (pow_nonneg hnodeNonnegative _)
    _ ≤ (a113Unit size / 128) * (1 / 6 : ℝ) :=
      mul_le_mul_of_nonneg_right hpower (by norm_num)
    _ = a113Unit size / 768 := by ring

/--
The denominator estimate also controls the h*U correction. The
precondition is only the frozen size range, not a bound imported from
the historical certificate.
-/
theorem a113HalfCoefficient_le_quarter (size : ℕ)
    (hsize : 521 ≤ size) :
    (a113HalfIndex size : ℝ) * a113Unit size ≤ 1 / 4 := by
  have hden := a113Denominator_ge_three_quarters size hsize
  have hunit : 0 ≤ a113Unit size := le_of_lt (a113Unit_pos size)
  have hstep :
      (a113HalfIndex size : ℝ) ≤
        ((a113HalfIndex size + 1 : ℕ) : ℝ) := by
    exact_mod_cast Nat.le_succ (a113HalfIndex size)
  have hmul := mul_le_mul_of_nonneg_right hstep hunit
  unfold a113Denominator at hden
  linarith

/-- The normalized h*U correction is bounded by one third. -/
theorem a113HalfCoefficient_div_denominator_le_third (size : ℕ)
    (hsize : 521 ≤ size) :
    (a113HalfIndex size : ℝ) * a113Unit size /
        a113Denominator size ≤ 1 / 3 := by
  have hd : (3 / 4 : ℝ) ≤ a113Denominator size :=
    a113Denominator_ge_three_quarters size hsize
  have hdpos := a113Denominator_pos size hsize
  have hh := a113HalfCoefficient_le_quarter size hsize
  apply (div_le_iff₀ hdpos).2
  nlinarith

end PrecategoryFormal
