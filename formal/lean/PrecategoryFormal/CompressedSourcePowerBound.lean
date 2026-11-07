import PrecategoryFormal.CompressedSourceNumerator

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.CompressedSourceSign

/--
For r in [0,1/4] and all n>=0, the critical power coefficient
(n+2)^2*r^(n+1) never exceeds 4r. This is the induction used in
the written proof that L_h is increasing near the source nodes.
-/
theorem quadratic_power_bound
    (n : ℕ) (r : ℝ) (hr : 0 ≤ r) (hrq : r ≤ 1 / 4) :
    ((n : ℝ) + 2)^2 * r^(n+1) ≤ 4*r := by
  induction n with
  | zero =>
      norm_num
  | succ n ih =>
      have hn : (0 : ℝ) ≤ (n : ℝ) := by positivity
      have hquad :
          ((n : ℝ) + 3)^2 / 4 ≤ ((n : ℝ) + 2)^2 := by
        nlinarith [sq_nonneg (n : ℝ)]
      have hscaled :
          ((n : ℝ) + 3)^2 * r ≤ ((n : ℝ) + 3)^2 / 4 := by
        have hh :=
          mul_le_mul_of_nonneg_left hrq
            (sq_nonneg ((n : ℝ) + 3))
        nlinarith
      have hcoeff :
          ((n : ℝ) + 3)^2 * r ≤ ((n : ℝ) + 2)^2 :=
        le_trans hscaled hquad
      have hmul :=
        mul_le_mul_of_nonneg_right hcoeff (pow_nonneg hr (n+1))
      calc
        (((n+1 : ℕ) : ℝ) + 2)^2 * r^((n+1)+1) =
            (((n : ℝ) + 3)^2 * r) * r^(n+1) := by
              push_cast
              rw [pow_succ]
              ring
        _ ≤ ((n : ℝ) + 2)^2 * r^(n+1) := hmul
        _ ≤ 4*r := ih

/--
Positivity of the formal derivative expression
L'_(n+2)(r) = 1-(n+2)^2*r^(n+1)
                +((n+2)^2-1)*r^(n+2)
for all r in (0,1/4). The identity with the actual analytic
derivative and the derivative-based monotonicity theorem are
separate formalization steps.
-/
theorem source_shape_derivative_expression_positive
    (n : ℕ) (r : ℝ) (hr : 0 < r) (hrq : r < 1 / 4) :
    0 < 1 - ((n : ℝ) + 2)^2 * r^(n+1) +
      (((n : ℝ) + 2)^2 - 1) * r^(n+2) := by
  have hn : (0 : ℝ) ≤ (n : ℝ) := by positivity
  have hcoef : 0 ≤ ((n : ℝ) + 2)^2 - 1 := by
    nlinarith [sq_nonneg (n : ℝ)]
  have hnonneg :
      0 ≤ (((n : ℝ) + 2)^2 - 1) * r^(n+2) :=
    mul_nonneg hcoef (pow_nonneg (le_of_lt hr) _)
  have hbound :=
    quadratic_power_bound n r (le_of_lt hr) (le_of_lt hrq)
  linarith

/--
For M=2h, the difference between the P baseline and the even
Q central baseline has exactly the positive product structure R.
-/
theorem even_centered_baseline_identity (h : ℕ) (r : ℝ) :
    (1+r^(2*h))/2-r^h = (1-r^h)^2/2 := by
  have hexp : 2*h = h+h := by omega
  rw [hexp, pow_add]
  ring

/--
For M=2h+1, the same difference is a product of two consecutive
power deficiencies. No parity approximation is involved.
-/
theorem odd_centered_baseline_identity (h : ℕ) (r : ℝ) :
    (1+r^(2*h+1))/2-(1+r)/2*r^h =
      (1-r^h)*(1-r^(h+1))/2 := by
  have hexp : 2*h+1 = h+(h+1) := by omega
  rw [hexp, pow_add, pow_succ]
  ring

end PrecategoryFormal.CompressedSourceSign
