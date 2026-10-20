# A113 — recovered source and independent contact-envelope proof

**Date:** 2026-10-19
**Status:** Original A113 Python certificate source recovered with CRC and
SHA-256 verification. The source's 23 exact gates passed an unchanged
execution. A separate elementary contact-envelope lemma is rederived
analytically. The full A113 uniform one-variation theorem is NOT yet
independently certified.

## 1. Recovered artifacts and truthful provenance

The original `A113_FULL_REPRODUCIBILITY_PACKAGE_20260912.zip` is still
invalid and does not match its dated manifest SHA-256. It must not be
replaced or renamed to hide that result.

Read-only local-header inspection nevertheless recovered the **first
ZIP member in its entirety**, with raw DEFLATE completion, 9,145
decompressed bytes and matching internal CRC-32:

`a113_tail_global_compressed_one_variation_certificate.py`

The verified SHA-256 of this member is

`46e1fec5197c7253e29156e592e2320905cd993caa66f3f5b9cd109471b11587`.

A separately readable reconstruction from the GitHub Actions log is
preserved without code edits under

`consolidation/recovered_provenance/a113_tail_global_compressed_one_variation_certificate.py`.

The independent replay script
`tools/replay_salvaged_a113_certificate.py` compares that visible file
byte-for-byte with the CRC-verified original ZIP member and checks the
same SHA-256 before executing the original source.

The recovered second ZIP member (the full JSON certificate) is
**truncated**. A114-A's source member is also truncated; the A112-G
JSON member fails DEFLATE/CRC validation. They remain unrecovered.

## 2. Re-execution of the unchanged original A113 source

[GitHub Actions run 39343954194](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39343954194)
used an isolated virtual environment with pinned SymPy 1.13.3 and
executed the recovered source without changing its arithmetic,
hypotheses, or output path.

The recovered script generated a fresh JSON result whose
**23/23 exact rational/symbolic checks were true**. It reports
strictly positive exact rational margins for:

- the small-left dominant core;
- the middle-left normalized estimate;
- the remote-right normalized estimate;
- the central `J=E_(b+1)-2 E_(b+2)` estimate.

The replay gate verifies the result's exact rational strings as
`fractions.Fraction` without floating sign decisions. An earlier
attempt failed because `python -I` could not find SymPy installed
outside the isolated environment. The virtual environment corrected
the dependency problem without modifying the original mathematics.

**Interpretation:** recovering and replaying the script certifies
that it executes and that its declared gates pass. It does not
independently prove that all its manually chosen algebraic bounds
really dominate the original A84 factor for every allowed parameter.
Those missing bridge justifications are listed below.

## 3. Independently rederived uniform contact-envelope lemma

Let

```text
M >= 521, s in [129/1000, 133/1000], h=floor(M/2),
U=2^(-h), beta=1/8,
c(s) = log(2)/(-2 log(s)),
b = ceil(M*c(s)).
```

The endpoint comparisons used in the historic script are strict:

```text
c(129/1000) > 16923/100000,
c(133/1000) < 17180/100000.
```

**These can be certified using only integer arithmetic**, without
evaluating a numerical logarithm. For a positive rational `r=p/q`,
`c(s)>r` is equivalent to `2^q*s^(2p)>1`. The reverse
inequality is equivalent to `<1`. Since

```text
c'(s) = log(2)/(2*s*(log(s))^2) > 0
```

on `0<s<1`, the exact endpoint checks imply
`16923/100000 < c(s) < 17180/100000`
for every real `s` in the frozen closed interval.

From the ceiling definition,

```text
b-1 < M*c(s) <= b.
```

The identity `s^(M*c(s)) = 2^(-M/2)` follows
directly from the definition of `c(s)`. Since `0<s<1`,

```text
s * 2^(-M/2) < s^b <= 2^(-M/2).                    (1)
```

For even `M=2h`, `2^(-M/2)=U`. Hence

```text
s < s^b/U <= 1.
```

For odd `M=2h+1`, `2^(-M/2)=U/sqrt(2)`. Hence

```text
s/sqrt(2) < s^b/U <= 1/sqrt(2).
```

The exact rational inequality
`1/2 > 49/100` implies
`1/sqrt(2) > 7/10`, so **uniformly in both parities**,

```text
(7/10)*s < s^b/U <= 1.                            (2)
```

This justifies the source's lower core coefficient
`RMIN=(7/10)*(129/1000)` directly, without a fitted
numerical approximation.

Next, because `h<=M/2`, `b>=M*c(s)` and
`c(s)>16923/100000`,

```text
h-3b < M*(1/2 - 3*16923/100000)
     <= 521*(1/2 - 3*16923/100000)
     < -4.
```

The left side is an integer, so `h-3b<=-5`.
Consequently,

```text
beta^b/U = 2^(h-3b) <= 1/32.                      (3)
```

This supplies the central beta-channel suppression used
in the original majorant. It is a derived parity-uniform bound,
not a finite-grid inference.

The `b` range is also uniform: `M*c(s)>521*16923/100000>88`
gives `b>=89`, while the upper bound
`b<M*17180/100000+1` and
`h >= (M-1)/2` prove `b+3<=h-2` for every `M>=521`.
The last inequality holds since its worst-case linear margin
at `M=521` is strictly positive and increases with `M`.

These conclusions use only the stated source window, integer
parity, monotonicity and ceiling definition. No KKT theorem,
native computation axiom, or archived certificate is assumed.

## 4. Independent computational controls

`tools/independent_a113_contact_envelopes.py` independently
checks both rational-power endpoint inequalities, the three
universal linear threshold gates, and the normalized
contact/dyadic inequalities for 24 rational selected controls
across even/odd ranks through `M=4097`.

**Important:** the 24 cases are regression controls; the
analytical argument in Section 3 establishes the all-`M`
contact-envelope implication.

The CI gate is separate from the unchanged A113 script replay.

## 5. Independent small-left sector closure (later checkpoint)

The new [small-left proof](A113_SMALL_LEFT_UNIFORM_PROOF_2026-10-19.md)
reconstructs the A83/A84 factor separately and proves the uniform
positive sign for every `M>=521`, every real `s` in the frozen source
interval and each `2<=k<=29`. It uses a positive homogeneous-polynomial
core and a conservative `20*2^(-floor(M/2))` remainder envelope.
Its arithmetic is checked by `tools/independent_a113_small_left.py` in
60 independent exact pointwise controls and rational universal threshold
gates. This removes the small-left *sector* from the open bridge list;
it does not certify the middle-left, right-remote or central sectors,
repair the invalid historical ZIP or supply a human review.

## 6. Exact unclosed proof obligations

The original source's 23 passed gates do not automatically establish
the full A113 theorem. The next independent review must verify:

1. the ten-term A84 factor identity connecting the actual adjacent
   compressed LP objective differences to the majorant decomposition;
2. all uniform remainder inequalities for `H_r`, `eta_r`,
   `Delta`, and each affine coefficient across both parities;
3. the claim that the small-left, middle-left, remote-right and
   central `J` error budgets bound the original `E_k`
   **for every admissible integer `k`, every `M>=521`,
   every real `s` in the closed interval**;
4. any overlap, omitted contact, equality or endpoint case in the
   partition `k<=29`, `30<=k<=b`, `k>=b+3`;
5. whether the Wronskian/Chebyshev and LP hypotheses required to
   infer the global compressed maximizer are stated completely;
6. a theorem-by-theorem classical literature comparison.

The original result is therefore **replay-confirmed, not yet
independently derivation-confirmed**. No physical result, novelty
claim or unrestricted LP classification follows from this step.
