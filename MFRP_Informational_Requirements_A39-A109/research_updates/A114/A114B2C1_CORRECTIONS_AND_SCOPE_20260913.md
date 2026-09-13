# A114-B2-C1 corrections and scope — 2026-09-13

## 1. The old `b+3` endpoint theorem was not copied blindly

A114-A used the same endpoint support in the strict compressed `b+3` phase, but its sign assumptions are not automatically valid in `b+2`. C1 re-runs the complete symbolic endpoint model on a new B2-specific box:

- `Q=s^(j-1)/U` is enlarged to `[9/1000,1/25]`;
- `Y=beta^j/U` is enlarged to `2^-13`;
- the contact bound is changed from `j=b+3` to `j=b+2`;
- gamma-tail caps are loosened accordingly.

After this change, the only uniform sign failures are exactly the intended branch discriminants `p_(j-1)^E <-> p0^C` and `r_E(q0)`.

## 2. The source box is separately proved

The endpoint certificate does not assume an empirically fitted `Q` interval. A standalone source-box certificate derives

`9/1000 < s^(b+1)/U < 1/25`

from:

- strict compressed `b+2` (`E_(b+1)>0`);
- the exact A113 ten-term majorants;
- the already-proved B2-B implication `Phi<0 => 3j-h>=13`;
- the A112-A V2 bridge and audited remainder caps.

## 3. No `r_E(q0)<0` claim is smuggled into C1

When `r_E(q0)<0`, the A114-A Q-reduced-cost argument no longer applies because the positive checkpoint at `q0` is absent. C1 therefore stops at `r_E(q0)>0` and makes no QI/QA claim.

The exact controls at `M=555` and `M=521` intentionally preserve this failure: the endpoint basis fails only at `rc_q_0`.

## 4. Finite evidence remains regression only

The Fraction controls validate transcription and branch sensitivity. They are not premises of the all-tail analytic proof.

## 5. Remaining frontier

After C1, the unproved strict-negative-pivot partition is:

- `p0^C>0` — candidate C branch;
- `p0^C<0, r_E(q0)<0` — QI/QA edge and gamma-minus cut;
- zero-discriminant boundaries.

General A114-B2 remains open until these are closed and audited.
