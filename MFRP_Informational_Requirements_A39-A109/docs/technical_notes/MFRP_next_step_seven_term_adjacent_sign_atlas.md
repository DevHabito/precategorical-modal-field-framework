# A83 — Seven-Term Adjacent-Difference Factorization and Complete Local Sign Atlas

**Programme:** Modal Field Research Programme  
**Audit:** A83  
**Status:** exact algebraic factorization; exact finite/local sign atlas for `10 <= M <= 80` and `129/1000 <= s <= 133/1000`

## 1. Question

A82 located the compressed maximizer at the rational probe by signs of adjacent objective differences

\[
D_{M,k}(s)=V_{M,k+1}(s)-V_{M,k}(s).
\]

Its exact cross numerator had degree `2M`. A83 asks whether that numerator has a smaller structural form, whether the local sign atlas can be completed rather than inferred from endpoint signs, and whether strict unimodality follows from discrete concavity.

## 2. Exact factorization

For the reduced compressed family

\[
P=\{0,k,M\},\qquad Q=\{1,h,h+1\},\qquad h=\lfloor M/2\rfloor,
\]

write

\[
B_k(r)=r^k-1+\frac{k}{M}(1-r^M),
\]

and

\[
\delta B_k(r)=B_{k+1}(r)-B_k(r)
=r^{k+1}-r^k+\frac{1-r^M}{M}.
\]

Let `beta=1/8`, `target=1/2`, and let `H_M(s)` be the reduced alpha-band coefficient from A81. Define

\[
X=A_*B_k(\beta)-H_\beta B_k(1/2),
\]

\[
Y=-A_*\delta B_k(\beta)+H_\beta\delta B_k(1/2),
\]

\[
W=-B_k(\beta)\delta B_k(1/2)+B_k(1/2)\delta B_k(\beta).
\]

Then the cross numerator factors exactly as

\[
\operatorname{num}D_{M,k}(s)=Z_M(s)E_{M,k}(s),
\]

where `Z_M` is the contact-independent interior-mass numerator and

\[
E_{M,k}(s)=X\delta B_k(s)+YB_k(s)+WH_M(s).
\]

For every audited adjacent pair, `E` has exactly seven nonzero exponents:

\[
\{M,h+1,h,k+1,k,1,0\}.
\]

The seven coefficients are

\[
e_{k+1}=X,\qquad e_k=-X+Y,
\]

\[
e_M=-\frac XM-\frac{k}{M}Y+\frac W2,
\]

\[
e_{h+1}=WH_{h+1},\quad e_h=WH_h,\quad e_1=WH_1,
\]

\[
e_0=\frac XM-\frac{M-k}{M}Y+W\left(\frac12-2\varepsilon\right).
\]

All 1,367 degree-`2M` cross numerators were reconstructed exactly from `Z_M E_{M,k}`.

## 3. Complete local sign atlas

A83 certifies `Z_M(s)>0` on the full local interval for every `M=10,...,80`. Hence the sign of the adjacent objective difference is the sign of the seven-term factor.

Of the 1,367 factors:

- 1,365 are sign-definite on the full interval;
- exactly two have one simple root;
- no same-endpoint-sign factor hides an even number of interior roots.

The two roots are:

\[
M=79,\ k=15,\qquad s\approx0.131138299445625328,
\]

with sign `negative -> positive`, and

\[
M=28,\ k=6,\qquad s\approx0.131364542019008629,
\]

with sign `positive -> negative`.

Thus the compressed maximizing contact changes as

\[
M=79:\quad 15\longrightarrow16,
\]

and

\[
M=28:\quad 7\longrightarrow6.
\]

Away from the two roots, every support has one strict compressed maximizer. At each root, exactly two adjacent contacts tie.

## 4. Discrete concavity is false

At `s0=131/1000`, A83 computed all 1,296 second differences of the compressed objective across `k`:

- positive: 1,141;
- negative: 155;
- zero: 0.

Strict discrete concavity holds for all contacts only for `M=10,...,15`. It fails for every `M>=16` in the audited range.

Therefore strict unimodality is not explained by global discrete concavity. The valid finite mechanism is a single sign variation in the adjacent-difference sequence.

## 5. Boundary of the result

The sparse factorization is an exact algebraic identity under the declared reduced contract. The positivity and sign-atlas theorem remain finite and local. The eight A82 primal-feasibility exceptions

\[
23,28,34,45,51,56,62,68
\]

remain unchanged. Locating the algebraic compressed maximizer does not replace the full KKT check of the lifted branch.

A83 does not establish an all-`M` contact formula, asymptotic periodicity, or a physical interpretation.

## 6. Next rigorous target

A84 should investigate whether the one-sign-variation property can be proved uniformly in `M` by a variation-diminishing or ratio-monotonicity argument for the seven-term factor family. The target must allow failure: finite exact validity through `M=80` is not evidence of an unrestricted theorem.
