import PrecategoryFormal.A119CertifiedExpression

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 8000000

namespace PrecategoryFormal.A119OddR13R19

open PrecategoryFormal.A119CertifiedExpression

/-!
The seven remaining high-contact odd-parity boxes of the A119 35-box
certificate. The exact evaluator computes the entire Xi-hat rational
formula with source s in [129/1000,133/1000] and each *unsplit*
r-specific enlarged critical alpha interval.

The complete Lean proof here is a Boolean kernel-reduced rational
interval inclusion check, not an axiom, a Python result, or an F3 claim.
-/

theorem odd_r13_passes :
    passes true 13 0 1 = true := by
  decide +kernel

theorem odd_r14_passes :
    passes true 14 0 1 = true := by
  decide +kernel

theorem odd_r15_passes :
    passes true 15 0 1 = true := by
  decide +kernel

theorem odd_r16_passes :
    passes true 16 0 1 = true := by
  decide +kernel

theorem odd_r17_passes :
    passes true 17 0 1 = true := by
  decide +kernel

theorem odd_r18_passes :
    passes true 18 0 1 = true := by
  decide +kernel

theorem odd_r19_passes :
    passes true 19 0 1 = true := by
  decide +kernel

end PrecategoryFormal.A119OddR13R19
