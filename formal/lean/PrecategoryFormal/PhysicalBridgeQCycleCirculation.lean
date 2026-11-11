import Mathlib

namespace PrecategoryFormal.PhysicalBridge

/--
Independent row offsets cancel in a three-cycle reciprocal score circulation.

This is the finite algebraic core of the gauge-invariant cycle quantity.
-/
theorem triangle_q_circulation_row_gauge_invariant
    (q01 q10 q12 q21 q20 q02 c0 c1 c2 : ℚ) :
    ((q01 + c0) - (q10 + c1))
      + ((q12 + c1) - (q21 + c2))
      + ((q20 + c2) - (q02 + c0))
    =
    (q01 - q10) + (q12 - q21) + (q20 - q02) := by
  ring

/--
Reversing a three-cycle changes the sign of its reciprocal q circulation.
-/
theorem triangle_q_circulation_reversal
    (q01 q10 q12 q21 q20 q02 : ℚ) :
    (q10 - q01) + (q21 - q12) + (q02 - q20)
    =
    -((q01 - q10) + (q12 - q21) + (q20 - q02)) := by
  ring

/--
A scalar potential difference has zero circulation around a three-cycle.
-/
theorem triangle_gradient_has_zero_circulation
    (phi0 phi1 phi2 : ℚ) :
    (phi1 - phi0) + (phi2 - phi1) + (phi0 - phi2) = 0 := by
  ring

end PrecategoryFormal.PhysicalBridge
