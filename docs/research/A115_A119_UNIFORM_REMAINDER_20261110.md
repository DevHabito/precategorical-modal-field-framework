# A115–A119: uniform collision remainder for the **reduced** comparison factor

**Date:** 2026-11-10  
**Base:** formal/a115-a122-critical-audit-20261106, original head f5294a1c3ce52e7dd03c7927e6a1c35ca1dba71d.  
**Status:** analytic research proof with an independently executed exact symbolic cancellation checker. NOT Lean certified, externally refereed, or certified novel.  
**Scope:** the A115 two-active-band family C2(k). No unrestricted F2 or F3 optimum is asserted.

## Precise question

A118 presents a pointwise expansion N_M=Lambda_p/M+Xi_p/M^2+o(M^-2). A119 uses a rational positivity certificate for Xi on Lambda=0. A step that ought to be explicit before a paper submission is a **uniform** bound on the error made by dropping the beta channels and finite-power terms.

We reconstruct this step from A115's actual factor, without assuming that the reduced candidate is feasible in the full LP.

## Proposition (uniform remainder in the frozen parameter rectangle)

Take beta=1/8, delta=1/1875 and

- 129/1000 <= s <= 133/1000;
- 8 <= alpha <= 45;
- parity p in {even,odd}, sigma_p=0 or 1/2;
- integer contact deficit 4 <= r <= 19;
- integer M>=1000 of the chosen parity.

Put h=M/2-sigma_p, k=h-r+1, tau=s(1+2alpha/M), u=tau^h. Form the original A115 compressed cofactor E_(M,k) and J_(M,k)=E_(M,k)-tau^-1 E_(M,k+1), using the parity-specific target tolerance epsilon=delta*a_tau*u. These expressions are defined here at the explicit k; when k agrees with the ceiling contact this is the original contact comparison.

**Claim:** There exists a constant C<infinity depending only on the displayed fixed rectangle such that

\[
\left|
\frac{J_{M,k}}{\tau^{h+k}}
-\frac{\Lambda_p(s,\alpha,r)}{M}
-\frac{\Xi_p(s,\alpha,r)}{M^2}
\right|\le\frac{C}{M^3}.
\]

Lambda_p and Xi_p are the *explicit reduced-factor coefficients* written in A117 and A118, not F3 objective values. The inequality has no numerical minimal threshold: C is not computed or optimized.

## Definitions used in the derivation

Let, for a in {beta,s,tau},

\[
A_a=(1+a^M)/2,\quad
B_a(k)=a^k-1+(k/M)(1-a^M),\quad
dB_a(k)=(a-1)a^k+(1-a^M)/M.
\]

Set L_h(a)=a-h a^h+(h-1)a^(h+1) and a_a=1 in the even case or (1+a)/2 in the odd case. The central-Q response has coefficients

\[
C_a=L_h(a)/L_h(\tau),\qquad
D_a=a_a a^h-a_\tau u C_a.
\]

The two active band coefficients are H_beta=A_beta-D_beta+2epsilon and H_s=A_s-D_s-2epsilon. A115's exact cofactor is

\[
E_k=(A_\tau B_\beta-H_\beta B_\tau)dB_s
 +(-A_\tau dB_\beta+H_\beta dB_\tau)B_s
 +(-B_\beta dB_\tau+B_\tau dB_\beta)H_s.
\]

The arguments k on B and dB are understood. These expressions follow from the actual C2(k) active equations, not from an assumed sign theorem.

## Proof: exact central expansion and geometric suppression

The identity A_a-a_a a^h=(1-a^h)(1-a^(M-h))/2 holds for either parity. Thus H_beta=1/2+uU and H_s=1/2+uV with **exact**

\[
U=a_\tau(C_\beta+2\delta)
-a_\beta(\beta/\tau)^h+\beta^M/(2u),
\]

\[
V=a_\tau(C_s-2\delta)
-a_s(s/\tau)^h+s^M/(2u).
\]

Define U0=a_tau(beta/tau+2delta), V0=a_tau(s/tau-2delta)-a_s(s/tau)^h. The term (s/tau)^h is **not** exponentially small in the collision scaling and is deliberately retained.

For tau<=3/20 and h>=2, h*tau^(h-1)<=2*tau<=3/10. Consequently

\[
L_h(\tau)=\tau[1-h\tau^{h-1}+(h-1)\tau^h]
\ge(7/10)\tau>0.
\]

Moreover |L_h(a)-a|<=2h a^h, so for a=beta,s,

\[
|C_a-a/\tau|=O(Mu)
\]

uniformly on the rectangle. Here tau<=0.133(1+90/1000)=0.14497<0.15 and beta/tau<=125/129. Writing K=beta^k/u=beta^(1-r)(beta/tau)^h gives

\[
u\le(3/20)^{M/2-1/2},\qquad
K\le\beta^{-18}(125/129)^{M/2-1/2}.
\]

Also beta^M,s^M,tau^M are each <=u^2. Therefore, uniformly,

\[
|U-U0|+|V-V0|=O(Mu+K)=O(0.99^M).
\]

All constants are finite because r belongs to the fixed finite set; beta^(-18) makes a *very loose* small-M bound, not a practicable threshold.

## Proof: exact weighted polynomial identity

Let x=1/M, q=k/M, W=s^k/u, T=tau^k/u, K=beta^k/u and v_a=a^M.

Substitute beta^k=uK, s^k=uW, tau^k=uT, H_beta=1/2+uU and H_s=1/2+uV in the **full** J=E_k-tau^-1E_(k+1). Give u weight 1 and each v_a weight 2.

The standalone checker at [audits/a115_a119_uniform_remainder_graded_audit_20261110.py](../../audits/a115_a119_uniform_remainder_graded_audit_20261110.py) expands the complete expression and asserts exact cancellation of every term with weight below 2; its weight-2, K-independent part equals u^2*T times

\[
\begin{aligned}
\mathcal J={}&\frac{(1-s)(\tau-s)}2 W
+x(1-\tau)(U0-V0)\\
&+U0\frac{W}{T\tau}
[(s-\tau)(s-1)(q-1)+x(s^2-2s+\tau)].
\end{aligned}
\]

Every other weight-2 term includes K and every other residual has weight >=3. The full expansion has 12 monomial groups. Since v_a<=u^2, q,W,T and the central coefficients are uniformly bounded, it follows **by termwise inequalities** that

\[
\frac{J}{u\tau^k}=\mathcal J+O(Mu+K)
               =\mathcal J+O(0.99^M)
\]

uniformly. The executable test certifies the polynomial identities; the bounds on actual powers are the analytic reasoning above, not a claim about the executable's scope.

## Proof: regularity at x=0

Under tau=s(1+2alpha x) and k=h-r+1, all non-rational x dependence in the displayed J-core is through

\[
f(x)=(s/\tau)^h
=(1+2\alpha x)^{-1/(2x)+\sigma_p},
\]

with continuous/analytic extension f(0)=exp(-alpha). The logarithm power series is uniformly convergent with its derivatives for |x|<=1/1000 and alpha in [8,45], since |2alpha x|<=9/100. Thus f and the complete core are three-times continuously differentiable with uniformly bounded third derivative on the compact parameter set, including x=0.

Taylor's theorem yields

\[
\mathcal J(x)=\Lambda_p x+\Xi_p x^2+O(x^3)
\]

with uniform remainder. The **specific** first two coefficients agree algebraically with A117 and A118 for both parities; the prior independent SymPy bridge checks the coefficient identities and the A119 critical substitution. Combine with the geometric error above and the boundedness of M^3(0.99)^M to obtain the proposition.

This is a hand-auditable analytic existence proof, **not** a kernel-checked Lean formalization. Quantitative constants and external specialist review are still missing.

## Consequence and careful limits

The separately checked A119 rational intervals have lower bounds greater than 1 for its declared critical rectangles (2304 even, 4096 odd), and the reported tail argument excludes later critical deficits. *Conditional on the validity of those tail and critical-substitution results*, on Lambda_p=0 we get the uniform eventual inequality

\[
N_M\ge M^{-2}-CM^{-3}>0
\]

for sufficiently large M in the relevant reduced contact cells. This improves the **reduced** eventual sign conclusion only. It does not show that the compared C2 candidates have nonnegative masses, satisfy the inherited gamma constraint, or globally optimize F2/F3.

The result does **not** address r increasing with M, unbounded alpha, arbitrary deformed targets, or the fixed-interior arithmetic subsequences of A120–A122.

## Verification and failed attempts

On 10 November 2026, the standalone weighted-degree checker returned PASS, with 12 full and 12 residual monomial groups. The independent source-to-coefficient bridge returned PASS for even and odd Lambda/Xi, and the existing independent finite-stress script reproduced 18 exact Fraction J controls with high-precision numerical asymptotic comparisons. No new Lean 4 execution was performed in this session.

During development, two draft checks initially failed due to treating K-dependent expressions as if K were zero and comparing expanded/factored expressions literally. The tests were corrected to compare exact symbolic differences and to set K=0 only for the K-independent core. The final version passed. No mathematical hypothesis was changed to hide a counterexample.

## Independent A117 cell-entry and A119 tail audit (same research session)

A separate exact-rational test is now committed at [a119_independent_tail_and_entry_20261110.py](../../audits/a119_independent_tail_and_entry_20261110.py). It was executed in the working container with PASS. An 80-term rational atanh-series enclosure proves 2 < -log(s) < 21/10 over the entire frozen source window. Rational inequalities give strictly positive entry margins:

- even: 176249084859 / 2500000000000;
- odd: 76540493262589821 / 4000000000000000000.

The cutoff lower margins are both strictly positive, independently of floating-point tolerances: approximately 0.0020902493780287305 at even r=13, and 0.00024277493510525955 at odd r=20. The exact rational fractions are printed by the script, and match the earlier repository record. The upper bounds on the successive negative-tail magnitude ratios are 57/400 (even) and 1197/8600 (odd), both below 1. The positive lower-envelope contribution increases linearly with r, while the negative part decreases for later deficits. Thus, **conditional on A117's displayed endpoint inequality and one-crossing setup**, the elementary monotonic extension does rule out later critical contacts; this is more than checking the cutoff sign in isolation.

The calculation is not an independently reconstructed A118-to-A119 Xi derivation, not a repetition of the 6400-box interval exhaustion in this session, and not an F3 optimizer theorem.

## Literature and publication gate

The underlying moment/extreme-measure optimization is not new:

- Karlin and Studden (1966), *Tchebycheff Systems*, Interscience.
- A. E. Eckberg Jr. (1977), *Sharp Bounds on Laplace-Stieltjes Transforms*, Mathematics of Operations Research 2(2), 135–142, DOI 10.1287/moor.2.2.135.
- Iosif Pinelis (2016), *On the extreme points of moments sets*, Mathematical Methods of Operations Research 83, 325–349, DOI 10.1007/s00186-015-0530-0.

No full-text prior-art comparison was completed for this exact collision remainder and parity-dependent critical expression. **Novelty is not certified.**

**Remaining obligations:** (i) independently referee the uniform bounds and A118 coefficient bridge, (ii) complete Lean 4 proof with all quantifiers, (iii) verify A119 cutoff exclusion from the critical-cell inequalities, (iv) derive an explicit useful C if claiming finite-M certification, and (v) decide whether the article is only about C2 or would need a genuine full-F3 primal/dual theorem.

**Editorial verdict:** a substantially strengthened *reduced-factor* asymptotic argument, not a globally optimal LP result and not a physical theory.
