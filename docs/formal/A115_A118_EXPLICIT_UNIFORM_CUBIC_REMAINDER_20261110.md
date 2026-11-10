# A115–A118 explicit uniform cubic remainder — independent polynomial certificate

**Recorded:** 2026-11-10. The object is the original reduced C2(k) adjacent cofactor, not an unrestricted F2/F3 optimal objective.
**Evidence tier:** analytic proof with an exact symbolic/rational monomial audit; the final inequality is NOT yet a Lean kernel theorem.

Assumptions: beta=1/8, delta=1/1875, source s in [129/1000,133/1000], collision alpha in [8,45], integer M>=1000, true parity sigma in {0,1/2}, contact deficit r in {4,...,19}, h=floor(M/2), k=h-r+1, tau=s(1+2alpha/M). The original A115 E_k includes every full M-th power. Put J=E_k-tau^(-1)*E_(k+1), H=8^18, and use the published Lambda_p and Xi_p of A117/A118.

## Result and proof layers

The following is a **uniform analytic estimate with an explicit, very crude constant**:

\[
\left|\frac{J}{\tau^{h+k}}-\frac{\Lambda_p}{M}-\frac{\Xi_p}{M^2}\right|
<\frac{10^{11}(8^{18})^2}{M^3}.
\]

Layer 1: the exact finite-power identity, K-channel correction and cubic-u correction have individually successful Lean algebra checks; the aggregate geometric bound (not yet kernel-checked as an inequality) gives

\[
\left|\frac{J}{u\tau^k}-x\,\mathcal B(x)\right|
<750H^2(99/100)^M,\qquad x=1/M.
\]

Layer 2: the exact source-derived bracket is linear in the h- and k-collision powers and has an exact factor x. Its linear-jet replacement \(\mathcal B_{\mathrm{jet}}\) has value \(\Lambda_p\) and derivative \(\Xi_p\) at x=0 in **both** parities; these identities were independently checked with exact SymPy in the source-to-A118 audit.

For the rational jet, the numerator of

\[
s^2(1+2\alpha x)^2
(\mathcal B_{\mathrm{jet}}(x)-\Lambda_p-\Xi_p x)
\]

is a polynomial with every x exponent at least 2. The new independent program [a115_uniform_jet_polynomial_bound_20261110.py](../../audits/a115_uniform_jet_polynomial_bound_20261110.py) constructs that polynomial from the source expression and sums **absolute rational monomial bounds** over x<=1/1000, s,beta,delta,e<=1, alpha<=45, z=s^(1-r)<=H and r<=19. The denominator is at least (129/1000)^2. The exact sums give a bound **strictly below \(10^{10}x^2\)** in both parities, with 53 even and 95 odd monomial groups. No random sampling is used.

Layer 3: the previously documented uniform Taylor bound for both exponents b=sigma and b=sigma+r-1<=18.5 gives

\[
|f_b(x)-e^{-\alpha}(1+\eta_b x)|<558000000x^2.
\]

The coefficients of the two powers in the exact bracket have magnitudes <46H and <768. Therefore the replacement adds <500000000000 H x^2, and the complete bracket has error <510000000000 H x^2.

Layer 4: the elementary binomial theorem proves for M>=6 that
\[
(99/100)^M\le 12\cdot99^3/M^3,
\]
because \((1+1/99)^M\ge {M\choose3}/99^3\) and \({M\choose3}\ge M^3/12\).
Combining the analytic core bound with the geometric error gives a coefficient
\(510000000000H+750H^2\cdot12\cdot99^3\), which the independent Fraction audit verifies is **strictly less** than \(10^{11}H^2\).

## What this does not establish

The constant is enormous and gives no useful sign threshold near M=1000. The derivation proves an **analytic** source-to-coefficient remainder statement conditional on the source-locked assumptions, not a kernel-checked final Lean theorem. The central response inequalities, logarithmic and exponential Taylor inequalities, and complete analytic bound still require formal Lean replay. The published coefficient identification has an independent symbolic source audit, but a final Lean derivative/jet theorem is still open.

It is not a feasibility/dual certificate for unrestricted F2/F3, not a proof that r<=19 exhausts all critical contacts, not a physical law, and not a claim of mathematical novelty. Independent mathematical refereeing remains essential.


## Exact CI audit read-back

The two-job symbolic and arithmetic workflow [42923563415](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42923563415) individually approved the uniform source-jet monomial certificate. The symbolic job printed 53 even-parity monomials with rational ceiling 8,120,225,541 and 95 odd-parity monomials with rational ceiling 4,569,365,712; both are strictly below the selected 10,000,000,000 bound. The job also passed the exact comparison of the combined constant with 100,000,000,000*(8^18)^2. These are rational polynomial arithmetic checks, not claims that the analytic log/exp theorems were replayed in Lean.
