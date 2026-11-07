import PrecategoryFormal.TargetFactorTenChannel

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.CompressedAdjacency

/--
The actual two active-band equalities are
  B_beta(k) * z + H_beta * t = C_beta
  B_s(k) * z + H_s * t = C_s.
The compressed objective is V_k = A*t + B_tau(k)*z.
The next contact uses the same H and C and replaces each B_r(k)
by B_r(k)+DeltaB_r(k).

The following cross-multiplied identity is universal polynomial
algebra. In particular, it does not assume a priori that E is
an adjacent value difference, that the bases are feasible, or
that the active bands are valid constraints of a global optimum.
-/
theorem exact_adjacent_cross_difference
    (Bb Bs Bt Db Ds Dt Hb Hs Cb Cs A : ℝ) :
    let Dk := Bb * Hs - Bs * Hb
    let Dnext := (Bb + Db) * Hs - (Bs + Ds) * Hb
    let Z := Cb * Hs - Cs * Hb
    let Nk := A * (Bb * Cs - Bs * Cb) + Bt * Z
    let Nnext := A * ((Bb + Db) * Cs - (Bs + Ds) * Cb) +
      (Bt + Dt) * Z
    let E := (A * Bb - Hb * Bt) * Ds +
      (-A * Db + Hb * Dt) * Bs +
      (-Bb * Dt + Bt * Db) * Hs
    Nnext * Dk - Nk * Dnext = -Z * E := by
  dsimp
  ring

/--
Purely rational cross multiplication: the denominators must
both be nonzero. Their *signs* are not assumed.
-/
theorem two_ratios_adjacent_cross_difference
    (n nnext d dnext : ℝ) (hd : d ≠ 0) (hdnext : dnext ≠ 0) :
    (nnext / dnext - n / d) * (d * dnext) =
      nnext * d - n * dnext := by
  field_simp [hd, hdnext]

/--
If the two candidate objective values have Cramer numerators
Nk,Nnext and nonzero determinants, the reduced-factor identity
is an *exact* equality of objective differences, not just a
sign-matching heuristic.
-/
theorem compressed_objective_difference_identity
    (Bb Bs Bt Db Ds Dt Hb Hs Cb Cs A : ℝ)
    (hDk : Bb * Hs - Bs * Hb ≠ 0)
    (hDnext : (Bb + Db) * Hs - (Bs + Ds) * Hb ≠ 0) :
    let Dk := Bb * Hs - Bs * Hb
    let Dnext := (Bb + Db) * Hs - (Bs + Ds) * Hb
    let Z := Cb * Hs - Cs * Hb
    let Nk := A * (Bb * Cs - Bs * Cb) + Bt * Z
    let Nnext := A * ((Bb + Db) * Cs - (Bs + Ds) * Cb) +
      (Bt + Dt) * Z
    let E := (A * Bb - Hb * Bt) * Ds +
      (-A * Db + Hb * Dt) * Bs +
      (-Bb * Dt + Bt * Db) * Hs
    (Nnext / Dnext - Nk / Dk) * (Dk * Dnext) = -Z * E := by
  dsimp
  calc
    ((A * ((Bb + Db) * Cs - (Bs + Ds) * Cb) +
        (Bt + Dt) * (Cb * Hs - Cs * Hb)) /
        ((Bb + Db) * Hs - (Bs + Ds) * Hb) -
      (A * (Bb * Cs - Bs * Cb) +
        Bt * (Cb * Hs - Cs * Hb)) / (Bb * Hs - Bs * Hb)) *
        ((Bb * Hs - Bs * Hb) *
          ((Bb + Db) * Hs - (Bs + Ds) * Hb)) =
        (A * ((Bb + Db) * Cs - (Bs + Ds) * Cb) +
            (Bt + Dt) * (Cb * Hs - Cs * Hb)) *
            (Bb * Hs - Bs * Hb) -
        (A * (Bb * Cs - Bs * Cb) +
            Bt * (Cb * Hs - Cs * Hb)) *
            ((Bb + Db) * Hs - (Bs + Ds) * Hb) := by
            exact two_ratios_adjacent_cross_difference
              _ _ _ _ hDk hDnext
    _ = -(Cb * Hs - Cs * Hb) *
          ((A * Bb - Hb * Bt) * Ds +
            (-A * Db + Hb * Dt) * Bs +
            (-Bb * Dt + Bt * Db) * Hs) := by
          simpa only [] using
            exact_adjacent_cross_difference
              Bb Bs Bt Db Ds Dt Hb Hs Cb Cs A

/--
The SIGN of E agrees with the direction of the candidate
objective exactly under this explicitly oriented factor:
Z<0 and Dk*Dnext>0. These hypotheses must be proved
from the model in a later theorem before using this to select
an optimal contact.
-/
theorem oriented_adjacent_sign_transfer
    (V Vnext E Z d dnext : ℝ)
    (hidentity : (Vnext - V) * (d * dnext) = -Z * E)
    (hdet : 0 < d * dnext) (hZ : Z < 0) :
    (V < Vnext ↔ 0 < E) := by
  constructor
  · intro hv
    have hmul : 0 < (Vnext - V) * (d * dnext) :=
      mul_pos (sub_pos.mpr hv) hdet
    rw [hidentity] at hmul
    by_contra hneg
    have hE : E ≤ 0 := le_of_not_gt hneg
    have hwrong : (-Z) * E ≤ 0 :=
      mul_nonpos_of_nonneg_of_nonpos (le_of_lt (neg_pos.mpr hZ)) hE
    linarith
  · intro hE
    have hmul : 0 < (-Z) * E := mul_pos (neg_pos.mpr hZ) hE
    rw [← hidentity] at hmul
    by_contra hneg
    have hnot : Vnext - V ≤ 0 := sub_nonpos.mpr (le_of_not_gt hneg)
    have hwrong : (Vnext - V) * (d * dnext) ≤ 0 :=
      mul_nonpos_of_nonpos_of_nonneg hnot (le_of_lt hdet)
    linarith

/--
The two active band equalities *force* the Cramer formulas for
the scaled total mass t and the interior P mass z. The condition
D != 0 is explicit and no primal nonnegativity or KKT property
is inferred.
-/
theorem active_band_cramer_solution
    (Bb Bs Hb Hs Cb Cs t z : ℝ)
    (hdet : Bb * Hs - Bs * Hb ≠ 0)
    (hbeta : Bb * z + Hb * t = Cb)
    (hs : Bs * z + Hs * t = Cs) :
    z = (Cb * Hs - Cs * Hb) / (Bb * Hs - Bs * Hb) ∧
      t = (Bb * Cs - Bs * Cb) / (Bb * Hs - Bs * Hb) := by
  have hz : z * (Bb * Hs - Bs * Hb) = Cb * Hs - Cs * Hb := by
    calc
      z * (Bb * Hs - Bs * Hb) =
          Hs * (Bb * z + Hb * t) - Hb * (Bs * z + Hs * t) := by
            ring
      _ = Cb * Hs - Cs * Hb := by
        rw [hbeta, hs]
        ring
  have ht : t * (Bb * Hs - Bs * Hb) = Bb * Cs - Bs * Cb := by
    calc
      t * (Bb * Hs - Bs * Hb) =
          Bb * (Bs * z + Hs * t) - Bs * (Bb * z + Hb * t) := by
            ring
      _ = Bb * Cs - Bs * Cb := by
        rw [hbeta, hs]
        ring
  exact ⟨(eq_div_iff hdet).2 hz, (eq_div_iff hdet).2 ht⟩

/--
The objective expression is the exact rational formula obtained by
eliminating t and z from the two actual active band equations.
-/
theorem active_band_objective_value
    (Bb Bs Bt Hb Hs Cb Cs A t z : ℝ)
    (hdet : Bb * Hs - Bs * Hb ≠ 0)
    (hbeta : Bb * z + Hb * t = Cb)
    (hs : Bs * z + Hs * t = Cs) :
    A * t + Bt * z =
      (A * (Bb * Cs - Bs * Cb) +
        Bt * (Cb * Hs - Cs * Hb)) /
          (Bb * Hs - Bs * Hb) := by
  obtain ⟨hz, ht⟩ :=
    active_band_cramer_solution Bb Bs Hb Hs Cb Cs t z hdet hbeta hs
  rw [ht, hz]
  ring

end PrecategoryFormal.CompressedAdjacency
