# Revalidating the A118 collision Taylor bound with Mathlib's log remainder

**Recorded:** 10 November 2026. **Branch:** research/a115-a119-uniform-remainder-20261110.

The prior hand-derived A118 estimate used the tight alternating cubic logarithm remainder \(z^4/4\). A standard Mathlib theorem \`Real.abs_log_sub_add_sum_range_le\`, applied to \(-z\) at order \(n=3\), provides the **slightly weaker but directly reusable** real inequality

\[
|\log(1+z)-(z-z^2/2+z^3/3)|\le z^4/(1-z)
\]

for \(0\le z<1\). The repository has submitted this precise Lean statement in [A118LogTaylorRemainder.lean](../../formal/lean/PrecategoryFormal/A118LogTaylorRemainder.lean). Do not call that module kernel-verified until its specific checker job passes.

## Exact uniform recalculation

For \(x=1/M\in(0,10^{-3}]\), \(8\le\alpha\le45\), and \(0\le b\le37/2\), set \(z=2\alpha x\le9/100\) and

\[
L=(-1/(2x)+b)\log(1+2\alpha x).
\]

With \(A=\alpha^2+2b\alpha\), \(B=-4\alpha^3/3-2b\alpha^2\), and \(v=L+\alpha\), the new log bound yields

\[
|L+\alpha-Ax-Bx^2|
\le\left(\frac{8\alpha^4}{1-z}+\frac83 b\alpha^3\right)x^3
<41\,000\,000x^3.
\]

Here \(|A|\le3690\), \(|B|\le196425\), so \(|v|<4000x\le4\), \(|v-Ax|<238000x^2\), \(|v+Ax|<7690x\). With the Mathlib-backed inequality \(e^4<55\), the standard exponential third-order Taylor remainder gives

\[
|e^v-(1+v+v^2/2)|<
\frac{55(4000)^3}{6}x^3.
\]

The quadratic difference is at most \(\frac{238000\cdot7690}{2}x^3\). Adding that term and the 41 million exponent remainder yields

\[
|e^v-(1+Ax+(B+A^2/2)x^2)|<590\,000\,000\,000x^3.
\]

Finally, \(e^{-\alpha}\le1\) and \(x\le10^{-3}\) yield, uniformly over **both** the h- and k-collision shifts,

\[
\boxed{|f_{\alpha,b}(x)-e^{-\alpha}(1+Ax)|
<600\,000\,000x^2.}
\]

The source bracket's exact coefficients of the two collision powers are bounded by \(46H\) and 768 for \(H=8^{18}\). The exact comparison

\[
(46H+768)\cdot600000000<500000000000H
\]

shows that **the same aggregate bracket and final cubic constant** \(C=10^{11}H^2\) from [the original source proof](A115_A118_EXPLICIT_UNIFORM_CUBIC_REMAINDER_20261110.md) remain sufficient. No sign threshold at M=1000 follows.

All decisive constant inequalities, including the rational \(1/(1-z)\) bound, are checked exactly in [a118_mathlib_compatible_taylor_gates_20261110.py](../../audits/a118_mathlib_compatible_taylor_gates_20261110.py). They are **not** samples of real parameters.

## Open formal obligations

The stated log remainder and the inequality \(\exp 4<55\) must pass their individual Lean kernel checks. Even then, the composed real collision-power Taylor bound and the final source-to-\(O(M^{-3})\) theorem still require their own Lean proofs. The independent source-jet coefficient identity is separately kernel-checked. Nothing here claims F2/F3 optimality, a new mathematical law, historical novelty, or physical pregeometry.
