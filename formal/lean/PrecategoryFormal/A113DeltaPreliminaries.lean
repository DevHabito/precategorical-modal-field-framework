import PrecategoryFormal.A113DefectEnvelopes
import Mathlib

set_option autoImplicit false
set_option warningAsError true
set_option exponentiation.threshold 512

namespace PrecategoryFormal

/-!
# A113 Delta preconditions: dyadic and high-power bounds

The stronger uniform estimates here prepare a proof of the
parity-sensitive source-minus-beta channel gap. They do not assert
that its historical strict interval has been established.
-/

/-- Geometric decay of the denominator correction beyond exponent 15. -/
private theorem a113DyadicCorrection_le_thousand :
    ∀ h : ℕ, 15 ≤ h →
      (((h + 1 : ℕ) : ℝ) * (1 / 2 : ℝ) ^ h) ≤ 1 / 1000 := by
  intro h hh
  induction h, hh using Nat.le_induction with
  | base =>
      norm_num
  | succ h hh ih =>
      have hcoef :
          (((h + 1 + 1 : ℕ) : ℝ) / 2) ≤
            (((h + 1 : ℕ) : ℝ)) := by
        push_cast
        have hn : 0 ≤ (h : ℝ) := Nat.cast_nonneg _
        linarith
      calc
        (((h + 1 + 1 : ℕ) : ℝ) * (1 / 2 : ℝ) ^ (h + 1)) =
            (((h + 1 + 1 : ℕ) : ℝ) / 2) *
              (1 / 2 : ℝ) ^ h := by rw [pow_succ]; ring
        _ ≤ (((h + 1 : ℕ) : ℝ) * (1 / 2 : ℝ) ^ h) :=
          mul_le_mul_of_nonneg_right hcoef (by positivity)
        _ ≤ 1 / 1000 := ih

/-- The actual denominator differs from 1 by at most 1/1000. -/
theorem a113Denominator_ge_999_thousand (size : ℕ)
    (hsize : 521 ≤ size) :
    (999 / 1000 : ℝ) ≤ a113Denominator size := by
  have hh : 15 ≤ a113HalfIndex size := by
    unfold a113HalfIndex
    omega
  have hbound := a113DyadicCorrection_le_thousand
    (a113HalfIndex size) hh
  unfold a113Denominator a113Unit
  linarith

/-- An elementary upper bound on the positive denominator. -/
theorem a113Denominator_le_one (size : ℕ) :
    a113Denominator size ≤ 1 := by
  have hunit : 0 ≤ a113Unit size :=
    le_of_lt (a113Unit_pos size)
  have hcoeff : (0 : ℝ) ≤ ((a113HalfIndex size + 1 : ℕ) : ℝ) :=
    Nat.cast_nonneg _
  have hproduct : 0 ≤
      ((a113HalfIndex size + 1 : ℕ) : ℝ) * a113Unit size :=
    mul_nonneg hcoeff hunit
  unfold a113Denominator
  linarith

/-- Uniform high-power control with a one-in-a-million relative cap. -/
theorem a113GeometricPowerBound_million (index : ℕ) (node : ℝ)
    (hindex : 14 ≤ index)
    (hnodeNonnegative : 0 ≤ node)
    (hnodeUpper : node ≤ 1 / 6) :
    node ^ index ≤ (1 / 2 : ℝ) ^ index / 1000000 := by
  induction index, hindex using Nat.le_induction with
  | base =>
      calc
        node ^ 14 ≤ (1 / 6 : ℝ) ^ 14 :=
          pow_le_pow_left₀ hnodeNonnegative hnodeUpper 14
        _ ≤ (1 / 2 : ℝ) ^ 14 / 1000000 := by norm_num
  | succ index hindex ih =>
      calc
        node ^ (index + 1) = node ^ index * node := pow_succ _ _
        _ ≤ node ^ index * (1 / 2 : ℝ) :=
          mul_le_mul_of_nonneg_left
            (by linarith) (pow_nonneg hnodeNonnegative index)
        _ ≤ ((1 / 2 : ℝ) ^ index / 1000000) * (1 / 2 : ℝ) :=
          mul_le_mul_of_nonneg_right ih (by norm_num)
        _ = (1 / 2 : ℝ) ^ (index + 1) / 1000000 := by
          rw [pow_succ]
          ring

/-- For any admissible real source, its half-index power is tiny. -/
theorem a113NodePower_le_unit_div_million
    (size : ℕ) (node : ℝ)
    (hsize : 521 ≤ size)
    (hnodeNonnegative : 0 ≤ node)
    (hnodeUpper : node ≤ 1 / 6) :
    node ^ a113HalfIndex size ≤ a113Unit size / 1000000 := by
  unfold a113Unit
  apply a113GeometricPowerBound_million
  · unfold a113HalfIndex
    omega
  · exact hnodeNonnegative
  · exact hnodeUpper

/-- The source/beta gap is an exact finite-size algebraic identity. -/
theorem a113H_sourceBeta_gap_exact (size : ℕ) (source : ℝ) :
    a113H size source false - a113H size (1 / 8) true =
      (source ^ size - (1 / 8 : ℝ) ^ size) / 2 -
        (a113Defect size source - a113Defect size (1 / 8)) -
        4 * a113Epsilon size := by
  rw [a113H_source_expansion size source,
    a113H_beta_expansion size (1 / 8)]
  ring

end PrecategoryFormal
