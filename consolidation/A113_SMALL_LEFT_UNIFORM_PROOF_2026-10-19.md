# A113 small-left sector — independent uniform positivity proof

**Date:** 2026-10-19  
**Status:** Independent analytic argument for the small-left sector only, with exact rational gate checks and independent pointwise reconstruction. No claim of a completed A113 theorem or external peer review.

## Contract and result

Let

```text
M >= 521, h = floor(M/2), U = 2^(-h),
129/1000 <= s <= 133/1000, beta = 1/8, tau = 1/2,
2 <= k <= 29.
```

For the A83/A84 adjacent-factor normalization, independently establish

```text
E_(M,k)(s) > 0
```

through a rational uniform lower bound. This result does not address `30 <= k <= b`, `k >= b+3`, central nesting, primal feasibility, or global lifted LP optimality.

## 1. Reconstruct the exact factor

The A83 cofactor definition is

```text
B_r = r^k - 1 + k a_r,      delta B_r = (r-1)r^k + a_r,
a_r = (1-r^M)/M,
A = (1+tau^M)/2,
X = A B_beta - H_beta B_tau,
Y = -A delta B_beta + H_beta delta B_tau,
W = -B_beta delta B_tau + B_tau delta B_beta,
E = X delta B_s + Y B_s + W H_s.
```

Here `H_beta` has the historical **plus** `2 epsilon` adjustment, while `H_s` has the **minus** adjustment. Their common `D_M(r)` is reconstructed from the explicit even/odd expressions in A84, rather than imported from any archived Python module.

Put `H_beta=H_s=A=1/2` and `a_r=1/M` to isolate the zero-`U` core. Expanding the cofactor formula leaves

```text
E0_k(s) = 1/2 * [
    (s-beta)*(beta*s)^k
  + (beta-tau)*(beta*tau)^k
  + (tau-s)*(s*tau)^k
].
```

This is not a limit taken at a finite `M`; it is a separately defined comparison expression.

## 2. Prove a positive core uniformly for all k in the sector

With `x=beta*s`, `y=beta*tau`, `z=s*tau`, direct multiplication gives the rational generating-function identity

```text
sum_(k>=1) [2 E0_k(s)] t^(k-1)
  = (s-beta)*(tau-beta)*(tau-s)
      / [(1-x*t)*(1-y*t)*(1-z*t)].
```

The coefficient of `t^(k-1)` on the right is `(s-beta)(tau-beta)(tau-s) h_(k-1)(x,y,z)`, where the complete homogeneous polynomial is a sum of nonnegative monomials. In particular `h_(k-1)(x,y,z) >= z^(k-1)`.

Since `beta < 129/1000 <= s <= 133/1000 < tau` and `1 <= k <= 29`,

```text
E0_k(s) >= L,
L = (1/2)*(129/1000-1/8)*(1/2-1/8)
         *(1/2-133/1000)*(129/2000)^28 > 0.
```

The exact rational check `L > 20/2^260` is part of the new standalone checker; no decimal rounding determines this comparison.

## 3. Uniform H-channel error, with both parities

For `r` equal to either `beta` or `s`, set `q=2r`. Then `0<r<1/6`, `q<1/3`, and `h>=260`.

The sequences `h 2^(-h)` and `(h+1)2^(-h)` decrease for `h>=260`. Direct integer checks at `h=260` establish

```text
h*U < 1/4,       (h+1)*U < 1/4,
d = 1-(h+1)*U > 3/4,
q^h < 1/1000,    r^M/U < 1/1000.
```

The last inequality follows from `M>=2h` and `r^M/U <= (2r^2)^h <= (1/18)^h`.

Use the exact A84 even expression

```text
D_even(r) = -2 U r/d
            +(1+2hU/d) r^h
            -2(h-1)U r^(h+1)/d.
```

Termwise absolute values and the inequalities above give

```text
|D_even(r)|/U
  <= (8/3)r + (5/3)q^h + (1/9)q^h
  < 4/9 + (16/9)/1000 < 1/2.
```

Similarly, the exact odd expression

```text
D_odd(r) = -(3/2) U r/d
           +(1/2+(3/2)hU/d)r^h
           +(1/2-(3/2)(h-1)U/d)r^(h+1)
```

implies

```text
|D_odd(r)|/U
  <= 2r + q^h + r*q^h
  < 1/3 + (7/6)/1000 < 1/2.
```

The historical tolerance is `epsilon=U/1875` for even `M`, `epsilon=U/2500` for odd `M`. Thus, with the correct opposite signs of the two adjustments,

```text
|H_r-1/2|/U
  <= r^M/(2U) + |D_M(r)|/U + 2 epsilon/U
  < 1/2000 + 1/2 + 2/1875 < 1.
```

Also `|A-1/2| <= U/2`, `|A|<=1`, `|H_r|<=1`, `0<a_r<=1/M` and `|a_r-1/M|<=U/M`. In particular, for any two of these moment slopes,

```text
|A a_i - H_r a_j| <= 3U/M,
|H_beta a_i - H_s a_j| <= 3U/M.
```

## 4. Bound every term of the ten-term remainder

The A84 expansion has three product terms, three affine exponential channels, and one constant term:

```text
E_k = A(s-beta)(beta*s)^k
    + H_s(beta-tau)(beta*tau)^k
    + H_beta(tau-s)(s*tau)^k
    + (c_beta+k*d_beta)*beta^k
    + (c_s+k*d_s)*s^k
    + (c_tau+k*d_tau)*tau^k + c_1.
```

In the zero-`U` comparison, the three affine channels and `c_1` vanish exactly. From the A84 algebra and the estimates in Section 3:

```text
total product-channel perturbation < 3U,
|c_beta|, |c_s|, |c_tau| < 5U,
|d_beta|, |d_s|, |d_tau| <= 3U/M,
|c_1| <= 6U/M.
```

All exponential bases lie strictly between zero and one. Consequently,

```text
|E_k-E0_k|
  < [3+15+(9k+6)/M]*U
  <= [18+(9*29+6)/521]*U
  < 20U.
```

Since `U<=2^(-260)` and `L>20*2^(-260)`, we have

```text
E_k >= E0_k - |E_k-E0_k| > L - 20U > 0.
```

This completes the all-`M), all-real-`s) small-left implication under exactly the declared contract. No finite-sample extrapolation is used.

## 5. Independent executable checks

Run:

```bash
python tools/independent_a113_small_left.py
```

The script uses only Python's `fractions.Fraction` and standard library. It independently reconstructs the cofactor and ten-term forms without importing the original A84/A113 modules, checks the strict rational constants used in this proof, and carries out 60 exact controls across `M=521,522,561,661`, three rational source points, and `k=2,3,7,15,29`.

Those 60 controls are implementation regressions, **not** the justification for the universal quantifiers. The reasoning in Sections 1–4 is the proof obligation; the checker guards its arithmetic gates and some representative algebraic reconstructions.

## 6. Assurance boundary and remaining work

This checkpoint closes only the small-left analytic implication. The original A113 recovered source still has unreviewed uniform bridge estimates for the middle-left, right-remote and central sectors. The historical A113 ZIP remains structurally invalid and must not be altered or relabeled. A theorem-level Lean implementation and independent human mathematical review have not been completed. No physical or originality statement follows.
