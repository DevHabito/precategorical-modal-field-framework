import PrecategoryFormal.CompressedPrimalFeasibility

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.CompressedSourceSign

/--
In the central Q block, the target deformation contributes a shared
term K*C_r to both source coefficients. It cancels from the Cramer
numerator Z. The only remaining target-dependent band term is
-2*epsilon*(L_beta+L_s)/D.

Here L_r is the three-site Q shape numerator,
R_r = (1-r^h)*(1-r^(M-h))/2 is the centered P baseline
minus its central Q slope without the shared target term,
D = L_tau, and K is the parity-dependent target amplitude.

This is a universal algebraic identity. It does not assert positivity
of any individual polynomial L_r or R_r.
-/
theorem central_source_numerator_cancellation
    (Lb Ls Rb Rs D K epsilon : ℝ) (hD : D ≠ 0) :
    D * ((Lb / D) * (Rs + K * (Ls / D) - 2 * epsilon) -
      (Ls / D) * (Rb + K * (Lb / D) + 2 * epsilon)) =
      Lb * Rs - Ls * Rb - 2 * epsilon * (Lb + Ls) := by
  field_simp [hD] <;> ring

/--
A sufficient condition for the non-quotient source expression to be
negative. L_beta<L_s and R_s<R_beta are each an independent
monotonicity obligation in the actual A115 model.
-/
theorem central_source_numerator_negative
    (Lb Ls Rb Rs epsilon : ℝ)
    (hLb : 0 < Lb) (hLs : Lb < Ls)
    (hRs : 0 < Rs) (hRb : Rs < Rb)
    (hepsilon : 0 ≤ epsilon) :
    Lb * Rs - Ls * Rb - 2 * epsilon * (Lb + Ls) < 0 := by
  have hLspos : 0 < Ls := lt_trans hLb hLs
  have hfirst : Lb * Rs < Ls * Rs :=
    mul_lt_mul_of_pos_right hLs hRs
  have hsecond : Ls * Rs < Ls * Rb :=
    mul_lt_mul_of_pos_left hRb hLspos
  have hcorrect :
      0 ≤ 2 * epsilon * (Lb + Ls) :=
    mul_nonneg
      (mul_nonneg (by norm_num : (0 : ℝ) ≤ 2) hepsilon)
      (le_of_lt (add_pos hLb hLspos))
  linarith

/--
Once the monotonicity conditions L_beta<L_s, R_s<R_beta,
the positive denominator D and nonnegative epsilon are established,
the *actual* common Cramer numerator Z is negative. No restriction
on K or use of a numerical grid is required in this conditional
statement.
-/
theorem central_Z_negative_of_monotonicity
    (Lb Ls Rb Rs D K epsilon : ℝ)
    (hD : 0 < D)
    (hLb : 0 < Lb) (hLs : Lb < Ls)
    (hRs : 0 < Rs) (hRb : Rs < Rb)
    (hepsilon : 0 ≤ epsilon) :
    (Lb / D) * (Rs + K * (Ls / D) - 2 * epsilon) -
      (Ls / D) * (Rb + K * (Lb / D) + 2 * epsilon) < 0 := by
  have hcancel :=
    central_source_numerator_cancellation
      Lb Ls Rb Rs D K epsilon (ne_of_gt hD)
  have hnegative :=
    central_source_numerator_negative
      Lb Ls Rb Rs epsilon hLb hLs hRs hRb hepsilon
  have hprod :
      D * ((Lb / D) * (Rs + K * (Ls / D) - 2 * epsilon) -
        (Ls / D) * (Rb + K * (Lb / D) + 2 * epsilon)) < 0 := by
    rw [hcancel]
    exact hnegative
  by_contra hnot
  have hnonnegative :
      0 ≤ (Lb / D) * (Rs + K * (Ls / D) - 2 * epsilon) -
        (Ls / D) * (Rb + K * (Lb / D) + 2 * epsilon) :=
    le_of_not_gt hnot
  have hwrong :
      0 ≤ D * ((Lb / D) * (Rs + K * (Ls / D) - 2 * epsilon) -
        (Ls / D) * (Rb + K * (Lb / D) + 2 * epsilon)) :=
    mul_nonneg (le_of_lt hD) hnonnegative
  linarith

end PrecategoryFormal.CompressedSourceSign
