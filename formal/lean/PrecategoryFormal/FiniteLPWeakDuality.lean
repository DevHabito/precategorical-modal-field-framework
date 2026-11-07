import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.WeakDuality

/--
Weak duality for a finite linear maximization problem

  maximize sum_i c_i * x_i
  subject to x_i >= 0 and sum_i A_(j,i)*x_i <= b_j.

A proposed dual upper bound y is valid only if

  y_j >= 0  and  c_i <= sum_j y_j*A_(j,i).

The conclusion is an upper bound, not a KKT-optimality or
complementary-slackness statement. Equality constraints in a
particular primal model must be encoded explicitly as paired rows
or eliminated with correctly oriented coefficients.

This theorem uses no numerical solver or unverified certificate.
-/
theorem finite_max_lp_weak_duality
    (n m : ℕ)
    (A : Fin m → Fin n → ℝ)
    (b : Fin m → ℝ) (c x : Fin n → ℝ)
    (y : Fin m → ℝ)
    (hx : ∀ i, 0 ≤ x i)
    (hy : ∀ j, 0 ≤ y j)
    (hprimal : ∀ j, (∑ i : Fin n, A j i * x i) ≤ b j)
    (hdual : ∀ i, c i ≤ ∑ j : Fin m, y j * A j i) :
    (∑ i : Fin n, c i * x i) ≤
      ∑ j : Fin m, y j * b j := by
  have hcross :
      (∑ i : Fin n, (∑ j : Fin m, y j * A j i) * x i) =
        ∑ j : Fin m, y j * (∑ i : Fin n, A j i * x i) := by
    calc
      (∑ i : Fin n, (∑ j : Fin m, y j * A j i) * x i) =
          ∑ i : Fin n, ∑ j : Fin m, y j * (A j i * x i) := by
            apply Finset.sum_congr rfl
            intro i hi
            rw [Finset.sum_mul]
            apply Finset.sum_congr rfl
            intro j hj
            ring
      _ = ∑ j : Fin m, ∑ i : Fin n, y j * (A j i * x i) := by
            rw [Finset.sum_comm]
      _ = ∑ j : Fin m, y j * (∑ i : Fin n, A j i * x i) := by
            apply Finset.sum_congr rfl
            intro j hj
            rw [Finset.mul_sum]
  calc
    (∑ i : Fin n, c i * x i) ≤
        ∑ i : Fin n, (∑ j : Fin m, y j * A j i) * x i := by
          apply Finset.sum_le_sum
          intro i hi
          exact mul_le_mul_of_nonneg_right (hdual i) (hx i)
    _ = ∑ j : Fin m, y j * (∑ i : Fin n, A j i * x i) :=
          hcross
    _ ≤ ∑ j : Fin m, y j * b j := by
          apply Finset.sum_le_sum
          intro j hj
          exact mul_le_mul_of_nonneg_left (hprimal j) (hy j)

end PrecategoryFormal.WeakDuality
