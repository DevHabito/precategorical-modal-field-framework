import PrecategoryFormal.A119CertifiedExpression

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 8000000

namespace PrecategoryFormal.A119R5Boxes

open PrecategoryFormal.A119CertifiedExpression

/--
Four full rational interval evaluations of the A119 critical expression
at contact deficit r=5. They use kernel reduction (not native_decide).
The two closed pieces in each parity meet at their shared half endpoint.
-/
theorem even_left :
    passes false 5 0 (1/2) = true := by
  decide +kernel

theorem even_right :
    passes false 5 (1/2) 1 = true := by
  decide +kernel

theorem odd_left :
    passes true 5 0 (1/2) = true := by
  decide +kernel

theorem odd_right :
    passes true 5 (1/2) 1 = true := by
  decide +kernel

/-- Source-window positivity for all rational alpha in the even r=5 cell. -/
theorem even_full
    (s α : ℚ)
    (hs : 129/1000 ≤ s ∧ s ≤ 133/1000)
    (hα : 10 ≤ α ∧ α ≤ 63/5) :
    0 < PrecategoryFormal.A119CriticalExpression.criticalXiHat s α false 5 := by
  rcases PrecategoryFormal.A119Compact.half_split_covers
    (10:ℚ) (63/5:ℚ) α hα.1 hα.2 with hleft | hright
  · exact certified_box_sound false 5 0 (1/2) s α hs
      (by constructor <;> norm_num [alphaBox] <;> linarith [hleft.1, hleft.2])
      even_left
  · exact certified_box_sound false 5 (1/2) 1 s α hs
      (by constructor <;> norm_num [alphaBox] <;> linarith [hright.1, hright.2])
      even_right

/-- Source-window positivity for all rational alpha in the odd r=5 cell. -/
theorem odd_full
    (s α : ℚ)
    (hs : 129/1000 ≤ s ∧ s ≤ 133/1000)
    (hα : 11 ≤ α ∧ α ≤ 273/20) :
    0 < PrecategoryFormal.A119CriticalExpression.criticalXiHat s α true 5 := by
  rcases PrecategoryFormal.A119Compact.half_split_covers
    (11:ℚ) (273/20:ℚ) α hα.1 hα.2 with hleft | hright
  · exact certified_box_sound true 5 0 (1/2) s α hs
      (by constructor <;> norm_num [alphaBox] <;> linarith [hleft.1, hleft.2])
      odd_left
  · exact certified_box_sound true 5 (1/2) 1 s α hs
      (by constructor <;> norm_num [alphaBox] <;> linarith [hright.1, hright.2])
      odd_right

end PrecategoryFormal.A119R5Boxes
