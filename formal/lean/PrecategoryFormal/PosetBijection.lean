import PrecategoryFormal.PosetSemantics

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Rebuilding a pair slot from its two endpoints recovers the original slot. -/
@[simp]
theorem pairSlot_pairLower_pairUpper {n : Nat} (p : PairSlot n) :
    pairSlot (pairLower p) (pairUpper p) p.2.isLt = p := by
  rcases p with ⟨j, i⟩
  apply Sigma.ext
  · rfl
  · apply Fin.ext
    rfl

/--
Encode a Boolean relation back into one three-state value per unordered pair.
The first branch records lower-to-upper comparability; the second records the
opposite direction; otherwise the pair is incomparable.
-/
def orientationOfRelation {n : Nat} (r : Fin n → Fin n → Bool) : OrientationAssignment n :=
  fun p =>
    if r (pairLower p) (pairUpper p) = true then 1
    else if r (pairUpper p) (pairLower p) = true then 2
    else 0

/-- The relation decoder is injective on orientation assignments. -/
theorem orientationOfRelation_orientationLE {n : Nat} (o : OrientationAssignment n) :
    orientationOfRelation (orientationLE o) = o := by
  funext p
  apply Fin.ext
  have hlt : (pairLower p).val < (pairUpper p).val := p.2.isLt
  have hnlt : ¬ (pairUpper p).val < (pairLower p).val := by omega
  have hstate : (o p).val = 0 ∨ (o p).val = 1 ∨ (o p).val = 2 := by omega
  rcases hstate with h0 | h1 | h2
  · simp [orientationOfRelation, orientationLE, hlt, hnlt, h0]
  · simp [orientationOfRelation, orientationLE, hlt, hnlt, h1]
  · simp [orientationOfRelation, orientationLE, hlt, hnlt, h2]

/--
Every Boolean partial-order matrix is recovered exactly after encoding its
unordered pairs and decoding them again.
-/
theorem orientationLE_orientationOfRelation {n : Nat}
    (r : Fin n → Fin n → Bool) (hr : IsPartialOrderMatrix r) :
    orientationLE (orientationOfRelation r) = r := by
  funext i j
  by_cases hij : i.val < j.val
  · have hji : ¬ j.val < i.val := by omega
    have hne : i ≠ j := by
      intro h
      subst j
      omega
    have hnotboth : ¬ (r i j = true ∧ r j i = true) := by
      rintro ⟨hijr, hjir⟩
      exact hne (hr.2.1 i j hijr hjir)
    cases hir : r i j <;> cases hri : r j i <;>
      simp_all [orientationLE, orientationOfRelation, hij, hji]
  · by_cases hji : j.val < i.val
    · have hne : i ≠ j := by
        intro h
        subst j
        omega
      have hnotboth : ¬ (r i j = true ∧ r j i = true) := by
        rintro ⟨hijr, hjir⟩
        exact hne (hr.2.1 i j hijr hjir)
      cases hir : r i j <;> cases hri : r j i <;>
        simp_all [orientationLE, orientationOfRelation, hij, hji]
    · have heq : i = j := by
        apply Fin.ext
        omega
      subst j
      rw [orientationLE_refl]
      exact (hr.1 i).symm

/-- The inverse encoding of a partial-order matrix always passes the finite checker. -/
theorem orientationOfRelation_transitive {n : Nat}
    (r : Fin n → Fin n → Bool) (hr : IsPartialOrderMatrix r) :
    orientationTransitiveBool (orientationOfRelation r) = true := by
  apply (orientationTransitiveBool_eq_true_iff _).2
  intro i j k hij hjk
  have hdecode := orientationLE_orientationOfRelation r hr
  rw [hdecode] at hij hjk ⊢
  exact hr.2.2 i j k hij hjk

/-- Accepted three-state encodings. -/
abbrev EncodedPoset (n : Nat) :=
  {o : OrientationAssignment n // orientationTransitiveBool o = true}

/-- Boolean relation matrices satisfying reflexivity, antisymmetry and transitivity. -/
abbrev PartialOrderMatrix (n : Nat) :=
  {r : Fin n → Fin n → Bool // IsPartialOrderMatrix r}

/--
Exact bijection between the finite three-state encoding and labeled Boolean
partial-order matrices on `Fin n`.
-/
def encodedPosetEquivPartialOrderMatrix (n : Nat) :
    EncodedPoset n ≃ PartialOrderMatrix n where
  toFun o := ⟨orientationLE o.1, orientationLE_isPartialOrderMatrix o.1 o.2⟩
  invFun r := ⟨orientationOfRelation r.1, orientationOfRelation_transitive r.1 r.2⟩
  left_inv o := by
    apply Subtype.ext
    exact orientationOfRelation_orientationLE o.1
  right_inv r := by
    apply Subtype.ext
    exact orientationLE_orientationOfRelation r.1 r.2

end PrecategoryFormal