import PrecategoryFormal.A119IntervalArithmetic

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.A119IntervalEvaluator

open PrecategoryFormal.A119IntervalArithmetic

/-- A closed interval with exact rational endpoints. -/
structure Interval where
  lo : ℚ
  hi : ℚ
deriving Repr, DecidableEq

def contains (i : Interval) (x : ℚ) : Prop := i.lo ≤ x ∧ x ≤ i.hi
def singleton (x : ℚ) : Interval := ⟨x, x⟩
def addI (x y : Interval) : Interval := ⟨x.lo + y.lo, x.hi + y.hi⟩
def subI (x y : Interval) : Interval := ⟨x.lo - y.hi, x.hi - y.lo⟩
def mulI (x y : Interval) : Interval :=
  ⟨fourLower x.lo x.hi y.lo y.hi,
    fourUpper x.lo x.hi y.lo y.hi⟩

/--
An interval division fails closed if the divisor interval touches zero.
A successful value contains every actual rational quotient.
-/
def divI? (x y : Interval) : Option Interval :=
  if 0 < y.lo ∨ y.hi < 0 then
    some ⟨fourLower x.lo x.hi (1/y.hi) (1/y.lo),
          fourUpper x.lo x.hi (1/y.hi) (1/y.lo)⟩
  else none

def powI (x : Interval) : ℕ → Interval
  | 0 => singleton 1
  | n+1 => mulI x (powI x n)

theorem add_sound (x y : Interval) (a b : ℚ)
    (ha : contains x a) (hb : contains y b) :
    contains (addI x y) (a+b) := by
  exact PrecategoryFormal.A119Compact.add_enclosure
    x.lo x.hi y.lo y.hi a b ha hb

theorem sub_sound (x y : Interval) (a b : ℚ)
    (ha : contains x a) (hb : contains y b) :
    contains (subI x y) (a-b) := by
  exact PrecategoryFormal.A119Compact.sub_enclosure
    x.lo x.hi y.lo y.hi a b ha hb

theorem mul_sound (x y : Interval) (a b : ℚ)
    (ha : contains x a) (hb : contains y b) :
    contains (mulI x y) (a*b) := by
  exact four_corner_mul_enclosure
    x.lo x.hi y.lo y.hi a b ha hb

theorem div_sound (x y z : Interval) (a b : ℚ)
    (ha : contains x a) (hb : contains y b)
    (hz : divI? x y = some z) :
    contains z (a/b) := by
  unfold divI? at hz
  split at hz
  · rename_i hsep
    cases hz
    exact division_enclosure
      x.lo x.hi y.lo y.hi a b ha hb hsep
  · contradiction

theorem pow_sound (x : Interval) (a : ℚ)
    (ha : contains x a) (n : ℕ) :
    contains (powI x n) (a^n) := by
  induction n with
  | zero =>
      simp [powI, contains, singleton]
  | succ n ih =>
      simpa [powI, pow_succ, mul_comm] using
        (mul_sound x (powI x n) a (a^n) ha ih)

/-- Minimal expression tree: a rational expression in source and alpha. -/
inductive Expr where
  | lit : ℚ → Expr
  | source : Expr
  | alpha : Expr
  | add : Expr → Expr → Expr
  | sub : Expr → Expr → Expr
  | mul : Expr → Expr → Expr
  | div : Expr → Expr → Expr
  | pow : Expr → ℕ → Expr
deriving Repr

def pointValue : Expr → ℚ → ℚ → ℚ
  | .lit c, _, _ => c
  | .source, s, _ => s
  | .alpha, _, α => α
  | .add p q, s, α => pointValue p s α + pointValue q s α
  | .sub p q, s, α => pointValue p s α - pointValue q s α
  | .mul p q, s, α => pointValue p s α * pointValue q s α
  | .div p q, s, α => pointValue p s α / pointValue q s α
  | .pow p n, s, α => (pointValue p s α)^n

def intervalValue : Expr → Interval → Interval → Option Interval
  | .lit c, _, _ => some (singleton c)
  | .source, S, _ => some S
  | .alpha, _, A => some A
  | .add p q, S, A => do
      let x ← intervalValue p S A
      let y ← intervalValue q S A
      return addI x y
  | .sub p q, S, A => do
      let x ← intervalValue p S A
      let y ← intervalValue q S A
      return subI x y
  | .mul p q, S, A => do
      let x ← intervalValue p S A
      let y ← intervalValue q S A
      return mulI x y
  | .div p q, S, A => do
      let x ← intervalValue p S A
      let y ← intervalValue q S A
      divI? x y
  | .pow p n, S, A => do
      let x ← intervalValue p S A
      return powI x n

/--
Compositional soundness: if interval evaluation returns a result,
every rational point inside the inputs is contained in the result.
This theorem does not assume positivity of the final expression.
-/
theorem intervalValue_sound
    (e : Expr) (S A : Interval) (s α : ℚ)
    (hs : contains S s) (hα : contains A α)
    (z : Interval) (hz : intervalValue e S A = some z) :
    contains z (pointValue e s α) := by
  induction e generalizing z with
  | lit c =>
      simp only [intervalValue, Option.some.injEq] at hz
      subst z
      exact ⟨le_refl _, le_refl _⟩
  | source =>
      simp only [intervalValue, Option.some.injEq] at hz
      subst z
      exact hs
  | alpha =>
      simp only [intervalValue, Option.some.injEq] at hz
      subst z
      exact hα
  | add p q ihp ihq =>
      cases hp : intervalValue p S A with
      | none => simp [intervalValue, hp] at hz
      | some x =>
        cases hq : intervalValue q S A with
        | none => simp [intervalValue, hp, hq] at hz
        | some y =>
          simp [intervalValue, hp, hq] at hz
          subst z
          exact add_sound x y (pointValue p s α) (pointValue q s α)
            (ihp x hp) (ihq y hq)
  | sub p q ihp ihq =>
      cases hp : intervalValue p S A with
      | none => simp [intervalValue, hp] at hz
      | some x =>
        cases hq : intervalValue q S A with
        | none => simp [intervalValue, hp, hq] at hz
        | some y =>
          simp [intervalValue, hp, hq] at hz
          subst z
          exact sub_sound x y (pointValue p s α) (pointValue q s α)
            (ihp x hp) (ihq y hq)
  | mul p q ihp ihq =>
      cases hp : intervalValue p S A with
      | none => simp [intervalValue, hp] at hz
      | some x =>
        cases hq : intervalValue q S A with
        | none => simp [intervalValue, hp, hq] at hz
        | some y =>
          simp [intervalValue, hp, hq] at hz
          subst z
          exact mul_sound x y (pointValue p s α) (pointValue q s α)
            (ihp x hp) (ihq y hq)
  | div p q ihp ihq =>
      cases hp : intervalValue p S A with
      | none => simp [intervalValue, hp] at hz
      | some x =>
        cases hq : intervalValue q S A with
        | none => simp [intervalValue, hp, hq] at hz
        | some y =>
          simp [intervalValue, hp, hq] at hz
          exact div_sound x y z (pointValue p s α) (pointValue q s α)
            (ihp x hp) (ihq y hq) hz
  | pow p n ihp =>
      cases hp : intervalValue p S A with
      | none => simp [intervalValue, hp] at hz
      | some x =>
          simp [intervalValue, hp] at hz
          subst z
          exact pow_sound x (pointValue p s α) (ihp x hp) n

end PrecategoryFormal.A119IntervalEvaluator
