# A113 small-left: exact remainder assembly and verification boundary

**Date:** 2026-11-03  
**Research author:** Felipe Gianini Romero  
**Baseline:** audit/2026-10-19-trust-and-integrity at \`8beff0808bf29c9d11467cd76a8b50a1c74a4174\`  
**Status:** mathematical assembly from named, previously formalized estimates; independent symbolic and rational tests passed; **new Lean source not compiled or kernel-replayed**.

## Why I returned to this question

The earlier small-left argument gave a useful route to positivity, but the Lean source still stopped short of assembling the complete finite-size remainder bound. I returned to that gap rather than opening another chronological A-number package. This note records exactly what I checked, what I derived from existing lemmas, and what is still missing.

The frozen contract is:

- integer M >= 521;
- integer 2 <= k <= 29;
- real 129/1000 <= s <= 133/1000;
- beta = 1/8 and tau = 1/2;
- h = floor(M/2), U = 2^(-h);
- E = a113ActualFactor M k s, with parity-specific source/beta channels;
- F = contactIdealCore k (1/8) (1/2) s.

The next formal target is:

    |E - F| < 20 U, and consequently E > 0.

The statement has no physical units or empirical interpretation.

## Definitions and direct provenance

I read the following exact source files at the baseline revision:

- \`formal/lean/PrecategoryFormal/A113FiniteChannels.lean\` — actual finite-M factor, parity, epsilon and U;
- \`formal/lean/PrecategoryFormal/A113SmallLeftBridge.lean\` — symbolic A83/A84 cofactor identity and conditional positivity;
- \`formal/lean/PrecategoryFormal/A113IdealCoreUniform.lean\` — uniform ideal-core lower bound;
- \`formal/lean/PrecategoryFormal/A113HEnvelopes.lean\` — beta/source H bounds;
- \`formal/lean/PrecategoryFormal/A113MomentEnvelopes.lean\` — target-mass and slope bounds;
- \`formal/lean/PrecategoryFormal/A113BilinearEnvelopes.lean\` — bilinear channel bounds;
- \`formal/lean/PrecategoryFormal/A113CoefficientEnvelopes.lean\` — coefficient bounds;
- \`formal/lean/PrecategoryFormal/A113CoefficientIdentity.lean\` — exact named-coefficient decomposition.

The previous analytic argument is preserved in \`consolidation/A113_SMALL_LEFT_UNIFORM_PROOF_2026-10-19.md\`. This checkpoint does not replace or rewrite that source.

## Mathematical deduction from existing source lemmas

The named-coefficient identity decomposes E-F into three product-channel deviations, three affine-linear channels and a constant:

    (A-1/2)(s-beta)(beta*s)^k
    + (H_s-1/2)(beta-tau)(beta*tau)^k
    + (H_beta-1/2)(tau-s)(s*tau)^k
    + (c_beta+k*d_beta)*beta^k
    + (c_s+k*d_s)*s^k
    + (c_tau+k*d_tau)*tau^k + c_1.

The displayed hypotheses here are **already theorem conclusions in the imported source modules**, not hypotheses I am introducing to make the answer work:

- |A-1/2| <= U/2;
- |H_s-1/2| < U and |H_beta-1/2| < U;
- |c_r| < 5U for each of the three affine coefficients;
- |d_r| <= 3U/M for each linear coefficient;
- |c_1| <= 6U/M.

Throughout this contract, the three node differences have absolute value at most one, and all node powers in the expansion lie in [0,1]. The triangle inequality therefore gives the conservative upper bounds

    product deviations <= 3U
    affine coefficients  < 15U
    linear coefficients  <= 9k U/M
    constant coefficient <= 6U/M.

Combining them yields

    |E-F| < (18 + (9k+6)/M) U.

Because M >= 521 and k <= 29, both positive integers,

    18 + (9k+6)/M <= 18 + 267/521 = 9645/521 < 20.

The separate ideal-core module proves F >= L for the same real-source and integer-contact range, where

    L = (1/2)*(129/1000-1/8)*(1/2-1/8)
        *(1/2-133/1000)*(129/2000)^28
      > 20/2^260.

The finite-channel module proves 0 < U <= 1/2^260 for M >= 521. Thus F > 20U > |E-F|, and E > 0 follows.

**What this establishes now:** a written, explicit assembly of the desired implication from the named source estimates, with exact arithmetic and without a new numerical fit. **What it does not establish now:** successful Lean elaboration or checker replay of that assembly. The correctness and independence of imported mathematical statements remain matters for theorem-level audit.

## Recomputed evidence (this session)

The standalone files in \`tools/research_2026_11_03/\` were run locally under Python 3.13.5 with SymPy 1.14.0:

1. \`pmff_independent_audit_2026-11-03.py\` checked the rational F3 witness, cubic identity, a negative control, the A113 generating-function identity and exact margin constants.
2. \`pmff_a113_independent_remainder_2026-11-03.py\` checked the A83/A84 expansion symbolically for arbitrary algebraic parameters, rejected a deliberate sign mutation, and passed 60 exact rational cases: M in {521,522,561,661}, s in {129/1000,131/1000,133/1000}, k in {2,3,7,15,29}.
3. \`pmff_a113_all_contacts_2026-11-03.py\` checked 336 exact rational cases on the same M/s grid with every integer k=2,...,29, including coefficient bounds, factor identity, error cap and positivity.

The third script imports the second script's local exact-model functions using \`runpy\`; these are **not independent implementations of all numerical components**. The 60 tested configurations are included in the 336-grid. No floating-point tolerance decides any assertion. The saved logs correspond to the local re-execution on this date, not a newly observed GitHub Actions run.

Finite tests do not prove all-M/all-real-s bounds. The universal claim rests on the mathematical derivation and the Lean lemmas, and the new Lean joining theorem has not yet been checked.

## Lean candidate, not a promoted theorem

\`consolidation/candidates/A113SmallLeftClosure.candidate.lean\` is a 215-line draft based on the existing module names. I have deliberately left it outside \`formal/lean/\` and outside the root import list, so that nobody will mistake an unchecked file for a certified project module.

To promote it, I must first:

1. place a **copy** in the formal Lean module tree on an isolated review branch and add the corresponding root import;
2. use the committed \`leanprover/lean4:v4.33.1\` toolchain and pinned mathlib manifest;
3. run \`lake build\`, the existing proof-placeholder gate, \`#print axioms\` for the two candidate declarations, and module-specific \`leanchecker\`;
4. preserve failures, make only justified proof corrections, and run the full regression/checker matrix;
5. compare the final formal statements back to A83/A84 definitions, including beta/source sign orientation.

The prior workflow at https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39491064741 reported 29 successful jobs at revision \`9f38572c9114dc9b6412a6faa0d1928107e11f5a\`. That is previous evidence for the imported modules, **not** a new successful run of this candidate or proof of the entire repository.

## Open questions and unrelated blockers

- The candidate's Lean elaboration, tactic correctness and transitive axiom trace are untested.
- A113's middle-left, remote-right and central sectors have separate proof obligations. The small-left result cannot silently close them.
- A112-G, A112-B and other global optimization statements remain subject to their own independent audits.
- The historical A112, A113 and A114-A ZIP-package problems recorded in \`consolidation/HISTORICAL_ZIP_INTEGRITY_FINDING_2026-10-19.md\` remain unresolved. No archive, historical checksum or original source is modified here.
- Root integrity indexes must be refreshed from a clean checkout and independently checked before this branch can be merged.
- Neither the mathematical formula nor passing tests implies a theory of physical spacetime, astrophysics or observed dynamics.
- This note does not claim novelty or priority; see the dated literature record in \`docs/novelty/VERIFIED_CONTEXT_2026-11-03.md\`.

**Next decision:** require an actual Lean build and axiom/checker trace for the isolated candidate. If the proof fails, record the failure precisely rather than weaken the statement or substitute a favorable sample.
