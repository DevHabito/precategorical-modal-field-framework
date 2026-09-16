import PrecategoryFormal.PosetCountBridge

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- A concrete `k`-element representative set in the `(m+1)`-vertex ground set. -/
abbrev RepresentativeChoice (m k : Nat) :=
  {s : Finset (CountGround m) // s ∈ representativeSets m k}

/--
Canonical coordinate model for an MF-R008 code.

The first coordinate chooses `k = j+1`, the second chooses the actual labeled
representative set containing `0`, and the third chooses a labeled partial
order on canonical coordinates `Fin k`.  The order payload has the same finite
cardinality for every representative set of size `k`; this is precisely the
fiber decomposition used in MF-R008.
-/
abbrev CanonicalRepresentativeCode (m : Nat) :=
  Σ j : Fin (m + 1), RepresentativeChoice m (j.val + 1) × PartialOrderMatrix (j.val + 1)

/-- The subtype of representative choices has the expected finite cardinality. -/
theorem natCard_representativeChoice (m k : Nat) :
    Nat.card (RepresentativeChoice m k) = (representativeSets m k).card := by
  classical
  exact Nat.subtype_card (representativeSets m k) (fun s => Iff.rfl)

/--
The explicit canonical code type has exactly the fiber-sum cardinality; the
count is therefore derived from a finite type rather than stipulated by the
formula.
-/
theorem natCard_canonicalRepresentativeCode (m : Nat) :
    Nat.card (CanonicalRepresentativeCode m) =
      representativeCodeCountFromFibers m labeledPosetCount := by
  classical
  rw [Nat.card_sigma]
  unfold representativeCodeCountFromFibers
  rw [← Fin.sum_univ_eq_sum_range]
  apply Finset.sum_congr rfl
  intro j hj
  rw [Nat.card_prod]
  rw [natCard_representativeChoice]
  rw [← labeledPosetCount_eq_natCard_partialOrderMatrix]

/-- The explicit five-vertex canonical code type has cardinality `5234`. -/
theorem natCard_canonicalRepresentativeCode_five :
    Nat.card (CanonicalRepresentativeCode 4) = 5234 := by
  rw [natCard_canonicalRepresentativeCode]
  exact representativeCodeCount_five_verified

end PrecategoryFormal