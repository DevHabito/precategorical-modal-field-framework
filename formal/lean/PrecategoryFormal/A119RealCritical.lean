import PrecategoryFormal.A119RealIntervalEvaluator
import PrecategoryFormal.A119CertifiedExpression

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 8000000

namespace PrecategoryFormal.A119RealCritical

open PrecategoryFormal.A119IntervalEvaluator
open PrecategoryFormal.A119CertifiedExpression
open PrecategoryFormal.A119RealIntervalCore
open PrecategoryFormal.A119RealIntervalEvaluator

/--
Real-number interpretation of the exact *reduced* A119 critical rational
expression; not a source-to-A115 coefficient derivation.
-/
noncomputable def criticalXiHatReal (s α : ℝ) (odd : Bool) (r : ℕ) : ℝ :=
  let beta : ℝ := 1/8
  let delta : ℝ := 1/1875
  let sigma : ℝ := if odd then 1/2 else 0
  let a : ℝ := if odd then (1+s)/2 else 1
  let B := beta/s + 2*delta
  let C := 1 - beta/s - 4*delta
  let A := a*(1-B)
  let D := (s^(r-2))⁻¹ - a*B
  let q := a*C/(A+α*D)
  let T := 1 - 2*delta
  let S := 1 - q - 2*delta
  let etaH := α^2+2*sigma*α
  let etaK := α^2+2*α*(sigma+(r:ℝ)-1)
  let B1 := 2*sigma*α*s*B - 2*a*α*beta/s
  let S1 := 2*sigma*α*s*T - 2*a*α - a*q*etaH
  let G2 := 2*α*(1+(1-s)*(α+2-sigma-(r:ℝ)))
  let main := (1-s)*α*(s^(r-2))⁻¹*q*etaH
  let sourceTerm := q*(a*B*G2-(1-s)*(α+1)*(B1+a*B*etaK))
  let target := (1-s)*(B1-S1)-2*α*s*a*(B-S)
  main + sourceTerm + target

/--
The rational-constant expression tree computes the *same* explicit
rational formula when its two variables are real numbers.
-/
theorem xiExpr_matches_real
    (s α : ℝ) (odd : Bool) (r : ℕ) :
    evalReal (xiExpr odd r) s α = criticalXiHatReal s α odd r := by
  cases odd <;>
    simp [xiExpr, evalReal, criticalXiHatReal, div_eq_mul_inv]
  all_goals ring

/--
If the existing exact rational interval evaluator reports a positive
enclosure, the result is strictly positive for *every real point* in
the two closed rational-endpoint input boxes. No density-only inference.
-/
theorem certified_box_sound_real
    (odd : Bool) (r : ℕ) (t₀ t₁ : ℚ) (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox odd r t₀ t₁) α)
    (hpass : passes odd r t₀ t₁ = true) :
    0 < criticalXiHatReal s α odd r := by
  unfold passes at hpass
  cases he : intervalValue (xiExpr odd r)
      sourceBox (alphaBox odd r t₀ t₁) with
  | none =>
      simp [he] at hpass
  | some box =>
      simp [he] at hpass
      have hlo : (0:ℝ) < (box.lo:ℝ) := by exact_mod_cast hpass
      have hinside : containsReal box (evalReal (xiExpr odd r) s α) :=
        intervalValue_sound_real (xiExpr odd r) sourceBox
          (alphaBox odd r t₀ t₁) s α hs hα box he
      rw [xiExpr_matches_real] at hinside
      exact lt_of_lt_of_le hlo hinside.1

/--
Concrete real-parameter consequence of one previously kernel-checked
rational certificate: every real point in the even r=4 upper-half box.
-/
theorem even_r4_upper_half_positive_real
    (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 4 (1/2) 1) α) :
    0 < criticalXiHatReal s α false 4 := by
  exact certified_box_sound_real false 4 (1/2) 1 s α hs hα
    PrecategoryFormal.A119BoxReplay.even_r4_upper_half_passes

end PrecategoryFormal.A119RealCritical
