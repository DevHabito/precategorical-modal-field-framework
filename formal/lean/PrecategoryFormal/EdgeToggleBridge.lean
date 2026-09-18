import PrecategoryFormal.EdgeToggleSemantics
import PrecategoryFormal.EdgeToggleEnumeration

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- The finite labeled carrier used by the mask-based graph model. -/
abbrev MaskVertex (n : Nat) := Fin n

/-- Mathematical edge relation decoded from a loopless directed graph mask. -/
def maskRelation (n graph : Nat) : MaskVertex n → MaskVertex n → Prop :=
  fun u v => maskHasDirectedEdge n graph u.val v.val = true

/--
A finite-set presentation of a forward-closed source/target separator for a
mask graph.  This is deliberately semantic: it does not use the optimized
bit-mask cut routine from `EdgeToggleEnumeration.lean`.
-/
def FinsetForwardClosedSeparator
    (n graph : Nat) (u v : MaskVertex n) (S : Finset (MaskVertex n)) : Prop :=
  u ∈ S ∧
  v ∉ S ∧
  ∀ ⦃x y : MaskVertex n⦄, x ∈ S → maskRelation n graph x y → y ∈ S

/-- The finite-set separator is exactly the generic separator predicate. -/
theorem finsetForwardClosedSeparator_iff
    (n graph : Nat) (u v : MaskVertex n) (S : Finset (MaskVertex n)) :
    FinsetForwardClosedSeparator n graph u v S ↔
      ForwardClosedSeparator (maskRelation n graph) u v (fun x => x ∈ S) := by
  rfl

/--
On a finite labeled carrier, non-reachability is equivalent to the existence
of a forward-closed separator represented as an actual `Finset`.

The forward direction converts the semantic separator supplied by
`not_relationReach_iff_exists_forwardClosedSeparator` into its finite truth
set.  Thus no bounded-path assumption is used.
-/
theorem not_maskRelationReach_iff_exists_finsetSeparator
    (n graph : Nat) (u v : MaskVertex n) :
    ¬ RelationReach (maskRelation n graph) u v ↔
      ∃ S : Finset (MaskVertex n),
        FinsetForwardClosedSeparator n graph u v S := by
  constructor
  · intro hnot
    obtain ⟨P, hP⟩ :=
      (not_relationReach_iff_exists_forwardClosedSeparator
        (maskRelation n graph) u v).1 hnot
    classical
    let S : Finset (MaskVertex n) := Finset.univ.filter P
    refine ⟨S, ?_⟩
    rcases hP with ⟨hu, hv, hclosed⟩
    refine ⟨?_, ?_, ?_⟩
    · simp [S, hu]
    · simpa [S] using hv
    · intro x y hx hxy
      have hxP : P x := by
        simpa [S] using hx
      have hyP : P y := hclosed hxP hxy
      simpa [S] using hyP
  · rintro ⟨S, hS⟩
    apply (not_relationReach_iff_exists_forwardClosedSeparator
      (maskRelation n graph) u v).2
    exact ⟨fun x => x ∈ S, (finsetForwardClosedSeparator_iff n graph u v S).1 hS⟩

/--
Reference executable checker for non-reachability.  It searches finite subsets
rather than using the optimized integer cut-mask implementation.
-/
def noReachFinsetBool
    (n graph : Nat) (u v : MaskVertex n) : Bool :=
  decide (∃ S : Finset (MaskVertex n),
    FinsetForwardClosedSeparator n graph u v S)

/--
Semantic correctness of the reference executable checker: it returns true
exactly when there is no mathematical reflexive-transitive path.
-/
theorem noReachFinsetBool_eq_true_iff
    (n graph : Nat) (u v : MaskVertex n) :
    noReachFinsetBool n graph u v = true ↔
      ¬ RelationReach (maskRelation n graph) u v := by
  change
    decide (∃ S : Finset (MaskVertex n),
      FinsetForwardClosedSeparator n graph u v S) = true ↔
      ¬ RelationReach (maskRelation n graph) u v
  rw [Bool.decide_iff]
  exact (not_maskRelationReach_iff_exists_finsetSeparator n graph u v).symm

end PrecategoryFormal
