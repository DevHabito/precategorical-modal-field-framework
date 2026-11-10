import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.A118LogExpElementary

/--
The first log-one-plus bound used in the collision expansion, for all
nonnegative real arguments. Its proof uses the existing Mathlib log
inequality, not an independent analytic axiom.
-/
theorem log_one_add_le_arg (z : ℝ) (hz : 0 ≤ z) :
    Real.log (1+z) ≤ z := by
  have hp : (0:ℝ) < 1+z := by linarith
  have h := Real.log_le_sub_one_of_pos hp
  linarith

/--
Exact rational-series enclosure of exp(1); no numeric evaluation
of a transcendental constant is imported as an assumption.
-/
theorem exp_one_lt_68_div_25 :
    Real.exp (1:ℝ) < 68/25 := by
  have h := Real.exp_bound' (x := (1:ℝ))
    (by norm_num) (by norm_num) (n := 8) (by norm_num)
  have hr :
      (∑ m ∈ Finset.range 8, (1:ℝ)^m / (Nat.factorial m : ℝ))+
        (1:ℝ)^8*(8+1)/((Nat.factorial 8 : ℝ)*8) < 68/25 := by
    norm_num [Finset.sum_range_succ, Nat.factorial]
  exact lt_of_le_of_lt h hr

/--
One quantitative Mathlib-backed ingredient for the exponential
third-order Taylor remainder in A118.
-/
theorem exp_four_lt_55 : Real.exp (4:ℝ) < 55 := by
  have heq : Real.exp (4:ℝ) = (Real.exp (1:ℝ))^4 := by
    calc
      Real.exp (4:ℝ) = Real.exp ((4:ℕ)*(1:ℝ)) := by norm_num
      _ = (Real.exp (1:ℝ))^4 := Real.exp_nat_mul (1:ℝ) 4
  rw [heq]
  calc
    (Real.exp (1:ℝ))^4 < (68/25:ℝ)^4 :=
      pow_lt_pow_left₀ exp_one_lt_68_div_25
        (Real.exp_pos (1:ℝ)).le (by norm_num)
    _ < 55 := by norm_num

end PrecategoryFormal.A118LogExpElementary
