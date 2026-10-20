import PrecategoryFormal.A113HEnvelopes
import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
# A113: finite target normalization and moment-slope bounds

All statements refer to the actual finite-M A83 definitions.
The small-left sign and the actual-to-ideal A84 remainder are not
assumed or asserted here.
-/

private theorem a113HalfPow_le_one (exponent : ℕ) :
    (1 / 2 : ℝ) ^ exponent ≤ 1 := by
  induction exponent with
  | zero => norm_num
  | succ n ih =>
      calc
        (1 / 2 : ℝ) ^ (n + 1) =
            (1 / 2 : ℝ) ^ n * (1 / 2 : ℝ) := pow_succ _ _
        _ ≤ (1 / 2 : ℝ) ^ n * 1 :=
          mul_le_mul_of_nonneg_left (by norm_num) (by positivity)
        _ = (1 / 2 : ℝ) ^ n := mul_one _
        _ ≤ 1 := ih

/--
The full-size target power is bounded by the historical dyadic
half-size scale for every integer M >= 521.
-/
theorem a113TargetPower_le_unit (size : ℕ)
    (hsize : 521 ≤ size) :
    (1 / 2 : ℝ) ^ size ≤ a113Unit size := by
  have hhalf : a113HalfIndex size ≤ size := by
    unfold a113HalfIndex
    omega
  obtain ⟨offset, hindex⟩ :
      ∃ offset : ℕ, size = a113HalfIndex size + offset := by
    refine ⟨size - a113HalfIndex size, ?_⟩
    omega
  calc
    (1 / 2 : ℝ) ^ size =
        (1 / 2 : ℝ) ^ (a113HalfIndex size + offset) :=
      congrArg (fun exponent : ℕ => (1 / 2 : ℝ) ^ exponent) hindex
    _ = (1 / 2 : ℝ) ^ a113HalfIndex size *
          (1 / 2 : ℝ) ^ offset := pow_add _ _ _
    _ ≤ (1 / 2 : ℝ) ^ a113HalfIndex size * 1 :=
      mul_le_mul_of_nonneg_left (a113HalfPow_le_one offset) (by positivity)
    _ = a113Unit size := by simp only [mul_one, a113Unit]

/--
The target mass retains its exact finite-size power correction.
-/
theorem a113TargetMass_sub_half (size : ℕ) :
    a113TargetMass size - (1 / 2 : ℝ) =
      (1 / 2 : ℝ) ^ size / 2 := by
  unfold a113TargetMass
  ring

/--
Absolute finite-size target-mass error and safe [1/2, 1] range.
-/
theorem a113TargetMass_abs_error_le_half_unit (size : ℕ)
    (hsize : 521 ≤ size) :
    |a113TargetMass size - (1 / 2 : ℝ)| ≤
      a113Unit size / 2 := by
  rw [a113TargetMass_sub_half]
  rw [abs_of_nonneg (by positivity)]
  exact div_le_div_of_nonneg_right
    (a113TargetPower_le_unit size hsize) (by norm_num)

theorem a113TargetMass_bounds (size : ℕ) :
    (1 / 2 : ℝ) ≤ a113TargetMass size ∧
      a113TargetMass size ≤ 1 := by
  have hpow0 : 0 ≤ (1 / 2 : ℝ) ^ size := by positivity
  have hpow1 : (1 / 2 : ℝ) ^ size ≤ 1 :=
    a113HalfPow_le_one size
  unfold a113TargetMass
  constructor <;> linarith

/--
All three A83 nodes are bounded by 1/2; this theorem covers
that entire interval, rather than using a special sampled node.
-/
theorem a113NodeFullPower_le_unit (size : ℕ) (node : ℝ)
    (hsize : 521 ≤ size)
    (hnode0 : 0 ≤ node) (hnode : node ≤ 1 / 2) :
    node ^ size ≤ a113Unit size := by
  have hpow : node ^ size ≤ (1 / 2 : ℝ) ^ size :=
    pow_le_pow_left₀ hnode0 hnode size
  exact le_trans hpow (a113TargetPower_le_unit size hsize)

/-- The actual slope differs from 1/M by the exact power residual. -/
theorem a113MomentSlope_sub_recipro (size : ℕ) (node : ℝ) :
    a113MomentSlope size node - (1 / (size : ℝ)) =
      -(node ^ size / (size : ℝ)) := by
  unfold a113MomentSlope
  ring

/--
The exact finite moment slope is nonnegative and at most 1/M.
-/
theorem a113MomentSlope_bounds (size : ℕ) (node : ℝ)
    (hsize : 521 ≤ size)
    (hnode0 : 0 ≤ node) (hnode : node ≤ 1 / 2) :
    0 ≤ a113MomentSlope size node ∧
      a113MomentSlope size node ≤ 1 / (size : ℝ) := by
  have hposNat : 0 < size := by omega
  have hpos : (0 : ℝ) < size := by exact_mod_cast hposNat
  have hpow0 : 0 ≤ node ^ size := pow_nonneg hnode0 size
  have hpow1 : node ^ size ≤ 1 := by
    calc
      node ^ size ≤ (1 / 2 : ℝ) ^ size :=
        pow_le_pow_left₀ hnode0 hnode size
      _ ≤ 1 := a113HalfPow_le_one size
  constructor
  · unfold a113MomentSlope
    exact div_nonneg (sub_nonneg.mpr hpow1) (le_of_lt hpos)
  · rw [show a113MomentSlope size node =
        1 / (size : ℝ) - node ^ size / (size : ℝ) by
          unfold a113MomentSlope
          ring]
    have hres : 0 ≤ node ^ size / (size : ℝ) :=
      div_nonneg hpow0 (le_of_lt hpos)
    linarith

/--
The exact slope error obeys U/M at all actual A83 nodes.
It is not a premise supplied by the retrospective A113 analysis.
-/
theorem a113MomentSlope_abs_error_le_unit_div_size
    (size : ℕ) (node : ℝ)
    (hsize : 521 ≤ size)
    (hnode0 : 0 ≤ node) (hnode : node ≤ 1 / 2) :
    |a113MomentSlope size node - 1 / (size : ℝ)| ≤
      a113Unit size / (size : ℝ) := by
  have hposNat : 0 < size := by omega
  have hpos : (0 : ℝ) < size := by exact_mod_cast hposNat
  rw [a113MomentSlope_sub_recipro, abs_neg,
    abs_of_nonneg (div_nonneg (pow_nonneg hnode0 size) (le_of_lt hpos))]
  exact div_le_div_of_nonneg_right
    (a113NodeFullPower_le_unit size node hsize hnode0 hnode)
    (le_of_lt hpos)

/--
At beta and source, the stronger U/(128 M) slope estimate is
available, while the target node uses the general U/M estimate.
-/
theorem a113SmallNodeMomentSlope_abs_error_le_unit_div_size
    (size : ℕ) (node : ℝ)
    (hsize : 521 ≤ size)
    (hnode0 : 0 ≤ node) (hnode : node ≤ 1 / 6) :
    |a113MomentSlope size node - 1 / (size : ℝ)| ≤
      a113Unit size / (128 * (size : ℝ)) := by
  have hposNat : 0 < size := by omega
  have hpos : (0 : ℝ) < size := by exact_mod_cast hposNat
  rw [a113MomentSlope_sub_recipro, abs_neg,
    abs_of_nonneg (div_nonneg (pow_nonneg hnode0 size) (le_of_lt hpos))]
  have hbound := a113FullPower_le_unit_div_128
    size node hsize hnode0 hnode
  have hdivide : node ^ size / (size : ℝ) ≤
      (a113Unit size / 128) / (size : ℝ) :=
    div_le_div_of_nonneg_right hbound (le_of_lt hpos)
  calc
    node ^ size / (size : ℝ) ≤
        (a113Unit size / 128) / (size : ℝ) := hdivide
    _ = a113Unit size / (128 * (size : ℝ)) := by ring

end PrecategoryFormal
