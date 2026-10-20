# A113 small-left D envelopes: analytic derivation and formal status

**Date:** 2026-10-20
**Status:** exact analytic derivation of parity envelopes; only the geometric and coefficient lemmas have been encoded in Lean in this checkpoint. Do not call the D conclusion kernel-certified yet.

For M>=521, put h=floor(M/2), U=2^(-h), d=1-(h+1)U and 0<=r<=1/6. Previously proven Lean lemmas give U>0 and d>=3/4>0. The new A113DefectEnvelopes.lean module establishes:

- r^h <= U/128, by induction from h>=5 and the exact base (1/6)^5 < (1/2)^5/128.
- r^(h+1) <= U/768.
- hU<=1/4 and hU/d<=1/3.

Also (h-1)U/d<=hU/d<=1/3 for h>=1. These inequalities yield *on paper*, independently for the actual frozen definitions:

Even case, by triangle inequality:

```text
|D_even(r)|/U <= 2*r/d
  + (1+2*h*U/d)*r^h/U
  + 2*(h-1)*U/d * r^(h+1)/U
<= 4/9 + (5/3)/128 + (2/3)/768
 = 11/24 < 1/2.
```

Odd case: the third coefficient `1/2-(3/2)*(h-1)*U/d` is between zero and 1/2. Thus

```text
|D_odd(r)|/U <= (3/2)*r/d
  + (1/2+(3/2)*h*U/d)*r^h/U
  + (1/2)*r^(h+1)/U
<= 1/3 + 1/128 + (1/2)/768
 = 175/512 < 1/2.
```

These exact rational endpoint comparisons were independently evaluated with Python fractions, not floating point. The mathematical argument is uniform in M and r, and includes both parity cases.

**Important assurance boundary:** the complete two-branch triangle-inequality derivation above has NOT yet been compiled or replayed by Lean. The already committed Lean lemmas supply the strong power and hU/d bounds; translating both remaining triangle-inequality steps into Lean is the next formal task. Do not silently promote this note into a kernel-certified D theorem.

With a checked `|D_M(r)|<U/2` the future H-channel theorem can use the retained opposite-sign epsilon adjustments. The all-contact finite-M remainder `|E_(M,k)-F_k|<20U`, and hence the complete finite-M sign law, remain open. Historical ZIP integrity also remains red.
