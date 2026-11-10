# A119: compact 35-rectangle rational positivity certificate

**Date:** 2026-11-10
**Scope:** A115-A119 reduced C2(k) critical-substitution formula, not the unrestricted F2/F3 optimum.
**Evidence:** an independent local Python Fraction implementation passed on 2026-11-10. The newly committed checker has not yet been executed in a new GitHub Actions run or by Lean.

## Result

The A119 historical checker used 25 deficit cases times a 16-by-16 rational grid, or 6,400 boxes. The same substituted critical coefficient Xi_hat has strictly positive interval lower endpoints on **35 closed rational boxes**.

Constants: beta=1/8, delta=1/1875, s in [129/1000,133/1000].
For parity sigma=0 (even), sigma=1/2 (odd), each candidate deficit r has alpha in the larger interval [A,B], where A=2(r+sigma), B=(21/10)(r+1+sigma).
Keep the entire original s interval in every box, without splitting it.
Partition the alpha coordinate as alpha=A+(B-A)t:

| r | parity | t endpoints | number per parity |
|---|---|---|---:|
| 4 | both | 0, 1/4, 1/2, 1 | 3 |
| 5,6,7 | both | 0, 1/2, 1 | 2 for each r |
| 8..12 | both | 0, 1 | 1 for each r |
| 13..19 | odd only | 0, 1 | 1 for each r |

Totals: **14 even and 21 odd boxes**. The closed intervals abut, so their unions contain the full enlarged rectangles used by A119. Under A117's independent 2 < -log(s) < 21/10 contact-cell bound, these include every actual critical cell.

## Exact rational output

All 35 boxes passed strict lower-bound positivity and the critical denominator and q positivity checks.

Overall minimum lower endpoint (even, r=4, t in [1/2,1]):

436152226670319684540420616481093 / 4002264870000313289466234723750000 > 0

Decimal display only: approximately 0.10897635234978477.

Odd minimum (odd, r=4, t in [1/2,1]):

334539706718612647585650758917552506997082603 / 1932898972921296034123328117372024031250000000 > 0

Decimal display only: approximately 0.17307666432923002.

These are conservative interval lower endpoints, NOT estimates of the true minimum of Xi_hat. The earlier 6,400-box implementation had a higher lower endpoint because its boxes were narrower; there is no contradiction.

The fixed 35-box partition is reproducible without adaptive search. Deliberately using only two coarse alpha boxes at r=4 fails positivity certification for both parities; this is a correct negative control of the interval method, NOT an actual negative Xi value.

## Implementation and reproduction

See [the committed rational verifier](../../audits/a119_compact_35box_fraction_certificate_20261110.py).
Run it with Python 3 and assertions enabled. Its formula implementation reuses the earlier audited A119 interval code but uses the new 35-box manifest.

A separately written local standard-library implementation, with a different interval class, was executed successfully. The independent local source SHA256 is 6efaf15ea52b45a7c967c92c8c7c98660432747779fd85c8b8e63e36acfa52a0 and the output log SHA256 is a6d35398d3c5160cbe723e7358ab6e9296092f9a024e85eba6071edcbf9baeea. The local replay is NOT represented as CI success for the newly committed GitHub file.

## Precise logical scope

At a genuine A117 critical root, e^(-alpha) equals a_p*C/(A_p+alpha*D_p,r), where C=1-beta/s-4delta, B=beta/s+2delta, A_p=a_p*(1-B) and D_p,r=s^(2-r)-a_p*B. Substituting into A118's Xi formula gives the rational Xi_hat checked above.

The 35-box check does not independently derive the source A115-to-A118 asymptotic coefficients, establish the high-deficit cutoff for even r>=13 and odd r>=20, prove unrestricted LP dual feasibility, demonstrate any integer resonance, produce a quantitative finite-M threshold, certify historical novelty or claim physical significance. The separate [tail and entry audit](../../audits/a119_independent_tail_and_entry_20261110.py) addresses the endpoint-tail step under the inherited A117 phase formula; the separate [uniform remainder note](A115_A119_UNIFORM_REMAINDER_20261110.md) addresses the analytic error bound.

## References and contribution boundary

- A. D. Brucker, T. Cameron-Burke, A. Stell (2024), Formally Verified Interval Arithmetic and Its Application to Program Verification, FormaliSE, DOI 10.1145/3644033.3644370. Interval splitting is classical method, not a new theorem.
- I. Pinelis (2016), On the extreme points of moments sets, Mathematical Methods of Operations Research 83, 325-349, DOI 10.1007/s00186-015-0530-0. Relevant prior art for the broader moment problem, not a confirmed match for this exact critical factor.

**Publication recommendation:** replace the historical 6,400-box subcertificate with this 35-box manifest after a separate checker run and mathematical review. Neither certificate by itself validates the full theorem chain or a global full-LP optimizer.
