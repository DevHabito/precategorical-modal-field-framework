import PrecategoryFormal.A119CertifiedExpression

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 8000000

namespace PrecategoryFormal.A119R8R12Boxes

open PrecategoryFormal.A119CertifiedExpression

/-! For r=8,...,12 each parity has one unsplit enlarged critical alpha
rectangle. These rational computations depend on the proved fail-closed
interval evaluator; no external Fraction result is a hypothesis. -/

theorem even_r8_passes :
    passes false 8 0 1 = true := by
  decide +kernel

theorem odd_r8_passes :
    passes true 8 0 1 = true := by
  decide +kernel

theorem even_r9_passes :
    passes false 9 0 1 = true := by
  decide +kernel

theorem odd_r9_passes :
    passes true 9 0 1 = true := by
  decide +kernel

theorem even_r10_passes :
    passes false 10 0 1 = true := by
  decide +kernel

theorem odd_r10_passes :
    passes true 10 0 1 = true := by
  decide +kernel

theorem even_r11_passes :
    passes false 11 0 1 = true := by
  decide +kernel

theorem odd_r11_passes :
    passes true 11 0 1 = true := by
  decide +kernel

theorem even_r12_passes :
    passes false 12 0 1 = true := by
  decide +kernel

theorem odd_r12_passes :
    passes true 12 0 1 = true := by
  decide +kernel

end PrecategoryFormal.A119R8R12Boxes
