# A114-B2-C — corrections and scope

## Status

This is a provenance and claim-boundary note for the residual-chain investigation. It is not a theorem statement.

## Corrections made before publication

1. A first numerical residual census contained an implementation bug: `mpmath.matrix[-1]` was treated like Python-list indexing when extracting the Charnes–Cooper scale. That census was discarded before promotion.
2. Three earlier exploratory examples used the wrong contact index by one unit. They were discarded and recomputed from the exact `b=ceil(M c(s))` gate.
3. An inherited list of twelve large-support KKT controls was replayed from scratch. Five labels/points failed the stated classification package: several had `Phi>0` and one negative-pivot point belonged to another residual class. The statement “those twelve pass” is withdrawn.
4. The final twelve controls in this package were selected only after exact premise reconstruction and then passed the complete `2M+9` KKT scan.
5. No floating-point sign enters either promoted executable certificate in this package.

## What is promoted

- an exact finite pivot-sign census on 28 strict-`b+2`, `Phi<0` records;
- zero failures of six declared pivot/sign relations on that census;
- twelve pointwise exact full-KKT certificates, three for each of `C`, `E`, `QI`, `QA`;
- the residual sign tree as a **conjectural analytic target** supported by exact finite evidence.

## What is not promoted

- no all-M residual classification theorem;
- no claim that the sign relations already have proved positive proportionality factors throughout the tail;
- no claim that `Phi<0` by itself selects a unique architecture;
- no statement at `Phi=0`.
