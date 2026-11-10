import PrecategoryFormal.A118SourceFirstJet

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 5000000

namespace PrecategoryFormal.A118SourceContactPower

open PrecategoryFormal.A118SourceFirstJet
open PrecategoryFormal.A119CriticalSubstitutionIdentity

/--
For any real nonzero s, a finite contact shift satisfies the exact
source power identity. No asymptotic approximation is involved.
-/
theorem source_contact_reciprocal
    (s : ℝ) (n : ℕ) (hs : s ≠ 0) :
    s * (s^(n+1))⁻¹ = (s^n)⁻¹ := by
  rw [pow_succ, mul_inv_rev]
  calc
    s*(s⁻¹*(s^n)⁻¹) = (s*s⁻¹)*(s^n)⁻¹ := by ring
    _ = (s^n)⁻¹ := by simp [hs]

/--
Removes the auxiliary source-power hypothesis of the previous
source-slope-to-A118 coefficient identity for every actual contact
index r=n+2. Both parities are covered by the Bool parameter.
This is an equality of algebraic first-jet expressions; separate
differentiability and analytic remainder proofs remain open.
-/
theorem source_slope_equals_xi_at_contact
    (s α e : ℝ) (odd : Bool) (n : ℕ) (hs : s ≠ 0) :
    sourceSlope s α (1/8) (1/1875)
        (if odd then (1+s)/2 else 1)
        (if odd then 1/2 else 0)
        (s^(n+1))⁻¹ e (n+2) =
      xiPublished s α e odd (n+2) := by
  have hcontact :
      s*(s^(n+1))⁻¹ = (s^((n+2)-2))⁻¹ := by
    simpa using source_contact_reciprocal s n hs
  have hjet :
      sourceSlope s α (1/8) (1/1875)
          (if odd then (1+s)/2 else 1)
          (if odd then 1/2 else 0)
          (s^(n+1))⁻¹ e (↑(n+2):ℝ) =
        xiPublished s α e odd (n+2) :=
    source_slope_matches_a118 s α (s^(n+1))⁻¹ e
      odd (n+2) hs hcontact
  simpa only [Nat.cast_add, Nat.cast_ofNat] using hjet

end PrecategoryFormal.A118SourceContactPower
