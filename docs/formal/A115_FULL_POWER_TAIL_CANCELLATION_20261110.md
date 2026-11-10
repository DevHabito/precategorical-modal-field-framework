# A115 exact full-length-power cancellation gate

**Recorded:** 10 November 2026.
**Status:** independent symbolic test PASS; the corresponding Lean 4 module is submitted and pending verification at this checkpoint.
**Scope:** the reduced adjacent cofactor C2(k), not F3 global optimality.

In the source-locked A115 contract keep the *full* M-th powers vb=beta^M, vs=s^M and vt=tau^M instead of setting them to zero. The definitions of A_tau, B_a(k) and Delta B_a(k) in `A115FullPowerTail.fullCofactor` include all three powers. It also retains beta^k=uK, s^k=uW, tau^k=uT and the response factors H_beta=1/2+uU, H_s=1/2+uV.

The independent SymPy polynomial comparison verified the following **exact** scaled identity at u=0:

```
2*(tau*E_k - E_(k+1)) = x*(tau-1)*vt*(vs-vb)
```

with x=1/M, q=k/M and the correct k-to-k+1 power shifts. Consequently no constant or *individual linear* vb,vs,vt term survives at u=0. A mixed quadratic finite-power channel remains, and it is explicitly retained. This is an algebraic specialization used to identify low-order cancellations, **not a claim that tau^h is ever zero** at finite M.

The Lean module `A115FullPowerTail.lean` states this fact as `zero_u_full_length_residual` and separately proves that setting all v variables to zero recovers exactly the prior reduced cofactor, not a different objective.

The original question — a uniform bound on the **actual** finite-M comparison after normalization — remains open. The next nontrivial step is a full algebraic decomposition involving u*vb, u*vs, u*vt, u^2*v terms, and products vb*vt and vs*vt. Those residual terms must be bounded uniformly, with a positive central denominator, geometric beta-channel suppression, and an analytic Taylor remainder for the collision power. No physical or historical novelty follows from this polynomial identity.

The prior exact reduced cofactor lemma also remains pending CI on this branch; neither Lean module is labeled PASS before the individual `leanchecker` job reports success.
