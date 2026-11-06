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

/--
Cross-multiplied central target equation for M = 2h.
Here `u` stands for τ^h and `D=τ-hu+(h-1)τu`.
The remaining central coordinates have numerators
`tD-h(1-ut)` and `(h-1)(1-ut)`.
This is a polynomial identity; division by D requires a separate
nonzero-denominator hypothesis.
-/
theorem even_central_target_numerator
    (h τ u t : ℝ) :
    let D := τ - h * u + (h - 1) * τ * u
    let v := 1 - u * t
    τ * v + u * (t * D - h * v) +
      τ * u * ((h - 1) * v) = D := by
  dsimp
  ring

/--
Cross-multiplied central mean equation for M = 2h.
-/
theorem even_central_mean_numerator
    (h τ u t : ℝ) :
    let D := τ - h * u + (h - 1) * τ * u
    let v := 1 - u * t
    v + h * (t * D - h * v) +
      (h + 1) * ((h - 1) * v) = h * t * D := by
  dsimp
  ring

/--
Cross-multiplied central target equation for M = 2h+1.
The odd coordinate numerators are `tD/2-hv` and
`tD/2+(h-1)v`.
-/
theorem odd_central_target_numerator
    (h τ u t : ℝ) :
    let D := τ - h * u + (h - 1) * τ * u
    let v := 1 - ((1 + τ) / 2) * u * t
    τ * v + u * ((t * D) / 2 - h * v) +
      τ * u * ((t * D) / 2 + (h - 1) * v) = D := by
  dsimp
  ring

/--
Cross-multiplied central mean equation for M = 2h+1.
-/
theorem odd_central_mean_numerator
    (h τ u t : ℝ) :
    let D := τ - h * u + (h - 1) * τ * u
    let v := 1 - ((1 + τ) / 2) * u * t
    v + h * ((t * D) / 2 - h * v) +
      (h + 1) * ((t * D) / 2 + (h - 1) * v) =
        (h + 1 / 2) * t * D := by
  dsimp
  ring

/--
The exact A115 finite-difference identity for the discrete
exponential/moment basis, with a common nonzero real M.
This identity is independent of parity and of the LP.
-/
theorem exponential_basis_difference
    (M r : ℝ) (k : ℕ) (hM : M ≠ 0) :
    (r ^ (k + 1) - ((M - ((k + 1 : ℕ) : ℝ)) / M) -
      (((k + 1 : ℕ) : ℝ) / M) * r ^ M) -
    (r ^ k - ((M - (k : ℝ)) / M) -
      ((k : ℝ) / M) * r ^ M) =
    r ^ (k + 1) - r ^ k + (1 - r ^ M) / M := by
  push_cast
  field_simp
  ring

/--
The geometric-polynomial factorization behind positivity of A115's
central denominator. This is a finite exact identity, with natural
exponents and an explicit finite sum.
-/
theorem central_denominator_geometric_identity (h : ℕ) (τ : ℝ) :
    1 - ((h + 1 : ℕ) : ℝ) * τ ^ h +
      (h : ℝ) * τ ^ (h + 1) =
    (1 - τ) ^ 2 *
      ∑ j ∈ Finset.range h, ((j + 1 : ℕ) : ℝ) * τ ^ j := by
  induction h with
  | zero =>
      simp
  | succ h ih =>
      calc
        1 - (((h + 1 + 1 : ℕ) : ℝ)) * τ ^ (h + 1) +
            ((h + 1 : ℕ) : ℝ) * τ ^ (h + 1 + 1) =
          (1 - ((h + 1 : ℕ) : ℝ) * τ ^ h +
              (h : ℝ) * τ ^ (h + 1)) +
            ((h + 1 : ℕ) : ℝ) * τ ^ h * (1 - τ) ^ 2 := by
              push_cast
              simp only [pow_succ]
              ring
        _ = (1 - τ) ^ 2 *
              (∑ j ∈ Finset.range h, ((j + 1 : ℕ) : ℝ) * τ ^ j) +
              ((h + 1 : ℕ) : ℝ) * τ ^ h * (1 - τ) ^ 2 := by rw [ih]
        _ = (1 - τ) ^ 2 *
              (∑ j ∈ Finset.range (h + 1),
                ((j + 1 : ℕ) : ℝ) * τ ^ j) := by
              rw [Finset.sum_range_succ]
              ring

/--
A version of the A115 exponential basis difference that keeps the
finite-support index and both exponents in Nat, unlike the convenient
more general real-exponent algebra lemma above.
-/
theorem exponential_basis_difference_nat
    (M k : ℕ) (r : ℝ) (hM : M ≠ 0) :
    (r ^ (k + 1) - ((M : ℝ) - ((k + 1 : ℕ) : ℝ)) / M -
      (((k + 1 : ℕ) : ℝ) / M) * r ^ M) -
    (r ^ k - ((M : ℝ) - (k : ℝ)) / M -
      ((k : ℝ) / M) * r ^ M) =
    r ^ (k + 1) - r ^ k + (1 - r ^ M) / M := by
  have hm : (M : ℝ) ≠ 0 := by exact_mod_cast hM
  push_cast
  field_simp
  ring

end PrecategoryFormal.TargetDeformation
