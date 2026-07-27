# A100 Changelog

- Solved the first unresolved A99 witness at `M=443`, `s=13/100` with no support or band-activity restrictions.
- Used a 180-digit two-phase revised-simplex calculation only to discover the candidate active set.
- Reconstructed the candidate independently in exact rational arithmetic.
- Identified `P={77,78,443}`, `Q={0,1,221,222}` with active `alpha+`, `beta-`, and `gamma-`.
- Certified 8 positive basic variables, 3 positive active multipliers, all 881 unused-atom reduced costs, and all 3 opposite-band slacks.
- Verified exact primal feasibility and exact primal-dual equality.
- Recorded 895/895 strict KKT conditions and a unique global optimum at the declared rational contract.
- Preserved the boundaries: no interval theorem, no resolution of `M=449,484,490`, no universal support law, and no physical claim.
