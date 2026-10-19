# C3 / A112 — independent determinant and Schur-complement derivation

**Date:** 2026-10-19  
**Assurance:** generic algebraic derivation with an elementary exponential
zero-count argument for the P-block orientation; six exact rational
finite controls passed independently. The **uniform sign of the final
source coefficient A(s) remains an inherited A112-G analytic premise**,
not an independently re-proved all-tail inequality.

## 1. Raw eight-equation LP equality system

Fix integers `M` and `j` with `0<j<j+1<M`. Set
`h=floor(M/2)`, `beta=1/8`, `gamma=1/16`, `tau=1/2`,
and `P=(0,j,j+1,M)`, `Q=(1,h,h+1)`.

Use eight unknowns ordered as `(p0,pj,p(j+1),pM,q1,qh,q(h+1),t)`.
The eight active equations, in **exactly this row order**, are:

1. `sum(P)-t=0`;
2. `sum(Q)-t=0`;
3. `sum(x*P)-M*t/2=0`;
4. `sum(x*Q)-M*t/2=0`;
5. `sum(tau^x*Q)=1`;
6. `sum(s^x*P)-sum(s^x*Q)-2*epsilon*t=0` (alpha+);
7. `-sum(beta^x*P)+sum(beta^x*Q)-2*epsilon*t=0` (beta-);
8. `sum(gamma^x*P)-sum(gamma^x*Q)-2*epsilon*t=0` (gamma+).

The centered mean, target and tolerance normalizations are those of the
frozen A112 contract. The determinant factorization below is algebraic
and does not assume primal positivity or a strict compressed maximum.

## 2. Source-independent seven-by-seven block

Temporarily omit row 6 and place it at the bottom. Moving row 6 past
rows 7 and 8 involves **two exchanges**, so the determinant retains
its sign.

Let `H` be the matrix of the other seven equations in the seven
P/Q mass variables, and let `k` be their coefficient column for `t`.
Then the full basis matrix is block-partitioned as

```text
B8 = [ H      k   ]
     [ alpha  alpha_t ]
```

with the understanding that row 6 is moved to the bottom by the
orientation-preserving permutation above.

On the natural P and Q subblocks,

```text
C = [ 1          1           1           1        ]
    [ 0          j/M         (j+1)/M     1        ]
    [ 1          beta^j      beta^(j+1)  beta^M   ]
    [ 1          gamma^j     gamma^(j+1) gamma^M  ]

Q = [ 1          1           1           ]
    [ 1          h           h+1         ]
    [ tau        tau^h       tau^(h+1)   ].
```

Grouping the four P rows `(1,3,7,8)` and the three Q rows `(2,4,5)`
of `H` requires an **odd** permutation. The beta-minus P
coefficient row has one further sign reversal relative to `C`.
The unnormalized P-mean row contributes a factor `M`.
Because the three Q normalization/mean/target rows have zero P entries,
the reordered seven-by-seven matrix is block triangular, regardless
of the P rows' Q coefficients. Therefore, without any inversion:

```text
det(H) = M * det(C) * det(Q).                         (1)
```

If `H` is nonsingular, the source-independent masses are affine
in `t` with slope vector `v = -H^(-1)*k`. The coefficient of `t`
in the remaining alpha row is

```text
A(s) = alpha_t + alpha*v
     = alpha_t - alpha*H^(-1)*k.
```

The Schur determinant identity now yields

```text
det(B8) = det(H)*A(s)
        = M*det(C)*det(Q)*A(s).                       (2)
```

This is the exact identity independently checked in the current
8x8 equation ordering. It is **not** an assertion that every historical
determinant symbol `D_G` has the same row normalization or sign:
those must be aligned explicitly before substituting (2) into a
different archive convention.

## 3. Q determinant: exact formula and sign

Subtract the first Q column from the other two and expand:

```text
det(Q) = (h-1)*(tau^(h+1)-tau)
       - h*(tau^h-tau)
       = [1-(h+1)*2^(-h)]/2.                         (3)
```

For every integer `h>=2`, `2^h > h+1` (base case and induction)
and therefore `det(Q)>0`. The actual analytic tail has `h>=260`.

The corrected exact determinant is NOT identically `1/2`:
that is only its asymptotic limit. Discarding the exponentially small
`(h+1)*2^(-h)` term would be an unjustified exactness shortcut.

## 4. P interpolation determinant: direct Chebyshev sign

Consider the four real functions, in this declared order,

```text
f0(x)=1, f1(x)=x/M, f2(x)=exp(a*x), f3(x)=exp(b*x),
a=log(beta)<0, b=log(gamma)=2*a<a.
```

No nontrivial linear combination of these functions can have four
distinct real zeros. Indeed, if it did, Rolle's theorem would give
at least two distinct zeros of its second derivative. When at least
one exponential coefficient is nonzero, the second derivative is
a sum of at most two exponential terms with distinct exponents;
dividing by a positive exponential reduces its zero equation to a
nonconstant monotone exponential equal to a constant, so it has
at most one zero. If both exponential coefficients vanish, the
combination is affine and cannot have four zeros unless it is
identically zero.

Thus the four-point evaluation determinant is never zero at ordered
distinct nodes. The ordered-quadruple domain is connected, so its
orientation is constant. Letting four nodes coalesce at `x`, its
leading divided-difference sign equals the sign of the Wronskian

```text
W(f0,f1,f2,f3)(x)
  = a^2*b^2*(b-a)*exp((a+b)*x)/M
  < 0.
```

Therefore `det(C)<0` for every `0<j<j+1<M`, independent
of the source parameter `s` and of adjacent primal positivity.
This specializes a classical extended-Chebyshev argument;
the technique is **not a new theorem or a priority claim**.

## 5. Final orientation: the remaining analytic hypothesis

Combining (2) and (3) with `M>0` and `det(C)<0`:

```text
A(s)<0  ==>  det(B8)>0.                              (4)
```

This sign transfer is mathematically conditional. The assertion
`A(s)<0` uniformly over every `M>=521`, every real
`s in [129/1000,133/1000]` and the localized contacts is
the analytic A112-G branch-regularity task. The historical
composition audit cites a separate certificate, but the full
archive-level inequalities have **not yet been independently rebuilt
from first principles in this new audit**.

The current derivation removes the potential circularity in the
determinant orientation once `A(s)<0` is independently established:
it does **not** invoke `p_j,p_(j+1)>0` in (1)–(4).

## 6. Exact six-control independent regression

`tools/independent_c3_determinant_orientation.py` constructs all
eight rows directly, computes `det(B8)`, `det(C)`, `det(Q)`
through exact rational elimination and obtains `A(s)` through a
separate source-independent seven-by-seven solve.

It verifies the full equality in (2), the exact (3), and the signs
`det(C)<0`, `det(Q)>0`, `A(s)<0`, `det(B8)>0`
for the predeclared controls:

| M | s | j | Parity |
|---:|---:|---:|---|
| 521 | 129/1000 | 91 | odd |
| 522 | 131/1000 | 91 | even |
| 561 | 53/400 | 98 | odd |
| 600 | 133/1000 | 106 | even |
| 821 | 129/1000 | 141 | odd |
| 1000 | 129/1000 | 171 | even |

All decisions use `Fraction`; decimals and determinant-condition-number
estimates are never used as sign gates.

CI: [independent-audit run 39341225813](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39341225813)
completed successfully. These finite evaluations are **not** a
replacement for the all-tail source-coefficient inequality.

## 7. What this does and does not establish

**Analytically reconstructed:** Q determinant formula/positivity,
global nonsingularity and negative orientation of the P four-function
evaluation determinant, and the universal Schur factorization for
the specified matrix convention.

**Finite independent checks:** the full eight-by-eight determinant
identity and final sign at six odd/even localized controls.

**Still open in this audit:** the quantitative uniform A112-G
`A(s)<0` certificate and its hypotheses; the A112-B interlacing
inequality; the A112-C full P/Q reduced-cost collapse and the
extended-Chebyshev zero-budget application; all A113 remote and
central *uniform* source-window bounds.

The complete original A112 tail certificates are stored inside
`A112_TAIL_CLOSURE_WORKING_SET_20260911.zip`. Until their critical
sublemmas are independently inspected and reproduced, the current
checkpoint must not be advertised as a clean-room all-tail verification.

## Classical background

- S. Karlin and W. J. Studden, *Tchebycheff Systems: With Applications
  in Analysis and Statistics*, Interscience, 1966.
- A modern reference discussing equivalent Wronskian sign and zero
  properties is the 2017 paper by Novaes and Torregrosa,
  *On extended Chebyshev systems with positive accuracy*,
  DOI: https://doi.org/10.1016/j.jmaa.2016.10.076.

The specific A112 application and source coefficient are project
specific; the Wronskian/extended-Chebyshev tool is classical.
