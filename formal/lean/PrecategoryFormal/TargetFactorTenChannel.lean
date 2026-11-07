import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.TargetFactor

/--
Universal cofactor-to-ten-channel identity for the A115 compressed
adjacent factor. The variables `bk`, `tk`, `sk` stand for the
exponential channels β^k, τ^k, s^k; `K` is the real cast of k;
`ab`, `aτ`, `as_` stand for (1-r^M)/M aτ the respective nodes.
No relations among the variables are needed.

This is an exact polynomial identity, NOT a theorem that a particular
primal or dual solution is feasible or globally optimal.
-/
theorem cofactor_ten_channel_identity
    (β τ s A Hβ Hs ab aτ as_ bk tk sk K : ℝ) :
    let Bb := bk - 1 + K * ab
    let Bt := tk - 1 + K * aτ
    let Bs := sk - 1 + K * as_
    let Db := (β - 1) * bk + ab
    let Dt := (τ - 1) * tk + aτ
    let Ds := (s - 1) * sk + as_
    let X := A * Bb - Hβ * Bt
    let Y := -A * Db + Hβ * Dt
    let W := -Bb * Dt + Bt * Db
    let cbs := A * (s - β)
    let cbt := Hs * (β - τ)
    let cst := Hβ * (τ - s)
    let cb := A * as_ + A * β - A - Hs * aτ - Hs * β + Hs
    let ckb := -(β - 1) * (A * as_ - Hs * aτ)
    let ct := -Hβ * as_ - Hβ * τ + Hβ + Hs * ab + Hs * τ - Hs
    let ckt := (τ - 1) * (Hβ * as_ - Hs * ab)
    let cs := -A * ab - A * s + A + Hβ * aτ + Hβ * s - Hβ
    let cks := (s - 1) * (A * ab - Hβ * aτ)
    let c1 := -A * as_ + A * ab + Hβ * as_ - Hβ * aτ - Hs * ab + Hs * aτ
    X * Ds + Y * Bs + W * Hs =
      cbs * bk * sk + cbt * bk * tk + cst * tk * sk +
      (cb + K * ckb) * bk + (ct + K * ckt) * tk +
      (cs + K * cks) * sk + c1 := by
  dsimp
  ring

/--
The actual 3x3 determinant behind the A115 cofactor combination.
Row order is (B_beta,B_tau,B_s), (H_beta,A,H_s),
(DeltaB_beta,DeltaB_tau,DeltaB_s). Its orientation is fixed
by this statement; swapping rows would reverse the sign.
This is determinant algebra, not yet a primal/dual sign theorem.
-/
theorem cofactor_factor_is_matrix_det
    (Bb Bt Bs Hb A Hs Db Dt Ds : ℝ) :
    Matrix.det
      (!![Bb, Bt, Bs; Hb, A, Hs; Db, Dt, Ds] :
        Matrix (Fin 3) (Fin 3) ℝ) =
      (A * Bb - Hb * Bt) * Ds +
      (-A * Db + Hb * Dt) * Bs +
      (-Bb * Dt + Bt * Db) * Hs := by
  simp [Matrix.det_fin_three]
  ring

end PrecategoryFormal.TargetFactor
