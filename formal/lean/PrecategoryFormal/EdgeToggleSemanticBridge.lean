import PrecategoryFormal.GraphSCCBridge
import PrecategoryFormal.EdgeToggleSensitivity

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Interpret an MF-R011 five-vertex bit mask as an ordinary Boolean digraph. -/
def maskGraph5 (g : GraphMask 5) : BoolDigraph :=
  fun u v => hasEdge g u.val v.val

/-- Reflexivity plus the original edge relation. -/
def referenceInitial5 (g : GraphMask 5) : BoolDigraph :=
  fun u v => decide (u = v) || maskGraph5 g u v

/-- One semantic Floyd-Warshall relation update through intermediate vertex `k`. -/
def referenceStep5 (r : BoolDigraph) (k : Vertex) : BoolDigraph :=
  fun u v => r u v || (r u k && r k v)

/--
A definitionally independent five-step reference closure.  Unlike `reachRows`,
this presentation is a direct relation transformer and is convenient for proofs.
-/
def referenceClosure5 (g : GraphMask 5) : BoolDigraph :=
  referenceStep5
    (referenceStep5
      (referenceStep5
        (referenceStep5
          (referenceStep5 (referenceInitial5 g) 0) 1) 2) 3) 4

/-- Every `true` entry of a Boolean relation denotes genuine mathematical reachability. -/
def RelationSound5 (g : GraphMask 5) (r : BoolDigraph) : Prop :=
  ∀ u v, r u v = true → Reach (maskGraph5 g) u v

theorem referenceInitial5_sound (g : GraphMask 5) :
    RelationSound5 g (referenceInitial5 g) := by
  intro u v h
  have h' : decide (u = v) = true ∨ maskGraph5 g u v = true := by
    simpa [referenceInitial5] using h
  rcases h' with huv | hedge
  · have huv' : u = v := by simpa using huv
    subst v
    exact Relation.ReflTransGen.refl
  · exact Relation.ReflTransGen.single hedge

/-- Floyd-Warshall's elementary update preserves reachability soundness. -/
theorem referenceStep5_sound
    (g : GraphMask 5) (r : BoolDigraph) (k : Vertex)
    (h : RelationSound5 g r) : RelationSound5 g (referenceStep5 r k) := by
  intro u v huv
  have huv' : r u v = true ∨ (r u k = true ∧ r k v = true) := by
    simpa [referenceStep5] using huv
  rcases huv' with direct | via
  · exact h u v direct
  · exact (h u k via.1).trans (h k v via.2)

/-- The direct five-step reference closure never invents a path. -/
theorem referenceClosure5_sound (g : GraphMask 5) :
    RelationSound5 g (referenceClosure5 g) := by
  apply referenceStep5_sound g
  apply referenceStep5_sound g
  apply referenceStep5_sound g
  apply referenceStep5_sound g
  apply referenceStep5_sound g
  exact referenceInitial5_sound g

/--
For the fixed five-vertex ensemble, the reference closure is reflexive,
contains every original edge, and is transitive.

This is an exact finite recognition theorem over all `2^20` masks.  It is not
presented as a generic Floyd-Warshall theorem for arbitrary finite types.
-/
def ReferenceClosureLaws5 (g : GraphMask 5) : Prop :=
  let r := referenceClosure5 g
  (∀ u, r u u = true) ∧
  (∀ u v, maskGraph5 g u v = true → r u v = true) ∧
  (∀ u v w, r u v = true → r v w = true → r u w = true)

theorem referenceClosureLaws5_all :
    ∀ g : GraphMask 5, ReferenceClosureLaws5 g := by
  native_decide

/-- Every mathematical path is present in the fixed five-vertex reference closure. -/
theorem referenceClosure5_complete
    (g : GraphMask 5) {u v : Vertex} (h : Reach (maskGraph5 g) u v) :
    referenceClosure5 g u v = true := by
  have laws := referenceClosureLaws5_all g
  induction h with
  | refl =>
      exact laws.1 _
  | tail hreach hedge ih =>
      exact laws.2.2 _ _ _ ih (laws.2.1 _ _ hedge)

/-- The independent reference closure is exactly `Relation.ReflTransGen`. -/
theorem referenceClosure5_eq_true_iff_reach
    (g : GraphMask 5) (u v : Vertex) :
    referenceClosure5 g u v = true ↔ Reach (maskGraph5 g) u v := by
  constructor
  · exact referenceClosure5_sound g u v
  · exact referenceClosure5_complete g

/--
Audit the compact `reachCode` used in the MF-R011 enumerator against the
independent semantic reference relation, cell by cell, and certify its 25-bit bound.
-/
def ReachCodeSemanticAudit5 (g : GraphMask 5) : Prop :=
  let code := reachCode g
  let r := referenceClosure5 g
  code < 2 ^ 25 ∧
    ∀ u v : Vertex, code.testBit (u.val * 5 + v.val) = r u v

/-- Exact all-graph bridge between the executable compact code and the reference closure. -/
theorem reachCodeSemanticAudit5_all :
    ∀ g : GraphMask 5, ReachCodeSemanticAudit5 g := by
  native_decide

/-- Every low reachability-code bit has the intended mathematical meaning. -/
theorem reachCode_testBit_iff_reach
    (g : GraphMask 5) (u v : Vertex) :
    (reachCode g).testBit (u.val * 5 + v.val) = true ↔
      Reach (maskGraph5 g) u v := by
  have hcell := (reachCodeSemanticAudit5_all g).2 u v
  rw [hcell]
  exact referenceClosure5_eq_true_iff_reach g u v

/-- Two compact codes are equal only if the full mathematical reachability relations agree. -/
theorem reachCode_eq_implies_sameReachability5
    {g h : GraphMask 5} (hc : reachCode g = reachCode h) :
    ∀ u v : Vertex,
      Reach (maskGraph5 g) u v ↔ Reach (maskGraph5 h) u v := by
  intro u v
  constructor
  · intro hreach
    apply (reachCode_testBit_iff_reach h u v).1
    rw [← hc]
    exact (reachCode_testBit_iff_reach g u v).2 hreach
  · intro hreach
    apply (reachCode_testBit_iff_reach g u v).1
    rw [hc]
    exact (reachCode_testBit_iff_reach h u v).2 hreach

/-- If the full mathematical reachability relations agree, their compact codes agree. -/
theorem sameReachability5_implies_reachCode_eq
    {g h : GraphMask 5}
    (hsame : ∀ u v : Vertex,
      Reach (maskGraph5 g) u v ↔ Reach (maskGraph5 h) u v) :
    reachCode g = reachCode h := by
  apply Nat.eq_of_testBit_eq
  intro i
  by_cases hi : i < 25
  · let u : Vertex := ⟨i / 5, by omega⟩
    let v : Vertex := ⟨i % 5, by omega⟩
    have hidx : u.val * 5 + v.val = i := by
      simpa [u, v] using Nat.div_add_mod i 5
    rw [← hidx, Bool.eq_iff_iff,
      reachCode_testBit_iff_reach,
      reachCode_testBit_iff_reach]
    exact hsame u v
  · have h25i : 25 ≤ i := Nat.le_of_not_gt hi
    have hg25 := (reachCodeSemanticAudit5_all g).1
    have hh25 := (reachCodeSemanticAudit5_all h).1
    have hp : 2 ^ 25 ≤ 2 ^ i := Nat.pow_le_pow_right (by decide) h25i
    have hg : reachCode g < 2 ^ i := Nat.lt_of_lt_of_le hg25 hp
    have hh : reachCode h < 2 ^ i := Nat.lt_of_lt_of_le hh25 hp
    rw [Nat.testBit_lt_two_pow hg, Nat.testBit_lt_two_pow hh]

/-- Exact semantic characterization of compact-code equality at `n = 5`. -/
theorem reachCode_eq_iff_sameReachability5 (g h : GraphMask 5) :
    reachCode g = reachCode h ↔
      ∀ u v : Vertex,
        Reach (maskGraph5 g) u v ↔ Reach (maskGraph5 h) u v := by
  constructor
  · exact reachCode_eq_implies_sameReachability5
  · exact sameReachability5_implies_reachCode_eq

end PrecategoryFormal
