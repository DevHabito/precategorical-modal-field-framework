import PrecategoryFormal.A113BilinearEnvelopes
import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
# A113: finite A84 affine, linear and constant coefficient envelopes

The coefficient definitions reproduce the historical A84 ten-term
expansion, with the original target and opposite beta/source channels.
The full actual-to-ideal remainder is deliberately not assumed.
-/

noncomputable def a113BetaBilinear (size : ℕ) (source : ℝ) : ℝ :=
  a113TargetMass size * a113MomentSlope size source -
    a113H size source false * a113MomentSlope size (1 / 2)

noncomputable def a113SourceBilinear (size : ℕ) : ℝ :=
  a113TargetMass size * a113MomentSlope size (1 / 8) -
    a113H size (1 / 8) true * a113MomentSlope size (1 / 2)

noncomputable def a113TargetBilinear (size : ℕ) (source : ℝ) : ℝ :=
  a113H size (1 / 8) true * a113MomentSlope size source -
    a113H size source false * a113MomentSlope size (1 / 8)

noncomputable def a113BetaAffine (size : ℕ) (source : ℝ) : ℝ :=
  a113BetaBilinear size source +
    ((1 / 8 : ℝ) - 1) *
      (a113TargetMass size - a113H size source false)

noncomputable def a113SourceAffine (size : ℕ) (source : ℝ) : ℝ :=
  -a113SourceBilinear size +
    (1 - source) * (a113TargetMass size - a113H size (1 / 8) true)

noncomputable def a113TargetAffine (size : ℕ) (source : ℝ) : ℝ :=
  -a113TargetBilinear size source +
    (1 - (1 / 2 : ℝ)) *
      (a113H size (1 / 8) true - a113H size source false)

noncomputable def a113BetaLinear (size : ℕ) (source : ℝ) : ℝ :=
  (1 - (1 / 8 : ℝ)) * a113BetaBilinear size source

noncomputable def a113SourceLinear (size : ℕ) (source : ℝ) : ℝ :=
  (source - 1) * a113SourceBilinear size

noncomputable def a113TargetLinear (size : ℕ) (source : ℝ) : ℝ :=
  ((1 / 2 : ℝ) - 1) * a113TargetBilinear size source

noncomputable def a113ConstantCoefficient (size : ℕ) (source : ℝ) : ℝ :=
  (a113H size (1 / 8) true - a113TargetMass size) *
      a113MomentSlope size source +
    (a113TargetMass size - a113H size source false) *
      a113MomentSlope size (1 / 8) +
    (a113H size source false - a113H size (1 / 8) true) *
      a113MomentSlope size (1 / 2)

/-- The two channel deviations imply a uniform pairwise difference. -/
private theorem a113ChannelDifferenceAbstract (left right unit : ℝ)
    (hleft : |left - 1 / 2| ≤ unit)
    (hright : |right - 1 / 2| ≤ unit) :
    |left - right| ≤ 2 * unit := by
  have hl := (abs_le.mp hleft).1
  have hu := (abs_le.mp hleft).2
  have hr := (abs_le.mp hright).1
  have hs := (abs_le.mp hright).2
  apply abs_le.mpr
  constructor <;> linarith

/-- All three historical pairs of channel values are within 2U. -/
theorem a113ChannelDifferencesBound (size : ℕ) (source : ℝ)
    (hsize : 521 ≤ size)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    |a113TargetMass size - a113H size source false| ≤
        2 * a113Unit size ∧
    |a113TargetMass size - a113H size (1 / 8) true| ≤
        2 * a113Unit size ∧
    |a113H size (1 / 8) true - a113H size source false| ≤
        2 * a113Unit size := by
  have hA : |a113TargetMass size - (1 / 2 : ℝ)| ≤
      a113Unit size := by
    have ha := a113TargetMass_abs_error_le_half_unit size hsize
    have hu := a113Unit_pos size
    linarith
  have hB : |a113H size (1 / 8) true - (1 / 2 : ℝ)| ≤
      a113Unit size :=
    le_of_lt (a113HBeta_abs_sub_half_lt_unit size hsize)
  have hS : |a113H size source false - (1 / 2 : ℝ)| ≤
      a113Unit size :=
    le_of_lt (a113HSource_abs_sub_half_lt_unit
      size source hsize hsLower hsUpper)
  exact ⟨a113ChannelDifferenceAbstract _ _ _ hA hS,
    a113ChannelDifferenceAbstract _ _ _ hA hB,
    a113ChannelDifferenceAbstract _ _ _ hB hS⟩

/-- A bounded node coefficient preserves the 3U/M linear cap. -/
private theorem a113LinearAbstract (coeff bilinear unit : ℝ) (size : ℕ)
    (hcoeff : |coeff| ≤ 1)
    (hbilinear : |bilinear| ≤ 3 * unit / (size : ℝ)) :
    |coeff * bilinear| ≤ 3 * unit / (size : ℝ) := by
  rw [abs_mul]
  calc
    |coeff| * |bilinear| ≤ 1 * |bilinear| :=
      mul_le_mul_of_nonneg_right hcoeff (abs_nonneg bilinear)
    _ = |bilinear| := one_mul _
    _ ≤ 3 * unit / (size : ℝ) := hbilinear

/-- A real-algebra cap for the full affine coefficient. -/
private theorem a113AffineAbstract (size : ℕ)
    (coeff bilinear difference unit : ℝ)
    (hsize : 521 ≤ size)
    (hunit : 0 < unit)
    (hcoeff : |coeff| ≤ 1)
    (hbilinear : |bilinear| ≤ 3 * unit / (size : ℝ))
    (hdifference : |difference| ≤ 2 * unit) :
    |bilinear + coeff * difference| < 5 * unit := by
  have hm : (521 : ℝ) ≤ size := by exact_mod_cast hsize
  have hmpos : (0 : ℝ) < size := by linarith
  have hr : (1 / (size : ℝ)) < 1 :=
    (div_lt_iff₀ hmpos).mpr (by linarith)
  have hbilinearSmall : 3 * unit / (size : ℝ) < 3 * unit := by
    calc
      3 * unit / (size : ℝ) = (3 * unit) * (1 / (size : ℝ)) := by ring
      _ < (3 * unit) * 1 :=
        mul_lt_mul_of_pos_left hr (by positivity)
      _ = 3 * unit := by ring
  have hproduct : |coeff * difference| ≤ 2 * unit := by
    rw [abs_mul]
    calc
      |coeff| * |difference| ≤ 1 * |difference| :=
        mul_le_mul_of_nonneg_right hcoeff (abs_nonneg difference)
      _ = |difference| := one_mul _
      _ ≤ 2 * unit := hdifference
  calc
    |bilinear + coeff * difference| ≤
        |bilinear| + |coeff * difference| := abs_add_le _ _
    _ < 5 * unit := by linarith

/-- Actual beta/source/target linear coefficients, all at once. -/
theorem a113LinearCoefficientsBound (size : ℕ) (source : ℝ)
    (hsize : 521 ≤ size)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    |a113BetaLinear size source| ≤ 3 * a113Unit size / (size : ℝ) ∧
    |a113SourceLinear size source| ≤ 3 * a113Unit size / (size : ℝ) ∧
    |a113TargetLinear size source| ≤ 3 * a113Unit size / (size : ℝ) := by
  have hb := a113BetaBilinearBound
    size source hsize hsLower hsUpper
  have hs := a113SourceBilinearBound size hsize
  have ht := a113TargetBilinearBound
    size source hsize hsLower hsUpper
  unfold a113BetaLinear a113SourceLinear a113TargetLinear
    a113BetaBilinear a113SourceBilinear a113TargetBilinear
  constructor
  · exact a113LinearAbstract _ _ _ size (by norm_num) hb
  constructor
  · apply a113LinearAbstract _ _ _ size
    · rw [abs_of_nonpos (by linarith : source - 1 ≤ 0)]
      linarith
    · exact hs
  · exact a113LinearAbstract _ _ _ size (by norm_num) ht

/-- The three actual historical affine coefficients are O(U). -/
theorem a113AffineCoefficientsBound (size : ℕ) (source : ℝ)
    (hsize : 521 ≤ size)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    |a113BetaAffine size source| < 5 * a113Unit size ∧
    |a113SourceAffine size source| < 5 * a113Unit size ∧
    |a113TargetAffine size source| < 5 * a113Unit size := by
  have hd := a113ChannelDifferencesBound
    size source hsize hsLower hsUpper
  have hb := a113BetaBilinearBound
    size source hsize hsLower hsUpper
  have hs := a113SourceBilinearBound size hsize
  have ht := a113TargetBilinearBound
    size source hsize hsLower hsUpper
  have hunit := a113Unit_pos size
  unfold a113BetaAffine a113SourceAffine a113TargetAffine
    a113BetaBilinear a113SourceBilinear a113TargetBilinear
  constructor
  · exact a113AffineAbstract size _ _ _ _
      hsize hunit (by norm_num) hb hd.1
  constructor
  · have hx := a113AffineAbstract size
      (1 - source)
      (-(a113TargetMass size * a113MomentSlope size (1 / 8) -
        a113H size (1 / 8) true * a113MomentSlope size (1 / 2)))
      (a113TargetMass size - a113H size (1 / 8) true)
      (a113Unit size) hsize hunit
      (by
        rw [abs_of_nonneg (by linarith : 0 ≤ 1 - source)]
        linarith)
      (by simpa only [abs_neg] using hs)
      hd.2.1
    exact hx
  · have hx := a113AffineAbstract size
      (1 - (1 / 2 : ℝ))
      (-(a113H size (1 / 8) true * a113MomentSlope size source -
        a113H size source false * a113MomentSlope size (1 / 8)))
      (a113H size (1 / 8) true - a113H size source false)
      (a113Unit size) hsize hunit
      (by norm_num) (by simpa only [abs_neg] using ht) hd.2.2
    exact hx

/-- The product of a channel difference and a slope has size 2U/M. -/
private theorem a113ConstantTermAbstract (size : ℕ)
    (difference slope unit : ℝ)
    (_hsize : 521 ≤ size)
    (hdiff : |difference| ≤ 2 * unit)
    (hzero : 0 ≤ slope)
    (hcap : slope ≤ 1 / (size : ℝ)) :
    |difference * slope| ≤ 2 * unit / (size : ℝ) := by
  have hu : 0 ≤ unit := by
    have habs : 0 ≤ |difference| := abs_nonneg _
    linarith
  calc
    |difference * slope| = |difference| * slope := by
      rw [abs_mul, abs_of_nonneg hzero]
    _ ≤ (2 * unit) * slope :=
      mul_le_mul_of_nonneg_right hdiff hzero
    _ ≤ (2 * unit) * (1 / (size : ℝ)) :=
      mul_le_mul_of_nonneg_left hcap (by positivity)
    _ = 2 * unit / (size : ℝ) := by ring

/-- Historical A84 constant-channel coefficient, without a sign guess. -/
theorem a113ConstantCoefficientBound (size : ℕ) (source : ℝ)
    (hsize : 521 ≤ size)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    |a113ConstantCoefficient size source| ≤
      6 * a113Unit size / (size : ℝ) := by
  have hd := a113ChannelDifferencesBound
    size source hsize hsLower hsUpper
  have hbs := a113MomentSlope_bounds
    size source hsize (by linarith) (by linarith)
  have hbb := a113MomentSlope_bounds
    size (1 / 8) hsize (by norm_num) (by norm_num)
  have hbt := a113MomentSlope_bounds
    size (1 / 2) hsize (by norm_num) (by norm_num)
  have h1 : |(a113H size (1 / 8) true - a113TargetMass size) *
      a113MomentSlope size source| ≤
      2 * a113Unit size / (size : ℝ) := by
    apply a113ConstantTermAbstract size _ _ _ hsize
    · rw [abs_sub_comm]
      exact hd.2.1
    · exact hbs.1
    · exact hbs.2
  have h2 : |(a113TargetMass size - a113H size source false) *
      a113MomentSlope size (1 / 8)| ≤
      2 * a113Unit size / (size : ℝ) :=
    a113ConstantTermAbstract size _ _ _ hsize hd.1 hbb.1 hbb.2
  have h3 : |(a113H size source false - a113H size (1 / 8) true) *
      a113MomentSlope size (1 / 2)| ≤
      2 * a113Unit size / (size : ℝ) := by
    apply a113ConstantTermAbstract size _ _ _ hsize
    · rw [abs_sub_comm]
      exact hd.2.2
    · exact hbt.1
    · exact hbt.2
  unfold a113ConstantCoefficient
  calc
    |(a113H size (1 / 8) true - a113TargetMass size) *
        a113MomentSlope size source +
      (a113TargetMass size - a113H size source false) *
        a113MomentSlope size (1 / 8) +
      (a113H size source false - a113H size (1 / 8) true) *
        a113MomentSlope size (1 / 2)| ≤
        |(a113H size (1 / 8) true - a113TargetMass size) *
          a113MomentSlope size source +
         (a113TargetMass size - a113H size source false) *
          a113MomentSlope size (1 / 8)| +
        |(a113H size source false - a113H size (1 / 8) true) *
          a113MomentSlope size (1 / 2)| :=
          abs_add_le _ _
    _ ≤
        (|(a113H size (1 / 8) true - a113TargetMass size) *
          a113MomentSlope size source| +
         |(a113TargetMass size - a113H size source false) *
          a113MomentSlope size (1 / 8)|) +
        |(a113H size source false - a113H size (1 / 8) true) *
          a113MomentSlope size (1 / 2)| := by
          have ht := abs_add_le
            ((a113H size (1 / 8) true - a113TargetMass size) *
              a113MomentSlope size source)
            ((a113TargetMass size - a113H size source false) *
              a113MomentSlope size (1 / 8))
          linarith
    _ ≤ 2 * a113Unit size / (size : ℝ) +
          2 * a113Unit size / (size : ℝ) +
          2 * a113Unit size / (size : ℝ) :=
          add_le_add (add_le_add h1 h2) h3
    _ = 6 * a113Unit size / (size : ℝ) := by ring

end PrecategoryFormal
