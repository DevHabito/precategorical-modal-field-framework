# A118 — second-order critical collision-layer expansion

**Date:** 2026-09-15  
**Status:** **PROVED under the inherited A115/A116/A117 target-deformed reduced-factor contract.**  
**Classification:** second-order asymptotic theorem + exact local critical certificate + finite computational stress.  
**Global positivity of the second-order coefficient is NOT proved.**  
**No physical or ontological interpretation is claimed.**

---

## 1. Scope

Keep the A117 collision scaling

\[
\tau_M=s+\frac{\lambda}{M},
\qquad
\frac{129}{1000}\le s\le\frac{133}{1000},
\qquad
\lambda>0,
\]

with

\[
\beta=\frac18,
\qquad
\delta=\frac1{1875}.
\]

Fix one parity. Put

\[
\sigma_p=
\begin{cases}
0,&M\text{ even},\\[2pt]
\frac12,&M\text{ odd},
\end{cases}
\qquad
h=\frac M2-\sigma_p.
\]

Let `r>=4` be the eventual A117 contact deficit, so for all sufficiently large `M` of the fixed parity,

\[
b_M=h-r,
\qquad
k_M=h-r+1.
\]

Define

\[
\alpha=\frac{\lambda}{2s},
\qquad
q=e^{-\alpha},
\qquad
u=\tau_M^h,
\]

and the normalized central transform

\[
N_M=
\frac{J_{\tau_M,k_M}}
{\tau_M^h\tau_M^{k_M}}.
\]

A117 proved

\[
M N_M\to\Lambda_p(s,\lambda,r).
\]

A118 computes the next coefficient.

---

## 2. Theorem — second-order expansion

For every fixed `s`, `lambda`, parity and eventual admissible deficit `r>=4`,

\[
\boxed{
N_M
=\frac{\Lambda_p}{M}
+\frac{\Xi_p}{M^2}
+o(M^{-2})
}
\]

along integers `M` of the fixed parity.

Equivalently,

\[
\boxed{
M^2\left(
N_M-\frac{\Lambda_p}{M}
\right)
\longrightarrow \Xi_p.
}
\]

On an A117 critical surface,

\[
\Lambda_p=0,
\]

this reduces to

\[
\boxed{
M^2N_M\longrightarrow\Xi_p.
}
\]

Thus, whenever `Xi_p != 0`, the finite critical sign is eventually the sign of `Xi_p`.

A118 does **not** prove that `Xi_p` is nonzero on every critical surface.

---

## 3. Notation for the coefficient

Set

\[
a_p(s)=
\begin{cases}
1,&M\text{ even},\\[2pt]
\dfrac{1+s}{2},&M\text{ odd},
\end{cases}
\]

and

\[
B=\frac\beta s+2\delta,
\qquad
T=1-2\delta,
\qquad
S=1-q-2\delta.
\]

Define the first exponent corrections

\[
\eta_h=\alpha^2+2\sigma_p\alpha,
\]

\[
\eta_k=\alpha^2+2\alpha(\sigma_p+r-1).
\]

Define

\[
B_1
=2\sigma_p\alpha s B
-2a_p\alpha\frac\beta s,
\]

\[
S_1
=2\sigma_p\alpha s T
-2a_p\alpha
-a_pq\eta_h.
\]

Finally set

\[
G_2
=2\alpha\left[
1+(1-s)(\alpha+2-\sigma_p-r)
\right].
\]

Then

\[
\boxed{
\Xi_p
=\Xi_{\rm main}
+\Xi_{\rm src}
+\Xi_{\rm tgt},
}
\]

where

\[
\boxed{
\Xi_{\rm main}
=(1-s)\alpha s^{2-r}q\eta_h,
}
\]

\[
\boxed{
\Xi_{\rm src}
=q\left[
 a_pB G_2
 -(1-s)(\alpha+1)
 \left(B_1+a_pB\eta_k\right)
\right],
}
\]

and

\[
\boxed{
\Xi_{\rm tgt}
=(1-s)(B_1-S_1)
-2\alpha s\,a_p(B-S).
}
\]

These formulas are parity-resolved through both `sigma_p` and `a_p`.

---

## 4. Exponential-ratio expansions

Since

\[
\tau_M=s\left(1+\frac{2\alpha}{M}\right),
\]

one has

\[
\log\frac{s}{\tau_M}
=-\frac{2\alpha}{M}
+\frac{2\alpha^2}{M^2}
+O(M^{-3}).
\]

With

\[
h=\frac M2-\sigma_p,
\]

this gives

\[
\boxed{
\left(\frac{s}{\tau_M}\right)^h
=q\left(
1+\frac{\eta_h}{M}
+O(M^{-2})
\right).
}
\]

Likewise, because

\[
k_M=h-r+1,
\]

\[
\boxed{
\left(\frac{s}{\tau_M}\right)^{k_M}
=q\left(
1+\frac{\eta_k}{M}
+O(M^{-2})
\right).
}
\]

The accompanying symbolic audit verifies these first-order corrections through the assembled `1/M^2` coefficient.

---

## 5. Central-Q corrections through first order

Write

\[
\mathcal B_M
=\frac{H_\beta-1/2}{\nu},
\qquad
\mathcal S_M
=\frac{H_s-1/2}{\nu}.
\]

The exact A115 Q-block gives, after discarding only exponentially smaller channels,

\[
\boxed{
\mathcal B_M
=a_pB+\frac{B_1}{M}+O(M^{-2}),
}
\]

\[
\boxed{
\mathcal S_M
=a_pS+\frac{S_1}{M}+O(M^{-2}).
}
\]

For odd parity the finite prefactor

\[
\frac{1+\tau_M}{2}
=\frac{1+s}{2}+\frac{\alpha s}{M}
\]

affects `B_1` and `S_1`. This is why the odd second-order formula cannot be obtained by copying the even one.

---

## 6. The three polynomial-order channels

At collision scale, the beta channels are exponentially smaller than every fixed power of `1/M`, and the A117 constant-channel grouping remains exponentially negligible after the A118 normalization.

Only three channels contribute through order `M^-2`.

### 6.1 `s tau` channel

Using

\[
\tau_M-s=\frac{2\alpha s}{M},
\qquad
\frac{s^{k_M}}{\nu}
=s^{1-r}\left(\frac{s}{\tau_M}\right)^h,
\]

its expansion is

\[
\frac{\Lambda_{\rm main}}M
+\frac{\Xi_{\rm main}}{M^2}
+o(M^{-2}).
\]

### 6.2 Source-affine channel

Up to exponentially small terms, the exact coefficient identities reduce to

\[
\frac{c_s}{\nu}
=-\mathcal B_M\left[(1-s)-\frac1M\right],
\]

\[
\frac{c_{ks}}\nu
=\frac{1-s}{M}\mathcal B_M.
\]

Expanding the exact source bracket in `J` produces the displayed `Xi_src`.

### 6.3 Target-slope channel

Similarly,

\[
-\frac{c_{k\tau}}\nu
=\frac{1-\tau_M}{M}
\left(\mathcal B_M-\mathcal S_M\right)
+o(M^{-2}),
\]

which yields `Xi_tgt`.

Adding the three channels proves the theorem.

The symbolic audit independently constructs this truncated core and verifies exactly that its coefficient of `1/M` is the A117 `Lambda_p` and its coefficient of `1/M^2` is the A118 `Xi_p`.

---

## 7. Critical-surface consequence

A117 reduces the critical condition to

\[
-a_pC
+q\left[A_p+\alpha D_{p,r}\right]
=0,
\]

where

\[
C=1-\frac\beta s-4\delta,
\]

\[
A_p=a_p(1-B),
\qquad
D_{p,r}=s^{2-r}-a_pB.
\]

At such a point,

\[
N_M=\frac{\Xi_p}{M^2}+o(M^{-2}).
\]

Therefore a complete leading+critical classification reduces to the sign problem

\[
\boxed{\Xi_p\ ?\ 0.}
\]

That sign problem remains open globally in A118.

---

## 8. Computational stress

The audit performs two independent kinds of computation.

### 8.1 Symbolic algebra gate

SymPy verifies exactly:

- the assembled `1/M` coefficient equals `Lambda_p`;
- the assembled `1/M^2` coefficient equals `Xi_p`.

Both gates pass.

### 8.2 Critical-root stress

Using high-precision root isolation only as finite evidence:

- a regular 101-point source grid over `[0.129,0.133]` produces **1500** mixed-cell critical roots;
- all 1500 have `Xi_p>0`;
- 250 additional pseudo-random source values produce **3770** further critical roots;
- all 3770 also have `Xi_p>0`.

The smallest regular-grid value is approximately

\[
\Xi\approx2.0613642968
\]

at

\[
s=0.129,
\quad p=\text{odd},
\quad r=4.
\]

These thousands of positive controls are **finite evidence only**. They are not used as premises of the theorem and do not prove global positivity.

---

## 9. Exact rational certificate at the apparent worst control

For

\[
s=\frac{129}{1000},
\qquad
p=\text{odd},
\qquad
r=4,
\]

rational Taylor bounds certify that the unique A117 critical root lies in

\[
\boxed{
10.560492<\alpha_*<10.560493.
}
\]

Propagating this bracket through an exact rational interval evaluation of `Xi_p` gives

\[
\boxed{
2.061361852<\Xi_p<2.061366276.
}
\]

In particular,

\[
\boxed{\Xi_p>2}
\]

for this rigorously isolated critical point.

This exact local certificate supports, but does not replace, a global proof.

---

## 10. Current epistemic status

### Proved

1. The second-order expansion
   \[
   N_M=\Lambda_p/M+\Xi_p/M^2+o(M^{-2}).
   \]
2. The explicit parity-resolved formula for `Xi_p`.
3. On `Lambda_p=0`,
   \[
   M^2N_M\to\Xi_p.
   \]
4. The exact rational positive certificate for the stated odd `s=0.129,r=4` critical point.

### Finite evidence

- `1500/1500` regular-grid critical roots have `Xi_p>0`;
- `3770/3770` additional random-source critical roots have `Xi_p>0`.

### Open

- whether
  \[
  \Xi_p>0
  \]
  on **every** A117 critical surface throughout the frozen source window;
- whether a higher degeneracy `Lambda_p=Xi_p=0` exists anywhere;
- an explicit finite realization threshold near a critical surface;
- any target-deformed A114 lifted active-set theorem.

---

## 11. Nonclaims

A118 does not claim:

- that finite root scans prove global positivity;
- that no third-order degeneracy exists;
- a universal or minimal finite `M` threshold;
- a target-deformed A114 staircase;
- any RZS, modal-field, spacetime, physical or ontological interpretation.
