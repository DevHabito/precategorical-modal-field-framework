# A117 — independent red-team audit

**Date:** 2026-09-15  
**Verdict:** **PASS WITH SCOPE**

This audit attacks the A117 boundary-layer phase classification rather than trying to confirm a preferred picture.

## 1. Claim under review

Under the inherited A115/A116 reduced-factor contract and the collision scaling

\[
\tau_M=s+\frac{\lambda}{M},
\]

A117 claims:

1. an eventual parity-resolved contact deficit;
2. a parity-unified leading limit for
   \[
   M\,J/(\tau^h\tau^k);
   \]
3. strict monotonic decrease of the leading phase function inside every admissible contact cell;
4. positive entry into every admissible cell;
5. consequently at most one positive-to-negative phase transition per cell.

It does **not** claim the next-order sign on the zero-limit surfaces.

---

## 2. Attack: copy the even formula into odd parity

**Attempt:** reuse the A116 even formula unchanged for `M=2h+1`.

**Result:** rejected.

The odd central-Q formula carries the factor

\[
a_{\rm odd}(s)=\frac{1+s}{2},
\]

both in the scale-normalized tolerance and in the leading `H_beta/H_s` corrections. The eventual contact cell is also shifted by one half unit because `M/2=h+1/2`.

A117 therefore derives odd parity independently.

Exact `Fraction` controls include odd positive and odd negative phases and agree with the separately derived odd limit sign.

---

## 3. Attack: ignore resonant ceiling surfaces

If

\[
x=\frac{\lambda}{2s(-\log s)}
\]

lands exactly on an integer (even parity) or half-integer (odd parity), a first-order contact formula alone is ambiguous.

A117 keeps the second term:

\[
M c_{\tau_M}(s)
=
\frac M2-x
+\frac{\alpha^2}{(-\log s)M}
+O(M^{-2}).
\]

The correction is positive, so the resonant surface belongs eventually to the preceding deficit cell. This yields

\[
r_p(x)=\lceil x-\sigma_p\rceil-1.
\]

The symbolic audit verifies the sign of this second-order coefficient.

**Disposition:** hardened; no unresolved ceiling convention remains at leading order.

---

## 4. Attack: use cells outside the A84 adjacent-factor domain

For

\[
b=h-r,
\qquad
k=b+1,
\]

the second factor in `J` is admissible only if

\[
k+1=h-r+2\le h-2.
\]

Thus

\[
\boxed{r\ge4}
\]

is a theorem premise for the boundary classification.

Cells with `r<4` are excluded rather than extrapolated.

---

## 5. Attack: phase function could oscillate inside one cell

Write

\[
F_{p,r}
=-a_pC+e^{-\alpha}(A_p+\alpha D_{p,r}).
\]

The derivative is exactly

\[
F'_{p,r}
=e^{-\alpha}
\left[D_{p,r}(1-\alpha)-A_p\right].
\]

On every admissible cell,

\[
\alpha>8,
\qquad
A_p>0,
\qquad
D_{p,r}>0,
\]

so

\[
F'_{p,r}<0.
\]

**Disposition:** multiple phase reversals inside a fixed cell are analytically impossible.

---

## 6. Attack: perhaps some cell starts negative

A117 does not infer the left-edge sign from finite samples. It proves a uniform lower bound over the full source interval and all `r>=4`.

The exact margins are

\[
F_{\rm even}^{\rm left}
>
\frac{176249084859}{2500000000000}>0,
\]

and

\[
F_{\rm odd}^{\rm left}
>
\frac{76540493262589821}{4000000000000000000}>0.
\]

The audit independently checks the rational inequalities used in these bounds, including

\[
2< -\log s<\frac{21}{10}.
\]

**Disposition:** every admissible cell is entered from the positive side.

---

## 7. Attack: hidden constant-channel contribution

A116 already exposed that a coarse constant-channel bound can be misleading after normalization.

A117 uses the exact telescoping grouping

\[
c_1
=(H_\beta-A)(a_s-a_\tau)
+(H_s-A)(a_\tau-a_\beta).
\]

In the `1/M` collision layer this gives

\[
c_1=O(u\tau^M/M),
\]

so the normalized constant contribution vanishes.

**Disposition:** no additional leading phase term is hidden in `c_1`.

---

## 8. Attack: numerical cancellation masquerading as phase structure

Deep boundary factors can be thousands of decimal orders below unity. During exploratory work, insufficient arbitrary precision produced false zeroes and a false sign.

Those calculations are not used.

The promoted audit computes finite `J` signs using exact `Fraction` arithmetic. The limiting phase sign is enclosed using rational Taylor lower/upper bounds for `exp(alpha)`.

Eight parity-resolved controls pass, including positive and negative phases in both parities.

**Disposition:** finite regression is protected against floating-point cancellation.

---

## 9. Attack: finite controls used as proof premises

They are not.

The classification theorem follows from the asymptotic coefficient limits, exact phase reduction, derivative sign and left-edge lower bounds. The finite controls are transcription/falsification checks only.

---

## 10. Attack: infinitely many negative cells at larger deficit

At the right cell edge,

\[
R_{p,r}(s)
=-a_pC
+(r+1+\sigma_p)Ls^{3+\sigma_p}
+O(r s^r).
\]

The linear positive term grows without bound while the last term decays exponentially. This is uniform over the frozen source window.

Therefore sufficiently large deficit cells are entirely positive.

**Disposition:** no infinite alternating cascade survives at leading order.

---

## 11. Critical surfaces

When

\[
\Lambda_p=0,
\]

A117 classifies the leading boundary term as critical and stops.

It does not infer the finite sign by continuity, finite sampling, or the Lambert representation. A next-order expansion is required.

This is the main open analytic frontier after A117.

---

## 12. Dependency and scope audit

A117 depends on:

- the exact target-deformed reduced factor of A115;
- the A84 contact/factor domain;
- the A64/A115 scale-normalized error contract;
- elementary asymptotic analysis and exact algebra.

It does not depend on:

- the refuted universal `M>=521` target-deformation claim;
- finite phase regressions as theorem premises;
- A114 lifted active-set classification;
- RZS, a modal field, or any physical interpretation.

## Final verdict

**PASS WITH SCOPE.**

The parity-resolved leading boundary-layer phase classification is internally consistent under the inherited reduced-factor contract. The codimension-one critical surfaces `Lambda_p=0` remain explicitly open at next order.
