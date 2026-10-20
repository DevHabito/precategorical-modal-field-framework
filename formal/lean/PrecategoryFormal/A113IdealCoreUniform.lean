import PrecategoryFormal.A113SmallLeftBridge
import Mathlib

set_option autoImplicit false
set_option warningAsError true
set_option exponentiation.threshold 512

namespace PrecategoryFormal

/-!
# A113: an unconditional lower bound for the ideal small-left core

This file deliberately proves the ideal-core estimate from its three
exponential-product terms. It does NOT assume a general homogeneous
polynomial identity, does not assume the desired A113 sign, and does
not estimate the difference between the true and ideal A83 factors.

The recursion is an independent route to the same positive lower bound
as the complete homogeneous symmetric-polynomial representation.
-/

/--
The three-node ideal core satisfies a first-order inequality with a
nonnegative remainder when 0 < beta < source < target.
This is an algebraic identity without sign hypotheses.
-/
theorem contactIdealCore_step_identity (k : ℕ)
    (beta target source : ℝ) :
    contactIdealCore (k + 1) beta target source =
      (source * target) * contactIdealCore k beta target source +
        (1 / 2 : ℝ) * (source - beta) * (target - beta) *
          (target * (beta * target) ^ k -
            source * (beta * source) ^ k) := by
  unfold contactIdealCore
  rw [pow_succ, pow_succ, pow_succ]
  ring

private theorem contactIdealCore_node_power_le
    (k : ℕ) (beta target source : ℝ)
    (hbeta : 0 ≤ beta) (hsource : 0 ≤ source)
    (hsourceTarget : source ≤ target) :
    source * (beta * source) ^ k ≤
      target * (beta * target) ^ k := by
  have hbetaSource : 0 ≤ beta * source := mul_nonneg hbeta hsource
  have hbetaTarget : beta * source ≤ beta * target := by
    exact mul_le_mul_of_nonneg_left hsourceTarget hbeta
  have hpow : (beta * source) ^ k ≤ (beta * target) ^ k := by
    exact pow_le_pow_left₀ hbetaSource hbetaTarget k
  calc
    source * (beta * source) ^ k
        ≤ target * (beta * source) ^ k := by
          exact mul_le_mul_of_nonneg_right hsourceTarget
            (pow_nonneg hbetaSource k)
    _ ≤ target * (beta * target) ^ k :=
      mul_le_mul_of_nonneg_left hpow (le_trans hsource hsourceTarget)

/--
The correction term in the recurrence is nonnegative, with no
floating-point comparison.
-/
theorem contactIdealCore_step_lower (k : ℕ)
    (beta target source : ℝ)
    (hbeta : 0 ≤ beta)
    (hsource : beta ≤ source)
    (htarget : source ≤ target) :
    (source * target) * contactIdealCore k beta target source ≤
      contactIdealCore (k + 1) beta target source := by
  rw [contactIdealCore_step_identity]
  have hs : 0 ≤ source := le_trans hbeta hsource
  have hfirst : 0 ≤ source - beta := sub_nonneg.mpr hsource
  have hsecond : 0 ≤ target - beta := sub_nonneg.mpr (le_trans hsource htarget)
  have hlast := contactIdealCore_node_power_le
    k beta target source hbeta hs htarget
  have hdiff :
      0 ≤ target * (beta * target) ^ k -
        source * (beta * source) ^ k := sub_nonneg.mpr hlast
  have hcorrection : 0 ≤
      (1 / 2 : ℝ) * (source - beta) * (target - beta) *
        (target * (beta * target) ^ k -
          source * (beta * source) ^ k) := by positivity
  linarith

/--
For all natural n the ideal core at contact n+1 dominates its
first-contact Vandermonde factor multiplied by (source*target)^n.
-/
theorem contactIdealCore_lower_power (n : ℕ)
    (beta target source : ℝ)
    (hbeta : 0 ≤ beta)
    (hsource : beta ≤ source)
    (htarget : source ≤ target) :
    (1 / 2 : ℝ) * (source - beta) *
        (target - beta) * (target - source) *
          (source * target) ^ n ≤
      contactIdealCore (n + 1) beta target source := by
  have hs : 0 ≤ source := le_trans hbeta hsource
  have ht : 0 ≤ target := le_trans hs htarget
  have hz : 0 ≤ source * target := mul_nonneg hs ht
  induction n with
  | zero =>
      rw [pow_zero, mul_one, contactIdealCore_one]
  | succ n ih =>
      have hstep := contactIdealCore_step_lower
        (n + 1) beta target source hbeta hsource htarget
      calc
        (1 / 2 : ℝ) * (source - beta) *
            (target - beta) * (target - source) *
              (source * target) ^ (n + 1)
            = (source * target) *
                ((1 / 2 : ℝ) * (source - beta) *
                  (target - beta) * (target - source) *
                    (source * target) ^ n) := by rw [pow_succ]; ring
        _ ≤ (source * target) *
              contactIdealCore (n + 1) beta target source :=
            mul_le_mul_of_nonneg_left ih hz
        _ ≤ contactIdealCore ((n + 1) + 1) beta target source := hstep

private theorem contactPow_antitone
    (z : ℝ) (hz : 0 ≤ z) (hone : z ≤ 1)
    (n m : ℕ) (hnm : n ≤ m) :
    z ^ m ≤ z ^ n := by
  obtain ⟨d, hd⟩ : ∃ d : ℕ, m = n + d := by omega
  subst m
  have hpow : ∀ j : ℕ, z ^ j ≤ 1 := by
    intro j
    induction j with
    | zero => simp
    | succ j ih =>
        calc
          z ^ (j + 1) = z ^ j * z := pow_succ z j
          _ ≤ z ^ j * 1 :=
            mul_le_mul_of_nonneg_left hone (pow_nonneg hz j)
          _ = z ^ j := mul_one _
          _ ≤ 1 := ih
  rw [pow_add]
  calc
    z ^ n * z ^ d ≤ z ^ n * 1 :=
      mul_le_mul_of_nonneg_left (hpow d) (pow_nonneg hz n)
    _ = z ^ n := mul_one _

/--
The ideal A113 core satisfies the fixed small-left *uniform*
rational lower bound for every real source and every contact 2..29.
No remaining analytic assumptions are used for this ideal-core bound.
-/
theorem contactA113IdealCore_uniform_lower (k : ℕ) (source : ℝ)
    (hkLower : 2 ≤ k)
    (hkUpper : k ≤ 29)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    (1 / 2 : ℝ) *
        (129 / 1000 - 1 / 8) *
        (1 / 2 - 1 / 8) *
        (1 / 2 - 133 / 1000) *
        (129 / 2000 : ℝ) ^ 28 ≤
      contactIdealCore k (1 / 8) (1 / 2) source := by
  obtain ⟨n, hk⟩ : ∃ n : ℕ, k = n + 1 := by omega
  subst k
  have hn : n ≤ 28 := by omega
  have hsBeta : (1 / 8 : ℝ) ≤ source := by linarith
  have hsTarget : source ≤ (1 / 2 : ℝ) := by linarith
  have hsPos : 0 ≤ source := by linarith
  have hzNonneg : 0 ≤ source * (1 / 2 : ℝ) := by positivity
  have hzUpper : source * (1 / 2 : ℝ) ≤ 1 := by linarith
  have hzLower : (129 / 2000 : ℝ) ≤ source * (1 / 2 : ℝ) := by
    nlinarith [hsLower]
  have hpowLower :
      (129 / 2000 : ℝ) ^ 28 ≤ (source * (1 / 2 : ℝ)) ^ 28 := by
    gcongr
  have hpowOrder :
      (source * (1 / 2 : ℝ)) ^ 28 ≤
        (source * (1 / 2 : ℝ)) ^ n :=
    contactPow_antitone _ hzNonneg hzUpper n 28 hn
  have hcNonneg : 0 ≤
      (1 / 2 : ℝ) * (source - 1 / 8) *
        (1 / 2 - 1 / 8) * (1 / 2 - source) := by
    have h1 : 0 ≤ source - (1 / 8 : ℝ) := by linarith
    have h2 : 0 ≤ (1 / 2 : ℝ) - source := by linarith
    positivity
  have hfactor :
      (1 / 2 : ℝ) *
        (129 / 1000 - 1 / 8) *
        (1 / 2 - 1 / 8) *
        (1 / 2 - 133 / 1000) ≤
      (1 / 2 : ℝ) * (source - 1 / 8) *
        (1 / 2 - 1 / 8) * (1 / 2 - source) := by
    have h1 : (129 / 1000 - 1 / 8 : ℝ) ≤ source - 1 / 8 := by linarith
    have h2 : (1 / 2 - 133 / 1000 : ℝ) ≤ 1 / 2 - source := by linarith
    gcongr
  calc
    (1 / 2 : ℝ) * (129 / 1000 - 1 / 8) *
        (1 / 2 - 1 / 8) * (1 / 2 - 133 / 1000) *
          (129 / 2000 : ℝ) ^ 28
      ≤ ((1 / 2 : ℝ) * (source - 1 / 8) *
          (1 / 2 - 1 / 8) * (1 / 2 - source)) *
          (129 / 2000 : ℝ) ^ 28 :=
        mul_le_mul_of_nonneg_right hfactor (by positivity)
    _ ≤ ((1 / 2 : ℝ) * (source - 1 / 8) *
          (1 / 2 - 1 / 8) * (1 / 2 - source)) *
          (source * (1 / 2 : ℝ)) ^ 28 :=
        mul_le_mul_of_nonneg_left hpowLower hcNonneg
    _ ≤ ((1 / 2 : ℝ) * (source - 1 / 8) *
          (1 / 2 - 1 / 8) * (1 / 2 - source)) *
          (source * (1 / 2 : ℝ)) ^ n :=
        mul_le_mul_of_nonneg_left hpowOrder hcNonneg
    _ ≤ contactIdealCore (n + 1) (1 / 8) (1 / 2) source :=
      contactIdealCore_lower_power n (1 / 8) (1 / 2) source
        (by norm_num) hsBeta hsTarget

/--
The earlier conditional positivity theorem can now be applied without
taking the ideal-core inequality as an externally supplied assumption.
The remainder and unit assumptions remain visible and unproved.
-/
theorem contactA113SmallLeftPositive_of_error_and_unit
    (M k : ℕ) (source : ℝ)
    (_hM : 521 ≤ M)
    (hkLower : 2 ≤ k)
    (hkUpper : k ≤ 29)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ))
    (targetMass betaH sourceH betaSlope targetSlope sourceSlope unit : ℝ)
    (herror :
      |contactAdjacentFactor k (1 / 8) (1 / 2) source
          targetMass betaH sourceH betaSlope targetSlope sourceSlope -
          contactIdealCore k (1 / 8) (1 / 2) source| < 20 * unit)
    (hunit : unit ≤ 1 / (2 : ℝ) ^ 260) :
    0 < contactAdjacentFactor k (1 / 8) (1 / 2) source
      targetMass betaH sourceH betaSlope targetSlope sourceSlope := by
  exact contactSmallLeftPositive_of_uniformBounds _ _ _ _
    (contactA113IdealCore_uniform_lower k source hkLower hkUpper hsLower hsUpper)
    herror hunit contactSmallLeftRationalMargin

end PrecategoryFormal
