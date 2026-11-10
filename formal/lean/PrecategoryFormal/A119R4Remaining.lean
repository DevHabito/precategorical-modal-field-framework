import PrecategoryFormal.A119BoxReplay

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 8000000

namespace PrecategoryFormal.A119R4Remaining

open PrecategoryFormal.A119CertifiedExpression

/--
The remaining four r=4 rectangles of the 35-box A119 certificate.
Each theorem computes the rational interval expression in the Lean kernel.
No Python output is used as a proof hypothesis.
-/
theorem even_r4_left_passes :
    passes false 4 0 (1/4) = true := by
  decide +kernel

theorem even_r4_middle_passes :
    passes false 4 (1/4) (1/2) = true := by
  decide +kernel

theorem odd_r4_left_passes :
    passes true 4 0 (1/4) = true := by
  decide +kernel

theorem odd_r4_middle_passes :
    passes true 4 (1/4) (1/2) = true := by
  decide +kernel

/--
Every r=4 subdivision has a kernel-derived Boolean evaluation.
The two upper-half results are imported from the prior verified module.
These statements are still restricted to the rational Xi-hat expression.
-/
theorem even_r4_all_pass :
    passes false 4 0 (1/4) = true ∧
    passes false 4 (1/4) (1/2) = true ∧
    passes false 4 (1/2) 1 = true := by
  exact ⟨even_r4_left_passes,
    even_r4_middle_passes,
    PrecategoryFormal.A119BoxReplay.even_r4_upper_half_passes⟩

theorem odd_r4_all_pass :
    passes true 4 0 (1/4) = true ∧
    passes true 4 (1/4) (1/2) = true ∧
    passes true 4 (1/2) 1 = true := by
  exact ⟨odd_r4_left_passes,
    odd_r4_middle_passes,
    PrecategoryFormal.A119BoxReplay.odd_r4_upper_half_passes⟩

end PrecategoryFormal.A119R4Remaining
