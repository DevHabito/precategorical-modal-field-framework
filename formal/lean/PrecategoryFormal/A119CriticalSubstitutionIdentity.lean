import PrecategoryFormal.A119RealCritical

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 1000000

namespace PrecategoryFormal.A119CriticalSubstitutionIdentity

open PrecategoryFormal.A119RealCritical

/--
This is the published A117 leading-phase denominator A_p+alpha*D_p,r,
not a global LP determinant. It is separated for an explicit nonzero
assumption in the algebraic critical-surface substitution.
-/
noncomputable def criticalDenominator (s α : ℝ) (odd : Bool) (r : ℕ) : ℝ :=
  let beta : ℝ := 1/8
  let delta : ℝ := 1/1875
  let a : ℝ := if odd then (1+s)/2 else 1
  let B := beta/s+2*delta
  let A := a*(1-B)
  let D := (s^(r-2))⁻¹-a*B
  A+α*D

noncomputable def criticalNumerator (s : ℝ) (odd : Bool) : ℝ :=
  let beta : ℝ := 1/8
  let delta : ℝ := 1/1875
  let a : ℝ := if odd then (1+s)/2 else 1
  a*(1-beta/s-4*delta)

/--
A118's explicitly published parity-resolved second-order coefficient
with its unspecialized exponential ratio q. This is a *definition* of
the published formula, not a derivation of the formula from finite-M
cofactors.
-/
noncomputable def xiPublished (s α q : ℝ) (odd : Bool) (r : ℕ) : ℝ :=
  let beta : ℝ := 1/8
  let delta : ℝ := 1/1875
  let sigma : ℝ := if odd then 1/2 else 0
  let a : ℝ := if odd then (1+s)/2 else 1
  let B := beta/s + 2*delta
  let T := 1-2*delta
  let S := 1-q-2*delta
  let etaH := α^2+2*sigma*α
  let etaK := α^2+2*α*(sigma+(r:ℝ)-1)
  let B1 := 2*sigma*α*s*B - 2*a*α*beta/s
  let S1 := 2*sigma*α*s*T - 2*a*α - a*q*etaH
  let G2 := 2*α*(1+(1-s)*(α+2-sigma-(r:ℝ)))
  let main := (1-s)*α*(s^(r-2))⁻¹*q*etaH
  let sourceTerm := q*(a*B*G2-(1-s)*(α+1)*(B1+a*B*etaK))
  let target := (1-s)*(B1-S1)-2*α*s*a*(B-S)
  main+sourceTerm+target

/--
Pure rational algebra: under the *exact* critical A117 equation and
a nonzero denominator, the explicitly published A118 second-order
coefficient equals the independently kernel-certified Xi-hat formula.
No asymptotic error bound is claimed.
-/
theorem published_xi_equals_critical_xihat
    (s α q : ℝ) (odd : Bool) (r : ℕ)
    (hcritical :
      q*criticalDenominator s α odd r =
        criticalNumerator s odd)
    (hdenom : criticalDenominator s α odd r ≠ 0) :
    xiPublished s α q odd r = criticalXiHatReal s α odd r := by
  have hq : q =
      criticalNumerator s odd / criticalDenominator s α odd r :=
    (eq_div_iff hdenom).2 hcritical
  rw [hq]
  cases odd
  · simp [xiPublished, criticalXiHatReal,
      criticalNumerator, criticalDenominator, div_eq_mul_inv]
    ring
  · simp [xiPublished, criticalXiHatReal,
      criticalNumerator, criticalDenominator, div_eq_mul_inv]
    ring

end PrecategoryFormal.A119CriticalSubstitutionIdentity
