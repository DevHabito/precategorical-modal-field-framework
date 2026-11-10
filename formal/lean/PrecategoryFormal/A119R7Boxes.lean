import PrecategoryFormal.A119CertifiedExpression

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 8000000

namespace PrecategoryFormal.A119R7Boxes

open PrecategoryFormal.A119CertifiedExpression

/-- Four exact rational-box checks at deficit r=7. -/
theorem even_left :
    passes false 7 0 (1/2) = true := by
  decide +kernel

theorem even_right :
    passes false 7 (1/2) 1 = true := by
  decide +kernel

theorem odd_left :
    passes true 7 0 (1/2) = true := by
  decide +kernel

theorem odd_right :
    passes true 7 (1/2) 1 = true := by
  decide +kernel

theorem even_full
    (s α : ℚ)
    (hs : 129/1000 ≤ s ∧ s ≤ 133/1000)
    (hα : 14 ≤ α ∧ α ≤ 84/5) :
    0 < PrecategoryFormal.A119CriticalExpression.criticalXiHat s α false 7 := by
  rcases PrecategoryFormal.A119Compact.half_split_covers
    (14:ℚ) (84/5:ℚ) α hα.1 hα.2 with hl | hr
  · exact certified_box_sound false 7 0 (1/2) s α hs
      (by constructor <;> norm_num [alphaBox] <;> linarith [hl.1, hl.2]) even_left
  · exact certified_box_sound false 7 (1/2) 1 s α hs
      (by constructor <;> norm_num [alphaBox] <;> linarith [hr.1, hr.2]) even_right

theorem odd_full
    (s α : ℚ)
    (hs : 129/1000 ≤ s ∧ s ≤ 133/1000)
    (hα : 15 ≤ α ∧ α ≤ 357/20) :
    0 < PrecategoryFormal.A119CriticalExpression.criticalXiHat s α true 7 := by
  rcases PrecategoryFormal.A119Compact.half_split_covers
    (15:ℚ) (357/20:ℚ) α hα.1 hα.2 with hl | hr
  · exact certified_box_sound true 7 0 (1/2) s α hs
      (by constructor <;> norm_num [alphaBox] <;> linarith [hl.1, hl.2]) odd_left
  · exact certified_box_sound true 7 (1/2) 1 s α hs
      (by constructor <;> norm_num [alphaBox] <;> linarith [hr.1, hr.2]) odd_right

end PrecategoryFormal.A119R7Boxes
