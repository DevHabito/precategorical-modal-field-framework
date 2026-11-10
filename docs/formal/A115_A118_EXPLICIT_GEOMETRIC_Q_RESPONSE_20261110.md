# A115–A118: explicit geometric bounds for the exact central Q response

**Date:** 2026-11-10
**Scope:** reduced C2(k) cofactor, frozen source and collision box.
**Evidence:** analytic inequalities with all decisive numerical comparisons independently rechecked by exact Python `Fraction`. This is **not yet an end-to-end Lean theorem** or a finite-M LP optimizer statement.

## Quantifiers

Let beta=1/8, delta=1/1875, s in [129/1000,133/1000], alpha in [8,45], M>=1000 an integer, h=floor(M/2), p=M mod 2, sigma_p=p/2, and

[
\tau=s\left(1+\frac{2\alpha}{M}\right),\quad
u=\tau^h,\quad
\rho=\frac{99}{100}.
]

Let (a_p(t)=1) in even parity and (a_p(t)=(1+t)/2) in odd parity. Define

[
L_h(t)=t-ht^h+(h-1)t^{h+1},\qquad
C_t=L_h(t)/L_h(\tau).
]

The **exact** original normalized response coefficients from A115 are

[
U=a_p(\tau)(C_\beta+2\delta)
 -a_p(\beta)(\beta/\tau)^h+\frac{\beta^M}{2u},
]
[
V=a_p(\tau)(C_s-2\delta)
 -a_p(s)(s/\tau)^h+\frac{s^M}{2u}.
]

The reduced comparison keeps

[
U_0=a_p(\tau)(\beta/\tau+2\delta),\quad
V_0=a_p(\tau)(s/\tau-2\delta)-a_p(s)(s/\tau)^h.
]

## Lemma 1: uniform positive central denominator

On the box, beta<s<tau<=3/20 and h>=2. For 0<tau<=3/20, the function h*tau^(h-2) is at most 2 for all integers h>=2: at h=2 it equals 2, and its ratio at successive indices is

[
\frac{h+1}{h}\tau\le\frac32\frac3{20}=\frac9{40}<1.
]

Therefore h*tau^(h-1)<=2tau<=3/10 and

[
L_h(\tau)=\tau[1-h\tau^{h-1}+(h-1)\tau^h]
\ge\frac7{10}\tau>0.
]

For either a=beta or a=s, since a<=tau,

[
|L_h(a)-a|\le2h a^h\le2h u,
\qquad |L_h(\tau)-\tau|\le2h u.
]

It follows by the exact quotient-difference identity that

[
\left|C_a-\frac a\tau\right|
\le\frac{40}{7}\frac{hu}{\tau}
\le\frac{20000}{903}Mu.
]

Every denominator is separated from zero, not assumed valid by numerical coincidence.

## Lemma 2: common geometric envelope

The exact rational comparisons are

[
\frac3{20}<\left(\frac25\right)^2,\qquad
\frac{125}{129}<\left(\frac{99}{100}\right)^2,
\qquad \frac{40}{99}<\frac12.
]

Because 2h=M-p, p in {0,1}, the first inequality gives

[
0<u\le\frac52\left(\frac25\right)^M.
]

For every M>=1, M/2^M<=1/2. Thus

[
Mu\le\frac54\rho^M.
]

Likewise beta/tau<=125/129 implies

[
(\beta/\tau)^h\le\frac{100}{99}\rho^M,
\qquad u\le\frac{100}{99}\rho^M.
]

Since beta,s<=tau<1 and M>=2h,

[
\beta^M\le u^2,\qquad s^M\le u^2.
]

The same argument supplies a uniform envelope for the finite beta contact channel: if 4<=r<=19 and k=h-r+1,

[
K=\frac{\beta^k}{u}
=\beta^{1-r}(\beta/\tau)^h
\le 8^{18}\frac{100}{99}\rho^M.
]

This constant is very large; it does **not** imply K is numerically small already at M=1000 for every r. It proves geometric decay with a uniform coefficient.

## Proposition: central response approximation with explicit constants

The exact U and V formulas and 0<a_p(t)<=1 give

[
|U-U_0|
\le\left|C_\beta-\beta/\tau\right|
 +(\beta/\tau)^h+\frac{\beta^M}{2u},
]
[
|V-V_0|
\le\left|C_s-s/\tau\right|+\frac{s^M}{2u}.
]

Combine Lemmas 1–2 to obtain

[
|U-U_0|\le
\left(\frac{25000}{903}+\frac{150}{99}\right)\rho^M
=\frac{290050}{9933}\rho^M<30\rho^M,
]

[
|V-V_0|\le
\left(\frac{25000}{903}+\frac{50}{99}\right)\rho^M
=\frac{840050}{29799}\rho^M<29\rho^M.
]

In particular

[
\boxed{|U-U_0|+|V-V_0|<59(99/100)^M}
]

uniformly across the **declared** source/alpha/M/parity box. The exact `Fraction` comparisons of tau<=3/20, both geometric bases and both final integer thresholds all returned TRUE in the research session.

## Scientific status and next proof work

These are analytic bounds under explicit hypotheses, not fitted observations. The constants are conservative and are not claims about an economically useful finite-M threshold.

This closes the *hand-derived* central-response and beta-channel geometric-envelope pieces of the uniform remainder argument. Formal Lean checks of the h-power induction, denominator lower bound, rational inequalities and final response estimates have not yet run.

The **full** normalized cofactor still requires bounding the u/v/K polynomial residual, checking the Taylor coefficient identities and obtaining one complete uniform constant for

[
|J/(u\tau^k)-\Lambda_p/M-\Xi_p/M^2|\le C/M^3.
]

The independent exact cofactor regression and the new Lean polynomial identities are documented separately. This note does not assert feasibility, dual optimality, general F2/F3 support, historical novelty, physical pregeometry or oncology relevance.
