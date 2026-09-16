import PrecategoryFormal.RepresentativeCodeType

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Reflexive, antisymmetric and transitive Boolean relation on an arbitrary type. -/
def IsBoolPartialOrder {α : Type*} (r : α → α → Bool) : Prop :=
  (∀ i, r i i = true) ∧
  (∀ i j, r i j = true → r j i = true → i = j) ∧
  (∀ i j k, r i j = true → r j k = true → r i k = true)

/-- Boolean presentation of a partial order on the actual carrier `α`. -/
abbrev BoolPartialOrder (α : Type*) :=
  {r : α → α → Bool // IsBoolPartialOrder r}

/-- The `Fin n` matrix presentation is definitionally the same order predicate. -/
def partialOrderMatrixEquivBoolPartialOrder (n : Nat) :
    PartialOrderMatrix n ≃ BoolPartialOrder (Fin n) where
  toFun r := ⟨r.1, r.2⟩
  invFun r := ⟨r.1, r.2⟩
  left_inv _ := rfl
  right_inv _ := rfl

/-- Transport Boolean partial orders across a bijection of carriers. -/
def boolPartialOrderCongr {α β : Type*} (e : α ≃ β) :
    BoolPartialOrder α ≃ BoolPartialOrder β where
  toFun r :=
    ⟨fun x y => r.1 (e.symm x) (e.symm y), by
      refine ⟨?_, ?_, ?_⟩
      · intro i
        exact r.2.1 (e.symm i)
      · intro i j hij hji
        exact e.symm.injective (r.2.2.1 (e.symm i) (e.symm j) hij hji)
      · intro i j k hij hjk
        exact r.2.2.2 (e.symm i) (e.symm j) (e.symm k) hij hjk⟩
  invFun r :=
    ⟨fun x y => r.1 (e x) (e y), by
      refine ⟨?_, ?_, ?_⟩
      · intro i
        exact r.2.1 (e i)
      · intro i j hij hji
        exact e.injective (r.2.2.1 (e i) (e j) hij hji)
      · intro i j k hij hjk
        exact r.2.2.2 (e i) (e j) (e k) hij hjk⟩
  left_inv r := by
    apply Subtype.ext
    funext i j
    simp
  right_inv r := by
    apply Subtype.ext
    funext i j
    simp

/-- Every representative choice in the `k`-fiber really has exactly `k` elements. -/
theorem representativeChoice_card {m k : Nat} (S : RepresentativeChoice m k) :
    S.1.card = k := by
  have hmem :
      S.1 ∈ ((Finset.univ : Finset (CountGround m)).powersetCard k) :=
    (Finset.mem_filter.mp S.2).1
  exact (Finset.mem_powersetCard.mp hmem).2

/--
For a concrete representative set `S`, partial orders on canonical coordinates
`Fin k` are exactly partial orders on the actual elements of `S`.
-/
def representativeOrderEquiv {m k : Nat} (S : RepresentativeChoice m k) :
    PartialOrderMatrix k ≃ BoolPartialOrder S.1 :=
  (partialOrderMatrixEquivBoolPartialOrder k).trans <|
    boolPartialOrderCongr (S.1.orderIsoOfFin (representativeChoice_card S)).toEquiv

/-- Literal MF-R008 code: choose the actual representative set and an order on that set. -/
abbrev LiteralRepresentativeCode (m : Nat) :=
  Σ j : Fin (m + 1),
    Σ S : RepresentativeChoice m (j.val + 1), BoolPartialOrder S.1

/-- One canonical fiber is equivalent to the corresponding literal dependent fiber. -/
def canonicalFiberEquivLiteral {m k : Nat} :
    RepresentativeChoice m k × PartialOrderMatrix k ≃
      (Σ S : RepresentativeChoice m k, BoolPartialOrder S.1) where
  toFun x := ⟨x.1, representativeOrderEquiv x.1 x.2⟩
  invFun x := ⟨x.1, (representativeOrderEquiv x.1).symm x.2⟩
  left_inv x := by
    rcases x with ⟨S, P⟩
    simp
  right_inv x := by
    rcases x with ⟨S, P⟩
    simp

/--
The canonical-coordinate code used for counting is exactly equivalent to the
literal published code `(S,P)` with `P` living on the actual representative set.
-/
def canonicalRepresentativeCodeEquivLiteral (m : Nat) :
    CanonicalRepresentativeCode m ≃ LiteralRepresentativeCode m :=
  Equiv.sigmaCongrRight fun _ => canonicalFiberEquivLiteral

/-- The literal MF-R008 code type has the same proved fiber-sum cardinality. -/
theorem natCard_literalRepresentativeCode (m : Nat) :
    Nat.card (LiteralRepresentativeCode m) =
      representativeCodeCountFromFibers m labeledPosetCount := by
  rw [← Nat.card_congr (canonicalRepresentativeCodeEquivLiteral m)]
  exact natCard_canonicalRepresentativeCode m

/-- The literal five-vertex MF-R008 code type has exactly `5234` elements. -/
theorem natCard_literalRepresentativeCode_five :
    Nat.card (LiteralRepresentativeCode 4) = 5234 := by
  rw [natCard_literalRepresentativeCode]
  exact representativeCodeCount_five_verified

end PrecategoryFormal
