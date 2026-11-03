import PrecategoryFormal.A113CoefficientIdentity
import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
# A113: exact adjacent-factor central-pair identity

This module proves algebraic transformations of E_k - 2*E_(k+1).
It does NOT prove a sign for that expression, establish the threshold
b(M,s), or establish the global one-variation theorem.
-/

/-- One affine-power channel under the central two-step combination. -/
theorem a113AffineDoubleStep (k : ℕ) (node coeff linear : ℝ) :
    (coeff + (k : ℝ) * linear) * node ^ k -
      2 * (coeff + ((k + 1 : ℕ) : ℝ) * linear) * node ^ (k + 1) =
    ((1 - 2 * node) * (coeff + (k : ℝ) * linear) -
      2 * node * linear) * node ^ k := by
  rw [pow_succ]
  push_cast
  ring

/-- At the target node 1/2, the affine coefficient cancels exactly. -/
theorem a113HalfTargetAffineDoubleStep (k : ℕ) (coeff linear : ℝ) :
    (coeff + (k : ℝ) * linear) * (1 / 2 : ℝ) ^ k -
      2 * (coeff + ((k + 1 : ℕ) : ℝ) * linear) *
        (1 / 2 : ℝ) ^ (k + 1) =
    -linear * (1 / 2 : ℝ) ^ k := by
  rw [a113AffineDoubleStep]
  ring

/--
The exact central-pair decomposition for the historical finite-M A83
factor. The target affine coefficient cancels; its linear coefficient
remains. No sign hypothesis or replacement error budget is used.
-/
theorem a113ActualFactorCentralPair_eq_expansion
    (size k : ℕ) (source : ℝ) :
    a113ActualFactor size k source -
        2 * a113ActualFactor size (k + 1) source =
      a113TargetMass size *
        (source - (1 / 8 : ℝ)) *
        (1 - 2 * ((1 / 8 : ℝ) * source)) *
        ((1 / 8 : ℝ) * source) ^ k +
      a113H size source false *
        ((1 / 8 : ℝ) - (1 / 2 : ℝ)) *
        (1 - 2 * ((1 / 8 : ℝ) * (1 / 2 : ℝ))) *
        ((1 / 8 : ℝ) * (1 / 2 : ℝ)) ^ k +
      a113H size (1 / 8) true *
        ((1 / 2 : ℝ) - source) *
        (1 - 2 * (source * (1 / 2 : ℝ))) *
        (source * (1 / 2 : ℝ)) ^ k +
      ((1 - 2 * (1 / 8 : ℝ)) *
          (a113BetaAffine size source +
            (k : ℝ) * a113BetaLinear size source) -
        2 * (1 / 8 : ℝ) * a113BetaLinear size source) *
        (1 / 8 : ℝ) ^ k +
      ((1 - 2 * source) *
          (a113SourceAffine size source +
            (k : ℝ) * a113SourceLinear size source) -
        2 * source * a113SourceLinear size source) *
        source ^ k -
      a113TargetLinear size source * (1 / 2 : ℝ) ^ k -
      a113ConstantCoefficient size source := by
  rw [a113ActualFactor_eq_namedCoefficients size k source,
    a113ActualFactor_eq_namedCoefficients size (k + 1) source]
  simp only [pow_succ, Nat.cast_add, Nat.cast_one]
  ring

end PrecategoryFormal
