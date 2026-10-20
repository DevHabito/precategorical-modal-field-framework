import PrecategoryFormal.A113CoefficientEnvelopes
import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
# A113: exact bounded-coefficient connection to the A84 factor

The coefficient envelopes are not transferred merely because they look
similar to A84; the identity is proved from the original definitions.
-/

/-- The named coefficients exactly reconstruct the historical A84 factor. -/
theorem a113ActualFactor_eq_namedCoefficients
    (size k : ℕ) (source : ℝ) :
    a113ActualFactor size k source =
      a113TargetMass size *
          (source - (1 / 8 : ℝ)) * ((1 / 8 : ℝ) * source) ^ k +
      a113H size source false *
          ((1 / 8 : ℝ) - 1 / 2) * ((1 / 8 : ℝ) * (1 / 2 : ℝ)) ^ k +
      a113H size (1 / 8) true *
          ((1 / 2 : ℝ) - source) * (source * (1 / 2 : ℝ)) ^ k +
      (a113BetaAffine size source +
          (k : ℝ) * a113BetaLinear size source) * (1 / 8 : ℝ) ^ k +
      (a113SourceAffine size source +
          (k : ℝ) * a113SourceLinear size source) * source ^ k +
      (a113TargetAffine size source +
          (k : ℝ) * a113TargetLinear size source) * (1 / 2 : ℝ) ^ k +
      a113ConstantCoefficient size source := by
  rw [a113ActualFactor_eq_tenTerm]
  unfold contactTenTermFactor
    a113BetaAffine a113SourceAffine a113TargetAffine
    a113BetaLinear a113SourceLinear a113TargetLinear
    a113ConstantCoefficient
    a113BetaBilinear a113SourceBilinear a113TargetBilinear
  ring

/--
Exact equality for actual minus ideal, without dropping finite-size
channels. A uniform error bound is a separate next proof obligation.
-/
theorem a113ActualFactor_sub_ideal_eq_namedErrors
    (size k : ℕ) (source : ℝ) :
    a113ActualFactor size k source -
        contactIdealCore k (1 / 8) (1 / 2) source =
      (a113TargetMass size - (1 / 2 : ℝ)) *
          (source - (1 / 8 : ℝ)) * ((1 / 8 : ℝ) * source) ^ k +
      (a113H size source false - (1 / 2 : ℝ)) *
          ((1 / 8 : ℝ) - 1 / 2) * ((1 / 8 : ℝ) * (1 / 2 : ℝ)) ^ k +
      (a113H size (1 / 8) true - (1 / 2 : ℝ)) *
          ((1 / 2 : ℝ) - source) * (source * (1 / 2 : ℝ)) ^ k +
      (a113BetaAffine size source +
          (k : ℝ) * a113BetaLinear size source) * (1 / 8 : ℝ) ^ k +
      (a113SourceAffine size source +
          (k : ℝ) * a113SourceLinear size source) * source ^ k +
      (a113TargetAffine size source +
          (k : ℝ) * a113TargetLinear size source) * (1 / 2 : ℝ) ^ k +
      a113ConstantCoefficient size source := by
  rw [a113ActualFactor_eq_namedCoefficients]
  unfold contactIdealCore
  ring

end PrecategoryFormal
