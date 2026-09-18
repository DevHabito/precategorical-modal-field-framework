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
All ordered vertex pairs that violate forward closure of `S`: the source is
inside `S`, the graph contains the directed edge, and the target is outside.
This finite object makes the executable checker constructive without asking
Lean for a global `Decidable` instance for a quantified proposition.
-/
def forwardClosureViolations
    (n graph : Nat) (S : Finset (MaskVertex n)) :
    Finset (MaskVertex n × MaskVertex n) :=
  ((Finset.univ : Finset (MaskVertex n)).product
      (Finset.univ : Finset (MaskVertex n))).filter fun xy =>
    xy.1 ∈ S ∧
      maskHasDirectedEdge n graph xy.1.val xy.2.val = true ∧
      xy.2 ∉ S

/-- No violation pair exists exactly when `S` is forward closed. -/
theorem forwardClosureViolations_card_eq_zero_iff
    (n graph : Nat) (S : Finset (MaskVertex n)) :
    (forwardClosureViolations n graph S).card = 0 ↔
      ∀ ⦃x y : MaskVertex n⦄, x ∈ S → maskRelation n graph x y → y ∈ S := by
  rw [Finset.card_eq_zero]
  constructor
  · intro hempty x y hx hxy
    by_contra hy
    have hedge :
        maskHasDirectedEdge n graph x.val y.val = true := by
      simpa [maskRelation] using hxy
    have hmem : (x, y) ∈ forwardClosureViolations n graph S := by
      apply Finset.mem_filter.mpr
      constructor
      · simp
      · exact ⟨hx, hedge, hy⟩
    rw [hempty] at hmem
    simp at hmem
  · intro hclosed
    apply Finset.eq_empty_iff_forall_notMem.mpr
    rintro ⟨x, y⟩ hmem
    have hdata :
        x ∈ S ∧
          maskHasDirectedEdge n graph x.val y.val = true ∧
          y ∉ S :=
      (Finset.mem_filter.mp hmem).2
    apply hdata.2.2
    apply hclosed hdata.1
    simpa [maskRelation] using hdata.2.1

/-- Constructive Boolean checker for one concrete finite separator. -/
def finsetForwardClosedSeparatorBool
    (n graph : Nat) (u v : MaskVertex n) (S : Finset (MaskVertex n)) : Bool :=
  decide (u ∈ S) &&
  !(decide (v ∈ S)) &&
  decide ((forwardClosureViolations n graph S).card = 0)

/-- The Boolean separator checker has exactly the intended proposition. -/
theorem finsetForwardClosedSeparatorBool_eq_true_iff
    (n graph : Nat) (u v : MaskVertex n) (S : Finset (MaskVertex n)) :
    finsetForwardClosedSeparatorBool n graph u v S = true ↔
      FinsetForwardClosedSeparator n graph u v S := by
  simp only [
    finsetForwardClosedSeparatorBool,
    Bool.and_eq_true,
    decide_eq_true_eq,
    not_decide_eq_true,
    FinsetForwardClosedSeparator
  ]
  rw [forwardClosureViolations_card_eq_zero_iff]
  exact and_assoc

/-- All concrete separator subsets accepted by the constructive checker. -/
def acceptedSeparatorFinsets
    (n graph : Nat) (u v : MaskVertex n) :
    Finset (Finset (MaskVertex n)) :=
  ((Finset.univ : Finset (MaskVertex n)).powerset).filter fun S =>
    finsetForwardClosedSeparatorBool n graph u v S = true

/--
Reference executable checker for non-reachability.  It searches the explicit
powerset of the finite carrier, independently of the optimized integer
cut-mask implementation.
-/
def noReachFinsetBool
    (n graph : Nat) (u v : MaskVertex n) : Bool :=
  decide (0 < (acceptedSeparatorFinsets n graph u v).card)

/-- The reference Boolean search is true exactly when some separator exists. -/
theorem noReachFinsetBool_eq_true_iff_exists
    (n graph : Nat) (u v : MaskVertex n) :
    noReachFinsetBool n graph u v = true ↔
      ∃ S : Finset (MaskVertex n),
        FinsetForwardClosedSeparator n graph u v S := by
  rw [show noReachFinsetBool n graph u v = true ↔
      0 < (acceptedSeparatorFinsets n graph u v).card by
        simp [noReachFinsetBool]]
  rw [Finset.card_pos]
  constructor
  · rintro ⟨S, hS⟩
    refine ⟨S, ?_⟩
    have hfiltered :
        finsetForwardClosedSeparatorBool n graph u v S = true := by
      exact (Finset.mem_filter.mp hS).2
    exact (finsetForwardClosedSeparatorBool_eq_true_iff n graph u v S).1 hfiltered
  · rintro ⟨S, hS⟩
    refine ⟨S, ?_⟩
    apply Finset.mem_filter.mpr
    constructor
    · simp
    · exact (finsetForwardClosedSeparatorBool_eq_true_iff n graph u v S).2 hS

/--
Semantic correctness of the reference executable checker: it returns true
exactly when there is no mathematical reflexive-transitive path.
-/
theorem noReachFinsetBool_eq_true_iff
    (n graph : Nat) (u v : MaskVertex n) :
    noReachFinsetBool n graph u v = true ↔
      ¬ RelationReach (maskRelation n graph) u v := by
  rw [noReachFinsetBool_eq_true_iff_exists]
  exact (not_maskRelationReach_iff_exists_finsetSeparator n graph u v).symm

end PrecategoryFormal
