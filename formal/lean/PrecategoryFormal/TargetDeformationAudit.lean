import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.TargetDeformation

/--
The target-affine channel of the A115 reduced factor is
`(a + k*b) * τ^k`. In the *scaled* adjacent difference,
the coefficient `a` cancels exactly. This is an algebraic lemma
only: it does not establish the full ten-channel A115 identity.
-/
theorem target_affine_scaled_cancellation
    (τ a b : ℝ) (k : ℕ) :
    τ * ((a + (k : ℝ) * b) * τ ^ k) -
      (a + ((k + 1 : ℕ) : ℝ) * b) * τ ^ (k + 1) =
      -b * τ ^ (k + 1) := by
  simp only [pow_succ, Nat.cast_add, Nat.cast_one]
  ring

/--
A119 substitutes the critical-surface equation into the second-order
coefficient. This lemma formalizes only the exact rearrangement:
the denominator must be nonzero. It does not prove that the
critical-surface equation holds or that the denominator is positive.
-/
theorem critical_surface_substitution
    (a C A D α q : ℝ)
    (hden : A + α * D ≠ 0)
    (hcritical : -a * C + q * (A + α * D) = 0) :
    q = a * C / (A + α * D) := by
  apply (eq_div_iff hden).2
  nlinarith [hcritical]

/--
When the three needed signs are proved separately, the substituted
critical exponential `q` is positive. This is a conditional
sign lemma, not an assertion that A119's hypotheses already hold.
-/
theorem critical_substitution_positive
    (a C A D α q : ℝ)
    (ha : 0 < a) (hC : 0 < C)
    (hden : 0 < A + α * D)
    (hcritical : -a * C + q * (A + α * D) = 0) :
    0 < q := by
  rw [critical_surface_substitution a C A D α q (ne_of_gt hden) hcritical]
  positivity

/--
A119's exact even-parity rational *cutoff inequality* at r=13,
independent of the interval-covering computation.
This is only one numeric inequality within A119's tail argument.
-/
theorem even_cutoff_rational_positive :
    0 <
      -(1 - (1 / 8 : ℚ) / (133 / 1000) - 4 / 1875)
        + (14 : ℚ) * 2 * (129 / 1000) ^ 3
        - 14 * (21 / 10 : ℚ) *
          ((1 / 8 : ℚ) / (129 / 1000) + 2 / 1875) *
          (133 / 1000 : ℚ) ^ 14 := by
  norm_num

end PrecategoryFormal.TargetDeformation
