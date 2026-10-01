import PrecategoryFormal.EntropicNonclosureWitness

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

noncomputable section

/-- Mean for weights on the rescaled support `{0,2,4,6}`. -/
def fourPointEvenSupportMean (_p0 p1 p2 p3 : ℝ) : ℝ :=
  2 * p1 + 4 * p2 + 6 * p3

/-- Frozen parameter-preserving witness `p+`. -/
def directNonclosurePPlus0 : ℝ := 31 / 80
def directNonclosurePPlus1 : ℝ := 3 / 8
def directNonclosurePPlus2 : ℝ := 7 / 80
def directNonclosurePPlus3 : ℝ := 3 / 20

/-- Frozen parameter-preserving witness `p-`. -/
def directNonclosurePMinus0 : ℝ := 33 / 80
def directNonclosurePMinus1 : ℝ := 9 / 40
def directNonclosurePMinus2 : ℝ := 5 / 16
def directNonclosurePMinus3 : ℝ := 1 / 20

/-- Every weight in the direct `p+` witness is strictly positive. -/
theorem directNonclosurePPlus_positive :
    0 < directNonclosurePPlus0 ∧
    0 < directNonclosurePPlus1 ∧
    0 < directNonclosurePPlus2 ∧
    0 < directNonclosurePPlus3 := by
  norm_num [directNonclosurePPlus0, directNonclosurePPlus1,
    directNonclosurePPlus2, directNonclosurePPlus3]

/-- Every weight in the direct `p-` witness is strictly positive. -/
theorem directNonclosurePMinus_positive :
    0 < directNonclosurePMinus0 ∧
    0 < directNonclosurePMinus1 ∧
    0 < directNonclosurePMinus2 ∧
    0 < directNonclosurePMinus3 := by
  norm_num [directNonclosurePMinus0, directNonclosurePMinus1,
    directNonclosurePMinus2, directNonclosurePMinus3]

/-- The direct `p+` witness is exactly normalized. -/
theorem directNonclosurePPlus_mass :
    fourPointMass
      directNonclosurePPlus0 directNonclosurePPlus1
      directNonclosurePPlus2 directNonclosurePPlus3 = 1 := by
  norm_num [fourPointMass, directNonclosurePPlus0, directNonclosurePPlus1,
    directNonclosurePPlus2, directNonclosurePPlus3]

/-- The direct `p-` witness is exactly normalized. -/
theorem directNonclosurePMinus_mass :
    fourPointMass
      directNonclosurePMinus0 directNonclosurePMinus1
      directNonclosurePMinus2 directNonclosurePMinus3 = 1 := by
  norm_num [fourPointMass, directNonclosurePMinus0, directNonclosurePMinus1,
    directNonclosurePMinus2, directNonclosurePMinus3]

/-- On support `{0,2,4,6}`, the direct `p+` witness has mean exactly `2`. -/
theorem directNonclosurePPlus_mean :
    fourPointEvenSupportMean
      directNonclosurePPlus0 directNonclosurePPlus1
      directNonclosurePPlus2 directNonclosurePPlus3 = 2 := by
  norm_num [fourPointEvenSupportMean, directNonclosurePPlus0,
    directNonclosurePPlus1, directNonclosurePPlus2, directNonclosurePPlus3]

/-- On support `{0,2,4,6}`, the direct `p-` witness has mean exactly `2`. -/
theorem directNonclosurePMinus_mean :
    fourPointEvenSupportMean
      directNonclosurePMinus0 directNonclosurePMinus1
      directNonclosurePMinus2 directNonclosurePMinus3 = 2 := by
  norm_num [fourPointEvenSupportMean, directNonclosurePMinus0,
    directNonclosurePMinus1, directNonclosurePMinus2, directNonclosurePMinus3]

/-- Both direct witnesses have the same base-`1/4` moment, exactly `313/640`. -/
theorem directNonclosurePPlus_quarterMoment :
    fourPointMoment (1 / 4 : ℝ)
      directNonclosurePPlus0 directNonclosurePPlus1
      directNonclosurePPlus2 directNonclosurePPlus3 = 313 / 640 := by
  norm_num [fourPointMoment, directNonclosurePPlus0, directNonclosurePPlus1,
    directNonclosurePPlus2, directNonclosurePPlus3]

theorem directNonclosurePMinus_quarterMoment :
    fourPointMoment (1 / 4 : ℝ)
      directNonclosurePMinus0 directNonclosurePMinus1
      directNonclosurePMinus2 directNonclosurePMinus3 = 313 / 640 := by
  norm_num [fourPointMoment, directNonclosurePMinus0, directNonclosurePMinus1,
    directNonclosurePMinus2, directNonclosurePMinus3]

/-- The base-`1/2` moments separate exactly. -/
theorem directNonclosurePPlus_halfMoment :
    fourPointMoment (1 / 2 : ℝ)
      directNonclosurePPlus0 directNonclosurePPlus1
      directNonclosurePPlus2 directNonclosurePPlus3 = 197 / 320 := by
  norm_num [fourPointMoment, directNonclosurePPlus0, directNonclosurePPlus1,
    directNonclosurePPlus2, directNonclosurePPlus3]

theorem directNonclosurePMinus_halfMoment :
    fourPointMoment (1 / 2 : ℝ)
      directNonclosurePMinus0 directNonclosurePMinus1
      directNonclosurePMinus2 directNonclosurePMinus3 = 39 / 64 := by
  norm_num [fourPointMoment, directNonclosurePMinus0, directNonclosurePMinus1,
    directNonclosurePMinus2, directNonclosurePMinus3]

/-- The base-`1/2` moment difference is exactly `1/160`. -/
theorem directNonclosure_halfMoment_difference :
    fourPointMoment (1 / 2 : ℝ)
        directNonclosurePPlus0 directNonclosurePPlus1
        directNonclosurePPlus2 directNonclosurePPlus3 -
      fourPointMoment (1 / 2 : ℝ)
        directNonclosurePMinus0 directNonclosurePMinus1
        directNonclosurePMinus2 directNonclosurePMinus3
      = 1 / 160 := by
  rw [directNonclosurePPlus_halfMoment, directNonclosurePMinus_halfMoment]
  norm_num

/--
The exact next-state exponential moments predicted by the updated support
`{1,2,3,4}` at `lambda = log 2` are `197/640` and `39/128`.
The analytic module will connect these rational values to `Real.exp`.
-/
theorem directNonclosurePPlus_nextMoment_rational :
    (1 / 2 : ℝ) *
      fourPointMoment (1 / 2 : ℝ)
        directNonclosurePPlus0 directNonclosurePPlus1
        directNonclosurePPlus2 directNonclosurePPlus3
      = 197 / 640 := by
  rw [directNonclosurePPlus_halfMoment]
  norm_num

theorem directNonclosurePMinus_nextMoment_rational :
    (1 / 2 : ℝ) *
      fourPointMoment (1 / 2 : ℝ)
        directNonclosurePMinus0 directNonclosurePMinus1
        directNonclosurePMinus2 directNonclosurePMinus3
      = 39 / 128 := by
  rw [directNonclosurePMinus_halfMoment]
  norm_num

/-- The exact next-state moment difference is `1/320`. -/
theorem directNonclosure_nextMoment_difference :
    (1 / 2 : ℝ) *
        fourPointMoment (1 / 2 : ℝ)
          directNonclosurePPlus0 directNonclosurePPlus1
          directNonclosurePPlus2 directNonclosurePPlus3 -
      (1 / 2 : ℝ) *
        fourPointMoment (1 / 2 : ℝ)
          directNonclosurePMinus0 directNonclosurePMinus1
          directNonclosurePMinus2 directNonclosurePMinus3
      = 1 / 320 := by
  rw [directNonclosurePPlus_nextMoment_rational,
    directNonclosurePMinus_nextMoment_rational]
  norm_num

/--
Finite rational core of the preferred MF-R049 witness.  It deliberately stops
before any use of `Real.exp` or `Real.log`.
-/
theorem directRationalNonclosureWitness :
    fourPointMass
        directNonclosurePPlus0 directNonclosurePPlus1
        directNonclosurePPlus2 directNonclosurePPlus3 = 1 ∧
    fourPointMass
        directNonclosurePMinus0 directNonclosurePMinus1
        directNonclosurePMinus2 directNonclosurePMinus3 = 1 ∧
    fourPointEvenSupportMean
        directNonclosurePPlus0 directNonclosurePPlus1
        directNonclosurePPlus2 directNonclosurePPlus3 =
      fourPointEvenSupportMean
        directNonclosurePMinus0 directNonclosurePMinus1
        directNonclosurePMinus2 directNonclosurePMinus3 ∧
    fourPointMoment (1 / 4 : ℝ)
        directNonclosurePPlus0 directNonclosurePPlus1
        directNonclosurePPlus2 directNonclosurePPlus3 =
      fourPointMoment (1 / 4 : ℝ)
        directNonclosurePMinus0 directNonclosurePMinus1
        directNonclosurePMinus2 directNonclosurePMinus3 ∧
    (1 / 2 : ℝ) *
        fourPointMoment (1 / 2 : ℝ)
          directNonclosurePPlus0 directNonclosurePPlus1
          directNonclosurePPlus2 directNonclosurePPlus3 ≠
      (1 / 2 : ℝ) *
        fourPointMoment (1 / 2 : ℝ)
          directNonclosurePMinus0 directNonclosurePMinus1
          directNonclosurePMinus2 directNonclosurePMinus3 := by
  refine ⟨directNonclosurePPlus_mass, directNonclosurePMinus_mass, ?_, ?_, ?_⟩
  · rw [directNonclosurePPlus_mean, directNonclosurePMinus_mean]
  · rw [directNonclosurePPlus_quarterMoment, directNonclosurePMinus_quarterMoment]
  · rw [directNonclosurePPlus_nextMoment_rational,
      directNonclosurePMinus_nextMoment_rational]
    norm_num

end

end PrecategoryFormal
