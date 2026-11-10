# A115–A118: explicit uniform Taylor bound for the collision power

**Research date:** 2026-11-10. **Branch:** `research/a115-a119-uniform-remainder-20261110`.  
**Status:** detailed analytic inequality with independently checked rational constant arithmetic; **not yet formalized in Lean 4**.  
**Scope:** one exponential collision-power factor in the reduced C2(k) expansion. Not a finite-M cofactor bound, full F3 theorem, or historical novelty claim.

## The obstacle

In the collision scaling tau=s(1+2 alpha/M), with x=1/M and h=M/2−sigma, the ratio appearing in the exact A115 cofactor has the form

[
f_{\alpha,\sigma}(x)
=(1+2\alpha x)^{-1/(2x)+\sigma}
\quad (x>0),
\qquad f_{\alpha,\sigma}(0)=e^{-\alpha}.
]

A118 needs its first two Taylor coefficients and a **single error bound**, uniform in the fixed rectangular parameter set

[
8\le\alpha\le45,\qquad
\sigma\in\{0,1/2\},\qquad
0\le x\le 1/1000.
]

The factor s drops out of this ratio after tau/s=1+2 alpha x.

## Explicit statement

Define

[
A=\alpha^2+2\sigma\alpha,\qquad
B=-\frac43\alpha^3-2\sigma\alpha^2.
]

Then, on the entire displayed set,

[
\boxed{
\left|
f_{\alpha,\sigma}(x)
-e^{-\alpha}
\left(1+Ax+\left[B+\frac{A^2}{2}\right]x^2\right)
\right|\le 50{,}000{,}000{,}000\,x^3.
}
]

The constant is intentionally crude. It is uniform, independent of s, alpha, sigma and M. This exact upper bound is useful for proof closure, not a claim about a practical finite-M threshold.

## Proof, with all numerical bounds exposed

For 0<x<=1/1000, put z=2 alpha x. Then 0<z<=9/100. The alternating logarithm series for 0<=z<1 gives, with genuine analytic remainder bounds,

[
|\log(1+z)-(z-z^2/2+z^3/3)|\le z^4/4,
]
[
|\log(1+z)-(z-z^2/2)|\le z^3/3.
]

Define the exponent L(x)=(-1/(2x)+sigma)log(1+2alpha x). Substitution yields

[
L(x)=-\alpha+Ax+Bx^2+R_L(x),
]

where

[
|R_L(x)|
\le\left(2\alpha^4+\frac83\sigma\alpha^3\right)x^3
\le 8{,}322{,}750\,x^3.
]

Both constants in the final inequality are exact rational/integer bounds:
2(45)^4+(4/3)(45)^3=8,322,750.

Let v=L+alpha. The preceding bounds give

[
|A|\le2070,\quad |B|\le123525,\quad
|v|\le2202 x<3,
]
[
|v-Ax|\le131848x^2,\qquad
|v+Ax|\le4272x.
]

For the exponential Taylor remainder, e^3<27 and

[
|e^v-(1+v+v^2/2)|
\le e^{|v|}|v|^3/6
<48{,}046{,}798{,}836\,x^3.
]

Furthermore,

[
|v-Ax-Bx^2|\le8{,}322{,}750\,x^3,
]
[
\frac12|v^2-A^2x^2|
=\frac12|v-Ax|\,|v+Ax|
\le281{,}627{,}328\,x^3.
]

Adding these exact upper bounds gives 48,336,748,914 x^3, strictly less than 50,000,000,000 x^3. Multiply by e^(-alpha)<=1. At x=0 both sides are zero by definition, so the inequality holds there too.

The only analytic inputs not yet replayed in Lean are the standard alternating-logarithm remainder inequalities and the exponential Taylor remainder. All subsequent comparisons are elementary exact rational arithmetic.

## Independent falsification controls

On the current session's high-precision mpmath evaluations, the absolute errors were below the stated bound at alpha=8,sigma=0,x=1/1000 and alpha=45,sigma=1/2,x=1/1000, as well as two other probes. These are finite cross-checks only: they do not constitute the proof. The bound itself follows from the analytic inequalities above, not sample points.

## What this proves and what it does not

This gives an explicit **uniform third-order approximation of the single collision power** f. The coefficients A and B are the ingredients entering the A118 parity-resolved corrections eta_h and the second-order expansion. The sign and magnitude of the full J cofactor still depend on the other power channels and their nonzero full-length terms.

Remaining formal obligations: implement this lemma over real parameters in Lean, obtain the corresponding expansion for (s/tau)^k (replace sigma by sigma+r−1), combine with exact cofactor channel algebra and central-Q bounds, and produce one explicit or abstract uniform constant C for the complete normalized N_M.

Do not call the full uniform O(M^-3) theorem Lean-proved until each dependency and final assembly has been kernel checked.
