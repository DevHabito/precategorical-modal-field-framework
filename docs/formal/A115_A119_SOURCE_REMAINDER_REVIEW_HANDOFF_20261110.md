# A115–A119 source-to-remainder research checkpoint

**Date:** 2026-11-10. **Branch:** research/a115-a119-uniform-remainder-20261110.
**Scope:** the original finite cofactor of the two-active-band reduced family C2(k); no claim of unrestricted F2/F3 primal-dual optimality.

## Result and exact hypotheses

The analytic derivation now gives an explicit uniform remainder estimate for beta=1/8, delta=1/1875, s in [129/1000,133/1000], alpha in [8,45], integer M>=1000, its actual even/odd parity, integer deficit r in [4,19], h=floor(M/2), k=h-r+1 and tau=s(1+2alpha/M). With the full original A115 adjacent cofactor J=E_k-tau^(-1)*E_(k+1):

\[
\left|J/\tau^{h+k}-\Lambda_p/M-\Xi_p/M^2\right|
<10^{11}(8^{18})^2/M^3.
\]

The large constant is uniform and analytically justified but **not yet certified in a single Lean theorem**. Its size does not certify finite-M sign at M=1000. This result is specific to the reduced-family expression; no contact optimality or full LP feasibility follows.

## Independent mathematical layers and evidence

**Exact original-vs-auxiliary algebra.** The new full-length-power identity contains all beta^M, s^M, tau^M and mixed channels, expressed as C0+u*C1+u^2*C2. The Lean module A115FinitePowerDecomposition passed [CI 42919833294](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42919833294), 50/50 SUCCESS. The independent symbolic code also passed, with negative controls for dropping any one of C0/C1/C2.

**Original-to-leading-core exponential suppression.** Separate exact-polynomial terms and independently derived central response estimates yield a uniform geometric envelope 750*(8^18)^2*(99/100)^M. The inequalities are documented in [A115_A118_AGGREGATE_GEOMETRIC_SUPPRESSION_20261110.md](A115_A118_AGGREGATE_GEOMETRIC_SUPPRESSION_20261110.md). Constant arithmetic passed exact Python CI [42921059293](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42921059293); this geometric inequality is not itself a Lean theorem.

**Exact x factor and leading phase.** The dominant core is exactly x times a rational bracket, with x=1/M, and the x=0 bracket reproduces the A117 Lambda expression. A115CollisionCoreFactor passed [Lean CI 42922256460](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42922256460), 51/51 SUCCESS. The previous two failed builds (42921508312 reserved identifier; 42921821575 linter warning) are preserved, with corrections that did not modify the mathematics.

**Source-derived Xi and cubic Taylor bound.** The bracket is linear in its two collision powers. An independent SymPy audit derives the A117 Lambda and A118 Xi as its first two coefficients in both parities; the exact rational jet residual has numerator divisible by x^2. An exact rational monomial envelope across 53 even and 95 odd terms yields less than 10^10*x^2. The log/exp Taylor estimate covers the full k-shift range b<=18.5, giving less than 558,000,000*x^2 for each power's first-order approximation. This is recorded in [A115_A118_SOURCE_COEFFICIENT_AND_TAYLOR_20261110.md](A115_A118_SOURCE_COEFFICIENT_AND_TAYLOR_20261110.md) and [A115_A118_EXPLICIT_UNIFORM_CUBIC_REMAINDER_20261110.md](A115_A118_EXPLICIT_UNIFORM_CUBIC_REMAINDER_20261110.md). The symbolic-source-jet CI [42923563415](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42923563415) approved the monomial certificate and coefficient tests.

**Conversion to inverse cubic.** The elementary binomial bound (99/100)^M <= 12*99^3/M^3 for integers M>=6 absorbs the geometric correction. Exact Fraction arithmetic verifies that all explicit constants fit below 10^11*(8^18)^2.

## Remaining scientific gates

1. Formalize the real exponential/log Taylor remainders, first derivatives and the source-to-A118 Xi coefficient identity in Lean.
2. Formalize the central response geometric inequalities and the monomial-bound transfer to a real-variable core.
3. Assemble the complete source-to-O(M^-3) estimate with one quantifier-safe Lean theorem, matching all source normalization and parity hypotheses.
4. Prove the A117 high-deficit contact classification and the relevant primal/dual feasibility and global LP questions separately. No global F3 optimum is implied.
5. Complete theorem-level prior-art comparison and external review before any originality or physical claim.

The main branch was not changed. The English notes preserve successful and failed tests, original source definitions, and the distinction between exact algebra, analytic estimates, and kernel-checked theorems.
