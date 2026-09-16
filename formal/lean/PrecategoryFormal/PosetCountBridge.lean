import PrecategoryFormal.PosetBijection
import PrecategoryFormal.RepresentativeCount

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/--
The executable enumeration count, now used as the formally justified number of
labeled partial orders after the encoding bijection has been established.
-/
def labeledPosetCount (n : Nat) : Nat := encodedPosetCount n

/-- The filtered executable count is the cardinal of the accepted-encoding subtype. -/
theorem encodedPosetCount_eq_natCard (n : Nat) :
    encodedPosetCount n = Nat.card (EncodedPoset n) := by
  unfold encodedPosetCount
  symm
  apply Nat.subtype_card
  intro o
  simp

/--
The executable number `labeledPosetCount n` is exactly the cardinality of
Boolean partial-order matrices on the labeled ground set `Fin n`.
-/
theorem labeledPosetCount_eq_natCard_partialOrderMatrix (n : Nat) :
    labeledPosetCount n = Nat.card (PartialOrderMatrix n) := by
  calc
    labeledPosetCount n = encodedPosetCount n := rfl
    _ = Nat.card (EncodedPoset n) := encodedPosetCount_eq_natCard n
    _ = Nat.card (PartialOrderMatrix n) :=
      Nat.card_congr (encodedPosetEquivPartialOrderMatrix n)

/-- Exact labeled-poset counts through four vertices. -/
theorem labeledPosetCount_small :
    labeledPosetCount 1 = 1 ∧
    labeledPosetCount 2 = 3 ∧
    labeledPosetCount 3 = 19 ∧
    labeledPosetCount 4 = 219 := by
  simpa [labeledPosetCount] using encodedPosetCount_small

/-- Exact labeled-poset count on five vertices. -/
theorem labeledPosetCount_five : labeledPosetCount 5 = 4231 := by
  simpa [labeledPosetCount] using encodedPosetCount_five

/--
MF-R008 structural formula with the quotient-poset factor replaced by its
actual formal cardinality.
-/
theorem representativeCodeCount_labeledPosets (m : Nat) :
    representativeCodeCountFromFibers m labeledPosetCount =
      ∑ j ∈ Finset.range (m + 1),
        Nat.choose m j * Nat.card (PartialOrderMatrix (j + 1)) := by
  rw [representativeCodeCountFromFibers_eq_binomial]
  apply Finset.sum_congr rfl
  intro j hj
  rw [labeledPosetCount_eq_natCard_partialOrderMatrix]

/--
Fully verified five-vertex arithmetic target: unlike the historical checkpoint,
this theorem computes the quotient-poset fiber sizes from the formal finite
encoding rather than assuming the table `1,3,19,219,4231`.
-/
theorem representativeCodeCount_five_verified :
    representativeCodeCountFromFibers 4 labeledPosetCount = 5234 := by
  native_decide

end PrecategoryFormal