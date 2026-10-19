import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
An independently derived, fully rational four-point witness for MF-R049.
The historical square-root witness remains unchanged.

The signed difference polynomial is
  D(t) = (t - 1)^2 * (t - 1/4) / 8.
Its double root at 1 preserves total mass and the first moment.
Its root at 1/4 preserves the initial exponential moment.
At 1/2 it is nonzero, so the rescaled moment differs.
-/

structure FourWeights where
  w0 : ℝ
  w1 : ℝ
  w2 : ℝ
  w3 : ℝ

def rationalPlus : FourWeights :=
  ⟨15 / 64, 22 / 64, 7 / 64, 20 / 64⟩

def rationalMinus : FourWeights :=
  ⟨17 / 64, 10 / 64, 25 / 64, 12 / 64⟩

def fourMass (p : FourWeights) : ℝ :=
  p.w0 + p.w1 + p.w2 + p.w3

def fourMean (p : FourWeights) : ℝ :=
  p.w1 + 2 * p.w2 + 3 * p.w3

def fourMoment (p : FourWeights) (t : ℝ) : ℝ :=
  p.w0 + p.w1 * t + p.w2 * t ^ 2 + p.w3 * t ^ 3

theorem rationalPlus_positive :
    0 < rationalPlus.w0 ∧ 0 < rationalPlus.w1 ∧
    0 < rationalPlus.w2 ∧ 0 < rationalPlus.w3 := by
  norm_num [rationalPlus]

theorem rationalMinus_positive :
    0 < rationalMinus.w0 ∧ 0 < rationalMinus.w1 ∧
    0 < rationalMinus.w2 ∧ 0 < rationalMinus.w3 := by
  norm_num [rationalMinus]

theorem rationalPlus_mass : fourMass rationalPlus = 1 := by
  norm_num [fourMass, rationalPlus]

theorem rationalMinus_mass : fourMass rationalMinus = 1 := by
  norm_num [fourMass, rationalMinus]

theorem rationalPlus_mean : fourMean rationalPlus = 3 / 2 := by
  norm_num [fourMean, rationalPlus]

theorem rationalMinus_mean : fourMean rationalMinus = 3 / 2 := by
  norm_num [fourMean, rationalMinus]

theorem rationalPlus_initial_moment :
    fourMoment rationalPlus (1 / 4) = 85 / 256 := by
  norm_num [fourMoment, rationalPlus]

theorem rationalMinus_initial_moment :
    fourMoment rationalMinus (1 / 4) = 85 / 256 := by
  norm_num [fourMoment, rationalMinus]

theorem rationalPlus_rescaled_moment :
    fourMoment rationalPlus (1 / 2) = 121 / 256 := by
  norm_num [fourMoment, rationalPlus]

theorem rationalMinus_rescaled_moment :
    fourMoment rationalMinus (1 / 2) = 119 / 256 := by
  norm_num [fourMoment, rationalMinus]

theorem rationalMoment_difference (t : ℝ) :
    fourMoment rationalPlus t - fourMoment rationalMinus t =
      (t - 1) ^ 2 * (t - 1 / 4) / 8 := by
  unfold fourMoment rationalPlus rationalMinus
  ring

theorem rationalInitialDataAgree :
    fourMass rationalPlus = fourMass rationalMinus ∧
    fourMean rationalPlus = fourMean rationalMinus ∧
    fourMoment rationalPlus (1 / 4) = fourMoment rationalMinus (1 / 4) := by
  constructor
  · rw [rationalPlus_mass, rationalMinus_mass]
  constructor
  · rw [rationalPlus_mean, rationalMinus_mean]
  · rw [rationalPlus_initial_moment, rationalMinus_initial_moment]

theorem rationalRescaledMomentsDiffer :
    fourMoment rationalPlus (1 / 2) ≠ fourMoment rationalMinus (1 / 2) := by
  rw [rationalPlus_rescaled_moment, rationalMinus_rescaled_moment]
  norm_num

end PrecategoryFormal
