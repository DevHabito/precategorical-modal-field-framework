# A122 — fixed-interior near-resonant rounding-layer theorem

**Date:** 2026-09-15  
**Status:** **PROVED under the inherited A120/A121 fixed-interior reduced-factor contract; exact finite hardening and a computer-assisted double-critical existence certificate are included.**  
**Classification:** asymptotic theorem + exact arithmetic audit + rigorous interval-sign certificate.  
**No global target-deformed maximizer theorem and no physical or ontological interpretation are claimed.**

---

## 1. Scope

Keep

\[
\beta=\frac18,\qquad \delta=\frac1{1875},\qquad
\frac{129}{1000}\le s\le\frac{133}{1000},
\]

and fix

\[
s<\tau<\frac{\beta}{s}<1.
\]

Fix one parity \(p\) and one integer offset \(j\). Write

\[
h=\lfloor M/2\rfloor,\qquad u_M=\tau^h,
\]

\[
c=\frac{\log\tau}{2\log s},\qquad
b_M=\lceil Mc\rceil,\qquad
\rho_M=b_M-Mc,
\]

\[
k_M=b_M+j,\qquad x_M=j+\rho_M=k_M-Mc.
\]

Use

\[
\sigma_{\rm even}=0,\qquad \sigma_{\rm odd}=\frac12,
\]

\[
a_{\rm even}=1,\qquad a_{\rm odd}=\frac{1+\tau}{2},
\]

and

\[
G=\frac{s-\beta}{\tau}-4\delta>0.
\]

Define

\[
P_p=\frac{\tau-s}{2}\tau^{\sigma_p},
\qquad
Q_p=a_p(1-\tau)G(1-c),
\]

\[
\Phi_p(x)=P_p s^x-Q_p,
\qquad
\xi_p=\frac{\log(Q_p/P_p)}{\log s}.
\]

Thus \(\Phi_p(\xi_p)=0\).

---

# 2. Theorem A — complete algebraic-order core

Let

\[
\mathcal N_{M,j}
=
\frac{E_{M,k_M}}{u_M\tau^{k_M}}.
\]

Then

\[
\boxed{
\mathcal N_{M,j}
=
\Phi_p(x_M)
+\frac{\Omega_p(x_M)}{M}
+R_{M,j},
}
\]

where

\[
\boxed{
\Omega_p(x)=a_pG\,[1+(1-\tau)x].
}
\]

Moreover, for every fixed integer \(N\ge0\),

\[
\boxed{M^N R_{M,j}\to0}
\]

along the chosen parity.

So, for a fixed interior pair, the algebraic asymptotic core terminates after the \(1/M\) term; all omitted channels are beyond every polynomial order.

## Proof

A120 starts from the exact ten-term representation of \(E_k\). After division by \(u_M\tau^k\), only the \(s\tau\) product channel and the target-affine \(\tau^k\) channel survive at algebraic orders.

The product coefficient is

\[
c_{s\tau}=H_\beta(\tau-s),
\]

and, for a fixed interior pair,

\[
H_\beta=\frac12+O(u_M).
\]

Also

\[
\frac{s^{k_M}}{u_M}=\tau^{\sigma_p}s^{x_M}
\]

exactly. Hence this channel equals

\[
P_p s^{x_M}+o(M^{-N})
\]

for every fixed \(N\).

For the target-affine channel, A120 gives

\[
c_\tau=(1-\tau)(H_\beta-H_s)+(H_s a_\beta-H_\beta a_s),
\]

\[
c_{k\tau}=(\tau-1)(H_\beta a_s-H_s a_\beta),
\]

with

\[
a_r=\frac{1-r^M}{M}.
\]

The fixed-interior estimates sharpen to

\[
\frac{H_\beta-H_s}{u_M}
=-a_pG+o(M^{-N})
\]

for every \(N\), and

\[
a_\beta=\frac1M+o(u_M M^{-N}),
\qquad
a_s=\frac1M+o(u_M M^{-N}).
\]

Therefore

\[
\frac{c_\tau+k_Mc_{k\tau}}{u_M}
=
a_pG\left[-(1-\tau)+\frac{1+(1-\tau)k_M}{M}\right]
+o(M^{-N}).
\]

Since

\[
\frac{k_M}{M}=c+\frac{x_M}{M},
\]

this becomes

\[
-Q_p+\frac{a_pG[1+(1-\tau)x_M]}{M}+o(M^{-N}).
\]

All other ten-term channels carry fixed ratios strictly below one, for example \((\beta/s)^{k_M}\), \((s/\tau)^{k_M}\), \((\beta/\tau)^{k_M}\), or \(\tau^{M-k_M}\). Since \(k_M/M\to c\in(0,1/2)\), they decay exponentially and therefore faster than every power of \(1/M\). This proves the theorem.

---

# 3. Theorem B — the correct near-resonant scale

Suppose a fixed-parity subsequence satisfies

\[
x_M\to\xi_p
\]

and

\[
\boxed{M(x_M-\xi_p)\to\eta\in\mathbb R.}
\]

Then

\[
\boxed{
M\mathcal N_{M,j}
\longrightarrow
\Theta_p(\eta)
:=Q_p\log s\,\eta+\Omega_p(\xi_p).
}
\]

Indeed,

\[
\Phi_p'(\xi_p)
=P_ps^{\xi_p}\log s
=Q_p\log s.
\]

Thus the displacement of the arithmetic phase contributes at the same order \(1/M\) as the intrinsic \(\Omega_p\) term.

Define the critical drift

\[
\boxed{
\eta_p^*
=-\frac{\Omega_p(\xi_p)}{Q_p\log s}.
}
\]

Because \(Q_p>0\) and \(\log s<0\), \(\Theta_p\) is strictly decreasing. Hence

\[
\eta<\eta_p^*\Longrightarrow E_{M,k_M}>0
\]

eventually, while

\[
\eta>\eta_p^*\Longrightarrow E_{M,k_M}<0
\]

eventually.

Therefore the A121 resonant factor cannot in general be classified from a static `Psi=0 => sign(Omega)` rule. The approach rate of the ceiling phase is part of the leading resonant data.

---

# 4. Corollary — next scaled phase layer

If

\[
x_M
=\xi_p+\frac\eta M+\frac\zeta{M^2}+o(M^{-2}),
\]

then

\[
\mathcal N_{M,j}
=
\frac{\Theta_p(\eta)}{M}
+\frac{\Upsilon_p(\eta,\zeta)}{M^2}
+o(M^{-2}),
\]

where

\[
\boxed{
\Upsilon_p(\eta,\zeta)
=Q_p\log s\,\zeta
+\frac12Q_p(\log s)^2\eta^2
+a_pG(1-\tau)\eta.
}
\]

Hence a tuned first resonant balance leads to a second **phase-drift** layer. It is not an independent intrinsic coefficient tower.

---

# 5. Theorem C — the intrinsic resonant coefficient can vanish

Define

\[
\omega_p(s,\tau)=\Omega_p(\xi_p(s,\tau)).
\]

The conjecture that \(\omega_p\) has one fixed nonzero sign throughout the inherited target region is false.

For even parity and

\[
s=\frac{129}{1000},
\]

the accompanying exact interval audit uses

\[
\log x=2\sum_{n\ge0}\frac{z^{2n+1}}{2n+1},
\qquad z=\frac{x-1}{x+1},
\]

with an exact rational geometric tail bound. It proves

\[
\omega_{\rm even}\left(\frac{129}{1000},\frac{131}{1000}\right)<0,
\]

and

\[
\omega_{\rm even}\left(\frac{129}{1000},\frac{132}{1000}\right)>0.
\]

The audit's human-readable interval displays are approximately

\[
-0.00197264<\omega_{\rm left}<-0.00197231,
\]

\[
0.00298661<\omega_{\rm right}<0.00298663,
\]

but the sign decisions themselves are exact `Fraction` assertions.

By continuity, the intermediate value theorem gives at least one

\[
\boxed{
\tau_*\in\left(\frac{131}{1000},\frac{132}{1000}\right)
}
\]

such that

\[
\boxed{
\Omega_{\rm even}(\xi_{\rm even})=0.
}
\]

A high-precision orientation calculation locates one such root near

\[
\tau_*\approx0.13134881724047417,
\qquad
\xi_{\rm even}\approx-1.15121008277.
\]

These decimals are not used in the proof.

At such an intrinsic double-critical parameter, if an arithmetic subsequence also obeys

\[
x_M-\xi_p=o(M^{-1}),
\]

then \(M\mathcal N_{M,j}\to0\). A122 does **not** assert that the actual discrete rounding sequence realizes exact or super-\(1/M\) resonance; that is a separate Diophantine problem.

---

# 6. Exact computational hardening

The audit reconstructs the exact A115 reduced factor with `fractions.Fraction` and compares it with the polynomial core.

For

\[
s=\frac{131}{1000},\qquad \tau=\frac15,
\]

four even controls

\[
M=4568,5596,6624,7652
\]

have exact normalized-factor signs

\[
+,+,-,-,
\]

matching the exact polynomial-core signs, with

\[
|R_M|<M^{-5}
\]

in all four cases.

Two odd controls

\[
M=959,1449
\]

likewise match signs \(+,-\), with exact

\[
|R_M|<M^{-3}.
\]

The JSON also reports floating \(\rho,\xi,\eta,\eta^*\) and \(\Theta\) values as diagnostics only. No promoted finite sign uses those floats.

---

# 7. What A122 establishes

1. The normalized fixed-interior factor has the complete algebraic-order core
   \[
   \Phi_p(x_M)+\Omega_p(x_M)/M.
   \]
2. The remainder is beyond every power of \(1/M\) for fixed interior parameters.
3. The A121 resonance is a joint intrinsic/arithmetic scaling problem.
4. The critical first drift is \(\eta_p^*\).
5. A second scaled phase layer follows explicitly when the first balance is tuned away.
6. The intrinsic resonant coefficient \(\Omega_p(\xi_p)\) is not sign-definite and can vanish inside the declared parameter region.

---

# 8. Nonclaims / open problems

A122 does **not** prove:

- uniqueness of the intrinsic double-critical \(\tau_*\);
- realization of exact phase resonance by the discrete sequence at \(\tau_*\);
- a uniform finite threshold over the full target region;
- collision scaling \(\tau-s=O(1/M)\) for these remote factors;
- a global target-deformed compressed-maximizer theorem;
- a target-deformed A114 lifted classification;
- novelty or priority relative to the literature;
- any RZS, modal-field, physical, spacetime, gravity, matter, or ontological interpretation.
