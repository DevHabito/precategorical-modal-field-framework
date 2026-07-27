# A98 — Exact unrestricted full-LP resolution of the first A97 residual obstruction

## Status

**Exact rational theorem at one declared finite contract.**

A97 left seven rational witnesses at which the endpoint-released family

\[
P=\{j-1,j,M\},\qquad Q=\{1,h,h+1\}
\]

failed because the nonbasic \(q_0\) column had negative reduced cost.  The direct substitution
\(Q=\{0,h,h+1\}\) also failed in all seven cases.  A98 removes every support restriction at the first residual witness:

\[
M=396,\qquad s=\frac{13}{100},\qquad h=198,\qquad j=70.
\]

A 180-digit revised-simplex computation was used only to discover a candidate active set.  The proof is an independent exact rational primal-dual certificate for the complete finite LP.

## Exact active set

The unrestricted optimum is

\[
\boxed{P=\{70,396\}},
\]

\[
\boxed{Q=\{0,1,198,199\}},
\]

with active bands

\[
\boxed{\alpha+,\quad\beta-}
\]

and both orientations of \(\gamma\) strictly inactive.

This is not the direct repair tested in A97.  The \(q_0\) direction enters **without replacing** \(q_1\): both lower-end Q atoms enter together, while the central pair \(198,199\) remains.  On the P side, the lower adjacent contact \(69\) disappears, leaving only the compressed contact \(70\) and the endpoint \(396\).

## Original probability laws

After undoing the Charnes–Cooper scale, the P law is approximately

\[
P(70)=0.60736196319018404908\ldots,
\]

\[
P(396)=0.39263803680981595092\ldots.
\]

The Q law is approximately

\[
Q(0)=1.3209284362\ldots\times10^{-63},
\]

\[
Q(1)=1.3626628286\ldots\times10^{-62},
\]

\[
Q(198)=1-O(10^{-60}),
\]

\[
Q(199)=2.9459896027\ldots\times10^{-60}.
\]

The very small Q masses are exact positive rationals.  They may not be rounded to zero in the certificate.

## Complete strict KKT certificate

A98 checks:

- 7 strictly positive basic variables;
- 2 strictly positive active-band multipliers;
- 788 strictly positive reduced costs for every unused P and Q atom;
- 4 strictly positive inactive-band slacks;
- exact satisfaction of all seven basis equations;
- exact equality of primal and dual objective values.

The total is

\[
\boxed{801\text{ strict KKT conditions}}.
\]

The smallest reduced cost is the unused atom \(p_{395}\), and it remains strictly positive:

\[
r_{p_{395}}=2.1781924501592989040\ldots\times10^{-24}>0.
\]

The smallest basic variable is \(q_0\) in scaled coordinates:

\[
q_0=0.00052893408551378870364\ldots>0.
\]

The smallest inactive slack is the \(\gamma-\) slack:

\[
0.00019322976158162709735\ldots>0.
\]

Strict feasibility and strict reduced costs establish the unique global optimum of the declared unrestricted finite LP.

## Structural conclusion

The A97 obstruction was not resolved by a one-column replacement.  It required a coordinated support reorganization:

\[
\boxed{
P:\{j-1,j,M\}\to\{j,M\},
\qquad
Q:\{1,h,h+1\}\to\{0,1,h,h+1\}.
}
\]

This is a genuine correction to the sparse active-set architecture.  It is not evidence for a physical object or law.

## What A98 does not prove

A98 does not prove:

1. persistence of this basis on an interval of \(s\);
2. resolution of the other six A97 residual obstructions;
3. a universal rule that \(q_0\) and \(q_1\) always enter together;
4. a universal two-atom P / four-atom Q theorem;
5. any physical, spatial, temporal, material, or ontological interpretation.

## Next rigorous target

A99 should proceed in two falsifiable stages:

1. build all 801 KKT expressions symbolically in \(s\) and isolate the maximal strict component containing \(s=13/100\);
2. test the A98 architecture at the six remaining A97 residual witnesses, while allowing a different unrestricted active set when it fails.

A numerical discovery may locate candidates, but every promoted result must again be reconstructed as an exact rational or interval primal-dual certificate.
