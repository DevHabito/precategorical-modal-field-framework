import PrecategoryFormal.A119CertifiedExpression

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 8000000

namespace PrecategoryFormal.A119BoxReplay

open PrecategoryFormal.A119CertifiedExpression

/--
First direct, *kernel-reduced* replay of a full rational interval
Xi-hat box. No precomputed final bound is admitted as a hypothesis.
The box is even parity, r=4, upper half of its alpha interval.
-/
theorem even_r4_upper_half_passes :
    passes false 4 (1/2) 1 = true := by
  decide

/--
Unlike the old endpoint-positivity theorem, this claim combines the
symbolic rational expression, fail-closed interval evaluation and a
concrete source/alpha rectangle.
-/
theorem even_r4_upper_half_positive
    (s α : ℚ)
    (hs : 129/1000 ≤ s ∧ s ≤ 133/1000)
    (hα : (alphaBox false 4 (1/2) 1).lo ≤ α ∧
      α ≤ (alphaBox false 4 (1/2) 1).hi) :
    0 < PrecategoryFormal.A119CriticalExpression.criticalXiHat s α false 4 := by
  exact certified_box_sound false 4 (1/2) 1 s α hs hα
    even_r4_upper_half_passes

end PrecategoryFormal.A119BoxReplay
