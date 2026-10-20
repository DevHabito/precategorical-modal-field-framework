# A113 A84 finite coefficient bounds — 2026-10-20

**Scope:** the frozen A83/A84 finite-size model only, with
\`M>=521\`, \`129/1000<=s<=133/1000\`, \`beta=1/8\`,
\`tau=1/2\` and \`U_M=2^(-floor(M/2))\`.

**Status:** submitted as
\`formal/lean/PrecategoryFormal/A113CoefficientEnvelopes.lean\`,
including umbrella import, selected \`#print axioms\` and an isolated
\`leanchecker\` job. Verification was **in progress** when this report
was created; the theorem source must not be described as certified
until all relevant jobs have completed on the exact revision.

## Historical coefficients

The independent local definitions reproduce precisely the coefficients
of the original \`contactTenTermFactor\` in
\`A113SmallLeftBridge.lean\`:

\`\`\`text
v_beta = A*a_s - H_s*a_tau
v_s    = A*a_beta - H_beta*a_tau
v_tau  = H_beta*a_s - H_s*a_beta

c_beta = v_beta + (beta-1)*(A-H_s)
c_s    = -v_s + (1-s)*(A-H_beta)
c_tau  = -v_tau + (1-tau)*(H_beta-H_s)

d_beta = (1-beta)*v_beta
d_s    = (s-1)*v_s
d_tau  = (tau-1)*v_tau

c_1 = (H_beta-A)*a_s + (A-H_s)*a_beta + (H_s-H_beta)*a_tau
\`\`\`

Here \`A=(1+tau^M)/2\`, \`a_r=(1-r^M)/M\`; the beta/source
\`H\` definitions retain the exact historical plus/minus signs
and parity-dependent tolerances.

## Derivation without the final E-F assumption

Earlier Lean modules establish
\`|A-1/2|<=U/2\`,
\`|H_beta-1/2|<U\`, \`|H_s-1/2|<U\`,
\`0<=a_r<=1/M\`, and
\`|v_beta|,|v_s|,|v_tau|<=3U/M\`.

The triangle inequality then supplies the conservative caps

\`\`\`text
|A-H_beta|<=2U
|A-H_s|<=2U
|H_beta-H_s|<=2U
\`\`\`

For \`0<=beta,s,tau<=1/2\`, all three multipliers in the affine
and linear channels have absolute value at most one. As \`M>=521\`,
\`3U/M<3U\`. Hence each affine channel obeys

\`\`\`text
|c_r| <= 3U/M+2U < 5U.
\`\`\`

Each linear channel obeys \`|d_r|<=3U/M\`. Each of the three
constant-channel summands has magnitude at most \`2U/M\`,
so \`|c_1|<=6U/M\`.

The new Lean module isolates the pairwise channel bounds and these
three families. None of its new theorems imports the desired
\`|E_(M,k)(s)-F_k(s)|<20U\` as a hypothesis.

## Limits of this checkpoint

This step supplies candidate uniform bounds for the seven historical
A84 coefficients; it does **not** by itself prove the A84 coefficient
definitions are wired to every historical source, the full ten-term
factor error, any of the remaining remote/central A113 sectors or
the global KKT classification.

A rigorous follow-up must show that substituting these exact
coefficients into the universally quantified ten-term identity
yields

\`\`\`text
|E_(M,k)(s)-F_k(s)|<20U
\`\`\`

for all admissible \`M,s,k\` in the small-left sector. The
previously certified ideal-core lower bound can then turn this
remainder into unconditional positivity. The historical three invalid
ZIP packages and external novelty review remain independent gates.
