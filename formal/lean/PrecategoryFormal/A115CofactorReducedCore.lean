import Mathlib

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 1000000

namespace PrecategoryFormal.A115CofactorReducedCore

/--
The A115 cofactor when the three full-length powers beta^M, s^M
and tau^M are set to zero *only for this auxiliary identity*.
The exponentially small beta^k channel K is NOT discarded.
q denotes k/M, not the A118 exponential ratio.
-/
def reducedCofactor (x q u β s τ K W T U V : ℝ) : ℝ :=
  let A : ℝ := 1/2
  let Hb : ℝ := 1/2+u*U
  let Hs : ℝ := 1/2+u*V
  let Bb := u*K-1+q
  let Bs := u*W-1+q
  let Bt := u*T-1+q
  let Db := (β-1)*u*K+x
  let Ds := (s-1)*u*W+x
  let Dt := (τ-1)*u*T+x
  (A*Bb-Hb*Bt)*Ds+
    (-A*Db+Hb*Dt)*Bs+
    (-Bb*Dt+Bt*Db)*Hs

/-- Twice tau times the K-independent u-squared coefficient. -/
def coreTau (x q s τ W T U V : ℝ) : ℝ :=
  τ*T*(1-s)*(τ-s)*W+
    2*τ*T*x*(1-τ)*(U-V)+
    2*U*W*((s-τ)*(s-1)*(q-1)+x*(s*s-2*s+τ))

/-- Twice tau times the explicit beta-channel contribution. -/
def betaRemainderTau (x q β s τ W T V : ℝ) : ℝ :=
  -τ*T*(β-1)*(β-τ)-
    2*V*((q-1)*(β-1)*(β-τ)+x*(β*β-2*β+τ))-
    W*(s-β)*(β*s-τ)

/-- Twice tau times the exact u-cubic contribution. -/
def cubicRemainderTau (β s τ K W T U V : ℝ) : ℝ :=
  2*τ*T*(-K*V*(β-1)*(β-τ)+U*W*(s-1)*(s-τ))

/--
All polynomial cancellations are explicit. The three displayed
corrections must be bounded later. Nothing here claims that the
discarded full-length powers are zero in the original finite-M model.
-/
theorem exact_reduced_adjacent_core
    (x q u β s τ K W T U V : ℝ) :
    2*(τ*reducedCofactor x q u β s τ K W T U V -
        reducedCofactor x (q+x) u β s τ (β*K) (s*W) (τ*T) U V) =
      u^2*coreTau x q s τ W T U V +
      u^2*K*betaRemainderTau x q β s τ W T V +
      u^3*cubicRemainderTau β s τ K W T U V := by
  dsimp [reducedCofactor, coreTau, betaRemainderTau,
    cubicRemainderTau]
  ring

end PrecategoryFormal.A115CofactorReducedCore
