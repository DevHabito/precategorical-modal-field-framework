import PrecategoryFormal.A115FullPowerTail

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 2000000

namespace PrecategoryFormal.A115FinitePowerDecomposition

open PrecategoryFormal.A115FullPowerTail
open PrecategoryFormal.A115CofactorReducedCore

/-- Degree-two contact polynomial for a node a in the exact cofactor. -/
def contactP (x q a τ : ℝ) : ℝ :=
  q*(a-1)*(a-τ)+x*(a*a-2*a+τ)

/-- Nonconfluent node separation factor. -/
def contactQ (a τ : ℝ) : ℝ := (a-1)*(a-τ)

/--
The full-length-power correction at order u⁰.
It retains the mixed vt*vs and vt*vb channels explicitly.
-/
def tailConstant (x τ vb vs vt : ℝ) : ℝ :=
  x*(τ-1)*vt*(vs-vb)

/--
The full-length-power correction at order u.
The nonlinear vb*vt and vs*vt terms must not be discarded.
-/
def tailLinear
    (x q β s τ K W T U V vb vs vt : ℝ) : ℝ :=
  vb*((τ-1)*x*(2*V-T*τ)+W*contactP x q s τ)+
  vs*((τ-1)*x*(T*τ-2*U)-K*contactP x q β τ)+
  vt*(K*(2*contactP x q β τ-contactQ β τ)+
      2*x*(τ-1)*(U-V)+
      W*(contactQ s τ-2*contactP x q s τ))+
  vb*vt*W*contactP x q s τ-
  vs*vt*K*contactP x q β τ

/-- Full-length-power correction at order u². -/
def tailQuadratic
    (x q β s τ K W T U V vb vs vt : ℝ) : ℝ :=
  2*T*τ*x*(τ-1)*(vs*U-vb*V)+
  vt*(2*K*V*contactP x q β τ+
      K*W*(β-s)*(β*s-τ)-
      2*U*W*contactP x q s τ)

/--
Exact finite-power correction, without any asymptotic truncation:
twice the tau-rescaled adjacent FULL cofactor minus the same
adjacent auxiliary cofactor equals C0+u*C1+u²*C2.

The original source has vb=beta^M, vs=s^M and vt=tau^M;
these remain independent polynomial variables in the theorem.
-/
theorem exact_full_power_correction
    (x q u β s τ K W T U V vb vs vt : ℝ) :
    2*(τ*(fullCofactor x q u β s τ K W T U V vb vs vt -
           reducedCofactor x q u β s τ K W T U V)-
       (fullCofactor x (q+x) u β s τ
          (β*K) (s*W) (τ*T) U V vb vs vt -
        reducedCofactor x (q+x) u β s τ
          (β*K) (s*W) (τ*T) U V)) =
      tailConstant x τ vb vs vt+
      u*tailLinear x q β s τ K W T U V vb vs vt+
      u^2*tailQuadratic x q β s τ K W T U V vb vs vt := by
  dsimp [fullCofactor, reducedCofactor, tailConstant,
    tailLinear, tailQuadratic, contactP, contactQ]
  ring

/--
The correction vanishes identically at zero full-length powers.
This is a consistency check, not a finite-M approximation.
-/
theorem no_tail_when_all_finite_powers_zero
    (x q u β s τ K W T U V : ℝ) :
    tailConstant x τ 0 0 0+
      u*tailLinear x q β s τ K W T U V 0 0 0+
      u^2*tailQuadratic x q β s τ K W T U V 0 0 0 = 0 := by
  simp [tailConstant, tailLinear, tailQuadratic]

/-- At u=0 the mixed full-length-power residue remains explicit. -/
theorem zero_u_mixed_power_term
    (x q β s τ K W T U V vb vs vt : ℝ) :
    tailConstant x τ vb vs vt+
      (0:ℝ)*tailLinear x q β s τ K W T U V vb vs vt+
      (0:ℝ)^2*tailQuadratic x q β s τ K W T U V vb vs vt =
      x*(τ-1)*vt*(vs-vb) := by
  simp [tailConstant]

end PrecategoryFormal.A115FinitePowerDecomposition
