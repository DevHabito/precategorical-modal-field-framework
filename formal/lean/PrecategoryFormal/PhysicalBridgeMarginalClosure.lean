import Mathlib

namespace PrecategoryFormal.PhysicalBridge

/--
Swapping two hidden-context states preserves their equal-weight marginal mean,
while the marginal derivative changes by the exact product
((a₁-a₂)(r-s))/2.

This is the finite algebraic core of the continuous-time marginal-closure
obstruction. It contains no physical assumptions.
-/
theorem two_context_swap_derivative_gap
    (a₁ a₂ r s b₁ b₂ : ℚ) :
    (((a₁ * r + b₁) + (a₂ * s + b₂)) / 2)
      - (((a₁ * s + b₁) + (a₂ * r + b₂)) / 2)
      =
      ((a₁ - a₂) * (r - s)) / 2 := by
  ring

/--
If an equal-weight two-context marginal derivative is unchanged under every
swap of conditioned scalar states, the multiplicative coefficients must agree.
-/
theorem universal_two_context_scalar_closure_forces_equal_coefficients
    (a₁ a₂ : ℚ)
    (h :
      ∀ r s : ℚ,
        (a₁ * r + a₂ * s) / 2
          =
        (a₁ * s + a₂ * r) / 2) :
    a₁ = a₂ := by
  have h10 := h 1 0
  norm_num at h10 ⊢
  linarith

/--
Two hidden affine maps with one common multiplier μ produce an averaged
sequence satisfying the exact three-point recurrence, even when their
intercepts and initial states differ.
-/
theorem common_multiplier_average_three_point_recurrence
    (μ c₁ c₂ x₁ x₂ : ℚ) :
    let y₀ := (x₁ + x₂) / 2
    let x₁₁ := μ * x₁ + c₁
    let x₂₁ := μ * x₂ + c₂
    let y₁ := (x₁₁ + x₂₁) / 2
    let x₁₂ := μ * x₁₁ + c₁
    let x₂₂ := μ * x₂₁ + c₂
    let y₂ := (x₁₂ + x₂₂) / 2
    y₂ - (1 + μ) * y₁ + μ * y₀ = 0 := by
  dsimp
  ring

end PrecategoryFormal.PhysicalBridge
