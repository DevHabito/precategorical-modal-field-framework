import PrecategoryFormal.A113CoefficientIdentity
import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
# Frozen A113 small-left closure (experimental, UNCOMPILED)

The proof closes the ten-term remainder using existing theorem-level
coefficient envelopes. Do not promote without the pinned Lean build,
axiom trace, and independent checker replay.
-/

private theorem a113PowAbsLeOne (x : ℝ) (n : ℕ)
    (hx0 : 0 ≤ x) (hx1 : x ≤ 1) : |x ^ n| ≤ 1 := by
  rw [abs_of_nonneg (pow_nonneg hx0 n)]
  induction n with
  | zero => norm_num
  | succ n ih =>
      calc
        x ^ (n + 1) = x ^ n * x := pow_succ _ _
        _ ≤ x ^ n * 1 :=
          mul_le_mul_of_nonneg_left hx1 (pow_nonneg hx0 n)
        _ = x ^ n := by ring
        _ ≤ 1 := ih

private theorem a113ProductCap (x y unit : ℝ)
    (hunit : 0 ≤ unit)
    (hx : |x| ≤ unit) (hy : |y| ≤ 1) :
    |x * y| ≤ unit := by
  rw [abs_mul]
  calc
    |x| * |y| ≤ unit * |y| :=
      mul_le_mul_of_nonneg_right hx (abs_nonneg y)
    _ ≤ unit * 1 := mul_le_mul_of_nonneg_left hy hunit
    _ = unit := by ring

private theorem a113TripleCap (x y z unit : ℝ)
    (hunit : 0 ≤ unit)
    (hx : |x| ≤ unit) (hy : |y| ≤ 1)
    (hz : |z| ≤ 1) :
    |x * y * z| ≤ unit := by
  exact a113ProductCap (x * y) z unit hunit
    (a113ProductCap x y unit hunit hx hy) hz

private theorem a113AffineCap
    (coeff linear base unit : ℝ) (size k : ℕ)
    (hunit : 0 ≤ unit) (hsize : 0 < (size : ℝ))
    (hc : |coeff| ≤ 5 * unit)
    (hd : |linear| ≤ 3 * unit / (size : ℝ))
    (hb : |base ^ k| ≤ 1) :
    |(coeff + (k : ℝ) * linear) * base ^ k| ≤
      5 * unit + (k : ℝ) * (3 * unit / (size : ℝ)) := by
  have hk0 : 0 ≤ (k : ℝ) := Nat.cast_nonneg _
  have hlin : |(k : ℝ) * linear| ≤
      (k : ℝ) * (3 * unit / (size : ℝ)) := by
    rw [abs_mul, abs_of_nonneg hk0]
    exact mul_le_mul_of_nonneg_left hd hk0
  have hsum : |coeff + (k : ℝ) * linear| ≤
      5 * unit + (k : ℝ) * (3 * unit / (size : ℝ)) := by
    calc
      _ ≤ |coeff| + |(k : ℝ) * linear| := abs_add_le _ _
      _ ≤ 5 * unit + (k : ℝ) * (3 * unit / (size : ℝ)) :=
        add_le_add hc hlin
  have hcap0 : 0 ≤ 5 * unit + (k : ℝ) * (3 * unit / (size : ℝ)) := by
    positivity
  exact a113ProductCap _ _ _ hcap0 hsum hb

/-- Explicit A83/A84 actual-to-ideal bound; no error-bound hypothesis. -/
theorem a113ActualFactor_abs_error_lt_twenty_units
    (size k : ℕ) (source : ℝ)
    (hsize : 521 ≤ size)
    (_hkLower : 2 ≤ k) (hkUpper : k ≤ 29)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    |a113ActualFactor size k source -
      contactIdealCore k (1 / 8) (1 / 2) source| <
        20 * a113Unit size := by
  let unit := a113Unit size
  let e1 := (a113TargetMass size - (1 / 2 : ℝ)) *
    (source - (1 / 8 : ℝ)) * ((1 / 8 : ℝ) * source) ^ k
  let e2 := (a113H size source false - (1 / 2 : ℝ)) *
    ((1 / 8 : ℝ) - 1 / 2) * ((1 / 8 : ℝ) * (1 / 2 : ℝ)) ^ k
  let e3 := (a113H size (1 / 8) true - (1 / 2 : ℝ)) *
    ((1 / 2 : ℝ) - source) * (source * (1 / 2 : ℝ)) ^ k
  let a1 := (a113BetaAffine size source +
    (k : ℝ) * a113BetaLinear size source) * (1 / 8 : ℝ) ^ k
  let a2 := (a113SourceAffine size source +
    (k : ℝ) * a113SourceLinear size source) * source ^ k
  let a3 := (a113TargetAffine size source +
    (k : ℝ) * a113TargetLinear size source) * (1 / 2 : ℝ) ^ k
  let c0 := a113ConstantCoefficient size source

  have hu : 0 < unit := a113Unit_pos size
  have hmReal : (521 : ℝ) ≤ size := by exact_mod_cast hsize
  have hmPos : 0 < (size : ℝ) := by linarith
  have hkReal : (k : ℝ) ≤ 29 := by exact_mod_cast hkUpper
  have hs0 : (0 : ℝ) ≤ source := by linarith
  have hs1 : source ≤ (1 : ℝ) := by linarith
  have hb1 : |source - (1 / 8 : ℝ)| ≤ 1 := by
    apply abs_le.mpr
    constructor <;> linarith
  have hb2 : |(1 / 8 : ℝ) - 1 / 2| ≤ 1 := by norm_num
  have hb3 : |(1 / 2 : ℝ) - source| ≤ 1 := by
    apply abs_le.mpr
    constructor <;> linarith

  have hbp1 : |((1 / 8 : ℝ) * source) ^ k| ≤ 1 :=
    a113PowAbsLeOne _ k (by positivity) (by nlinarith [hsUpper])
  have hbp2 : |((1 / 8 : ℝ) * (1 / 2 : ℝ)) ^ k| ≤ 1 :=
    a113PowAbsLeOne _ k (by norm_num) (by norm_num)
  have hbp3 : |(source * (1 / 2 : ℝ)) ^ k| ≤ 1 :=
    a113PowAbsLeOne _ k (by positivity) (by nlinarith [hsUpper])
  have hpBeta : |(1 / 8 : ℝ) ^ k| ≤ 1 :=
    a113PowAbsLeOne _ k (by norm_num) (by norm_num)
  have hpSource : |source ^ k| ≤ 1 :=
    a113PowAbsLeOne _ k hs0 hs1
  have hpTarget : |(1 / 2 : ℝ) ^ k| ≤ 1 :=
    a113PowAbsLeOne _ k (by norm_num) (by norm_num)

  have hA : |a113TargetMass size - (1 / 2 : ℝ)| ≤ unit := by
    have hh := a113TargetMass_abs_error_le_half_unit size hsize
    dsimp [unit]
    linarith [a113Unit_pos size]
  have hHs : |a113H size source false - (1 / 2 : ℝ)| ≤ unit :=
    le_of_lt (a113HSource_abs_sub_half_lt_unit size source
      hsize hsLower hsUpper)
  have hHb : |a113H size (1 / 8) true - (1 / 2 : ℝ)| ≤ unit :=
    le_of_lt (a113HBeta_abs_sub_half_lt_unit size hsize)
  have he1 : |e1| ≤ unit := by
    dsimp [e1]
    exact a113TripleCap _ _ _ _ (le_of_lt hu) hA hb1 hbp1
  have he2 : |e2| ≤ unit := by
    dsimp [e2]
    exact a113TripleCap _ _ _ _ (le_of_lt hu) hHs hb2 hbp2
  have he3 : |e3| ≤ unit := by
    dsimp [e3]
    exact a113TripleCap _ _ _ _ (le_of_lt hu) hHb hb3 hbp3

  have hcs := a113AffineCoefficientsBound size source
    hsize hsLower hsUpper
  have hds := a113LinearCoefficientsBound size source
    hsize hsLower hsUpper
  have ha1 : |a1| ≤ 5 * unit + (k : ℝ) * (3 * unit / (size : ℝ)) := by
    dsimp [a1, unit]
    exact a113AffineCap _ _ _ _ size k (le_of_lt (a113Unit_pos size))
      hmPos (le_of_lt hcs.1) hds.1 hpBeta
  have ha2 : |a2| ≤ 5 * unit + (k : ℝ) * (3 * unit / (size : ℝ)) := by
    dsimp [a2, unit]
    exact a113AffineCap _ _ _ _ size k (le_of_lt (a113Unit_pos size))
      hmPos (le_of_lt hcs.2.1) hds.2.1 hpSource
  have ha3 : |a3| ≤ 5 * unit + (k : ℝ) * (3 * unit / (size : ℝ)) := by
    dsimp [a3, unit]
    exact a113AffineCap _ _ _ _ size k (le_of_lt (a113Unit_pos size))
      hmPos (le_of_lt hcs.2.2) hds.2.2 hpTarget
  have hc0 : |c0| ≤ 6 * unit / (size : ℝ) := by
    dsimp [c0, unit]
    exact a113ConstantCoefficientBound size source
      hsize hsLower hsUpper

  have htri : |e1 + e2 + e3 + a1 + a2 + a3 + c0| ≤
      |e1| + |e2| + |e3| + |a1| + |a2| + |a3| + |c0| := by
    have h12 := abs_add_le e1 e2
    have h123 := abs_add_le (e1 + e2) e3
    have h1234 := abs_add_le (e1 + e2 + e3) a1
    have h12345 := abs_add_le (e1 + e2 + e3 + a1) a2
    have h123456 := abs_add_le (e1 + e2 + e3 + a1 + a2) a3
    have h1234567 := abs_add_le (e1 + e2 + e3 + a1 + a2 + a3) c0
    linarith

  have hsum : |e1 + e2 + e3 + a1 + a2 + a3 + c0| ≤
      (18 + (9 * (k : ℝ) + 6) / (size : ℝ)) * unit := by
    calc
      _ ≤ |e1| + |e2| + |e3| + |a1| + |a2| + |a3| + |c0| := htri
      _ ≤ 3 * unit + 3 * (5 * unit +
          (k : ℝ) * (3 * unit / (size : ℝ))) +
          6 * unit / (size : ℝ) := by
            linarith [he1, he2, he3, ha1, ha2, ha3, hc0]
      _ = (18 + (9 * (k : ℝ) + 6) / (size : ℝ)) * unit := by ring

  have hnumber : (9 * (k : ℝ) + 6) ≤ 267 := by linarith
  have hscale : 521 * (9 * (k : ℝ) + 6) ≤ 267 * (size : ℝ) := by
    nlinarith [hnumber, hmReal]
  have hratio : (9 * (k : ℝ) + 6) / (size : ℝ) ≤ (267 : ℝ) / 521 := by
    apply (div_le_iff₀ hmPos).2
    nlinarith [hscale]
  have hcoeff : 18 + (9 * (k : ℝ) + 6) / (size : ℝ) < 20 := by
    linarith
  have hfinal := mul_lt_mul_of_pos_right hcoeff hu
  calc
    |a113ActualFactor size k source -
        contactIdealCore k (1 / 8) (1 / 2) source| =
        |e1 + e2 + e3 + a1 + a2 + a3 + c0| := by
          rw [a113ActualFactor_sub_ideal_eq_namedErrors]
    _ ≤ (18 + (9 * (k : ℝ) + 6) / (size : ℝ)) * unit := hsum
    _ < 20 * a113Unit size := hfinal

/-- Full historical A113 small-left positivity, at the frozen contract. -/
theorem a113ActualFactor_smallLeft_pos
    (size k : ℕ) (source : ℝ)
    (hsize : 521 ≤ size)
    (hkLower : 2 ≤ k) (hkUpper : k ≤ 29)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    0 < a113ActualFactor size k source := by
  exact a113ActualFactor_pos_of_uniform_error size k source
    hsize hkLower hkUpper hsLower hsUpper
    (a113ActualFactor_abs_error_lt_twenty_units
      size k source hsize hkLower hkUpper hsLower hsUpper)

end PrecategoryFormal