import PrecategoryFormal.A119IntervalEvaluator
import PrecategoryFormal.A119CriticalExpression

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.A119CertifiedExpression

open PrecategoryFormal.A119IntervalEvaluator
open PrecategoryFormal.A119CriticalExpression

/--
The exact rational computation behind the A119 critical Xi-hat.
It has no logarithm or floating-point operation. Each arithmetic node is
evaluated through the *proved-sound* interval expression interpreter.
-/
def xiExpr (odd : Bool) (r : ℕ) : Expr :=
  let c := Expr.lit
  let s := Expr.source
  let α := Expr.alpha
  let beta := c (1/8)
  let delta := c (1/1875)
  let sigma := if odd then c (1/2) else c 0
  let a := if odd then Expr.div (Expr.add (c 1) s) (c 2) else c 1
  let B := Expr.add (Expr.div beta s) (Expr.mul (c 2) delta)
  let C := Expr.sub (Expr.sub (c 1) (Expr.div beta s)) (Expr.mul (c 4) delta)
  let A := Expr.mul a (Expr.sub (c 1) B)
  let D := Expr.sub (Expr.div (c 1) (Expr.pow s (r-2))) (Expr.mul a B)
  let q := Expr.div (Expr.mul a C) (Expr.add A (Expr.mul α D))
  let T := Expr.sub (c 1) (Expr.mul (c 2) delta)
  let S := Expr.sub (Expr.sub (c 1) q) (Expr.mul (c 2) delta)
  let etaH := Expr.add (Expr.pow α 2) (Expr.mul (Expr.mul (c 2) sigma) α)
  let etaK := Expr.add (Expr.pow α 2)
    (Expr.mul (Expr.mul (c 2) α)
      (Expr.sub (Expr.add sigma (c (r:ℚ))) (c 1)))
  let B1 := Expr.sub
    (Expr.mul (Expr.mul (Expr.mul (Expr.mul (c 2) sigma) α) s) B)
    (Expr.div (Expr.mul (Expr.mul (Expr.mul (c 2) a) α) beta) s)
  let S1 := Expr.sub
    (Expr.sub
      (Expr.sub
        (Expr.mul (Expr.mul (Expr.mul (c 2) sigma) α)
          (Expr.mul s T))
        (Expr.mul (Expr.mul (c 2) a) α))
      (Expr.mul (Expr.mul a q) etaH))
    (c 0)
  let G2 := Expr.mul (Expr.mul (c 2) α)
    (Expr.add (c 1)
      (Expr.mul (Expr.sub (c 1) s)
        (Expr.sub (Expr.add (Expr.sub (Expr.add α (c 2)) sigma) (c 0))
          (c (r:ℚ)))))
  let main := Expr.mul
    (Expr.mul
      (Expr.mul
        (Expr.mul (Expr.sub (c 1) s) α)
        (Expr.div (c 1) (Expr.pow s (r-2)))) q) etaH
  let sourceTerm := Expr.mul q
    (Expr.sub
      (Expr.mul (Expr.mul a B) G2)
      (Expr.mul (Expr.mul (Expr.sub (c 1) s) (Expr.add α (c 1)))
        (Expr.add B1 (Expr.mul (Expr.mul a B) etaK))))
  let target := Expr.sub
    (Expr.mul (Expr.sub (c 1) s) (Expr.sub B1 S1))
    (Expr.mul
      (Expr.mul (Expr.mul (c 2) α) s)
        (Expr.mul a (Expr.sub B S)))
  Expr.add (Expr.add main sourceTerm) target

/--
The expression-tree semantics match the separately declared rational
critical Xi-hat function. A formula-level proof; not an A115 derivation.
-/
theorem xiExpr_matches_critical
    (s α : ℚ) (odd : Bool) (r : ℕ) :
    pointValue (xiExpr odd r) s α =
      criticalXiHat s α odd r := by
  cases odd <;>
    simp [xiExpr, pointValue, criticalXiHat, div_eq_mul_inv] <;> ring

def sourceBox : Interval := ⟨129/1000, 133/1000⟩

def alphaBox (odd : Bool) (r : ℕ) (t₀ t₁ : ℚ) : Interval :=
  let sigma : ℚ := if odd then 1/2 else 0
  let left : ℚ := 2 * ((r:ℚ) + sigma)
  let right : ℚ := (21/10) * ((r:ℚ) + 1 + sigma)
  ⟨left+(right-left)*t₀, left+(right-left)*t₁⟩

/-- True iff the certified interpreter returns a strictly positive range. -/
def passes (odd : Bool) (r : ℕ) (t₀ t₁ : ℚ) : Bool :=
  match intervalValue (xiExpr odd r) sourceBox (alphaBox odd r t₀ t₁) with
  | none => false
  | some box => decide (0 < box.lo)

/--
One certificate's *semantic* inference. Once the Boolean check is kernel
proved, every mathematical point inside that box has Xi-hat>0.
-/
theorem certified_box_sound
    (odd : Bool) (r : ℕ) (t₀ t₁ s α : ℚ)
    (hs : 129/1000 ≤ s ∧ s ≤ 133/1000)
    (hα : (alphaBox odd r t₀ t₁).lo ≤ α ∧
      α ≤ (alphaBox odd r t₀ t₁).hi)
    (hpass : passes odd r t₀ t₁ = true) :
    0 < criticalXiHat s α odd r := by
  unfold passes at hpass
  cases he : intervalValue (xiExpr odd r)
      sourceBox (alphaBox odd r t₀ t₁) with
  | none =>
      simp [he] at hpass
  | some box =>
      simp [he] at hpass
      have hlo : 0 < box.lo := hpass
      have hinside : contains box (pointValue (xiExpr odd r) s α) :=
        intervalValue_sound (xiExpr odd r) sourceBox
          (alphaBox odd r t₀ t₁) s α hs hα box he
      rw [xiExpr_matches_critical] at hinside
      exact lt_of_lt_of_le hlo hinside.1

end PrecategoryFormal.A119CertifiedExpression
