import PrecategoryFormal.EdgeToggleSemanticBridge

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- A directed non-loop edge on the five labeled vertices. -/
abbrev DirectedNonloopEdge5 := { p : Vertex × Vertex // p.1 ≠ p.2 }

/-- Every row-major directed-edge index lies in the declared 20-coordinate mask. -/
theorem edgeIndex5_lt (u v : Vertex) :
    edgeIndex 5 u.val v.val < edgeCount 5 := by
  fin_cases u <;> fin_cases v <;> native_decide

/-- The published row-major, diagonal-deleted coordinate of a directed non-loop edge. -/
def directedEdgeCoord5 (e : DirectedNonloopEdge5) : Fin (edgeCount 5) :=
  ⟨edgeIndex 5 e.1.1.val e.1.2.val, edgeIndex5_lt e.1.1 e.1.2⟩

/-- Explicit finite decidability plumbing for coordinate bijectivity. -/
private instance directedEdgeCoord5BijectiveDecidable :
    Decidable (Function.Bijective directedEdgeCoord5) := by
  unfold Function.Bijective Function.Injective Function.Surjective
  letI : DecidablePred (fun a : DirectedNonloopEdge5 =>
      ∀ b : DirectedNonloopEdge5,
        directedEdgeCoord5 a = directedEdgeCoord5 b → a = b) :=
    fun _ => inferInstance
  letI : DecidablePred (fun e : Fin (edgeCount 5) =>
      ∃ a : DirectedNonloopEdge5, directedEdgeCoord5 a = e) :=
    fun _ => inferInstance
  infer_instance

/-- The 20 bit coordinates are exactly the 20 directed non-loop edges. -/
theorem directedEdgeCoord5_bijective : Function.Bijective directedEdgeCoord5 := by
  native_decide

/-- Canonical equivalence between actual directed non-loop edges and mask coordinates. -/
def directedEdgeCoordEquiv5 : DirectedNonloopEdge5 ≃ Fin (edgeCount 5) :=
  Equiv.ofBijective directedEdgeCoord5 directedEdgeCoord5_bijective

/-- A shifted singleton bit is true at exactly its selected coordinate. -/
theorem singletonBit_testBit (e i : Nat) :
    (1 <<< e).testBit i = decide (i = e) := by
  rw [Bool.eq_iff_iff]
  simp [Nat.testBit_shiftLeft, Nat.testBit_one_eq_true_iff_self_eq_zero]
  omega

/-- `toggleMask` is literal xor with one selected coordinate bit. -/
theorem toggleMask_testBit
    {n : Nat} (g : GraphMask n) (e : Fin (edgeCount n)) (i : Nat) :
    (toggleMask g e).val.testBit i =
      (g.val.testBit i ^^ decide (i = e.val)) := by
  simp [toggleMask, Nat.testBit_xor, singletonBit_testBit]

/-- The selected bit is complemented. -/
theorem toggleMask_selected
    {n : Nat} (g : GraphMask n) (e : Fin (edgeCount n)) :
    (toggleMask g e).val.testBit e.val = !(g.val.testBit e.val) := by
  rw [toggleMask_testBit]
  simp

/-- Every unselected bit is unchanged. -/
theorem toggleMask_other
    {n : Nat} (g : GraphMask n) (e : Fin (edgeCount n)) (i : Nat)
    (h : i ≠ e.val) :
    (toggleMask g e).val.testBit i = g.val.testBit i := by
  rw [toggleMask_testBit]
  simp [h]

/-- On a genuine non-loop edge, graph adjacency is exactly its mask coordinate bit. -/
theorem maskGraph5_edge_coord (g : GraphMask 5) (e : DirectedNonloopEdge5) :
    maskGraph5 g e.1.1 e.1.2 = g.val.testBit (directedEdgeCoord5 e).val := by
  rcases e with ⟨⟨u, v⟩, huv⟩
  have hval : u.val ≠ v.val := by
    intro h
    exact huv (Fin.ext h)
  simp [maskGraph5, hasEdge, directedEdgeCoord5, u.isLt, v.isLt, hval]

/-- The interpreted mask graph has no self-loops. -/
theorem maskGraph5_loop_false (g : GraphMask 5) (u : Vertex) :
    maskGraph5 g u u = false := by
  simp [maskGraph5, hasEdge]

/-- Toggling the coordinate of an actual edge complements that edge. -/
theorem toggleMask_flips_edge5 (g : GraphMask 5) (e : DirectedNonloopEdge5) :
    maskGraph5 (toggleMask g (directedEdgeCoord5 e)) e.1.1 e.1.2 =
      !(maskGraph5 g e.1.1 e.1.2) := by
  rw [maskGraph5_edge_coord, maskGraph5_edge_coord]
  exact toggleMask_selected g (directedEdgeCoord5 e)

/-- Toggling one actual edge leaves every other actual edge unchanged. -/
theorem toggleMask_preserves_other_edge5
    (g : GraphMask 5) (e f : DirectedNonloopEdge5) (hfe : f ≠ e) :
    maskGraph5 (toggleMask g (directedEdgeCoord5 e)) f.1.1 f.1.2 =
      maskGraph5 g f.1.1 f.1.2 := by
  rw [maskGraph5_edge_coord, maskGraph5_edge_coord]
  apply toggleMask_other
  intro hval
  apply hfe
  apply directedEdgeCoord5_bijective.1
  exact Fin.ext hval

/--
Every declared mask coordinate therefore names one unique directed non-loop edge,
and toggling that coordinate has exactly the published graph-edge semantics.
-/
theorem coordinate_toggle_has_unique_edge_semantics5
    (g : GraphMask 5) (c : Fin (edgeCount 5)) :
    let e := directedEdgeCoordEquiv5.symm c
    maskGraph5 (toggleMask g c) e.1.1 e.1.2 = !(maskGraph5 g e.1.1 e.1.2) ∧
      ∀ f : DirectedNonloopEdge5, f ≠ e →
        maskGraph5 (toggleMask g c) f.1.1 f.1.2 = maskGraph5 g f.1.1 f.1.2 := by
  let e := directedEdgeCoordEquiv5.symm c
  have hcoord : directedEdgeCoord5 e = c := directedEdgeCoordEquiv5.apply_symm_apply c
  subst c
  constructor
  · exact toggleMask_flips_edge5 g e
  · intro f hfe
    exact toggleMask_preserves_other_edge5 g e f hfe

end PrecategoryFormal
