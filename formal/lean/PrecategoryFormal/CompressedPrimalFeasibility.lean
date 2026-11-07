import PrecategoryFormal.CompressedActualBandComparison
import PrecategoryFormal.TargetPrimalBridge

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.CompressedPrimalFeasibility

open PrecategoryFormal.PrimalBridge
open PrecategoryFormal.CompressedAdjacency

/--
For the three-site P support {0,k,M}, this is the exact linear
characterization of nonnegative scaled weights.
It is valid for real t,z and natural M,k with M>0; using k<M
is necessary for interpreting the support as three distinct atoms,
not for the algebraic equivalence itself.
-/
theorem three_site_p_weights_nonnegative_iff
    (M k : ℕ) (t z : ℝ) (hM : M ≠ 0) :
    (0 ≤ leftEndpoint M k t z ∧
      0 ≤ z ∧ 0 ≤ rightEndpoint M k t z) ↔
    (0 ≤ z ∧
      2 * ((M : ℝ) - (k : ℝ)) * z ≤ (M : ℝ) * t ∧
      2 * (k : ℝ) * z ≤ (M : ℝ) * t) := by
  have hMpos : (0 : ℝ) < (M : ℝ) := by
    exact_mod_cast Nat.pos_of_ne_zero hM
  have hleft :
      0 ≤ leftEndpoint M k t z ↔
        2 * ((M : ℝ) - (k : ℝ)) * z ≤ (M : ℝ) * t := by
    unfold leftEndpoint
    have hrewrite :
        (((M : ℝ) - (k : ℝ)) / (M : ℝ)) * z =
          (((M : ℝ) - (k : ℝ)) * z) / (M : ℝ) := by
      ring
    rw [hrewrite, sub_nonneg, div_le_iff₀ hMpos]
    constructor <;> intro h <;> nlinarith
  have hright :
      0 ≤ rightEndpoint M k t z ↔
        2 * (k : ℝ) * z ≤ (M : ℝ) * t := by
    unfold rightEndpoint
    have hrewrite :
        ((k : ℝ) / (M : ℝ)) * z =
          ((k : ℝ) * z) / (M : ℝ) := by
      ring
    rw [hrewrite, sub_nonneg, div_le_iff₀ hMpos]
    constructor <;> intro h <;> nlinarith
  constructor
  · rintro ⟨hp0, hz, hpM⟩
    exact ⟨hz, hleft.mp hp0, hright.mp hpM⟩
  · rintro ⟨hz, hp0, hpM⟩
    exact ⟨hleft.mpr hp0, hz, hright.mpr hpM⟩

/--
Nonnegative weights imply nonnegative total mass, even before
the extra requirement t>0 needed for probability normalization.
-/
theorem three_site_p_weights_total_nonnegative
    (M k : ℕ) (t z : ℝ) (hM : M ≠ 0)
    (hp0 : 0 ≤ leftEndpoint M k t z)
    (hz : 0 ≤ z)
    (hpM : 0 ≤ rightEndpoint M k t z) :
    0 ≤ t := by
  have hmass := endpoint_mass_identity M k t z hM
  linarith

/--
Both actual active-band solutions have the same Cramer numerator Z.
If both interior masses are strictly positive and Z is negative,
both Cramer determinants must be negative.
No independent determinant sign assumption is required.
-/
theorem positive_interior_forces_negative_determinants
    (Bb Bs Db Ds Hb Hs Cb Cs t z tnext znext : ℝ)
    (hbeta : Bb * z + Hb * t = Cb)
    (hs : Bs * z + Hs * t = Cs)
    (hbetanext : (Bb + Db) * znext + Hb * tnext = Cb)
    (hsnext : (Bs + Ds) * znext + Hs * tnext = Cs)
    (hz : 0 < z) (hznext : 0 < znext)
    (hZ : Cb * Hs - Cs * Hb < 0) :
    Bb * Hs - Bs * Hb < 0 ∧
      (Bb + Db) * Hs - (Bs + Ds) * Hb < 0 := by
  have hfirst :
      z * (Bb * Hs - Bs * Hb) = Cb * Hs - Cs * Hb := by
    calc
      z * (Bb * Hs - Bs * Hb) =
          Hs * (Bb * z + Hb * t) - Hb * (Bs * z + Hs * t) := by
            ring
      _ = Cb * Hs - Cs * Hb := by
        rw [hbeta, hs]
        ring
  have hsecond :
      znext * ((Bb + Db) * Hs - (Bs + Ds) * Hb) =
        Cb * Hs - Cs * Hb := by
    calc
      znext * ((Bb + Db) * Hs - (Bs + Ds) * Hb) =
          Hs * ((Bb + Db) * znext + Hb * tnext) -
            Hb * ((Bs + Ds) * znext + Hs * tnext) := by
            ring
      _ = Cb * Hs - Cs * Hb := by
        rw [hbetanext, hsnext]
        ring
  have hd : Bb * Hs - Bs * Hb < 0 := by
    by_contra hnot
    have hnonneg : 0 ≤ Bb * Hs - Bs * Hb := le_of_not_gt hnot
    have hprod : 0 ≤ z * (Bb * Hs - Bs * Hb) :=
      mul_nonneg (le_of_lt hz) hnonneg
    rw [hfirst] at hprod
    linarith
  have hdnext :
      (Bb + Db) * Hs - (Bs + Ds) * Hb < 0 := by
    by_contra hnot
    have hnonneg :
        0 ≤ (Bb + Db) * Hs - (Bs + Ds) * Hb := le_of_not_gt hnot
    have hprod :
        0 ≤ znext * ((Bb + Db) * Hs - (Bs + Ds) * Hb) :=
      mul_nonneg (le_of_lt hznext) hnonneg
    rw [hsecond] at hprod
    linarith
  exact ⟨hd, hdnext⟩

/--
An actual two-contact sign comparison now needs only Z<0 and positive
interior masses, together with the two active-band equations.
The nonzero determinants and their sign product are derived.
This is a conditional *compressed* comparison, not global LP KKT.
-/
theorem positive_interior_adjacent_objective_sign_iff
    (Bb Bs Bt Db Ds Dt Hb Hs Cb Cs A t z tnext znext : ℝ)
    (hbeta : Bb * z + Hb * t = Cb)
    (hs : Bs * z + Hs * t = Cs)
    (hbetanext : (Bb + Db) * znext + Hb * tnext = Cb)
    (hsnext : (Bs + Ds) * znext + Hs * tnext = Cs)
    (hz : 0 < z) (hznext : 0 < znext)
    (hZ : Cb * Hs - Cs * Hb < 0) :
    A * t + Bt * z < A * tnext + (Bt + Dt) * znext ↔
      0 < (A * Bb - Hb * Bt) * Ds +
        (-A * Db + Hb * Dt) * Bs +
        (-Bb * Dt + Bt * Db) * Hs := by
  obtain ⟨hd, hdnext⟩ :=
    positive_interior_forces_negative_determinants
      Bb Bs Db Ds Hb Hs Cb Cs t z tnext znext
      hbeta hs hbetanext hsnext hz hznext hZ
  have hprod :
      0 < (Bb * Hs - Bs * Hb) *
        ((Bb + Db) * Hs - (Bs + Ds) * Hb) :=
    mul_pos_of_neg_of_neg hd hdnext
  exact active_band_adjacent_objective_sign_iff
    Bb Bs Bt Db Ds Dt Hb Hs Cb Cs A t z tnext znext
    (ne_of_lt hd) (ne_of_lt hdnext)
    hbeta hs hbetanext hsnext hZ hprod

end PrecategoryFormal.CompressedPrimalFeasibility
