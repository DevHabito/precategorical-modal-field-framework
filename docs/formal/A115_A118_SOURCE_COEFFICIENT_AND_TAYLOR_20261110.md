# Source-derived A117/A118 coefficients and enlarged collision-power remainder

**Date:** 2026-11-10. **Working branch:** research/a115-a119-uniform-remainder-20261110.
**Status:** independent exact symbolic coefficient audit and analytic uniform Taylor derivation. The explicit source-to-coefficient calculation has **not yet been kernel-replayed end-to-end in Lean**. No F2/F3 global optimality or novelty is asserted.

## The source-to-coefficient gate

The exact dominant A115 normalized core satisfies \(\mathcal J(x)=x\mathcal B(x)\) under \(\tau=s(1+2\alpha x)\), \(q=1/2-(\sigma+r-1)x\). The bracket is defined in [A115CollisionCoreFactor.lean](../../formal/lean/PrecategoryFormal/A115CollisionCoreFactor.lean), where its exact factorization and leading A117 coefficient are submitted for Lean proof.

Put \(e=e^{-\alpha}\), \(z=s^{1-r}\), \(b=\sigma+r-1\), \(\eta_h=\alpha^2+2\sigma\alpha\), and \(\eta_k=\alpha^2+2b\alpha\). Replace the two collision-power inputs **temporarily** by their linear jets \(f_h=e(1+\eta_h x)\) and \(f_k=e(1+\eta_k x)\). Expanding the resulting *rational* bracket without fitting any parameter gives

\[
\mathcal B_{\rm jet}(0)=\Lambda_p(s,\alpha,r)
\quad\text{and}\quad
\mathcal B_{\rm jet}'(0)=\Xi_p(s,\alpha,r).
\]

The \(\Xi_p\) on the right is exactly the published A118 second-order coefficient with its original \(q=e\), \(B_1,S_1,G_2\) terms and the identity \(s z=s^{2-r}\); it is **not** the A119 critical-substitution formula assumed as a starting point. Both equalities passed independent symbolic reduction for even and odd parity in [a115_source_to_a118_jet_audit_20261110.py](../../audits/a115_source_to_a118_jet_audit_20261110.py).

The rational numerator of \(\mathcal B_{\rm jet}(x)-\Lambda_p-\Xi_p x\) is **divisible by \(x^2\)** in both parities, and its denominator is a product of powers of \(s\) and \(1+2\alpha x\), bounded away from zero on the frozen compact box. Thus it has a **uniform** \(O(x^2)\) rational remainder. This is more direct than inferring the A118 coefficients from an already assumed sign of \(\Xi\).

## An explicit bound for both collision powers

The original h-power and the k-power are

\[
f_{\alpha,b}(x)=(1+2\alpha x)^{-1/(2x)+b},
\qquad
0<x\le10^{-3},
\]

with the continuous value \(f_{\alpha,b}(0)=e^{-\alpha}\). The h case has \(b=\sigma\in\{0,1/2\}\); the k case has \(b=\sigma+r-1\in[3,37/2]\). Therefore **one common bound must cover \(0\le b\le37/2\)**. A Taylor constant proved only for the h case must not be copied into the k case.

Set

\[
A=\alpha^2+2b\alpha,\qquad
B=-\frac43\alpha^3-2b\alpha^2.
\]

Using the alternating logarithm remainder for \(z=2\alpha x\in[0,9/100]\),

\[
\left|
(-1/(2x)+b)\log(1+2\alpha x)+
\alpha-Ax-Bx^2
\right|
\le
\left(2\alpha^4+\frac83 b\alpha^3\right)x^3
\le 12\,696\,750x^3.
\]

Thus \(|A|\le3690\), \(|B|\le196425\), and with \(v=\log f+\alpha\) one gets \(|v|<3900x<4\), \(|v-Ax|<209122x^2\), \(|v+Ax|<7590x\). The standard exponential Taylor inequality and the exact bound \(e^4<55\) give

\[
\begin{aligned}
\left|f_{\alpha,b}(x)-
e^{-\alpha}\left[1+Ax+
\left(B+\frac12 A^2\right)x^2\right]\right|
&\le (543\,757\,500\,000+793\,617\,990+
12\,696\,750)x^3\\
&=544\,563\,814\,740x^3\\
&<550\,000\,000\,000x^3.
\end{aligned}
\]

In particular, because \(|B+A^2/2|\le7\,004\,475\),

\[
\boxed{\left|f_{\alpha,b}(x)-e^{-\alpha}(1+Ax)\right|
<558\,000\,000x^2.}
\]

The inequality includes \(x=0\) by the defined continuous extension. All numerical constants, including a **rational series upper bound** for \(e^4<55\), are independently checked by [a118_collision_power_taylor_gates_20261110.py](../../audits/a118_collision_power_taylor_gates_20261110.py); it does not substitute for the underlying analytic Taylor remainder theorems.

## Consequence for the actual reduced factor

The earlier exact polynomial identities and the [aggregate geometric error note](A115_A118_AGGREGATE_GEOMETRIC_SUPPRESSION_20261110.md) give

\[
\left|\frac{J_{\rm full}}{u\tau^k}-\mathcal J(x)\right|
<750(8^{18})^2(99/100)^M.
\]

The expression \(\mathcal B(x)\) is rational in \(x,s,\alpha\) and **linear** in the two power functions \(f_h(x),f_k(x)\), whose linear jets have the uniform \(x^2\) bound just established. Its remaining rational coefficients are uniformly bounded on the compact domain \(s\ge129/1000\), \(\tau\ge129/1000\) and \(0\le x\le1/1000\). Consequently

\[
|\mathcal B(x)-\Lambda_p-\Xi_p x|\le C_{\rm bracket}x^2
\]

for **some finite constant** \(C_{\rm bracket}\) independent of \(s,\alpha,r,\sigma,M\). The finite rational polynomial numerator is explicitly divisible by \(x^2\) and the denominator stays separated from zero. Multiplying by \(x=1/M\) gives the cubic remainder for the dominant core. Because \(\sup_{M\ge1000} M^3(99/100)^M<\infty\), combining with the geometric error yields the desired **analytic existence** of a uniform \(C\) for the reduced original finite cofactor:

\[
\left|\frac{J_{M,k}}{\tau^{h+k}}
-\frac{\Lambda_p}{M}-\frac{\Xi_p}{M^2}\right|
\le \frac{C}{M^3}.
\]

**This is an analytic proof assembly, not an end-to-end Lean theorem.** The coefficient identifications are independently checked in SymPy, and some exact source identities have independent Lean certificates. The precise \(C\), formal source-to-jet lemma, rational coefficient bounds, and all analytic uniform estimates have **not** yet been assembled into a kernel-checked final result. Independent human mathematical review is still required before claiming a publication-ready A118 theorem.

This proof applies to the frozen source/alpha window, parity and fixed deficit r=4,...,19 with k=h-r+1 and M>=1000. It does not assert that the chosen sparse candidate is F2/F3 feasible or globally optimal, does not prove all critical contacts fall within this range, and does not establish novelty or physical consequences.
