# Notation and terminology: A115–A122

*Working dictionary — 6 November 2026*

This dictionary belongs to the target-deformation study. Its purpose is to make the paper readable without relying on internal labels or changing definitions halfway through a calculation. Notation is taken from A115, A117, A118 and A122, and from the Lean modules linked below. Where the same symbol was used in different ways in the source notes, that ambiguity is recorded rather than concealed.

## The finite problem

| Symbol | Meaning | Domain or caution |
|---|---|---|
| `M` | Upper support index; support is `{0,…,M}` | Positive integer; central three-site formulas use `M ≥ 4` |
| `x` | Support coordinate | Integer between 0 and M |
| `p_x, q_x` | Nonnegative, non-normalized weights of two measures | Not the parity index `p` |
| `t` | Common total mass of the scaled weights | `sum_x p_x = sum_x q_x = t`; positive for probability normalization |
| `mu_x, nu_x` | Probability weights `p_x/t, q_x/t` | Requires `t>0` |
| `G_mu(r), G_nu(r)` | Transforms `sum_x mu_x r^x`, `sum_x nu_x r^x` | `0<r<1` in this study |
| `beta (β)` | Reference transform node | Frozen at `1/8` |
| `delta (δ)` | Scale-normalized tolerance constant | Frozen at `1/1875` |
| `s` | Moving source node | Frozen window `[129/1000,133/1000]` |
| `tau (τ)` | Target transform node | Variable; collision and fixed-interior studies use distinct regimes |
| `epsilon_{τ,M}` | Absolute tolerance for the deformed target normalization | `δ τ^h` for even M; `δ(1+τ)τ^h/2` for odd M |
| `h` | Central integer index `floor(M/2)` | Natural number; `M=2h` or `2h+1` |
| `u`, `u_M` | `τ^h` | Not the probability measure `nu` |
| `Q` | Central support `{1,h,h+1}` | Support of one three-site block; *not* the full feasible LP |
| `q_1,q_h,q_{h+1}` | The weights of the central Q block | Their exact nonnegativity interval is Lean-certified |
| `D_τ` | Central denominator `τ-hτ^h+(h-1)τ^(h+1)` | Positive when `h≥2, 0<τ<1` |
| `B_{M,k}(r)` | Moment-adjusted basis `r^k-(M-k)/M-(k/M)r^M` | `M>0`, integer `k` in the finite model |
| `ΔB_{M,k}(r)` | Adjacent difference `B_{M,k+1}(r)-B_{M,k}(r)` | Equals `(r-1)r^k+(1-r^M)/M` |
| `H_β,H_s` | Cofactor/band quantities from the reduced A115 factor | Do not treat as independent LP feasibility certificates |
| `X,Y,W` | Cofactor coefficients of `ΔB_s,B_s,H_s` | In the source, `E=X ΔB_s+Y B_s+W H_s` |
| `E_{M,k}` | Reduced adjacent factor used for local sign analysis | Its cofactor and ten-channel forms are algebraically equivalent |
| `J_{τ,k}` | Transformed adjacent factor `E_{M,k}-τ^(-1)E_{M,k+1}` | Requires `τ>0`; keep the same M and s |
| `b_M` | Contact locator `ceil(M log τ/(2 log s))` | Also characterized by exact integer power comparisons |

## The collision regime: A116–A119

Here the target moves with M: `τ_M=s+λ/M`, with `λ>0`.

| Symbol | Meaning |
|---|---|
| `λ` | Fixed collision separation scale |
| `L` | `-log s>0` |
| `α` | `λ/(2s)` |
| `σ_p` | Parity shift: 0 for even M; 1/2 for odd M |
| `a_p(s)` | Parity amplitude: 1 for even M; `(1+s)/2` for odd M |
| `r` **(contact deficit)** | Eventual integer `h-b_M`; *not* the transform argument also called r in `B_{M,k}(r)` |
| `k_M` | Collision contact `b_M+1=h-r+1`, once the deficit stabilizes |
| `N_M` | Normalized transformed factor `J_{τ_M,k_M}/(τ_M^h τ_M^{k_M})` |
| `Λ_p` | First-order coefficient in `N_M=Λ_p/M+…` |
| `Ξ_p` | Second-order coefficient in `N_M=Λ_p/M+Ξ_p/M²+o(M^-2)` |
| `q=e^{-α}` | Exponential abbreviation in A117–A119 | **Not** a central weight `q_x` |

The exact rational interval certificate in A119 proves positivity for the **published expression after substitution on the critical surface**. The entire substitution from the original LP is a separate proof obligation.

## The fixed-interior rounding regime: A120–A122

Here `s` and `τ` are fixed, with `s<τ<β/s<1`. Do not use a collision-layer parity amplitude here.

| Symbol | Meaning |
|---|---|
| `c` | `log τ/(2 log s)` |
| `ρ_M` | `b_M-Mc`, the rounding phase in `[0,1)` |
| `j` | Fixed integer contact offset |
| `k_M` | `b_M+j` |
| `x_M` | `j+ρ_M=k_M-Mc` |
| `σ_p` | Parity shift: 0 even, 1/2 odd |
| `a_p(τ)` | Parity amplitude: 1 even, `(1+τ)/2` odd (**not** `a_p(s)`) |
| `G` | `(s-β)/τ-4δ`, positive under A122's stated domain |
| `P_p` | `(τ-s)τ^σ_p/2` |
| `Q_p` | `a_p(τ)(1-τ)G(1-c)` | **Not** the central support Q |
| `Φ_p(x)` | `P_p s^x-Q_p` |
| `ξ_p` | `log(Q_p/P_p)/log s`, root of `Φ_p` |
| `Ω_p(x)` | `a_p(τ)G[1+(1-τ)x]` |
| `𝒩_{M,j}` | Normalized factor `E_{M,k_M}/(τ^h τ^{k_M})` |
| `R_{M,j}` | Remainder in `𝒩=Φ_p(x_M)+Ω_p(x_M)/M+R` |

**Name collision:** the scripts sometimes use `B`, `C`, `D`, `A`, `q`, `r` as local algebra variables. Those are not globally stable symbols. Read them from the relevant formula, not from this global dictionary.

## Status vocabulary

- **Lean-checked:** this exact statement compiled and passed individual Leanchecker kernel replay on an identified commit.
- **Exact computational check:** a finite execution with integer or rational arithmetic; it does not prove a statement for untested parameters.
- **Interval certificate:** finitely many rational enclosures with proved containment, contingent on the correctness of the formula being enclosed.
- **Source theorem:** a claim in the project's A-series manuscript; it is not automatically independently reconstructed or Lean-checked.
- **Novelty not certified:** no systematic claim of priority over the literature is made.

## Primary project definitions

- [A115 mathematical source](../../MFRP_Informational_Requirements_A39-A109/research_updates/A115/A115_TARGET_NODE_DEFORMATION_EXACT_AUDIT_20260914.md)
- [A117 collision definitions](../../MFRP_Informational_Requirements_A39-A109/research_updates/A117/A117_BOUNDARY_LAYER_PHASE_CLASSIFICATION_THEOREM_20260915.md)
- [A118 second-order expansion](../../MFRP_Informational_Requirements_A39-A109/research_updates/A118/A118_SECOND_ORDER_CRITICAL_LAYER_THEOREM_20260915.md)
- [A122 rounding phase](../../MFRP_Informational_Requirements_A39-A109/research_updates/A122/A122_NEAR_RESONANT_ROUNDING_LAYER_THEOREM_20260915.md)
- [Lean central and feasibility lemmas](../../formal/lean/PrecategoryFormal/TargetDeformationAudit.lean)
- [Lean ten-channel identity](../../formal/lean/PrecategoryFormal/TargetFactorTenChannel.lean)
- [Lean finite-basis bridge](../../formal/lean/PrecategoryFormal/TargetFactorBasisBridge.lean)

## Primal-to-factor formalization additions (November 6)

| Symbol | Meaning | Scope |
|---|---|---|
| `z` | Scaled mass `p_k` at the movable P support point `k` | In the three-site P support `{0,k,M}`, with `0<k<M` |
| `p_0,p_M` | Endpoint masses forced by total mass `t` and mean `M/2` | `p_M=t/2-(k/M)z`; `p_0=t/2-((M-k)/M)z` |
| `transform M w r` | Finite, unnormalized transform `sum_{x=0}^M w_x r^x` | Definition in `TargetPrimalBridge.lean` |
| `leftEndpoint,rightEndpoint` | Lean definitions of the two solved endpoint masses | Algebraic real weights; their nonnegativity is not implicit |
| `Matrix.det` for the factor | Oriented determinant with rows `(B_beta,B_tau,B_s)`, `(H_beta,A,H_s)`, `(DeltaB_beta,DeltaB_tau,DeltaB_s)` | Its identification with E is algebraic; KKT sign is a distinct obligation |

The source of these additions is [A115 Primal-to-Basis Bridge](../formal/A115_PRIMAL_TO_BASIS_BRIDGE_20261106.md). Keep the P support `{0,k,M}` distinct from the Q support `{1,h,h+1}`.

## The compressed active-band system and sign convention (7 November)

| Symbol | Definition | Caution |
|---|---|---|
| `C_r` | Constant term of the central-Q transform `Q_r=C_r+D_r*t` | Not the target factor `C` used as a local variable in A119 |
| `H_beta` | `A_beta-D_beta+2*epsilon` for the **beta-lower** active band | The plus sign comes from `P_beta-Q_beta=-2*epsilon*t` |
| `H_s` | `A_s-D_s-2*epsilon` for the **s-upper** active band | The minus sign comes from `P_s-Q_s=+2*epsilon*t` |
| `Delta_k` | `B_beta(k)*H_s-B_s(k)*H_beta` | **Our** orientation; it is the negative of A81's determinant coefficient |
| `Z` | `C_beta*H_s-C_s*H_beta` | **Our** orientation; it is the negative of A81/A83's positive interior-mass numerator |
| `Z_source` | `C_s*H_beta-H_s*C_beta=-Z` | Use this to read A83's `Z_source*E` factorization correctly |
| `N_k` | `A_tau*(B_beta(k)*C_s-B_s(k)*C_beta)+B_tau(k)*Z` | Cramer numerator of the actual scaled target objective |
| `V_k` | `N_k/Delta_k=A_tau*t_k+B_tau(k)*z_k` | Exact rational objective, not merely its sign factor |

The factor identity is `(V_(k+1)-V_k)*Delta_k*Delta_(k+1)=-Z*E_(M,k)`. The signs are the same when `Z<0` and `Delta_k*Delta_(k+1)>0`. See [the source-level and Lean analysis](../formal/A115_COMPRESSED_ADJACENT_OBJECTIVE_IDENTITY_20261107.md).
