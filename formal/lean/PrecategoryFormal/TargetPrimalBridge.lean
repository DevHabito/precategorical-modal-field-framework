import PrecategoryFormal.TargetFactorBasisBridge

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.PrimalBridge

/--
A finite discrete transform before normalizing the measures. The index
really ranges over the finite support {0,...,M}.
-/
noncomputable def transform (M : ℕ) (w : Fin (M+1) → ℝ) (r : ℝ) : ℝ :=
  ∑ x : Fin (M+1), w x * r ^ (x : ℕ)

/-- Scaling every weight by t scales its finite transform by t. -/
theorem transform_scale (M : ℕ) (μ p : Fin (M+1) → ℝ)
    (r t : ℝ) (hscale : ∀ x, p x = t * μ x) :
    transform M p r = t * transform M μ r := by
  unfold transform
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro x hx
  rw [hscale x]
  ring

/--
Under the scaled Q target constraint and the common scaling of both
measures, the original linear target objective is exactly the ratio
of the corresponding probability transforms. The denominator's
nonvanishing is explicit; no optimization claim is made.
-/
theorem target_ratio_from_scaled_primal
    (M : ℕ) (μ ν p q : Fin (M+1) → ℝ)
    (τ t : ℝ)
    (hp : ∀ x, p x = t * μ x)
    (hq : ∀ x, q x = t * ν x)
    (hgoal : transform M q τ = 1) :
    transform M ν τ ≠ 0 ∧
      transform M p τ = transform M μ τ / transform M ν τ := by
  have ht : t * transform M ν τ = 1 := by
    calc
      t * transform M ν τ = transform M q τ := by
        rw [transform_scale M ν q τ t hq]
      _ = 1 := hgoal
  have hν : transform M ν τ ≠ 0 := by
    intro hzero
    rw [hzero] at ht
    norm_num at ht
  have htformula : t = 1 / transform M ν τ := by
    apply (eq_div_iff hν).2
    nlinarith [ht]
  constructor
  · exact hν
  · calc
      transform M p τ = t * transform M μ τ :=
        transform_scale M μ p τ t hp
      _ = transform M μ τ / transform M ν τ := by
        rw [htformula]
        ring

/--
The affine endpoint weights that solve normalization and mean M/2
when a third atom of mass z is placed at k. They are algebraic
weights; their nonnegativity must still be checked separately.
-/
noncomputable def leftEndpoint (M k : ℕ) (t z : ℝ) : ℝ :=
  t/2 - (((M : ℝ)-(k : ℝ))/(M : ℝ))*z

noncomputable def rightEndpoint (M k : ℕ) (t z : ℝ) : ℝ :=
  t/2 - ((k : ℝ)/(M : ℝ))*z

theorem endpoint_mass_identity (M k : ℕ) (t z : ℝ)
    (hM : M ≠ 0) :
    leftEndpoint M k t z + z + rightEndpoint M k t z = t := by
  have hm : (M : ℝ) ≠ 0 := by exact_mod_cast hM
  unfold leftEndpoint rightEndpoint
  field_simp [hm]
  ring

theorem endpoint_mean_identity (M k : ℕ) (t z : ℝ)
    (hM : M ≠ 0) :
    (k : ℝ)*z+(M : ℝ)*rightEndpoint M k t z =
      ((M : ℝ)/2)*t := by
  have hm : (M : ℝ) ≠ 0 := by exact_mod_cast hM
  unfold rightEndpoint
  field_simp [hm]
  ring

/--
Exact derivation of the A115 moment-adjusted basis from the primal
three-site mass and first-moment equations. This goes one step
earlier than the universal cofactor algebra: it identifies B as the
coefficient of the movable interior mass z in a genuine finite
support transform.
-/
theorem three_site_transform_basis
    (M k : ℕ) (t z r : ℝ) (hM : M ≠ 0) :
    leftEndpoint M k t z + z * r^k +
        rightEndpoint M k t z * r^M =
      t/2 * (1+r^M) +
        z * PrecategoryFormal.TargetFactor.finiteBasis M k r := by
  have hm : (M : ℝ) ≠ 0 := by exact_mod_cast hM
  unfold leftEndpoint rightEndpoint PrecategoryFormal.TargetFactor.finiteBasis
  field_simp [hm]
  ring

end PrecategoryFormal.PrimalBridge
