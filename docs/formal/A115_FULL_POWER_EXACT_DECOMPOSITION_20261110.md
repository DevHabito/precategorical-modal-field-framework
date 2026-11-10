# Exact full-length-power correction in the A115 adjacent factor

**Recorded:** 2026-11-10. **Scope:** original reduced C2(k) active-band cofactor.
**Status:** independently checked by SymPy using polynomial arithmetic; **new Lean proof submitted, not assumed passed**.

Let x=1/M, q=k/M, u=tau^h, K=beta^k/u, W=s^k/u, T=tau^k/u. The full cofactor E is constructed with A_tau=(1+vt)/2, vb=beta^M, vs=s^M, vt=tau^M in every B_a and Delta B_a, and H_beta=1/2+uU, H_s=1/2+uV. The auxiliary reduced cofactor E0 sets vb=vs=vt=0 **only as an algebraic comparison**, not as a finite-M assumption.

Define J_full=E(k)-tau^(-1)E(k+1), and J_aux=E0(k)-tau^(-1)E0(k+1). Exact polynomial cancellation gives

    2*tau*(J_full-J_aux)=C0+u*C1+u^2*C2,

where

    C0=x*(tau-1)*vt*(vs-vb),

and the full formulas for C1 and C2, preserving all vb,vs,vt, vb*vt, vs*vt and K terms, are defined in [A115FinitePowerDecomposition.lean](../../formal/lean/PrecategoryFormal/A115FinitePowerDecomposition.lean).

Independent symbolic re-expansion of both original cofactors yields an identically zero difference. The standalone [audit program](../../audits/a115_full_power_tail_symbolic_20261110.py) reproduces this check and includes three negative controls (dropping C0, C1 or C2 must fail), plus zero-full-power and u=0 specializations. An earlier independent Fraction regression checks the finite originals at six integer/parity configurations.

**Important distinction:** the three polynomials depend on q,x,base nodes and U,V. They are not constant coefficients of a full-M asymptotic series, and their magnitudes remain to be bounded. The decomposition proves an *exact algebraic identity*, not a numerical M threshold or a uniform O(M^-3) theorem.

The algebra shows that no u^3 full-power **difference** survives: the cubic-u channel in the auxiliary cofactors was handled separately by A115CofactorReducedCore. This is useful for the final suppression estimate but is not a proof of geometric decay on its own.

**Next gates:** (1) replay exact_full_power_correction with the pinned Lean checker; (2) prove a compact uniform bound on all Cj using tau>0, K,W,T and the central response bounds; (3) formalize the analytic Taylor remainder for both h and k contact powers; (4) derive Lambda and Xi by differentiating the actual A115 core; (5) assemble a uniform error constant. The global F2/F3 optimizer and novelty remain open.
