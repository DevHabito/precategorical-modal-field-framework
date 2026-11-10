import PrecategoryFormal.A119R4Remaining

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.A119R4Coverage

open PrecategoryFormal.A119CertifiedExpression

/--
Six rational interval certificates and their shared endpoints cover the
entire r=4 enlarged alpha range, separately for each parity.
No half-open endpoint is silently discarded.
-/
theorem even_r4_complete
    (s α : ℚ)
    (hs : 129/1000 ≤ s ∧ s ≤ 133/1000)
    (hα : 8 ≤ α ∧ α ≤ 21/2) :
    0 < PrecategoryFormal.A119CriticalExpression.criticalXiHat s α false 4 := by
  rcases PrecategoryFormal.A119Compact.quarter_half_split_covers
    (8:ℚ) (21/2:ℚ) α hα.1 hα.2 with hleft | hmid | hright
  · exact certified_box_sound false 4 0 (1/4) s α hs
      (by constructor <;> norm_num [alphaBox] <;> linarith [hleft.1, hleft.2])
      PrecategoryFormal.A119R4Remaining.even_r4_left_passes
  · exact certified_box_sound false 4 (1/4) (1/2) s α hs
      (by constructor <;> norm_num [alphaBox] <;> linarith [hmid.1, hmid.2])
      PrecategoryFormal.A119R4Remaining.even_r4_middle_passes
  · exact certified_box_sound false 4 (1/2) 1 s α hs
      (by constructor <;> norm_num [alphaBox] <;> linarith [hright.1, hright.2])
      PrecategoryFormal.A119BoxReplay.even_r4_upper_half_passes

theorem odd_r4_complete
    (s α : ℚ)
    (hs : 129/1000 ≤ s ∧ s ≤ 133/1000)
    (hα : 9 ≤ α ∧ α ≤ 231/20) :
    0 < PrecategoryFormal.A119CriticalExpression.criticalXiHat s α true 4 := by
  rcases PrecategoryFormal.A119Compact.quarter_half_split_covers
    (9:ℚ) (231/20:ℚ) α hα.1 hα.2 with hleft | hmid | hright
  · exact certified_box_sound true 4 0 (1/4) s α hs
      (by constructor <;> norm_num [alphaBox] <;> linarith [hleft.1, hleft.2])
      PrecategoryFormal.A119R4Remaining.odd_r4_left_passes
  · exact certified_box_sound true 4 (1/4) (1/2) s α hs
      (by constructor <;> norm_num [alphaBox] <;> linarith [hmid.1, hmid.2])
      PrecategoryFormal.A119R4Remaining.odd_r4_middle_passes
  · exact certified_box_sound true 4 (1/2) 1 s α hs
      (by constructor <;> norm_num [alphaBox] <;> linarith [hright.1, hright.2])
      PrecategoryFormal.A119BoxReplay.odd_r4_upper_half_passes

end PrecategoryFormal.A119R4Coverage
