import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Total mass of a four-point weight vector on support `{0,1,2,3}`. -/
def fourPointMass (p0 p1 p2 p3 : ℝ) : ℝ :=
  p0 + p1 + p2 + p3

/-- Mean of a four-point weight vector on support `{0,1,2,3}`. -/
def fourPointMean (p0 p1 p2 p3 : ℝ) : ℝ :=
  p1 + 2 * p2 + 3 * p3

/-- Polynomial/exponential moment at base `r` on support `{0,1,2,3}`. -/
def fourPointMoment (r p0 p1 p2 p3 : ℝ) : ℝ :=
  p0 + p1 * r + p2 * r ^ 2 + p3 * r ^ 3

/-- Difference polynomial used to derive the rational witness. -/
def nonclosureDifferencePolynomial (z : ℝ) : ℝ :=
  4 * z ^ 3 - 9 * z ^ 2 + 6 * z - 1

/-- The frozen difference polynomial has the root structure required by the witness. -/
theorem nonclosureDifferencePolynomial_factor (z : ℝ) :
    nonclosureDifferencePolynomial z = (z - 1) ^ 2 * (4 * z - 1) := by
  unfold nonclosureDifferencePolynomial
  ring

/-- Equal normalization constraint. -/
theorem nonclosureDifferencePolynomial_one :
    nonclosureDifferencePolynomial 1 = 0 := by
  norm_num [nonclosureDifferencePolynomial]

/-- Equal initial base-`1/4` moment constraint. -/
theorem nonclosureDifferencePolynomial_quarter :
    nonclosureDifferencePolynomial (1 / 4 : ℝ) = 0 := by
  norm_num [nonclosureDifferencePolynomial]

/-- The rescaled base-`1/2` moment is separated exactly. -/
theorem nonclosureDifferencePolynomial_half :
    nonclosureDifferencePolynomial (1 / 2 : ℝ) = 1 / 4 := by
  norm_num [nonclosureDifferencePolynomial]

/-- Frozen positive four-point witness `p+`. -/
def nonclosurePPlus0 : ℝ := 9 / 40
def nonclosurePPlus1 : ℝ := 2 / 5
def nonclosurePPlus2 : ℝ := 1 / 40
def nonclosurePPlus3 : ℝ := 7 / 20

/-- Frozen positive four-point witness `p-`. -/
def nonclosurePMinus0 : ℝ := 11 / 40
def nonclosurePMinus1 : ℝ := 1 / 10
def nonclosurePMinus2 : ℝ := 19 / 40
def nonclosurePMinus3 : ℝ := 3 / 20

/-- Every weight in `p+` is strictly positive. -/
theorem nonclosurePPlus_positive :
    0 < nonclosurePPlus0 ∧
    0 < nonclosurePPlus1 ∧
    0 < nonclosurePPlus2 ∧
    0 < nonclosurePPlus3 := by
  norm_num [nonclosurePPlus0, nonclosurePPlus1, nonclosurePPlus2, nonclosurePPlus3]

/-- Every weight in `p-` is strictly positive. -/
theorem nonclosurePMinus_positive :
    0 < nonclosurePMinus0 ∧
    0 < nonclosurePMinus1 ∧
    0 < nonclosurePMinus2 ∧
    0 < nonclosurePMinus3 := by
  norm_num [nonclosurePMinus0, nonclosurePMinus1, nonclosurePMinus2, nonclosurePMinus3]

/-- `p+` is exactly normalized. -/
theorem nonclosurePPlus_mass :
    fourPointMass
      nonclosurePPlus0 nonclosurePPlus1 nonclosurePPlus2 nonclosurePPlus3 = 1 := by
  norm_num [fourPointMass, nonclosurePPlus0, nonclosurePPlus1,
    nonclosurePPlus2, nonclosurePPlus3]

/-- `p-` is exactly normalized. -/
theorem nonclosurePMinus_mass :
    fourPointMass
      nonclosurePMinus0 nonclosurePMinus1 nonclosurePMinus2 nonclosurePMinus3 = 1 := by
  norm_num [fourPointMass, nonclosurePMinus0, nonclosurePMinus1,
    nonclosurePMinus2, nonclosurePMinus3]

/-- The two witnesses have the same exact mean `3/2`. -/
theorem nonclosurePPlus_mean :
    fourPointMean
      nonclosurePPlus0 nonclosurePPlus1 nonclosurePPlus2 nonclosurePPlus3 = 3 / 2 := by
  norm_num [fourPointMean, nonclosurePPlus0, nonclosurePPlus1,
    nonclosurePPlus2, nonclosurePPlus3]

theorem nonclosurePMinus_mean :
    fourPointMean
      nonclosurePMinus0 nonclosurePMinus1 nonclosurePMinus2 nonclosurePMinus3 = 3 / 2 := by
  norm_num [fourPointMean, nonclosurePMinus0, nonclosurePMinus1,
    nonclosurePMinus2, nonclosurePMinus3]

/-- At base `1/4`, both exact moments are `85/256`. -/
theorem nonclosurePPlus_quarterMoment :
    fourPointMoment (1 / 4 : ℝ)
      nonclosurePPlus0 nonclosurePPlus1 nonclosurePPlus2 nonclosurePPlus3 = 85 / 256 := by
  norm_num [fourPointMoment, nonclosurePPlus0, nonclosurePPlus1,
    nonclosurePPlus2, nonclosurePPlus3]

theorem nonclosurePMinus_quarterMoment :
    fourPointMoment (1 / 4 : ℝ)
      nonclosurePMinus0 nonclosurePMinus1 nonclosurePMinus2 nonclosurePMinus3 = 85 / 256 := by
  norm_num [fourPointMoment, nonclosurePMinus0, nonclosurePMinus1,
    nonclosurePMinus2, nonclosurePMinus3]

/-- At base `1/2`, the exact moments differ. -/
theorem nonclosurePPlus_halfMoment :
    fourPointMoment (1 / 2 : ℝ)
      nonclosurePPlus0 nonclosurePPlus1 nonclosurePPlus2 nonclosurePPlus3 = 19 / 40 := by
  norm_num [fourPointMoment, nonclosurePPlus0, nonclosurePPlus1,
    nonclosurePPlus2, nonclosurePPlus3]

theorem nonclosurePMinus_halfMoment :
    fourPointMoment (1 / 2 : ℝ)
      nonclosurePMinus0 nonclosurePMinus1 nonclosurePMinus2 nonclosurePMinus3 = 37 / 80 := by
  norm_num [fourPointMoment, nonclosurePMinus0, nonclosurePMinus1,
    nonclosurePMinus2, nonclosurePMinus3]

/-- The rescaled moments differ by exactly `1/80`, with no approximation. -/
theorem nonclosure_halfMoment_difference :
    fourPointMoment (1 / 2 : ℝ)
        nonclosurePPlus0 nonclosurePPlus1 nonclosurePPlus2 nonclosurePPlus3 -
      fourPointMoment (1 / 2 : ℝ)
        nonclosurePMinus0 nonclosurePMinus1 nonclosurePMinus2 nonclosurePMinus3
      = 1 / 80 := by
  rw [nonclosurePPlus_halfMoment, nonclosurePMinus_halfMoment]
  norm_num

/-- The finite algebraic obstruction needed by MF-R049, separated from `exp`/`log`. -/
theorem rationalFourPointNonclosureWitness :
    fourPointMass
        nonclosurePPlus0 nonclosurePPlus1 nonclosurePPlus2 nonclosurePPlus3 = 1 ∧
    fourPointMass
        nonclosurePMinus0 nonclosurePMinus1 nonclosurePMinus2 nonclosurePMinus3 = 1 ∧
    fourPointMean
        nonclosurePPlus0 nonclosurePPlus1 nonclosurePPlus2 nonclosurePPlus3 =
      fourPointMean
        nonclosurePMinus0 nonclosurePMinus1 nonclosurePMinus2 nonclosurePMinus3 ∧
    fourPointMoment (1 / 4 : ℝ)
        nonclosurePPlus0 nonclosurePPlus1 nonclosurePPlus2 nonclosurePPlus3 =
      fourPointMoment (1 / 4 : ℝ)
        nonclosurePMinus0 nonclosurePMinus1 nonclosurePMinus2 nonclosurePMinus3 ∧
    fourPointMoment (1 / 2 : ℝ)
        nonclosurePPlus0 nonclosurePPlus1 nonclosurePPlus2 nonclosurePPlus3 ≠
      fourPointMoment (1 / 2 : ℝ)
        nonclosurePMinus0 nonclosurePMinus1 nonclosurePMinus2 nonclosurePMinus3 := by
  refine ⟨nonclosurePPlus_mass, nonclosurePMinus_mass, ?_, ?_, ?_⟩
  · rw [nonclosurePPlus_mean, nonclosurePMinus_mean]
  · rw [nonclosurePPlus_quarterMoment, nonclosurePMinus_quarterMoment]
  · rw [nonclosurePPlus_halfMoment, nonclosurePMinus_halfMoment]
    norm_num

end PrecategoryFormal
