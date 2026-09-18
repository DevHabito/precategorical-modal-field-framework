import PrecategoryFormal.EdgeTogglePairing

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Relabel a directed relation by a vertex permutation. -/
def relabelRelation {α : Type*}
    (σ : Equiv.Perm α) (r : α → α → Prop) : α → α → Prop :=
  fun x y => r (σ.symm x) (σ.symm y)

/-- A path in a relabeled relation pulls back to a path in the original relation. -/
theorem relabeledReach_to_original {α : Type*}
    (σ : Equiv.Perm α) (r : α → α → Prop)
    {x y : α}
    (h : RelationReach (relabelRelation σ r) x y) :
    RelationReach r (σ.symm x) (σ.symm y) := by
  induction h with
  | refl =>
      exact Relation.ReflTransGen.refl
  | tail hxy hyz ih =>
      apply ih.tail
      simpa [relabelRelation] using hyz

/-- A path in the original relation pushes forward to the relabeled relation. -/
theorem originalReach_to_relabel {α : Type*}
    (σ : Equiv.Perm α) (r : α → α → Prop)
    {x y : α}
    (h : RelationReach r x y) :
    RelationReach (relabelRelation σ r) (σ x) (σ y) := by
  induction h with
  | refl =>
      exact Relation.ReflTransGen.refl
  | tail hxy hyz ih =>
      apply ih.tail
      simpa [relabelRelation] using hyz

/-- Exact reachability equivariance under relabeling. -/
theorem relationReach_relabel_iff {α : Type*}
    (σ : Equiv.Perm α) (r : α → α → Prop) (x y : α) :
    RelationReach (relabelRelation σ r) x y ↔
      RelationReach r (σ.symm x) (σ.symm y) := by
  constructor
  · exact relabeledReach_to_original σ r
  · intro h
    have hpushed :=
      originalReach_to_relabel σ r h
    simpa using hpushed

/-- Full reachability-preorder equality is invariant under relabeling. -/
theorem sameReachability_relabel_iff {α : Type*}
    (σ : Equiv.Perm α) (r s : α → α → Prop) :
    SameReachability (relabelRelation σ r) (relabelRelation σ s) ↔
      SameReachability r s := by
  constructor
  · intro h x y
    have hxy := h (σ x) (σ y)
    simpa [relationReach_relabel_iff] using hxy
  · intro h x y
    rw [relationReach_relabel_iff, relationReach_relabel_iff]
    exact h (σ.symm x) (σ.symm y)

/-- Relabeling commutes with adding one distinguished edge. -/
theorem relabelRelation_addEdge {α : Type*}
    (σ : Equiv.Perm α) (r : α → α → Prop) (u v : α) :
    relabelRelation σ (addRelationEdge r u v) =
      addRelationEdge (relabelRelation σ r) (σ u) (σ v) := by
  funext x y
  simp [relabelRelation, addRelationEdge]

/-- Pivotality of a distinguished edge is invariant under relabeling. -/
theorem addEdge_changes_relabel_iff {α : Type*}
    (σ : Equiv.Perm α) (r : α → α → Prop) (u v : α) :
    (¬ SameReachability
      (relabelRelation σ r)
      (addRelationEdge (relabelRelation σ r) (σ u) (σ v)))
    ↔
    (¬ SameReachability r (addRelationEdge r u v)) := by
  rw [addEdge_changesReachability_iff, addEdge_changesReachability_iff]
  have hreach :=
    relationReach_relabel_iff σ r (σ u) (σ v)
  simpa using not_congr hreach

/--
A concrete permutation sending one ordered pair of distinct vertices to
another ordered pair of distinct vertices.
-/
def orderedPairPerm {α : Type*} [DecidableEq α]
    (u v u' v' : α) : Equiv.Perm α :=
  (Equiv.swap u u').trans
    (Equiv.swap ((Equiv.swap u u') v) v')

/-- The ordered-pair permutation sends the source to the requested source. -/
theorem orderedPairPerm_apply_source {α : Type*} [DecidableEq α]
    {u v u' v' : α}
    (huv : u ≠ v) (huv' : u' ≠ v') :
    orderedPairPerm u v u' v' u = u' := by
  let s₁ : Equiv.Perm α := Equiv.swap u u'
  let w : α := s₁ v
  have hw : w ≠ u' := by
    intro h
    have heq : s₁ v = s₁ u := by
      simpa [w, s₁] using h
    have hvu : v = u := s₁.injective heq
    exact huv hvu.symm
  change (Equiv.swap w v') (s₁ u) = u'
  have hsu : s₁ u = u' := by
    simp [s₁]
  rw [hsu]
  exact Equiv.swap_apply_of_ne_of_ne hw.symm huv'

/-- The ordered-pair permutation sends the target to the requested target. -/
theorem orderedPairPerm_apply_target {α : Type*} [DecidableEq α]
    {u v u' v' : α}
    (huv : u ≠ v) :
    orderedPairPerm u v u' v' v = v' := by
  let s₁ : Equiv.Perm α := Equiv.swap u u'
  let w : α := s₁ v
  change (Equiv.swap w v') (s₁ v) = v'
  change (Equiv.swap w v') w = v'
  exact Equiv.swap_apply_left w v'

/--
Any two directed non-loop edge positions are related by a vertex permutation.
-/
theorem exists_perm_maps_ordered_pair {α : Type*} [DecidableEq α]
    {u v u' v' : α}
    (huv : u ≠ v) (huv' : u' ≠ v') :
    ∃ σ : Equiv.Perm α, σ u = u' ∧ σ v = v' := by
  refine ⟨orderedPairPerm u v u' v', ?_, ?_⟩
  · exact orderedPairPerm_apply_source huv huv'
  · exact orderedPairPerm_apply_target huv

end PrecategoryFormal
