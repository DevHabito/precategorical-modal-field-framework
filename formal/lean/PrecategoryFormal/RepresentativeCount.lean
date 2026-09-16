import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

open scoped BigOperators

/--
For the representative-count theorem it is convenient to write the ground set
as `Fin (m + 1)`, so vertex `0` exists without a separate nonemptiness premise.
The original parameter is `n = m + 1`.
-/
abbrev CountGround (m : Nat) := Fin (m + 1)

/--
The `k`-element candidate sets of SCC minimum representatives.  Such a set must
contain vertex `0`, because the SCC containing the globally minimum label has
minimum representative `0`.
-/
def representativeSets (m k : Nat) : Finset (Finset (CountGround m)) :=
  ((Finset.univ : Finset (CountGround m)).powersetCard k).filter
    (({0} : Finset (CountGround m)) ⊆ ·)

/--
Core combinatorial lemma for MF-R008: among `m + 1` labeled vertices, the
number of `k`-element representative sets containing `0` is `choose m (k - 1)`.
-/
theorem card_representativeSets (m k : Nat) (hk : 1 ≤ k) :
    (representativeSets m k).card = Nat.choose m (k - 1) := by
  simpa [representativeSets] using
    Finset.card_filter_powersetCard_subset
      ({0} : Finset (CountGround m))
      (Finset.univ : Finset (CountGround m))
      k
      (by simp)
      (by simpa using hk)

/--
Abstract grouped code count before using the binomial formula.

`p k` is the number of possible quotient-poset payloads on a fixed labeled
`k`-element representative set.  This definition only performs the finite
fiber sum: number of possible representative sets times the size of each
`k`-fiber.
-/
def representativeCodeCountFromFibers (m : Nat) (p : Nat → Nat) : Nat :=
  ∑ j ∈ Finset.range (m + 1),
    (representativeSets m (j + 1)).card * p (j + 1)

/--
MF-R008 structural counting identity, in the shifted index `j = k - 1`:

`N_rep(m+1) = sum_{j=0}^m choose(m,j) * p(j+1)`.

Equivalently, with `n = m+1` and `k=j+1`, this is
`sum_{k=1}^n choose(n-1,k-1) * p(k)`.
-/
theorem representativeCodeCountFromFibers_eq_binomial
    (m : Nat) (p : Nat → Nat) :
    representativeCodeCountFromFibers m p =
      ∑ j ∈ Finset.range (m + 1), Nat.choose m j * p (j + 1) := by
  unfold representativeCodeCountFromFibers
  apply Finset.sum_congr rfl
  intro j hj
  rw [card_representativeSets m (j + 1) (Nat.succ_le_succ (Nat.zero_le j))]
  simp

/--
The historical finite table used for the `n=5` arithmetic checkpoint.
This is deliberately *not* a proof that these are the numbers of labeled
posets; the independent formal verification of those five values is a
separate obligation.
-/
def historicalPosetCountTable : Nat → Nat
  | 1 => 1
  | 2 => 3
  | 3 => 19
  | 4 => 219
  | 5 => 4231
  | _ => 0

/--
Pure arithmetic checkpoint: once the quotient-poset fiber sizes are
`1,3,19,219,4231`, the representative-code count on five vertices is `5234`.
This theorem does not certify the poset-count table itself.
-/
theorem representativeCodeCount_five_arithmetic_checkpoint :
    representativeCodeCountFromFibers 4 historicalPosetCountTable = 5234 := by
  native_decide

end PrecategoryFormal