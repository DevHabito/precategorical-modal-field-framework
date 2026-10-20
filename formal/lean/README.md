# Lean formalization — Consolidation 1.0

## Assurance qualification: native finite computation

The pinned Lean 4.33.1 development uses `native_decide` in finite enumerations and some witness/semantic checks. In this toolchain, native evaluation carries a compiler-trust axiom. Passing `lake build` and `leanchecker` does **not** imply that those finite computations were reduced by the kernel alone. The project must distinguish kernel-checked deductive lemmas from finite calculations accepted through native evaluation. The descriptions below report the historical CI outcomes, not an axiom-free certification of every theorem.

Run `#print axioms` against each promoted theorem in the pinned environment and record its transitive dependencies. See [the assurance checkpoint](../../consolidation/ASSURANCE_CHECKPOINT_2026-10-19.md) and the [official Lean reference](https://lean-lang.org/doc/reference/latest/ValidatingProofs/). The Lean build and selected axiom-printing commands subsequently passed in GitHub Actions; see [the captured nine-theorem trace](../../consolidation/LEAN_AXIOM_DEPENDENCIES_2026-10-19.md). This does not mean all theorems were proved without native axioms.

This directory is the proof-kernel track for the first Consolidation 1.0 claims. It currently contains end-to-end formal work for **MF-R008 / C1.1** and the explicit witness form of **MF-R009 / C1.2**.

## MF-R008 / C1.1 — representative-code count

The formal chain is deliberately split into independent modules.

`PrecategoryFormal/RepresentativeCount.lean` proves the representative-set combinatorics. For the `(m+1)`-label ground set, the `k`-element representative sets containing label `0` have cardinality

`Nat.choose m (k - 1)`.

It then derives the shifted-binomial fiber identity rather than defining the final theorem by the desired closed form.

`PrecategoryFormal/PosetEnumeration.lean` gives an independent finite enumeration of labeled posets. Each unordered pair has exactly three states — incomparable, lower-to-upper, or upper-to-lower — so antisymmetry is built into the candidate space. On five labels there are exactly `3^10 = 59049` candidates before the transitivity filter. Lean `native_decide` verifies

`p(1),…,p(5) = 1,3,19,219,4231`.

`PrecategoryFormal/PosetSemantics.lean` proves that the decoded relation is reflexive and antisymmetric and that the executable Boolean transitivity checker is equivalent to mathematical transitivity.

`PrecategoryFormal/PosetBijection.lean` constructs an exact equivalence between accepted three-state encodings and Boolean partial-order matrices on `Fin n`.

`PrecategoryFormal/PosetCountBridge.lean` identifies the executable count with the cardinality of the partial-order type and derives the verified five-vertex fiber count `5234`.

`PrecategoryFormal/RepresentativeCodeType.lean` defines an explicit canonical code type, so the fiber-sum formula is a theorem about a finite type rather than a stipulated definition.

`PrecategoryFormal/LiteralRepresentativeCode.lean` closes the carrier-level gap. It transports partial orders across the canonical increasing bijection `Fin k ≃ S`, proves the canonical coordinate code equivalent to the literal published code `(S,P)` where `P` lives on the actual representative set `S`, and proves

`Nat.card (LiteralRepresentativeCode 4) = 5234`.

`PrecategoryFormal/RepresentativeRealization.lean` closes the realizability gap. For every literal code `(S,P)` it constructs an explicit loopless directed graph and proves:

- graph reachability is exactly the order `P` lifted through the representative map;
- mutual reachability is equivalent to equality of representatives, so the SCCs are exactly the representative fibers;
- every selected representative is fixed by the representative map and is the minimum label in its SCC;
- reachability between the selected representatives is exactly `P`.

Thus the counted literal code space is not merely an abstract candidate superset: every counted `(S,P)` pair has a directed-graph realization with the declared SCC-minimum and quotient-order semantics.

No historical Python count is imported into Lean as an axiom.

## MF-R009 / C1.2 — explicit non-injectivity witness

`PrecategoryFormal/RepresentativeCode.lean` formalizes the encoding-level collision:

- a five-vertex minimum-block representation;
- the two explicit A8.1 witness partitions;
- validity of both minimum-representative maps;
- exact historical representative code `100663296` for both witnesses;
- inequality of the two full block assignments;
- non-injectivity of the historical representative-code map.

`PrecategoryFormal/GraphSCCBridge.lean` closes the explicit graph-to-code bridge:

- the two original A8.1 directed graphs are defined by their edge relations;
- directed reachability is defined mathematically as `Relation.ReflTransGen` of the edge relation;
- SCC equivalence is mutual reachability;
- finite path certificates are proved sound for mathematical reachability;
- for each witness graph, mutual reachability is proved equivalent to equality of the proposed SCC minimum map;
- each representative is proved to lie in its SCC and to have minimum vertex label there;
- the quotient of the two SCCs is proved to be an antichain;
- a direct executable reconstruction of the historical A8 representative code reproduces `100663296` for each original graph;
- the direct graph code agrees with the already checked abstract condensation code on both witnesses.

The final theorem `mf_r009_graph_level_code_collision` therefore establishes the explicit MF-R009 counterexample end to end from the two original directed graphs through SCC semantics to the historical code collision.

## Verification status

**MF-R008 declared counting theorem, including literal-code realizability: END-TO-END LEAN/KERNEL PASS.**

**MF-R009 explicit witness: END-TO-END LEAN/KERNEL PASS.**

The repository CI uses pinned Lean `v4.33.1` / mathlib `v4.33.1`, rejects `sorry`/`admit` proof placeholders, and runs a complete `lake build`. The bundled `leanchecker` is then run separately for every project module. The checker stage is intentionally sharded across CI runners: this changes only scheduling, not the replay obligation, and prevents runner lifetime limits from masking the independent kernel replay.

The MF-R008 small-poset values are exact finite computations discharged with Lean `native_decide`; they are not presented as a new analytic formula for the poset-count sequence.

## MF-R049 / C2 — exact dynamic nonclosure

The historical irrational four-point witness is preserved outside this
formalization. A second witness was constructed **analytically**, not fitted
from numerical data, from the signed moment polynomial
`(t - 1)^2 * (t - 1/4) / 8`.

- `PrecategoryFormal/DynamicNonclosure.lean` proves positivity,
  normalization, equal weighted means, equal initial exponential moments,
  and an exact nonzero rescaled-moment difference for two rational vectors.
- `PrecategoryFormal/DynamicNonclosureTransport.lean` starts from the
  **actual four-term exponential sum** after an affine update; proves its
  factorization; applies the centered contraction; and uses strict
  positivity and logarithm injectivity to prove the next scores differ.
- The final theorem `rationalScalarNonclosure` combines equal initial
  mass, mean, and fixed-parameter score with unequal next scores.

The pinned Lean 4.33.1 build and the five selected C2 `#print axioms`
commands passed in
[CI run 39337980598](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39337980598).
The two new modules also passed their independent `leanchecker` replays.
None of the five selected theorems depends on a `native_decide` axiom:
their printed dependencies are the standard Lean logical axioms
`propext`, `Classical.choice`, and `Quot.sound`.

This proves only a scoped four-point existence counterexample; it does
not rule out closure on restricted families, certify novelty, or establish
physical dynamics. Full derivation:
[Consolidation F3](../../consolidation/F3_RATIONAL_NONCLOSURE_2026-10-19.md).

## A113 / C3 — algebraic small-left bridge (in progress)

`PrecategoryFormal/A113SmallLeftBridge.lean` is a **scoped formalization** of
part of the clean-room A113 review. It defines the A83 cofactor factor
using independent moment slopes and derives the A84 ten-term expression
by a universally quantified polynomial identity. It also checks the
zero-unit comparison core, the exact positive first/second-contact
identities, and the frozen rational core-versus-error threshold.

The theorem `contactA113SmallLeftPositive_of_analyticEnvelopes` is
**conditional**: its premises explicitly include the positive core
lower bound, the uniform absolute remainder bound and the unit bound.
It does not establish those three inequalities for the actual
`M>=521`, `2<=k<=29` exponential-moment parameters. Passing an axiom
trace or Lean compilation of this implication does **not** close the
unconditional uniform small-left A113 theorem.

The separate mathematical proof is recorded in
[`A113_SMALL_LEFT_UNIFORM_PROOF_2026-10-19.md`](../../consolidation/A113_SMALL_LEFT_UNIFORM_PROOF_2026-10-19.md),
with a 60-case rational regression script. The next formal task is to
prove the actual core lower bound for all contacts and then derive the
A84 H/slope/error estimates in Lean, not to convert those obligations
into assumptions hidden under reassuring theorem names.

As with all new modules, the final proof status must be grounded in the
actual pinned GitHub Actions `lake build`, `#print axioms`, and
`leanchecker` results for the **exact head commit**, not inferred from a
previous passing run.

## A113 / C3 — unconditional ideal-core bound (2026-10-20)

`PrecategoryFormal/A113IdealCoreUniform.lean` proves the exact ideal-core
recurrence for all natural contacts, proves its correction term is
nonnegative for ordered nonnegative nodes, and derives a lower bound
by induction. In the frozen window `s in [129/1000,133/1000]`, the
result gives the required rational bound `L <= contactIdealCore k`
for every `2<=k<=29`, without assuming any A113 numerical result.

The pinned Lean 4.33.1 build, selected `#print axioms` commands and
the dedicated `leanchecker` for this new module passed in
[formal run 39403579662](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39403579662).
The five selected theorem traces contain only `propext`,
`Classical.choice`, and `Quot.sound`, with no native computation axiom.
Two other checker jobs initially failed because their separate runners
could not download the Lean toolchain (TLS connection errors); this is
not a proof failure for the ideal-core module, but the full matrix
needs those jobs rerun before it can be called green.

`contactA113SmallLeftPositive_of_error_and_unit` now needs the
**actual-to-ideal remainder bound and unit bound** as assumptions;
the universal ideal-core lower bound is a proved lemma. No theorem
has yet established that the frozen `D_M`/`H_r` channels satisfy
the remainder assumptions for all `M>=521` and all real sources.
Therefore the original complete A113 small-left positivity theorem
is **still unproved in Lean**.

Proof derivation and exact scope:
[ideal-core recurrence checkpoint](../../consolidation/A113_IDEAL_CORE_RECURRENCE_2026-10-20.md).

## A113 / C3 — finite parity channels and dyadic denominator proof (2026-10-20)

`PrecategoryFormal/A113FiniteChannels.lean` now defines the actual finite-`M`
historical normalization. It keeps the even and odd `D_M(r)` expressions
separate, chooses `epsilon_M=U_M/1875` or `U_M/2500` by parity,
and encodes the critical `+2 epsilon_M` beta and `-2 epsilon_M`
source adjustments. The real A83 cofactor is constructed from these
parameters without replacing it by the ideal core.

The theorem `a113Unit_le_boundary` proves
`M>=521 -> U_M<=1/2^260`. A geometric induction proves
`a113Denominator_ge_three_quarters` and therefore positivity of
`d_M=1-(floor(M/2)+1)*U_M`. Theorems also check the opposite-channel
difference and exact A83/A84 ten-term algebra. These claims compiled
in the pinned Lean run
[39425842288](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39425842288).
The selected axiom traces report only `propext`, `Classical.choice`
and `Quot.sound`, without native-computation axioms.
Check the dedicated independent `leanchecker` result separately.

The actual-factor sign theorem is still **conditional on the
unproved uniform real-finite remainder bound**
`|a113ActualFactor M k s - contactIdealCore k 1/8 1/2 s|<20*U_M`.
This checkpoint does not prove that bound or close all of A113.
Derivation and scope:
[finite channel checkpoint](../../consolidation/A113_FINITE_CHANNELS_LEAN_CHECKPOINT_2026-10-20.md).

## A113 / C3 — exact geometric defect envelopes (2026-10-20)

`PrecategoryFormal/A113DefectEnvelopes.lean` proves, for every
`M>=521` and real `0<=r<=1/6`, that
`r^floor(M/2)<=U_M/128` and
`r^(floor(M/2)+1)<=U_M/768`. It also proves
`floor(M/2)*U_M<=1/4` and the normalized coefficient
`floor(M/2)*U_M/d_M<=1/3`, with exact rational induction
and no floating-point extrapolation.

The even/odd triangle-inequality steps are now formally proved in
`PrecategoryFormal/A113DefectSigns.lean`. The Lean theorems establish
`|D_even(r)|<U_M/2`, `|D_odd(r)|<U_M/2`, and the combined parity claim
`|D_M(r)|<U_M/2` for every integer `M>=521` and real `0<=r<=1/6`.
The pinned build, selected axiom trace and dedicated `leanchecker`
succeeded in [run 39456447948](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39456447948).
The selected axiom dependencies are `propext`, `Classical.choice`,
and `Quot.sound`, without `native_decide`. The exact `11/24`
and `175/512` estimates are intermediate algebraic calculations,
not separately exported theorem statements.

The corresponding H-channel deviations have since been formally proved
in `PrecategoryFormal/A113HEnvelopes.lean`. The theorem proves, for all
`M>=521`, both the general Boolean-corrected deviation bound
`|H_M(r,channel)-1/2|<U_M` for real `0<=r<=1/6`, and the
specific historical positive beta and negative source bounds for
`beta=1/8` and `s in [129/1000,133/1000]`.

Pinned [Lean Actions run 39463059505](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39463059505)
at source revision `68391595cd64a082496f488b59744bd63b95dd7c`
passed the build, five selected axiom traces and isolated
`leanchecker (PrecategoryFormal.A113HEnvelopes)`.
The traces list only `propext`, `Classical.choice`, `Quot.sound`;
no `native_decide` dependency was found for these theorems.

The **complete actual-to-ideal A113 remainder**
`|E_(M,k)-F_k|<20U_M` remains unproved in Lean. Formalized H bounds
do not by themselves prove the A113 sign. See the
[H-envelope checkpoint](../../consolidation/A113_H_ENVELOPES_FORMAL_CHECKPOINT_2026-10-20.md)
and [formal defect checkpoint](../../consolidation/A113_DEFECT_SIGNS_FORMAL_CHECKPOINT_2026-10-20.md).

## A113 / C3 — target normalization and moment slopes (2026-10-20)

The new `PrecategoryFormal/A113MomentEnvelopes.lean` proves the exact
finite-M target and slope bounds for every integer `M>=521` and
every real `0<=r<=1/2`. It establishes
`|A_M-1/2|<=U_M/2`, `1/2<=A_M<=1`,
`0<=a_M(r)<=1/M` and `|a_M(r)-1/M|<=U_M/M`.
For the beta/source nodes `r<=1/6` it sharpens the slope error to
`U_M/(128*M)`, without redefining the original moment slope.

The pinned Lean 4.33.1 `lake build` and seven selected axiom traces
passed at code commit `3dd0525f9bc9644f71be51e775aab3829cfb8562`
in [formal run 39466591437](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39466591437).
The printed axiom dependencies are only `propext`,
`Classical.choice` and `Quot.sound`. The dedicated
`leanchecker (PrecategoryFormal.A113MomentEnvelopes)` subsequently
passed, and the complete 26-job matrix finished green, in
[run 39467407162](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39467407162),
at commit `b77745052bbb716ae67cd69784cb702ebe168dea`. 

An independently written standard-library Fraction replay also passed
30 size/node controls in [audit run 39466979975](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39466979975).
Sampling is only a regression check, not a proof of the universal
quantifiers. The A84 affine/linear/constant perturbation bounds and
`|E-F|<20U_M` remain formally open. See the
[target and slope checkpoint](../../consolidation/A113_TARGET_AND_MOMENT_ENVELOPES_2026-10-20.md).

## A113 / C3 — first bilinear channel coefficient bounds (2026-10-20)

`PrecategoryFormal/A113BilinearEnvelopes.lean` encodes the actual three
A84 bilinear channel products `A*a_s-H_s*a_tau`,
`A*a_beta-H_beta*a_tau` and `H_beta*a_s-H_s*a_beta`.
For every integer `M>=521` and source `129/1000<=s<=133/1000`,
the source proves a `3*U_M/M` absolute cap on each expression using
the earlier formally checked H, target-mass and slope deviations.

The first root-import builds **failed** on proof-assembly errors
(an unclosed rational equality and incorrect triangle-inequality
orientation). These were fixed in source commit
`2a5a99bcfca63d4cf0cb23153fbddc72772b3f9e`
without adjusting the assumptions or statements. The pinned corrected
[formal run 39487978993](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39487978993),
selected axiom trace and independent
`leanchecker (PrecategoryFormal.A113BilinearEnvelopes)` must complete
successfully before certifying the new module. Earlier passing builds
before the root import did not validate these new declarations.
An independent exact-rational script was added to the audit workflow
to regress the affine, linear, constant and E/F envelopes at sampled
size/source/contact values; these checks are not universal proofs.

This is a component of, **not** a substitute for, the open uniform
`|E_(M,k)(s)-F_k(s)|<20*U_M` bound. See the
[bilinear checkpoint](../../consolidation/A113_BILINEAR_COEFFICIENT_CHECKPOINT_2026-10-20.md).

## Deliberate nonclaims

The MF-R008 formalization proves the declared representative-code counting theorem and the realizability of every counted literal code. It does **not** retain or count discarded SCC membership assignments as part of the code, make the representative code injective, establish novelty/priority, or imply anything physical.

For MF-R009, `ReachWithinBool 4` is used as an executable bounded-path evaluator for the two concrete five-vertex witnesses. We have proved its equivalence with the corresponding bounded proposition and proved bounded certificates sound for mathematical reachability.

We have **not** yet proved the reusable general theorem that every `Relation.ReflTransGen` path in every five-vertex directed graph can always be reduced to a path of length at most four. Therefore `witnessGraphRepresentativeCode4` is not yet promoted as a verified generic encoder for arbitrary five-vertex graphs.

This limitation does not weaken the explicit MF-R009 witness theorem: the exact SCC partitions, minimum representatives, absence of cross-SCC reachability, quotient antichain structure, and the two direct code values are all independently established for the two concrete graphs.

## Build

```bash
cd formal/lean
lake build
```

The committed `lake-manifest.json` pins the resolved dependency revisions used by CI.
