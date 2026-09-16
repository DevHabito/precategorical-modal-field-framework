import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/--
A slot for one unordered pair of vertices of `Fin n`.

The first component is the larger endpoint `j`; the second is an element of
`Fin j`, hence a smaller endpoint `i < j`.  Thus every unordered pair occurs
exactly once without storing a redundant symmetry bit.
-/
abbrev PairSlot (n : Nat) := Σ j : Fin n, Fin j.val

/--
For each unordered pair choose one of three states:

* `0`: incomparable;
* `1`: lower endpoint is below the upper endpoint;
* `2`: upper endpoint is below the lower endpoint.

This representation builds antisymmetry into the candidate space.
-/
abbrev OrientationAssignment (n : Nat) := PairSlot n → Fin 3

/-- The lower endpoint of a pair slot, coerced back into `Fin n`. -/
def pairLower {n : Nat} (p : PairSlot n) : Fin n :=
  ⟨p.2.val, lt_trans p.2.isLt p.1.isLt⟩

/-- The upper endpoint of a pair slot. -/
def pairUpper {n : Nat} (p : PairSlot n) : Fin n := p.1

/-- Construct the unique slot for endpoints `i < j`. -/
def pairSlot {n : Nat} (i j : Fin n) (h : i.val < j.val) : PairSlot n :=
  ⟨j, ⟨i.val, h⟩⟩

/--
Decode one orientation assignment into a reflexive Boolean relation.
The diagonal is always true; off diagonal, the unique unordered-pair state
chooses at most one direction.
-/
def orientationLE {n : Nat} (o : OrientationAssignment n) (i j : Fin n) : Bool :=
  if hij : i.val < j.val then
    decide ((o (pairSlot i j hij)).val = 1)
  else if hji : j.val < i.val then
    decide ((o (pairSlot j i hji)).val = 2)
  else
    true

/-- Executable transitivity test for an orientation assignment. -/
def orientationTransitiveBool {n : Nat} (o : OrientationAssignment n) : Bool :=
  (List.finRange n).all fun i =>
    (List.finRange n).all fun j =>
      (List.finRange n).all fun k =>
        !(orientationLE o i j && orientationLE o j k) || orientationLE o i k

/-- Number of transitive three-state orientation assignments on `n` labeled vertices. -/
def encodedPosetCount (n : Nat) : Nat :=
  ((Finset.univ : Finset (OrientationAssignment n)).filter
    (fun o => orientationTransitiveBool o = true)).card

/-- There are exactly `3^10 = 59049` antisymmetric orientation candidates on five labels. -/
theorem orientationAssignment_card_five :
    Fintype.card (OrientationAssignment 5) = 59049 := by
  native_decide

/-- Exact finite enumeration checkpoints for `n = 1,2,3,4`. -/
theorem encodedPosetCount_small :
    encodedPosetCount 1 = 1 ∧
    encodedPosetCount 2 = 3 ∧
    encodedPosetCount 3 = 19 ∧
    encodedPosetCount 4 = 219 := by
  native_decide

/-- Exact finite enumeration checkpoint for five labels. -/
theorem encodedPosetCount_five : encodedPosetCount 5 = 4231 := by
  native_decide

end PrecategoryFormal