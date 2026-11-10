import Mathlib

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 2000000

namespace PrecategoryFormal.A115CollisionCoreFactor

/--
The exact normalized K-independent A115 core, with fk=W/T supplied
aSource its own contact-ratio variable; no Taylor approximation is used.
-/
noncomputable def collisionCore
    (x q s τ W fk U V : ℝ) : ℝ :=
  (1-s)*(τ-s)*W/2+
  x*(1-τ)*(U-V)+
  U*fk/τ*((s-τ)*(s-1)*(q-1)+x*(s*s-2*s+τ))

/--
The exact bracket after using tau=s(1+2alpha*x), q=1/2-b*x,
W=z*fh, fk=(s/tau)^k, and the untruncated leading central
responses U0,V0. The variables fh and fk are intentionally
independent: no exponential asymptotic is assumed.
-/
noncomputable def collisionBracket
    (x s α β δ aTarget aSource z b fh fk : ℝ) : ℝ :=
  let τ := s*(1+2*α*x)
  let U := aTarget*(β/τ+2*δ)
  let g0 := s*α*(s-1)+s*s-s
  let g1 := 2*s*α*(b*(s-1)+1)
  α*s*(1-s)*z*fh+
    (1-τ)*(aTarget*((β-s)/τ+4*δ)+aSource*fh)+
    U*fk/τ*(g0+x*g1)

/--
The A115 dominant core has an EXACT factor x=1/M.
No physical limit or term of order x was discarded.
-/
theorem exact_collision_x_factor
    (x s α β δ aTarget aSource z b fh fk : ℝ)
    (_hτ : s*(1+2*α*x) ≠ 0) :
    collisionCore x (1/2-b*x) s (s*(1+2*α*x))
      (z*fh) fk
      (aTarget*(β/(s*(1+2*α*x))+2*δ))
      (aTarget*(s/(s*(1+2*α*x))-2*δ)-aSource*fh) =
      x*collisionBracket x s α β δ aTarget aSource z b fh fk := by
  dsimp [collisionCore, collisionBracket]
  field_simp [_hτ]
  ring

/--
At x=0 and with both collision powers equal to e, the exact
source-derived bracket equals the published A117 leading phase.
Here z=s^(1-r), e=exp(-alpha), and a=a_p(s) may be substituted
*after* this general algebraic identity.
-/
theorem collision_zero_matches_A117_phase
    (s α β δ a z b e : ℝ) (hs : s ≠ 0) :
    collisionBracket 0 s α β δ a a z b e e =
      (1-s)*(-a*(1-β/s-4*δ)+
        e*(a*(1-(β/s+2*δ))+
          α*(s*z-a*(β/s+2*δ)))) := by
  dsimp [collisionBracket]
  field_simp [hs]
  ring

end PrecategoryFormal.A115CollisionCoreFactor
