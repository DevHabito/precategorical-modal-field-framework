# A80–A114 longitudinal scientific audit — 2026-09-13

## Verdict

**PASS WITH EXPLICIT HISTORICAL REFUTATION, SCOPE QUALIFICATIONS, AND ONE DOCUMENTATION REPAIR REQUIRED.**

This audit reviews the mathematical and provenance chain from A80 through the current promoted A114-B2-C2 result. It is deliberately stricter than checking whether stored files say `PASS`.

The central conclusions are:

1. **No promoted downstream theorem was found to depend on the refuted A108 one-sided boundary conjecture.** A108 remains a genuine falsification and must never be relabeled as a pass.
2. **A110 independently repairs/supersedes A108 in the finite `14<=M<=520` gamma-plus contract** by proving the bilateral adjacent-boundary mechanism over the complete finite A94/A102 envelope.
3. **A112 supplies the analytic-tail gamma-plus structural theorem** for `M>=521`, but only inside the frozen gamma-plus architecture and strict compressed phase. It is not a global active-set theorem.
4. **A113 cleanly separates compressed-objective structure from lifted-LP selection.** A94+A113 give all-support compressed one-variation in the declared source window; they do not themselves choose a lifted KKT architecture.
5. **A114-A, A114-B1, A114-B2-A, A114-B2-B, A114-B2-C1 and A114-B2-C2 preserve the compressed/lifted distinction and have explicit logical or analytic certificates.** Finite censuses are used as regression/falsification controls, not as all-tail premises.
6. The current mathematical frontier is genuinely narrower than the older A114 README states: in the strict `b+2`, `Phi<0` interior, C1 and C2 leave only the `QI` versus `QA` branch when `p0^C<0` and `r_E(q0)<0`, plus zero-discriminant boundaries.
7. The human-facing `research_updates/A114/README.md` is stale because it predates B2-B/C1/C2. This is a documentation defect, not a mathematical invalidation. It must be repaired as part of this audit.

This audit does **not** claim a fresh rerun of every expensive A80–A114 computation. It checks committed theorem/result records, prior verification reports, declared contracts, dependency statements, counterexamples, and the current promoted A114 artifacts. Where a historical package was not freshly replayed, that limitation is stated explicitly.

---

## Audit method

Each stage was reviewed along four independent ledgers:

- **mathematical validity:** what is actually proved, refuted, or only observed;
- **scope:** finite grid, finite continuum, rational witness, frozen architecture, analytic tail, or full LP;
- **dependency:** whether later claims use only already-certified premises and whether any circular implication is present;
- **provenance/reproducibility:** exact certificates, independent reconstructions, hashes, negative controls, and known replay limitations.

Special adversarial checks were made for the failure modes already encountered in the programme:

- compressed maximizer falsely identified with a feasible/full-KKT basis;
- finite witness or census promoted to a continuum/all-M theorem;
- a condition proved under primal positivity reused backwards to prove primal positivity;
- a refuted historical conjecture silently retained as a downstream premise;
- zero/degenerate boundaries silently absorbed into strict theorems;
- exploratory or numerically fitted thresholds used as theorem premises;
- stale human documentation disagreeing with the current promoted mathematical state.

---

## A80–A82: local compression, exact reduction, and the first crucial warning

### A80 — certified finite local atlas

**Status:** `CERTIFIED_FINITE_LOCAL_ATLAS`.

A80 works on `M=10..80`, the source interval `[129/1000,133/1000]`, and the A78-selected contact at the reference probe. It certifies 71 selected contacts, 142 exact six-term boundary polynomials, 20 exact compression windows, and 1,888 interval KKT conditions.

**Scope boundary retained:** the six-term law is certified for the selected finite family; no all-M coefficient theorem is claimed.

### A81 — certified finite algebraic reduction

**Status:** `CERTIFIED_FINITE_ALGEBRAIC_REDUCTION`.

A81 derives the two-variable boundary system, verifies positive `T` and `Delta` on all 1,438 admissible finite contacts, reconstructs all 142 selected A80 boundaries, and recovers the endpoint root classification.

**Important caveat retained:** independently primitive-normalizing lower and upper polynomials can divide by different contents, so the raw exact gap identity must not be applied after separate primitive normalization.

### A82 — certified locator with primal-feasibility exceptions

**Status:** `CERTIFIED_FINITE_LOCATOR_WITH_FEASIBILITY_EXCEPTIONS`.

A82 proves exact adjacent-objective identities and strict compressed-objective unimodality at the declared probe for all 71 supports. It also finds **eight compressed-maximizer primal-feasibility exceptions**, with 15 negative basic variables in total.

This is a foundational audit constraint:

> an algebraic compressed maximizer is not automatically a feasible compressed LP basis, much less a full lifted KKT optimum.

All downstream lifted claims must therefore retain complete KKT validation or an independently proved full-KKT closure theorem.

**Verdict for A80–A82:** internally consistent; no illicit compressed-to-lifted promotion detected.

---

## A83–A94: from local factorization to finite-support continuum compressed structure

### A83

**Status:** `CERTIFIED_LOCAL_CONTINUUM_FACTOR_ATLAS_WITH_NEGATIVE_RESULT`.

The seven-term factorization and local sign atlas are exact. Global discrete concavity is explicitly **rejected**, and A82's eight feasibility exceptions remain in force.

### A84

**Status:** `CERTIFIED_REDUCTION_PLUS_FINITE_STRESS`.

The ten-term k-space reduction is structural; finite stress tests support one-variation, while the coefficient-only variation-diminishing shortcut is recorded as insufficient.

### A85

**Status:** `CERTIFIED_DOMINANT_BALANCE_WITH_COUNTEREXAMPLE`.

Parity-resolved dominant balance is certified in its declared regime. The exact `M=12` counterexample blocks a universal small-support extrapolation.

### A86

**Status:** `CERTIFIED_FINITE_THREE_CONTACT_LOCALIZER`.

The three-contact localizer is finite and remains limited to its declared range (`M<=300`).

### A87

**Status:** `CERTIFIED_CLASSIFIER_WITH_REJECTED_GLOBAL_MONOTONICITY`.

The secant-residual classifier succeeds in its declared finite family; global factor monotonicity is not promoted.

### A88

**Status:** `CERTIFIED_FINITE_STRESS_AND_ASYMPTOTIC_LEADING_LIMITS`.

Large finite stress and parity-leading limits are evidence/ingredients, not by themselves an all-M continuum theorem.

### A89

**Status:** `CERTIFIED_ANALYTIC_LOCAL_SECANT_TAIL_THEOREM`.

A89 makes the legitimate transition to an analytic tail statement on the full source interval for `M>=521`, with an explicit positive margin. The certified threshold is stated as sufficient, not minimal.

### A90

**Status:** `CERTIFIED_FINITE_GRID_ONE_VARIATION`.

A90 audits every admissible contact for `M=10..520` at nine rational probes and preserves fifteen exact counterexamples to extending A86's three-contact strip beyond its contract. In particular, `M=325,s=129/1000` requires offset `+3`.

### A91

**Status:** `CERTIFIED_FINITE_OFFSET3_CLASSIFIER`.

The offset-three cells are resolved exactly. The earlier parity-corrected locator is not promoted as an exact rounding rule.

### A92

**Status:** `CERTIFIED_CONTINUUM_CELL_ATLAS`.

A92 promotes the decisive-factor analysis from a rational grid to 858 algebraic continuum cells, including windows missed by the earlier probe grid. This is the correct way to repair grid incompleteness.

### A93

**Status:** `CERTIFIED_SELECTED_CELL_GLOBAL_COMPRESSED`.

The selected local windows are promoted to full-sequence compressed-maximizer statements by exact one-variation checks.

### A94

**Status:** `CERTIFIED_FINITE_SUPPORT_CONTINUUM_GLOBAL_COMPRESSED`.

A94 certifies full-sequence one-variation on all 858 finite-support continuum cells, with 653 fixed maximizers and 205 adjacent transitions.

**Critical scope boundary:** A94 explicitly remains a **compressed-objective, non-KKT, nonphysical** theorem. This boundary is respected by A95 onward.

**Verdict for A83–A94:** PASS under declared contracts. Negative results and range failures are preserved rather than overwritten; the grid-to-continuum transition is explicit, not assumed.

---

## A95–A106: discovering and resolving lifted active-set obstructions

### A95

**Status:** `CERTIFIED_RATIONAL_WITNESS_LIFT_OBSTRUCTION`.

Of 1,063 exact A94 phase witnesses, 980 admit the natural strict lift and 83 do not. The first obstruction at `M=125,s=33/250` defeats every previously declared F2/F3 candidate. A95 correctly stops at an obstruction theorem: it does not pretend to know the missing active set and does not claim continuum closure.

### A96

**Status:** `CERTIFIED_POINTWISE_FULL_LP`.

The first A95 obstruction is resolved by unrestricted exact full-LP KKT analysis. This is pointwise, not yet an interval theorem.

### A97

**Status:** `CERTIFIED_ENDPOINT_INTERVAL_PLUS_POINTWISE_RESOLUTION`.

The endpoint-released architecture is promoted to an exact strict-KKT interval where proved; 76 of the 83 A95 obstruction witnesses are resolved and seven q0-entry residual obstructions are retained.

### A98

**Status:** `CERTIFIED_POINTWISE_FULL_LP`.

The first q0/q1 residual is resolved by unrestricted exact KKT.

### A99

**Status:** `CERTIFIED_Q0Q1_CONTINUUM_WITH_RESIDUALS`.

The gamma-inactive q0/q1 basis is continued on exact strict components where proved, while four residual obstructions are preserved.

### A100

**Status:** `CERTIFIED_POINTWISE_GAMMA_MINUS_FULL_LP`.

The first A99 residual is resolved by a gamma-minus-active q0/q1 architecture through complete exact KKT.

### A101

**Status:** `CERTIFIED_GAMMA_ACTIVE_INTERVALS_AND_POINTWISE_OBSTRUCTION_CLOSURE`.

The gamma-active architecture is continued where proved, and the 83 A95 obstruction witnesses are closed pointwise.

### A102

**Status:** `CERTIFIED_COMPLETE_RATIONAL_WITNESS_ATLAS`.

All 1,063 A95 rational witnesses are merged with no missing/duplicate/unresolved key: 980 legacy natural, 76 endpoint-released, 3 q0/q1 gamma-inactive, 4 q0/q1 gamma-active. The archive records 676,847 exact KKT conditions and an independent 183-branch replay with zero mismatch.

**Critical scope boundary retained:** A102 is a **pointwise rational-witness atlas**, not automatically a continuum theorem.

### A103

**Status:** `CERTIFIED_ENDPOINT_RELEASED_CONTINUUM_ATLAS`.

The 76 endpoint-released witness segments are promoted only after exact interval analysis.

### A104

**Status:** `CERTIFIED_Q0Q1_CONTINUUM_ATLAS`.

The seven exceptional q0/q1 source segments receive exact two-sided strict components with competing-root ordering and outside counterexamples.

### A105

**Status:** `CERTIFIED_TWO_BAND_CONTINUUM_ATLAS`.

All 40 legacy two-band source segments are classified as proper two-sided strict subcomponents; no complete-source-segment claim is made.

### A106

**Status:** `CERTIFIED_GAMMA_MINUS_CONTINUUM_ATLAS`.

All 18 legacy gamma-minus segments are classified exactly: one complete segment and 17 proper one-sided subcomponents. The lower adjacent mass `p_(j-1)` is identified as the common finite-atlas exit mechanism for the partial records.

**Verdict for A95–A106:** PASS under declared contracts. The sequence correctly distinguishes discovery at rational witnesses from later continuum promotion; no witness-to-continuum shortcut was detected.

---

## A107–A109: a real falsification, not a blemish to hide

### A107

**Status:** `CERTIFIED_LOCAL_GAMMA_PLUS_CONTINUUM_EXPLORATION`.

A107 extends exact gamma-plus continuum work and motivates a boundary pattern. Its empirical/structural patterns are not treated here as universal theorems.

### A108

**Status:** `REFUTED_SUPERSEDED`.

The A108 universal one-sided boundary claim is **false**. Canonical rank 105 gives an exact right `basic_p_22` boundary.

This is not a failed audit of the entire programme. It is a successful falsification of a conjecture. The correct scientific handling is exactly what the repository does: retain the counterexample, retain the historical artifacts, and replace the claim rather than silently modifying it.

A108 must never be summarized as `PASS`.

### A109

**Status:** `SUPPORTED_PROSPECTIVE_FINITE_EVIDENCE; LATER SUPERSEDED STRUCTURALLY BY A110 IN THE FINITE DOMAIN`.

A109 replaces the one-sided conjecture with a bilateral adjacent-boundary classifier. In the stored mathematically resolved prospective sequence through rank 414, no class/boundary mismatch is recorded; however the package explicitly does **not** claim an all-922 theorem. H19 (ranks 415–430) was frozen but not executed in the supplied historical package.

The packaging validation did not freshly rerun the complete rank-1..414 historical computation; it verified integrity/accounting artifacts and tests.

### Downstream-contamination check

Repository reference searches for `A108` and the phrase `one-sided boundary` locate the falsified claim in the A107–A109 historical package, documentation, and manuscript material. No A110–A114 theorem dependency on the one-sided A108 rule was found.

A110 references A109 because it proves the **correct bilateral rule** independently on the complete finite A94/A102 envelope.

**Verdict for A107–A109:** the historical record is scientifically healthy provided A108 remains explicitly refuted. No downstream contamination by the false A108 premise was detected.

---

## A110–A112: finite structural repair and analytic-tail gamma-plus theorem

### A110

**Status:** `CERTIFIED_FINITE_STRUCTURAL_THEOREM`.

On the frozen finite `14<=M<=520` source/gamma-plus contract, A110 closes the bilateral adjacent-boundary mechanism independently of the prospective A109 sequence.

The theorem audits all 1,870 A94-envelope `(M,j)` pairs, including exact reduced-cost threshold ordering, active-dual protection, conditional `RQ(2)` positivity, and opposite monotonicity of `p_j` and `p_(j+1)`.

Thus the strict KKT component is exactly

`{s: p_j(s)>0 and p_(j+1)(s)>0}`

inside the frozen phase, with left boundary `p_(j+1)=0` and right boundary `p_j=0`.

This is the mathematical finite-domain repair that supersedes A108's false unilateral rule.

### A111/A111B

**Status:** `FINITE_RECONNAISSANCE_ONLY`.

Preregistered exact tail checks, including selected stress cases through `M=5000`, found no counterexample to the intended tail structure. They remain finite reconnaissance and are not used as the analytic theorem.

### A112

**Status:** `CERTIFIED_ANALYTIC_TAIL_STRUCTURAL_THEOREM`.

For `M>=521` inside the frozen gamma-plus family and a strict compressed phase, A112 proves full strict KKT exactly where the adjacent masses `p_j,p_(j+1)` are positive; the common-positive set is one interval with only those adjacent-mass internal boundaries.

The final A112 package explicitly records and repairs several false or incomplete intermediate claims:

- `j in {b+1,b+2} => RQ(2)>0` is false; an exact `M=600,s=133/1000` counterexample is preserved;
- two provisional tail corrections were discarded after gamma-contact terms were zeroed too early;
- an implicit regularity gap in the first monotonicity argument was repaired by proving `A(s)<0<B(s)` before using `t'(s)>0`;
- continuation-only “cannot be the first zero” arguments were replaced with pointwise implications.

The machine-readable logical composition audit marks all authoritative B–G certificate dependencies `PASS` and states the claim boundary explicitly.

**Critical boundary:** A112 is a **local structural all-tail theorem for the frozen gamma-plus family**, not a global theorem selecting gamma-plus among every lifted architecture.

**Verdict for A110–A112:** PASS under declared contracts. A110 is the correct finite structural replacement for A108; A112 is its analytic-tail analogue within the frozen gamma-plus architecture.

---

## A113: all-support compressed one-variation, still not lifted selection

**Status:** `CERTIFIED_ANALYTIC_TAIL_GLOBAL_COMPRESSED_THEOREM`.

A113 proves for `M>=521` on the full source window:

- `E_(M,k)>0` for `k<=b`;
- `E_(M,k)<0` for `k>=b+3`;
- `E_(b+1)-2E_(b+2)>0`.

Therefore the complete compressed adjacent-factor sequence has exactly one positive-to-negative variation and the compressed maximizer lies in `{b+1,b+2,b+3}`.

Combined with A94, this gives the all-support-size (`M>=14`) compressed one-variation theorem in the declared source window.

A113 explicitly preserves two falsifications:

- the `b+3` phase does not disappear in the tail (`M=561,s=129/1000`);
- `E_(b+1)-E_(b+2)>0` is not uniformly true in the deep tail.

The successful central quantity is `E_(b+1)-2E_(b+2)>0`.

**Critical boundary:** A113 concerns the compressed objective. It does not select a lifted full-LP active set.

**Verdict:** PASS. No compressed/lifted conflation detected.

---

## A114: lifted active-set selection

### A114-A — strict `b+3`

**Status:** `CERTIFIED_LIFTED_BPLUS3_BRANCH`.

The logical composition audit passes. The proof depends on A113 strict `b+3`, exact endpoint-system inequalities, simplex exchange, and ECT zero-count closure. It uses finite exact solves only as independent regression evidence. The stronger statement `j=b+3` without strict compressed maximality is explicitly rejected by a negative control.

### A114-B1 — strict `b+1`

**Status:** `CERTIFIED_LIFTED_BPLUS1_PIVOT_THEOREM`.

The principal historical circularity risk is explicitly repaired: `D_G>0` is proved from `D_G=det(C)A(s)`, A110's determinant sign, and A112-G branch regularity **before** adjacent primal positivity is assumed. The pivot rule is therefore not obtained by reversing A112-B.

The `Phi=0` degeneracy is retained as non-strict; strict uniqueness is not claimed there.

### A114-B2-W1

**Status:** `CERTIFIED_POINTWISE_NEGATIVE_PIVOT_WITNESS`.

The exact point `M=521,s=129/1000` proves a q0/q1 gamma-minus optimum and shows that non-gamma-plus architectures survive in the analytic tail. An exploratory run with the wrong odd-parity epsilon scale is explicitly marked invalid; the theorem relies on corrected exact certificates, not that discovery run.

### A114-B2-A — strict `b+2`, `Phi>0`

**Status:** `CERTIFIED_POSITIVE_PIVOT_BPLUS2_BRANCH`.

The logical audit confirms that adjacent positivity is derived from exact Cramer identities plus the independent determinant orientation, and that A112-D uses the compressed sign at the correct contact. The A102 census is regression evidence only.

### A114-B2-B — `Phi<0` exclusion lemma

**Status:** `CERTIFIED_NEGATIVE_PIVOT_PURE_GAMMA_MINUS_EXCLUSION`.

The analytic lemma proves

`Phi<0 => 3j-h>=13`

and then excludes the pure central-Q gamma-minus basis by exact even/odd Cramer inequalities. Finite scans and small-M examples are independent controls, not premises. Small-M negative controls demonstrate why the tail gate is essential.

### A114-B2-C1 — endpoint-released conditional branch

**Status:** `CERTIFIED_ENDPOINT_RELEASED_CONDITIONAL_BRANCH`.

Under strict `b+2`, `Phi<0`,

`p0^C<0 and r_E(q0)>0 => E`,

where `E` is the endpoint-released architecture. The published logical audit separates the B2-specific source box, exact exchange identity, ECT closures and full KKT conclusion. Finite controls are explicitly regression only.

### A114-B2-C2 — compressed conditional branch

**Status:** `CERTIFIED_COMPRESSED_CONDITIONAL_BRANCH`.

Under strict `b+2`, `Phi<0`,

`p0^C>0 => C`,

where `C` is the two-band compressed architecture. The promoted analytic certificate passes 49/49 exact rational gates and the logical audit passes 15/15 checks. The gamma-plus inactive slack is protected by an exact bordered-basis pivot identity, not a fitted census rule.

### Current unpromoted frontier

**Status:** `OPEN_ANALYTIC_FRONTIER`.

After C1 and C2, the only open strict interior branch on the negative-pivot `b+2` tail is

`p0^C<0 and r_E(q0)<0`,

where q0/q1 gamma-inactive (`QI`) and q0/q1 gamma-minus-active (`QA`) compete.

The QI/QA identities currently under investigation are **not included in this audit as proved theorems** because they have not yet been promoted through an analytic certificate and logical audit.

Zero-discriminant boundaries remain separate. In particular, no generic strict claim is made on `p0^C=0` or `r_E(q0)=0`; the `b+2` `Phi=0` architecture classification also remains outside the current strict B2 theorem set.

---

## Cross-generation dependency audit

The promoted dependency spine is consistent:

1. A80–A83 establish exact local/reduced identities while preserving feasibility exceptions.
2. A84–A94 build the compressed-objective factor theory and finite continuum atlas without claiming lifted KKT.
3. A95 discovers lift obstructions; A96–A106 identify and promote the missing active-set families without assuming the natural lift.
4. A108's false one-sided conjecture is refuted and retained historically.
5. A110 independently proves the corrected bilateral rule in the complete finite gamma-plus envelope; no A108 premise is needed.
6. A112 proves the corresponding analytic-tail structural theorem inside the frozen gamma-plus family, with its own composition audit and corrected intermediate claims.
7. A113 proves global compressed one-variation in the tail and explicitly does not perform lifted selection.
8. A114 uses A112/A113 identities and signs to prove full-LP branch theorems, with separate determinant-orientation repairs and exact KKT closure.

### Circularity result

**No promoted circular dependency was detected in the current A110–A114 chain.**

The most serious potential circularity — using `D_G>0` proved under adjacent positivity to infer adjacent positivity — is explicitly repaired in A114-B1 before B2-A reuses the orientation.

### A108 contamination result

**No downstream dependency on the refuted A108 one-sided rule was detected.**

A108 remains a historical falsification; A110 supplies a new proof of the corrected bilateral rule in the finite domain.

---

## Reproducibility and provenance audit

### A80–A106 baseline

The previously committed packaging validation reports that the untouched A39–A106 baseline verifier returned:

- 68 audit results;
- 1,013 gates;
- 110 figures;
- zero failures;
- overall `PASS`.

This longitudinal review did not freshly rerun every expensive historical script. Therefore the correct statement is **committed baseline verified by the stored verifier/report**, not “freshly replayed A80–A106 in this audit session.”

### A107–A109

The update verifier passed its integrity/accounting checks and tests, but the packaging report explicitly says the full historical rank-1..414 sequence was not freshly rerun. H19 was frozen and not executed.

### A110–A114

The promoted tail results increasingly use independent exact reconstructions, logical-composition audits, explicit negative controls, and hashes/manifests. A114 C1/C2 additionally separate finite census evidence from all-tail analytic premises.

**Provenance verdict:** adequate for the current theorem claims, with the historical replay limitations above retained explicitly.

---

## Formal findings

### F1 — historical refutation

**Severity:** expected scientific falsification, not current-chain failure.

A108's universal one-sided boundary rule is false at canonical rank 105. Status must remain `REFUTED_SUPERSEDED`.

### F2 — no A108 downstream contamination detected

**Severity:** none.

Searches and current theorem dependency records show no use of the refuted A108 one-sided premise in A110–A114.

### F3 — compressed/lifted distinction preserved

**Severity:** none.

A82 exposes the danger; A94/A113 retain compressed-only scope; A95 onward performs lifted/full-KKT resolution explicitly.

### F4 — finite evidence is generally not promoted as analytic proof

**Severity:** none for promoted current theorems.

A89, A110, A112, A113 and A114 explicitly distinguish finite controls from analytic/continuum proofs.

### F5 — A114 README documentation drift

**Severity:** documentation defect; repair required.

The current A114 README predates B2-B/C1/C2 and still states that the entire `Phi<=0` B2 region remains open. The mathematical artifacts on `main` prove more than that. The README must be updated without deleting the historical path.

### F6 — current QI/QA work is not yet a theorem

**Severity:** open research frontier.

The derived QI/QA pivot identities are promising but remain unpromoted and are excluded from the proved ledger until an exact analytic certificate, independent controls and a logical audit are committed.

---

## Final scientific ledger

The longitudinal state after this audit is:

- **A80–A106:** certified under their declared finite/grid/continuum/witness contracts; no stored PASS is interpreted beyond its scope.
- **A107:** valid local/finite exploration.
- **A108:** **REFUTED** and superseded.
- **A109:** strong prospective evidence for the bilateral rule, not an all-record theorem; later structurally superseded by A110 in the finite domain.
- **A110:** proved finite bilateral structural theorem.
- **A111/A111B:** finite reconnaissance only.
- **A112:** proved conditional analytic-tail gamma-plus structural theorem.
- **A113:** proved analytic-tail global compressed one-variation theorem; not lifted selection.
- **A114-A:** proved strict `b+3` lift.
- **A114-B1:** proved/closed strict `b+1` lift including non-strict pivot classification.
- **A114-B2-A:** proved strict `b+2`, `Phi>0` lift.
- **A114-B2-B:** proved `Phi<0` pure-gamma-minus exclusion.
- **A114-B2-C1:** proved `p0^C<0, r_E(q0)>0 => E`.
- **A114-B2-C2:** proved `p0^C>0 => C`.
- **A114-B2 QI/QA edge:** open.

Therefore the current programme is **not invalidated by A108**. The correct global audit verdict is:

> **The promoted mathematical chain from A80 through A114-B2-C2 is internally coherent under its declared contracts, with A108 explicitly refuted/superseded, no detected downstream dependence on that false conjecture, and one current documentation drift in the A114 README that must be repaired.**

No physical interpretation is implied by this audit.