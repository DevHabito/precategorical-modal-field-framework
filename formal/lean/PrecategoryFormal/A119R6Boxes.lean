import PrecategoryFormal.A119CertifiedExpression

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 8000000

namespace PrecategoryFormal.A119R6Boxes

open PrecategoryFormal.A119CertifiedExpression

/-- Four exact rational enclosures at deficit r=6, split at alpha midpoint. -/
theorem even_left :
    passes false 6 0 (1/2) = true := by
  decide +kernel

theorem even_right :
    passes false 6 (1/2) 1 = true := by
  decide +kernel

theorem odd_left :
    passes true 6 0 (1/2) = true := by
  decide +kernel

theorem odd_right :
    passes true 6 (1/2) 1 = true := by
  decide +kernel

end PrecategoryFormal.A119R6Boxes
