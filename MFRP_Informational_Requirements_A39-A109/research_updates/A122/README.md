# A122 — near-resonant rounding layer

A122 refines the A121 phase-front resonance for fixed interior target deformation.

## Status

**PROVED under the inherited A120/A121 fixed-interior reduced-factor contract; red-team PASS WITH SCOPE.**

For

\[
\mathcal N_{M,j}=\frac{E_{M,b_M+j}}{\tau^{\lfloor M/2\rfloor}\tau^{b_M+j}},
\qquad x_M=j+\rho_M,
\]

A122 proves

\[
\mathcal N_{M,j}
=\Phi_p(x_M)+\frac{\Omega_p(x_M)}{M}+R_{M,j},
\]

with

\[
\Omega_p(x)=a_pG[1+(1-\tau)x]
\]

and

\[
M^N R_{M,j}\to0
\]

for every fixed \(N\).

Near the A121 phase front \(x=\xi_p\), if

\[
M(x_M-\xi_p)\to\eta,
\]

then

\[
M\mathcal N_{M,j}\to Q_p\log s\,\eta+\Omega_p(\xi_p).
\]

Thus the resonant sign depends jointly on the intrinsic \(1/M\) term and the arithmetic approach rate of the rounding phase.

A122 also gives an exact computer-assisted IVT certificate that, for even parity at \(s=129/1000\), the intrinsic resonant coefficient changes sign between \(\tau=131/1000\) and \(132/1000\). Hence at least one interior \(\tau_*\) has \(\Omega_{\rm even}(\xi_{\rm even})=0\).

Exact hardening:

- 4 even near-resonant Fraction controls: signs `+,+,-,-`, all exact remainders `< M^-5`;
- 2 odd controls: signs `+,-`, exact remainders `< M^-3`;
- exact rational logarithm intervals certify the double-critical sign bracket.

Open:

- realization of exact/super-`1/M` phase resonance by the arithmetic sequence;
- uniqueness of the intrinsic double-critical target;
- collision scaling `tau-s=O(1/M)` for remote factors;
- global target-deformed maximizer localization;
- target-deformed A114;
- novelty/priority;
- any physical or ontological interpretation.
