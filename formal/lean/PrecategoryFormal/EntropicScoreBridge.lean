import PrecategoryFormal.EntropicNonclosureDirectWitness

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

noncomputable section

/-- Entropic score written as a function of one positive exponential moment. -/
def entropicScoreFromMoment (lambda moment : ℝ) : ℝ :=
  -Real.log moment / lambda

/-- `log 2` is strictly positive. -/
theorem log_two_pos : 0 < Real.log 2 := by
  exact Real.log_pos (by norm_num)

/-- In particular, `log 2` is nonzero. -/
theorem log_two_ne_zero : Real.log 2 ≠ 0 :=
  ne_of_gt log_two_pos

/-- The exact base identity used throughout the rationalized MF-R049 witness. -/
theorem exp_neg_log_two :
    Real.exp (-Real.log 2) = (1 / 2 : ℝ) := by
  calc
    Real.exp (-Real.log 2) = (Real.exp (Real.log 2))⁻¹ := Real.exp_neg _
    _ = (2 : ℝ)⁻¹ := by rw [Real.exp_log (by norm_num)]
    _ = (1 / 2 : ℝ) := by norm_num

/-- Integer multiples of `-log 2` give exact powers of `1/2`. -/
theorem exp_neg_nat_mul_log_two (n : ℕ) :
    Real.exp (-(n : ℝ) * Real.log 2) = (1 / 2 : ℝ) ^ n := by
  calc
    Real.exp (-(n : ℝ) * Real.log 2)
        = Real.exp ((n : ℝ) * (-Real.log 2)) := by
            congr 1
            ring
    _ = (Real.exp (-Real.log 2)) ^ n := Real.exp_nat_mul _ _
    _ = (1 / 2 : ℝ) ^ n := by rw [exp_neg_log_two]

/--
At a fixed nonzero parameter, the entropic score is injective in a positive
exponential moment.  This is only an analytic plumbing lemma; it carries no
closure or novelty claim.
-/
theorem entropicScoreFromMoment_injective_pos
    {lambda m₁ m₂ : ℝ}
    (hlambda : lambda ≠ 0)
    (hm₁ : 0 < m₁)
    (hm₂ : 0 < m₂)
    (hscore : entropicScoreFromMoment lambda m₁ =
      entropicScoreFromMoment lambda m₂) :
    m₁ = m₂ := by
  have hmul := congrArg (fun x : ℝ => x * lambda) hscore
  have hneglog : -Real.log m₁ = -Real.log m₂ := by
    simpa [entropicScoreFromMoment, hlambda] using hmul
  have hlog : Real.log m₁ = Real.log m₂ := by
    linarith
  have hexp := congrArg Real.exp hlog
  simpa [Real.exp_log hm₁, Real.exp_log hm₂] using hexp

/-- Distinct positive moments yield distinct scores at a fixed nonzero parameter. -/
theorem entropicScoreFromMoment_ne_of_pos
    {lambda m₁ m₂ : ℝ}
    (hlambda : lambda ≠ 0)
    (hm₁ : 0 < m₁)
    (hm₂ : 0 < m₂)
    (hm : m₁ ≠ m₂) :
    entropicScoreFromMoment lambda m₁ ≠
      entropicScoreFromMoment lambda m₂ := by
  intro hscore
  exact hm (entropicScoreFromMoment_injective_pos hlambda hm₁ hm₂ hscore)

end

end PrecategoryFormal
