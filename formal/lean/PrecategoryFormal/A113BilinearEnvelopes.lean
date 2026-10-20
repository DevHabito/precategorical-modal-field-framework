import PrecategoryFormal.A113MomentEnvelopes
import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
# A113: bilinear moment-channel envelopes

These are the three finite-size products appearing in the
beta/source/target affine and linear coefficients of the historical
ten-term A84 factor. The estimates are uniform in M and the source.
-/

/--
A bilinear cancellation estimate. Both coefficients are close to
1/2, and both slopes are close to the same positive scale.
All error bounds appear explicitly as premises, never as conclusions
smuggled into the theorem's assumptions.
-/
private theorem a113BilinearCancellation
    (left right leftSlope rightSlope unit scale : ℝ)
    (hunit : 0 ≤ unit)
    (hleft : |left - 1 / 2| ≤ unit)
    (hright : |right - 1 / 2| ≤ unit)
    (hleftSlope0 : 0 ≤ leftSlope)
    (hleftSlope : leftSlope ≤ scale)
    (hrightSlope0 : 0 ≤ rightSlope)
    (hrightSlope : rightSlope ≤ scale)
    (hleftError : |leftSlope - scale| ≤ unit * scale)
    (hrightError : |rightSlope - scale| ≤ unit * scale) :
    |left * leftSlope - right * rightSlope| ≤
      3 * unit * scale := by
  have hleftProduct :
      |(left - 1 / 2) * leftSlope| ≤ unit * scale := by
    calc
      |(left - 1 / 2) * leftSlope| =
          |left - 1 / 2| * leftSlope := by
            rw [abs_mul, abs_of_nonneg hleftSlope0]
      _ ≤ unit * leftSlope :=
        mul_le_mul_of_nonneg_right hleft hleftSlope0
      _ ≤ unit * scale :=
        mul_le_mul_of_nonneg_left hleftSlope hunit
  have hrightProduct :
      |(1 / 2 - right) * rightSlope| ≤ unit * scale := by
    calc
      |(1 / 2 - right) * rightSlope| =
          |right - 1 / 2| * rightSlope := by
            rw [abs_mul, abs_of_nonneg hrightSlope0, abs_sub_comm]
      _ ≤ unit * rightSlope :=
        mul_le_mul_of_nonneg_right hright hrightSlope0
      _ ≤ unit * scale :=
        mul_le_mul_of_nonneg_left hrightSlope hunit
  have hleftLower := (abs_le.mp hleftError).1
  have hleftUpper := (abs_le.mp hleftError).2
  have hrightLower := (abs_le.mp hrightError).1
  have hrightUpper := (abs_le.mp hrightError).2
  have hdiff : |leftSlope - rightSlope| ≤
      2 * unit * scale := by
    apply abs_le.mpr
    constructor <;> nlinarith
  have hmiddle :
      |(1 / 2 : ℝ) * (leftSlope - rightSlope)| ≤
        unit * scale := by
    calc
      |(1 / 2 : ℝ) * (leftSlope - rightSlope)| =
          |leftSlope - rightSlope| / 2 := by
            rw [abs_mul]
            norm_num
      _ ≤ unit * scale := by linarith
  have hexact :
      left * leftSlope - right * rightSlope =
        (left - 1 / 2) * leftSlope +
          (1 / 2 : ℝ) * (leftSlope - rightSlope) +
          (1 / 2 - right) * rightSlope := by ring
  rw [hexact]
  calc
    |(left - 1 / 2) * leftSlope +
          (1 / 2 : ℝ) * (leftSlope - rightSlope) +
          (1 / 2 - right) * rightSlope| ≤
        |(left - 1 / 2) * leftSlope +
          (1 / 2 : ℝ) * (leftSlope - rightSlope)| +
        |(1 / 2 - right) * rightSlope| :=
          abs_add_le _ _
    _ ≤
        (|(left - 1 / 2) * leftSlope| +
          |(1 / 2 : ℝ) * (leftSlope - rightSlope)|) +
        |(1 / 2 - right) * rightSlope| :=
          add_le_add_right (abs_add_le _ _) _
    _ ≤ 3 * unit * scale := by
          linarith [hleftProduct, hmiddle, hrightProduct]

/--
The general finite-size consequence for arbitrary two channel
values satisfying their previously proven half-mass deviations.
-/
theorem a113BilinearMomentChannelBound
    (size : ℕ) (left right leftNode rightNode : ℝ)
    (hsize : 521 ≤ size)
    (hleftNode0 : 0 ≤ leftNode)
    (hleftNode : leftNode ≤ 1 / 2)
    (hrightNode0 : 0 ≤ rightNode)
    (hrightNode : rightNode ≤ 1 / 2)
    (hleft : |left - 1 / 2| ≤ a113Unit size)
    (hright : |right - 1 / 2| ≤ a113Unit size) :
    |left * a113MomentSlope size leftNode -
      right * a113MomentSlope size rightNode| ≤
        3 * a113Unit size / (size : ℝ) := by
  have hls := a113MomentSlope_bounds
    size leftNode hsize hleftNode0 hleftNode
  have hrs := a113MomentSlope_bounds
    size rightNode hsize hrightNode0 hrightNode
  have hle := a113MomentSlope_abs_error_le_unit_div_size
    size leftNode hsize hleftNode0 hleftNode
  have hre := a113MomentSlope_abs_error_le_unit_div_size
    size rightNode hsize hrightNode0 hrightNode
  have hle' :
      |a113MomentSlope size leftNode - 1 / (size : ℝ)| ≤
        a113Unit size * (1 / (size : ℝ)) := by
    calc
      _ ≤ a113Unit size / (size : ℝ) := hle
      _ = a113Unit size * (1 / (size : ℝ)) := by ring
  have hre' :
      |a113MomentSlope size rightNode - 1 / (size : ℝ)| ≤
        a113Unit size * (1 / (size : ℝ)) := by
    calc
      _ ≤ a113Unit size / (size : ℝ) := hre
      _ = a113Unit size * (1 / (size : ℝ)) := by ring
  have hbound := a113BilinearCancellation
    left right
    (a113MomentSlope size leftNode)
    (a113MomentSlope size rightNode)
    (a113Unit size) (1 / (size : ℝ))
    (le_of_lt (a113Unit_pos size))
    hleft hright hls.1 hls.2 hrs.1 hrs.2 hle' hre'
  calc
    |left * a113MomentSlope size leftNode -
      right * a113MomentSlope size rightNode| ≤
        3 * a113Unit size * (1 / (size : ℝ)) := hbound
    _ = 3 * a113Unit size / (size : ℝ) := by ring

/-- The bilinear part shared by the historical beta coefficients. -/
theorem a113BetaBilinearBound
    (size : ℕ) (source : ℝ)
    (hsize : 521 ≤ size)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    |a113TargetMass size * a113MomentSlope size source -
      a113H size source false * a113MomentSlope size (1 / 2)| ≤
        3 * a113Unit size / (size : ℝ) := by
  apply a113BilinearMomentChannelBound size
    (a113TargetMass size) (a113H size source false)
    source (1 / 2) hsize
  · linarith
  · linarith
  · norm_num
  · norm_num
  · have h := a113TargetMass_abs_error_le_half_unit size hsize
    have hu := a113Unit_pos size
    linarith
  · exact le_of_lt
      (a113HSource_abs_sub_half_lt_unit
        size source hsize hsLower hsUpper)

/-- The bilinear part shared by the historical source coefficients. -/
theorem a113SourceBilinearBound
    (size : ℕ) (hsize : 521 ≤ size) :
    |a113TargetMass size * a113MomentSlope size (1 / 8) -
      a113H size (1 / 8) true * a113MomentSlope size (1 / 2)| ≤
        3 * a113Unit size / (size : ℝ) := by
  apply a113BilinearMomentChannelBound size
    (a113TargetMass size) (a113H size (1 / 8) true)
    (1 / 8) (1 / 2) hsize
  · norm_num
  · norm_num
  · norm_num
  · norm_num
  · have h := a113TargetMass_abs_error_le_half_unit size hsize
    have hu := a113Unit_pos size
    linarith
  · exact le_of_lt (a113HBeta_abs_sub_half_lt_unit size hsize)

/-- The bilinear part shared by the historical target coefficients. -/
theorem a113TargetBilinearBound
    (size : ℕ) (source : ℝ)
    (hsize : 521 ≤ size)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    |a113H size (1 / 8) true * a113MomentSlope size source -
      a113H size source false * a113MomentSlope size (1 / 8)| ≤
        3 * a113Unit size / (size : ℝ) := by
  apply a113BilinearMomentChannelBound size
    (a113H size (1 / 8) true)
    (a113H size source false) source (1 / 8) hsize
  · linarith
  · linarith
  · norm_num
  · norm_num
  · exact le_of_lt (a113HBeta_abs_sub_half_lt_unit size hsize)
  · exact le_of_lt
      (a113HSource_abs_sub_half_lt_unit
        size source hsize hsLower hsUpper)

end PrecategoryFormal
