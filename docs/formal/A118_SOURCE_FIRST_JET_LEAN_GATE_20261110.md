# A118 source-first-jet algebraic identity — independent Lean gate

**Recorded:** 10 November 2026. **Branch:** `research/a115-a119-uniform-remainder-20261110`.
**Status:** the independent full symbolic equality has been executed with SymPy and returned EXACT ZERO. The corresponding four Lean statements are **submitted for CI, not presumed accepted**.

The source-derived A115 collision bracket is an exact rational expression `collisionBracket`. Its parity-dependent parameters include the central source normalizer a, the shift sigma, source s, collision alpha, contact deficit r, and independent contact factor z=s^(1-r). In the expansions, the central target a_tau differs from a by exactly 2*sigma*alpha*s*x; the two collision powers have first-order slopes e*(alpha^2+2*sigma*alpha) and e*(alpha^2+2*alpha*(sigma+r-1)).

The [new Lean module](../../formal/lean/PrecategoryFormal/A118SourceFirstJet.lean) defines `sourceSlope` by the first-order product/quotient rules at x=0 and independently defines `xiBySourceZ` by the original A118 expression with its s^(2-r) contact factor still represented by s*z. The theorem `source_slope_equals_published_xi` is a **universal real algebraic identity** without parity-specific case fitting.

It separately proves that the only difference between `xiBySourceZ` and the repository's existing definition of `xiPublished` is a factor of `s*z-(s^(r-2))⁻¹`. Thus `source_slope_matches_a118` has the explicit geometric contact hypothesis `s*z=(s^(r-2))⁻¹`, together with s!=0. No other assumptions are inserted.

**Remaining formal step:** prove that `sourceSlope` is actually the derivative at x=0 of the original rational bracket with the two collision powers replaced by their correct first-order approximations. The present Lean definitions do not make that derivative claim automatically true. A separate analytic proof is needed for the true exponential/log collision factors and all uniform remainder inequalities. Passing these algebra lemmas would strengthen the source-to-A118 coefficient identification, not finish the O(M^-3) Lean theorem.

The full C2(k) finite cofactor, its power channels, the A119 35 real sign boxes, contact coverage and full F3 optimality are separate logical steps. No novelty or physics claim is made here.
