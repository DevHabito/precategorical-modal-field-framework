# Independent arithmetic checks: A119 and A122

**Date:** 2026-11-06  
**Branch:** `research/a115-a122-independent-paper-audit-20261106`  
**Evidence type:** separately implemented exact-rational computations. Not a complete independent validation of the inherited theorem chain.

## 1. A119: covering check

The published A119 audit was read from `MFRP_Informational_Requirements_A39-A109/research_updates/A119/a119_global_critical_xi_positivity_audit.py`. I then implemented the interval arithmetic and A118-substitution formula in a separate 1,998-byte Python script, **not by invoking the repository script**.

Operations: rational interval addition, multiplication, division, and integer powers; inclusive endpoints; natural interval propagation of the published rational expression for `Xi-hat`. The initial source interval is `[129/1000,133/1000]`. The contact rectangles use `2(r+sigma)<=alpha<=(21/10)(r+1+sigma)`, 16 partitions on each coordinate. The even deficits are `r=4..12`; odd `r=4..19`.

Observed execution:

| parity | boxes evaluated | smallest certified lower endpoint | box location |
|---|---:|---|---|
| even | 2304 | `7962094616280060340361057850523941099377/4460543890481278214239707910840320000000` | r=4, i=0, j=0 |
| odd | 4096 | `3296636265099577642233577213168576496429665038806348563/2438741833785351580293579578096010608476160000000000000` | r=4, i=0, j=0 |

All 6,400 lower endpoints were strictly positive. **These independently obtained fractions exactly match the A119 manuscript.**

I also independently computed the stated analytic cutoff lower bounds and found positive rational values: even approximately `0.0020902493780287305` at r=13; odd approximately `0.00024277493510525955` at r=20. Both positivity comparisons were exact; decimals are display approximations.

**Interpretation:** the interval certificate is computationally reproducible and its result agrees with the project's published certificate. It is still necessary to check independently (i) the A115-to-A118 symbolic reductions, (ii) the inequality implying exclusion of all later deficit cells, and (iii) the derivation of the critical substitution itself. The output alone is **not** a complete theorem proof.

## 2. A122: independent interval-sign check

A second standalone Python script used exact `fractions.Fraction` arithmetic to enclose logarithms. For `x<1`, define `z=(x-1)/(x+1)`; expand `log(x)=2 sum_{k>=0} z^(2k+1)/(2k+1)`. The 70-term truncation is enclosed by an explicit geometric-tail majorant `2*|z|^(2n+1)/((2n+1)*(1-z^2))`. All subsequent interval operations are rational, with no floating-point sign decisions.

Using A122's definitions `c=log(tau)/(2log(s))`, `G=(s-beta)/tau-4delta`, `P=(tau-s)/2`, `Q=(1-tau)G(1-c)`, `xi=log(Q/P)/log(s)` and `Omega_even(xi)=G[1+(1-tau)xi]`, I checked:

| source s | target tau | enclosed Omega_even(xi), decimal display | exact sign |
|---|---|---|---|
| 129/1000 | 131/1000 | [-0.001972611525827406,-0.001972611525744094] | strictly negative |
| 129/1000 | 132/1000 | [0.0029866169718171763,0.0029866169718171767] | strictly positive |

Provided `Omega_even(xi)` is continuous on the intervening target interval (its denominators and logarithm arguments are positive there), the intermediate value theorem establishes at least one zero in `(131/1000,132/1000)`. This is a continuous-parameter existence result; it **does not prove an integer rounding subsequence** achieves exact or super-1/M resonance. The reproductions agree in sign with A122's manuscript.

## 3. Literature and originality pressure (bibliography verified in this session)

- Alan F. Karr (1983), “Extreme Points of Certain Sets of Probability Measures, with Applications,” *Mathematics of Operations Research* **8**(1), 74–85. DOI: https://doi.org/10.1287/moor.8.1.74 . The abstract explicitly includes probability measures with prescribed values of Laplace transforms. This is **close prior art** for the finite moment/transform extremal setup, not an exact match to the target-deformed asymptotic sign results.
- Samuel Karlin and William J. Studden (1966), *Tchebycheff Systems: With Applications in Analysis and Statistics*, Interscience. Catalogued in CERN and Google Books. Foundational background on moment space/extremal representations.
- Robert G. Jeroslow (1973), “Asymptotic Linear Programming,” *Operations Research* **21**(5), 1128–1141. DOI: https://doi.org/10.1287/opre.21.5.1128 . Its abstract addresses eventual parametric LP behavior; note that its coefficients are rational functions of a parameter, so it is a conceptual neighbor **not an automatic equivalent** of this exponentially parameterized family.
- Ramon E. Moore, R. Baker Kearfott, and Michael J. Cloud, *Introduction to Interval Analysis*, SIAM, chapter 11, “Applications,” https://doi.org/10.1137/1.9780898717716.ch11 . Standard validation framework for inclusion-certified computer-assisted reasoning.

## 4. Immediate next falsification gates

1. Independently derive the reduced factor `E_M,k` from the underlying optimization constraints, including all signs and normalizations; then reproduce `Xi-hat` from A118, rather than trusting the expression in A119.
2. Inspect A117's resonance endpoint convention, particularly ceiling at exactly integral contact phase and odd/even half-cell shift.
3. Verify the full inequality that excludes all `r>=13` (even) and `r>=20` (odd), not merely positivity at the cutoff index.
4. Determine whether A119's fixed numerical `s,beta,delta` assumptions are structurally necessary; any wider generalization requires separate proof.
5. Do not identify classical equidistribution, the IVT, or rational interval arithmetic itself as new contributions.

**Provisional verdict:** A119's exact covering certificate and A122's continuous double-critical sign change passed targeted independent reproductions, but originality, complete proof-chain validity, and publication readiness remain **uncertified**.
