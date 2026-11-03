# A113 Delta: strict rational error budget

**Research author:** Felipe Gianini Romero  
**Date:** 2026-11-03  
**Status:** exact arithmetic checked; universally quantified Lean source-to-budget inequalities remain pending.

## What I calculated

The original parity-specific source-minus-beta channel gap is

    Delta_M(s) = [H_M(s,false)-H_M(1/8,true)]/U_M.

The already audited finite channels fix `M>=521`, `s in [129/1000,133/1000]`, `h=floor(M/2)`, and `U=2^-h`. The previous `A113DeltaPreliminaries.lean` candidate strengthens the denominator estimate to `d>=999/1000` and the half-index node-power estimate to `s^h<=U/10^6`. Those theorems must compile before they may be used as certified premises.

Write the **nonnegative normalized power differences**

    P = (s^M - beta^M)/(2U),
    Q = (s^h - beta^h)/U,
    R = (s^(h+1) - beta^(h+1))/U.

From `beta<=s<=1/6`, monotonic powers and `M>=h`, the intended source-to-budget gates are

    0 <= P <= (1/2)10^-6,
    0 <= Q <= 10^-6,
    0 <= R <= 10^-6.

The existing Lean source already proves `hU/d <= 1/3`. Together with `h>=1`, this also gives `0 <= (h-1)U/d <= 1/3`. These cap the signed normalized defect terms.

Using the exact even/odd Delta decompositions in `A113_DELTA_CHANNEL_AUDIT_2026-11-03.md`, the resulting **conditional scalar** bounds are:

    Even:
      2*(129/1000-1/8)-4/1875-(5/3)*10^-6
      <= Delta_even <=
      2*(133/1000-1/8)/(999/1000)-4/1875
        +(1/2+2/3)*10^-6.

    Odd:
      (3/2)*(129/1000-1/8)-4/2500-(3/2)*10^-6
      <= Delta_odd <=
      (3/2)*(133/1000-1/8)/(999/1000)-4/2500
        +(1/2)*10^-6.

The standalone `tools/research_2026_11_03/pmff_a113_delta_error_budget.py` verifies all four endpoint inequalities in `Fraction` arithmetic, preserving exact margins:

| Bound | Exact bound | Strict margin to target |
| --- | --- | --- |
| Even lower | 1173/200000 | 313/200000 above 43/10000 |
| Even upper | 27739931/1998000000 | 232069/1998000000 below 7/500 |
| Odd lower | 8797/2000000 | 197/2000000 above 43/10000 |
| Odd upper | 6934733/666000000 | 2389267/666000000 below 7/500 |

The calculation contains two deliberate negative controls: the earlier weak `d>=3/4` fails the even upper gate, and a loose power budget `Q<=1/1000` fails the odd lower gate. Thus the choice of sharper constants has a mathematically traceable purpose; none were adjusted to match a finite-data result.

**What is *not* yet demonstrated:** the universal Lean derivation of `P,Q,R` bounds from the actual source definitions, the exact parity expansion of normalized Delta and the final quantified interval statement. The displayed scalar comparisons do not silently discharge these obligations. The source interval is continuous, not just the sampled endpoints.

## Next formal engineering step

Formalize the source-to-budget gates first; prove the scalar even and odd bounds as separate reusable lemmas; then compose them with the exact H channel identity and parity selection. Require pinned `lake build`, `#print axioms` and `leanchecker` at the exact code revision. Any failed proof must remain in the record.

No physical interpretation, all-tail A113 claim, or originality claim is attached to this checkpoint.
