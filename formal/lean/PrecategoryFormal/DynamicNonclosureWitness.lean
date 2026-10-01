import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Four rational weights on the fixed support `q = (0,1,2,3)`. -/
structure FourWeights where
  p0 : ℚ
  p1 : ℚ
  p2 : ℚ
  p3 : ℚ
  deriving DecidableEq

/-- Total mass of a four-point weight vector. -/
def FourWeights.total (p : FourWeights) : ℚ :=
  p.p0 + p.p1 + p.p2 + p.p3

/-- Mean on the fixed support `q = (0,1,2,3)`. -/
def FourWeights.mean (p : FourWeights) : ℚ :=
  p.p1 + 2 * p.p2 + 3 * p.p3

/--
Geometric moment on the fixed support: `sum_i p_i r^q_i` for
`q = (0,1,2,3)`.
-/
def FourWeights.geomMoment (r : ℚ) (p : FourWeights) : ℚ :=
  p.p0 + p.p1 * r + p.p2 * r^2 + p.p3 * r^3

/-- Strict positivity of every weight. -/
def FourWeights.StrictlyPositive (p : FourWeights) : Prop :=
  0 < p.p0 ∧ 0 < p.p1 ∧ 0 < p.p2 ∧ 0 < p.p3

/-- Rationalized MF-R049 witness, plus branch. -/
def nonclosurePlus : FourWeights :=
  ⟨19 / 80, 13 / 40, 11 / 80, 3 / 10⟩

/-- Rationalized MF-R049 witness, minus branch. -/
def nonclosureMinus : FourWeights :=
  ⟨21 / 80, 7 / 40, 29 / 80, 1 / 5⟩

/-- Both witness distributions have strictly positive entries. -/
theorem nonclosurePlus_positive : nonclosurePlus.StrictlyPositive := by
  norm_num [FourWeights.StrictlyPositive, nonclosurePlus]

/-- Both witness distributions have strictly positive entries. -/
theorem nonclosureMinus_positive : nonclosureMinus.StrictlyPositive := by
  norm_num [FourWeights.StrictlyPositive, nonclosureMinus]

/-- The plus witness is normalized. -/
theorem nonclosurePlus_total : nonclosurePlus.total = 1 := by
  norm_num [FourWeights.total, nonclosurePlus]

/-- The minus witness is normalized. -/
theorem nonclosureMinus_total : nonclosureMinus.total = 1 := by
  norm_num [FourWeights.total, nonclosureMinus]

/-- The two witnesses have the same exact mean `3/2`. -/
theorem nonclosurePlus_mean : nonclosurePlus.mean = 3 / 2 := by
  norm_num [FourWeights.mean, nonclosurePlus]

theorem nonclosureMinus_mean : nonclosureMinus.mean = 3 / 2 := by
  norm_num [FourWeights.mean, nonclosureMinus]

/-- At base `r=1/4` (corresponding to `lambda = log 4`), both moments are `85/256`. -/
theorem nonclosurePlus_initialMoment :
    nonclosurePlus.geomMoment (1 / 4) = 85 / 256 := by
  norm_num [FourWeights.geomMoment, nonclosurePlus]

theorem nonclosureMinus_initialMoment :
    nonclosureMinus.geomMoment (1 / 4) = 85 / 256 := by
  norm_num [FourWeights.geomMoment, nonclosureMinus]

/-- At transported base `r=1/2`, the plus moment is `151/320`. -/
theorem nonclosurePlus_transportMoment :
    nonclosurePlus.geomMoment (1 / 2) = 151 / 320 := by
  norm_num [FourWeights.geomMoment, nonclosurePlus]

/-- At transported base `r=1/2`, the minus moment is `149/320`. -/
theorem nonclosureMinus_transportMoment :
    nonclosureMinus.geomMoment (1 / 2) = 149 / 320 := by
  norm_num [FourWeights.geomMoment, nonclosureMinus]

/-- The transported moments differ by the exact positive rational `1/160`. -/
theorem nonclosure_transportMoment_difference :
    nonclosurePlus.geomMoment (1 / 2) -
      nonclosureMinus.geomMoment (1 / 2) = 1 / 160 := by
  rw [nonclosurePlus_transportMoment, nonclosureMinus_transportMoment]
  norm_num

/-- In particular, the transported geometric moments are unequal. -/
theorem nonclosure_transportMoment_ne :
    nonclosurePlus.geomMoment (1 / 2) ≠
      nonclosureMinus.geomMoment (1 / 2) := by
  intro h
  have hd :
      nonclosurePlus.geomMoment (1 / 2) -
        nonclosureMinus.geomMoment (1 / 2) = 0 := by
    rw [h]
    ring
  rw [nonclosure_transportMoment_difference] at hd
  norm_num at hd

/--
Exact algebraic core of MF-R049: two strictly positive normalized four-point
probability vectors have the same mean and the same initial geometric moment,
but a different transported geometric moment.
-/
theorem dynamicNonclosure_rational_witness :
    nonclosurePlus.StrictlyPositive ∧
    nonclosureMinus.StrictlyPositive ∧
    nonclosurePlus.total = 1 ∧
    nonclosureMinus.total = 1 ∧
    nonclosurePlus.mean = nonclosureMinus.mean ∧
    nonclosurePlus.geomMoment (1 / 4) =
      nonclosureMinus.geomMoment (1 / 4) ∧
    nonclosurePlus.geomMoment (1 / 2) ≠
      nonclosureMinus.geomMoment (1 / 2) := by
  refine ⟨nonclosurePlus_positive, nonclosureMinus_positive,
    nonclosurePlus_total, nonclosureMinus_total, ?_, ?_,
    nonclosure_transportMoment_ne⟩
  · rw [nonclosurePlus_mean, nonclosureMinus_mean]
  · rw [nonclosurePlus_initialMoment, nonclosureMinus_initialMoment]

end PrecategoryFormal
