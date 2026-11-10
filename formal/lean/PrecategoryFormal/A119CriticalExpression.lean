import PrecategoryFormal.A119IntervalArithmetic

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.A119CriticalExpression

/--
Exact rational critical-substitution expression from the published A118/A119
formula. This is a *definition* of the expression, not a derivation from A115
or a statement about the unrestricted F2/F3 optimizer.

odd=false means even M; odd=true means odd M.
Only r >= 2 is intended, so s^(r-2) encodes s^(r-2) with a reciprocal.
-/
def criticalXiHat (s α : ℚ) (odd : Bool) (r : ℕ) : ℚ :=
  let beta : ℚ := 1/8
  let delta : ℚ := 1/1875
  let sigma : ℚ := if odd then 1/2 else 0
  let a : ℚ := if odd then (1+s)/2 else 1
  let B := beta/s + 2*delta
  let C := 1 - beta/s - 4*delta
  let A := a*(1-B)
  let D := (s^(r-2))⁻¹ - a*B
  let q := a*C/(A+α*D)
  let T := 1 - 2*delta
  let S := 1 - q - 2*delta
  let etaH := α^2+2*sigma*α
  let etaK := α^2+2*α*(sigma+(r:ℚ)-1)
  let B1 := 2*sigma*α*s*B - 2*a*α*beta/s
  let S1 := 2*sigma*α*s*T - 2*a*α - a*q*etaH
  let G2 := 2*α*(1+(1-s)*(α+2-sigma-(r:ℚ)))
  let main := (1-s)*α*(s^(r-2))⁻¹*q*etaH
  let source := q*(a*B*G2-(1-s)*(α+1)*(B1+a*B*etaK))
  let target := (1-s)*(B1-S1)-2*α*s*a*(B-S)
  main + source + target

/--
A direct exact evaluation at one even-parity rational input, reconstructed
independently with Python Fraction before it was placed in this module.
The point need not satisfy Lambda=0: this validates the *rational formula*.
-/
theorem even_r4_anchor :
    criticalXiHat (129/1000) 8 false 4 =
      (51866142966881744 : ℚ) / 24790160053359375 := by
  norm_num [criticalXiHat]

/-- The exact corresponding odd-parity anchor, at a different alpha. -/
theorem odd_r4_anchor :
    criticalXiHat (129/1000) 9 true 4 =
      (2429919448126013663457 : ℚ) / 1560406595032373046875 := by
  norm_num [criticalXiHat]

/--
These exact rational instances are positive. They are not a 35-box
positivity theorem, and cannot replace the interval inclusion proof.
-/
theorem anchors_positive :
    0 < criticalXiHat (129/1000) 8 false 4 ∧
      0 < criticalXiHat (129/1000) 9 true 4 := by
  rw [even_r4_anchor, odd_r4_anchor]
  constructor <;> norm_num

end PrecategoryFormal.A119CriticalExpression
