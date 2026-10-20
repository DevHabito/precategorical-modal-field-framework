import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
# A113: small-left algebraic bridge

This module formalizes the exact A83-to-A84 algebraic reduction,
the zero-unit comparison factor, and a conditional quantitative
positivity transfer. It does NOT prove the uniform A113 remainder
estimate or the all-contact small-left theorem.

The historical source and its frozen parameter values are kept
separate from this universal algebraic calculation.
-/

/-- Contact mass from a node power and an independent moment slope. -/
def contactMass (k : ℕ) (node slope : ℝ) : ℝ :=
  node ^ k - 1 + (k : ℝ) * slope

/-- Adjacent-contact mass difference with an independent moment slope. -/
def contactMassDifference (k : ℕ) (node slope : ℝ) : ℝ :=
  (node - 1) * node ^ k + slope

/--
The exact A83 cofactor factor, with independently supplied target
normalization, beta/source H-values, and node moment slopes.
-/
def contactAdjacentFactor (k : ℕ) (beta target source targetMass
    betaH sourceH betaSlope targetSlope sourceSlope : ℝ) : ℝ :=
  let betaMass := contactMass k beta betaSlope
  let targetMassAtK := contactMass k target targetSlope
  let sourceMass := contactMass k source sourceSlope
  let betaDifference := contactMassDifference k beta betaSlope
  let targetDifference := contactMassDifference k target targetSlope
  let sourceDifference := contactMassDifference k source sourceSlope
  (targetMass * betaMass - betaH * targetMassAtK) * sourceDifference +
    (-targetMass * betaDifference + betaH * targetDifference) * sourceMass +
    (-betaMass * targetDifference + targetMassAtK * betaDifference) * sourceH

/--
The ten-term A84 expansion, grouped into three products,
three affine-exponential channels and one constant channel.
-/
def contactTenTermFactor (k : ℕ) (beta target source targetMass
    betaH sourceH betaSlope targetSlope sourceSlope : ℝ) : ℝ :=
  let betaAffine :=
    targetMass * sourceSlope - sourceH * targetSlope +
      (beta - 1) * (targetMass - sourceH)
  let betaLinear :=
    (1 - beta) * (targetMass * sourceSlope - sourceH * targetSlope)
  let sourceAffine :=
    -targetMass * betaSlope + betaH * targetSlope +
      (1 - source) * (targetMass - betaH)
  let sourceLinear :=
    (source - 1) * (targetMass * betaSlope - betaH * targetSlope)
  let targetAffine :=
    -betaH * sourceSlope + sourceH * betaSlope +
      (1 - target) * (betaH - sourceH)
  let targetLinear :=
    (target - 1) * (betaH * sourceSlope - sourceH * betaSlope)
  let constant :=
    (betaH - targetMass) * sourceSlope +
      (targetMass - sourceH) * betaSlope +
      (sourceH - betaH) * targetSlope
  targetMass * (source - beta) * (beta * source) ^ k +
    sourceH * (beta - target) * (beta * target) ^ k +
    betaH * (target - source) * (source * target) ^ k +
    (betaAffine + (k : ℝ) * betaLinear) * beta ^ k +
    (sourceAffine + (k : ℝ) * sourceLinear) * source ^ k +
    (targetAffine + (k : ℝ) * targetLinear) * target ^ k +
    constant

/--
Exact A83/A84 bridge: a symbolic identity for every natural contact,
all real nodes, all H-values and all moment slopes. No numeric
experiments, sign assumptions or native-decide certificates enter.
-/
theorem contactAdjacentFactor_eq_tenTermFactor (k : ℕ)
    (beta target source targetMass betaH sourceH
      betaSlope targetSlope sourceSlope : ℝ) :
    contactAdjacentFactor k beta target source targetMass
        betaH sourceH betaSlope targetSlope sourceSlope =
      contactTenTermFactor k beta target source targetMass
        betaH sourceH betaSlope targetSlope sourceSlope := by
  unfold contactAdjacentFactor contactTenTermFactor
    contactMass contactMassDifference
  simp only [mul_pow]
  ring

/-- The leading comparison factor obtained from equal half-moments. -/
noncomputable def contactIdealCore (k : ℕ) (beta target source : ℝ) : ℝ :=
  (1 / 2 : ℝ) *
    ((source - beta) * (beta * source) ^ k +
     (beta - target) * (beta * target) ^ k +
     (target - source) * (source * target) ^ k)

/--
The ideal core follows from the actual cofactor algebra when the three
moment slopes coincide and targetMass = betaH = sourceH = 1/2.
This is an exact comparison identity, not a finite-M substitution.
-/
theorem contactIdealCore_from_cofactors (k : ℕ)
    (beta target source commonSlope : ℝ) :
    contactAdjacentFactor k beta target source
        (1 / 2) (1 / 2) (1 / 2)
        commonSlope commonSlope commonSlope =
      contactIdealCore k beta target source := by
  rw [contactAdjacentFactor_eq_tenTermFactor]
  unfold contactTenTermFactor contactIdealCore
  simp only [mul_pow]
  ring

/-- The first ideal-contact factor has the exact positive product form. -/
theorem contactIdealCore_one (beta target source : ℝ) :
    contactIdealCore 1 beta target source =
      (1 / 2 : ℝ) * (source - beta) *
        (target - beta) * (target - source) := by
  unfold contactIdealCore
  simp only [pow_one]
  ring

theorem contactIdealCore_one_pos
    (beta target source : ℝ)
    (hb : beta < source)
    (hs : source < target) :
    0 < contactIdealCore 1 beta target source := by
  rw [contactIdealCore_one]
  have h1 : 0 < source - beta := by linarith
  have h2 : 0 < target - beta := by linarith
  have h3 : 0 < target - source := by linarith
  positivity

/-- A second exact factorization without using a historical certificate. -/
theorem contactIdealCore_two (beta target source : ℝ) :
    contactIdealCore 2 beta target source =
      (1 / 2 : ℝ) * (source - beta) *
        (target - beta) * (target - source) *
          (beta * source + beta * target + source * target) := by
  unfold contactIdealCore
  simp only [mul_pow]
  ring

theorem contactIdealCore_two_pos
    (beta target source : ℝ)
    (hbpos : 0 < beta)
    (hb : beta < source)
    (hs : source < target) :
    0 < contactIdealCore 2 beta target source := by
  rw [contactIdealCore_two]
  have hsource : 0 < source := lt_trans hbpos hb
  have htarget : 0 < target := lt_trans hsource hs
  have h1 : 0 < source - beta := by linarith
  have h2 : 0 < target - beta := by linarith
  have h3 : 0 < target - source := by linarith
  positivity

/--
The fixed contract's rational baseline exceeds the worst conservative
small-left perturbation cap. This is an exact rational comparison.
-/
theorem contactSmallLeftRationalMargin :
    (20 : ℝ) / (2 : ℝ) ^ 260 <
      (1 / 2 : ℝ) *
        (129 / 1000 - 1 / 8) *
        (1 / 2 - 1 / 8) *
        (1 / 2 - 133 / 1000) *
        (129 / 2000 : ℝ) ^ 28 := by
  rw [div_lt_iff₀ (show (0 : ℝ) < (2 : ℝ) ^ 260 by positivity)]
  norm_num

/--
Conditional sign transport. Crucially, the uniform core lower bound,
the actual-minus-core bound, and the unit bound are *hypotheses*.
No claim is made here that Lean has established them for every M,k,s.
-/
theorem contactSmallLeftPositive_of_uniformBounds
    (actual core unit lower : ℝ)
    (hcore : lower ≤ core)
    (herror : |actual - core| < 20 * unit)
    (hunit : unit ≤ 1 / (2 : ℝ) ^ 260)
    (hlower : 20 / (2 : ℝ) ^ 260 < lower) :
    0 < actual := by
  have herrorLower := (abs_lt.mp herror).1
  have hcap : 20 * unit ≤ 20 / (2 : ℝ) ^ 260 := by
    calc
      20 * unit ≤ 20 * (1 / (2 : ℝ) ^ 260) :=
        mul_le_mul_of_nonneg_left hunit (by norm_num)
      _ = 20 / (2 : ℝ) ^ 260 := by ring
  linarith

/--
Specialization to the real A83 factor. It remains explicitly
conditional on uniform analytic estimates for the H-channels,
moment slopes and power remainder.
-/
theorem contactA113SmallLeftPositive_of_analyticEnvelopes
    (M k : ℕ) (source : ℝ)
    (_hM : 521 ≤ M)
    (_hkLower : 2 ≤ k)
    (_hkUpper : k ≤ 29)
    (_hsLower : (129 / 1000 : ℝ) ≤ source)
    (_hsUpper : source ≤ (133 / 1000 : ℝ))
    (targetMass betaH sourceH betaSlope targetSlope sourceSlope unit : ℝ)
    (hcore :
      (1 / 2 : ℝ) *
        (129 / 1000 - 1 / 8) *
        (1 / 2 - 1 / 8) *
        (1 / 2 - 133 / 1000) *
        (129 / 2000 : ℝ) ^ 28 ≤
      contactIdealCore k (1 / 8) (1 / 2) source)
    (herror :
      |contactAdjacentFactor k (1 / 8) (1 / 2) source
          targetMass betaH sourceH betaSlope targetSlope sourceSlope -
          contactIdealCore k (1 / 8) (1 / 2) source| < 20 * unit)
    (hunit : unit ≤ 1 / (2 : ℝ) ^ 260) :
    0 < contactAdjacentFactor k (1 / 8) (1 / 2) source
      targetMass betaH sourceH betaSlope targetSlope sourceSlope := by
  have hmargin := contactSmallLeftRationalMargin
  exact contactSmallLeftPositive_of_uniformBounds
    _ _ _ _ hcore herror hunit hmargin

end PrecategoryFormal
