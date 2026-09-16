import PrecategoryFormal.PosetEnumeration

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

@[simp]
theorem pairLower_pairSlot {n : Nat} (i j : Fin n) (h : i.val < j.val) :
    pairLower (pairSlot i j h) = i := by
  apply Fin.ext
  rfl

@[simp]
theorem pairUpper_pairSlot {n : Nat} (i j : Fin n) (h : i.val < j.val) :
    pairUpper (pairSlot i j h) = j := by
  rfl

/-- The decoded relation is reflexive for every orientation assignment. -/
@[simp]
theorem orientationLE_refl {n : Nat} (o : OrientationAssignment n) (i : Fin n) :
    orientationLE o i i = true := by
  simp [orientationLE]

/--
The three-state pair representation makes antisymmetry structural: opposite
strict directions cannot both be true for distinct vertices.
-/
theorem orientationLE_antisymm {n : Nat} (o : OrientationAssignment n) {i j : Fin n}
    (hij : orientationLE o i j = true)
    (hji : orientationLE o j i = true) : i = j := by
  by_contra hne
  have hvalne : i.val ≠ j.val := by
    intro hv
    exact hne (Fin.ext hv)
  by_cases hlt : i.val < j.val
  · have hnrev : ¬ j.val < i.val := by omega
    simp [orientationLE, hlt, hnrev] at hij hji
    omega
  · have hgt : j.val < i.val := by omega
    simp [orientationLE, hlt, hgt] at hij hji
    omega

/-- Mathematical transitivity of the decoded Boolean relation. -/
def OrientationTransitive {n : Nat} (o : OrientationAssignment n) : Prop :=
  ∀ i j k : Fin n,
    orientationLE o i j = true →
    orientationLE o j k = true →
    orientationLE o i k = true

/-- The executable finite checker is exactly the mathematical transitivity predicate. -/
theorem orientationTransitiveBool_eq_true_iff {n : Nat} (o : OrientationAssignment n) :
    orientationTransitiveBool o = true ↔ OrientationTransitive o := by
  constructor
  · intro h
    have h' :
        ∀ i j k : Fin n,
          (orientationLE o i j = false ∨ orientationLE o j k = false) ∨
            orientationLE o i k = true := by
      simpa [orientationTransitiveBool] using h
    intro i j k hij hjk
    rcases h' i j k with hfalse | hik
    · rcases hfalse with hfalse | hfalse
      · rw [hij] at hfalse
        simp at hfalse
      · rw [hjk] at hfalse
        simp at hfalse
    · exact hik
  · intro h
    have h' :
        ∀ i j k : Fin n,
          (orientationLE o i j = false ∨ orientationLE o j k = false) ∨
            orientationLE o i k = true := by
      intro i j k
      cases hij : orientationLE o i j with
      | false => exact Or.inl (Or.inl rfl)
      | true =>
          cases hjk : orientationLE o j k with
          | false => exact Or.inl (Or.inr rfl)
          | true => exact Or.inr (h i j k hij hjk)
    simpa [orientationTransitiveBool] using h'

/-- Boolean relation-matrix formulation of a labeled partial order. -/
def IsPartialOrderMatrix {n : Nat} (r : Fin n → Fin n → Bool) : Prop :=
  (∀ i, r i i = true) ∧
  (∀ i j, r i j = true → r j i = true → i = j) ∧
  (∀ i j k, r i j = true → r j k = true → r i k = true)

/-- Every transitive accepted orientation decodes to a genuine partial-order matrix. -/
theorem orientationLE_isPartialOrderMatrix {n : Nat} (o : OrientationAssignment n)
    (htrans : orientationTransitiveBool o = true) :
    IsPartialOrderMatrix (orientationLE o) := by
  refine ⟨?_, ?_, ?_⟩
  · intro i
    exact orientationLE_refl o i
  · intro i j hij hji
    exact orientationLE_antisymm o hij hji
  · exact (orientationTransitiveBool_eq_true_iff o).1 htrans

end PrecategoryFormal