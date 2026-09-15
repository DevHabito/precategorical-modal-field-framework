# Consolidation 1.0 — independent verification protocol

The project must distinguish between a derivation and a genuinely independent attempt to break that derivation. Re-reading the same proof with the same model and the same intermediate notes is useful editing, but it is not strong independence.

## Verification ladder

### V0 — source proof

A human-readable derivation with explicit hypotheses and no hidden appeal to project interpretation.

### V1 — executable exact check

Independent executable verification where appropriate:

- exact integer/rational arithmetic;
- exhaustive finite enumeration;
- symbolic identity checking;
- rigorous interval arithmetic.

This checks implementation-level obligations but does not replace a proof of a universal theorem unless the finite/interval reduction itself is proved.

### V2 — blind rederivation

A second solver/model receives only:

- definitions;
- theorem statement;
- allowed background lemmas.

It does **not** receive the original derivation, red-team note, expected intermediate formulas, or final proof outline.

The rederivation is compared only after completion. Shared final formulas are evidence of convergence; disagreement triggers investigation rather than majority voting.

### V3 — proof-kernel verification

Lean 4/mathlib checks the formal statement from formal hypotheses with no `sorry` in files marked verified.

This is the strongest internal logical check, but it still does not establish novelty, empirical relevance, or truth of the hypotheses about nature.

### V4 — external specialist exposure

Submit isolated claims, not the full programme, to an appropriate venue:

- combinatorial sequences/statistics: OEIS where applicable;
- mathematical manuscript/preprint: arXiv after suitable preparation/endorsement requirements are met;
- focused prior-art or theorem-identification question: MathOverflow or specialist correspondence;
- ordinary journal peer review when a manuscript is mature enough.

External disagreement is recorded and answered at claim level.

## Blind adversarial prompt rule

When AI is used for V2, the prompt should explicitly request falsification:

1. derive independently from definitions;
2. search for counterexamples before proving;
3. identify every imported assumption;
4. reject the statement if one admissible counterexample exists;
5. separate proof from finite evidence;
6. do not infer physical meaning.

The verifier should not be told that the result previously passed another audit.

## Common-mode failure controls

Whenever possible, vary at least two of the following:

- model/provider;
- proof route;
- implementation language;
- arithmetic representation;
- theorem formulation;
- finite test generator;
- symbolic versus numerical method.

Two scripts that import the same helper functions are not independent implementations.

## Promotion labels

A consolidated claim should carry one of these verification labels:

- `V0` — proof only;
- `V0+V1` — proof plus exact executable hardening;
- `V0+V1+V2` — plus blind independent rederivation;
- `FORMAL` — V3 kernel-checked;
- `EXTERNALLY_CHECKED` — meaningful V4 specialist feedback has been incorporated.

These labels describe verification depth, not novelty.

## Failure policy

If an independent check breaks a claim:

- freeze promotion immediately;
- preserve the failed version and counterexample;
- determine whether the theorem can be repaired by an already implicit assumption;
- if a new assumption is required, treat the repaired theorem as a different theorem;
- never silently narrow a parameter window merely to save a preferred narrative.
