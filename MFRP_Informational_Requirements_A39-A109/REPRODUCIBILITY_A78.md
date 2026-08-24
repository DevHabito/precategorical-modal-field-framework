# Reproducibility and Scope — A78

A78 is an exact finite rational-probe audit.

- Probe: `s0 = 131/1000`.
- Support range: integer `M = 10,...,80`.
- Arithmetic: exact SymPy rationals.
- Candidate branches: 9230.
- Certification: full finite-LP KKT signs, including every nonbasic reduced cost and inactive observation-band slack.

The committed compact result records the selected branch for every support size and the exact objective ratio. The branch catalogue records the classification and first failing condition class for every rejected branch.

The result is pointwise in `s`. It is not an interval theorem and must not be extrapolated to arbitrary support sizes.
