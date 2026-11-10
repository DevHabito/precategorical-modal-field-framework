import PrecategoryFormal.A119RealIntervalCore

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.A119RealIntervalEvaluator

open PrecategoryFormal.A119IntervalEvaluator
open PrecategoryFormal.A119RealIntervalCore

/--
Interpret the very same rational-constant A119 expression tree over reals,
rather than assuming pointwise real inputs are rational.
-/
def evalReal : Expr → ℝ → ℝ → ℝ
  | .lit c, _, _ => (c:ℝ)
  | .source, s, _ => s
  | .alpha, _, α => α
  | .add p q, s, α => evalReal p s α + evalReal q s α
  | .sub p q, s, α => evalReal p s α - evalReal q s α
  | .mul p q, s, α => evalReal p s α * evalReal q s α
  | .div p q, s, α => evalReal p s α / evalReal q s α
  | .pow p n, s, α => (evalReal p s α)^n

theorem pow_real_sound (x : Interval) (a : ℝ)
    (ha : containsReal x a) (n : ℕ) :
    containsReal (powI x n) (a^n) := by
  induction n with
  | zero =>
      simp [powI, containsReal, singleton]
  | succ n ih =>
      simpa [powI, pow_succ, mul_comm] using
        (mul_real_sound x (powI x n) a (a^n) ha ih)

/--
Exact rational endpoint interval computations enclose every real point
evaluation, for all expression trees on two real variables. This theorem
does not rely on density of rationals, nor on floating point arithmetic.
-/
theorem intervalValue_sound_real
    (e : Expr) (S A : Interval) (s α : ℝ)
    (hs : containsReal S s) (hα : containsReal A α)
    (z : Interval) (hz : intervalValue e S A = some z) :
    containsReal z (evalReal e s α) := by
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
          exact add_real_sound x y (evalReal p s α) (evalReal q s α)
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
          exact sub_real_sound x y (evalReal p s α) (evalReal q s α)
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
          exact mul_real_sound x y (evalReal p s α) (evalReal q s α)
            (ihp x hp) (ihq y hq)
  | div p q ihp ihq =>
      cases hp : intervalValue p S A with
      | none => simp [intervalValue, hp] at hz
      | some x =>
        cases hq : intervalValue q S A with
        | none => simp [intervalValue, hp, hq] at hz
        | some y =>
          simp [intervalValue, hp, hq] at hz
          exact div_real_sound x y z (evalReal p s α) (evalReal q s α)
            (ihp x hp) (ihq y hq) hz
  | pow p n ihp =>
      cases hp : intervalValue p S A with
      | none => simp [intervalValue, hp] at hz
      | some x =>
          simp [intervalValue, hp] at hz
          subst z
          exact pow_real_sound x (evalReal p s α) (ihp x hp) n

end PrecategoryFormal.A119RealIntervalEvaluator
