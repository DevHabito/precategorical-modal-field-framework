import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.TargetFactor

/--
Universal cofactor-to-ten-channel identity for the A115 compressed
adjacent factor. The variables `bk`, `tk`, `sk` stand for the
exponential channels β^k, τ^k, s^k; `K` is the real cast of k;
`ab`, `at`, `as_` stand for (1-r^M)/M at the respective nodes.
No relations among the variables are needed.

This is an exact polynomial identity, NOT a theorem that a particular
primal or dual solution is feasible or globally optimal.
-/
theorem cofactor_ten_channel_identity
    (β τ s A Hβ Hs ab at as_ bk tk sk K : ℝ) :
    let Bb := bk - 1 + K * ab
    let Bt := tk - 1 + K * at
    let Bs := sk - 1 + K * as_
    let Db := (β - 1) * bk + ab
    let Dt := (τ - 1) * tk + at
    let Ds := (s - 1) * sk + as_
    let X := A * Bb - Hβ * Bt
    let Y := -A * Db + Hβ * Dt
    let W := -Bb * Dt + Bt * Db
    let cbs := A * (s - β)
    let cbt := Hs * (β - τ)
    let cst := Hβ * (τ - s)
    let cb := A * as_ + A * β - A - Hs * at - Hs * β + Hs
    let ckb := -(β - 1) * (A * as_ - Hs * at)
    let ct := -Hβ * as_ - Hβ * τ + Hβ + Hs * ab + Hs * τ - Hs
    let ckt := (τ - 1) * (Hβ * as_ - Hs * ab)
    let cs := -A * ab - A * s + A + Hβ * at + Hβ * s - Hβ
    let cks := (s - 1) * (A * ab - Hβ * at)
    let c1 := -A * as_ + A * ab + Hβ * as_ - Hβ * at - Hs * ab + Hs * at
    X * Ds + Y * Bs + W * Hs =
      cbs * bk * sk + cbt * bk * tk + cst * tk * sk +
      (cb + K * ckb) * bk + (ct + K * ckt) * tk +
      (cs + K * cks) * sk + c1 := by
  dsimp
  ring

end PrecategoryFormal.TargetFactor
