# A114-B2-W1 correction note

The first exploratory M=521 simplex run used the even-parity epsilon scale `1875`, which is inconsistent with the odd-M frozen contract. That run is excluded from the promoted evidence.

A corrected rerun uses `M=521`, `s=129/1000`, and `epsilon=1/(2500*2^260)`. It returns the same candidate support and active bands: `P={90,91,521}`, `Q={0,1,260,261}`, with `alpha+`, `beta-`, `gamma-` active.

The promoted result relies on the exact SymPy KKT certificate and the independent `fractions.Fraction` cross-check, not on the exploratory solve.

This result is **PROVED POINTWISE / B2 STILL OPEN**. No all-tail rule such as `F_(b+2)^up<0 => q0/q1 gamma-minus` is claimed.
