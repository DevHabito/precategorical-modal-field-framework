import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

open Filter MeasureTheory Set
open scoped Topology

namespace PrecategoryFormal.PhysicalBridge

/-- The final reduced real integral in the flat 2+1 coefficient calculation. -/
theorem d3ReducedBulkIntegral :
    (∫ w : ℝ in (-1 : ℝ)..1, (1 / 4 : ℝ) * (1 + w ^ 2)⁻¹) = Real.pi / 8 := by
  rw [intervalIntegral.integral_const_mul, integral_inv_one_add_sq,
    Real.arctan_one, Real.arctan_neg, Real.arctan_one]
  ring

theorem d3ReducedRecoveryCoefficient :
    3 * (256 / 9 : ℝ) *
      (∫ w : ℝ in (-1 : ℝ)..1, (1 / 4 : ℝ) * (1 + w ^ 2)⁻¹) =
      32 * Real.pi / 3 := by
  rw [d3ReducedBulkIntegral]
  ring

/-- Linear factor after the substitution in the flat 3+1 integral. -/
theorem d4ExponentialHalfLine :
    (∫ x : ℝ in Ioi (0 : ℝ), Real.exp (-(2 : ℝ) * x)) = 1 / 2 := by
  rw [integral_exp_mul_Ioi (by norm_num : -(2 : ℝ) < 0)]
  norm_num

/-- Flat 3+1 coefficient from the product of the two separated factors. -/
theorem d4GaussianRecoveryCoefficient :
    144 * ((∫ x : ℝ in Ioi (0 : ℝ), Real.exp (-(2 : ℝ) * x)) *
      (∫ u : ℝ in Ioi (0 : ℝ), Real.exp (-(1 : ℝ) * u ^ 2))) ^ 2 =
      9 * Real.pi := by
  rw [d4ExponentialHalfLine, integral_gaussian_Ioi, div_one]
  calc
    _ = 9 * (Real.sqrt Real.pi) ^ 2 := by ring
    _ = 9 * Real.pi := by rw [Real.sq_sqrt Real.pi_pos.le]

/-- In a nonempty graph without isolates, disconnectedness supplies two
unreachable vertices that each have a neighbor. -/
theorem twoEdgeComponentsOfDisconnectedWithoutIsolates {V : Type*} [Nonempty V]
    (G : SimpleGraph V) (hn : ∀ v, ∃ w, G.Adj v w) (hd : ¬ G.Connected) :
    ∃ u v, (∃ u', G.Adj u u') ∧ (∃ v', G.Adj v v') ∧ ¬ G.Reachable u v := by
  classical
  have hp : ¬ (∀ u v, G.Reachable u v) := fun h => hd ⟨h⟩
  obtain ⟨u, hu⟩ := not_forall.mp hp
  obtain ⟨v, huv⟩ := not_forall.mp hu
  exact ⟨u, v, hn u, hn v, huv⟩

/-- The squeeze step from the no-isolate and multiple-component limits.
The model-specific probability inequality and limits are inputs. -/
theorem connectivityLimitOfNoIsolateLimit
    (noIsolates connected multipleComponents : ℕ → ℝ) (p : ℝ)
    (hno : Tendsto noIsolates atTop (𝓝 p))
    (hmultiple : Tendsto multipleComponents atTop (𝓝 0))
    (hl : ∀ᶠ n in atTop, noIsolates n - multipleComponents n ≤ connected n)
    (hu : ∀ᶠ n in atTop, connected n ≤ noIsolates n) :
    Tendsto connected atTop (𝓝 p) := by
  have hlow : Tendsto (fun n => noIsolates n - multipleComponents n) atTop (𝓝 p) := by
    simpa only [sub_zero] using hno.sub hmultiple
  exact hlow.squeeze' hno hl hu

end PrecategoryFormal.PhysicalBridge
