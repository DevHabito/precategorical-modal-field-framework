import PrecategoryFormal.EntropicScoreBridge

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

noncomputable section

/-- The declared centered half-contraction. -/
def centeredHalf (mean q : ℝ) : ℝ :=
  mean + (1 / 2 : ℝ) * (q - mean)

/-- The support `{0,2,4,6}` is sent exactly to `{1,2,3,4}` at common mean `2`. -/
theorem centeredHalf_even_support :
    centeredHalf 2 0 = 1 ∧
    centeredHalf 2 2 = 2 ∧
    centeredHalf 2 4 = 3 ∧
    centeredHalf 2 6 = 4 := by
  norm_num [centeredHalf]

/-- Exponential moment on an explicitly supplied four-point support. -/
def fourPointExpMoment
    (lambda q0 q1 q2 q3 p0 p1 p2 p3 : ℝ) : ℝ :=
  p0 * Real.exp (-q0 * lambda) +
  p1 * Real.exp (-q1 * lambda) +
  p2 * Real.exp (-q2 * lambda) +
  p3 * Real.exp (-q3 * lambda)

/-- Initial exponential moment of the direct plus witness at `lambda = log 2`. -/
theorem directNonclosurePPlus_initialExpMoment :
    fourPointExpMoment (Real.log 2) 0 2 4 6
      directNonclosurePPlus0 directNonclosurePPlus1
      directNonclosurePPlus2 directNonclosurePPlus3 = 313 / 640 := by
  unfold fourPointExpMoment
  rw [show Real.exp (-0 * Real.log 2) = (1 / 2 : ℝ) ^ 0 by
        simpa using exp_neg_nat_mul_log_two 0]
  rw [show Real.exp (-2 * Real.log 2) = (1 / 2 : ℝ) ^ 2 by
        simpa using exp_neg_nat_mul_log_two 2]
  rw [show Real.exp (-4 * Real.log 2) = (1 / 2 : ℝ) ^ 4 by
        simpa using exp_neg_nat_mul_log_two 4]
  rw [show Real.exp (-6 * Real.log 2) = (1 / 2 : ℝ) ^ 6 by
        simpa using exp_neg_nat_mul_log_two 6]
  norm_num [directNonclosurePPlus0, directNonclosurePPlus1,
    directNonclosurePPlus2, directNonclosurePPlus3]

/-- Initial exponential moment of the direct minus witness at `lambda = log 2`. -/
theorem directNonclosurePMinus_initialExpMoment :
    fourPointExpMoment (Real.log 2) 0 2 4 6
      directNonclosurePMinus0 directNonclosurePMinus1
      directNonclosurePMinus2 directNonclosurePMinus3 = 313 / 640 := by
  unfold fourPointExpMoment
  rw [show Real.exp (-0 * Real.log 2) = (1 / 2 : ℝ) ^ 0 by
        simpa using exp_neg_nat_mul_log_two 0]
  rw [show Real.exp (-2 * Real.log 2) = (1 / 2 : ℝ) ^ 2 by
        simpa using exp_neg_nat_mul_log_two 2]
  rw [show Real.exp (-4 * Real.log 2) = (1 / 2 : ℝ) ^ 4 by
        simpa using exp_neg_nat_mul_log_two 4]
  rw [show Real.exp (-6 * Real.log 2) = (1 / 2 : ℝ) ^ 6 by
        simpa using exp_neg_nat_mul_log_two 6]
  norm_num [directNonclosurePMinus0, directNonclosurePMinus1,
    directNonclosurePMinus2, directNonclosurePMinus3]

/-- The two direct witnesses therefore have the same initial entropic score. -/
theorem directNonclosure_initialScore_eq :
    entropicScoreFromMoment (Real.log 2)
        (fourPointExpMoment (Real.log 2) 0 2 4 6
          directNonclosurePPlus0 directNonclosurePPlus1
          directNonclosurePPlus2 directNonclosurePPlus3) =
      entropicScoreFromMoment (Real.log 2)
        (fourPointExpMoment (Real.log 2) 0 2 4 6
          directNonclosurePMinus0 directNonclosurePMinus1
          directNonclosurePMinus2 directNonclosurePMinus3) := by
  rw [directNonclosurePPlus_initialExpMoment,
    directNonclosurePMinus_initialExpMoment]

/-- Next exponential moment of the plus witness after the centered half-contraction. -/
theorem directNonclosurePPlus_nextExpMoment :
    fourPointExpMoment (Real.log 2)
      (centeredHalf 2 0) (centeredHalf 2 2)
      (centeredHalf 2 4) (centeredHalf 2 6)
      directNonclosurePPlus0 directNonclosurePPlus1
      directNonclosurePPlus2 directNonclosurePPlus3 = 197 / 640 := by
  rcases centeredHalf_even_support with ⟨h0, h1, h2, h3⟩
  rw [h0, h1, h2, h3]
  unfold fourPointExpMoment
  rw [show Real.exp (-1 * Real.log 2) = (1 / 2 : ℝ) ^ 1 by
        simpa using exp_neg_nat_mul_log_two 1]
  rw [show Real.exp (-2 * Real.log 2) = (1 / 2 : ℝ) ^ 2 by
        simpa using exp_neg_nat_mul_log_two 2]
  rw [show Real.exp (-3 * Real.log 2) = (1 / 2 : ℝ) ^ 3 by
        simpa using exp_neg_nat_mul_log_two 3]
  rw [show Real.exp (-4 * Real.log 2) = (1 / 2 : ℝ) ^ 4 by
        simpa using exp_neg_nat_mul_log_two 4]
  norm_num [directNonclosurePPlus0, directNonclosurePPlus1,
    directNonclosurePPlus2, directNonclosurePPlus3]

/-- Next exponential moment of the minus witness after the centered half-contraction. -/
theorem directNonclosurePMinus_nextExpMoment :
    fourPointExpMoment (Real.log 2)
      (centeredHalf 2 0) (centeredHalf 2 2)
      (centeredHalf 2 4) (centeredHalf 2 6)
      directNonclosurePMinus0 directNonclosurePMinus1
      directNonclosurePMinus2 directNonclosurePMinus3 = 39 / 128 := by
  rcases centeredHalf_even_support with ⟨h0, h1, h2, h3⟩
  rw [h0, h1, h2, h3]
  unfold fourPointExpMoment
  rw [show Real.exp (-1 * Real.log 2) = (1 / 2 : ℝ) ^ 1 by
        simpa using exp_neg_nat_mul_log_two 1]
  rw [show Real.exp (-2 * Real.log 2) = (1 / 2 : ℝ) ^ 2 by
        simpa using exp_neg_nat_mul_log_two 2]
  rw [show Real.exp (-3 * Real.log 2) = (1 / 2 : ℝ) ^ 3 by
        simpa using exp_neg_nat_mul_log_two 3]
  rw [show Real.exp (-4 * Real.log 2) = (1 / 2 : ℝ) ^ 4 by
        simpa using exp_neg_nat_mul_log_two 4]
  norm_num [directNonclosurePMinus0, directNonclosurePMinus1,
    directNonclosurePMinus2, directNonclosurePMinus3]

/-- The two next exponential moments are exactly unequal. -/
theorem directNonclosure_nextExpMoment_ne :
    fourPointExpMoment (Real.log 2)
        (centeredHalf 2 0) (centeredHalf 2 2)
        (centeredHalf 2 4) (centeredHalf 2 6)
        directNonclosurePPlus0 directNonclosurePPlus1
        directNonclosurePPlus2 directNonclosurePPlus3 ≠
      fourPointExpMoment (Real.log 2)
        (centeredHalf 2 0) (centeredHalf 2 2)
        (centeredHalf 2 4) (centeredHalf 2 6)
        directNonclosurePMinus0 directNonclosurePMinus1
        directNonclosurePMinus2 directNonclosurePMinus3 := by
  rw [directNonclosurePPlus_nextExpMoment,
    directNonclosurePMinus_nextExpMoment]
  norm_num

/-- The two next entropic scores are unequal at the same fixed `lambda = log 2`. -/
theorem directNonclosure_nextScore_ne :
    entropicScoreFromMoment (Real.log 2)
        (fourPointExpMoment (Real.log 2)
          (centeredHalf 2 0) (centeredHalf 2 2)
          (centeredHalf 2 4) (centeredHalf 2 6)
          directNonclosurePPlus0 directNonclosurePPlus1
          directNonclosurePPlus2 directNonclosurePPlus3) ≠
      entropicScoreFromMoment (Real.log 2)
        (fourPointExpMoment (Real.log 2)
          (centeredHalf 2 0) (centeredHalf 2 2)
          (centeredHalf 2 4) (centeredHalf 2 6)
          directNonclosurePMinus0 directNonclosurePMinus1
          directNonclosurePMinus2 directNonclosurePMinus3) := by
  apply entropicScoreFromMoment_ne_of_pos log_two_ne_zero
  · rw [directNonclosurePPlus_nextExpMoment]
    norm_num
  · rw [directNonclosurePMinus_nextExpMoment]
    norm_num
  · exact directNonclosure_nextExpMoment_ne

/--
End-to-end MF-R049 witness at the declared historical parameters
`lambda = log 2`, `a = 1/2`: the two strictly positive normalized distributions
have the same mean and the same initial entropic score, but different next
entropic scores after the centered half-contraction.
-/
theorem mf_r049_dynamic_nonclosure :
    directNonclosurePPlus_positive ∧
    directNonclosurePMinus_positive ∧
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
    entropicScoreFromMoment (Real.log 2)
        (fourPointExpMoment (Real.log 2) 0 2 4 6
          directNonclosurePPlus0 directNonclosurePPlus1
          directNonclosurePPlus2 directNonclosurePPlus3) =
      entropicScoreFromMoment (Real.log 2)
        (fourPointExpMoment (Real.log 2) 0 2 4 6
          directNonclosurePMinus0 directNonclosurePMinus1
          directNonclosurePMinus2 directNonclosurePMinus3) ∧
    entropicScoreFromMoment (Real.log 2)
        (fourPointExpMoment (Real.log 2)
          (centeredHalf 2 0) (centeredHalf 2 2)
          (centeredHalf 2 4) (centeredHalf 2 6)
          directNonclosurePPlus0 directNonclosurePPlus1
          directNonclosurePPlus2 directNonclosurePPlus3) ≠
      entropicScoreFromMoment (Real.log 2)
        (fourPointExpMoment (Real.log 2)
          (centeredHalf 2 0) (centeredHalf 2 2)
          (centeredHalf 2 4) (centeredHalf 2 6)
          directNonclosurePMinus0 directNonclosurePMinus1
          directNonclosurePMinus2 directNonclosurePMinus3) := by
  refine ⟨directNonclosurePPlus_positive, directNonclosurePMinus_positive,
    directNonclosurePPlus_mass, directNonclosurePMinus_mass, ?_,
    directNonclosure_initialScore_eq, directNonclosure_nextScore_ne⟩
  rw [directNonclosurePPlus_mean, directNonclosurePMinus_mean]

end

end PrecategoryFormal
