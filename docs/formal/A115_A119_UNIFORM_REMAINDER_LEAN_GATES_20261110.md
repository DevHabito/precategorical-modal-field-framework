# A115–A119 uniform collision remainder: Lean 4 formalization gate

**Date:** 2026-11-10  
**Parent research note:** [A115_A119_UNIFORM_REMAINDER_20261110.md](../research/A115_A119_UNIFORM_REMAINDER_20261110.md)  
**Status:** proof obligations only; no Lean claims are made for this new remainder result. Existing Lean 4.33.1 / Mathlib v4.33.1 toolchain is preserved.

## Target statement

Formalize the reduced cofactor comparison with beta=1/8, delta=1/1875,
s in [129/1000,133/1000], alpha in [8,45], deficit r in Finset.Icc 4 19,
and parity p=0 or 1. For M sufficiently large of that parity and k=h-r+1,
prove there exist **one** M0 and **one** nonnegative constant C, both
independent of s,alpha,r and parity, such that

    |J/(tau^(h+k)) - Lambda_p/M - Xi_p/M^2| <= C/M^3.

Do not claim this is about F2 or F3 optimum values.

## Gates, in dependency order

1. **Exact reduced definitions.** Encode A_a, B_a(k), dB_a(k),
   L_h(a), C_a, D_a, H_beta, H_s, E_k, J_k from original active equations.
   Verify odd and even Q blocks separately. Exclude zero denominators.
2. **A rational polynomial lemma.** Substitute beta^k=uK, s^k=uW,
   tau^k=uT, H_beta=1/2+uU, H_s=1/2+uV, and v_a=a^M.
   Prove an exact identity isolating u^2*T times the dominant expression.
   Preserve the terms involving K and v_a as an explicit finite remainder;
   do not treat them as definitionally zero.
3. **Finite-power bounds.** Prove L_h(tau)>=(7/10)*tau for
   0<tau<=3/20, h>=2; a^M<=u^2 when a<=tau and M=2h or 2h+1;
   C_a-a/tau=O(Mu). Bound U,V,W,T and the K term with all source
   quantifiers.
4. **Geometric suppression.** Establish a uniform rho<1
   (for example 99/100) and a constant C_geom for which the complete
   normalized non-core remainder <=C_geom*rho^M.
5. **Removable x=0 singularity.** Prove that
   f(x)=(1+2alpha*x)^(-1/(2*x)+sigma) for x>0 extends three-times
   continuously differentiably at 0 with f(0)=exp(-alpha), and that
   the third derivative has a uniform bound on the compact parameter box.
6. **Coefficient identities.** Derive Lambda_p and Xi_p from the
   Taylor coefficients of the exact dominant core. Do not import A118
   coefficient correctness as an axiom.
7. **Uniform theorem.** Combine the remainder bounds, parity split,
   finite r set and geometric domination by 1/M^3. Give explicit
   dependence of the final C and M0 on the frozen parameter rectangle.
8. **A119 corollary.** Formally connect critical Lambda=0,
   exact interval-positivity Xi>1 and the new uniform bound to eventual
   J>0. Prove contact selection and tail-cell exclusion independently.
   Never replace F3 primal-dual feasibility with J positivity.

## Acceptance controls

- Fresh compilation with the repository's pinned toolchain.
- No sorry, admit, hidden axiom, unsafe shortcuts, or unverified opaque trusted proof.
- Inspect print axioms for new critical declarations; describe any native-computation trust dependencies.
- Dedicated small semantic and algebraic negative controls to catch a reversed
  comparator, missing 1/tau factor or a dropped negative remainder.
- Record failed proof attempts and exact CI run SHA/results before using the
  phrase "Lean-verified".

## Current evidence

The exact identity is supported by the SymPy script
[a115_a119_uniform_remainder_graded_audit_20261110.py](../../audits/a115_a119_uniform_remainder_graded_audit_20261110.py),
the analytic bounds are documented in the research note,
and source-window endpoint/tail rational checks are supported by
[a119_independent_tail_and_entry_20261110.py](../../audits/a119_independent_tail_and_entry_20261110.py).

**Not performed:** a Lean formalization or CI for the new theorem,
a global LP optimum proof, an originality certification.
