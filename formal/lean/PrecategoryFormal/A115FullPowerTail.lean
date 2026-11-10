import PrecategoryFormal.A115CofactorReducedCore

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 1000000

namespace PrecategoryFormal.A115FullPowerTail

/--
A115 cofactor with all three finite full-length power channels retained:
vb=beta^M, vs=s^M, vt=tau^M, and bk=uK, sk=uW, tk=uT.
The scalar q is k/M, x is 1/M. U,V are central response factors.
-/
def fullCofactor
    (x q u β s τ K W T U V vb vs vt : ℝ) : ℝ :=
  let A : ℝ := (1+vt)/2
  let Hb : ℝ := 1/2+u*U
  let Hs : ℝ := 1/2+u*V
  let Bb := u*K-1+q*(1-vb)
  let Bs := u*W-1+q*(1-vs)
  let Bt := u*T-1+q*(1-vt)
  let Db := (β-1)*u*K+x*(1-vb)
  let Ds := (s-1)*u*W+x*(1-vs)
  let Dt := (τ-1)*u*T+x*(1-vt)
  (A*Bb-Hb*Bt)*Ds+
    (-A*Db+Hb*Dt)*Bs+
    (-Bb*Dt+Bt*Db)*Hs

/--
At u=0, with finite full-length powers STILL PRESENT, all terms
constant or linear in vb,vs,vt cancel in the scaled adjacent cofactor.
The exact leftover is the beta/source times target *quadratic* channel.

This is not the actual finite-M specialization: u=tau^h>0. It
isolates an exact finite-power cancellation that remains true before
bounding the u-dependent residual.
-/
theorem zero_u_full_length_residual
    (x q β s τ K W T U V vb vs vt : ℝ) :
    2*(τ*fullCofactor x q 0 β s τ K W T U V vb vs vt -
        fullCofactor x (q+x) 0 β s τ (β*K) (s*W) (τ*T)
          U V vb vs vt) =
      x*(τ-1)*vt*(vs-vb) := by
  dsimp [fullCofactor]
  ring

/--
Specializing the full finite-power cofactor to vb=vs=vt=0
recovers precisely the auxiliary reduced cofactor. No full-power
channel is silently dropped from the original definition.
-/
theorem full_specializes_to_reduced
    (x q u β s τ K W T U V : ℝ) :
    fullCofactor x q u β s τ K W T U V 0 0 0 =
      PrecategoryFormal.A115CofactorReducedCore.reducedCofactor
        x q u β s τ K W T U V := by
  dsimp [fullCofactor,
    PrecategoryFormal.A115CofactorReducedCore.reducedCofactor]
  ring

end PrecategoryFormal.A115FullPowerTail
