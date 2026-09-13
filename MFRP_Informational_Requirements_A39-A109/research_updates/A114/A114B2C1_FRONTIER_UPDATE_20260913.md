# A114-B2 frontier update after C1 — 2026-09-13

A114-B2-C1 closes one conditional branch inside the strict compressed `b+2`, negative-pivot tail.

Under

`M>=521`, `129/1000<=s<=133/1000`, strict compressed maximizer `j=b+2`, and `Phi=F_(b+2)^up<0`,

let `C` be the compressed two-band basis and `E` the endpoint-released basis. If

`p0^C<0` and `r_E(q0)>0`,

then `E` satisfies the complete strict KKT system and is the unique strict global basic optimum.

The proof includes a new analytic source box

`9/1000 < s^(b+1)/2^(-h) < 1/25`,

an exact C-to-E Cramer exchange identity, a 121/121 protected endpoint certificate, a standalone Fraction reconstruction with positive and hostile controls, and a logical composition audit.

The remaining strict `Phi<0` frontier is:

- `p0^C>0`: compressed two-band branch candidate;
- `p0^C<0, r_E(q0)<0`: q0/q1 edge, where gamma-inactive QI and gamma-minus-active QA compete;
- the degenerate boundaries `p0^C=0` and `r_E(q0)=0`.

`Phi=0` also remains open. A114-B2 is therefore not yet globally closed.
