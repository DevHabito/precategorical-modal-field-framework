import PrecategoryFormal.CompressedAdjacentObjective

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.CompressedAdjacency

/--
This is the promised bridge from the two *actual* active band
equations at adjacent contacts to the E factor. No Cramer
numerator is an input hypothesis: it is derived using
active_band_objective_value.

This compares two algebraic compressed candidates, not two
certified global LP optima.
-/
theorem active_band_adjacent_objective_difference
    (Bb Bs Bt Db Ds Dt Hb Hs Cb Cs A t z tnext znext : ℝ)
    (hdet : Bb * Hs - Bs * Hb ≠ 0)
    (hdetnext : (Bb + Db) * Hs - (Bs + Ds) * Hb ≠ 0)
    (hbeta : Bb * z + Hb * t = Cb)
    (hs : Bs * z + Hs * t = Cs)
    (hbetanext : (Bb + Db) * znext + Hb * tnext = Cb)
    (hsnext : (Bs + Ds) * znext + Hs * tnext = Cs) :
    ((A * tnext + (Bt + Dt) * znext) -
      (A * t + Bt * z)) *
      ((Bb * Hs - Bs * Hb) *
        ((Bb + Db) * Hs - (Bs + Ds) * Hb)) =
      -(Cb * Hs - Cs * Hb) *
        ((A * Bb - Hb * Bt) * Ds +
          (-A * Db + Hb * Dt) * Bs +
          (-Bb * Dt + Bt * Db) * Hs) := by
  have hV :
      A * t + Bt * z =
        (A * (Bb * Cs - Bs * Cb) +
          Bt * (Cb * Hs - Cs * Hb)) /
          (Bb * Hs - Bs * Hb) :=
    active_band_objective_value Bb Bs Bt Hb Hs Cb Cs A t z
      hdet hbeta hs
  have hVnext :
      A * tnext + (Bt + Dt) * znext =
        (A * ((Bb + Db) * Cs - (Bs + Ds) * Cb) +
          (Bt + Dt) * (Cb * Hs - Cs * Hb)) /
          ((Bb + Db) * Hs - (Bs + Ds) * Hb) :=
    active_band_objective_value (Bb + Db) (Bs + Ds) (Bt + Dt)
      Hb Hs Cb Cs A tnext znext hdetnext hbetanext hsnext
  rw [hVnext, hV]
  exact compressed_objective_difference_identity
    Bb Bs Bt Db Ds Dt Hb Hs Cb Cs A hdet hdetnext

/--
For candidates solving the stated active band equalities, this
conditional theorem transfers the sign of E to the actual
objective. It has two separate orientation hypotheses:
Z<0 and the product of Cramer determinants is positive.
Those cannot be silently dropped.
-/
theorem active_band_adjacent_objective_sign_iff
    (Bb Bs Bt Db Ds Dt Hb Hs Cb Cs A t z tnext znext : ℝ)
    (hdet : Bb * Hs - Bs * Hb ≠ 0)
    (hdetnext : (Bb + Db) * Hs - (Bs + Ds) * Hb ≠ 0)
    (hbeta : Bb * z + Hb * t = Cb)
    (hs : Bs * z + Hs * t = Cs)
    (hbetanext : (Bb + Db) * znext + Hb * tnext = Cb)
    (hsnext : (Bs + Ds) * znext + Hs * tnext = Cs)
    (hZ : Cb * Hs - Cs * Hb < 0)
    (hprod : 0 <
      (Bb * Hs - Bs * Hb) *
        ((Bb + Db) * Hs - (Bs + Ds) * Hb)) :
    A * t + Bt * z < A * tnext + (Bt + Dt) * znext ↔
      0 < (A * Bb - Hb * Bt) * Ds +
        (-A * Db + Hb * Dt) * Bs +
        (-Bb * Dt + Bt * Db) * Hs := by
  have hidentity :=
    active_band_adjacent_objective_difference
      Bb Bs Bt Db Ds Dt Hb Hs Cb Cs A t z tnext znext
      hdet hdetnext hbeta hs hbetanext hsnext
  exact oriented_adjacent_sign_transfer
    (A * t + Bt * z)
    (A * tnext + (Bt + Dt) * znext)
    ((A * Bb - Hb * Bt) * Ds +
      (-A * Db + Hb * Dt) * Bs +
      (-Bb * Dt + Bt * Db) * Hs)
    (Cb * Hs - Cs * Hb)
    (Bb * Hs - Bs * Hb)
    ((Bb + Db) * Hs - (Bs + Ds) * Hb)
    hidentity hprod hZ

end PrecategoryFormal.CompressedAdjacency
