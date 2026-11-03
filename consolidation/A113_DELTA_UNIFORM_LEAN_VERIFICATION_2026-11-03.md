# A113 source-minus-beta Delta: uniform Lean-verified bound

**Research author:** Felipe Gianini Romero  
**Date verified:** 3 November 2026  
**Code revision:** `b720be0ae1366a50e4a4a9fd4b06b90f87809c2f`  
**Full regression:** [GitHub Actions 41727101617](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41727101617) — **SUCCESS**.  
**Scope:** the two finite-size H channels in the frozen A113 source interval. This is **not** the full A113 one-variation theorem.

## The exact result I can now defend

Let `M` be a natural number with `M>=521`, `s` an arbitrary **real** number in the **closed** interval `[129/1000,133/1000]`, `h=floor(M/2)`, `U=2^-h`, `beta=1/8`, and `epsilon_M` the historical even/odd tolerance. Use precisely the original finite-M channel definitions in `PrecategoryFormal.A113FiniteChannels`:

    H_s = (1+s^M)/2 - D_M(s) - 2 epsilon_M,
    H_beta = (1+beta^M)/2 - D_M(beta) + 2 epsilon_M.

Then:

    43/10000 < (H_s-H_beta)/U < 7/500.

The final declarations are:

- `PrecategoryFormal.a113Delta_uniform_interval`
- `PrecategoryFormal.a113H_sourceBeta_gap_uniform_interval`

Neither takes the desired Delta inequality as a premise. These are **universally quantified** results over the stated integers and real interval; finite sampling did not supply the universal quantifier.

## Where the proof comes from

I did not substitute an idealized H function or force the margins by assuming the conclusion. The proof is deliberately split into units that can fail independently.

1. **Denominator and dyadic scale.** `A113DeltaPreliminaries.lean` proves `d=1-(h+1)U>=999/1000` for every admissible M, and `r^h<=U/10^6` for every `0<=r<=1/6`. The estimates come from monotone geometric induction with exact rational base cases; no chosen grid of M values appears in the proof.
2. **One-sided power differences.** `A113DeltaPowerGaps.lean` controls the actual, nonnegative `(s^n-beta^n)/U` at `n=h,h+1,M`, each no larger than `10^-6`. The sign follows from `beta<=s`, not an absolute-value shortcut.
3. **Strict rational budgets.** `A113DeltaScalarBudgets.lean` proves even- and odd-parity implications from explicit bounds `0<=P<=1/(2*10^6)`, `0<=Q,R<=1/10^6`, `0<=X,Y<=1/3`, and `999/1000<=d<=1`. The actual available exact margins were checked separately with Python `Fraction` arithmetic.
4. **Actual source definitions.** `A113DeltaParityIdentities.lean` proves that both scalar expressions are *equal* to the original finite-M H gap under their respective parities. The target source/beta epsilon adjustments have the intended opposite signs; they were not swapped to make the bound work.
5. **Final composition.** `A113DeltaUniform.lean` invokes the preceding lemmas, the earlier Lean proof `a113HalfCoefficient_div_denominator_le_third`, and the integer half-index inequality. It proves the strict interval for both parities under only the source and size contract.

The main theorem source is [A113DeltaUniform.lean](../formal/lean/PrecategoryFormal/A113DeltaUniform.lean); the complete root import makes it part of the pinned project build.

## What the exact GitHub log says

I inspected the completed job logs, not merely the GitHub status badge. At the exact source revision `b720be0ae1366a50e4a4a9fd4b06b90f87809c2f`:

- Lean 4.33.1 compiled the complete pinned project and reported **8,742 jobs built successfully**.
- The forbidden-placeholder gate found no `sorry` or `admit` in the Lean source.
- All **35 distinct modules** completed `leanchecker`; the log includes `PASS PrecategoryFormal.A113DeltaUniform`.
- `#print axioms` for both new universal Delta theorems reports exactly `[propext, Classical.choice, Quot.sound]`.
- No `native_decide` axiom or `sorryAx` appears in the reported dependency lists of these two theorems.

The last qualification is specific to these statements. Older finite graph enumeration results elsewhere in this repository continue to carry their documented native-computation trust dependencies. A green full-module check does not change that fact.

### Adversarial and failure history

The first power-gap Lean attempt [41725088460](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41725088460) failed while rewriting `node^M`. `rw [hsplit,pow_add]` also rewrote a nested `M` inside `floor(M/2)`, leaving an unsolved goal. The later 33-module build at [41725479992](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41725479992) inherited that same error. I preserved the raw diagnostic in [the dated failure note](A113_DELTA_POWER_GAPS_FIRST_BUILD_FAILURE_2026-11-03.md).

The correction was a scope-limited use of `congrArg` followed by `pow_add`. No statement, coefficient, constant or hypothesis was changed. The fixed code later compiled in [41725671300](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41725671300). Subsequent complete checks passed at [33 modules](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41726163238), [34 modules](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41726508195), and finally [35 modules](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41727101617).

This failure remains a **FAIL** in the research history; it is not retroactively converted into a passing run.

### Independent exact computations

The separate [Python CI 41724713362](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41724713362) passed the symbolic/finite tests and exact even/odd Delta margin arithmetic, including two negative controls. The most restrictive scalar lower margin is the odd-parity one:

    odd lower = 8797/2000000,
    odd lower - 43/10000 = 197/2000000 > 0.

The independent 21-point parity/source check also passed in [41722823626](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41722823626). These are independent tests of subclaims, **not** a substitute for the mathematical proof or a second Lean implementation.

## Exactly what remains unresolved

This closes the **normalized H-channel Delta interval**. It does **not** prove:

- `J=E_(b+1)-2E_(b+2)>0` for the central contacts;
- the full middle-left or remote-right factor signs;
- the global compressed A113 sign-variation or maximizer claim;
- the lifted A112/A114 primal/dual/KKT cases and equality boundaries;
- recovery of the three previously identified malformed historical A112/A113/A114-A ZIP containers;
- a physical law, a model of spacetime, an astronomical prediction, or originality against the mathematical literature.

The next mathematical engineering obligation is to connect the *exact* central-pair factor in `A113CentralPairIdentity.lean` to the logarithmic contact threshold `b(M,s)` and derive quantitative bounds for the remaining transformed affine channels and `eta`. The recovered A113 source lists `J`-margin arithmetic gates; their positivity as numbers is not enough without universal bounds from the original factor.

## Literature boundary

The analytic setting is part of an established body of work on moment spaces, Chebyshev systems and linear-programming extreme points. See the bibliography and explicit limits of its priority comparison in [the C3 adversarial audit](C3_A110_A114_ADVERSARIAL_CHECKPOINT_2026-10-19.md): Samuel Karlin and William J. Studden (1966), *Tchebycheff Systems*; Gerhard Winkler (1988), “Extreme Points of Moment Sets”; and András Prékopa (1990), “The Discrete Moment Problem and Linear Programming.” Those references precede this research's broad mathematical techniques. I have **not** established that they do or do not contain an equivalent theorem for this frozen Delta expression.

**Research status:** a scoped formal theorem has been verified with the disclosed Lean axioms. No unverified physical, originality or all-tail claim is promoted here.
