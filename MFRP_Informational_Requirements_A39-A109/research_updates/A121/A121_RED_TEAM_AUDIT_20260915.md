# A121 — red-team audit

**Date:** 2026-09-15  
**Verdict:** **PASS WITH SCOPE**

A121 is audited as a fixed-interior, fixed-offset consequence of A120. The audit does not treat the phase-staircase picture as a global maximizer theorem.

## Attacks performed

1. **Two-variable illusion attack.**  
   A120 has \(\Psi_{p,j}(\rho)=P_ps^{j+\rho}-Q_p\). The proof rewrites the family through the single coordinate \(x=j+\rho\); no independent phase variable is invented.

2. **Wrong sign-orientation attack.**  
   Since \(0<s<1\), \(x\mapsto s^x\) is strictly decreasing. Therefore the limiting sign goes from positive to negative as \(j+\rho\) increases. The reverse orientation would contradict the derivative.

3. **Multiple-reversal attack.**  
   The limiting family has one threshold \(\xi_p\). For the finite factors, eventual positivity of every fixed adjacent
   \[
   J^{(j)}=E_{b+j}-\tau^{-1}E_{b+j+1}
   \]
   prevents a later \(-\to+\) reversal inside any fixed finite offset window.

4. **Resonance attack.**  
   At \(j+\rho=\xi_p\), the A120 leading term vanishes. A121 explicitly leaves that marginal finite factor unresolved instead of assigning a sign by continuity.

5. **Global-maximizer overreach attack.**  
   The local peak theorem uses only the two adjacent factors around the transition. It is not promoted to a global compressed maximum because no all-contact target-deformed tail theorem has been proved.

6. **Uniform-threshold attack.**  
   Exact arithmetic gives
   \[
   M=1200,\quad s=129/1000,\quad \tau=3/20,\quad j=3
   \]
   with \(J^{(3)}<0\). Thus the eventual nesting theorem is not rewritten as a small or universal finite bound.

7. **Parity attack.**  
   The analytic theorem retains the A120 parity constants \(a_p,\sigma_p\). Exact finite sentinels are included for both even and odd \(M\).

8. **Frozen-regression attack.**  
   The exact audit rechecks 21 \(\tau=1/2\) controls from the A113 window. All preserve positive \(E_b\), negative \(E_{b+3}\), and one-variation across \(j=0,1,2,3\).

9. **Finite-sentinel overreach attack.**  
   The eight two-site finite controls are regression/hardening only. Infinite alternation is inherited analytically from A120's irrationality and density argument, not inferred from those eight examples.

## Result

No contradiction was found in:

- the one-coordinate phase front;
- the threshold formula;
- eventual adjacent nesting at each fixed offset;
- eventual one-variation in every fixed finite offset window;
- the nonresonant two-site local-peak rule.

## Scope preserved

A121 makes no:

- global target-deformed compressed-maximizer claim;
- target-deformed A114 claim;
- collision-layer remote-factor claim;
- novelty/priority claim;
- physical or ontological claim.
