import PrecategoryFormal.A115CollisionCoreFactor
import PrecategoryFormal.A119CriticalSubstitutionIdentity

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 2000000

namespace PrecategoryFormal.A118SourceFirstJet

open PrecategoryFormal.A119CriticalSubstitutionIdentity

/--
The coefficient obtained by the formal first-order product, reciprocal,
and chain rules applied to the A115 collision bracket at x=0.
Here z is a separate source contact factor s^(1-r).
This is an algebraic first-jet formula; its identification with a
real analytic derivative is a distinct proof obligation.
-/
noncomputable def sourceSlope
    (s α β δ a σ z e r : ℝ) : ℝ :=
  let b := σ+r-1
  let etaH := α^2+2*σ*α
  let etaK := α^2+2*α*b
  let B := β/s+2*δ
  let p := 2*σ*α*s
  let g0 := s*(s-1)*(α+1)
  let g1 := 2*s*α*(b*(s-1)+1)
  let H0 := a*((β-s)/s+4*δ+e)
  let H1 := p*((β-s)/s+4*δ)-2*a*α*(β-s)/s+a*e*etaH
  let U1 := p*B-2*a*α*β/s
  α*s*(1-s)*z*e*etaH-2*α*s*H0+(1-s)*H1+
    e/s*(U1*g0+a*B*etaK*g0-2*α*a*B*g0+a*B*g1)

/--
The published A118 parity-resolved expression, except that
s^(2-r) is represented by the independent algebraic factor s*z.
This avoids assuming a natural-power identity during the coefficient
comparison.
-/
noncomputable def xiBySourceZ
    (s α β δ a σ z e r : ℝ) : ℝ :=
  let B := β/s+2*δ
  let etaH := α^2+2*σ*α
  let etaK := α^2+2*α*(σ+r-1)
  let B1 := 2*σ*α*s*B-2*a*α*β/s
  let S1 := 2*σ*α*s*(1-2*δ)-2*a*α-a*e*etaH
  let G2 := 2*α*(1+(1-s)*(α+2-σ-r))
  let S0 := 1-e-2*δ
  (1-s)*α*s*z*e*etaH+
    e*(a*B*G2-(1-s)*(α+1)*(B1+a*B*etaK))+
    (1-s)*(B1-S1)-2*α*s*a*(B-S0)

/--
The first A115 source jet coincides exactly with the independent
published A118 coefficient formula in BOTH parities. The lemma
holds for arbitrary real sigma and a, hence also for both specified
parity choices. Division by s is explicit.
-/
theorem source_slope_equals_published_xi
    (s α β δ a σ z e r : ℝ) (hs : s ≠ 0) :
    sourceSlope s α β δ a σ z e r =
      xiBySourceZ s α β δ a σ z e r := by
  dsimp [sourceSlope, xiBySourceZ]
  field_simp [hs] <;> ring

/--
A complete algebraic bridge to the existing A118 definition:
the ONLY difference is the source contact identity
s*z = (s^(r-2))^-1. This equality is a source representation
condition, not an optimality assumption.
-/
theorem source_xi_minus_published
    (s α z e : ℝ) (odd : Bool) (r : ℕ) :
    xiBySourceZ s α (1/8) (1/1875)
        (if odd then (1+s)/2 else 1)
        (if odd then 1/2 else 0) z e r -
      xiPublished s α e odd r =
      (1-s)*α*e*(s*z-(s^(r-2))⁻¹) := by
  cases odd <;>
    simp [xiBySourceZ, xiPublished, div_eq_mul_inv] <;> ring

theorem source_slope_matches_a118
    (s α z e : ℝ) (odd : Bool) (r : ℕ)
    (hs : s ≠ 0)
    (hsource : s*z = (s^(r-2))⁻¹) :
    sourceSlope s α (1/8) (1/1875)
        (if odd then (1+s)/2 else 1)
        (if odd then 1/2 else 0) z e r =
      xiPublished s α e odd r := by
  rw [source_slope_equals_published_xi
    (hs := hs)]
  have h := source_xi_minus_published s α z e odd r
  rw [hsource, sub_self, mul_zero] at h
  exact sub_eq_zero.mp h

end PrecategoryFormal.A118SourceFirstJet
