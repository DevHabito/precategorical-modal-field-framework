import PrecategoryFormal.DynamicNonclosure
import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
The analytic bridge for MF-R049. A four-point affine update is expressed
as an actual sum of four exponential terms, not defined by the desired
factorization. No floating-point approximation or native_decide is used.
-/

noncomputable def affineFourExponentialMoment
    (p : FourWeights) (lam scale shift : ℝ) : ℝ :=
  p.w0 * Real.exp (-lam * shift) +
  p.w1 * Real.exp (-lam * (scale + shift)) +
  p.w2 * Real.exp (-lam * (2 * scale + shift)) +
  p.w3 * Real.exp (-lam * (3 * scale + shift))

theorem affineFourExponentialMoment_factorization
    (p : FourWeights) (lam scale shift : ℝ) :
    affineFourExponentialMoment p lam scale shift =
      Real.exp (-lam * shift) *
        fourMoment p (Real.exp (-(scale * lam))) := by
  have h1 :
      Real.exp (-lam * (scale + shift)) =
        Real.exp (-lam * shift) * Real.exp (-(scale * lam)) := by
    rw [← Real.exp_add]
    congr 1
    ring
  have h2 :
      Real.exp (-lam * (2 * scale + shift)) =
        Real.exp (-lam * shift) * Real.exp (-(scale * lam)) ^ 2 := by
    calc
      Real.exp (-lam * (2 * scale + shift)) =
          Real.exp (-lam * shift) *
            Real.exp (-(scale * lam) + -(scale * lam)) := by
              rw [← Real.exp_add]
              congr 1
              ring
      _ = _ := by rw [Real.exp_add, pow_two]
  have h3 :
      Real.exp (-lam * (3 * scale + shift)) =
        Real.exp (-lam * shift) * Real.exp (-(scale * lam)) ^ 3 := by
    calc
      Real.exp (-lam * (3 * scale + shift)) =
          Real.exp (-lam * shift) *
            Real.exp (-(scale * lam) + -(scale * lam) + -(scale * lam)) := by
              rw [← Real.exp_add]
              congr 1
              ring
      _ = _ := by rw [Real.exp_add, Real.exp_add]; ring
  unfold affineFourExponentialMoment fourMoment
  rw [h1, h2, h3]
  ring

noncomputable def centeredFourExponentialMoment
    (p : FourWeights) (lam scale : ℝ) : ℝ :=
  affineFourExponentialMoment p lam scale
    ((1 - scale) * fourMean p)

theorem centeredFourExponentialMoment_transport
    (p : FourWeights) (lam scale : ℝ) :
    centeredFourExponentialMoment p lam scale =
      Real.exp (-lam * ((1 - scale) * fourMean p)) *
        fourMoment p (Real.exp (-(scale * lam))) := by
  exact affineFourExponentialMoment_factorization p lam scale
    ((1 - scale) * fourMean p)

noncomputable def rationalInitialLambda : ℝ := 2 * Real.log 2

theorem exp_neg_log_two :
    Real.exp (-Real.log (2 : ℝ)) = 1 / 2 := by
  rw [Real.exp_neg, Real.exp_log (by norm_num : (0 : ℝ) < 2)]
  norm_num

theorem rationalInitialLambda_pos : 0 < rationalInitialLambda := by
  unfold rationalInitialLambda
  have hlog : 0 < Real.log (2 : ℝ) :=
    Real.log_pos (by norm_num : (1 : ℝ) < 2)
  positivity

theorem initialExpFactor :
    Real.exp (-rationalInitialLambda) = 1 / 4 := by
  have h :
      -rationalInitialLambda =
        -Real.log (2 : ℝ) + -Real.log (2 : ℝ) := by
    unfold rationalInitialLambda
    ring
  rw [h, Real.exp_add, exp_neg_log_two]
  norm_num

theorem halfExpFactor :
    Real.exp (-((1 / 2 : ℝ) * rationalInitialLambda)) = 1 / 2 := by
  have h :
      -((1 / 2 : ℝ) * rationalInitialLambda) =
        -Real.log (2 : ℝ) := by
    unfold rationalInitialLambda
    ring
  rw [h, exp_neg_log_two]

noncomputable def rationalScore (p : FourWeights) (lam : ℝ) : ℝ :=
  -(Real.log (fourMoment p (Real.exp (-lam)))) / lam

theorem rationalScoresInitiallyEqual :
    rationalScore rationalPlus rationalInitialLambda =
      rationalScore rationalMinus rationalInitialLambda := by
  unfold rationalScore
  rw [initialExpFactor, rationalPlus_initial_moment,
    rationalMinus_initial_moment]

theorem rationalPlusFutureMoment :
    centeredFourExponentialMoment rationalPlus rationalInitialLambda (1 / 2) =
      Real.exp (-rationalInitialLambda * (3 / 4)) * (121 / 256) := by
  rw [centeredFourExponentialMoment_transport,
    rationalPlus_mean, halfExpFactor,
    rationalPlus_rescaled_moment]
  ring

theorem rationalMinusFutureMoment :
    centeredFourExponentialMoment rationalMinus rationalInitialLambda (1 / 2) =
      Real.exp (-rationalInitialLambda * (3 / 4)) * (119 / 256) := by
  rw [centeredFourExponentialMoment_transport,
    rationalMinus_mean, halfExpFactor,
    rationalMinus_rescaled_moment]
  ring

theorem rationalFutureMomentsDiffer :
    centeredFourExponentialMoment rationalPlus rationalInitialLambda (1 / 2) ≠
      centeredFourExponentialMoment rationalMinus rationalInitialLambda (1 / 2) := by
  rw [rationalPlusFutureMoment, rationalMinusFutureMoment]
  intro heq
  have hpositive : 0 < Real.exp (-rationalInitialLambda * (3 / 4)) :=
    Real.exp_pos _
  nlinarith

noncomputable def rationalFutureScore (p : FourWeights) : ℝ :=
  -(Real.log (centeredFourExponentialMoment p rationalInitialLambda (1 / 2))) /
    rationalInitialLambda

theorem rationalFutureScoresDiffer :
    rationalFutureScore rationalPlus ≠ rationalFutureScore rationalMinus := by
  have hplus :
      0 < centeredFourExponentialMoment rationalPlus rationalInitialLambda (1 / 2) := by
    rw [rationalPlusFutureMoment]
    positivity
  have hminus :
      0 < centeredFourExponentialMoment rationalMinus rationalInitialLambda (1 / 2) := by
    rw [rationalMinusFutureMoment]
    positivity
  have hlam : rationalInitialLambda ≠ 0 :=
    ne_of_gt rationalInitialLambda_pos
  intro heq
  have hlogs :
      Real.log (centeredFourExponentialMoment
          rationalPlus rationalInitialLambda (1 / 2)) =
        Real.log (centeredFourExponentialMoment
          rationalMinus rationalInitialLambda (1 / 2)) := by
    unfold rationalFutureScore at heq
    have hmul := congrArg (fun x : ℝ => x * rationalInitialLambda) heq
    have hneg :
        -Real.log (centeredFourExponentialMoment
            rationalPlus rationalInitialLambda (1 / 2)) =
          -Real.log (centeredFourExponentialMoment
            rationalMinus rationalInitialLambda (1 / 2)) := by
      simpa [hlam] using hmul
    exact neg_injective hneg
  have hmoments :
      centeredFourExponentialMoment rationalPlus rationalInitialLambda (1 / 2) =
        centeredFourExponentialMoment rationalMinus rationalInitialLambda (1 / 2) := by
    calc
      centeredFourExponentialMoment rationalPlus rationalInitialLambda (1 / 2) =
          Real.exp (Real.log (centeredFourExponentialMoment
            rationalPlus rationalInitialLambda (1 / 2))) :=
          (Real.exp_log hplus).symm
      _ = Real.exp (Real.log (centeredFourExponentialMoment
            rationalMinus rationalInitialLambda (1 / 2))) := by rw [hlogs]
      _ = centeredFourExponentialMoment rationalMinus rationalInitialLambda
            (1 / 2) := Real.exp_log hminus
  exact rationalFutureMomentsDiffer hmoments

/-- MF-R049: equal initial macrostates need not have equal future scores. -/
theorem rationalScalarNonclosure :
    fourMass rationalPlus = fourMass rationalMinus ∧
    fourMean rationalPlus = fourMean rationalMinus ∧
    rationalScore rationalPlus rationalInitialLambda =
      rationalScore rationalMinus rationalInitialLambda ∧
    rationalFutureScore rationalPlus ≠ rationalFutureScore rationalMinus := by
  constructor
  · rw [rationalPlus_mass, rationalMinus_mass]
  constructor
  · rw [rationalPlus_mean, rationalMinus_mean]
  constructor
  · exact rationalScoresInitiallyEqual
  · exact rationalFutureScoresDiffer

end PrecategoryFormal
