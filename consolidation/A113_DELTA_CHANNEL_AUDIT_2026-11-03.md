# A113 beta/source H-channel gap — independent finite checkpoint

**Research author:** Felipe Gianini Romero  
**Date:** 2026-11-03  
**Status:** self-contained exact-rational finite audit of a historical inequality. **The universal interval bound remains unproved in this checkpoint.**

## Why this is the next obligation

The positive central two-step expression depends on a difference between the two parity-sensitive H channels. The recovered A113 certificate uses the normalized quantity

    Delta_M(s) = (H_M(s, source) - H_M(beta, beta))/U_M,
    beta=1/8, U_M=2^(-floor(M/2)),

and checks the target interval

    43/10000 < Delta_M(s) < 7/500.

The recovered script's numerical gates passed in its historical isolated replay, but they did not establish all required continuous majorant-to-factor implications. I need a clean proof of these **one-sided** channel-difference inequalities before promoting the central sign theorem.

I reopened `formal/lean/PrecategoryFormal/A113FiniteChannels.lean` at the current branch and used its exact even/odd definitions, including the **opposite** beta/source tolerance adjustments. The available universal H estimate, `|H_r-1/2|<U`, is not strong enough by itself: combining two such bounds only gives a difference in `(-2U,2U)`, and says nothing about the narrow strictly positive interval above.

## Exact decomposition

Set `h=floor(M/2)`, `u=2^(-h)`, `d=1-(h+1)u`, `beta=1/8` and `r=s`. Both source and beta channels include the same parity-specific defect `D_M(r)`, but their epsilon adjustments have opposite signs.

The original definitions imply, **exactly**,

    Delta = (s^M-beta^M)/(2u) - [D_M(s)-D_M(beta)]/u
            - 4*epsilon/u.

For even M, substituting the historical defect gives

    Delta_even =
        2*(s-beta)/d - 4/1875
        + (s^M-beta^M)/(2u)
        - (1+2*h*u/d)*(s^h-beta^h)/u
        + (2*(h-1)*u/d)*(s^(h+1)-beta^(h+1))/u.

For odd M:

    Delta_odd =
        (3/2)*(s-beta)/d - 4/2500
        + (s^M-beta^M)/(2u)
        - (1/2+(3/2)*h*u/d)*(s^h-beta^h)/u
        - (1/2-(3/2)*(h-1)*u/d)*
            (s^(h+1)-beta^(h+1))/u.

These identities expose a positive leading gap, a known signed epsilon shift, and explicit high-power corrections. They are **not** inequalities obtained by fitting tests. Derive uniform estimates for the residual terms separately and do not discard them merely because they appear small.

## Independent exact finite verification

The standalone script `tools/research_2026_11_03/pmff_a113_delta_channels.py` uses Python standard-library `Fraction` arithmetic and does **not** import the recovered original source. It computes both H channels directly, compares their difference exactly with the parity-expanded expression above, tests the historical strict rational bounds and checks that reversing the epsilon sign orientations is detected.

I executed 21 combinations locally: `M in {521,522,561,661,1000,2049,4097}` and `s in {129/1000,131/1000,133/1000}`. The source endpoints are included, both parities are present, and all asserted comparisons passed. The script is also added to the dedicated research regression workflow for an independent CI environment.

There are only **21 finite sampled points**. This neither establishes the continuous-source interval nor exhausts every natural M. The apparent numeric margin must not be promoted to a theorem. In particular, the leading odd-parity lower estimate at the lower source endpoint is `(3/2)*(129/1000-1/8)-4/2500=11/2500`, only `1/10000` above the desired lower `43/10000`. A rigorous lower bound therefore needs a controlled residual, not a qualitative “tiny error” assertion.

## Next proof gates

1. Prove in Lean an explicit bound on `(h+1)2^(-h)` sharper than the present `d>=3/4` so the even-parity upper bound remains below `7/500`.
2. Bound each normalized high-power difference uniformly for all real `s` in the closed interval, with exact rational margins and both parities.
3. Establish the strict lower and upper Delta inequalities as Lean conclusions with **no Delta hypothesis** in their statements.
4. Obtain `#print axioms` and `leanchecker` evidence at the exact commit.
5. Only then combine those bounds with the actual A113 central-pair expansion and the independently justified threshold contact estimates.

The larger A113 central sign, remote sectors, global compressed optimizer and physical interpretation are **still open** here. The relevant classical Tchebycheff/moment-space foundations are already documented with authors, dates and source links in `consolidation/C3_A110_A114_ADVERSARIAL_CHECKPOINT_2026-10-19.md`; no priority claim is made in this checkpoint.
